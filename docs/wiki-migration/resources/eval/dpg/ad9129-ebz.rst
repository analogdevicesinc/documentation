AD9129-EBZ Evaluation Board Quick Start Guide
=============================================

|

.. warning::

   \ **NOTE:**

   | Support using DPG2/DPG3 project on this website is only for legacy purposes. The support for this project has been discontinued, and ADS7 is the recommended replacement.


You can return to Homepage here: `AD9119/AD9129 Evaluation Boards <https://wiki.analog.com/resources/eval/dpg/eval-ad9129>`_

Getting Started with the AD9129 Evaluation Board and Software
-------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  AD9129-EBZ Evaluation Board
-  Mini-USB Cable
-  Evaluation Board CD

Recommended Equipment List
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  +5Vdc, -5 Vdc Power Supply
-  Data Pattern Generator Series 2 (DPG2)
-  Spectrum Analyzer Ex: Agilent PXA or Rohde Schwarz FSU
-  Sinusoidal Clock Source (>2 GHz, <0.5ps RMS jitter) Ex: R&S SMA100

Introduction
------------

The AD9129-EBZ connects to a DPG2 to allow for quick evaluation of the AD9129, a high-speed, RF Digital to Analog converter (RF DAC). The DPG2 automatically formats the data and sends it to the AD9129-EBZ, simplifying evaluation of the device. The Evaluation Board (EVB) runs from +5 volt and -5 volt supplies. Figure 2 is an image of the top side of the AD9129 EVB.

AD9129 Evaluation Software
--------------------------

The AD9129 Evaluation Board software has an easy-to-use legacy graphical user interface (GUI), but ACE, a newer evaluation software from ADI, is the preferred evaluation software. Both are included on the Evaluation Board CD. Additionally, DPGDownloader can be downloaded from the DPG Web site at http://www.analog.com/dpg. This will install DPGDownloader (for loading vectors into the DPG) and the AD9129 SPI Controller application. ACE can be downloaded from the ACE website at https://wiki.analog.com/resources/tools-software/ace. The ACE plug-in for the evaluation board is available for download on the AD9129 eval webpage in the *Software* section at http://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9129.html#eb-buy.

Hardware Setup
--------------

Connect +5V to P3, GND to P4, and -5V to P5. A low phase noise, high frequency clock source should be connected to the SMA connector, J3, labeled “CLK”, and the spectrum analyzer should be connected to the SMA connector, J1. The evaluation board connects to the DPG2 unit through connectors P1 and P2. The PC should be connected to the EVB using the mini-USB connector XP2 after installation of the Evaluation Board software.

.. container:: column


   ..

|image1|

.. container:: column


   ..

|image2|

.. container:: column

   Figure 1 - Block diagram of the AD9129 lab bench set-up


.. container:: column

   Figure 2 - Top view of AD9129-EBZ Evaluation Board



Getting Started
---------------

The PC software comes on the included Evaluation Board CD, but may also be downloaded from the DPG Web site at http://www.analog.com/dpg and the ACE website at https://wiki.analog.com/resources/tools-software/ace. The installation will include the DPG Downloader as well as all the necessary AD9129 files including schematic, board layout, data sheet, SPI GUI, and other files.The ACE plug-in for the AD9129 is available on the eval website. The following procedure will set up a basic 1-carrier, 256-QAM signal. This can be done with either ACE or the SPI software, though ACE is preferred.

A. ACE
~~~~~~

Initial Set-Up
^^^^^^^^^^^^^^

1. Install the DPG Downloader, ACE, AD9129 ACE plug-in, and AD9129 software and support files on your PC 2. Start ACE 3. Connect the EVB to your PC and lab equipment as shown in Figure 1 above. Use a USB cable to connect your PC to the EVB, and another USB cable to connect your PC to the DPG unit. It is suggested that the basic set-up is verified before making any modifications to the evaluation board.

Load ACE Settings
^^^^^^^^^^^^^^^^^

Open ACE from the start window. It can be found by following the file path to the program or by searching in the windows search bar for “ACE.” The |ace_icon_small.png| icon indicates the ACE software.

If the board is connected properly, ACE will detect it and display it on the Start page under *Attached Hardware*. Double click this board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9129_detected.png
   :alt: ad9129_detected.png
   :align: center

Ensure that the |connection_icon.png| button is green in the subsystem image under the “System” tab. If not, click it, select the AD9129, and click *Acquire*. Double click on the subsystem image.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9129_system.png
   :alt: ad9129_system.png
   :align: center

On the board diagram, click *Run Example Startup Routine*. This will set the parameters for this example.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9129_chipview.png
   :alt: ad9129_chipview.png
   :align: center

For further changes, double click on the AD9129 on the board diagram. This will bring up the chip block diagram, which can be used to set other parameters, such as data format and PLL Config. The PLL and DLL should both be locked and the delay cells should be checked. If not, click *Read All* in the upper left corner of the page. For more details about altering parameters, see the *ACE Software Features* section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9129_clickview.png
   :alt: ad9129_clickview.png
   :align: center

Configure Hardware
^^^^^^^^^^^^^^^^^^

Configure the hardware according to the hardware set-up instructions given in the *Hardware Setup* section above. Set the frequency of the signal generator to 2 GHz, and the output level to 0 dBm. The spectrum analyzer can be configured with Start Frequency = 20 MHz, Stop Frequency 1 GHz, and Resolution Bandwidth of 100 kHz. Use an Average/RMS detector setting, and choose Input Attenuation to be 10 dB. This can be adjusted later if indications are that the analyzer is causing degradations (warnings on the analyzer itself, or third order products appearing on the output spectrum).

Load Pattern from the DPG2
^^^^^^^^^^^^^^^^^^^^^^^^^^

Open DPGDownloader (Start > Programs > Analog Devices > DPG > DPGDownloader). Ensure that the program detects the AD9129, as indicated in the *Evaluation Board* drop-down list, and select it. For this evaluation board, LVDS is the only valid Port Configuration. If it is not selected automatically, select it from the *Port Configuration* drop-down list. The *Data Clock Frequency* window may not yet show a clock frequency, but it normally does. Click on *Add Generated Waveform*, and then *Single Tone*. Enter the data rate, or DAC clock frequency, as 2GHz and the desired frequency as 200 MHz. Next, choose the *Resolution* to be 14 bits. Ensure that the DPDDownloader settings match the figure below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9129_dpgd_singletone.png
   :alt: ad9129_dpgd_singletone.png
   :align: center

Next, in the lower portion of the screen, select *Single Tone* as the Data Vector. The other options can be left at their default values. The Data Clock Out (DCO) frequency from the AD9129 should be reported in the Data Clock Frequency window as roughly 500 MHz. Make sure the DPG2 unit is powered up and the AD9129 eval board is plugged into it correctly. Click the Download button (|image3|) to download the pattern from the computer to the DPG2 unit, wait for the Play (|image4|) button to become active, and then click the Play (|image5|) button to begin vector playback to the AD9129.

Result
^^^^^^

The final result should be a clean 200 MHz tone as shown below. To best verify the set-up, match the settings seen below on the spectrum analyzer screen.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9129_newspectrum.png
   :alt: ad9129_newspectrum.png
   :align: center

B. SPI Software/GUI
~~~~~~~~~~~~~~~~~~~

.. _initial-set-up-1:

Initial Set-Up
^^^^^^^^^^^^^^

| 1. Install the DPG Downloader and AD9129 software and support files on your PC
| 2. Start the AD9129 Control Panel GUI (but don’t hit the run arrow yet)
| 3. Connect the EVB to your PC and lab equipment as shown in Figure 1 above. Use a USB cable to connect your PC to the EVB, and another USB cable to connect your PC to the DPG2 unit. Note that a DPG3 unit can also be used.
| It is suggested that the basic set-up is verified before making any modifications to the evaluation board.

Load Initial Settings
^^^^^^^^^^^^^^^^^^^^^

To begin, open the AD9129 SPI application (Start > Programs > Analog Devices > AD9129 > AD9129_27 SPI). The screen should look similar to Figure 3 on the Common tab. The AD9129 SPI loads default settings that should be usable for most applications.


|image6|

.. container:: centeralign

   Figure 3. Entry screen of the AD9129 SPI GUI


.. _configure-hardware-1:

Configure Hardware
^^^^^^^^^^^^^^^^^^

Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the signal generator to 2.455125926 GHz, and the output level to 0 dBm. The spectrum analyzer can be configured with Start Frequency = 20 MHz, Stop Frequency 1 GHz, and Resolution Bandwidth of 100 kHz. Use an Average/RMS detector setting, and choose Input Attenuation to be 10 dB. This can be adjusted later if indications are that the analyzer is causing degradations (warnings on the analyzer itself, or third order products appearing on the output spectrum.).

Enable the PLL
^^^^^^^^^^^^^^

On the “PLL” tab, the “Controller Ena” button should be green. Click the "Play" button (|image7|) to program the registers. The Readback light next to the button should change from red to green, and the PLL LOCK light should turn green. Note that in some cases, it may be necessary to click the “Controller Reset” button (it goes to green), click the (|image8|) button, and then click the “Controller Reset” button (it goes to red) and the (|image9|) button again to reset the PLL in order for it to lock.


|image10|

.. container:: centeralign

   Figure 4. PLL screen of the AD9129 SPI GUI


.. _load-pattern-from-the-dpg2-1:

Load Pattern from the DPG2
^^^^^^^^^^^^^^^^^^^^^^^^^^

Open DPGDownloader (Start > Programs > Analog Devices > DPG > DPGDownloader). Ensure that the program detects the AD9129, as indicated in the “Evaluation Board” drop-down list, and select it. For this evaluation board, LVDS is the only valid Port Configuration, and it will be selected automatically. The “Data Clock Frequency” window may not yet show a clock frequency, but it normally does.


|image11|

.. container:: centeralign

   Figure 5. Choose “Cable Infrastructure” as the vector type


Click on “Add Generated Waveform”, and then “Cable Infrastructure”, as shown in Figure 5. A Cable Infrastructure panel will be added to the vector list. Enter the sample rate, or DAC clock frequency, 2.455125946 GHz. Next, choose the “Resolution” to be 14 bits. Choose a center frequency of 108 MHz. Keep “Relative Amplitude” as 0 dB, and “Number of Channels” as ‘1’. Then, click the “Add Channels” button. The signal should appear on the list of signals as shown in Figure 6.



|image12|

.. container:: centeralign

   Figure 6. DPG Downloader Upper section, used to select and configure the desired signal to be generated


Next, in the lower portion of the screen, select “1I: CIFR Vector (I)” as the Data Vector. The other options can be left at their default values. The Data Clock Out (DCO) frequency from the AD9129 should be reported in the Data Clock Frequency window as roughly 613.69 MHz.



|image13|

.. container:: centeralign

   Figure 7. DPG Downloader Lower section, used to select the desired vector and download it to the DPG2 unit


Make sure the DPG2 unit is powered up and the AD9129 eval board is plugged into it correctly. Click the "Download" button (|image14|) to download the pattern from the computer to the DPG2 unit, wait for the Play (|image15|) button to become active, and then click the Play (|image16|) button to begin vector playback to the AD9129.

Enable the LVDS Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^

On the AD9129 SPI GUI’s “DLL” tab, the “DUTY Corr Ena” button and the “DLL_ENA” button should be green (selected). Click the (|image17|) button to program the registers. The Readback light next to both buttons should change from red to green, and the DLL Lock light should change from red to green. It may be necessary to click the (|image18|) button again to get a full readback status since the controller may take slightly longer to lock than the GUI allowed on the first write and then readback.


|image19|

.. container:: centeralign

   Figure 8. DLL screen of the AD9129 SPI GUI


In rare cases, the data link may have gotten corrupted and the registers not programmed correctly. In these cases, the output of the DAC will show significantly degraded performance. To remedy this situation, click the “DUTY Corr Ena” button and the “DLL_ENA” buttons, and then click the (|image20|) button to program the registers. Then, re-click the “DUTY Corr Ena” button and the “DLL_ENA” buttons, and then click the (|image21|) button to program the registers. This disables and re-enables the Data Interface DLL and allows it to re-lock to the DCI. At this time, it is also possible to click the "Repeat" button (|image22|) to continuously program the part, making the SPI GUI run in a more interactive mode.

.. _result-1:

Result
^^^^^^

The final result should be a single 256-QAM carrier centered at 108 MHz, as shown in Figure 9. An attenuation of 10 dB was used in this measurement, which raises the noise floor of the measurement, but avoided saturating the input and causing higher-ordered products from being created. A second plot is shown in Figure 10, in which the attenuation was reduced to 6 dB. It can be seen that the third harmonic increased in amplitude by about 6 dB, and the noise floor reduced by 4 dB, indicating the input of the spectrum analyzer is affecting the measurement.


|image23|

.. container:: centeralign

   Figure 9. Single 256-QAM channel at AD9129 output


   |image24|

.. container:: centeralign

   Figure 10. 256-QAM channel at AD9129 output with 6 dB attenuation setting on spectrum analyzer input


SPI Software
------------

The AD9129 SPI software is conveniently organized in a series of tabs that groups registers according to their functions. In this way, all registers associated with the fDAC PLL, for example, are on the “PLL” tab, all registers associated with the data clock Delay Locked Loop (DLL) are on the “DLL” tab, and so on. A full description of each register and its settings is given in the AD9129 data sheet. Some of the registers and their functions are described here as they pertain to the AD9129 evaluation board. Please note that some of the screen images in this document may not match exactly with the latest revision of the software, due to ongoing improvements and enhancements to the software. The full screen layout is shown in Figure 11. The tabs can be seen across the top of the work area, and a “READBACK” area is below the active tab area. This READBACK section is present on each of the tabs, so that the user can quickly assess status of the PLL and DLL lock, as well as parity and the FIFO phase. Each of the tabs is discussed in its own section below.


|image25|

.. container:: centeralign

   Figure 11. Common tab on the AD9129 SPI GUI


Common Tab
~~~~~~~~~~

The common tab has selections that apply to the general configuration of the DAC. The Reset bit is set or reset here, as well as basic configuration of the serial port: Short vs. Long mode; SDIO pin as an output or bi-directional, MSB or LSB first for the data words, format of the data words (unsigned or two’s complement), and whether the 2x interpolator filter is ENabled (“DDR”) or DISabled (“SDR”). With the 2x interpolator filter enabled, two filter options are available to provide either 25 or 40 dB of out of band rejection. Filter selection is controlled in the common tab. The mode of the Frame/Parity pins is also chosen on this tab, along with MixMode™ or Normal mode for the DAC output. Finally, the SPI_FRM_ACK bit (reg 0x11[6]) is set on this tab. That bit is used to flag an interrupt if the SPIFrmReq bit is set, which indicates that a SPI-based FIFO alignment has been requested.

PLL Tab
~~~~~~~

.. container:: column

   The PLL tab has functions associated with the DAC clock PLL on it. In addition to the enable bit discussed in the Getting Started section, this tab also has settings associated with the PLL retimer registers, reg 0x33 – 0x38. The interrupt control and status bits associated with the PLL (in regs 0x03 – 0x06) are also in this section.


.. container:: column



   ..

|image26|

.. container:: right centeralign

   Figure 12. PLL tab of the AD9129 SPI GUI



DLL Tab
~~~~~~~

.. container:: column

   The DLL tab has the DLL Enable and Duty Cycle Correction Enable bits as discussed in the Getting Started section. Additional status bits associated with the Data interface DLL are also on this tab, including lock status bits, lock lost bit, warning bits, etc. These are mostly located in the Data Control and Data Status registers, regs 0x0A – 0x0F. The bypass delay cell area is for test only and can be ignored.


.. container:: column



   ..

|image27|

.. container:: right centeralign

   Figure 13. DLL tab of the AD9129 SPI GUI



FIFO Tab
~~~~~~~~

.. container:: column

   The FIFO tab has controls and status lights associated with the data interface FIFO. For most uses of the AD9129 EVB, these controls can be left in their default state, and there is no need to change them in the SPI. For more details on the FIFO’s operation and the control and status registers for it, please consult the AD9129 Data Sheet. The FIFO registers are located in address range 0x11 – 0x17.


.. container:: column



   ..

|image28|

.. container:: right centeralign

   Figure 14. FIFO tab of the AD9129 SPI GUI



Parity Tab
~~~~~~~~~~

.. container:: column

   Similar to the FIFO tab, the Parity tab can be left in its default state for most uses of the AD9129 EVB. Parity can be enabled and disabled on this tab, and Even or Odd Parity can be chosen. The parity counter values are also shown. These controls and status bits are associated with the parity registers located at addresses 0x5C – 0x5E. The parity interrupts are in the Interrupt Control and Status registers, 0x03 – 0x06. To reset the parity counters, click the PARITY_FALL_RESET and PARITY_RISE_RESET buttons, then press the |image29| button repeatedly until the values are reset. Alternatively, the |image30| button can be pressed, and then the SPI programming will run in a loop, and the count values can be observed to go to ‘0’, at which time the PARITY_FALL_RESET and PARITY_RISE_RESET buttons can be unclicked.


.. container:: column



   ..

|image31|

.. container:: right centeralign

   Figure 15. FIFO tab of the AD9129 SPI GUI



Power Control (PD) Tab
~~~~~~~~~~~~~~~~~~~~~~

.. container:: column

   The Power Control, or Power Down, tab contains individual controls to power down various blocks on the AD9129. These are associated with the power down registers, 0x01 and 0x02.


.. container:: column



   ..

|image32|

.. container:: right centeralign

   Figure 16. Power Down tab of the AD9129 SPI GUI



Analog Tab
~~~~~~~~~~

.. container:: column

   On the Analog tab, the Full Scale Current of the DAC output can be set by using the increment/decrement arrows or by typing an integer value into the yellow window. This updates registers 0x20 and 0x21 with the new value. The other controls on this tab should be left to their default values.


.. container:: column



   ..

|image33|

.. container:: right centeralign

   Figure 17. Analog control tab of the AD9129 SPI GUI



Save/Load Tab
~~~~~~~~~~~~~

.. container:: column

   The Save/Load tab enables a different way of configuring the AD9129. The “Save” function allows a user to save to a file all of the settings currently set in the various tabs. The “Load” function allows these settings to be recalled and loaded at a later date. While useful in some situations, this method of loading saved settings does not modify the screens or the tabs, it simply loads the settings directly to the DAC, so it can be confusing to use this function. It is recommended that the user begin with the user GUI and tab interface, and only use this “Save/Load” function as an advanced feature.


.. container:: column



   ..

|image34|

.. container:: right centeralign

   Figure 18. Save/Load tab of the AD9129 SPI GUI



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

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/bench_setup_9129_evb.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure2_9129_EBZ.png
   :width: 400px
.. |ace_icon_small.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ace_icon_small.png
.. |connection_icon.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/connection_icon.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/Download.png
   :width: 15px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_pattern.png
   :width: 15px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_pattern.png
   :width: 15px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure3.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure5.png
   :width: 500px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure6.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure6_9129-EBZ.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure7_9129-EBZ.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/Download.png
   :width: 15px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_pattern.png
   :width: 15px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_pattern.png
   :width: 15px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure9.png
   :width: 600px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/repeat_play_vi.png
   :width: 15px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure9_9129-EBZ.png
   :width: 500px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure10_9129-EBZ.png
   :width: 500px
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure14_common_tab.png
   :width: 500px
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure15_pll_tab.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure16_dll.png
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure17_FIFO_tab.png
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image30| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/repeat_play_vi.png
   :width: 15px
.. |image31| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure18_Parity_tab.png
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure19_power_control_tab.png
   :width: 200px
.. |image33| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure20_analog_tab.png
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure21_file_load_tab.png
   :width: 400px
.. |ad9122_nco.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_nco.png
.. |ad9739a_on.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_on.png
.. |ad9739a_off.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_off.png
.. |ad9122_memmap.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_memmap.png
.. |ad9122_macrocommands.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_macrocommands.png
.. |ad9122_m2hconvert_5.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_m2hconvert_5.png
.. |ad9122_m2hconvert_4.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_m2hconvert_4.png
