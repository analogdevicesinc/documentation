ADRV9001/2 Quick Start Guides
=============================

The Quick Start Guides provide a simple step by step instruction on how to do an initial system setup for the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` and :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` boards on various FPGA development boards. They will discuss how to program the bitstream, run a no-OS program or boot a Linux distribution.

Supported Carriers
------------------

The :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` and :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` is, by definition a "FPGA mezzanine card" (FMC), that means it needs a carrier to plug into. The carriers we support are:

+----------------------------------------------------------------------------------------------------------------------+-------------------------------------+--------------------+
| Board                                                                                                                | ADRV9002NP                          |                    |
+======================================================================================================================+=====================================+====================+
|                                                                                                                      | **CMOS inteface**                   | **LVDS interface** |
+----------------------------------------------------------------------------------------------------------------------+-------------------------------------+--------------------+
| `ZCU102 <https://www.xilinx.com/ZCU102>`_                                                                            | √                                   | √                  |
+----------------------------------------------------------------------------------------------------------------------+-------------------------------------+--------------------+
| `ZC706 <https://www.xilinx.com/ZC706>`_                                                                              | √ **<fc #ff0000>VADJ 1.8V</fc>**\ ¹ | N/A²               |
+----------------------------------------------------------------------------------------------------------------------+-------------------------------------+--------------------+
| `Zed Board <http://zedboard.org/product/zedboard>`_                                                                  | √ **<fc #ff0000>VADJ 1.8V</fc>**    | N/A²               |
+----------------------------------------------------------------------------------------------------------------------+-------------------------------------+--------------------+
| `Arria 10 SoC <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_  | √                                   | N/A³               |
+----------------------------------------------------------------------------------------------------------------------+-------------------------------------+--------------------+

| ¹ Instruction for reprogramming the VADJ can be found `here <https://www.xilinx.com/Attachment/ZC706_Power_Controllers_Reprogramming_Steps.pdf>`_ and `here <https://forums.xilinx.com/t5/Xilinx-Evaluation-Boards/ZC706-Doesn-t-work-with-VADJ-at-1-8v/td-p/430086>`_
| ² See :doc:`Cmos only operation </wiki-migration/resources/eval/user-guides/adrv9002/quickstart>` section
| ³ Not supported due sub-optimal mapping of the clock pins from the source synchronous interfaces.

CMOS only operation
-------------------

On the ZC706 / ZedBoard platforms the FMC connectors map to HR IO banks. The HR banks have a limitation that when using LVDS I/O standard you must set the bank VCCO voltage to 2.5V, however the ADRV9001 evaluation board is using IO supplies of 1.8V and does not have level shifters for the single ended lines. Therefore the VCCO of the banks must be set to 1.8 V (VADJ) and limiting the operation to CMOS mode only. More information on the limitation see `7 Series Select IO guide <https://www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`_ section 'LVDS and LVDS_25' and Table 1-43

Supported Environments
----------------------

The supported OS are:

+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+--------------------------+
| Board                                                                                                                | HDL | Linux Software | No-OS Software | Required Minimum Release |
+======================================================================================================================+=====+================+================+==========================+
| `ZCU102 <https://www.xilinx.com/ZCU102>`_                                                                            | √   | √              | √              | 2019-R2                  |
+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+--------------------------+
| `ZC706 <https://www.xilinx.com/ZC706>`_                                                                              | √   | √              | √              | 2020-R1                  |
+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+--------------------------+
| `Zed Board <http://zedboard.org/product/zedboard>`_                                                                  | √   | √              | √              | 2019-R2                  |
+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+--------------------------+
| `Arria 10 SoC <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_  | √   | √              | N/A            | 2020-R1                  |
+----------------------------------------------------------------------------------------------------------------------+-----+----------------+----------------+--------------------------+

Hardware Setup
--------------

In most carriers, the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` and :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` boards connects to the HPC1 connector (unless otherwise noted). The carrier setup requires power, UART (115200), ethernet (Linux), DisplayPort or HDMI (if available) and/or JTAG (no-OS) connections. A few typical setups are shown below.

Identify your hardware
~~~~~~~~~~~~~~~~~~~~~~

Evaluation boards were equipped with different silicon revisions. All boards built since the middle of December 2020 have C0 silicon, older ones use B0 silicon these are no longer shipped. You can identify the board you have based on its label.

======== ================
Label    Silicon Revision
======== ================
|image1| **B0**
|image2| **B0**
|image3| **C0**
|image4| **C0**
======== ================

.. tip::

   Each revision of silicon requires its corresponding software support files in the later steps.


ZCU102 + ADRV9002NP
-------------------

:doc:`ADRV9002 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/zynqmp>`

ZC706 + ADRV9002NP
------------------

:doc:`ADRV9002 Zynq SoC ZC706 Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/zynq>`

Zed Board + ADRV9002NP
----------------------

:doc:`ADRV9002 Zynq Zed Board Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/zed>`

============

.. include:: common.rst .. include:: common.rst

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/adrv9002_b0_np_w1.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/adrv9002_b0_np_w2.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/adrv9002xbcz_c0_np_w1.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/adrv9002xbcz_c0_np_w2.png
