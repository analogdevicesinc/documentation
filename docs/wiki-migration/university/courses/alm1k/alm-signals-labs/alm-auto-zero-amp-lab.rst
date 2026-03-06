Activity: Auto-Zeroing Amplifier
================================

Objective:
----------

The objective of this lab activity is to explore switching or chopping techniques to auto-zero DC offsets from an amplifier stage. When the lowest offset and drift performance is a requirement, auto-zeroing (offset-cancelled) amplifiers may be the best solution.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

Background:
-----------

For the lowest offset and drift performance, auto-zeroing (offset-cancelled) amplifiers may be the only solution. The best bipolar amplifiers offer offset voltages of 25 μV and 0.1 μV/ºC drift. Offset voltages less than 5 μV with practically no measurable offset drift are obtainable by using autp-zeroing, albeit with some penalties.

A basic auto-zero amplifier circuit is shown in Figure 1. When the switches are in the "Z" (auto-zero) position, capacitors C2 and C3 are charged to the amplifier input and output offset voltage, respectively. When the switches are in the "S" (sample) position, V\ :sub:`IN` is connected to V\ :sub:`OUT` through the path comprised of R1, R2, C2, the amplifier stage, C3, and R3. The switching frequency is usually between a low of a few hundred Hz and a high of several kHz, and it should be noted that because this is a sampling system, the input frequency must be much less than one-half the switching (sampling) frequency in order to prevent errors due to aliasing.

The circuit spends 50% of its time capturing its own offset-and-drift error, and 50% of its time subtracting the captured error from the amplified input. The output is a square wave that’s only related to the input half the time. There are three main ways to deal with the square-wave output:

-  You can filter it, but that loses the advantage of being able to run the amplifier at high speed i.e. close to the switching frequency. The R1-C1 combination serves as an antialiasing filter. It is also assumed that after a steady state condition is reached, there is only a minimal amount of charge transferred during the switching cycles. The output capacitor, C4, and the load, RL, must be chosen such that there is minimal V\ :sub:`OUT` droop during the auto-zero half of the cycle.
-  You can add a track-and-hold circuit after the amplifier to capture output during the sample half of the cycle, and skip over the parts that drop to the common mode level (0V). However, the output is still only tracks the input half the time and you might introduce more offset and drift errors from the T/H stage.
-  You can use two offset-cancelled amps running out of phase with each other. When one is zeroing out its own error, the other is producing a valid output. That is called a "ping-pong amplifier", and provides a good mixture of offset error cancellation and less filtering on the output to remove switching frequency content. However, it is also more complex in that two complete amplifiers and switching network are needed.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/auto-zero-amplifier_fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1: Classic Chopper Amplifier


In this lab activity, a simple amplifier stage and a LTC1043 analog switch are used as elements of a auto-zero amplifier. A very simple amplifier stage with a large input to output offset that can be used to demonstrate the auto-zero concept is the :doc:`NPN emitter follower </wiki-migration/university/courses/alm1k/alm-lab-11>`.

Referring to the simulation schematic shown in figure 2, the various functions of this circuit can be identified. The NPN emitter follower consisting of Q1, R1 and R2 is used as an AC coupled amplifier stage by capacitors C1 and C2. The LTC1043 analog switch contains an oscillator that drives the single pole double throw (SPDT) switches. Switches at pins S1A and S2A function as a SPDT switch, alternately connecting the AC coupled input (at C1) of the amplifier stage to the input (source Vin) and a common mode level (+2.5V from source V3) through pin Ca+.

Switches pins S3A and S4A perform the same function alternately connecting the AC coupled output (at C2) of the amplifier stage to the output low pass filter (C3 and R3) and a common mode level (+2.5V) through pin Ca-.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/auto-zero-amplifier_fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Auto Zero amplifier simulation schematic


In operation, the input signal is modulated (shifted up to the switching frequency) by the input switches, amplified by the ac coupled amplifier stage, and then demodulated back down to DC by the output switches. The 20 kΩ, 2nF low pass filter minimizes the high frequency ripple in the output.

For Further Study:
~~~~~~~~~~~~~~~~~~

ADI Mini Tutorial on `Chopper Amplifiers <http://www.analog.com/static/imported-files/tutorials/MT-055.pdf>`__

Building a auto-zero amplifier
------------------------------

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 – LTC1043 analog switch
| 1 – 2N3904 NPN transistor
| 1 – 2N3906 PNP transistor
| 1 – 470Ω resistor
| 1 – 20 KΩ resistor
| 1 – 47 KΩ resistor
| 2 – 0.1 uF capacitors
| 2 – 1 nF capacitors
| 2 – 100 pF capacitors

Directions:
~~~~~~~~~~~

Connect the components on your breadboard as indicated in figure 3 to build one auto-zero amplifier section. The listed resistor and capacitor values should provide working results but you may like to experiment with the values of certain component to see how changes can affect your results.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/auto-zero-amplifier_fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, NPN follower Auto-Zero Amplifier


The switching frequency is set by changing the frequency of the internal oscillator in the LTC1043. Capacitor C4 will lower the frequency. A range of frequencies should be tested, connecting one 100 pF capacitor as C4 or two 100 pF capacitors in series and parallel will produce a range of frequencies. The highest value should lower it to around 20 KHz.

Auto-zero Amplifier DC Transfer Characteristic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Measure the transfer characteristic (DC gain) of the auto-zero amplifier by applying DC voltages between +1.5 V and +3.5 V to the input and measuring the output. This can be done manually using generator AWG1 with a DC wave shape and setting the Max value. Be sure to take sufficient data to determine the linear and nonlinear ranges of the transfer characteristic. To reduce data taking time, try using the waveform generator to provide a very low frequency (<< 100 Hz) triangle signal. For example, a 1.5V Min and 3.5V Max setting and 10 Hz frequency.

Chopper Amplifier Frequency Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Apply a sinusoidal signal of 1.5 to 3.5 volt swing to the input and measure the gain of the entire system from 100 to 20 KHz. Use the Bode Plotting tool to plot gain and phase vs. frequency for the entire system, paying special attention to the 1000 Hz to 20 KHz range and the region near the frequency of the switching clock.

Ping-Pong a second auto-zero amplifier
--------------------------------------

As was pointed out in the background section, two offset-cancelled amps running out of phase with each other can be used to reduce the filtering requirements at the output. When one is capturing its own error, the other is producing valid output. That’s called a ‘ping-pong amplifier’, and provides the best mix of offset cancellation and full-speed operation.

Build the second auto-zero amplifier as shown in figure 4 on your breadboard. Note that the amplifier stage used in this case is a PNP emitter follower. We do this to help reinforce the idea that any offset in the amplifier is zeroed out no matter if it is positive or negative.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/auto-zero-amplifier_fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, PNP follower Auto-Zero Amplifier


Test the second amplifier DC and AC response as you did the first one. Once you are convinced that it is working properly, you can connect the two inputs together, Pins 5 and 7 and the two outputs together, Pins 13 and 15. Now test the combined ping-pong amplifier DC and AC response with and without the output low pass filter.

Auto Zero Amplifier Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Report the waveforms taken for the AC Amplifier in response to DC inputs. Discuss and explain the salient features of this response.

Plot or present the DC transfer characteristic of the offset-cancelled amplifier. Discuss and explain the salient features of this characteristic. Was the output of the offset-cancelled amplifier what you expected? Include a Bode plot (gain/phase versus frequency) of the offset-cancelled Amplifier from the data taken above. Comment on the bandwidth of the amplifier and the gain near the switching frequency.

**For Further Reading:**

| :adi:`LTC1043 datasheet <media/en/technical-documentation/data-sheets/1043fa.pdf>`
| `MT-088: Analog Switches and Multiplexer Basics <http://www.analog.com/media/en/training-seminars/tutorials/MT-088.pdf>`__
| :adi:`Demystifying Auto-Zero Amplifiers—Part 1 <media/en/analog-dialogue/volume-34/number-1/articles/demystifying-auto-zero-amplifiers-part-1.pdf>`
| :adi:`Demystifying Auto-Zero Amplifiers—Part 2 <media/en/analog-dialogue/volume-34/number-1/articles/demystifying-auto-zero-amplifiers-part-2.pdf>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**
