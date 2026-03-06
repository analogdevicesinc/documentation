ADEMA127 Technical Reference Manual
===================================

Overview
--------

**\*Some specifications about the board, the chip, etc. Typically the information found on the** :adi:`en/products` **website**\ \*

Supported devices
-----------------

**\*IF IT APPLIES**\ \*

Supported carriers
------------------

**\*At least one. Should be updated each time the project is ported to another carrier**\ \*

Hardware requirements
---------------------

\**\* MENTION THESE \**\*

-  Boards and PMODs used
-  Cables and their type
-  1x SD card (at least 16GB); follow :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  Power supplies
-  Other add-ons, etc.

**\*THIS IS JUST AN EXAMPLE**\ \*

-  :adi:`AD9695-1300EBZ <AD9695>`
-  `ZCU102 <https://www.xilinx.com/ZCU102>`__
-  :doc:`AD-SYNCHRONA14-EBZ </wiki-migration/resources/eval/user-guides/ad-synchrona14-ebz>`
-  :adi:`ADALM2000 (M2K) <en/ADALM2000.html>`
-  :doc:`ADALM2000 BNC adapter board </wiki-migration/university/tools/m2k/accessories/bnc>`
-  5 \* SMA to SMA cable
-  Ethernet cable
-  1x SD card (at least 16GB); follow :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  3 \* 50 Ohm DC to 12Ghz SMA Termination
-  VADJ of Zedboard must be set to **2.5V**
-  Jumpers P1 and P2 must be put in (1,2) position
-  On ZCU102: switch 6 from SW15 must be put in ON position to be able to boot from SD card
-  Power supply of 12V for the carrier

Block design
------------

Block diagram
~~~~~~~~~~~~~

\**\* MUST HAVE \**\* The data path and clock domains are depicted on the below diagram:

\*\* TIP: upload the .svg file for the diagram to have high quality \*\*

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9695_fmc_02.svg
   :alt: ad9695_fmc_02.svg

Clock scheme **\*IF IT APPLIES**\ \*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  External clock source :doc:`AD-SYNCHRONA14-EBZ </wiki-migration/resources/eval/user-guides/ad-synchrona14-ebz>`
-  SYSREF clocks are LVDS
-  ADCCLK and REFCLK are LVPECL

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/timing_ad9695_1.png
   :alt: timing_ad9695_1.png

Description of components
~~~~~~~~~~~~~~~~~~~~~~~~~

**\*OTHER COMPONENTS FROM THE PROJECT, EX: SYNCHRONA**\ \*

Only the channels presented in the clocking selection are relevant. For the rest, you can either disable them or just put a divided frequency of the source clock.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/synchronasettings1.png
   :alt: synchronasettings1.png

Configurations
^^^^^^^^^^^^^^

Limitations
^^^^^^^^^^^

**\*EXAMPLE OF CONFIGURATION/LIMITATION. PLEASE WRITE THIS KIND OF INFORMATION IF IT APPLIES TO THE PROJECT**\ \*

The design has one JESD receive chain with 4 lanes at rate of 13Gbps. The JESD receive chain consists of a physical layer represented by an XCVR module, a link layer represented by an RX JESD LINK module and transport layer represented by a RX JESD TPL module. The link operates in Subclass 1.

The link is set for full bandwidth mode and operate with the following parameters:

Deframer paramaters: L=4, M=2, F=1, S=1, N’=16

| SYSREF - 5.078125 MHZ
| REFCLK – 325MHz (Lane Rate/40)
| DEVICECLK -325 MHz
| ADCCLK – 1300MHz
| JESD204B Lane Rate – 13Gbps

The transport layer component presents on its output 128 bits at once on every clock cycle, representing 4 samples per converter. The two receive chains are merged together and transferred to the DDR with a single DMA.

IP list
~~~~~~~

\**\* Embedded from the hdldownloads page, master branch \**\*

\**\* THIS IS JUST AN EXAMPLE \**\*

.. admonition:: Download
   :class: download

   
   -  :git-hdl:`AXI_AD4858 <library/axi_ad4858>`
   -  :git-hdl:`AXI_PWM_GEN <library/axi_pwm_gen>`
   -  :git-hdl:`AXI_CLKGEN <library/axi_clkgen>`
   -  :git-hdl:`AXI_DMAC <library/axi_dmac>`
   -  :git-hdl:`UTIL_UPACK2 <library/util_pack/util_upack2>`
   -  :git-hdl:`UTIL_CPACK2 <library/util_pack/util_cpack2>`
   


I2C connections
~~~~~~~~~~~~~~~

SPI connections
~~~~~~~~~~~~~~~

GPIOs
~~~~~

CPU/Memory interconnects addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\**\* THIS IS JUST AN EXAMPLE \**\*

=========== ==========
Instance    Address
=========== ==========
axi_ad4858  0x43c00000
axi_pwm_gen 0x43d00000
ad4858_dma  0x43e00000
adc_clkgen  0x44000000
=========== ==========

Interrupts
~~~~~~~~~~

Below are the Programmable Logic interrupts used in this project.

++++ Click here to see the interrupts table \|

============= === ========== =========== ============ =============
Instance name HDL Linux Zynq Actual Zynq Linux ZynqMP Actual ZynqMP
============= === ========== =========== ============ =============
---           15  59         91          111          143
---           14  58         90          110          142
---           13  57         89          109          141
---           12  56         88          108          140
---           11  55         87          107          139
---           10  54         86          106          138
---           9   53         85          105          137
---           8   52         84          104          136
---           7   36         68          96           128
---           6   35         67          95           127
---           5   34         66          94           126
---           4   33         65          93           125
---           3   32         64          92           124
---           2   31         63          91           123
---           1   30         62          90           122
---           0   29         61          89           121
============= === ========== =========== ============ =============

++++

**\*These are the project-specific interrupts (usually found in /project_name/common/Project_name_bd,tcl).
Add the name of the component that uses that interrupt.
Use a hidden section so this page won't get to be kilometers long.\\\\**\ \*

Building the HDL project
------------------------

**\*YOU CAN KEEP THE FIRST LINE SINCE IT IS GENERIC**\ \*

| The design is built upon ADI's generic HDL reference design framework.
| ADI does not distribute the bit/elf files of these projects so they must be built from the sources available :git-hdl>`__. To get the source you must `clone <https::`here </git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>` the HDL repository.

Then go to the **\*PROJECT LOCATION WITHIN HDL (EX: projects/ad9695/zcu102)**\ \* location and run the make command by typing in your command prompt:

**Linux/Cygwin**

**\*Say which is the default configuration that's built when running ``make``, give examples of running with all parameters and also with just one. Say that it will create a folder with the name ... when running with the following parameters.**\ \*

::

   user@analog:~$ cd hdl/projects/cn0577/zed
   user@analog:~/hdl/projects/cn0577/zed$ make TWOLANES=0

| 
| It will create a folder called ``TWOS`` because the script that builds the project, removes the strings "JESD" and "LANE" from the parameter's name because Linux has a maximum path length of 260 characters.
| **\*KEEP THIS LINE TOO**\ \* Check :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` on how to prepare your SD card with the proper boot files.
| A more comprehensive build guide can be found in the :doc:`HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`.

System setup
------------

**\* Upload a picture of what your setup looks like.
Attention: hide board labels (e.g., from AssetTiger) and other information that is ADI internal only.**\ \*

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/setup_ad9695_zcu102_1.jpg
   :alt: setup_ad9695_zcu102_1.jpg
   :width: 800px

\**\* PLESE KEEP THIS WHOLE SECTION AND ADAPT IT TO YOUR PROJECT, ESPECIALLY IF YOU HAVE EXTERNAL CLOCKS OR OTHER SIGNALS \**\*

Connections
~~~~~~~~~~~

\**\* MENTION THESE \**\*

-  What VADJ to be used for each type of setup
-  How the jumpers/switches should be set on the board/carrier
-  On which FMC port should the board be placed
-  Other changes to the board and the carrier
-  AD9695 connected to ZCU102 on FMC HPC1

====== ========
ZCU102 SYNCRONA
====== ========
J79    CH2_P
J80    CH2_N
====== ========

============ ========
ADC9695 EVAL SYNCRONA
============ ========
J202         CH10_P
J200         CH1_P
P202         CH9_P
============ ========

Resources
---------

\**\* MENTION THESE \**\*

-  Link to the project source code
-  Links to the wiki documentation of the IPs that are used in this project
-  Links to the Linux driver and devicetree source code and wiki documentation
-  Links to the datasheets/schematics of the boards used in this wiki page

More information
----------------

-  :doc:`ADI reference designs HDL user guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`ADI HDL architecture </wiki-migration/resources/fpga/docs/arch>` wiki page
-  :doc:`How to build an ADI HDL project </wiki-migration/resources/fpga/docs/build>`
-  Other relevant information

\**\* THIS IS JUST AN EXAMPLE \**\*

-  :doc:`EVALUATING THE AD9695/AD9697 ANALOG-TO-DIGITAL CONVERTER </wiki-migration/resources/eval/ad9695-1300ebz>`
-  :doc:`AD-SYNCHRONA14-EBZ </wiki-migration/resources/eval/user-guides/ad-synchrona14-ebz>`
-  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`
-  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`
-  :doc:`AXI_PWM_GEN </wiki-migration/resources/fpga/docs/axi_pwm_gen>` wiki documentation
-  :doc:`AXI_CLKGEN </wiki-migration/resources/fpga/docs/axi_clkgen>` wiki documentation
-  :doc:`High-Speed DMA Controller Peripheral </wiki-migration/resources/fpga/docs/axi_dmac>` wiki documentation
-  `UTIL_CPACK2 <https://wiki.analog.com/resources/fpga/docs/util_cpack2>`__ wiki documentation
-  `UTIL_UPACK2 <https://wiki.analog.com/resources/fpga/docs/util_upack2>`__ wiki documentation
-  :doc:`How to prepare an SD card </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` with boot files
-  :doc:`ADI reference designs HDL user guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`ADI HDL architecture </wiki-migration/resources/fpga/docs/arch>` wiki page
-  :doc:`How to build an ADI HDL project </wiki-migration/resources/fpga/docs/build>`

Support
-------

Analog Devices will provide **limited** online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone FPGA reference designs <community/fpga>` forum.

It should be noted, that the older the tools' versions and release branches are, the lower the chances to receive support from ADI engineers.
