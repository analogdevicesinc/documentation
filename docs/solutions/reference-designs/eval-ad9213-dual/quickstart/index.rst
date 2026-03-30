.. _eval-ad9213-dual quickstart:

Quick start
===============================================================================

The quick start guide provides step-by-step instructions on how to perform
an initial system bring-up for the :adi:`EVAL-AD9213-DUAL-EBZ` evaluation board
on the supported FPGA development board. This guide covers Synchronized 10G
Mode and Interleaved 20G Mode for data capture and visualization in
:ref:`iio-oscilloscope` and
:adi:`VisualAnalog <en/resources/interactive-design-tools/visualanalog.html>`.

.. toctree::

   On Intel Stratix 10 SX SoC <stratix10>

.. _eval-ad9213-dual carriers:

Supported carriers
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - AD9213-DUAL-EBZ
   * - Intel Stratix 10 SX SoC Development Kit (1SX280HU2F50E1VGAS)
     - FMC+

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - Intel Stratix 10 SX SoC
     - Yes
     - Yes
     - ---

Hardware setup
-------------------------------------------------------------------------------

The AD9213-DUAL-EBZ connects to the Intel Stratix 10 SX SoC Development
Kit via the two FMC+ connectors. The following connections and equipment
are required:

- **USB**: Connect the Mini-USB port (JTAG) and the Micro-USB port (serial,
  115200 baud 8N1) to the host PC.
- **Power**: Two separate power adapters are needed - one for the Intel
  Stratix 10 SX SoC board and a 12 V adapter for the AD9213-DUAL-EBZ.
- **Clock reference**: A 500 MHz differential clock signal is required.
  Use a differential signal generator such as the
  :adi:`AD-SYNCHRONA14-EBZ` directly, or a
  single-ended signal generator combined with a balun to produce the
  differential output.
- **Test signal** (for dual-channel capture): Connect a signal generator
  through a band-pass filter into an RF power splitter, then route the two
  outputs via phase-matched coaxial cables to the AD9213-DUAL-EBZ analog
  inputs.

.. figure:: ../images/ad9213_dualbrd_plus_stratix10_image_two_power_adapters.jpeg
   :alt: Image of Intel Stratix 10 SX SoC board with AD9213-DUAL-EBZ
         connected via FMC+
   :align: center

   AD9213-DUAL-EBZ and Intel Stratix 10 SX Board - Setup

.. figure:: ../images/ad9213_dualbrd_plus_stratix10_diagram_two_power_adapters.jpeg
   :alt: Diagram of Intel Stratix 10 SX SoC board with AD9213-DUAL-EBZ
         connected via FMC+
   :align: center

   AD9213-DUAL-EBZ and Intel Stratix 10 SX Board - Typical Setup