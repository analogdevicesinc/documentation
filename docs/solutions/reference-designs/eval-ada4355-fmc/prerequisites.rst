.. _eval-ada4355-fmc prerequisites:

Prerequisites
===============================================================================

What you need depends on which evaluation platform you are using.

EVAL-ADA4355EBZ (KC705)
-------------------------------------------------------------------------------

Hardware prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :adi:`EVAL-ADA4355EBZ <ADA4355>` evaluation board
#. Xilinx KC705 FPGA evaluation platform
#. DC2159A communication interface board (included with KC705)
#. 12 V power supply for the KC705
#. 5 V regulated power supply for the ADA4355 evaluation board
   (user provided)
#. USB cable (for DC2159A to PC connection)
#. Host PC running Windows

Software prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. ADA4355 Evaluation Software (see
   :ref:`Downloads <eval-ada4355ebz downloads>`)
#. MATLAB Runtime engine (installed automatically with the
   evaluation software if not already present)

EVAL-ADA4356EBZ (ZedBoard)
-------------------------------------------------------------------------------

Hardware prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :adi:`EVAL-ADA4356EBZ <ADA4356>` evaluation board
#. `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
   FPGA carrier platform
#. 12 V power supply for the ZedBoard
#. Some way to interact with the ZedBoard:

   - Micro-USB cable for UART console
   - LAN cable (Ethernet) for SSH or IIO applications

#. Internet connection (without proxies makes things much easier)
   to update the scripts/binaries on the SD card.
#. An SD card with at least 16 GB of memory (in case you are using
   Linux).
#. Signal generator or current source for analog input signals.

Software prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain
   the IIO plugin)
#. :git-iio-oscilloscope:`IIO Oscilloscope <releases>`
#. UART terminal application (PuTTY/TeraTerm/Minicom), 115200 8N1

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or
   loan; getting one yourself is the normal part of development or
   evaluation.
