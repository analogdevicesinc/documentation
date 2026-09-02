.. _ad_fmcdaq2_ebz prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The AD9680/AD9144-based evaluation board: :adi:`AD-FMCDAQ2-EBZ`
#. An FPGA carrier platform. Our recommended ones can be found
   :ref:`here <ad_fmcdaq2_ebz carriers>`.

   - There are a few more boards, which do work, but are currently not supported
     by us. The experience with the fabric-only solutions is very close to the
     ARM/FPGA SoC based solutions, but the GUI runs on a host PC (Windows or
     Linux).

#. Some way to interact with the FPGA platform:

   #. for the ARM/FPGA SoC platforms, this normally includes:

      - USB Mouse
      -  [Optional] USB keyboard/mouse for the Zynq Device
      -  [Optional] HDMI Display (monitor or TV FULL HD only)

   #. for the FPGA only solutions, this includes:

      - LAN cable (Ethernet)
      -  You need a Host PC (Windows or Linux).

#. Internet connection (without proxies makes things much easier) to update the
   scripts/binaries on the SD card that came with the ADI FMC Card (firewalls
   are OK, proxies make things a pain).
#. RF Test equipment
#. An SD card with at least 16GB of memory (in case you're using Linux). You
   should have received one when purchasing the evaluation board.

Software prerequisites
-------------------------------------------------------------------------------

Normally, for basic functionalities regarding visualizing the data received from
the FPGA, we use the following:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain the IIO
   plugin)

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan; getting
   one yourself is the normal part of development or evaluation.
