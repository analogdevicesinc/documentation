Class A NPN Emitter-Follower Amplifier
======================================

.. image:: https://wiki.analog.com/_media/analogTV>5180379850001
   :alt: analogTV>5180379850001
   :align: right

Introduction
------------

The common-emitter amplifier introduced in the "Class A NPN Common-Emitter Amplifier" lab provided voltage and current amplification, but suffered from a large output resistance that was equal to the equivalent collector resistance that was present for AC signals. The emitter-follower, EF, also called common-collector, CC, amplifier provides nearly unity voltage gain, and current gain, which can be large, and low output resistance. Emitter-follower amplifiers are commonly used as output stages that are capable of driving low impedance loads due to their current gains and low output resistances. The name "emitter-follower" originates from the fact that the output signal, taken at the emitter, follows the input signal, applied at the base, with nearly unity gain. "Emitter-follower" is more descriptive than "common-collector," and will be used henceforth for this reason. As with the CE amplifier, we will study the EF amplifier using a single transistor biased in a Class A configuration.

Unlike the CE amplifier, the output voltage and input voltage of an EF amplifier are in-phase with each other and of nearly the same magnitude. This is the sense in which the output voltage at the emitter "follows" the input. The collector is generally connected directly to the power supply and the emitter is connected to another supply voltage -- often ground -- through an emitter resistor, R\ :sub:`E`. The operation of an EF amplifier constitutes a form of negative feedback. Negative feedback systems are discussed in further detail in later labs, but can be briefly described as systems in which part or all of an output quantity is fed back upstream in the system in such a way as to reduce an error that exists between the existing condition and the desired condition. Automotive cruise control is an example of an everyday negative feedback system in which the speed of an automobile is constantly monitored and adjusted in such a way as to minimize the error between the current speed and the speed set by the driver. Negative feedback systems are often used to regulate physical phenomena. Reference to the schematic in the Procedure section of the lab will be helpful when reading the remainder of this section. In the emitter-follower amplifier, the negative feedback occurs as follows: starting at the emitter, as the emitter voltage v\ :sub:`E` increases, the base-emitter voltage v\ :sub:`BE` decreases, which in turn reduces the base current i\ :sub:`B`, which reduces the collector current i\ :sub:`C` by the i\ :sub:`C` = βi\ :sub:`B` relationship; recalling that for large β we can say that i\ :sub:`E` ≈ i\ :sub:`C` (the exact relationship between i\ :sub:`E` and i\ :sub:`B`) is i\ :sub:`E` = (1 + β)i\ :sub:`B`, and (1 + β)i\ :sub:`B` ≈ βi\ :sub:`B` for large β) we see that i\ :sub:`E` decreases as i\ :sub:`C`, thuis reducing v\ :sub:`E`. This negative feedback action regulates the bias point and voltage gain of the emitter-follower, keeping the voltage gain close to unity. This same feedback loop helps regulate the operating bias point in the CE amplifier. In many, if not most, applications, we can view the emitter follower as having unity voltage gain with the output voltage shifted down from the input voltage by one v\ :sub:`BE` drop. The bias point considerations for the Class A emitter-follower amplifier are the same as for the Class A CE amplifier.

The current gain and low output impedance of the emitter-follower amplifier make it ideal for driving low impedance loads, which may be DC- or AC-coupled. Many amplifiers are designed with emitter-follower output stages placed after voltage gain stages. In this lab we design, build, and evaluate a single Class A emitter-follower amplifier, then place it after the CE amplifier used in the Class A NPN Common-Emitter Amplifier lab in a DC-coupled fashion to illustrate how it can be used to drive an AC-coupled load much heavier than the 1 KΩ load used in that lab, and that it eliminates the gain loss due to the loading of the high output resistance of the CE stage. An example of how an emitter-follower stage can be added to an operational amplifier "inside the loop" to drive a low impedance loudspeaker is shown in the "Audio Amplifier with Electret Microphone" lab.

Objective
---------

To design, build, and test an emitter-follower amplifier using a 2N3904 NPN transistor, with an input resistance of at least 1 KΩ that is capable of driving an AC-coupled 47 Ω load with a 1 V\ :sub:`P-P` sine wave. To increase the load to 10 Ω and observe that this heavier load can still be driven, limited by the available current. To verify that the amplifier has approximately unity gain and that the Q-point is close to its designed value. To observe the buffering effect of the emitter follower and show how output loading is minimal as compared with a CE amplifier. To understand and be able to calculate emitter-follower amplifier voltage gain, power gain, efficiency, and power dissipation. To append the emitter-follower stage to the output of the CE amplifier designed in the "Class A NPN Common-Emitter Amplifier" lab in a DC-coupled fashion to show how buffers are added to voltage gain stages in order to drive low impedance loads. Following completion of this lab you should be able to explain the basic operation of an emitter-follower amplifier, explain how negative feedback stabilizes the gain of a common-emitter amplifier, explain why output loading does not affect an emitter-follower amplifier nearly as much as a CE amplifier, and calculate the amplifier voltage gain, power gain, efficiency, and power dissipation of a Class A emitter-follower amplifier.

Materials and Apparatus
-----------------------

-  Data sheet handout for the 2N3904 NPN transistor
-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (2) 2N3904 NPN transistor from the ADALP2000 Analog Parts Kit
-  (1) 10 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 47 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 68 Ω resistor from the ADALP2000 Analog Parts Kit
-  (2) 100 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 470 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 1 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 1.5 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (2) 4.7 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 6.8 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (2) 47 μF capacitor from the ADALP2000 Analog Parts Kit
-  (1) 220 μF capacitor from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Construct the following circuit on the solderless breadboard\


|lab_11_image_1.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard. Note that this circuit has been added to the CE amplifier breadboard from the "Class A NPN Common-Emitter Amplifier" lab.\

|lab_11_assembly_image_1.png|

-  Run PixelPulse and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Disable “Repeated Sweep” mode; waveforms can be paused for analysis
-  Set up the M1K to source voltage/measure current on Channel A and measure voltage on Channel B
-  Set up Channel A source waveform for a 500 Hz “Sine” output that swings between 2.5 V and 3.5 V
-  Observe the output voltage into the 47 Ω load resistor on Channel B and verify that it is swinging nominally +/- 0.5 V about the 2.5 V baseline and that it is in-phase with the input signal
-  Observe the voltage at the emitter on Channel B and verify that it is swinging nominally +/- 0.5 V about a 1.7 V bias voltage and that it is also in-phase with the input signal. Note that these bias voltages may vary somewhat due to resistor tolerances
-  Note any visible distortions in the output signals
-  Remove the input signal and measure the DC bias voltages at the base, emitter, and collector, and verify that these are at their designed levels, allowing for resistor tolerances
-  Calculate the voltage gain, power gain, and efficiency of this amplifier; compare the power dissipation of this circuit with that of the CE amplifier in the "Class A NPN Common-Emitter Amplifier" lab
-  Set up Channel A source waveform for a 500 Hz “Sine” output that swings between 2.43 V and 2.57 V
-  Remove the AC-coupling capacitor and bias resistors from the amplifier input and connect it to the output of the CE amplifier from the "Class A NPN Common-Emitter Amplifier" lab as shown in the schematic. Note the change in the emitter-follower bias point\

|lab_11_image_2.png|

-  Refer to the illustration below for one way to interconnect the two amplifiers on the solderless breadboard\

|lab_11_assembly_image_2.png|

-  Verify that the voltage across the 47 Ω load resistor is swinging +/- 0.5V about the 2.5 V bias voltage
-  Calculate the rms power dissipation in the load resistor
-  Estimate the voltage swing that would be present across the 47 Ω load resistor if it were driven by the CE stage alone, without the emitter-follower buffer in place
-  Reduce the swing of the input voltage to 2.48 V to 2.52 V
-  Replace the 47 Ω load resistor with a 10 Ω resistor
-  Verify that the output voltage swings 300 mV\ :sub:`P-P` about the 2.5 V bias voltage
-  Calculate the load current into the 10 Ω load resistor

Theory
------

The emitter-follower amplifier presents a high input resistance to signals applied to its base and provides a low resistance effective voltage source at its output. These characteristics make the emitter-follower amplifier well suited for use as a voltage *buffer* amplifier. Buffer amplifiers are used to buffer heavy loads from signal sources that have a high output resistance. A good buffer has a high input resistance so as not to significantly load the output resistance of the source that is being buffered and a low resistance voltage source output that is capable of driving heavy loads with minimal loading loss.

Our amplifier needs to drive a 47 Ω load with a +/-0.5 V sine wave, which requires approximately +/-10.6 mA. We will make the base bias point at about mid-supply. Starting with a mid-supply base bias voltage, we can estimate the emitter voltage to be 2.5 V - 0.7 V = 1.8 V. When the output sine wave is at its minimum level, the emitter resistor must sink all of the current fed back from the load (remember that the 47 μF capacitor acts like a short circuit to the 500 Hz signal compared with the 47 Ω load resistor). The current from the emitter backs off, allowing the current flowing back from the load to pass through the emitter resistor. A KCL calculation made at the emitter shows that the current out of the emitter is equal to the sum of the current flowing to ground through the emitter resistor and the current fed back from the load. The current flowing through the emitter resistor must therefore be at least equal to the maximum current flowing back from the load when the output waveform is at its minimum, otherwise we would have to have a negative emitter current. When the output signal is at its minimum, the voltage on the emitter is approximately 1.8 V - 0.5 V = 1.3 V. The maximum current flowing back from the load, which occurs at the waveform minimum, was determined to be 10.6 mA. The emitter current must be at least this large at this point so the maximum emitter resistor value is 1.3 V/10.6 mA ≈ 123 Ω. We want to have some margin, and 100 Ω would be a little too close, so we will go with the next smallest value of 68 Ω for the emitter resistor. This value gives an approximate Q-point bias current of 1.8 V/68 Ω ≈ 26.5 mA.

If we want to make a first-round estimate of the voltage drop incurred due to base current, remembering that i\ :sub:`E` ≈ i\ :sub:`C`, we use β = 200 to estimate the base current as i\ :sub:`B` ≈ 26.5 mA/200 ≈ 133 μA. The base bias current is on the high side because we are using a large emitter current. The voltage drop due to the base current can be estimated to be (133 μA)(2.2 KΩ||2.2 KΩ) ≈ 0.15 V. This reduction will in turn reduce the emitter voltage, which will reduce the emitter current, which will reduce the base current and its associated voltage drop, so a reasonable estimate for base bias voltage reduction due to base bias current would be about 0.1 V, so we will use 2.4 V for the base voltage. Now, a more accurate emitter bias voltage can be established as 2.4 V - 0.7 V = 1.7 V. The emitter bias current can be calculated as 1.7 V/68 Ω = 25 mA.

The input resistance looking into the base of the transistor used in the emitter-follower amplifier R\ :sub:`i,base` is the same as that of the CE amplifier

:math:`R_{i,base} = βr_e + (1 + β)R_E`

Using β = 200 from the Introduction to Transistors lab, and substituting numbers from this lab, we have

:math:`\displaystyle R_{i,base} = 200\frac{26 mV}{{25 mA}} + (1 + 200)({68 Ω}||{47 Ω}) ≈ 208 Ω + 11.5 KΩ ≈ 5.6 KΩ`

When we use the voltage divider to provide base bias, we need to include the resistors in the divider in parallel with the input resistance looking into the base, so the total input resistance R\ :sub:`i`\ is

:math:`R_i = 2.2 KΩ||2.2 KΩ||5.6 KΩ ≈ 0.92 KΩ`

Note that this result falls slightly short of our design goal of having a minimum input resistance of 1 KΩ. This is primarily due to the 2.2 KΩ resistors that were used to set up the base bias voltage. We could increase the value of these resistors a small amount and raise the input resistance to at least 1 KΩ, but the next largest value in the kit is 4.7 KΩ, which would give us considerably more unnecessary voltage drop on the base bias voltage. The best solution, if all commercially available resistor values were available, would be to use the smallest available resistor value that meets the input resistance requirement.

For large β (≥ 100) the output resistance looking into the emitter of the emitter-follower amplifier R\ :sub:`o` is calculated as

:math:`R_o = r_e + R_S/(1 + β)`

where R\ :sub:`S` is the total equivalent source resistance in the base circuit. In our circuit, R\ :sub:`S` is equal to the parallel combination of the base bias resistors and the source resistance feeding the base. Note that when the emitter-follower amplifier is fed by the low resistance voltage source output of the M1K, R\ :sub:`S` ≈ 0 and the output resistance is simply the incremental emitter resistance r\ :sub:`e`.

:math:`R_o = r_e = 26 mV/25 mA ≈ 1 Ω`

When we place the emitter-follower on the output of the CE amplifier from the "Class A NPN Common-Emitter Amplifier" lab, we have nonzero R\ :sub:`S`, and need to include it in out calculation of R\ :sub:`o`

:math:`\displaystyle R_o = r_e + R_S/(1 + β) = 1 Ω + \frac{470 Ω||2.2 KΩ||2.2 KΩ}{1 + 200} ≈ 1 Ω + 1.6 Ω = 2.6 Ω`

We will see a small voltage divider loss when driving the 47 Ω load, and a more pronounced loss when driving the 10 Ω load. With the emitter-follower amplifier buffering the CE amplifier, we will have voltage divider factors of 47 Ω/49.6 Ω ≈ 0.95 for the 47 Ω load and 10 Ω/12.6 Ω ≈ 0.79 for the 10 Ω load.

We can calculate the efficiency of the emitter-follower amplifier studied in this lab.

For the emitter-follower amplifier by itself driving +/-1 V into the 47 Ω load resistor, the power into the load is:

:math:`P_LOAD = (1/√2)(0.5 V_PEAK)(1/√2)(10.6 mA_PEAK) = 2.65 mW_rms`

Note that the power into the load could also have been calculated using the [v\ :sub:`LOAD`\ (rms)]\ :sup:`2`/R\ :sub:`L` formula.

The quiescent power drawn from the supply is:

:math:`P_SUPPLY = V_CE(Q)I_C(Q) = (5.0 V - 1.7 V)(25 mA) ≈ 82.5 mW`

The efficiency is therefore:

:math:`\eta = 2.65 mW/82.5 mW ≈ 3.2%`

For the emitter-follower amplifier buffering the CE amplifier driving +/-0.5 V into the 47 Ω load resistor, the power into the load is again:

:math:`P_LOAD = 2.65 mW_rms`

The total quiescent power drawn from the supply, using the results already calculated in the CE amplifier lab, is:

:math:`P_SUPPLY = P_SUPPLY(CE Amp) + V_CE(Q)I_C(Q) = 11.7 mW + (5.0 V - 2.1 V)(31 mA) ≈ 102 mW`

The efficiency is therefore:

:math:`\eta = 2.65 mW/102 mW ≈ 2.6%`

If we substitute the 10 Ω load for the 47 Ω load, we lower the output voltage across the load to about +/- 0.15 V, and the power into the load is

:math:`P_LOAD = (1/√2)(0.15 V_PEAK)(1/√2)(12.5 mA_PEAK) = 0.94 mW_rms`

The efficiency is now only

:math:`\eta = 0.94 mW/102 mW ≈ 0.92%`

It is important to note that the voltage divider losses between the emitter-follower output and the load were omitted.

We can calculate the power gain of the two cascaded amplifiers with the 47 Ω load using the results obtained in the "Class A NPN Common-Emitter Amplifier" lab. The voltage gain is essentially the same as it was for the CE amplifier because the voltage gain of the emitter-follower amplifier is very close to unity and the input resistance of the CE is unchanged. The power gain is therefore

:math:`\displaystyle A_P = A_V^2\frac{R_i}{{R_L}} = (-5.1)^2\frac{1.2 KΩ}{{47 Ω}} ≈ 664`

:math:`A_P(dB) = 10log_10(664) ≈ 28 dB`

From this result, we can see how adding the emitter-follower output stage increased the overall power gain by providing current gain to drive the heavier load.

Observations and Conclusions
----------------------------

-  Emitter-follower amplifiers provide significant current gain and unity voltage gain
-  The operation of an emitter-follower amplifier involves a form of negative feedback
-  Emitter-follower amplifiers have high input resistance and low output resistance
-  Emitter-follower amplifiers are often used to buffer heavy loads that require large output currents from sources that have high source resistances
-  Adding an emitter-follower stage to a CE amplifier can significantly increase the power gain of the overall amplifier

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`

.. |lab_11_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_11_image_1.png
   :width: 800px
.. |lab_11_assembly_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_11_assembly_image_1.png
   :width: 1000px
.. |lab_11_image_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_11_image_2.png
   :width: 800px
.. |lab_11_assembly_image_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_11_assembly_image_2.png
   :width: 1000px
