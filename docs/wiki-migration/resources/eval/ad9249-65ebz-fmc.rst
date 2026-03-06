EVALUATING THE AD9249 ANALOG-TO-DIGITAL CONVERTER (FMC Compatible Board)
========================================================================

Preface
-------

| This user guide describes the :adi:`AD9249` evaluation board :adi:`AD9249-65EBZ <AD9249>`, which provides the support circuitry required to operate the ADC in its various modes and configurations. The board described here is the version with the FMC connector that interfaces with the HSC-ADC-EVALEZ FPGA board. The application software used to interface with the device is also described.
| The :adi:`AD9249` data sheet provides additional information and should be consulted when using the evaluation board. All documents and software tools are available at :adi:`www.analog.com/hsadcevalboard <hsadcevalboard>`. For additional information or questions, send an email to highspeed.converters@analog.com.

Typical Measurement Setup
-------------------------

|image1|

.. container:: centeralign

   *Figure 1. Evaluation Board Connection—*\ :adi:`AD9249-65EBZ <AD9249>` *(on Left) and* :adi:`HSC-ADC-EVALEZ <hsadcevalboard>` *(on Right)*


Features
--------

-  SPI interface for setup and control
-  External, on-board oscillator
-  On-board LDO regulator or switching regulator, needing a single external 6V, 2A dc supply
-  ADC VREF configurable for ADC-internal reference, on-board reference, off-board reference
-  VisualAnalog® and SPIController software interfaces

Helpful Documents
-----------------

-  :adi:`AD9249` data sheet
-  High speed ADC FIFO evaluation kit (:adi:`HSC-ADC-EVALEZ <hsadcevalboard>`)
-  HSC-ADC-EVALEZ Wiki Guide :doc:`hsc-adc-evale </wiki-migration/resources/eval/hsc-adc-evale>`
-  :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter Evaluation Tool Version 1.0 User Manual*
-  :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*
-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*

Design and Integration Files
----------------------------

-  :adi:`Schematics, layout files, bill of materials <static/imported-files/eval_boards/AD9249_Design_Integration.zip>`

Equipment Needed
----------------

-  Analog signal source(s) and antialiasing filter(s)
-  Sample clock source (if not using the on-board crystal oscillator)
-  Switching power supply (6.0V, 2.5A) for AD9249-65EBZ
-  Switching power supply (12V, 3,3A) for HSC-ADC-EVALEZ
-  PC running Windows®
-  USB 2.0 port
-  :adi:`AD9249-65EBZ <AD9249>` board
-  :adi:`HSC-ADC-EVALEZ <hsadcevalboard>` FPGA-based data capture kit

Getting Started
---------------

| This section provides quick start procedures for using the :adi:`AD9249-65EBZ <AD9249>` board. Both the default and optional ADC settings are described.

Configuring the Board
~~~~~~~~~~~~~~~~~~~~~

Before using the software for testing, configure the evaluation board as follows:

-  Connect the evaluation board to the data capture board, as shown in Figure 1.
-  On the ADC evaluation board, confirm that the jumpers are installed as shown in Figure 2.
-  Connect one 6V, 2.5A switching power supply (such as the CUI, Inc., EPS060250UH-PHP-SZ that is supplied) to the :adi:`AD9249-65EBZ <AD9249>`.
-  Connect the 12V, 3.3A switching power supply to the :adi:`HSC-ADC-EVALEZ <hsadcevalboard>` board.
-  Connect the :adi:`HSC-ADC-EVALEZ <hsadcevalboard>` board (P702) to the PC using a USB cable.
-  On the ADC evaluation board, use a clean signal generator with low phase noise to provide an input signal to the desired channel(s). Use a shielded, RG-58, 50Ω coaxial cable (optimally 1 m or shorter) to connect the signal generator. For best results, use a narrow-band, band-pass filter with 50Ω terminations and an appropriate center frequency. (Analog Devices, Inc. uses TTE, Allen Avionics, and K&L band-pass filters.)

Evaluation Board Hardware
-------------------------

| The evaluation board provides the support circuitry required to operate the :adi:`AD9249` in its various modes and configurations. Figure 1 shows the typical bench characterization setup used to evaluate AC performance. It is critical that the signal sources used for the analog input and clock have very low phase noise (ideally ~100 fs rms jitter) to realize the optimum performance of the signal chain. Proper filtering of the analog input signal to remove harmonics and lower the integrated or broadband noise at the input is necessary to achieve the specified noise performance.
| See :adi:`AD9249 Design Support <static/imported-files/eval_boards/AD9249_Design_Integration.zip>` for the schematics and layout diagrams. These diagrams demonstrate the routing and grounding techniques that should be applied at the system level when designing application boards using these converters.

Power Supplies
~~~~~~~~~~~~~~

| This evaluation board comes with a wall-mountable switching power supply that provides a 6V, 2A maximum output. Connect the supply to a 100V ac to 240V ac, 47Hz to 63Hz wall outlet. The output from the supply is provided through a 2.1mm inner diameter jack that connects to the printed circuit board (PCB) at P101. The 6V supply is fused and conditioned on the PCB before connecting to the low dropout linear regulators that supply the proper bias to each of the various sections on the board.
| The evaluation board can be powered in a nondefault condition using external bench power supplies. To do this, remove the E102, E103, E110, and E113 ferrite beads to disconnect the on-board LDOs from the power planes. Note that in some board configurations some of these might already be uninstalled. P102 and P103 headers can be installed to facilitate connection of external bench supplies to the board. E106, E107, E108 and E109 need to be populated to connect P102 and P103 to the board power domains. A 1.8V , 0.5A supply is needed for both 1.8V_DUT_AVDD and 1.8V_DRVDD. Although the voltage requirements are the same for 1.8V_DUT_AVDD and 1.8V_DRVDD, it is recommended that separate supplies be used for each of these.
| Two additional supplies, 3.3V_CLK and 1.8V_DVDD, are used to power additional on board circuitry. If used, these supplies should each have at least 0.5A current capability.

Input Signals
~~~~~~~~~~~~~

| When connecting the ADC clock and analog source, use clean signal generators with low phase noise, such as the Rohde & Schwarz SMA, or an equivalent. Use a shielded, RG-58, 50Ω coaxial cable (optimally 1 m or shorter) for connecting to the evaluation board. Enter the desired frequency and amplitude (see the Specifications section in the data sheet). When connecting the analog input source, use of a multipole, narrow-band band-pass filter with 50Ω terminations is recommended. Analog Devices uses band-pass filters from TTE and K&L Microwave, Inc. Connect the filters as close to the evaluation board as possible.
| If an external clock source is used instead of the onboard crystal oscillator, it should also be supplied with a clean signal generator as previously specified for the analog input signals. Analog Devices evaluation boards typically can accept ~2.8V p-p or 13 dBm sine wave input for the clock at the board SMA clock connector. If an external off-board clock source is used, remove the jumper on J804, and C810, to disable and disconnect the on-board crystal oscillator.

Output Signals
~~~~~~~~~~~~~~

The default setup uses the Analog Devices high speed converter evaluation platform (:adi:`HSC-ADC-EVALEZ <hsadcevalboard>`) for data capture. The serial LVDS outputs from the ADC are routed to J1 and J2 using 100Ω differential traces. For more information on the data capture board and its optional settings, visit :adi:`www.analog.com/hsadcevalboard <hsadcevalboard>`.

Jumper Settings
---------------

| Set the jumper settings/link options on the evaluation board for the required operating modes before powering on the board. The functions of the jumpers are described in Table 1. Figure 2 shows the default jumper settings.

Table 1. Jumper Settings
^^^^^^^^^^^^^^^^^^^^^^^^

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Jumper | Description                                                                                                                                                                                                                            |
+========+========================================================================================================================================================================================================================================+
| J204   | Use this jumper to power down the ADC. Using the SPI, the PDWN pin can be configured to invoke the STBY (standby) function instead of power down.                                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P1     | This jumper sets the ADC for SPI communications with the :adi:`HSC-ADC-EVALEZ <hsadcevalboard>`.                                                                                                                                       |
|        | Connect Pin 1 to Pin 2 for SDIO, Pin 4 to Pin 5 for SCLK, Pin 8 to Pin 9 for CSB1 and Pin 11 to Pin 12 for CSB2.                                                                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J804   | This jumper enables the on-board crystal oscillator. Remove this jumper (and optimally C810) if an external off-board clock source is used.                                                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J202   | This jumper selects between internal V\ :sub:`REF` and external V\ :sub:`REF`.                                                                                                                                                         |
|        | To choose the ADC's internal 1V reference, connect Pin 3 (DUT_SENSE) to Pin 5 (GND) as shown in Figure 2.                                                                                                                              |
|        | To use the on-board :adi:`AD822` buffered reference, connect Pin 2 (DUT_SENSE) to Pin 1 (AVDD), and connect Pin 4 (DUT_VREF) to Pin 6 (EXT_REF). Adjust external VREF to be 1.0V using potentiometer R202.                             |
|        | To apply a reference voltage from an external off-board source, connect Pin 2 (DUT_SENSE) to Pin 1 (AVDD) and apply the reference voltage to Pin 4 (DUT_VREF). The AD9249 reference voltage is specified to be 1.0 V.                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| |image2|

.. container:: centeralign

   *Figure 2. Default Jumper Connections for* :adi:`AD9249-65EBZ <AD9249>` *Board*


Evaluation Board Circuitry
--------------------------

| This section explains the default and optional ADC settings or modes allowed on the :adi:`AD9249-65EBZ <AD9249>` board.

Power
~~~~~

| Connect the switching power supply that is supplied in the evaluation kit between a rated 100V ac to 240V ac, 47Hz to 63Hz wall outlet and P101.

Analog Input
~~~~~~~~~~~~

| The sixteen channel inputs on the evaluation board are set up for a double balun-coupled analog input with a 50Ω impedance. The default analog input configuration supports analog input frequencies of up to ~200 MHz.

RBIAS
~~~~~

| RBIAS has a default setting of 10 kΩ (R205 and R288) to ground and is used to set the ADC core bias current. Note that using a resistor value other than 10kΩ, 1% resistors for RBIAS1 and RBIAS2 may degrade the performance of the device.

Clock
~~~~~

| The default clock input circuit is derived from a simple transformer-coupled circuit using a high bandwidth 1:1 impedance ratio transformer (T801) that adds negligible jitter to the clock path. The clock input is 50 Ω terminated and ac-coupled to handle single-ended sinusoidal inputs. The transformer converts the single-ended input to a differential signal that is clipped by CR801 before entering the ADC clock inputs. The :adi:`AD9249` ADC is equipped with an internal clock divider (programmable divide ratios of 1 through 8) to facilitate usage with higher frequency clocks. When using the internal divider and a higher input clock frequency, remove CR801 to preserve the slew rate of the clock signal.
| The :adi:`AD9249-65EBZ <AD9249>` board is set up to be clocked through the transformer-coupled input network from the crystal oscillator, Y801. If a different clock source is desired, remove C810 (optional) and Jumper J804 to disable the oscillator from running and connect the external clock source to the SMA connector, J802 (labeled CLK+).

Modes of Operation
------------------

Standalone (PIN) Mode
~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD9249` ADC can operate in pin mode if there is no need to program and change the default modes of operation via the SPI. For applications that do not require SPI mode operation, the CSB1 and CSB2 pins are tied to 1.8V_DVDD by removing jumpers on Pin 8 and Pin 11 of P1. In this configuration SDIO/DFS (P1 Pin 2) controls the output data format, and SCLK/DTP (P1 Pin 5) controls the digital output test pattern. Table 2 and Table 3 specify the settings for pin mode operation.

Table 2. Digital Output Format Pin Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

======================================== ===============
SDIO/DFS (P1 Pin 2) Voltage              Device Mode
======================================== ===============
1.8V_DUT_AVDD (jumper P1 Pin 2 to Pin 3) Twos Complement
GND ("float" P1 Pin 2)                   Offset Binary
======================================== ===============

Table 3. Digital Test Pattern Pin Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

======================================== =================
SCLK/DTP (P1 Pin 5) Voltage              Output Format
======================================== =================
GND ("float" P1 Pin 5)                   Normal Operation
1.8V_DUT_AVDD (jumper P1 Pin 5 to Pin 6) 10 0000 0000 0000
======================================== =================

Note that the above settings only apply when CSB1 and CSB2 are tied high (P1 Pin 8 and Pin 11 "floating") at power up.

Additional information on the Standalone (PIN) Mode is provided in the :adi:`AD9249` data sheet.

Default Mode
~~~~~~~~~~~~

To operate the device under test (DUT) using the SPI, follow the jumper settings for P1 as shown in Table 1.

How To Use The Software For Testing
-----------------------------------

Setting up the ADC Data Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The installers for VisualAnalog and SPIController are in the following locations:
| `visualanalog_setup.exe <https://wiki.analog.com/ftp/ftp.analog.com/pub/hssp_sw/visualanalog/visualanalog_setup.exe>`__
| `spicontroller_setup.exe <https://wiki.analog.com/ftp/ftp.analog.com/pub/adispi/a2dcomponents/install/spicontroller_setup.exe>`__
| Run these installers on the PC that is connected to the evaluation setup before proceeding.

| After configuring the board hardware, set up the ADC data capture using the following steps:

-  Start VisualAnalog on the connected PC. The appropriate part type should be listed in the status bar of the **VisualAnalog – New Canvas** window. Select the template that corresponds to the type of testing to be performed (see Figure 3).\ |image3|\

.. container:: centeralign

   \ *Figure 3. VisualAnalog, New Canvas Window*\


\* After the template is selected, a message might appear asking if the default configuration can be used to program the FPGA (see Figure 4). If this message appears, click **Yes**, and the window will close.
   |image4|\

.. container:: centeralign

   \ *Figure 4. VisualAnalog Default Configuration Message*\


-  To view the canvas and associated functional blocks, click the **Expand Display** button, located on the bottom right corner of the window (see Figure 5), to see what is shown in Figure 6.

| |image5|

.. container:: centeralign

   \ *Figure 5. VisualAnalog Window Toolbar, Collapsed Display*

   |


\



|image6|

.. container:: centeralign

   \ *Figure 6. VisualAnalog, Main Window Expanded Display*\


4. To configure VisualAnalog to operate with the AD9249, push the Settings button on the ADCDataCapture block, as shown in Figure 7.



|image7|

.. container:: centeralign

   \ *Figure 7. VisualAnalog ADC Data Capture Block*\


| 5. In the ADC Data Capture Settings Window, General Tab, select AD9249 to be the device, enter the sample clock frequency (65 is the default value), as shown in Figure 8. The sample frequency entered here is used for scaling of frequency values in test results and graphs. In the Output Data field, the channels to be tested are selected, as well as the FFT capture depth ("Length"). Note that the total of the capture depths for all selected channels cannot exceed 256k. |image8|

.. container:: centeralign

   \ *Figure 8. VisualAnalog ADC Data Capture Settings Window, General Tab*\


| 6. In the ADC Data Capture Settings Window, Capture Board Tab, enter 30 in the Fill Delay field. Push the Browse button to navigate to the FPGA program file for the AD9249. The default installation location and filename will be similar to: C:\\Program Files\\Analog Devices\\VisualAnalog\\Hardware\\HADv6\\AD9249_hadv6.mcs
| Push the **program button**. |image9|

.. container:: centeralign

   \ *Figure 9. VisualAnalog ADC Data Capture Settings Window, Capture Board Tab*\


| 7. VisualAnalog is now setup to work with the AD9249-65EBZ in the default condition. Other VisualAnalog features and capture settings are documented in the :adi:`AN-905 Application Note <AN-905>`, *VisualAnalog Converter Evaluation Tool Version 1.0 User Manual*.

Evaluation And Test
-------------------

Setting up the SPI Controller Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| After the ADC data capture board setup is complete, set up the SPI controller software using the following procedure:

-  Open the SPI controller software by going to the **Start** menu or by double-clicking the **SPIController** software desktop icon. If prompted for a configuration file, select .cfg file whose name begins with AD9249. If not prompted, check the title bar of the window to determine which configuration is loaded. If necessary, choose **Cfg Open** from the **File** menu and select the appropriate file based on your part type. Note that the **CHIP ID(1)** box should be filled to indicate whether the correct SPI controller configuration file is loaded (see Figure 10).\ |image10|\

.. container:: centeralign

   \ *Figure 10. SPI Controller, CHIP ID(1) Box*\


\* Click the **New DUT** button in the **SPIController** window (see Figure 11)\ |image11|\

.. container:: centeralign

   \ *Figure 11. SPI Controller, New DUT Button*\


\* In the **ADCBase 0** tab of the **SPIController** window, find the **CLOCK DIVIDE(B)** box (see Figure 12), and the **MODES(8)** box (see Figure 13). If using the clock divider, use the drop-down box to select the correct clock divide ratio, if necessary. If there is any interruption of the ADC clock during power-up or during operation, a Digital Reset may be needed to re-initialize the ADC (Figure 13). For additional information, refer to the data sheet, the :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*, and the :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*.\ |image12|\

.. container:: centeralign

   \ *Figure 12. SPI Controller, CLOCK DIVIDE(B) Box*\


|image13|\

.. container:: centeralign

   \ *Figure 13. SPI Controller, Chip Power Mode - Digital Reset Selection*\


\* Note that other settings can be changed on the **ADCBase 0 tab** (see Figure 12) and the **ADC A** through **ADC H** tabs (see Figure 14) to set up the part in the desired mode. The **ADCBase 0** tab settings affect the entire part, whereas the settings on the **ADC A** through **ADC H** tabs each affect the selected channel only. The B1 (Bank1), B2 (Bank2) and All buttons at the right end of the SPIController button row (as seen in Figure 13 and Figure 14) determine which bank of ADCs is affected by the SPIController settings. The All button is pushed by default which means that the **ADCBase 0** tab settings affect all channels on both ADC banks. The settings in the **ADC A** through **ADC H** will likewise affect their respective channels in both banks. For example, with the All button pushed, settings in the **ADC A** tab will affect channels A1 and A2. If the All button is un-pushed and the B1 (Bank1) button remains pushed, the settings in the **ADC A** tab will only affect channel A1. See the data sheet, the :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*, and the :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*, for additional information on the available settings.\ |image14|\

.. container:: centeralign

   \ *Figure 14. SPI Controller, Example ADC A Page*\


\* Invoke a Digital Reset as shown in Figure 13 before testing. After selecting Reset, select Chip run to return to normal operation.
-  To begin testing, click the **Run** or **Continuous Run** button in the **VisualAnalog** toolbar (see Figure 15).\ |image15|\

.. container:: centeralign

   \ *Figure 15. Run/Continuous Run Buttons (Encircled in Red) in VisualAnalog Toolbar, Collapsed Display*\


Adjusting the Amplitude of the Input Signal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The next step is to adjust the amplitude of the input signal for each channel as follows:

-  Adjust the amplitude of the input signal so that the fundamental is at the desired level. Examine the **Fund Power** reading in the left panel of the **VisualAnalog Graph - AD9249 FFT** window (see Figure 16).\ |image16|\

.. container:: centeralign

   //Figure 16. Graph Window of VisualAnalog //


\* Repeat this procedure for the other channels, if desired
-  Click the floppy-disk icon within the **VisualAnalog Graph - AD9249 FFT** window to save the performance data as a .csv formatted file for plotting or analysis.

Troubleshooting Tips
--------------------

Lack of SPI communication will cause difficulty in configuring the ADC.

-  Go to the **Global** tab of the **SPIController** window and push the **Read** button in the **GENERIC READ/WRITE** window. This will read the contents of ADC register 0x00. If SPI communication is working properly and the ADC is powered up, the value 0x18 hexadecimal will appear. If the contents show 0x00, the ADC is not powered up or SPI communication is not working.
-  Check that there is correct power to the :adi:`AD9249-65EBZ <AD9249>` board, and to the :adi:`HSC-ADC-EVALEZ <hsadcevalboard>`.
-  Check that the USB cable is properly connected from the PC to the :adi:`HSC-ADC-EVALEZ <hsadcevalboard>`.
-  The LED on the **VisualAnalog ADCDataCapture** block should be green. If it is red, push the USB button on the same block to refresh the connection.

If the FFT plot appears abnormal, do the following:

-  If you see an abnormal noise floor, go to the **ADCBase0** tab of the **SPIController** window and toggle the **Chip Power Mode** in **MODES(8)** from **Chip Run** to **Reset** and back (Figure 13).
-  If you see a normal noise floor when you disconnect the signal generator from the analog input, be sure that you are not overdriving the ADC. Reduce the input level, if necessary.
-  In **VisualAnalog**, click the **Settings** icon in the **Input Formatter** block. Check that **Number Format** is set to the correct encoding (twos complement by default). Check that the **Number Format** in the **VisualAnalog Input Formatter** matches the data format selected in the **SPIController ADCBase0 OUTPUT MODE(14)** window. Repeat for the other channels.

If the FFT appears normal but the performance is poor, check the following:

-  Make sure that an appropriate filter is used on the analog input.
-  Make sure that the signal generators for the clock and the analog input are clean (low phase noise).
-  Change the analog input frequency slightly if noncoherent sampling is being used.
-  Make sure that the SPI configuration file matches the product being evaluated.

If the FFT window remains blank after **Run** in VisualAnalog (see Figure 15) is clicked, do the following:

-  Make sure that the evaluation board is securely connected to the :adi:`HSC-ADC-EVALEZ <hsadcevalboard>` board.
-  Make sure that the correct FPGA program was installed by clicking the **Settings** icon in the **ADC Data Capture** block in VisualAnalog. Then select the **FPGA** tab and verify that the proper FPGA .mcs file (one containing "AD9249" in the filename) is selected for the part.
-  Make sure that the FPGA has been programmed by verifying that the **DONE** LED is illuminated on the :adi:`HSC-ADC-EVALEZ <hsadcevalboard>` board. If the **DONE** LED is not illuminated, click the **Settings** icon in the **ADC Data Capture** block in VisualAnalog. Then select the **FPGA** tab and verify that the proper FPGA .mcs file (one containing "AD9249" in the filename) is selected for the part. Then push the **Program** button. The LED should light up.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/AD9249-65EBZ_top_level.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/AD9249_65ebz_default_jumpers.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/AD9249_VA_New_Canvas_window.PNG
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/10235-005.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/AD9249_VA_toolbar_collapsed.PNG
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/AD9249_VA_avg_FFT_window_2ch_expanded.PNG
   :width: 700px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/AD9656_ADC_DataCaptureSettings_button.PNG
   :width: 200px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/AD9249_ADC_DataCaptureSettings_GeneralTab.PNG
   :width: 500px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/AD9249_ADC_DataCaptureSettings_CaptureBoardTab.PNG
   :width: 500px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/AD9249_SPIController_Global_tab_ChipID.PNG
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/AD9249_spicontroller_global_tab_newdUT_button.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/AD9249_SPIController_ADCBase0_tab_ClkDiv.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/AD9249_SPIController_ADCBase0_tab_DigReset.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/AD9249_SPIController_ADCA_tab.PNG
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/AD9249_VA_toolbar_collapsed_run_button.PNG
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/AD9249_FFT_example.png
   :width: 600px
