.. imported from: https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux/project-list

.. _ad7124-asdz:

EVAL-AD7124-ASDZ User Guide
============================

24-Bit, Low Power, Low Noise Sigma-Delta ADC Evaluation Board

Introduction
------------

The :adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124-4>` and
:adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124-8>` are fully-featured evaluation boards
for the :adi:`AD7124-4` and :adi:`AD7124-8` 24-bit, low power, low noise
sigma-delta analog-to-digital converters (ADC). The boards include an on-board
:adi:`ADR4525` 2.5 V precision reference, excitation current source connections,
configurable input connectors for RTD, thermocouple, bridge, and thermistor
measurements, and multiple power supply options.

The evaluation boards connect to a PC via the EVAL-SDP-CB1Z (SDP-B) or
EVAL-SDP-CK1Z system demonstration platform. The accompanying Evaluation+
software provides full register control, waveform analysis, histogram
generation, and preconfigured demo modes for common sensor types.

.. figure:: eval-ad7124-asdz-setup.jpg
   :align: center
   :width: 600

   EVAL-AD7124-ASDZ connected to SDP-B motherboard

Supported Devices
-----------------

- :adi:`AD7124-4` -- 4 differential / 7 single-ended inputs (24-lead TSSOP /
  32-lead LFCSP)
- :adi:`AD7124-8` -- 8 differential / 15 single-ended inputs (32-lead LFCSP)

Functional Block Diagram
------------------------

.. figure:: ad7124_functional_block_diagram.png
   :align: center

   AD7124 functional block diagram

About the AD7124
----------------

The :adi:`AD7124-4` / :adi:`AD7124-8` is a low power, low noise, completely
integrated analog front end for high precision measurement applications. The
device contains a low noise, 24-bit sigma-delta ADC, with an on-chip
programmable gain amplifier (PGA) that allows small amplitude signals to be
interfaced directly to the ADC.

Key features include:

- Three integrated power modes for optimizing current consumption, output data
  rates, and RMS noise
- Multiple filter options including sinc4, sinc3, fast settling, and
  post-filters with simultaneous 50 Hz and 60 Hz rejection
- Precision, low noise, low drift internal 2.5 V bandgap reference
- Programmable low drift excitation current sources and burnout detection
  currents
- Bias voltage generator (AVDD/2) for common-mode setting
- Integrated channel sequencer supporting up to 16 channels with per-channel
  configuration
- Extensive diagnostic functionality (CRC, signal chain checks, serial
  interface checks) for IEC 61508 compliance with SFF > 90%
- Single 2.7 V to 3.6 V analog supply or dual 1.8 V supply; digital supply
  1.65 V to 3.6 V

Hardware Requirements
---------------------

- EVAL-AD7124-xASDZ evaluation board (x = 4 or 8)
- EVAL-SDP-CB1Z (SDP-B) or EVAL-SDP-CK1Z system demonstration platform
- USB cable (Mini-B to A)
- Windows PC with USB 2.0 port

Hardware Setup
--------------

1. Install the evaluation software and SDP-B drivers **before** connecting the
   hardware to the PC via USB.
2. Mechanically couple the evaluation board to the SDP-B board using the
   provided plastic screw-washer set (Connector A or B).
3. Connect the SDP-B board to the PC via USB cable.

On-Board Connectors
~~~~~~~~~~~~~~~~~~~~

**Connector J1** (RTD / Thermocouple -- 7 pins)

.. list-table::
   :header-rows: 1

   * - Pin
     - Function
   * - 1
     - AIN0, Excitation Current IOUT0, Noise test
   * - 2
     - AIN1, Excitation Current IOUT1, Noise test
   * - 3
     - AIN2 (RTD+)
   * - 4
     - AIN3 (RTD-)
   * - 5
     - AIN4 (TC+)
   * - 6
     - AIN5 (TC-)
   * - 7
     - REFIN1+ / REFIN1-

**Connector J2** (Bridge -- 8 pins)

.. list-table::
   :header-rows: 1

   * - Pin
     - Function
   * - 1
     - GND / SHIELD
   * - 2
     - Power Switch, Excitation-
   * - 3
     - REFIN- / SENSE-
   * - 4
     - AIN6 (AINN)
   * - 5
     - AIN5 (AINP)
   * - 6
     - REFIN+ / SENSE+
   * - 7
     - AVDD, Excitation+
   * - 8
     - GND / SHIELD

**Connector J4** (8 pins) -- Analog inputs AIN8 through AIN15, one per pin.

**Connector A2** -- Dedicated thermocouple input connection.

**Connector J3** -- SDP-120 pin connector for SDP-B board interface.

Power Supply Options
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Supply
     - Default
     - Configuration
   * - AVDD
     - 3.3 V (ADP1720)
     - LK15=A, LK18=A (3.3 V); LK18=B (1.8 V split supply); LK15=B
       (external via J7)
   * - AVSS
     - AGND
     - LK17=B (AGND); LK17=A (−1.8 V split supply); LK16=B (external)
   * - IOVDD
     - 3.3 V (ADP150ACBZ)
     - LK19=B (on-board LDO); LK19=A (external via J9)

Key Hardware Link Options
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Link
     - Default
     - Function
   * - LK1
     - Inserted
     - Shorts AIN0 to AIN1 for noise testing
   * - LK3
     - Position A
     - Selects external REFIN+ source (J2 or J1)
   * - LK6
     - Position A
     - REFIN+ source: A = 2.5 V LDO, B = REFOUT, removed = J1/J2
   * - LK7--LK10
     - Inserted
     - Used for 4-wire bridge demos
   * - LK15
     - Position A
     - AVDD source: A = internal LDOs, B = external J7
   * - LK17
     - Position B
     - AVSS connection: A = −1.8 V, B = AGND
   * - LK18
     - Position A
     - AVDD regulator: A = 3.3 V, B = 1.8 V
   * - LK19
     - Position B
     - IOVDD source: A = external, B = LDO

Reference Options
~~~~~~~~~~~~~~~~~

The evaluation board includes an on-board :adi:`ADR4525` (2.5 V) external
reference. The :adi:`AD7124-4` / :adi:`AD7124-8` also has an internal 2.5 V
reference that can be enabled via the ADC_Control register.

Reference selection is configured through the AD7124 Configuration registers
(Setup 0--7) in the evaluation software.

Evaluation Software
-------------------

The Evaluation+ software provides complete control and analysis of the
AD7124 evaluation board. The software must be installed before connecting the
hardware.

Software Features
~~~~~~~~~~~~~~~~~

- **Configuration Tab** -- Block diagram view of the AD7124, ADC reset, demo
  mode selection, and reference configuration
- **Waveform Tab** -- Graphs conversion results with peak-to-peak noise, RMS
  noise, and resolution calculations
- **Histogram Tab** -- Generates histograms of sampled data with noise analysis
- **Modelling Performance Tab** -- Ideal AD7124 model for filter frequency
  response, step response, and settling time analysis
- **Register Map Tab** -- Direct register read/write access with bit-level
  editing, search, and configuration save/load (including C file export)

Demo Modes
~~~~~~~~~~

The software includes eight preconfigured demo modes:

#. Noise Test
#. 2-Wire RTD
#. 3-Wire RTD
#. 4-Wire RTD
#. Thermocouple
#. Thermistor
#. 4-Wire Bridge
#. 6-Wire Bridge

Quick Start
~~~~~~~~~~~

#. Download and install the `AD7124 Evaluation+ Software
   <https://www.analog.com/media/en/evaluation-boards-kits/evaluation-software/ad7124-eval-plus-installer.zip>`__.
#. Install the SDP-B system demonstration platform drivers.
#. Restart the PC after installation.
#. Connect the EVAL-AD7124-xASDZ to the SDP-B board and connect via USB.
#. Launch the software from **Programs > Analog Devices**.
#. Click **Refresh** if a connectivity error appears.
#. Run the **Noise Test Demo** to verify the setup.

Software Support
----------------

No-OS Projects
~~~~~~~~~~~~~~

The AD7124 is supported by the following no-OS projects and drivers:

- :git-no-OS:`projects/ad7124-4sdz`
- :git-no-OS:`projects/ad7124-8pmdz`
- :git-no-OS:`drivers/adc/ad7124`

Firmware applications for the SDP-K1 controller board are available in the
precision-converters-firmware repository:

- `AD7124 Console Application
  <https://github.com/analogdevicesinc/precision-converters-firmware/tree/main/projects/ad7124_console>`__
- `AD7124 IIO Application
  <https://github.com/analogdevicesinc/precision-converters-firmware/tree/main/projects/ad7124_iio>`__
- `AD7124 Temperature Measurement Application
  <https://github.com/analogdevicesinc/precision-converters-firmware/tree/main/projects/ad7124_temperature-measure>`__

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The AD7124 is supported by a mainlined Linux IIO driver:

- :git-linux:`drivers/iio/adc/ad7124.c`
- :git-linux:`Documentation/devicetree/bindings/iio/adc/adi,ad7124.yaml`

More Information
----------------

- :adi:`AD7124-4 Product Page <AD7124-4>`
- :adi:`AD7124-8 Product Page <AD7124-8>`
- :adi:`AD7124 Evaluation Board Schematic (PDF)
  <media/en/evaluation-boards-kits/evaluation-design-schematics/7124_schematic.pdf>`
- :adi:`AD7124 Evaluation Board BOM (PDF)
  <media/en/evaluation-boards-kits/evaluation-design-bom/ad7124_bom.pdf>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`Precision Converters Forum <precision-converters>`.
