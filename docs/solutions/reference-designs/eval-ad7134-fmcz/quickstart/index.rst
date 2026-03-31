.. _eval-ad7134-fmcz quickstart:

Quickstart
==========

The Quick start guides provide simple step by step instructions on how to
do an initial system setup for the :adi:`EVAL-AD7134FMCZ` board on various
FPGA development boards. In these guides, we will discuss how to program
the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   Zedboard <zed>

.. _eval-ad7134-fmcz carriers:

Supported carriers
------------------

The :adi:`EVAL-AD7134FMCZ`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD7134-FMCZ
   - - `ZedBoard
       <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC

Supported Environments
----------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - `ZedBoard
       <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes

Hardware Setup
--------------

The :adi:`EVAL-AD7134FMCZ` board connects to the FMC LPC
connector of the carrier board. The carrier setup requires power,
UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS)
connections.

A few typical setups are shown below.

ZedBoard + EVAL-AD7134FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/ad7134_hardware_setup_linux.jpg
   :align: center
   :width: 500

   ZedBoard + EVAL-AD7134FMCZ hardware setup
