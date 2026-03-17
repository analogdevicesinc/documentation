.. _ad9434 quickstart:

Quick start guides
===============================================================================

The Quick start guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD9434` boards on various FPGA
development boards. In these guides, we will discuss how to program the
bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZedBoard <zedboard>
   On ZC706 <zc706>

.. _ad9434 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9434` is, by definition a "FPGA mezzanine card" (FMC); that
means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD9434
   - - :xilinx:`ZC706`
     - FMC LPC
   - - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
     - FMC LPC

Supported Environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - :xilinx:`ZC706`
     - Yes
     - Yes
     - Yes
   - - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
     - Yes
     - Yes
     - Yes

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-AD9434` board connect to the LPC connector
(unless otherwise noted). The carrier setup requires power, UART (115200),
Ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections. A few
typical setups are shown below.

ZedBoard + EVAL-AD9434
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad9434_zed_os_setup.png
   :width: 800

ZC706 + EVAL-AD9434
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad9434_zc706_os_setup.png
   :width: 800