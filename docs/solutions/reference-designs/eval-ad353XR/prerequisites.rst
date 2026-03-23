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

#. :adi:`SDP-I-FMC <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-i-fmc.html>`
   or equivalent adapter board for connecting the evaluation
   board to the FPGA carrier

   .. todo::

      Confirm exact adapter/connector used and add part number.

#. Jumper wires to tap the SPI signals
#. 1x Micro-USB to USB Type-A cable (for UART access)
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
  :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

For capturing and visualizing data from the device:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later
   (must contain the IIO plugin)
#. :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`, a graphical
   tool for capturing and visualizing IIO device data

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   obtaining one is part of the normal evaluation or development process.
