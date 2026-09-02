.. _ad_fmcadc3_ebz prerequisites:

Prerequisites
===============================================================================

.. warning::

   The :adi:`AD-FMCADC3-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The AD9625-based evaluation board: :adi:`AD-FMCADC3-EBZ`
#. An FPGA carrier platform. Our supported ones can be found
   :ref:`here <ad_fmcadc3_ebz carriers>`.
#. A signal source for the analog input connector (J201 - labeled "Ain"):
#. A UART cable for serial console access (115200 baud, 8N1)
#. An SD card with at least 16 GB of memory.

Software prerequisites
-------------------------------------------------------------------------------

Normally, for basic functionalities regarding visualizing the data captured
from the ADC, we use the following:

#. :ref:`iio-oscilloscope`, a graphical
   tool for capturing and displaying IIO device data
#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must include the IIO
   plugin)

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
