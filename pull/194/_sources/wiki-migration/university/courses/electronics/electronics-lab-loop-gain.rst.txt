Activity: Measuring Loop Gain, For ADALM2000
============================================

Objective:
----------

The objective of this Lab activity is to apply the Voltage Injection Method using the ADALM2000 network analyzer and a transformer to measure the loop gain of a negative feedback system such an inverting op-amp gain stage.

Background:
-----------

Negative feedback is commonly used in control systems. Figure 1 shows a simple system with negative feedback.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Negative feedback system


The output voltage is related to the input voltage by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_e1.png
   :width: 200px

This is the closed loop transfer function. T(S) is called the loop gain which is the product of all gains around the loop and equals in this case to T(S) = G(S)H(S).

With the loop gain we can apply the Nyquist stability criterion to measure the gain and phase margin and determine the overall stability of the closed loop system.

The loop gain of a system can be derived from a mathematical model of the system. Such models often do not consider all the parasitics and unwanted effects that might exist in the real system. It can be very useful to measure the loop gain of a negative feedback system during the design process.

Loop Gain Measurement
~~~~~~~~~~~~~~~~~~~~~

One method to measure the loop gain in negative feedback systems is the voltage injection method. The following shows how the voltage injection method can be applied in practice and what has to be considered to achieve correct results.

Using a suitable injection transformer ( the ADALP2000 Analog Parts kit contains a HPH1-1400L ) we can inject a test voltage at an appropriate injection-point in the feedback loop of the system. Then the response of the loop can be measured using a network analyzer like the ADALM2000.

Figure 2 shows a setup using the voltage injection method to measure the loop gain of a feedback system. A low value resistor is inserted in the feedback loop at the injection-point. The injection transformer secondary winding is connected across the injection resistor to apply the test voltage. This allows the injection of a test voltage without changing the DC-bias operating point of the system.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Voltage Injection Method


The network analyzer inputs are connected to both sides of the injection resistor using voltage probes. The loop gain is then measured by measuring the complex voltage gain from point A to B.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_e2.png
   :width: 150px

Where T(S) is the measured loop gain and V\ :sub:`Sig` and V\ :sub:`Ref` are voltages measured by the network analyzer.

The measured loop gain, T(S) approximately equals the actual loop gain if the following two conditions are met.

Condition 1

The impedance looking forward around the feedback loop ( Z\ :sub:`IN`\ (S) of block H(S) ) is much greater than the impedance looking backwards from the injection point ( Z\ :sub:`OUT`\ (S) of block G(S) ).

:math:`|Z_IN (S)| >> |Z_OUT (S)|`

Condition 2

The second condition that must be fulfilled to ensure that the measured loop gain equals approximately the real loop gain is:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_e3.png
   :width: 200px

From these conditions we see that it is important to choose a suitable injection point that fulfills both conditions.

The first condition is often fulfilled at the output of an op-amp for example which is normally a low impedance. Other suitable points are generally at high impedance inputs like op-amp inputs.

The second condition is more difficult to check. Especially small loop gain results, above the crossover frequency need to be checked very carefully.

The magnitude of the injection voltage should be kept as low as possible to avoid large signal effects as saturation or other nonlinearities will influence the measurement.

The size of the injection resistor does not directly influence the measurement result if it is kept relatively small 50Ω or less is a good number.

The frequency response of the transformer and the dynamic range of the network analyzer will limit the loop gain measurement. In the lab set up below you will be using the HPH1-1400L transformer that has a usable frequency response of perhaps 10 KHz to 5 MHz. To measure loop response at lower frequencies a transformer with much higher winding inductance will be needed. The HPH1-1400L, or similar wide band transformers like a T1-6T ( Minicircuits ) or WB1010 ( Coilcraft ) should be sufficient to observe the loop response near unity gain ( 0 dB ) of some of the operational amplifiers supplied in the ADALP2000 Analog Parts Kit when connected as inverting gain stages with feedback resistor ratios ( H(S) ) or feedback factor of 1/2 to 1/11.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 2 - 10 Ω resistors
| 1 - 100 Ω resistor
| 2 - 1 KΩ resistors
| 1 - 10 KΩ resistor
| 1 - OP27 op-amp
| 1 - OP37 op-amp
| 1 - OP97 op-amp
| 1 - HPH1-1400L transformer ( or transformers, T1-6T from Minicircuits, WB1010 from Coilcraft )
| 2 - 0.1 uF Capacitors (used to de-couple the Vp and Vn power supplies)

Directions:
-----------

Build the measurement setup as shown in figure 3 below. Remember to supply power to the op amp, +5 V to pin 7 and -5V to pin 4 with 0.1uF capacitors used to de-couple the Vp and Vn power supplies ( not shown in schematic diagram for simplicity ). If you are using the HPH1-1400L transformer for T\ :sub:`1` you should connect three of the 6 windings in series for the primary and the remaining three windings in series for the secondary ( see this :doc:`activity on transformers </wiki-migration/university/labs/comms_lab_transformers_adalm2000>` for more details ). Resistor R\ :sub:`1` is set to 1 KΩ and R\ :sub:`2` is either 1 KΩ or 10 KΩ to test different loop gains with the three different op-amps. Voltage divider R\ :sub:`4` and R\ :sub:`5` serves two purposes. First the 10 Ω R\ :sub:`4` matches the impedance of the resistor inserted in the feedback loop, R\ :sub:`3`. The AWG in the ADALM2000 cannot directly drive the 10 Ω resistor so the 100 Ω R\ :sub:`5` increases the load resistance to a value high enough for the AWG to safely drive. The attenuation of the divider also allows us to set the amplitude of the AWG high enough to provide a low noise signal while still injecting a small signal into the loop.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 Loop Gain Measurement setup


Hardware Setup:
---------------

The green squares indicate where to connect the ADALM2000 module AWG, scope channels and power supplies. Be sure to turn on the power supplies only after you double check your wiring.

Open the voltage supply control window to turn on and off the fixed +5 and -5 volt power supplies. Open the Network Analyzer Instrument and set the sweep to start at 10 KHz and stop at 5 MHz. The Max gain should be set to 1X. Set the Amplitude to 3V peak-to-peak and the Offset to zero volts. Under the Bode scale set the magnitude top to 40 dB and range to 80 dB. Set the phase top to 180º and range to 360º. Under scope channels click on use channel 1 as reference. Set the number of steps to 500.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 4. Loop Gain Measurement breadboard circuit


Procedure:
----------

Start by using the lower bandwidth OP97 amplifier from the ADALP2000 Parts Kit for your first measurements. With both R\ :sub:`1` and R\ :sub:`2` equal to 1 KΩ. Turn on the power supplies and run a single sweep. Note the frequency where the loop gain is unity ( 0 dB ) and the phase at that frequency. Be sure to export the sweep data to a .csv file for further analysis in either Excel or Matlab.

A plot example is presented in Figure 5.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 5. Loop Gain Measurement plot


Next replace the OP97 amplifier with the higher bandwidth OP27 amplifier from the Parts Kit. Be sure to turn off the power supplies before removing the op-amp from your circuit. Turn on the power supplies and run a single sweep. Note the new frequency where the loop gain is unity ( 0 dB ) and the phase at that frequency and compare this to the measured result for the OP97. Be sure to export the sweep data to a .csv file for further analysis in either Excel or Matlab. Now replace R\ :sub:`2` with a 10 KΩ resistor. Run a single sweep. Note the new frequency where the loop gain is unity ( 0 dB ) and the phase at that frequency and compare this to the measured result for the OP27 with R\ :sub:`2` equal to 1 KΩ.

Next replace the OP27 amplifier with a OP37 amplifier from the Parts Kit. Be sure to turn off the power supplies before removing the op-amp from your circuit. Turn on the power supplies and run a single sweep. Note the new frequency where the loop gain is unity ( 0 dB ) and the phase at that frequency and compare this to the measured result for the OP27 with R\ :sub:`2` equal to 10 KΩ. Be sure to export the sweep data to a .csv file for further analysis in either Excel or Matlab.

Questions:
----------

Why did the unity gain frequency change for the case with R\ :sub:`2` equal to 1 KΩ for the OP97 vs. the OP27 amplifiers?

Why did the unity gain frequency change for the case of the OP27 with R\ :sub:`2` equal to 10 KΩ vs. 1 KΩ?

Why did the unity gain frequency change for the case with R\ :sub:`2` equal to 10 KΩ for the OP27 vs. the OP37 amplifiers?

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/loop_gain_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/loop_gain_ltspice`
   


**For Further Reading:**

| Measurement of loop gain in feedback systems. Middlebrook, R.D. s.l. : International Journal of Electronics, 1975, Bd. 38. http:*scholar.google.com/scholar?cluster=5040596387593898653
  http:*\ en.wikipedia.org/wiki/Nyquist_stability_criterion
| http:*en.wikipedia.org/wiki/Phase_margin
  http:*\ en.wikipedia.org/wiki/Bode_plot#Gain_margin_and_phase_margin
| http://www.edn.com/electronics-blogs/analog-bytes/4434609/Loop-gain-measurements-

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/loop_gain-bb.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/loop_gain-wav.png
