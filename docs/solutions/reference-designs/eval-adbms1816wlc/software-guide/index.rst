.. _eval-adbms1816wlc software:

Software Guide
==============

This guide provides step-by-step instructions for installing firmware,
configuring the GUI, and evaluating the AD-BMSE2E3WLC-SL system.

Software Resources
------------------

.. note:: **A MyAnalog.com account is required to download the software resources.**

   Follow the steps below to create a MyAnalog account:

   #. Go to :adi:`MyAnalog </>` and create an account using email. Select the **Register with email** option to get started.
   #. Once you have a MyAnalog account, log in using your credentials, then proceed to download the required files listed below.

.. admonition:: Download

    Required software for evaluating the AD-BMSE2E3WLC-SL:

    - :adi:`AD-BMSE2E3WLC-SL Firmware 1.0.0 </en/resources/evaluation-hardware-and-software/embedded-development-software/software-download.html?swpart=SD_EDFIEI2>`
    - `ACE Software 1.30.3522.122 Installer <https://swdownloads.analog.com/ACE/ACEInstall_1.30.3522.122.exe>`__
    - `AD-BMSE2E3WLC-SL ACE GUI Plugin Installer <https://www.analog.com/plugins/ace/board.ADBMSE2E3WLC.1.2026.3330839.acezip>`__
    - `MAX32625PICO Image <https://github.com/analogdevicesinc/max32625pico-firmware-images/raw/master/bin/max32625_max32666fthr_if_crc_swd_v1.0.5.bin>`_
    - Code editor (such as Visual Studio Code)
    - Terminal application (such as Tera Term)

----

Firmware
--------

Prepare the MAX32666FTHR for Firmware Upload
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect the **10-pin SWD ribbon cable** to the **MAX32666FTHR**.
- Connect the other end to the **MAX32625PICO**.
- Connect the **MAX32625PICO** to your PC using a **micro-USB cable**.
- Download the MAX32625PICO image (see link above).
- Extract the contents of the archive and locate the **MAX32625_PICO.bin** file.
- Copy the **MAX32625_PICO.bin** file into the **MAINTENANCE** folder of the connected MAX32625PICO.
- Wait for the transfer to complete.

   .. figure:: max32625_pico_bin_upload.png

      Uploading the MAX32625_PICO.bin file

   **Successful installation indicators:**

    - The device renames to **DAPLINK**.
    - A **MAX32666.HTM** file appears in the folder.

Pre-built Binaries
~~~~~~~~~~~~~~~~~~

Pre-built ``HEX`` files are provided in the ``bin/`` folder for supported
boards. No additional toolchain or build setup is required. Copy the
appropriate file onto the MAX32625PICO DAPLINK debugger drive.

+---------------------------------------------------+------------------+
| File Name                                         | Target Board     |
+===================================================+==================+
| bms_measurement-max32666fthr-iio-2x-adbms1816.hex | MAX32666FTHR     |
+---------------------------------------------------+------------------+
| bms_measurement-max32690fthr-iio-2x-adbms1816.hex | MAX32690FTHR     |
+---------------------------------------------------+------------------+
| bms_measurement-max32690apard-iio-2x-adbms1816.hex| AD-APARD32690-SL |
+---------------------------------------------------+------------------+

These binaries are built with::

   IIO_EXAMPLE = y
   NUM_DEV = 2

The number of active devices is determined at runtime by the VSEL jumper:

   * LOW = 1 device / 48V
   * HIGH = 2 devices / 96V

If a different example or configuration is required, build the firmware
binaries from source.

Flash the Pre-built Binary File into the MAX32666FTHR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Download the ``AD-BMSE2E3WLC-SL Firmware 1.0.0`` package.
- Copy the matching ``HEX`` file (select based on the MCU board used) from the ``bin/`` folder to the DAPLINK drive.
- The MAX32625PICO debugger flashes the MCU and remounts the drive when complete.

   **Verification:**

    - A successful upload is indicated by the absence of a **FAIL.TXT** file
      in the DAPLINK folder.

Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~

The AD-BMSE2E3WLC-SL firmware allows device monitoring and diagnostics through a command-line interface (CLI).
For this purpose, a terminal emulator such as Tera Term is recommended.

- Open the Tera Term application (other terminals can also be used, but Tera Term is recommended).
- Select ``Serial``, then choose the correct COM port number associated with the microcontroller.
- Click the ``Setup`` tab, then ``Serial Port``.

   - Set the speed to **115200**.
   - Then, click the ``New setting`` button.

- Click the ``Setup`` tab, then ``Terminal``.

- Under the New-line setting, set Receive to ``AUTO``.

- Click the hardware ``RESET`` button on the microcontroller board.
- The BMS data will be printed on the Tera Term terminal.

   Sample reading:

   .. figure:: sample-reading-in-cli.png

      Sample BMS Data Output

Building the Firmware from Source
---------------------------------

**Since the AD-BMSE2E3WLC-48V baseboard is MCU-agnostic, users can swap the MAX32666FTHR MCU with any supported Maxim MCU.
The firmware can be built from scratch by following the instructions below:**

Requirements
~~~~~~~~~~~~

Extract the contents of the downloaded ``AD-BMSE2E3WLC-SL Firmware 1.0.0`` zip file. The package already includes no-OS and all
required sources. No git cloning or submodule initialization is required.

Directory structure::

   ad-bmse2e3wlc-sl-firmware-1.0.0/
   ├── bin/
   ├── no-OS/
   ├── no-OS-BMS-Examples-Rel1.0.0/
   │   ├── adbms/
   │   └── examples/
   └── README.md

Install `make <https://www.gnu.org/software/make/>`_ for your operating system.

Then, install Git Bash. The following instructions are provided for each operating system:

Windows
^^^^^^^

Install Git Bash:

   https://git-scm.com/downloads

Then run::

   ./no-OS/tools/scripts/git-bash.sh

Linux (Debian/Ubuntu)
^^^^^^^^^^^^^^^^^^^^^

::

   sudo apt install make

macOS
^^^^^^

::

   xcode-select --install

Build Requirements
~~~~~~~~~~~~~~~~~~

For Maxim Platform
^^^^^^^^^^^^^^^^^^

* Download and install MaximSDK:

  https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A

Recommended installation locations:

+----------+--------------------------------------------+
| OS       | Recommended Install Path                   |
+==========+============================================+
| Windows  | ``C:\MaximSDK``                            |
+----------+--------------------------------------------+
| Linux    | ``$HOME/msdk``                             |
+----------+--------------------------------------------+
| macOS    | ``$HOME/msdk``                             |
+----------+--------------------------------------------+

For more information on setting up and building no-OS projects:
https://developer.analog.com/docs/no-os/latest/build_guides/build_maxim.html


Build Instructions
~~~~~~~~~~~~~~~~~~

For Maxim Build
^^^^^^^^^^^^^^^

1. Open a terminal.

+---------------+---------------------------------------------+
| OS            | Terminal                                    |
+===============+=============================================+
| Windows       | Git Bash or MSYS2                           |
+---------------+---------------------------------------------+
| Linux/macOS   | Any standard terminal (bash, zsh, etc.)     |
+---------------+---------------------------------------------+

2. Set the ``MAXIM_LIBRARIES`` environment variable.

   Windows (Git Bash / MSYS2)::

      export MAXIM_LIBRARIES=/c/MaximSDK/Libraries

   Linux / macOS::

      export MAXIM_LIBRARIES=$HOME/msdk/Libraries


3. Change to the examples directory::

      cd no-OS-BMS-Examples-Rel1.0.0/examples

   Select the desired example by editing the Makefile:

   .. code-block:: makefile

      # Select the example measurement (Note: Select 1 example at a time)

      ADBMS1816_BASIC = n
      ADBMS1816_BALANCING = n
      ADBMS1816_DCC_BALANCING = n
      ADBMS1816_FUEL_GAUGE = n
      IIO_EXAMPLE = y

.. note::

   Only one example should be set to ``y`` at a time.

Board Auto-Detection
^^^^^^^^^^^^^^^^^^^^

Supported TARGET suffixes:

   * ``max32665fthr`` - MAX32665/MAX32666FTHR
   * ``max32690apard`` - APARD32690
   * ``max32690fthr`` - MAX32690FTHR
   * ``max32690`` - defaults to APARD32690

.. note::

   The Maxim toolchain uses ``max32665`` for both MAX32665 and MAX32666.
   Use ``max32665fthr`` when building for MAX32666FTHR.

Example::

   make TARGET=max32665fthr

Build::

   make TARGET=max32665fthr

Use a different no-OS path::

   make TARGET=max32665fthr NO-OS=<path to no-OS>

Run::

   make TARGET=max32665fthr NO-OS=<path to no-OS> run

Clean::

   make TARGET=max32665fthr NO-OS=<path to no-OS> clean

Reset::

   make TARGET=max32665fthr NO-OS=<path to no-OS> reset

Open VS Code project::

   make TARGET=max32665fthr NO-OS=<path to no-OS> maxim_sdkopen

Currently Supported MCUs
^^^^^^^^^^^^^^^^^^^^^^^^

   * MAX32666FTHR
   * MAX32690FTHR
   * AD-APARD32690-SL

Refer to::

   examples/src/platform/maxim/parameters.h

for pinouts.

----

General Configuration Options
-----------------------------

.. code-block:: makefile

   # Total Number of ADBMS devices in the chain
   NUM_DEV = 2

   # Delay in milliseconds
   MEASUREMENTS_FREQ_MS = 1000

   # Set to 0 for continuous measurements
   NUM_MEAS_LOOP = 1

   # Set to y when measuring execution time
   TIME_PROFILING ?= n

   # Use a separate serial port
   NO_OS_USB_UART = y

.. note::

   ``NUM_DEV`` is a compile-time setting. The actual number of active devices
   is determined at runtime by the VSEL jumper.

   * Jumper LOW  -> 48V stack / 1 device
   * Jumper HIGH -> 96V stack / 2 devices

   Ensure that the jumper position matches the hardware configuration.

Example Measurements
~~~~~~~~~~~~~~~~~~~~~

Available example flags:

.. code-block:: makefile

   ADBMS1816_BASIC = n
   ADBMS1816_BALANCING = n
   ADBMS1816_DCC_BALANCING = n
   ADBMS1816_FUEL_GAUGE = n
   IIO_EXAMPLE = n

.. note::

   Each example prints the device ID register values.

ADBMS1816_BASIC
^^^^^^^^^^^^^^^

Performs basic daisy-chain measurements using N x ADBMS1816 devices.

Measures:

   * Cell voltages
   * VSTACK
   * Pack current
   * Auxiliary voltages
   * Temperature

Example::

   ADBMS1816 (1) Unique ID: 0xXX 0xXX 0xXX 0xXX 0xXX 0xXX
   ADBMS1816 (2) Unique ID: 0xXX 0xXX 0xXX 0xXX 0xXX 0xXX

   Cell 1 = X.XXXX V
   ...
   Cell 16 = X.XXXX V

   VSTACK = XX.XXXX V
   Current = X.XXXX A
   Temperature = XX.XX deg C

ADBMS1816_BALANCING
^^^^^^^^^^^^^^^^^^^

Performs PWM (Pulse Width Modulation) balancing.

Key parameters:

   * ``BAL_THRESHOLD_RAW``
   * ``BAL_DCTO``
   * ``WDG_TIMEOUT_MS``

Example::

   PWM Balancing Round 1
   ^^^^^^^^^^^^^^^^^^^^^

   Cell 1 = X.XXXX V
   ...
   Cell 16 = X.XXXX V

   Min cell voltage = X.XXXX V

   Cells above threshold (10 mV):
      Dev 1 Cell 3: delta = XX counts, PWM duty = X/15

   Entering extended balancing (DCTO = 5 min)...

   Balancing complete. All cells within threshold.

ADBMS1816_DCC_BALANCING
^^^^^^^^^^^^^^^^^^^^^^^^

Performs DCC (Direct Cell Control) balancing.

Key parameters:

   * ``BAL_THRESHOLD_RAW``
   * ``DCC_PHASE_DURATION_MS``
   * ``KEEPALIVE_INTERVAL_MS``

Example::

   DCC Balancing Round 1
   ^^^^^^^^^^^^^^^^^^^^^

   Min cell voltage = X.XXXX V

   --- Odd Phase (60s) ---
   Discharging cells: Dev 1 [1,3,5,7,9,11,13,15]

   --- Even Phase (60s) ---
   Discharging cells: Dev 1 [2,4,6,8,10,12,14,16]

   Balancing complete. All cells within threshold.

ADBMS1816_FUEL_GAUGE
^^^^^^^^^^^^^^^^^^^^

Estimates:

   * State of Charge (SoC)
   * State of Health (SoH)

Features:

   * Coulomb counter support
   * OCV re-anchoring
   * Fixed-point arithmetic
   * Automatic channel detection

Example::

   --- Device 0 ---

   CellV=X.XXXX V  SoC=NN.nn %  SoH=NN.nn %
   ...

   CellV=0.0000 V (unconnected)

   Pack SoC (weakest cell): NN.nn %
   Pack SoH (weakest cell): NN.nn %

   Equivalent full cycles: N

----

Graphical User Interface (GUI)
------------------------------

Setup
~~~~~

**Step 1: Download Required Files**

    - Download the plugin package: **Board.ADBMSE2E3WLC ACEZIP.zip** (save locally)
    - Download the latest :adi:`ACE software <ace>` from Analog Devices.

    .. figure:: ace-download.png

        ACE Software Download

**Step 2: Install ACE Software**

    - Run the installer.
    - Follow on-screen installation steps, as shown in the following figures:

    .. figure:: ace-installation.png
        :width: 800 px
    
        ACE Software Installation Steps

    - Verify installation via the Start Menu.

    .. figure:: ace-start-menu.png
       :align: center

       ACE Software Start Menu Verification

**Step 3: Load Plugin**

    - Run the downloaded ``ACEZIP file``.

    - Accept the prompt warning about unapproved EULA plugins.

    .. figure:: plugin-tou.png
       :width: 500 px

    - Continue to load the plugin.

   .. figure:: test-plugin.png

        AD-BMSE2E3WLC-SL Plugin

Launching and Configuring the GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - Power up the hardware setup again (connect all USB cables to the PC or to a USB hub).

    - Launch ACE and **double-click the plugin**.

    - Open **Settings** (as in the figure below).

    .. figure:: ace-homepage.png

        ACE GUI Homepage

**Configure Serial Communication**

    - Open **Device Manager** and note the **COM port number**.

    .. figure:: device-manager-comport.png

       Device Manager COM Port Detection

In ACE:

1. Go to **Settings → Serial Ports** and enter the detected COM port.

2. Set **Protocol = IIO**, then ``Enable`` the port.

3. Click ``OK`` to apply the settings.

    .. figure:: ace-serial-ports-config.png

       ACE Serial Port Settings

4. Restart ACE.

   Expected Result: Plugin **AD-BMSE2E3WLC-48V** appears.

    .. figure:: ad-bmse2e3wlc-48v-plugin.png

       ACE Plugin Detection

.. note::

    If the plugin does not appear or load in the ACE GUI, verify the installed libiio version on your PC.

    |

    To check the installed version:

    1. Open ``Control Panel`` → ``Programs and Features`` (or Settings → Apps → Installed Apps).

        .. figure:: libiio-check.png

           Control Panel - Programs and Features

    2. Locate libiio in the list of installed programs.
    3. Verify that the installed version is **0.26**.
    
        .. figure:: libiio-version.png
            :width: 500 px

            Installed libiio Version Check

    The ACE plugin requires **libiio v0.26** to function correctly. 
    If an earlier version is installed (for example, v0.25), please upgrade to v0.26 using the following link:

    https://github.com/analogdevicesinc/libiio/releases/download/v0.26/libiio-0.26.ga0eca0d2-setup.exe

----

GUI Overview
~~~~~~~~~~~~

The AD-BMSE2E3WLC GUI provides real-time monitoring of
battery-pack parameters, cell voltages, current measurements,
operating state, and temperature information. The dashboard is
designed to provide a quick overview of battery health and
system status during evaluation and testing.

.. figure:: gui.png

    AD-BMSE2E3WLC-SL GUI

Main Dashboard Layout
^^^^^^^^^^^^^^^^^^^^^

The GUI is divided into three primary sections:

1. System Status Indicators (Top Middle Section)
2. Vehicle State and Temperature Monitoring (Top Right Section)
3. Individual Cell Voltage Monitoring (Bottom Section)

Stack Voltage Gauge
^^^^^^^^^^^^^^^^^^^

The **Stack Voltage** gauge displays the total voltage of the
battery pack.

    Purpose

    * Monitors overall pack voltage.
    * Confirms proper connectivity of all battery cells.
    * Verifies battery charging and discharging behavior.

    Displayed Information:

    * Real-time pack voltage value.
    * Green indicator showing normal operation.
    * Gauge range covering the supported battery stack voltage.

    Example

    * Displayed value: **86.70V**

**Module Current Gauge**

The **Module Current** gauge displays the instantaneous battery
current.

    Purpose

    * Indicates whether the battery is charging or discharging.
    * Monitors load current and charging current.

    Current Direction

    * Positive (+) Current: Charging
    * Negative (-) Current: Discharging

    Example

    * Displayed value: **-1.95A**
    * Indicates the battery is supplying current to a load.

**Max Charge Current Gauge**

The **Max Charge Current** gauge displays the allowable charging
current configured by the BMS.

    Purpose

    * Indicates the maximum current permitted during charging.
    * May be limited by battery conditions, temperature, or safety
      requirements.

    Monitoring Use

    * Verify charging limits before connecting a charger.
    * Validate BMS protection settings.

    Example

    * Displayed value: **0A**

**Max Discharge Current Gauge**

The **Max Discharge Current** gauge displays the allowable
discharge current.

    Purpose

    * Indicates the maximum current available to the load.
    * Helps validate discharge protection behavior.

    Monitoring Use

    * Verify discharge capability during driving conditions.
    * Observe current-limit changes caused by faults or temperature
      restrictions.

    Example

    * Displayed value: **1.95A**

Vehicle State Selection
^^^^^^^^^^^^^^^^^^^^^^^

The **Vehicle State** panel allows the user to select and
monitor the current operating mode.

Available States:

+----------+--------------------------------------------------+
| State    | Description                                      |
+==========+==================================================+
| Parked   | Low-activity mode; output path disabled or       |
|          | limited.                                         |
+----------+--------------------------------------------------+
| Driving  | Vehicle is actively supplying power to the load. |
+----------+--------------------------------------------------+
| Charging | Battery is connected to a charging source.       |
+----------+--------------------------------------------------+
| Fault    | System enters protection mode due to an          |
|          | abnormal condition.                              |
+----------+--------------------------------------------------+

Purpose

Vehicle states control the behavior of the BMS and allow users
to evaluate operating-state transitions during system testing.

Temperature Sensors
^^^^^^^^^^^^^^^^^^^

The **Temperature Sensors** section displays temperature
measurements from connected thermistors.

    Displayed Information

    * BMS 1 temperature channels
    * BMS 2 temperature channels

    Purpose

    * Monitor battery-pack temperature.
    * Verify thermistor operation.
    * Evaluate thermal protection functionality.

    Typical Applications

    * Overtemperature testing
    * Thermal characterization

Cell Voltage Monitoring
^^^^^^^^^^^^^^^^^^^^^^^

The lower section of the GUI displays individual cell voltages
for each monitored battery cell.

    **BMS 1 Cell Monitor**

    * Cells 1 to 16
    * Individual voltage readings
    * Battery charge indicators

    **BMS 2 Cell Monitor**

    * Cells 1 to 16
    * Individual voltage readings
    * Battery charge indicators

Visual Indicators
^^^^^^^^^^^^^^^^^

+------------------------+--------------------------------------+
| Indicator              | Meaning                              |
+========================+======================================+
| Green Check Mark       | Parameter or cell voltage is within  |
|                        | the normal operating range.          |
+------------------------+--------------------------------------+
| Battery Icon           | Visual representation of the cell    |
|                        | level or status.                     |
+------------------------+--------------------------------------+
| Green Battery Level    | Cell voltage is present and measured |
|                        | successfully.                        |
+------------------------+--------------------------------------+
| Voltage Reading        | Actual measured cell voltage value.  |
+------------------------+--------------------------------------+
| Gauge Pointer in Green | Measurement is within expected       |
| Region                 | operating limits.                    |
+------------------------+--------------------------------------+
| Fault State Selected   | Protective action is active or a     |
|                        | fault condition has been detected.   |
+------------------------+--------------------------------------+

The dashboard serves as the primary real-time monitoring
interface for validating pack voltage, current flow, cell voltages, 
temperatures, and operating-state transitions during evaluation.

----

Functional Testing Using GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware Connectivity Verification Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    - Change the pin header setting for the EVAL-ADBMS1816WLC from **pin 2→3 to pin 1→2**

        .. figure:: shunt-connection-mode.png
            :width: 300 px

            EVAL-ADBMS1816WLC Connection Mode Setting

    - Open the ACE GUI and run the plugin.

        - Expected: No output on BMS2

        .. figure:: without-bms-output.png
            :width: 800 px

            EVAL-ADBMS1816WLC without BMS2 Output

    - Restore P17 to its **original setting (pin 2→3)**:

        - Output on BMS2 should now be present.

        .. figure:: with-bms2-output.png
            :width: 800 px

            EVAL-ADBMS1816WLC with BMS2 Output

Voltage Adjustment Test
^^^^^^^^^^^^^^^^^^^^^^^

**Minimum Voltage Test**

1. Rotate both DC2472A knobs **clockwise** (for the minimum setting).

2. Expected readings:

     - Cell voltage: **1.3V to 1.7V**

     - Stack voltage: decreases

    .. figure:: min-voltage-test.png
       :width: 650 px

       AD-BMSE2E3WLC-SL Minimum Voltage Test

**Maximum Voltage Test**

1. Rotate both DC2472A knobs **counterclockwise** (for the maximum setting).
2. Expected readings:

    - Cell voltage: **4.0V to 5.0V**

    - Stack voltage: increases

    .. figure:: max-voltage-test.png
       :width: 650 px

       AD-BMSE2E3WLC-SL Maximum Voltage Test

   You may adjust one emulator at a time to observe the changes clearly.

----

Output Power Delivery Test
^^^^^^^^^^^^^^^^^^^^^^^^^^

Measure using a **Digital Multimeter (DMM)**:

    - Connect **DMM (–)** to **Ground**.
    - Connect **DMM (+)** to **TP23**.

   Expected reading: **4.0V to 4.7V**

In GUI:

    - Set **Vehicle State = Driving**.
    - Verify the voltage again.

    .. figure:: driving-mode-pd.png
       :width: 650 px

       AD-BMSE2E3WLC-SL Power Delivery Test - "Driving" Mode

    **Vehicle State = Parked**

    .. figure:: parked-mode-pd.png

       AD-BMSE2E3WLC-SL Power Delivery Test - "Parked" Mode

|

**Shutdown Procedure**

Follow this sequence to safely power down:

1. Disconnect power from MAX32666FTHR microcontroller.
2. Disconnect power from both DC2472A battery cell emulators.
3. Remove all cables.
4. Return hardware to proper storage.
