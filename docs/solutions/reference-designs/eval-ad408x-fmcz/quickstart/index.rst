Quick Start
================================================================================

The Quick Start Guides provide simple step-by-step instructions on how to do an
initial system setup for the :adi:`EVAL-AD4080-FMC`, :adi:`EVAL-AD4083-FMC` and
:adi:`EVAL-AD4086-FMC` boards on various FPGA development boards. They will
discuss how to program the bitstream, run a no-OS program or boot a Linux
distribution.

.. toctree::
   :maxdepth: 1

   On Zedboard <zed>

.. _ad408x-fmcz carriers:

Supported Carriers
--------------------------------------------------------------------------------

The :adi:`EVAL-AD4080-FMC`, :adi:`EVAL-AD4083-FMC` and :adi:`EVAL-AD4086-FMC`
are, by definition, "FPGA mezzanine cards" (FMC), which means they need a
carrier to plug into. The carriers we support are:

.. list-table::
   :header-rows: 1

   * - Board
     - EVAL-AD4080-FMC
     - EVAL-AD4083-FMC
     - EVAL-AD4086-FMC
   * - `Zedboard <https://digilent.com/reference/programmable-logic/zedboard/start>`_
     - FMC LPC
     - FMC LPC
     - FMC LPC

Supported Environments
--------------------------------------------------------------------------------

The supported environments are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - no-OS software
   * - `Zedboard <https://digilent.com/reference/programmable-logic/zedboard/start>`_
     - Yes
     - Yes
     - ---

Hardware Setup
--------------------------------------------------------------------------------

In most carriers, the :adi:`EVAL-AD4080-FMC`, :adi:`EVAL-AD4083-FMC` and
:adi:`EVAL-AD4086-FMC` boards connect to the **LPC** connector (unless otherwise
noted). The carrier setup requires power, UART (115200), ethernet (Linux), and
HDMI (if available). A few typical setups are shown below.

Zedboard + EVAL-AD4080-FMC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/zed_ad4080.jpg
   :width: 800
