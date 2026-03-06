AXI Stream FIFO Core
====================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/util_axis_fifo/index.html\


The util_axis_fifo IP core is a simple FIFO (First Input First Output) with AXI streaming interfaces, supporting synchronous and asynchronous operation modes. It can be used to mitigate data rate differences or transfer an AXI stream to a different clock domain.

Features
--------

-  Supports Intel/Altera and Xilinx devices
-  Configurable data width and depth
-  Support asynchronous (double clocked) mode
-  Supports TLAST to indicate packet boundary
-  Supports FULL/EMPTY and ALMOST_FULL/ALMOST_EMPTY status signals
-  Support zero-deep implementation

Functional Description
----------------------

The util_axis_fifo is a generic First Input First Output module, that can be used to control clock and data rate differences or to do data buffering on a AXI4 stream based data path. FIFO's write interface is an AXI4 slave streaming interface, and the FIFO's read interface is an AXI4 master streaming interface. The depth of the FIFO is defined by the equation, which is a function of the ADDRESS_WIDTH and DATA_WIDTH parameters:

**FIFO depth in bytes = DATA_WIDTH/8 \* 2 ^ ADDRESS_WIDTH**

The FIFO has three different status indicator ports on both side, which provides information about the state of the FIFO for both the source and destination logic:

-  FULL or EMPTY - If these outputs are asserted the FIFO is full or empty. In case of a full FIFO all the write operations are suspended. In case of an empty FIFO all the read operations are suspended.
-  ALMOST_EMPTY/ALMOST_FULL - It can be used to foresee a potential FULL or EMPTY state, asserting before the EMPTY/FULL before a predefined number of word. The offset between ALMOST_EMPTY and EMPTY, and between ALMOST_FULL and FULL can be set by using the parameters ALMOST_EMPTY_THRESHOLD and ALMOST_FULL_THRESHOLD.
-  S_AXIS_ROOM - Indicate how many word can be written in the FIFO at the current moment, until the FIFO become FULL.
-  M_AXIS_LEVEL - Indicate how many word can be read from the FIFO at the current moment, until the FIFO become EMPTY.

.. important::

   In case of asynchronous mode, because of the delays introduced by the clock domain crossing logic, the ROOM and LEVEL indicators can not reflect the actual state of the FIFO in real time. Source and destination logic should take this into account when controlling the data stream into and from the FIFO. Carefully adjusting the ALMOST_EMPTY/ALMOST_FULL indicators can provide a save operating margin.


Parameters
----------

+----------------------------+---------------------------------------------------------------------------------+---------------+
| Name                       | Description                                                                     | Default Value |
+============================+=================================================================================+===============+
| ``DATA_WIDTH``             | Data width of AXI streaming interface                                           | 64            |
+----------------------------+---------------------------------------------------------------------------------+---------------+
| ``ADDRESS_WIDTH``          | Width of the address, defines the depth of the FIFO                             | 5             |
+----------------------------+---------------------------------------------------------------------------------+---------------+
| ``ASYNC_CLK``              | Clocking mode, if set the FIFO operates on asynchronous mode                    | 1             |
+----------------------------+---------------------------------------------------------------------------------+---------------+
| ``M_AXIS_REGISTERED``      | Add and additional register stage to the AXI stream master interface            | 1             |
+----------------------------+---------------------------------------------------------------------------------+---------------+
| ``ALMOST_EMPTY_THRESHOLD`` | Defines the offset (in data beats) between the almost empty and empty assertion | 16            |
+----------------------------+---------------------------------------------------------------------------------+---------------+
| ``ALMOST_FULL_THRESHOLD``  | Defines the offset (in data beats) between the almost full and full assertion   | 16            |
+----------------------------+---------------------------------------------------------------------------------+---------------+

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
