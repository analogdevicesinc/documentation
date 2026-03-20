.. _ad7768 quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD7768` / :adi:`EVAL-AD7768-4`
boards on various FPGA development boards. In these guides, we will discuss how
to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZED <zed>

.. _ad7768 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7768` / :adi:`EVAL-AD7768-4`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD7768
     - EVAL-AD7768-4
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC
     - FMC LPC

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - Eval Board
     - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - EVAL-AD7768
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes
   - - EVAL-AD7768-4
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - No

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-AD7768` / :adi:`EVAL-AD7768-4` boards
connect to the FMC LPC connector (unless otherwise noted). The carrier setup
requires power, UART (115200), Ethernet (Linux), HDMI (if available) and/or
JTAG (no-OS) connections. A few typical setups are shown below.

ZED + EVAL-AD7768
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad7768_zed_setup.jpg
   :width: 800

Go to :ref:`the setup guide <ad7768 quickstart zed>`.
