Activity: Common Emitter Amplifier Loop Gain
============================================

Objective:
----------

The objective of this Lab activity is to apply the Voltage Injection Method, that was introduced in the lab activity to :doc:`measure the loop gain </wiki-migration/university/courses/electronics/electronics-lab-loop-gain>` of an inverting op-amp stage, to measure the loop gain of a common emitter amplifier with negative feedback biasing and Miller capacitor.

Background:
-----------

Negative feedback is commonly used in control systems. Figure 1 shows a simple system with negative feedback.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1 Negative feedback system


The output voltage is related to the input voltage by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_e1.png
   :align: center
   :width: 200px

This is the closed loop transfer function. T(S) is called the loop gain which is the product of all gains around the loop and equals in this case to T(S) = G(S)H(S).

With the loop gain we can apply the Nyquist stability criterion to measure the gain and phase margin and determine the overall stability of the closed loop system.

The loop gain of a system can be derived from a mathematical model of the system. Such models often do not consider all the parasitics and unwanted effects that might exist in the real system. It can be very useful to measure the loop gain of a negative feedback system during the design process.

Loop Gain Measurement
~~~~~~~~~~~~~~~~~~~~~

**To Review:** One method to measure the loop gain in negative feedback systems is the voltage injection method. The following shows how the voltage injection method can be applied in practice and what has to be considered to achieve correct results.

Using a suitable injection transformer ( the ADALP2000 Analog Parts kit contains a HPH1-1400L ) we can inject a test voltage at an appropriate injection-point in the feedback loop of the system. Then the response of the loop can be measured using a network analyzer like the ADALM2000.

Figure 2 shows a setup using the voltage injection method to measure the loop gain of a feedback system. A low value resistor is inserted in the feedback loop at the injection-point. The injection transformer secondary winding is connected across the injection resistor to apply the test voltage. This allows the injection of a test voltage without changing the DC-bias operating point of the system.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Voltage Injection Method


The network analyzer inputs are connected to both sides of the injection resistor using voltage probes. The loop gain is then measured by measuring the complex voltage gain from point A to B.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_e2.png
   :align: center
   :width: 140px

Where T(S) is the measured loop gain and V\ :sub:`Sig` and V\ :sub:`Ref` are voltages measured by the network analyzer.

The measured loop gain, T(S) approximately equals the actual loop gain if the following two conditions are met.

| Condition 1
| The impedance looking forward around the feedback loop ( Z\ :sub:`IN`\ (S) of block H(S) ) is much greater than the impedance looking backwards from the injection point ( Z\ :sub:`OUT`\ (S) of block G(S) ).

:math:`|Z_IN (S)| >> |Z_OUT (S)|`

| Condition 2
| The second condition that must be fulfilled to ensure that the measured loop gain equals approximately the real loop gain is:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/amlg_e3.png
   :align: center
   :width: 200px

From these conditions we see that it is important to choose a suitable injection point that fulfills both conditions.

The first condition is often fulfilled at the output of an op-amp for example which is normally a low impedance. Other suitable points are generally at high impedance inputs like op-amp inputs.

The second condition is more difficult to check. Especially small loop gain results, above the crossover frequency need to be checked very carefully.

The magnitude of the injection voltage should be kept as low as possible to avoid large signal effects as saturation or other nonlinearities will influence the measurement.

The size of the injection resistor does not directly influence the measurement result if it is kept relatively small 50? or less is a good number.

The frequency response of the transformer and the dynamic range of the network analyzer will limit the loop gain measurement. In the lab set up below you will be using the HPH1-1400L transformer that has a usable frequency response of perhaps 10 KHz to 5 MHz. To measure loop response at lower frequencies a transformer with much higher winding inductance will be needed. The HPH1-1400L, or similar wide band transformers like a T1-6T ( Minicircuits ) or WB1010 ( Coilcraft ) should be sufficient to observe the loop response near the unity gain ( 0 dB ) frequency of the common emitter amplifier configurations used in this lab activity.

Using negative ( shunt ) feedback for bias
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Chapter 9 section 7 </wiki-migration/university/courses/electronics/text/chapter-9>` of the online Electronics I text introduced a biasing technique for the common emitter amplifier, called shunt feedback. This is accomplished by the introduction of some fraction of the collector signal back to the input at the base. This is done via the biasing resistor (R\ :sub:`B`), as shown in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/acelg_f3.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 3, Common emitter amplifier with shunt feedback bias


The negative feedback loop from the output at the collector and the input at the base can be broken at three different points to inject the test voltage as shown in figure 4. Scheme ( a ) breaks the loop by inserting the test voltage in series with the collector of the transistor. Scheme ( b ) breaks the loop in series with the feedback resistor between the output ( junction of the collector and R\ :sub:`C` ) and R\ :sub:`B`. The third scheme ( c ) inserts the test voltage between the feedback resistor and the base of the transistor. Each of these schemes meets Condition 1 above to a greater or lesser extent and will give slightly different results for the loop response.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/acelg_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 Three test voltage injection points


Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 2 - 10 Ω resistors
| 1 - 100 Ω resistor
| 1 - 470 Ω resistor
| 1 - 2.2 KΩ resistor
| 1 - 3.3 KΩ resistor
| 2 - 4.7 KΩ resistors
| 1 - 10 KO resistor
| 1 - 47 KΩ resistor
| 1 - 2N3904 NPN transistor ( or equivalent )
| 1 - 39 pF capacitor
| 1 - 100 pF capacitor
| 1 - 470 pF capacitor
| 1 - HPH1-1400L transformer ( or transformers, T1-6T from Minicircuits, WB1010 from Coilcraft )

Directions:
~~~~~~~~~~~

Build the measurement setup as shown in figure 5 below. If you are using the HPH1-1400L transformer for T\ :sub:`1` you should connect three of the 6 windings in series for the primary and the remaining three windings in series for the secondary ( see this :doc:`Transformers </wiki-migration/university/courses/alm1k/alm-lab-transformers>` for more details ).

There are three resistors, R\ :sub:`C`, R\ :sub:`B`, R\ :sub:`E` and one capacitor, C\ :sub:`M`, that determine the loop gain of this circuit. You will be running frequency sweeps with the network analyzer testing various combinations of component values.

Voltage divider R\ :sub:`2` and R\ :sub:`3` serves two purposes. First the 10 Ω R\ :sub:`2` matches the impedance of the resistor inserted in the feedback loop, R\ :sub:`1`. The AWG in the ADALM2000 cannot directly drive the 10 Ω resistor so the 100 Ω R\ :sub:`3` increases the load resistance to a value high enough for the AWG to safely drive. The attenuation of the divider also allows us to set the amplitude of the AWG high enough to provide a low noise signal while still injecting a small signal into the loop.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/acelg_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5 CE Loop Gain measurement setup


When building an experiment on a solder-less breadboard, you add the small (stray) capacitor between adjacent rows of connection points to the circuit. This is because the way the solder-less breadboard is built, it has rows of metal connection strips laid side by side (0.1 inch apart) separated by plastic dividers. Because the strips are fairly long and they are in parallel, they have a significant capacitance between them ( see this activity on :doc:`solder-less breadboard stray capacitance </wiki-migration/university/courses/electronics/electronics-lab-breadboard-coupling>` for more details ). This stray capacitance will appear in parallel with Miller feedback capacitor C\ :sub:`M` between the collector and the base.

When building this circuit it is recommended to leave a blank ( floating ) row between the collector and base pins of the NPN transistor. The 2N3904 devices has a pin order of EBC with the base in the center. Other types of transistors may have a ECB pin order with the collector in the center. In either case it is best to leave a blank row between both outer pins and the center pin. To see the effect of this stray capacitance after completing the lab re-build your circuit with the collector and base leads of Q\ :sub:`1` plugged into adjacent rows on the breadboard and remeasure the response with no C\ :sub:`M`.

Hardware Setup:
~~~~~~~~~~~~~~~

The green squares indicate where to connect the ADALM2000 AWG, scope channels and power supplies. Be sure to turn on the power supplies only after you double check your wiring.

Open the voltage supply control window to turn on and off the fixed +5 volt power supply. Open the Network Analyzer Instrument and set the sweep to start at 10 KHz and stop at 5 MHz. The Max gain should be set to 0.1X. Set the Amplitude to 3.5 V peak-to-peak and the Offset to zero volts. Under the Bode scale set the magnitude top to 40 dB and range to 80 dB. Set the phase top to 180º and range to 360º. Under scope channels click on use channel 1 as reference. Set the number of steps to 500.

Procedure:
~~~~~~~~~~

For your first measurements, start with R\ :sub:`C`\ equal to 10 KΩ, R\ :sub:`B` equal to 2.2 KΩ and R\ :sub:`E` equal to 0 Ω ( short with a wire jumper ). With C\ :sub:`M` equal to 0 pF ( open, no capacitor inserted ). Turn on the power supplies and run a single sweep. Note the frequency where the loop gain is unity ( 0 dB ) and the phase at that frequency. This configuration should result in a unity gain frequency actually beyond the 10 MHz frequency sweep range and you will need to extrapolate based on the slope of the gain curve. Be sure to export the sweep data to a .csv file for further analysis in either Excel or Matlab.

Be sure to turn off the power supplies before changing resistors or capacitors in your circuit. Now insert a 39 pF capacitor for C\ :sub:`M`. Turn on the power supplies and run a single sweep. Note the new frequency where the loop gain is unity ( 0 dB ) and the phase at that frequency and compare this to the measured ( extrapolated) result for no C\ :sub:`M`. Be sure to export the sweep data to a .csv file for further analysis in either Excel or Matlab. Now replace C\ :sub:`M` with a 100 pF capacitor. Run a single sweep. Note the new frequency where the loop gain is unity ( 0 dB ) and the phase at that frequency and compare this to the measured result for the with C\ :sub:`M` equal to 39 pF. Do another sweep with C\ :sub:`M` equal to 470 pF if you have one. Again compare the 0 dB frequency with your other measurements. Can you predict the 0 dB frequency based on the value of C\ :sub:`M`?

Next replace R\ :sub:`B` with a 3.3 KΩ or 4.7 KΩ depending on which value(s) you have available. Remove CM going back to a "0 pF" value. Be sure to turn off the power supplies before changing resistors in your circuit. Turn on the power supplies and run a single sweep. Note the new frequency where the loop gain is unity ( 0 dB ) and the phase at that frequency and compare this to the measured result for the with R\ :sub:`B` equal to 2.2 KΩ. Again go through the procedure of taking measurements for as many values of CM as you did in the first step. Be sure to export the sweep data to a .csv file for further analysis in either Excel or Matlab.

For extra credit try other values for R\ :sub:`C` and also try inserting an actual resistor for R\ :sub:`E`. Good values to try for R\ :sub:`C` might be 6.8 KΩ and 20 KΩ. Good values to try for R\ :sub:`E` might be 68 Ω, 100 Ω, 470 Ω and 1 KΩ. Again how does changing these resistor values effect the loop response?

Another extra credit exercise would be to compare the measured response for the other two injection configurations (b) and (c) in figure 4 and explain why the results were different based on Condition 1 and Condition 2 discussed in the section on measuring loop gain above.

Questions:
~~~~~~~~~~

| Why did the unity gain frequency change for the cases with C\ :sub:`M` equal to 39 pF and 100 pF for the amplifier?
| Why did the unity gain frequency change for the case of the with R\ :sub:`B` equal to 4.7 KΩ vs. 2.2 KΩ?
| Why did the unity gain frequency change for the case with R\ :sub:`E` inserted?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  LTSpice files: :git-education_tools:`m2k/ltspice/ce_loop_gain_ltspice`
   


**For Further Reading:**

| Measurement of loop gain in feedback systems. Middlebrook, R.D. s.l. : International Journal of Electronics, 1975, Bd. 38. http:*scholar.google.com/scholar?cluster=5040596387593898653
  http:*\ en.wikipedia.org/wiki/Nyquist_stability_criterion
| http:*en.wikipedia.org/wiki/Phase_margin
  http:*\ en.wikipedia.org/wiki/Bode_plot
| http://www.edn.com/electronics-blogs/analog-bytes/4434609/Loop-gain-measurements-
| **Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**
