.. _ad485x_fmcz prerequisites:

Prerequisites
==============

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

- The :adi:`EVAL-AD4858` evaluation board
- The `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
  carrier board

Required Software
-----------------

- SD Card 16GB image using the instructions here:
  :dokuwiki:`Zynq & Altera SoC Quick Start Guide <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`
- A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

.. note::

   Instructions on how to build the Zynq Linux kernel and devicetrees
   from source can be found here:

   - :ref:`Building the Zynq Linux kernel and devicetrees from source <linux-kernel zynq>`
   - :external+hdl:ref:`How to build the Zynq boot image BOOT.BIN <build_boot_bin>`

Required Hardware
-----------------

- :adi:`EVAL-AD4858`
- `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
- Signal generator
- 1x Ethernet cable

Optional Hardware
-----------------

- :adi:` M2K <adalm2000>`
- :dokuwiki:`M2K BNC adapter board <university/tools/m2k/accessories/bnc>`
- 2x BNC to SMA cables
- 2x Micro-B USB cables

.. note::

   For custom systems where the :adi:`AD4858` chip is used, we recommend using
   an external clock, and not a clock from the FPGA like it is done in this
   reference design.
