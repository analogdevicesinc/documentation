Chapter 12: Differential amplifiers
===================================

The differential amplifier is probably the most widely used circuit building block in analog integrated circuits, principally op amps. We had a brief glimpse at one back in Chapter 3 section 3.4.3 when we were discussing input bias current. The differential amplifier can be implemented with BJTs or MOSFETs. A differential amplifier multiplies the voltage difference between two inputs (Vin+ - Vin-) by some constant factor Ad, the differential gain. It may have either one output or a pair of outputs where the signal of interest is the voltage difference between the two outputs. A differential amplifier also tends to reject the part of the input signals that are common to both inputs (Vin+ + Vin-)/2 . This is referred to as the common mode signal.

12.1 Starting with the basics
-----------------------------

It is often easiest to start again with the very basic single transistor and build a workable differential amplifier as a logical progression from there. Consider the single transistor amplifier stage, figure 12.1.1, which is similar to what we explored in the section on the degenerated common emitter back in Chapter 9. This amplifier can actually be viewed as either an inverting common emitter amplifier when driven from V\ :sub:`neg` and with V\ :sub:`pos` considered an AC ground. Or as a non-inverting common base amplifier when driven from V\ :sub:`pos` and with V\ :sub:`neg` considered an AC ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr12_f1.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 12.1.1 AC coupled difference amplifier


Let's assume that we make the coupling capacitors, C\ :sub:`1` and C\ :sub:`2`, sufficiently large so that we can view them as AC shorts for the signal frequencies of interest. The small signal voltage gain from V\ :sub:`neg` to V\ :sub:`out` is:

:math:`A_vn = -g_m R_L`

Likewise, the small signal voltage gain from V\ :sub:`pos` to V\ :sub:`out` is:

:math:`A_vp = g_m R_L`

The transistor amplifies the small signal voltage across its V\ :sub:`be` which in this case is V\ :sub:`pos`-V\ :sub:`neg`. If we apply equal amplitude, in phase signals to V\ :sub:`pos` and V\ :sub:`neg`, such that V\ :sub:`pos`-V\ :sub:`neg` = 0 then there will be no varying signal across V\ :sub:`be` and the output signal at V\ :sub:`out` will be zero. On the other hand, if we apply equal amplitude signals that are 180º out of phase with each other, then V\ :sub:`pos`-V\ :sub:`neg` = twice the amplitude of the inputs. This difference voltage will appear across V\ :sub:`be` and be amplified by g\ :sub:`m`\ \*R\ :sub:`L` at V\ :sub:`out`.

The inverting or negative input terminal of our simple difference amplifier has the relatively high input impedance of the common emitter stage while the non-inverting or positive input terminal of the amplifier has the relatively low input impedance of the common base stage. The importance of this observation and how it can be put to good use will become apparent in the next chapter (13) on transimpedance amplifiers.

It would be advantageous if our differential amplifier had more symmetric inputs where the input impedance for both the positive and negative inputs was as high as possible, ideally infinite. An additional step to get us in that direction is shown in figure 12.1.2. If we now include an emitter follower stage, Q\ :sub:`2`, to buffer the relatively low impedance of the common base amplifier path of the positive input we get a more symmetrical pair of inputs.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr12_f2.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 12.1.2 difference amplifier with emitter follower added.


Because we are still AC coupling our input signals a second set of biasing resistors, R\ :sub:`B3` and R\ :sub:`B4` are necessary to provide DC bias for the new emitter follower. If we instead DC couple the now symmetric inputs the biasing resistors become unnecessary and our difference amplifier now takes on the look of the classic differential pair we will discuss in the next section.

12.2 Long-tailed pair
---------------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr12_f3.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 12.2.1: A long-tailed pair with resistor loads


The classic differential pair amplifier is formed from at least two identical transistors, configured with the emitters for BJT transistors or the sources for FETs connected together. A long-tailed pair (LTP), or emitter coupled (source coupled) pair, is a pair of transistors where the shared emitter or source node is supplied from a more or less constant current source/sink, which could be as simple as a relatively large value resistor connected to the negative supply, such as R\ :sub:`tail` in figure 12.2.1, (or the positive supply for p-type devices) that develops a large voltage drop relative to the amplitude of the input signal thus the "long tail". Given the more or less constant current supplied to the emitters or sources the summation of the two collector or drain currents is also more or less constant with signal.

The two inputs at the bases or gates can be fed with a differential or balanced input signal and the two outputs from the collectors or drains remain balanced, or one input could be grounded to convert a single ended input signal to a differential output.

The higher the resistance of the current source R\ :sub:`tail`, the lower the common mode gain or A\ :sub:`c` is, and the better the common mode rejection ratio (CMRR). In more sophisticated designs, an active constant current source may be substituted for the high resistance R\ :sub:`tail`. With two inputs and two outputs, this forms a differential amplifier stage. The two bases or gates are inputs which are differentially amplified by the pair.

Even though this circuit is designed to have two inputs and two outputs, it is not necessary to use both inputs and both outputs. (Remember, a differential amplifier was defined as having two possible inputs and two possible outputs.) A differential amplifier can be connected as a single-input, single-output device; a single-input, differential-output device; or a differential-input, differential-output device. The output may be single-ended (taken from just one of the collectors or drains, or differential depending on the needs of the subsequent circuitry.

In a long-tailed pair built using BJTs, the emitters are connected together, and then through the current source to ground or to a negative supply (for an LTP using NPN transistors). In this form, one of the transistors can be thought of as an amplifier operating in common emitter configuration, and the other as an emitter follower, feeding the other input signal into the emitter of the first stage as we discussed in the previous section. Since a transistor will amplify the current flowing between base and emitter, it follows that the current flowing in the collector circuit of the first transistor is proportional to the difference between the two inputs. However since the circuit is totally symmetrical, either element can be viewed as an amplifier or as a follower, understanding how the circuit functions does not depend on which role you assign to which device.

The bias condition assumes equal voltages at V\ :sub:`pos` and V\ :sub:`neg`, forcing the bias current I\ :sub:`tail` (set by R\ :sub:`tail`) to split equally between the transistors resulting in I\ :sub:`C1` = I\ :sub:`C2`. With R\ :sub:`C1` = R\ :sub:`C2`, equal voltages develop at V\ :sub:`out`\ + and V\ :sub:`out`-.

Using MOSFETs, we can construct an source-coupled differential pair, which is a counterpart of the emitter-coupled differential pair using BJTs. The main advantage of using MOSFETs for a differential pair compared to BJTs is the nearly infinite input impedance, while the disadvantage is generally lower differential gain.

Assuming the two MOSFETs are the same. The analysis of the source-coupled differential pair proceeds in the same way as the emitter-coupled differential pair for both common-mode signal and differential input signal. The transfer characteristics for drain current I\ :sub:`d1` and I\ :sub:`d2` are shown in the figure.

12.3 Differential Gain
----------------------

We can calculate the differential voltage gain as follows. Consider Q\ :sub:`1` and Q\ :sub:`2` as current sources controlled by their base voltages. R\ :sub:`C1` and R\ :sub:`C2` then convert the currents back into voltages. First, the small signal collector current

:math:`i_C = g_m v_BE`

Where the transconductance g\ :sub:`m` (Amps/Volts) is set by the DC collector current

:math:`g_m = I_c / V_T = I_c / 25 mV` at room temperature.

Then, R\ :sub:`C` converts I\ :sub:`c` back to a voltage.

:math:`v_C = R_C \times g_m v_BE`

Bringing the input V\ :sub:`diff` = V\ :sub:`pos` - V\ :sub:`neg`\ into the picture, notice it divides equally across the two base-emitter junctions, but with opposite polarities. Putting it all together you get a single-ended output at each collector

:math:`v_C1 = R_C1 \times g_m \times (+V_diff / 2)`

:math:`v_C2 = R_C2 \times g_m \times (-V_diff / 2)`

Subtracting the two outputs gets you a differential output of

:math:`v_C1 - v_C2 = R_C \times g_m \times V_diff`

An example to set the bias: R\ :sub:`tail` sets the bias at Ie = (-0.6V - V\ :sub:`DD`) / R\ :sub:`tail` = (-0.6 V - (-15 V)) / 7.2 kΩ = 2 mA which divides equally between Q\ :sub:`1` and Q\ :sub:`2` giving

:math:`I_c1 = I_c2 approx I_e / 2 approx 1mA`

Finally, we easily calculate g\ :sub:`m` = 1 mA / 25 mV = 0.04 A/V. The single-ended gain becomes:

:math:`\displaystyle v_C1 / V_diff = R_C1 \times g_m \times \frac{1}{2} = 1 k \times 0.04 \times \frac{1}{2} = 20 V/V`

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr12_f4.png
   :align: center
   :width: 650px

The output from a differential amplifier is itself often differential. If this is not desired, then only one output can be used, disregarding the other output. Or to avoid sacrificing gain, a differential to single-ended stage can be used following the differential stage. This is often implemented with an active current mirror load instead of the collector/drain resistors.

Long-tailed pairs are frequently used in circuits that implement linear amplifiers with feedback, as in operational amplifiers, and in other circuits that require a differential amplifier.

When used as a switch, the "left" base or gate is used as signal input and the "right" base or gate is grounded; output is taken from the right collector or drain. When the input is zero or negative, the output is close to zero; when the input is positive, the output is most-positive, dynamic operation being the same as the amplifier use described above.

Bias stability and independence from variations in device parameters can be improved by negative feedback introduced via emitter or source degeneration resistors.

The differential pair with a small differential input signal v\ :sub:`i`

|image1| |image2|

Small-Signal Operation

:math:`v_d << V_T`

**Some Formulas**

1. Differential Input Resistance

:math:`R_id = 2 ( ß+1 ) ( r_e + R_Tail )`

2. Differential Voltage gain

:math:`\displaystyle A_d = -\frac{2 \alpha R_c}{2(r_e+R_E)} approx -R_C/(r_e+R_E)`

3. Common mode gain:

:math:`\displaystyle v_C1 = v_C2 = -v_CM \frac{\alpha R_C }{2R+r_e} approx - v_CM \frac{\alpha R_c}{2R}`

:math:`\displaystyle A_CM = - \frac{\alpha R_c}{2R}`

**Increasing the linear differential input range of the diff pair**

Sometimes it is advantageous to add emitter degeneration resistor REF to the circuit, as shown in the figure 12.3.1. The resistors have the disadvantage of reducing the differential voltage gain of the circuit. However, two reasons for this is to increase input impedance and to reduce distortion due to the nonlinearity of the BJTs. The right figure shows the transfer characteristic of the differential amplifier (R\ :sub:`EF`\ =40V\ :sub:`T`/I\ :sub:`EE`).

To improve linearity, we introduce emitter-degeneration resistors, which increase the linear range from a few V\ :sub:`T` to about I\ :sub:`Tail`\ R.

| **ADALM1000 Lab Activity 12,** :doc:`BJT Differential Amplifier </wiki-migration/university/courses/alm1k/alm-lab-12>`
| **ADALM1000 Lab Activity 12m,** :doc:`MOS Differential Amplifier </wiki-migration/university/courses/alm1k/alm-lab-12m>`

| **ADALM2000 Lab Activity 12,** :doc:`BJT Differential Amplifier </wiki-migration/university/courses/electronics/electronics-lab-12>`
| **ADALM2000 Lab Activity 12m,** :doc:`MOS Differential Amplifier </wiki-migration/university/courses/electronics/electronics-lab-12m>`

The current mirror as a load
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following figure shows a variation of the emitter-coupled pair in which the collector resistors are replaced by a current mirror. This circuit is particularly favored in integrated circuits, because matched transistors are much easier to construct than precession matched high value resistors. A simple analysis by assuming large ß so that base currents of Q\ :sub:`3` and Q\ :sub:`4` are neglected, results in the equation as follows:

:math:`i_o = partial I_EE tanh(v_id/(2V_T))`

For

:math:`|i_o| < V_T, i_o`

is approximately proportional to v\ :sub:`id`. Notice furthermore that the common-mode input component does not affect the output current.

Summary
-------

This chapter has presented information on differential amplifiers. The information that follows summarizes the important points of this chapter.

A difference amplifier is any amplifier with an output signal dependent upon the difference between the input signals. A two-input, single-output difference amplifier can be made by combining the common-emitter and common-base configurations in a single transistor.

A difference amplifier can have input signals that are in phase with each other, 180º out of phase with each other, or out of phase by something other than 180º with each other.

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-11>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-13>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr12_e1.png
   :width: 150px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr12_e2.png
   :width: 150px
