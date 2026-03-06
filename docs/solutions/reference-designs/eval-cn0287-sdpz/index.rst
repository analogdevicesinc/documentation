.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0287

.. _eval-cn0287-sdpz:

EVAL-CN0287-SDPZ
=================

Isolated 4-Channel Temperature Measurement System.

.. figure:: cn0287_00_1024_81_.png

   EVAL-CN0287-SDPZ Evaluation Board

Overview
--------

:adi:`CN0287 <CN0287>` is a completely isolated 4-channel temperature
measurement circuit optimized for performance, input flexibility, robustness,
and low cost. It supports all types of thermocouples with cold junction
compensation and any type of RTD (resistance temperature detector) with
resistances up to 4 kOhm for 2-, 3-, or 4-wire connection configurations.

The RTD excitation current is programmable for optimum noise and linearity
performance. RTD measurements achieve 0.1 degrees C accuracy (typical), and
Type-K thermocouple measurements achieve 0.05 degrees C typical accuracy because
of the 16-bit :adi:`ADT7310` digital temperature sensor used for cold-junction
compensation. The circuit uses a four-channel :adi:`AD7193` 24-bit sigma-delta
ADC with on-chip PGA for high accuracy and low noise.

Input transient and overvoltage protection are provided by low leakage transient
voltage suppressors (TVS) and Schottky diodes. The SPI-compatible digital inputs
and outputs are isolated (2500 V rms), and the circuit is operated on a fully
isolated power supply.

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` controller board (**SDP-B Board**)
- :adi:`EVAL-CN0287-SDPZ <CN0287>` evaluation board (**CN-0287 Board**)
- :adi:`EVAL-CFTL-6V-PWRZ` **+6 V power supply** or equivalent
- `CN0287 Evaluation Software
  <https://swdownloads.analog.com/cse/cftl/CN0287/1.0.2/CN0287_Evaluation_Software.zip>`__
- PC with the following minimum requirements:

  - Windows XP Service Pack 2 (32-bit) or later
  - USB type A port
  - Processor rated at 1 GHz or faster
  - 512 MB RAM and 500 MB available hard disk space

- USB type A to USB type mini-B cable
- One type of temperature sensor or precision DC signal generator:

  - RTD (Resistance Temperature Detector): PT100, PT1000
  - TC (Thermocouple): Type J, Type K, Type T, Type S
  - Signal Generator: FLUKE 5700A Calibrator or equivalent

General Setup
-------------

- The :adi:`EVAL-CN0287-SDPZ <CN0287>` (**CN-0287 Board**) connects to the
  :adi:`EVAL-SDP-CB1Z` (**SDP-B Board**) via the 120-pin connector.
- The :adi:`EVAL-CFTL-6V-PWRZ` (**+6 V DC Power Supply**) powers the
  EVAL-CN0287-SDPZ via the DC barrel jack.
- The :adi:`EVAL-SDP-CB1Z` (**SDP-B Board**) connects to the PC via the USB
  cable.

.. figure:: hardware_connection_with_label.png

   Hardware Connection

Installing the Software
------------------------

#. Extract the file **CN0287 SDP Evaluation Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the `CN0287 Evaluation Software
      <https://swdownloads.analog.com/cse/cftl/CN0287/1.0.2/CN0287_Evaluation_Software.zip>`__
      to the default directory path **C:\\Program Files\\Analog Devices\\CN0287\\**
      and all National Instruments products to
      **C:\\Program Files\\National Instruments\\**.

   .. figure:: software_installation_1.png

      CN0287 Software Installation - Setup Wizard

#. Click **Next** to view the installation review page.

   .. figure:: software_installation_2.png

      CN0287 Software Installation - Review Page

#. Click **Next** to start the installation.

   .. figure:: software_installation_3.png

      CN0287 Software Installation - Progress

#. Upon completion of the installation of the **CN0287 SDP Eval Software**, the
   installer for the **ADI SDP Drivers** will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: software_installation_4.png

      ADI SDP Drivers Installation

#. Press **Next** to set the installation location for the **SDP Drivers**.

   .. note::

      It is recommended that you install the drivers to the default directory
      path **C:\\Program Files\\Analog Devices\\SDP\\Drivers**.

   .. figure:: software_installation_5.png

      SDP Drivers Installation Location

#. Press **Next** to install the SDP Drivers and complete the installation of
   all software. Click **Finish** when done.

   .. figure:: software_installation_6.png

      SDP Drivers Installation Complete

Connecting the Hardware
------------------------

.. figure:: cn0287_test_setup.png

   CN0287 Test Setup

.. figure:: jumpersetting.png

   Connector Configuration and Jumper Placements

#. Connect the :adi:`EVAL-CN0287-SDPZ <CN0287>` (CN0287 Board) to
   :adi:`EVAL-SDP-CB1Z` (SDP Board) through the 120-pin SMD connector.
#. Do the jumper setting correctly based on the type of temperature sensor for
   evaluation.
#. Plug the mini-USB side of the cable into the mini-USB connector J1 on the
   SDP Board and leave the other side of the cable (USB Type A) disconnected.
#. Connect the sensor correctly by the way shown in the Connector Configuration
   and Jumper Placements diagram.
#. With DC power supply off, plug the EVAL-CFTL-6V-PWRZ (6 V DC Power Supply)
   into **J2** on the CN0287 Board. **CN5** is also a screw terminal for
   connecting to the 6 V power supply by ordinary wire.
#. Connect the USB-Type-A side of the USB cable to the PC.

Using the Evaluation Software
------------------------------

Software Front Panel
~~~~~~~~~~~~~~~~~~~~~

.. figure:: sw_frontpanel_4.png

   CN0287 Evaluation Software Front Panel

The software front panel contains the following controls and indicators:

#. **Connect to SDP-B Board Button** -- When this button is pressed, the SDP-B
   Board makes a USB connection to the CN0287 Board. A connection to the SDP-B
   Board must be made to use the software.
#. **Run Button** -- When this button is pressed, the SDP-B Board will start
   continuous acquisition of temperature data based on the current channel
   configuration.
#. **Step Button** -- When this button is pressed, the SDP-B Board will stop
   data collection.
#. **Clear Button** -- When this button is pressed, the CN0287 Evaluation
   software will clear the data already collected on the **Temperature Tab** and
   clear all the graphs on the **Temperature Graph Tab**.
#. **Save Data Button** -- When this button is pressed, the CN0287 Evaluation
   software will save the history data of the graph on the **Temperature Graph
   Tab**.
#. **Control Tabs**:

   - *Configuration Tab*: Clicking this tab brings all the configuration items
     to the front.
   - *Temperature Tab*: Clicking this tab brings the Temperature Data to the
     front.
   - *Temperature Graph Tab*: Clicking this tab brings the Temperature Graphs to
     the front, showing the plot of temperature vs. time.
   - *SW/Version Tab*: Clicking this tab shows the firmware version of the SDP
     board the software is currently connected with and some additional
     functions.

   .. figure:: software_swversion_tab.png

      SW/Version Info Tab

#. **Configuration Block for All Channels** -- All the configuration items,
   explained in detail in the following sections.
#. **System Status String Indicator** -- This indicator displays a message to
   the user detailing the current state of the software.
#. **System Status LED Indicator** -- This indicator displays the current state
   of the software in the form of an LED. There are three status LED colors:

   - |inactive_led| Inactive
   - |busy_led| Busy
   - |error_led| Error

   .. |inactive_led| image:: cn0272-software-inactive.png
   .. |busy_led| image:: cn0272-software-busy.png
   .. |error_led| image:: cn0272-software-error.png

Configuration Tab
~~~~~~~~~~~~~~~~~~

.. figure:: channel_configuration_2.png

   Channel Configuration

The Configuration Tab provides the following controls for each channel:

#. **Enable Button** -- Enables or disables the selected channel.
#. **Sensor Type Dropdown Menu** -- Select the type of the temperature sensor
   connected to the current channel.
#. **Sensor Wiring Dropdown Menu** -- Select the wiring method used to connect
   the temperature sensor to the daughter board for the current channel.
#. **Advanced Settling Button** -- When this button is pressed, a window named
   **"CH[x] Advanced Settling"** pops up with more detailed settings for
   channel [x] (where [x] is the channel number 1, 2, 3, or 4).

   .. figure:: advanced_settling_with_notes.png

      CH[x] Advanced Setting Pop-up Window

   .. note::

      Only make changes on the **Advanced Setting** pop-up window when you
      clearly understand the meaning and effect of the configuration. It is
      recommended to read the :adi:`AD7193` datasheet and
      :adi:`CN0287 Circuit Note <CN0287>` for more details.

#. **Schematic Diagram for Current Channel** -- This schematic diagram shows the
   type of the sensor, the way of connecting the sensor to the connector, and
   the on-board jumper setting based on the current configuration.
#. **Alarm High** and **Alarm Low** text boxes -- Set upper and lower limit
   temperature thresholds by changing the value of these text boxes. The
   **"Alarm Function"** LED Indicator on the **Temperature Tab** will turn on
   when the current temperature goes out of range.
#. **Calibrate Button** -- When this button is pressed, a window named
   **"CH[x] Calibration"** pops up. Follow the tips on the pop-up window to
   calibrate the current channel correctly.

   .. figure:: calibration_pop_up_windows.png

      CH[x] Calibration Pop-up Window

Temperature Tab
~~~~~~~~~~~~~~~~

.. figure:: channeltemperature_with_label.png

   Temperature Tab Display

The Temperature Tab displays the following information for each channel:

#. **Temperature (degC)** -- The measurement result shown in this text box is
   temperature in degrees Centigrade.
#. **Voltage (mV)** -- The measurement result shown in this text box is the
   voltage on the sensor converted based on the RAW Data and current
   configuration.
#. **RAW Data (Hex)** -- The digital result in hex directly read from the
   :adi:`AD7193`.
#. **Sensor Connection** -- This LED indicator shows the connection status
   between the sensor and daughter board.

   a. Connection Summary for all the necessary wires used for connection:

      - "Connection Good!": All the necessary wires for the current sensor
        under the current wiring method are connected well.
      - "Wire Broken!": At least one of the necessary wires for the current
        sensor under the current wiring method is broken.
      - "Channel Disabled!": Current channel is disabled for measurement and
        wire connection checking.

   b. Connection Status for each necessary wire for the current sensor and
      wiring method:

      - "Good!": This wire is connected well to the daughter board.
      - "Broken": This wire is broken.
      - "Unused!": This wire does not need to be connected under the current
        sensor type and wiring method.
      - "Unknown": The software cannot judge the connection status.

#. **Alarm Function** LED Indicator:

   - In Range!: the current temperature is in the range defined by **High
     Alarm** and **Low Alarm** on the **Configuration Tab**.
   - High Alarm!!: the current temperature is higher than the **High Alarm**
     value on the **Configuration Tab**.
   - Low Alarm!!: the current temperature is lower than the **Low Alarm** value
     on the **Configuration Tab**.

Temperature Graph Tab
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: sw_frontpanel_temepraturegraphtab_withlabel.png

   Temperature Graph Tab Display

The Temperature Graph Tab displays the following for each channel:

#. **CH [x]** -- Channel Number of the graph below.
#. **Text indicator** -- Shows the digital value of the current temperature
   measurement result.
#. **Graph** -- Shows the current temperature vs. time.
#. **Upper threshold line** -- The upper-limit temperature threshold configured
   in the **High Alarm** text box on the **Configuration Tab**.
#. **Lower threshold line** -- The lower-limit temperature threshold configured
   in the **Low Alarm** text box on the **Configuration Tab**.

Establishing a USB Connection Link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Follow the instructions to properly install the software and connect the
   hardware as described in the previous sections.
#. Open the file named **CN0287.exe** in the installation directory.

   .. note::

      If the software was installed to the default location, it will be found at
      **C:\\Program Files\\Analog Devices\\CN0287\\CN0287.exe**.

#. Select the connector to use from the **SDP Connector Dropdown Menu**.
#. Click the **Connect Button**. A window with a progress bar will load.

   .. figure:: cn0272-software-wait.png

      Connection Progress Bar

#. Upon success, the **System Status String Indicator** will display
   *SDP-B Ready to Acquire Data*.

Make Advanced Settling
~~~~~~~~~~~~~~~~~~~~~~~

#. **Establish a USB Connection Link**.
#. Set the *Sensor Type* and *Sensor Wiring* correctly based on the current
   application.
#. Click *Advanced Settling Button* for the selected channel.
#. Make proper settings on the pop-up window.
#. Click "OK" to activate the current setting.

   .. note::

      If you click "Cancel", the Advanced Setting process just made will be
      ignored and no effect acts on the measurement result.

General Flow to Start or Stop Acquisition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **Establish a USB Connection Link**.
#. Select the *Sensor Type* and *Sensor Wiring*.
#. Check the *Schematic Diagram* to guarantee the wiring and jumper settings
   are correct.
#. Make the *Advanced Setting* and *Calibrate* if necessary.
#. Switch to the **Temperature Tab** and click *Run Button* to start
   acquisition.
#. See the measurement result on **Temperature Tab**.
#. Click the *Stop Button* to stop the acquisition.

Establishing an ADC Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **Establish a USB Connection Link**.
#. Set the *Sensor Type* and *Sensor Wiring* correctly based on the current
   application.
#. **Make Advanced Setting** if necessary.
#. Click *Calibrate Button* for the selected channel.
#. Do the following actions on the pop-up window:

   a. Select *ADC Calibration* on the pop-up window.
   b. Click *Zeroscale Calibrate* and wait for 1 second.
   c. Click *Fullscale Calibrate* and wait for 1 second.
   d. Click *OK* to activate the current calibration parameters.

   .. note::

      If you click *Cancel*, the calibration process just performed will be
      ignored and no effect acts on the measurement result.

Establishing a System Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **Establish a USB Connection Link**.
#. Set the *Sensor Type* and *Sensor Wiring* correctly based on the current
   application.
#. **Make Advanced Setting** if necessary.
#. Click *Calibrate Button* for the selected channel.
#. Do the following actions on the pop-up window:

   a. Select *System Calibration* on the pop-up window.
   b. Add Zeroscale calibration signal on the hardware and enter the same value
      into the *Zeroscale Value text box*.
   c. Click *Zeroscale Calibrate* and wait for 1 second.
   d. Add Fullscale calibration signal on the hardware and enter the same value
      into the *Fullscale Value text box*.
   e. Click *Fullscale Calibrate* and wait for 1 second.
   f. Click *OK* to activate the current calibration parameters.

   .. note::

      If you click *Cancel*, the calibration process just performed will be
      ignored and no effect acts on the measurement result.

Saving Configuration to Customer Default
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **Establish a USB Connection Link**.
#. **Make Advanced Setting** or **Calibration** based on the current
   application.
#. Switch to **SW/Version Info Tab**.
#. Click *Save into EEPROM* to store the current configuration changes and
   calibration parameters into the on-board EEPROM.

   .. note::

      The configurations and calibration parameters will become the customer
      default value and will be uploaded by the software automatically from
      EEPROM when a new connection with the daughter board is established.

Recovering to Factory Default Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **Establish a USB Connection Link**.
#. Switch to the **SW/Version Info Tab**.
#. Click **Recover to Default Button** to recover the factory default
   configuration.

   .. note::

      This function is used to recover the board from unexpected conditions
      caused by mis-operations.

Documents
---------

- :adi:`CN0287 Circuit Note <CN0287>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0287-SDPZ Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0287-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS Project

Additional Information
----------------------

- :adi:`AD7193 Product Page <AD7193>`
- :adi:`ADT7310 Product Page <ADT7310>`
- :adi:`ADM3483 Product Page <ADM3483>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
