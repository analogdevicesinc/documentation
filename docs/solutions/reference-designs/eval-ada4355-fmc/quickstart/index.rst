.. _eval-ada4355-fmc quickstart:

Quickstart
===============================================================================

The Quick Start Guide provides simple step by step instructions on
how to do an initial system setup for the :adi:`EVAL-ADA4356EBZ`
board.

FPGA-based evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this guide when evaluating with an FPGA carrier board. It
covers SD card preparation, hardware assembly, Linux boot, and
testing with Scopy and IIO Oscilloscope.

.. toctree::

   On ZedBoard <zed>

.. _eval-ada4355-fmc carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-ADA4356EBZ` is an FMC mezzanine card that needs a
carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-ADA4356EBZ
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   - - Eval Board
     - FPGA board
     - HDL
     - Linux software
   - - EVAL-ADA4356EBZ
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes

Hardware setup
-------------------------------------------------------------------------------

On the ZedBoard, the :adi:`EVAL-ADA4356EBZ` connects to the FMC LPC
connector. The carrier setup requires power (12 V), Ethernet,
and UART (115200) connections.

.. image:: ../images/ada4356_zed.jpg
   :width: 800
