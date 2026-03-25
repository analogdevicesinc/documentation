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

CoraZ7s
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/full_set_up_cora.jpeg
   :alt: Full setup - CoraZ7s with EVAL-AD3530R connected
   :width: 700

   CoraZ7s with EVAL-AD3530R

DE10-Nano
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/de10_nano_setup.jpeg
   :alt: DE10-Nano with connections
   :width: 700

   DE10-Nano with connections

ZedBoard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/zed_board_setup.jpeg
   :alt: ZedBoard with connections
   :width: 700

   ZedBoard with connections

.. figure:: ../images/ad353xr_setup.jpeg
   :alt: EVAL-AD3530R evaluation board on ZedBoard setup
   :width: 700

   EVAL-AD3530R on ZedBoard
