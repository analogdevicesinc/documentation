EVAL-AD-IMP2501-SL Impedance Analyzer Demo/Evaluation Setup
===========================================================

.. note::

   Add hardware revision and firmware revision details here


The EVAL-AD-IMP2501-SL Impedance Analyzer Demo is an evaluation system that is comprised of both the AD-IMP2501DBZ-SL and the AD-IMP2501EBZ-SL boards.

The **AD-IMP2501DBZ-SL** is a high-performance, impedance analyzer module.

-  Highly compact, 31.24mm x 12.83mm System-on-Module (SOM)
-  Impedance measurements from 0.1 Hz to 1.5 MHz
-  Current or Voltage drive application modes
-  16-bit acquisition channels
-  Operates from a single 5V supply
-  UART interface <fc #ff0000>(additional BLE 5.2, USB, and SPI hardware support capable)</fc>
-  Meets patient leakage requirements for IEC 60601-1
-  6 display mode formats in SI units
-  Graphical user interface and Python API for easy system evaluation and data collection

The **AD-IMP2501EBZ-SL** is an easy-to-use evaluation and development breakout board that enables convenient access to the functionality of the AD-IMP2501DBZ-SL Impedance Analyzer Measurement Module.

-  USB C connector provides power and serial communication to host PC
-  On board FTDI USB to UART conversion
-  SMA connectors for interfacing with external load
-  On board loads with jumper configurations for testing and evaluation without external components

EVAL-AD-IMP2501-SL Evaluation Kit Contents
------------------------------------------

-  **AD-IMP2501EBZ-SL** Impedance Demonstration Board
-  USB Cable

| 
| ==== Additional Equipment Required ====

-  **AD-IMP2501DBZ-SL** Impedance Analyzer Measurement Module

.. important::

   It is critical to purchase **both** the the **AD-IMP2501DBZ-SL** Impedance Analyzer Measurement Module and the **AD-IMP2501EBZ-SL** Impedance Demonstration Board. These are sold separately.


Optional Equipment
------------------

-  Programming equipment for Firmware Updates

   -  :adi:`MAX32625PICO2 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/max32625pico2.html#eb-overview>`

-  Impedance measurement accessories. Available from various test and measurement manufacturers, for example:

   -  `Keysight's Impedance Measurement Accessories <https://www.keysight.com/en/pc-1000002552%3Aepsg%3Apgr/lcr-meter-impedance-measurement-product-accessories>`__
   -  `B+K Precision TL89S1 SMD Test Fixture <https://www.digikey.com/en/products/detail/b-k-precision/TL89S1/7915183>`__
   -  `B+K Precision TL89F1 4-Terminal Test Fixture for leaded components <https://www.digikey.com/en/products/detail/b-k-precision/TL89F2/6618989>`__
   -  `SMA Male Pin to BNC Jack <https://www.digikey.com/en/products/detail/pomona-electronics/4290/678700>`__

-  Calibration Standards and Accessories

   -  `IET Labs <https://www.ietlabs.com/>`__ (former General Radio products)
   -  `Keysight 42090A Open Termination <https://www.keysight.com/en/pd-1000003831%3Aepsg%3Apro-pn-42090A/open-termination-4-terminal-pair>`__
   -  `Keysight 42091A Short Termination <https://www.keysight.com/en/pd-1000003830%3Aepsg%3Apro-pn-42091A/short-termination-4-terminal-pair>`__
   -  `Keysight 42030A Four Terminal Pair Standard Resistor Set <https://www.keysight.com/en/pd-1000003832%3Aepsg%3Apro-pn-42030A/four-terminal-pair-standard-resistor-set>`__
   -  `Keysight 16380A Standard Air Capacitor Set (1pF to 1000pF) <https://www.keysight.com/en/pd-1000003834%3Aepsg%3Apro-pn-16380A/standard-air-capacitor-set-1pf-to-1000pf>`__
   -  `Keysight 16380C Capacitance Standard Set (0.01uF to 10uF) <https://www.keysight.com/en/pd-1000003833%3Aepsg%3Apro-pn-16380C/capacitance-standard-set-001uf-to-10uf>`__

-  LCR Meter for verification

   -  `Keysight E4980A Precision LCR Meter <https://www.keysight.com/en/pd-715495-pn-E4980A/precision-lcr-meter-20-hz-to-2-mhz>`__

| 
| ===== Quick Start ===== Follow these steps to start evaluating the AD-IMP2501DBZ-SL:

-  Driver Installation
-  Terminal Emulator/GUI Installation
-  Hardware Setup
-  Command Line or GUI Operation
-  Performing Impedance Measurements

These steps are explained in detail in the following sections.

--------------

1. USB Driver Installation
--------------------------

.. note::

   The default communication interface to the EVAL-AD-IMP250-SL is via its USB port. Using the USB Type C cable included with the evaluation board (TTL-232R-RPI), FTDI's Virtual COM Port (VCP) drivers must be downloaded from their website located at https://www.ftdichip.com/Drivers/VCP.htm


**Installation steps:**

-  Download the driver setup executable for the host OS version from https://www.ftdichip.com/Drivers/VCP.htm

   -  Note: for detailed instructions, visit https://www.ftdichip.com/Support/Documents/InstallGuides.htm

-  Unzip the file and run the setup executable
-  Connect the USB cable to the PC
-  Open the Device Manager
-  In the Device Manager window, verify that the USB Serial Port is displayed under “Ports (COM & LPT)” and that a serial port identifier has been assigned as shown below (the COM# may be different than shown here):

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/dev_mgr_vcp_installed.png
   :align: center
   :width: 600px

| 

--------------

2a. Terminal Emulator Installation
----------------------------------

To communicate with AD-IMP2501DBZ-SL via its command-line interface and UART, a terminal emulator like TeraTerm is recommended. Any other terminal emulator such as PuTTY or user preferred emulator should be acceptable but may not be tested. For instruction purposes we will continue with TeraTerm.

.. admonition:: Download
   :class: download

   \ https://github.com/TeraTermProject/teraterm/releases\


Download and run the latest stable release. Follow the on-screen instructions.

| **Note:** Some terminals do not support the ANSI Escape Codes which manipulate the cursor position. If the ANSI Escape Codes are not supported, the terminal will render them as boxes. TeraTerm supports these characters.
| ----

.. important::

   UPDATE or REMOVE based on Python GUI release


.. important::

   
   2b. GUI Installation
   ~~~~~~~~~~~~~~~~~~~~
   
   .. note::

      If planning to operate and evaluate from the command line, skip this step and proceed to step **3**.

   
   The evaluation GUI is LabVIEW based and requires two runtime engines provided by National Instruments (Copyright © 2023 National Instruments Corporation. All Rights Reserved).
   
   -  Download and install the LabVIEW Runtime Engine, version 2023 Q1 64 bit. You can download this Run-time engine directly from National Instrument’s website below. This will require you to have or register for a NI User Account in order to download the software from their online portal. Alternatively, an option to download the executable offline is available on that page.
   
   .. admonition:: Download
      :class: download

      \ https://www.ni.com/en/support/downloads/software-products/download.labview-runtime.html#477317\

   
   -  Regardless of how you access the run time engine installer, run the file “ni-labview-2023-runtime-engine_23.1_online.exe” and follow the steps to install the run-time engine.
   
   .. important::

      A reboot is required at the end of this installation process.

   
   -  Download and install the LabVIEW NI-VISA Runtime Engine (version 2023 Q3 64 bit) provided by National Instruments directly from National Instrument’s website below. As above, this will require you to have or register for a NI User Account in order to download the software from their online portal. An option to download the executable offline is available on that page.
   
   .. admonition:: Download
      :class: download

      \ https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html#484351\

   
   -  Run the file “ni-visa_23.5_online.exe” and follow the steps to install the run-time engine.
   -  During the installation, you may be asked if you would like to install any additional packages. These are not necessary to run this GUI. You can select “Deselect all other options” and proceed with the installation.
   
   .. important::

      A reboot is required at the end of this installation process.

   
   --------------
   


3. Basic Hardware Setup
-----------------------

The following figure shows the basic connections required for evaluating the ADMX2501B.

<WRAP>\ |image1|\ </WRAP>

-  Insert the AD-IMP2501DBZ-SL module into the AD-IMP2501EBZ-SL board in the location shown above. Use the small white triangle on both the module and the carrier board to orient properly. The connectors are different sizes, so they can only be inserted in one orientation shown, but excessive force in the wrong orientation could damage the connectors.
-  Use the picture below and the following tables to install the correct jumpers for your desired operation. The first table is for power and general communication. The second table is for EIS on board measurements. The third table is for EIS off board measurements.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/fishercat_jumper_positions.png
   :align: center
   :width: 600px

-  Verify jumpers are installed in the locations designated by the following table for power and communication.

================== ================ ==================
Jumper Designation Install Position Description
================== ================ ==================
P4                 Not Installed    Programming Header
P5                 Not Installed    Debug UART TX
P6                 Not Installed    Debug UART RX
P11                Pins 1-2         USB C Power Supply
P14                Pins 1-2         USB C DM
P15                Pins 1-2         USB C DP
P16                Pins 1-2         FTDI UART RX
P17                Pins 1-2         FTDI UART TX
P18                Pins 1-2         FTDI Power
P20                Not Installed    CAN Bus
================== ================ ==================

-  For EIS on board measurements install jumpers according to the following table. Note that to select an onboard load, both jumpers, corresponding to the appropriate load, need to be installed. If the user selects their own component in position 8, no jumpers should be installed on P21 or P22.

================== ================ =======================
Jumper Designation Install Position Description
================== ================ =======================
P27                Pins 1-2         EIS HCUR
P28                Pins 1-2         EIS HPOT
P29                Pins 1-2         EIS LPOT
P30                Pins 1-2         EIS LCUR
P23                Pins 1-2         HCUR to HPOT connection
P24                Pins 1-2         LCUR to LPOT connection
P21                Selectable:      
:::                Pins 1-2         10k ohms
:::                Pins 3-4         1k ohms
:::                Pins 5-6         100 ohms
:::                Pins 7-8         10 ohms
:::                Pins 9-10        0 ohms
P22                Selectable:      
:::                Pins 1-2         10k ohms
:::                Pins 3-4         1k ohms
:::                Pins 5-6         100 ohms
:::                Pins 7-8         10 ohms
:::                Pins 9-10        0 ohms
P8                 Not Installed    User selectable load
P12                Pins 1-2         EIS HCUR SMA
:::                Pins 5-6         EIS HPOT SMA
:::                Pins 9-10        EIS LPOT SMA
:::                Pins 13-14       EIS LCUR SMA
================== ================ =======================

-  For EIS off board measurements using the SMA connectors, install jumpers according to the following table. Connect SMA cables to J1-J4, and verify no jumpers are installed on P8, P21, P22, P23, and P24.

================== ================ =======================
Jumper Designation Install Position Description
================== ================ =======================
P27                Pins 1-2         EIS HCUR
P28                Pins 1-2         EIS HPOT
P29                Pins 1-2         EIS LPOT
P30                Pins 1-2         EIS LCUR
P23                Pins 1-2         HCUR to HPOT connection
P24                Pins 1-2         LCUR to LPOT connection
P21                Not Installed    10k ohms
:::                :::              1k ohms
:::                :::              100 ohms
:::                :::              10 ohms
:::                :::              0 ohms
P22                Not Installed    10k ohms
:::                :::              1k ohms
:::                :::              100 ohms
:::                :::              10 ohms
:::                :::              0 ohms
P8                 Not Installed    User selectable load
================== ================ =======================

-  For EIS off board measurements using the DIN connector, only change jumpers on P12 according to the following table. Connect DIN cable to P7.

================== ================ ============
Jumper Designation Install Position Description
================== ================ ============
P12                Pins 3-4         EIS HCUR SMA
:::                Pins 7-8         EIS HPOT SMA
:::                Pins 11-12       EIS LPOT SMA
:::                Pins 15-16       EIS LCUR SMA
================== ================ ============

-  Connect the USB C cable to P3 on AD-IMP2501EBZ-SL and the host PC.
-  An LED on the top side of the AD-IMP2501DBZ-SL should turn on, blink twice, and turn off. It should now only turn on when data is being processed.

--------------

4. Opening a Session via Teraterm
---------------------------------

After TeraTerm has been installed, and the system is powered on. Open TeraTerm and choose Serial connection. Select the COM port identified earlier in the Device Manager. Click OK. Then choose the dropdown labeled Setup, click Serial port, and ensure that the COM port is set and the following are set accordingly, Speed = 115200, Data = 8 bits, Parity = none, Stop bits = 1 bits, Flow control = None. Click New setting. Optionally, choose Setup→Save setup. Save the file to the default directory. Now, when launching TeraTerm, it will automatically try to connect with those saved settings.

Verify the board is communicating properly by checking the following:

-  Press ENTER within the terminal and verify the entry ">>" prompt.
-  Type ``version`` and press ENTER to display the module name and firmware revision.
-  Type ``get`` and press ENTER to see the current parameter settings on the AD-IMP2501DBZ-SL.
-  Type ``help`` and press ENTER to see a list of all commands supported by AD-IMP2501DBZ-SL.

| 
| Note that closing the TeraTerm window does not reset the AD-IMP2501DBZ-SL settings from the last session.

--------------

5. Performing Basic Measurements via Command Line
-------------------------------------------------

Upon opening a session with TeraTerm, the AD-IMP2501DBZ-SL is ready to perform impedance measurements.

.. important::

   The measurements reported by the module may not be accurate unless it has been calibrated. For detailed instructions on how to calibrate the module, please refer to the `Calibration Procedure <https://wiki.analog.com/eval-admx2501ebz>`__ section in this user guide.


By default, the module is set to perform single-point impedance measurements in rectangular coordinates with a 300mV peak-to-peak signal (magnitude = 300) at 1kHz, and no DC offset. To initiate a measurement type the **"z"** command at the prompt and press ENTER.

Type ``get`` and press ENTER to view the current default parameter settings in the terminal window.


|image2|

Measurement settings are not always in their base SI form. Frequency is in Hz, delays are in milliseconds. The signal magnitude sets the peak-to-peak value, centered around the offset voltage. The DC offset is in millivolts.

The AC magnitude can be configured anywhere between approximately 10mV pk-pk and 2.4V pk-pk. This represents the generated signal, but the actual magnitude across the DUT will be be dependent on the DUT impedance, due to the onboard 100Ω source resistance (for current limiting and patient protection, can be modified for different applications); see `Selecting a Measurement Range <https://wiki.analog.com/eval-admx2501ebz>`__ for details.

.. tip::

   The order in which the settings commands are entered is not important.


Example
~~~~~~~

Perform a 100 ohm (Jumpers on P21.5-6 and P22.5-6 in the EIS on board measurement table above) resistive measurement at 100kHz with a 1V pk-pk magnitude. Return 5 readings, displayed in Magnitude and Phase (in degrees), where each is an average of 10 samples.

::

   >>freq 100000
    Frequency: 100000Hz

   >>display 2
    Display Mode: Impedance, Magnitude and Phase in degrees (Z, deg)

   >>mag 1000
    Signal Magnitude: 1000mV

   >>avg 10
    Average: 10

   >>count 5
    Count: 5

   >>z

   0, 1.024279e+02, -1.312940e+00
   0, 4.878047e-02, 4.109422e-02
   1, 1.024257e+02, -1.305184e+00
   1, 5.721481e-02, 5.543189e-02
   2, 1.024132e+02, -1.303233e+00
   2, 3.633902e-02, 4.070190e-02
   3, 1.024019e+02, -1.310408e+00
   3, 4.281778e-02, 4.233954e-02
   4, 1.023718e+02, -1.320099e+00
   4, 4.378229e-02, 3.729085e-02

   >>

| 
| Output is displayed as index, Magnitude, Phase (in degrees). The second line with the same index indicates the standard deviation of the averaged samples for both Magnitude and Phase of the previous measurement.

.. note::

   By default, auto-range is not selected and the default gain channels are selected as 0 (x1 Voltage Gain) and 0 (x50 Current Gain).


--------------

Using the Help Functionality in the Command-Line Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``help`` command will display all the commands available to the user from the command-line interface (CLI). Use this command while operating for a quick refresher. See the **AD-IMP2501DBZ-SL Available Commands** section for more details on each command.

| |image3| |image4|

AD-IMP2501DBZ-SL Available Commands
-----------------------------------

| All commands should be in lower case type and each command and input value should be separated by spaces. Only one command can be entered at a time. An incorrect format or command that is not listed will result in the terminal prompting the user to correct their input, or type ``help`` to review the list. At any point, to cancel a measurement or any command that is currently running on the system, hit “Esc” and the system will abort the current command and prompt the user for a new input.
| \* **help:** Typing ``help`` and hitting enter will display all the available commands the user can choose from. The command, followed by the necessary input/s separated by spaces. A short description of the command and inputs are provided on the left. An empty bracket “< >” indicates that no input is necessary other than the command itself.

-  **z:** Typing ``z`` starts a measurement and returns impedance data to the screen. This is considered one measurement loop.
-  **appmode:** Typing ``appmode`` allows the user to select different frequency ranges for different application types. Currently, there are two ranges, 1Hz to 1.5MHz, and 0.01Hz to 10kHz. The 0.01Hz to 10kHz range is primarily untested at this point in time.
-  **freq:** Typing ``freq`` and a value between 1 and 1000000 changes the frequency parameter of the next single frequency measurement.
-  **sweeptype:** Typing ``sweeptype`` and ``0`` disables the sweep measurement. Typing ``1`` as an input enables a frequency sweep measurement. Enabling sweeptype will utilize the sweeprange and sweepscale parameters.
-  **sweeprange:** Typing ``sweeprange`` and two values selects the sweep range. The first value indicates the starting frequency point of the sweep and the second value indicates the ending frequency point of the sweep. The number of points between the sweep start and sweep stop will be determined by the count parameter. The spacing between points will be determined by sweepscale parameter.
-  **sweepscale:** Typing ``sweepscale`` and ``0`` enables a linear distribution of points in the sweeprange or typing ``1`` enables a logarithmic distribution.
-  **drive:** Typing ``drive`` and ``0`` enables the voltage drive output while typing ``1`` enables the current drive output.
-  **count:** Typing ``count`` and a value between 1 and 255 sets the number of measurements to display to the screen per measurement loop. This will apply to both single frequency measurements or sweeps.
-  **avg:** Typing ``avg`` and a value between 1 and 255 sets how many measurements will be taken and then averaged for every displayed measurement.
-  **trigger:** Typing ``trigger`` and a value between 0 and 255 sets how many times to run the measurement loop. Setting trigger to 0 will enable a continuous measurement loop and will end when the user aborts by entering “ESC”.
-  **mag:** Typing ``mag`` and a value between 20 and 2400 sets the signal magnitude in mV. This is the magnitude generated before the load and before the current limiting series resistor. The current limiting resistor is set to 100 ohms but could be changed depending on the application.
-  **gain:** Typing ``gain`` and two values. The first is either ``0`` or ``1`` to determine which channel gain should be adjusted. 0 represents the voltage receive path and 1 represents the current receive path. The second value is either 0 – 3 if the voltage gain channel was chosen or 0 – 2 if the current gain channel was chosen. These gain values will multiply the measured signal via hardware and are approximately equal to x1, x2, x4, and x8 for the voltage channel and equal to x50, x500 and x5000 for the current channel.
-  **dcoffset:** Typing ``dcoffset`` and a value between -2500 and 2500 sets the DC voltage offset of the output signal.
-  **measdelay:** Typing ``measdelay`` and a value between 1 and 60000 sets the delay between displayed measurements in milliseconds.
-  **trigdelay:** Typing ``trigdelay`` and a value between 0 and 60000 sets the delay between displayed measurement loops in milliseconds.
-  **autogain:** Typing ``autogain`` and ``0`` to disable the system auto gain feature or ``1`` to enable the auto gain. When auto gain is enabled the voltage and current gain channels will be automatically selected for each measurement. It is not recommended to have auto gain turned on during frequency sweeps. There will not be a recording of which gain setting was used for each sweep measurement and it is possible that slight discrepancies between gain settings could exist. Gains will be re-evaluated and re-set after each measurement.
-  **display:** Typing ``display`` and a value between 0 and 6 chooses the format of the displayed measurement. 0 will turn off the display. 1 will format the measurements in impedance rectangular form [R, X] (Resistance, Reactance). 2 will format the measurements in impedance magnitude and phase (in degrees). 3 will format the measurements in impedance magnitude and phase (radians). 4 will format the measurements in admittance rectangular form [G, B] (Conductance, Susceptance). 5 will format the measurements in admittance magnitude and phase (in degrees). 6 will format the measurements in admittance magnitude and phase (radians).
-  **imprange:** Typing ``imprange`` and two values between 0 and 100000 represents the impedance warning threshold. The first value represents the minimum impedance value the user expects and the second value represents the maximum impedance value. Any measured value outside this range will cause the system to generate a warning message. Typing 0 and 0 will turn warnings off.
-  **devwarn:** Typing ``devwarn`` and two values represents the standard deviation warning. These values should be entered for measurements in rectangular form. The first value represents the deviation range of “R” and second represents the deviation range of “X”. This threshold will only be applied if avg is greater than 1. Typing 0 and 0 will turn warnings off.
-  **correction:** Typing ``correction`` and a value between 0 and 2 changes the calibration setting. 0 represents no calibration applied to the measurements. 1 will apply only calibration adjustments to the measurements. 2 will apply both calibration and compensation adjustments.
-  **calopen:** Typing ``calopen`` initiates the open calibration procedure. H_CUR and H_POT nodes should be tied together and the L_CUR and L_POT nodes should be tied together.
-  **calshort:** Typing ``calshort`` initiates the short calibration procedure. H_CUR and H_POT nodes should be tied together with the L_CUR and L_POT nodes.
-  **calload:** Typing ``calload`` followed by two values initiates the load calibration procedure. The first value represents the true resistive part of the connected load and the second value represents the true reactive part of the connected load. Connect the H_CUR and H_POT nodes to one side of the desired load and the L_CUR and L_POT nodes to the other side of the load.
-  **calread:** Typing ``calread`` followed by two values reads the saved calibration values for a specific gain combination. The first value represents the voltage gain setting and the second represents the current gain setting.
-  **calcommit:** Typing ``calcommit`` saves any calibration data that has been measured in this session to memory. Calibration data will not be saved after a power cycle if it is not committed to memory.
-  **calclear:** Typing ``calclear`` erases all saved calibration data that has been saved to memory.
-  **compopen:** Typing ``compopen`` initiates the open compensation procedure. H_CUR and H_POT nodes should be tied together and the L_CUR and L_POT nodes should be tied together.
-  **compshort:** Typing ``compshort`` initiates the short compensation procedure. H_CUR and H_POT nodes should be tied together with the L_CUR and L_POT nodes.
-  **compload:** Typing ``compload`` followed by two values initiates the load compensation procedure. The first value represents the true resistive part of the connected load and the second value represents the true reactive part of the connected load. Connect the H_CUR and H_POT nodes to one side of the desired load and the L_CUR and L_POT nodes to the other side of the load.
-  **compread:** Typing ``compread`` followed by two values reads the saved compensation values for a specific gain combination. The first value represents the voltage gain setting and the second represents the current gain setting.
-  **get:** Typing ``get`` prints the current system configuration parameters to the screen.
-  **selftest:** Typing ``selftest`` runs a system self test. The system should be set up in an open configuration with H_CUR and H_POT tied together and L_CUR and L_POT tied together with no load attached.
-  **default:** Typing ``default`` sets the system back to its original default configuration.
-  **version:** Typing ``version`` reads the firmware version that is currently loaded on the module.
-  **restart:** Typing ``restart`` internally power cycles and restarts the system. This will not change the configuration after the module comes back online.

--------------

Useful Hints
^^^^^^^^^^^^

Measurement Display Modes
-------------------------

The AD-IMP2501DBZ-SL returns a result in one of 7 different display modes, shown below. The result is always reported in the base SI unit. For instance, ``display mode 1`` (R, X) returns the impedance in rectangular form, both in ohms.

+---------------------+------------------------------------------------+--------+------------------+
| Display Mode Number | Mode Name                                      | Form   | SI Unit          |
+=====================+================================================+========+==================+
| 0                   | Display Off                                    | N/A    | None             |
+---------------------+------------------------------------------------+--------+------------------+
| 1                   | Impedance in rectangular coordinates (default) | R, X   | Ohms, Ohms       |
+---------------------+------------------------------------------------+--------+------------------+
| 2                   | Impedance in magnitude and phase in degrees    | Z, deg | Ohms, Degrees    |
+---------------------+------------------------------------------------+--------+------------------+
| 3                   | Impedance in magnitude and phase in radians    | Z, rad | Ohms, Radians    |
+---------------------+------------------------------------------------+--------+------------------+
| 4                   | Admittance in rectangular coordinates          | G, B   | Siemens, Siemens |
+---------------------+------------------------------------------------+--------+------------------+
| 5                   | Admittance in magnitude and phase in degrees   | Y, deg | Siemens, Degrees |
+---------------------+------------------------------------------------+--------+------------------+
| 6                   | Admittance in magnitude and phase in radians   | Y, rad | Siemens, Radians |
+---------------------+------------------------------------------------+--------+------------------+

Selecting a Measurement Range
-----------------------------

By default, the AD-IMP2501DBZ-SL is not auto-ranging mode, and will use the default or previously set gain settings. Auto-range can be turned on which will use the highest voltage and current settings based on the frequency and magnitude of the signal.

.. note::

   The auto-ranging algorithm is applied to each measurement. This will slow the measurement time. When performing frequency sweeps, the impedance of the device under test will change and the auto-range could detect a new setting for a later measurement than the first measurement in the sweep. These changes will not be recorded so it is not advised to use auto-range during frequency sweeps unless tested and it has been determined there are no incongruent measurement points.


   | <fc #ff0000>DO WE WANT TO INCLUDE ALL THIS INFO HERE</fc>
|

.. important::

   In some cases, the user may want to select a specific measurement range. The measurement range is mostly affected by the transimpedance of channel 1 and the test signal magnitude. It is recommended to select the transimpedance value that is smaller than the expected value of the impedance under test, but larger than the next transimpedance selection.

   
   For example, if the DUT's expected impedance value is 2kΩ, enter the following in the command line prompt:
   
   ::
   
      ADMX2001> setgain ch0 0
        voltGain = 0
      ADMX2001> setgain ch1 1
        currGain = 1
   
   The command ``setgain ch1`` modifies the current measurement range of L_CUR (channel 1). This is done by setting different values for (R\ :sub:`TIA`) in the feedback loop of the transimpedance amplifier A2. The command ``setgain ch1 1`` sets the transimpedance to 499Ω, appropriate for the 1kΩ-10kΩ range. It is not recommended to use the 10kΩ-100kΩ range for a 2kΩ load since this could exceed the current input channel measurement capabilities and return incorrect readings.
   
   The ADMX2001B uses a balancing bridge architecture. A 100 ohm series resistor Rs protects the source channel. When calculating the current through a DUT or the actual AC magnitude across that DUT, this resistor must be factored in. A transimpedance amplifier is used in measuring the current, and has a 10 ohm input protection resistor R\ :sub:`IN`. A simplified diagram is shown below. In the diagram, Z\ :sub:`X` is the DUT (unknown impedance). The transimpedance amplifier holds the connection point to R\ :sub:`IN` (inverting terminal of the TIA) at 0V. Since R\ :sub:`S`, Z\ :sub:`X` and R\ :sub:`IN` are in series, the DUT current is equal to (magnitude setting Vpk)/(\|Z\ :sub:`X`\ \| + 100Ω + 10Ω).

   
   |image5|

   Available current gain settings and the transimpedance values associated with them are listed below.
   
   ======== ================= ==============
   Ch1 Gain Max Input Current Transimpedance
   ======== ================= ==============
   0        25mA              49.9Ω
   1        2.5mA             499Ω
   2        250uA             4.99kΩ
   3        25uA              49.9kΩ
   ======== ================= ==============
   
   Continuing from the previous example, when the DUT is 2kΩ and the magnitude is set to the maximum setting of 2.25Vpk, the current through the DUT (and into the TIA) is 2.25Vpk/(2kΩ + 110Ω) = 1.06mA. Then selecting ch1 gain to be 1 makes the measurement fit well within the max input current range of 2.5mA.
   
   The command ``setgain ch0`` modifies the input voltage range of channel 0 (between terminals H_POT and L_POT). This is less common, but it can be used to improve measurement sensitivity if the impedance under test is smaller than the lead impedance or less than 100Ω. It can also be used if the magnitude of the test signal is small. This can be the case with sensitive loads, or when the test frequency is high.
   
   Available voltage gain values for channel 0 are listed below.
   
   ======== ======================= ===========
   Ch0 Gain Max Input Voltage Range Gain Factor
   ======== ======================= ===========
   0        ±2.5V                   1
   1        ±1.25V                  2
   2        ±625mV                  4
   3        ±312.5mV                8
   ======== ======================= ===========
   
   The DUT voltage is determined by the set magnitude and the two series protection resistors. The DUT voltage is equal to (magnitude setting Vpk)*(\|Z\ :sub:`X`\ \|)/(\|Z\ :sub:`X`\ \| + 110Ω). For example, to measure a 25Ω DUT with the magnitude set to the maximum setting of 2.25Vpk, the DUT voltage is 2.25Vpk*(25Ω)/(25Ω + 110Ω) = 416.7mVpk, a little under the 625mVpk limit. To utilize the full range, set the ch0 gain = 2.
   
   Voltages across and currents through the DUT that exceed these maximum values for each gain range may result in the ADC saturating, causing the measurement to fail.
   
   Typing the command ``setgain`` will display the gain of both input channels and whether or not autoranging is enabled.
   
   ::
   
      ADMX2001> setgain
      Autorange enabled
      voltGain = 1
      currGain = 3
      ADMX2001>
   
   To turn autoranging back on after setting a manual range type ``setgain auto``
   
   Even though 16 gain combinations are possible, most measurements can be performed with the 7 combinations shown in the table below.
   
   ======== ======== ===========================
   Ch0 Gain Ch1 Gain Impedance Measurement Range
   ======== ======== ===========================
   3        0        < 10Ω
   2        0        < 25Ω
   1        0        < 50Ω
   0        0        100Ω to 1kΩ
   0        1        1kΩ to 10kΩ
   0        2        10kΩ to 100kΩ
   0        3        > 100kΩ
   ======== ======== ===========================
   
   These are the same ranges that the autoranging algorithm uses. The previously mentioned procedures can be used to calculate the DUT current and voltage. The following section shows how to estimate the impedance value of the DUT to determine the measurement range. Note that these measurement ranges apply for ``magnitude = 1`` and ``offset = 0``. They may not apply for other settings. To calculate whether the ADC will saturate, use the balancing bridge diagram above. Using the sum of the signal magnitude and offset, calculate what the current through the 110Ω resistors + DUT will be, and choose a gain from the Ch1 gain table. Then, calculate the voltage across the DUT due to this current through it, and choose a voltage gain from the Ch0 gain table.
   
   For a 2kΩ DUT where the sum of the magnitude and offset is 1Vpk, using the two equations we find:
   
   -  DUT current = 1Vpk/(2kΩ + 110Ω) = 0.47mA, select Ch1 Gain = 1.
   -  DUT voltage = 1Vpk*2kΩ/(2kΩ + 110Ω) = 948mV, select Ch0 Gain = 0 or 1.
   -  The above selection matches the suggested gain combination (0,1) with a given impedance measurement range from 1kΩ to 10kΩ.
   
   Estimating the Impedance and Admittance of Capacitive and Inductive Devices
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
   Impedance is defined as the opposition to the flow of alternating current. Admittance is the reciprocal of impedance, or how easy is for alternating current to flow. Electrical components such as resistors, capacitors and inductors have a direct relationship between their value and the expected impedance (Z):
   
   | Z = X = -1/(2πfC) for capacitors
   | Z = X = 2πfL for inductors
   | Z = R for resistors
   | Where f is the frequency of the signal; C, L, and R are the component values in Farads, Henries and Ohms respectively. R represents resistance and X reactance.
   
   For admittance (Y):
   
   | Y = B = 2πfC for capacitors
   | Y = B = -1/(2πfL) for inductors
   | Y = G = 1/R for resistors
   | Where f is the frequency of the signal; C, L, and R are the component values in Farads, Henries and Ohms respectively. G represents conductivity and B susceptance.
   
   All components, regardless of their construction, will show a combination of resistive (conductive) and reactive (susceptive) properties. These properties can be expressed in the form of ideal electrical components combined either in series or parallel. At any given frequency, impedance/admittance can be expressed as a combination of the reactive element (capacitor or inductor) and a resistive element. The total impedance or admittance magnitude can be obtained by calculating the square-root of the sum of squares (RSS) of the two components or
   
   | 
   | %% \|Z\| = sqrt(R*R + X*X)%%
   | %% \|Y\| = sqrt(G*G + B*B)%%
   | To determine the best measurement range for measurement, it is necessary to estimate the impedance or admittance of the device under test at the frequency of measurement using the equations above. A simpler method to obtain an approximate value based on the expected capacitance or inductance value is through the reactance chart shown below.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/reactance_chart_labeled.jpg
      :align: center
      :width: 600px
   
   To find the approximate impedance or admittance value for a capacitor or inductor, find the closest expected value assigned to the diagonal lines and find its equivalent impedance/admittance value on the vertical axis at the frequency of interest (on the horizontal axis). For example, the impedance of a 159fF capacitor, which is represented by the red solid diagonal line in the reactance chart, exhibits \|Z|=1MΩ at 1MHz, indicated by the "1M" tick on the vertical axis. This matches the estimated value using equation Z = X = -1/(2πfC). Similarly, for a 15.9nF capacitor, which is shown as blue solid diagonal line in the chart, \|Z|=10KΩ at 1kHz.


Reducing Measurement Noise
--------------------------

The ``avg`` command determines how many samples are averaged for each reading returned. Averaging reduces noise and is helpful in applications that require detecting small changes in a value or when the impedance component of interest is small in comparison to the total impedance magnitude. The default is set to 1, which means no averaging is done.

.. tip::

   Averaging increases the time required to return a reading. So finding the compromise between improved noise and measurement speed will depend on the application. At some point there is a limited return as the average value continues to increases. This threshold of limited return will depend on the application.


Improving Measurement Precision
-------------------------------

To ensure precise and accurate measurements, impedance measurements should be performed with appropriate test fixtures. Measurement leads can introduce additional errors due to parasitic impedances that will vary depending on mechanical configuration and cabling.


| To help ensure repeatable and stable measurements, custom-made fixtures that minimize impedance fluctuations due to mechanical configuration are recommended. To test surface-mount components, fixtures like the `B+K Precision TL89S1 <https://www.digikey.com/en/products/detail/b-k-precision/TL89S1/7915183>`__ or the `Keysight 16034G <https://www.keysight.com/en/pd-1000000474%3Aepsg%3Apro-pn-16034G/smd-test-fixture>`__ are good examples. For a full list of recommended accessories, please refer to the Recommended Accessories Section at the beginning of this user guide. These fixtures are not possible for all applications and some systems will require relative versus absolute precision.

Performing Parametric Sweeps
----------------------------

The AD-IMP2501DBZ-SL can automatically perform measurements that sweep the frequency parameter. This is common in EIS applications (Electrical Impedance Spectroscopy). The frequency increments can be linear or logarithmic.

By default, the sweep function is off. To enable parametric sweeps, use the ``sweeptype`` command and specify the sweep type, ``1`` for frequency sweep, ``0`` to turn off. The ``sweeprange`` command allows the user to enter the start and end points of the sweep. The number of incremental points including the start and stop points is determined by the ``count`` command.

.. _example-1:

Example
~~~~~~~

Perform an 11-point logarithmic frequency sweep from 1kHz to 1MHz.

::

   >>count 11
    Count: 11

   >>sweeptype 1
    Sweep Type: Frequency

   >>sweeprange 1000 1000000
    Sweep Start: 1000Hz
    Sweep Stop: 1000000Hz

   >>sweepscale 1
    Scale: Log

   >>z

   1.000000e+03, 1.031255e+02, -1.630275e-02
   1.995262e+03, 1.023943e+02, -2.934620e-02
   3.981072e+03, 1.025097e+02, -4.382038e-02
   7.943283e+03, 1.024828e+02, -1.119833e-01
   1.584893e+04, 1.024931e+02, -2.017830e-01
   3.162278e+04, 1.024935e+02, -4.088743e-01
   6.309575e+04, 1.024701e+02, -8.741217e-01
   1.258926e+05, 1.024697e+02, -1.634526e+00
   2.511887e+05, 1.026109e+02, -3.280124e+00
   5.011873e+05, 1.029818e+02, -6.563277e+00
   1.000000e+06, 1.043930e+02, -1.319202e+01

   >>

.. note::

   When sweeping frequency, the first value printed will be the frequency value instead of index, followed by the measurement in the display format selected.


Plotting Measurement Data
-------------------------

When acquiring multiple measurements or performing sweeps, it is useful to plot the results to observe trends or characteristics of the device under test. TeraTerm allows the user to save a log by going to File->Log, which can then be copy and pasted into a \*.csv file that can be opened by spreadsheet applications such as Microsoft Excel®. The log file must be saved BEFORE taking any measurements.

To plot the acquired data in Microsoft Excel, follow the steps below:

-  In TeraTerm, click File, in the dropdown list select Log, and save the log file with any name and location, but make sure to change the default extension from \*.log to \*.csv
-  Select the settings desired and hit "OK"
-  Configure the ADMX2001B and run the ``z`` command to acquire the desired measurements
-  A separate TeraTerm window named "TeraTerm:Log" will have opened, click "Close" to stop logging data
-  Open the file with Excel
-  Select the data to plot and insert a scatter plot to visualize the data

|

Optimizing Measurement Timing
-----------------------------

This section describes what settings impact the measurement time and how. The measurement time is dependent on a number of factors. Command transmission time, configured delays, source setup time, ADC acquisition time, count setting, averages, etc. Some factors, like the ADC acquisition time, are dependent on the frequency since the ADC needs to capture a minimum number of cycles of the waveform.

Delay Usage and Measurement Sequencing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The commands ``measdelay`` (measurement delay) and ``trigdelay`` (trigger delay) can be used to control the settling time between measurements.

-  The measurement delay or ``measdelay`` is observed before each measurement, but not between samples when averaging. The delay is also applied during sweeps and between multiple counts. Both the DC offset and AC test signal are enabled during the delay, but the ADCs do not capture data for the measurement until the delay has elapsed.
-  The ideal measurement delay suitable for different DUTs may vary. When measuring a large capacitive load, consider the settling time it requires to charge; a longer measdelay is preferred to prevent accuracy loss.
-  Trigger delay is only observed after trigger events controlled by the ``trigger`` command. It is easiest to think of trigger events as measurement loops. One measurement loop could consist of multiple measurements and then repeats several times. If configured, the DC offset will be enabled during the trigger delay, but the AC source will only start after the delay for the data capture.

To setup ``measdelay`` and ``trigdelay``, simply enter the command followed by a value in milliseconds, up to a maximum of 60 seconds.

Below is a demonstration on how each measurement time parameter fits in the measurement sequence. Note that the sinusoidal excitation is turned on during periods marked with blocks in light/dark green. If enabled, the DC offset will turn on during the tdelay blocks. The example measurement uses a 100 Ohm onboard resistor as the DUT.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/command_timing_diagram.png
   :align: center
   :width: 1000px

1. Single sample measurement. When measuring one count sample, a ``measdelay`` is observed before each measurement where the single sample is captured.

::

   >>count 1
    Count: 1

   >>avg 1
    Average: 1

   >>z

   1.000000e+03, 1.022631e+02, -4.570409e-02

2. Multiple samples averaging. When measuring with ``avg`` > 1, ``measdelay`` is observed only before the first sample, but not between samples. The display now shows 2 lines after a measurement due to averaging. The second line shows the index, the standard deviation of the first display unit, the standard deviation of the second display unit.

::

   >>count 1
    Count: 1

   >>avg 10
    Average: 10

   >>z

   1.000000e+03, 1.022631e+02, -4.570409e-02
   1.000000e+03, 5.502485e-01, 4.377977e-01

3. Multiple counts measurement. When adding multiple counts of a single sample measurement, ``measdelay`` is observed before each measurement in their individual count.

::

   >>count 3
    Count: 3

   >>avg 1
    Average: 1

   >>z

   0, 1.025080e+02, -6.183665e-01
   1, 1.027569e+02, -1.343047e+00
   2, 1.030360e+02, -3.661266e-01

4. Multiple triggers measurement. When ``trigger`` > 1, multiple measurement triggers are enabled. Based on single measurement cycle setting (say ``count`` = 3, ``avg`` = 1), multiple measurement events are triggered. The ``trigdelay`` defines the delay time between these trigger events.

::

   >>count 3
    Count: 3

   >>avg 1
    Average: 1

   >>trigdelay 250
    Trigger Delay: 250ms

   >>trigger 3
    Trigger Count: 3

   >>z

   0, 1.024911e+02, -1.148774e-01
   1, 1.025547e+02, -1.195827e-01
   2, 1.024493e+02, -1.660484e-01

   0, 1.024618e+02, -1.313231e-01
   1, 1.025220e+02, -1.391520e-01
   2, 1.024505e+02, -1.339683e-01

   0, 1.025001e+02, -1.355432e-01
   1, 1.024866e+02, -1.084897e-01
   2, 1.025063e+02, -1.583959e-01

--------------


| <fc #ff0000>DO WE WANT TO INCLUDE ALL THIS INFO HERE</fc>
|

.. important::

   
   Optimizing Single Point Measurements
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   In version 1.3.2, many optimizations were added to reduce the measurement time.
   
   -  The ``initiate`` and ``trigger`` mode (trigger mode), previously used only for external triggers, is now optimized for faster measurements. See `Trigger Input/Output Ports <https://wiki.analog.com/eval-admx2001ebz>`__ for details on how to use trigger mode (also referred to as the WAIT_FOR_TRIGGER state).
   -  When in trigger mode, most commands are disabled. This is because measurement attributes like frequency, gain, magnitude, offset, delays, and others are locked. Locking them means that for each measurement, setup and initialization tasks for those attributes can be skipped because they will always be unchanged. This saves a significant amount of time on each measurement, especially reducing the time between a trigger being received and the measurement acquisition starting.
   
      -  Sweeps do not benefit from this optimization, because the sweep attribute cannot be updated in trigger mode.
      -  If enabled, the DC offset is always on in trigger mode. The autorange must be off to enable the DC offset. Keeping the DC offset enabled constantly can be useful when testing with DUTs that need a long DC settling time, as that delay does not need to be repeated for every measurement.
   
   -  The measurement is only reported over the active interface (UART commmand line interface or SPI). The active interface is set based on the most recently sent command. For instance, if the command ``initiate`` is sent over UART, and then the command TRIGGER (0x18) is sent over SPI, the result will be readable in the SPI FIFO and not accessible on UART. If INITIATE (0x17) is sent over SPI, and then ``trigger`` is sent over UART, the result will print immediately to UART and not be accessible in the SPI FIFO. See `ADMX2001B SPI Interface <:doc:`/wiki-migration/resources/eval/user-guides/admx/eval-admx2001ebz/spi-interface`>`__ for details on how to operate the SPI interface.
   
      -  The SPI interface is the fastest and can save multiple milliseconds over using the UART (command line) interface.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/trigger_mode.png
      :align: center
      :width: 800px
   
   --------------
   
   To achieve the fastest single-point measurement time, there are a few points to consider.
   
   -  Interface: The SPI interface should be used to receive the measurement data. Either interface can be used to configure measurement settings, this will not impact the speed of each measurement. The active interface is updated every time a command is sent, to whichever interface sent that command.
   -  Trigger source: In trigger mode, there are three options for the trigger source.
   
      -  The ``trigger`` command can be sent over the UART (CLI). This is the slowest method, and since ``trigger`` will be the most recent command, it will always report the result over the UART (CLI).
      -  The TRIGGER (0x18) command can be sent over SPI. This is the preferred method as it is fast, and easy to set up. It also guarantees that the active interface will be set to SPI.
      -  A pulse can be applied to the TRIG_IN pin. For this pulse to be registered, external trigger mode must be enabled; see `Trigger Input/Output Ports <https://wiki.analog.com/eval-admx2001ebz>`__. Measurements initiated with the external trigger can report data over either the UART or SPI interfaces, dependent on where the most recent command was received. For instance, this could be the ``initiate`` command in CLI, or INITIATE (0x17) over SPI.
   
   -  Trigger count: when using trigger mode, the trigger count (tcount) sets a condition for automatically exiting trigger mode. It will receive ``tcount``\ \*triggers before returning to the normal operating mode. To continue measuring in trigger mode, the ``initiate`` command is needed to re-enter the mode. To exit trigger mode before completing ``tcount``\ \*triggers, the ``abort`` command can be used (0x1A) in SPI.
   
      -  There is also support for an "infinite" trigger mode. Run ``tcount 65536`` to enter this mode; the only way to exit trigger mode in this case is with the ``abort`` command. Normal ``z`` measurements are disabled when ``tcount`` is set to 65536.
   
   -  Autorange: The autorange should be disabled for the fastest measurements. The autorange tests the ideal gain by taking multiple measurements with different gain settings, and checking for ADC saturation. Therefore, it can significantly increase the measurement time.
   
      -  When using the autorange with trigger mode, the autorange test is performed when the ``initiate`` command runs. See the flow chart above. Leaving and re-entering trigger mode will update the selected gain.
   
   -  Delays: The trigger delay (tdelay) and measurement delay (mdelay) directly impact the measurement time. In trigger mode, the tdelay is applied once per supplied trigger, and the mdelay is supplied once per count (not tcount). Therefore, a typical single measurement will have tdelay+mdelay added on. The default tdelay is 4 ms; this can typically be set to 0 ms with no negative impacts; this is recommended to optimize the measurement time. The default mdelay is 1 ms; at frequencies above 10 kHz, setting this to 0 ms will cause the ADC to capture some data before the AC source has fully turned on. This typically has no impact on the measurement result, allowing 1 ms to be saved per measurement, but it should be tested with each setup.
   -  Frequency: the measurement time is highly dependent on the test frequency below ~3 kHz. This is because the system tries to capture a minimum of 3 cycles of the excitation waveform. See the log plot below for the measurement time across frequency.
   -  Display mode: the measurement time is also dependent on the display mode. Rectangular formats like display mode 6 (R, X) and 15 (G, B) are the fastest, as they require the least processing. Modes with angle in degrees or radians (polar form) can take 2-3 extra milliseconds; see the chart below.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/measurement_time.png
      :align: center
      :width: 1200px
   
   \*Typical measurement times above are based on the following settings:
   
   -  Interface = SPI, SPI trigger source
   -  Mode = trigger mode
   -  mdelay = 0
   -  tdelay = 0
   -  average = 1
   -  calibration = on (can save 1-2 ms turning calibration off)
   -  autorange = off
   
   Note that measurements taken over the UART will be slower.


--------------

Calibration Procedure
^^^^^^^^^^^^^^^^^^^^^

A few milliseconds after power up, the AD-IMP2501DBZ-SL is ready to perform measurements. However, any readings and their units are scaled and assigned using nominal circuit parameters. Measurement accuracy should only be evaluated after performing calibration on the module. Using an external calibration source with certified traceability. For example, the `Keysight E4980A <https://www.keysight.com/us/en/product/E4980A/precision-lcr-meter-20-hz-2-mhz.html>`__ can be used to validate.

There are three basic calibration steps involved in calibrating the module: open calibration, short calibration, and load calibration. The first two correct the module and test lead parasitics. The latter provides traceability to an external source. The calibration steps must be performed in the order open->short->load. Open and load calibration are the most important. Short calibration may need to be skipped in certain gain/load ranges where the current ADC would saturate. Open calibration may need to be skipped in gain/load ranges that the voltage ADC would saturate.

|image6| |image7| |image8|

.. tip::

   When performing load calibration for a given gain setting, the optimal load device (usually a resistor) is one with an impedance magnitude close to that of the eventual load impedance. This will give the best system accuracy.

   
   Resistors, capacitors or inductors can be used for calibration. High-quality resistors (e.g. thin film or metal film), air capacitors, and gas-filled capacitors tend to provide the best results. Alternatively, C0G/NP0 type ceramic capacitors can be used as well. The true value of these components must be determined with traceable measurements from another meter, such as the Keysight E4980A.


Each measurement configuration (ch0 and ch1 gain combination) needs to be calibrated separately. If calibration is performed for only one gain combination, calibration needs to be carried out again if the gain configuration changes. There are a total of **12** possible gain combinations based on the 4 gain and 3 transimpedance settings for channel 0 (voltage) and channel 1 (current) respectively.

If the user calibrates at a specific gain, then changes the load and calibrates again, the user will overwrite the result of the first calibration. Support for calibration over frequency is included and incorporates the entire 1Hz to 1.5MHz range.

Calibration Steps
-----------------

To calibrate the module in a specific gain combination, follow the steps below:

-  Select the desired measurement configuration (gain, magnitude, and offset)
-  Connect the H_POT and H_CUR terminal together and the L_POT and L_CUR terminals together to form two separate connection pairs
-  If using the on board loads, apply the jumpers as designated below:

================== ================ =======================
Jumper Designation Install Position Description
================== ================ =======================
P27                Pins 1-2         EIS HCUR
P28                Pins 1-2         EIS HPOT
P29                Pins 1-2         EIS LPOT
P30                Pins 1-2         EIS LCUR
P23                Pins 1-2         HCUR to HPOT connection
P24                Pins 1-2         LCUR to LPOT connection
P21                Not Installed    User Selectable Load
P22                Not Installed    User Selectable Load
P8                 Not Installed    User Selectable Load
P12                Pins 1-2         EIS HCUR SMA
:::                Pins 5-6         EIS HPOT SMA
:::                Pins 9-10        EIS LPOT SMA
:::                Pins 13-14       EIS LCUR SMA
================== ================ =======================

-  If using test clips or SMA cables that are tied together at the clip, remove jumpers from P23 and P24. Place them so the clips are separated as close to the same distance as they will be when the DUT is connected.

.. note::

   Open calibration at high frequencies and in higher impedance measurement ranges is especially susceptible to error, due to the increased opportunity for coupling into the current measurement path. The test setup is especially important under these conditions


-  Run the ``calopen`` command and follow the prompts when ready.
-  Connect all the measurement terminals together.

   -  When measuring very small impedances, short calibration becomes extremely important. Many fixtures have a low repeatability under these conditions. Optimizing the repeatability of the setup is critical to getting a meaningful result, for both calibration and measurement.
   -  In some instances ``calopen`` or ``calshort`` cannot be run due to the gain or magnitude setting with the desired load. In this instance, do not run the command, the system will use the default values. Alternatively, consider a different gain combination for that desired load.

-  Run the ``calshort`` command, if possible, and follow the prompts when ready.
-  Connect a known impedance between the measurement leads or choose a connection configuration from the on board resistors.
-  Run the ``calload <value1> <value2>`` command where ``<value1>`` is the true resistive value of the component (Ohms) and ``<value 2>`` is the true reactive value of the component (Ohms) and follow the prompts when ready.

   -  To obtain true values of resistive and reactive components beforehand, use a calibrated LCR meter and select Rs and X for the display mode.
   -  For improved results, a standard resistor set like the `Keysight 42030A <https://www.keysight.com/en/pd-1000003832%3Aepsg%3Apro-pn-42030A/four-terminal-pair-standard-resistor-set>`__ can be used.

After completing the steps above, calibration coefficients are generated and stored in RAM. These coefficients will be applied to any subsequent measurements when that gain combination is applied and the calibration is enabled, but will be lost after a power cycle or reset of the module. To store the coefficients in non-volatile memory (flash) the command ``calcommit`` must be executed. For example:

::

   >>calcommit
    Are you sure you want to commit the current calibration data to memory!?

    Press Y/y when ready to proceed or N/n to cancel.
   >>y
    Calibration data committed to memory...
   >>

This will store the calibration coefficients in RAM to flash. Power loss will no longer remove the stored calibration data.

.. note::

   This commit of calibration data does not need to be done immediately after running the calibration. As long as it is completed before the next power loss the data will be saved. Multiple gain combination calibrations can be completed before committing all the data to non-volatile memory.


Calibration Example
-------------------

Calibrate the gain setting (0, 1) with a resistor of value 100 Ohms. <fc #ff0000>The true resistance Rt from the E4980A at 100kHz was measured as 1000.019 Ohms, and the true reactance Xt was 0.822 Ohms.</fc>

::

   >>gain 0 0
    Voltage Gain: x1

   >>gain 1 1
    Current Gain: x500

   >>mag 300
    Signal Magnitude: 300mV

   >>dcoffset 0
    DC Offset: 0mV

   >>calopen

    Beginning open load calibration... Connect the H_POT and H_CUR together and the L_POT and L_CUR together.

    Then hit Y/y when ready to proceed or N/n to cancel.        <--- Connect open load now

   >>y

    Beginning Calibration...

    Calibration Stage Completed...

   >>calshort

    Beginning short load calibration... Connect all the measurement terminals together.

    Then hit Y/y when ready to proceed or N/n to cancel.        <--- Connect short load now

   >>y

    Beginning Calibration...

    Calibration Stage Completed...

   >>calload 100 0

    Beginning user load calibration... Connect known impedance between the measurements leads.

    Then hit Y/y when ready to proceed or N/n to cancel.        <--- Connect calibration load now (100Ω on board resistor)

   >>y

    Beginning Calibration...

    Calibration Stage Completed...

   >>calread 0 1

    Calibration Data
   --------------------------
     R Gain Coeff: -2.409224e+06
     X Gain Coeff: 5.887465e+06
     R Open Coeff: 2.458235e+06
     X Open Coeff: -6.021623e+06
    R Short Coeff: 1.214380e-02
    X Short Coeff: -4.682108e-03
     G Gain Coeff: -7.332180e+01
     B Gain Coeff: -2.819907e+01
     G Open Coeff: 5.811038e-08
     B Open Coeff: 1.423455e-07
    G Short Coeff: 7.168965e+01
    B Short Coeff: 2.764033e+01
   --------------------------

   >>calcommit

    Are you sure you want to commit the current calibration data to memory!?

    Press Y/y when ready to proceed or N/n to cancel.

   >>y

    Calibration data committed to memory...

   >>count 5        <--- simply for more samples
    Count: 5

   >>z        <--- measurement with no calibration enabled

   0, 1.013174e+02, 6.936672e-01
   1, 1.016581e+02, 1.105903e+00
   2, 1.030758e+02, -1.493440e-01
   3, 1.010275e+02, 9.489138e-02
   4, 1.036238e+02, -3.363047e-01

   >>correction 1       
    Correction Mode: Calibration Enabled

   >>z

   0, 9.975729e+01, -5.334712e-01
   1, 1.005431e+02, 2.199431e-01
   2, 1.001880e+02, -5.269702e-01
   3, 1.004466e+02, 1.122557e+00
   4, 9.954122e+01, -1.490209e-01

   >>

Reading Calibration Coefficients
--------------------------------

Calibration coefficients for each gain can be read to the terminal. To read the currently loaded coefficients for a certain gain setting, run the command ``calread <vgain> <igain>``. This prints the 12 AC coefficients to the terminal, where they could be noted for future reference. If the gain combination has not been calibrated yet, the default values will be shown.

::

   >>calread 0 1

    Calibration Data
   --------------------------
     R Gain Coeff: -2.409224e+06
     X Gain Coeff: 5.887465e+06
     R Open Coeff: 2.458235e+06
     X Open Coeff: -6.021623e+06
    R Short Coeff: 1.214380e-02
    X Short Coeff: -4.682108e-03
     G Gain Coeff: -7.332180e+01
     B Gain Coeff: -2.819907e+01
     G Open Coeff: 5.811038e-08
     B Open Coeff: 1.423455e-07
    G Short Coeff: 7.168965e+01
    B Short Coeff: 2.764033e+01
   --------------------------

   >>calread 1 0

    Calibration Data
   --------------------------
     R Gain Coeff: -1.000000e+06
     X Gain Coeff: -1.000000e+06
     R Open Coeff: 1.000000e+06
     X Open Coeff: 1.000000e+06
    R Short Coeff: 0.000000e+00
    X Short Coeff: 0.000000e+00
     G Gain Coeff: -1.000000e+06
     B Gain Coeff: -1.000000e+06
     G Open Coeff: 0.000000e+00
     B Open Coeff: 0.000000e+00
    G Short Coeff: 1.000000e+06
    B Short Coeff: 1.000000e+06
   --------------------------

   >>

All gain combinations that will be utilized should be configured, otherwise the default coefficients will be used even if calibration is turned on. Coefficients must be saved using ``calcommit``; otherwise, they will be lost if the system reboots or loses power.

--------------

Compensation Procedure
----------------------

Compensation is an additional measurement adjustment function designed to account for changes in the test fixture or application setup that were not present during calibration. This feature is useable, but it is also reasonable to recalibrate for each fixture/setup, and use the commands detailed in `Calibration Steps <https://wiki.analog.com/eval-admx2501ebz>`__ to save data for each config.

To configure compensation coefficients, run the same steps in the calibration procedure, but use the ``comp`` commands instead of the ``cal`` commands. Make sure the commands are run with the setup fully intact and all connections to the DUT in place. Refer to the help section on available commands for the specific list and associated names for compensation located at `Available Commands <https://wiki.analog.com/eval-admx2501ebz>`__

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/fishercat_compensation.png
   :align: center
   :width: 600px

--------------

EVAL-ADMX2001EBZ Terminal Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/eval-admx2001ebz_diagram_3.png
   :align: center
   :width: 600px

+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| Terminal Name         | Description                                                                                                               |
+=======================+===========================================================================================================================+
| H_CUR                 | Signal source terminal. It generates the excitation required for measurement. This terminal can source up to +/-5V @ 50mA |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| H_POT                 | Voltage sense terminal. Connect to H_CUR at the device under test (DUT)                                                   |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| L_POT                 | Voltage sense terminal. Connect to L_CUR at the device under test (DUT)                                                   |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| L_CUR                 | Current sense terminal. Return path for the excitation signal. Connect to the opposite end of the DUT as H_CUR            |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| UART TX               | UART transmitter pin. Connect to TX pin on the UART to USB cable. Uses 3.3V logic                                         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| UART RX               | UART receiver pin. Connect to RX pin on the UART to USB cable. Uses 3.3V logic                                            |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| UART GND              | UART ground. Connect to ground pin on the UART to USB cable                                                               |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| CLK_SEL               | Jumper selection of internal or external clock. Set to internal for default operation                                     |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| TRIG_IN               | Trigger input. Use for hardware-timed acquisition only, otherwise leave disconnected                                      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| TRIG_OUT              | Measurement complete trigger out                                                                                          |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| CLK_IN                | External clock input. Use a LVCMOS 50MHz clock signal and set CLK_SEL to EXT position                                     |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| CLK_OUT               | Clock output. These two terminals have a buffered replica of the 50MHz main clock                                         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| PMOD                  | Controller and Peripheral PMOD terminals for SPI port                                                                     |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| Header P6 pins [9-10] | Digital output 0-1                                                                                                        |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| Header P7 pins [1-6]  | Digital output 2-7                                                                                                        |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+

| 

SPI Interface
-------------

The ADMX2001B supports a SPI interface in addition to the UART CLI interface. The SPI bus can be accessed on Header P6 and both PMOD headers of EVAL-ADMX2001EBZ, or pins B14-B17 of the ADMX2001B module. A full command reference for the SPI interface can be found at `ADMX2001B SPI Interface. <:doc:`/wiki-migration/resources/eval/user-guides/admx/eval-admx2001ebz/spi-interface`>`__

Trigger Input / Output Ports
----------------------------

The EVAL-ADMX2001EBZ has SMA terminals for the trigger input and output ports. These can be used to synchronize multiple modules or control measurement timing with an external instrument. To use the trigger input, the module must be configured to external ``trig_mode`` using the command ``trig_mode <internal/external>``. By default, the board is in internal ``trig_mode``, and ignores pulses on the TRIG_IN port. Next, set the trigger count with ``tcount <count>``. This controls how many external triggers the module will respond to before exiting the WAIT_FOR_TRIGGER state. There is also an "infinite" trigger setting; if the tcount is set to 65536, then it will respond to unlimited triggers and never exit the WAIT_FOR_TRIGGER state automatically. Now, type the command ``initiate``. The module will enter the WAIT_FOR_TRIGGER state. Most commands are disabled in this state. The module will automatically return to the IDLE state after receiving ``tcount`` triggers, or immediately if it receives the ``abort`` command. While in the WAIT_FOR_TRIGGER state, a software trigger can be provided with the command ``trigger``, in both internal or external ``trig_mode``. If the ``trig_mode`` is external, then a 3.3V 15μs pulse (min) to the TRIG_IN port will be registered as a trigger.

When a measurement is initiated from the WAIT_FOR_TRIGGER state, either by an external trigger or software trigger, it will generate a 3.3V 15μs pulse on the TRIG_OUT port.

Immediately after running ``initiate``, the autorange algorithm will run (if the autorange is enabled). The gain chosen by this instance of the autorange will be locked in for subsequent measurements in trigger mode. If the DC offset is enabled, then the DC offset will be applied as soon as the ``initiate`` command runs. The DC offset and autorange cannot be used at the same time.

.. important::

   Warning: when the ``initiate`` command is run, the board will reload the calibration data automatically from the flash. Any coefficients that were not committed (saved to the flash) will be lost. This process is the same as running the command ``calibrate reload``. Verify that any calibration data that should be applied during trigger mode measurements is saved for it to be applied, and not lost.


PMOD Headers
------------

The EVAL-ADMX2001EBZ features PMOD_IN and PMOD_OUT headers for interfacing with a host over SPI.

+------------+------------+-----------------------------------------------------------------------+
| Pin Number | Pinout     | Note                                                                  |
+============+============+=======================================================================+
| 1          | No Connect |                                                                       |
+------------+------------+-----------------------------------------------------------------------+
| 2          | SDI        |                                                                       |
+------------+------------+-----------------------------------------------------------------------+
| 3          | SDO        |                                                                       |
+------------+------------+-----------------------------------------------------------------------+
| 4          | SCLK       | 20 MHz max                                                            |
+------------+------------+-----------------------------------------------------------------------+
| 5          | GND        |                                                                       |
+------------+------------+-----------------------------------------------------------------------+
| 6          | VCC        | 3.3V, PMOD_OUT only.

.. important::

   VCC current not limited


|
+------------+------------+-----------------------------------------------------------------------+
| 7          | No Connect |                                                                       |
+------------+------------+-----------------------------------------------------------------------+
| 8          | No Connect |                                                                       |
+------------+------------+-----------------------------------------------------------------------+
| 9          | CS         |                                                                       |
+------------+------------+-----------------------------------------------------------------------+
| 10         | No Connect |                                                                       |
+------------+------------+-----------------------------------------------------------------------+
| 11         | GND        |                                                                       |
+------------+------------+-----------------------------------------------------------------------+
| 12         | VCC        | 3.3V, PMOD_OUT only.

.. important::

   VCC current not limited


|
+------------+------------+-----------------------------------------------------------------------+

Pins 6 and 12 are No Connect on PMOD_IN (P12). On PMOD_OUT (P11), they connect to the 3.3V supply, and there is no current limiting on the board.

Digital Output Pins
-------------------

The ADMX2001B features eight general purpose digital output pins, intended for controlling external MUXes or other peripherals. Support was added in version 1.2.2. The outputs are broken out on EVAL-ADMX2001EBZ, and can be accessed on pins 9-10 of P6, and pins 1-6 of P7. They can be set with the command ``gpio_ctrl <N>`` where N is a decimal from 0-255, and each of the 8 inputs are controlled by the respective bit for that position. Digital output 0 corresponds to the LSB. For instance, configuring ``gpio_ctrl 133`` (1000 0101 in binary) will set high P6 pin 9, and P7 pins 1 and 6.

=================== ========== =========
Header : Pin Number Bit Number N Setting
=================== ========== =========
P6 : 9              0          1
P6 : 10             1          2
P7 : 2              2          4
P7 : 3              3          8
P7 : 4              4          16
P7 : 5              5          32
P7 : 6              6          64
P7 : 7              7          128
=================== ========== =========

--------------

ADMX2001B Pin Configuration and Function Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx2001b_pinout_top.png
   :align: center
   :width: 600px

+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| Pin Number                                | Mnemonic    | Description                                                                                   |
+===========================================+=============+===============================================================================================+
| Center Pad                                | GND         | Ground                                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A1-4, B1-4                                | VDD         | Power supply terminals. Apply +3.3V nominal                                                   |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A18                                       | VCC         | 5V rail, not current limited. Leave unconnected.                                              |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A18                                       | VEE         | -5V rail, not current limited. Leave unconnected.                                             |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A23                                       | CLKIN       | External clock input. Must connect to 50MHz source or CLKOUT terminal                         |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A25                                       | CLKOUT      | Clock output. If using external clock on CLKIN, leave unconnected. Otherwise connect to CLKIN |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A22, A24, A26                             | GND         | Ground                                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B5, B7, B9, B11, B13, B18, B21            | GND         | Ground                                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B10                                       | TRIGIN      | Measurement trigger input. If unused, leave unconnected                                       |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B12                                       | TRIGOUT     | Measurement trigger output. If unused, leave unconnected                                      |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B14                                       | SCK         | Serial data clock input                                                                       |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B15                                       | SDI         | Serial data input                                                                             |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B16                                       | SDO         | Serial data output                                                                            |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B17                                       | CS          | Serial interface port chip select input                                                       |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B19                                       | TX          | UART transmit output. Connect to host’s receiver                                              |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B20                                       | RX          | UART receive input. Connect to host’s transmitter                                             |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B22                                       | JTAG_VCC    | JTAG power out.                                                                               |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B23                                       | TCK         | JTAG test clock.                                                                              |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B24                                       | TDO         | JTAG test data out.                                                                           |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B25                                       | TMS         | JTAG test mode select.                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B26                                       | TDI         | JTAG test data in.                                                                            |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C18-C25                                   | GPIO0-GPIO7 | General-purpose digital output terminals                                                      |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C1, C3, C4, C6, C7, C9, C10, C12-C17, C26 | GND         | Ground                                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| D1, D3, D4, D6, D7, D9, D10, D12          | GND         | Ground                                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C2, D2                                    | HCUR        | Source terminal                                                                               |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C5, D5                                    | HPOT        | Voltage measurement high terminal. Tie to HCUR at the device under test                       |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C8, D8                                    | LPOT        | Voltage measurement low terminal. Tie to LCUR at the device under test                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C11, D11                                  | LCUR        | Current measurement input                                                                     |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| All other pins                            | NC          | Do not connect                                                                                |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+

| 
| ----

Firmware Updates
^^^^^^^^^^^^^^^^

The ADMX2001B module firmware is user-updatable. Programming files must be requested by contacting admx-support@analog.com. Make a myAnalog account on :adi:`(analog.com) <en/index.html>`, by clicking in the top right. Then, email admx-support@analog.com, and mention the email associated with the myAnalog account.


| 
|

.. important::

   Warning: updating between certain firmware versions can cause saved calibration coefficients to be lost.


**Equipment List:**

-  EVAL-ADMX2001EBZ board
-  ADMX2001B Impedance Analyzer Measurement Module
-  Intel Altera USB Blaster `(Terasic) <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=46>`__
-  Universal power adapter with 9VDC output

**Software Prerequisites:**

-  Python 3.7 or greater
-  Latest Intel Quartus Prime Programmer And Tools

   -  Navigate to the downloads page for the latest Quartus Prime Lite Edition, and click the "Additional Software" tab. Alternatively, the full Quartus Prime Lite Edition can be used. Both are free, but the programmer is a smaller download

-  Drivers installed for the Altera USB Blaster
-  Firmware programming folder containing \*.pof file (downloaded from Analog.com, request from admx-support@analog.com)

**Board Programming Setup**

-  Connect the USB Blaster to the computer over USB and verify the driver installation
-  Plug the ADMX2001B module into EVAL-ADMX2001EBZ board
-  Connect the USB blaster to the port labeled "P8 JTAG" on the EVAL-ADMX2001EBZ
-  Connect the EVAL-ADMX2001EBZ to a 9V DC supply

| 

Update Using Installation Script
--------------------------------

| Versions 1.2.4+ comes bundled with an installation script to simplify the firmware installation process.
|

.. note::

   This script is the preferred installation method.


   | \* Follow the steps under **Board Programming Setup**

-  Ensure that Quartus Prime 18.1 or newer is installed in the following path: ``C:\intelFPGA_lite\<version_number>\quartus``
-  Open a command prompt window
-  Navigate to the Tools folder present in the installation directory of ``Admx2001Firmware-Relx.y.z``, ``C:\Analog Devices\Admx2001Firmware-Relx.y.z\Tools``

   -  Here, x, y, & z represents the release number (1.2.4 for example)

-  Run the following command: ``python admx2001_flash_pof.py --pof "C:\Analog Devices\Admx2001Firmware-Relx.y.z\Firmware\admx_lcr_encrypted.pof"``

   -  Ensure that x.y.z is replaced with the appropriate release number (1.2.4 for example)

-  Wait until the message "Programming POF completed successfully" is displayed in the terminal. It may take around 20 to 30 seconds for the process to complete.

   -

.. important::

   Do not unplug the board or otherwise interrupt the programming process.


-  When the programming is completed (message displayed and prompt appears) close the terminal and unplug the USB blaster. The firmware update is complete.

|

| ----

Update Using Manual Programmer
------------------------------

Versions 1.2.2 and older do not come bundled with an installation script. The Quartus Prime Programmer interface can be used to perform the update. The installation script is the preferred method, as selecting the wrong settings in the manual programming tool can cause the board to no longer boot. It will need to be returned/swapped.

If there are issues preventing the installation script from working to program the board, the manual programmer method can be used. In this case, contact admx-support@analog.com for assistance using the manual programmer.

| 
| ----

Firmware Release Highlights
---------------------------

Currently available firmare versions and release highlights:

+---------+--------+-------------------------------------------------------------------------------------------------------------+
| Version | Status | Release Highlights                                                                                          |
+=========+========+=============================================================================================================+
| 1.3.2   | Stable | Measurement time optimizations, minor bug fixes                                                             |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.3.1   | Stable | Substantial measurement noise improvements, bug fixes and more                                              |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.2.4   | Stable | Same firmware as 1.2.2. Installation script added to release package                                        |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.2.2   | Stable | Adds calibration over frequency, configurable digital outputs, external trigger support, bug fixes and more |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.2.0   | Stable | Bug fixes, noise and repeatability improvements. Calibration with complex loads now supported               |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.1.1   | Legacy | Same fixes as 1.2.0, but not compatible with boards using the flash memory.                                 |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.1.0   | Legacy | Added SPI interface and built in self test                                                                  |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.0.1   | Legacy |                                                                                                             |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.0.0   | Legacy |                                                                                                             |
+---------+--------+-------------------------------------------------------------------------------------------------------------+

The full release notes are included with each firmware download.

--------------

Python Scripting
^^^^^^^^^^^^^^^^

To facilitate easier measurement optimization on a PC, there is a library of Python functions which make it easy to operate the command-line interface from a Python script. Instead of typing commands over TeraTerm, the library accesses the Serial port directly, and calling the library functions will execute the same commands that are normally typed into the terminal emulator.

These Python libraries are currently accessible by request. First, make a myAnalog account on :adi:`(analog.com) <en/index.html>` by clicking in the top right. Then, email admx-support@analog.com, and mention the email associated with the myAnalog account.

The Python script download includes an example measurement sweep script, which shows how to set up the Serial port, configure measurements and begin collecting data. More example scripts are coming in the future. Nearly all functions found in the command-line interface have corresponding Python functions in the library. These functions also perform a certain degree of error checking. This library is for evaluation purposes only.

--------------

Python Graphical User Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since firmware version 1.3.2, the firmware downloads include a Python based graphical user interface (GUI). The GUI does not yet support all features of the ADMX2001B, but it provides an quicker start and easier experimentation compared to using the UART command-line interface (CLI). The GUI communicates with the board over the UART CLI in the background, so any open terminals connected to the board need to be closed prior to using the GUI.

The GUI requires some 3rd-party Python libraries. The download includes a README.txt file with instructions on how to download these libraries.

Currently, the GUI supports:

-  Automatic and manual gain selection
-  Calibrated measurements (but not the process of calibrating the board)
-  Continuous or singular measurements
-  18 display modes in SI units
-  Frequency, offset, magnitude and average settings

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx2001b_python_gui_example.png
   :align: center
   :width: 400px

The Python GUI is bundled with the latest firmware downloads and available by request. First, make a myAnalog account on :adi:`(analog.com) <en/index.html>` by clicking in the top right. Then, email admx-support@analog.com, and mention the email associated with the myAnalog account.

Taking Measurements via Python Eval Script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TO BE POPULATED

--------------

--------------

Support
^^^^^^^

For support, general questions, or firmware update help, reach out to admx-support@analog.com.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/fishercat_hardware_setup.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/fishercat_get_default.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/fishercat_help_command_page1.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/fishercat_help_command_page2.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/Source_and_measurement_channels_v3_renumbered.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/open_short_load_config.png
   :width: 800px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/fishercat_open_short_load.png
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/open_short_load_config_photo.png
   :width: 800px
