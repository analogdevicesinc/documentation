.. _ad_fmcjesdadc1_ebz quickstart:

Quick start
===============================================================================

.. warning::

   The :adi:`AD-FMCJESDADC1-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

The Quick Start Guide provides step-by-step instructions on how to do an
initial system setup for the AD-FMCJESDADC1-EBZ board.

.. _ad_fmcjesdadc1_ebz carriers:

Supported carriers
-------------------------------------------------------------------------------

The AD-FMCJESDADC1-EBZ board connects to the HPC FMC connector on the carrier.

.. list-table::
   :header-rows: 1

   * - Board
     - AD-FMCJESDADC1-EBZ
   * - :xilinx:`KC705`
     - FMC HPC
   * - :xilinx:`VC707`
     - FMC1 HPC
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
   * - :xilinx:`KC705`
     - Yes
     - Yes (up to 2022_r2)
     - Yes
   * - :xilinx:`VC707`
     - Yes
     - Yes (up to 2022_r2)
     - Yes
   * - :xilinx:`ZC706`
     - Yes
     - Yes (up to 2022_r2)
     - Yes

.. _ad_fmcjesdadc1_ebz hardware-setup:

Hardware setup
-------------------------------------------------------------------------------

The carrier setup requires power, UART connection (115200 baud, 8N1), Ethernet
(for Linux), and JTAG (for No-OS) connections.

Connect the AD-FMCJESDADC1-EBZ FMC board to the FPGA carrier:

- On the KC705: FMC HPC connector
- On the VC707: FMC1 HPC connector
- On the ZC706: HPC connector
- Connect USB JTAG (Micro USB) to your host PC
- Connect UART cable to the USB UART port (115200 baud, 8N1)
- Connect an Ethernet cable (required for Linux remote access)
- Turn on the power switch on the FPGA board

.. toctree::
   :hidden:

   microblaze
