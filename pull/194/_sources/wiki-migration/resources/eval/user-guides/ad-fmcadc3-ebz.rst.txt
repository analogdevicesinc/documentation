AD-FMCADC3-EBZ FMC Board
========================

The :adi:`AD-FMCADC3-EBZ <EVAL-AD-FMCADC3-EBZ>` is a high speed data acquisition board featuring :adi:`AD9625` single channel ADC at 2500 MSPS and the ADA4961 :adi:`ADA4961` Low Distortion, 3.2 GHz, RF DGA driving the converter. The FMC form factor supports the JESD204B high speed serial interface. This board meets most of the FMC specifications in terms of mechanical size, mounting hole locations, and more. For that information, please refer to the FMC specification. Although this board does meet most of the FMC specifications, it is not meant as a `commercial off the shelf <https://en.wikipedia.org/wiki/Commercial_off-the-shelf>`_ (COTS) board. If you want a commercial, ready to integrate product, please refer to one of the many FMC manufacturers. This board is targeted to use the ADI reference designs that work with Xilinx development systems. ADI provides complete source (HDL and software) to re-create those projects (minus the IP provided by the FPGA vendors, which we use), but may not provide enough info to port this to your custom platform.

Contains
--------

The card contains:

-  :adi:`AD9625` 12-bit ADC with sampling speeds of up to 2500 MSPS, with a :adi:`JESD204B <JESD204>` digital interface.
-  :adi:`ADA4961` Low Distortion, 3.2 GHz, RF Digital Gain Amplifier.
-  :adi:`ADP7104` is a 20V, 500mA, low noise, CMOS LDO
-  :adi:`ADP1753` is a low dropout linear regulators that operate from 1.6 V to 3.6 V and provide up to 800mA of output current.
-  :adi:`ADP2119` is a 2A, 1.2MHz, synchronous step-down DC-to-DC regulator
-  :adi:`ADP1741` is a 2A, low Vin, low dropout, CMOS linear regulator
-  :adi:`ADR280` is a ultralow power high PSRR voltage reference.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/img_1568.jpeg
   :alt: AD-FMCADC3-EBZ
   :align: center
   :width: 200px

Revision A
----------

The revision A board has the amplifier gain control via spi. When powering up the FMCADC3 board. The gain of the amplifier will default to an attenuated state. When applying a signal source to the FMCADC3 at the analog input connector, J201. Use a low jitter, low noise signal source with a level at -20dBm. Apply a signal source no greater than -8dBm when achieving full-scale of the converter and maximum gain is of the amplifier is applied.

FPGA Code
---------

:doc:`Xilinx FPGA Code </wiki-migration/resources/fpga/xilinx/fmc/ad-fmcadc3-ebz>`

The `AD-FMCADC2-EBZ <https://wiki.analog.com/ad-fmcadc2-ebz>`_ and the AD-FMCADC3-EBZ use common HDL. .. include:: ../../fpga/docs/hdl/downloads_insert.rst .. include:: ../../fpga/docs/hdl/downloads_insert.rst

Linux
-----

-  :doc:`AD9625 AXI Linux driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`ADA4961 Low Distortion, 3.2 GHz, RF DGA Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`JESD204B/C Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`: Linux driver for the JESD204B receive core.
-  :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
-  :doc:`ZC706 Linux image </wiki-migration/resources/tools-software/linux-software/zynq_images>`
-  :doc:`Linux on the VC707 </wiki-migration/resources/eval/user-guides/ad-fmcadc2-ebz/quickstart/microblaze>`

Specifications
--------------

The AD-FMCADC3-EBZ board's primary purpose is to quickly and easily connect to an FMC carrier platform and start collecting data using the AD9625. The board is designed to be easy to use. Out of the box the board will self power and self clock when connected to and FMC carrier. The only other required equipment is your chosen signal source to provide and input signal to "Ain".

This rapid prototyping board also has 4 vertically mounted SMA connectors. These are labeled SYSREF IN and SYSREF OUT. These are to enable synchronization of multiple AD-FMCADC3-EBZ boards together using characteristics of the JESD204B high speed serial interface between the AD9625 and FPGA.

Clocking
========

The AD-FMCADC3-EBZ provides multiple options for clocking the AD9625. The default configuration of the board clocks the ADC using an on-board 2.5 GHz, low noise, crystal oscillator from Crystek. This oscillator is then routed through a wide band transformer producing the differential clock for the ADC. Alternatively, the oscillator can be disconnected and an external clock source connected by only changing two components on the board. A single ended clock connected to the CLK+ input would then be routed through the transformer in the same way.

Finally, the option exists to connect a differential clock to the board using both the CLK+ and CLK- inputs. Then referencing the schematic make the component changes to directly route the differential input bypassing the transformer.

Front End
=========

The AD-FMCADC3-EBZ uses a passive front end designed for very wide bandwidth. A single ended input needs to be provided to "Ain". A 1:2 impedance ratio broadband balun then converts the input signal differentially to the ADA4961 inputs and has a 1.6GHz bandwidth at -3dB.

Downloads
---------

.. admonition:: Download
   :class: download

   Rev A

   
   `Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/02_039614a.pdf>`_
   
   `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc3-ebz-bom-04152015-new.xlsx>`_
   
   `PCBoard Fab Drawing and Brd File for AllegroFree Viewer <https://wiki.analog.com/_media/resources/eval/user-guides/09_039614a_fab.zip>`_
   
   `PCBoard Gerber files <https://wiki.analog.com/_media/resources/eval/user-guides/20_039614a_cam.zip>`_
   

