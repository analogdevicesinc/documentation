.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcmotcon1-ebz

.. _ad-fmcmotcon1-ebz:

AD-FMCMOTCON1-EBZ
==================

.. warning::

   The :adi:`AD-FMCMOTCON1-EBZ` board has been retired and is no longer
   available for sale. Support has been discontinued. The HDL project has been
   removed from the main branch but is still available in the
   :git-hdl:`hdl_2014_r1 <hdl_2014_r1:projects/motor_control>` release branch.

The :adi:`AD-FMCMOTCON1-EBZ` is a complete motor drive system on an FMC board.
It provides a complete motor drive system demonstrating efficient control of
Brushed DC, BLDC, PMSM, and Stepper motors. The system incorporates high
quality power sources, reliable power/control/feedback signal isolation,
accurate measurement of motor current and voltage signals, high speed
interfaces for control signals to allow fast controller response, and flexible
control with FPGA/SoC interface.

.. image:: mc_system.jpg
   :align: center
   :width: 500

Introduction
------------

The ADI FMC motor drive solution consists of the following products:

- **AD-FMCMOTCON1-EBZ** - Controller board. Compatible with all Xilinx
  FPGA platforms with FMC LPC or HPC connectors.
- **AD-DRVLV1-EBZ** - Low voltage drive board. Connects to the controller
  board and has a power stage that can drive Brushed DC / BLDC / PMSM /
  Stepper motors up to 48 V and 18 A.
- **AD-DYNO1-EBZ** - Dynamometer drive system. Acts as an electronically
  adjustable load with two BLDC motors connected in a dyno setup.

The **AD-DYNO1-EBZ** dynamometer consists of two BLDC motors directly coupled
through a rigid connection. One BLDC motor acts as a load controlled by the
DYNO's embedded control system, while the second motor is driven by the
AD-FMCMOTCON1-EBZ.

This platform is intended to be used as a prototyping system to verify the
hardware and the control algorithms before moving to the production stage.
Example reference designs showing how to use the control solution with Xilinx
FPGAs or SoCs and Simulink from MathWorks are provided together with the
hardware.

Features
~~~~~~~~

- Provide an efficient drive system for different types of electric motors
- Address power and isolation challenges encountered in motor control
  applications
- Provide accurate measurement of motor feedback signals
- Achieve flexible control with FPGA/SoC interface
- High speed industrial Ethernet interface
- Example reference designs for Xilinx FPGAs and Simulink from MathWorks

Added Value
~~~~~~~~~~~

- Complete control solution showing how to integrate hardware for power,
  isolation, measurement, and control
- Increased control flexibility due to FPGA interfacing capabilities
- Increased versatility to control different types of motors
- Example reference designs showing how to use the control solution with
  Xilinx FPGAs and Simulink from MathWorks

.. toctree::
   :hidden:

   hardware
   quickstart
   reference_hdl
   software
