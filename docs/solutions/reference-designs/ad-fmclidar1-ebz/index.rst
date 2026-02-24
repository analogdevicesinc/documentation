.. _ad-fmclidar1-ebz:

AD-FMCLIDAR1-EBZ
=================

.. warning::

   Support for the AD-FMCLIDAR1-EBZ is discontinued on all supported carriers
   (Arria 10 SoC, ZC706, ZCU102) and it will not be supported in future
   releases. The last release with pre-built files is **2021_r1**. Check the
   :doc:`Kuiper Linux </linux/kuiper/index>` page for all releases.
   The HDL project source code can still be found on the
   :git-hdl:`hdl_2021_r1 <hdl_2021_r1:projects/ad_fmclidar1_ebz>` release
   branch.

The :adi:`AD-FMCLIDAR1-EBZ
<en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-FMCLIDAR1-EBZ.html>`
is a prototyping platform for LiDAR applications that can be used on FPGA
development boards enabled with FMC HPC connector and JESD204B support
capability. It offers developers a working-out-of-box platform that can be
used for developing software and algorithms for a broad range of applications.

.. image:: lidar_system.jpg
   :align: center
   :width: 500

Introduction
------------

The full system hardware includes:

- Data Acquisition (DAQ) Board
- Laser Transmitter Board
- AFE Receiver Board

Features
~~~~~~~~

- 1D non-scanning LiDAR
- Horizontal resolution 16 pixels
- Data sampling up to 1 GSPS on 4 separate channels
- Design is verified to comply with Class I Laser Safety
- Standardized FMC connector plugs into FPGA board of choice
- Out of box demo for target range measurement
- Complete open source software framework
- Licensable JESD204B interface framework for deterministic data delivery
  to host
- Wrappers for MATLAB, Python
- LiDAR specific API for system control and data acquisition
- Platform development environment support includes Industry standard Linux
  Industrial I/O (IIO) applications, MATLAB, Simulink, custom C/C++, Python,
  and C# applications
- HDL reference designs and drivers to allow zero day development

.. image:: highlevel_blk_dig.png
   :align: center
   :width: 500

.. toctree::
   :hidden:

   hardware
   quickstart
   software
