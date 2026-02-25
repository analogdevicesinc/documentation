.. _eval-cn0235-sdpz:

EVAL-CN0235-SDPZ
=================

Fully Isolated Lithium Ion Battery Monitoring System.

Overview
--------

:adi:`CN0235` is a fully isolated lithium ion battery monitoring system.
Lithium ion (Li-Ion) battery stacks contain a large number of individual cells
that must be monitored correctly in order to enhance the battery efficiency,
prolong the battery life, and ensure safety.

The 6-channel :adi:`AD7280A` devices act as the primary monitor, providing
accurate voltage measurement data to the System Demonstration Platform (SDP-B)
evaluation board, and the 6-channel :adi:`AD8280` devices act as the secondary
monitor and protection system. Both devices can operate from a single wide
supply range of 8 V to 30 V and operate over the industrial temperature range
of -40 degC to +105 degC.

The :adi:`AD7280A` contains an internal +/-3 ppm reference that allows a cell
voltage measurement accuracy of +/-1.6 mV. The ADC resolution is 12 bits and
allows conversion of up to 48 cells within 7 us. It also has cell balancing
interface outputs designed to control external FET transistors to allow
discharging of individual cells and forcing all the cells in the stack to have
identical voltages.

The :adi:`AD8280` functions independently of the primary monitor and provides
alarm functions indicating out of tolerance conditions. It contains its own
reference and LDO, both of which are powered completely from the battery cell
stack. The reference, in conjunction with external resistor dividers, is used
to establish trip points for the over/undervoltages. Each cell channel contains
programmable deglitching (D/G) circuitry to avoid alarming from transient input
levels.

Required Equipment
------------------

- :adi:`EVAL-CN0235-SDPZ <EVAL-CN0235-SDPZ>` evaluation board
- :adi:`EVAL-SDP-CB1Z` evaluation board (SDP-B board)
- CN0235 evaluation software (supplied with provided CD in kit)
- USB Type-A plug to USB Mini-B plug cable
- +6 V wall wart power supply
- PC with minimum requirements:

  - Windows XP SP2, Windows Vista, or Windows 7
    Business/Enterprise/Ultimate editions
  - Intel Pentium processor (x86 compatible), 1 GHz or faster
  - 512 MB RAM and 2 GB available hard disk space
  - .NET 3.5 Framework

General Setup
-------------

- The :adi:`EVAL-CN0235-SDPZ <EVAL-CN0235-SDPZ>` **(CN0235 Board)** connects
  to the :adi:`EVAL-SDP-CB1Z` **(SDP-B Board)** via the 120-pin SMD connector.
- The CN0235 Board is powered by a +6 V wall wart via the DC barrel jack.
- The SDP-B Board connects to the PC via the USB cable.

.. figure:: cn0235_general_setup.png
   :align: center

   CN0235 general setup

.. list-table:: General Setup Callouts
   :header-rows: 1
   :widths: 10 90

   * - #
     - Description
   * - 1
     - **SDP USB connection** -- Connect to PC through USB Type-A to mini-USB.
   * - 2
     - **Jumper Configuration** -- Sets AD8280 and AD7280A configuration (see
       Jumper Configuration section below).
   * - 3
     - **VIN0 to VIN6** -- Lithium ion battery stacks input. Used when only
       one device is required. See the AD7280A datasheet page 17 and page 22
       for proper battery connection for different numbers of cells.
   * - 4
     - **VIN7 to VIN12** -- Lithium ion battery stacks input. Used when two
       devices are required. See the AD7280A datasheet page 18 for proper
       battery cell connection using two devices.
   * - 5
     - **Power Supply** -- The board may be powered using a +6 V wall wart
       connected to the barrel jack or using an external power supply
       configured to +6 V.
   * - 6
     - **SPI breakout pins** -- Breakout pins of the digital lines coming from
       the SDP board to AD7280A devices.

Jumper Configuration
~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0235_jumper_config.png
   :width: 200 px
   :align: center

   AD8280 Jumper Configurations

.. list-table::
   :header-rows: 1
   :widths: 15 45 40

   * - Jumper
     - Description
     - Configuration
   * - NPTC
     - Selects NTC or PTC thermistor for AD8280's VTx inputs
     - HIGH: PTC thermistor; LOW: NTC thermistor
   * - ALARMSEL
     - Selects three separate alarms or one shared alarm for AD8280
     - HIGH: Three separate alarms; LOW: One shared alarm
   * - DGT0, DGT1, DGT2
     - Sets the deglitch time for AD8280 for transient immunity at cell inputs
     - Deglitch time may be set from 0 s to 10 s. Refer to the AD8280
       datasheet page 20 table 7.
   * - SEL0, SEL1
     - Sets the number of cells to be monitored for AD8280
     - The number of cells may be set to three, four, five, or six. Refer to
       the AD8280 datasheet page 19 table 5.
   * - J31 : J36
     - Sets the bottom AD7280A auxiliary ADC inputs
     - Required for temperature measurement
   * - J20 : J29
     - Sets the top AD7280A auxiliary ADC inputs
     - Required for temperature measurement
   * - J30 and J12
     - AD7280A's Vreg and ground male headers
     - Leave open

Connecting the Hardware
-----------------------

.. figure:: cn0235_hardware.jpg
   :align: center

   CN0235 hardware setup

#. Connect the :adi:`EVAL-CN0235-SDPZ <EVAL-CN0235-SDPZ>` to the
   :adi:`EVAL-SDP-CB1Z` (SDP Board) through the 120-pin SMD connector. Nylon
   hardware should be used to firmly secure the two boards, using the holes
   provided at the ends of the 120-pin connectors.
#. Set the jumpers correctly based on the desired evaluation settings (see
   Jumper Configuration section above).
#. Plug the mini-USB side of the cable into connector J1 on the SDP Board and
   leave the USB Type-A side disconnected.
#. Connect the battery stack to J1 and J2 based on the number of cells
   configured by SEL0 and SEL1.
#. Plug in the wall wart and connect it to the barrel jack connector on the
   EVAL-CN0235-SDPZ.
#. Connect the USB Type-A side of the USB cable to the PC.

Software Installation
---------------------

#. Extract **CN0235 Eval Software.zip** and run **setup.exe**.

   .. note::

      It is recommended to install the CN0235 evaluation software to the
      default directory path ``C:\Program Files\Analog Devices\CN0235\`` and
      all National Instruments products to
      ``C:\Program Files\National Instruments\``.

   .. figure:: cn0235-software-1.png
      :align: center

      CN0235 software installer

#. Click **Next** to view the installation review page.

   .. figure:: cn0235-software-2.png
      :align: center

      Installation review page

#. Click **Next** to start the installation.

   .. figure:: cn0235-software-3.png
      :align: center

      Installation progress

#. Upon completion, the installer for the **ADI SDP Drivers** will execute.

   .. note::

      Close all other applications before clicking **Next** to allow updating
      relevant system files without rebooting.

   .. figure:: cn0235-software-4.png
      :align: center

      SDP Drivers installer start

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended to install the drivers to the default directory path
      ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: cn0235-sdp_installer-1.png
      :align: center

      SDP Drivers installation location

#. Press **Next** to install the SDP Drivers and complete the installation.
   Click **Finish** when done.

   .. figure:: cn0235-sdp_installer-2.png
      :align: center

      SDP Drivers installation complete

Using the Evaluation Software
-----------------------------

Software Front Panel
~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0235_sw_frontpanel.png
   :align: center

   CN0235 evaluation software front panel

The evaluation software front panel provides the following controls and
indicators:

#. **Connect to SDP-B Board Button** -- Establishes a USB connection between
   the SDP-B Board and the CN0235 Board. A connection must be made before
   using the software.
#. **Device Selector** -- Selects the number of devices to be activated.
#. **Enable Real Time ADC Reads** -- When checked, continuous data acquisition
   by the ADC starts.
#. **Read ADC** -- Performs a single capture read by the ADC.
#. **Software Reset** -- Reverts all configuration changes back to default
   state.
#. **Hardware PD** -- Puts the :adi:`AD7280A` into Full Power-Down mode (only
   5 uA maximum current) and disables the :adi:`AD8280`.
#. **Software PD** -- Puts the :adi:`AD7280A` into Software Power-Down mode
   (only 3.8 mA maximum current) and disables the :adi:`AD8280`.
#. **Software/Hardware PU** -- Powers up the :adi:`AD7280A` from software or
   hardware power-down mode. Does not enable the :adi:`AD8280`.
#. **Enable/Disable AD8280** -- Enables or disables the secondary battery
   monitoring and protection system.
#. **Self-Test AD8280** -- Executes the self-test feature of the AD8280.
#. **Save Data to File** -- Records the voltage and temperature readings of
   both devices in codes and volts format. The file may be saved as .txt or
   .xls.

Control Tabs
~~~~~~~~~~~~

Voltage (Codes) Tab
^^^^^^^^^^^^^^^^^^^

The voltage (code format) tab features two types of display:

**Tank Display**

.. figure:: cn0235_voltagecodes_tank_display.png
   :align: center

   Voltage (Codes) tank display

The tank display provides the ADC code equivalent of the reading in bar-like
comparison for each channel. This type of display provides the latest reading
of the lithium ion battery cells.

**Graph Display**

.. figure:: cn0235_voltagecodes_graph_display.png
   :align: center

   Voltage (Codes) graph display

The graphical display tab provides the user with more features or options for
the reading analysis.

#. **Codes vs Sample graph** -- This plot provides the user with the behavior
   of each cell in a form of a line chart, enabling the user to picture out the
   current behavior of each lithium ion cell with time.
#. **Latest channel code value** -- Similar to the tank display, this is the
   latest reading of the lithium ion battery cells by the AD7280A.
#. **Plot navigator** -- Allows the user to see the history of the battery
   reading.
#. **Additional graph functions** -- The three additional functions act as a
   pointer, plot view modifier, and manual plot navigator respectively.

A right-click on the graph will give the user additional plot and data control
features.

.. figure:: cn0235_graph_display_rightclick.png
   :align: center

   Graph display right-click context menu

Voltage (Volts) Tab
^^^^^^^^^^^^^^^^^^^

The voltage (volts format) tab features two types of display:

**Tank Display**

.. figure:: cn0235_voltagevolts_tank_display.png
   :align: center

   Voltage (Volts) tank display

The tank display provides the ADC voltage equivalent of the reading in bar-like
comparison for each channel. This type of display provides the latest reading
of the lithium ion battery cells.

**Graph Display**

.. figure:: cn0235_voltagevolts_graph_display.png
   :align: center

   Voltage (Volts) graph display

The graphical display tab provides the user with more features or options for
the measurement analysis.

#. **Codes vs Sample graph** -- This plot provides the user with the behavior
   of each cell in a form of a line chart, enabling the user to picture out the
   current behavior of each lithium ion cell with time.
#. **Latest channel code value** -- Similar to the tank display, this is the
   latest reading of the lithium ion battery cells by the AD7280A.
#. **Plot navigator** -- Allows the user to see the history of the battery
   reading.
#. **Additional graph functions** -- The three additional functions act as a
   pointer, plot view modifier, and manual plot navigator respectively.

Temperature (Codes) Tab
^^^^^^^^^^^^^^^^^^^^^^^^

The temperature (codes format) tab features two types of display:

**Tank Display**

.. figure:: cn0235_tempcodes_tank_display.png
   :align: center

   Temperature (Codes) tank display

The tank display provides the ADC code temperature reading of the thermistor
in bar-like comparison for each channel. This type of display provides the
latest reading of the lithium ion battery cells.

**Graph Display**

.. figure:: cn0235_tempcodes_graph_display.png
   :align: center

   Temperature (Codes) graph display

The graphical display tab provides the user with more features or options for
the reading analysis.

#. **Codes vs Sample graph** -- This plot provides the user with the behavior
   of each cell in a form of a line chart, enabling the user to picture out the
   current behavior of each lithium ion cell with time.
#. **Latest channel code value** -- Similar to the tank display, this is the
   latest reading of the lithium ion battery cells by the AD7280A.
#. **Plot navigator** -- Allows the user to see the history of the battery
   reading.
#. **Additional graph functions** -- The three additional functions act as a
   pointer, plot view modifier, and manual plot navigator respectively.

Temperature (Volts) Tab
^^^^^^^^^^^^^^^^^^^^^^^^

The temperature (volts format) tab features two types of display:

**Tank Display**

.. figure:: cn0235_tempvolts_tank_display.png
   :align: center

   Temperature (Volts) tank display

The tank display provides the ADC voltage equivalent of the thermistor reading
in bar-like comparison for each channel. This type of display provides the
latest reading of the lithium ion battery cells.

**Graph Display**

.. figure:: cn0235_tempvolts_graph_display.png
   :align: center

   Temperature (Volts) graph display

The graphical display tab provides the user with more features or options for
the measurement analysis.

#. **Codes vs Sample graph** -- This plot provides the user with the behavior
   of each cell in a form of a line chart, enabling the user to picture out the
   current behavior of each lithium ion cell with time.
#. **Latest channel code value** -- Similar to the tank display, this is the
   latest reading of the lithium ion battery cells by the AD7280A.
#. **Plot navigator** -- Allows the user to see the history of the battery
   reading.
#. **Additional graph functions** -- The three additional functions act as a
   pointer, plot view modifier, and manual plot navigator respectively.

Configure AD7280A Tab
^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0235_config_ad7280a.png
   :align: center

   AD7280A configuration tab

#. **Force Update** -- Updates the AD7280A configuration.
#. **Voltage and Temperature Thresholds** -- Sets ceiling and floor values
   for voltage and temperature that determine when warning indicators
   activate.
#. **Conversion Averaging** -- Sets the AD7280A's conversion averaging
   feature where acquisition and conversion of each cell input is repeated
   before results are read back through the SPI interface.
#. **Acquisition Time** -- Sets the time required to acquire an input signal.
   Calculated as: tACQ = 10 x ((Rsource + R) x C), where R = 300 ohm,
   C = 15 pF, and Rsource is any extra source impedance. See the AD7280A
   datasheet page 21 for details.
#. **Self-Test AD7280A** -- Initiates the self-test conversion to verify ADC
   and reference buffer operation. The self-test result varies between
   Code 970 and Code 990.
#. **Cell Balance Outputs** -- Sets the cell balance output of the AD7280A
   to drive external transistor gates, providing 0 V or 5 V output with
   respect to the negative terminal of the battery cell being balanced.
#. **Cell Balance Timers** -- Sets the on-time of each cell balance output.
   Timer may be set from 0 minutes to 36.9 minutes with 71.5-second
   resolution.
#. **Thermistor Term Resistor** -- Sets if the thermistor termination pin
   AUXterm will be used. Due to settling time requirements, this option
   should only be used when the acquisition time is set to 1.6 us.

Advanced Tab
^^^^^^^^^^^^

.. figure:: cn0235_advanced.png
   :align: center

   Advanced register read/write tab

The advanced tab allows the user to read/write to the :adi:`AD7280A`
registers:

#. **Dev0 and Dev1 Register Address** -- Lists register addresses and
   current content.
#. **Read Register** -- Updates the register address array of both devices.
#. **Write Register** -- Writes a new value to a specified register.

.. warning::

   Read and understand the AD7280A and AD8280 datasheets before writing new
   values to registers.

SDP Firmware Release Info Tab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0235_firmware_info.png
   :align: center

   SDP firmware release information

Provides the SDP board firmware version currently in use.

Warning Indicators
~~~~~~~~~~~~~~~~~~

- **AD7280 Alert** -- Primary monitor alert indicator. Lights up when voltage
  or temperature readings exceed user-defined thresholds from the AD7280A
  configuration.
- **Under Voltage** -- Secondary monitor alert indicator. Lights up when
  voltage or temperature readings fall below the user-defined floor threshold.
- **Over Voltage** -- Secondary monitor alert indicator. Lights up when voltage
  or temperature readings exceed the user-defined ceiling threshold.

Documents
---------

- :adi:`CN0235 Circuit Note <CN0235>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0235-SDPZ Design & Integration Files
   <https://www.analog.com/cn0235-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD7280A Product Page <AD7280A>`
- :adi:`AD8280 Product Page <AD8280>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
