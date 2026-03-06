AD-FMCADC7-EBZ FMC Board
========================

Introduction
------------

The :adi:`AD-FMCADC7-EBZ` is a high speed single channel data acquisition board featuring the :adi:`AD9625` a single channel differential Analog-to-Digital converter at 2.5 GHz and an :adi:`ADL5567` dual channel differential 4.8 GHz amplifier. This is an FMC compatible board. The clocking can be done three different ways including external variations and on-board variations with Crystek oscillator and an :adi:`ADF4355-2`.

ADI also provides reference designs (HDL and software) for this board to work with commonly available Altera and Xilinx development boards.

Hardware
--------

The AD-FMCADC7-EBZ board's primary purpose is to demonstrate the capabilities of the devices on board quickly and easily by providing a seamless interface to an FMC carrier platform and running the reference design on the carrier FPGA. The board is designed to self power and self clock when connected to the FMC carrier. The analog signals ( AIN+ and AIN-) are connected to J202 and J201. This rapid prototyping board is default set up with to utilize input J202 for a single-ended connection from a signal generator.

Devices
~~~~~~~

The FMC board includes the following products by Analog Devices:

-  :adi:`ADR280ARTZ <ADR280>` 1.2 V Ultralow Power High PSRR Voltage Reference
-  :adi:`AD9625BBPZ-2.5 <AD9625>` 12-Bit, 2.5 GSPS, 1.3 V/2.5 V Analog-to-Digital Converter
-  :adi:`ADL5567ACPZ <ADL5567>` 4.8 GHz Ultrahigh Dynamic Range, Dual Differential Amplifier
-  :adi:`ADF4355-2BCPZ` Microwave Wideband Synthesizer with Integrated VCO
-  :adi:`AD7291BCPZ` 8-Channel, I2C, 12-Bit SAR ADC with Temperature Sensor
-  :adi:`ADP1753ACPZ` 0.8 A, Low VIN, Low Dropout Linear Regulator
-  :adi:`ADP7104ARDZ-R7` 20 V, 500 mA, Low Noise, CMOS LDO
-  :adi:`ADP1741ACPZ` 2 A, Low VIN, Low Dropout Linear Regulator
-  :adi:`ADP2119ACPZ <ADP2119>` 2 A/1.25 A, 1.2 MHz, Synchronous, Step-Down DC-to-DC Regulator
-  :adi:`ADP2442ACPZ <ADP2442>` 36 V,1 A, Synchronous, Step-Down, DC-to-DC Regulator with

   -  External Clock Synchronization

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc7-top.jpg
   :align: center
   :width: 200px

::

                                                    Top View

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc7-bot.jpg
   :align: center
   :width: 200px

::

                                                    Bottom View

Clocking
~~~~~~~~

The AD-FMCADC7-EBZ includes various clocking options:

-  2.5GHz Crystek on-board oscillator, Y401, to a differential balun which connects directly to the converter's clock input pins.
-  An external reference supplied at J301 to use in conjunction with the ADF4355-2.
-  122.88MHz Crystek on-board oscillator reference to the ADF4355-2

Analog Front End
~~~~~~~~~~~~~~~~

The AD-FMCADC7-EBZ uses a active front end designed for very wide bandwidth. A single ended input needs to be provided to the analog inputs at -15dBm. The broadband amplifier gains and converts the analog input signal deferentially to the converter's inputs and has a 1.8GHz bandwidth at -3dB. The amplifier's gain can be adjusted independently with some simple resistor modifications.

Revision B
~~~~~~~~~~

The revision B board is default set for the amplifier to be at max gain with dc coupling. Hardware changes are required to change either the gain or dc coupling to ac coupling.

Downloads (Hardware)
--------------------

.. admonition:: Download
   :class: download

   
   Rev B:
   
   -  `20_040403b_artwork.zip <https://wiki.analog.com/_media/resources/eval/user-guides/20_040403b_artwork.zip>`__\ \| Gerber files}}
   -  `Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/ad_fmcadcv7b.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadcv7b-ebz_bom-12142015-final.xls>`__
   

