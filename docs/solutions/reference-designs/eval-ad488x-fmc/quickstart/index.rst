.. _ad488x quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD488X-FMC <eval-ad4884>`
board on various FPGA development boards. In these guides, we will discuss how
to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZED <zed>

.. _ad488x carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD488X-FMC <eval-ad4884>`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD488X-FMC
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - No

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-AD488X-FMC <eval-ad4884>` board
connects to the FMC LPC connector (unless otherwise noted). The carrier
setup requires power, UART (115200), Ethernet (Linux), HDMI (if available)
and/or JTAG (no-OS) connections. A few typical setups are shown below.

ZED + EVAL-AD488X-FMC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to :ref:`the setup guide <ad488x quickstart zed>`.
