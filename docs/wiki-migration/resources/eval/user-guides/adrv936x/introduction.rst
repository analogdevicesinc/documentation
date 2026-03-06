Introduction to boards based on the AD9361/AD9363/AD9364
========================================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361_plus_zed.png
   :align: right
   :width: 300px

There are several high-speed analog modules designed to showcase the :adi:`AD9361` family of high performance, highly integrated RF agile transceivers intended for use in RF applications, such as 3G and 4G base station and software defined radios. Its programmability and wide-band capability make it ideal for a broad range of transceiver applications. The device combines an RF front end with a flexible mixed-signal base-band section and integrated frequency synthesizers, simplifying design-in by providing a configurable digital interface to a processor or FPGA.

The AD9361 and AD9364 chip operates in the 70MHz to 6GHz range, covering most licensed and unlicensed bands. The boards, due to discrete external components may have less performance on some of the RF input/output connectors (for example - the FMCOMMS2 and specific connectors on the FMCOMMS5 are specifically tuned to 2.4GHz). The AD9361 and AD9364 both supports channel bandwidths from less than 200kHz to 56MHz by both changing sample rate, and by changing digital filters, and decimation inside the device itself.

| 

Available AD936x Boards
-----------------------

Overview
~~~~~~~~

+------------------------------------------------------------------+---------------+--------------+---------------------+---------------------+----------------------------------------------------------+-------------------+
| Board                                                            | AD936x Device | Simultaneous | Tx                  | Rx                  | Purpose                                                  | Connector         |
|                                                                  |               | Tx / Rx      | (Ranges)            | (Ranges)            |                                                          |                   |
+==================================================================+===============+==============+=====================+=====================+==========================================================+===================+
| :doc:`ADALM-PLUTO </wiki-migration/university/tools/pluto>`      | 1 x AD9363    | 1 x 1        | 1 (325 - 3800 MHz)  | 1 (325 - 3800 MHz)  | Active Learning Module                                   | Stand Alone (USB) |
+------------------------------------------------------------------+---------------+--------------+---------------------+---------------------+----------------------------------------------------------+-------------------+
| `ADRV9364-Z7020 <https://wiki.analog.com/../adrv9364-z7020>`__   | 1 x AD9364    | 1 x 1        | 1 (70 - 6000 MHz)   | 1 (70 - 6000 MHz)   | Highly Integrated System on Module                       | 4 x FCI           |
+------------------------------------------------------------------+---------------+--------------+---------------------+---------------------+----------------------------------------------------------+-------------------+
| `ADRV9361-Z7035 <https://wiki.analog.com/../adrv936x_rfsom>`__   | 1 x AD9361    | 2 x 2        | 2 (70 - 6000 MHz)   | 2 (70 - 6000 MHz)   | Highly Integrated System on Module                       | 4 x FCI           |
+------------------------------------------------------------------+---------------+--------------+---------------------+---------------------+----------------------------------------------------------+-------------------+
| `AD-FMCOMMS2-EBZ <https://wiki.analog.com/../ad-fmcomms2-ebz>`__ | 1 x AD9361    | 2 x 2        | 2 (2400 - 2500 MHz) | 2 (2400 - 2500 MHz) | Best RF performance in a narrow range                    | FMC-LPC           |
+------------------------------------------------------------------+---------------+--------------+---------------------+---------------------+----------------------------------------------------------+-------------------+
| `AD-FMCOMMS3-EBZ <https://wiki.analog.com/../ad-fmcomms3-ebz>`__ | 1 x AD9361    | 2 x 2        | 2 (70 - 6000 MHz)   | 2 (70 - 6000 MHz)   | Software test and waveform development                   | FMC-LPC           |
+------------------------------------------------------------------+---------------+--------------+---------------------+---------------------+----------------------------------------------------------+-------------------+
| `AD-FMCOMMS4-EBZ <https://wiki.analog.com/../ad-fmcomms4-ebz>`__ | 1 x AD9364    | 1 x 1        | 1 (2400 - 2500 MHz) | 1 (2400 - 2500 MHz) |                                                          | FMC-LPC           |
|                                                                  |               |              | 1 (70 - 6000 MHz)   | 1 (70 - 6000 MHz)   |                                                          |                   |
+------------------------------------------------------------------+---------------+--------------+---------------------+---------------------+----------------------------------------------------------+-------------------+
| `AD-FMCOMMS5-EBZ <https://wiki.analog.com/../ad-fmcomms5-ebz>`__ | 2 x AD9361    | 4 x 4        | 4 (2400 - 2500 MHz) | 4 (2400 - 2500 MHz) | MIMO test platform, can be synchronized in the RF domain | 2 x FMC-LPC       |
|                                                                  |               |              | 4 (70 - 6000 MHz)   | 4 (70 - 6000 MHz)   |                                                          |                   |
+------------------------------------------------------------------+---------------+--------------+---------------------+---------------------+----------------------------------------------------------+-------------------+
| `ARRADIO <https://wiki.analog.com/../arradio>`__                 | 1 x AD9361    | 2 x 2        | 2 (2400 - 2500 MHz) | 2 (2400 - 2500 MHz) | Best RF performance in a narrow range                    | HSMC              |
+------------------------------------------------------------------+---------------+--------------+---------------------+---------------------+----------------------------------------------------------+-------------------+

.. important::

   While the AD9361 digital interface supports both LVDS and CMOS mode, all the FMCOMMS boards have been verified in LVDS mode only. Configuring the digital interface in CMOS mode is not tested nor supported on these platforms. This is due to the purposefully weak CMOS drivers (To keep the noise off the part as much as possible) that are part of the digital interface and the large capacitance of the FMC connector.

   
   If you configure any board to work in CMOS mode, and it does not, this is expected. If it does work, it just means the combination of AD9361 board, AD9361, connectors, carrier layout and FPGA are barely working.
   
   CMOS mode is known to work on platforms without connectors between the AD936x and the Digital BaseBande device (like PicoZed SDR).


AD936x Board Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~

The :doc:`ADALM-PLUTO </wiki-migration/university/tools/pluto>` is just the AD9363 in a 1 x 1 RF configuration with on-board Z7010 FPGA. PlutoSDR is a self contained RF lab in your hand, powered through USB. The board includes a narrow tuning range balun, which is performance optimized for 2.4GHz.

The `ADRV9364-Z7020 <https://wiki.analog.com/../adrv9364-z7020>`__ board is the AD9364 in a 1 x 1 RF configuration with on-board Z7020 FPGA. Hence the features and capabilities of the device extends to the board. The board includes a narrow tuning range balun, which is performance optimized for 2.4GHz. If you want a different range, you can change baluns (footprint compatible options are available). This board has four FCI 0.8mm connectors.

The `ADRV9361-Z7035 <https://wiki.analog.com/../adrv936x_rfsom>`__ board is the AD9361 in a 2 x 2 RF configuration with on-board Z7035 FPGA. Hence the features and capabilities of the device extends to the board. The board includes a narrow tuning range balun, which is performance optimized for 2.4GHz. If you want a different range, you can change baluns (footprint compatible options are available). This board has four FCI 0.8mm connectors.

The `AD-FMCOMMS2-EBZ <https://wiki.analog.com/../ad-fmcomms2-ebz>`__ board is the AD9361 in a 2 x 2 RF configuration. Hence the features and capabilities of the device extends to the board. The board includes a narrow tuning range balun, which is performance optimized for 2.4GHz, and provides datasheet specifications. If you want a different range, you can change baluns (footprint compatible options are available). This board has a FMC connector.

The `AD-FMCOMMS3-EBZ <https://wiki.analog.com/../ad-fmcomms3-ebz>`__ board is the AD9361 in a 2 x 2 RF configuration. Hence the features and capabilities of the device extends to the board. The board includes a wide tuning range RF transformer, which is close to datasheet specifications, but may not meet all specs over the entire 70 - 6000 MHz RF range.

The `AD-FMCOMMS4-EBZ <https://wiki.analog.com/../ad-fmcomms4-ebz>`__ board is the AD9364 in a 1 x 1 RF configuration. Hence the features and capabilities of the device extends to the board. The board includes both a narrow and wide tuning range balun on a multiplexed input/output.

The `AD-FMCOMMS5-EBZ <https://wiki.analog.com/../ad-fmcomms5-ebz>`__ board is two AD9361's in a 4 x 4 RF configuration, which demonstrates how to synchronize multiple devices together. The features and capabilities of the device extends to the board. The board includes both a narrow and wide tuning range baluns on a different SMA connectors.

The `ARRADIO <https://wiki.analog.com/../arradio>`__ board is the AD9361 in a 2 x 2 RF configuration. Hence the features and capabilities of the device extends to the board. The board includes a narrow tuning range balun, which is performance optimized for 2.4GHz, and provides datasheet specifications. If you want a different range, you can change baluns (footprint compatible options are available). This board has an HSMC connector.

Available Carrier Boards
------------------------

.. _overview-1:

Overview
~~~~~~~~

+----------------+-----------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------------------+-----------------------------------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------------------+----------------------------------------------------------+-------------------------------------------------------------------------------+
| Board          | `FMC Carrier <https://wiki.analog.com/../pzsdr/carriers/fmc>`__ | `Breakout Board <https://wiki.analog.com/../pzsdr/carriers/brk>`__ | `PCIe Carrier <https://wiki.analog.com/../pzsdr/carriers/pcie>`__ | `PackRF Carrier <https://wiki.analog.com/../pzsdr/carriers/packrf>`__ | `AC701 <https://www.xilinx.com/AC701>`__ | `KC705 <https://www.xilinx.com/KC705>`__ | `VC707 <https://www.xilinx.com/VC707>`__ | `ZC702 <https://www.xilinx.com/ZC702>`__ | `ZC706 <https://www.xilinx.com/ZC706>`__ | `Zed Board <http://zedboard.org/product/zedboard>`__ | `MITX045 <http://zedboard.org/product/mini-itx-board>`__ | `SoCKit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`__ |
+================+=================================================================+====================================================================+===================================================================+=======================================================================+==========================================+==========================================+==========================================+==========================================+==========================================+======================================================+==========================================================+===============================================================================+
| ADALM-Pluto    |                                                                 |                                                                    |                                                                   |                                                                       |                                          |                                          |                                          |                                          |                                          |                                                      |                                                          |                                                                               |
+----------------+-----------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------------------+-----------------------------------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------------------+----------------------------------------------------------+-------------------------------------------------------------------------------+
| ADRV9364-Z7020 | √                                                               | √                                                                  | √                                                                 | √                                                                     |                                          |                                          |                                          |                                          |                                          |                                                      |                                                          |                                                                               |
+----------------+-----------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------------------+-----------------------------------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------------------+----------------------------------------------------------+-------------------------------------------------------------------------------+
| ADRV9361-Z7035 | √                                                               | √                                                                  | √                                                                 | √                                                                     |                                          |                                          |                                          |                                          |                                          |                                                      |                                                          |                                                                               |
+----------------+-----------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------------------+-----------------------------------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------------------+----------------------------------------------------------+-------------------------------------------------------------------------------+
| FMCOMMS2/3/4   |                                                                 |                                                                    |                                                                   |                                                                       | √                                        | √                                        | √                                        | √                                        | √                                        | √                                                    | √                                                        |                                                                               |
+----------------+-----------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------------------+-----------------------------------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------------------+----------------------------------------------------------+-------------------------------------------------------------------------------+
| FMCOMMS5       |                                                                 |                                                                    |                                                                   |                                                                       |                                          |                                          |                                          |                                          | √                                        | √                                                    |                                                          |                                                                               |
+----------------+-----------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------------------+-----------------------------------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------------------+----------------------------------------------------------+-------------------------------------------------------------------------------+
| Arradio        |                                                                 |                                                                    |                                                                   |                                                                       |                                          |                                          |                                          |                                          |                                          |                                                      |                                                          | √                                                                             |
+----------------+-----------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------------------+-----------------------------------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------+------------------------------------------------------+----------------------------------------------------------+-------------------------------------------------------------------------------+

\*The `ADALM-Pluto <https://wiki.analog.com/../adrv9364-z7020>`__ is a stand alone unit requiring only USB for power and communications.

Carrier Board Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~

Applications
------------

-  Wireless communications demonstration and learning tool
-  Remote radio head
-  Software-defined radio
-  Satellite modems
-  Test and measurement equipment
-  Radar and advanced imaging
-  General purpose data acquisition

Specifications & Features
-------------------------

-  General purpose design suitable for any application
-  Software tunable across wide frequency range (70MHz to 6GHz)
-  Less than 200kHz to 56MHz channel bandwidth
-  Powered from single FMC connector
-  Supports MIMO radio, with less than 1 sample sync on both ADC and DAC
-  Includes schematics, layout, BOM, HDL, Linux drivers and application software
-  Supports add on cards for spectrum specific designs (PA, LNA etc)

   -  :doc:`AD-FREQCVT1-EBZ </wiki-migration/resources/eval/user-guides/ad-freqcvt1-ebz>` is frequency up and down conversion to allow the AD9361 to operate down to 1MHz.
   -  :doc:`AD-TRXBOOST1-EBZ </wiki-migration/resources/eval/user-guides/ad-trxboost1-ebz>` is to add an pre-amp to the TX output and an LNA to the RX input of the AD9361.

-  SPI access for all device registers

Getting started
---------------

The items needed to get started are:

-  :doc:`Quickstart </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`

They detail supported carriers, external equipment requirements and how to set the boot switches.

Once you have a working platform, study this material.

-  :doc:`Introduction </wiki-migration/resources/eval/user-guides/ad9361>` to the AD9361/AD9364
-  :doc:`Tuning </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>` the AD9361/AD9364 FIR Filters for your application
-  How to :doc:`simulate </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>` the part with `MathWorks SimRF <https://www.mathworks.com/hardware-support/analog-devices-rf-transceivers.html>`__, to see if it is appropriate for your application
-  Measuring actual RF performance, either with the :doc:`built in software </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`, or with test equipment
-  How the part performs in specific algorithms, streaming data to :doc:`MATLAB, Simulink </wiki-migration/resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`, or :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
-  How the :doc:`Linux </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>` or :doc:`no-OS </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/no-os-functions>` driver works, or can be integrated into your system
-  Create your own `custom HDL from Simulink <https://www.mathworks.com/hardware-support/zynq-sdr.html>`__ and insert it into the ADI design to see how it works
-  Modifying the :doc:`reference_hdl ADI provided HDL </wiki-migration/resources/fpga/docs/tips>`
-  Tuning other paramters, like :doc:`ACG for your application/waveform </wiki-migration/resources/eval/user-guides/ad9361_agc_tuning>`
-  Review a real world example using the part (ADS-B) :adi:`Part 1 <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`, :adi:`Part 2 <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`, :adi:`Part 3 <library/analogDialogue/archives/49-11/four-step-sdr-03.html>` and :adi:`Part 4 <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`
-  Look at `FMCOMMS2 <https://wiki.analog.com/../ad-fmcomms2-ebz/hardware>`__, `FMCOMMS3 <https://wiki.analog.com/../ad-fmcomms3-ebz/hardware>`__, `FMCOMMS4 <https://wiki.analog.com/../ad-fmcomms4-ebz/hardware>`__, `FMCOMMS5 <https://wiki.analog.com/../ad-fmcomms5-ebz/hardware>`__ schematics and layout to see how to get the best performance in your hardware design.

A detailed list of things that can be done with these boards, can be found in each board page:

-  `ARRADIO <https://wiki.analog.com/../arradio>`__
-  :doc:`ADALM-PLUTO </wiki-migration/university/tools/pluto>`
-  `ADRV9364-Z7020 <https://wiki.analog.com/../adrv9364-z7020>`__
-  `ADRV9361-Z7035 <https://wiki.analog.com/../adrv936x_rfsom>`__
-  `AD-FMCOMMS2-EBZ <https://wiki.analog.com/../ad-fmcomms2-ebz>`__
-  `AD-FMCOMMS3-EBZ <https://wiki.analog.com/../ad-fmcomms3-ebz>`__
-  `AD-FMCOMMS4-EBZ <https://wiki.analog.com/../ad-fmcomms4-ebz>`__
-  `AD-FMCOMMS5-EBZ <https://wiki.analog.com/../ad-fmcomms5-ebz>`__
