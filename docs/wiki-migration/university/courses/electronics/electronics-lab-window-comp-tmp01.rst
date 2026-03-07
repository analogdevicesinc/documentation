Activity: Temperature Control using Window Comparator
=====================================================

Objective
---------

The objective of this lab activity is to use two high speed voltage comparators as a Window-Comparator and program the TMP01 Low Power Programmable Temperature Controller using this approach.

A Window-Comparator is a circuit configuration, usually consisting of a pair of voltage comparators (inverting and non-inverting), in which the output indicates whether an input signal is within the voltage range bounded by two different thresholds. One which triggers an op-amp comparator on detection of some upper voltage threshold, V\ :sub:`REF(HIGH)` and one which triggers an op-amp comparator on detection of a lower voltage threshold level, V\ :sub:`REF(LOW)`. The voltage levels between these two upper and lower reference voltages is called the “window”.

Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 2 – AD8561 Comparators
| 1 – 2N3904 NPN transistor
| 2 – 1N914 small signal diodes
| 1 – LED ( any color )
| 3 – 10KΩ resistor
| 1 – 20KΩ resistor
| 1 – 470Ω resistor

Window Comparator
-----------------

Background
~~~~~~~~~~

Consider the circuit presented in Figure 1.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 1 Window Comparator


The circuit uses a voltage divider network, formed of three equal value resistors R1 = R2 = R3. The voltage drops across each resistor will also be equal at one-third of the reference voltage (V\ :sub:`REF`). Therefore, the upper reference (V\ :sub:`REF(HIGH)`) is set to 2/3V\ :sub:`REF` and the lower reference to 1/3V\ :sub:`REF`.

Considering that we use the When V\ :sub:`IN` is below the lower voltage level, (V\ :sub:`REF(LOW)`) which equates to 1/3V\ :sub:`REF`, the output will be HIGH and D2 will be forward biased. Due to the positive voltage at base the npn transistor, Q1 moves into the saturation. Thus, the output voltage is zero, and the supply voltage will drop on R5 and D3, turning the LED on.

When V\ :sub:`IN` exceeds this 1/3V\ :sub:`REF` lower voltage level and it is below 2/3V\ :sub:`REF` (V\ :sub:`REF(HIGH)`), both comparators' outputs will be LOW and the diodes reverse-biased. No voltage is applied to the base of Q1,the transistor is in cut-off and no collector current flows through R6 or R5, D3. The output voltage is the supply voltage V+.

When V\ :sub:`IN` is above the upper voltage level, (V\ :sub:`REF(HIGH)`) which equates to 2/3V\ :sub:`REF`, the output will be HIGH and D1 will be forward biased. Due to the positive voltage at base the npn transistor, Q1 moves into the saturation. Thus, the output voltage is zero, and the supply voltage will drop on R5 and D3, turning the LED on.

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for the window comparator circuit.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 2. Window Comparator breadboard circuit


Procedure
~~~~~~~~~

Use the first waveform generator (W1) as source to provide a Triangular signal with 5V amplitude peak-to-peak, 100Hz frequency and 2.5V offset.

Use the second waveform generator (W2) as 5V constant reference voltage.

Supply the circuit using the 5V power supply.

Configure the scope so that output signal is displayed on channel 2 and the input signal is displayed on channel 1.

A plot example is presented in Figure 3.

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   Figure 3. Window Comparator waveforms


On the plot the "windows" can be noticed when the input voltage is between the upper and the lower voltage references.

Temperature Control
-------------------

.. _background-1:

Background
~~~~~~~~~~

An example of a window comparator application is a simple temperature controller circuit (Figure 2). The temperature sensor, TMP01, has the dual comparator configuration of figure 1 built in. By choosing the proper values for R\ :sub:`1`, R\ :sub:`2` and R\ :sub:`3` the circuit monitors if the temperature holds in the required range (25 ± ~10 °C).

The TMP01 is a linear voltage-output temperature sensor, with a window comparator that can be programmed by the user to activate one of two open-collector outputs when a predetermined temperature set point voltage has been exceeded. A low drift voltage reference is available for set point programming. By connecting the two open collector outputs together as a single wire OR output we can obtain a signal which is at a logic high when the ambient temperature is within the target window.

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   Figure 4 Temperature sensor window comparator


Programming TMP01
~~~~~~~~~~~~~~~~~

In the basic fixed set point application utilizing a simple resistor ladder voltage divider, the desired temperature set points are programmed in the following sequence:

1. Select the desired hysteresis temperature.

2. Calculate the hysteresis current I\ :sub:`VREF`.

3. Select the desired set point temperatures.

4. Calculate the individual resistor divider ladder values needed to develop the desired comparator set point voltages at SET HIGH and SET LOW.

The hysteresis current is readily calculated. For example, for 2 degrees of hysteresis, I\ :sub:`VREF` = 17 μA. Next, the set point voltages, V\ :sub:`SETHIGH` and V\ :sub:`SETLOW`, are determined using the VPTAT scale factor of 5 mV/K = 5 mV/(°C + 273.15), which is 1.49 V for 25°C. Then, calculate the divider resistors, based on those set points. The equations used to calculate the resistors are:

V\ :sub:`SETHIGH` = (T\ :sub:`SETHIGH`\ + 273.15) (5 mV/°C)

V\ :sub:`SETLOW` = (T\ :sub:`SETLOW` + 273.15) (5 mV/°C)

R\ :sub:`1` (in kΩ) = (V\ :sub:`VREF`\ −V\ :sub:`SETHIGH`)/I\ :sub:`VREF`\ = (2.5 V −V\ :sub:`SETHIGH`)/I\ :sub:`VREF`

R\ :sub:`2` (in kΩ) = (V\ :sub:`SETHIGH`\ −V\ :sub:`SETLOW`)/I\ :sub:`VREF`

R\ :sub:`3` (in kΩ) = V\ :sub:`SETLOW`/I\ :sub:`VREF`

The total R\ :sub:`1` + R\ :sub:`2` + R\ :sub:`3` is equal to the load resistance needed to draw the desired hysteresis current from the reference, or I\ :sub:`VREF`.

I\ :sub:`VREF` = 2.5V/( R\ :sub:`1` + R\ :sub:`2` + R\ :sub:`3`)

Since VREF = 2.5 V, with a reference load resistance of 357 kΩ or greater (output current 7 μA or less), the temperature setpoint hysteresis is zero degrees. Larger values of load resistance only decrease the output current below 7 μA and have no effect on the operation of the device. The amount of hysteresis is determined by selecting a value of load resistance for VREF.

Tasks
~~~~~

1. Build the following circuit:

.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   Figure 5 Temperature Measurement


Measure VPTAT output value and compute the actual measured temperature in degrees Kelvin and degrees Celsius.

2. Build the following circuit:

.. container:: centeralign

   \ |image6|\


.. container:: centeralign

   Figure 6 Temperature Control


2.a. Identify the components and try to draw the circuit schematic.

2.b. Using the information provided by the breadboard circuit, compute the following parameters:

-  I\ :sub:`VREF`
-  V\ :sub:`SETHIGH`
-  V\ :sub:`SETLOW`
-  T\ :sub:`SETHIGH`
-  T\ :sub:`SETLOW`

2.c. How many degrees is the temperature setpoint hysteresis? How can you change this value?

2.d. How does the circuit work? When will LED1 (red) and LED2 (blue) turn on? Explain your answer.

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/temp_ctrl_bb`
   -  LTspice files: :git-education_tools:`m2k/fritzing/temp_ctrl_ltspice`
   


Further Reading
---------------

Additional resources:

-  :adi:`TMP01 Low Power Programmable Temperature Controller <static/imported-files/data_sheets/TMP01.pdf>`
-  :adi:`Adding Test Capability to a Window Comparator <library/analogdialogue/archives/42-10/testing_comparators.html>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/window_comp-sch.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/window_comp-bb.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/window_comp-wav.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/tmp01_window_comp-sch.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/tmp01-bb1.png
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/tmp01-bb2.png
