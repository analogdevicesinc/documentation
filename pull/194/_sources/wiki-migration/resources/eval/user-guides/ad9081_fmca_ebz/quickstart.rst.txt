AD9081/AD9082 Quick Start Guides
================================

The Quick Start Guides provide a simple step by step instruction on how to do an initial system setup for the :adi:`AD9081-FMCA-EBZ` and :adi:`AD9082-FMCA-EBZ` boards on various FPGA development boards. They will discuss how to program the bitstream, run a no-OS program or boot a Linux distribution.

Supported Carriers
------------------

The :adi:`AD9081-FMCA-EBZ` and :adi:`AD9082-FMCA-EBZ` is, by definition a "FPGA mezzanine card" (FMC), that means it needs a carrier to plug into. The carriers we support are:

+--------------------------------------------+-----------------+-----------------+
| Board                                      | AD9081-FMCA-EBZ | AD9082-FMCA-EBZ |
+============================================+=================+=================+
| `ZCU102 <https://www.xilinx.com/ZCU102>`_  | √               | √               |
+--------------------------------------------+-----------------+-----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`_    | √               | √               |
+--------------------------------------------+-----------------+-----------------+
| `VCU118 <https://www.xilinx.com/VCU118>`_  | √               | √               |
+--------------------------------------------+-----------------+-----------------+
| `VCU128 <https://www.xilinx.com/VCU128>`_  | √               | √               |
+--------------------------------------------+-----------------+-----------------+
| `VCK190 <https://www.xilinx.com/VCK190>`_  | √               | √               |
+--------------------------------------------+-----------------+-----------------+
| `A10Soc <https://www.intel.com/A10Soc>`_   | √               | √               |
+--------------------------------------------+-----------------+-----------------+

Supported Environments
----------------------

The supported OS are:

+--------------------------------------------+-----+----------------+----------------+
| Board                                      | HDL | Linux Software | No-OS Software |
+============================================+=====+================+================+
| `ZCU102 <https://www.xilinx.com/ZCU102>`_  | √   | √              | √              |
+--------------------------------------------+-----+----------------+----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`_    | √   | √              | √              |
+--------------------------------------------+-----+----------------+----------------+
| `VCU118 <https://www.xilinx.com/VCU118>`_  | √   | √              | √              |
+--------------------------------------------+-----+----------------+----------------+

Quick Start Guides
------------------

ZC706 + AD9081-FMCA-EBZ
~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Zynq-7000 SoC ZC706 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynq>`

ZCU102 + AD9081-FMCA-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD9081 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp>`

VCU118 + AD9081-FMCA-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Virtex UltraScale+ VCU118 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/microblaze>`

VCK190 + AD9081-FMCA-EBZ/AD9082-FMCA-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Versal ACAP VCK190 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/versal>`

A10SoC + AD9081-FMCA-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Arria10 SoC Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081/quickstart/a10soc>`

Hardware Setup
--------------

In most carriers, the :adi:`AD9081-FMCA-EBZ` board connects to the HPC0 connector (unless otherwise noted). The carrier setup requires power, UART (115200), ethernet (Linux), DisplayPort or HDMI (if available) and/or JTAG (no-OS) connections. A few typical setups are shown below.

.. include:: ad9081_fmca_ebz_hdl.rst

HDL Reference Design
--------------------

-  :doc:`AD9081-FMCA-EBZ (Single MxFE) HDL Reference Design </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_fmca_ebz_hdl>`

Software support
----------------

-  :doc:`AD9081 Linux Driver Support </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

.. include:: common.rst .. include:: common.rst
