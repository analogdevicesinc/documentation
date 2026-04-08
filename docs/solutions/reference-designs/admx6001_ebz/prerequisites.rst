.. _admx6001 prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The :adi:`ADMX6001-EBZ` evaluation board
#. An FPGA carrier platform. Our recommended one can be found
   :ref:`here <admx6001 carriers>`.
#. Dual 12 V / 65 W power supplies (one for the ADMX6001-EBZ, one for the
   VCU118)
#. Benchtop function generator (signal source)
#. Micro-USB cables (×2, for UART console)
#. LAN cable (Ethernet, for IIO applications)
#. A host PC running Windows 10 or Windows 11 (with cooling fan recommended
   due to board heat dissipation)

Software prerequisites
-------------------------------------------------------------------------------

#. Xilinx ``xsct`` or ``xsdb``, included in
   :xilinx:`Vivado Lab Edition 2024.2 or later <support/download.html>`
   (for FPGA programming)
#. `Silicon Labs USB-to-UART VCP drivers
   <https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers>`__
   (for serial console access)
#. `Tera Term 5.4.0
   <https://github.com/TeraTermProject/teraterm/releases>`__ or later —
   UART terminal, 115200 baud, 8N1
#. :ref:`iio-oscilloscope` for data visualization (optional)
#. Python 3.11 or later with the :external+pyadi-iio:doc:`PyADI-IIO <index>`
   library (optional)

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
