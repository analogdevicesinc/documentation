.. _eval-ad353xr quickstart:

Quick start
===============================================================================

The quick start guide provides step-by-step instructions on how to do
an initial system setup for the :adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R`
evaluation board on the supported FPGA carrier. This guide covers how to
prepare the SD card, program the bitstream, and boot Kuiper Linux.

.. toctree::

   On CoraZ7s + EVAL-AD353XR <coraz7s>
   On DE10-Nano + EVAL-AD353XR <de10nano>
   On ZedBoard + EVAL-AD353XR <zed>

.. _eval-ad353xr carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD3530R` and :adi:`EVAL-AD3531R` connect to the FPGA carrier
via SPI and GPIO signals, routed through an adapter board.

.. list-table::
   :header-rows: 1

   * - FPGA board
     - :adi:`EVAL-AD3530R`
     - :adi:`EVAL-AD3531R`
   * - CoraZ7-07S
     - SPI
     - SPI
   * - DE10-Nano
     - SPI
     - SPI
   * - ZedBoard
     - SPI (FMC LPC)
     - SPI (FMC LPC)

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - CoraZ7-07S
     - Yes
     - Yes
     - ---
   * - DE10-Nano
     - Yes
     - Yes
     - ---
   * - ZedBoard
     - Yes
     - Yes
     - ---

Hardware setup
-------------------------------------------------------------------------------

.. todo::

   Add hardware setup photos for each carrier once hardware is available.
   One subsection per carrier following the ad9213-docs pattern.
