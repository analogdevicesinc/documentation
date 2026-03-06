Activity: Envelope Detector
===========================

Objective
---------

In this lab activity we will use :adi:`ADALM2000 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm2000.html>` and :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>` to introduce envelope detection and amplitude modulation. The signal's envelope is equivalent to its outline, and an envelope detector connects all the peaks in this signal. Envelope detection has numerous applications in the fields of signal processing and communications, one of which is amplitude modulation (AM) detection.

Amplitude modulation (AM) is a modulation technique used in electronic communication, most commonly for transmitting information via a radio carrier wave. In amplitude modulation, the amplitude (signal strength) of the carrier wave is varied in proportion to the waveform being transmitted. That waveform may, for instance, correspond to the sounds to be reproduced by a loudspeaker, or the light intensity of television pixels.

A typical **amplitude modulated signal** has the following equation:

:math:`s(t) = [1 + k cos(w_m t)] A cos(w_c t)`

where:

-   :math:`m(t) = k cos(w_m t)` - message signal
-   :math:`c(t) = Acos(w_c t)` - carrier signal
-  k - modulation index (typically varies between 0 and 1)
-  ω\ :sub:`m` - message frequency
-  A - carrier amplitude
-  ω\ :sub:`c` - carrier frequency

An envelope detector is an electronic circuit that takes a high-frequency signal as input and provides an output which is the envelope of the original signal. (ω\ :sub:`c` >> ω\ :sub:`m`)

It consists of two main elements:

-  Diode / rectifier - serves to enhance one half of the received signal over the other.
-  Low pass filter - required to remove the high frequency elements that remain within the signal after detection / demodulation. The filter usually consists of a very simple RC network but in some cases It can be provided simply by relying on the limited frequency response of the circuitry following the rectifier.

Materials
~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 2 - 1 KΩ resistor
| 2 - 1uF capacitor
| 2 - 1N914 diode

Envelope Detector
-----------------

Background
~~~~~~~~~~

Consider the circuit presented in Figure 1.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 1. Basic Envelope Detector Circuit


The capacitor in the circuit stores up charge on the rising edge, and releases it slowly through the resistor when the signal falls. The diode in series rectifies the incoming signal, allowing current flow only when the positive input terminal is at a higher potential than the negative input terminal.

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for the envelope detector circuit.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 2. Envelope Detector breadboard circuit


Procedure
~~~~~~~~~

Use the first waveform generator as source to provide the AM signal, with the following parameters:

-  k = 0.5
-  ω\ :sub:`c` = 10KHz
-  ω\ :sub:`m` = 100Hz
-  A = 3

To generate the AM signal use the math function from the Scopy signal generator. Set the record length to 20ms, the sample rate to 75MSPS and apply the following function: *(1+0.5*cos(2*pi*100*t))*3*cos(2*pi*100*100*t)*. The generated waveform is presented in Figure 3.

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   Figure 3. Generated AM signal


Configure the scope so that output signal is displayed on channel 1.

Disconnect the capacitor from the circuit and observe the output signal. A plot example is presented in Figure 4.

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   Figure 4. Positive Half of the generated AM signal


Without the capacitor connected, the circuit works like a positive half-wave rectifier that keeps the part of the signal that is above 0V.

Now connect the capacitor back to the circuit. A plot example is presented in Figure 5.

.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   Figure 5. Positive half wave Envelope


The obtained signal is the envelope of the positive half wave obtained previously. It is actually the 100 Hz message signal with some 10 KHz variations on it (introduced by the carrier signal).

Frequency Domain Spectrum
~~~~~~~~~~~~~~~~~~~~~~~~~

We can also view these signals in the frequency domain using the Spectrum Analyzer tool. First we can look at the 10 KHz carrier and 100 Hz message signals together (since both are present at the output of this circuit). Enable channel 1 and set the sweep range from 10 Hz to 15kHz. Run a single sweep. Enable markers 1 and 2 from the Markers tab and the Marker Table. Move each marker using "Prev Peak", "Next Peak" to set them on the carrier and the message signal. A plot example is presented in Figure 6.

.. container:: centeralign

   \ |image6|\


.. container:: centeralign

   Figure 6. Message and carrier signals


Set the Sweep range from 9 kHz to 11kHz. In Figure 7, the main peak is at the 10 KHz carrier frequency and there are the modulation side-bands +/- 100 Hz on either side of the carrier. (i.e. 9900 Hz and 10100 Hz).

.. container:: centeralign

   \ |image7|\


.. container:: centeralign

   Figure 7. Demodulated Carrier signal spectrum


Set the Sweep range from 20Hz to 180Hz. In Figure 8, the main peak is at the 100Hz message frequency.

.. container:: centeralign

   \ |image8|\


.. container:: centeralign

   Figure 8. Deodulated message signal spectrum


Since the frequency analysis is made on the output signal using a basic envelope detector circuit, we are able to see both the message and carrier signal. In contrast to the applied input signal, where the carrier amplitude is larger than the message amplitude, on the spectrum analyzer plot we can notice that, in terms of magnitude, the message signal (100 Hz) is emphasized with respect to the carrier signal (see Marker table).

Extended Envelope Detector
--------------------------

.. _background-1:

Background
~~~~~~~~~~

Consider the circuit presented in Figure 9.

.. container:: centeralign

   \ |image9|\


.. container:: centeralign

   Figure 9. Positive and negative Envelope Detector Circuit


A similar circuit is added to the circuit in Figure 1 , the only difference being that the diode is reversed, allowing the negative voltages to pass through the RC circuit.

.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for the extended envelope detector circuit.

.. container:: centeralign

   \ |image10|\


.. container:: centeralign

   Figure 10. Extended Envelope Detector breadboard circuit


.. _procedure-1:

Procedure
^^^^^^^^^

Use the first waveform generator as source to provide the AM signal, with the following parameters:

-  k = 0.5
-  ω\ :sub:`c` = 10KHz
-  ω\ :sub:`m` = 100Hz
-  A = 3

To generate the AM signal use the math function from the Scopy signal generator. Set the record length to 50ms and apply the following function: *(1+0.5*cos(2*pi*100*t))*3*cos(2*pi*100*100*t)*. The generated waveform is presented in Figure 11. (with 5 displayed periods)

.. container:: centeralign

   \ |image11|\


.. container:: centeralign

   Figure 11. Generated AM signal


Configure the scope so that output signal is displayed on channel 1.

Disconnect the capacitors C1 and C2 from the circuit and observe the output signal. A plot example is presented in Figure 12.

.. container:: centeralign

   \ |image12|\


.. container:: centeralign

   Figure 12. Positive Half and Negative Half of the generated AM signal


Without the capacitors connected, the circuit works like a positive half-wave rectifier and negative half-wave rectifier, separating the positive half from the negative one.

Now connect the capacitor back to the circuit. A plot example is presented in Figure 13.

.. container:: centeralign

   \ |image13|\


.. container:: centeralign

   Figure 13. Positive half wave Envelope and Negative half wave Envelope


The obtained signal is the envelope of the positive half wave and negative half wave obtained previously.

Questions
---------

1. What happens if the capacitor/resistor values are changed? Which are the drawbacks in this case?

2. For the circuit in Figure 1, if a resistor is added in series with the diode, between D1 and R1, how is the output affected? Explain the differences.

Extra Activity: Biased Envelope Detector
----------------------------------------

The simple diode based envelope detector of Figure 1 does not well or at all if the amplitude i.e. Swing is less than the forward turn voltage of the diode. It will suffer significant distortion on the negative half of the modulation signal for high modulation indexes (near 100%) when the diode is not fully turned on. A way around this limitation is to introduce a small DC bias to the diode. This small bias current moves to quiescent operating point of the circuit to right at the turn on point of the diode.

.. _materials-1:

Materials
~~~~~~~~~

| ADALM1000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 1.5 KΩ resistor (brown green red)
| 1 - 10 KΩ resistor (brown black orange)
| 1 - 20 KΩ resistor (red black orange)
| 2 - 1.0uF capacitor, C1, C2
| 1 - 2N3904 NPN transistor
| 1 - 1N914 diode

.. _background-2:

Background
~~~~~~~~~~

Consider the circuit shown in Figure 14.

.. container:: centeralign

   \ |image14|\


.. container:: centeralign

   Figure 14. Biased Envelope Detector circuit


The amplitude modulated signal is AC coupled into the Base of NPN transistor Q1 which is configured as an emitter follower. Voltage divider R1 and R2 along with diode D1 act to set the DC bias point of the AC coupled input (:doc:`DC restoration </wiki-migration/university/courses/electronics/text/chapter-7>`). Absent any modulated input the DC quiescent operating point seen at the emitter of Q1 will be the voltage at the junction of R1 and R2 minus the diode drop of D1 and the VBE of Q1. The base current of Q1 flows in diode D1 forward biasing it. During the positive half cycles of the modulated input D1 turns off and the input signal peaks charge filter capacitor C2. During the negative half cycles of the input signal transistor Q1 turns off and D1 turns on harder supplying the input current.

.. _hardware-setup-2:

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for the biased envelope detector circuit.

.. container:: centeralign

   \ |image15|\


.. container:: centeralign

   Figure 15. Biased Envelope Detector breadboard circuit


.. _procedure-2:

Procedure
~~~~~~~~~

Connect the circuit to 5V supply.

To test this circuit first use the same modulated signal you used in the simple diode envelope detector example. Compare the new design to the simple diode envelope detector. Using the same steps as earlier generate AM signals with smaller amplitudes / higher modulation indexes and compare the outputs of these two detector designs.

A plot example of the input and output waveforms for the biased envelope detector is presented in Figure 16.

.. container:: centeralign

   \ |image16|\


.. container:: centeralign

   Figure 16. Biased Envelope Detector waveforms


Further Reading
---------------

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/env_detector_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/env_detector_ltspice`
   


Additional resources:

-  :adi:`Understanding, Operating, and Interfacing to Integrated Diode-Based RF Detectors <en/technical-articles/integrated-diode-based-rf-detectors.html>`
-  :adi:`Amplitude Modulation of the AD9850 Direct Digital Synthesizer <media/en/technical-documentation/application-notes/AN-423.pdf>`
-  :adi:`Multipliers and Modulators <en/analog-dialogue/raqs/raq-issue-92.html>`
-  :adi:`Envelope and TruPwr RMS Detector <media/en/technical-documentation/data-sheets/ADL5511.pdf>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/env_detector_ltspice.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/env_detector-bb.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/env_detector-wgen.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/env_detector-wav1.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/env_detector-wav2.png
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/env_detector-freq1.png
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/env_detector-freq3.png
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/env_detector-freq2.png
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/ext_env_det.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/ext_env_detector-bb.png
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/ext_env_detector-wgen.png
.. |image12| image:: https://wiki.analog.com/_media/university/courses/electronics/ext_env_detector-wav1.png
.. |image13| image:: https://wiki.analog.com/_media/university/courses/electronics/ext_env_detector-wav2.png
.. |image14| image:: https://wiki.analog.com/_media/university/courses/electronics/bias_env_detector.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/university/courses/electronics/bias_env_detector-bb.png
.. |image16| image:: https://wiki.analog.com/_media/university/courses/electronics/bias_env_detector-wav.png
