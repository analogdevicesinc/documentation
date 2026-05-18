.. _eval-ad463x-quickstart:

Quick start guide
===============================================================================

The Quick start guides provide simple step-by-step instructions on how to do
an initial system setup for the :adi:`EVAL-AD4630-24` / :adi:`EVAL-AD4630-16` /
:adi:`EVAL-AD4030-24` boards on various FPGA development boards. In these
guides, we will discuss how to program the bitstream, run a no-OS program or
boot a Linux distribution.

.. toctree::

   On ZedBoard <zynq>

.. _eval-ad463x-carriers:

Supported carriers
-------------------------------------------------------------------------------

The EVAL-AD463x-FMCZ / EVAL-AD4030-24FMCZ is, by definition, an "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - EVAL-AD4630-24
     - EVAL-AD4630-16
     - EVAL-AD4030-24
   * - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_
     - FMC LPC
     - FMC LPC
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

On the ZedBoard, the EVAL-AD463x-FMCZ / EVAL-AD4030-24FMCZ boards connect to
the FMC LPC connector. The carrier setup requires power (12 V), USB OTG, and
input signal connections.

ZedBoard + EVAL-AD463x-FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/zedboard_ad4630_16_setup.jpg
   :align: center
   :width: 600

The AD463x/AD403x family uses the Digilent ZedBoard as the default system
controller. The
`ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_
web page contains more technical documentation on the board. In addition to the
ZedBoard, other 3rd party boards that have an FMC form factor may also be used
with the AD463x/AD403x family of boards.

Go to
:ref:`the setup guide <eval-ad463x-quickstart-zedboard>`.
