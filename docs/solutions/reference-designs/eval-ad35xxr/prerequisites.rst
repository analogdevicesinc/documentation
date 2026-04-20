.. _eval-ad35xxr evb prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need
to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. One of the AD35xxR evaluation boards:

   - :adi:`EVAL-AD3552RFMC1Z <EVAL-AD3552R>` - optimized for high-speed
     dynamic performance (EVAL-AD3552RFMC1Z)
   - :adi:`EVAL-AD3552RFMC2Z <EVAL-AD3552R>` - optimized for DC precision
     (EVAL-AD3552RFMC2Z)
   - :adi:`EVAL-AD3542RFMCZ <EVAL-AD3542R>` - 12-bit variant

#. `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/
   avnet-board-families/zedboard/>`_ Rev D or later (Zynq-7000 SoC)
#. 16 GB (or larger) Class 10 micro-SD card
#. 12 V, 3 A power supply for the ZedBoard
#. Micro-USB cable (UART, J14 on ZedBoard)
#. Ethernet cable
#. An oscilloscope for monitoring DAC outputs (J4, J5 SMB connectors)

Software prerequisites
-------------------------------------------------------------------------------

The following files must be placed on the micro-SD card boot partition
before powering on the ZedBoard. They are available as part of the ADI
Kuiper Linux image:

- ``BOOT.BIN`` - pre-built boot binary for the EVAL-AD3552R on ZedBoard
- ``uImage`` - Linux kernel image
- ``devicetree.dtb`` - device tree blob for the ZedBoard + EVAL-AD3552R

For basic data visualization and DAC control we use:

#. :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` - graphical
   tool for capturing and visualizing IIO device data
#. :external+scopy:doc:`Scopy <index>` - oscilloscope and waveform
   generator application
#. `libiio <https://github.com/analogdevicesinc/libiio/releases>`_
   (required by IIO Oscilloscope and pyadi-iio on the host PC)
#. :git-pyadi-iio:`PyADI-IIO </>` - optional Python scripting interface

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   obtaining a ZedBoard is a normal part of evaluation and development.
