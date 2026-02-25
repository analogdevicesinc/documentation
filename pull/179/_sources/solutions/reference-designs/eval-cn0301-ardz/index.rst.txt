.. _eval-cn0301-ardz:

EVAL-CN0301-SDPZ
=================

LVDT Signal Conditioning Circuit.

Overview
--------

:adi:`CN0301` is a linear variable differential transformer (LVDT) signal
conditioning circuit. The system converts the output of the LVDT sensor to a
unipolar DC voltage and drives the inputs of a successive approximation
analog-to-digital converter (ADC).

This circuit uses a single chip solution that drives the excitation signal of
the primary side of the LVDT and converts the secondary side. The complete
system uses a 12-bit ADC resulting in a dynamic range of 82 dB at a standard
LVDT bandwidth of 250 Hz. The signal conditioning circuitry consumes only
15 mA from the +/-15 V supply and 3 mA from the +5 V supply, making this
configuration suitable for industrial precision position and gauging
applications such as flight control surface position feedback.

.. figure:: cn0301-simplified_schematic.png
   :align: center

   CN0301 Simplified Schematic

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` Controller Board (**SDP-B Board**)
- :adi:`EVAL-CN0301-SDPZ` Evaluation Board (**CN-0301 Board**)
- :adi:`EVAL-CFTL-6V-PWRZ` +6 V Power Supply or equivalent
- Linear Variable Differential Transformer (Measurement Specialties, Inc.
  E-100 Economy Series LVDT)
- CN-0301 Evaluation Software
- PC running Windows with USB type A port
- USB type A to USB type mini-B cable

General Setup
-------------

- The EVAL-CN0301-SDPZ connects to the EVAL-SDP-CB1Z via the 120-pin
  connector.
- The +6 V DC power supply powers the EVAL-CN0301-SDPZ via the DC barrel
  jack.
- The EVAL-SDP-CB1Z connects to the PC via the USB cable.
- The LVDT connects to the EVAL-CN0301-SDPZ via the 6-pin header at **J1**.

.. figure:: cn0301-test_setup.png
   :align: center

   CN0301 Test Setup Block Diagram

Connecting the Hardware
-----------------------

#. Connect the LVDT to **J1** of the EVAL-CN0301-SDPZ as described in the
   circuit note wiring schematic.

   .. note::

      If a different LVDT is used other than the E-100 LVDT from Measurement
      Specialties, the wiring schematic will be different.

   .. figure:: cn0301-hardware.png
      :width: 600 px
      :align: center

      LVDT Connection to EVAL-CN0301-SDPZ

#. Connect **J8** of the EVAL-CN0301-SDPZ to **CON A** of the EVAL-SDP-CB1Z.
#. Connect the +6 V DC power supply to the barrel jack at **J4** or the screw
   terminal at **J3** on the EVAL-CN0301-SDPZ.
#. Connect the USB cable to **J1** of the EVAL-SDP-CB1Z.

Using the Evaluation Software
------------------------------

Software Controls
~~~~~~~~~~~~~~~~~

- **Connect/Reconnect Button** -- Makes a USB connection between the SDP-B
  Board and the CN-0301 Board. A connection must be established to use the
  software.
- **Run Button** -- Begins data collection and displays acquisitions in the
  chart.
- **Stop Button** -- Stops collecting data from the CN-0301 Board.
- **Save Data Button** -- Saves collected data to a tab-delimited ASCII
  spreadsheet file.
- **Clear Data Button** -- Clears all collected data from the chart history.
- **Control Tabs**:

  - *Acquire Data* -- Brings the data collection chart to the front.
  - *Configure System* -- Brings the system configuration settings to the
    front.

- **Channel 1 / Channel 2 Numerical Indicators** -- Display the current
  position from null on each channel.
- **Channel Enable Checkboxes** -- Determines which channels display in the
  chart.
- **Select Units Radio Buttons** -- Determines the Y-Axis units of the data
  (Inches or ADC Codes).
- **ADC Conversion Out of Range LED** -- Indicates whether a conversion
  result is outside the allowable range.
- **LVDT Full Scale Range Panel** -- Configures the maximum stroke range of
  the LVDT (default: 0.20 inches).

Data Acquisition Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open the CN0301.exe application from the installation directory.
#. Click the **Connect/Reconnect** button to establish a USB connection.
#. Click **Run** to begin data acquisition.
#. Click **Stop** when acquisition is complete.
#. Click **Save Data** to export data to a spreadsheet file.

Information regarding the internal register structure can be found in the
:adi:`AD7992` datasheet.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0301-SDPZ Design & Integration Files <https://www.analog.com/cn0301-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

More Information and Useful Links
----------------------------------

- :adi:`CN0301 Circuit Note Page <CN0301>`
- :adi:`AD7992 Product Page <AD7992>`
- :adi:`EVAL-SDP-CB1Z Product Page <EVAL-SDP-CB1Z>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`ez/reference-designs`.
