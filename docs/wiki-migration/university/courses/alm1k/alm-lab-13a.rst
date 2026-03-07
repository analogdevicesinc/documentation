Activity: Amplifier Output Stages - ADALM1000
=============================================

Objective:
----------

To investigate simple push-pull or class B amplifier output stage examples.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

The role of an output stage is to provide power gain. It should have high input impedance and low output impedance. An obvious choice for this stage is the emitter follower. However, in order to provide both current sourcing and sinking capabilities, two complementary followers are needed, an NPN type to source current and a PNP type to sink current. The result is known as the push-pull configuration, of which figure 1 shows a simple configuration. Here R\ :sub:`1` and R\ :sub:`2` are used to sense the collector currents of Q\ :sub:`1` and Q\ :sub:`2`, as well as to limit these currents in case of output overloading.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 2 - 100 Ω resistors
| 1 - 2.2 KΩ resistor
| 2 - 10 KΩ resistors
| 2 - NPN transistors ( 2N3904 or SSM2212 )
| 2 - PNP transistors ( 2N3906 or SSM2220 )

Directions:
~~~~~~~~~~~

Before starting make sure the power supplies from the ALM1000 hardware are disconnected from the breadboard. The circuit and the connections to the Lab hardware are as indicated in figure 1. The channel B Hi-Z mode input CB-H should to be connected to the junction of Q\ :sub:`1` and Q\ :sub:`2` emitters.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-13a_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Push - Pull Output stage


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A voltage generator, CA-V, should be configured for a 100 Hz sine wave with 2.0 volt Min value and 3.0 volt Max value.

Procedure:
~~~~~~~~~~

Next, apply power and adjust the voltage generator so that CA-V is a 100 Hz triangle wave. Use the oscilloscope in the x-y mode to observe the voltage-transfer curve of the circuit. Save the curve to a .csv or .eps file for inclusion in your lab report, label all breakpoints, slopes, and saturation levels, and justify them in terms of circuit operation and given component values.

Switch the scope to the time display mode, and adjust the waveform generator so that CA-V is a 100 Hz sine wave with the Min and Max values both equal to 2.5 V.

Gradually increase the amplitude of the sine wave, keeping it centered on 2.5 V, until you just begin to see an signal on scope channel B appear at the output. For what range of amplitude values of CA-V can we say that both Q\ :sub:`1` and Q\ :sub:`2` are essentially off? Confirm this by observing the voltages of the current-sensing resistances R\ :sub:`1` and R\ :sub:`2`.

Lower the CA-V Min value to 1V, and raise the Max value to 4 V. Record the P-P amplitude of the output waveform as well as the collector currents of Q\ :sub:`1` and Q\ :sub:`2`, which can be found from the voltages across R\ :sub:`1` and R\ :sub:`2`, and justify your findings in terms of circuit operation and the given component values.

Repeat, but with CA-V Min value lowered to 0 V and Max value raised a 5 V; and comment.

Simulate the circuit of figure 1 using ADIsimPE (or SIMetrix), compare with your lab findings, and justify any differences.

Questions:
~~~~~~~~~~

Add questions here.

Reducing Output Distortion:
---------------------------

The large amount of distortion at the zero-crossings in the basic push-pull stage of figure 1 is a result of a dead zone when both the NPN and PNP emitter followers are off. The waveform's dead zone at the zero-crossings is dramatically reduced if we pre-bias the BJTs with two V\ :sub:`BE` drops, as shown in figure 2. Here, the pre-bias function is provided by diode connected NPN Q\ :sub:`1` and PNP Q\ :sub:`3`. Resistors R\ :sub:`1` and R\ :sub:`2` provide bias current and set the idle current that flows in the output devices Q\ :sub:`2` and Q\ :sub:`4`.

.. _directions-1:

Directions:
~~~~~~~~~~~

With the power disconnected, assemble the circuit of figure 2, keeping leads as short and neat as possible. NPN transistors Q\ :sub:`1` and Q\ :sub:`2`, PNP transistor Q\ :sub:`3`\ and Q\ :sub:`4` should be selected from the available devices with the best matching of V\ :sub:`BE`. Transistors fabricated in the same package such as the SSM2212 or the CA3046 tend to match much better than individual devices.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-13a_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Push - pull output stage with zero-crossing distortion elimination.


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Use the same hardware setup as you did for the circuit in figure 1.

.. _procedure-1:

Procedure:
~~~~~~~~~~

If we examine figure 2, the loop formed by the base emitter voltages of Q\ :sub:`1`, Q\ :sub:`2`, Q\ :sub:`3` and Q\ :sub:`4` we know that the sum of the voltage drops around the loop must sum to zero. Thus if Q\ :sub:`1` is identical to Q\ :sub:`2` and Q\ :sub:`3` is identical to Q\ :sub:`4`, the voltage around the loop will be zero only when the current in Q\ :sub:`1` is identical to the current in Q\ :sub:`2` and the current in Q\ :sub:`3` is identical to the current in Q\ :sub:`4`. Thus when the output is at 2.5 volts i.e. there is no current in R\ :sub:`L`, the input must also be at 2.5 volts.

Use the oscilloscope in the X-Y mode to observe the voltage-transfer curve of the circuit. Save the curve to a .csv or .eps file for inclusion in your lab report, label all breakpoints, slopes, and saturation levels, and justify them in terms of circuit operation and given component values.

.. _questions-1:

Questions:
~~~~~~~~~~

Display the input / output transfer curve of the circuit of figure 2, save the date to a .csv file or save the cures to a .eps file, label all breakpoints, slopes, and saturation levels. In your lab report justify them in terms of circuit operation and the given component values.

Apply a 100 Hz sine wave centered on 2.5 V offset and various amplitudes, and verify that the circuit yields Vout ? Vin all the way down to small amplitudes. What is the upper limit on the amplitude of CA-V before the circuit starts to distort? Justify quantitatively in terms of the transfer curve just observed.

Using your scope input, measure Vout as well as the voltage across R\ :sub:`3` and R\ :sub:`4` for the following DC values of Vin: 1 V, 2 V, 2.5 V, 3 V, 4 V. Then, tabulate Vout and the current in R\ :sub:`L` as well as the collector currents of Q\ :sub:`2` and Q\ :sub:`4` and comment. Use the DC shape of the voltage generator to set the DC value.

Measure the input impedance by inserting a 10 KΩ resistor in series with the signal generator (between CA-V and the emitters of Q\ :sub:`1`\ and Q\ :sub:`3`) and connecting the channel B Hi-Z input at the emitter of Q\ :sub:`1`. Use the CA-V - CB-V Math waveform to display the voltage across the 10 KΩ resistor. Capture the input current vs. the input voltage and calculate the input resistance from the slope of the curve. Justify your results based on the component values used in the circuit.

Simulate the circuit of figure 2 using ADIsimPE (or SIMetrix), compare with your lab findings, and justify any differences.

Another Configuration:
----------------------

Remembering the loop formed by the base emitter voltages of Q\ :sub:`1`, Q\ :sub:`2`, Q\ :sub:`3` and Q\ :sub:`4` we also know that the order of the voltage drops around the loop can be interchanged. So if we interchange the V\ :sub:`BE`'s of NPN Q\ :sub:`1` and PNP Q\ :sub:`3` we get the configuration shown in figure 3. This arrangement is sometime referred to as a "diamond buffer" because of the shape formed by the four emitter / base connections. Some of you may recognize the combination of Q\ :sub:`3` and Q\ :sub:`2` as the low offset follower we discussed earlier in the lab section on emitter followers. The circuit uses the V\ :sub:`BE` shift up of a PNP emitter follower to partially cancel the V\ :sub:`BE` shift down of an NPN emitter follower. Transistors Q\ :sub:`1` and Q\ :sub:`4` are simply the complement of Q\ :sub:`3` and Q\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-13a_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Emitter follower zero-crossing distortion elimination


.. _hardware-setup-2:

Hardware Setup:
~~~~~~~~~~~~~~~

Use the same hardware setup as you did for the circuit in figure 2.

.. _procedure-2:

Procedure:
~~~~~~~~~~

Display the input / output transfer curve of the circuit of figure 3, save the date to a .csv file or save the cures to a .eps file, label all breakpoints, slopes, and saturation levels, and justify them in terms of circuit operation and the given component values. How do they compare to the circuit in figure 2?

.. _questions-2:

Questions:
~~~~~~~~~~

Apply a 100 Hz sine wave centered on 2.5 V and various amplitudes, and verify that the circuit yields Vout ? Vin all the way down to small amplitudes. What is the upper limit on the amplitude of CA-V before the circuit starts to distort? Justify quantitatively in terms of the transfer curve just observed.

Using your scope input, measure Vout as well as the voltage across R\ :sub:`3` and R\ :sub:`4` for the following DC values of Vin: 1V, 2V, 2.5 V, 3 V, 4 V. Then, tabulate Vout and the current in R\ :sub:`L` as well as the collector currents of Q\ :sub:`2` and Q\ :sub:`4` and comment. Use the DC shape of the CA generator to set the DC value.

Measure the input impedance by inserting a 10 KΩ resistor in series with the signal generator (between CA-V and the bases of Q\ :sub:`1`\ and Q\ :sub:`3`) and connect the channel CB-H scope to measure the voltage across the 10 KΩ resistor as you did for the circuit in figure 3. Capture the input current vs. the input voltage and calculate the input resistance from the slope of the curve. Justify your results based on the component values used in the circuit. How do your results compare to what you measured for the circuit in figure 2?

Simulate the circuit of figure 3 using ADIsimPE (or SIMetrix), compare with your lab findings, and justify any differences.

Yet another configuration:
--------------------------

In figure 4 we see another slight variation on the circuit in figure 3. Since the aim of these output stages id to provide an output voltage that is ideally identical to the input, transistors Q\ :sub:`1` and Q\ :sub:`2` can be thought of as being "diode" connected similar to the arrangement in figure 2 but with the NPN and PNP interchanged. This will not be exactly the case in real life so there will be a small error current flowing back into the emitters of Q\ :sub:`2` and Q\ :sub:`4` based on any mismatches between the devices.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-13a_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Push-Pull output stage version 4


Repeat the same test you performed on the figure 2 and figure 3 circuits on the circuit in figure 4.

**For Further Reading:**

| `Push-Pull Output <https://en.wikipedia.org/wiki/Push-pull_output>`_
| :adi:`Increase amplifier output drive using a push-pull stage <en/technical-articles/increase-amplifier-output-drive-using-a-push-pull-amplifier-stage.html>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/electronics>`
