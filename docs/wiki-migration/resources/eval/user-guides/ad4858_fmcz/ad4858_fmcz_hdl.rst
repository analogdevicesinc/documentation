EVAL-AD4858 HDL Reference Design
================================

.. warning::

   This documentation is deprecated The new doc is available at https://analogdevicesinc.github.io/hdl/projects/ad485x_fmcz/index.html


Overview
--------

:adi:`EVAL-AD4858 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4858>` board contains :adi:`AD4858 <en/products/ad4858.html>` chip, which is a 20-bit, low noise 8-channel simultaneous sampling successive approximation register (SAR) ADC, with buffered differential, wide common range picoamp inputs.

More about simultaneous sampling A/D converters :adi:`here <en/product-category/simultaneous-sampling-ad-converters.html>`.

The :adi:`EVAL-AD4858 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4858>` supports pin-selectable SPI CMOS and LVDS serial interfaces. In CMOS mode, applications may employ between 1-8 lanes of serial output data, allowing the user to optimize bus width and data throughput. In LVDS mode, pins SDO+/-, SCKI+/- and SCKO+/- function as differential serial data input, clock output and clock input pins respectively (from the FPGA's point of view).

Supported carriers
------------------

-  `Zedboard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__

Hardware requirements
---------------------

-  :adi:`EVAL-AD4858 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD48588>`
-  `Zedboard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__
-  Signal generator
-  1x Ethernet cable
-  1x Micro-B USB cable for UART connectivity (optional)
-  1x SD card (at least 16GB); follow :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` to set up the card

Block design
------------

Block diagram
~~~~~~~~~~~~~

The data path and clock domains are depicted in the following diagram:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4858_fmcz/ad4858_fmcz_block_diagram.svg
   :align: center

Clock scheme
~~~~~~~~~~~~

| Depending on the configuration used (CMOS or LVDS), the scheme differs a little bit. See the differences between the diagrams from below.
| |image1|

| Because of limitations from the evaluation board, we used an internal clock of the FPGA.

Therefore, the external clocks given to AXI_AD4858 IP are:

-  in LVDS mode:

   -  ``external_clk`` = 200MHz (F_CLK0)
   -  ``external_fast_clk`` = 400MHz (F_CLK1)

-  in CMOS mode:

   -  ``external_clk`` = 100MHz (F_CLK0)

| ++++About the frequency calculation for the MMCM from axi_pwm_gen\| :math:`F_VCO = 1000 \times (CLKFBOUT__MULT__F) / (CLKIN_PERIOD \times DIVCLK_DIVIDE)` (MHz)
| :math:`F_CLK0 = F_VCO / CLKOUT0_DIVIDE_F` (MHz)
| :math:`F_CLK1 = F_VCO / CLKOUT1_DIVIDE_F` (MHz)

In :git-hdl:`our designs <projects/ad485x_fmcz/common/ad485x_fmcz_bd.tcl>`, the following parameters mean:

-  VCO_DIV = DIVCLK_DIVIDE
-  VCO_MUL = CLKFBOUT_MULT_F
-  CLK0_DIV = CLKOUT0_DIVIDE_F
-  CLK1_DIV = CLKOUT1_DIVIDE_F

For more details regarding the MMCM clock frequencies, check the `UG472 (7 series) <https://www.xilinx.com/content/dam/xilinx/support/documents/user_guides/ug472_7Series_Clocking.pdf>`__ and `UG572 (UltraScale/+) <https://www.xilinx.com/support/documents/user_guides/ug572-ultrascale-clocking.pdf>`__. ++++

| 
| For custom systems where the :adi:`AD4858 <en/products/ad4858.html>` chip is used, we recommend using an external clock, and not a clock from the FPGA like it is done in this reference design.

Description of components
~~~~~~~~~~~~~~~~~~~~~~~~~

The :doc:`AXI_AD4858 </wiki-migration/resources/fpga/docs/axi_ad4858>` IP core contains 2 configuration modes, these being :git-hdl:`CMOS <library/axi_ad485x/axi_ad485x_cmos.v>` and :git-hdl:`LVDS <library/axi_ad485x/axi_ad485x_lvds.v>`. Depending on which of them you want to use, different files are being used (see :git-hdl:`here <projects/ad485x_fmcz/zed/system_project.tcl#L18-L22>`).

Configurations
^^^^^^^^^^^^^^

The :adi:`EVAL-AD4858 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4858>`'s digital interface has two serial conversion data output modes: CMOS and LVDS. Depending on which is selected at build time (see section *Building the HDL project* section), specific files are used for the project. They have different constraints files and different top modules.

The :adi:`AD4858 <en/products/ad4858.html>` chip has 3 modes of configuration regarding the packet format: 20/24/32-bit format, which is configurable at runtime.

Limitations
^^^^^^^^^^^

| The period of the SCKI clock signal is limited to a minimum of 2.5ns (at most 400MHz). Having SCKI frequency constrained, the case where the conversion time is maximum (715ns) is not achievable with the 24 and 32-bit packet formats.
| In other words, if you want to use the maximum conversion rate of 400MHz, then you can use **only** the 20-bit packet format.

IP list
~~~~~~~

.. admonition:: Download
   :class: download

   
   -  :git-hdl:`AXI_AD485x <library/axi_ad485x>`
   -  :git-hdl:`AXI_PWM_GEN <library/axi_pwm_gen>`
   -  :git-hdl:`AXI_CLKGEN <library/axi_clkgen>`
   -  :git-hdl:`AXI_DMAC <library/axi_dmac>`
   -  :git-hdl:`UTIL_CPACK2 <library/util_pack/util_cpack2>`
   


CPU/Memory interconnects addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ===========
Instance    Address
=========== ===========
axi_ad4858  0x43C0 0000
axi_pwm_gen 0x43D0 0000
ad4858_dma  0x43E0 0000
adc_clkgen  0x4400 0000
=========== ===========

Interrupts
~~~~~~~~~~

Below are the Programmable Logic interrupts used in this project.

++++ Click here to see the interrupts table \|

============== === ========== =========== ============ =============
Instance name  HDL Linux Zynq Actual Zynq Linux ZynqMP Actual ZynqMP
============== === ========== =========== ============ =============
---            15  59         91          111          143
...            ..  ..         ..          ..           ..
**ad4858_dma** 10  54         86          106          138
---            9   53         85          105          137
---            8   52         84          104          136
---            7   36         68          96           128
---            ..  ..         ..          ..           ..
---            0   29         61          89           121
============== === ========== =========== ============ =============

++++

Building the HDL project
------------------------

ADI does not distribute the bit/elf files of these projects, so they must be built from the sources available :git-hdl>`__. To get the source you must `clone <https::`here </git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>` the HDL repository.

Then go to :git-hdl:`projects/ad485x_fmcz/zed` location and run the make command by typing in your command prompt one of the following commands, depending on which configuration you want to use:

-  CMOS version of the project: ``make LVDS_CMOS_N=0``
-  LVDS version of project: ``make LVDS_CMOS_N=1``

**Linux/Cygwin**

::

   user@analog:~$ cd hdl/projects/ad485x_fmcz/zed
   user@analog:~/hdl/projects/ad485x_fmcz/zed$ make LVDS_CMOS_N=0

| Check :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` on how to prepare your SD card with the proper boot files.
| A more comprehensive build guide can be found in the :doc:`HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`.

System setup
------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4858_fmcz/ad4858_fmcz_zed_setup.jpg
   :align: center

As for the signal generator, you can use whichever Signal Generator you want.

In this setup, we chose to use :adi:`M2K <en/ADALM2000.html>` (with a :doc:`BNC adapter board </wiki-migration/university/tools/m2k/accessories/bnc>`) as signal generator for channel 0, while testing the system in LVDS mode. Using :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>`, we set the amplitude, frequency, offset and phase of the generated signals.

A more comprehensive guide on how to use :adi:`M2K <en/ADALM2000.html>` and Scopy can be found :doc:`here </wiki-migration/university/tools/m2k/users>` and :doc:`here </wiki-migration/university/tools/m2k/scopy>`.

Resources
~~~~~~~~~

-  :adi:`ADALM2000 (M2K) <en/ADALM2000.html>`
-  :doc:`M2K BNC adapter board </wiki-migration/university/tools/m2k/accessories/bnc>`
-  2x BNC to SMA cables
-  2x Micro-B USB cables

Connections
~~~~~~~~~~~

-  AD4858-FMCZ connected to FMC port of Zedboard
-  M2K connected to PC using Micro-B USB cable
-  2x BNC to SMA cables connected from SMA0+/- (AD4858-FMCZ) to W1/W2 (BNC adapter board)
-  1x Micro-B USB for M2K connectivity to the PC
-  1x Micro-B USB for UART on Zedboard

.. _resources-1:

Resources
---------

.. admonition:: Download
   :class: download

   
   -  :git-hdl:`AXI_AD485x IP <library/axi_ad485x>`
   -  :git-hdl:`AD4858_FMCZ on Zed <projects/ad485x_fmcz/zed>` HDL project
   -  :git-linux:`AD4858-FMCZ Linux devicetree <arch/arm/boot/dts/zynq-zed-adv7511-ad4858.dts>`
   -  :git-linux:`AD4858-FMCZ Linux driver <drivers/iio/adc/ad4858.c>`
   


More information
----------------

-  :adi:`AD4858 <en/products/ad4858.html>` chip datasheet
-  :doc:`AXI_AD4858 IP </wiki-migration/resources/fpga/docs/axi_ad4858>` wiki documentation
-  :doc:`AXI_PWM_GEN </wiki-migration/resources/fpga/docs/axi_pwm_gen>` wiki documentation
-  :doc:`AXI_CLKGEN </wiki-migration/resources/fpga/docs/axi_clkgen>` wiki documentation
-  :doc:`High-Speed DMA Controller Peripheral </wiki-migration/resources/fpga/docs/axi_dmac>` wiki documentation
-  `UTIL_CPACK2 <https://wiki.analog.com/resources/fpga/docs/util_cpack2>`__ wiki documentation
-  :doc:`How to prepare an SD card </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` with boot files
-  :doc:`ADI reference designs HDL user guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`ADI HDL architecture </wiki-migration/resources/fpga/docs/arch>` wiki page
-  :doc:`How to build an ADI HDL project </wiki-migration/resources/fpga/docs/build>`

Support
-------

Analog Devices will provide **limited** online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone FPGA reference designs <community/fpga>` forum.

It should be noted, that the older the tools' versions and release branches are, the lower the chances to receive support from ADI engineers.

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/ad4858/ad4858_fmcz_clock_path.jpg
