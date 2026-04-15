.. _eval-ad777x prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need
to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The :adi:`EVAL-AD7770-AD7779` evaluation board. All three device
   variants (AD7770, AD7771, AD7779) share the same hardware form factor
   and connect to the ZedBoard via FMC LPC. The active device is
   selected in firmware. Refer to the evaluation board user guide for
   board-level details.
#. An FPGA carrier platform:
   `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`_
   (Zynq-7000 ARM/FPGA SoC development board)
#. A micro-SD card (16 GB or larger)
#. A Micro-USB cable for UART console access
#. A network cable (Ethernet) connected to a router or switch

Software prerequisites
-------------------------------------------------------------------------------

The following software files are required to boot the system. Pre-built
files for this reference design are distributed as part of the ADI
Kuiper Linux SD card image:

- ``BOOT.BIN`` - first-stage bootloader, FPGA bitstream, and FSBL
- ``uImage`` - Linux kernel image
- ``devicetree.dtb`` - device tree blob for the ZedBoard + AD777X

.. note::

   These files are meant to be placed on the FAT boot partition of a
   Kuiper Linux SD card. They replace the default boot files for the
   ZedBoard. The root filesystem (ext4 partition) is provided by the
   Kuiper Linux image. See :external+kuiper:ref:`use-kuiper-image` for
   instructions on flashing the Kuiper Linux image to an SD card.

   If you prefer to build from source, the HDL project is available at
   :git-hdl:`projects/ad777x_fmcz`. Build instructions can be found at
   :external+hdl:ref:`Build an HDL project <build_hdl>`.

Normally, for basic functionalities regarding visualizing the data
received from the FPGA, we use the following:

#. :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`, a
   graphical tool for capturing and visualizing IIO device data
#. :external+scopy:doc:`Scopy <index>` v2.0 or later
   (must contain the IIO plugin)

A UART terminal application (e.g. PuTTY, Tera Term, Minicom) configured
for 115200 baud, 8N1 is needed to observe the boot process and interact
with the Linux shell.

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   obtaining one is a normal part of development or evaluation.
