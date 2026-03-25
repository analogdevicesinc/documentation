Quick Start
===========

Zynq (ZC702, ZC706, ZedBoard)
------------------------------

Required Hardware
~~~~~~~~~~~~~~~~~

- :xilinx:`ZC702 <products/boards-and-kits/ek-z7-zc702-g.html>`,
  :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`, or
  `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
- AD-FMCOMMS1-EBZ FMC board
- SD card (16 GB or larger)
- USB keyboard and mouse
- HDMI display (monitor or TV)
- Antenna or SMA cable for Tx-to-Rx loopback

Setup
~~~~~

#. Write the :doc:`Kuiper Linux </linux/kuiper/index>` image to the SD card.
#. Connect the AD-FMCOMMS1-EBZ to the FMC connector on the carrier board.
#. Connect an HDMI display and USB keyboard/mouse.
#. Insert the SD card and power on the board.
#. The IIO Oscilloscope application launches automatically on the desktop after
   boot completes.

The IIO Oscilloscope can also be used remotely over the network by connecting
to the board's IP address from a host PC.

MicroBlaze (KC705, VC707)
-------------------------

Required Hardware
~~~~~~~~~~~~~~~~~

- :xilinx:`KC705 <products/boards-and-kits/ek-k7-kc705-g.html>` or
  :xilinx:`VC707 <products/boards-and-kits/ek-v7-vc707-g.html>`
- AD-FMCOMMS1-EBZ FMC board (use FMC LPC on KC705, FMC2 on VC707)
- Micro / Mini-USB cable for JTAG

Required Software
~~~~~~~~~~~~~~~~~

- Bitfile and Linux ELF image
- Xilinx XSCT console (or XMD for older ISE toolchains)
- A UART terminal (PuTTY / Tera Term / Minicom), baud rate 115200 (8N1)

Setup
~~~~~

#. Connect the AD-FMCOMMS1-EBZ to the appropriate FMC connector.
#. Connect USB JTAG (Micro USB) to your host PC.
#. Turn on the power switch on the FPGA board.
#. Open the XSCT console to configure the FPGA and download the ELF image.
#. After boot, connect to the :doc:`IIO Oscilloscope
   </software/iio-oscilloscope/index>` remotely from a network-enabled host
   PC using the board's IP address.

No-OS (Baremetal)
-----------------

A baremetal no-OS driver is available for quick hardware verification. Build
the HDL bitfile, then use the SDK sample program to generate the no-OS ELF
file. This provides basic device initialization and register-level access
without requiring a Linux boot.

.. note::

   This is a persistent file system. Always shut down properly from the
   terminal (``sudo shutdown -h now``) before disconnecting power, otherwise
   the SD card may be corrupted.
