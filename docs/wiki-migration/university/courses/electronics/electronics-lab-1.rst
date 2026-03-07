Activity: Simple Op Amps, For ADALM2000
=======================================

Objective:
----------

In this lab we introduce the operational amplifier (op amp), an active circuit that is designed with certain characteristics (high input resistance, low output resistance, and a large differential gain) that make it a nearly ideal amplifier and useful building-block in many circuits applications. In this lab you will learn about DC biasing for active circuits and explore a few of the basic functional op amp circuits. We will also use this lab to continue developing skills with the lab hardware.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 1 kΩ resistor
| 2 4.7 kΩ resistors
| 2 10 kΩ resistors
| 2 OP97 ( Low slew rate amplifier supplied with the recent versions of ADALP2000 Analog Parts Kit )
| 2 0.1uF Capacitors (radial lead)

1.1 Op-Amp Basics
-----------------

First Step: Connecting DC Power:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Op amps must always be supplied with DC power and therefore it is best to configure these connections first before adding any other circuit components. Figure 1.1 shows one possible power arrangement on your solder-less breadboard. We use two of the long rails for the positive and negative supply voltages, and two others for any ground connections that may be required. Included are the so-called “supply de-coupling” capacitors connected between the power-supply and ground rails. It is too early to discuss in great detail the purpose of these capacitors, but they are used to reduce noise on the supply lines and avoid parasitic oscillations. It is considered good practice in analog circuit design to always include small bypass capacitors close to the supply pins of each op amp in your circuit.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1_f1-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1.1 Power connections


Insert the op amp into your breadboard and add the wires and supply capacitors as shown in figure 1.1. To avoid problems later you may want to attach a small label to the breadboard to indicate which rails correspond to Vp, Vn, and ground. Color coding your wires, red for Vp, black for Vn and green for ground, can also help to keep the connections organized.

Next, attach the supply and GND connections from the ADALM2000 board to the terminals on your breadboard. Use jumper wires to power the rails as shown. Remember, the power-supply GND terminal will be our circuit “ground” reference. Once you have your supply connections you may want to use a DMM to probe the IC pins directly to insure that pin 7 is at +5V and pin 4 is at -5V. Remember you must have the Scopy software running and have turned on the power supplies before measuring the voltages with the voltmeter.

Unity-Gain Amplifier (Voltage Follower):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Background:
^^^^^^^^^^^

Our first op-amp circuit is a simple one, shown in figure 1.2. This is called a unity-gain buffer, or sometimes just a voltage follower, defined by the transfer function Vout = Vin. At first glance it may seem like a useless device, but as we will show later it finds use because of its high input resistance and low output resistance.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.2 Unity Gain Follower


Hardware Setup:
^^^^^^^^^^^^^^^

Using your breadboard and the ADALM2000 power supplies, construct the circuit shown in figure 1.3. Note that the power connections have not been explicitly shown here; it is assumed that those connections must be made in any real circuit (as you did in the previous step), so it is unnecessary to show them in the schematic from this point on. Use jumper wires to connect input and output to the waveform generator and oscilloscope leads. Don’t forget to ground the scope negative input leads C1- and C2- (ground connections are not shown in the schematic).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/v_follower-bb.png

.. container:: centeralign

   Figure 1.3. Unity Gain Follower Breadboard Circuit


Procedure:
^^^^^^^^^^

Use the first waveform generator as source Vin to provide a 2V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit. Configure the scope so that the input signal is displayed on channel 2 and the output signal is displayed on channel 1.Export a plot of the two resulting waveforms and include it your lab report, noting the parameters of the waveforms (peak values and the fundamental time-period or frequency). Your waveforms should confirm the description of this as a “unity-gain” or “voltage follower” circuit.

A plot example is presented in Figure 1.4.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/v_follower-waveform.png

.. container:: centeralign

   Figure 1.4. Unity Gain Follower Waveforms


Slew Rate Limitations:
~~~~~~~~~~~~~~~~~~~~~~

For an ideal op-amp the output will follow the input signal precisely for any input signals, but in a real amplifier the output signal can never respond instantaneously to the input signal. This non-ideality can be observed when the input signal is a rapidly changing function of time. For large-amplitude signals this limitation is quantified by the slew rate, which is the maximum rate-of-change (slope) of the output voltage that the op-amp is capable of delivering. The units of slew-rate are usually expressed as V/μs.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1_f1-3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.5 Slew Rate


Set the waveform generator to a square wave signal with a 2V amplitude peak-to-peak and increase the frequency until you see a significant departure from ideal behavior, that is, when the output starts looking more like a trapezoid than a square wave. You will likely need to adjust the time scale (Sec/Div) on the scope display to see this. Export a plot of the output waveforms at this point and measure its 10-90% rise time (and 90-10% fall time) as defined in figure 1.5. Also note the peak-to-peak voltage of the output signal. Compute and record the slew rate for both rising and falling outputs according to your measurements. Comment on why the response to rising and falling edges might be different.

A waveform that exemplifies the slew rate is presented in figure 1.6.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/v_follower-slewr_waveform.png
   :align: right

.. container:: centeralign

   Figure 1.6 Slew Rate Waveform


Buffering Example:
~~~~~~~~~~~~~~~~~~

The high input resistance of the op amp (zero input current) means there is very little loading on the generator; i.e., no current is drawn from the source circuit and therefore no voltage drops on any internal (Thevenin) resistance. Thus in this configuration the op amp acts like a “buffer” to shield the source from the loading effects from other parts of the system. From the perspective of the load circuit the buffer transforms a non-ideal voltage source into a nearly ideal source. figure 1.7 describes a simple circuit that we can use to demonstrate this feature of a unity-gain buffer. Here the buffer is inserted between a voltage-divider circuit and some “load” resistance:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.7 Buffer Example


Turn off the power supplies and add the resistors to your circuit as shown in figure 1.7 (note we have not changed the op-amp connections here, we’ve just flipped the op-amp symbol relative to figure 1.2).

Turn on the power supplies and set the waveform generator to a 1 kHz sine signal with a 4V amplitude peak-to-peak. Use the scope to simultaneously observe Vin and Vout and record the amplitudes in your lab report.

Remove the 10 kΩ load and substitute a 1 kΩ resistor instead. Record the amplitude.

Now move the 1 kΩ load between pin 3 and ground, so that it is in parallel with the 4.7 kΩ resistor. Record how the output amplitude has changed. Can you predict the new output amplitude?

1.2 Simple Amplifier Configurations
-----------------------------------

Inverting Amplifier:
~~~~~~~~~~~~~~~~~~~~

.. _background-1:

Background:
^^^^^^^^^^^

Figure 1.8 shows the conventional inverting amplifier configuration with a 10 kΩ “load” resistor at the output.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.8 Inverting amplifier configuration


.. _hardware-setup-1:

Hardware Setup:
^^^^^^^^^^^^^^^

Now assemble the inverting amplifier circuit shown in figure 1.9 using R\ :sub:`2` = 4.7kΩ . Remember to shut off the power supply before assembling a new circuit. Cut and bend the resistor leads as needed to keep them flat against the board surface, and use the shortest jumper wires for each connection (as in figure 1.1). Remember, the breadboard gives you a lot of flexibility. For example, the leads of resistor R\ :sub:`2` do not necessarily have to bridge over the op amp from pin 2 to pin 6; you could use an intermediate node and a jumper wire to go around the device instead.

Turn on the power supplies and observe the current draw to be sure there are no accidental shorts. Now adjust the waveform generator to produce a 2 volt amplitude peak-to-peak, 1 kHz sine wave at the input (Vin), and again display both the input and output on the oscilloscope. Measure and record the voltage gain of this circuit, and compare to the theory that was discussed in class. Export a plot of the input/output waveforms to be included your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/inverting_amp-bb.png

.. container:: centeralign

   Figure 1.9. Inverting amplifier Breadboard Circuit


This is a good point to comment on circuit debugging. At some point in this class you are likely to have trouble getting your circuit to work. That is not unexpected, nobody is perfect. However, you should not simply assume that a non-working circuit must imply a malfunctioning part or lab instrument. That is almost never true; 99% of all circuit problems are simple wiring or power supply errors. Even experienced engineers will make mistakes from time to time, and consequently, learning how to “debug” circuit problems is a very important part of the learning process. It is NOT the TA’s responsibility to diagnose errors for you, and if you find yourself relying on others in this way then you are missing a key point of the lab and you will be unlikely to succeed in later coursework. Unless smoke is issuing from your op amp or there are brown burn marks on your resistors or your capacitor has exploded, your components are probably fine, in fact most of them can tolerate a little abuse before significant damage is done. The best thing to do when things aren’t working is to just turn off the power supplies and look for a simple explanation before blaming parts or equipment. The DMM can be valuable debugging tool in this regard.

.. _procedure-1:

Procedure:
^^^^^^^^^^

Use the first waveform generator as source Vin to provide a 2V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit. Configure the scope so that the input signal is displayed on channel 2 and the output signal is displayed on channel 1.

A plot example is presented in Figure 1.10.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/inverting_amp-waveform.png

.. container:: centeralign

   Figure 1.10. Inverting amplifier Waveforms


Output Saturation:
~~~~~~~~~~~~~~~~~~

Now change the feedback resistor R\ :sub:`2` in figure 1.8 from 4.7 kΩ to 10 kΩ . What is the gain now? Slowly increase the amplitude of the input signal to 2 volts, and export the waveforms into your lab notebook. The output voltage of any op amp is ultimately limited by the supply voltages, and in many cases the actual limits are much smaller than the supply voltages due to internal voltage drops in the circuitry. Quantify the internal voltage drops in the OP97 based on your measurements above.

Summing Amplifier Circuit:
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _background-2:

Background:
^^^^^^^^^^^

The circuit of figure 1.11 is a basic inverting amplifier with an additional input, called a “summing” amplifier. Using superposition we can show that Vout is a linear sum of Vin1 and Vin2, each with their own unique gain or scale factor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.11 Summing Amplifier configuration


.. _hardware-setup-2:

Hardware Setup:
^^^^^^^^^^^^^^^

With the power turned off, modify your inverting amplifier circuit as shown in figure 1.12. Use the second waveform generator output for Vin2. Turn the amplitude all the way down to zero so that you can adjust up from zero during the experiment.

Now apply a 2 volt amplitude peak-to-peak sine wave for Vin1 and 1 volts DC for Vin2. Observe and record the input/output waveforms on the oscilloscope screen. Pay close attention to the ground signal level of the output channel on the oscilloscope screen. When used in this way, such a circuit could be called a level shifter.

Adjust the DC offset of waveform generator W1 (Vin1) until Vout has zero DC component. Estimate the required DC offset by observing the input waveform on the scope (note: it is not Vin2 , be sure to understand why).

Reset the offset of waveform generator W1 to zero. With channel 2 of the scope (the channel connected to the op amp output) set for 2V/div, increase the offset voltage of waveform generator W2, Vin2 slowly. What happens to Vout? Record the DC voltage of the output.

Return the offset voltage of waveform generator W2 to approximately +1V. Set the scope to 1V/div, and adjust the scope offset so you can see the complete Vout waveform. Turn Vin2 back up to the value you increased it to in the previous step. What does the oscilloscope trace for Vout look like? Does the amplifier appear to be amplifying?

.. image:: https://wiki.analog.com/_media/university/courses/electronics/summing_amp-bb.png

.. container:: centeralign

   Figure 1.12. Summing Amplifier Breadboard Circuit


.. _procedure-2:

Procedure:
^^^^^^^^^^

Use the first waveform generator as source Vin to provide a 2V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit. The second waveform generator is used to generate 1V constant voltage. Configure the scope so that the input signal is displayed on channel 2 and the output signal is displayed on channel 1.

A plot example is presented in Figure 1.13.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/summing_amp-waveform.png

.. container:: centeralign

   Figure 1.13. Summing Amplifier Waveforms


Non-Inverting Amplifier:
~~~~~~~~~~~~~~~~~~~~~~~~

.. _background-3:

Background:
^^^^^^^^^^^

The non-inverting amplifier configuration is shown in figure 1.14. Like the unity-gain buffer, this circuit has the (usually) desirable property of high input resistance, so it is useful for buffering non-ideal sources:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a1_f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.14 Non-inverting Amplifier with gain


.. _hardware-setup-3:

Hardware Setup:
^^^^^^^^^^^^^^^

Assemble the non-inverting amplifier circuit shown in figure 1.15. Remember to shut off the power supplies before assembling the new circuit. Start with R\ :sub:`2` = 1kΩ.

Apply a 2 volt amplitude peak-to-peak, 1 kHz sine wave at the input, and display both input and output on the scope. Measure the voltage gain of this circuit, and compare to the theory discussed in class. Export a plot of the waveforms and include it in your lab report.

Increase the feedback resistor (R\ :sub:`2`) from 1 kΩ to about 5 kΩ. What is the gain now?

Increase the feedback resistance further until the onset of clipping, that is, until the peaks of the output signal begin to be flattened due to output saturation. Record the value of resistance where this happens. Now increase the feedback resistance to 100 kΩ. Describe and draw waveforms in your notebook. What is the theoretical gain at this point? How small would the input signal have to be in order to keep the output level to less than 5V given this gain? Try to adjust the waveform generator to this value. Describe the output achieved.

The last step underscores an important consideration for high-gain amplifiers. High-gain necessarily implies a large output for a small input level. Sometimes this can lead to inadvertent saturation due to the amplification of some low-level noise or interference, for example the amplification of stray 60Hz signals from power-lines that can sometimes be picked up. Amplifiers will amplify any signals at the input terminals…whether you want it or not!

.. image:: https://wiki.analog.com/_media/university/courses/electronics/noninverting_amp-bb.png

.. container:: centeralign

   Figure 1.15. Non-Inverting Amplifier Breadboard Circuit


.. _procedure-3:

Procedure:
^^^^^^^^^^

Use the first waveform generator as source Vin to provide a 2V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit. Configure the scope so that the input signal is displayed on channel 2 and the output signal is displayed on channel 1.

A plot example is presented in Figure 1.16.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/noninverting_amp-waveform.png

.. container:: centeralign

   Figure 1.16. Non-Inverting Amplifier Waveforms


Congratulations! You have now completed Lab Activity 1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As noted in the previous lab: keep all your leftover electrical components!

Specific Discussion Items for Lab Report
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some specific ideas for the report might be as follows:

■ Slew rate: discuss how you measured and computed the slew rate in the unity-gain buffer configuration, and compare this with the value listed in the OP97 data sheet.

■ Buffering: explain why the buffer amplifier in figure 1.7 allowed the voltage divider circuit to function perfectly with differently load resistances.

■ Output saturation: explain your observations of output voltage saturation in the inverting amplifier configuration and your estimate of the internal voltages drops. How close does the output come to the supply rails in this experiment and also later when used as a comparator with different power-supply voltages? Can you guess what the output voltage swing would be for an op-amp that is advertised as a “rail-to-rail” device?

■ Summing circuit: using superposition, derive the expected transfer characteristic for the circuit of figure 1.11; that is, find the output voltage in terms of Vin1 and Vin2 . Compare the predictions of the ideal relationship with your data.


| ■ Comparator: discuss your measurements and what would happen if the polarity of Vref is reversed
|

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`opamp_bb <m2k/fritzing/simple_op_amps_bb>`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/opamp_ltspice`
   


**Continue to next Op Amp Lab Activity:** :doc:`Op Amp as Comparator </wiki-migration/university/courses/electronics/electronics-lab-opamp-comparator>`

| **More on Op Amps in amplifier configuration:** :doc:`Variable Gain Amplifiers </wiki-migration/university/courses/electronics/electronics-lab-variable-gain-amplifier>`
| **Return to Lab Activity:** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`
