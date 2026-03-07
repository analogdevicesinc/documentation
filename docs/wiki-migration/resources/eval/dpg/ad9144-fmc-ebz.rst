AD9144-FMC-EBZ Evaluation Board Quick Start Guide
=================================================

Getting Started with the AD9144-FMC-EBZ Evaluation Board and Software
---------------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  :adi:`AD9144-FMC-EBZ` Evaluation Board for ADS7
-  Evaluation Board CD
-  Mini-USB Cable

Recommended Equipment List
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Sinusoidal Clock Sources
-  Spectrum Analyzer
-  Oscilloscope
-  Data Pattern Generator ADS7

Introduction
------------

The AD9144-FMC-EBZ connects to an ADS7 data pattern generator system. The AD9144 is a quad JESD204B signal processing RF Digital to Analog Converter. The ADS7 automatically formats the data and sends it to the AD9144-FMC-EBZ via its JESD204B lanes. The AD9144-FMC-EBZ is an FMC mezzanine card. +12V, +3.3V, and VADJ power supply rails are provided by the ADS7 system via the FMC connector P1. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, JESD204B SYSREF signals, and a GBTCLK clock used by the ADS7. There is also an FMC standard I2C bus that is used by the ADS7 to identify the AD9144-FMC-EBZ. This I2C interface is implemented in software in the AD9144-FMC-EBZ PIC processor (XU1). All ADS7 to/from AD9144-FMC-EBZ interface signals are connected via the FMC connector P1.

AD9144 Evaluation Software
--------------------------

The AD9144 Evaluation Board software runs on the easy-to-use SPIPro graphical user interface (GUI). It is included on the Evaluation Board CD. Registers on the AD9144 and AD9516 products are programmed via a USB cable connecting the user’s PC to the AD9144-FMC-EBZ XP2 connector. Software in the AD9144-FMC-EBZ PIC processor (XU1) provides the interface between the USB bus and the SPI busses of the AD9144 and AD9516.

Hardware Setup
--------------

Connect +5.0V to P5, GND to P6. A low phase noise high frequency clock source should be connected to the SMA connector, J1. This is the DACCLK input. The spectrum analyzer should be connected to the SMA connector, J4. A +1.0V power supply must be connected to the VTT probe point near SMA connector J9, along with a GND connection to the GND probe point next to it. The evaluation board connects to the DPG3 through the connectors P4. The PC should be connected to the EVB using the mini-USB connector XP2 after installation of the Evaluation Board software. Figure 1 shows the block diagram of the set-up.

.. container:: center

   |image1| |image2|

   
   +---------------------------------------------------------+-------------------------------------------------+
   | Figure 1. Block diagram of the FMC-EBZ lab bench set-up | Figure 2. Top and Bottom view of AD9144-FMC-EBZ |
   +---------------------------------------------------------+-------------------------------------------------+
   


A low phase noise high frequency clock source should be connected to the SMA connector J1. A spectrum analyzer should be connected to the SMA connector J4. J5, J14 and J17 of the EVB should be connected to an oscilloscope. The evaluation board connects to the ADS7 through the connector P4. The PC should be connected to the EVB using the mini-USB connector XP2 after installation of the Evaluation Board software. Figure 1 shows a block diagram of the set-up.

Getting Started
---------------

The PC software is included in the CD shipped with the EVB. The installation will include the DPG Downloader software as well as all the necessary AD9144 files including schematic, board layout, datasheet, and other files.

Initial Set-Up
~~~~~~~~~~~~~~

| 1. Install the DPG Downloader and SPIPro software and support files on your PC. Follow the instructions in the installation wizard and use the default (recommended) installation settings.
| 2. Plug the AD9144-FMC-EBZ into port FMC_1 of the ADS7 System. Use a USB cable to connect the EVB to your PC and connect the lab equipment to the EVB as shown in Figure 1.
| 3. Connect the ADS7 unit to your PC via USB and turn on the ADS7.

Single-Tone Demonstration
~~~~~~~~~~~~~~~~~~~~~~~~~

| These settings configure the AD9144 to output a sine wave using the DPG3 and allow the user to view the single-tone performance at the DAC output, under the condition: Fdata = 368.64MHz, 4X interpolation, IF = 20MHz.
| === Single Tone Demo Lab Bench Configuration Procedure:=== These settings configure the AD9144 to output a 112Mhz -1dbFS sine wave using the ADS7 on all four AD9144 DACs.

- Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 1500MHz, and the output level to 3dBm. The spectrum analyzer can be configured as shown in Figure 8 with a resolution bandwidth of 100kHz. Choose an Input Attenuation of 24dB.


| - On your lab computer, open the SPIPro application (Start > All Programs > Analog Devices > AD9144 > SPIPro). You will see the GUI shown in Figure 5 come up.
|

.. container:: center


   ..

|image3|

   +----------------------------------------+

   | Figure 3. Initial DPG Downloader Panel |

   +----------------------------------------+
   


Single Tone Demo Hardware and Software Start Up Procedure:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| 1. Run DPG Downloader. It will say AD9144 as shown in Figure 3
| 2. Execute Port Configuration ‘Below 7.5Gbps’. This will turn on the ADS7 FMC power supplies that power the FMC EVB.
|

.. container:: center


   ..

|image4|

   +-----------------------------------------+

   | Figure 4. DPG Downloader Display Step 2 |

   +-----------------------------------------+
   
   |


3. Open SPIPro. It will say AD9144-FMC-EBZ in the upper left hand corner.



| 4. Select single link, JESD mode 0, Interpolation 2. Press ‘Configure DAC and Clock’ button. JESD204B PLL lock will turn green.
|

.. container:: center


   ..

|image5|

   +-------------------------------------------+

   | Figure 5. Fully Configured SPIPro Display |

   +-------------------------------------------+
   
   |


5. Select Single Tone under the Add Generated Waveforms Tab. Set Data Rate: 750Mhz, Desired Frequency: 112Mhz, Amplitude: -1dbFS, Uncheck Unsigned Data, Check Generate Complex Data (I and Q)
| 6. Populate the data playback selections as shown in Figure 6.
| 7. Click Download ( ) and Play ( ). The spectrum in figure 7 will appear on all 4 DAC outputs (J17, J4, J5, and J14), Serial Line Rate will be 7.5Gsps.

.. container:: center


   ..

|image6|

   +------------------------------------------------------------------+

   | Figure 6. AD9144-FMC-EBZ Fully Configured DPG Downloader Display |

   +------------------------------------------------------------------+
   


| 8. Here’s what you will see on DAC0, DAC1, and DAC3 on the scope

.. container:: center


   ..

|image7|

   +-------------------------------------+

   | Figure 7. DAC Outputs Scope Display |

   +-------------------------------------+
   
   9. Here is what you will see at the output of DAC2 on the Spectrum Analyzer.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_8_ad9144_fmc_ebz_spectrum_capture_1.png
   
   +------------------------------------------------+

   
   | Figure 8. DAC Output Spectrum Analyzer Display |

   +------------------------------------------------+
   


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_1_ad9144_fmc_ebz_lab_bench_set-up.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_2_ad9144_fmc_ebz_board_photo.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_3_ad9144_fmc_ebz_dp3_gui_initial.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_4_ad9144_fmc_ebz_initial_dpg_downloader_.png
   :width: 900px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_5_ad9144_fmc_ebz_spipro_gui.png
   :width: 900px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_6_ad9144_fmc_ebz_dp3_gui.png
   :width: 900px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_7_ad9144_fmc_ebz_scope_capture.png
