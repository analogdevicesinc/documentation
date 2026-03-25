.. _eval-ad353xr prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need
to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The AD353XR-based evaluation board: :adi:`EVAL-AD3530R` or
   :adi:`EVAL-AD3531R`
#. An FPGA carrier platform (one of):

   - `CoraZ7-07s 
     <https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development/>`_
   - `DE10-Nano
     <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`_
   - `ZedBoard
     <https://digilent.com/reference/programmable-logic/zedboard/start>`_

   .. note::

      The ZedBoard FMC connector is low pin count. VADJ must be set to
      **2.5 V** before powering on.

#. `FMC XM105
   <https://www.amd.com/en/products/adaptive-socs-and-fpgas/board-accessories/hw-fmc-xm105-g.html>`__
   or equivalent FMC to header adapter board for connecting the evaluation board to
   the FPGA carrier
#. Jumper wires to tap the SPI signals
#. 1x USB cable for UART access (Micro-USB for ZedBoard/CoraZ7, Mini-USB for DE10-Nano)
#. 1x Ethernet cable (for network access)
#. 1x microSD card (at least 16 GB)

Software prerequisites
-------------------------------------------------------------------------------

The following software is needed on the host PC:

.. note::

   Pre-built files for this reference design are not yet available.
   The files must be built manually using the links above. Official release
   artifacts will be provided here once available. For now, check:
   :external+hdl:ref:`Build an HDL project <build_hdl>` and 
   :ref:`Build the Linux kernel <linux-kernel>`

- A UART terminal (e.g. PuTTY, Tera Term, Minicom) configured for
  115200 baud, 8N1
- A microSD card flashed with the ADI Kuiper Linux image; follow
  :external+kuiper:doc:`this guide <index>`

For capturing and visualizing data from the device:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later
   (must contain the IIO plugin)
#. :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`, a graphical
   tool for capturing and visualizing IIO device data

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   obtaining one is part of the normal evaluation or development process.
