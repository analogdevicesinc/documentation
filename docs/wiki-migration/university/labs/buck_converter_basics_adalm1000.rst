Activity: Buck Converter Basics, for ADALM1000
==============================================


.. note::

   See `university/labs/buck_converter_basics <https://wiki.analog.com/university/labs/buck_converter_basics#objective>`_


Activity: DC-DC Boost Converter - ADALM1000
===========================================

Objective:
----------

The object of this activity is to explore an inductor based circuit which can produce an output voltage which is higher than the supplied voltage. This class of circuits are referred to as DC to DC converters or boost regulators. In this activity the voltage from a 1.5 V supply ( battery ) will be boosted to a voltage high enough to drive two LEDs in series.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

The circuits used in this Lab activity while generally low current can potentially produce voltages beyond the 0 to 5 V analog input range of the ALM1000. :doc:`Input voltage divider techniques </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>` as discussed in the document on ALM1000 analog inputs would be required. Refer to the document and construct and use input voltage dividers as necessary when preforming these experiments with the ALM1000.

Background Basics:
------------------

When the current flowing in an inductor is quickly interrupted a large voltage spike is observed across the inductor. This large voltage spike can in fact be useful in some cases. One example is the DC to DC boost converter, which is a circuit that can create a larger DC voltage from a smaller one with very high efficiency. The basic idea is to combine an inductive spike generator with a rectifier circuit, as shown in figure 2. Whenever the transistor is abruptly turned off the voltage at the drain spikes up, the diode D\ :sub:`1` is forward biased and current will flow from the inductor to charge up the storage capacitors C\ :sub:`3` and C\ :sub:`4`. When the drain voltage subsequently drops below the voltage on the capacitor, the diode is reverse biased and the output voltage remains constant. Just as in the chapter on AC power supplies, the output capacitor must be sized appropriately to minimize the ripple relating to the current flowing in the load. We will just use a small capacitor here and hence the circuit will not be able to source a large output current.

This exercise will expand on these concepts, deriving a converter that “boosts” a low voltage to a high voltage. Subsequent activities will close the loop around these circuits and examine loop stability and time-domain response.

.. image:: https://wiki.analog.com/_media/page>/university/labs/open_loop_boost_and_buck_adalm2000#Activity 1/ An Ideal* Open-Loop Boost Converter Simulation&footer
   :alt:  An Ideal\* Open-Loop Boost Converter Simulation&footer

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 1 - 2N3904 small signal NPN transistor
| 1 – ZVN3310 NMOS FET (ZVN2110A, 2N7000 or power FET device such as IRF510)
| 1 – 1 KΩ resistor
| 1 – 100 Ω resistor
| 1 – 47 Ω resistor
| 1 – 1 KΩ potentiometer
| 2 – 47 uF capacitors
| 2 – 0.1 uF capacitors
| 1 - HPH1-1400L (Coilcraft Hexapath inductor or other value from 1mH to 4.7mH)
| 2 – rectifier diodes (1N4001, 1N3064)
| 2 – LEDs ( one red one yellow )

*Optional Additional Equipment:*

| 1.5 V AA battery and holder
| Small handheld DMM

Simple inductor and switch DC/DC Converter:
-------------------------------------------

Directions:
~~~~~~~~~~~

First step is to build a 1.5V power supply ( to simulate a single cell battery ) as shown in figure 1. Build the circuit on one end of your solder-less breadboard being sure to leave space for the rest of this lab’s circuits. Note, if you have a 1.5 Volt battery (AA) and a battery holder with wires attached, you could substitute that as the 1.5 V supply.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab15a_f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1, 1.5 Volt power supply


Once you have the 1.5 V supply constructed, you will need to adjust the potentiometer, R\ :sub:`1`, such that the output is set to 1.5 V. Use one or the other of the ALM1000 inputs in Hi-Z mode to measure the voltage. ( display the AVG voltage for the channel you choose ). An optional DMM could also be used to measure the DC voltage. Note the dashed green box in figure 1 surrounding the ground connections. Later you will be measuring the current in ground for different sections of the circuit. The ground connections in figure 1 will always be connected directly to the ground of the ALM1000. The other sections of ground will, at various times, be either connected to the main ground or the CH-B connector pin on the ALM1000. So as you construct the circuit keep these "ground" connections separate, i.e. don’t use one of the common power bus strips for all the "grounds".

Temporarily connect one of your LEDs from the 1.5 V output to ground. Be careful to note the polarity of the diode so it will be forward biased. Does it light up? Probably not since 1.5 V is generally not enough to turn on an LED. We need a way to boost the 1.5 V to a higher voltage to light a single LED let alone two LEDs connected in series. Disconnect the 2.5 V supply and remove the LED before moving to the next construction step.

Next, on your solderless breadboard construct the DC-DC boost circuit section as shown in figure 2.

The 6 winding HPH1-1400L inductor can be configured for 6 different inductance values depending on how many windings are connected in series. Connecting all 6 windings in series will give 36 times ( N\ :sup:`2` ) the inductance of a single winding ( 0.2 mH ) or about 7 mH. 5 windings = 25 X 0.2 or about 5 mH, 4 windings = 16 X 0.2 or about 3.6mH. Any or all of these configurations should work for L\ :sub:`1`.

You can use a 1N4001 or a 1N3064 for the rectifier diode D\ :sub:`1` and the snubber diode D\ :sub:`2`. Be sure to connect the left end of L\ :sub:`1` to the 1.5V supply from the section in figure 1. The gate of the NMOS switch transistor M\ :sub:`1` is connected to the CH-A output of the ALM1000.

The ground connections in figure 2 shown in the dashed green boxes will sometimes be connected directly to the ground of the ALM1000. At other times, they will either be connected to the main ground or the CH-B connector pin on the ALM1000 depending which branch current is being measured. So as you construct the circuit keep the "ground #2" connections separate from the "ground #3" connections (and the "ground #1" connections from figure 1), i.e. don’t use one of the common power bus strips for all the "grounds".

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab15a_f2.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 2, DC to DC boost converter section


Procedure:
~~~~~~~~~~

Start with the three sections of ground ( #1 and #2 and #3 ) all connected to the main ALM1000 ground. With CH-B in Hi-Z mode you will be using it to observe various voltage waveforms around the circuit.

Start with a switching frequency of 2 kHz which is supplied by AWG A, CA-V. Set the Min value to 0 and the Max value to 3.5 ( enough to turn on M\ :sub:`1` ). Set the mode to SVMI and the shape to square.

Using CH-B in Hi-Z mode observe and save the voltage waveforms seen at the following circuit nodes. First, the 1.5 V input source. Second, the drain of M\ :sub:`1`. Third the "boosted" output, V\ :sub:`OUT`\ at the top of LED\ :sub:`1`. You should also measure the current in the LEDs by taking the voltage at the junction of R\ :sub:`3` and LED\ :sub:`2` divided by the value of R\ :sub:`3`, 100 Ω.

What is the average DC voltage of the "boosted" output? What is the p-p ripple seen on the waveform? What is the average DC current in the LEDs and what is the p-p ripple seen in the current? Record the values in your lab report.

You may want to save snap-shots of the voltage traces or save the VBuffB array to another temporary data array to be plotted later when you are making the current measurements.

Measuring Currents:
~~~~~~~~~~~~~~~~~~~

Now that we have measured all the interesting voltage waveforms associated with the circuit we need to measure the relevant current waveforms as well.

If we set the channel B voltage to a DC value we can think of it as an AC ( and DC ) ammeter with one end connected to the set DC voltage. The DC voltage we set could be a supply voltage or it could be 0V and we would then be measuring the current flowing into or out of ground.

The first current we will measure is the current in the inductor L\ :sub:`1`. Be sure the frequency of the clock CH-A is still set to 2 KHz. Set AWG CH-B to SVMI mode and Shape to DC with a Max value of 1.5 V, to match the 1.5 V from the 1.5 V supply from figure 1 ( or AA battery if you are using that ). Because the shape is set to DC the Min and frequency values are ignored. Disconnect the left end of L\ :sub:`1` from the 1.5V supply and connect L\ :sub:`1` to CH-B. Under the curves menu be sure to select the CB-I trace to be displayed.

Hit the run button and you should see the square wave ( switch drive ) on the CA-V trace, the constant 1.5V DC voltage on the CB-V trace and the inductor current on the CB-I trace. Adjust the CB-I vertical scale as needed to fit the peak amplitude of the current on the screen.

Note the time when switch M\ :sub:`1` is on and when M\ :sub:`1` is off and the current in L\ :sub:`1`. Take a snap-shot of the CB-I current trace for future reference ( or save the IBuffB array into another array so it can be plotted later).

Disconnect L\ :sub:`1` from CH-B and reconnect it to the 1.5V supply.

Now we want to measure the currents in the two sections of "ground" you separated out when you built the breadboard. First, disconnect the ground #2 section from the main ground bus and connect it to CH-B. Set CH-B Max value to 0 ( the same voltage as ground ). The current in ground #2 is just the current in M\ :sub:`1`, the switch.

Hit the run button and you should see the square wave ( switch drive ) on the CA-V trace, the constant 0V DC voltage on the CB-V trace and the M\ :sub:`1` source current on the CB-I trace. Adjust the CB-I vertical scale as needed to fit the peak amplitude of the current on the screen. Note the polarity ( direction ) of the current. Display the saved L\ :sub:`1` current trace and compare the two. What part of the L\ :sub:`1` current flows in M\ :sub:`1` and where in time does it flow? Save the CB-I trace of ground section #2. (save the IBuffB array into another array ).

Now we will measure the current in the LED load, including the by-pass filter capacitors C\ :sub:`3` and C\ :sub:`4`. Disconnect the ground #2 section from CH-B and reconnect it to the main ground bus. Disconnect the ground #3 section from the main ground bus and connect it to CH-B. The current in ground #3 combines the LED current and the current in the capacitors C\ :sub:`3` and C\ :sub:`4` which is also the current in diode D\ :sub:`1`.

Hit the run button and you should see the square wave ( switch drive ) on the CA-V trace, the constant 0V DC voltage on the CB-V trace and the LED load current on the CB-I trace. Adjust the CB-I vertical scale as needed to fit the peak amplitude of the current on the screen. Note the polarity ( direction ) of the current. Display the saved L\ :sub:`1` current trace and compare the two. What part of the L\ :sub:`1` current flows in load and where in time does it flow? Save the CB-I trace of ground section #3. (save the IBuffB array into another array ).

Conservation of current says that the sum of the current in M\ :sub:`1` and D\ :sub:`1` should be the same as the current in L\ :sub:`1`. Use the Math plotting function to plot the sum of the saved ground #2 and ground #3 data buffers. Compare this to the measured L\ :sub:`1` current waveform.

As additional investigation.

Now increase the frequency to 4, 6 and 8 KHz. Measure and record the boosted output voltage waveform and the current waveforms. Explain what has changed and why?

With a 2 KHz clock frequency, reduce the duty-cycle of the CH-A square wave switch drive waveform from 50% to 45%, 35% and 25%. How does the duty cycle change the voltage and current waveforms?

Appendix:
---------

Improved 1.5V sources
~~~~~~~~~~~~~~~~~~~~~

The output impedance ( load regulation ) of the simple emitter follower in figure 1 can be improved through the addition of feedback. Shown in figure A1 is a follower circuit where the single NPN ( Q\ :sub:`1` is a 2N3904) transistor is replaced with a NPN/PNP compound transistor ( Q\ :sub:`2` is a 2N3906 ). The load regulation of a single transistor follower is a function of how much the V\ :sub:`BE` changes as the emitter current changes. In the case of the compound transistor configuration a small increase in the current of Q\ :sub:`1` is amplified and causes a much larger current to flow in PNP transistor Q\ :sub:`2`.

There is also the added benefit that the base current of Q\ :sub:`1` is now much smaller and its effect on the voltage divider of R\ :sub:`1` and R\ :sub:`2` is much smaller.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab15a_fa1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure A1, Improved follower


Even better load regulation can be achieved by using an op-amp to provide high gain. As shown in figure A2, the output of the op-amp drives the base of transistor Q\ :sub:`1` to whatever bias voltage is need to maintain the emitter voltage ( negative input of the op-amp ) equal to the voltage set at the positive input of the op-amp by the voltage divider. The circuit can essentially source current up to the maximum current limit of the transistor or the +5V power supply with very little change in the +1.5V output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab15a_fa2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure A2, Precision follower


**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/dc-dc_boost_converters_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/dc-dc_boost_converters-bb`

**For Further Reading:**

| `Boost_converter <https://en.wikipedia.org/wiki/Boost_converter>`_
| `Compound Transistor <https://en.wikipedia.org/wiki/Sziklai_pair>`_

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/circuits>`



.. note::

   See `university/labs/buck_converter_basics <https://wiki.analog.com/university/labs/buck_converter_basics#background>`_


Materials
---------

ADALM1000 Active Learning Module PC running LTspice and ALICE Solder-less breadboard and jumper wire kit Components from ADALP2000 parts kit as required Optional: :doc:`ADALM-BUCK-ARDZ Module </wiki-migration/university/tools/lab_hw/adalm_buck>` 12V power supply (preferred), 9 V battery or 5V USB power supply (workable) Voltmeter (optional) LTspice files for this activity: `buck_converter_basics_ltspice_files.zip <https://wiki.analog.com/_media/university/courses/electronics/buck_basics/buck_converter_basics_ltspice_files.zip>`_

Activity 1: An Open-Loop 2:1 Buck Converter
-------------------------------------------


.. note::

   See `university/labs/buck_converter_basics <https://wiki.analog.com/university/labs/buck_converter_basics#theory_and_simulation>`_


Circuit Testing
~~~~~~~~~~~~~~~

**Software Requirements**

To measure this circuit with the ADALM1000 module you will need to use the Equivalent Time Sampling functionality within the ALICE 1.3 user interface. One of the advanced features that can be enabled in ALICE is Equivalent Time Sampling which, for certain classes of periodic waveforms, can increase the apparent sampling to MSPS rates. How to use ETS is outlined in the :doc:`ALICE Equivalent Time Sampling User’s Guide </wiki-migration/university/tools/m1k/alice/advanced-equivalent-time-sampling-guide>`

An assembled PC board version of the buck converter circuit is available as the ADALM-BUCK-ARDZ experiment board.


|image1|

.. container:: centeralign

   Figure A1.12, ADALM-BUCK-ARDZ test board


This board is actually an Arduino compatible shield and for the tests is used in conjunction with an Arduino running the following sketch:

.. admonition:: Download
   :class: download

   
   -  Arduino Sketch: :git-Linduino:`LT1054 closed loop buck with duty cycle control <LTSketchbook/Active%20Learning/LT1054_voltage_mode_buck_DC_ctrl>`
   


While there are a number of connections required to construct this test circuit, it can be assembled on a solderless breadboard as in figure A1.13. Note that the HPH1-1400L has six inductors that can be connected in any way (series, parallel, or a combination of the two). Be sure to observe proper polarity, connecting all inductors in series as shown.

   


|image2|

.. container:: centeralign

   Figure A1.13. Breadboard Circuit


The circuit could also be constructed on a solderable breadboard which matches the layout of typical solderless breadboards. Or on an Arduino compatible proto-typing shield following the wiring of the ADALM-BUCK-ARDZ experiment board.



|image3|

.. container:: centeralign

   Figure A1.14. Alternate Construction Method


Measure the ripple current for different numbers of series-connected inductors. The figure below shows the ripple current for 2, 3, 4, 5, and 6 inductors. How well does this match the LTspice simulation?



|image4|

.. container:: centeralign

   Figure A1.15. Ripple Current for 2 to 6 Windings in Series


*(Notice the "steps" in the switch node voltage as the inductor current passes through zero. After switching, current initially flows through diodes D1 or D2. As the current passes through zero and switches direction, the LT1054 output driver "takes over" and drives the switch node. In the LTspice simulation, try probing the LT1054 CAP+ current, D1 current, and D2 current separately, noting that the inductor current is the sum of the three.)*

Measure the ripple voltage at the output of the converter, with a 22uF output capacitor. Then place an additional 47uF capacitor in parallel, for a total of 69uF. Does the measured ripple match the simulated ripple reasonably well? Note that both the inductor and electrolytic capacitors can have a very wide tolerance - tolerances of +/-20% are common for inductors, and -20%/+80% is a common tolerance for electrolytic capacitors. The animated figure below shows the ripple voltage for output capacitances of 22uF and 22uF+47uF.


|image5|

.. container:: centeralign

   Figure A1.16. Output Ripple for 22uF, 22+47uF output capacitance


Activity 2: An Open-Loop Variable Buck Converter
------------------------------------------------


.. note::

   See `university/labs/buck_converter_basics <https://wiki.analog.com/university/labs/buck_converter_basics#theory_and_simulation1>`_


Circuit Testing
~~~~~~~~~~~~~~~

Use M1K to override the LT1054's internal oscillator. Use the AWG controls and take measurements at 20%, 40%, 60%, 80% duty cycle.

<<add setup details, make a ALICE config file.>>

Set back to 50%, then connect a 50-ohm load. Calculate the approximate output impedance.

Activity 3: A closed-Loop, Voltage Mode Buck Converter
------------------------------------------------------


.. note::

   See `university/labs/buck_converter_basics <https://wiki.analog.com/university/labs/buck_converter_basics#theory_and_simulation2>`_


Circuit Testing
~~~~~~~~~~~~~~~

Connect the buck output to the A0 analog pin on the Arduino and the Arduino's D3 digital signal to the buck converter's control input. Figure A2.17 shows connections to an Arduino Uno clone. The yellow wire connects the buck output to the Arduino's A0 input, and the blue wire connects the Arduino's PWM output on Digital Pin 3 to the oscillator override input. (Using two ground wires ensures a lower inductance connection between circuit grounds.)


|image6|

.. container:: centeralign

   Figure A2.17. Buck Converter with Arduino Control


Copy this Arduino sketch into your Arduino sketchbook (and restart the Arduino IDE if it's open.)

.. admonition:: Download
   :class: download

   
   -  Arduino Sketch: :git-Linduino:`LT1054 closed loop buck with duty cycle control <LTSketchbook/Active%20Learning/LT1054_voltage_mode_buck_DC_ctrl>`
   


The following figure shows the operation of the closed-loop circuit. The set point voltage is 3.141V, and the purple trace starts out close to this value at the left hand side of the screen shot. A 50 ohm load is then connected to the output, drawing approximately 120mA, and producing a dip in the output voltage. The Arduino loop detects this and increases the PWM frequency accordingly, restoring the voltage to its correct value. Then the resistor is removed, producing an increase in the output voltage. Once again, the Arduino loop detects this disturbance and compensates.

   


|image7|

.. container:: centeralign

   Figure A2.18. Arduino Controlled Buck Transient Response


.. admonition:: Download
   :class: download

   **Resources:**

   
   -  LTspice files: :git-education_tools:`m2k/ltspice/buck_ltspice`
   -  Fritzing files: :git-education_tools:`m2k/fritzing/buck_bb`
   -  Python Script files:
   


Going Further
-------------

This activity borrows heavily from Analog Devices Application Note 140, which is an excellent reference to build upon concepts in this activity:

http://www.analog.com/media/en/technical-documentation/application-notes/AN140fb.pdf

AN19 is the LT1070 design manual, rich with examples:

http://www.analog.com/media/en/technical-documentation/application-notes/an19fc.pdf

Article on simulating SMPS loop gain (and why it's often unnecessary):

http://www.analog.com/en/technical-articles/ltspice-extracting-switch-mode-power-supply-loop-gain-in-simulation-and-why-you-usually-don-t-need.html

Questions:
----------

Slide Deck
----------

A slide deck is provided as a companion to this exercise, and can be used to help in presenting this material in classroom, lab setting, or in hands-on workshops.

.. admonition:: Download
   :class: download

   `Buck Converter Basics Slide Deck <https://wiki.analog.com/_media/university/courses/electronics/buck_basics/workshop_buck_converter_basics.pptx>`_


**Return to Lab Activity** :doc:`Power Lab Table of Contents </wiki-migration/university/labs/power>`

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f10.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/buck_basics/lt1054_2_to_1_bb.png
   :width: 700px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/buck_basics/lt1054_buck_perma_proto_sm.jpg
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/university/labs/m1k-buck-ardz-ripple-current.png
   :width: 650px
.. |image5| image:: https://wiki.analog.com/_media/university/labs/m1k-buck-ardz-ripple-voltage.png
   :width: 650px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/buck_basics/lt1054_arduino_in_loop.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/university/labs/m1k-buck-ardz-transient-step.png
   :width: 650px
