AD-FMCADC4-EBZ FMC Board
========================

Introduction
------------

.. important::

   The :adi:`EVAL-AD-FMCADC4-EBZ` board has been retired, and is no longer available for sale. It has been removed from the HDL and software repository, but is still available in the history.


The :adi:`EVAL-AD-FMCADC4-EBZ` is a high speed four channel data acquisition board featuring two :adi:`AD9680` dual channel ADC at 1000 MSPS (1240 MSPS) and four ADA4961 :adi:`ADA4961` low distortion, 3.2 GHz, RF DGA driving each converter. The FMC form factor supports the JESD204B high speed serial interface. All clocking and channel synchronization is provisioned on-board using the AD9528 :adi:`AD9528` clock generator. This board meets most of the FMC specifications in terms of mechanical size, mounting hole locations etc., for further details, please refer to the FMC specification.

Although this board does meet most of the FMC specifications, it is not meant as a `commercial off the shelf <https://en.wikipedia.org/wiki/Commercial_off-the-shelf>`_ (COTS) board. If a commercial, ready to go integrate product is required, please refer to one of the many FMC manufacturers.

ADI also provides reference designs (HDL and software) for this board to work with commonly available Altera and Xilinx development boards.

Hardware
--------

The AD-FMCADC4-EBZ board's primary purpose is to demonstrate the capabilities of the devices on board quickly and easily by providing a seamless interface to an FMC carrier platform and running the reference design on the carrier FPGA. The board is designed to self power and self clock when connected to the FMC carrier. The analog signals (up to four) are connected to J301A, J301B, J301C and J301D. This rapid prototyping board can also be synchronized across channels.

Devices
~~~~~~~

The FMC board includes the following products by Analog Devices:

-  :adi:`AD9680` 14-bit dual channel ADC with sampling speeds of up to 1250 MSPS, with a :adi:`JESD204B <JESD204>` digital interface.
-  :adi:`ADA4961` Low Distortion, 3.2 GHz, RF Digital Gain Amplifier.
-  :adi:`AD9528` JESD204B Clock Generator with 14 LVDS Outputs
-  :adi:`ADP2384` 20 V, 4 A, Synchronous, Step-Down DC-to-DC Regulator
-  :adi:`ADP7104` is a 20V, 500mA, low noise, CMOS LDO
-  :adi:`ADM7154` 600 mA, Ultra Low Noise, High PSRR, RF Linear Regulator
-  :adi:`ADM7172` 6.5 V, 2 A, Ultralow Noise, High PSRR, Fast Transient Response CMOS LDO
-  :adi:`ADP1741` is a 2A, low Vin, low dropout, CMOS linear regulator

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/20150331_135648-final.jpg
   :align: center
   :width: 300px

::

                                                    Top View

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/20150402_100228-finalbot.jpg
   :align: center
   :width: 300px

::

                                                    Bottom View

Clocking
~~~~~~~~

The AD-FMCADC4-EBZ includes an on-board 80MHz reference oscillator from Crystek. This feature can be disconnected and an external reference can be applied through J901. When referencing the schematic make sure the proper component changes are made in order to directly route the input into the AD9528.

Analog Front End
~~~~~~~~~~~~~~~~

The AD-FMCADC4-EBZ uses a passive front end designed for very wide bandwidth. A single ended input needs to be provided to the analog inputs mentioned earlier. A 1:2 impedance ratio broadband balun then converts the input signal differentially to the ADA4961 inputs and has a 1.6GHz bandwidth at -3dB. Each channel amplifier can be adjusted independently in terms of gain.

Revision A
~~~~~~~~~~

The revision A board supports amplifier gain control via spi. After power-up, the gain of the amplifier defaults to an attenuated state. Use a low jitter, low noise signal source with a level at -20dBm to the analog inputs (J301-A/B/C/D). Apply a signal source no greater than -10dBm to achieve full-scale of the converter when maximum gain of the amplifier is applied.

Running No-OS Application & Changing Sampling Rate to 1.24GHz
-------------------------------------------------------------

The HDL reference design is built around a processor as in an embedded system. You may use either Linux or No-OS software to demonstrate the design (details in the downloads section). In order to run the HDL with the No-OS application, first we need to build the HDL bit file and software elf file.

At the time of this writing, we are using the 'dev' branch for both. The :doc:`HDL user guide </wiki-migration/resources/fpga/docs/hdl>` contains the instructions to build the bit file. **Please make sure you use the 'dev' branch (checkout dev right after cloning).**

Once the bit file is ready, follow these instructions to build the elf file. This assumes you are following our directory structures. If you are not, just get the idea from here and port it to your environment. However you have to figure out things on your own.

-  Clone :git-no-OS>`__ repository
-  Checkout the latest release branch (git checkout branch)\ `hdl release notes <https::`No-OS </github.com/analogdevicesinc/hdl/releases>`
-  Change the directory to \`fmcadc4/zc706\`.
-  Make the elf file by running \`make\` or \`make HDF-FILE=<HDL-REPO>/projects/fmcadc4/zc706/fmcadc4_zc706.sdk/system_top.hdf\`
-  \`make run\` to download trough JTAG the hdl bitstream and software elf, this will also start the processor
-  \`make capture\` read through the memory debugger the captured samples in RAM. Tha data will be saved in .csv files

If you are more comfortable with the GUI, import all the files (or folders) that the make uses.

A typical run looks like this:

::

   [~/github/noos/ad-fmcadc4-ebz/zc706]> make HDF-FILE=~/github/hdl/projects/fmcadc4/zc706/fmcadc4_zc706.sdk/system_top.hdf 
   xsct -s ../../scripts/xilinx_xsct.tcl ~/github/hdl/projects/fmcadc4/zc706/fmcadc4_zc706.sdk/system_top.hdf >> xilinx_xsct.log 2>&1
                                                                                                                                                                                                    
   arm-xilinx-eabi-gcc -DXILINX -Ibsp/ps7_cortexa9_0/include -I.. -I../../common_drivers/adc_core -I../../common_drivers/jesd204b_gt -I../../common_drivers/jesd204b_v51 -I../../common_drivers/xilinx_platform_drivers -I../../drivers/ad9528 -I../../drivers/ad9680 -Os -ffunction-sections -fdata-sections -o zc706.elf sw/src/platform.c ../ad_fmcadc4_ebz.c ../../common_drivers/adc_core/adc_core.c ../../common_drivers/jesd204b_gt/jesd204b_gt.c ../../common_drivers/jesd204b_v51/jesd204b_v51.c ../../common_drivers/xilinx_platform_drivers/platform_drivers.c ../../drivers/ad9528/ad9528.c ../../drivers/ad9680/ad9680.c -Lbsp/ps7_cortexa9_0/lib/ -Tsw/src/lscript.ld -Wl,--start-group,-lxil,-lgcc,-lc,--end-group
   [~/github/noos/ad-fmcadc4-ebz/zc706]

Start an UART terminal.

::

   [USB0]
   port    = /dev/ttyUSB0
   speed   = 115200
   bits    = 8
   stopbits    = 1
   parity  = none
   crlfauto    = True ## if not set, expect non-aligned text

   [~/github/noos/ad-fmcadc4-ebz/zc706]> gtkterm -c USB0 &

For the \`make run\` case. You can also run it using Vivado or SDK - up to you.

::

   [~/github/noos/fmcadc4/zc706]> make run

    make run
   xsdb  ../../../no-OS/scripts/xsdb.tcl ZYNQ_PS7
   attempting to launch hw_server

   ****** Xilinx hw_server v2017.4.1
     **** Build date : Jan 30 2018-15:42:25
       ** Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.

   INFO: hw_server application started
   INFO: Use Ctrl-C to exit hw_server application

   INFO: To connect to this hw_server instance use url: TCP:127.0.0.1:3121

   100%    6MB   1.7MB/s  00:03
   Downloading Program -- ~/github/noos/fmcadc4/zc706/sw/Release/sw.elf
           section, .text: 0x00100000 - 0x00113487
           section, .init: 0x00113488 - 0x0011349f
           section, .fini: 0x001134a0 - 0x001134b7
           section, .rodata: 0x001134b8 - 0x00114387
           section, .data: 0x00114388 - 0x00114de3
           section, .eh_frame: 0x00114de4 - 0x00114de7
           section, .mmu_tbl: 0x00118000 - 0x0011bfff
           section, .ARM.exidx: 0x0011c000 - 0x0011c007
           section, .init_array: 0x0011c008 - 0x0011c00b
           section, .fini_array: 0x0011c00c - 0x0011c00f
           section, .bss: 0x0011c010 - 0x0011c373
           section, .heap: 0x0011c374 - 0x0011e37f
           section, .stack: 0x0011e380 - 0x00121b7f
   100%    0MB   0.6MB/s  00:00
   Setting PC to Program Start Address 0x00100000
   Successfully downloaded ~/github/noos/fmcadc4/zc706/sw/Release/sw.elf

The following messages should appear on the terminal.

::

   QPLL ENABLE
   Rx link is enabled
   Measured Link Clock: 250 MHz
   Link status: DATA
   SYSREF captured: Yes
   adc_setup adc core initialized (1000 MHz).
   adc_setup adc core initialized (1000 MHz).
   RX capture done.

A brief background information on what is happening. Let's look at the No-OS main function. First, it configures and sets the GPIO based on the board.

.. code:: c

        ad_gpio_set(GPIO_AD9528_STATUS, 0x0);
        ad_gpio_set(GPIO_AD9528_RSTN, 0x0); // reset
        ad_gpio_set(GPIO_AD9528_RSTN, 0x1); // bring out of reset

The clock chip is programmed to output the desired clocks and sys-ref signals. The default setting is 1GHz for the AD9680 and 500MHz for the FPGA.

::

        ad9528_setup(&ad9528_spi_device, &ad9528_param);

The transceiver cores are initialized. Here only DRP access is possible. If you are planning to change the transceivers, this is where they should be.

::

        xcvr_setup(&ad9680_xcvr);

The AD9680 devices are initialized (checking the PLL status)

::

        ad9680_setup(&ad9680_0_spi_device, ad9680_0_param);
        ad9680_setup(&ad9680_1_spi_device, ad9680_1_param);

The design uses ADI's JESD IP- it needs to be programmed to match the device settings (frame count, byte count, scrambling and such).

::

        jesd_setup(ad9680_jesd);

After the above setup, bring the transceivers up, here we check for everything on the link, starting from the PLL locked to SYNC deasserted.

::

        axi_jesd204_rx_status_read(ad9680_jesd);

The individual AD9680 cores are brought out of reset.

::

        adc_setup(ad9680_0_core);

The ADC has a PRBS generator at the sample level that can be monitored in the FPGA. This is a robust way to confirming the link status. The software monitors this and reports any errors.

This is setting the PRBS generator in the device.

::

       ad9680_test(&ad9680_0_spi_device, AD9680_TEST_PN9);

This is setting the PRBS monitors in the FPGA.

::

       adc_pn_mon(ad9680_0_core, ADC_PN9)

If you don't see any other messages in the UART other than the ones mentioned above- all is well.

Here is the ILA plot screen capture

.. note::

   We are not supporting the ILA in the reference designs since the hdl_2016_r1 release


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc4_ila.png
   :alt: FMCADC4-ILA
   :width: 500px

Downloads (Hardware)
--------------------

.. admonition:: Download
   :class: download

   Rev A:

   
   -  `Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc4-ebz/20_039601a_top.pdf>`_
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc4-ebz/039601a_bom.xls>`_
   -  `PCBoard Fab Drawing <https://wiki.analog.com/_media/resources/eval/user-guides/ska_eval_fab.pdf>`_
   -  `PCBoard Gerber files <https://wiki.analog.com/_media/resources/eval/user-guides/ska_eval_cam2.zip>`_
   


Downloads (HDL)
---------------

.. include:: ../../fpga/docs/hdl/downloads_insert.rst .. include:: ../../fpga/docs/hdl/downloads_insert.rst

Downloads (Linux)
-----------------

-  :doc:`JESD204B/C Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`: Linux driver for the JESD204B receive core.
-  :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
-  :doc:`AD9680-ADA4961 Linux driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`ZC706 Linux image </wiki-migration/resources/tools-software/linux-software/zynq_images>`
