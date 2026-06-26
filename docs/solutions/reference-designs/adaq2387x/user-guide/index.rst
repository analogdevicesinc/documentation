.. _eval-adaq23875-fmcz user-guide:

User guide
===============================================================================

The ADAQ2387x family of evaluation boards share a common hardware platform and
software flow. This page covers the hardware and software aspects that apply to
all boards. For device-specific details, refer to the individual user guides:

- :ref:`eval-adaq23875` — EVAL-ADAQ23875FMCZ (16-bit, 15 MSPS)
- :ref:`eval-adaq23876-8` — EVAL-ADAQ23876FMCZ / EVAL-ADAQ23878FMCZ
  (16-/18-bit, 15 MSPS)

.. toctree::
   :hidden:
   :glob:

   *

Supported Devices
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Evaluation Board
     - Resolution
     - Device
   * - :adi:`EVAL-ADAQ23875FMCZ <EVAL-ADAQ23875>`
     - 16-bit
     - :adi:`ADAQ23875` — 15 MSPS, High Speed, Precision µModule DAQ
   * - :adi:`EVAL-ADAQ23876FMCZ <EVAL-ADAQ23876>`
     - 16-bit
     - :adi:`ADAQ23876` — 15 MSPS, High Speed, Precision µModule DAQ
   * - :adi:`EVAL-ADAQ23878FMCZ <EVAL-ADAQ23878>`
     - 18-bit
     - :adi:`ADAQ23878` — 15 MSPS, High Speed, Precision µModule DAQ

Hardware Overview
-------------------------------------------------------------------------------

All boards connect to the ZedBoard via the 160-pin FMC (FPGA Mezzanine Card)
connector (P5) and share the same on-board power supply topology, voltage
reference options, and FMC interface.

Power Supplies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On-board regulators derive all required supply rails from the 12 V input
delivered through the ZedBoard FMC connector.

.. list-table:: On-Board Power Supplies (all variants)
   :header-rows: 1
   :widths: 15 15 30 40

   * - Rail
     - Voltage
     - Regulator
     - Description
   * - +VS
     - 7 V
     - :adi:`LTM8049` + :adi:`ADP7118`
     - Positive analog supply
   * - VDD
     - 5 V
     - :adi:`LTM8049` + :adi:`ADP7118`
     - Digital supply
   * - VIO
     - 2.5 V
     - :adi:`LT3023`
     - Digital I/O supply
   * - −VS
     - −2.0 V
     - :adi:`LTM8049` + :adi:`ADP7183`
     - Negative analog supply

Decoupling capacitors are placed close to each device. A single ground plane
minimises high-frequency noise interference.

Voltage Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two reference options are populated on all boards:

- **U5** — :adi:`LTC6655` 4.096 V reference (default)
- **U3** — :adi:`ADR4520` 2.048 V reference

In the default configuration, the REFBUF pin provides 4.096 V and the VCMO
pin is buffered at 2.048 V (midscale).

Analog Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SMA connectors (VIN+ and VIN−) provide the differential analog inputs from a
low-noise signal source (Audio Precision SYS-2700 or SYS-x555 series).
Optional :adi:`ADA4899-1` amplifiers (A2, A3) can be placed in the signal
path in unity-gain configuration.

.. note::

   For input frequencies below 100 kHz, use a low-noise audio precision signal
   source (SYS-2700 series) with outputs set to balanced floating.

The number of available input routing configurations differs per board — see
the individual user guides for the link option tables.

FMC Connector (P5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 160-pin FMC connector (P5) carries SPI communication signals, clock,
control lines, and power rails between the evaluation board and the ZedBoard.

- User-defined differential pairs use **P/N** suffixes.
- Clock signals use the **CC** suffix and connect to global FPGA clock lines.

Both conventions follow the VITA 57 specification.

Board Layout Guidelines
-------------------------------------------------------------------------------

PCB Layout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Use a multilayer board with an internal, clean ground plane in the first
  layer beneath the µModule.
- Route input and output signals symmetrically.
- Solder all ground pins of the µModule directly to the ground plane using
  multiple vias.
- **Remove ground and power planes** under the analog input/output and digital
  input/output pins (including F1 and F2) to avoid parasitic capacitance, which
  degrades distortion and linearity performance.

Signal Separation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The µModule pinout places analog signals on the left side and digital signals
on the right side.

- Keep sensitive analog and digital sections physically separated on the PCB.
- Keep power supply circuitry away from the analog signal path.
- Fast switching signals (CNV±, CLK±) and digital outputs (DA±, DB±) must not
  run near or cross analog signal paths.

Bypass Capacitors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use high-quality ceramic bypass capacitors of at least 2.2 µF (0402, X5R) at
the output of each LDO regulator generating a µModule supply rail (VDD, VIO,
VS+, VS−) to GND. All other required bypass capacitors are already integrated
within the µModule package. External decoupling on REFIN, VDD, and VIO pins
can be removed without significant impact on performance.

Mechanical Stress
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended soldering method is IR reflow or convection soldering with a
controlled temperature profile. Hand soldering with a heat gun or soldering
iron is **not** recommended — mechanical stress from mounting can cause subtle
SNR degradation and shifts in the internal voltage reference.

Design Files
-------------------------------------------------------------------------------

Complete design support packages (schematics, PCB layout, Bill of Materials)
are available on the respective product pages:

- :adi:`EVAL-ADAQ23875FMCZ <EVAL-ADAQ23875>`
- :adi:`EVAL-ADAQ23876FMCZ <EVAL-ADAQ23876>`
- :adi:`EVAL-ADAQ23878FMCZ <EVAL-ADAQ23878>`
