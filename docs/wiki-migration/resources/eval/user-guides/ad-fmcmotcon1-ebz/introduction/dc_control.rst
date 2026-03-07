Brushed DC Motor Control
========================

The Brushed DC motor is the simplest type of motor to control, all that needs to be done is to vary the supply voltage and the motor's speed will vary proportional to the voltage. The most common technique used to vary the applied voltage is called **Pulse Width Modulation (PWM)**, where constant amplitude voltage pulses of varying widths are provided to the motor - the wider the pulse, the more energy transferred to the motor. The frequency of the pulses is high enough that the motor’s inductance averages them, and it runs smooth.

A single transistor and diode can control the speed of a dc motor.

-  The motor speed (voltage) is proportional to the transistor ON duty cycle.
-  Positive torque only—passive braking.

An H-bridge power circuit enables four quadrant control

-  Forward and reverse motion and braking
-  Complementary PWM signals applied to the high and low side switches in the bridge

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/introduction/dc_control.png
   :width: 400px

.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#drives
   :alt: Electric Motor Drives#..:\|Overview#bldc_control|Brushless DC Motor Control
