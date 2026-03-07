Activity: Linear Feedback Shift Register (LFSR), For ADALM2000
==============================================================

Objective:
----------

The objective of this lab activity is to explore the operation of the linear feedback shift register to generate pseudo-random sequences of binary numbers.

Background:
-----------

In digital signal processing, a linear-feedback shift register, or LFSR, is a shift register where the input bit is a linear function of its previous state.

A common linear function of single bits is the XOR. The XOR function can also be viewed as part of the digital addition function in that XORs are used as the Sum portion of the simplest form of the half adder. An LFSR is most often a shift register where the input bit is driven by the exclusive-or (XOR) of certain bits of the contents of the overall shift register.

The initial value of the LFSR is called the seed, and because the operation of the register is deterministic, the stream of output value it produces is completely determined by its current (or previous) state. In addition, because a register of finite length has a finite number of possible states, it must eventually enter a repeating cycle. A sufficiently long LFSR with a well-chosen feedback function can produce a sequence of bits which appears random and which has a very long cycle before repeating.

Applications of LFSRs include generating pseudo-random numbers, pseudo-noise sequences, fast digital counters, and whitening sequences. Both hardware and software implementations of LFSRs are common.

The mathematics of a cyclic redundancy check, used to provide a quick check against transmission errors, are closely related to those of an LFSR.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - CD4035 4 bit shift register or similar logic device
| 1 - 74HC86 Quad two input XOR gate or similar logic device

Directions:
-----------

Build the linear feedback shift register circuit shown in figure 1, preferably on your solder-less breadboard. The CD4035 4 bit shift register is shown but another similar shift register with parallel outputs could be substituted. A two input XOR gate can also be constructed using the CD4007 CMOS transistor array as shown in the lab activity on the :doc:`transmission gate XOR </wiki-migration/university/courses/electronics/electronics-lab-30>`.

Connect the D0-D3 digital inputs and the D5 digital output on the ADALM2000 connector and the positive 5 volt power and ground to the circuit as shown.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/alfsr_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Linear-feedback shift register circuit


Hardware Setup:
---------------

Turn on the +5 V power supply only after you have double checked your wiring.

Procedure:
----------

Start the Scopy software. Open power supply control window and turn on the +5 Volt power supply, VP+. Open up the Digital Pattern Generator screen. Add a signal. Select DIO 5. Set the type to clock. You should see something that looks like the screen below in figure 2. Lastly, hit the Run button.

.. container:: centeralign

   Figure 2 Digital pattern generator screen.


Open the edit signal parameters window. Make sure the type is set to clock and the output is set to PP (push-pull). Set the frequency to 5 KHz. With the Duty cycle set to 50%.

Open the logic analyzer window and add a bus signal for DIO 0-3. Check the show as analog box when you make the bus. Hit the Run button. You should see a random sequence something like what is shown in figure 3. Notice that the pattern repeats every 15 clocks.

.. container:: centeralign

   Figure 3 Logic Analyzer screen.


Questions:
----------

As an alternative to the XOR based feedback in an LFSR, an XNOR gate can also be used. The inverted XNOR function is an affine feedback, not strictly a linear feedback, but it results in an equivalent counter whose state is the complement of the state of an XOR based LFSR. A state with all ones is not possible when using an XNOR gate, in the same way as a state with all zeroes is not possible when using an XOR gate. The all 1's or all 0's state is considered illegal because the shift register would remain "locked-up" in this state. Try switching the XOR gate in your circuit with an XNOR gate. An XNOR gate function can be made by simply inverting the gate output with an inverter gate. Compare the two output sequences you see with the XOR and XNOR feedback.

For Additional credit:
~~~~~~~~~~~~~~~~~~~~~~

Try using a second (and third) CD4035 to make a longer shift register to make a longer pseudo-random sequence. Try combining different taps with the XOR to make different patterns. To produce an analog representation of the binary numbers, connect the 8 bit output from your longer shift register to the :doc:`R-2R resistor DAC </wiki-migration/university/courses/electronics/electronics-lab-14>` from that lab activity.

**For Further Reading:**

| http:*en.wikipedia.org/wiki/XOR_gate
  http:*\ en.wikipedia.org/wiki/Shift_register
| http://en.wikipedia.org/wiki/Linear_feedback_shift_register

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**
