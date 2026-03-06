AD9208-DUAL-EBZ HDL reference design
====================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/ad9208_dual_ebz/index.html\


Functional Overview
-------------------

The AD9208-DUAL-EBZ reference design is a processor based (e.g. Microblaze) embedded system. The device interfaces to the FPGA transceivers followed by the individual JESD204B and ADC cores. The cores are programmable through an AXI-Lite interface. The samples are passed to the system memory (DDR).

.. admonition:: Download
   :class: download

   :git-hdl:`projects/ad9208_dual_ebz`


The reference design supports the following evaluation board:

=============================================== ===================
Hardware                                        Evaluation Document
=============================================== ===================
:adi:`DUAL-AD9208 <AD9208>` DUAL-AD9208
=============================================== ===================

Supported Carriers
------------------

-  `VCU118 <https://www.xilinx.com/VCU118>`__ FMC+ Slot

Building the HDL project
------------------------

General build instructions can be found here: :doc:`Building HDL </wiki-migration/resources/fpga/docs/build>`

Block Diagram
-------------

The data path and clock domains are depicted on the below diagram:


|image1|

The design has two JESD receive chains each having 8 lanes at rate of 15Gbps. The JESD receive chain consists of a physical layer represented by an XCVR module, a link layer represented by an RX JESD LINK module and transport layer represented by a RX JESD TPL module. The links operate in Subclass 1 by using the SYSREF signal to edge align the internal local multiframe clock and to release the received data in the same moment from all lanes. Therefore ensuring that data from all channels is synchronized at the application layer.

Both links are set for full bandwidth mode and operate with the following parameters:

-  Deframer paramaters: L=8, M=2, F=1, S=2, N’=16
-  GLBLCLK – 375MHz (Lane Rate/40)
-  REFCLK – 750MHz (Lane Rate/20)
-  SYSREF – 1.46MHz (DEVCLK/2048)
-  DEVCLK – 3000MHz
-  JESD204B Lane Rate – 15Gbps

Both transport layer components present on their output 256 bits at once on every clock cycle, representing 8 samples per converter. The two receive chains are merged together and transferred to the DDR with a single DMA. An ADC buffer is used to store 65k samples per converter in the fabric before transferring it with the DMA.

Clock sources
~~~~~~~~~~~~~

The clock sources are depicted on the below diagram:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208_dual_ebz/ad9208_vcu118_clocking.png
   :align: center

Both physical layer transceiver modules receive the same reference clock from the clock chip SCLKOUT8 output. The global clock (LaneRate/40) it is received directly from the clock chip SCLKOUT9 output.

More Information
----------------

-  :doc:`AD9208-DUAL-EBZ Virtex UltraScale+ VCU118 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9208_dual_ebz/quickstart/vcu118>`
-  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`
-  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`
-  :doc:`AD9208 ADC Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9208>`

Support
-------

Analog Devices will provide limited online support for anyone using the core with Analog Devices components (ADC, DAC, Video, Audio, etc) via the :ez:`EngineerZone <community/fpga>`.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208_dual_ebz/vcu118_ad9208_dual_ebz.png
