AD9152-ADRF6720-EBZ Evaluation Board Quick Start Guide
======================================================

Getting Started with the AD9152-ADRF6720-EBZ Evaluation Board and Software
--------------------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  :adi:`AD9152-ADRF6720-EBZ <AD9152>` Evaluation Board
-  Evaluation Board CD
-  Mini-USB Cable

Recommended Equipment List
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  +5Vdc, Power Supply
-  2 Sinusoidal Clock Sources
-  Spectrum Analyzer
-  Data Pattern Generator Series 3 (DPG3)

Introduction
------------

The AD9152-ADRF6720-EBZ connects to a DPG3 for quick evaluation of the :adi:`AD9152`, a high-speed, signal processing Digital to Analog Converter. The DPG3 automatically formats the data and sends it to the AD9152-ADRF6720-EBZ, simplifying evaluation of the device. The Evaluation Board (EVB) runs from a +5V supply. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, REFCLK and DPG3 input clock. Figure 2 is an image of the top side of the AD9152-ADRF6720-EBZ.

AD9152-ADRF6720 Evaluation Software
-----------------------------------

The AD9152-ADRF6720 Evaluation Board software has an easy-to-use graphical user interface (GUI). It is included on the Evaluation Board CD, or can be downloaded from the DPG website at http://www.analog.com/dpg. This will install DPGDownloader (for generating and loading vectors into the DPG3) and AD9152-ADRF6720 SPI software.

Hardware Setup
--------------

Connect +5.0V to P5, GND to P6. A low phase noise high frequency clock source should be connected to the SMA connector, J1. This is the DACCLK input. The spectrum analyzer should be connected to the SMA connector, J17/J4 They are the DAC0 output. The External LO should be connected to the SMA connector of J18. The evaluation board connects to the DPG3 through the connector P4. The PC should be connected to the EVB using the mini-USB connector XP2 after installation of the Evaluation Board software. Figure 1 shows the block diagram of the set-up.

.. container:: center

   
   +-----------------------------------------------------------------+-------------------------------------------+
   | |image3|                                                        | |image4|                                  |
   +-----------------------------------------------------------------+-------------------------------------------+
   | Figure 1. Block diagram of the AD9152-ADRF6720 lab bench set-up | Figure 2. Top view of AD9152-ADRF6720-EBZ |
   +-----------------------------------------------------------------+-------------------------------------------+
   


Getting Started
---------------

The PC software comes on the included Evaluation Board CD, but may also be downloaded from the DPG Web site at http://www.analog.com/dpg. The installation will include the DPG Downloader software as well as all the necessary AD9152-ADRF6720 files including schematic, board layout, datasheet, AD9152-ADRF6720 SPI, and other files.

Initial Set-Up
~~~~~~~~~~~~~~

| 1. Install the DPG Downloader and AD9152-ADRF6720 SPI software and support files on your PC. Follow the instructions in the installation wizard and use the default (recommended) installation settings.
| 2. Use a USB cable to connect the EVB to your PC and connect the lab equipment to the EVB.
| 3. Connect the DGP3 unit to your PC and turn on the unit.

Single-Tone Test
~~~~~~~~~~~~~~~~

| These settings configure the AD9152_6720 to output a sine wave using the DPG3 and allow the user to view the single-tone performance at the Mod output, under the condition: Fdata = 375MHz, 4X interpolation, IF = 200MHz, LO = 2GHz (external).

Configure DPG Vector Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. To begin, turn on the external +5V supply.

2. Open DPG Downloader if you have not done so. (Start > All Programs > Analog Devices > DPG > DPGDownloader). Ensure that the program detects the AD9152-ADRF6720, as indicated in the “Evaluation Board” drop-down list, and select it.

3. Set “Port configuration” to “2X4 37G 187M ” in the DPG Downloader panel and select Mode 4 in the JESD Mode drop-down box.

4. Click on “Add Generated Waveform”, and then “Single Tone”. A Single Tone panel will be added to the vector list. Enter the Data Rate, in this case 350MHz and the desired frequency, 100MHz. Enter the digital amplitude. In this case we use -10dBFS. Uncheck the “Unsigned Data” box, check the “Generate complex data (I & Q)”, as in Figure 3.


| 5. Select the data vector of 100MHz desired frequency ’in-phase’ data in the “DAC0” drop down menu and the ‘Quadrature’ data in the “DAC1”. At this point, the DPG Downloader panel should look like Figure 3.
|

.. container:: center

   
   +--------------------------------+
   | |image5|                       |
   +--------------------------------+

   | Figure 3. DPG Downloader Panel |

   +--------------------------------+
   


Configuring SPI
^^^^^^^^^^^^^^^

| 1. Open the AD9152 SPI application (Start > All Programs > Analog Devices > AD9152 > AD9152 SPI). The screen should look similar to Figure 4.
|

.. container:: center

   
   +----------+
   | |image6| |
   +----------+
   
   +---------------------------------------------------+

   
   | Figure 4. Entry Screen of the AD9152 SPI software |

   +---------------------------------------------------+
   


| 2. Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 1.5GHz, and the output level to +3dBm. The spectrum analyzer can be configured with Start Frequency = 10 MHz, Stop Frequency = 1.5GHz, and Resolution Bandwidth of 30 kHz. Choose Input Attenuation to be 10dB. This can be adjusted later if indications are that the analyzer is causing degradations.
| 3. Follow the sequence below to configure the AD9152 SPI registers.

| a. The Links should be set to single link. The JESD Mode is set to 4, Interpolation set to 4, and FDAC set to 1.5GHz. Click “Commit” button to initialize the AD9152. The JESD204B PLL should be locked indicated with bright green JESD204B PLL readback LED.
| b. . At this point the data clock frequency on the LED panel of the DPG3 should read 187MHz and the Serial Line Rate in the DPG3 software panel should read 3.75Gbps.
| c. Click “Read All Registers” in the top menu bar. You should see “JESD204B PLL Lock Readback” LED readback is bright green indicating that the SERDES PLL is locked.

.. container:: center

   
   +----------+
   | |image7| |
   +----------+
   
   +---------------------------------------------------+

   
   | Figure 5. Entry Screen of the AD9152 SPI software |

   +---------------------------------------------------+
   


| d. Click Download (|image8|) and Play (|image9|) in the DPG Downloader screen.

e. Configure the ADRF6720 by a startup sequence, Select “ Restore Registers from File” in the “File” menu, then Select the file called ADRF6720_PLLoff_for_AD9152_6720_evb.csv. See Figure6.

.. container:: center

   
   +-------------------------------------------------+
   | |image10|                                       |
   +-------------------------------------------------+

   | Figure 6. AD9152-EBZ Eval Board output Spectrum |

   +-------------------------------------------------+
   


| f. The current on the 5V supply should read about 1479mA. If you do not see the output, gently push the board toward the DPG3. This ensures that the board is firmly connected to the DPG3. The four registers codeGrpSync, FrameSync, GoodCheckSum and Initial LaneSync should all read 0F indicating the lanes are working correctly. The output should appear as Figure 7.

.. container:: center

   
   +----------------------------------------------------------+
   | |image11|                                                |
   +----------------------------------------------------------+

   | Figure 7. AD9152-ADRF6720 EBZ Eval Board output Spectrum |

   +----------------------------------------------------------+
   


Note
~~~~

| In single link JESD204B mode 4,5,6,7,9,10, the Serdes line cross-bar setting as shown below, are added in this software to match the data mapping the DPG3 requires. They are not required if the data source is not a DPG3.
| write(0x308,0x08)
| write(0x309,0x1A)

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9152/ad9152-6720-ebz_system1.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9152/AD9152-6720-EBZ_photo.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9152/ad9152-6720-ebz_system1.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9152/AD9152-6720-EBZ_photo.png
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9152/dpg_downloader_pane1.png
   :width: 800px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9152/ad9152_spipro0.png
   :width: 800px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9152/ad9152_spirpro1.png
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/image009.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/image010.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9152/ad9152-6720_6720_cfg_download.png
   :width: 800px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9152/ad9152-6720-ebz_rf_output.png
   :width: 600px
