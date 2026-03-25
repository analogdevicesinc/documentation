.. _arradio prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`_
   board by Arrow & Terasic for the :adi:`AD9361`
#. An FPGA carrier platform. Our recommended one is the
   `Terasic C5 SoCkit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_.
#. For the ARM/FPGA SoC platform (Terasic C5 SoCkit), you will need:

   - An 16GB (or larger) Micro-SD Card
   - USB keyboard and mouse
   - OTG Cable (for the USB keyboard and mouse)
   - A VGA compatible monitor
   - Ethernet cable
   - 1 x Micro-USB cable (for UART terminal access)

#. Internet connection (without proxies makes things much easier) to update
   the scripts/binaries on the SD card (firewalls are OK, proxies make things
   a pain).
#. RF Test equipment

HSMC supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Arradio evaluation board is powered through the HSMC connector.

The VADJ values can be checked out in the README.md file of each combination
with an FPGA, at: :git-hdl:`projects/arradio`.

Software prerequisites
-------------------------------------------------------------------------------

Normally, for basic functionalities regarding visualizing the data received
from the FPGA, we use the following:

#. A Host PC (Linux) for initial setup and configuration
#. A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)
#. :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` for data
   visualization and device control

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
