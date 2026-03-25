.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0560

.. _eval-cn0560-ardz:

EVAL-CN0560-FMCZ
=================

High Precision Wide Bandwidth Current Measurement.

.. figure:: evb_photo.jpg
   :align: center

   EVAL-CN0560-FMCZ evaluation board

Overview
--------

:adi:`CN0560` is a complete, wide-range current measurement system suitable
for power characterization, ATE, and power analyzers. The system provides
accuracy, bandwidth, and drift performance at the level of benchtop test
equipment in a compact form factor for continuous monitoring.

The circuit features high-accuracy measurement of three current ranges using
a combination of shunt resistors and on-board amplifiers with the
:adi:`ADAQ23878` precision uModule data acquisition solution rated at 18-bit,
15 MSPS. The three measurement ranges are:

.. list-table::
   :header-rows: 1
   :widths: 20 25 25 30

   * - Current Range
     - Shunt Resistor
     - Max Voltage Drop
     - Input Connector
   * - 10 uA
     - 5 kOhm
     - 50 mV
     - Banana jack pair
   * - 10 mA
     - 5 Ohm
     - 50 mV
     - Banana jack pair
   * - 10 A
     - 5 mOhm
     - 50 mV
     - Banana jack pair

Key components include:

- :adi:`ADAQ23878` uModule DAQ (18-bit, 15 MSPS SAR ADC)
- :adi:`ADA4898-1` low noise operational amplifiers (U9, U10)
- :adi:`LT5400` quad matched precision resistor network (RN1)
- :adi:`AD8421` optional instrumentation amplifier (3 nV/sqrtHz)
- :adi:`ADG5209` high-voltage latch-up proof multiplexer for range selection
- :adi:`LTC6655` precision voltage reference (4.096 V option)
- :adi:`ADR4520` precision voltage reference (2.048 V option)
- :adi:`AD9513` 800 MHz clock distribution IC
- :adi:`LTM8049` dual SEPIC/inverting uModule DC-DC converters

.. figure:: block_diagram.jpg
   :align: center

   EVAL-CN0560-FMCZ simplified block diagram

Required Equipment
------------------

- EVAL-CN0560-FMCZ evaluation board
- :adi:`EVAL-SDP-CH1Z` (SDP-H1) controller board
- Current source (e.g., Keithley 2400)
- Standard USB A to USB mini-B cable
- DC benchtop power supply (e.g., Keithley E3631A)

Required Software
~~~~~~~~~~~~~~~~~

- ACE (Analog Devices Configuration and Evaluation software)
- EVAL-CN0560-FMCZ ACE plug-in
- SDP-H1 driver

Evaluation Setup
----------------

The following figures show the test setup connections for each current range.

.. figure:: 10ua_test_setup.jpg
   :align: center

   10 uA range test setup connection

.. figure:: 10ma_test_setup.jpg
   :align: center

   10 mA range test setup connection

.. figure:: 10a_test_setup.jpg
   :align: center

   10 A range test setup connection

Hardware Overview
-----------------

Link Configuration
~~~~~~~~~~~~~~~~~~~

All jumper positions must be set correctly before applying power. The figure
below shows the default link configuration for the EVAL-CN0560-FMCZ.

.. figure:: link_configuration.jpg
   :align: center

   Default link configuration

Current Range Selection
~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`ADG5209` multiplexer selects the active current range. Range
selection is controlled via shunt jumpers on headers P13, P7, P14, and P8,
or through software control when appropriately configured.

Banana jack connectors are paired for each current range. Users can connect
return paths to ground using jumper provisions (R15, R127, R129).

.. figure:: range_sw.jpg
   :align: center

   Software-controlled range selection configuration

.. figure:: range_10ua.jpg
   :align: center

   10 uA input range configuration

.. figure:: range_10ma.jpg
   :align: center

   10 mA input range configuration

.. figure:: range_10a.jpg
   :align: center

   10 A input range configuration

.. figure:: range_gnd_in.jpg
   :align: center

   Grounded inputs configuration

Amplifier Options
~~~~~~~~~~~~~~~~~

Two :adi:`ADA4898-1` unity-gain amplifiers paired with the :adi:`LT5400`
matched resistor network provide CMRR superior to that achievable with
independent matching. Alternatively, a single :adi:`AD8421` instrumentation
amplifier can be substituted by modifying connections on JP1, JP2, JP7,
and JP8.

Gain Configuration
~~~~~~~~~~~~~~~~~~

The :adi:`ADAQ23878` FDA gain is configured via header connections on P4 and
P6, offering settings of 0.37, 0.73, 1.38, and 2.25.

.. figure:: gain_configuration.jpg
   :align: center

   FDA gain configuration settings

.. figure:: gain_0.37.jpg
   :align: center

   Gain = 0.37 configuration (P4 and P6)

.. figure:: gain_0.73.jpg
   :align: center

   Gain = 0.73 configuration (P4 and P6)

.. figure:: gain_1.38.jpg
   :align: center

   Gain = 1.38 configuration (P4 and P6)

.. figure:: gain_2.25.jpg
   :align: center

   Gain = 2.25 configuration (P4 and P6)

Power Supply Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~

The simplified power tree generates the following rails from the 3.3 V input:

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Output Rail
     - Source
     - Purpose
   * - +7 V, -2.5 V
     - 3.3 V input
     - Intermediate rails
   * - +15.5 V, -15.5 V
     - 3.3 V input
     - Intermediate rails
   * - +6.5 V
     - +7 V rail
     - ADAQ23878 FDA (VS+)
   * - -2 V
     - -2.5 V rail
     - ADAQ23878 FDA (VS-)
   * - +5 V
     - +7 V rail
     - :adi:`LTC6655` reference
   * - +15 V, -15 V
     - +/-15.5 V rails
     - :adi:`ADA4898-1` amplifiers, :adi:`ADG5209`

.. figure:: power_tree.jpg
   :align: center

   EVAL-CN0560-FMCZ power tree

The board is factory-configured to provide 4.096 V on the REFBUF pin and a
buffered 2.048 V (midscale) at the FDA's VCMO pin.

Power supply components include:

- :adi:`LTM8049` dual SEPIC/inverting uModule DC-DC converters (U2, U6)
- :adi:`ADP7118` low noise LDO (U4)
- :adi:`ADP7183` ultralow noise LDO (U7)
- :adi:`LT3023` dual low noise micropower LDO (U8)
- :adi:`LT3032` dual LDO (U16)

SDP-H1 Controller Board
~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-SDP-CH1Z` (SDP-H1) is a high-speed controller board for the
system demonstration platform. It features:

- Xilinx Spartan 6 FPGA
- ADSP-BF527 processor
- USB 2.0 high-speed connectivity
- FMC low pin count (LPC) connector with full differential LVDS and
  single-ended LVCMOS support
- 160-pin connector exposing Blackfin processor peripherals
- Configurable serial, parallel, I2C, SPI, and GPIO interfaces

Dynamic Performance Testing
----------------------------

To evaluate dynamic performance (FFT, INL, DNL, time-domain measurements):

#. Remove the 5 kOhm Rshunt (R29) on the 10 uA input path.
#. Connect signal source (e.g., AP2722) to the CN0560 and SDP-H1.
#. Set the output to 50 mV peak-to-peak.

For frequencies below 100 kHz, a low-noise audio precision signal source
(SYS-2700 series) is recommended with balanced floating outputs. Alternative
precision sources may require additional band-pass filtering depending on
desired input bandwidth.

.. figure:: ap2722_dr_setup.jpg
   :align: center

   Dynamic performance test setup with AP2722

Software Setup
--------------

ACE Software Launch
~~~~~~~~~~~~~~~~~~~

#. Select Start menu > All Programs > Analog Devices > ACE > ACE.exe.
#. The ADAQ23878 icon appears in the Attached Hardware section.
#. If not connected via USB/SDP-H1, connect the board and wait several
   seconds.
#. Double-click the ADAQ23878 board icon to open the Board View Window.
#. Click "Software Defaults" then "Apply Changes".
#. Click "Proceed to Analysis" to open the evaluation interface.

To exit the software, click the file icon on the upper right tab, then
click Exit.

.. figure:: ace_main_window.jpg
   :align: center

   ACE main window showing attached hardware

.. figure:: board_view.jpg
   :align: center

   Board View window

.. figure:: chip_view.jpg
   :align: center

   Chip View window

Analysis Software Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Capture Panel Controls**

- **Throughput**: Default 15 MSPS sampling frequency, adjustable minimum
  20 kSPS.
- **Sample Count**: Up to 1,048,576 samples per channel.
- **Output Mode**: Two-lane mode (2 bits simultaneous) or one-lane mode
  (1 bit), controlled by the TWOLANES signal via P1 configuration.
- **Oversampling**: Configurable ratio increasing effective resolution.
  Oversampling by a factor of four provides one additional bit of resolution,
  or a 6 dB increase in dynamic range.

.. figure:: analysis.jpg
   :align: center

   Analysis window with capture panel controls

**Waveform Tab**

Displays successive sample outputs with zoom and pan tools. Display units are
selectable as hexadecimal, volts, or codes. Dynamic axis scaling is available.

.. figure:: waveform.jpg
   :align: center

   Waveform display tab

**Histogram Tab**

Shows code distribution frequency, useful for DC performance analysis and
noise assessment. Related DC performance metrics are displayed in the
results pane.

.. figure:: histogram.jpg
   :align: center

   Histogram display tab

**FFT Tab**

FFT analysis with oversampling up to 256x. The dynamic range improvement
follows:

.. math::

   \Delta DR = 10 \times \log_{10}(OSR) \; \text{(in dB)}

.. figure:: fft.jpg
   :align: center

   FFT analysis display

.. figure:: oversampling.jpg
   :align: center

   Oversampling configuration and results

**INL and DNL Tab**

Linearity analysis results:

- **INL**: Deviation of each code from the ideal straight line (negative full
  scale 1/2 LSB before first transition, positive full scale 1-1/2 LSB after
  last transition).
- **DNL**: Maximum deviation from ideal 1 LSB code spacing.

To test, apply a sinusoidal signal 0.5 dB above full scale at the VIN+/VIN-
SMA inputs. Configure hits-per-code for desired accuracy (higher numbers
increase test time).

.. figure:: inl.jpg
   :align: center

   INL linearity analysis

.. figure:: dnl.jpg
   :align: center

   DNL linearity analysis

PCB Layout Guidelines
---------------------

Key design considerations:

- Use a multilayer board with a clean internal ground plane in the first layer
  beneath the EVAL-CN0560-FMCZ.
- Route input/output signals symmetrically.
- Solder ground pins directly to the ground plane using multiple vias.
- Remove ground and power planes under analog input/output and digital
  input/output pins (including F1, F2) to eliminate parasitic capacitance.
- Separate analog and digital sections.
- Keep power supply circuitry away from analog signal paths.
- Avoid routing fast switching signals (CNV+/-, CLK+/-) or digital outputs
  (DA+/-, DB+/-) near or crossing analog signal paths.

**Bypass Capacitors**: Use good quality ceramic bypass capacitors of at least
2.2 uF (0402, X5R) at LDO outputs (VDD, VIO, VS+, VS-). Removal of external
decoupling on REFIN, VDD, VIO near the uModule causes no significant
performance impact.

**Mechanical Stress**: IR reflow or convection soldering with a controlled
temperature profile is recommended. Hand soldering with a heat gun or
soldering iron is not recommended due to potential SNR and reference voltage
changes.

Troubleshooting
---------------

**System Setup**

Install ACE software and the SDP-H1 driver before connecting the evaluation
board to the PC.

**Connection Procedure**

#. Ensure all configuration links are in appropriate positions.
#. Connect EVAL-CN0560-FMCZ securely to the 160-way connector on the SDP-H1.
#. Connect the SDP-H1 to the PC via USB cable (no external power supply is
   needed for the CN0560).

**Verification Steps**

#. Allow the found new hardware wizard to run; search drivers if needed.
#. Click "Yes" if prompted for permission changes.
#. Use Device Manager to verify proper connection.
#. Confirm "Analog Devices SDP-H1" appears under ADI Development Tools.

**Disconnection**

Always remove power from the SDP-H1 or click the reset tact switch before
disconnecting the EVAL-CN0560-FMCZ.

Documents
---------

- :adi:`CN0560 Circuit Note <CN0560>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0560-FMCZ Design & Integration Files
   <https://www.analog.com/cn0560-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project files

Additional Information
----------------------

- :adi:`ADAQ23878 Product Page <ADAQ23878>`
- :adi:`ADA4898-1 Product Page <ADA4898-1>`
- :adi:`AD8421 Product Page <AD8421>`
- :adi:`ADG5209 Product Page <ADG5209>`
- :adi:`AD9513 Product Page <AD9513>`
- :adi:`ADR4520 Product Page <ADR4520>`
- :adi:`LTC6655 Product Page <LTC6655>`
- :adi:`LTM8049 Product Page <LTM8049>`
- :adi:`ADP7118 Product Page <ADP7118>`
- :adi:`ADP7183 Product Page <ADP7183>`
- :adi:`LT3023 Product Page <LT3023>`
- :adi:`LT3032 Product Page <LT3032>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
