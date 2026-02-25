.. _eval-cn0216-ardz:

EVAL-CN0216-ARDZ
================

Precision Weigh Scale Signal Conditioning System.

Overview
--------

:adi:`CN0216 <CN0216>` is a precision weigh scale signal conditioning system.
It uses the :adi:`AD7791`, a low power buffered 24-bit sigma-delta ADC along
with two external :adi:`ADA4528-1` (or dual :adi:`ADA4528-2`) zero-drift
amplifiers. This solution allows for high dc gain with a single supply.

Ultralow noise, low offset voltage, and low drift amplifiers are used at the
front end for amplification of the low-level signal from the load cell. The
circuit yields 15.3 bit noise-free code resolution for a load cell with a
full-scale output of 10 mV.

This circuit allows great flexibility in designing a custom low-level signal
conditioning front end that gives the user the ability to easily optimize the
overall transfer function of the combined sensor-amplifier-converter circuit.
The :adi:`AD7791` maintains good performance over the complete output data
range, from 9.5 Hz to 120 Hz, which allows it to be used in weigh scale
applications that operate at various low speeds.

.. figure:: cn0216-simplified_schematic.png
   :align: center

   CN0216 Simplified Schematic

Evaluation Board Variants
-------------------------

The CN0216 circuit is available in several evaluation board form factors:

- **EVAL-CN0216-SDPZ** -- Connects to ADI's System Demonstration Platform
  (SDP-B) via the 120-pin connector. Powered by a +6 V supply.
- **EVAL-CN0216-PMDZ** -- PMOD-compatible form factor.
- **EVAL-CN0216-ARDZ** -- Arduino shield form factor for use with
  EVAL-ADICUP360 or Arduino Uno baseboards.

EVAL-CN0216-SDPZ Software User Guide
-------------------------------------

Required Equipment
~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B Board)
- :adi:`EVAL-CN0216-SDPZ <EVAL-CN0216-SDPZ>` evaluation board (CN0216 Board)
- :adi:`EVAL-CFTL-6V-PWRZ` (+6 V power supply) or equivalent
- CN0216 Evaluation Software
- USB Type-A to USB Mini-B cable
- PC with Windows XP SP2 or later (32-bit), USB port, 1 GHz processor,
  512 MB RAM, 500 MB free disk space
- Tedea-Huntleigh Model 1042 load cell (or any 4- or 6-wire load cell)

.. note::

   Any 4- or 6-wire load cells can be used with the CN0216 Board. This guide
   was written with the Tedea-Huntleigh Model 1042 in mind.

General Setup
~~~~~~~~~~~~~

- The EVAL-CN0216-SDPZ (CN0216 Board) connects to the :adi:`EVAL-SDP-CB1Z`
  (SDP-B Board) via the 120-pin connector.
- The :adi:`EVAL-CFTL-6V-PWRZ` (+6 V DC power supply) powers the CN0216 Board
  via the DC barrel jack.
- The SDP-B Board connects to the PC via the USB cable.
- The load cell connects to the CN0216 Board via the 8-pin header.

.. figure:: cn0216-test_setup.png
   :align: center

   CN0216 Test Setup

Connecting the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

Connect the Tedea-Huntleigh (Model 1042) load cell to the 8-pin header of the
EVAL-CN0216-SDPZ (CN0216 Board) as depicted below.

.. note::

   If a different load cell is used other than the Tedea-Huntleigh Model 1042,
   the wiring schematic will be different.

.. figure:: cn0216-wiring_table.png
   :align: center

   Load Cell Wiring Table

.. figure:: cn0216-wiring_schematic.png
   :align: center

   Load Cell Wiring Schematic

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Control and Indicator Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0216-software.png
   :align: center

   CN0216 Evaluation Software -- Main Tab

.. figure:: cn0216-software2.png
   :align: center

   CN0216 Evaluation Software -- Calibrate System Tab

.. list-table::
   :header-rows: 1
   :widths: 10 25 65

   * - #
     - Control
     - Description
   * - 1
     - Connect/Reconnect Button
     - Makes a USB connection to the CN0216 Board via the SDP-B Board. A
       connection must be made before using the software.
   * - 2
     - Run Button
     - Collects conversion data and presents the acquisitions in the chart.
   * - 3
     - Stop Button
     - Stops collecting data from the CN0216 Board.
   * - 4
     - Clear Chart Button
     - Clears all data collected from the chart history.
   * - 5
     - Control Tabs
     - **Main** -- Data collection chart. **Calibrate System** -- System
       configuration settings.
   * - 6
     - Current Weight Indicator
     - Displays the mass (in grams) on the load cell.
   * - 7
     - Chart Controls
     - Zoom-in, zoom-out, and pan through the data collected.
   * - 8
     - Select Units Radio Buttons
     - Determines the Y-axis units of the data displayed in the chart.
   * - 9
     - System Status String
     - Displays a message detailing the current state of the software.
   * - 10
     - System Status LED
     - Displays the current state: Inactive, Busy, or Error.
   * - 11
     - Calibration Weight Control
     - Set to the weight of the object used to calibrate the load cell.
   * - 12
     - Calibrate Button
     - Initiates the calibration of the load cell.
   * - 13
     - ADC Mode Radio Buttons
     - Sets the mode of the AD7791. Default is **Unbuffered Mode**.
       **Buffered Mode** turns the on-chip analog input buffer ON.
       **Unbuffered Mode** turns it OFF.
   * - 14
     - ADC Channel Select
     - Selects the analog input channel. Default is **AIN(+)-AIN(-)**.
       Options: AIN(+)-AIN(-) (normal), AIN(-)-AIN(-) (shorted inputs),
       Vdd Monitor (attenuated by 5 using internal 1.17 V reference).
   * - 15
     - Update Rate Radio Buttons
     - Changes the output word rate. Default is **9.5 Hz**.
   * - 16
     - Configure ADC Button
     - Applies the current ADC Mode, Channel Select, and Update Rate settings.

Establishing a USB Connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install the software and connect the hardware.
#. Open **CN0216.exe** from the installation directory.

   .. note::

      Default location: ``C:\Program Files\Analog Devices\CN0216\CN0216.exe``

#. Click the **Connect/Reconnect** button. A progress bar window will appear.
#. Upon success, the System Status will display *SDP Board Ready to Acquire
   Data*.

Capturing Data
^^^^^^^^^^^^^^

#. Establish a USB connection.
#. Click the **Run** button.
#. Click the **Stop** button when acquisition is complete.

Calibrating the Load Cell
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Establish a USB connection.
#. Click the **Calibrate System** control tab.
#. Set the **Calibration Weight** control to the weight (in grams) of the
   calibration weight.
#. Place the calibration weight on the load cell.
#. Click the **Calibrate** button and wait for calibration to complete.

   .. figure:: cn0216-calibrate-wait.png
      :align: center

      Calibration in progress

#. Remove the calibration weight when prompted.

   .. figure:: cn0216-calibrate-continue.png
      :align: center

      Remove calibration weight prompt

#. Click the **Continue** button.
#. Wait for calibration to complete.

EVAL-CN0216-ARDZ Arduino Shield
-------------------------------

For hardware details and software demos using the EVAL-CN0216-ARDZ Arduino
shield with the EVAL-ADICUP360, see the subpages below.

.. toctree::

   hardware
   software

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   EVAL-CN0216-ARDZ Design & Integration Files (Rev C and Rev B available)

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Gerber Files
   - Allegro Board Files

Documents
---------

- :adi:`CN0216 Circuit Note <CN0216>`

Additional Information
----------------------

- :adi:`AD7791 Product Page <AD7791>`
- :adi:`ADA4528-1 Product Page <ADA4528-1>`
- :adi:`ADA4528-2 Product Page <ADA4528-2>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
