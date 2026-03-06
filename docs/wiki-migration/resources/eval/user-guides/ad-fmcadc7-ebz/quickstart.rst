AD-FMCADC7-EBZ Quick Start Guides
=================================

.. important::

   This project is obsolete, and is no longer supported. The source code can be found in the last release where it was present, hdl_2021_r2 for both HDL and software support.


The Quick Start Guides provide simple step by step instructions on how to do an initial system setup for the AD-FMCADC7-EBZ boards on supported carriers.

Supported Carriers
------------------

======================================== ==============
Board                                    AD-FMCADC7-EBZ
======================================== ==============
`ZC706 <https://www.xilinx.com/ZC706>`__ v
======================================== ==============

Hardware Setup
--------------

In most carriers, the AD-FMCADC7-EBZ board connects to the HPC connector (unless otherwise noted). The carrier setup requires power, UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections. The Zynq carriers program the FPGA and boots Linux from the SD card. The fabric only carriers use XMD to program the FPGA and download the Linux image. Please follow the specific switch settings for Linux or JTAG (no-OS) mode of your carrier of choice.

Linux Quick Start Guide
-----------------------

All you need to do is build SD card or download the SD card image of the latest releases. The instructions are :doc:`here </wiki-migration/resources/tools-software/linux-software/zynq_images>`.
