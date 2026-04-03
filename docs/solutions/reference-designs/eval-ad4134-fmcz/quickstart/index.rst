.. _eval-ad4134-fmcz quickstart:

Quickstart
==========

The Quick start guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD4134FMCZ`
board on various FPGA development boards. In these guides, we will discuss how
to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZedBoard <zed>

.. _eval-ad4134-fmcz carriers:

Supported carriers
------------------

The :adi:`EVAL-AD4134FMCZ`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD4134FMCZ
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC

Supported environments
----------------------

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
--------------

On the ZedBoard, the :adi:`EVAL-AD4134FMCZ` board connects to the FMC LPC
connector. The carrier setup requires power, UART (115200), Ethernet (Linux),
and/or JTAG (no-OS) connections.

ZedBoard + EVAL-AD4134FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/ad4134_setup_hardware.jpg
   :align: center
   :width: 600

   ZedBoard + EVAL-AD4134FMCZ setup
