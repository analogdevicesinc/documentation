Chapter 4: Op Amp applications - Advanced topics
================================================

In this chapter we explore a number of example op amp configuration that are presented to illustrate certain advanced applications for operational amplifiers. Many of these more advanced uses for op amps will probably make more sense after the reader has studied the material on Bipolar Junction and Field Effect transistors in later chapters. The reader can skip this material for now and circle back after gaining an understanding of how transistors work.

4.1 Precision Voltage to Current Converter
------------------------------------------

The very high forward gain (A\ :sub:`VOL`) and differential input nature of the operational amplifier can be used to create a nearly ideal voltage controlled current source or V-to-I converter. Note in figure 4.1, the input voltage to be converted is applied to the non-inverting input terminal of the op amp. The inverting input terminal is connected in feedback to one end of the resistor R\ :sub:`1` and the source of transistor M\ :sub:`1`. The output of the op-amp drives the Gate of the transistor. The high open loop gain of the amplifier will force the Gate of M\ :sub:`1` to the required voltage such that V\ :sub:`IN` appears across R\ :sub:`1`. The current in R\ :sub:`1` will thus be V\ :sub:`IN`/R\ :sub:`1` and will flow only in the Source of M\ :sub:`1` and also thus appear in the Drain of M\ :sub:`1`\ as I\ :sub:`OUT`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.1 Precision Voltage to Current converter


This configuration is also often referred to as an Active Cascode. To understand the concept of the cascode or common gate (base) amplifier the reader is directed to study the section in Chapter 9 on the Cascode (9.3).

An instructive application for this circuit technique can be found in this article on how to :adi:`convert 1V to 5V signal to 4mA to 20mA output. <media/en/technical-documentation/technical-articles/d61_en-convert.pdf>`

4.1.1 The Active Voltage to Current Converter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Figure 4.1.1 shows a classic voltage to current (V-to-I) converter. The resistor values can be selected such that the output current in the load, varies only with the input voltage, V\ :sub:`IN`, and is independent of the load. The circuit is widely used in industrial instruments for supplying a 4 to 20 mA signal for example. Also often referred to as a Howland current pump this configuration has two advantages over the MOSFET based circuit shown in figure 4.1. The first is a high output impedance and the second is the ability to provide bipolar (both sourcing and sinking) output currents.

The circuit has its limitations due in part to the requirement that the resistor ratios must be quite accurate to obtain a near ideal current source. Published literature describing the circuit provides design methods that are for special cases or are for approximate designs. In this chapter we explore simple design formulas that can be used to determine the component values that produce a near ideal current source. These formulas also provide a general method for calculating the output current, I\ :sub:`LOAD`, for any selection of resistor values, not just the constant-current selection. Usually in order to improve stability, the circuit is made symmetrical. Therefore R\ :sub:`1` = R\ :sub:`3`, R\ :sub:`2` = R\ :sub:`4`, and R\ :sub:`S` = R\ :sub:`S'`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.1.1 non-inverting voltage to current converter


For a true current output, I\ :sub:`LOAD`, as a function of the input voltage, V\ :sub:`IN`, you must satisfy the following equations:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-e1.png
   :align: center
   :width: 300px

The load current is:

|image1|\ (1)

The Output impedance is:

|image2|\ (2)

In equation 1, any four of the terms can be arbitrarily selected and then the fifth term is determined by solving the resulting equation. With R\ :sub:`1` = 150 kΩ, R\ :sub:`2` = 15 kΩ, R\ :sub:`S` = 50 Ω, and V\ :sub:`IN` can vary from 0 to 5 V, I\ :sub:`LOAD` will vary from 0 mA to 10 mA, and the circuit has a very high output impedance.

if R\ :sub:`S` changes from 50 Ω to 200 Ω, the feedback changes fourfold, and you would expect that the output current would change fourfold, to 0 to 2.5 mA. You can check the result by substituting in the general formula for the output current.

Looking at equation 2, the output impedance, Z\ :sub:`OUT` will be infinity if R\ :sub:`1`\ =R\ :sub:`3`, R\ :sub:`2`\ =R\ :sub:`4` and R\ :sub:`S`\ =R\ :sub:`S'` because the bottom term in the ratio will be exactly zero. To the extent that the resistors do not match the output impedance could be either positive of negative. For example if R\ :sub:`3` were slightly larger than R\ :sub:`1` the bottom term would be negative.

More details on the Howland current source can be found in :adi:`A large current source with high accuracy and fast settling <media/en/analog-dialogue/volume-52/number-4/a-large-current-source-with-high-accuracy-and-fast-settling.pdf>` and :adi:`Choose resistors to minimize errors in grounded-load current source <media/en/analog-dialogue/volume-47/number-2/articles/choose-resistors-to-minimize-errors.pdf>`.

4.2 Precision Current to Voltage Converter
------------------------------------------

A simple single resistor can be used to convert a current into a voltage but the voltage cannot be used directly to drive other parts of a system without potentially disturbing or altering the voltage. Often a buffer amplifier is required or the voltage may need to be shifter or "referred" to a different node (supply voltage or ground) in the circuit. Op amp circuits like those in figure 4.2 can perform this function.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.2 Precision Current to Voltage converter


Two configurations are shown in figure 4.2. Version (a) produces an output voltage V\ :sub:`OUT` from input current I\ :sub:`IN`. The output voltage is produced with respect to ground due to the virtual ground at the - input terminal of the amplifier and is negative (V\ :sub:`OUT` = -I\ :sub:`IN`\ R\ :sub:`1`) for currents flowing into the virtual ground (from the +V as shown) and positive for currents flowing out of the virtual ground (flowing toward -V). Version (b) produces an output voltage V\ :sub:`OUT` from input current I\ :sub:`IN` as well but now it is produced with respect to some negative node potential, -V. Unlike version (a) which accepts both sourcing and sinking currents, version (b) will only operate for currents flowing into the virtual ground at the - input terminal. There is an advantage to using a MOSFET, M\ :sub:`1`, over a bipolar transistor. In the MOSFET all the current in the drain also flows in the source (no current in gate) whereas in the case of a BJT the emitter current is increased due to the base current. The current in R\ :sub:`1` will thus be slightly larger than I\ :sub:`IN` and the voltage V\ :sub:`OUT` will not be exactly equal to I\ :sub:`IN`\ \*R\ :sub:`1`.

4.3 Precision Current Mirror
----------------------------

The simple transistor based current mirror is covered in detail in Chapter 11. Here we introduce the op amp in the feedback loop of the diode connected transistor. The very large gain of the amplifier greatly reduced many of the sources of error found in the simple two transistor current mirror.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.3 Precision Current Mirror


The two MOSFETs M\ :sub:`1` and M\ :sub:`2` must be well matched (and be at the same temperature) as well as the two resistors R\ :sub:`1` and R\ :sub:`2` if I\ :sub:`OUT` is to be well matched to I\ :sub:`IN`. If two bipolar (NPN) transistors were to be used in this case, the op amp will supply all the base current for the two transistors and providing the a and V\ :sub:`BE` (I\ :sub:`S` actually) of the two devices is well matched (and R\ :sub:`1` and R\ :sub:`2` of course) the gain of the mirror will be nearly exactly 1 in spite of the finite ß. It is also important to note that the feedback current from the drain of M\ :sub:`1` is to the + input terminal of the op amp. This is because of the phase inversion of the common source configuration of M\ :sub:`1`.

4.4 Simulated Inductor
----------------------

Before the introduction of the transistor and the integrated circuit, coils of wire with large inductance were used in electronic filters. An inductor can be replaced by a much smaller assembly consisting of a capacitor, operational amplifiers or transistors, and resistors. This is especially useful in integrated circuit technology where building inductors from large loops of wire is impractical.

The circuit in Figure 4.4 reverses the operation of a capacitor, thus making a simulated inductor. An inductor resists any change in its current, so when a dc voltage is applied to an inductance, the current rises slowly, and the voltage falls as the external resistance becomes more significant.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.4. Simulated Inductor Circuit


An inductor passes low frequencies more readily than high frequencies, the opposite of a capacitor. An ideal inductor has zero resistance. It passes dc without limitation, but it has infinite impedance at infinite frequency.

For the circuit in figure 4.4, if a DC voltage step is suddenly applied to the inverting input through resistor R\ :sub:`L`, the op amp ignores the sudden step because the change is also coupled directly to the non-inverting input via C\ :sub:`1`. The op amp represents high impedance, just as an inductor does. As C\ :sub:`1` charges through R\ :sub:`1`, the voltage across R\ :sub:`1`\ falls, so the op-amp draws current from the input through R\ :sub:`L`. This continues as the capacitor charges, and eventually the op-amp has an input and output close to virtual ground because the lower end of R\ :sub:`1` is connected to ground.

When C\ :sub:`1` is fully charged, resistor R\ :sub:`L` limits the current flow, and this appears as a series resistance within the simulated inductor. This series resistance limits the Q of the inductor. Real inductors generally have much less resistance than the simulated variety.

| There are some limitations of a simulated inductor like this:
| \* One end of the inductor is connected to virtual ground.
| \* The simulated inductor cannot be made with high Q, due to the series resistor R\ :sub:`L`.
| \* It does not have the same energy storage as a real inductor. The collapse of the magnetic field in a real inductor causes large voltage spikes of opposite polarity. The simulated inductor is limited to the voltage swing of the op amp, so the flyback pulse is limited to the voltage swing.

4.5 All-Pass Filter
-------------------

The all-pass filter passes all frequencies at the same gain. It is used to change the phase of the signal, and it can also be used as a phase-correction circuit. The circuit shown in figure 4.5 has a 90° phase shift at F(90°). At DC, the phase shift is 180°, and at high frequencies it is 0°. R\ :sub:`1` = R\ :sub:`2` = R\ :sub:`3` = R F(90°) = 1/(2?R\ :sub:`1`\ \*C\ :sub:`1`)

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.5. All-Pass Filter Circuit


.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.6 Gain/Phase simulation plot of All-Pass circuit


4.6 Negative impedance converter
--------------------------------

The negative impedance converter (NIC) is an op-amp circuit which acts as a negative load. This is achieved by introducing a phase shift of 180° (inversion) between the voltage and the current for a signal source. There are two versions of this circuit - with voltage inversion (VNIC) and with current inversion (INIC). The basic circuit of an INIC and its analysis is shown figure 4.7.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.7 Negative impedance converter.


INIC is a non-inverting amplifier (the op-amp and the voltage divider R\ :sub:`1`, R\ :sub:`2` in figure 4.7) with a resistor (R\ :sub:`3`) connected between its output and input. The op-amp output voltage is

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-e4.png
   :align: center
   :width: 200px

The current going from the operational amplifier output through resistor R\ :sub:`3` toward the source Vin is -Is, and

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-e5.png
   :align: center
   :width: 200px

So the input V\ :sub:`in` experiences an opposing current - I\ :sub:`in` that is proportional to V\ :sub:`in`, and the circuit acts like a resistor with negative resistance

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-e6.png
   :align: center
   :width: 200px

In general, elements R\ :sub:`1`, R\ :sub:`2`, and R\ :sub:`3` need not be pure resistances (i.e., they may be capacitors, inductors, or impedance networks).

4.7 Capacitance Multiplier
--------------------------

The circuit in figure 4.8(a) uses an op-amp and a small capacitor, C\ :sub:`1`, to simulate a much larger capacitor. It simulates the simple RC circuit of figure 4.8(b); the resistor R\ :sub:`2`\ is the same size as the resistor in the circuit being simulated (R\ :sub:`3`), but the capacitor C\ :sub:`1` is N times smaller than C\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.8 Op-amp capacitance multiplier


Current flows from the input source through R\ :sub:`1` to the capacitor (C\ :sub:`1`). If R\ :sub:`1`, for example, is 100 times larger than R\ :sub:`2`, there is 1/100th the current through it into the capacitor. For a given input voltage, the rate of change in voltage in C\ :sub:`1`\ is the same as in the equivalent C\ :sub:`2`\ in figure 4.8(b), but C\ :sub:`2` appears to have 100 times the capacitance to make up for 1/100th the current.

The voltages across the two capacitors are the same, but the currents are not. The op-amp causes the negative input to be held at the same voltage as the voltage across C\ :sub:`1`. This means R\ :sub:`2` has the same voltage across it as R\ :sub:`3`, and therefore the same current. Since the total current from V\ :sub:`IN` is the sum of the current in R\ :sub:`1` and R\ :sub:`2` and R\ :sub:`2` is N times smaller than R\ :sub:`1` the apparent charging current is N+1 times larger than the current in C\ :sub:`1`.

4.8 Using Op Amps As Comparators
--------------------------------

Op Amps and comparators may seem interchangeable at first glance based on their symbols and pinouts and one might be tempted to use or substitute readily available op amps as voltage comparators in their designs. There are some important differences however. Comparators are designed to work without negative feedback or open-loop, they are designed to drive digital logic circuits from their outputs, and they are designed to work at high speed with minimal instability. Op amps are not generally designed for use as comparators, they may saturate if over-driven which may cause it to recover comparatively slowly. Many have input stages which behave in unexpected ways when driven with large differential voltages, in fact, in many cases, the differential input voltage range of the op amp is limited. And op amp outputs are rarely compatible with logic.

Yet many designers still try to use op amps as comparators. While this may work at low speeds and low resolutions, many times the results are not satisfactory. Not all of the issues involved with using an op amp as a comparator can be resolved by reference to the op amp data sheet, since op amps are not intended for use as comparators.

The most common issues are speed (as we have already mentioned), the effects of input structures (protection diodes, phase inversion in FET amplifiers, and many others), output structures which are not intended to drive logic, hysteresis and stability, and common-mode effects.

4.8.1 Speed Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~

Most comparators are quite fast, but so are many op amps. Why should we expect low speed when using an op amp as a comparator?

A comparator is designed to be used with large differential input voltages, whereas op amps normally operate with their differential input voltage minimized by negative feedback. When an op amp is over-driven, sometimes by as little as a few millivolts, some of the internal stages may saturate. If this occurs the device will take a comparatively long time to come out of saturation and will therefore be much slower than if it always remained unsaturated (see figure 4.9).

The time to come out of saturation of an overdriven op amp is likely to be considerably longer than the normal group delay of the amplifier, and will often depend on the amount of overdrive. Since few op amps have this saturation recovery time specified for various amounts of overdrive it will generally be necessary to determine, by experimental measurements in the lab, the behavior of the amplifier under the conditions of overdrive to be expected in a particular design.

The results of such experimental measurements should be regarded with suspicion and the values of propagation delay through the op amp comparator which is chosen for worst-case design calculations should be at least twice the worst value seen in any experiment.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.9: Effects of Saturation on Amplifier Speed when Used as a Comparator


4.8.2 Output Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output of a comparator is designed to drive a particular logic family or families, while the output of an op amp is designed to swing close to it's supply rails if not to the supply rails. Frequently the logic being driven by the op amp comparator will not share the op amp's supplies and the op amp rail to rail swing may go outside the logic supply rails-this will probably damage the logic circuitry, and the resulting short circuit may damage the op amp as well.

There are three types of logic which we must consider: ECL, TTL and CMOS.

ECL is a very fast current steering logic family. It is unlikely that an op amp would be used as a comparator in applications where ECL's highest speed is involved, for reasons given above, so we shall usually be concerned only to drive ECL logic levels from an op amp's signal swing and some additional loss of speed due to stray capacities will be unimportant. To do this we need only three resistors, as shown in figure 4.10.

R\ :sub:`1`, R\ :sub:`2` and R\ :sub:`3` are chosen so that when the op amp output is positive the level at the gate is -0.8 V, and when it is low it is -1.6 V. ECL is occasionally used with positive, rather than negative, supplies (often called PECL where the -5.2V rail is connected to ground and the ground is connected to a positive supply voltage), the same basic interface circuit may be used but the values must be recalculated. Using low resistance values for R\ :sub:`1`, R\ :sub:`2` and R\ :sub:`3` will minimize the effects of stray capacitance but at the same time will increase power consumption.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.10: Op Amp Comparator Driving ECL Logic


Although CMOS and TTL input structures, logic levels, and current flows are quite different (although some versions of CMOS is specified to work with TTL input levels) the same interface circuitry will work perfectly well with both types of logic, since they both work for logic 0 near to 0V and logic 1 near to +5V or whatever the positive supply rail is for that logic family.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.11: Op Amp Comparator Driving TTL or CMOS Logic


The simplest interface uses a single N-channel MOS transistor, M\ :sub:`1` and a pull-up resistor, R\ :sub:`L`, as shown in figure 4.15. It is important to note here that this interface circuit inverts the output of the op amp and thus reverses the sense of the + and - inputs. A similar circuit may be made with an NPN transistor, Q\ :sub:`1`, R\ :sub:`L`, and an additional resistor, R\ :sub:`1` and diode D\ :sub:`1`. A resistor between the op amp output and the MOS FET gate and the diode to ground are generally not needed (left side of figure 4.11) because the gate can withstand relatively large voltages with respect to the source. In the case of the NPN BJT (right side of figure 4.11) the resistor serves to limit the base current and the diode limits the maximum reverse bias on the base to one diode drop (-0.7V) below ground. These circuits are simple, inexpensive and reliable, and the outputs of several op amps may be connected through separate transistors with their collectors connected in parallel and a single R\ :sub:`L` to give a "wired-or" function. The speed of the 0-1 transition depends on the value of R\ :sub:`L` and the stray capacity of the output node. The lower the value of R\ :sub:`L` the faster the response will be, but the higher the power consumption.

By using two MOS devices, one P-channel and one N-channel, it is possible to make a CMOS/TTL interface using only two components which has no quiescent power consumption in either state (figure 4.16). Furthermore, it may be made inverting or non-inverting by simple positioning of components. It does, however, have a large current surge during switching, when both devices are on at once, and unless MOS devices with high channel resistance are used a current limiting resistor may be necessary to reduce this effect. It is also important, in this application and the one in figure 4.11, to use MOS devices with gate-source breakdown voltages, V\ :sub:`BGS`, greater than the output voltages of the comparator in either direction. A value of V\ :sub:`BGS` > ±25 V is common in MOS devices and is usually adequate, but many MOS devices contain gate protection diodes which reduce the value-these should not be used.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f13.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.12: Op Amp Comparator with CMOS Driver


4.8.3 Input Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a number of effects which must be considered regarding the inputs of op amps when used as comparators. The first-level assumption engineers make about all op amps and comparators is that they have infinite input impedance and can be regarded as open circuits (except for current feedback (transimpedance) op amps, which have a high impedance on their non-inverting input but a low impedance of a few tens of ohms on their inverting input)

But many op amps (especially bias-compensated ones such as the OP-07 and its many descendants) contain protective circuitry to prevent large differential input voltages from damaging the input stage transistors. Protective circuitry such as current limiting resistors and clamp diodes, as shown in figure 4.13, are often integrated between the input pins and the sensitive input transistors. This protection circuit will greatly lower the input impedance for differential input voltages greater than +/- 700 mV.

Other op amp designs contain more complex input circuitry, which only has high impedance when the differential voltage applied to it is less than a few tens of mV, or which may actually be damaged by differential voltages of more than a few volts. It is therefore necessary, when using an op amp as a comparator, to study the manufacturer's data sheet to determine how the input circuitry behaves when large differential voltages are applied to it. It is always necessary to study the data sheet when using an integrated circuit to ensure that its non-ideal behavior, and every integrated circuit ever made has some non-ideal behavior, is compatible with the proposed design - it is just more important than usual in the present case.

Of course some comparator applications never involve large differential voltages-or if they do the comparator input impedance when large differential voltages are present is comparatively unimportant. In such cases it may be appropriate to use as a comparator an op amp whose input circuitry behaves non-linearly-but the issues involved must be considered, not just ignored.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f14.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4.13: Op Amp Input Structure with Protection


As mentioned elsewhere in this text, nearly all BIFET op amps exhibit anomalous behavior when their inputs are close to one of their supplies (usually the negative supply). Their inverting and non-inverting inputs may become interchanged. If this should occur when the op amp is being used as a comparator the phase of the system involved will be inverted, which could well be inconvenient. The solution is, again, careful reading of the data sheet to determine just what common-mode range is acceptable.

Also, the absence of negative feedback means that, unlike that of op amp circuits, the input impedance is not multiplied by the loop gain. As a result, the input current varies as the comparator switches. Therefore the driving impedance, along with parasitic feedback paths, can play a key role in affecting circuit stability. While negative feedback tends to keep amplifiers within their linear region, positive feedback forces them into saturation.

Section Summary
~~~~~~~~~~~~~~~

Operational amplifiers are not designed to be used as comparators, so this section has been, intentionally, a little discouraging. Nevertheless there are some cases where the use of an op amp as a comparator is a useful engineering decision-what is important is to make it a considered decision, and ensure that the op amp chosen will perform as expected. To do this it is necessary to read the manufacturer's data sheet carefully, to consider the effects of non-ideal op amp performance, and to calculate the effects of op amp parameters on the overall circuit. Since the op amp is being used in a non-standard manner some experimentation may also be necessary, since the amplifier used for the experiment will not necessarily be typical and the results of experiments should always be interpreted somewhat pessimistically.

**ADALM1000 Lab Activity** :doc:`Comparators </wiki-migration/university/courses/alm1k/alm-lab-comp>`

4.9 Operational amplifier Schmitt trigger
-----------------------------------------

Although the simple voltage comparator circuit using either an ordinary operational amplifier or a special comparator is often adequate, the input waveform may be slow or have noise superimposed on it. This can result in the possibility that the output will switch back and forth several times as the input transitions through the comparator threshold voltage. The very large open loop gain of the amplifier will allow only small levels of noise on the input to cause the output to change. This may not cause a problem in some circumstances, but if the output from the operational amplifier comparator is being fed into fast logic circuitry, then it can often result in problems. For example, if the desire is to count the number of times the input crosses the threshold then these multiple output changes per input transition will give false readings.

The problem can be solved very easily by adding some positive feedback to the operational amplifier or comparator circuit. This is provided by the addition of R\ :sub:`3` in the circuit in figure 4.14. The circuit is known as a Schmitt trigger. Resistor divider R\ :sub:`1` and R\ :sub:`2` set the comparison voltage at the non-inverting input of the op amp.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-f15.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4.14 Operational amplifier Schmitt trigger circuit


The effect of the new resistor (R\ :sub:`3`) is to give the circuit different switching thresholds dependent upon the output state of the comparator or op amp. When the output of the comparator is high, this voltage is fed back to the non-inverting input of the op amp or comparator. As a result the comparison threshold becomes higher. When the output is switched low, the comparison threshold is lowered. This gives the circuit what is called hysteresis.

It is straight forward to calculate the resistor values needed for the Schmitt trigger circuit. The center voltage about which the circuit will switch is determined by the voltage divider consisting of R\ :sub:`1` and R\ :sub:`2`. This should be chosen first. Then the feedback resistor R\ :sub:`3` can be calculated. This will provide a level of hysteresis that is equal to the output swing of the op amp reduced by the voltage divider (attenuation) formed as a result of R\ :sub:`3` and the parallel combination of R\ :sub:`1` and R\ :sub:`2`. The higher the value of R\ :sub:`3` with respect to R\ :sub:`1`\ \||R\ :sub:`2` the smaller the hysteresis, or the difference between the two threshold levels.

The fact that the positive feedback applied within the circuit ensures that there is effectively a higher gain and therefore the switching is faster. This is particularly useful when the input waveform may be slow. However a speed up capacitor can be applied within the Schmitt trigger circuit to increase the switching speed still further. By placing a capacitor across the positive feedback resistor R\ :sub:`3`, the gain can be increased during the changeover, making the switching even faster. This capacitor, known as a speed up capacitor may be anywhere between 10 pF and 100 pF dependent upon the circuit.

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-3>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-5>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-e2.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr4-e3.png
   :width: 300px
