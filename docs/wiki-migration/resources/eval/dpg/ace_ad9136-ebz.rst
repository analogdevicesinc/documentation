AD9136/AD9135-EBZ Evaluation Board Quick Start Guide
====================================================

Getting Started with the AD9136/AD9135-EBZ Evaluation Board and Software
------------------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  :adi:`EVAL-AD9135` or :adi:`EVAL-AD9136` Evaluation Board for the :adi:`AD9136`/:adi:`AD9135`
-  Evaluation Board CD
-  Mini-USB Cable

Recommended Equipment List
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  +5Vdc, Power Supply
-  1 Sinusoidal Clock Sources
-  Spectrum Analyzer
-  Data Pattern Generator Series 3 (DPG3)

Introduction
------------

The AD9136/AD9135-EBZ connects to a DPG3 for quick evaluation of the :adi:`AD9136`/:adi:`AD9135`, a high-speed, signal processing Digital to Analog Converter. The DPG3 automatically formats the data and sends it to the AD9136/AD9135-EBZ, simplifying evaluation of the device. The Evaluation Board (EVB) runs from a +5V supply. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, REFCLK and DPG3 input clock. Figure 2 is an image of the top side of the AD9136-EBZ.

AD9136/AD9135 Evaluation Software
---------------------------------

The AD9136/AD9135 Evaluation Board software runs on the easy-to-use ACE (Analysis|Control|Evaluate) graphical user interface (GUI). It is included on the Evaluation Board CD. Registers on the AD9136/AD9135 and AD9516 products are programmed via a USB cable connecting the user’s PC to the AD9144-EBZ XP2 connector. Software in the AD9136-EBZ/AD9135-EBZ PIC processor (XU1) provides the interface between the USB bus and the SPI busses of the AD9136/AD9135 and AD9516.

Hardware Setup
--------------

Connect +5.0V to P5, GND to P6. A low phase noise high frequency clock source should be connected to the SMA connector, J1. This is the DACCLK input. The spectrum analyzer should be connected to the SMA connector, J17. This is the DAC0 output. The evaluation board connects to the DPG3 through the connector P4. The PC should be connected to the EVB using the mini-USB connector XP2 after installation of the Evaluation Board software. Figure 1 shows the block diagram of the set-up.

.. container:: center

   
   +---------------------------------------------------------------+----------------------------------+
   | |image3|                                                      | |image4|                         |
   +---------------------------------------------------------------+----------------------------------+
   | Figure 1. Block diagram of the AD9136/AD9135 lab bench set-up | Figure 2. Top view of AD9136-EBZ |
   +---------------------------------------------------------------+----------------------------------+
   


Getting Started
---------------

The PC software comes on the included Evaluation Board CD, but may also be downloaded from the DPG Web site at http://www.analog.com/dpg. The installation will include the DPG Downloader software as well as all the necessary AD9136/AD9135 files including schematic, board layout, datasheet, AD9136/AD9135 SPI, and other files.

Initial Set-Up
~~~~~~~~~~~~~~

| 1. Install the DPG Downloader and AD9136/AD9135 SPI software and support files on your PC. Follow the instructions in the installation wizard and use the default (recommended) installation settings.
| 2. Use a USB cable to connect the EVB to your PC and connect the lab equipment to the EVB.
| 3. Connect the DGP3 unit to your PC and turn on the unit.

Single-Tone Test
~~~~~~~~~~~~~~~~

| These settings configure the AD9136/AD9135 to output a sine wave using the DPG3 and allow the user to view the single-tone performance at the DAC output, under the condition: Fdata = 1.6GHz, 1X interpolation, 4-carrier WCDMA signal with center frequency = 100MHz.
| === Configure DPG Vector Software === 1. To begin, turn on the external +5V supply.
| 2. Open DPG Downloader if you have not done so. (Start > All Programs > Analog Devices > DPG > DPGDownloader). Ensure that the program detects the AD9136/AD9135, as indicated in the “Evaluation Board” drop-down list, shown in Figure 3.

.. container:: center

   
   +---------------------------------------+
   | |image5|                              |
   +---------------------------------------+

   | Figure 3. Initial DPGDownloader Panel |

   +---------------------------------------+
   
   |


3. Select "QBF 2X4 85G 425M" from the "Port Configuration" drop-down list to configure the DPG for Dual Link and "Mode 8" from the "JESD Mode" drop-down list.
| 3. Click on “Add Generated Waveform”, and then “Wireless Infrastructure”. A WIFR panel will be added to the vector list. Enter the Data Rate, in this case 1.6GHz and the desired frequency, 100MHz. Enter the digital amplitude. In this case we use 0dBFS. Select "2's Complement" from the Number Format drop-down list. Input the center frequency of "100MHz" at the bottom of the panel, choose "WCDMA" from the Standard drop-down menu and increase the No. of Carriers to "4" - then hit the "Add Carriers" button. The DPG Downloader panel should look like Figure 3.
| 4. Select the WIFR vector (I) in the “DAC0” drop down menu and the WIFR vector (Q) in the “DAC1”. At this point, the DPG Downloader panel should look like Figure 4.
|

.. container:: center

   
   +------------------------------------------+
   | |image6|                                 |
   +------------------------------------------+

   | Figure 4. Configured DPGDownloader Panel |

   +------------------------------------------+
   


Configuring SPI
^^^^^^^^^^^^^^^

| 1. Open ACE (Start > All Programs > Analog Devices > ACE). It should recognize the AD9136-EBZ or AD9135-EBZ in the attached hardware section when the application startup screen displays, as showing in Figure 5 for the AD9136-EBZ.
|

.. container:: center

   
   +------------------------------------------------------------------------+
   | |image7|                                                               |
   +------------------------------------------------------------------------+

   | Figure 5. Initial ACE Startup Window with Attached Hardware AD9136-EBZ |

   +------------------------------------------------------------------------+
   


| 2. Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 1.6GHz, and the output level to 3dBm. The spectrum analyzer can be configured with Start Frequency = 1 MHz, Stop Frequency = 800 MHz, and Resolution Bandwidth of 30 kHz, and Trace Detector to Average (Log/RMS/V). Choose Input Attenuation to be 8dB. This can be adjusted later if indications are that the analyzer is causing degradations.
| 3. Follow the sequence below to configure the AD9136-EBZ/AD9135-EBZ Setup Wizard settings.
| a. The Links should be set to dual link. The JESD Mode is set to 8, Interpolation set to 1, and FDAC set to 1.6GHz, as shown in Figure 6.

| b. Hit “Apply” and the wizard will execute a startup routine to configure the AD9516 and the AD9136/AD9135. Once complete, the SERDES PLL lock indicator on the board will turn green if it locked and the display will look like Figure 7.

.. container:: center

   
   +--------------------------------------------------------+
   | |image8|                                               |
   +--------------------------------------------------------+

   | Figure 6. Configured ACE Wizard GUI for the AD9136-EBZ |

   +--------------------------------------------------------+
   
   +------------------------------------------------------------------------+
   | |image9|                                                               |
   +------------------------------------------------------------------------+

   | Figure 7. ACE Wizard Executed and SERDES PLL Locked for the AD9136-EBZ |

   +------------------------------------------------------------------------+
   


4. Return to DPGDownloader and note the Serial Line Rate readback should read 8Gbps indicating that the clocks going to the FPGA are configured properly for this setup, as shown in Figure 8.

| 5. Click Download (|9154_down_arrow.png|) and Play (|9154_right_green_arrow.png|) in the DPGDownloader screen.

.. container:: center

   
   +---------------------------------------------------------+
   | |image10|                                               |
   +---------------------------------------------------------+

   | Figure 8. Executed DPGDownloader GUI for the AD9136-EBZ |

   +---------------------------------------------------------+
   


| The current on the 5V supply should read about 1430mA. If you do not see the output, gently push the board toward the DPG3. This ensures that the board is firmly connected to the DPG3. The four register readbacks on the board view for Code Group Sync, Frame Sync, Good CheckSum and Initial Lane Sync should all read 0x0F indicating the lanes are working correctly, as seen in Figure 7.
| 6. The output spectrum of the DAC should look like Figure 9 below.

.. container:: center

   
   +------------------------------------------------------------+
   | |image11|                                                  |
   +------------------------------------------------------------+

   | Figure 9. AD9136/AD9135-EBZ Eval Board DAC output Spectrum |

   +------------------------------------------------------------+
   


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136/figure_1.png
   :width: 440px
   :height: 260px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136/figure_2.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136/figure_1.png
   :width: 440px
   :height: 260px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136/figure_2.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/AD9136-EBZ_DPGStartup.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/AD9136-EBZ_DPGSetup.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/AD9136-EBZ_ACEStartup.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/ad9136-ebz_ACESetup.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/ad9136-ebz_ACEWizRan.png
   :width: 600px
.. |9154_down_arrow.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_down_arrow.png
.. |9154_right_green_arrow.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_right_green_arrow.png
.. |image10| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/ad9136-ebz_DPGDwnld.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/ad9136_1.6ghzdac_1x_4xwcdma_fout100m_plloff.png
   :width: 600px
