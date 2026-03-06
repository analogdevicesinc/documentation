Pristis HDL Reference Design
============================

Overview
--------

﻿The part is a Parametric measurement Unit specifically designed to test LED drivers used in next-generation high resolution screen technology. ﻿It contains 8 channels each consisting of 5 DACs per channel, 3 of which(3 dual-purpose DACs) are used to control a PMU to force current or voltage in different ranges OR a programable active load current to common output pin.﻿ 2 of the DACs are used to control a comparator high and low levels.

This device is a high performance, highly integrated, high voltage parametric measurement unit with 8 independent channels. Each PMU channel can be programmed to Force Voltage Measure Voltage, Force Voltage Measure Current, Force Current Measure Voltage or Force Current Measure Current. Each PMU channel also includes clamp and comparator functions. Each channel includes a programmable active load with independent control of the sourcing/sinking currents to the DUT with a ±2mA range. All functions are controlled via a 4 wire SPI interface.

**\*Some specifications about the board, the chip, etc. Typically the information found on the** :adi:`en/products` **website**\ \* TODO: no ADI page yet

Supported devices
-----------------

-  AD53580 (TODO: page)

Supported carriers
------------------

-  `ZedBoard <https://www.xilinx.com/products/boards-and-kits/1-8dyf-11.html>`__

Hardware requirements
---------------------

-  TODO: add missing HW, and webpages
-  `ZedBoard <https://www.xilinx.com/products/boards-and-kits/1-8dyf-11.html>`__
-  Pristis EVB/image
-  SD card (at least 16GB); follow :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  Power supply of 12V for the carrier
-  Micro USB Cable

Block design
------------

There were 2 versions of the block diagram that both serves as SPI driver of the device. The version 1 utilizes the SPI controller of Zynq SoC while the version 2 uses the :doc:`SPI Engine </wiki-migration/resources/fpga/peripherals/spi_engine>`.

Block diagram
~~~~~~~~~~~~~

Version 1
^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/v1_pristis_block_diagram.svg
   :align: center
   :width: 600px

Version 2
^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/v2_pristis_block_diagram.svg
   :align: center
   :width: 600px

IP list
~~~~~~~

.. admonition:: Download
   :class: download

   
   -  :git-hdl:`AXI_PWM_GEN <library/axi_pwm_gen>`
   -  :git-hdl:`SPI_ENGINE <library/spi_engine>`
   -  :git-hdl:`AXI_DMAC <library/axi_dmac>`
   


SPI connections
~~~~~~~~~~~~~~~

====== ===============
Signal ZedBoard Pinout
====== ===============
SCLK   M20
CS_n   M19
MOSI   N19
MISO   N20
====== ===============

GPIOs
~~~~~

====== ===============
Signal ZedBoard Pinout
====== ===============
BUSYB  J18
RESETB T19
LOADB  L17
====== ===============

Interrupts
~~~~~~~~~~

Below are the Programmable Logic interrupts used in this project.

++++ Click here to see the interrupts table \|

============= === ========== =========== ============ =============
Instance name HDL Linux Zynq Actual Zynq Linux ZynqMP Actual ZynqMP
============= === ========== =========== ============ =============
axi_hdmi_dma  15  59         91          111          143
axi_iic_main  14  58         90          110          142
---           13  57         89          109          141
---           12  56         88          108          140
axi_iic_fmc   11  55         87          107          139
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

Building the HDL project
------------------------

| The design is built upon ADI's generic HDL reference design framework.
| ADI does not distribute the bit/elf files of these projects so they must be built from the sources available :git-hdl>`__. To get the source you must `clone <https::`here </git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>` the HDL repository.

Then go to projects/pristis/zed location and run the make command by typing in your command prompt:

**Linux/Cygwin**

::

   user@analog:~$ cd hdl/projects/pristis/zed
   user@analog:~/hdl/projects/pristis/zed$ make

| Check :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` on how to prepare your SD card with the proper boot files.
| A more comprehensive build guide can be found in the :doc:`HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`.

System setup
------------

| |image1|
| This setup only includes the carrier and a breakout board setup for its FMC port. The breakout board setup was done to probe the signals coming out of the carrier to test whether the driver is working as intended.

Connections
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/zedboard_jumper_map.png
   :width: 400px

====== ========
Jumper Position
====== ========
JP7    GND
JP8    GND
JP9    3V3
JP10   3V3
JP11   GND
JP18   3V3
====== ========

Resources
---------

-  :git-hdl:`Project source code <projects/pcg_hdl_ad53580_ext>`
-  :git-linux:`DAC Linux driver source codes <drivers/iio/dac>`
-  :git-linux:`Linux devicetree source codes <arch/arm/boot/dts>`
-  TODO: Links to the datasheets/schematics of the boards used in this wiki page
-  `ZedBoard Hardware User's Guide <https://digilent.com/reference/_media/zedboard:zedboard_ug.pdf>`__

More information
----------------

-  :doc:`ADI reference designs HDL user guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`ADI HDL architecture </wiki-migration/resources/fpga/docs/arch>` wiki page
-  :doc:`How to build an ADI HDL project </wiki-migration/resources/fpga/docs/build>`

Support
-------

Analog Devices will provide **limited** online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone FPGA reference designs <community/fpga>` forum.

It should be noted, that the older the tools' versions and release branches are, the lower the chances to receive support from ADI engineers.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pristis_setup.png
   :width: 800px
