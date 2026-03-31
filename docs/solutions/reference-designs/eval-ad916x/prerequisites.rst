.. _eval-ad916x prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The AD916X-based evaluation board: :adi:`EVAL-AD916X-FMCZ <EVAL-AD916X>`
#. A supported FPGA carrier platform, currently
   :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
   on HPC0
#. An FPGA carrier platform. Our recommended ones can be found
   :ref:`here <eval-ad916x carriers>`.

   - There are a few more boards, which do work, but are currently not
     supported by us. The experience with the fabric-only solutions is very
     close to the ARM/FPGA SoC based solutions, but the GUI runs on a host PC
     (Windows or Linux).

#. Some way to interact with the FPGA platform:

   #. for the ARM/FPGA SoC platforms, this normally includes:

      - HDMI or DisplayPort monitor
      - USB Keyboard
      - USB Mouse

   #. for the FPGA only solutions, this includes:

      - LAN cable (Ethernet)
      - Host PC (Windows or Linux)

#. Internet connection (without proxies makes things much easier) to update
   the scripts/binaries on the SD card that came with the ADI FMC Card
   (firewalls are OK, proxies make things a pain).

#. RF Test Equipment:

   - RF spectrum analyzer or signal analyzer (to measure and visualize the
     DAC output spectrum and performance)
   - SMA cables

#. An SD card with at least 16GB of memory (in case you're using Linux). You
   should have received one when purchasing the evaluation board.

Software prerequisites
-------------------------------------------------------------------------------

.. note::

   Pre-built files for this reference design are not yet available.
   The files must be built manually using the links below. Official release
   artifacts will be provided here once available. For now, check:

     -  :external+hdl:ref:`build_hdl`
     -  :external+hdl:ref:`build_boot_bin`
     -  :ref:`linux-kernel zynqmp`

   You can also check the available Linux driver Linux at
   :git-linux:`AD9162 IIO driver <drivers/iio/frequency/ad9162.c>`
   and the HDL repository at :git-hdl:`EVAL-AD916X HDL <projects/ad916x_fmc>`.


The following files must be gathered into a single working directory
before programming the board:

- HDL boot image: ``BOOT.BIN``
- Linux Kernel image: ``uImage``
- Linux device tree: ``devicetree.dtb``

  - Built from available dts files for AD916x in the Linux kernel source tree:
  - :git-hdl:`EVAL-AD916X HDL <projects/ad916x_fmc/zcu102>` (check readme for details)

Normally, for basic functionalities regarding visualizing the
data received from the FPGA, we use the following:

#. :ref:`iio-oscilloscope`, a graphical
   tool for capturing and visualizing IIO device data
#. :external+scopy:doc:`Scopy <index>` v2.0 or later
   (must contain the IIO plugin)
#. UART terminal application (PuTTY/TeraTerm/Minicom), 115200 8N1

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
