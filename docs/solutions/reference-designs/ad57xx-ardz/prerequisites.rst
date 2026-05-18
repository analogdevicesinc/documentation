.. _ad57xx prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a
minimum, you need to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The AD57xx-based evaluation boards:
   :adi:`EVAL-AD5780ARDZ`, :adi:`EVAL-AD5781ARDZ`,
   or :adi:`EVAL-AD5791ARDZ`.
#. A voltage reference daughter board (EV-ADR445-REFZ is
   included with each evaluation kit; EV-LTC6655-REFZ,
   EV-LTZ1000-REFZ, or EV-ADR1001-REFZ are available
   separately for improved performance).
#. An FPGA carrier platform. Our recommended ones can be found
   :ref:`here <ad57xx-ardz carriers>`.

   - There are a few more boards, which do work, but are
     currently not supported by us. The experience with the
     fabric-only solutions is very close to the ARM/FPGA SoC
     based solutions, but the GUI runs on a host PC (Windows
     or Linux).

#. Some way to interact with the FPGA platform:

   #. for the ARM/FPGA SoC platforms, this normally includes:

      - HDMI or DisplayPort monitor
      - USB Keyboard
      - USB Mouse

   #. for the FPGA only solutions, this includes:

      - LAN cable (Ethernet)
      - Host PC (Windows or Linux)

#. Internet connection (without proxies makes things much
   easier) to update the scripts/binaries on the SD card
   (firewalls are OK, proxies make things a pain).
#. An SD card with at least 16GB of memory (in case you're
   using Linux). You should have received one when purchasing
   the evaluation board.

Software prerequisites
-------------------------------------------------------------------------------

Normally, for basic functionalities regarding controlling the
DAC output and interfacing with the FPGA, we use the following:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must
   contain the IIO plugin)

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale
   or loan; getting one yourself is the normal part of
   development or evaluation.
