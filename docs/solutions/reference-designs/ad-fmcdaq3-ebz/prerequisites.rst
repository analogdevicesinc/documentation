.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq3-ebz/prerequisites

.. _ad_fmcdaq3_ebz prerequisites:

Prerequisites
=============

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
----------------------

#. The AD-FMCDAQ3-EBZ evaluation board: :adi:`AD-FMCDAQ3-EBZ`
#. An FPGA carrier platform. Our recommended ones can be found
   :ref:`here <ad_fmcdaq3_ebz carriers>`.
#. An SD card with at least 16GB of memory; see
   :external+kuiper:doc:`Kuiper <index>`
#. USB cable (Micro-B for UART)
#. Ethernet cable (for Linux)

Software prerequisites
----------------------

Normally, for basic functionalities regarding visualizing the data received
from the FPGA, we use the following:

#. :git-iio-oscilloscope:`IIO Oscilloscope <releases+>` — graphical waveform and spectrum analyzer
#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain the IIO
   plugin)

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan; getting
   one yourself is the normal part of development or evaluation.
