Activity: Differential Temperature Sensor
=========================================

Objectives:
-----------

A diode's forward voltage drop, V\ :sub:`D`, decreases by approximately 2 mV for each 1º C rise in temperature, assuming a constant current in the diode. The circuit shown in figure 1 uses this property as the basis of a crude temperature sensor, differential temperature actually. It is best if the diodes are of the same type, ideally from the same manufacturer. Both diodes are forward-biased using equal resistor values to establish the same current, at least when the diodes are at the same temperature. Diode D\ :sub:`sense` serves as the temperature sensor while diode D\ :sub:`ref` serves as the temperature reference maintained at a constant temperature, say at room temperature (25º C) which is convenient. The difference in diode voltages V\ :sub:`Temp` is consequently proportional to the difference in temperature.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less Breadboard
| 2 - Resistors (1KΩ)
| 2 - small signal diode (1N914 or similar)

Directions:
-----------

Construct the circuit of figure 1 using two 1N914 diodes.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a25_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 differential temperature circuit


Hardware Setup:
---------------

Connect scope input 1+ to the positive terminal of V\ :sub:`Temp` and connect scope input 1- to the negative terminal of V\ :sub:`Temp`. Use the Scopy Voltmeter or Oscilloscope instruments to monitor the value of V\ :sub:`Temp` using the True RMS measurement display. Use auto-range for the Voltmeter or set the "Volts/Div" scale for the Oscilloscope to its most sensitive value (10 mV) and ensure that Channel 1 is enabled. Connect Vp to the 5V Power Supply.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/difftemp-bb.png
   :align: center

.. container:: centeralign

   Figure 2 Differential Temperature Breadboard Circuit


Procedure:
----------

1. Allow both diodes to reach the same temperature, i.e., T\ :sub:`sense` = T\ :sub:`ref` . Measure and record the voltage offset as V\ :sub:`Temp` set; subtract this offset voltage from your later measurements.


|image1|

.. container:: centeralign

   Figure 3 T\ :sub:`sense` = T\ :sub:`ref` Differential Temperature Waveform


2. Heat the sensor diode by squeezing it between your fingers. Wait for the voltage to stabilize, subtract V\ :sub:`Temp` set, and then record this value as the "body temperature" voltage. You might also try blowing through a straw to direct your warm breath at the sensor diode.



|image2|

.. container:: centeralign

   Figure 4 T\ :sub:`sense` > T\ :sub:`ref` Differential Temperature Waveform


3. If available, wrap the sense diode in a thin plastic bag and submerge it in ice water to chill the sensor diode. Again, wait for the voltage to stabilize, subtract V\ :sub:`Temp` set, and then record its value as the "freezing point of water" voltage.

4. Determine the sensitivity of the temperature sensor output V\ :sub:`Temp` in millivolts per ºC.

Questions:
----------

| Can you derive the sensitivity in mV/ºC you measured from the diode equation?
| What is the purpose of the reference diode in this configuration?
| This circuit only measures the difference in temperature not the absolute temperature of either diode. How could you use the temperature dependence of a simple diode circuit like this to determine the actual temperature of the sense diode ( i.e. relative to absolute zero )?
|

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/diff_temp_sensor_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/diff_temp_sensor_ltspice`
   


Further exploration:
--------------------

Try substituting a pair of diode connected (base and collector shorted together) NPN or PNP transistors from your ADALP2000 Analog Parts Kit. Does the differential voltage V\ :sub:`Temp` follow the same sensitivity in mV/ºC you measured from the diodes?

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/difftemp-wav1.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/difftemp-wav2.png
