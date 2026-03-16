.. _ad9213 evb prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need
to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The AD9213-based evaluation board: :adi:`EVAL-AD9213`
#. An FPGA carrier platform: AMD Xilinx :xilinx:`VCU118`
#. A ZX180V-HSPC FMC VITA 57.4 Mezzanine card breakout adapter

   - Required because the :adi:`EVAL-AD9213` does not natively
     support JTAG boot. The breakout adapter exposes the FMC+ pins so that
     a wire can be placed between pins D30 and D31 to close the JTAG chain.

#. 2x Micro-USB cables (one for JTAG, one for UART)
#. External power supply for the evaluation board
#. Some way to interact with the FPGA platform:

   - A UART terminal (e.g. PuTTY/Tera Term/Minicom) configured for
     115200 baud, 8N1

Software prerequisites
-------------------------------------------------------------------------------

The following files must be gathered into a single working directory
before programming the board:

- ``system_top.bit``,  HDL bitstream file
- ``simpleImage.vcu118_ad9213_evb.strip``,  Linux kernel image
- ``run.tcl``, tcl script

.. note::

   Pre-built files for this reference design are not yet available.
   The files must be built manually using the links above. Official release
   artifacts will be provided here once available. For now, check:
   :external+hdl:ref:`Build an HDL project <build_hdl>` and
   :ref:`linux-kernel microblaze`. You can also check the in-development 
   Linux branch at :git-linux:`9213 branch <9213:/>` and the HDL repository
   at :git-hdl:`ad9213_evb <projects/ad9213_evb>`.

To program the board, Xilinx ``xsct`` or ``xsdb`` must be installed on
the host PC (included in the Xilinx Vitis or Vivado toolchain).

Normally, for basic functionalities regarding visualizing the
data received from the FPGA, we use the following:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later
   (must contain the IIO plugin)
#. :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`, a graphical
   tool for capturing and visualizing IIO device data

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
