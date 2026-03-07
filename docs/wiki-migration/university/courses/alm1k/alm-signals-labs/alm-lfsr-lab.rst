Activity: Linear Feedback Shift Register (LFSR), For ADALM1000
==============================================================

Objective:
----------

The objective of this lab activity is to explore the operation of the linear feedback shift register to generate pseudo-random sequences of binary numbers.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage/measure current –V is added as in CA-V or when configured to force current /measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

Background:
-----------

In digital signal processing, a linear-feedback shift register, or LFSR, is a shift register where the input bit is a linear function of its previous state.

A common linear function of single bits is the XOR. The XOR function can also be viewed as part of the digital addition function in that XORs are used as the Sum portion of the simplest form of the half adder. An LFSR is most often a shift register where the input bit is driven by the exclusive-or (XOR) of certain bits of the contents of the overall shift register.

The initial value of the LFSR is called the seed, and because the operation of the register is deterministic, the stream of output value it produces is completely determined by its current (or previous) state. In addition, because a register of finite length has a finite number of possible states, it must eventually enter a repeating cycle. A sufficiently long LFSR with a well-chosen feedback function can produce a sequence of bits which appears random and which has a very long cycle before repeating.

Both hardware and software implementations of LFSRs are common.

Applications of LFSRs include:

-   Data Encryption/Decryption
-   Digital Signal Processing
-   Wireless Communications
-   Built-in Self Test (BIST)
-   Test Pattern Generators
-   Data Integrity Checksums
-   Data Compression
-   Pseudo-random Number Generation (PN)
-   Pseudo-noise sequences
-   Direct Sequence Spread Spectrum
-   Scrambler/Descrambler
-   Optimized fast digital Counters

The mathematics of a cyclic redundancy check, used to provide a quick check against transmission errors, are closely related to those of an LFSR.

Materials:
----------

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 – 74HC273 Octal D-Type register or similar logic device
| 1 – 74HC86 Quad two input XOR gate (or XOR gate from CD4007 etc.)

Directions:
-----------

On your solder-less breadboard, build the linear feedback shift register circuit shown in figure 1, with the feedback taken at the 3rd and 4th bits. The 74HC273 octal D-type register is used to make (up to) an 8 bit shift register as shown but any other similar shift register with parallel outputs could be substituted. A two input XOR gate can also be constructed using individual logic gates or the CD4007 CMOS transistor array as shown in the lab activity on the :doc:`XOR gate </wiki-migration/university/courses/alm1k/alm-lab-30>`. Connect the positive 5 volt power and ground to the circuit as shown. Be sure that both digital chips receive power and ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-lfsr-fig_1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Linear-feedback shift register circuit


Hardware Setup:
---------------

Connect the +5 V power supply only after you have double checked your wiring. AWG channel A is used to provide the input clock at pin 11 of the shift register. Set channel A to SVMI mode with Min value of 0 and Max value of 5. Set the Frequency to 1000 (1KHz). Set the shape to Square. Set channel B to Hi-Z mode to observe the bit outputs at the shift register outputs and the XOR gate output.

Procedure:
----------

Start the ALICE Desktop software. Connect the channel B scope input to any one of the shift register outputs. Hit the Run button. You should see a string of pulse of what looks like randomly changing width. We can use a low pass filter to get an idea as to the average width, or length of time, the output is high or low. A simple RC low pass stage as shown in figure 2 can be used to generate an analog representation of the average.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-lfsr-fig_2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, Low pass filtering one digital output


The same pattern should appear at all the outputs of the shift register but delayed by different numbers of clock cycles depending on where along the shift register you are looking. Try feeding back different outputs of the 8 bit shift register to make a different length shift register to make a longer or shorter pseudo-random sequence. Also try combining different combinations of taps with the XOR to make different patterns. We can't look at more than one output at a time using the channel B scope input. The following show some ways to observe multiple digital outputs by combining them in an analog fashion into one signal. The first scheme is to extend the idea in figure 2 to sum multiple digital signals using equal value resistors as in figure 3. The output voltage as measured by scope channel B is proportional to the number of 1's. If all the digital outputs are low (0 V) then the output is 0V. If all the digital outputs are High (5 V) then the output is 5 V. If 4 digital outputs are low (0 V) and 4 digital outputs are High (5 V) then the output is 2.5 V. We won't know which outputs are high and low just how many.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-lfsr-fig_3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Equal weight analog reconstruction circuit


If we use more resistors to apply different weights to each digital output we can produce analog output values that represent different combinations of the outputs. In figure 4 we have used a combination of series and parallel connections for resistors from the ADALP2000 parts kit to weight each digital output in a binary fashion then there will be 256 unique output voltages. We needed to create 8 different resistor values each twice as big as the previous value. This can require a number of different resistors of widely differing values.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-lfsr-fig_4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Binary weight analog reconstruction circuit


We can also create binary weights by using an R/2R resistor network as in figure 5. This technique uses only 2 resistors values and can be built using resistors of the same value by using either 2 in parallel or 2 in series to make the other value.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-lfsr-fig_5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, R/2R analog reconstruction circuit


Using either the resistor network in figure 4 or 5, you should see a random sequence something like what is shown in figure 6. Notice that the pattern repeats every 255 clock cycles.

Questions:
----------

As an alternative to the XOR based feedback in an LFSR, an XNOR gate can also be used. The inverted XNOR function is an affine feedback, not strictly a linear feedback, but it results in an equivalent counter whose state is the complement of the state of an XOR based LFSR. A state with all ones is not possible when using an XNOR gate, in the same way as a state with all zeroes is not possible when using an XOR gate. The all 1's or all 0's state is considered illegal because the shift register would remain "locked-up" in this state. Try switching the XOR gate in your circuit with an XNOR gate. An XNOR gate function can be made by simply inverting the gate output with an inverter gate. Compare the two output sequences you see with the XOR and XNOR feedback.

Appendix:
~~~~~~~~~

**74HC273 functional block diagram**

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-lfsr-fig_6.png
   :align: center
   :width: 250px

.. container:: centeralign

   74HC273 Pinout


\**For Further Reading: \*\*

| `XOR_gate <https://en.wikipedia.org/wiki/XOR_gate>`_
| `Shift_register <https://en.wikipedia.org/wiki/Shift_register>`_
| `Linear_feedback_shift_register <https://en.wikipedia.org/wiki/Linear_feedback_shift_register>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**
