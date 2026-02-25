.. _eval-cn0376-sdpz:

EVAL-CN0376-SDPZ
=================

Dual-Channel Isolated Thermocouple/RTD Input for PLC/DCS.

Overview
--------

:adi:`CN0376 Circuit Note <CN0376>` is a dual-channel, channel-to-channel
isolated thermocouple or RTD input suitable for programmable logic controllers
(PLC) and distributed control systems (DCS). Each channel can accept either a
thermocouple or an RTD input. The entire circuit is powered from a standard 24 V
bus supply.

The :adi:`AD7124-4` 24-bit sigma-delta ADC with programmable gain array (PGA)
and voltage reference provides the complete set of features to implement a
flexible input capable of connection to either thermocouple or RTD sensors.
Features include on-chip reference, PGA, excitation currents, bias voltage
generator, and flexible filtering with enhanced 50 Hz and 60 Hz rejection
options. The :adi:`AD7124-4` is in a small 5 mm x 5 mm LFCSP package, making it
ideal in channel-to-channel isolated designs where space is a premium. It also
includes multiple diagnostic functions that are available to the user.

The :adi:`ADuM5010` isolated dc-to-dc converter provides 3.3 V isolated power
via integrated isoPower technology. The :adi:`ADuM1441` isolates the SPI
interface for the :adi:`AD7124-4`. The ADuM1441 micropower isolator consumes
only 4.8 uA per channel when idle, resulting in an energy efficient solution.
The :adi:`ADP2441` 36 V step-down dc-to-dc regulator accepts an industrial
standard 24 V supply with wide tolerance on the input voltage and steps it down
to 5 V for use by the system.

The EVAL-CN0376-SDPZ evaluation board connects to ADI's System Demonstration
Platform (SDP) and also features PMOD-compatible headers for interfacing with
other development platforms.

.. figure:: cn0376_board.png
   :width: 600px
   :align: center

   EVAL-CN0376-SDPZ evaluation board

Required Equipment
------------------

- :adi:`EVAL-CN0376-SDPZ <EVAL-CN0376-SDPZ>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- DC power supply (+12 V to +24 V)
- RTD (PT100 or PT1000)
- Thermocouple
- CN0376 Evaluation Software
- PC with the following minimum requirements:

  - Windows Vista/7 (32-bit)
  - USB Type-A port
  - Processor rated at 1 GHz or faster
  - 1 GB RAM and 500 MB available hard disk space

- USB Type-A to USB Mini-B cable

Hardware Setup
--------------

.. figure:: board_guide.png
   :width: 600px
   :align: center

   EVAL-CN0376-SDPZ board layout and connector locations

- The EVAL-CN0376-SDPZ **(CN-0376 Board)** connects to the
  :adi:`EVAL-SDP-CB1Z` **(SDP-B Board)** via the 120-pin connector.
- The :adi:`EVAL-SDP-CB1Z` **(SDP-B Board)** connects to the PC via the USB
  cable.
- Header **P4** is a PMOD-compatible SPI header for communication to Channel 1.
- Header **P5** is a PMOD-compatible SPI header for communication to Channel 2.
- Header **PWR_SEL** is used for selecting the power source of the system using
  a jumper (Terminal Block P3 or PMOD).
- Terminal block **P3** is the power supply input (input range: +5.5 V to
  +36 V DC).
- Terminal block **P1** is the sensor input (RTD or thermocouple) for Channel 1.
- Terminal block **P2** is the sensor input (RTD or thermocouple) for Channel 2.

Sensor Connection
~~~~~~~~~~~~~~~~~

.. figure:: wiring_guide.png
   :width: 500px
   :align: center

   Sensor wiring guide

**2-Wire RTD**

- Connect RTD to AIN+ and AIN- terminals.
- Short terminals IEXC and AIN+.
- Short terminals RETURN and AIN-.

**3-Wire RTD**

- Connect RTD wires to AIN+, AIN-, and RETURN terminals.
- Short terminals IEXC and AIN+.

**4-Wire RTD**

- Connect RTD to IEXC, AIN+, AIN-, and RETURN terminals.

**Thermocouple**

- Connect thermocouple to AIN+ and AIN- terminals.

Power Options
~~~~~~~~~~~~~

**Jumper Position EXT**

.. figure:: pwr_sel2.png
   :width: 200px

   PWR_SEL jumper in EXT position

- System is powered using terminal block P3 (input range: +5.5 V to +36 V DC).
- When no supply is present on P3, the system draws power from USB when using
  the SDP.

**Jumper Position PMOD**

.. figure:: pwr_sel1.png
   :width: 200px

   PWR_SEL jumper in PMOD position

- System is powered using the PMOD headers (+3.3 V DC).

Installing the Evaluation Software
-----------------------------------

#. Extract the file **CN0376_Evaluation_Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN-0376 Evaluation Software to
      the default directory path
      ``C:\Program Files\Analog Devices\CN0376\`` and all National Instruments
      products to ``C:\Program Files\National Instruments\``.

   .. figure:: install1.png

      CN0376 evaluation software installation wizard

#. Click **Next** to view the installation review page.

   .. figure:: install2.png

      Installation review page

#. Click **Next** to start the installation.

   .. figure:: install4.png

      Installation progress

#. Upon completion of the installation of the **CN-0376 Evaluation Software**,
   the installer for the **ADI SDP Drivers** will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: cn0357-install4.png

      ADI SDP Drivers installation wizard

#. Press **Next** to set the installation location for the **SDP Drivers**.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: cn0357-install5.png

      SDP Drivers installation location

#. Press **Next** to install the **SDP Drivers** and complete the installation
   of all software. Click **Finish** when done.

   .. figure:: cn0357-install6.png

      SDP Drivers installation complete

Using the Evaluation Software
-----------------------------

Software Control and Indicator Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Main Tab
^^^^^^^^

.. figure:: software_main_1.png
   :width: 600px
   :align: center

   CN0376 evaluation software -- Main tab

#. **Run/Stop** -- Start/Stop data acquisition from the evaluation board.
#. **Clear Data** -- Clear the data on the chart and on voltage/current
   indicators.
#. **Save Data** -- Save the data collected to a tab-delimited ASCII
   spreadsheet file.
#. **Reset** -- Reset the evaluation board and software to the default startup
   configuration.
#. **Channel 1 Temperature Display** -- Displays the temperature reading from
   Channel 1 (in degrees Celsius).
#. **Channel 1 RTD Resistance/TC Voltage Display**:

   - Displays the equivalent RTD resistance of Channel 1 when in RTD mode.
   - Displays the thermocouple voltage of Channel 1 when in thermocouple mode.

#. **Channel 2 Temperature Display** -- Displays the temperature reading from
   Channel 2 (in degrees Celsius).
#. **Channel 2 RTD Resistance/TC Voltage Display**:

   - Displays the equivalent RTD resistance of Channel 2 when in RTD mode.
   - Displays the thermocouple voltage of Channel 2 when in thermocouple mode.

#. **Cold Junction Compensation Information** -- Displays the temperature and
   resistance of the CJC thermistor of both Channel 1 and 2 when in
   thermocouple mode.
#. **Display Units**:

    - Temperature -- data on the chart is displayed as degrees Celsius.
    - ADC Code -- data on the chart is displayed as ADC codes.

#. **Chart** -- Data plot for the data acquisition (may be displayed as
   voltage/current value or ADC code).
#. **Status Bar** -- Displays a message to the user detailing the current
   state of the software. There are three status LED colors:

   |inactive| Inactive
   |busy| Busy
   |error| Error

.. |inactive| image:: cn0357-software-inactive.png
.. |busy| image:: cn0357-software-busy.png
.. |error| image:: cn0357-software-error.png

Histogram Tab
^^^^^^^^^^^^^

.. figure:: software_histogram_1.png
   :width: 600px
   :align: center

   CN0376 evaluation software -- Histogram tab

.. note::

   User needs to sample data first using **Run** to get histogram data on this
   page.

#. **Select Channel** -- Channel selection for histogram display.
#. **Get Histogram** -- Analyzes the data from the selected channel and
   displays the histogram data.
#. **Maximum Code** -- Display for the highest code from the sampled data of
   the selected channel.
#. **Minimum Code** -- Display for the lowest code from the sampled data of
   the selected channel.
#. **Code Spread** -- Display for the difference between the highest and
   lowest code from the sampled data of the selected channel.
#. **Peak-to-Peak Resolution** -- Display for computed peak-to-peak resolution
   (bits) of the selected channel.
#. **Histogram Graph** -- Plot for the histogram data.

Configuration Tab
^^^^^^^^^^^^^^^^^

Allows for ADC configuration of either channel.

.. figure:: software_config.png
   :width: 600px
   :align: center

   CN0376 evaluation software -- Configuration tab

**Input Type**

- **PT100** -- Activates the excitation current source and configures the ADC
  to read from PT100 RTD.
- **PT1000** -- Activates the excitation current source and configures the ADC
  to read from PT1000 RTD.
- **Thermocouple** -- Activates the TC bias, CJC, and configures the ADC to
  read from thermocouple.

**RTD Connection**

- **2-Wire** -- Excitation current available at IEXC pin. Short IEXC and AIN+
  pins. Short AIN- and RETURN pins.
- **3-Wire** -- Matched excitation currents available at IEXC and AIN- pins.
- **4-Wire** -- Excitation current available at IEXC pin. Short IEXC and AIN+
  pins.

**Power Mode** -- Select the power mode of the ADC. This affects power
consumption and ADC data rate. Consult the :adi:`AD7124-4` datasheet for more
information.

**Filter Type** -- Select the digital filter used for the ADC conversion.
Consult the :adi:`AD7124-4` datasheet for more information.

**Post Filter** -- Select the data rate when the post filters are used.

**Sampling Rate** -- Slider control to change the ADC data rate. The numerical
display shows the corresponding data rate. This is dependent on the power mode
and filter type.

**Enabled/Disabled** -- Toggle to enable or disable the corresponding channel.

**Configure** -- Press this button to apply the configurations to the
corresponding channel.

Advanced Configuration Tab
^^^^^^^^^^^^^^^^^^^^^^^^^^

Allows control of excitation current, burnout current, PGA gain, and for
enabling ADC error checks.

.. figure:: software_advconfig.png
   :width: 600px
   :align: center

   CN0376 evaluation software -- Advanced Configuration tab

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

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0376-SDPZ Design & Integration Files
   <https://www.analog.com/CN0376-DesignSupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD7124-4 Product Page <AD7124-4>`
- :adi:`ADuM5010 Product Page <ADUM5010>`
- :adi:`ADuM1441 Product Page <ADUM1441>`
- :adi:`ADP2441 Product Page <ADP2441>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
