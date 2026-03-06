Source synchronous interface design with FPGAs
==============================================

This page presents a possible design solution for a source synchronous interface. This solution can be used to interface any converters, which has a source synchronous data interface. The main focus is on a generic interface architecture, all the information regarding the FPGA vendors specific hardware modules and IP's can be found at the FPGA manufacturer site. Although there are useful links on the Reference section, which point to those sites and documentations.

What is a source synchronous interface?
---------------------------------------

Source synchronous interface is a common interface type on chip-to-chip communication. The base idea behind the interface, is to send a copy of the clock along with the data, and in this way simplify the timing model of the interface. This interface type is a successor of the system synchronous interface, where both the source and destination IC receive the clock from a common source (clock generator IC).

The following block diagram illustrate the architecture of the physical interface.

Architecture
------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/source_sync_if_1.svg
   :alt: Source synchronous interface implementation
   :align: center

In general a source synchronous interface consist a clock reception module, which contains all the necessary IO resource instances to receive the digital interface clock from the device. In function of the device type, it may contain a data reception and/or a data transmission module. The interface for the FPGA logic is a simplified FIFO interface. More information about the interface can be found `here <https://wiki.analog.com/resources/fpga/docs/adi_fifo_if>`__.

The CORE_CLK can have the same frequency as the PHY_CLK or an integer division of PHY_CLK frequency. The generic rule of thumb is to try to keep the CORE_CLK's frequency bellow 200 Mhz. Because in general the CORE_CLK is used throughout the data path, using a too high CORE_CLK can significantly reduce the timing margins, making almost impossible to close timing.

If the frequency of the PHY_CLK is too high, SERDES macros are used to convert the interface clock and data rate into a more manageable level.

Implementation with Xilinx FPGAs
--------------------------------

Files
~~~~~

+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Name                                                                                      | Description                                                                                       |
+===========================================================================================+===================================================================================================+
| `ad_data_clk.v <https://github.com/hdl?master/library/xilinx/common/ad_data_clk.v>`__     | Clock reception module, contains an input clock buffer and a global clock buffer for distribution |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| `ad_data_in.v <https://github.com/hdl?master/library/xilinx/common/ad_data_in.v>`__       | Data reception module, general architecture looks like following: **ibuf -> idelay -> iddr**      |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| `ad_data_out.v <https://github.com/hdl?master/library/xilinx/common/ad_data_out.v>`__     | Data transmission module, general architecture looks like following: **oddr -> odelay -> obuf**   |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| `ad_serdes_clk.v <https://github.com/hdl?master/library/xilinx/common/ad_serdes_clk.v>`__ | Clock reception module for SERDES architecture, a path looks like following: **ibuf -> mmcm**     |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| `ad_serdes_in.v <https://github.com/hdl?master/library/xilinx/common/ad_serdes_in.v>`__   | Data reception module, general architecture looks like following: **ibuf -> idelay -> iserdes**   |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| `ad_serdes_out.v <https://github.com/hdl?master/library/xilinx/common/ad_serdes_out.v>`__ | Data transmission module, general architecture looks like following: **oserdes -> obuf**          |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

References
~~~~~~~~~~

-  `Virtex 6 Clock Resources <https://www.xilinx.com/support/documentation/user_guides/ug362.pdf>`__
-  `Virtex 6 SelectIO Resources <https://www.xilinx.com/support/documentation/user_guides/ug361.pdf>`__
-  `7 Series Clock Resources <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`__
-  `7 Series SelectIO Resources <https://www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`__
-  `Ultrascale Clock Resources <https://www.xilinx.com/support/documentation/user_guides/ug572-ultrascale-clocking.pdf>`__
-  `Ultrascale SelectIO Resources <https://www.xilinx.com/support/documentation/user_guides/ug571-ultrascale-selectio.pdf>`__

Implementation with Intel/Altera FPGAs
--------------------------------------
