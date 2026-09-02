.. _adv7511 quickstart:

Quick start guides
===============================================================================

The Quick start guides provide simple step-by-step instructions on how to do
an initial system setup for the ADV7511 HDMI transmitter on various FPGA
evaluation boards. In these guides, we will discuss how to program the
bitstream, run a no-OS program, or boot a Linux distribution (for Zynq
platforms).

.. toctree::

   On AC701 <ac701>
   On KC705 <kc705>
   On VC707 <vc707>
   On ZC702 <zc702>
   On ZC706 <zc706>
   On ZedBoard <zed>

.. _adv7511 carriers:

Supported carriers
-------------------------------------------------------------------------------

The ADV7511 HDMI transmitter is integrated on-board the following Xilinx
FPGA evaluation platforms:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - FPGA Family
     - ADV7511 Location
   - - :xilinx:`ZC702`
     - Zynq-7000 SoC
     - On-board
   - - :xilinx:`ZC706`
     - Zynq-7000 SoC
     - On-board
   - - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
     - Zynq-7000 SoC
     - On-board

.. note::

   The following carriers are last supported only in the
   :git-hdl:`hdl_2017_r1 <hdl_2017_r1:projects/adv7511>` release:
   :xilinx:`AC701` (Artix-7), :xilinx:`KC705` (Kintex-7), and
   :xilinx:`VC707` (Virtex-7).

Supported Environments
-------------------------------------------------------------------------------

The supported OS and software environments are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - :xilinx:`ZC702`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`ZC706`
     - Yes
     - Yes
     - Yes
   - - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
     - Yes
     - Yes
     - Yes

.. note::

   The :xilinx:`AC701`, :xilinx:`KC705`, and :xilinx:`VC707` carriers are
   last supported only in the :git-hdl:`hdl_2017_r1 <hdl_2017_r1:projects/adv7511>`
   release with no-OS software only.

Hardware setup
-------------------------------------------------------------------------------

The ADV7511 is integrated on-board each evaluation platform, so no FMC card
connection is required. The basic setup requires:

- Power supply for the FPGA board
- UART connection (115200 baud, 8N1) for serial console
- HDMI cable connected to a monitor
- For Zynq boards running Linux: Ethernet connection, HDMI monitor, USB
  keyboard/mouse (optional)
- For FPGA-only boards: JTAG connection for programming
