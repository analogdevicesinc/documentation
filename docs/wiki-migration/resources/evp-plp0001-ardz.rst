EVP-PLP0001-ARDZ-User Guide
===========================

Supported Devices
=================

-  :adi:`AD4696`
-  :adi:`ADR3625`
-  `MAX41400 <https://www.maximintegrated.com/MAX41400>`__
-  `MAX77326 <https://www.maximintegrated.com/MAX77326>`__
-  `MAX40023 <https://www.maximintegrated.com/MAX40023>`__

Features
========

| The purpose of the board is to evaluate the low power signal chain presented in :adi:`precision-low-power.html <en/applications/technology/precision-technology/precision-low-power.html>`.
| This consists of: Low-power In Amp `MAX41400 <https://www.maximintegrated.com/MAX41400>`__, multi-channel ADC :adi:`AD4696` with low-power functionalities such as HiZ mode and the :adi:`ADR3625` precision micropower reference. EVP-PLP0001-ARDZ is compatible with the SDP-K1 board PC-based software for control and data analysis.

Evaluation Kit Contents
=======================

EVP-PLP0001-ARDZ evaluation board

Equipment Needed
================

-  System demonstration platform (SDP)—Controller board :adi:`SDP-K1`
-  PC running Windows Vista SP2 (32-bit or 64-bit), Windows 7 SP1 (32-bit or 64-bit), Windows 8.1 (32-bit or 64bit),or Windows 10 (32-bit or 64-bit) with a USB 2.0 port
-  DC/AC signal source

Software Needed
===============

-  :adi:`ACE` Board.PLP0001 ACE plugin
-  :adi:`SDP-K1` driver

General Description
===================

| The EVP-PLP0001-ARDZ is a evaluation board designed to evaluate the signal chain composed of the two banks through eight `MAX41400 <https://www.maximintegrated.com/MAX41400>`__, the reference :adi:`ADR3625`, the COM buffer `MAX40023 <https://www.maximintegrated.com/MAX40023>`__ and the ADC :adi:`AD4696` .The EVP-PLP0001-ARDZ can be controlled by the system demonstration platform, :adi:`SDP-K1` controller board via the Arduino Header connector. The *<fc #0000FF>SDP-K1</fc>* board controls the EVP-PLP0001-ARDZ through the USB port of the PC using the analysis, control, evaluation (ACE) software, which is available for download on the ACE software page. Note that the EVP-PLP0001-ARDZ has 8 channels direct to the 8 ADC inputs (ch0-ch7). Another 8 channels that are divided into two banks. Bank 0 which are channels ch8-ch11 and Bank 1 which are channels ch12-ch15. These two banks have implemented programmable gain amplifiers (PGA) that can be controlled through the software. Full details on the SDP-K1 board are available on the :adi:`SDP-K1` product page. The comprehensive ACE user guide is available on the :adi:`ACE` page.

.. container:: centeralign


|image1|

   |
   
   .. container:: centeralign

      //**Figure 1. EVP-PLP0001-ARDZ EVALUATION BOARD (LEFT) CONNECTED TO SDP-K1 BOARD (RIGHT)** //

   


The signal chain of the board is composed by direct inputs and two banks (Figure 2):

-  **Direct inputs** : Represents channels 0 to 7 and It can be driven directly to sensor.
-  **Bank0** : Represents channels 8 to 11 and is composed of 4 MAX41400 driven to ADC IN8 to IN11 inputs.
-  **Bank1** : Represents channels 12 to 15 and is composed of 4 MAX41400 driven to ADC IN12 to IN14 inputs.

|

.. container:: centeralign


|image2|

   |
   
   .. container:: centeralign

      //\**Figure 2. Direct channels and banks 0 and 1 \*\* //

   


These banks are configurable by software through two lines:

-  <fc #f4a460>Shutdown line</fc>: Through the signals SHDN_N_B0 (for bank 0) and SHDN_N_B1 (for bank 1) both signals coming from the Arduino form factor (If you use these signals, you will turn off the 4 MAX41400 of the bank, not the MAX41400 one by one). If you want to turn off/on each MAX41400 one by one there is the option to do it manually with headers P7,P8,P9 and P10 for channels 0 to 3 and P11,P13,P17 and P18 for channels 4 to 7(schematic pages 7 and 8).
-  <fc #87ceeb>Gain lines</fc>: Each bank can be controlled through the signals G1_B0 , G1_B0 for bank 0 and G1_B1, G1_B1 for bank 1. **This means that all 4 MAX41400 in each bank will have the same gain**.

|

.. container:: centeralign


|image3|

   |
   
   .. container:: centeralign

      //\**Figure 3. Control lines for banks 0 and 1 \*\* //

   


Evaluation Board Quick Start Guide
==================================

The EVP-PLP0001-ARDZ is powered by the SDP-K1 board by default. To evaluate the all the system take the following steps:

-  Download and install the ACE software, which is available on the AD4696 plug-in manager. Ensure that the SDP-K1 board is disconnected from the USB port of the PC when installing the ACE software. The PC may need to be restarted after the installation.

   -  You must be using ACE
   -  In the Plug In Manager, go to available packages and hit Refresh
   -  This can take several minutes so give it plenty time to refresh
   -  After installing the **Board.PLP0001** plug in, go to Available Updates tab and if there is an update for the plug in, install it.

-  Install libiio wrapper

::

     *Must select this option when installing ACE.
     *If ACE is already installed, open the Help tab in Ace and the installer is linked there
   * Find COM port in Device Manager Figure 23.
   * Ensure that the link options are configured as detailed in Table 1.
   * Connect the //<fc #0000FF>SDP-K1</fc>// board to the EVP-PLP0001-ARDZ via the Arduino connector.
   * Connect the //<fc #0000FF>SDP-K1</fc>// board to the PC via the USB cable.
   * If using Windows® XP, search for the //<fc #0000FF>SDP-K1</fc>// drivers. Choose to automatically search for the drivers for the SDP-K1 board if prompted by the operating system.
   * Launch the ACE software.
   * Add serial port to ACE.
     *Open Settings and select Serial Ports tab
     *Click the blue + button to add a new port and fill out with info as Figure 4.

.. container:: centeralign

   {{ :resources:ace_internal_serial.png?direct&400 |}}

   
   .. container:: centeralign

      //**Figure 4. Adding ports in ACE** //

   


-  Close ACE and load the correct firmware to the SDP-K1. If you have some familiarity with the Mbed platform, the following is a basic list of steps required to start running the code, see below for more details:.

.. admonition:: Download
   :class: download

   Latest firmware (Use below link):`EVP-PLP0001-ARDZ IIO Firmware Application <https://os.mbed.com/teams/AnalogDevices/code/EVAL-AD717x-AD411x-IIO/>`__

   


-  Import the code into `Keil Studio <https://studio.keil.arm.com/>`__ from `EVP-PLP0001-ARDZ IIO Firmware Application <https://os.mbed.com/teams/AnalogDevices/code/EVAL-AD717x-AD411x-IIO/>`__
-  Ensure SDP-K1 controller board is selected as the active target (Figure 5).

.. container:: centeralign

   \ |image4|\

   
   .. container:: centeralign

      //**Figure 5. SDP-K1 controller board selected as target** *

   


\* Set the imported project folder as active project (Right click on the plp_0001_mbed_iio-application→ Set Active Project). \* Make sure that all the dependent libraries are imported. This happens automatically when the active project has been configured. \* Compile the code by clicking on the option shown in the Figure 6.

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ **Figure 6. Compile the code** *

   


\* After a successful compile, a binary will be downloaded to your computer store this on your local drive.

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ **Figure 7. Generated bin file** *

   


\* Connect SDP-K1, open File Explorer and select the SDP-K1. It should appear as a device in This PC.

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ **Figure 8. SDP-K1 detected** *

   


\* Open a separate window where the .bin file is stored, copy the .hex file into the SDP-K1.

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ **Figure 9. SDP-K1 detected** //

   


-  Open ACE and the board will be detected by the **Board.PLP0001** plug in.
-  Connect an input signal to some channel.

Evaluation Board Connection Diagram
-----------------------------------

|

.. container:: centeralign


|image5|

   |
   
   .. container:: centeralign

      \ **Figure 10. Typical Setup of the EVP-PLP0001-ARDZ and the SDP-K1 Board**\

   


Evaluation Board Hardware
=========================

Link Configuration Options
--------------------------

Multiple link options must be set properly to select the appropriate operating setup before using the EVP-PLP0001-ARDZ. The functions of these options are detailed in Table 1.

Setup Conditions
~~~~~~~~~~~~~~~~

Ensure that all link positions are set as required by the selected operating mode before applying power and signals to the EVP-PLP0001-ARDZ. Table 1 shows the default positions of the links when the EVP-PLP0001-ARDZ is packaged.

**Table 1. Link Options for EVP-PLP0001-ARDZ**

+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link Name       | Function                                      | Default Position | Description                                                                                                                                                                           |
+=================+===============================================+==================+=======================================================================================================================================================================================+
| P9,P10,P7,P8    | Enable/Disable the MAX41400 output for Bank 0 | 3-4              | In position 3-4 you allow the control through the microcontroller. In position 2-4 you manually enable the MAX41400 output. In position 4-6 you manually disable the MAX41400 output. |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P11,P13,P17,P18 | Enable/Disable the MAX41400 output Bank 1     | 3-4              | In position 3-4 you allow the control through the microcontroller. In position 2-4 you manually enable the MAX41400 output. In position 4-6 you manually disable the MAX41400 output. |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P29             | Enable/Disable the 3.3V led control.          | 1-2              | It is used to check that the 3.3V power supply is working properly.                                                                                                                   |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P30             | Enable/Disable the 1.8V led control.          | 1-2              | It is used to check that the 1.8V power supply is working properly.                                                                                                                   |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P27             | Enable/Disable the SIMO MAX77642 output       | 4-6              | Connect in position 4-6 as there is no software developed to control via microcontroller.                                                                                             |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P26             | Enable/Disable the SIMO MAX77642 output       | 4-6              | Connect in position 4-6 as there is no software developed to control via microcontroller.                                                                                             |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P15             | Current measurement                           | 1-2              | It is used to measure the total current consumption of the complete system.                                                                                                           |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P16             | Current measurement                           | 1-2              | Used to measure the power consumption from SIMO MAX77642.                                                                                                                             |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P20             | Current measurement                           | 1-2              | Used to measure the power consumption from digital interface.                                                                                                                         |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P24             | Current measurement                           | 1-2              | Used to measure the power consumption from AD4696.                                                                                                                                    |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P25             | Current measurement                           | 1-2              | Used to measure the power consumption from AD4696 Input/Output Interface Digital Power.                                                                                               |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P14             | Select VREF/2 or an external ground           | 1-2              | Used to select between an external ground or the Vref/2 signal coming from the MAX40023 COM-BUFFER. These signals are sent to the COM pin of the ADC.                                 |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P21             | Current measurement                           | 1-2              | Used to measure the power consumption from ADR3625.                                                                                                                                   |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P22             | Current measurement                           | 1-2              | Used to measure the power consumption from MAX40023.                                                                                                                                  |
+-----------------+-----------------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Make sure that links **P27** and **P26** are in positions 4-6 for powering the EVP-PLP0001-ARDZ, as shown in the figure below. If everything is correct, LEDs D51 and D52 should be on.

.. container:: centeralign


|image6|

   |
   
   .. container:: centeralign

      \ **Figure 11. Links to enable 1.8V and 3.3V**\

   


Banks 0 and 1 can be enabled through the microcontroller in position **3-4 (default position)** as shown in Figure 12 or enable manually in position 2-4 Figure 13 (HI). It can also be manually shutdown by setting it to position 4-6 Figure 14 (LO).

.. container:: centeralign


|image7|

   |
   
   .. container:: centeralign

      \ **Figure 12. Default position for banks 0 and 1 (enable/disable through the microcontroller)**\

   


.. container:: centeralign


   


|image8|

   |
   
   .. container:: centeralign

      \ *\**Figure 13. Position 2-4 (manual enable) \*\**\

   


.. container:: centeralign


   


|image9|

   |
   
   .. container:: centeralign

      \ *\**Figure 14. Position 4-6 (manual disable) \*\**\

   


Evaluation Board Circuitry
==========================

Sockets and Connectors
----------------------

The test points on the EVP-PLP0001-ARDZ are described in Table 2. The default interface to the EVP-PLP0001-ARDZ is via the Arduino connector, which connects the EVP-PLP0001-ARDZ to the SDP-K1 board.

Test Points
===========

There are several test points on the EVP-PLP0001-ARDZ. These test points provide access to the evaluation board signals to allow probing, evaluation and debugging.

**Table 2. On-Board test points**

========= ============================================
Connector Function
========= ============================================
3.3V      3.3V host power supply
3.3VREG   3.3V regulated
1.8REG    1.8V regulated
VREF      Reference Voltage
COM       External ground or VREF/2
SIMO0     SBB0 MAX77642 output
SIMO1     SBB1 MAX77642 output
PD_B0     Power down bank 0
G1_B0     Pin 1 of the gain selector in bank 0
G2_B0     Pin 2 of the gain selector in bank 0
PD_B1     Power down bank 1
G1_B1     Pin 1 of the gain selector in bank 1
G2_B2     Pin 2 of the gain selector in bank 1
EN_REF    Enable reference
PD_BUF    Power down buffer
/CS       Chip Select Input for ADC SPI communication
SCK       Clock signal for ADC SPI communication
SDI       Serial Data Input for ADC SPI communication
SDO       Serial Data Output for ADC SPI communication
RESET     ADC Reset Input
CNV       Convert Input for ADC SPI communication
BUSY      ADC Busy Indicator
ALERT     ADC alert Indicator
EXTGND    External ground
========= ============================================

Evaluation Board Software
=========================

Software Installation Procedure
-------------------------------

Download the :adi:`ACE` software from the AD4696 product page and install the ACE software on the PC before using the EVP-PLP0001-ARDZ. The installation process consists of the ACE software installation and the SDP-K1 driver installation. To ensure that the evaluation system is recognized when it is connected to the PC, install the ACE software and SDP-K1 driver before connecting the EVP-PLP0001-ARDZ and the SDP-K1 board to the USB port of the PC.

Installing the ACE Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install the *<fc #0000FF>ACE</fc>* software, take the following steps:

-  Download the *<fc #0000FF>ACE</fc>* software to a Windows-based PC.
-  Double click the **ACEInstall.exe** file to begin the installation. By default, the software is saved to the following location: **C:\\Program Files (x86)\\Analog Devices\\ACE**.
-  A window appears asking for permission to allow the program to make changes to the PC. Click **Yes** to begin the installation process.
-  Click **Next** > to continue the installation, as shown in Figure 15.

.. container:: centeralign

   \ |image10|\

   
   .. container:: centeralign

      //**Figure 15. ACE Software Installation Confirmation** *

   


\* Allow to keep ACE updated to the latest versions (see Figure 16).

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ **Figure 16. Keep ACE updated** *

   


\* Read the software license agreement and click* **I Agree** *(see Figure 17).

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ \**Figure 17. License Agreement \*\* *

   


\* Choose an installation location and click* **Next >** *(see Figure 18).

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ \**Figure 18. Choose Installation Location \*\* *

   


\* Select the* **Prerequisites, High Speed DAC Components and Precision Converter Components** *checkbox to include the installation of the SDP-K1 driver and click* **Install** *(see Figure 19). The installation is in progress (see Figure 20).

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ \**Figure 19. Choose Components Section \*\* *

   


.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ \**Figure 20. Installation in Progress \*\* *

   


\* During the installation you will be requested to install the IIO drivers, select in the checkbox the* **LibIIO and LibIIODivers** *to install (see Figure 21).

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ \**Figure 21. Select components section to install IIO drivers \*\* *

   


\* When the installation is complete (see Figure 22), click* **Next >** *and then click* **Finish** *to complete.

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ \**Figure 22. Installation Completed \*\* //

   


Evaluation Board Setup Procedures
=================================

Figure 5 shows a diagram of the connections between the EVP-PLP0001-ARDZ and the SDP-K1 board. To ensure that the evaluation system is recognized when it is connected to the PC, install the ACE software and SDP-K1 driver before connecting the EVP-PLP0001-ARDZ and the SDP-K1 board to the USB port of the PC. When the ACE software installation is complete, set up the EVP-PLP0001-ARDZ and the SDP-K1 board as described in the following sections.

Connecting the EVP-PLP0001-ARDZ and the SDP-K1 Board to the PC
--------------------------------------------------------------

To connect the EVP-PLP0001-ARDZ and the SDP-K1 board to the PC, take the following steps:

-  Ensure that all configuration links are in the appropriate positions, as detailed in Table 1.
-  Connect the EVP-PLP0001-ARDZ securely to the Arduino connector on the SDP-K1 board. The EVP-PLP0001-ARDZ does not require an external power supply adapter.
-  Connect the SDP-K1 board to the PC via the USB cable enclosed in the SDP-K1 kit.
-  Connect SDP-K1 VIO_ADJUST to 3.3V − Header **P14 SDP-K1**.

Verifying Board Connection
--------------------------

To verify the board connection, take the following steps:

-  When the SDP-K1 board is plugged into the PC, allow the Found New Hardware Wizard to run. If using Windows XP, search for the SDP-K1 drivers. If prompted by the operating system, choose to automatically search for the drivers for the SDP-K1 board.
-  A window may appear asking for permission to allow the program to make changes to the computer. In this case, click Yes. The Computer Management window opens.
-  Under System Tools, click **Device Manager** and use the **Device Manager** window to ensure that the SDP-K1 board is connected to the PC properly. If the SDP-K1 driver software is installed and the board is connected to the PC properly, **SDP-K1** appears under **Portable Devices** in the **Device Manager window**, as shown in Figure 23.

.. container:: centeralign

   \ |image11|\

   
   .. container:: centeralign

      //\**Figure 23. Device Manager Window \*\* //

   


Disconnecting the EVP-PLP0001-ARDZ
----------------------------------

Always remove power from the SDP-K1 board and the EVP-PLP0001-ARDZ or click the reset tact switch located alongside the USB port before disconnecting EVP-PLP0001-ARDZ from the SDP-K1 board.

Using the ACE Software for Testing
==================================

Launching ACE Software
----------------------

When the EVP-PLP0001-ARDZ and SDP-K1 boards are properly connected to the PC, launch the ACE software. To launch the ACE software, take the following steps.

-  From the **Start** menu, select **All Programs** > **Analog Devices** > **ACE** > **ACE.exe** to open the main software window, as shown in Figure 24.

.. container:: centeralign

   \ |image12|\

   
   .. container:: centeralign

      //\**Figure 24. ACE Software Main Windows \*\* *

   


\* The EVP-PLP0001-ARDZ icon appears in the Attached Hardware section. If the EVP-PLP0001-ARDZ is not connected to the USB port via the SDP-K1 board when the software is launched, the EVP-PLP0001-ARDZ icon does not appear in the Attached Hardware section. In this case, connect the EVP-PLP0001-ARDZ and SDP-K1 board to the USB port of the PC, wait a few seconds, and then continue following these instructions. \* Double click the* **PLP0001 Board** *icon to open the window shown in Figure 25.

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ \**Figure 25. ACE Software Main Windows \*\* *

   


\* You can select the icons in dark blue* **AD4696, ADR3625 or GPIO Control** *these icons are programmable blocks. Click a dark blue block icons to open a configurable window that allows customization for data capture. By clicking on the* **ADR3625** *you can enable or disable it, on the other hand by entering* **GPIO CONTROL** *you can configure the gains of the two banks and its enable/disable and you can also enable/disable the buffer. In this case, double clicked in the AD4696 chip icon to open the window shown in Figure 26.

.. container:: centeralign

   \ \

   
   .. container:: centeralign

      *\ \**Figure 26. Chip View \*\* //

   


Memory Map Window Features
--------------------------

Click **Proceed to Memory Map** in the bottom right corner of the chip view (see Figure 26) to open the window shown in Figure 27. The memory map shows all AD4696 registers.

Apply Changes
~~~~~~~~~~~~~

The registers are in the default values at power up. To change the register values, click the + Icon next to the **Address (Hex)** column, then select the boxes that correspond to the configuration being edited. The values in the boxes toggle between 1 and 0. To apply the values changed to all registers, click **Apply Changes** to write to the registers.

Apply Selected
~~~~~~~~~~~~~~

In some cases, the values of every register have changed, but the user may want to only implement changes on a selected register. To select a specific register, click the register name and then click **Apply Selected** to write a new value on a selected register to the AD4696.

Read All
~~~~~~~~

Click **Read All** to read the values of all AD4696 registers.

Read Selected
~~~~~~~~~~~~~

To select a read, highlight the desired register to be read. Click **Read Selected** to read the selected AD4696 register(s).

Reset Chip
~~~~~~~~~~

Click **Reset Chip** to allow the software to reset the AD4696.

Diff
~~~~

Click **Diff** to check for differences in register values between the ACE software and the AD4696.

Software Defaults
~~~~~~~~~~~~~~~~~

To revert all register values back to the default values, click **Software Defaults** and then click **Apply Changes** to write to the AD4696.

.. container:: centeralign

   \ |image13|\

   
   .. container:: centeralign

      //\**Figure 27. Memory map view \*\* //

   


Analysis View
-------------

Click **Proceed to Analysis** in the bottom right corner of the chip view window (see Figure 28) to open the analysis view window shown in Figure 23. The analysis view contains the **Waveform tab**, **Histogram tab**, and **FFT tab**.

.. container:: centeralign

   \ |image14|\

   
   .. container:: centeralign

      //\**Figure 28. Analysis View \*\* //

   


Waveform Tab
~~~~~~~~~~~~

The Waveform tab displays data in the form of time vs discrete data values with the results, as shown in Figure 29. The Capture pane contains the capture settings, which reflect onto the registers automatically before data capture.

.. container:: centeralign

   \ |image15|\

   
   .. container:: centeralign

      //\**Figure 29. Waveform Tab \*\* //

   


Capture Pane
~~~~~~~~~~~~

The **Sample Count** dropdown list in the **General Capture Settings** section allows the user to select the number of samples per channel per capture.

Click **Run Once** in the **Device Settings** section to start a data capture of the samples at the sample rate specified in the **Sample Count** dropdown list. These samples are stored on the FPGA device and are only transferred to the PC when the sample frame is complete.

Click **Run Continuously** in the **Device Settings** section to start a data capture that gathers samples continuously with one batch of data at a time.

Waveform Graph
~~~~~~~~~~~~~~

The data waveform graph shows each successive sample of the ADC output. The user can zoom in on and pan across the waveform graph using the embedded waveform tools. The channels to display can be selected in the **Display Channels** section of the **Results** pane. Click the display unit’s dropdown list to select whether the data graph displays in units of Hex, volts, or codes Figure 30. The axis controls are dynamic. When selecting either y-scale dynamic or x-scale dynamic, the corresponding axis width automatically adjusts to show the entire range of the ADC results after each batch of samples.

.. container:: centeralign

   \ |image16|\

   
   .. container:: centeralign

      //\**Figure 30. Dropdown list \*\* //

   


Result Pane (Waveform Tab)
~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Display Channels** section allows the user to select which channels to capture. The data for a specific channel is only shown if that channel is selected before the capture. The **Waveform Results** section displays maximum and minimum amplitude, peak to peak, average, RMS data for the selected channels. Click **Export** in the **Results** pane to export captured data. The waveform, histogram, and fast Fourier transform (FFT) data is stored in .xml files along with the values of parameters at capture.

Histogram Tab
~~~~~~~~~~~~~

The **Histogram** tab contains the histogram graph and the **Results** pane, as shown in Figure 31. The **Results** pane displays the information related to the ADC performance. The histogram graph displays the number of hits per code within the sampled data. This graph is useful for dc analysis and indicates the noise performance of the device.

.. container:: centeralign

   \ |image17|\

   
   .. container:: centeralign

      //\**Figure 31. Histogram Tab \*\* //

   


FFT Tab
~~~~~~~

The **FFT tab** displays FFT information for the last batch of samples gathered, as shown in Figure 32.

.. container:: centeralign

   \ |image18|\

   
   .. container:: centeralign

      //\**Figure 32. FFT Tab \*\* //

   


Results Pane (FTT)
~~~~~~~~~~~~~~~~~~

The **Results** section displays the sample frequency, fundamental frequency, and fundamental power, SNR and other noise performance results. Also displays the harmonic content of the sampled signal and dc power when viewing the FFT analysis.

Exiting the Software
--------------------

To exit the software, click **File** and then click **Exit**.

Troubleshooting section
=======================

-  Make sure that all links are in the default positions (see Table 1).
-  Make sure that the following **test points** have the correct voltages:

   -  **3.3V** provides 3.3V coming from the host (SDP-K1)

      -  **3.3REG** provides 3.3V regulated
      -  **1.8REG** provides 1.8V regulated
      -  **VREF** provides 2.5V
      -  **COM** if the link P14 is connected to VREF/2 provides 1.25V.

-  Make sure that leds **D51** and **D52** are turned on. If not, check that links **P27** and **P26** are both in default positions 4-6 (HI) as shown in Figure 5.
-  If the LED1 (D56) on the SPD-K1 board is blinking red, check that the .bin file has been uploaded correctly to the SDP-K1. If the error still happens, check that the power supplies are correct and verify that you have correctly plugged the EVP-PLP0001-ARDZ to the SPD-K1 through the Arduino connector.

Useful links
============

-  Simulation tool for signal chain:
   ` <adi>>`__\ https://beta-tools.analog.com/noise/#precisionLowPower
-  Article concerning timing factors and solutions to reduce power while maintaining accuracy in low-power systems:
   :adi:`what-are-the-important-timing-factors-for-low-power-precision-signal-chain-apps-part-1.html <en/analog-dialogue/articles/what-are-the-important-timing-factors-for-low-power-precision-signal-chain-apps-part-1.html>`
-  Article concerning how to Leverage Input High-Z Technology to Reduce Solution Power and Size:
   :adi:`how-to-leverage-input-high-z-technology.html?Campaign_Source=linkedin&Campaign_name=everyonesocial&Campaign_medium=2f18e02a-2694-4baa-9873-7918a782dd80&es_id=2d646be4ff <en/technical-articles/how-to-leverage-input-high-z-technology.html?Campaign_Source=linkedin&Campaign_name=everyonesocial&Campaign_medium=2f18e02a-2694-4baa-9873-7918a782dd80&es_id=2d646be4ff>`
-  LTSpice Signal chain simulation files:
   :adi:`single-channel-voltage-current-biosignal-measurement.zip <media/en/simulation-models/ltspice-demo-circuits/single-channel-voltage-current-biosignal-measurement.zip>`

.. |image1| image:: https://wiki.analog.com/_media/resources/evp-plp0001-ardz.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/board_general_overview.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/bankscontroll.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/target.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/typical_setup.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/positions_lk2.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/3-4_possition.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/2-4_possition_1.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/4-6_possition_1.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/1.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/com.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/ace_sw_main1.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/memorymapview.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/analysisview.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/waveform_tab1.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/waveform_tab.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/histogram_tab.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/fft_tab.png
   :width: 400px
