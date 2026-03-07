EVALUATING THE AD9246S ANALOG-TO-DIGITAL CONVERTER
==================================================

Preface
-------

| This user guide describes the :adi:`ad9246S` evaluation board which provides all of the support circuitry required to operate this product in its various modes and configurations. The application software used to interface with the devices is also described. The evaluation board has Tyco connectors that mate to the :adi:`HSC-ADC-EVALCZ <hsadcevalboard>` data capture board.
| The :adi:`ad9246S` and :adi:`ad9246` data sheets provide additional information and should be consulted when using the evaluation board. All documents and software tools are available at :adi:`www.analog.com/hsadcevalboard <hsadcevalboard>`. For additional information or questions, send an email to aero@analog.com.

Typical Measurement Setup
-------------------------

|image1|\

.. container:: centeralign

   \ *Figure 1. AD9246S Evaluation Board Connection (6V DC Wall Power)—*\ :adi:`EVAL-AD9246S <AD9246S>`\


Features
--------

-  Full featured evaluation board for the :adi:`ad9246S`
-  SPI interface for setup and control
-  External clocking
-  Balun/transformer input drive
-  On-board LDO regulator needing a single external 6 V, 2 A DC supply
-  VisualAnalog® and SPI controller software interfaces

Helpful Documents
-----------------

-  :adi:`AD9246S` military data sheet
-  :adi:`AD9246` data sheet
-  High speed ADC FIFO evaluation kits (:adi:`HSC ADC Data Capture Boards <hsadcevalboard>`)
-  High speed ADC FIFO evaluation kit Wiki Page (`HSC-ADC-EVALCZ <https://wiki.analog.com/resources/eval/hsc-adc-evalc>`_)
-  :adi:`AN-905 Application Note <an-905>`, *VisualAnalog\ TM Converter Evaluation Tool Version 1.0 User Manual*
-  :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*
-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`AN-835 Application Note <an-835>`, *Understanding High Speed ADC Testing and Evaluation*

Evaluation Board Files
----------------------

The evaluation board layout, BOM, and schematic files for the :adi:`EVAL-AD9246S <AD9246S>` board can be downloaded from the links below.

| **DISCLAIMER: The footprint used for layout on the evaluation board is provided for general reference only. The exact footprint required for mounting this device onto a printed circuit board will depend on the device lead forming and may differ from what is provided herein. It is recommended to generate specific footprint information from the users lead forming specifications when placing this device on the application printed circuit board.**
| ==== Artwork: ==== `09-046595-01a.zip <https://wiki.analog.com/_media/resources/eval/09-046595-01a.zip>`_
| ==== BOM: ==== `05-046595-01-a.zip <https://wiki.analog.com/_media/resources/eval/05-046595-01-a.zip>`_
| ==== Schematic: ==== `02_046595a_top_wiki.pdf <https://wiki.analog.com/_media/resources/eval/02_046595a_top_wiki.pdf>`_

Equipment Needed
----------------

-  Analog signal source and antialiasing filter
-  Sample clock source (Rohde-Schwarz SMA100A or similar low phase noise signal generator)
-  (1) 6.0 V, 2.5 A switching power supply, CUI EPS060250UH-PHP-SZ provided
-  (1) 6.0 V, 2 A switching power supply, RAI S060S200A1 provided
-  PC running Windows®
-  USB 2.0 port
-  :adi:`EVAL-AD9246S <AD9246S>` board
-  :adi:`HSC-ADC-EVALCZ <hsadcevalboard>` FPGA-based data capture kit

| 
| ===== Visual Analog Canvases and FPGA File Needed ===== The canvas files required to run the :adi:`EVAL-AD9246S <AD9246S>` board need to be downloaded, unzipped, and saved to an accessible location.
| The canvas files can be downloaded from here:
| `ad9246s_va_canvases.zip <https://wiki.analog.com/_media/resources/eval/ad9246s_va_canvases.zip>`_
| The FPGa file can be download from here:
| `ad9265_cmos.zip <https://wiki.analog.com/_media/resources/eval/ad9265_cmos.zip>`_

Getting Started
---------------

| This section provides quick start procedures for using the :adi:`EVAL-AD9246S <AD9246S>` board. Both the default and optional settings are described.

Configuring the Board
~~~~~~~~~~~~~~~~~~~~~

Before using the software for testing, configure the evaluation board as follows:

-  Connect the evaluation board to the data capture board, as shown in Figure 1.
-  Connect one 6 V, 2 A switching power supply (such as the Royal Access, Inc., S060S200A1 that is supplied) to the :adi:`EVAL-AD9246S <AD9246S>`.
-  Connect one 6 V, 2.5 A switching power supply (such as the supplied CUI, Inc., EPS060250UH-PHP-SZ) to the :adi:`HSC-ADC-EVALCZ <hsadcevalboard>` board.
-  Connect the :adi:`HSC-ADC-EVALCZ <hsadcevalboard>` board (P702) to the PC using a USB cable.
-  On the ADC evaluation board, confirm that the correct jumpers are installed.

   -  Jumpers should be placed P204, P205, P203, and P206
   -  Additionally, jumpers should be placed on pins 1-2, pins 4-5, and pins 8-9 of P500.
   -  See Figure 2 as well as Table 1 for more details.

-  On the ADC evaluation board, use a clean signal generator with low phase noise to provide an input signal to the :adi:`AD9246S` analog input. Use a 1 m, shielded, RG-58, 50 Ω coaxial cable to connect the signal generator. For best results, use a narrow-band, band-pass filter with 50 Ω terminations and an appropriate center frequency. (Analog Devices, Inc., uses TTE, Allen Avionics, and K&L band-pass filters.)

Evaluation Board Hardware
-------------------------

| The evaluation board provides the support circuitry required to operate the :adi:`AD9246S` in its various modes and configurations. Figure 1 shows the typical bench characterization setup used to evaluate AC performance. It is critical that the signal sources used for the analog input and clock have very low phase noise (<1 ps rms jitter) to realize the optimum performance of the signal chain. Proper filtering of the analog input signal to remove harmonics and lower the integrated or broadband noise at the input is necessary to achieve the specified noise performance.
| See the evaluation board page linked from the :adi:`AD9246S` product page for the complete schematics and bill of materials (BOM). The evaluation board layout is available upon request. The layout diagrams demonstrate the routing and grounding techniques that should be applied at the system level when designing application boards using this converter.
| ==== Power Supplies ==== This evaluation board comes with a wall-mountable switching power supply that provides a 6 V, 2 A maximum output. Connect the supply to a 100 V ac to 240 V ac, 47 Hz to 63 Hz wall outlet. The output from the supply is provided through a 2.1 mm inner diameter jack that connects to the printed circuit board (PCB) at P200. The 6 V supply is fused and conditioned on the PCB before connecting to the low dropout linear regulators that supply the proper bias to each of the various sections on the board.
| The evaluation board can be powered in a nondefault condition using external bench power supplies. To do this, remove the all the jumpers listed above (and in Table 1) to disconnect the outputs from the on-board LDOs. This enables the user to bias each section of the board individually. Use P202 and P201 to connect a different supply for each section. A 1.8 V, 0.5 A supply is needed for 1.8 V_AVDD, a 2.5 V, 0.5 A supply is needed for DRVDD, a 2.5 V 0.5 A supply is needed for V-DIG, and a 3.3 V, 0.5 A supply is needed for 3P3V.

Input Signals
~~~~~~~~~~~~~

| When connecting the ADC clock and analog source, use clean signal generators with low phase noise, such as the Rohde & Schwarz SMA signal generator or an equivalent. Use a 1 m shielded, RG-58, 50 Ω coaxial cable for connecting to the evaluation board. Enter the desired frequency and amplitude (see the Specifications section in the :adi:`ad9246S` data sheet). When connecting the analog input source, use of a multipole, narrow-band band-pass filter with 50 Ω terminations is recommended. Analog Devices uses band-pass filters from TTE and K&L Microwave, Inc. Connect the filters directly to the evaluation board.
| If an external clock source is used, it should also be supplied with a clean signal generator as previously specified. Analog Devices evaluation boards typically can accept ~2.8 V p-p or 13 dBm sine wave input for the clock.

Output Signals
~~~~~~~~~~~~~~

The :adi:`ad9246S` evaluation board uses the Analog Devices high speed converter evaluation platform (:adi:`HSC-ADC-EVALCZ <hsadcevalboard>`) for data capture. The :adi:`ad9246S` digital outputs from the ADC are routed to through buffer U500 and on to Connector P600 using 50 Ω traces. For more information on the data capture board and its optional settings, visit :adi:`www.analog.com/hsadcevalboard <hsadcevalboard>`.

Jumper Settings
---------------

| Set the jumper settings/link options on the evaluation board for the required operating modes before powering on the board. The functions of the jumpers for the board are described in Table 1. Figures 2 shows the default jumper settings.

Table 1. Jumper Settings for the AD9246S Evaluation Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Jumper | Description                                                                                                                                                                                                                        |
+========+====================================================================================================================================================================================================================================+
| P204   | This jumper sets up the 1.8 V power supply voltage for the :adi:`ad9246S` AVDD supply input.                                                                                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P205   | This jumper sets up the 2.5 V power supply voltage for the :adi:`ad9246S` DRVDD supply input.                                                                                                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P203   | This jumper sets up the 3.3 V power supply voltage for the OTR circuitry.                                                                                                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P206   | This jumper sets up the 2.5 V power supply voltage for the digital output buffer and SPI buffer for the :adi:`ad9246S` digital outputs and serial SPI control.                                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P500   | By defaults jumpers connect pins 1-2, 4-5, and 8-9 to allow the FPGA on the :adi:`HSC-ADC-EVALCZ <hsadcevalboard>` data capture board to drive the :adi:`ad9246S` SPI interface.                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| |image2|\

.. container:: centeralign

   \ *Figure 2. Default Jumper Connections for* :adi:`EVAL-AD9246S <AD9246S>` *Evaluation Board*\


Power
~~~~~

| Plug the switching power supply into a wall outlet rated at 100 V ac to 240 V ac, 47 Hz to 63 Hz. Connect the DC output connector to P200 on the evaluation board.

Analog Input
~~~~~~~~~~~~

| The analog input on the evaluation board is set up for a double balun-coupled analog input with a 50 Ω impedance. The default analog input configuration supports analog input frequencies of up to ~300 MHz. For additional information on recommended input networks, see the :adi:`AD9246S` data sheet.

Clock
~~~~~

The default clock input circuit connects to the Nyquist clock input of the :adi:`AD9246S`. The clock is derived from a simple transformer-coupled circuit using a high bandwidth 1:1 impedance ratio transformer (T400) that adds a low amount of jitter to the clock path. The clock input is 50 Ω terminated and ac-coupled to handle single-ended sine wave types of inputs. The transformer converts the single-ended input to a differential signal before entering the ADC clock inputs. The clock input for the clock is the CLK+ SMA connector J400.

How To Use The Software For Testing
-----------------------------------

Setting up the ADC Data Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| After configuring the board, set up the ADC data capture using the following steps:

-  Open VisualAnalog on the connected PC. The appropriate part type should be listed in the status bar of the **VisualAnalog – Existing Canvas** window. Navigate to the location where the AD9246S canvases have been store and select the template that corresponds to the type of testing to be performed (see Figure 3a). Click the "Open" button. |image3|\

.. container:: centeralign

   \ *Figure 3a. VisualAnalog, Existing Canvas Window*\


-   Once Visual Analog opens click on the settings in the ADC Data Capture block to select the appropriate FPGA bin file for the AD9246S. For this product the FPGA bin file is AD9265_CMOS.bin. Download this file from this Wiki page and save to a known location such as the one shown in Figure 3B. Select this file and click the **Program** button. (See Figure 3b)

|image4|\

.. container:: centeralign

   \ *Figure 3b. VisualAnalog, Programming the FPGA for the AD9246S*\


-  To change features to settings other than the default settings, click the **Expand Display** button, located in the bottom right corner of the window (see Figure 4), to see what is shown in Figure 5.
-  Change the features and capture settings by consulting the detailed instructions in the :adi:`AN-905 Application Note <AN-905>`, *VisualAnalog\ TM Converter Evaluation Tool Version 1.0 User Manual*. After the changes are made to the capture settings, click the **Collapse Display** button.

\\\\\


|image5|

.. container:: centeralign

   \ *Figure 4. VisualAnalog Window Toolbar, Collapsed Display*\


.. container:: centeralign

   \ |image6|\


.. container:: centeralign

   \ *Figure 5. VisualAnalog, Main Window, Expanded Display*\


Evaluation And Test
-------------------

Setting up the SPI Controller Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| After the ADC data capture board setup is complete, set up the SPI controller software using the following procedure:

-  Open the SPI controller software by going to the **Start** menu or by double-clicking the **SPIController** software desktop icon. If prompted for a configuration file, select the appropriate one. If not, check the title bar of the window to determine which configuration is loaded. If necessary, choose **Cfg Open** from the **File** menu and select the appropriate file based on your part type. Note that the **CHIP ID(1)** box should be filled to indicate whether the correct SPI controller configuration file is loaded (see Figure 6). |image7|\

.. container:: centeralign

   \ *Figure 6. SPI Controller, CHIP ID(1) Box*\


-  Click the **New DUT** button in the **SPIController** window (see Figure 11).\ |image8|\

.. container:: centeralign

   \ *Figure 7. SPI Controller, New DUT Button*\


-  In the **ADCBase 0** tab of the **SPIController** window, various selections can be made to change the device settings for the :adi:`ad9246S`. For additional information, refer to the data sheet, the :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*, and the :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*.\



|image9|

.. container:: centeralign

   \ *Figure 8. SPI Controller, ADCBase0*\


-  Click the **Run** button in the **VisualAnalog** toolbar (see Figure 9). |image10|\

.. container:: centeralign

   \ *Figure 9. Run Button (Encircled in Red) in VisualAnalog Toolbar, Collapsed Display*\


Adjusting the Amplitude of the Input Signal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The next step is to adjust the amplitude of the input signal for each channel as follows:

-  Adjust the amplitude of the input signal so that the fundamental is at the desired level. Examine the **Fund Power** reading in the left panel of the **VisualAnalog Graph - AD9246S FFT** window (see Figure 9).\ |image11|\

.. container:: centeralign

   \ *Figure 9. Graph Window of VisualAnalog*


-  Click the disk icon within the **VisualAnalog Graph - AD9246S FFT** window to save the performance plot data as a .csv formatted file.

Troubleshooting Tips
--------------------

If the FFT plot appears abnormal, do the following:

-  If you see an abnormal noise floor, go to the **ADCBase0** tab of the **SPIController** window and toggle the **Chip Power Mode** in **MODES(8)** from **Chip Run** to **Reset** and back.
-  If you see a normal noise floor when you disconnect the signal generator from the analog input, be sure that you are not overdriving the ADC. Reduce the input level if necessary.
-  In VisualAnalog, click the **Settings** icon in the **Input Formatter** block. Check that **Number Format** is set to the correct encoding (offset binary by default). Repeat for the other channels.

If the FFT appears normal but the performance is poor, check the following:

-  Make sure that an appropriate filter is used on the analog input.
-  Make sure that the signal generators for the clock and the analog input are clean (low phase noise).
-  Change the analog input frequency slightly if noncoherent sampling is being used.
-  Make sure that the SPI configuration file matches the product being evaluated.

If the FFT window remains blank after **Run** in VisualAnalog (see Figure 9) is clicked, do the following:

-  Make sure that the evaluation board is securely connected to the :adi:`HSC-ADC-EVALCZ <hsadcevalboard>` board.
-  Make sure that the FPGA has been programmed by verifying that the **DONE** LED is illuminated on the :adi:`HSC-ADC-EVALCZ <hsadcevalboard>` board. If this LED is not illuminated, make sure that the U4 switch on the board is in the correct position for USB CONFIG.
-  Make sure that the correct FPGA program was installed by clicking the **Settings** icon in the **ADC Data Capture** block in VisualAnalog. Then select the **FPGA** tab and verify that the proper FPGA bin file is selected for the part.

If VisualAnalog indicates that the **FIFO Capture timed out**, do the following:

-  Make sure that all power and USB connections are secure.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_eval_board_connections.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_eval_board_jumpers.jpg
   :width: 850px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_va_canvas_select.png
   :width: 450px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_program_fpga.png
   :width: 450px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_expand_display.jpg
   :width: 1100px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_va_fft.png
   :width: 850px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_spicontroller_adcglobal.png
   :width: 750px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_spicontroller_adcglobal_newdut.png
   :width: 750px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_spicontroller_adcbase0.png
   :width: 750px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_va_run_button.jpg
   :width: 950px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/ad9246s_fft.png
   :width: 600px
