.. _ad_fmcadc2_ebz quickstart:

Quick start
===============================================================================

.. warning::

   The :adi:`AD-FMCADC2-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

The Quick Start Guide provides step-by-step instructions on how to do an
initial system setup for the AD-FMCADC2-EBZ board.

.. _ad_fmcadc2_ebz carriers:

Supported carriers
-------------------------------------------------------------------------------

The AD-FMCADC2-EBZ connects to a single FMC HPC connector on the carrier.

.. list-table::
   :header-rows: 1

   * - Board
     - AD-FMCADC2-EBZ
   * - :xilinx:`VC707`
     - FMC1 HPC
   * - :xilinx:`ZC706`
     - FMC HPC

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
     - No-OS
   * - :xilinx:`VC707`
     - Yes
     - Yes (up to 2021_r2)
     - Yes
   * - :xilinx:`ZC706`
     - Yes
     - Yes (up to 2021_r2)
     - Yes

.. _ad_fmcadc2_ebz hardware-setup:

Hardware setup
-------------------------------------------------------------------------------

The carrier setup requires power, UART connection (115200 baud), and JTAG.
Connect the AD-FMCADC2-EBZ FMC board to the FPGA carrier:

- On the VC707: FMC1 HPC connector
- Connect USB JTAG (Micro USB) to your host PC
- Connect UART cable to the USB UART port (115200 baud, 8N1)
- Turn on the power switch on the FPGA board

.. toctree::
   :hidden:

   quickstart
