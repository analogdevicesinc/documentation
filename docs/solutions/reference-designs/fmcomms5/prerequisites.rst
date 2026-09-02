.. _fmcomms5-prerequisites:

Prerequisites
=============

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
----------------------

#. An :adi:`AD-FMCOMMS5-EBZ` evaluation board.
#. A carrier board with **two adjacent FMC connectors**. The supported
   options are:

   .. list-table::
      :header-rows: 1

      -  - Carrier board
         - Connector
      -  - :xilinx:`ZC706`
         - Dual FMC (HPC)
      -  - :xilinx:`ZC702`
         - Dual FMC (LPC)
      -  - :xilinx:`ZCU102`
         - Dual FMC (HPC)

   .. warning::

      The AD-FMCOMMS5-EBZ uses a dual FMC connector. Carrier boards
      with only a single FMC connector are **not** supported.

#. A way to interact with the carrier:

   - ARM/FPGA SoC carriers (ZC702, ZC706): HDMI or VGA monitor, USB
     keyboard and mouse
   - ZynqMP carrier (ZCU102): DisplayPort monitor, USB keyboard and
     mouse (both optional; UART via Micro-USB is sufficient)

#. An internet connection for updating SD card scripts and binaries.
#. RF test equipment (signal generator, spectrum analyzer) or SMA
   loopback cables for basic functional testing.

Software prerequisites
----------------------

#. :external+kuiper:doc:`Kuiper <index>` SD card image for Zynq-based carriers
   (ZC702, ZC706) and ZynqMP-based carriers (ZCU102).
#. `balenaEtcher <https://etcher.balena.io/>`_ or similar tool to
   write the SD card image.
#. UART terminal application (PuTTY, Tera Term, Minicom, etc.),
   configured for baud rate 115200 (8N1).
#. :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`
   (pre-installed on the Kuiper Linux image, or available for remote
   connection from a host PC).
