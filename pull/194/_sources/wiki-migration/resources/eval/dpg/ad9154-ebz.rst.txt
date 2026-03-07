SPIPRO AD9154-EBZ Evaluation Board Quick Start Guide
====================================================

Getting Started with the AD9154-EBZ Evaluation Board and Software
-----------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  :adi:`AD9154-EBZ` Evaluation Board for DPG3
-  Evaluation Board CD
-  Mini-USB Cable

Recommended Equipment List
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  +5VDC Lab Power Supply
-  Sinusoidal Clock Source
-  Spectrum Analyzer
-  Oscilloscope
-  Data Pattern Generator Series 3 (DPG3)

Introduction
------------

The AD9154-EBZ connects to a DPG3. The AD9154 is a quad JESD204B signal processing RF Digital to Analog Converter. The DPG3 automatically formats the data and sends it to the AD9154-EBZ via its JESD204B lanes. The Evaluation Board (EVB) runs from a single +5V lab supply. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, JESD204B SYSREF signals, and a CFRAME clock used by the DPG3.

AD9154 Evaluation Software
--------------------------

There are two evaluation softwares available for the AD9154: ACE, the preferred evaluation software from ADI, and the legacy SPIPro graphical user interface (GUI). Both are included on the Evaluation Board CD. ACE can also be downloaded from the ACE website at https://wiki.analog.com/resources/tools-software/ace. In addition, the ACE plugin for the AD9154 is available in the software section of the :adi:`EVAL-AD9154` eval webpage. DPGDownloader is used with both evaluation softwares and can be downloaded from the DPG website at http://www.analog.com/dpg.

Hardware Setup
--------------

Figure 1 shows the block diagram of the set-up.

.. container:: center

   
   +----------+
   | |image1| |
   +----------+
   
   +----------------------------------------+

   
   | Figure 1. AD9154-EBZ Lab Block Diagram |

   +----------------------------------------+
   


.. container:: center

   
   +----------+
   | |image2| |
   +----------+
   
   +----------------------------------+

   
   | Figure 2. Top view of AD9154-EBZ |

   +----------------------------------+
   


Connect +5.0V to P5, GND to P6. A low phase noise high frequency clock source should be connected to the SMA connector J1 (CLK_IN). A spectrum analyzer should be connected to the SMA connector J17. Connect J4, J5, and J7 to an oscilloscope. The evaluation board connects to the DPG3 through the connector P4. The PC should be connected to the EVB using the mini-USB connector XP2. Figure 1 shows a block diagram of the set-up.

Getting Started
---------------

The PC software is included in the CD shipped with the EVB. The installation includes the DPG Downloader software as well as all the necessary AD9154 files including schematic, board layout, datasheet, and other files. The AD9154 Evaluation Software section details the necessary evaluation software.

Initial Set-Up
~~~~~~~~~~~~~~

1. Install the DPG Downloader and ACE (or the SPIPro software) and support files on your PC. Follow the instructions in the installation wizard and use the default (recommended) installation settings.

2. Use a USB cable to connect the EVB to your PC and connect the lab equipment to the EVB.

3. Connect the DPG3 unit to your PC and turn on the unit.

Single Tone Demonstration
~~~~~~~~~~~~~~~~~~~~~~~~~

These settings configure the AD9154 to output a 112Mhz -1dbFS sine wave using the DPG3 on all four AD9154 DACs.

Using ACE
^^^^^^^^^

1. Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 1.5 GHz, and the output level to 3dBm. The spectrum analyzer can be configured as shown in Figure 9 with a resolution bandwidth of 100kHz. Choose an Input Attenuation of 24dB.

| 2. Open ACE (Start > All Programs > Analog Devices > ACE > ACE). The |ace_icon_small.png| icon indicates the ACE software. If the board is connected properly, the screen should look similar to Figure 3. Double click on this board.
|

.. container:: center

   
   +----------+
   | |image3| |
   +----------+
   
   +----------------------------------+

   
   | Figure 3. Detected AD9154 in ACE |

   +----------------------------------+
   


Ensure that the |connection_icon.png| button is green in the subsystem image under the “System” tab, as shown in Figure 4. If not, click it, select the AD9154, and click "Acquire." Double click on the subsystem image to reach the board block diagram.

.. container:: center

   
   +----------+
   | |image4| |
   +----------+
   
   +-------------------------+

   
   | Figure 4. AD9154 system |

   +-------------------------+
   


Next to the board block diagram, click "Modify" under "Initial Configuration Summary."

.. container:: center

   
   +----------+
   | |image5| |
   +----------+
   
   +-----------------------------------------------------------------------------+

   
   | Figure 5. AD9154 board block diagram. The JESD PLL should not be locked yet |

   +-----------------------------------------------------------------------------+
   


Select "Single Link" from the pull-down menu next to Links, and set the JESD Mode to 0. Ensure that the Subclass box is unchecked, and set interpolation to 2. The FDAC frequency should be set to 1.5 GHz. The settings should match Figure 6. Select "Apply."

.. container:: center

   
   +----------+
   | |image6| |
   +----------+
   
   +---------------------------------------------------------+

   
   | Figure 6. Initial configuration settings for the AD9154 |

   +---------------------------------------------------------+
   


Double click on the dark blue AD9154 chip block in the board block diagram. The chip block diagram should appear, as shown in Figure 7. The JESD PLL should now be locked on both the board and chip block diagrams. Other parameters can be changed on both block diagrams, but do not need to be for this test. For more information about changing parameters in ACE, see the ACE Software Features section.

.. container:: center

   
   +----------+
   | |image7| |
   +----------+
   
   +-------------------------------------+

   
   | Figure 7. AD9154 chip block diagram |

   +-------------------------------------+
   


3. Open DPGDownloader. (Start > All Programs > Analog Devices > DPG > DPGDownloader). DPGDownloader GUI will come up. Select the Port configuration QBF 1X8 85G 425M. The configuration progress bar will then show a moving green indication. Once port configuration is complete, select “Add Generated Waveform” and “Single Tone." Set Data Rate to 750 MHz, Desired Frequency to 112 MHz, Amplitude to -1.0 dBFS, uncheck unsigned, check Generate Complex Data (I&Q). Under Data Playback, select I data for DAC 0 and DAC2, and Q data for DAC 1 and DAC3. These settings should match those in the DPGDownloader panel in Figure 8.

.. container:: center

   
   +----------+
   | |image8| |
   +----------+
   
   +----------------------------------+

   
   | Figure 8. DPGDownloader settings |

   +----------------------------------+
   


4. Click Download (|image9|) and Play (|image10|) in the DPG Downloader screen. The spectrum in Figure 9 will appear on all 4 DAC outputs (J17, J4, J5, and J7), Serial Line Rate will be 7.5 Gbps. The current on the 5V supply should read around 1800mA - 1950mA. Figure 10 is a scope capture of the DAC output signal taken on three of the channels.

   


| 5. Here is what you will see at the output of DAC0 on the Spectrum Analyzer.
|

.. container:: center

   
   +-----------+
   | |image11| |
   +-----------+
   
   +------------------------------------------------+

   
   | Figure 9. DAC Output Spectrum Analyzer Display |

   +------------------------------------------------+
   


6. Here’s what you will see on DAC1, DAC2, and DAC3 on the scope.

.. container:: center

   
   +-----------+
   | |image12| |
   +-----------+
   
   +--------------------------------------+

   
   | Figure 10. DAC Outputs Scope Display |

   +--------------------------------------+
   


Using the SPIPro software
^^^^^^^^^^^^^^^^^^^^^^^^^

1. Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 1.5 GHz, and the output level to 3dBm. The spectrum analyzer can be configured as shown in Figure 15 with a resolution bandwidth of 100kHz. Choose an Input Attenuation of 24dB.

2. On your lab computer, open the AD9154 SPIPro application (Start > All Programs > Analog Devices > AD9154 > AD9154 SPI). You will see the GUI shown in Figure 11 come up.

.. container:: center

   
   +-----------+
   | |image13| |
   +-----------+
   
   +--------------------------------------+

   
   | Figure 11. AD9154 SPIPro at start up |

   +--------------------------------------+
   


3. SPIPro Start Up Sequence.

a. Select “Single” for Links.

b. Select JESD Mode 0.

c. Uncheck the “Subclass 1” box

d. Select “2” for Interpolation.

e. Press the “Configure DAC and Clock” Button

f. The JESD204B PLL Lock Readback light should turn green and register bit settings will be populated. The GUI will look like Figure 12, except that values in “CodeGrpSync”, “FrameSync”, “GoodCheckSum”, and “InitialLaneSync” may be different because the link JESD204B Transmitter has not yet been set up.

4. DPGDownloader Start Up Sequence

a. Open DPGDownloader. (Start > All Programs > Analog Devices > DPG > DPGDownloader). DPGDownloader GUI will come up as shown Figure 13.

b. Select the Port configuration QBF 1X8 85G 425M. The configuration progress bar will then show a moving green indication.

c. Once port configuration is complete, select “Add Generated Waveform” and “Single Tone”.

d. Set Data Rate to 750 MHz, Desired Frequency to 112 MHz, Amplitude to -1.0 dBFS, uncheck unsigned, check Generate Complex Data (I&Q).

e. Under Data Playback, select I data for DAC 0 and DAC2, and Q data for DAC 1 and DAC3. The DPGDownloader settings should resemble Figure 14.

f. Click Download (|image14|) and Play (|image15|) in the DPG Downloader screen. The spectrum in Figure 15 will appear on all 4 DAC outputs (J17, J4, J5, and J7), Serial Line Rate will be 7.5Gbps. Figure 16 is a scope capture of the DAC output signal taken on three of the channels.

5. On SPIPro Quick Start Tab, click “Read All Registers” and confirm the GUI looks the same as Figure 12.

6. The current on the 5V supply should read around 1800mA - 1950mA.

.. container:: center

   
   +-----------+
   | |image16| |
   +-----------+
   
   +-------------------------------------------+

   
   | Figure 12. Fully Configured AD9154 SPIPro |

   +-------------------------------------------+
   


.. container:: center

   
   +-----------+
   | |image17| |
   +-----------+
   
   +---------------------------------------------+

   
   | Figure 13. DPG Downloader Panel at Start Up |

   +---------------------------------------------+
   


.. container:: center

   
   +-----------+
   | |image18| |
   +-----------+
   
   +--------------------------------------------------+

   
   | Figure 14. Fully Configured DPG Downloader Panel |

   +--------------------------------------------------+

   | 7. Here is what you will see at the output of DAC0 on the Spectrum Analyzer.
|

.. container:: center

   
   +-----------+
   | |image19| |
   +-----------+
   
   +-------------------------------------------------+

   
   | Figure 15. DAC Output Spectrum Analyzer Display |

   +-------------------------------------------------+
   


8. Here’s what you will see on DAC1, DAC2, and DAC3 on the scope.

.. container:: center

   
   +-----------+
   | |image20| |
   +-----------+
   
   +--------------------------------------+

   
   | Figure 16. DAC Outputs Scope Display |

   +--------------------------------------+
   


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

.. |image1| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/9154ebz_figure_1_1.png
.. |image2| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/9154ebz_figure_2.png
.. |ace_icon_small.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ace_icon_small.png
.. |image3| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9154_detected.png
.. |connection_icon.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/connection_icon.png
.. |image4| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9154_system.png
.. |image5| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9154_boardview_enabled.png
.. |image6| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9154_applypage.png
.. |image7| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9154_chipview.png
.. |image8| image:: https://wiki.analog.com/_media/{{ /resources/eval/user-guides/ad9154_dpgd.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/image009.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/dpg/image010.png
.. |image11| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/9154ebz_figure_7.png
.. |image12| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/9154ebz_figure_8.png
.. |image13| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/9154ebz_figure_3.png
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/dpg/image009.png
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/dpg/image010.png
.. |image16| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/9154ebz_figure_4.png
.. |image17| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/9154ebz_figure_5.png
.. |image18| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/9154ebz_figure_6.png
.. |image19| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/9154ebz_figure_7.png
.. |image20| image:: https://wiki.analog.com/_media/{{ /resources/eval/dpg/9154ebz_figure_8.png
.. |ad9122_nco.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_nco.png
.. |ad9739a_on.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_on.png
.. |ad9739a_off.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_off.png
.. |ad9122_memmap.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_memmap.png
.. |ad9122_macrocommands.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_macrocommands.png
.. |ad9122_m2hconvert_5.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_m2hconvert_5.png
.. |ad9122_m2hconvert_4.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_m2hconvert_4.png
