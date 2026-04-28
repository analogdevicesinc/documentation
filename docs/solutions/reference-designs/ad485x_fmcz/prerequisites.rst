.. _ad485x_fmcz prerequisites:

Prerequisites
=============

What you need depends on what you are trying to do. As a minimum,
you need to start out with:

Hardware prerequisites
----------------------

#. An :adi:`EVAL-AD4858` evaluation board
#. An FPGA carrier platform. Our recommended one can be found
   :ref:`here <ad485x_fmcz carriers>`.
#. Some way to interact with the FPGA platform:

   - Micro-USB cable for UART console
   - LAN cable (Ethernet) for SSH or IIO applications
   - Micro-USB cable for JTAG (for no-OS)

#. Internet connection to update the scripts/binaries on the SD card.
#. Test equipment for generating analog input signals.
#. An SD card with at least 16GB of memory (in case you're using
   Linux). You should have received one when purchasing the
   evaluation board.

Software prerequisites
----------------------

Normally, for basic functionalities regarding visualizing the data
received from the FPGA, we use the following:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain
   the IIO plugin)
#. :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`
#. UART terminal application (PuTTY/TeraTerm/Minicom), 115200 8N1

.. note::

   Instructions on how to build the Zynq Linux kernel and devicetrees
   from source can be found here:

   - :ref:`Building the Zynq Linux kernel and devicetrees from source <linux-kernel zynq>`
   - :external+hdl:ref:`How to build the Zynq boot image BOOT.BIN <build_boot_bin>`

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or
   loan; getting one yourself is the normal part of development or
   evaluation.

Optional Hardware
-----------------

- :adi:`M2K <adalm2000>`
- :dokuwiki:`M2K BNC adapter board <university/tools/m2k/accessories/bnc>`
- 2x BNC to SMA cables
- 2x Micro-B USB cables

.. note::

   For custom systems where the :adi:`AD4858` chip is used, we recommend using
   an external clock, and not a clock from the FPGA like it is done in this
   reference design.
