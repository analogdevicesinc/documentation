.. _fmcomms11 quickstart:

Quick start guide
===============================================================================

The Quick start guide provides simple step by step
instructions on how to do an initial system setup for the
:adi:`AD-FMCOMMS11-EBZ` board on the :xilinx:`ZC706`
carrier.

.. toctree::

   On ZC706 <zc706>

.. _fmcomms11 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`AD-FMCOMMS11-EBZ`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to
plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - AD-FMCOMMS11-EBZ
   - - :xilinx:`ZC706`
     - FMC HPC

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - :xilinx:`ZC706`
     - Yes
     - Yes
     - ---

Hardware setup
-------------------------------------------------------------------------------

On the ZC706, the :adi:`AD-FMCOMMS11-EBZ` board connects
to the FMC HPC connector. The carrier setup requires
power, UART (115200), Ethernet (Linux) and HDMI (if
available) connections. A typical setup is shown below.

ZC706 + AD-FMCOMMS11-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/system_test_setup.png
   :width: 800
