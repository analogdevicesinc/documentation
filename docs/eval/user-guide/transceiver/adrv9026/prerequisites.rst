.. _adrv902x prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The ADRV9026/ADRV9029-based evaluation board:
   :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>`
#. An FPGA carrier platform. Our recommended ones are either:

   - The AMD Xilinx ZCU102 :xilinx:`ZCU102`. The fabric on this device is
     large, and if you are looking at targeting - this is the recommended
     option.
   - The AMD Xilinx :xilinx:`VCK190`. The fabric on this device is much
     larger.
   - There are a few more boards, which do work, but are currently not
     supported by us. The experience with the fabric-only solutions is very
     close to the ARM/FPGA SoC based solutions, but the GUI runs on a host PC
     (Windows or Linux).
   - :ref:`See the supported carriers <adrv902x carriers>`.

#. Some way to interact with the FPGA platform:

   #. for the ARM/FPGA SoC platforms, this normally includes:

      - HDMI or DisplayPort monitor
      - USB Keyboard
      - USB Mouse

   #. for the FPGA only solutions, this includes:

      - LAN cable (Ethernet)
      - Host PC (Windows or Linux)

#. Internet connection (without proxies makes things much easier) to update the
   scripts/binaries on the SD card that came with the ADI FMC Card (firewalls
   are OK, proxies make things a pain).
#. RF Test equipment
#. An SD card with at leas 16GB of memory (in case you're using Linux). You
   should have received one when purchasing the evaluation board.

Software prerequisites
-------------------------------------------------------------------------------

Normally, for basic functionalities regarding visualizing the data received
from the FPGA, we use the following:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain the IIO plugin)

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan; getting
   one yourself is the normal part of development or evaluation.
