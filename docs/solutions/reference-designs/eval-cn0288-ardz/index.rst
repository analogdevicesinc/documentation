.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0288

.. _eval-cn0288-ardz:

EVAL-CN0288-ARDZ
================

LVDT Signal Conditioning Circuit with 12-bit ADC.

Overview
--------

:adi:`CN0288` is a linear variable differential transformer (LVDT) signal
conditioning circuit. The system converts the output of the LVDT sensor to a
unipolar DC voltage and drives the inputs of a successive approximation
analog-to-digital converter (ADC).

This circuit uses a single chip solution that drives the excitation signal of
the primary side of the LVDT and converts the secondary side. The complete
system uses a 12-bit ADC resulting in a dynamic range of 82 dB at a standard
LVDT bandwidth of 250 Hz. The signal conditioning circuitry of the system
consumes only 15 mA of current from the +/-15 V supply and 3 mA from the +5 V
supply making this configuration suitable for industrial precision position and
gauging applications such as flight control surface position feedback.

.. figure:: cn0288-simplified_schematic.png
   :align: center

   CN0288 Simplified Schematic

.. figure:: cn0288-hardware.png
   :align: center
   :width: 600

   EVAL-CN0288-SDPZ Evaluation Board

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` Controller Board (SDP-B Board)
- :adi:`EVAL-CN0288-SDPZ` Evaluation Board (CN0288 Board)
- :adi:`EVAL-CFTL-6V-PWRZ` +6 V Power Supply or equivalent
- Linear Variable Differential Transformer (Measurement Specialties, Inc.
  E-100 Economy Series LVDT)
- `CN0288 Evaluation Software
  <https://www.analog.com/CN0288>`__
- PC with USB type A port (Windows XP SP2 or later)
- USB type A to USB type mini-B cable

General Setup
-------------

- The EVAL-CN0288-SDPZ (CN0288 Board) connects to the :adi:`EVAL-SDP-CB1Z`
  (SDP-B Board) via the 120-pin connector.
- The :adi:`EVAL-CFTL-6V-PWRZ` (+6 V DC Power Supply) powers the
  EVAL-CN0288-SDPZ (CN0288 Board) via the DC barrel jack.
- The :adi:`EVAL-SDP-CB1Z` (SDP-B Board) connects to the PC via the USB cable.
- The LVDT connects to the EVAL-CN0288-SDPZ (CN0288 Board) via the 6-pin
  header at J3.

.. figure:: cn0288-test_setup.png
   :align: center

   CN0288 General Test Setup

Using the Evaluation Software
------------------------------

Software Controls
~~~~~~~~~~~~~~~~~

.. figure:: cn0288-software.png
   :align: center
   :width: 600

   CN0288 Evaluation Software Interface

The CN0288 evaluation software provides the following controls and indicators:

- **Connect/Reconnect Button** -- establishes a USB connection between the
  SDP-B Board and the CN0288 Board.
- **Run Button** -- starts data collection, presenting acquisitions in the
  chart.
- **Stop Button** -- stops data collection.
- **Save Data Button** -- saves captured data to a tab-delimited ASCII
  spreadsheet file.
- **Clear Data Button** -- clears all data from the chart history.
- **Channel 1/2 Numerical Indicators** -- display current position from null.
- **Channel Enable Checkboxes** -- select which channels to display.
- **Select Units Radio Buttons** -- choose between Inches and ADC Codes for
  the Y-axis.
- **ADC Conversion Thresholds Panel** -- allows reading and writing the
  :adi:`AD7992` ADC threshold registers.
- **LVDT Full Scale Range Panel** -- configures the maximum stroke range of
  the LVDT (default 0.2 inches).

Establishing a USB Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install the software and connect the hardware as described above.
#. Open **CN0288.exe** from the installation directory.
#. Click the **Connect/Reconnect** button. A progress bar will appear.
#. Upon success, the System Status indicator will display
   "SDP Board Ready to Acquire Data".

Capturing Data
~~~~~~~~~~~~~~

#. Establish a USB connection.
#. Click the **Run** button to begin acquisition.
#. Click the **Stop** button when acquisition is complete.

Saving Data
~~~~~~~~~~~

#. Capture data as described above.
#. Click the **Save Data** button.
#. Select the desired format (Inches or ADC Codes) and channels.
#. Choose a file location and name, then click **OK**.

The software saves the spreadsheet file as ASCII text with tab-separated
columns.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `CN0288 Design & Integration Files <https://www.analog.com/CN0288>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD598 Product Page <AD598>`
- :adi:`AD7992 Product Page <AD7992>`
- :adi:`CN0288 Circuit Note <CN0288>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
