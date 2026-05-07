.. _adv7513 prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The `DE10-Nano <https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/terasic-de10-nano-kit.html>`__
   evaluation board (the :adi:`ADV7513` HDMI transmitter is integrated on-board)
#. An HDMI monitor with a spare HDMI input
#. An HDMI cable
#. A way to interact with the board:

   - USB cable for UART (115200 baud, 8N1)

#. Power supply for the board
#. A MicroSD card (4 GB or larger) and an SD card reader

Software prerequisites
-------------------------------------------------------------------------------

#. :external+kuiper:doc:`Kuiper Linux <index>` SD card image
#. Intel Quartus Prime (to generate an updated bitstream if needed)

   .. note::

      Pre-built bitstreams for the DE10-Nano are included in the Kuiper Linux
      release. You only need Quartus Prime if you are modifying the HDL design.

#. The :adi:`ADV7513` Linux driver is part of the upstream kernel and ADI
   Kuiper Linux image. It is loaded via the ``adv7511`` module with the
   ``"adi,adv7513"`` compatible string in the device tree.

