AD654 LED Flasher Lab
=====================

.. image:: https://wiki.analog.com/_media/analogTV>4800534505001
   :alt: analogTV>4800534505001
   :align: right

Introduction
------------

The AD654 is a voltage-to-frequency converter that is often used to convert sensor-derived information in voltage form, such as the voltage obtained from a temperature sensor, into frequency, in order to reliably transmit the information from one point to another. In many situations, frequency transmission is more robust than simple voltage transmission. In this experiment we construct a simple circuit to flash a LED at a frequency that depends on the voltage applied to the AD654.

Objective
---------

To build a simple LED flashing circuit using one IC and a few external components. To show a simple negative feedback amplifier, and show how to compensate for input bias currents. Following completion of this lab you should be able to describe the basic operation of the AD654 and its major application, explain what bias currents are and how to compensate for them, and describe the basic behavior of the two inputs of an op-amp that is connected in a negative feedback configuration.

Materials and Apparatus
-----------------------

-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (1) AD654 from the ADALP2000 Analog Parts Kit
-  (2) 5 MΩ resistors from the ADALP2000 Analog Parts Kit
-  (1) 100 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 10 KΩ potentiometer from the ADALP2000 Analog Parts Kit
-  (1) 0.1 μF capacitor from the ADALP2000 Analog Parts Kit
-  (1) Red LED from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Construct the circuit shown in the schematic below on the solderless breadboard; note that the +5 V power is to be supplied by the M1K\


|lab_3_image_1.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_3_assembly_image_1e.png|

-  Refer to the illustration below that shows how to connect the components\

|lab_3_assembly_image_2a.png|

-  Run PixelPulse on the computer and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Connect the M1K +5 V power supply to the circuit as indicated in the schematic
-  Observe the LED flashing and use the potentiometer to adjust the flash rate.
-  Set up Channel A of the M1K to measure voltage and observe the voltage on Pin 1 of the AD654 using PixelPulse
-  Use a jumper wire to short across R\ :sub:`C`, as indicated by the dotted line in the schematic
-  Set up Channel B of the M1K to measure voltage and connect AD654 Pin 4 to Channel A and Pin 3 to Channel B
-  Use the potentiometer to adjust the voltage on Pin 4 and observe the voltage levels on Pins 3 and 4 using PixelPulse
-  Verify that the voltage on Pin 3 closely tracks the voltage applied to Pin 4

Theory
------

The input voltage (Pin 4) range for single-supply operation is specified as 0 V to +V\ :sub:`S` – 4 V, which in this case is 0 V to 1 V. While this specification is for normal linear operation, the absolute maximum input limit is +V\ :sub:`S` on a single supply, so we are not in danger of damaging the chip with our input voltage that can run up to +5 V. The output frequency in the linear portion of the V\ :sub:`IN` range is defined as

:math:`\displaystyle f_OUT = V_IN(\frac{1}{10}V{R_T}{C_T}) = V_IN(\frac{1}{10}V{(5 MΩ)}{(0.1 μF)}) = V_IN(\frac{1}{10}V{(0.5s)}) = V_IN(\frac{1}{5}Vs)`

For V\ :sub:`IN` = 1 V, we have f = 0.2 Hz.

The oscillation frequency is determined by R\ :sub:`T` and C\ :sub:`T`. In voltage-to-frequency conversion applications the oscillation frequency is typically set to be in the tens or hundreds of kilohertz, but for this lab it was set to flash the LED at a rate that was observable. The low rate requires a large RC time constant, which was obtained with the 0.1 μF capacitor and 5 MΩ resistor.

The op-amp requires a small input bias current on each input, and these currents are closely, but not perfectly matched. The current flowing through R\ :sub:`T` produces a voltage drop across R\ :sub:`T`, introducing an error into the frequency setting. Compensation resistor, R\ :sub:`C`, a resistor equal in value to R\ :sub:`T`, is added to the non-inverting input (Pin 4) to produce a nearly identical voltage drop is as is across R\ :sub:`T`. This technique minimizes the offset error between the two op-amp inputs, and produces the most accurate output frequency. This is an important consideration in circuits that are used as voltage-to-frequency converters, but not so important in simple LED flashing circuits. When observing the voltage on Pin 4, a jumper wire must be placed across R\ :sub:`C` (shown as dotted line in the schematic) in order to eliminate DC losses that occur due to the M1K input loading the 5 MΩ source resistance.

In a voltage-feedback op-amp circuit, negative feedback causes the feedback voltage on the inverting input to track the voltage on the non-inverting input. The voltage on Pin 3 is the feedback voltage, and this should track the voltage applied to Pin 4 very closely as long as the output of the emitter follower can follow it and the input common-mode range is not violated.

Observations and Conclusions
----------------------------

-  The AD654 is a voltage-to frequency converter that can be used for many functions, ranging from precise signal transmission to simple LED flashing
-  Op-amp circuits require input bias currents, and offset errors can be minimized by matching the resistances that each input bias current flows through
-  The two voltage-feedback op-amp input voltage levels track each other closely when negative feedback is applied around the op-amp

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`

.. |lab_3_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_3_image_1.png
   :width: 600px
.. |lab_3_assembly_image_1e.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_3_assembly_image_1e.png
   :width: 800px
.. |lab_3_assembly_image_2a.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_3_assembly_image_2a.png
   :width: 800px
