.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0376

.. _eval-cn0376-ardz:

EVAL-CN0376-ARDZ
=================

Dual-Channel Isolated Thermocouple/RTD Temperature Measurement System.

Overview
--------

:adi:`CN0376 <CN0376>` is a dual-channel, channel-to-channel isolated,
thermocouple or RTD input suitable for programmable logic controllers (PLC) and
distributed control systems (DCS). Each channel can accept either a
thermocouple or an RTD input. The entire circuit is powered from a standard
24 V bus supply.

The :adi:`AD7124-4` 24-bit sigma-delta ADC with programmable gain array (PGA)
and voltage reference provides the complete set of features to implement a
flexible input capable of connection to either thermocouple or RTD sensors.
Features include on-chip reference, PGA, excitation currents, bias voltage
generator, and flexible filtering with enhanced 50 Hz and 60 Hz rejection
options. The AD7124-4 is in a small 5 mm x 5 mm LFCSP package, making it ideal
in channel-to-channel isolated designs where space is a premium. It also
includes multiple diagnostic functions available to the user.

The :adi:`ADuM5010` isolated dc-to-dc converter provides 3.3 V isolated power
via integrated isoPower technology. The :adi:`ADuM1441` isolates the SPI
interface for the AD7124-4. The ADuM1441 micropower isolator consumes only
4.8 uA per channel when idle, resulting in an energy efficient solution.

The :adi:`ADP2441` 36 V step-down dc-to-dc regulator accepts an industrial
standard 24 V supply, with wide tolerance on the input voltage, and steps it
down to 5 V to be used by the system.

The EVAL-CN0376-SDPZ connects to ADI's System Demonstration Platform (SDP) and
also features PMOD-compatible headers for interfacing with other development
platforms.

.. figure:: cn0376_board.png
   :align: center
   :width: 600

   EVAL-CN0376-SDPZ Evaluation Board

Required Equipment
------------------

- :adi:`EVAL-CN0376-SDPZ <EVAL-CN0376-SDPZ>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B Board)
- DC power supply (+12 V to +24 V)
- RTD (PT100 or PT1000)
- Thermocouple
- CN0376 Evaluation Software
- PC with Windows Vista/7 (32-bit), USB Type-A port, 1 GHz processor,
  1 GB RAM, 500 MB free disk space
- USB Type-A to USB Mini-B cable

General Setup
-------------

.. figure:: board_guide.png
   :align: center
   :width: 600

   EVAL-CN0376-SDPZ Board Layout

- The EVAL-CN0376-SDPZ (CN0376 Board) connects to the :adi:`EVAL-SDP-CB1Z`
  (SDP-B Board) via the 120-pin connector.
- The SDP-B Board connects to the PC via the USB cable.
- Header **P4** is a PMOD-compatible SPI header for communication to Channel 1.
- Header **P5** is a PMOD-compatible SPI header for communication to Channel 2.
- Header **PWR_SEL** selects the power source (Terminal Block P3 or PMOD) using
  a jumper.
- Terminal block **P3** is the power supply input (input range: +5.5 V to
  +36 V DC).
- Terminal block **P1** is the sensor input (RTD or thermocouple) for
  Channel 1.
- Terminal block **P2** is the sensor input (RTD or thermocouple) for
  Channel 2.

Sensor Connection
~~~~~~~~~~~~~~~~~

.. figure:: wiring_guide.png
   :align: center
   :width: 500

   Sensor Wiring Guide

**2-Wire RTD:**

- Connect RTD to AIN+ and AIN- terminals
- Short terminals IEXC and AIN+
- Short terminals RETURN and AIN-

**3-Wire RTD:**

- Connect RTD wires to AIN+, AIN-, and RETURN terminals
- Short terminals IEXC and AIN+

**4-Wire RTD:**

- Connect RTD to IEXC, AIN+, AIN-, and RETURN terminals

**Thermocouple:**

- Connect thermocouple to AIN+ and AIN- terminals

Power Options
~~~~~~~~~~~~~

**Jumper Position EXT:**

.. figure:: pwr_sel2.png
   :align: center
   :width: 200

   EXT jumper position

- System is powered using terminal block P3 (input range: +5.5 V to +36 V DC)
- When no supply is present on P3, the system draws power from USB when using
  the SDP

**Jumper Position PMOD:**

.. figure:: pwr_sel1.png
   :align: center
   :width: 200

   PMOD jumper position

- System is powered using the PMOD headers (+3.3 V DC)

Installing the Evaluation Software
-----------------------------------

#. Extract the file **CN0376_Evaluation_Software.zip** and open **setup.exe**.

   .. note::

      It is recommended to install the CN0376 Evaluation Software to the
      default path ``C:\Program Files\Analog Devices\CN0376\`` and all
      National Instruments products to ``C:\Program Files\National Instruments\``.

#. Click **Next** to view the installation review page.
#. Click **Next** to start the installation.
#. Upon completion, the ADI SDP Drivers installer will execute.

   .. note::

      Close all other applications before clicking "Next" to allow system file
      updates without rebooting.

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      Recommended path: ``C:\Program Files\Analog Devices\SDP\Drivers``

#. Press **Next** to install the SDP Drivers. Click **Finish** when done.

Using the Evaluation Software
------------------------------

Software Control and Indicator Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Main Tab
^^^^^^^^

.. figure:: software_main_1.png
   :align: center
   :width: 600

   CN0376 Evaluation Software -- Main Tab

.. list-table::
   :header-rows: 1
   :widths: 10 25 65

   * - #
     - Control
     - Description
   * - 1
     - Run/Stop
     - Start/Stop data acquisition from the evaluation board.
   * - 2
     - Clear Data
     - Clear the data on the chart and on voltage/current indicators.
   * - 3
     - Save Data
     - Save the collected data to a tab-delimited ASCII spreadsheet file.
   * - 4
     - Reset
     - Reset the evaluation board and software to the default startup
       configuration.
   * - 5
     - Channel 1 Temperature Display
     - Displays the temperature reading from Channel 1 (degrees Celsius).
   * - 6
     - Channel 1 RTD Resistance / TC Voltage Display
     - Displays the RTD resistance (in RTD mode) or thermocouple voltage
       (in TC mode) for Channel 1.
   * - 7
     - Channel 2 Temperature Display
     - Displays the temperature reading from Channel 2 (degrees Celsius).
   * - 8
     - Channel 2 RTD Resistance / TC Voltage Display
     - Displays the RTD resistance (in RTD mode) or thermocouple voltage
       (in TC mode) for Channel 2.
   * - 9
     - Cold Junction Compensation
     - Displays the temperature and resistance of the CJC thermistor of both
       channels when in thermocouple mode.
   * - 10
     - Display Units
     - **Temperature** -- Data displayed in degrees Celsius.
       **ADC Code** -- Data displayed as ADC codes.
   * - 11
     - Chart
     - Data plot for the data acquisition (voltage/current or ADC code).
   * - 12
     - Status Bar
     - Displays the current state of the software: Inactive, Busy, or Error.

Histogram Tab
^^^^^^^^^^^^^

.. figure:: software_histogram_1.png
   :align: center
   :width: 600

   CN0376 Evaluation Software -- Histogram Tab

.. important::

   User needs to sample data first using **Run** to get histogram data on this
   page.

.. list-table::
   :header-rows: 1
   :widths: 10 25 65

   * - #
     - Control
     - Description
   * - 1
     - Select Channel
     - Channel selection for histogram display.
   * - 2
     - Get Histogram
     - Analyzes the data from the selected channel and displays the histogram.
   * - 3
     - Maximum Code
     - Highest code from the sampled data of the selected channel.
   * - 4
     - Minimum Code
     - Lowest code from the sampled data of the selected channel.
   * - 5
     - Code Spread
     - Difference between the highest and lowest code.
   * - 6
     - Peak-to-Peak Resolution
     - Computed peak-to-peak resolution (bits) of the selected channel.
   * - 7
     - Histogram Graph
     - Plot for the histogram data.

Configuration Tab
^^^^^^^^^^^^^^^^^

Allows ADC configuration of either channel.

.. figure:: software_config.png
   :align: center
   :width: 600

   CN0376 Evaluation Software -- Configuration Tab

**Input Type:**

- **PT100** -- Activates the excitation current source and configures the ADC
  to read from PT100 RTD.
- **PT1000** -- Activates the excitation current source and configures the ADC
  to read from PT1000 RTD.
- **Thermocouple** -- Activates the TC bias, CJC, and configures the ADC to
  read from thermocouple.

**RTD Connection:**

- **2-Wire** -- Excitation current available at IEXC pin. Short IEXC and AIN+
  pins. Short AIN- and RETURN pins.
- **3-Wire** -- Matched excitation currents available at IEXC and AIN- pins.
- **4-Wire** -- Excitation current available at IEXC pin. Short IEXC and AIN+
  pins.

**Power Mode** -- Select Power Mode of the ADC. This affects power consumption
and ADC data rate. Consult the :adi:`AD7124-4` datasheet for more information.

**Filter Type** -- Select the digital filter used for ADC conversion. Consult
the AD7124-4 datasheet for more information.

**Post Filter** -- Select the data rate when post filters are used.

**Sampling Rate** -- Slider control to change the ADC data rate. The numerical
display shows the corresponding data rate. This is dependent on the power mode
and filter type.

**Enabled/Disabled** -- Toggle to enable or disable the corresponding channel.

**Configure** -- Press this button to apply the configurations to the
corresponding channel.

Advanced Configuration Tab
^^^^^^^^^^^^^^^^^^^^^^^^^^

Allows control of excitation current, burnout current, PGA gain, and enables
ADC error checks.

.. figure:: software_advconfig.png
   :align: center
   :width: 600

   CN0376 Evaluation Software -- Advanced Configuration Tab

Error Flags Tab
^^^^^^^^^^^^^^^

ADC error indicators. Consult the :adi:`AD7124-4` datasheet for information
regarding the ADC errors.

Running the System
~~~~~~~~~~~~~~~~~~

#. Open the **CN0376.exe** application from the default installation location.
#. The software will connect to the board automatically.
#. Click the **Run** button.
#. Click the **Stop** button when acquisition is complete.

Saving Data to a Spreadsheet File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Click the **Save Data** button.
#. Browse to the directory location where the spreadsheet file is to be saved.
#. Name the file.
#. Click the **OK** button.

.. note::

   The software saves the spreadsheet file as ASCII text with columns separated
   by tabs.

Documents
---------

- :adi:`CN0376 Circuit Note <CN0376>`

Additional Information
----------------------

- :adi:`AD7124-4 Product Page <AD7124-4>`
- :adi:`ADuM5010 Product Page <ADuM5010>`
- :adi:`ADuM1441 Product Page <ADuM1441>`
- :adi:`ADP2441 Product Page <ADP2441>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
