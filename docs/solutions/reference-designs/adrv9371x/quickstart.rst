ADRV9371/PCBZ Quick Start Guides
================================

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the ADRV9371-N/PCBZ, ADRV9371-W/PCBZ boards on various
FPGA development boards. They will discuss how to program the bitstream, run a
no-OS program or boot a Linux distribution.

Supported Carriers
------------------

The ADRV9371/PCBZ is, by definition a "FPGA mezzanine card" (FMC), that means it
needs a carrier to plug into. The carriers we support are:

+----------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+-----------------+
| Board                                                                                                                | ADRV9371-N/PCBZ | ADRV9371-W/PCBZ | ADRV9375-N/PCBZ |
+======================================================================================================================+=================+=================+=================+
| `ZCU102 <https://www.xilinx.com/ZCU102>`_                                                                            | √               | √               | √               |
+----------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+-----------------+
| `KCU105 <https://www.xilinx.com/KCU105>`_                                                                            | √               | √               | √               |
+----------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+-----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`_                                                                              | √               | √               | √               |
+----------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+-----------------+
| `Arria 10 SoC <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_  | √               | √               | √               |
+----------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+-----------------+
| `Arria 10 GX <https://www.altera.com/products/boards_and_kits/dev-kits/altera/kit-a10-gx-fpga.html>`_                | √               | √               | √               |
+----------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+-----------------+

Supported Environments
----------------------

The supported OS are:

+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+
| Board                                                                                                                | HDL | Linux Software | No-OS Software |
+======================================================================================================================+=====+================+================+
| `ZCU102 <https://www.xilinx.com/ZCU102>`_                                                                            | √   | √              | √              |
+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+
| `KCU105 <https://www.xilinx.com/KCU105>`_                                                                            | √   | √              | √              |
+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`_                                                                              | √   | √              | √              |
+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+
| `Arria 10 SoC <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_  | √   | √              |                |
+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+
| `Arria 10 GX <https://www.altera.com/products/boards_and_kits/dev-kits/altera/kit-a10-gx-fpga.html>`_                | √   | √              | √              |
+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+

Hardware Setup
--------------

In most carriers, the ADRV9371/PCBZ board connects to the HPC connector (unless
otherwise noted). The carrier setup requires power, UART (115200), ethernet
(Linux), HDMI (if available) and/or JTAG (no-OS) connections. A few typical
setups are shown below.

ZC706 + ADRV9371/PCBZ
~~~~~~~~~~~~~~~~~~~~~

.. image:: images/mykonos_system_overview.png
   :align: center
   :width: 800

ZCU102 + ADRV9371/PCBZ
~~~~~~~~~~~~~~~~~~~~~~

Connect ADRV9371 into HPC0 on your ZCU102.

Unboxing guide
~~~~~~~~~~~~~~

:ez:`Detailed unboxing guide <cfs-file/__key/communityserver-discussions-components-files/703/AD9371-and-ADRV9009-setup-with-ZCU102-or-ZC706-April2019.pdf>`
