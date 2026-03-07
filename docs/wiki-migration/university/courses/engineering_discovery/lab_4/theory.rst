Audio Amplifier with Electret Microphone
========================================

Introduction
------------

Audio amplifiers come in many varieties. Low noise audio preamplifiers amplify the very small signals produced by microphones, tape heads, turntable styli, etc… to “line” levels on the order of several volts, suitable for further processing, while contributing minimal noise and distortion to the signal. Line level audio amplifiers are used to sum, filter, and otherwise process the signals that are output from the preamplifiers. High power audio amplifiers amplify the power of the line level signals, making them suitable to drive low impedance, high power loads such as loudspeakers.

In this experiment we design and build an audio amplifier that takes the small output voltage from an electret microphone and amplifies it such that it can drive a small loudspeaker. An electret microphone is a type of condenser (capacitor) microphone that has an essentially permanent charge on the capacitor plates, eliminating the requirement of external phantom power that is used to bias the capacitor in traditional condenser microphones. Most commercially available electret microphones, however, contain an integrated preamplifier – often an open-drain FET circuit – and therefore require a small amount of low-voltage power.

Simple audio amplifiers can be designed using transistors, with or without negative feedback. Negative feedback, however, provides a very important improvement in distortion performance. In this experiment we design and build an AC-coupled non-inverting operational amplifier with a desired voltage gain of ten, with an inside-the-loop emitter-follower on its output with AC-coupling to the loudspeaker. The op-amp section provides voltage gain, and the emitter-follower functions as a buffer, providing the current required to drive the loudspeaker. Placing the emitter-follower inside the feedback loop improves its overall performance.

A list of reference documents and their associated links is provided at the end.

Amplifier Design
----------------

The amplifier is designed to operate from the single +5 V supply available from the M1K, and therefore requires an op-amp that is specified to operate from a +5 V supply. The OP484 quad op-amp provided in the ADALP2000 Parts Kit has moderate input-referred noise and meets the power supply requirement, making it a good candidate for the op-amp portion of the circuit; the 2N3904 NPN transistor, also contained in the kit, is used for the emitter-follower portion of the circuit. Since only one amplifier is required, the remaining three op-amps in the OP484 are set to unity gain with inputs set to the mid-supply voltage of +2.5 V. Note that the limited number of resistor and capacitor values available in the kit affect the design in ways that may deviate from those that would produce the optimal design.

The electret microphone in the ADALP2000 Parts Kit is similar to the Challenge Electronics CEM-C9745JAD462P2.54R microphone. This microphone includes an open-drain FET preamplifier, and requires a drain resistor, R\ :sub:`D`, with value between 680 Ω and 2.2 KΩ, connected between its output and the +5V supply as shown in Figure 1. The drain resistor is set at 2.2 KΩ in this design, which places the drain voltage at approximately +4.5 V with a +5.0 V supply.

.. image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_4/audio_amplifier_theory_1.png
   :alt: audio_amplifier_theory_1.png
   :align: center
   :width: 250px

.. container:: centeralign

   === Figure 1. Electret Microphone Output Stage ===


The amplifier is operating on a single +5 V supply, therefore the op-amp DC levels are biased to a mid-supply voltage of +2.5 V and input, output, and feedback signals are AC-coupled. AC-coupling of the input signal allows the DC level out of the microphone to differ from the DC level into the amplifier.

The design goal is to drive a nominally 400 mV\ :sub:`P-P` signal into an eight ohm loudspeaker, following AC-coupling referenced to ground, requiring about ±25 mA. The emitter-follower is Class A, and thus requires a quiescent current (Q-point) of at least 25 mA, but for practical circuits with non-ideal transistors it should be biased higher. We will initially set the quiescent current at a minimum of 30 mA, allowing for variations due to component availability. The 2N3904 can handle collector current swings up to about 100 mA, with some moderate distortion; in this case the ideal collector current swing is zero to just under 60 mA (limited due to V\ :sub:`CE`\ (sat)). Since the emitter-follower is contained inside a negative feedback loop, the overall distortion will be reduced in proportion to the available loop gain. Clearly, clipping will occur when the 2N3904 collector current goes to zero. Refer to Figure 2 for a schematic diagram of the overall circuit.

.. image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_4/audio_amplifier_theory_2.png
   :alt: audio_amplifier_theory_2.png
   :align: center
   :width: 900px

.. container:: centeralign

   === Figure 2. Overall Amplifier Schematic Diagram ===


Since the feedback loop is AC-coupled with C\ :sub:`G`, the DC closed-loop gain is unity, which places the 2N3904 emitter bias voltage at the input mid-supply voltage of +2.5 V and the base voltage at +2.5 V + 0.7 V = +3.2 V. The emitter resistor R\ :sub:`E` is calculated as (2.5 V)/(30 mA) = 83.3 Ω. A 68 Ω resistor is available in the kit so this value will be used for R\ :sub:`E`, resulting in a quiescent collector current of approximately 37 mA. Quiescent power dissipation in R\ :sub:`E` is (2.5 V)\ :sup:`2`/68 Ω ≈ 92 mW, and the signal adds a negligible amount of power dissipation, so the 0.25 W resistor from the kit is sufficient to handle the power. The power dissipation in the 2N3904 is approximately (V\ :sub:`CE`)x(I\ :sub:`C`) = (5.0 V – 2.5 V)x(37 mA) ≈ 93 mW, which is well within the 625 mW maximum limit specified for the 2N3904 in the TO-92 package at +25º C.

The input impedance of an emitter-follower can be modeled as a capacitance in parallel with a resistance, which can appear negative. The inductance in the circuitry feeding the emitter-follower, combined with the parallel input capacitance and negative resistance can produce oscillations in the emitter-follower, and a small series resistance, R\ :sub:`B`, is often placed in series with the transistor base to make the overall resistance in the circuit positive. A 47 Ω resistor from the kit is used for R\ :sub:`B`.

We need to consider the capacitive load presented to the op-amp by the base of the 2N3904, since capacitive loading produces an undesired pole in the loop transfer function with the amplifier open-loop output resistance, thereby adding lagging phase shift and decreasing phase margin. Without the capacitive load, the OP484 has approximately 65 degrees of phase margin with a non-inverting gain of ten, indicating a very stable amplifier. The input capacitance of the emitter-follower is approximately the collector-base capacitance, C\ :sub:`μ`, plus the base-emitter capacitance, C\ :sub:`π`, divided by (1 + g\ :sub:`m`\ R\ :sub:`L`) where g\ :sub:`m` is the transistor transconductance and R\ :sub:`L` is the total load resistance on the emitter. The transconductance is equal to the quiescent collector current I\ :sub:`C` divided by the thermal voltage V\ :sub:`T`, which is approximately 26 mV at room temperature. Mathematically, this is

:math:`C_{IN} = C_{μ} + C_{π}/1 + g_{m}R_{L}`

We have the following in our circuit:

-  I\ :sub:`C` = 37 mA
-  C\ :sub:`μ` = 4 pF (from 2N3904 data sheet)
-  C\ :sub:`π` = 8 pF (from 2N3904 data sheet)
-  R\ :sub:`L` = 68 Ω \|\| 8 Ω ≈ 7.2 Ω

We can now calculate the input capacitance of the emitter follower as

:math:`C_{IN} = 4 pF + 8 pF/{1 + {{37 mA}/{26 mV}}){7.2 Ω} approx 4.7 pF`

The OP484 data sheet presents plots of closed-loop output resistance, which is equal to the open-loop output resistance divided by one plus the loop gain, and therefore increases with frequency as the open-loop gain decreases with frequency. A convenient point at f = 200 KHz from the G = +10 (feedback factor = 0.1) plot in Figure 23 of the OP484 data sheet indicates a closed-loop output resistance of approximately 135 Ω. Figure 16 in the OP484 indicates that the open-loop gain is approximately 33 dB (≈ x45) at 200 KHz, making the loop gain approximately 45 x 0.1 = 4.5. The open-loop output resistance is therefore approximately (135 Ω)(1 + 4.5) ≈ 743 Ω. This is a relatively large value, commonly seen in rail-to-rail output op amps that use common-emitter output stages.

For the worst case calculation we can simply add R\ :sub:`B` to the 743 Ω op-amp output resistance to obtain a total series resistance of 790 Ω. The pole formed by the 4.7 pF load capacitance and 790 Ω output resistance is at approximately 43 MHz, well above the 0 dB crossover frequency of about 4 MHz. The lagging phase shift at 4 MHz contributed by this pole is equal to atan[(4 MHz)/(43 MHz)] ≈ 5.3 degrees, thus reducing the phase margin to about 60 degrees. There is also some delay through the emitter-follower, which can be converted to phase at a particular frequency, but this is negligible in this design. The 60 degrees of phase margin has sufficient safety margin to produce a stable amplifier in spite of other small phase shifts introduced by layout parasitics produced by using the solderless breadboard.

We can now select the feedback and gain resistors, R\ :sub:`F` and R\ :sub:`G`, to obtain our desired non-inverting gain of ten. It’s best to use small-valued resistors in low noise designs to minimize output noise due to the resistor thermal noise. Making the resistor values too low in a traditional amplifier, however, places undue load on the amplifier output that can increase harmonic distortion and ultimately exceed the amplifier’s output current rating. The emitter follower on this amplifier’s output increases its output current capability and places a very light load on the op-amp output. The non-inverting gain is equal to 1 + R\ :sub:`F`/R\ :sub:`G`, so for a non-inverting gain of ten we require R\ :sub:`F`/R\ :sub:`G` = 9. There are no values in the kit to obtain this, so we will settle for R\ :sub:`F`/R\ :sub:`G` = 10, producing a non-inverting gain of 11. Reasonable choices from the values available in the kit for R\ :sub:`F` and R\ :sub:`G`, in light of the amplifier noise specifications (the noise gain = 11, so the OP484 input referred noise of 3.9 nV/√Hz appears at the output as about 43 nV/√Hz), are R\ :sub:`F` = 1 KΩ and R\ :sub:`G` = 100 Ω.

For AC-coupled audio amplifiers, the AC-coupling highpass cutoff frequency should be well below 20 Hz. The limiting factor in this respect for this amplifier is the highpass cutoff frequency of the AC-coupling into the speaker. The largest capacitor in the kit is 220 μF, which produces a highpass cutoff frequency of about 90 Hz into an 8 Ω speaker. In view of this limit, the remaining highpass cutoff frequencies are selected to be below 90 Hz.

AC-coupling capacitor C\ :sub:`M` is used to isolate the microphone’s +4.5 V output bias levels from the desired op-amp input bias level of +2.5 V. Bias resistors R\ :sub:`B1` and R\ :sub:`B2` are equal in value and develop the op-amp input bias from the +5 V supply. Making these resistors 20 KΩ places a 10 KΩ load on the microphone preamplifier’s 2.2 KΩ output resistance, resulting in a voltage divider loss factor of approximately 0.82. The kit contains a 4.7 μF electrolytic capacitor, which produces a highpass cutoff frequency of about 2.8 Hz in the microphone circuit comprised of a 2.2 KΩ source resistance and 10 KΩ load resistance. Note that the positive capacitor terminal is connected to the microphone, which has the higher bias voltage.

The AC-coupling capacitor used in the feedback loop, C\ :sub:`G`, blocks DC current flow and produces unity DC closed-loop gain. As frequency increases the closed-loop gain moves from unity up to 1 + R\ :sub:`F`/R\ :sub:`G`. The zero frequency, where the gain begins to increase, is at 1/2π(R\ :sub:`F` + R\ :sub:`G`)C\ :sub:`G` and the pole frequency, where the gain levels off to 1 + R\ :sub:`F`/R\ :sub:`G` is at 1/2πR\ :sub:`G`\ C\ :sub:`G`. The 47 μF electrolytic capacitor in the kit, when coupled with the gain resistor value of 100 Ω, produces a pole frequency of approximately 34 Hz. This can be considered to be the highpass cutoff frequency of the feedback loop.

The power supply bypass capacitor, C\ :sub:`BP`, provides a low power supply impedance at audio frequencies, and is selected to be 47 μF.

We’re now ready to complete the final amplifier schematic drawing, shown in Figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_4/audio_amplifier_theory_3.png
   :alt: audio_amplifier_theory_3.png
   :align: center
   :width: 900px

.. container:: centeralign

   === Figure 3. Final Amplifier Schematic Drawing ===


The amplifier produces up to approximately 400 mV\ :sub:`P-P` into the speaker for reasonable acoustic input levels. The gain is easily changed to accommodate other acoustic input levels by changing the R\ :sub:`F`/R\ :sub:`G` ratio.

Online References
-----------------

OP484 Data Sheet

http://www.analog.com/en/products/amplifiers/operational-amplifiers/high-voltage-amplifiers-greaterthanequalto-12v/op484.html

2N3904 Data Sheet

http://www.nxp.com/documents/data_sheet/2N3904_4.pdf

CEM-C9745JAD462P2.54R Electret Microphone Data Sheet

http://www.challengeelectronics.com/microphones/omni_directional/
