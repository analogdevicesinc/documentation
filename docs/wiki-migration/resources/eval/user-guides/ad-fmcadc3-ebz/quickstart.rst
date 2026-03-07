AD-FMCADC3-EBZ Quick Start Guides
=================================

The Quick Start Guides provide a simple step by step instruction on how to do an initial system setup for the AD-FMCADC3-EBZ boards on various FPGA development boards. They will discuss how to program the bitstream, run a no-OS program or boot a Linux distribution.

Supported Carriers
------------------

The AD-FMCADC3-EBZ is, by definition a "FPGA mezzanine card" (FMC), that means it needs a carrier to plug into. The carriers we support are:

======================================== ==============
Board                                    AD-FMCADC3-EBZ
======================================== ==============
`VC707 <https://www.xilinx.com/VC707>`_ v
`ZC706 <https://www.xilinx.com/ZC706>`_ v
======================================== ==============

The supported OS are:

+------------------------------------------+-----+----------------+----------------+
| Board                                    | HDL | Linux Software | No-OS Software |
+==========================================+=====+================+================+
| `VC707 <https://www.xilinx.com/VC707>`_  | v   | v              | -              |
+------------------------------------------+-----+----------------+----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`_  | v   | v              | -              |
+------------------------------------------+-----+----------------+----------------+

Hardware Setup
--------------

In most carriers, the AD-FMCADC3-EBZ board connects to the HPC connector (unless otherwise noted). The carrier setup requires power, UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections. A typical setup is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc3-ebz/software/linux/ad-fmcadc3-ebz_zc706.png
   :align: center
   :width: 800px
