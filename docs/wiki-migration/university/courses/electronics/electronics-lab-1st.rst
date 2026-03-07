Activity: Op Amp Settling Time, For ADALM2000
=============================================

Settling Time Background:
-------------------------

The settling time of an amplifier or any signal chain for that matter is defined as the time it takes the output to respond to a step change in the input and come into, and remain within a defined error band around the final value, as measured relative to the 50% point of the input pulse, as shown in figure 1 below.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1st_f1.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 1: Settling Time


-   Error band is usually defined to be a percentage of the step 1%, 0.5%, 0.1%, etc.
-   Settling time is often non-linear; it may take 30 times as long to settle to 0.01% as to 0.1%.
-   Manufacturers often choose an error band which makes the op amp look good.

Unlike a Digital-to-Analog Converter, there is no obvious error band for an op amp (a DAC naturally has an error band of 1 LSB, or perhaps ±1 LSB). So, an appropriate band must be chosen and defined, along with other definitions, such as the step size (1 V, 5 V, 10 V, etc.). What is chosen will depend on the performance of the op amp, but since the value chosen will vary from device to device, comparisons are often difficult. This is true because amplifier settling is not as simple as a single pole RC system, and many different time constants may be involved. Examples are early op amps using dielectrically isolated (DI) processes. These had very fast settling to 1% of full-scale, but they took almost forever to settle to 0.1 %. Similarly, some very high precision op amps have thermal effects that cause settling to 0.001% or better to take tens of mSec, although they will settle to 0.025% in a few µSec.

It should also be noted that thermal effects can cause significant differences between short-term settling time (generally measured in nanoseconds) and long-term settling time (generally measured in microseconds or milliseconds). In many AC applications, long-term settling time is not important; but if as it is in DC data acquisition systems, it must be measured on a much different time scale that short-term settling time.

Measuring Settling Time:
~~~~~~~~~~~~~~~~~~~~~~~~

Measuring fast settling time to high accuracy is very difficult. Great care is required in order to generate fast, highly accurate, low noise, flat top pulses. Large amplitude step voltages will overdrive many oscilloscope front ends, when the input scaling is set for high sensitivity.

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 2 10 kΩ resistors
| 1 10 kΩ potentiometer
| 2 Schottky diodes (the 1N914 Si diodes supplied in the ADALP2000 Analog Parts Kit can be used but will not work as well)
| 1 OP27 op-amp
| 1 OP37 op-amp
| 1 OP97 ( slow settling amplifier )
| 2 0.1uF Capacitors (used to de-couple the Vp and Vn power supplies)

Directions:
~~~~~~~~~~~

Build the test setup as shown in figure 2 below. Remember to supply power to the op amp, +5 V to pin 7 and -5V to pin 4 with 0.1uF capacitors used to de-couple the Vp and Vn power supplies. This arrangement is useful in making settling time measurements on op amps such as this operating in the inverting mode. The signal at the "false summing node" ( the wiper of the potentiometer ) represents the difference between the output and the input signal, multiplied by the constant k., i.e. the Error signal.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1st_f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2: Measuring Settling Time Using a "False Summing Node"


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1st_e1.png
   :align: center
   :width: 175px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1st_e2.png
   :align: center
   :width: 100px

There are many subtleties involved in making this setup work reliably. The resistances should be low in value, to minimize parasitic time constants. The back to back Schottky diode clamps, D\ :sub:`1`, D\ :sub:`2` help prevent scope overdrive, and allow use of a high vertical sensitivity setting. Regular diodes such as the 1N914 types supplied in the Parts kit will clamp at a much higher voltage and may store more charge due to higher capacitance than Schottky diodes. With R\ :sub:`1` = R\ :sub:`2`\ =10kΩ, then k = 0.5. Thus the error band at the Error output will be 5 mV for 1% settling with a 1V input step.

Hardware Setup:
~~~~~~~~~~~~~~~

Waveform generator 1 should be configured for a 60 KHz square wave 1V amplitude peak-to-peak and 0 volt offset. Scope channel 1 is used to monitor the input square wave and should be set to 500 mV/div and used as the trigger source. Scope channel 2 is used to alternately measure the op amp output, V\ :sub:`2`, and the Error signal at the wiper of the potentiometer. Channel 2 should be set to 500 mV/div when observing the output of the amplifier but should be set to a more sensitive scale of 100 mV/div when observing the Error signal.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 3. Op Amp Settling Time breadboard circuit


Procedure:
~~~~~~~~~~

First use a OP27 amplifier from the Analog Parts Kit for your measurements. The potentiometer should be set near the center of its adjustment range beforehand and should be fine-tuned such that the flat portion of both halves of the signal are nearly equal and centered near 0 Volts, note figure 4. Export the Error waveform showing the settling to both rising and falling input steps for inclusion in your Lab report. You can also store the Error waveform, scope channel 2, for the OP27 as a reference waveform (R1) for future comparison to the settling response of other amplifiers.

Next replace the OP27 amplifier with a OP37 amplifier from the Parts Kit. Again export the Error waveform showing the settling to both rising and falling input steps for inclusion in your Lab report. Overlay the OP37 settling waveform with the saved reference waveform of the OP27. Compare the settling time and general characteristics of each. You should also again store the Error waveform, scope channel 2, for the OP37 as a reference waveform (R2) for future comparison.

Finally replace the OP37 with the much slower settling OP97 amplifier. Again export the Error waveform showing the settling to both rising and falling input steps for inclusion in your Lab report. Overlay the OP97 settling waveform with the saved reference waveforms of the OP27 and OP37. Compare the settling time and general characteristics of each.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/opamp_settling_time-wav.png
   :align: center

.. container:: centeralign

   Figure 4 Example settling waveforms


Questions:
~~~~~~~~~~

The faster amplifiers show a ringing settling characteristic. What circuit component(s) could you add to remove the ringing ( perhaps at the cost of a longer settling time )?

Try using lower value resistors for R\ :sub:`1` and R\ :sub:`2` ( 1KΩ for example ) and a lower value for the potentiometer ( 5KΩ or lower ). How does this change the settling waveforms you see if any?

Additional Background on settling time measurements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases, a second (very fast) amplifier stage may be used after the false summing node, to increase the Error signal level. Many modern digitizing oscilloscopes, such as the ADALM2000 module, are less sensitive to input overdrive and can be used to measure the Error waveform directly. This must be verified for each oscilloscope by examining the operating manual carefully. Note that a direct measurement allows measurements of settling time in both the inverting and non-inverting modes. An example of the output step response to a flat pulse input for the OP27 and OP97 op amps is shown in figure 3. Notice that the settling time to 1% is approximately 2.8 µSec for the OP27 and 4.2 µSec for the OP97.

In making settling time measurements of this type, it is also imperative to use a pulse source capable of generating a pulse of very fast rise and fall times and sufficient flatness. In other words, if the op amp under test has a settling time of 20 nSec to 0.1%, the applied pulse should settle to better than 0.05% in less than 5 nSec. This is beyond the capabilities of the AWG sources built into the ADALM2000 module.

This type of source can be expensive, but a simple circuit as shown in Figure 5 can be used with a reasonably flat generator to ensure a flat pulse output.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1st_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5: A Simple Flat Pulse Generator


The circuit in figure 4 works best if low capacitance Schottky diodes are used for D\ :sub:`1`, D\ :sub:`2`, D\ :sub:`3`, and the lead lengths on all the connections are minimized. A short length of 50Ω coax can be used to connect the pulse generator to the circuit, however best results are obtained if the test fixture is connected directly to the output of the generator. The pulse generator is adjusted to output a positive-going pulse at "A" which rises from approximately -1.8 V to +0.5 V in less than 5 nSec (assuming the settling time of the test device is in the order of 20 nSec). Shorter rise times may generate ringing, and longer rise times can degrade the test device settling time; therefore some optimization is required in the actual circuit to get best performance. When the pulse generator output "A" goes above 0 V, D\ :sub:`1` begins to conduct, and D\ :sub:`2`/D\ :sub:`3` are reversed biased. The "0V" region of the signal "B" at the input of the device to be tested is flat "by definition"-neglecting the leakage current and stray capacitance of the D\ :sub:`2`-D\ :sub:`3` series combination. The D\ :sub:`1` diode and its 100O resistor help maintain an approximate 50O termination during the time the pulse at "A" is positive.

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/opamp_settling_time_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/opamp_settling_time_ltspice`
   


For further reading:
~~~~~~~~~~~~~~~~~~~~

| :adi:`MT-046.pdf <media/en/training-seminars/tutorials/MT-046.pdf>`
| http://www.analog.com/static/imported-files/application_notes/466359863287538299597392756AN359.pdf
| `Settling time <https://en.wikipedia.org/wiki/Settling_time>`_

Return to Lab Activities :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/opamp_settling_time-bb.png
