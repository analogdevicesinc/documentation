.. _ad_fmcmotcon1_ebz chipscope_quickstart:

AD-FMCMOTCON1-EBZ ISE Project with Chipscope
===============================================================================

.. warning::

   The :adi:`AD-FMCMOTCON1-EBZ` is a **legacy product** and is no longer
   actively supported. This documentation is provided for reference only.

This guide provides some quick instructions on how to setup the
AD-FMCMOTCON1-EBZ on either:

-  `ZED Board <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`_

Software Tools
-------------------------------------------------------------------------------

-  Xilinx ISE 14.6
-  Xilinx Chipscope Pro 14.6

System Setup
-------------------------------------------------------------------------------

To setup the hardware follow the steps described in the
:ref:`Linux on Zynq Quick Start Guide <ad_fmcmotcon1_ebz zedboard_quickstart>`.

The FPGA must be programmed with the **top.bit** bitstream that results after
compiling the ISE project. This has already been done; the bitstream was
generated and can be found in the ISE project's folder. To program the FPGA
use the **iMPACT** tool from Xilinx.

Chipscope Interface
-------------------------------------------------------------------------------

The user interface uses Xilinx Chipscope 14.6. In order to be able to see the plots from sections
C and D, the triggers from UNIT:1 and UNIT:2 must be enabled.

.. figure:: ../images/chipscope.jpg
   :alt: Chipscope user interface
   :align: center
   :width: 800

   Chipscope user interface

**Section A** is used for control.

.. list-table:: Table 1: Section A parameter description
   :header-rows: 1
   :widths: 20 10 70

   * - Name
     - Width
     - Description
   * - PWM
     - 32
     - PWM value for controlling the motor. Must be larger than 0x480 and
       less than 0x800.
   * - GAIN
     - 2
     - Amplification on the ADC signal chain: 0 = Gain 1, 1 = Gain 4,
       2 = Gain 2, 3 = Gain 8.
   * - RUN_MOTOR
     - 1
     - Start / Stop the motor.
   * - STAR_MOTOR
     - 1
     - Set to 1 for star-wired motors, set to 0 for delta-wired motors.
   * - CW_DIR
     - 1
     - Set to 1 for clockwise rotation, set to 0 for counter-clockwise.

**Section B** is used for checking the waveform for the currents in the
design.

.. list-table:: Table 2: Section B parameter description
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Description
   * - IA_DRV
     - IA current as read on the low voltage motor driver board
   * - IB_DRV
     - IB current as read on the low voltage motor driver board
   * - IT_DRV
     - IT current as read on the low voltage motor driver board
   * - IA
     - IA current as read on the controller board
   * - IB
     - IB current as read on the controller board
   * - IT
     - IT current as read on the controller board
   * - VBUS
     - VBUS voltage as seen on the controller board
   * - SPEED
     - Time between a change of the HALL sensors state, measured in 100 ns
       units
   * - POSITION
     - HALL sensors reading

**Section C** is used to represent graphically the speed of the motor.

.. list-table:: Table 3: Section C parameter description
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Description
   * - SPEED
     - Time between a change of the HALL sensors state, measured in 100 ns
       units

**Section D** is used to plot the currents and voltages described in
section B.
