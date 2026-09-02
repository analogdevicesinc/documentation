.. _ad_fmcadc7_ebz quickstart:

Quick start
===============================================================================

.. warning::

   The :adi:`AD-FMCADC7-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

The Quick Start Guide provides step-by-step instructions on how to do an
initial system setup for the AD-FMCADC7-EBZ board.

.. _ad_fmcadc7_ebz carriers:

Supported carriers
-------------------------------------------------------------------------------

The AD-FMCADC7-EBZ board connects to the HPC FMC connector on the carrier.

.. list-table::
   :header-rows: 1

   * - Board
     - AD-FMCADC7-EBZ
   * - :xilinx:`ZC706`
     - HPC

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
     - No-OS
   * - :xilinx:`ZC706`
     - Yes
     - Yes (up to 2021_r2)
     - Yes

.. _ad_fmcadc7_ebz hardware-setup:

Hardware setup
-------------------------------------------------------------------------------

The carrier setup requires power, UART connection (115200 baud, 8N1), Ethernet
(for Linux), and JTAG (for No-OS) connections. The Zynq carrier programs the
FPGA and boots Linux from the SD card.

Connect the AD-FMCADC7-EBZ FMC board to the FPGA carrier:

- On the ZC706: HPC FMC connector
- Connect USB JTAG (Micro USB) to your host PC
- Connect UART cable to the USB UART port (115200 baud, 8N1)
- Connect an Ethernet cable (required for Linux remote access)
- Turn on the power switch on the FPGA board

.. toctree::
   :hidden:

   zc706
