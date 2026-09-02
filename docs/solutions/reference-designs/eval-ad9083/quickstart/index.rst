.. _eval-ad9083 quickstart:

Quickstart
==========

The Quick start guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD9083`
board on various FPGA development boards. In these guides, we will discuss how
to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZCU102 <zcu102>
   On ADS8-V3EBZ <ads8-v3ebz>

.. _eval-ad9083 carriers:

Supported carriers
------------------

The :adi:`EVAL-AD9083`, is, by definition a "FPGA mezzanine card" (FMC); that
means it needs a carrier to plug into.

The carriers we support are listed below, as well as the FMC port where to
connect the evaluation board:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD9083
   - - :xilinx:`ZCU102`
     - FMC HPC0

Supported environments
----------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes

Hardware setup
--------------

On most carriers, the :adi:`EVAL-AD9083` board connects to the HPC0 connector
(unless otherwise noted). The carrier setup requires power, UART (115200),
Ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections.

ZCU102 + EVAL-AD9083
~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad9083_zcu102_linux.jpeg
   :width: 900
