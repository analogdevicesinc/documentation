.. _ad_fmcadc3_ebz quickstart:

Quick start
===============================================================================

.. warning::

   The :adi:`AD-FMCADC3-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

The Quick Start Guide provides step-by-step instructions on how to do an
initial system setup for the AD-FMCADC3-EBZ boards.

.. _ad_fmcadc3_ebz carriers:

Supported carriers
-------------------------------------------------------------------------------

The AD-FMCADC3-EBZ is an FMC board that needs a carrier to plug into. In most
carriers, the AD-FMCADC3-EBZ connects to the HPC connector (unless otherwise
noted).

.. list-table::
   :header-rows: 1

   * - Board
     - AD-FMCADC3-EBZ
   * - :xilinx:`VC707`
     - FMC HPC
   * - :xilinx:`ZC706`
     - FMC HPC

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux Software
     - No-OS Software
   * - :xilinx:`VC707`
     - Yes
     - Yes
     - ---
   * - :xilinx:`ZC706`
     - Yes
     - Yes
     - ---

.. _ad_fmcadc3_ebz hardware-setup:

Hardware setup
-------------------------------------------------------------------------------

The carrier setup requires power, UART connection (115200 baud), Ethernet cable
to connect to local network, HDMI (if available) and/or JTAG. A typical setup
with the ZC706 is shown below.

.. figure:: ../images/ad-fmcadc3-ebz_zc706_setup.png
   :alt: AD-FMCADC3-EBZ connected to the ZC706 FPGA carrier
   :align: center
   :width: 800

   AD-FMCADC3-EBZ with ZC706 hardware setup
