.. _ad-fmcmotcon2-ebz:

AD-FMCMOTCON2-EBZ
==================

.. warning::

   The :adi:`AD-FMCMOTCON2-EBZ
   <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Eval-FMCMOTCON2.html#eb-overview>`
   board has been retired and is no longer available for sale. Support has been
   discontinued. The HDL project has been removed from the main branch but is
   still available in the
   :git-hdl:`hdl_2018_r2 <hdl_2018_r2:projects/motcon2_fmc>` release branch.

The :adi:`AD-FMCMOTCON2-EBZ
<en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Eval-FMCMOTCON2.html#eb-overview>`
is a complete motor drive system on an FMC board. It provides efficient and
high dynamic control of three phase PMSM, BLDC, induction, and stepper motors
up to 48 V and 20 A. Two motors can be driven at the same time, each motor
having its separate power supply.

.. image:: mc2_system.jpg
   :align: center
   :width: 500

Introduction
------------

The kit consists of two boards: a controller board and a drive board. The
system incorporates high quality power supplies, reliable power/control/
feedback signal isolation, accurate measurement of motor current and voltage
signals, high speed interfaces for control signals to allow fast controller
response, industrial Ethernet high speed interfaces, single ended Hall,
differential Hall, encoder and resolver interfaces, digital position sensors
interface, and flexible control with an FPGA/SoC interface.

The **AD-DYNO2-EBZ** dynamometer is provided as an extension of the drive
system. This is a dynamically adjustable load system that can be used to test
real-time motor control performance. It consists of two BLDC motors directly
coupled through a rigid connection. One BLDC motor acts as a load controlled
by the DYNO's embedded control system, while the second motor is driven by the
AD-FMCMOTCON2-EBZ. The load can also be driven by the AD-FMCMOTCON2-EBZ to
implement dynamic load profiles.

This platform is intended to be used as a prototyping system to verify the
hardware and the control algorithms before moving to the production stage.

The controller and drive boards are provided as a kit and cannot be purchased
separately. They are both distributed under the AD-FMCMOTCON2-EBZ part number.

Interfaces
~~~~~~~~~~

The controller board provides the following interfaces for dual motor control:

- 2x Gigabit Ethernet PHYs (RGMII mode) for industrial Ethernet
- 2x Hall sensor interfaces (single-ended and differential)
- 2x Encoder interfaces
- Digital position sensor interfaces (EnDat, BiSS)
- 6 high-speed ADC digital interfaces (data + clock)
- 18 isolated drive signals (dual H-bridge capable)
- 2 isolated GPOs + 2 isolated GPIs
- FMC signal voltage adaptation for all FMC voltage levels
- BEMF zero-cross detection for sensorless motor control
- Reverse voltage protection and integrated overcurrent protection

.. toctree::
   :hidden:

   hardware
   quickstart
   software
