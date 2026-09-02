.. _ad-fmclidar1-ebz:

AD-FMCLIDAR1-EBZ (Obsolete)
================================================================================

Prototyping platform for LiDAR applications with FMC HPC connector and
JESD204B support.

.. warning::

   Support for the ad_fmclidar_ebz is discontinued on all supported carriers:
   Arria10 SOC, zc706 and zcu102. ad_fmclidar_ebz will not be supported in
   future releases, last release in which pre-build files can be found is
   2021_r1. Check the
   :external+kuiper:doc:`Kuiper <index>`
   to see all available Kuiper Linux releases.

Overview
--------------------------------------------------------------------------------

The :adi:`AD-FMCLIDAR1-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-FMCLIDAR1-EBZ.html>`
is a prototyping platform for LiDAR applications that can be used on FPGA
development boards enabled with FMC HPC connector and JESD204B support
capability. It offers developers a working-out-of-box platform that can be
used for developing software and algorithms for a broad range of applications.

The full system hardware includes:

- Data Acquisition (DAQ) Board
- Laser Transmitter Board
- AFE Receiver Board

Features:

- 1D Non-Scanning LiDAR
- Horizontal resolution 16 pixels
- Data sampling up to 1GSPS on 4 separate Channels
- Design is verified to comply with Class I Laser Safety
- Standardised FMC connector plugs into FPGA board of choice
- Out of box demo for target range measurement
- Complete open source software framework
- Licensable JESD204B interface framework for deterministic data delivery
  to host
- Wrappers for Matlab, Python
- LiDAR specific API for system control & data acquisition
- Platform development environment support includes Industry standard Linux
  Industrial I/O (IIO) Applications, MATLAB, Simulink, custom C/C+, Python,
  and C# applications
- HDL reference designs and drivers to allow zero day development

Applications:

- LiDAR range finding and distance measurement
- Object detection and 3D mapping
- Autonomous vehicle prototyping

.. figure:: images/lidar_system_1.jpg
   :width: 500

   AD-FMCLIDAR1-EBZ

.. toctree::
   :hidden:

   ad-fmclidar1-ebz
   hardware_daq
   hardware_laser
   hardware_afe
   system_evaluation

Table of contents
--------------------------------------------------------------------------------

#. :doc:`User guide <ad-fmclidar1-ebz>`
#. :doc:`DAQ Board Hardware <hardware_daq>`
#. :doc:`Laser Board Hardware <hardware_laser>`
#. :doc:`AFE Board Hardware <hardware_afe>`
#. :doc:`System evaluation <system_evaluation>`
#. :external+hdl:doc:`HDL Reference Design <projects/ad_fmclidar1_ebz/index>`

Help and support
--------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on the
:ez:`/` technical support community, but before that, please make
sure you read our documentation thoroughly.

.. esd-warning::
