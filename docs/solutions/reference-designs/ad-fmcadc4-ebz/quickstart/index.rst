.. _ad_fmcadc4_ebz quickstart:

Quick start
===============================================================================

.. warning::

   The :adi:`AD-FMCADC4-EBZ` is a **legacy product** that has been retired
   and is no longer available for sale. It has been removed from the HDL and
   software repositories, but is still available in the git history. This
   documentation is provided for reference only.

The Quick Start Guide provides step-by-step instructions on how to do an
initial system setup for the AD-FMCADC4-EBZ boards.

.. _ad_fmcadc4_ebz carriers:

Supported carriers
-------------------------------------------------------------------------------

The AD-FMCADC4-EBZ is an FMC board that needs a carrier to plug into. In most
carriers, the AD-FMCADC4-EBZ connects to the HPC connector (unless otherwise
noted).

.. list-table::
   :header-rows: 1

   * - Board
     - AD-FMCADC4-EBZ
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
   * - :xilinx:`ZC706`
     - Yes
     - Yes
     - ---

.. _ad_fmcadc4_ebz hardware-setup:

Hardware setup
-------------------------------------------------------------------------------

The carrier setup requires power, UART connection (115200 baud), Ethernet cable
to connect to local network, HDMI (if available) and/or JTAG. A typical setup
with the ZC706 is shown below.

.. figure:: ../images/ad-fmcadc4-ebz_zc706.png
   :alt: AD-FMCADC4-EBZ connected to the ZC706 FPGA carrier
   :align: center
   :width: 800

   AD-FMCADC4-EBZ with ZC706 hardware setup
