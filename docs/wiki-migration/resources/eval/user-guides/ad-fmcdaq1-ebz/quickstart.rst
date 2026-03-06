AD-FMCDAQ1-EBZ Quick Start Guides
=================================

The Quick Start Guides provide a simple step by step instruction on how to do an initial system setup for the AD-FMCDAQ1-EBZ boards on various FPGA development boards. They will discuss how to program the bitstream, run a no-OS program or boot a Linux distribution.

Supported Carriers
------------------

The AD-FMCDAQ1-EBZ is, by definition a "FPGA mezzanine card" (FMC), that means it needs a carrier to plug into. The carriers we support are:

========================================== ==============
Board                                      AD-FMCDAQ2-EBZ
========================================== ==============
`KC705 <https://www.xilinx.com/KC705>`__   v
`KCU105 <https://www.xilinx.com/KCU105>`__ v
`VC707 <https://www.xilinx.com/VC707>`__   v
`ZC706 <https://www.xilinx.com/ZC706>`__   v
========================================== ==============

The supported OS are:

+--------------------------------------------+-----+----------------+----------------+
| Board                                      | HDL | Linux Software | No-OS Software |
+============================================+=====+================+================+
| `KC705 <https://www.xilinx.com/KC705>`__   | v   | v              | v              |
+--------------------------------------------+-----+----------------+----------------+
| `KCU105 <https://www.xilinx.com/KCU105>`__ | v   | v              | v              |
+--------------------------------------------+-----+----------------+----------------+
| `VC707 <https://www.xilinx.com/VC707>`__   | v   | v              | v              |
+--------------------------------------------+-----+----------------+----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`__   | v   | v              | v              |
+--------------------------------------------+-----+----------------+----------------+

Hardware Setup
--------------

In most carriers, the AD-FMCDAQ1-EBZ board connects to the HPC connector (unless otherwise noted). The carrier setup requires power, UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections. A typical setup is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq1-ebz/daq1_carrier.jpg
   :align: center
   :width: 800px
