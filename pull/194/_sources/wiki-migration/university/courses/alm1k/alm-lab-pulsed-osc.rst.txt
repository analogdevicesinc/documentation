Activity: Pulsed Oscillators
============================

Objective:
----------

The objective of this lab activity is to investigate the characteristic of an oscillator which produces a pulsed output (short burst of cycles) which is gated by an input square wave.

Background:
-----------

A sinusoidal (sine-wave) oscillator is will produce an output waveform at a predetermined frequency for an indefinite period of time; that is, it operates continuously. Many electronic circuits in equipment such as radar require that an oscillator be turned on for a specific period of time and that it remain in an off condition until required at a later time. These circuits are referred to as Pulsed Oscillators or Ringing Oscillators. They are nothing more than sine-wave oscillators that are turned on and off at specific times. Figure 1 shows the circuit diagram of a pulsed oscillator with the resonant tank in the emitter circuit. A positive input on V\ :sub:`Gate` makes Q\ :sub:`1` conduct heavily and current flows through L\ :sub:`1`; therefore no oscillations can take place. A negative-going input pulse (referred to as a gate) cuts off Q\ :sub:`1`, and the tank oscillates or rings until the gate input ends or until the ringing dies out or stops, whichever comes first.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/apulse_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Pulsed Oscillator


To see how this circuit operates, assume that the Q of the LC tank circuit is high enough to prevent damping. An output from the circuit is obtained when the input gate goes negative (T0 to T1 and T2 to T3). The remainder of the time (T1 to T2) the transistor conducts heavily and there is no output from the circuit. The width of the input gate controls the duration of the output signal. Making the gate wider causes the output to oscillate or ring for a longer time. The resonate frequency of the LC tank is given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/ata1_e1.png
   :align: center
   :width: 170px

There are several different varieties of pulsed oscillators for different applications. The schematic diagram shown in figure 1 is an emitter-loaded pulsed oscillator. The tank circuit could also be placed in the collector, in which case it is referred to as a collector-loaded pulsed oscillator. The difference between the emitter-loaded and the collector-loaded oscillator is in the output signal. The first cycle of an emitter-loaded NPN pulsed oscillator is negative. The first cycle of the collector-loaded pulsed oscillator is positive. If a PNP is used, the oscillator will reverse the direction of the first cycle of both the emitter-loaded and the collector-loaded oscillator.

You probably have noticed by now that feedback has not been mentioned in this discussion. Remember that positive feedback was a requirement for an oscillator to sustain oscillation. In the case of the pulsed oscillator, oscillations are only produced for a very short period of time. Note, however, that as the width of the input gate (which cuts off the transistor) is increased, the amplitude of the sine wave begins to decrease (dampen) near the end of the gate period because of the lack of feedback. If a long period of oscillation is required for a particular application, an oscillator circuit with feedback will be needed. The principle of operation remains the same except that the feedback network sustains the oscillation period for the desired amount of time.

Materials:
~~~~~~~~~~

| ADLM1000 module
| Solder-less breadboard
| Jumper wires
| 1 – small signal NPN transistor (2N3904)
| 1 – 100 KΩ resistor
| 1 – 1 mH indictor
| 1 – 1.0 uF capacitor
| 1 – 0.1 uF capacitor

Directions:
~~~~~~~~~~~

Build the pulsed oscillator circuit shown in figure 2 on your solder-less breadboard. The green squares indicate where to connect the ALM1000 AWG output and input channels and power supply. Be sure to only connect the power supply after you double check your wiring.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-pulsed-oscillator-fig2.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 2, Pulsed oscillator circuit


Hardware Setup:
~~~~~~~~~~~~~~~

Setup AWG CH A as a square wave with Min set to 1.5 and Max set to 3.5. Set the frequency to 500 Hz and the duty cycle to 20% ( square wave high for 20% of the period ). Set both vertical scales to 0.5 V/div and the time base to 1 mSec/div. Set the trigger on the falling edge of CA-V. Use AWG CH B in Split I/O mode and the BIN pin to measure the output of the oscillator.

Procedure:
~~~~~~~~~~

Connect the +5V power supply and hit Run button. Observe the output waveform. It should consist of a burst of a few cycles of sinewave starting at the falling edge of the AWG A square wave and ending on the rising edge.

Notice that the output sine wave swings positive and negative around the 2.5 V level where the bottom of the LC tank is connected. Measure the frequency of the output sinewave. Measure the peak to peak amplitude of the first and last cycle of the output sinewave burst. Change the Min/Max swing values of the input pulse and measure how the amplitude of the sinewave changes. Try adjusting the duty-cycle of the pulse as well.

How much has the amplitude fallen off from the start to the end of the burst? What causes the amplitude fall off with time.

Questions:
~~~~~~~~~~

How does the measured output sinewave frequency compare to what you calculate using the formula for an LC tank and the values for L and C you used? Does the amount of dampening of the output amplitude make sense based on the internal DC resistance of the inductor you used? If not what other factors might contribute to the dampening?

**For Further Reading:**

**Return to Lab Activity Table of Contents.**
