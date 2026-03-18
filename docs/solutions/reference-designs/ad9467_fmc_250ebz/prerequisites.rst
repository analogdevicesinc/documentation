.. _ad9467_fmc_250ebz prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The :adi:`AD9467`-based evaluation board:
   :adi:`EVAL-AD9467`

#. An FPGA carrier platform. Our recommended ones can be found
   :ref:`here <ad9467_fmc_250ebz carriers>`.

#. Some way to interact with the FPGA platform:

   #. for the ARM/FPGA SoC platforms, this normally includes:

      - HDMI or DisplayPort monitor
      - USB Keyboard
      - USB Mouse

   #. for the FPGA only solutions, this includes:

      - LAN cable (Ethernet)
      - Host PC (Windows or Linux)

#. Internet connection (without proxies makes things much easier) to connect to the FPGA carrier and test the board.

#. RF Test equipment:

   - Signal generator for clock input 250 MHz
   - Signal generator for analog input (for data capture)

#. An SD card with at least 16GB of memory (in case you're using Linux). You
   should have received one when purchasing the evaluation board.

Software prerequisites
-------------------------------------------------------------------------------

Normally, for basic functionalities regarding visualizing the data received
from the FPGA, we use the following:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain the IIO plugin)

#. UART terminal software (Tera Term, Putty, or equivalent) at 115200 baud rate

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan; getting
   one yourself is the normal part of development or evaluation.
