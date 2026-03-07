An Introduction to Electrical Filters
=====================================

.. image:: https://wiki.analog.com/_media/analogTV>5087537094001
   :alt: analogTV>5087537094001
   :align: right

Introduction
------------

Most electrical filters are circuits that select certain bands of frequencies to pass along, or accept, and other bands of frequencies to stop, or reject. The frequency at which the transition between passing and rejecting input signals occurs is called the "cutoff" frequency, often abbreviated as f\ :sub:`C`. The band of frequencies that is passed is called the "passband" of the filter, also called the "bandwidth." We will be concerned with filters that operate on signal voltages. There are other types of filters that manipulate the phases of signals that pass through them, but we are not going to cover these in this lab. The simplest filters are constructed of two passive elements -- either a resistor and capacitor (RC), or a resistor and inductor (RL). Each of these two-element filters can be arranged to pass low frequencies and reject high frequencies, or pass high frequencies and reject low frequencies, depending upon which element the output voltage is taken across. Not surprisingly, the filters that pass low frequencies are referred to as "lowpass" filters and the filters that pass high frequencies are referred to as "highpass" filters.

A commonly-encountered arrangement of lowpass and highpass filters can be found in the crossover networks in two-way loudspeaker systems consisting of a low frequency driver called the woofer and a high frequency driver called the tweeter. The lowpass filter passes low frequencies to the woofer, which is designed to reproduce these frequencies, and rejects the high frequencies that the woofer cannot reproduce. Similarly, the highpass filter passes high frequencies to the tweeter, which it is designed to reproduce, and blocks the low frequencies that the tweeter cannot reproduce, or could even damage the tweeter. Ideally, the overall audio output from the loudspeaker system will cover the entire audio range, divided between the woofer and tweeter.

In this experiment we design and build a lowpass RC filter and a highpass RC filter using components available in the ADALP2000 Analog Parts Kit. The cutoff frequency of the lowpass filter is designed to be approximately 100 Hz, and the highpass filter cutoff frequency is designed to be approximately 200 Hz. It is important to note that the lopwass filter passes DC -- the ultimate low frequency signal -- while the highpass filter does not.

After building and testing the two filters we will construct two very simple circuits that detect when signals are approximately in each filter's passband, and drive a LED to indicate this. We can then connect the two filters together and sweep the frequency of the input signal from a very low frequency that is in the lowpass filter's passband but not in the highpass filter's passband up to a high frequency that is not in the lowpass filter's passband but is in the highpass filter's passband. We can then observe the LEDs switch on and off as a function of the input frequency.

Objective
---------

To study RC lowpass and highpass filters and design a simple circuit to detect the approximate amplitude of a signal and illuminate a LED when the amplitude is above a predetermined threshold. Upon completion of this lab you should be able to describe the basic operation of RC lowpass and highpass filters, describe the operation of a simple low-accuracy peak detector, explain what a voltage comparator is, and explain how the comparator output can drive a LED.

Materials and Apparatus
-----------------------

-  Data sheet handout for AD8561 voltage comparator
-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (2) AD8561 from the ADALP2000 Analog Parts Kit
-  (2) 1N914 diode from the ADALP2000 Analog Parts Kit
-  (1) Red LED from the ADALP2000 Analog Parts Kit
-  (1) Green LED from the ADALP2000 Analog Parts Kit
-  (2) 68 Ω resistor from the ADALP2000 Analog Parts Kit
-  (2) 100 Ω resistor from the ADALP2000 Analog Parts Kit
-  (2) 200 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (2) 10 KΩ potentiometer from the ADALP2000 Analog Parts Kit
-  (2) 10 μF capacitor from the ADALP2000 Analog Parts Kit
-  (1) 22 μF capacitor from the ADALP2000 Analog Parts Kit
-  (1) 47 μF capacitor from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Construct the following lowpass filter circuit on the solderless breadboard\


|lab_5_image_1.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_5_assembly_image_1b.png|

-  Run PixelPulse on the computer and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Connect the M1K to the circuit as indicated in the schematic
-  Set up PixelPulse to source voltage/measure current on Channel A and measure voltage on Channel B
-  Set up Channel A to source a 10 Hz sine wave that swings between 0 V and 5 V and verify that the voltage observed on Channel B is similar to that sourced on Channel A
-  Gradually increase the frequency of the sine wave sourced by Channel A to 1000 Hz, and observe the decrease in amplitude of the measured signal on Channel B
-  Adjust the frequency generated by Channel A until the peak-to-peak level of the waveform measured on Channel B is approximately 3.5 V and record this frequency
-  Modify the circuit on the solderless breadboard according to the following schematic\

|lab_5_image_2b.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_5_assembly_image_2b.png|

-  Set up Channel A to source a 10 Hz sine wave that swings between 0 V and 5 V and record the DC level measured on Channel B
-  Record the DC levels measured on Channel B for the following input frequencies (swinging 0 V to 5 V): 18 Hz, 32 Hz, 56 Hz, 100 Hz, 180 Hz, 320 Hz, 560 Hz, and 1000 Hz
-  Add the following highpass filter circuit to the solderless breadboard\

|lab_5_image_3.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_5_assembly_image_3b.png|

-  Set up Channel A to source a 10 Hz sine wave that swings between 0 V and 5 V and verify that the voltage observed on Channel B is much smaller than that sourced on Channel A
-  Gradually increase the frequency of the sine wave sourced by Channel A to 1000 Hz, and observe the increase in amplitude of the measured signal on Channel B
-  Adjust the frequency generated by Channel A until the peak-to-peak level of the waveform measured on Channel B is approximately 3.5 V and record this frequency
-  Modify the circuit on the solderless breadboard according to the following schematic\

|lab_5_image_4b.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_5_assembly_image_4b.png|

-  Set up Channel A to source a 10 Hz sine wave that swings between 0 V and 5 V and record the DC level measured on Channel B
-  Record the DC levels measured on Channel B for the following input frequencies (swinging 0 V to 5 V): 18 Hz, 32 Hz, 56 Hz, 100 Hz, 200 Hz, 320 Hz, 560 Hz, and 1000 Hz
-  Construct two comparator circuits on the solderless breadboard -- one for each of the two filters -- according to the following schematic (Use a RED LED for the lowpass filter and a GREEN LED for the highpass filter)\

|lab_5_image_5.png|

-  Connect the two filter inputs together and to Channel A of the M1K
-  Refer to the illustration below for one way to add the comparator circuitry to the existing filters constructed on the solderless breadboard\

|lab_5_assembly_image_5b.png|

-  Adjust the potentiometer in the lowpass filter comparator circuit to obtain a voltage at the wiper that is equal to the level measured earlier for a 100 Hz input frequency
-  Adjust the potentiometer in the highpass filter comparatorŗ circuit to obtain a voltage at the wiper that is equal to the level measured earlier for a 200 Hz input frequency
-  Set up Channel A to source a 10 Hz sine wave that swings between 0 V and 5 V
-  Gradually increase the frequency of the sine wave sourced by Channel A to 1000 Hz
-  Verify that the RED LED illuminates for frequencies between 10 Hz and approximately 100 Hz and turns off for higher frequencies, indicating the filter's lowpass response
-  Verify that the GREEN LED illuminates for frequencies between approximately 200 Hz and 1000 Hz and turns off for lower frequencies, indicating the filter's highpass response

Theory
------

Series RC circuits can realize the simplest lowpass and highpass filters that operate on voltages, though current-mode operation is also possible. The filter is lowpass when the output voltage is taken across the capacitor and is highpass when the output voltage is taken across the resistor. The filter operates as a two-element voltage divider between the resistance of the resistor, R, and the reactance of the capacitor, 1/2πfC. Since the capacitive reactance varies inversely with frequency, the voltage across the capacitor decreases with frequency, producing the lowpass frequency response. By Kirchhoff's Voltage Law, the voltage across the resistor increases with frequency in a complementary fashion to that of the capacitor, producing the highpass response. The cutoff frequency f\ :sub:`C` is defined as the frequency at which the capacitive reactance is equal to the resistance. Setting R = 1/2πf\ :sub:`C`\ C and solving for f\ :sub:`C` gives the following result.

:math:`\displaystyle f_C = \frac{1}{2} \pi RC`

At the cutoff frequency, the amplitude of the sinusoidal output voltage in response to a sinusoidal input voltage is equal to the reciprocal of the square-root of two times the input voltage amplitude, or about 70.7% of the input voltage amplitude.

The lowpass filter in the lab is comprised of a 68 Ω resistor and a 22 μF capacitor, and therefore has a cutoff frequency of approximately 106 Hz. Because of the tolerances of the resistor and capacitor, the actual cutoff frequency will deviate from this value. The frequency at which the peak-to-peak output amplitude was measured to drop from about 5 V to (0.707)*5 V ≈ 3.5 V in the lowpass filter part of the lab should have been close to 106 Hz.

The highpass filter in the lab is comprised of a 68 Ω resistor and a 10 μF capacitor, and therefore has a cutoff frequency of approximately 234 Hz. As with the lowpass filter, component tolerances will introduce a small cutoff frequency error. The frequency at which the peak-to-peak output amplitude was measured to drop from about 5 V to (0.707)*5 V ≈ 3.5 V in the highpass filter part of the lab should have been close to 234 Hz.

It's important to note that the resistor in the highpass filter is referenced to +2.5 V instead of ground. The highpass filter cannot pass DC, and it can therefore be viewed as a circuit the removes the DC level from its input signal. The DC level on the other side of the resistor sets the DC level on the output side of the highpasss filter as long as the output does not have a significant DC load. This is true because DC current cannot flow back through the capacitor and there is no significant load current, so the DC voltage drop across the resistor in the highpass filter is effectively zero. Placing the output DC level at 2.5 V places the output swing in the center of the M1K input range. If the resistor were referenced to ground, the highpass filter output would swing above and below ground, and the negative excursions would not be visible on the M1K.

After making basic characterizations of the filters, simple, rather inaccurate, peak detectors consisting of series diodes and shunt capacitors are added to the filter outputs in order to give a rough indication of the filter output level. The peak detector allows the capacitor to charge when the voltage out of the filter is greater than the capacitor voltage plus the forward diode drop. The diode is a nonlinear element with a varying forward voltage drop, so the capacitor will not be able to charge to the actual peak voltage out of the filter. Once the signal out of the filter passes its peak, the diode becomes reverse-biased and conducts very little current, allowing to the capacitor to hold a rough estimate of the peak level that includes the error due to the diode drop. The capacitor voltage does not stay perfectly constant while the diode is reverse biased because the diode leaks current when reverse biased, and current leaks into the M1K when the when the capacitor voltage is measured. The current leakages cause the capacitor voltage to sag during reverse-biased parts of the cycle. The sag is more noticeable for low frequency inputs when the reverse-biased times are long. This brings up an important dilemma that is encountered in all peak detectors. A small capacitor is desirable for fast charging times required in detecting the peaks of high frequency signals, but a large capacitor is required to achieve long hold times for low frequency signals. Ultimately, a compromise must be reached in selecting the capacitor value in a given application. Much more accurate peak detectors can be built using negative feedback circuits that remove the diode drop error from the measurement.

Since these peak detectors include errors, it is best to measure their outputs for various levels output from the filters. In the lab, frequencies roughly a quarter-decade apart are used to characterize the peak detectors. One of these frequencies is chosen to be approximately equal to the cutoff frequency of the respective filter -- 100 Hz for the lowpass filter and 200 Hz for the highpass filter. These peak detector output levels are used to set the threshold levels of the comparators that detect when the signals are in the filter passbands and drive the corresponding LEDs.

A comparator is a high-gain amplifier with a differential input and a binary output that is used to detect when input signals are above or below a predetermined threshold voltage. A comparator is similar to an operational amplifier that is set up in an open-loop configuration, though operational amplifiers should not be used as comparators for a number of reasons. There are many comparators on the market that are specifically designed to be operated open-loop and provide a specific type of digital logic output. Comparators can also be operated in a closed-loop positive-feedback configuration to produce hysteresis. Hysteresis is a feature in which the operation of the comparator depends on its history. It provides two thresholds -- a higher one for increasing inputs and a lower one for decreasing inputs. One of the major benefits of hysteresis is that it prevents the comparator output from "chattering" when the input signal is changing very slowly about the threshold. Hysteresis would be a nice feature in this application if the input frequencies were hovering near the filter cutoff frequencies, but it was not included for simplicity's sake. It is introduced and explained in the "Simple Proximity Detector" lab.

The comparators are set up with threshold voltages on their inverting inputs. The output logic goes to a "high" level when the voltage on the non-inverting input exceeds the threshold voltage by a small amount. We want to drive the LED when the threshold is exceeded, indicating that the input signal is in the filter passband, and it is best to drive the LED when the comparator output is in the "low" logic state. The AD8561 has true and complimentary outputs. The true output goes high when the input voltage exceeds the threshold voltage is exceeded and low when the input voltage is below the threshold voltage. The complementary output beaves in the opposite fashion. Since the complementary output goes "low" when the input voltage exceeds the threshold voltage, it is used to drive the LED. If the comparator only had a true output, the same result could be achieved by swapping the input signals, i.e., placing the threshold voltage on the non-inverting input and the input signal on the inverting input.

Observations and Conclusions
----------------------------

-  An electric filter is a circuit that passes certain frequencies and rejects other frequencies
-  The simplest filters consist of two elements, RC and RL
-  A lowpass filter passes low frequencies and rejects high frequencies
-  A highpasss filter passes high frequencies and rejects low frequencies
-  A highpass filter does not pass DC
-  RC and RL circuits can each be designed as simple lowpass or highpass filters
-  The passband of a filter is commonly defined as the band of frequencies for which the amplitude of the output signal ranges from 100% to 70.7% of the input amplitude
-  The end of the passband is called the cutoff frequency, f\ :sub:`C`
-  A simple, low-accuracy peak detector can be constructed using a diode and a capacitor
-  The diode drop introduces errors in the simple peak detector
-  A tradeoff must be made when selecting a capacitor for a peak detector -- smaller is better for high frequencies and larger is better for low frequencies
-  A comparator is a high-gain amplifier that is often used to provide a binary output indicating whether an input signal is above or below a predetermined threshold
-  Operational amplifiers should not be used as comparators

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`

.. |lab_5_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_5_image_1.png
   :width: 600px
.. |lab_5_assembly_image_1b.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_5_assembly_image_1b.png
   :width: 800px
.. |lab_5_image_2b.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_5_image_2b.png
   :width: 1000px
.. |lab_5_assembly_image_2b.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_5_assembly_image_2b.png
   :width: 800px
.. |lab_5_image_3.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_5_image_3.png
   :width: 600px
.. |lab_5_assembly_image_3b.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_5_assembly_image_3b.png
   :width: 800px
.. |lab_5_image_4b.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_5_image_4b.png
   :width: 1000px
.. |lab_5_assembly_image_4b.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_5_assembly_image_4b.png
   :width: 800px
.. |lab_5_image_5.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_5_image_5.png
   :width: 800px
.. |lab_5_assembly_image_5b.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_5_assembly_image_5b.png
   :width: 1000px
