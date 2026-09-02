.. _ad485x_fmcz quickstart:

Quick start guide
===============================================================================

The Quick Start Guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD4858` boards.

FPGA-based evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use these guides when evaluating with an FPGA carrier board. They
cover bitstream programming and Linux boot.

.. toctree::
   :titlesonly:

   On ZedBoard <zed>

.. _ad485x_fmcz carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD4858` is, by definition, a "FPGA mezzanine card"
(FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD4858
   - - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
     - FMC LPC

Supported environments
-------------------------------------------------------------------------------

The supported environments are:

.. list-table::
   :header-rows: 1

   - - Eval Board
     - FPGA board
     - HDL
     - Linux
     - No-OS
   - - EVAL-AD4858
     - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
     - Yes
     - Yes
     - No
