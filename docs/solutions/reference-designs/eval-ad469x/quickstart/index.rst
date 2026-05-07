.. _eval-ad469x-quickstart:

Quick start guide
===============================================================================

The Quick start guides provide simple step-by-step instructions on how to do
an initial system setup for the :adi:`EVAL-AD4696` board on various FPGA
development boards. In these guides, we will discuss how to program the
bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZedBoard <zed>

.. _eval-ad469x-carriers:

Supported carriers
-------------------------------------------------------------------------------

The EVAL-AD469x is, by definition, an "FPGA mezzanine card" (FMC); that means
it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - EVAL-AD4696
   * - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_
     - FMC LPC

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_
     - Yes
     - Yes
     - Yes

Hardware setup
-------------------------------------------------------------------------------

On the ZedBoard, the EVAL-AD469x board connects to the FMC LPC connector.
The carrier setup requires power (12 V), USB OTG, and input signal
connections.

ZedBoard + EVAL-AD469x
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to
:ref:`the setup guide <eval-ad469x-quickstart-zedboard>`.
