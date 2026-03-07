Activity: Basic Logic Gates, For ADALM1000
==========================================

Objective:
----------

The main objective of this activity is to familiarize you with the lab equipment and learn about the operation of the fundamental combinational logic elements, AND, OR, NAND, and NOR gates. The TA will explain how to use the ADALM1000, solder-less breadboard, and CMOS logic chips.

To become familiar with basic logic gates and logic functions.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

Binary Numbers
~~~~~~~~~~~~~~

The power of the digital logic used to construct digital systems like computers comes from the fundamental simplicity of the binary number systems. Binary digits (called Bits) have only two values (0 and 1) rather than the ten values (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) of decimal numbers. Using binary numbers makes representation of a number very long (number of Bits). Since a computer or other digital hardware is used to keep track, length (number of Bits) does not matter so much.

| Decimal Number (example): 27 = 2\*10\ :sup:`1` + 7\*10\ :sup:`0` = 20 + 7
| Binary Number (example): 11011 = 1\*2\ :sup:`4` + 1\*2\ :sup:`3` + 0\*2\ :sup:`2` + 1\*2\ :sup:`1` + 1\*2\ :sup:`0` = 16 + 8 + 0 + 2 + 1 = 27

| 1. Convert the following decimal numbers to binary: 13, 3300
| 2. Create a table showing all numbers from 0 to 15

Logic Gates
~~~~~~~~~~~

The AND Gate
^^^^^^^^^^^^

Our first multiple-input gates is the AND gate, so-called because the output of this gate will be “high” (1) if and only if all inputs (first input and the second input and . . .) are “high” (1). If any of the inputs are “low” (0), the output will be in a “low” (0) state. The two-input AND gate truth table is as shown:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-1.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 1, The AND gate


| AND Gate Truth Table:
| ^ A ^ B ^ Output ^

= = =
0 0 0
1 0 0
0 1 0
1 1 1
= = =

The NAND Gate
^^^^^^^^^^^^^

A variation of the AND gate is called the NAND gate or NOT AND. The word “NAND” is the contraction of NOT and AND. The NAND gate behaves the same as an AND gate with a NOT (inverter) gate connected to the output terminal. To symbolize this output signal inversion, the NAND gate symbol has a bubble on the output line. The truth table for a NAND gate is as one might expect, exactly inverted that of the AND gate.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-2.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 2, The NAND gate


| NAND Gate Truth Table:
| ^ A ^ B ^ Output ^

= = =
0 0 1
1 0 1
0 1 1
1 1 0
= = =

The OR Gate
^^^^^^^^^^^

The next gate to investigate is the OR gate. The output of this gate will be “high” (1) if any of the inputs (first input or the second input or . . .) are “high” (1). The output of an OR gate goes “low” (0) if and only if all inputs are “low” (0).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-3.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 3, The OR gate


| OR Gate Truth Table:
| ^ A ^ B ^ Output ^

= = =
0 0 0
1 0 1
0 1 1
1 1 1
= = =

The NOR Gate
^^^^^^^^^^^^

As might be suspected, the NOR gate is an OR gate with its output inverted, just like the NAND gate is an AND gate with an inverted output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-4.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 4, The NOR gate


| NOR Gate Truth Table:
| ^ A ^ B ^ Output ^

= = =
0 0 1
1 0 0
0 1 0
1 1 0
= = =

NOR gates, like all multiple-input gates seen thus far, can be manufactured with more than two inputs. Still, the same logical principle applies: the output goes “low” (0) if any of the inputs are made “high” (1). The output is “high” (1) only when all inputs are “low” (0).

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 - 74HC08 Quad AND Gate
| 1 - 74HC32 Quad OR Gate
| 1 – 74HC04 Hex Inverter (NOT Gate)

For the activity, find the corresponding IC chips and wire the circuit shown in the following diagrams (figures 10-12) one at a time on your breadboard. The logic gates you need to use are 74HC04 Hex inverter, 74HC08 Quad AND gate, and 74HC32 74HC32 Quad OR gate. The IC package contains 4 individual gates, wire one gate at a time and test the functionality.

Remember to connect the + 5 V power supply to the IC power V\ :sub:`DD` (usually pin 14) and GND to the ground pin (usually pin 7). Also, remember that more than one output of the gates should never be connected (shorted) together. If you do so, the two outputs will fight each other and may damage the chip.

Configuring the software
~~~~~~~~~~~~~~~~~~~~~~~~

The ALM1000 has two waveform generator outputs (CH A and CH B) that can be used to provide the two inputs, A and B, to the logic gates you will be testing. Configure the AWG channels as shown in figure 5. The Mode for both channels is set to SVMI Split I/O which produces the voltage waveforms on the CH A and CH B pins while splitting the inputs for the two channels on to the AIN and BIN pins which will be used to measure the logic gate outputs. The Min and Max voltages are set to 0 and 5 to produce the logic low and logic high levels. Be sure that the Sync AWG box is checked.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-5.png
   :align: center
   :width: 220px

.. container:: centeralign

   Figure 5, AWG channel settings


If we set the frequency of channel A to 100 Hz and the frequency of channel B to 200 Hz, the four input combinations shown in the above Truth Tables will be produced over one cycle of channel A. On the Shape drop down menu for both channels check Trapezoid and Burst as shown if figure 6. A Trapezoid waveform with a 0 Rise Time and 50% duty cycle is simply a square wave. When you click on burst (when not already checked) the software will first prompt you for the number of cycles in the burst. Enter 10 for channel A and 20 for channel B. Second it will prompt you for a delay (when to start the burst). Enter 10 for channel A and 2.5 for channel B.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-6.png
   :align: center
   :width: 110px

.. container:: centeralign

   Figure 6, Channel Shape settings


We would like to display both the inputs and outputs of the logic gates on the oscilloscope screen at the same time. The scope inputs, AIN and BIN, can be connected to the gate outputs but we would need two more scope input channels to simultaneously display the two gate inputs (AWG outputs). The software provides a couple of "Math" traces that can be used to display the waveform data being sent to the AWG channels. This will be the same as if the actual output voltage was measured. From the Curves drop down menus select CA-V, CB-V, Math-X and Math-Y.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-7.png
   :align: center
   :width: 120px

.. container:: centeralign

   Figure 7, Curves settings


We now need to tell the software what data we want to appear in the Math traces. The AWG A and AWG B waveform data points are contained in two arrays, AWGAwaveform[] and AWGBwaveform[]. Click on the Math button to open the Math formula control window as shown in figure 8.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-8.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 8, Math Formula settings


Enter AWGAwaveform[t] and AWGBwaveform[t] into the X and Y Math Trace Formula entry locations respectively. The Units for both should be V (for volts) of course. We need to choose a set of vertical axis controls for the traces as well. Enter I-A for X and I-B for Y. Click on Apply buttons to apply your entries. You can use the Check buttons to make sure there are no typos in the formula you entered.

To better display the four traces on the scope grid so they are not all on top of each other we can use the vertical range and position settings to arrange then at different locations on the grid. Set the V/Div for all four traces to 5 (the traces will be one vertical division tall). Set the Pos controls as shown in figure 9 to stagger the traces vertically.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-9.png
   :align: center
   :width: 720px

.. container:: centeralign

   Figure 9, Vertical Range and Position settings


The purple and red (Math) traces are the inputs to the logic gates (AWG outputs) and the green and orange traces are the logic gate outputs.

You can do all this configuration automatically by loading the intro-logic-gates.cfg contained in this zip archive `intro-logic-gates.zip <https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-logic-gates.zip>`_.

One chip at a time
~~~~~~~~~~~~~~~~~~

Plug in the 74HC08 and 74HC32 chip and connect one of the four gates at a time as shown the following figures. Connect the A and B inputs of one of the gates to the CH A and CH B pin, and the output to the AIN or BIN pins. Record your observations (scope traces and resulting Truth Table) in your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10, AND and OR logic function


Inverting the output of the AND gate provides the NOT AND function or NAND gate. Similarly, inverting the output of the OR gate provides the NOT OR function or NOR gate. Add the 74HC94 Hex inverter to your breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, NAND and NOR logic function


Inverting the inputs of the AND gate provides the Negative AND function. Similarly, inverting the inputs of the OR gate provides the Negative OR function. Contrary to your first instinct, the logical behavior of a Negative-AND gate is not the same as a NAND gate. Its truth table, actually, is identical to a NOR gate. The behavior and truth table of a Negative-OR gate is the same as for a NAND gate.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 12, Negative AND and Negative OR logic function


EXPERIMENT RESULTS
------------------

| Witnessed by:
| Date \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Recorded Truth Table

1. Which pairs of gates have inverting relations according to the truth table?

2. Write an algebraic equation for each type of gate using the inputs A and B (refer to the datasheet pin-outs, or textbook, or ask TA)

OR:

NOR:

AND:

NAND:

The Exclusive-OR Gate
~~~~~~~~~~~~~~~~~~~~~

The previous gates are all fairly direct variations on the three basic logic functions: AND, OR, and NOT. The Exclusive-OR gate, however, is something different.

Exclusive-OR gates output a “high” (1) logic level if the inputs are at different logic levels, either 0 and 1 or 1 and 0. Conversely, they output a “low” (0) logic level if the inputs are at the same logic levels. The Exclusive-OR (sometimes called XOR) gate has both a symbol and a truth table pattern that is unique:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-13.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 13, Exclusive OR function from AND, OR NOT gates


| XOR Gate Truth Table:
| ^ A ^ B ^ Output ^

= = =
0 0 0
1 0 1
0 1 1
1 1 0
= = =

There are equivalent circuits for an Exclusive-OR gate made up of AND, OR, and NOT gates, just as there were for NAND, NOR, and the negative-input gates. A rather direct approach to simulating an Exclusive-OR gate is to start with a regular OR gate, then add additional gates (AND gates) to inhibit the output from going “high” (1) when both inputs are “high” (1):

In this circuit, the final AND gate act as a buffer for the output of the OR gate whenever the NAND gate’s output is high, which it is for the first three input state combinations (00, 01, and 10). However, when both inputs are “high” (1), the NAND gate outputs a “low” (0) logic level, which forces the final AND gate to produce a “low” (0) output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-basic-logic-gates-fig-14.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 14, Exclusive OR gate


The Exclusive-NOR Gate
~~~~~~~~~~~~~~~~~~~~~~

Finally, our last gate for analysis is the Exclusive-NOR gate, otherwise known as the XNOR gate. It is equivalent to an Exclusive-OR gate with an inverted output. The truth table for this gate is exactly opposite as for the Exclusive-OR gate:

| XNOR Gate Truth Table:
| ^ A ^ B ^ Output ^

= = =
0 0 1
1 0 0
0 1 0
1 1 1
= = =

A mathematician named DeMorgan developed a pair of important rules regarding group complementation in Boolean algebra. By group complementation, we are referring to the complement of a group of terms, represented by a long bar over more than one variable.

You should recall from the chapter on logic gates that inverting all inputs to a gate reverses that gate’s essential function from AND to OR, or vice versa, and also inverts the output. So, an OR gate with all inputs inverted (a Negative-OR gate) behaves the same as a NAND gate, and an AND gate with all inputs inverted (a Negative-AND gate) behaves the same as a NOR gate. DeMorgan’s theorems state the same equivalence in “backward” form: that inverting the output of any gate results in the same function as the opposite type of gate (AND vs. OR) with inverted inputs:

REVIEW:
-------

-  Logical operation for an AND gate: output is “high” only if all inputs are “high.”
-  Logical operation for an OR gate: output is “high” if input A or input B are “high.”
-  Logical operation for a NAND gate: output is not “high” if all inputs are “high.”
-  Logical operation for a NOR gate: output is not “high” if any input is “high.”
-  A Negative-AND gate behaves like a NOR gate.
-  A Negative-OR gate behaves like a NAND gate.
-  Logical operation for an Exclusive-OR gate: output is “high” if the input logic levels are different.
-  Logical operation for an Exclusive-NOR gate: output is “high” if the input logic levels are the same

**For Further Reading:**

| `Logic Gates <https://en.wikipedia.org/wiki/Logic_gate>`_
| `The Inverter, NOT gate <https://en.wikipedia.org/wiki/Inverter_(logic_gate)>`_
| `The AND gate <https://en.wikipedia.org/wiki/AND_gate>`_
| `The NAND gate <https://en.wikipedia.org/wiki/NAND_gate>`_
| `The OR gate <https://en.wikipedia.org/wiki/OR_gate>`_
| `The NOR gate <https://en.wikipedia.org/wiki/NOR_gate>`_
| `The XOR gate <https://en.wikipedia.org/wiki/XOR_gate>`_
| `De Morgan duality <https://en.wikipedia.org/wiki/De_Morgan%27s_laws>`_

**Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
