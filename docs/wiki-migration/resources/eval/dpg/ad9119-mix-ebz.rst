AD9119-MIX-EBZ Evaluation Board Quick Start Guide
=================================================

|

.. warning::

   \ **NOTE:**

   | Support using DPG2/DPG3 project on this website is only for legacy purposes. The support for this project has been discontinued, and ADS7 is the recommended replacement.


You can return to Homepage here: `AD9119/AD9129 Evaluation Boards <https://wiki.analog.com/resources/eval/dpg/eval-ad9129>`_

Getting Started with the AD9119 Mix-mode(tm) Evaluation Board and Software
--------------------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  AD9119-MIX-EBZ Evaluation Board
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

The AD9119-MIX-EBZ connects to a DPG2 to allow for quick evaluation of the AD9119, a high-speed, RF Digital to Analog converter (RF DAC). The DPG2 automatically formats the data and sends it to the AD9119-MIX-EBZ, simplifying evaluation of the device. The Evaluation Board (EVB) runs from +5 volt and -5 volt supplies. Figure 2 is an image of the top side of the AD9119 EVB.

AD9119 Evaluation Software
--------------------------

The AD9119 uses the AD9129 Evaulation Board software. The AD9129 Evaluation Board software has an easy-to-use graphical user interface (GUI). It is included on the Evaluation Board CD, or can be downloaded from the DPG Web site at http://www.analog.com/dpg. This will install DPGDownloader (for loading vectors into the DPG2) and the AD9129 SPI Controller application.

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

   Figure 1 - Block diagram of the AD9119 lab bench set-up


.. container:: column

   Figure 2 - Top view of AD9119-MIX-EBZ Evaluation Board (uses the AD9129 EVB)



Getting Started
---------------

The PC software comes on the included Evaluation Board CD, but may also be downloaded from the DPG Web site at http://www.analog.com/dpg. The installation will include the DPG Downloader as well as all the necessary AD9129 files including schematic, board layout, data sheet, SPI GUI, and other files. The following procedure will set up a basic 1-carrier, 256-QAM signal.

Initial Set-Up
~~~~~~~~~~~~~~

| 1. Install the DPG Downloader and AD9129 software and support files on your PC
| 2. Start the AD9129 Control Panel GUI (but don’t hit the run arrow yet)
| 3. Connect the EVB to your PC and lab equipment as shown in Figure 1 above. Use a USB cable to connect your PC to the EVB, and another USB cable to connect your PC to the DPG2 unit. Note that a DPG3 unit can also be used.
| It is suggested that the basic set-up is verified before making any modifications to the evaluation board.

Load Initial Settings
~~~~~~~~~~~~~~~~~~~~~

To begin, open the AD9129 SPI application (Start > Programs > Analog Devices > AD9129 > AD9129_27 SPI). The screen should look similar to Figure 3 on the Common tab. The AD9129 SPI loads default settings that should be usable for most applications.


|image3|

.. container:: centeralign

   Figure 3. Entry screen of the AD9129 SPI GUI


Configure Hardware
~~~~~~~~~~~~~~~~~~

Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the signal generator to 2.455125926 GHz, and the output level to 0 dBm. The spectrum analyzer can be configured with Start Frequency = 20 MHz, Stop Frequency 1 GHz, and Resolution Bandwidth of 100 kHz. Use an Average/RMS detector setting, and choose Input Attenuation to be 10 dB. This can be adjusted later if indications are that the analyzer is causing degradations (warnings on the analyzer itself, or third order products appearing on the output spectrum.).

Enable the PLL
~~~~~~~~~~~~~~

On the “PLL” tab, the “Controller Ena” button should be green. Click the "Play" button (|image4|) to program the registers. The Readback light next to the button should change from red to green, and the PLL LOCK light should turn green. Note that in some cases, it may be necessary to click the “Controller Reset” button (it goes to green), click the (|image5|) button, and then click the “Controller Reset” button (it goes to red) and the (|image6|) button again to reset the PLL in order for it to lock.


|image7|

.. container:: centeralign

   Figure 4. PLL screen of the AD9129 SPI GUI


Load Pattern from the DPG2
~~~~~~~~~~~~~~~~~~~~~~~~~~

Open DPGDownloader (Start > Programs > Analog Devices > DPG > DPGDownloader). Ensure that the program detects the AD9119, as indicated in the “Evaluation Board” drop-down list, and select it. For this evaluation board, LVDS is the only valid Port Configuration, and it will be selected automatically. The “Data Clock Frequency” window may not yet show a clock frequency, but it normally does.


|image8|

.. container:: centeralign

   Figure 5. Choose “Cable Infrastructure” as the vector type


Click on “Add Generated Waveform”, and then “Cable Infrastructure”, as shown in Figure 5. A Cable Infrastructure panel will be added to the vector list. Enter the sample rate, or DAC clock frequency, 2.455125946 GHz. Next, choose the “Resolution” to be 14 bits. Choose a center frequency of 108 MHz. Keep “Relative Amplitude” as 0 dB, and “Number of Channels” as ‘1’. Then, click the “Add Channels” button. The signal should appear on the list of signals as shown in Figure 6.



|image9|

.. container:: centeralign

   Figure 6. DPG Downloader Upper section, used to select and configure the desired signal to be generated


Next, in the lower portion of the screen, select “1I: CIFR Vector (I)” as the Data Vector. The other options can be left at their default values. The Data Clock Out (DCO) frequency from the AD9119 should be reported in the Data Clock Frequency window as roughly 613.69 MHz.



|image10|

.. container:: centeralign

   Figure 7. DPG Downloader Lower section, used to select the desired vector and download it to the DPG2 unit


Make sure the DPG2 unit is powered up and the AD9119 eval board is plugged into it correctly. Click the "Download" button (|image11|) to download the pattern from the computer to the DPG2 unit, wait for the Play (|image12|) button to become active, and then click the Play (|image13|) button to begin vector playback to the AD9119.

Enable the LVDS Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~

On the AD9129 SPI GUI’s “DLL” tab, the “DUTY Corr Ena” button and the “DLL_ENA” button should be green (selected). Click the (|image14|) button to program the registers. The Readback light next to both buttons should change from red to green, and the DLL Lock light should change from red to green. It may be necessary to click the (|image15|) button again to get a full readback status since the controller may take slightly longer to lock than the GUI allowed on the first write and then readback.


|image16|

.. container:: centeralign

   Figure 8. DLL screen of the AD9129 SPI GUI


In rare cases, the data link may have gotten corrupted and the registers not programmed correctly. In these cases, the output of the DAC will show significantly degraded performance. To remedy this situation, click the “DUTY Corr Ena” button and the “DLL_ENA” buttons, and then click the (|image17|) button to program the registers. Then, re-click the “DUTY Corr Ena” button and the “DLL_ENA” buttons, and then click the (|image18|) button to program the registers. This disables and re-enables the Data Interface DLL and allows it to re-lock to the DCI. At this time, it is also possible to click the "Repeat" button (|image19|) to continuously program the part, making the SPI GUI run in a more interactive mode.

Result
~~~~~~

The final result should be a single 256-QAM carrier centered at 108 MHz, as shown in Figure 9. An attenuation of 10 dB was used in this measurement, which raises the noise floor of the measurement, but avoided saturating the input and causing higher-ordered products from being created. A second plot is shown in Figure 10, in which the attenuation was reduced to 6 dB. It can be seen that the third harmonic increased in amplitude by about 6 dB, and the noise floor reduced by 4 dB, indicating the input of the spectrum analyzer is affecting the measurement.


|image20|

.. container:: centeralign

   Figure 9. Single 256-QAM channel at AD9129 output


   |image21|

.. container:: centeralign

   Figure 10. 256-QAM channel at AD9129 output with 6 dB attenuation setting on spectrum analyzer input


Mix-Mode Operation
~~~~~~~~~~~~~~~~~~

The AD9119-MIX-EBZ is equipped with a wideband balun to enable operation in the second and third Nyquist zones. To enable mix-mode, press the “Mix-Mode?” button on the Common screen to make it turn green, as shown in Figure 11.


|image22|

.. container:: centeralign

   Figure 11. Common tab showing mix-mode enabled. Also showing 2x interpolator mode enabled with the FIR40 filter chosen.


When using mix-mode and targeting a signal to the second Nyquist zone, it is important to remember that the center frequency chosen in the DPG window is the offset from the DACCLK sample frequency, not 0 Hz. For example, to place the carrier at 1982.5 MHz with a 2.4576 GHz DACCLK as in Figure 12, program the DPG Downloader center frequency to 475 MHz and enable mix-mode. Figure 12 shows the IMD performance of several different DAC output currents and the loss in output power expected with lower currents.

.. container:: column


   ..

|image23|

.. container:: column


   ..

|image24|

.. container:: centeralign

   Figure 12. Single channel WDMA signal with different DAC output currents: 33mA vs. 28 mA (Left), 33mA vs. 24 mA (Right)


SPI Software
------------

The AD9129 SPI software is conveniently organized in a series of tabs that groups registers according to their functions. In this way, all registers associated with the fDAC PLL, for example, are on the “PLL” tab, all registers associated with the data clock Delay Locked Loop (DLL) are on the “DLL” tab, and so on. A full description of each register and its settings is given in the AD9119/AD9129 data sheet. Some of the registers and their functions are described here as they pertain to the AD9119 evaluation board. Please note that some of the screen images in this document may not match exactly with the latest revision of the software, due to ongoing improvements and enhancements to the software. The full screen layout is shown in Figure 13. The tabs can be seen across the top of the work area, and a “READBACK” area is below the active tab area. This READBACK section is present on each of the tabs, so that the user can quickly assess status of the PLL and DLL lock, as well as parity and the FIFO phase. Each of the tabs is discussed in its own section below.


|image25|

.. container:: centeralign

   Figure 13. Common tab on the AD9129 SPI GUI


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

   Figure 14. PLL tab of the AD9129 SPI GUI



DLL Tab
~~~~~~~

.. container:: column

   The DLL tab has the DLL Enable and Duty Cycle Correction Enable bits as discussed in the Getting Started section. Additional status bits associated with the Data interface DLL are also on this tab, including lock status bits, lock lost bit, warning bits, etc. These are mostly located in the Data Control and Data Status registers, regs 0x0A – 0x0F. The bypass delay cell area is for test only and can be ignored.


.. container:: column



   ..

|image27|

.. container:: right centeralign

   Figure 15. DLL tab of the AD9129 SPI GUI



FIFO Tab
~~~~~~~~

.. container:: column

   The FIFO tab has controls and status lights associated with the data interface FIFO. For most uses of the AD9119 EVB, these controls can be left in their default state, and there is no need to change them in the SPI. For more details on the FIFO’s operation and the control and status registers for it, please consult the AD9119/AD9129 Data Sheet. The FIFO registers are located in address range 0x11 – 0x17.


.. container:: column



   ..

|image28|

.. container:: right centeralign

   Figure 16. FIFO tab of the AD9129 SPI GUI



Parity Tab
~~~~~~~~~~

.. container:: column

   Similar to the FIFO tab, the Parity tab can be left in its default state for most uses of the AD9119 EVB. Parity can be enabled and disabled on this tab, and Even or Odd Parity can be chosen. The parity counter values are also shown. These controls and status bits are associated with the parity registers located at addresses 0x5C – 0x5E. The parity interrupts are in the Interrupt Control and Status registers, 0x03 – 0x06. To reset the parity counters, click the PARITY_FALL_RESET and PARITY_RISE_RESET buttons, then press the |image29| button repeatedly until the values are reset. Alternatively, the |image30| button can be pressed, and then the SPI programming will run in a loop, and the count values can be observed to go to ‘0’, at which time the PARITY_FALL_RESET and PARITY_RISE_RESET buttons can be unclicked.


.. container:: column



   ..

|image31|

.. container:: right centeralign

   Figure 17. FIFO tab of the AD9129 SPI GUI



Power Control (PD) Tab
~~~~~~~~~~~~~~~~~~~~~~

.. container:: column

   The Power Control, or Power Down, tab contains individual controls to power down various blocks on the AD9119. These are associated with the power down registers, 0x01 and 0x02.


.. container:: column



   ..

|image32|

.. container:: right centeralign

   Figure 18. Power Down tab of the AD9129 SPI GUI



Analog Tab
~~~~~~~~~~

.. container:: column

   On the Analog tab, the Full Scale Current of the DAC output can be set by using the increment/decrement arrows or by typing an integer value into the yellow window. This updates registers 0x20 and 0x21 with the new value. The other controls on this tab should be left to their default values.


.. container:: column



   ..

|image33|

.. container:: right centeralign

   Figure 19. Analog control tab of the AD9129 SPI GUI



Save/Load Tab
~~~~~~~~~~~~~

.. container:: column

   The Save/Load tab enables a different way of configuring the AD9119. The “Save” function allows a user to save to a file all of the settings currently set in the various tabs. The “Load” function allows these settings to be recalled and loaded at a later date. While useful in some situations, this method of loading saved settings does not modify the screens or the tabs, it simply loads the settings directly to the DAC, so it can be confusing to use this function. It is recommended that the user begin with the user GUI and tab interface, and only use this “Save/Load” function as an advanced feature.


.. container:: column



   ..

|image34|

.. container:: right centeralign

   Figure 20. Save/Load tab of the AD9129 SPI GUI



.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/bench_setup_9119_evb.png
   :width: 350px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure2_9129-MIX-EBZ.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure3.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure5.png
   :width: 500px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure6.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure6_9129-EBZ.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure7_9129-EBZ.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/Download.png
   :width: 15px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_pattern.png
   :width: 15px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_pattern.png
   :width: 15px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure9.png
   :width: 600px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/play_vi.png
   :width: 15px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/repeat_play_vi.png
   :width: 15px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure9_9129-EBZ.png
   :width: 500px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure10_9129-EBZ.png
   :width: 500px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure11_ad9129-mix-ebz.png
   :width: 500px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure12b_9129-MIX-EBZ.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9129/figure12a_9129-MIX-EBZ.png
   :width: 400px
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
