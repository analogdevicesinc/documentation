SPIPRO AD9154-FMC-EBZ Evaluation Board Quick Start Guide
========================================================

Getting Started with the AD9154-FMC-EBZ Evaluation Board and Software
---------------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  :adi:`AD9154-FMC-EBZ` Evaluation Board for ADS7
-  Evaluation Board CD
-  Mini-USB Cable

Recommended Equipment List
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Sinusoidal Clock Source
-  Spectrum Analyzer
-  Oscilloscope
-  Data Pattern Generator with FMC Interface ADS7

Introduction
------------

The AD9154-FMC-EBZ connects to an ADS7 data pattern generator system. The AD9154 is a quad JESD204B signal processing RF Digital to Analog Converter. The ADS7 automatically formats the data and sends it to the AD9154-FMC-EBZ via its JESD204B lanes. The AD9154-FMC-EBZ is an FMC mezzanine card. +12V, +3.3V, and VADJ power supply rails are provided by the ADS7 system via the FMC connector P1. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, JESD204B SYSREF signals, and a GBTCLK clock used by the ADS7. There is also an FMC standard I2C bus that is used by the ADS7 to identify the AD9154-FMC-EBZ. This I2C interface is implemented in firmware in the AD9154-FMC-EBZ PIC processor (XU1). PIC firmware is installed in PIC non-volatile memory by ADI. All ADS7 to/from AD9154-FMC-EBZ interface signals are connected via the FMC connector P1.

AD9154 Evaluation Software
--------------------------

The AD9154 Evaluation Board software runs on the SPIPro graphical user interface (GUI). It is included on the Evaluation Board CD. Registers on the AD9154 and AD9516 products are programmed via a USB cable connecting the user’s PC to the AD9154-FMC-EBZ XP2 connector. Software in the AD9154-FMC-EBZ PIC processor (XU1) provides the interface between the USB bus and the SPI busses of the AD9154 and AD9516.

Hardware Setup
--------------

Figure 1 shows the block diagram of the set-up.

.. container:: center


|image1|

   +--------------------------------------------+

   | Figure 1. AD9154-FMC-EBZ Lab Block Diagram |

   +--------------------------------------------+
   
   .. image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_fmc_figure_2_photo.png
   
   +-------------------------------------------------+

   
   | Figure 2. Top and Bottom view of AD9154-FMC-EBZ |

   +-------------------------------------------------+
   


A low phase noise high frequency clock source should be connected to the SMA connector J1. A spectrum analyzer should be connected to the EVB SMA connector J4. Connect SMA connectors J5, J14 and J17 of the EVB to an oscilloscope. The evaluation board connects to the ADS7 through the connector P1. The PC should be connected to the EVB using the mini-USB connector XP2. Figure 1 shows a block diagram of the set-up.

Getting Started
---------------

The PC software is included in the CD shipped with the EVB. The installation will include the software as well as all the AD9154 EVB files including schematic, board layout, datasheet, this quick start guide and other files.

Initial Set-Up
~~~~~~~~~~~~~~

| 1. Install the customer evaluation board software and support files, including DPGDownloader and SPIPro GUI on your PC. Follow the instructions in the installation wizard and use the default (recommended) installation settings.
| 2. Plug the AD9154-FMC-EBZ into port FMC_1 of the ADS7 System. Use a USB cable to connect the EVB to your PC and connect the lab equipment to the EVB as shown in Figure 1.
| 3. Connect the ADS7 unit to your PC via USB and turn on the ADS7.
| 4. Connect SMA connector J5 to a spectrum analyzer, connect SMA connectors J17, J4 and J14 to an oscilloscope.

Single Tone Demonstration
~~~~~~~~~~~~~~~~~~~~~~~~~

Single Tone Demo Lab Bench Configuration Procedure:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These settings configure the AD9154 to output a 181Mhz 0dbFS sine wave using the ADS7 on all four AD9154 DACs.

- Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 1500MHz, and the output level to 3dBm. The spectrum analyzer can be configured as shown in Figure 8 with a resolution bandwidth of 300kHz. Choose an Input Attenuation of 22dB.

.. container:: center

   
   .. image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/9154_fmcfigure_6_start_dpg.png
   
   +----------------------------------------+

   
   | Figure 3. Initial DPG Downloader Panel |

   +----------------------------------------+
   


Single Tone Demo Hardware and Software Start Up Procedure:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| 1. Run DPG Downloader from Start->Analog Devices->DPG->DPG Downloader. The DPG Downloader GUI will say Evaluation Board: AD9154 and Port Configuration: JESD204B as shown in Figure 3. At this point, the ADS7 FMC power supplies will be turned on.
|

<WRAP center> 2. Open SPIPro from Start->Analog Devices->AD9154->AD9154 SPI. It will say AD9154-FMC-EBZ in the upper left hand corner.


| 3. Select single link, JESD mode 0, Interpolation 2. Leave all other settings in their default state. Press ‘Configure DAC and Clock’ button. JESD204B PLL lock will turn green.
|

.. container:: center


|image2|

   +-------------------------------------------+

   | Figure 4. Fully Configured SPIPro Display |

   +-------------------------------------------+
   


4. In DPG Downloader Window Select Single Tone under the Add Generated Waveforms Tab. Set Data Rate: 750Mhz, Desired Frequency: 181Mhz, Amplitude: 0dbFS, Uncheck Unsigned Data, Check Generate Complex Data (I&Q)

5. Select JESD Mode: Mode 0

6. Populate the data playback selections for each DAC output as shown in Figure 5.

7. Click Download button and click Play button. The signals shown in figures 7 and 8 will appear on the DAC outputs (J17, J4, J5, and J14), Serial Line Rate will be 7.5Gbps. The green SYNC check mark indicates that the JESD204B link running.

.. container:: center


|image3|

   +------------------------------------------------------------------+

   | Figure 5. AD9154-FMC-EBZ Fully Configured DPG Downloader Display |

   +------------------------------------------------------------------+
   


| 8. Here’s what you will see on DAC0, DAC1, and DAC3 on the scope

.. container:: center


|image4|

   +-------------------------------------+

   | Figure 6. DAC Outputs Scope Display |

   +-------------------------------------+
   
   9. Here is what you will see at the output of DAC2 on the Spectrum Analyzer.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_fmc_figure_9_sa_1.png
   
   +------------------------------------------------+

   
   | Figure 7. DAC Output Spectrum Analyzer Display |

   +------------------------------------------------+
   


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154fmc_figure_1_lab_block_diagram.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/9154_fmcfigure_4_ad9154_spi.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_fmcfigure_7_configured_dpgdownlaoder.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_fmcfigure_8_scope_1.png
