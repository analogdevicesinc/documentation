.. _ad-fmcdaq2-ebz quickstart:

AD-FMCDAQ2-EBZ Quick Start Guides
==================================

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the AD-FMCDAQ2-EBZ boards on various FPGA development
boards. They will discuss how to program the bitstream, run a no-OS program or
boot a Linux distribution.

Supported Carriers
------------------

The AD-FMCDAQ2-EBZ is, by definition a "FPGA mezzanine card" (FMC), that means
it needs a carrier to plug into. The carriers we support are:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Board
     - Quickstart Guide
   * - :intel:`Arria10 SoC Dev Kit <content/www/us/en/products/details/fpga/arria/10.html>`
     - :doc:`quickstart/a10soc`
   * - :intel:`Arria10 GX FPGA Dev Kit <content/www/us/en/products/details/fpga/development-kits/arria/10-gx.html>`
     - :doc:`quickstart/a10gx`
   * - :xilinx:`KC705 <products/boards-and-kits/ek-k7-kc705-g.html>`
     - :doc:`quickstart/microblaze`
   * - :xilinx:`KCU105 <products/boards-and-kits/kcu105.html>`
     - :doc:`quickstart/microblaze`
   * - :xilinx:`VC707 <products/boards-and-kits/ek-v7-vc707-g.html>`
     - :doc:`quickstart/microblaze`
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - :doc:`quickstart/zynq`
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - :doc:`quickstart/zcu102`

The supported OS are:

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Board
     - HDL
     - Linux Software
     - No-OS Software
   * - :intel:`Arria10 SoC Dev Kit <content/www/us/en/products/details/fpga/arria/10.html>`
     - YES
     - YES
     - NO
   * - :intel:`Arria10 GX FPGA Dev Kit <content/www/us/en/products/details/fpga/development-kits/arria/10-gx.html>`
     - NO (only until hdl_2021_r1 branch)
     - NO
     - NO
   * - :xilinx:`KC705 <products/boards-and-kits/ek-k7-kc705-g.html>`
     - YES
     - YES
     - YES
   * - :xilinx:`KCU105 <products/boards-and-kits/kcu105.html>`
     - YES
     - YES
     - YES
   * - :xilinx:`VC707 <products/boards-and-kits/ek-v7-vc707-g.html>`
     - NO (only until hdl_2018_r2 branch)
     - NO
     - NO
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - YES
     - YES
     - YES
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - YES
     - YES
     - YES

Hardware Setup
--------------

In most carriers, the AD-FMCDAQ2-EBZ board connects to the HPC connector (unless
otherwise noted). The carrier setup requires power, UART (115200), ethernet
(Linux), HDMI (if available) and/or JTAG (no-OS) connections.
