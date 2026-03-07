AD-FMCADC2-EBZ FMC Board
========================

|

.. warning::

   \ **NOTE:**

   | Support for the ad-fmcadc2-ebz is discontinued starting with 2022_R2 Kuiper Linux release and it will not be supported in future releases. Last release in which pre-build files can be found is 2021_r2. Check this :doc:`link </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>` to see all Kuiper releases.


The :adi:`AD-FMCADC2-EBZ` is a high speed data acquisition board featuring :adi:`AD9625` single channel ADC at 2500 MSPS, in a FMC form factor which supports the JESD204B high speed serial interface. This board meets most of the FMC specifications in terms of mechanical size, mounting hole locations, and more. For that information, please refer to the FMC specification.

Although this board does meet most of the FMC specifications, it is not meant as a `commercial off the shelf <https://en.wikipedia.org/wiki/Commercial_off-the-shelf>`_ (COTS) board. If you want a commercial, ready to integrate product, please refer to one of the many FMC manufacturers.

This board is targeted to use the ADI reference designs that work with Xilinx development systems. ADI provides complete source (HDL and software) to re-create those projects (minus the IP provided by the FPGA vendors, which we use), but may not provide enough info to port this to your custom platform.

Contains
--------

The card contains:

-  :adi:`AD9625` 12-bit ADC with sampling speeds of up to 2500 MSPS, with a :adi:`JESD204B <JESD204>` digital interface.
-  :adi:`ADP7104` is a 20V, 500mA, low noise, CMOS LDO
-  :adi:`ADP1753` is a low dropout linear regulators that operate from 1.6 V to 3.6 V and provide up to 800mA of output current.
-  :adi:`ADP2119` is a 2A, 1.2MHz, synchronous step-down DC-to-DC regulator
-  :adi:`ADP1741` is a 2A, low Vin, low dropout, CMOS linear regulator
-  :adi:`ADR280` is a ultralow power high PSRR voltage reference.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/ad-fmcadc2-ebz-photo.jpg
   :alt: ad-fmcadc2-ebz-photo.jpg
   :width: 420px

Note For Revision C
-------------------

If you have a revision C board as indicated in etch next to the white scratch pad area of the PCB we recommend writing to the Serial Output Adjust Register. If you are using the reference design this is done for you. Otherwise when you configure the AD9625 it is suggested that you increase the serial output emphasis by writing to register 0x015 bits 5:4 either 10 or 11.

FPGA Code
---------

:doc:`Xilinx FPGA Code </wiki-migration/resources/fpga/xilinx/fmc/ad-fmcadc2-ebz>`

Eye Scan
--------

Eye scan for this board can be found at :doc:`jesd_eye_scan </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`.

Linux
-----

-  :doc:`AD9625 Linux driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`JESD204B/C Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`: Linux driver for the JESD204B receive core.
-  :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
-  :doc:`ZC706 Linux image </wiki-migration/resources/tools-software/linux-software/zynq_images>`
-  :doc:`Linux on the VC707 </wiki-migration/resources/eval/user-guides/ad-fmcadc2-ebz/quickstart/microblaze>`

Specifications
--------------

The AD-FMCADC2-EBZ board's primary purpose is to quickly and easily connect to an FMC carrier platform and start collecting data using the AD9625. The board is designed to be easy to use. Out of the box the board will self power and self clock when connected to and FMC carrier. The only other required equipment is your chosen signal source to provide and input signal to "Ain".

This rapid prototyping board also has 4 vertically mounted SMA connectors. These are labeled SYSREF IN and SYSREF OUT. These are to enable synchronization of multiple AD-FMCADC2-EBZ boards together using characteristics of the JESD204B high speed serial interface between the AD9625 and FPGA.

Clocking
========

The AD-FMCADC2-EBZ provides multiple options for clocking the AD9625. The default configuration of the board clocks the ADC using an on-board 2.5 GHz, low noise, crystal oscillator. This oscillator is then routed through a wide band transformer producing the differential clock for the ADC.

Alternatively, the oscillator can be disconnected and an external clock source connected by only changing two components on the board. A single ended clock connected to the CLK+ input would then be routed through the transformer in the same way.

Finally, the option exists to connect a differential clock to the board using both the CLK+ and CLK- inputs. Then referencing the schematic make the component changes to directly route the differential input bypassing the transformer.

Front End
=========

The AD-FMCADC2-EBZ uses a passive front end designed for very wide bandwidth. A single ended input needs to be provided to "Ain". A 500 kHz to 6 GHz broadband balun then converts the input signal to differential.

Layout
======

Downloads
---------

Rev C

.. admonition:: Download
   :class: download

   
   -  `02-036007-01-c-1.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/02-036007-01-c-1.pdf>`_
   -  `AD-FMCADC2-EBZ_gerbers.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/AD-FMCADC2-EBZ_gerbers.zip>`_
   -  `05_036007_c_bom_wiki.xlsx <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/05_036007_c_bom_wiki.xlsx>`_
   


Rev D

.. admonition:: Download
   :class: download

   
   -  `02_036007d.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/02_036007d.pdf>`_
   -  `AD-FMCADC2-EBZ_RevD_gerbers.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/AD-FMCADC2-EBZ_RevD_gerbers.zip>`_
   -  `036007_d_bom_wiki.xlsx <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/036007_d_bom_wiki.xlsx>`_
   

