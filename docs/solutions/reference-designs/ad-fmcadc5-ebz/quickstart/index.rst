.. _ad_fmcadc5_ebz quickstart:

Quick start
===============================================================================

.. warning::

   The :adi:`AD-FMCADC5-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

The Quick Start Guide provides step-by-step instructions on how to do an
initial system setup for the AD-FMCADC5-EBZ boards.

.. _ad_fmcadc5_ebz carriers:

Supported carriers
-------------------------------------------------------------------------------

The AD-FMCADC5-EBZ is a double FMC wide board that needs a carrier with two
fully populated FMC connectors. It connects to both the FMC1 and FMC2
connectors on the carrier.

.. list-table::
   :header-rows: 1

   * - Board
     - AD-FMCADC5-EBZ
   * - :xilinx:`VC707`
     - FMC1 & FMC2

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

.. _ad_fmcadc5_ebz hardware-setup:

Hardware setup
-------------------------------------------------------------------------------

The carrier setup requires power, UART connection (115200 baud), and JTAG.
Connect the AD-FMCADC5-EBZ FMC board to the FPGA carrier:

- On the VC707: FMC1 & FMC2 connector
- Connect USB JTAG (Micro USB) to your host PC
- Connect UART cable to the USB UART port (115200 baud, 8N1)
- Turn on the power switch on the FPGA board

.. toctree::
   :hidden:

   vc707
