AD9144-ADRF6720-EBZ Evaluation Board Quick Start Guide
======================================================

Getting Started with the AD9144-ADRF6720-EBZ Evaluation Board and Software
--------------------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  AD9144-ADRF6720-EBZ Evaluation Board Rev 2
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

The AD9144-ADRF6720-EBZ Evaluation board (13016 Rev B)(SAP part number AD9144-M6720-EBZ) connects to a DPG3 for quick evaluation of the AD9144(a high-speed, signal processing Digital to Analog Converter) and the ADRF6720 (Analog Quadrature Modulator with integrated PLL) combined performance. The Evaluation board include the AD9144 +two ADRF6720 AQMs to make two seperate TX paths output on SMA's J4 and J14.The DPG3 automatically formats the data and sends it to the AD9144-ADRF6720-EBZ, simplifying evaluation of the device. The Evaluation Board (EVB) runs from a +5V supply. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, REFCLK and DPG3 input clock.Figure 2 is an image of the top side of the AD9144-ADRF6720-EBZ.

AD9144 Evaluation Software
--------------------------

The AD9144 Evaluation Board software has an easy-to-use graphical user interface (GUI). It is included on the Evaluation Board CD, or can be downloaded from the DPG website at http://www.analog.com/dpg. This will install DPGDownloader (for generating and loading vectors into the DPG3) and AD9144 SPI software.

Hardware Setup
--------------

Connect +5.0V to P5, GND to P6. One low phase noise high frequency clock source should be connected to the SMA connector, J1. J1 is the clock input of the AD9516, whose outputs feed into the DAC and the DPG3. The other low phase noise high frequency clock source should be connected to the SMA connector, J18 (the ADRF6720-1 LO input), and the spectrum analyzer should be connected to the SMA connector, J4 (the ADRF6720-1 RF1 output) or J14 (the ADRF6720-2 RF2 output) . The default settings for ADRF6720-1 feeds the LO to the other AQM ADRF6720-2. The evaluation board connects to the DPG3 through the connectors P4. The PC should be connected to the EVB using the mini-USB connector XP2 after installation of the Evaluation Board software. Figure 1 shows the block diagram of the set-up.

.. container:: center

   
   +--------------------------------------------------------+-------------------------------------------+
   | |image3|                                               | |image4|                                  |
   +--------------------------------------------------------+-------------------------------------------+
   | Figure 1. Block diagram of the AD9144 lab bench set-up | Figure 2. Top view of AD9144-ADRF6720-EBZ |
   +--------------------------------------------------------+-------------------------------------------+
   


Getting Started
---------------

The PC software comes on the included Evaluation Board CD, but may also be downloaded from the DPG Web site at http://www.analog.com/dpg. The installation will include the DPG Downloader software as well as all the necessary AD9144 files including schematic, board layout, datasheet, AD9144 SPI, and other files.

Initial Set-Up
~~~~~~~~~~~~~~

| 1. Install the DPG Downloader and AD9144 SPI software and support files on your PC. Follow the instructions in the installation wizard and use the default (recommended) installation settings.
| 2. Use a USB cable to connect the EVB to your PC and connect the lab equipment to the EVB.
| 3. Connect the DGP3 unit to your PC and turn on the unit.

Single-Tone Test with DAC PLL used
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| These settings configure the AD9144 to output a sine wave using the DPG3 and allow the user to view the single-tone performance at the IQMOD output, under the condition: Fdata = 500MHz, 4X interpolation, REFCLK = 250MHz Input signal = 70MHz,Nco =100MHz LO = 1000MHz, RF = 1170MHz.

Configure the DPG Downloader Vector Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| 1. To begin, turn on the external +5V supply.
| 2. Open DPG Downloader if you have not done so. (Start > All Programs > Analog Devices > DPG > DPGDownloader). Ensure that the program detects the AD9144, as indicated in the “Evaluation Board” drop-down list and select the "QBF 2X4 5G 250M" option from the "Port Configuration" drop-down list. The “Serial Line Rate” window will show the incorrect clock rate until after the SPI software has been started; then it will change to the correct frequency. The DPG Downloader panel should look like Figure 3.
|

.. container:: center

   
   +--------------------------------+
   | |image5|                       |
   +--------------------------------+

   | Figure 3. DPG Downloader Panel |

   +--------------------------------+

   | 3. Click on “Add Generated Waveform”, and then “Single Tone”. As shown in Figure 4, a Single Tone panel will be added to the vector list. Enter the sample rate, in this case 500MHz and the desired frequency, 70MHz. Enter the digital amplitude. In this case we use -4dBFS. Check the “Generate Complex Data (I & Q)” box and uncheck the “Unsigned Data” box. Select the In-Phase data vector in the “DAC0” and “DAC2” drop down menu and the Quadrature data vector in the “DAC1” and “DAC3”. Be sure to select the appropriate JESD Mode from the drop-down list ("Mode 4" for this example) that will match what is being set in the AD9144 through the SPI program.
|

.. container:: center

   
   +------------------------------------------+
   | |image6|                                 |
   +------------------------------------------+

   | Figure 4. DPG Downloader sinewave vector |

   +------------------------------------------+
   


| 4. Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 500MHz for AD9516 clock input (divides down to 250MHz for the RefClk frequency), and the output level to 3dBm. Set the frequency of the LO clock signal generator to 1GHz, and the output level to 6dBm. The spectrum analyzer can be configured with Center Frequency = 1.11GHz, Span = 400 MHz, and Resolution Bandwidth of 30 kHz. Choose Input Attenuation to be 24dB. This can be adjusted later if indications are that the analyzer is causing degradations.

Configure the SPI Software
^^^^^^^^^^^^^^^^^^^^^^^^^^

| 1. Open the AD9144-6720 SPI application (Start > All Programs > Analog Devices > AD9144 > AD9144 SPI). The screen should look similar to Figure 5.
|

.. container:: center

   
   +----------+
   | |image7| |
   +----------+
   
   +---------------------------------------------------+

   
   | Figure 5. Entry Screen of the AD9144 SPI software |

   +---------------------------------------------------+
   


| 2. Follow the sequence below to configure the AD9144 SPI registers.
| a. Open the AD9144 customer SPI software and go to the Quick Start tab. (See Figure 5.) The parameters in the top left corner need to be selected in the Quick Start List in the panel. The Links should be set to dual link, mode (which is the interface mode) set to 4, Subclass 1 box checked, Interpolation set to 4, the DAC PLL box checked, REFCLK = 250MHz Fin =500MHz and FDAC set to 2GHz.
| b. Click the “Configure DAC and Clock” button to initialize the AD9144. The JESD204B PLL lock should show PLL is locked, and the PLL Lock light should be bring green indicating the DAC PLL is also locked.
| c. Click the “Read All Registers” button in the top menu bar.
| d. The four registers "codeGrpSync, FrameSync, GoodCheckSum and Initial LaneSync" should all read 0F indicating the lanes are working correctly. The code will be different than 0F for other interface modes.At this point the "Serial Line Rate" readback on the DPG3 panel should read 5Gbps.
| e. Click Download (|image8|) and Play (|image9|) in the DPG Downloader screen.
| f. Configure the ADRF6720 modulators by selecting the "Restore Registers from File" button on the top right. Then select the "ADRF6720.csv" file from the pop-up browser window (should be located in the directory under "C:\\Program Files (x86)\\Analog Devices\\HSDAC\\AD9144\\SPIPro").
| g. For the "Select Sideband" control choose "Upper" on the Quick Start tab so that the output places the fout above the LO frequency.

| 3. Once all the steps have been completed up to this point, the SPI software program should look like Figure 6.
|

.. container:: center

   
   +-----------+
   | |image10| |
   +-----------+
   
   +------------------------------------------------------+

   
   | Figure 6. AD9144-ADRF6720 SPI Software Program Setup |

   +------------------------------------------------------+

   | 4. The current on the 5V supply should read about 2200mA. If you do not see the output, gently push the board toward the DPG3. This ensures that the board is firmly connected to the DPG3.
|

.. container:: center

   
   +-----------+
   | |image11| |
   +-----------+
   
   +------------------------------------------------------+

   
   | Figure 7. AD9144-ADRF6720 Eval Board output Spectrum |

   +------------------------------------------------------+
   


Single-Tone Test with NCO used
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 1. In the AD9144 customer SPI software go to the Quick Start tab. Set the FDAC to 2GHz and selecting the shift frequency, for this example we will use -50MHz. Select "Fine (uses FTW)" from the "Modulation Type" drop-down list, the NCO FTW will change from 00000 to F99999999998. Next click the ftw undate req button, the ftw update light should turn bring green at this point. See Figure 7. The analyzer spectrum shows the tone at 120MHz from the Lo frequency shown in Figure 8.
|

.. container:: center

   
   +------------------------------------+
   | |image12|                          |
   +------------------------------------+

   | Figure 7. SPI Panel set up for NCO |

   +------------------------------------+
   


.. container:: center

   
   +----------------------------------------+
   | |120mhz_tone_using_50mhznco_shift.png| |
   +----------------------------------------+
   
   +--------------------------------------------------------------------+

   
   | Figure 8. AD9144-ADRF6720 Eval Board output Spectrum with NCO used |

   +--------------------------------------------------------------------+
   


| 

Note
~~~~

| In single link JESD204B mode 2 through 10, four additional register writes, as shown below, are added in this software to match the data mapping the DPG3 requires. They are not required if the data source is not a DPG3.
| write(0x308,0x2c)
| write(0x309,0x3e)
| write(0x30A,0x08)
| write(0x30B,0x1a)

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_1.png
   :width: 440px
   :height: 260px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_2.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_1.png
   :width: 440px
   :height: 260px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_2.png
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/ad9144-adrf6720-ebz_dpg_downloader.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/ad9144-adrf6720-ebz_dpg_downloader_final.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/ad9144-adrf6720-ebz_initialviewp.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/image009.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/image010.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/ad9144-adrf6720-ebz_finalsetup_nonco.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/dpg/70mhz_tone_lo_1ghz.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/ad9144-adrf6720-ebz_finalsetup_withnco.png
   :width: 600px
.. |120mhz_tone_using_50mhznco_shift.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/120mhz_tone_using_50mhznco_shift.png
   :width: 600px
