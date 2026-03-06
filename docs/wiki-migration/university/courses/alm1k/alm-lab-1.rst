Activity: Simple Op Amps, For ADALM1000
=======================================

Objective:
----------

In this lab we introduce the operational amplifier (op amp), an active circuit that is designed with certain characteristics (high input resistance, low output resistance, and a large differential gain) that make it a nearly ideal amplifier and useful building-block in many circuits applications. In this lab you will learn about DC biasing for active circuits and explore a few of the basic functional op amp circuits. We will also use this lab to continue developing skills with the lab hardware.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The blue shaded rectangles indicate connections to the M1000 digital I/O connector.

The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard, and jumper wire kit
| 1 - 1 kΩ resistor
| 3 - 4.7 kΩ resistors
| 2 - 10 kΩ resistors
| 1 - 20 kΩ resistor
| 2 - AD8541 ( CMOS rail to rail amplifier )
| 2 - 0.1uF Capacitors (radial lead)

1.1 Op-Amp Basics
-----------------

First Step: Connecting DC Power:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Op amps must always be supplied with DC power and therefore it is best to configure these connections first before adding any other circuit components. Figure 1.1 shows one possible power arrangement on your solder-less breadboard. We use two of the long rails for the positive supply voltage and ground, and one for 2.5 V mid supply connections that may be required. Included are the so-called "supply de-coupling" capacitor connected between the power-supply and ground rails. It is too early to discuss in great detail the purpose of these capacitors, but they are used to reduce noise on the supply lines and avoid parasitic oscillations. It is considered good practice in analog circuit design to always include small bypass capacitors close to the supply pins of each op amp in your circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab1_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.1 Power connections


Insert the op amp into your breadboard and add the wires and supply capacitors as shown in figure 1.1. To avoid problems later you may want to attach a small label to the breadboard to indicate which rails correspond to +5 V, +2.5V and ground. Color coding your wires, red for +5 V, black for +2.5 V and green for ground, can also help to keep the connections organized.

Next, attach the +5 V supply and GND connections from the ALM1000 board to the terminals on your breadboard. Use jumper wires to power the rails. Remember, the power-supply GND terminal will be our circuit "ground" reference. Once you have your supply connections you may want to use a DMM to probe the IC pins directly to insure that pin 7 is at +5 V and pin 4 is at 0 V (ground).

Remember you must have the ALM1000 plugged into the USB port before measuring the voltages with the volt meter.

Unity-Gain Amplifier (Voltage Follower):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our first op amp circuit is a simple one, shown in figure 1.2. This is called a unity-gain buffer, or sometimes just a voltage follower, defined by the transfer function Vout = Vin. At first glance it may seem like a useless device, but as we will show later it finds use because of its high input resistance and low output resistance.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab1_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.2 Unity Gain Follower


Using your breadboard and the ALM1000 power supplies, construct the circuit shown in figure 1.2. Note that the power connections have not been explicitly shown here; it is assumed that those connections must be made in any real circuit (as you did in the previous step), so it is unnecessary to show them in the schematic from this point on. Use jumper wires to connect input and output to the waveform generator output, CA-V and oscilloscope input CB-H.

Use the channel A voltage generator set to a 1.0 V Min value and a 4.0 V Max value (3 Vp-p centered on 2.5V ), 500 Hz sine wave. Configure the scope so that the input signal trace is displayed CA-V and the output signal trace is displayed CB-V. Export a plot of the two resulting waveforms and include it your lab report, noting the parameters of the waveforms (peak values and the fundamental time-period or frequency). Your waveforms should confirm the description of this as a "unity-gain" or "voltage follower" circuit.

Buffering Example:
~~~~~~~~~~~~~~~~~~

The high input resistance of the op-amp (zero input current) means there is very little loading on the generator; i.e., no current is drawn from the source circuit and therefore no voltage drops on any internal (Thevenin) resistance. Thus in this configuration the op-amp acts like a "buffer" to shield the source from the loading effects from other parts of the system. From the perspective of the load circuit the buffer transforms a non-ideal voltage source into a nearly ideal source. figure 1.3 describes a simple circuit that we can use to demonstrate this feature of a unity-gain buffer. Here the buffer is inserted between a voltage-divider circuit and some "load" resistance, the 10 KΩ resistor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab1_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.3 Buffer Example


Disconnect the power supplies and add the resistors to your circuit as shown in figure 1.3 (note we have not changed the op-amp connections here, we've just flipped the op-amp symbol relative to figure 1.2 to better arrange the wires).

Reconnect the power supplies and set the waveform generator to a 500 Hz sine wave set to a 0.5 V Min value and a 4.5 V Max value (4 Vp-p centered on 2.5V ). Simultaneously observe Vin, CA-V and Vout CB-H and record the amplitudes in your lab report. Use scope input CB-H to also measure the amplitude of the signal seen on pin 3 of the op-amp.

Remove the 10 KΩ load and substitute a 1 KΩ resistor instead. Record the amplitude. Now move the 1 KΩ load between pin 3 and +2.5 V, so that it is in parallel with the 4.7 KΩ resistor. Record how the output amplitude has changed. Can you predict the new output amplitude?

1.2 Simple Amplifier Configurations
-----------------------------------

Inverting Amplifier:
~~~~~~~~~~~~~~~~~~~~

Figure 1.4 shows the conventional inverting amplifier configuration with a 10 KΩ "load" resistor at the output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab1_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.4 Inverting amplifier configuration


Now assemble the inverting amplifier circuit shown in figure 1.4 using R\ :sub:`2` = 4.7kΩ . Remember to disconnect the power supply before assembling a new circuit. Cut and bend the resistor leads as needed to keep them flat against the board surface, and use the shortest jumper wires for each connection (as in figure 1.1). Remember, the breadboard gives you a lot of flexibility. For example, the leads of resistor R\ :sub:`2` do not necessarily have to bridge over the op-amp from pin 2 to pin 6; you could use an intermediate node and a jumper wire to go around the device instead.

Reconnect the power supplies and observe the current draw to be sure there are no accidental shorts. Now adjust the waveform generator to a 500 Hz sine wave set to a 2.1 V Min value and a 2.9 V Max value (0.8 Vp-p centered on 2.5V ) and again display both the input and output on the oscilloscope. Measure and record the voltage gain of this circuit, and compare to the theory that was discussed in class. Export a plot of the input/output waveforms to be included your lab report.

This is a good point to comment on circuit debugging. At some point in this class you are likely to have trouble getting your circuit to work. That is not unexpected, nobody is perfect. However, you should not simply assume that a non-working circuit must imply a malfunctioning part or lab instrument. That is almost never true; 99% of all circuit problems are simple wiring or power supply errors. Even experienced engineers will make mistakes from time to time, and consequently, learning how to "debug" circuit problems is a very important part of the learning process. It is NOT the TA's responsibility to diagnose errors for you, and if you find yourself relying on others in this way then you are missing a key point of the lab and you will be unlikely to succeed in later coursework. Unless smoke is issuing from your op amp or there are brown burn marks on your resistors or your capacitor has exploded, your components are probably fine, in fact most of them can tolerate a little abuse before significant damage is done. The best thing to do when things aren't working is to just disconnect the power supplies and look for a simple explanation before blaming parts or equipment. The DMM can be valuable debugging tool in this regard.

Output Saturation:
~~~~~~~~~~~~~~~~~~

Now change the feedback resistor R\ :sub:`2` in figure 1.5 from 4.7 KΩ to 10 KΩ . What is the gain now? Slowly increase the amplitude of the input signal to 2 volts still centered on 2.5 V, and export the waveforms into your lab notebook. The output voltage of any op amp is ultimately limited by the supply voltages, and in many cases the actual limits are much smaller than the supply voltages due to internal voltage drops in the circuitry. Quantify the internal voltage drops in the AD8541 based on your measurements above. If you have time try substituting a OP97 or OP27 amplifier for the AD8514 and compare the minimum and maximum output voltages that it can produce.

Summing Amplifier Circuit:
~~~~~~~~~~~~~~~~~~~~~~~~~~

The circuit of figure 1.5 is a basic inverting amplifier with four inputs, called a "summing" amplifier. Figure 1.5 is configured slightly differently than you may see in text books because of the single positive supply voltage available from the ALM1000. The non-inverting (+) input of the amplifier is connected to +2.5 V, which is half the supply voltage, rather than ground. This changes the summing amplifier equations. The input voltages, which appear across the input resistors, now are taken with respect to the +2.5 V so called common mode level. They should have the 2.5 V subtracted so 0 V in becomes -2.5V and +3.3V in becomes +0.8V. The output voltage should also be taken with respect to the +2.5 V level. To make the conventional equation come out right the output voltage will also have the 2.5 V common mode level subtracted. Another way to think about this is to consider the case where all the inputs are at +2.5 V ( or are left floating ). There will be no current flowing in any of the input resistors ( they have 0 V across them ) and as a result the feedback resistor will also have no current flowing in it ( it has 0 V across it ). The output will be at 2.5 V.

For this circuit you will be using the four digital outputs, PIO 0-3 as input voltage sources. Each digital output has either a "low" output near 0 V or a "high" output near 3.3 V. Using superposition ( and correcting for the 2.5 V common mode level ) we can show that Vout is a linear sum of V\ :sub:`PIO0`, V\ :sub:`PIO1`, V\ :sub:`PIO2` and V\ :sub:`PIO3` each with their own unique gain or scale factor set by the ratio of the 1 KΩ feedback resistor divided by their respective resistors.

PIO 0 has the highest value and will have the smallest change in the output ( least significant bit ) and PIO 3 has the lowest value and will have the largest change in the output ( most significant bit ). Notice that the POI 3 resistor is made from 2 4.7 KΩ resistors in parallel.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab1_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.5 Summing Amplifier configuration


With the power disconnected, modify your inverting amplifier circuit as shown in figure 1.5. Reconnect the power and using the digital output controls, fill in the following two tables. In the first table, record the "low" and "high" voltages for each digital output. Use the CB-H scope input in Hi-Z mode to do this. In the second table record the output voltage for all 16 combinations of 1's and 0's for PIO 3-0. You should also confirm that the output voltage is indeed +2.5V when all four bits are floating or in the high-z [X] state.

==== ======= ========
\    V "low" V "high"
==== ======= ========
PIO0         
PIO1         
PIO2         
PIO3         
==== ======= ========

Table 1

============== =============
Digital Bits   V\ :sub:`OUT`
============== =============
P3, P2, P1, P0 
0000           
0001           
0010           
0011           
0100           
0101           
0110           
0111           
1000           
1001           
1010           
1011           
1100           
1101           
1110           
1111           
============== =============

Table 2

Using the resistor values calculate the expected output voltage for each input combination and compare to your measured values.

Non-Inverting Amplifier:
~~~~~~~~~~~~~~~~~~~~~~~~

The non-inverting amplifier configuration is shown in figure 1.6. Like the unity-gain buffer, this circuit has the (usually) desirable property of high input resistance, so it is useful for buffering non-ideal sources, however with a gain greater than one.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab1_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.6 Non-inverting Amplifier with gain


Assemble the non-inverting amplifier circuit shown in figure 1.6. Remember to shut off the power supplies before assembling the new circuit. Start with R\ :sub:`2` = 1 KΩ.

Apply a 500 Hz sine wave from CA-V set to a 2.0 V Min value and a 3.0 V Max value (1 Vp-p centered on 2.5V ) and display both input and output waveforms on the scope. Measure the voltage gain of this circuit, and compare to the theory discussed in class. Export a plot of the waveforms and include it in your lab report.

Increase the feedback resistor (R\ :sub:`2`) from 1 KΩ to about 4.7 KΩ. Remember you may need to reduce the amplitude of the input to prevent the output from saturating (clipping). What is the gain now?

Increase the feedback resistance further until the onset of clipping, that is, until the peaks of the output signal begin to be flattened due to output saturation. Record the value of resistance where this happens. Now increase the feedback resistance to 100 KΩ. Describe and draw waveforms in your notebook. What is the theoretical gain at this point? How small would the input signal have to be in order to keep the output level to less than 5V given this gain? Try to adjust the waveform generator to this value. Describe the output achieved.

The last step underscores an important consideration for high-gain amplifiers. High-gain necessarily implies a large output for a small input level. Sometimes this can lead to inadvertent saturation due to the amplification of some low-level noise or interference, for example the amplification of stray 60Hz signals from power-lines that can sometimes be picked up. Amplifiers will amplify any signals at the input terminals...whether you want it or not!

1.3 Using an Op-Amp as a Comparator
-----------------------------------

The high intrinsic gain of the op-amp and the output saturation effects can be exploited by configuring the op-amp as a comparator as in figure 1.7. This is essentially a binary-state decision-making circuit: if the voltage at the "+" terminal is greater than the voltage at the "-" terminal, Vin > Vref , the output goes "high" (saturates at its maximum value). Conversely if Vin < Vref the output goes "low". The circuit compares the voltages at the two inputs and generates an output based on the relative values. Unlike all the previous circuits there is no feedback between the input and output; we say that the circuit is operating "open-loop".

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab1_f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.7 Op-Amp as Comparator


Comparators are used in different ways, and in future sections we will see them in action in several labs. Here we will use the comparator in a common configuration that generates a square wave with a variable pulse width.

Start by disconnecting the power supplies and assemble the circuit. Use the fixed 2.5 V output for the DC source on the inverting input, Vref.

Again configure the waveform generator CA-V on the non-inverting input, for a 2V Min value and 3V Max value triangle wave ( centered on 2.5 V ) at 500 Hz. With the power supply reconnected, export the input and output waveforms.

Now slowly shift the center of the triangle wave by increasing ( positive shift ) or decreasing ( negative shift ) the Min and Max values and observe what happens at the output. Can you explain this?

Repeat the above for a sine wave and sawtooth input waveforms and record your observations for your lab report.

Extra Credit
------------

For experimenters who finish early or want an additional challenge, see if you can modify the comparator circuit using your red and green LEDs at the output so that the red LED lights for negative voltages and the green LED lights for positive voltages. Turn down the frequency to a few Hz (or less) so you can see them turn on-and-off in real time. Don't forget that the LEDs will need a current-limiting resistor so that the current through it is no more than 20mA.

**Congratulations! You have now completed Lab Activity 1**

As noted in the previous lab: keep all your leftover electrical components!

**Specific Discussion Items for Lab Report**

| Some specific ideas for the report might be as follows:
| Slew rate: discuss how you measured and computed the slew rate in the unity-gain buffer configuration, and compare this with the value listed in the OP97 data sheet.
| Buffering: explain why the buffer amplifier in figure 1.6 allowed the voltage divider circuit to function perfectly with differently load resistances.
| Output saturation: explain your observations of output voltage saturation in the inverting amplifier configuration and your estimate of the internal voltages drops. How close does the output come to the supply rails in this experiment and also later when used as a comparator with different power-supply voltages? Can you guess what the output voltage swing would be for an op-amp that is advertised as a "rail-to-rail" device?
| Summing circuit: using superposition, derive the expected transfer characteristic for the circuit of figure 1.6; that is, find the output voltage in terms of Vin1 and Vin2 . Compare the predictions of the ideal relationship with your data.
| Comparator: discuss your measurements and what would happen if the polarity of Vref is reversed.

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/basic_config_opamp_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/basic_config_opamp_bb`

**For Further Reading:**

| `Operational amplifier <https://en.wikipedia.org/wiki/Operational_amplifier>`__
| `Operational amplifier applications <https://en.wikipedia.org/wiki/Operational_amplifier_applications>`__
| :adi:`Commonly Used Amplifier Configurations <media/en/news-marketing-collateral/product-selection-guide/Op_Amps_SG_2011-12_equations.pdf>`

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
| **Return to Electronics Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
