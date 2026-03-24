.. _ad_fmcmotcon1_ebz prerequisites:

Prerequisites
===============================================================================

.. warning::

   The :adi:`AD-FMCMOTCON1-EBZ` is a **legacy product** and is no longer
   actively supported. This documentation is provided for reference only.

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The controller board: :adi:`AD-FMCMOTCON1-EBZ`
#. The low voltage drive board: :adi:`AD-DRVLV1-EBZ`
#. An FPGA carrier platform. Our supported ones can be found
   :ref:`here <ad_fmcmotcon1_ebz carriers>`.
#. A BLDC motor with Hall effect sensors (or compatible encoder).
#. A 24 V, 3 A capable DC lab power supply.
#. A UART/USB cable for serial console access (115200 baud, 8N1).
#. An Ethernet cable (required for Linux remote access).
#. :adi:`AD-DYNO1-EBZ` — Dynamometer drive system (optional).

Software prerequisites
-------------------------------------------------------------------------------

#. An SD card loaded with the ADI Kuiper Linux distribution.
   See :external+kuiper:doc:`Kuiper Linux <index>` for flashing instructions.
#. :ref:`iio-oscilloscope`, a graphical tool for monitoring and controlling
   IIO devices.

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
