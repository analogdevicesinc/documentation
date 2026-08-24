.. _freqcvt1 prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The :adi:`AD-FREQCVT1-EBZ` 
#. An :adi:`AD-FMCOMMS3/4/5 <AD-FMCOMMS3-EBZ>` platform
#. An FPGA carrier platform. Our recommended one can be found
   :ref:`here <freqcvt1 carriers>`.

#. Some way to interact with the FPGA platform:

   - Micro-USB cable for UART console
   - LAN cable (Ethernet) for SSH or IIO applications
   - HDMI or DisplayPort monitor (Optional)
   - USB Keyboard (Optional)
   - USB Mouse (Optional)

#. SMA loopback cable
#. 12-pin ribbon cable
#. 3-pin power cable
#. SD card with at least 16 GB of memory

Software prerequisites
-------------------------------------------------------------------------------
The following software is needed on the host PC:

.. note::

   Pre-built files for this reference design are not yet available. The files
   must be built manually using the links above. Official release artifacts will
   be provided here once available. For now, check:
   :external+hdl:ref:`Build an HDL project <build_hdl>` and
   :ref:`Build the Linux kernel <linux-kernel>`

#. SD card 16 GB imaged with :external+kuiper:doc:`Kuiper <index>` (check out
   that guide on how to do it, then come back here).
#. A UART terminal (PuTTY/Tera Term/Minicom), 115200 baud, 8N1.
#. :ref:`iio-oscilloscope` for data visualization.

For capturing and visualizing data from the device:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain the IIO
   plugin)
#. :ref:`iio-oscilloscope`, a graphical tool
   for capturing and visualizing IIO device data

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan; getting
   one yourself is the normal part of development or evaluation.
