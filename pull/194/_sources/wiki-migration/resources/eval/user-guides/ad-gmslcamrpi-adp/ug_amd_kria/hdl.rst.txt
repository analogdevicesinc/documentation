GMSL HDL Reference Design
=========================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/ad_gmsl2eth_sl/index.html\


A brief introduction of the acronyms that are going to be used:

-  MIPI- Mobile Industry Processor Interface
-  MIPI CSI-2 - MIPI's camera serial interface specification
-  GMSL - Gigabit Multimedia Serial Link
-  VC - Virtual channel

Introduction
------------

Used devices
~~~~~~~~~~~~

-  :adi:`MAX96724`
-  :adi:`AD-GMSLCAMRPI-ADP# <design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-GMSLCAMRPI-ADP.html>`

Supported FPGA carrier
~~~~~~~~~~~~~~~~~~~~~~

-  `AMD/XILINX KV260 <https://www.xilinx.com/products/som/kria/kv260-vision-starter-kit.html>`_

Reference HDL Design
--------------------

The design is built upon ADI's generic HDL reference design framework. Thus, this reference design is used to interface the GMSL technology by using the MIPI CSI-2 `specification <https://www.mipi.org/specifications/csi-2>`_ for high-speed data transmission, and I2C standard for control. An in-depth presentation and instructions about the HDL design framework in general, can be found in the :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`.

Block Design
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/ug_amd_kria/gmsl_hdl_block_design1.png
   :align: center

The architecture of this reference design is composed of multiple Xilinx's multimedia IPs that have the following roles:

-  AMD-Xilinx's MIPI CSI-2 Rx Subsystem IP (receive video data from the GMSL deserializer's PHY using the 2-lane 15-pin connector);
-  AMD-Xilinx's AXIS Switch IP (handle MIPI's virtual-channel option by redirecting each virtual channel to corresponding Video Framebuffer Write instance);
-  AMD-Xilinx's Video Framebuffer Write IP (video-specific DMA engine);

Using the HDL reference design
------------------------------

In order to build the HDL design the user has to go through the following steps:

-  Confirm that you have the right tools (see :git-hdl:`Release notes <releases>`)
-  Clone the HDL GitHub repository (see :doc:`/wiki-migration/resources/fpga/docs/git`)
-  Choose the required interface (see caption **Switching between interface types**)
-  Build the project (see :doc:`/wiki-migration/resources/fpga/docs/build`)

As regards the design's IPs, this GMSL-based reference design contains multiple AMD-Xilinx-related multimedia IPs such as MIPI CSI-2 Rx Subsystem, Axi-Stream Switch, Axi-Stream Subset Converter and Video Framebuffer Write, all these ones being available free of charge using standard AMD-Xilinx's Vivado version.

AXI4-LITE control interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

====================== ===========
Instance               Address
====================== ===========
mipi_csi2_rx_subsyst_0 0x84A0 0000
axi_iic_mipi           0x84A2 0000
v_frmbuf_wr_0          0x84A4 0000
v_frmbuf_wr_1          0x84A6 0000
v_frmbuf_wr_2          0x84A8 0000
v_frmbuf_wr_3          0x84AA 0000
====================== ===========

PL Interrupts
~~~~~~~~~~~~~

====================================== ============= ===================
Instance                               HDL interrupt Linux PsU interrupt
====================================== ============= ===================
---                                    0             89
---                                    1             90
---                                    2             91
---                                    3             92
---                                    4             93
---                                    5             94
---                                    6             95
---                                    7             96
v_frmbuf_wr_3/interrupt                8             104
v_frmbuf_wr_2/interrupt                9             105
v_frmbuf_wr_1/interrupt                10            106
v_frmbuf_wr_0/interrupt                11            107
axi_iic_mipi/iic2intc_irpt             12            108
mipi_csi2_rx_subsyst_0/csirxss_csi_irq 13            109
---                                    14            110
---                                    15            111
====================================== ============= ===================

GPIO signals
~~~~~~~~~~~~

Ps8 EMIO offset = 78

================ ==== ==============
GPIO Signal      GPIO HDL GPIO EMIOn
================ ==== ==============
fan_en_b         78   0
csirxss_rstn     79   1
ap_rstn_frmbuf_0 80   2
ap_rstn_frmbuf_1 90   3
ap_rstn_frmbuf_2 91   4
ap_rstn_frmbuf_3 92   5
================ ==== ==============

HDL Project
-----------

-


|MAX96724 HDL Project.|

User Guide
----------

-


|Project's User Guide.|

Support
-------

.. hint::

   **Questions?** Feel free to ask your questions in EngineerZone support forums.

   
   -  :ez:`FPGA Reference Design <community/fpga>`
   -  :ez:`Linux Drivers <community/linux-software-drivers>`.
   


.. |MAX96724 HDL Project.| image:: https://wiki.analog.com/_media/:git-hdl:`projects/max96724/kv260`
.. |Project's User Guide.| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/ug_amd_kria
