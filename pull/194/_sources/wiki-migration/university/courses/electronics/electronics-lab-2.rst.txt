Activity: Diode I vs. V curves, For ADALM2000
=============================================

Objective:
----------

The purpose of this activity is to investigate the current vs. voltage characteristics of a PN junction diode.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less Breadboard
| 1 - Resistor (1KΩ or any similar value from 1KΩ to 5KΩ)
| 1 - small signal diode (1N914 or similar)

Directions:
-----------

The current vs. voltage characteristics of the PN junction diode can be measured using the ADALM2000 Board and the following connections. The green boxes indicate where to connect the ADALM2000 board. Set up the breadboard with waveform generator output, W1, attached to one end of the resistor. The 2+ scope input is also connected here. The other end of the resistor is connected to one end of the diode as shown in the first diagram. The 2- scope input as well as the 1+ scope input is also connected to the second end of the resistor. The other end of the diode is connected to ground along with the 1- scope input.


|image1|

.. container:: centeralign

   Figure 1. Connection diagram for diode I/V curves


Hardware Setup:
~~~~~~~~~~~~~~~

The waveform generator should be configured for a 100 Hz triangle wave with 6 volt amplitude peak-to-peak and 0 volt offset. The differential input of scope channel 2 (2+,2-) is used to measure the current in the resistor (and diode). The Single ended input of scope channel 1 (1+) is used to measure the voltage across the diode (1- input can be grounded). The Scope should be setup with channel 1 at 500mV per division and channel 2 set also at 500mV per division. The current flowing through the diode, I\ :sub:`D`, is the voltage measured by channel 2 divided by the resistor value (1KΩ in this example). Use the XY display mode to plot the voltage across the diode (scope channel 1) on the X axis vs. the current in the diode (scope channel 2) on the Y axis.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/c_vs_v_diode-bb.png
   :width: 600px

.. container:: centeralign

   Figure 2. Current vs. Voltage, linear scales


Procedure:
----------

.. container:: centeralign

   |image2|\


.. container:: centeralign

   Figure 3. Current vs. Voltage, linear scales Scopy plot


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_p1.png
   :align: center

.. container:: centeralign

   Figure 4. Current vs. Voltage, linear scales Excel plot


Load the captured data into spreadsheet program like Excel and calculate the diode current I\ :sub:`D`. Plot the current vs. the voltage across the diode. The diode voltage, current relationship is logarithmic. If plotted on log scale the line should be straight as seen in the second plot.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_p2.png
   :align: center

.. container:: centeralign

   Figure 5. Current vs. Voltage on log scale


Questions:
----------

What is the mathematical expression for the diode current, I\ :sub:`D`, given the voltage across the diode V\ :sub:`D`?

Further exploration on diode characteristics:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Measure the diode characteristics, V\ :sub:`D` at a fixed I\ :sub:`D`, of multiple 1N914 diodes; there should be four included in the ADALP2000 Analog Parts Kit and ask to exchange some with a lab-mate to get even more samples. Calculate the mean and coefficient of variation (CV) of your measurements, (CV is defined as the standard deviation divided by the mean as a percentage ). Discuss the amount of variation you observe, which is often a measure of what semiconductor engineers call process variation.

Replace the 1N914 diodes with a light-emitting diode, or LED. You should have red, yellow, green and infrared LEDs in the ADALP2000 Analog Parts Kit. Do the LED diodes have similar mathematical expressions for the diode current, I\ :sub:`D`, given the voltage across the diode V\ :sub:`D`\ as the IN914? In what way are the similar and in what way are they different? Do the red, yellow and green LEDs "turn on" at the same forward voltage?

Activity 2a. Half wave rectifier
================================

.. _objective-1:

Objective:
----------

The purpose of this activity is to investigate the use of a diode as a half wave rectifier.

.. _materials-1:

Materials:
----------

| 1 - Resistor (4.7KΩ or any similar value)
| 1 - small signal diode (1N914 or similar)

.. _directions-1:

Directions:
-----------

Set up the breadboard with waveform generator output W1 attached to one end of the diode. The other end of the diode is connected to one end of the load resistor as shown in figure 6. The other end of the resistor is connected to ground. Single ended input of scope channel 2 (2+) is also connected to the end of the resistor not connected to ground (2- input can be grounded).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6. Connection diagram for half wave diode rectifier


.. _hardware-setup-1:

Hardware Setup:
---------------

The waveform generator should be configured for a 100 Hz Sine wave with 6 volt amplitude peak-to-peak and 0 volt offset. The scope channel 2 (2+) is used to measure the voltage across the load resistor, R\ :sub:`L`. Both scope channels should be set to 500mV per division.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/half_wave-bb.png
   :align: center

.. container:: centeralign

   Figure 7. Half Wave Diode Rectifier Breadboard Circuit


.. _procedure-1:

Procedure:
----------

Plot the two waveforms using Oscilloscope feature from the Scopy tool.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/half_wave-waveform.png
   :align: center

.. container:: centeralign

   Figure 8. Half Wave rectified waveform


.. _questions-1:

Questions:
----------

Why is the peak value of the rectified output less than the peak value of the AC input and by how much? At what point in the input waveform does the rectified waveform become positive i.e. something other than zero? What happens if the direction of the diode is reversed? Repeat the experiment with the direction of the diode reversed.

Further Exploration:
~~~~~~~~~~~~~~~~~~~~

Replace the 1N914 diode with a light-emitting diode, or LED. You probably need to increase the AWG1 amplitude to 10V peak-to-peak to accommodate the higher forward voltage drop of the LED. 1. How does the waveform for the rectified output compare to your earlier results with the 1N914 diode? By how much does the forward-bias voltage drop increase? 2. Experiment with the three different waveform shapes while the waveform generator remains set to 100 Hz, pay attention to the brightness of the LED. Discuss your observations of waveform shape and brightness and relate these observations to your measured effective DC values for each waveform shape. 3. Reduce the waveform generator frequency, and experiment with values as low at 0.2 Hz (one cycle every five seconds). Discuss the behavior of the LED optical intensity for each of the three waveform shapes when the waveform generator frequency is 1 Hz or less. 4. At what frequency does the flashing LED stop flickering and begin to appear as a constant intensity?

Activity 2b. Full wave rectifier
================================

.. _objective-2:

Objective:
----------

The purpose of this activity is to investigate the use of two diodes as a full wave rectifier.

.. _materials-2:

Materials:
----------

| 1 - Resistor (4.7KΩ or any similar value)
| 2 - small signal Diodes (1N914 or similar)

.. _directions-2:

Directions:
-----------

Set up the breadboard with W1 attached to one end of the first diode, D\ :sub:`1`, and W2 to one end of the second diode, D\ :sub:`2`. Both diodes should face in the same direction. The other end of each diode is connected to one end of the load resistor as shown figure 9. The other end of the resistor is connected to ground. Single ended input of scope channel 2 (2+) is connected to the junction of the resistor and the two diodes.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9. Connection diagram for full wave diode rectifier


.. _hardware-setup-2:

Hardware Setup:
---------------

The first waveform generator, W1, should be configured for a 100 Hz Sine wave with 6 volt amplitude peak-to-peak and 0 volt offset. The second AWG generator, W2, should be configured also for a 100 Hz Sine wave with 6 volt peak-to-peak amplitude and 0 volt offset but with the phase set to 180 degrees. The Single ended input of scope channel 2 (2+) is used to measure the voltage across the load resistor. Both scope channels should be set to 500mV per division.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/full_wave-bb.png
   :align: center

.. container:: centeralign

   Figure 10. Full Wave Diode Rectifier Breadboard Circuit


.. _procedure-2:

Procedure:
----------

Plot the two waveforms using the Oscilloscope provided by the Scopy tool. If both 0 degree and 180 degree phases of the AC input are available, then a second diode can fill in the missing half-wave of the input and produce the full-wave rectified signal shown in this plot. Again the forward voltage of the diodes is apparent and the output waveform does not come to a sharp point at the zero crossing due to the non-zero turn on voltage of the diodes.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/full_wave-waveform.png
   :align: center

.. container:: centeralign

   Figure 11. Full Wave rectified waveform


.. _questions-2:

Questions:
----------

-  What happens if the direction of the diodes is reversed? Repeat experiment with the direction of both diodes reversed.
-  What happens if the direction of one diode is opposite of the other? Repeat experiment with the direction of one diode (D\ :sub:`1`) reversed.
-  How could both 0 degree and 180 degree phases be created from a single source (a transformer?)?

.. _further-exploration-1:

Further exploration:
~~~~~~~~~~~~~~~~~~~~

Replace D\ :sub:`1` and D\ :sub:`2` with red and green LEDs. Increase the amplitude of AWG1 to 10V peak-to-peak( to accommodate the higher turn on voltage of the LEDs ). Slow the frequency of AWG1 to 5 Hz or less. Are the two LEDs ever both on at the same time? 1. How does the waveform for the rectified output compare to your earlier results with the 1N914 diodes? By how much does the forward-bias voltage drop increase? 2. Experiment with the three different waveform shapes while the waveform generator is set to 100 Hz, pay attention to the brightness of the LEDs. Discuss your observations of waveform shape and brightness and relate these observations to your measured effective DC values for each waveform shape. 3. Reduce the waveform generator frequency, and experiment with values as low at 0.2 Hz (one cycle every five seconds). Discuss the behavior of the LED optical intensity for each of the three waveform shapes when the waveform generator frequency is 1 Hz or less. 4. At what frequency do the flashing LEDs stop flickering and begin to appear as a constant intensity?

2c. Bridge rectifier
====================

.. _objective-3:

Objective:
----------

The purpose of this activity is to investigate the use of four diodes as a bridge rectifier.

.. _materials-3:

Materials:
----------

| 1 - Resistor (4.7KΩ or any similar value)
| 4 - small signal Diodes (1N914 or similar)

.. _directions-3:

Directions:
-----------

Four diodes can be arranged in a bridge configuration to provide a full-wave rectification from a single AC phase as shown here. However, it can also be seen that only the AC input or the load can be referenced to ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f4_r2.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 12. Connection diagram for diode bridge rectifier


.. _hardware-setup-3:

Hardware Setup:
---------------

The waveform generator should be configured for a 100 Hz Sine wave with 6 volt peak-to-peak amplitude and 0 volt offset. The scope channel 2 (2+. 2-) is used to measure the voltage across the load resistor, R\ :sub:`L`. Both scope channels should be set to 500mV per division.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/bridge-bb.png
   :align: center

.. container:: centeralign

   Figure 13. Diode Bridge Rectifier Breadboard Circuit


.. _procedure-3:

Procedure:
----------

Plot the two waveforms using the Oscilloscope provided by the Scopy tool. The disadvantage of this circuit is that now two diode drops are in series with the load and the peak value of the rectified output is less than the AC input by 1.2 Volts rather than the 0.6 V in the previous circuits.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/bridge-waveform.png
   :align: center

.. container:: centeralign

   Figure 14. Full Wave Bridge rectifier waveforms


.. _questions-3:

Questions:
----------

How would you reconfigure this circuit to allow one end of the load resistor to be connected to ground rather than how it is shown figure 4 with one end of the AC source grounded?

.. _further-exploration-2:

Further exploration:
~~~~~~~~~~~~~~~~~~~~

Replace all four diodes D\ :sub:`1`, D\ :sub:`2`, D\ :sub:`3` and D\ :sub:`4` with red and green LEDs. Increase the amplitude of AWG1 to 10V peak-to-peak ( to accommodate the higher turn on voltage of the LEDs ). Slow the frequency of AWG1 to 5 Hz or less. Are two of LEDs ever both on at the same time? If so which two? 1. How does the waveform for the rectified output compare to your earlier results with the 1N914 diodes? By how much does the forward-bias voltage drop increase? 2. Experiment with the three different waveform shapes while the waveform generator is set to 100 Hz, pay attention to the brightness of the LEDs. Discuss your observations of waveform shape and brightness and relate these observations to your measured effective DC values for each waveform shape. 3. Reduce the waveform generator frequency, and experiment with values as low at 0.2 Hz (one cycle every five seconds). Discuss the behavior of the LED optical intensity for each of the three waveform shapes when the waveform generator frequency is 1 Hz or less. 4. At what frequency do the flashing LEDs stop flickering and begin to appear as a constant intensity?

Activity 2d. Limiter / Clamp circuit
====================================

.. _objective-4:

Objective:
----------

The purpose of this activity is to investigate the use of diode as a amplitude limiting or clamp circuit.

.. _materials-4:

Materials:
----------

| 1 - 10KΩ Resistor (or any similar value)
| 2 - small signal Diodes (1N914 or similar)

.. _directions-4:

Directions:
-----------

Set up the breadboard with waveform generator output (W1) attached to one end of the 10K resistor as shown in figure 15. One diode (D\ :sub:`1`) is connected between the other end of the 10K resistor and the output of the second function generator. The second diode D\ :sub:`2` is connected between ground and the top of D\ :sub:`1` as shown. Scope channel 2 (2+) is connected to the common connection of the resistor and the two diodes.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 15. Connection diagram for diode clamp


.. _hardware-setup-4:

Hardware Setup:
---------------

The first waveform generator should be configured for a 100 Hz Sine wave with 6 volt peak-to-peak amplitude and 0 volt offset. The second waveform generator should be configured with 0 amplitude and 0 offset to start. The offset of the second generator will be varied and the effect on the output signal observed. Scope channel 2 (2+) is used to measure the clamped / limited voltage and should be set to 500mV/div.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/clamp-bb.png
   :align: center

.. container:: centeralign

   Figure 16. Diode Clamp Breadboard Circuit


.. _procedure-4:

Procedure:
----------

With the DC offset value of waveform generator 2 set to zero observe the minimum and maximum values of the voltage seen on scope channel 2 (2+). Adjust the DC offset of generator 2 between -2V and +2V and observe the minimum and maximum voltage seen on the scope. Reverse the direction of both diodes, D\ :sub:`1` and D\ :sub:`2`. Repeat the sweep of the DC offset and observe the minimum and maximum voltages seen on the scope. How do the two sets of measurements compare?

.. image:: https://wiki.analog.com/_media/university/courses/electronics/clamp-waveform.png
   :align: center

.. container:: centeralign

   Figure 17. Diode Clamp waveforms


.. _questions-4:

Questions:
----------

What happens to the voltage limits if both diodes, D\ :sub:`1` and D\ :sub:`2` are connected to the second generator output?

Activity 2e. AC coupling and DC restoration
===========================================

.. _objective-5:

Objective:
----------

The purpose of this activity is to investigate AC coupling and the use of diode as a DC restoration circuit. Many signals contain a DC component. Often this DC must be removed and perhaps restored to a different DC level later in the signal path.

.. _materials-5:

Materials:
----------

| 1 - 1.0 uF Capacitor( or any similar value )
| 1 - small signal Diode (1N914 or similar)

.. _directions-5:

Directions:
-----------

Set up the breadboard with W1 attached to one end of the 1.0uF capacitor as shown in figure 18. The Diode (D\ :sub:`1`) is connected between the other end of the 1.0uF capacitor and the output of the second waveform generator, W2. Single ended input of scope channel 2 (2+) is connected to the common connection of the capacitor and the diode.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 18. Connection diagram for DC Restoration circuit


.. _hardware-setup-5:

Hardware Setup:
---------------

The first waveform generator should be configured for a 1KHz Sine wave with 2 volt amplitude peak-to-peak and 0 volt offset to start. The offset will be varied and the effect on the output observed. The second waveform generator should be configured with 0 amplitude and 0 offset to start. The offset will be varied and the effect on the output observed. Scope channel 2 (2+) is used to measure the voltage and should be set to 500mV/div.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/DC_rest-bb.png
   :align: center

.. container:: centeralign

   Figure 19. DC Restoration Breadboard Circuit


.. _procedure-5:

Procedure:
----------

Plot the two waveforms using the Oscilloscope provided by the Scopy tool.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/DC_rest-waveform.png
   :align: center

.. container:: centeralign

   Figure 20. DC Restoration waveforms


Replace diode D\ :sub:`1` in the circuit with a 10K resistor. Using the measurement tab on the Scope, read and record the positive and negative peak values and mean value of channel2 (2+) as the offset of waveform generator channel 1 is changed between -1 and +1 volt. Now set waveform generator channel 1 to a square wave again with 2V peak-to-peak amplitude value. As done before read and record the positive and negative peak values and the mean value as the duty cycle of the square wave is changed between 10% and 90%. Now remove the 10KΩ resistor and put diode D\ :sub:`1` back in place. Repeat the same measurements, adjusting DC offset and duty cycle, that were just taken with resistor. How do they compare? Reverse the direction of diode D1 and again repeat these same measurements. How do they compare to the previous two?

.. _questions-5:

Questions:
----------

What happened when the direction of D\ :sub:`1` was reversed? What is the effect of setting different DC values for the output of generator 2 (W2)?

Activity 2f. Variable attenuator
================================

.. _objective-6:

Objective:
----------

The goal of this activity is to build, characterize and analyze a small signal variable attenuator using a diode.

.. _materials-6:

Materials:
----------

| 1 - 2.2KΩ Resistor
| 1 - 4.7KΩ Resistor
| 1 - 10KΩ Resistor
| 1 - 5KΩ Variable resistor, potentiometer
| 2 - 0.1uF Capacitors
| 1 - small signal Diode (1N914 or similar)

.. _directions-6:

Directions:
-----------

Set up the breadboard with the first waveform generator attached to one end of the 0.1uF capacitor as shown in figure 21. Resistor R\ :sub:`1` is connected between the second end of C\ :sub:`1` and junction of D\ :sub:`1`, R\ :sub:`2` and C\ :sub:`2`. The other end of D\ :sub:`1` is connected to ground. The second end of resistor R\ :sub:`2` is connected to the wiper of the potentiometer R\ :sub:`3`. The ends of R\ :sub:`3` are connected to ground and Vp (5V) respectively. Scope channel 2 (2+) is connected to the common connection of capacitor C\ :sub:`2` and load resistor R\ :sub:`4`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 21. Connection diagram for variable attenuator


.. _hardware-setup-6:

Hardware Setup:
---------------

Waveform generator W1 should be configured for a 10KHz Sine wave with 200 mV peak-to-peak amplitude (or less) and offset set to 0. The set scope channel 1+ at 100mV per division and scope channel 2+ connected R4 at 100mV per division. Set the measurements tab to display Ch1 peak-peak and Ch2 peak-peak.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/var_atten-bb.png
   :align: center

.. container:: centeralign

   Figure 22. Variable Attenuator Breadboard Circuit


.. _procedure-6:

Procedure:
----------

Plot the two waveforms using the Oscilloscope provided by the Scopy tool.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/var_atten-waveform.png
   :align: center

.. container:: centeralign

   Figure 23. Variable Attenuator waveforms


| The purpose of C\ :sub:`1` (and C\ :sub:`2`) is to block DC current from the input and output circuits so the operating point of the diode is not affected. The attenuator uses the fact that that "small signal" resistance of the diode r\ :sub:`D` is a function the DC current flowing in the diode I\ :sub:`D`. See Equations below: |image3| |image4| Where:
| n is the diode area ( size ) scale factor
| V\ :sub:`T` is the Thermal Voltage
| I\ :sub:`D` is the diode current
| k is Boltzmann's constant
| q is the electron charge
| T is the absolute temperature
| In the circuit a voltage divider is set up between R\ :sub:`1` and the resistance of D\ :sub:`1`. The current in D\ :sub:`1`\ is varied by changing the current in R\ :sub:`2`. When the current in D\ :sub:`1` is small r\ :sub:`D`\ is large and the fraction of the input signal seen at the output is large. As the current in D\ :sub:`1` increases, its resistance decreases and the fraction of the input seen at the output decreases.

.. _questions-6:

Questions:
----------

What is the maximum input signal level that you can use without distorting the output signal? What circuit parameter determines the upper limit of the input signal?

Activity 2g. Absolute value circuits
====================================

.. _objective-7:

Objective:
----------

The purpose of this activity is to investigate absolute value circuits. Rectifiers, or 'absolute-value' circuits are often used as detectors to convert the amplitudes of AC signals to DC values to be more easily measured. For this type of circuit, the AC signal is first high-pass filtered to remove any DC term and then rectified and perhaps low pass filtered. As we have seen in the simple rectifier circuits constructed with diodes, the circuit does not respond well to signals with a magnitude less than a diode-drop (0.6V for silicon diodes). This limits their use in designs where small amplitudes are to be measured. For designs in which a high degree of precision is needed, op-amps can be used in conjunction with diodes to build precision rectifiers.

.. _materials-7:

Materials:
----------

| 1 - Dual Op AMP (such as ADTL082 or similar)
| 5 - 10KΩ Resistors
| 2 - small signal Diodes (1N914 or similar)
| 2 - 4.7uF decoupling capacitors

.. _directions-7:

Directions:
-----------

The inverting op-amp circuit can be converted into an "ideal" (linear precision) half-wave rectifier by adding two diodes as shown in figure 24. For the negative half of the input diode D\ :sub:`1` is reverse biased and diode D\ :sub:`2` is forward biased and the circuit operates as a conventional inverter with a gain of -1. For the positive half of the input, diode D\ :sub:`1` is forward biased, closing the feedback around the amplifier. Diode D\ :sub:`2` is reverse biased disconnecting the output from the amplifier. The output will be at the virtual ground potential ( - input terminal ) through the 10K ohm resistor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 24. Connection diagram for precision half-wave rectifier


.. _hardware-setup-7:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abs_val1-bb.png
   :align: center

.. container:: centeralign

   Figure 25. Precision Half-Wave Rectifier Breadboard Circuit


.. _procedure-7:

Procedure:
----------

The peak of the rectified output, as seen in the plot here, is now equal to the peak value of the input. There is also a sharp transition as the input crosses zero. The experimenter should investigate the waveforms at different points in the circuit to explain why this circuit works better than the simple diode half wave rectifier.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abs_val1-waveform.png
   :align: center

.. container:: centeralign

   Figure 26. Precision Half-Wave Rectifier waveforms


.. _directions-8:

Directions:
-----------

The circuit shown in figure 27 is an absolute value circuit, often called a precision full-wave rectifier. It should operate like a full wave rectifier circuit constructed with ideal diodes ( the voltage across the diode, in forward conduction, equals 0 volts). The actual diodes used in the circuit will have a forward voltage of around 0.6 V.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 27. Connection diagram for absolute value circuit


.. _hardware-setup-8:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abs_val2-bb.png
   :align: center

.. container:: centeralign

   Figure 28. Absolute Value Breadboard Circuit


.. _procedure-8:

Procedure:
----------

| For this laboratory exercise you should:
| a) Study the circuit and determine how it works. There is very fundamental concept that should help in understanding how this circuit operates. Given an op-amp configured with negative feedback, the inverting and non-inverting input terminals will try to reach the same voltage level, often referred to as a virtual short.
| b) Plan some tests to see if this circuit indeed is an absolute value circuit. Perform these tests, fully documenting all tests and results.
| c) Make the input voltage a 6 Volt amplitude sinusoid, at 1KHz. Carefully measure and record voltages at all nodes in the circuit.
| |image5|

.. container:: centeralign

   Figure 29. Absolute Value waveforms


.. _questions-7:

Questions:
----------

Report on your experiments by fully documenting all tests and results.

Activity 2h. A Voltage Doubler circuit
======================================

Voltage doublers are very useful in situations where the load current is relatively light, and the required DC voltage is higher than what is available from the system power supply.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 30. Connection diagram for voltage doubler circuit


How this circuit operates is not as straight-forward as the diode rectifier circuits we examined earlier. To understand this circuit we need to take a look at it during successive half-cycles of the ac input from W1. We will start by assuming ideal components and that C\ :sub:`1` = C\ :sub:`2`.

-   During the first negative half-cycle, D\ :sub:`1` will be forward biased and will hold the right end of C\ :sub:`1` at one diode drop below ground. Therefore C\ :sub:`1` will charge to a voltage nearly equal to the peak voltage (v\ :sub:`peak`) of the AC input, with its left end being negative with respect to ground.<sub> </sub>
-   During the following positive half cycle, D\ :sub:`1` will be reverse biased and will not conduct current. The voltage on C\ :sub:`1` will add to the AC input voltage, so a voltage of approximately 2v\ :sub:`peak` will appear at the left end of D\ :sub:`2`. Since C\ :sub:`2` is not yet charged at all, this will forward bias D\ :sub:`2` and allow the voltage at the right end of C\ :sub:`1` to be applied to the top of C\ :sub:`2`. C\ :sub:`2` will charge as C\ :sub:`1` discharges, until the two capacitors can no longer forward-bias D\ :sub:`2`. For the first positive half-cycle, the voltage on C\ :sub:`2` will be equal to v\ :sub:`peak`, and C\ :sub:`1` will be completely discharged, so that all the voltage at the left end of D\ :sub:`2` comes from the AC input.<sub> </sub>
-   On the next negative half-cycle, C1 charges again to v\ :sub:`peak`, through D\ :sub:`1`. If there is no load to discharge C\ :sub:`2`, its output will remain at +v\ :sub:`peak`.<sub> </sub>
-   On the second positive half-cycle, C\ :sub:`2` is still charged to +v\ :sub:`peak`, while the voltage at the left end of D\ :sub:`2` is again +2v\ :sub:`peak`. Again, C\ :sub:`1` transfers part of its charge to C\ :sub:`2`, but this time they stop when C\ :sub:`2` is charged to a voltage of +1.5v\ :sub:`peak`.<sub> </sub>
-   This action continues, cycle by cycle, with C\ :sub:`1` being fully recharged to v\ :sub:`p` on each negative half cycle, and then charging C\ :sub:`2` to a voltage halfway between its starting voltage and +2v\ :sub:`peak`. C\ :sub:`2` will never quite charge to +2v\ :sub:`peak`, but it will come very close.<sub> </sub>

With non-ideal components there is a small (0.6) voltage drop across each diode when it is forward biased. This will reduce the maximum no load output voltage of the doubler. Any load on this circuit, such as R\ :sub:`L`, will draw current from C\ :sub:`2` at all times, thus discharging this capacitor to some extent. On each positive half-cycle C\ :sub:`1` will recharge C\ :sub:`2` from the voltage it had at the start of the half-cycle halfway up to +2v\ :sub:`peak`. The ripple on the output will be larger and the average DC value will be lower.

Note that the output current capacity of this circuit is only half the current capacity of a normal rectifier circuit. Any additional load current taken from the voltage doubler will simply cause C\ :sub:`2` to discharge faster, thus reducing the output voltage. It is never possible to get more power out of the voltage doubler than goes into it.

The charging and recharging of C\ :sub:`2`\ can be made faster if C\ :sub:`1` is made larger than C\ :sub:`2`. For example, if C\ :sub:`1` = 10µF and C\ :sub:`2` = 1µF, C\ :sub:`1` can transfer much more charge to C\ :sub:`2` on each positive half-cycle, and the voltage on C\ :sub:`2` will increase much faster than the voltage on C\ :sub:`1` will decrease. Of course, this also means that the output current capacity is even more limited, since C\ :sub:`2` will discharge rapidly as well as charging rapidly.

.. _hardware-setup-9:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/doubler-bb.png
   :align: center

.. container:: centeralign

   Figure 31. Voltage Doubler Breadboard Circuit


.. _procedure-9:

Procedure:
----------

Plot the two waveforms using the Oscilloscope provided by the Scopy tool.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/doubler-waveform.png
   :align: center

.. container:: centeralign

   Figure 32. Voltage Doubler waveforms


.. _questions-8:

Questions:
----------

1. This circuit produces a positive DC output voltage. How can it be reconfigured to make a negative output voltage? Sketch your voltage inverter circuit. Construct the voltage inverter and repeat the experiment / report tasks you did with the voltage doubler. 2. What is the minimum peak voltage of the AC input below which the circuit no longer functions? 3. Try different input waveforms. Which is better, Sine, Square, Triangle and why? How does the duty-cycle of the AC input effect the DC output and why?

Activity 2i. Push - Pull Voltage Doubler
========================================

A limitation of the voltage doubler circuit is that it only uses one half (positive in the previous example) of the AC input. In the next circuit the diodes and capacitors are rearranged slightly, and are driven in a push-pull or H bridge fashion. The result is that now two current pulses per cycle are delivered to the load. The output voltage will be higher by one half the driver supply voltage. The output will be 2.5X the supply minus two diode drops.

What happens to the output voltage across R\ :sub:`L` if the direction of the four diodes are reversed?

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 33. push-pull voltage doubler


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 34. CMOS Inverter driver


.. admonition:: Download
   :class: download

   \*\* Lab Resources:\*\*

   
   -  Fritzing files: :git-education_tools:`diode_bb <m2k/fritzing/diodes_bb>`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/diode_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a2_f1.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/i_vs_v_diode-wav.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/a2_e1.png
   :width: 100px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/a2_e2.png
   :width: 100px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/abs_val2-waveform.png
