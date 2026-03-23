.. _eval-ad9213-dual quickstart:

Quick start
===============================================================================

The quick start guide provides step-by-step instructions on how to perform
an initial system bring-up for the AD9213-DUAL-EBZ evaluation board on
the supported FPGA development board. This guide covers Synchronized 10G
Mode and Interleaved 20G Mode for data capture and visualization in
:ref:`iio-oscilloscope` and VisualAnalog.

.. toctree::

   On Intel Stratix 10 SX SoC <stratix10>

.. _eval-ad9213-dual carriers:

Supported carriers
-------------------------------------------------------------------------------

The AD9213-DUAL-EBZ connects to the FPGA carrier via an FMC+ connector.

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
Kit via the FMC+ connector. The setup requires a power supply, a UART
terminal (115200 baud, 8N1), and USB connections for JTAG and serial
communication.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213_dualbrd_plus_stratix10_diagram_two_power_adapters.png
   :alt: Intel Stratix 10 SX SoC board with AD9213-DUAL-EBZ connected via
         FMC+
   :align: center

   AD9213-DUAL-EBZ and Intel Stratix 10 SX Board — Typical Setup
