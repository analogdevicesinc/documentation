.. _ad77681 quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD7768-1` / :adi:`EVAL-ADAQ7768-1`
boards.

FPGA-based evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use these guides when evaluating with an FPGA carrier board. They cover
bitstream programming, no-OS programs and Linux boot.

.. toctree::

   On ZED <zed>

.. _ad77681 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7768-1` / :adi:`EVAL-ADAQ7768-1`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD7768-1
     - EVAL-ADAQ7768-1
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
   - - EVAL-AD7768-1
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes
   - - EVAL-ADAQ7768-1
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - No
     - No

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-AD7768-1` / :adi:`EVAL-ADAQ7768-1` boards
connect to the FMC LPC connector (unless otherwise noted). The carrier setup
requires power, UART (115200), Ethernet (Linux), HDMI (if available) and/or
JTAG (no-OS) connections. A few typical setups are shown below.

ZED + EVAL-AD7768-1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad77681_zed.jpg
   :width: 800

ZED + EVAL-ADAQ7768-1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adaq77681_zed.jpg
   :width: 800

SDP-based evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use these guides when evaluating with the SDP (System Demonstration Platform)
controller boards and the ACE software on a PC.

.. toctree::

   AD7768-1 on SDP-K1 <ad77681_mbed_iio_app>
   ADAQ7768-1 on SDP-H1 <adaq77681-eval-board>
