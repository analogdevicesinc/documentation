HDL Architecture
================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated. Please check out our latest guide at https://analogdevicesinc.github.io/hdl/user_guide/architecture.html\


Every HDL design of a reference project can be divided into two subsystems:

-  **Base design** --- description of what the **carrier** contains:

   -  an embedded processor - soft or hard
   -  all the peripheral IPs (that are necessary to run a Linux distribution on the system)
   -  these designs are specific to each carrier, making them **carrier dependent**
   -  it describes part of the *system_wrapper* module
   -  located in :git-hdl:`/hdl/projects/common/\* <projects/common>`; one for each carrier

-  **Board design** --- description of what the **board** attached to the carrier contains:

   -  all the necessary IPs needed to support the board
   -  these designs are common to all carriers, making them **carrier independent**
   -  it describes part of the *system_wrapper* module
   -  located in */hdl/projects/$project_name/common/\*bd.tcl*

How they're instantiated:
-------------------------

In case of a project, inside the *system_bd.tcl* file, we have to source the *base design first*, then the *board design*.

Example
-------

Take FMCOMMS2 with Zedboard, the *system_bd.tcl* will look like the following:

<block 60%>

::

   source $ad_hdl_dir/projects/common/zed/zed_system_bd.tcl
   source ../common/fmcomms2_bd.tcl

</block>

Typical project diagram
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/base_platform_12.svg
   :alt: HDL overall system
   :align: center

--------------

Base Design
~~~~~~~~~~~

The base design contains all the I/O peripheral and memory interfaces and processing components, which are necessary for a fully functional Linux system. The majority of these components are Intel and Xilinx IP cores.

Typically, this contains:

-  Microprocessor
-  Memory interface controller
-  Peripheral interfaces

Microprocessor
^^^^^^^^^^^^^^

| In our designs, we use only two types:

+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| **Intel**                                                                                              |                                                                                                    | **Xilinx**                                                                                                                                                                   |                                                                                |                                                                                   |
+========================================================================================================+====================================================================================================+==============================================================================================================================================================================+================================================================================+===================================================================================+
| **SoC**                                                                                                | **FPGA**                                                                                           | **SoC**                                                                                                                                                                      | **FPGA**                                                                       | `ACAP <https://www.xilinx.com/an/adaptive-compute-acceleration-platforms.html>`__ |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| `HPS <https://www.intel.com/content/www/us/en/products/programmable/soc/arria-10/applications.html>`__ | `NIOS II <https://www.intel.com/content/www/us/en/products/programmable/processor/nios-ii.html>`__ | `PS7 <https://www.xilinx.com/products/intellectual-property/processing_system7.html>`__ `PS8 <https://www.xilinx.com/products/intellectual-property/zynq-ultra-ps-e.html>`__ | `MicroBlaze™ <https://www.xilinx.com/products/design-tools/microblaze.html>`__ | `Versal <https://www.xilinx.com/products/silicon-devices/acap/versal.html>`__     |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+

| Worth mentioning in case of SoCs, the **Hard Processor System** (HPS) or **Processing System 7/8** (PS7/8) do not contain just the dual-core ARM® Cortex® - A9 MPCore™ processor, they also have other integrated peripherals and memory interfaces. For more information please visit the manufacturer's website, listed in the table above.

-  ``PS7`` --- `Zynq-7000 SoC Processing System <https://docs.xilinx.com/v/u/en-US/pg082-processing-system7>`__ (``processing_system7``)
-  ``PS8`` --- `Zynq UltraScale+ MPSoC Processing System <https://docs.xilinx.com/viewer/book-attachment/xFC3qkokxbD~75kj6nPLuw/2o4flzqn5OqWHaMHwpG3Qg>`__ (``zynq_ultra_ps_e``)
-  ``Versal`` --- `Versal ACAP CIPS <https://docs.xilinx.com/viewer/book-attachment/dwmjhDJGICdJqD4swyVzcQ/4xHxwamgexYelFW1G2yn3w>`__ (``versal_cips``)

Memory Interface Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In almost all cases, the carrier board is not made and designed by Analog Devices, so the external memory solution of the system is given. Meaning we can not support, modify or alter this important part of the system, in several cases we even have system limitations because of it (e.g. the memory interface is not fast enough to handle the required data throughput).

Under the two links below the user can find the landing page of the available memory solutions for both Altera and Xilinx:

-  Intel's memory interfaces: https://www.intel.com/content/www/us/en/programmable/support/support-resources/external-memory.html
-  Xilinx's memory interfaces: https://www.xilinx.com/products/intellectual-property/mig.html#documentation

Peripheral Interfaces
^^^^^^^^^^^^^^^^^^^^^

| These interfaces are used to control external peripherals located on the prototyping board or the FMC IO board.
| In HDL, these ports are named slightly different than how they're in the documentations. Thus, to make it easier for beginners, here you have the naming of the ports depending on the microprocessor used.

SPI
"""

In general, the base system has two Serial Peripheral Interfaces, which are used as a control interface for FMC/HSMC devices. These SPI interfaces are controlled by the integrated SPI controller of the **Hard Processor System** (HPS) or **Processing System 7/8** (PS7/8) or an Intel or Xilinx SPI controller core.

I2C/I2S/SPDIF
"""""""""""""

A couple of carrier boards require these standard interfaces for different purposes, for example, a configuration interface for an audio peripheral device. These peripherals do not necessarily have vital roles in the reference design, it's more like a generic goal to support all the provided peripherals of the carrier board.

HDMI
""""

There is HDMI support for all the carriers which are using the ADV7511 as HDMI transmitter. The HDMI transmitter core can be found :git-hdl:`here <library/axi_hdmi_tx>`.

GPIOs
"""""

The general rule of thumb is to define 64 GPIO pins for the base design:

-  bits [31: 0] always belong to the carrier board;
-  bits [63:32] will be assigned to switches, buttons and/or LEDs, which can be found on the FMC board.

When some of these GPIOs are not used, the input pins should have the output pins driven to them, so that Vivado will not complain about inputs not being assigned to.

Depending on the processor type, add these values to the GPIO number from the HDL project to obtain the final number used in software:

-  PS7 EMIO offset = 54
-  PS8 EMIO offset = 78

Connectivity
""""""""""""

-  Ethernet
-  USB OTG

These interfaces designs are borrowed from the golden reference design of the board.

Interrupts
^^^^^^^^^^

When developing the Linux software parts for an HDL project, the interrupts number to the PS have a different number in the software side.

Not a rule, but in our designs we preffer to use firstly the interrupts from 15 and to go down to 0. Be careful when assigning one, because it might be used in the base design of the carrier!

Always check which are used (in */projects/common/:math:`carrier/`\ carrier_system_bd.tcl*)

++++ Click here to see the interrupts table \|

============= ========== =========== ============ =============
HDL interrupt Linux Zynq Actual Zynq Linux ZynqMP Actual ZynqMP
============= ========== =========== ============ =============
15            59         91          111          143
14            58         90          110          142
13            57         89          109          141
12            56         88          108          140
11            55         87          107          139
10            54         86          106          138
9             53         85          105          137
8             52         84          104          136
7             36         68          96           128
6             35         67          95           127
5             34         66          94           126
4             33         65          93           125
3             32         64          92           124
2             31         63          91           123
1             30         62          90           122
0             29         61          89           121
============= ========== =========== ============ =============

++++

--------------

Board design
~~~~~~~~~~~~

Board capabilities - Xilinx platforms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. raw:: html

   <details><summary>Click to expand</summary>

++++ Board capabilities \| .. include:: arch/xilinx_platforms.rst ++++

.. raw:: html

   </details>


Board capabilities - Intel platforms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. raw:: html

   <details><summary>Click to expand</summary>

++++ Board capabilities \| .. include:: arch/intel_platforms.rst ++++

.. raw:: html

   </details>


--------------

File structure of a project
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   In :git-hdl:`/projects/common/$carrier_name/ <projects/common>` you can find templates for the *system_top.v*, *Makefile*, etc. to help you when creating a new project.


Project files for Xilinx boards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A project for a Xilinx FPGA board should contain the following files:

-  **Makefile** --- auto-generated file; contains all the IP dependencies needed for the project to be built

-  **system_project.tcl** --- script that creates the actual Vivado project and runs the synthesis/implementation of the design

-  **system_bd.tcl** --- sources the *base design first*, then the *board design*, and afterwards it contains all the IP instances and connections that must be added on top of the sourced files, to complete the design of the project (these are specific to the combination of this carrier and board)

-  **system_constr.xdc** --- constraints file of the design; it’s the connection between the physical pins of the FPGA that you want to use and the HDL code that describes the behavior; here you define the FMC I/O pins, board-specific clock signals, timing constraints, etc. The constraints specific to the carrier are imported in the *system_project.tcl* file

-  **system_top.v** --- contains everything about the HDL part of the project; it instantiates the *system_wrapper* module, IO buffers, I/ODDRs, modules that transform signals from LVDS to single-ended, etc. The I/O ports of this Verilog module will be connected to actual I/O pads of the FPGA.

   -  *system_wrapper* --- tool generated file and can be found at *<project_name>.srcs/sources_1/bd/system/hdl/system_wrapper.v*

      -  the I/O ports of this module are declared in either *system_bd.tcl* or in the **board** design file
      -  this can be visualized in Vivado at the Block Design section
      -  the base design, board design and system_bd.tcl describe this module, making the connections between the instantiated IPs

Project files for Intel boards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A project for an Intel FPGA board should contain the following files:

-  **Makefile** --- auto-generated file; contains all the IP dependencies needed for the project to be built

-  **system_project.tcl** --- script that creates the actual Quartus project and runs the synthesis/implementation of the design. It also contains the I/O definitions for the interfaces between the board and the FPGA

-  **system_qsys.tcl** --- also called **platform designer**; sources the *base design first*, then the *board design*, and afterwards it contains all the IP instances and connections that must be added on top of the sourced files, to complete the design of the project (these are specific to the combination of this carrier and board)

-  **system_constr.sdc** --- contains clock definitions and other path constraints

-  **system_top.v** --- contains everything about the HDL part of the project; it instantiates the *system_wrapper* module, IO buffers, I/ODDRs, modules that transform signals from LVDS to single-ended, etc. The I/O ports of this Verilog module will be connected to actual I/O pads of the FPGA

Examples
--------

Some carriers have a different name for these files, for example A10SoC has constraints file for both PL side and PS side:

-  a10soc_plddr4_assign.tcl --- constraints file for the PL
-  a10soc_system_assign.tcl --- constraints file for the PS

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#run
   :alt: Running on hardware#hdl|Main page#ip_cores|IP Cores
