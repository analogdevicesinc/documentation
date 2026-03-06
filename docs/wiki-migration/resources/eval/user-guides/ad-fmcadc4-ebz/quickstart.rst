AD-FMCADC4-EBZ Quick Start Guides
=================================

The Quick Start Guides provide a simple step by step instructions on how to do an initial system setup for the AD-FMCADC4-EBZ boards on various FPGA development boards. They will discuss how to program the bitstream, run a no-OS program or boot a Linux distribution.

Supported Carriers
------------------

The AD-FMCADC4-EBZ is, by definition a "FPGA mezzanine card" (FMC), that means it needs a carrier to plug into. The carriers we support are:

======================================== ==============
Board                                    AD-FMCADC4-EBZ
======================================== ==============
`ZC706 <https://www.xilinx.com/ZC706>`__ √
======================================== ==============

The supported OS are:

+------------------------------------------+-----+----------------+----------------+
| Board                                    | HDL | Linux Software | No-OS Software |
+==========================================+=====+================+================+
| `ZC706 <https://www.xilinx.com/ZC706>`__ | √   | √              | -              |
+------------------------------------------+-----+----------------+----------------+

Hardware Setup
--------------

In most carriers, the AD-FMCADC4-EBZ board connects to the HPC connector (unless otherwise noted). The carrier setup requires power, UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections. A typical setup is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc4-ebz/software/linux/ad-fmcadc4-ebz_zc706.png
   :align: center
   :width: 800px
