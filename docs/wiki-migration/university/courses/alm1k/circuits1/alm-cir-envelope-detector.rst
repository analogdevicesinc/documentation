Activity: AM Modulation and the Envelope Detector
=================================================

Objective:
----------

In this lab activity we will use the :adi:`ADALM1000 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm1000.html>` to introduce amplitude modulation (AM) and envelope detection demodulation. A signal's envelope is equivalent to its outline, and an envelope detector connects the amplitude peaks of the signal. :doc:`Envelope detection </wiki-migration/university/courses/electronics/text/chapter-7>` has numerous applications in the fields of signal processing and communications, one of which is amplitude modulation (AM) detection or demodulation.

Amplitude modulation (AM) is a modulation technique used in electronic communication, most commonly for transmitting information via a radio frequency carrier wave. In amplitude modulation, the amplitude (signal strength) of the carrier wave is varied in proportion to the waveform being transmitted. That waveform may, for instance, correspond to the sounds to be reproduced by a loudspeaker, or the light intensity of television pixels.

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

-  Diode / rectifier - serves to pass one half of the received signal over the other.
-  Low pass filter - required to remove the high frequency content that remains in the signal after detection / demodulation. The filter can consist of a very simple RC low pass filter network but in some cases It can be provided simply by relying on the limited frequency response of the circuitry following the rectifier.

Materials:
~~~~~~~~~~

| ADALM1000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 10 KΩ resistor (brown black orange)
| 2 - 0.1uF capacitors (104)
| 1 - 1N914 diode

Envelope Detector
-----------------

Consider the circuit presented in Figure 1. Two 0.1 uF capacitors are used in parallel to form a 0.2 uF total capacitance which along with the 10 KΩ resistor for a simple low pass filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-envel-det-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Envelope Detector Circuit


The capacitor in the circuit stores up charge on the rising edge, and releases it slowly through the resistor when the signal falls. The diode in series rectifies the incoming signal, allowing current flow only when the positive input terminal is at a higher potential than the negative input terminal.

Hardware Setup:
^^^^^^^^^^^^^^^

Build the circuit from figure 1 on your solderless breadboard for the envelope detector. Leave the CH A and CH B connections to the ADALM1000 disconnected for now while we generate an amplitude modulated test signal.

Procedure:
^^^^^^^^^^

We will use the channel A waveform generator as source to provide the AM signal, with the following parameters:

-  Min = 1.7
-  Max = 3.3
-  Freq = 100Hz

We will use the channel B waveform generator as source to provide the carrier signal, with the following parameters:

-  Min = 1.5
-  Max = 3.5
-  Freq = 10KHz

With both CH A and CH B set to SVMI mode and Shape Sine you should see waveforms something like those shown in figure 2. Set the Horizontal time scale to 2.0 mSec/Div to display 2 cycles of the 100 Hz waveform.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-envel-det-fig2.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 2, Generated modulating and carrier signals


To generate the modulated signal we will use the Math function from the ALICE signal generator CH A. With the program paused, select the Math option under the Shape drop down menu. Enter the following equation which multiplies the captured modulation waveform from channel A with the captured carrier waveform from channel B. Because the signals are centered on 2.5 V that DC portion of the waveforms much be subtracted out. The 2.5 volt offset is then added back to after the multiplication to center the modulated signal in the 0 to 5 V range of the ALM1000.

(VBuffA-0.6)*(VBuffB-2.5)+2.5

The generated waveform is presented in Figure 3 as the green trace from CH A. Disconnect the capacitors from the circuit and observe the output signal. With CH B in the Hi Z mode connect it both CH-A and CH-B to your circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-envel-det-fig3.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 3, Positive Half of the generated AM signal


Use the vertical range and position controls to shift the traces so that they don not overlap each other. This make it easier to see the two waveforms. Without the capacitor connected, the circuit works like a positive half-wave rectifier that keeps the part of the signal that is above 2.5 V.

Now connect the capacitors back to the circuit. A plot example is presented in Figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-envel-det-fig4.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 4, Filtered demodulated signal


The resulting demodulated signal is the envelope of the positive half wave obtained previously. It is actually the 100 Hz message signal with some 10 KHz ripple on it.

Frequency Domain Spectrum
-------------------------

We can also view these signals in the frequency domain using the Spectrum Analyzer tool. First we can look at the 10 KHz carrier and 100 Hz modulating signals separately. Configure the CH A and CH B signal generators as they were back in the first step where they were both set to sine shape and in SVMI mode. Disconnect both channels from your circuit so that they don't interfere with each other.

Open the Spectrum analyzer tool. Set the Cut-DC option to on. Select the CA-dBV and CB-dbV curves for display. Set the Start frequency 100 and the Stop frequency to 50000 with the log frequency scale. Set the number of samples to 16384. With the analyzer running you should see something like the spectrum shown in figure 5.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-envel-det-fig5.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 5, Carrier and modulating signal spectrum


As we can see we have the single peak at 100 Hz of the modulating signal on CH-A and the single peak at 10 KHz of the carrier signal on CH-B.

Now regenerate the Math modulated waveform in Channel A. You can reconnect CH-A and CH-B to your circuit and put CH-B back in Hi-Z mode. Now if we zoom into the channel A spectrum by setting the start frequency to 8000 and the stop frequency to 12000 we can see, in figure 6, the main peak is at the 10 KHz carrier frequency and there are the modulation side-bands +/- 100 Hz on either side of the carrier. (i.e. 9900 Hz and 10100 Hz.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-envel-det-fig6.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 6, Modulated Carrier signal spectrum


With the filter capacitor, if we look at the spectrum of the demodulated signal after the envelop detector we see the large peak at 100 Hz and a greatly attenuated peak at the 10 KHz carrier frequency as shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-envel-det-fig7.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 7, Filtered Demodulated signal after envelope detector spectrum


Biased Envelope Detector
------------------------

The simple diode based envelope detector of figure 1 does not perform well or at all if the amplitude i.e. Swing is less than the forward turn voltage of the diode. It will suffer significant distortion on the negative half of the modulation signal for high modulation indexes (near 100%) when the diode is not fully turned on. A way around this limitation is to introduce a small DC bias to the diode. This small bias current moves to quiescent operating point of the circuit to right at the turn on point of the diode.

.. _materials-1:

Materials:
~~~~~~~~~~

| ADALM1000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 1.5 KΩ resistor (brown green red)
| 1 - 10 KΩ resistor (brown black orange)
| 1 - 20 KΩ resistor (red black orange)
| 1 - 0.22uF capacitor, C\ :sub:`1` (224)
| 1 - 1.0uF capacitor, C\ :sub:`2`
| 1 - 2N3904 NPN transistor
| 1 - 1N914 diode

On your solder-less breadboard construct the biased envelope detector circuit as shown in Figure 8. The amplitude modulated signal is AC coupled into the Base of NPN transistor Q\ :sub:`1` which is configured as an emitter follower. Voltage divider R\ :sub:`1` and R\ :sub:`2` along with diode D\ :sub:`1` act to set the DC bias point of the AC coupled input (:doc:`DC restoration </wiki-migration/university/courses/electronics/text/chapter-7>`). Absent any modulated input the DC quiescent operating point seen at the emitter of Q\ :sub:`1` will be the voltage at the junction of R\ :sub:`1` and R\ :sub:`2` minus the diode drop of D\ :sub:`1` and the V\ :sub:`BE` of Q\ :sub:`1`. The base current of Q\ :sub:`1` flows in diode D\ :sub:`1` forward biasing it. During the positive half cycles of the modulated input D\ :sub:`1` turns off and the input signal peaks charge filter capacitor C\ :sub:`2`. During the negative half cycles of the input signal transistor Q\ :sub:`1` turns off and D\ :sub:`1` turns on harder supplying the input current.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-envel-det-fig8.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 8. Biased Envelope Detector circuit


To test this circuit first use the same modulated signal you used in the simple diode envelope detector example. Compare the new design to the simple diode envelope detector. Using the same steps as earlier generate AM signals with smaller amplitudes / higher modulation indexes and compare the outputs of these two detector designs.

**For Further Reading:**

-  :adi:`Understanding, Operating, and Interfacing to Integrated Diode-Based RF Detectors <en/technical-articles/integrated-diode-based-rf-detectors.html>`
-  :adi:`Amplitude Modulation of the AD9850 Direct Digital Synthesizer <media/en/technical-documentation/application-notes/AN-423.pdf>`
-  :adi:`Multipliers and Modulators <en/analog-dialogue/raqs/raq-issue-92.html>`
-  :adi:`Envelope and TruPwr RMS Detector <media/en/technical-documentation/data-sheets/ADL5511.pdf>`

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
