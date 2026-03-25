.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ltpa-rl2000

.. _eval-ltpa-rl2000:

EVAL-LTPA-RL2000
=================

Portable USB Efficiency Meter.

Overview
--------

The EVAL-LTPA-RL2000 is a portable, USB efficiency meter based on the
LTpowerAnalyzer that allows you to plot DC efficiency and power loss of a DC-DC
power supply, across multiple values of load current. This instrument operates
independently and does not require the ADALM2000 or the
:ref:`EVAL-LTPA-KIT <eval-ltpa-kit>` main board.

.. figure:: eval-ltpa-rl2000_angle-evaluation-board.jpg
   :align: center

   EVAL-LTPA-RL2000 efficiency meter

Key capabilities:

- Two ±125 V DC voltmeters for input/output voltage measurement
- 30 A DC current meter with programmable 0--5 V voltage drop for power supply
  input
- 30 A (150 W max) DC current load for power supply output
- Internal temperature sensing with rear-mounted cooling fan
- Thermal protection for high-power applications (70 °C shutdown)
- USB-C interface for data and power

Specifications
--------------

.. list-table::
   :header-rows: 1
   :widths: 40 20 20 20

   * - Parameter
     - Min
     - Max
     - Units
   * - **Voltmeters**
     -
     -
     -
   * - Input DC Voltage Range
     - ±125
     -
     - V
   * - Resolution
     - 1
     -
     - mV
   * - Input Impedance
     - 2
     -
     - MOhm
   * - Accuracy [1]_
     - 0.01 + 0.01
     -
     - %
   * - **Current Meter**
     -
     -
     -
   * - Input DC Current Range
     - 10 x 10\ :sup:`-6`
     - 30
     - A
   * - Resolution (10 uA range)
     -
     - 10
     - nA
   * - Resolution (100 uA range)
     -
     - 10
     - nA
   * - Resolution (1 mA range)
     -
     - 100
     - nA
   * - Resolution (10 mA range)
     -
     - 1
     - uA
   * - Resolution (100 mA range)
     -
     - 10
     - uA
   * - Resolution (1 A range)
     -
     - 100
     - uA
   * - Resolution (10 A range)
     -
     - 1
     - mA
   * - Resolution (30 A range)
     -
     - 1
     - mA
   * - Accuracy [1]_
     - 0.025 + 0.01
     -
     - %
   * - Servo Voltage Accuracy [1]_
     - 0.01 + 0.01
     -
     - %
   * - Shutdown Temperature
     - 70
     -
     - °C
   * - **Current Load**
     -
     -
     -
   * - DC Load Current Range
     - 10 x 10\ :sup:`-6`
     - 30
     - A
   * - Accuracy [1]_
     - 0.025 + 0.01
     -
     - %
   * - Load Voltage
     -
     - 75
     - V
   * - Load Power
     -
     - 150
     - W
   * - Shutdown Temperature
     - 70
     -
     - °C

.. [1] Accuracy specification: ± (% of reading + % of range)

About Efficiency Measurements
-----------------------------

Efficiency is calculated as the ratio of a power supply's output power to its
input power. Simply put, it is a measure of how much of the input power can be
converted into useful output and supplied to the load.

Efficiency is a critical parameter for evaluating power supply design
performance. Excessive power loss increases energy consumption and unwanted heat
dissipation. Low efficiency results in shorter battery life and higher board
temperatures.

To measure efficiency:

1. Determine input power and output power by measuring the respective voltages
   and currents.
2. Efficiency varies with load current (e.g., ~92% at 10 A versus significantly
   less at light loads).
3. It is essential to plot efficiency across multiple load current values for a
   complete characterization.

.. figure:: 32._rl2000.png
   :align: center

   Example efficiency plot

The generic test setup uses a programmable current load to sweep the output
current of the device under test (DUT). An ammeter measures the input current
while two voltmeters monitor the input and output voltages. From these
measurements, input power, output power, efficiency, and power loss can be
calculated.

.. figure:: 31._rl2000.png
   :align: center

   Efficiency test setup diagram

Hardware Interface
------------------

USB-C Connector
~~~~~~~~~~~~~~~

The USB-C interface connects to the host PC for power and data communication.
The LTpowerAnalyzer software automatically detects the RL2000 efficiency meter
and displays its control interface window during start-up.

.. figure:: eval-ltpa-rl2000_front-evaluation-board.jpg
   :align: center

   EVAL-LTPA-RL2000 front panel

Terminals
~~~~~~~~~

The EVAL-LTPA-RL2000 has four pairs of terminals:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Terminal Pair
     - Function
   * - Current 1
     - Current Meter (±) Terminals. Measures input supply current of DUT.
   * - Voltage 1
     - Voltmeter 1 (±) Terminals. Measures input supply voltage of DUT.
   * - Voltage 2
     - Voltmeter 2 (±) Terminals. Measures output voltage of DUT.
   * - Current 2
     - Current Load (±) Terminals. Programmable load for DUT.

Hardware Setup
--------------

Setup Requirements
~~~~~~~~~~~~~~~~~~

- EVAL-LTPA-RL2000 (LTpowerAnalyzer RL2000 Efficiency Meter)
- Device Under Test (e.g., LT8642S Demo Board)
- DC Power Supply

It is recommended to use short cables to connect the RL2000 to the DUT to
minimize parasitics.

.. figure:: 33._rl2000.png
   :align: center

   Hardware setup overview

Connection Procedure
~~~~~~~~~~~~~~~~~~~~

**Step 1:** Connect the Current 1 terminals between the (+) terminal of the
input power source and the (+) input of the DUT. This monitors the input
current.

**Step 2:** Connect the Voltage 1 terminals across the (+) and (-) input pins
of the DUT. This measures the voltage at the input.

**Step 3:** Connect the Voltage 2 terminals across the (+) and (-) output pins
of the DUT. This measures the voltage at the output.

**Step 4:** Connect the Current 2 terminals across the (+) and (-) output pins
of the DUT. This serves as the programmable load for sweeping the output
current.

**Step 5:** Connect a USB-C cable from your PC to the USB port on the RL2000 to
complete the setup.

Example Setup Using the LT8642S Demo Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following diagram shows the hardware setup using the LT8642S demo board
(included with the :ref:`EVAL-LTPA-KIT <eval-ltpa-kit>`) as the DUT.

.. figure:: 37._rl2000.png
   :align: center

   Example setup using the LT8642S demo board

Typical Applications
--------------------

Basic Setup
~~~~~~~~~~~

.. figure:: 25._rl2000.png
   :align: center

   Basic efficiency measurement setup

Basic Setup with Servo Voltage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how the input voltage (V1) remains relatively stable
when the servo voltage is enabled.

.. figure:: 26._rl2000.png
   :align: center

   Basic setup with servo voltage enabled

Basic Setup with Micro-Power DUT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For low-power DUTs, leakage currents into Voltage 1 and Voltage 2 can skew
current measurements. The RL2000 can compensate for this in the software by
calculating the leakage currents and removing them from the measured currents,
as well as adding settling time to allow the load current time to stabilize.

.. figure:: 34._rl2000.png
   :align: center

   Basic setup with micro-power DUT

Basic Setup with Negative Output Voltages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The RL2000 is also capable of measuring negative voltages.

.. figure:: 30._rl2000.png
   :align: center

   Setup for negative output voltage measurement

Setup for DUTs with Multiple Power Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to use two RL2000s to measure the efficiency of a DUT
with two input supplies. In this test case, the output power measurement of the
top RL2000 is disabled in the software.

.. figure:: 28._rl2000.png
   :align: center

   Setup for DUTs with multiple power inputs

Setup for Higher Load Currents (>30 A)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load currents up to 60 A can be achieved by sharing the load current between two
RL2000s connected in parallel. In this test case, the input power measurement of
the top RL2000 is disabled in the software.

.. figure:: 29._rl2000.png
   :align: center

   Setup for higher load currents using two RL2000s in parallel

Setup for Low Output Voltages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At low output voltages, the current load may not produce accurate load current
depending on settings. An easy way to compensate for this is to use a second
supply to bias the output with a negative voltage.

.. figure:: 35._rl2000.png
   :align: center

   Setup for low output voltages (schematic)

.. figure:: 36._rl2000.png
   :align: center

   Setup for low output voltages (wiring)

Making an Efficiency Plot Measurement
-------------------------------------

This section provides a step-by-step guide for using the DC Sweep feature of
the LTpowerAnalyzer software to create an efficiency plot.

.. figure:: 14._rl2000.png
   :align: center

   LTpowerAnalyzer software status bar showing RL2000 connection

Check the status bar at the bottom of the main window to confirm the RL2000
efficiency meter connection with no errors. The DC sweep is done entirely by the
RL2000 without the M2K, main board, or current probe.

Step 1: Run a DC Sweep
~~~~~~~~~~~~~~~~~~~~~~~

1. Click on the **DC Sweep** tab.
2. Select the meter for sweeping load current. If multiple RL2000s are
   connected, use the **Blink Led** function to identify the selected meter.
3. Set start and end values for the sweep.
4. Select the sweep rate (**Logarithmic** or **Linear**).
5. Set the number of data points per decade (logarithmic) or intervals (linear).
6. Click the **Run** button to start the load current sweep and efficiency
   measurement.
7. When complete, select measurement data (efficiency, power loss, etc.) for Y1
   and Y2 axes. Adjust graph settings as needed.

.. figure:: 17._rl2000.png
   :align: center

   DC Sweep measurement setup and graph

Step 2: Rename the Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Click on the **DATA** tab on the right.
2. Click on the Name value to change. Type the desired waveform name and press
   **ENTER** or **RETURN**.

The legend will automatically be updated to the new name.

.. figure:: 10._rl2000.png
   :align: center

   Renaming measurement waveforms

Step 3: Edit the Title
~~~~~~~~~~~~~~~~~~~~~~

1. Right-click on the graph and select **Edit Title**.
2. Type in the new title.
3. Click the **OK** button.

The plot title will be automatically updated to the new title.

.. figure:: 18._rl2000.png
   :align: center

   Editing the plot title

.. figure:: 19._rl2000.png
   :align: center

   Updated plot title

Step 4: Add a Text Annotation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Right-click on the graph and select **Add Text Annotation**.
2. Type in the text annotations.
3. Click the **OK** button.

Select the new annotation by placing the cursor over it and then left-click. The
annotation can then be resized and moved as needed.

.. figure:: 20._rl2000.png
   :align: center

   Adding a text annotation

.. figure:: 21._rl2000.png
   :align: center

   Editing the annotation text

.. figure:: 22._rl2000.png
   :align: center

   Annotation placed on the graph

Step 5: Saving Results
~~~~~~~~~~~~~~~~~~~~~~

1. Select the **Save** option in the File tab: **File > Save**.
2. Enter the file name of the saved data.
3. Click **Save**. A Data File type will save the setup and the data.

The Setup File type will only save the setup.

.. figure:: 23._rl2000.png
   :align: center

   Save dialog

.. figure:: 24._rl2000.png
   :align: center

   Save file name entry

Software Interface
------------------

RL2000 Control Panel
~~~~~~~~~~~~~~~~~~~~

The RL2000 control panel automatically appears as a separate window in the
LTpowerAnalyzer software when an efficiency meter is connected.

.. figure:: 1._rl2000.png
   :align: center

   RL2000 control panel

Power Loss and Efficiency Measurements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Measurement
     - Description
   * - Input Power
     - Total input power of the device under test.
   * - Output Power
     - Total output power of the device under test.
   * - Power Loss
     - Total power loss of the device under test.
   * - Efficiency
     - Efficiency of the device under test.

Meter Selection
^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Control
     - Function
   * - Select Meter
     - Selects the meter being actively controlled by the interface. Meters are
       numbered by the order of connection.
   * - Blink Led
     - Blinks front panel LED. Used to identify the selected meter when multiple
       RL2000s are connected.
   * - Reset
     - Returns all meter settings to default values.
   * - Info
     - Displays information about the meter (hardware/firmware versions, serial
       number, serial port, etc.).

Input Meter Readings
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Reading
     - Description
   * - Input Voltage
     - DC input voltage of DUT. Measured across Voltage 1 terminals.
   * - Input Current
     - DC input current of DUT. Measured through Current 1 terminals.
   * - Input Power
     - DC input power of DUT. Calculated using Voltage 1 and Current 1
       measurements.
   * - Efficiency (checkbox)
     - Input power measurement enable. Adds input power reading to total used in
       power loss and efficiency calculations.
   * - VM Comp
     - Voltmeter current compensation enable. Applies offset to input current
       reading to compensate for leakage current through Voltage 1 terminals.
       Improves measurement accuracy at low current values.

Output Meter Readings
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Reading
     - Description
   * - Output Voltage
     - DC output voltage of DUT. Measured across Voltage 2 terminals.
   * - Output Current
     - DC output current of DUT. Measured through Current 2 terminals.
   * - Output Power
     - DC output power of DUT. Calculated using Voltage 2 and Current 2
       measurements.
   * - Efficiency (checkbox)
     - Output power measurement enable. Adds output power reading to total used
       in power loss and efficiency calculations.
   * - VM Comp
     - Voltmeter current compensation enable. Applies offset to output current
       reading to compensate for leakage current through Voltage 2 terminals.
       Improves measurement accuracy at low current values.

Meter Settings
^^^^^^^^^^^^^^

**Sample Rate:** Selects the measurement speed of the internal converters.
Higher speed settings are faster, but result in a noisier measurement.

**Settling Time:** Sets the amount of time to wait for the load current to
settle before performing a measurement.

**Servo Voltage:** Sets the amount of voltage drop across the input current
meter (Current 1). The servo voltage enable checkbox activates the servo voltage
function for the input current meter.

**Load Current:** Sets the amount of output current drawn by the current load
(Current 2).

- **Zero:** Resets the load current setting to zero amperes.
- **Enable:** Current load enable checkbox to activate Current 2.
- **Share:** Current share enable checkbox to automatically divide load current
  equally among all connected meters.

Status Bar
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Status
     - Description
   * - Error
     - Error code if a problem occurs during operation. Displays "No Error" if
       functioning properly.
   * - Temperature
     - Internal temperature of current meter and load. Fan activates
       automatically at 32 °C. Shutdown occurs at 70 °C.

DC Sweep Measurement and Graph Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The measurement setup is on the left side of the DC Sweep window. Click on the
**GRAPH** tab on the right to bring up the graph setup.

.. figure:: 13._rl2000.png
   :align: center

   DC Sweep measurement and graph setup

DC Sweep Measurement Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**RL2000 Section:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Control
     - Function
   * - Select Meter
     - Selects the meter for sweeping load current. Meters are numbered by the
       order of connection.
   * - Blink Led
     - Blinks front panel LED to identify the selected meter when multiple
       RL2000s are connected.
   * - Reset
     - Returns all meter settings to default values.
   * - Info
     - Displays meter information (hardware/firmware versions, serial number,
       serial port, etc.).

**Sweep Section:**

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Parameter
     - Range
     - Description
   * - Start Current
     - 1 uA to 30 A
     - Sets the initial load current value in the DC sweep.
   * - End Current
     - 1 uA to 30 A
     - Sets the final load current value in the DC sweep.
   * - Points Per Decade / Total Intervals
     - 1 to 200
     - Sets number of points per decade for logarithmic sweeps, or number of
       intervals for linear sweeps.
   * - Log
     - ---
     - Logarithmic sweep. Sweeps load current values in logarithmic scale.
   * - Linear
     - ---
     - Linear sweep. Sweeps load current values in linear scale.
   * - Run / Stop
     - ---
     - Triggers start of DC sweep. Click again to stop a sweep in progress.
   * - Append
     - ---
     - Append data checkbox. Check to plot next sweep on existing graph.
       Unchecked erases previous graphs.

DC Sweep Graph Setup
^^^^^^^^^^^^^^^^^^^^

**X Axis:**

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Parameter
     - Range
     - Description
   * - Minimum
     - 1 uA to 100 A
     - Lower bound for X-axis.
   * - Maximum
     - 1 uA to 100 A
     - Upper bound for X-axis.
   * - AutoScale
     - ---
     - X-axis data automatically scaled.
   * - Log
     - ---
     - X-axis data plotted using log-10 scale.
   * - Increments
     - 1 to 20 divisions
     - Number of major divisions.

**Y1 Axis:**

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Parameter
     - Range
     - Description
   * - Data
     - ---
     - Parameter plotted on Y1 axis [2]_.
   * - Minimum
     - -1000 to 990
     - Lower bound for Y1-axis.
   * - Maximum
     - -990 to 1000
     - Upper bound for Y1-axis.
   * - AutoScale
     - ---
     - Y1-axis data automatically scaled.
   * - Log
     - ---
     - Y1-axis data plotted using log-10 scale.
   * - Increments
     - 1 to 20 divisions
     - Number of major divisions.

**Y2 Axis:**

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Parameter
     - Range
     - Description
   * - Data
     - ---
     - Parameter plotted on Y2 axis [2]_.
   * - Minimum
     - -1000 to 990
     - Lower bound for Y2-axis.
   * - Maximum
     - -990 to 1000
     - Upper bound for Y2-axis.
   * - AutoScale
     - ---
     - Y2-axis data automatically scaled.
   * - Log
     - ---
     - Y2-axis data plotted using log-10 scale.
   * - Increments
     - 1 to 20 divisions
     - Number of major divisions.

.. [2] Parameters available for Y1 and Y2 axes: Input Voltage (V1), Input
   Current (I1), Output Voltage (V2), Output Current (I2), Efficiency, Input
   Power (Power1), Output Power (Power2), Power Loss, Load Current (Iload).

Additional Information
----------------------

- :adi:`EVAL-LTPA-RL2000 Product Page <EVAL-LTPA-RL2000>`
- :adi:`EVAL-LTPA-KIT Product Page <EVAL-LTPA-KIT>`
- :ref:`EVAL-LTPA-KIT Overview <eval-ltpa-kit>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
