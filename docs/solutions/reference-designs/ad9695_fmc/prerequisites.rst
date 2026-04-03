.. _ad9695 prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The AD9695/AD9697-based evaluation board:
   :adi:`AD9695-1300EBZ <AD9695>`
#. An FPGA carrier platform. Our recommended one can be found
   :ref:`here <ad9695 carriers>`.

#. Some way to interact with the FPGA platform:

   - Micro-USB cable for UART console
   - LAN cable (Ethernet) for SSH or IIO applications
   - HDMI or DisplayPort monitor (Optional)
   - USB Keyboard (Optional)
   - USB Mouse (Optional)

#. A clock source, any low-noise clock generator with multiple outputs
   can be used. The following items are needed only if using the
   :adi:`AD-SYNCHRONA14-EBZ <AD-SYNCHRONA14-EBZ>`:

   - :adi:`AD-SYNCHRONA14-EBZ <AD-SYNCHRONA14-EBZ>` clock source board
     (Optional)
   - Serial port module for the AD-SYNCHRONA14-EBZ serial interface
     (Optional)
   - 20-pin GPIO ribbon cable for serial communication between the ZCU102
     and the AD-SYNCHRONA14-EBZ, connected pin-to-pin, all 20 pins
     (Optional)
   - 3× SMA 50Ω terminators for unused AD-SYNCHRONA14-EBZ output channels
     (Optional)

#. SMA cables (for connections between the clock source, AD9695, and signal
   generator)
#. Low phase noise signal generator with antialiasing filter (analog input
   source)
#. ZCU102 power supply (12 V)
#. SD card with at least 16 GB of memory

Software prerequisites
-------------------------------------------------------------------------------

#. SD card 16 GB imaged with :external+kuiper:doc:`Kuiper <index>`
   (check out that guide on how to do it, then come back here).
#. A UART terminal (PuTTY/Tera Term/Minicom), 115200 baud, 8N1.
#. :ref:`iio-oscilloscope` for data visualization.

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
