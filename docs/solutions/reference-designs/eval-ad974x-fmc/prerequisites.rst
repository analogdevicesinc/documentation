.. _eval-ad974x fmc ebz prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need
to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. One of the AD974x evaluation boards:

   - :adi:`EVAL-AD9740 <EVAL-AD9740>` - 10-bit variant
   - :adi:`EVAL-AD9742 <EVAL-AD9742>` - 12-bit variant
   - :adi:`EVAL-AD9744 <EVAL-AD9744>` - 14-bit variant
   - :adi:`EVAL-AD9748 <EVAL-AD9748>` -  8-bit variant

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
before powering on the Zedboard. They are available as part of the ADI
Kuiper Linux image:

- ``BOOT.BIN`` - pre-built boot binary for the EVAL-AD9740 / EVAL-AD9742 /
  EVAL-AD9744 / EVAL-AD9748 on Zedboard
- ``uImage`` - Linux kernel image
- ``devicetree.dtb`` - device tree blob for the Zedboard + EVAL-AD9740 /
  EVAL-AD9742 / EVAL-AD9744 / EVAL-AD9748

For basic data visualization and DAC control we use:

#. :git-libiio:`libiio <releases/latest+>` (required by pyadi-iio on the host PC)
#. :git-pyadi-iio:`PyADI-IIO </>` - optional Python scripting interface

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   obtaining a Zedboard is a normal part of evaluation and development.
