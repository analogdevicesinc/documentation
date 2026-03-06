AD-FMCDAQ3-EBZ Quick Start Guides
=================================

The Quick Start Guides provide a simple step by step instruction on how to do an initial system setup for the AD-FMCDAQ3-EBZ boards on various FPGA development boards. They will discuss how to program the bitstream, run a no-OS program or boot a Linux distribution.

Supported Carriers
------------------

The AD-FMCDAQ3-EBZ is, by definition a "FPGA mezzanine card" (FMC), that means it needs a carrier to plug into. The carriers we support are:

+------------------------------------------------------------------------+----------------+
| Board                                                                  | AD-FMCDAQ3-EBZ |
+========================================================================+================+
| `A10GX <https://www.intel.com/content/www/us/en/programmable/A10GX>`__ | v              |
+------------------------------------------------------------------------+----------------+
| `KCU105 <https://www.xilinx.com/KCU105>`__                             | v              |
+------------------------------------------------------------------------+----------------+
| `VCU118 <https://www.xilinx.com/VCU118>`__                             | v              |
+------------------------------------------------------------------------+----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`__                               | v              |
+------------------------------------------------------------------------+----------------+
| `ZCU102 <https://www.xilinx.com/ZCU102>`__                             | v              |
+------------------------------------------------------------------------+----------------+

The supported OS are:

+------------------------------------------------------------------------+----------------+----------------+
| Board                                                                  | Linux Software | No-OS Software |
+========================================================================+================+================+
| `A10GX <https://www.intel.com/content/www/us/en/programmable/A10GX>`__ | v              | v              |
+------------------------------------------------------------------------+----------------+----------------+
| `KCU105 <https://www.xilinx.com/KCU105>`__                             | v              | v              |
+------------------------------------------------------------------------+----------------+----------------+
| `VCU118 <https://www.xilinx.com/VCU118>`__                             | v              | v              |
+------------------------------------------------------------------------+----------------+----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`__                               | v              | v              |
+------------------------------------------------------------------------+----------------+----------------+
| `ZCU102 <https://www.xilinx.com/ZCU102>`__                             | v              | v              |
+------------------------------------------------------------------------+----------------+----------------+

-  :doc:`Arria 10 GX Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart/a10gx>`
-  :doc:`Kintex UltraScale KCU105 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart/kcu105>`
-  :doc:`Virtex UltraScale+ VCU118 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart/vcu118>`
-  :doc:`Zynq UltraScale ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart/zcu102>`
-  :doc:`Zynq ZC706 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart/zynq>`

Hardware Setup
--------------

In most carriers, the AD-FMCDAQ3-EBZ board connects to the HPC connector (unless otherwise noted). The carrier setup requires power, UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections. A typical setup is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq3-ebz/hardware/daq3_zc706_setup.jpg
   :align: center
   :width: 600px
