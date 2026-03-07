AD9136/AD9135-EBZ Evaluation Board Quick Start Guide
====================================================

Getting Started with the AD9136/AD9135-EBZ Evaluation Board and Software
------------------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  :adi:`AD9135-EBZ` or :adi:`AD9136-EBZ` Evaluation Board
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

The AD9136/AD9135-EBZ connects to a DPG3 for quick evaluation of the :adi:`AD9136-EBZ` or :adi:`AD9135-EBZ`, a high-speed, signal processing Digital to Analog Converter. The DPG3 automatically formats the data and sends it to the AD9136/AD9135-EBZ, simplifying evaluation of the device. The Evaluation Board (EVB) runs from a +5V supply. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, REFCLK and DPG3 input clock. Figure 2 is an image of the top side of the AD9136-EBZ.

AD9136/AD9135 Evaluation Software
---------------------------------

The AD9136/AD9135 Evaluation Board software has a legacy easy-to-use graphical user interface (GUI) included with the DPGDownloader. It is included on the Evaluation Board CD, or can be downloaded from the DPG website at http://www.analog.com/dpg. This will install DPGDownloader (for generating and loading vectors into the DPG3) and AD9136/AD9135 SPI software. However, ACE, or Analysis|Control|Evaluation, is the preferred evaluation software over the SPI software. ACE is included on the Evaluation Board CD or can be downloaded from https://wiki.analog.com/resources/tools-software/ace. The ACE plug-in for the AD9136/AD9135 is available in the software section of the eval website for both the :adi:`EVAL-AD9135` and :adi:`EVAL-AD9136`.

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

The PC software comes on the included Evaluation Board CD, but may also be downloaded from the DPG Web site at http://www.analog.com/dpg and the ACE website at https://wiki.analog.com/resources/tools-software/ace. The installation will include the DPG Downloader software as well as all the necessary AD9136/AD9135 files including schematic, board layout, datasheet, AD9136/AD9135 SPI, and other files. The ACE installation will include the necessary evaluation software, which is preferred over the DPGDownloader GUI. The following set-up describes how to use either ACE or the legacy SPI GUI to generate an output.

Initial Set-Up
~~~~~~~~~~~~~~

| 1. Install the DPG Downloader and ACE or the AD9136/AD9135 SPI software and support files on your PC. Follow the instructions in the installation wizard and use the default (recommended) installation settings.
| 2. Use a USB cable to connect the EVB to your PC and connect the lab equipment to the EVB.
| 3. Connect the DGP3 unit to your PC and turn on the unit.

Single-Tone Test
~~~~~~~~~~~~~~~~

| These settings configure the AD9136/AD9135 to output a sine wave using the DPG3 and allow the user to view the single-tone performance at the DAC output, under the condition: Fdata = 1.6GHz, 1X interpolation, 4-carrier WCDMA signal with center frequency = 100MHz.
| === Configure DPG Vector Software === 1. To begin, turn on the external +5V supply.
| 2. Open DPG Downloader if you have not done so. (Start > All Programs > Analog Devices > DPG > DPGDownloader). Ensure that the program detects the AD9136/AD9135, as indicated in the “Evaluation Board” drop-down list, and select it. Select "QBF 2X4 85G 425M" from the "Port Configuration" drop-down list and "Mode 8" from the "JESD Mode" drop-down list.
| 3. Click on “Add Generated Waveform”, and then “Wireless Infrastructure”. A WIFR panel will be added to the vector list. Enter the Data Rate, in this case 1.6GHz and the desired frequency, 100MHz. Enter the digital amplitude. In this case we use 0dBFS. Select "2's Complement" from the Number Format drop-down list. Input the center frequency of "100MHz" at the bottom of the panel, choose "WCDMA" from the Standard drop-down menu and increase the No. of Carriers to "4" - then hit the "Add Carriers" button.
| 4. Select the WIFR vector (I) in the “DAC0” drop down menu and the WIFR vector (Q) in the “DAC1”. At this point, the DPG Downloader panel should look like Figure 3.
|

.. container:: center

   
   +--------------------------------+
   | |image5|                       |
   +--------------------------------+

   | Figure 3. DPG Downloader Panel |

   +--------------------------------+
   


Configuring SPI using ACE
^^^^^^^^^^^^^^^^^^^^^^^^^

| 1. Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 1.6GHz, and the output level to 3dBm. The spectrum analyzer can be configured with Start Frequency = 1 MHz, Stop Frequency = 800 MHz, and Resolution Bandwidth of 30 kHz, and Trace Detector to Average (Log/RMS/V). Choose Input Attenuation to be 8dB. This can be adjusted later if indications are that the analyzer is causing degradations.
| 2. Open ACE (Start > All Programs > Analog Devices > ACE > ACE). The |ace_icon_small.png| icon indicates the ACE software. If the board is connected properly, the screen should look similar to Figure 4. Double click on this board.
|

.. container:: center

   
   +----------+
   | |image6| |
   +----------+
   
   +----------------------------------+

   
   | Figure 4. Detected AD9135 in ACE |

   +----------------------------------+
   


Ensure that the |connection_icon.png| button is green in the subsystem image under the “System” tab, as shown in Figure 5. If not, click it, select the AD9136/5, and click *Acquire*. Double click on the subsystem image to reach the board block diagram.

.. container:: center

   
   +----------+
   | |image7| |
   +----------+
   
   +-------------------------+

   
   | Figure 5. AD9135 system |

   +-------------------------+
   


Next to the board block diagram, click "Modify" under "Initial Configuration Summary."

.. container:: center

   
   +----------+
   | |image8| |
   +----------+
   
   +-----------------------------------------------------------------------------+

   
   | Figure 6. AD9135 board block diagram. The JESD PLL should not be locked yet |

   +-----------------------------------------------------------------------------+
   


Select "Dual Link" from the pull-down menu next to Links, and set the JESD Mode to 8. Check the Subclass box and set interpolation to 1. The FDAC frequency should be set to 1.6 GHz. The settings should match Figure 6. Select "Apply."

.. container:: center

   
   +----------+
   | |image9| |
   +----------+
   
   +---------------------------------------------------------+

   
   | Figure 7. Initial configuration settings for the AD9135 |

   +---------------------------------------------------------+
   


Double click on the dark blue AD9135 chip block in the board block diagram. The chip block diagram should appear, as shown in Figure 8. The JESD PLL should now be locked on both the board and chip block diagrams. Other parameters can be changed on both block diagrams, but do not need to be for this test. For more information about changing parameters in ACE, see the ACE Software Features section.

.. container:: center

   
   +-----------+
   | |image10| |
   +-----------+
   
   +-------------------------------------+

   
   | Figure 8. AD9135 chip block diagram |

   +-------------------------------------+
   


| 3. On the DPGDownloader panel, seen in Figure 3, the Serial Line Rate in the should read 8Gbps.
| Click Download (|image11|) and Play (|image12|) in the DPG Downloader screen.

| The current on the 5V supply should read about 1430mA. If you do not see the output, gently push the board toward the DPG3. This ensures that the board is firmly connected to the DPG3. The four registers codeGrpSync, FrameSync, GoodCheckSum and Initial LaneSync should all read 0F indicating the lanes are working correctly.
| 4. The output spectrum of the DAC should look like Figure 9 below.

.. container:: center

   
   +------------------------------------------------------------+
   | |image13|                                                  |
   +------------------------------------------------------------+

   | Figure 9. AD9136/AD9135-EBZ Eval Board DAC output Spectrum |

   +------------------------------------------------------------+
   


Configuring SPI using the legacy SPI Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| 1. Open the AD9136/AD9135 SPI application (Start > All Programs > Analog Devices > AD9136/AD9135 > AD9136/AD9135 SPI). The screen should look similar to Figure 10.
|

.. container:: center

   
   +-----------+
   | |image14| |
   +-----------+
   
   +-----------------------------------------------------------+

   
   | Figure 10. Entry Screen of the AD9136/AD9135 SPI software |

   +-----------------------------------------------------------+
   


| 2. Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 1.6GHz, and the output level to 3dBm. The spectrum analyzer can be configured with Start Frequency = 1 MHz, Stop Frequency = 800 MHz, and Resolution Bandwidth of 30 kHz, and Trace Detector to Average (Log/RMS/V). Choose Input Attenuation to be 8dB. This can be adjusted later if indications are that the analyzer is causing degradations.
| 3. Follow the sequence below to configure the AD9136/AD9135 SPI registers.
| a. The Links should be set to dual link. The JESD Mode is set to 8, Subclass 1 box checked, Interpolation set to 1, and FDAC set to 1.6GHz. Click “Commit” button to initialize the AD9136/AD9135. The JESD204B PLL should be locked indicated with bright green JESD204B PLL readback LED.
| b. At this point the Serial Line Rate in the DPG3 software panel should read 8Gbps.
|

.. container:: center

   
   +---------------------------------------------------------------+
   | |image15|                                                     |
   +---------------------------------------------------------------+

   | Figure 11. Configured panel of the AD9136/AD9135 SPI software |

   +---------------------------------------------------------------+
   


| d. Click Download (|image16|) and Play (|image17|) in the DPG Downloader screen.

| e. The current on the 5V supply should read about 1430mA. If you do not see the output, gently push the board toward the DPG3. This ensures that the board is firmly connected to the DPG3. The four registers codeGrpSync, FrameSync, GoodCheckSum and Initial LaneSync should all read 0F indicating the lanes are working correctly.
| 4. The output spectrum of the DAC should look like Figure 12 below.

.. container:: center

   
   +-------------------------------------------------------------+
   | |image18|                                                   |
   +-------------------------------------------------------------+

   | Figure 12. AD9136/AD9135-EBZ Eval Board DAC output Spectrum |

   +-------------------------------------------------------------+
   


ACE Software Features
---------------------

The ACE software is organized to allow the user to evaluate and control the AD9122A evaluation board. The “Initial Configuration” wizard, which is only available for certain boards, controls the DAC and PLL setups. Block diagram views of the board and chip contain elements that can be used to vary parameters like ref current and data format. These parameters can be changed using check boxes, drop down menus, and input boxes. Some parameters do not have settings shown in the diagram. Double click on the parameter to view the available settings, seen with the NCO settings below.


|ad9122_nco.png|

.. container:: centeralign

   NCO settings for the AD9122


In addition, some parameters can be enabled or disabled. This feature is evident by the color of the block parameter. For example, if the block parameter is dark blue, the parameter is enabled. If it is light grey, it is disabled. To enable or disable a parameter, click on it.

.. container:: column


   ..

|ad9739a_on.png|

.. container:: column


   ..

|ad9739a_off.png|

.. container:: column

   
   .. container:: centeralign

      Enabled parameter

   


.. container:: column

   
   .. container:: centeralign

      Disabled parameter

   



More direct changes to registers and bit fields can be made in the memory map, which is linked from the chip block diagram through the “Proceed to Memory Map” button. In this view, names, addresses, and data can be manually altered by the user.


   



|ad9122_memmap.png|

.. container:: centeralign

   Bench Set-Up


ACE also contains the Macro Tool, which can be used to record register reads and writes. This is executed in the memory map view or with the initialization wizard. To use, check the “Record Sub-Commands” checkbox and press the record button. Changes in the memory map, which are bolded until they are applied to the part, are recorded as UI commands by the macro tool once the changes are made. Changed register write commands for the controls are also recorded. Hit “Apply Changes” to execute the commands and make changes in the memory map. To stop recording, click the “Stop Recording” button. A macro tool page with the command steps will be created. The macro can be saved using the “Save Macro” button so that it may be loaded for future use.



|ad9122_macrocommands.png|

.. container:: centeralign

   Macro tool in ACE. The *Stop Recording*, *Record*, and *Save Macro* commands are located at the top of the macro tool.


The raw macro file will be saved using ACE syntax, which is not easily readable. To remedy this, the ACE software download includes the Macro to Hex Conversion Tool. The user can choose to include or exclude register write, reads, and/or comments in the conversion. The file pathways for the source and save paths should be the same, except that one should be an .acemacro file and the other should be a .txt file. The “Convert” button converts and opens the converted text file, which is easier to read. The conversion tool can also convert back to an .acemacro file if desired.

.. container:: column


   ..

|ad9122_m2hconvert_5.png|

.. container:: column


   ..

|ad9122_m2hconvert_4.png|

.. container:: column

   
   .. container:: centeralign

      Conversion set-up for macro to hex

   


.. container:: column

   
   .. container:: centeralign

      Converted text file

   



For more information about ACE and its features, visit https://wiki.analog.com/resources/tools-software/ace.

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
.. |image5| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9135_dpgd_new.png
.. |ace_icon_small.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ace_icon_small.png
.. |image6| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9135_detected.png
.. |connection_icon.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/connection_icon.png
.. |image7| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9135_system.png
.. |image8| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9135_boardview_new.png
.. |image9| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9135_applypage_new.png
.. |image10| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9135_chipview_new.png
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/dpg/image009.png
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/dpg/image010.png
.. |image13| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/ad9136_1.6ghzdac_1x_4xwcdma_fout100m_plloff.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/ad9136-ebz_spipro_initialview.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/ad9136-ebz_spipro_finalview.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/dpg/image009.png
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/dpg/image010.png
.. |image18| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/ad9136/ad9136_1.6ghzdac_1x_4xwcdma_fout100m_plloff.png
   :width: 600px
.. |ad9122_nco.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_nco.png
.. |ad9739a_on.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_on.png
.. |ad9739a_off.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_off.png
.. |ad9122_memmap.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_memmap.png
.. |ad9122_macrocommands.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_macrocommands.png
.. |ad9122_m2hconvert_5.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_m2hconvert_5.png
.. |ad9122_m2hconvert_4.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_m2hconvert_4.png
