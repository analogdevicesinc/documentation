Asymmetric AXI Stream FIFO Core
===============================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/util_axis_fifo_asym/index.html\


The util_axis_fifo_asym IP core is a simple FIFO (First Input First Output) with AXI streaming interfaces, supporting synchronous and asynchronous operation modes with an asymmetric data width on its salve and master interface. It can be used to mitigate data width differences or transfer an AXI stream to a different clock domain.

Features
--------

-  Supports Intel/Altera and Xilinx devices
-  Configurable data width and depth
-  Asymmetric data width
-  Support asynchronous (double clocked) mode
-  Supports TLAST to indicate packet boundary
-  Supports TKEEP to indicate valid data bytes
-  Supports FULL/EMPTY and ALMOST_FULL/ALMOST_EMPTY status signals

Functional Description
----------------------

The FIFO is based on the :doc:`util_axis_fifo </wiki-migration/resources/fpga/docs/util_axis_fifo>`, using it as its atomic building block.

The configuration of the atomic util_axis_fifo blocks are calculated as follows:

::

   // define which interface has a wider bus
   localparam RATIO_TYPE = (S_DATA_WIDTH >= M_DATA_WIDTH) ? 1 : 0;
   // bus width ratio
   localparam RATIO = (RATIO_TYPE) ? S_DATA_WIDTH/M_DATA_WIDTH : M_DATA_WIDTH/S_DATA_WIDTH;
   // atomic parameters - NOTE: depth is defined by master or slave and limitation attributes
   localparam A_WIDTH = (RATIO_TYPE) ? M_DATA_WIDTH : S_DATA_WIDTH;
   localparam A_ADDRESS = (ADDRESS_WIDTH_PERSPECTIVE) ?
       ((FIFO_LIMITED) ? ((RATIO_TYPE) ? (ADDRESS_WIDTH-$clog2(RATIO)) : ADDRESS_WIDTH) : ADDRESS_WIDTH) :
       ((FIFO_LIMITED) ? ((RATIO_TYPE) ? ADDRESS_WIDTH : (ADDRESS_WIDTH-$clog2(RATIO))) : ADDRESS_WIDTH);
   localparam A_ALMOST_FULL_THRESHOLD = (RATIO_TYPE) ? ALMOST_FULL_THRESHOLD : (ALMOST_FULL_THRESHOLD/RATIO);
   localparam A_ALMOST_EMPTY_THRESHOLD = (RATIO_TYPE) ? (ALMOST_EMPTY_THRESHOLD/RATIO) : ALMOST_EMPTY_THRESHOLD;

Status signal delays
~~~~~~~~~~~~~~~~~~~~

.. important::

   In case of asynchronous mode, because of the delays introduced by the clock domain crossing logic, the ROOM and LEVEL indicators can not reflect the actual state of the FIFO in real time. Source and destination logic should take this into account when controlling the data stream into and from the FIFO. Carefully adjusting the ALMOST_EMPTY/ALMOST_FULL indicators can provide a save operating margin.


The FIFO has three different status indicator ports on both side, which provides information about the state of the FIFO for both the source and destination logic:

-  FULL or EMPTY - If these outputs are asserted the FIFO is full or empty. In case of a full FIFO all the write operations are suspended. In case of an empty FIFO all the read operations are suspended.
-  ALMOST_EMPTY/ALMOST_FULL - It can be used to foresee a potential FULL or EMPTY state, asserting before the EMPTY/FULL before a predefined number of word. The offset between ALMOST_EMPTY and EMPTY, and between ALMOST_FULL and FULL can be set by using the parameters ALMOST_EMPTY_THRESHOLD and ALMOST_FULL_THRESHOLD. The offset values are automatically adjusted according to M_DATA_WIDTH and S_DATA_WIDTH ratio.
-  S_AXIS_ROOM - Indicate how many word can be written in the FIFO at the current moment, until the FIFO become FULL.
-  M_AXIS_LEVEL - Indicate how many word can be read from the FIFO at the current moment, until the FIFO become EMPTY.

FIFO Depth Calculation
~~~~~~~~~~~~~~~~~~~~~~

The FIFO Depth is calculated based on parameters M_DATA_WIDTH, S_DATA_WIDTH, ADDRESS_WIDTH, FIFO_LIMITED and ADDRESS_WIDTH_PERSPECTIVE:

-  ADDRESS_WIDTH_PERSPECTIVE is 1 and FIFO_LIMITED is 1 - This means that the address specified is from the perspective of the Master interface. Since the limit is enabled the FIFO size will be reduced if the S_DATA_WIDTH is > M_DATA_WIDTH, leading to a smaller FIFO implementation.
-  ADDRESS_WIDTH_PERSPECTIVE is 1 and FIFO_LIMITED is 0 - This means that the address specified is from the perspective of the Master interface. Since the limit is disable the FIFO size will remain the same if the S_DATA_WIDTH is > M_DATA_WIDTH, leading to a bigger FIFO implementation.
-  ADDRESS_WIDTH_PERSPECTIVE is 0 and FIFO_LIMITED is 1 - This means that the address specified is from the perspective of the Slave interface. Since the limit is enabled the FIFO size will be reduced if the S_DATA_WIDTH is < M_DATA_WIDTH, leading to a smaller FIFO implementation.
-  ADDRESS_WIDTH_PERSPECTIVE is 0 and FIFO_LIMITED is 0 - This means that the address specified is from the perspective of the Slave interface. Since the limit is disable the FIFO size will remain the same if the S_DATA_WIDTH is < M_DATA_WIDTH, leading to a bigger FIFO implementation.

Parameters
----------

+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| Name                          | Description                                                                                 | Default Value |
+===============================+=============================================================================================+===============+
| ``S_DATA_WIDTH``              | Data width of Slave AXI streaming interface                                                 | 64            |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| ``M_DATA_WIDTH``              | Data width of Master AXI streaming interface                                                | 128           |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| ``ADDRESS_WIDTH``             | Width of the address, defines the depth of the FIFO                                         | 5             |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| ``ASYNC_CLK``                 | Clocking mode, if set the FIFO operates on asynchronous mode                                | 1             |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| ``M_AXIS_REGISTERED``         | Add and additional register stage to the AXI stream master interface                        | 1             |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| ``ALMOST_EMPTY_THRESHOLD``    | Defines the offset (in data beats) between the almost empty and empty assertion             | 4             |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| ``ALMOST_FULL_THRESHOLD``     | Defines the offset (in data beats) between the almost full and full assertion               | 4             |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| ``TLAST_EN``                  | Enables or disable registering of TLAST signal                                              | 0             |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| ``TKEEP_EN``                  | Enables or disable registering of TKEEP signal                                              | 0             |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| ``FIFO_LIMITED``              | Enable the address limit that is set to the FIFO with respect to the specified address size | 0             |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+
| ``ADDRESS_WIDTH_PERSPECTIVE`` | Sets address size from the perspective of Master (1) or Slave (0)                           | 0             |
+-------------------------------+---------------------------------------------------------------------------------------------+---------------+

Interface
---------

+---------------------------------------+---------------------------+---------------------------------------------------------+
| Interface/Pin                         | Type                      | Description                                             |
+=======================================+===========================+=========================================================+
| \*\* Slave AXI Stream interface \*\*  |                           |                                                         |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' s_axis_aclk ''                     | input                     | Slave AXI stream clock signal                           |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' s_axis_aresetn ''                  | input                     | Slave AXI stream reset signal (active low)              |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' s_axis_ready ''                    | output                    | Slave AXI stream ready                                  |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' s_axis_valid ''                    | input                     | Slave AXI stream valid                                  |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' s_axis_data ''                     | input[DATA_WIDTH-1:0]     | Slave AXI stream ready                                  |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' s_axis_tlast ''                    | input                     | Slave AXI stream TLAST signal, for packet boundary      |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' s_axis_room ''                     | output[ADDRESS_WIDTH-1:0] | Indicates how much space (in data beats) is in the FIFO |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' s_axis_almost_empty ''             | output                    | If set the FIFO is almost empty                         |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' s_axis_empty ''                    | output                    | If set the FIFO is empty                                |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| \*\* Master AXI Stream interface \*\* |                           |                                                         |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' m_axis_aclk ''                     | input                     | Master AXI stream clock signal                          |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' m_axis_aresetn ''                  | input                     | Master AXI stream reset signal (active low)             |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' m_axis_ready ''                    | input                     | Master AXI stream ready                                 |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' m_axis_valid ''                    | output                    | Master AXI stream valid                                 |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' m_axis_data ''                     | output[DATA_WIDTH-1:0]    | Master AXI stream ready                                 |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' m_axis_tlast ''                    | output                    | Master AXI stream TLAST signal, for packet boundary     |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' m_axis_level ''                    | output[ADDRESS_WIDTH-1:0] | Indicates how much data is in the FIFO                  |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' m_axis_almost_full ''              | output                    | If set the FIFO is almost full                          |
+---------------------------------------+---------------------------+---------------------------------------------------------+
| '' m_axis_full ''                     | output                    | If set the FIFO is full                                 |
+---------------------------------------+---------------------------+---------------------------------------------------------+

Register Map
------------

This core does not have a register map.

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
