Quick Start
================================================================================

The Quick Start Guides provide simple step-by-step instructions on how to do an
initial system setup for the :adi:`EVAL-AD9081`, :adi:`EVAL-AD9082`,
:adi:`EVAL-AD9986`, or :adi:`EVAL-AD9988` boards on various FPGA development
boards. They will discuss how to program the bitstream, run a no-OS program or
boot a Linux distribution.

.. toctree::
   :maxdepth: 1

   On VCK190 <vck190>

.. _ad9209-fmca carriers:

Supported Carriers
--------------------------------------------------------------------------------

The :adi:`EVAL-AD9081`, :adi:`EVAL-AD9082`, :adi:`EVAL-AD9986`, and
:adi:`EVAL-AD9988` are, by definition, "FPGA mezzanine cards" (FMC), which means
they need a carrier to plug into. The carriers we support are:

.. list-table::
   :header-rows: 1

   * - Board
     - EVAL-AD9081*
     - EVAL-AD9082*
     - EVAL-AD9986*
     - EVAL-AD9988*
   * - :xilinx:`VCK190`
     - FMCP1
     - FMCP1
     - FMCP1
     - FMCP1

.. note::

  \* only the RX path is used.

Supported Environments
--------------------------------------------------------------------------------

The supported environments are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - :xilinx:`VCK190`
     - Yes
     - Yes
     - ---

Hardware Setup
--------------------------------------------------------------------------------

In most carriers, the :adi:`EVAL-AD9081`, :adi:`EVAL-AD9082`,
:adi:`EVAL-AD9986`, or :adi:`EVAL-AD9988` boards connect to the **FMCP1**
connector (unless otherwise noted). The carrier setup requires power, UART
(115200), ethernet (Linux), and HDMI (if available). A few typical setups are
shown below.

VCK190 + EVAL-AD9081
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/vck190_ad9209.jpg
   :width: 800
