Lab Activity: Generating sine waves from triangle waves
=======================================================

Objective:
----------

The circuit we are evaluating in this lab activity generates an approximate sine wave from a triangle wave by using the properties of the differential pair of transistors contained in the SSM2212 NPN matched transistor pair. We know that the transconductance of a differential pair of transistors is defined as:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a_sin_e1.png
   :align: center
   :width: 250px

Where I\ :sub:`o` is the differential pair tail current, V\ :sub:`in` is the differential input voltage, and V\ :sub:`T` is the thermal voltage which is about 26 mV at room temperature.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - 10 KΩ resistor
| 4 - 4.7 KΩ resistors
| 1 - 2.2 KΩ resistor
| 2 - 220 Ω resistors
| 1 - 390 Ω resistor
| 1 - 500 Ω potentiometer
| 1 - 100 pF capacitor
| 2 - Small signal NPN transistors (SSM2212 NPN matched pair)
| 1 - Opamp (OP27 )

Description:
------------

Construct the circuit in figure 1 on your solder-less breadboard. The +5 V ( pin 7 ) and -5 V ( pin 4 ) power supply connections for the OP27 amplifier were left off of the schematic but remember to connect them or the circuit will not function.

Procedure:
----------

| Set the AWG 1 to the Following:
| \* Amplitude (peak-to-peak) = 3.6V
| \* Offset = 0V
| \* Frequency = 1KHz
| \* Triangle wave
| Adjust the 500 Ω potentiometer, R\ :sub:`6`, for the best symmetry in the output sine wave shape. Using the FFT display and looking for the minimum even order distortion may be a good way to test the quality of the output sine wave. You may want to adjust the amplitude and DC offset of the input triangle wave to see if that can improve the odd order harmonics in the output.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a_sin_f1.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 1, Differential pair triangle to sine converter


In the case of this circuit, the output voltage will be approximately:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a_sin_e2.png
   :align: center
   :width: 200px

Where RL is the 4.7 KΩ load resistors on the output. The division by 2 happens because we only taking a single ended output, not a differential output.

So the output voltage will be a function of the input voltage and the hyperbolic tangent. The first few terms of the Taylor series of the sine and hyperbolic tangent functions are:

Sine:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a_sin_e3.png
   :align: center
   :width: 150px

Hyperbolic Tangent:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a_sin_e4.png
   :align: center
   :width: 150px

Comparing the two Taylor series will see that they are both linear to first order. What this means is that if we apply a triangle wave to a differential pair with a hyperbolic tangent transfer function, and keep the amplitude low, that is on the order of 2V\ :sub:`T`, what you get out should be nearly indistinguishable from a sine wave. The purpose of the 2.2 kΩ resistor and the 220 Ω resistor at the input of the differential pair (base of Q\ :sub:`1`) is to attenuate the triangle wave signal from the AWG to operate the circuit in the range where the output is as low a distortion sine wave as possible.

Hardware Setup
--------------

Connect the circuit shown in figure 1 to a breadboard.


|image1|

.. container:: centeralign

   Figure 2, Differential pair triangle to sine converter breadboard connections


With the use of M2K, the output s shown below.



|image2|

.. container:: centeralign

   Figure 3, Differential pair triangle to sine converter Scopy plot


Triangle Wave Generator
-----------------------

To make a stand-alone sine wave generator we need to replace the ADALM2000 module AWG with a triangle wave generator. The AD654 voltage-to-frequency converter IC will be the basis of the triangle wave generator. The normal output of the AD654 is an open collector digital square wave signal. The internal timing circuit of the AD654 however uses a ramp generator and this internal ramp waveform is available in differential form across the external timing capacitor connected to pins 6 and 7 in figure 2. We cannot use this triangle wave signal directly without disturbing the internal timing of the AD654. We can use the AD8226 instrumentation amplifier to buffer and convert the differential signal to a single ended signal. By adjusting the amplitude of this triangle wave signal, we can use it to drive the triangle wave to sine wave converter circuit from figure 1.

.. _materials-1:

Materials:
----------

| 2 - 1 KΩ resistors
| 1 - 47 KΩ resistor
| 1 - 6.8 KΩ resistor
| 1 - 220 Ω resistor
| 1 - 5 KΩ potentiometer
| 1 - 0.1 uF capacitor
| 1 - 1 uF capacitor
| 1 - Red LED
| 1 - AD654 V-to-F converter
| 1 - AD8226 IN-AMP
| 1 - Small signal NPN transistor (2N3904)

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a_sin_f2.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 4, V-to-F triangle wave generator


When connecting the triangle wave output from the AD8226 to the input of the triangle to sine converter, replace the 2.2 KΩ fixed resistor R\ :sub:`1` with a 5 KΩ potentiometer to adjust the signal amplitude for optimal sine wave shape.

.. _hardware-setup-1:

Hardware Setup
--------------

Connect the circuit shown in figure 4 to a breadboard.


|image3|

.. container:: centeralign

   Figure 5, V-to-F triangle wave generator breadboard connections


With the use of M2K, the output s shown below. We can adjust the gain resistor of the in-amp (R16) so that the output of the circuit will be in the range instrumentation amplifier supply. In the Scopy plot below, R16 is at 168kΩ.



|image4|

.. container:: centeralign

   Figure 6, V-to-F triangle wave generator Scopy plot


.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/diffpair_triangle_to_sine_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/diffpair_triangle_to_sine_ltspice`
   


For further reading:
~~~~~~~~~~~~~~~~~~~~

| Wikipedia page on the hyperbolic tangent, http://en.wikipedia.org/wiki/Hyperbolic_function
| Application Note: http://www.analog.com/static/imported-files/application_notes/444186898AN278.pdf

**Return to Lab Activities** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a_sin_nf2.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a_sin_nf3.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/a_sin_nf5.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/a_sin_nf6.png
   :width: 500px
