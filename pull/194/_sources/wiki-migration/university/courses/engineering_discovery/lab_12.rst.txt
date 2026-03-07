Class A NPN Common-Base and Cascode Amplifiers
==============================================

.. image:: https://wiki.analog.com/_media/analogTV>5183327709001
   :alt: analogTV>5183327709001
   :align: right

Introduction
------------

Common-emitter and emitter-follower amplifiers are the most widely used single-transistor amplifiers. The common-base configuration, illustrated below in its basic NPN form, is used less frequently as a stand-alone voltage amplifier stage, mostly because it has a low input resistance, but it is often combined with a common-emitter stage to form a *cascode* amplifier. In a common-base voltage amplifier, the input voltage is applied to the emitter and the output voltage is taken from the collector, and the input and output voltages are in-phase. The in-phase relationship can be understood by observing that when the signal voltage applied to the emitter increases, the base-emitter voltage v\ :sub:`BE` decreases, causing the emitter/collector current to decrease, decreasing the voltage drop across the collector resistor, R\ :sub:`C`, thereby increasing the collector voltage. Because of its low input resistance, the common-base amplifier is sometimes used as a current-in/voltage-out amplifier or current buffer. Its operation in the cascode configuration is acting as a current-in/voltage-out amplifier because it takes the collector current from the common-emitter stage as its input and produces an output voltage at its collector.\


|lab_12_image_1.png|

As with all linear Class A BJT amplifiers, the transistor must operate in the forward active region in the common-base amplifier. This means that the base-emitter junction must be forward biased, the collector-base junction must be reverse biased, and operation must be prevented from entering the saturation region. These bias conditions can be seen in the schematic shown in the "Procedure" section for the common-base stage as well as the CE stage in the cascode amplifier. The base is often biased using a resistive voltage divider, voltage regulator, or available power supply, and an emitter resistor, R\ :sub:`E` is used to establish the emitter current. The base should always be bypassed with a capacitor that produces a low impedance AC ground at all signal frequencies. If the amplifier is DC-coupled, the voltage source applied to the base must also provide a low DC resistance. The collector circuit is similar to what is used in the common-emitter amplifier, and in its simplest form consists of a resistor, R\ :sub:`C` connected between the collector and the power supply.

The input of a common-base amplifier looks into the emitter, which is the same as looking into the output resistance of an emitter-follower amplifier. As we saw in the "Class A NPN Emitter-Follower Amplifier" lab, the emitter-follower output resistance is low, which is desirable for a voltage amplifier output, but is not desirable for a voltage amplifier input. With a low-impedance voltage source providing the base bias, the common-base input resistance is simply r\ :sub:`e`, which is equal to the ratio of the thermal voltage V\ :sub:`T` to the collector bias current I\ :sub:`C`, or R\ :sub:`IN` = V\ :sub:`T`/I\ :sub:`C` ≈ 26 mV/I\ :sub:`C` at room temperature. The gain of a common-base amplifier can be calculated using detailed circuit analysis or approximated by inspection as was done with the CE amplifier. Using the same approach as was done with the CE amplifier, the gain of the common-base amplifier with a low-impedance base driving circuit is A\ :sub:`V` = R\ :sub:`C`/r\ :sub:`e`. Besides the low input resistance issue, the gain of the common-base amplifier depends on r\ :sub:`e`, which is small (producing high gain, which may not be desirable), temperature dependent, and nonlinear. When combined with a CE stage to form a cascode amplifier, we will see that the r\ :sub:`e` of the common-base amplifier becomes the effective collector resistance of the CE stage, and is cancelled out of the cascode amplifier gain equation when the emitter resistor is 100% capacitively bypassed. The greatest advantage of the cascode amplifier, however, is that it reduces the *Miller effect*, which causes the bandwidth of a CE stage to decrease as its gain increases. With the r\ :sub:`e` of the common-base stage as the effective collector resistance of the CE stage and the r\ :sub:`e` of the CE stage as the emitter resistance when the emitter bias-setting resistor is fully bypassed, the gain of the CE stage is -r\ :sub:`e,CB`/r\ :sub:`e,CE` ≈ -1 when the two transistors are well-matched. The voltage gain is provided by the collector current flowing through the collector resistor in the common-base stage, and the common-base amplifier bandwidth is not diminished by the Miller effect. The important benefit realized by the cascode configuration is that high gains can be achieved without significant bandwidth loss due to the Miller effect, but it requires two transistors. As with CE amplifiers, an emitter-follower stage is often added on the output of the common-base stage to drive low impedance loads.

In this lab, we will not build a standalone common-base amplifier, but will instead study the use of the common-base amplifier in a cascode amplifier.

Objective
---------

To understand the operating principles of common-base and cascode amplifiers. To design, build, and test a cascode amplifier using two 2N3904 NPN transistor stages, with an input resistance of at least 1 KΩ and a voltage gain of a little less than 10. To understand how to set up the proper bias conditions for a cascode amplifier and verify that the bias voltages in the circuit are close to their designed values. Following completion of this lab you should be able to explain the basic operation of common-base and cascode amplifiers, and be able to calculate the voltage gain for each of these amplifiers.

Materials and Apparatus
-----------------------

-  Data sheet handout for the 2N3904 NPN transistor
-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (2) 2N3904 NPN transistor from the ADALP2000 Analog Parts Kit
-  (1) 47 Ω resistor from the ADALP2000 Analog Parts Kit
-  (2) 100 Ω resistor from the ADALP2000 Analog Parts Kit
-  (2) 470 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 2.2 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 6.8 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 22 μF capacitor from the ADALP2000 Analog Parts Kit
-  (2) 47 μF capacitor from the ADALP2000 Analog Parts Kit
-  (1) 220 μF capacitor from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Construct the following circuit on the solderless breadboard\


|lab_12_image_2.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_12_assembly_image_1.png|

-  Run PixelPulse and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Disable "Repeated Sweep" mode (waveforms can be frozen for evaluation by pressing "pause")
-  Set up the M1K to source voltage/measure current on Channel A and measure voltage on Channel B
-  Set up Channel A source waveform for a 100 Hz “Sine” output that swings between 2.4 V and of 2.6 V
-  Observe the output voltage at the collector of the common-base stage on Channel B and verify that it is swinging about a bias voltage of approximately 3.7 V and that it is out-of-phase with the input signal
-  Measure the approximate peak-to-peak voltage of the output signal and calculate the voltage gain of the cascode amplifier as A\ :sub:`V` = v\ :sub:`o,P-P`/v\ :sub:`i,P-P`
-  Verify that the measured voltage gain of the amplifier is close to the theoretical gain calculation
-  Remove the input signal and measure the bias voltages, and verify that the measured values are close to those indicated in the schematic
-  Note any visible distortions in the output signal
-  Experiment with input signals of various different peak-to-peak levels and observe the effects of these variations on the output signal

Theory
------

The common-base amplifier has a very low input resistance, which is equal to the incremental emitter resistance r\ :sub:`e`. This is the same as the output resistance of the emitter-follower amplifier that has a low equivalent resistance on its base, which makes sense since we are looking into the emitter. One of the most common uses of the common-base stage is as the output stage of a cascode amplifier.

The cascode amplifier is comprised of a common-emitter input stage and a common base output stage. The common-emitter stage provides high input resistance, which is desirable for voltage amplifiers. The common-emitter stage, however, suffers from the Miller effect, which produces a reduction in amplifier bandwidth as the amplifier voltage gain is increased. When the emitter resistor used to bias the common-emitter stage is fully bypassed with a capacitor, its gain is equal to -(collector resistance)/(r\ :sub:`e` of the common-emitter stage). With the common-base stage as the "load" on the common-emitter stage, the collector resistance seen by the common-emitter stage is r\ :sub:`e` of the common-base stage. If the two transistors used in the amplifiers are well-matched, the r\ :sub:`e` of the common-emitter stage will approximately equal r\ :sub:`e` of the common base stage, and the gain of the common-emitter stage will be approximately -1. The common-base amplifier configuration does not suffer from the Miller effect, so it can provide the required voltage gain without any bandwidth penalty. The two amplifiers together, therefore, can provide voltage gain without incurring the bandwidth reduction due to the Miller effect.

The approximate overall gain of the cascode stage can be quickly determined by inspection, using a few simplifications used in the common-emitter lab. The first simplification is to ignore base currents and think of the emitter and collector currents in both transistors all being equal. Referring to the cascode amplifier schematic, we can think of the same current flowing through the path consisting of the collector and emitter of the common-base transistor into the collector and emitter of the common-emitter stage, much in the same way as the current would flow in a series circuit. Using the results from the common-emitter lab, we can see that when the emitter bias resistor is fully bypassed, the AC voltage gain of the cascode amplifier is simply -R\ :sub:`C`/r\ :sub:`e,CE`. In our circuit, part of the emitter bias resistor is bypassed and part is not. THe two 100 Ω resistors are bypassed with the 220 μF capacitor, leaving the 47 Ω resistor unbypassed. The unbypassed portion of the emitter bias resistor R\ :sub:`E,UBP` is in series with r\ :sub:`e,CE`, so the total emitter resistance used for AC signal gain is now r\ :sub:`e,CE` + R\ :sub:`E,UBP`. The general approximate voltage gain for the cascode amplifier can now be expressed as

:math:`A_V = -R_C/(r_{e,CE} + R_{E,UBP})`

In the cascode amplifier studied in this lab, the collector DC bias current I\ :sub:`C` is approximately 2.8 mA, so r\ :sub:`e,CE` can be calculated to be

:math:`r_{e,CE} ≈ 26 mV/2.8 mA ≈ 9 Ω`

We can now calculate the overall voltage gain as

:math:`A_V = -470 Ω/(9 Ω + 47 Ω) ≈ -8.4`

The output voltage is biased up at approximately 3.7 VDC which allows a +/-1 V output signal to swing with minimal distortion.

Observations and Conclusions
----------------------------

-  Common-base amplifiers have low input resistance and are therefore seldom used as voltage amplifiers
-  Common-base amplifiers are sometimes used as standalone current-in/voltage-out and current buffer amplifiers
-  A very common use for a common-base amplifier is as the output stage of a cascode amplifier
-  A cascode amplifier is comprised of a common-emitter input stage and a common-base output stage
-  The Miller effect occurs in common-emitter amplifiers and causes the bandwidth of the amplifier to decrease as the voltage gain of the amplifier increases
-  The load resistance of the common-emitter stage in a cascode amplifier is equal to the low incremental emitter resistance of the common-base stage, and this keeps the magnitude of the voltage gain of the common-emitter stage ≤ 1, minimizing the Miller effect
-  Voltage gain in a cascode amplifier is provided by the common-base output stage, which does not suffer from the Miller effect
-  The output voltage of a cascode amplifier is out-of-phase with its input voltage
-  Voltage gain of the cascode amplifier is similar in form to that of a common-emitter amplifier
-  An emitter-follower stage can be added to a cascode amplifier output in order to drive low impedance loads in much the same way that it is done with common-emitter amplifiers

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`

.. |lab_12_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_12_image_1.png
   :width: 400px
.. |lab_12_image_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_12_image_2.png
   :width: 800px
.. |lab_12_assembly_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_12_assembly_image_1.png
   :width: 1000px
