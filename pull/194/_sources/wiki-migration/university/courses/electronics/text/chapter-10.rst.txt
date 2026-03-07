Chapter 10: Multi stage amplifier configurations
================================================

For most systems a single transistor amplifier does not provide sufficient gain or bandwidth or will not have the correct input or output impedance matching. The solution is to combine multiple stages of amplification. We have the three basic one transistor amplifier configurations to use as building blocks to create more complex amplifier systems which can provide better optimized specifications and performance. The sections in this chapter tend to use BJT devices to illustrate the circuit concepts but these multi-stage amplifiers can be constructed from MOS FET devices, or a combination, just as easily and the methods used to analyze them are much the same as well.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.1 Two stage cascade amplifier


It is necessary to consider what happens when non-ideal amplifiers are put in series. Looking at the example in figure 10.1, it is clear that the input and output resistances (or impedances) come into play by reducing the overall gain. If the amplifiers were ideal (R\ :sub:`out` = 0 and R\ :sub:`in` = ∞), and amplifier stages #1 and #2 had gains of A\ :sub:`1` and A\ :sub:`2`, the overall gain would simply be A\ :sub:`1`\ \*A\ :sub:`2`. For the above example, let us now calculate the gain assuming nothing about the R\ :sub:`in` and R\ :sub:`out` of each stage, treating them as voltage dividers between the two stages and between the last stage and the output load. Note that in practice, impedances, Z\ :sub:`in`, Z\ :sub:`out`, would normally be used, not resistances, but the simple resistance will serve to illustrate the point here.

.. container:: indent

   First amplification stage with loss between stage #1 and #2:


:math:`V_in2=A_1 V_in1 (R_in2/(R_in2+R_out1 ))`

.. container:: indent

   Second amplification stage with loss due to R\ :sub:`out2` and R\ :sub:`L`:


:math:`V_out=A_2 V_in2 (R_L/(R_L+R_out2 ))`

.. container:: indent

   Overall gain equation:


:math:`V_out/V_in =?A_1 A?_2 (R_in2/(R_in2+R_out1 ))(R_L/(R_L+R_out2 ))`

As we would expect, the overall equation reduces to the ideal case of A\ :sub:`V` = A\ :sub:`1`\ \*A\ :sub:`2` for two ideal stages when we let the R\ :sub:`out` go to 0 and the R\ :sub:`in` go to infinity. As a matter of fact, we really only need R\ :sub:`out` to go to 0 to have the resistor dividers to go to 1. The above equations assume that the individual amplifier gains, A do not change with output loading. That effect, if any, is modeled in the R\ :sub:`out`.

For most integrated circuit amplifiers where R\ :sub:`in` is in the MΩ to GΩ range, and R\ :sub:`out` is in the 50 to 100 Ω range, the gains are pretty close to being the simple product of the gain stages. To confirm this assertion, assume a low performance op amp with R\ :sub:`out` = 100Ω and R\ :sub:`in` = 1MΩ, what is the gain with two stages of gain A\ :sub:`1` and A\ :sub:`2` in series? (assume R\ :sub:`L` = 1 MΩ)

:math:`V_out/V_in = A_1 A_2 (1MΩ/(1MΩ+100Ω))(1MΩ/(1MΩ+100Ω))=A_1 A_2 (0.9999)(0.9999) = 0.9998A_1 A_2`

The answer is pretty close to A\ :sub:`1`\ \*A\ :sub:`2`. In fact, you would have to go to a cascade of 100 stages with these specifications before you even lost 1% of the expected ideal gain (i.e. to get 0.99 A\ :sup:`100`). By the time you reached that point, other adverse effects would have caused much more trouble, for example, the fact that noise from each successive stage is added to the noise coming into that stage and is further amplified on down the cascade of amplifiers.

There are practical reasons why you just can't continue cascading stages "forever..." If DC-coupled, real-world offsets can be impossible to trim out. Even if AC-coupled, noise from preceding stages gets amplified by each downstream amplifier stage, making for nothing but a noise source after a while. We generally refer all noise to the input of the signal chain, taking out the effects of the gain stages.

10.1 Cascade of two single transistor stages
--------------------------------------------

The impact of input and output loading can be minimized by cascading two amplifiers with appropriate input and output characteristics. Multistage cascading can be used to create amplifiers with high input resistance, low output resistance and large gains.

10.1.1 Common Emitter / Common Collector cascade
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The cascade of a Common Emitter amplifier stage followed by a Common Collector (emitter-follower) amplifier stage can provide a good overall voltage amplifier, figure 10.1.1. The Common Emitter input resistance is relatively high and Common Collector output resistance is relatively low. The voltage follower second stage, Q\ :sub:`2`, contributes no increase in voltage gain but provides a near voltage-source (low resistance) output so that the gain is nearly independent of load resistance. The high input resistance of the Common Emitter stage, Q\ :sub:`1`, makes the input voltage nearly independent of input-source resistance. Multiple Common Emitter stages can be cascaded with emitter follower stages inserted between them to reduce the attenuation due to inter-stage loading.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.1.1 Common Emitter, Common Collector


Calculating the DC biasing conditions and the required resistance values for each stage in the cascade is preformed just as we have done in the previous chapter on single stage amplifiers. The effect of inter-stage loading must then be take into account as we just discussed in the opening section of this chapter.

10.1.2 DC coupled Common Emitter stages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another multi-stage amplifier to explore is to simply cascade two common emitter stages. Figure 10.1.2 shows two n-type common emitter stages in cascade.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.1.2 DC coupled Common Emitter stages


The complication in calculating the gain of cascaded stages comes from the non-ideal coupling between stages due to loading. Two cascaded common emitter stages are shown in figure 10.1.2. Because the input resistance of the second stage (resistors R\ :sub:`3` and R\ :sub:`4`) forms a voltage divider with the output resistance (R\ :sub:`C1`) of the first stage, the total gain is not simply the product of the gain for the individual (separated) stages.

The total voltage gain can be calculated in either of two ways. First way: the gain of the first stage is calculated including the loading of the R\ :sub:`3`,R\ :sub:`4` resistor divider. Then the second-stage gain is calculated from the collector of Q\ :sub:`1` which is the output of the first stage. Because the loading (R\ :sub:`3`,R\ :sub:`4` output divider) was accounted for in the first-stage gain, the second-stage gain input quantity is the Q\ :sub:`2` base voltage, v\ :sub:`B2` = v\ :sub:`o1`.

Second way: the first-stage gain is found by disconnecting the input of the second stage, thereby eliminating output loading. Then the Thevenin equivalent output of the first stage is connected to the input of the second stage and its gain is calculated, including the input divider formed by the first-stage output resistance and second-stage input resistance. In this case, the first-stage gain output quantity is the Thevenin equivalent voltage, not the actual collector voltage of the amplifier with the second stage connected. The second way includes inter-stage loading as an input divider in the gain of the second stage while the first way includes it as an output divider in the gain of the first stage.

In DC coupled multistage cascaded common emitter amplifiers the output bias level of each stage increases to maintain the collector more positive than the base (constant current operation). If this voltage "stacking" is severe, little head room is left in the final stages of the cascade. The R\ :sub:`3`, R\ :sub:`4`\ resistor divider in figure 10.1.2 not only reduces the signal amplitude seen at the base of Q\ :sub:`2`, it also reduces the DC bias level from the collector of Q\ :sub:`1` to a more manageable DC level at the base of Q\ :sub:`2`. This happens at the cost of overall signal gain in the combined amplifier.

10.1.3 AC coupled Common Emitter stages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to create a multistage cascade where each stage is separately biased and coupled to adjacent stages via DC blocking capacitors. Inserting coupling capacitors between stages blocks the DC operating bias level of one stage from affecting the DC operating point of the next. This solves many of the limitations we saw in section 10.1.2. However, the resulting overall amplifier can no longer respond to DC, or very low frequency, inputs.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.1.3 AC coupled Common Emitter stages


The infinity symbol next to coupling capacitors C\ :sub:`1` C\ :sub:`2` and C\ :sub:`3` is used to indicate that the unspecified capacitance is large enough at the specified signal frequency to have a negligible reactance and can be treated as an AC short-circuit. It is also useful to note at this point that the method of including capacitors across the emitter degeneration resistors R\ :sub:`E1` and R\ :sub:`E2` to increase the gain at higher frequencies can be employed in the case of these multistage amplifiers as well as the single stage amplifiers discussed in Chapter 9.

10.1.4 Complementary Pair Amplifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not only can NPN transistors or n-type MOS devices be combined in multiple stages, so can the complementary PNP and p-type MOS devices. Having both polarities of transistors allows for more flexibility in how amplifier sages can be combined and can make biasing easier as well.

For example, a complementary cascade amplifier is shown in figure 10.1.4. The second common emitter stage uses a PNP transistor. The gain calculation procedure is the same as the all-NPN cascade. The advantage of the complementary cascade amplifier is that the p-stage collector DC operating point tends to cancel the bias level "stacking" issue we encountered in the all n-type common emitter amplifier cascade we explored in section 10.1.2.

By using complementary devices, active level shifting can be combined with amplification.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.1.4 complementary cascade amplifier


A two-stage 'Complementary Pair' BJT amplifier circuit diagram is shown in figure 10.1.4. The rationale behind a complementary pair cascade is a problem that can arise with a cascade of similar n-type stages. To avoid saturation the collector voltage of each stage must be greater than the base voltage, enough greater to allow for the collector voltage signal swing. However since the base voltage of the second stage is taken from the collector of the first stage it is inherently larger that the first stage base voltage, and the second stage collector voltage is still higher. But this decreases the available amplitude for the amplified signal. Adding a third stage would even further aggravate this situation.

If a PNP second stage is used a base voltage close to the positive power supply accommodates a desirable higher first stage NPN collector voltage. Moreover a third NPN stage can be cascaded at the PNP stage output without the severe voltage offset problem of a cascade of similar stages.

Estimating the DC bias voltages and currents is simplified considerably under the assumption that the PNP base current is small compared to the NPN collector current. Of course this is not necessarily so but there are two reasons generally favoring such a relationship. Considering the common DC power supply and the bias configuration one might expect intuitively that the two transistors will have roughly comparable collector currents, and a typical PNP ß of about 120 would then support the approximation. A sort of circular reasoning based on an enlightened self-interest suggests that a simplifying approximation relatively easy to implement in fact will be implemented so as actually to simplify the circuit design process. In any event the assumption can be made and subsequently justified explicitly by verifying the consistency of the assumption with values calculated using it. And of course adjustments can be made if and where needed in an iterative process.

The approximation we are recommending here makes the bias calculations for each stage effectively independent of one another. The estimate so made can be refined by a second iteration in which rather than neglecting the PNP base current the value of this current estimated from the first iteration is used. This refinement is rarely if ever necessary. The use of modern circuit simulation software can of course speed up this iteration process.

10.2 Design Example
-------------------

Design a Complementary Pair amplifier stage using 2N3904 and 2N3906 transistor's (β ˜ 120, V\ :sub:`BE` ˜ 0.7v). Use a supply voltage of 10 volts, and a source resistance of 15 KΩ. Estimate the DC bias voltages and currents, and compare these with the results of a computer simulation. Determine the small signal gain for a nominal 1 KHz signal.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.2.1 Complementary Pair amplifier stage


The partitioning of the stages for the bias calculation suggests the circuit shown in figure 10.2.1 performs as a cascade of two common emitter stages, each with emitter degeneration. Consider the resistors R\ :sub:`E1` and R\ :sub:`E2` that appear in the emitter paths of the small signal parameter circuit. Because of the transistor current amplification this resistance transformed into the transistor base is larger by a factor of ß+1, and this typically is generally significantly larger than r\ :sub:`e`\ with which it is in series. Hence, roughly, an AC voltage v\ :sub:`b` at the base of the NPN device (for example) appears almost entirely across the emitter resistor. The small signal emitter current is essentially equal to the small signal collector current, and the approximate voltage gain for the first stage is -R\ :sub:`C1`/R\ :sub:`E1`. (Note the 180° phase shift) Similarly an estimate for the PNP stage voltage gain is -R\ :sub:`C2`/R\ :sub:`E2`. For the two stage cascade the gain estimate then is the product of these two gains. Note however there is also an input transfer loss of R\ :sub:`B`/(R\ :sub:`B` + 15kΩ). Where R\ :sub:`B` can be approximated by the parallel combination of bias resistors R\ :sub:`1` and R\ :sub:`2`

The first step is to estimate the DC bias currents and voltages for the design using the simplified large signal BJT models.

Next we use the simplified small signal parameter transistor model to estimate the AC voltage gain. Compare this estimate against the approximate calculation described above, as well as the computed gain.

In this respect consider further the implication that each stage gain depends largely on the ratio of the collector resistance to the (un bypassed) emitter resistance.

.. warning::

   This section may be incomplete due to lack of interest.


10.3 The Cascode
----------------

The cascode is a two-stage amplifier composed of a single transconductance amplifier (usually a common source/emitter stage) followed by a current follower (usually a common gate/base stage ). Compared to a single amplifier stage, this combination may have one or more of the following advantages: higher input-output isolation, higher input impedance, higher output impedance, higher gain or higher bandwidth. In modern circuits, the cascode is often constructed from two transistors (BJTs or FETs), with one operating as a common emitter/source and the other as a common base/gate. The cascode improves input-output isolation (or reverse transmission) as there is less direct coupling from the output to input. This greatly reduces the Miller multiplication of stray coupling capacitance between input and output and thus contributes to a much higher bandwidth.

Figure 10.3.1 shows the basic form of the cascode amplifier with a common emitter/source amplifier as input stage, Q\ :sub:`1` or M\ :sub:`1`, driven by signal source V\ :sub:`in`. This input stage then drives a common base/gate amplifier, Q\ :sub:`2` or M\ :sub:`2`, as the output stage, with an output signal at V\ :sub:`out`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.3.1 The Cascode Amplifier


The advantage of the cascode configuration stems from the placement of an upper transistor as the load of the input transistor's output terminal (collector / drain). This upper transistor is referred to as the cascode device. Because at high frequencies the cascode transistor's base/gate is effectively grounded by DC voltage source V\ :sub:`Bias`, the cascode device's emitter / source voltage (and therefore the lower input transistor's collector / drain) is held at a more constant voltage during operation. In other words, the cascode device exhibits a low input resistance to the lower transistor, making the voltage gain seen at the collector / drain of the lower device very small, which dramatically reduces the Miller feedback capacitance from the lower transistor's collector to base or drain to gate. This loss of voltage gain is recovered by the cascode transistor. Thus, the cascode transistor permits the lower common emitter / source stage to operate with minimum negative (Miller) feedback, improving the bandwidth of the overall amplifier.

The base or gate of the cascode device is electrically AC grounded, so charge and discharge of stray capacitance C\ :sub:`cb` or C\ :sub:`dg` between collector and base or drain and gate is simply through R\ :sub:`L` the output load, and the frequency response is affected only for frequencies above the associated RC time constant: In the case of a FET device t = C\ :sub:`dg` R\ :sub:`D`\ \||R\ :sub:`out`, namely f = 1/(2pt), a rather high frequency because C\ :sub:`dg` is small. That is, the upper FET gate does not suffer from Miller multiplication of C\ :sub:`dg`.

If the cascode device stage were operated alone using its emitter or source as input node (i.e. common base/gate configuration), it would have good voltage gain and wide bandwidth. However, its low input impedance would limit its usefulness to very low impedance voltage drivers. Adding the lower common emitter/source stage results in an increased input impedance, allowing the cascode stage to be driven by a higher impedance source.

If one were to replace the upper device with a typical resistive load, and take the output from the input transistor's collector or drain the common emitter/source configuration would offer the same input impedance as the cascode configuration, but the cascode configuration would offer a potentially greater gain and much greater bandwidth.

As shown, the cascode circuit using two stacked FET's imposes some restrictions on the two FET's-namely, the upper FET must be biased so its source voltage is high enough (the lower FET drain voltage may swing too low, causing it to leave saturation). Insurance of this condition for FET's requires careful selection for the pair, or special biasing of the upper FET gate, increasing cost.

The cascode circuit can be built using the same type transistors, or even mixed with one FET and one BJT. In the latter case, the BJT must be the upper transistor; otherwise, the (lower) BJT will always saturate (unless extraordinary steps are taken to bias it).

10.3.2 Cascode biasing techniques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f10.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.3.2 cascode biasing techniques


Let us suppose that I need to build an amplifier that operates from a 100 volt power supply, however the transistors that I have available have a collector to emitter breakdown voltage (BV\ :sub:`CEO`) of only 25 volts. A cascode or as series of cascodes may also be combined with a voltage ladder to form a high voltage transistor. The input transistor may be any low-BV\ :sub:`CEO` type, while the others, acting as stacked linear series voltage regulators, must be able to withstand a sizeable fraction of the supply voltage. The amplifier shown in figure 10.3.3.

Note that, for a large output voltage swing, their base voltages should not be bypassed to ground by capacitors, and the uppermost ladder resistor should be able to withstand the full supply voltage.

10.3.4 The Folded Cascode
~~~~~~~~~~~~~~~~~~~~~~~~~

Rather than stacking the transistors one on top of the other, which can reduce or limit the available signal swing, it is often advantageous to "fold" the cascode device as shown in figure 10.3.5.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f11.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.3.5 Simple folded cascode amplifier


10.3.5 The Folded Cascode biasing techniques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.3.6


10.3.6 The Shunt Feedback Cascode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Additionally, a variation on the cascode amplifier combines it with the shunt-feedback. The basic shunt feedback circuit is shown in figure 10.3.7 (a), and with BJT T model (b).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f13.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10.3.7 The shunt feedback common emitter amplifier


It is a transresistance (current in, voltage out) amplifier, with a transresistance of:

:math:`v_o/i_in =-\alpha R_F + r_e, R_L ⇒ infty`

if R\ :sub:`L` approaches being a current source (is large relative to R\ :sub:`F` ). For R\ :sub:`F` >> r\ :sub:`e` and α ≈ 1, the transresistance is approximately R\ :sub:`F`. The shunt feedback amplifier can be used for high-speed applications. When combined with the cascode, the resulting amplifier - the shunt feedback cascode - is shown in figure 10.3.8 (a) with the small-signal model in (b).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr10_f14.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10.3.8 The shunt feedback cascode


R\ :sub:`1` in series with R\ :sub:`2` is basically R\ :sub:`F`. Because the current through R\ :sub:`2` loses both base currents before being returned to the input node, both a\ :sub:`Q1` and a\ :sub:`Q2` appear in the second gain term. Unlike the simple shunt feedback stage, C\ :sub:`bc` of either BJT does not shunt R\ :sub:`F`, and is divided between transistors. The voltage at the base of Q\ :sub:`2` varies, as the midpoint of an R\ :sub:`1`, R\ :sub:`2` voltage divider, and Q\ :sub:`2` is not a purely common base configuration. The two feedback resistor values can be chosen to adjust the extent of the Miller effect across the base collector junctions of the transistors.

If speed is not the most important design parameter, but voltage is, then this amplifier provides the advantage of dividing the collector voltage across two series BJTs. If R\ :sub:`1` = R\ :sub:`2`, then each BJT need have only about half the breakdown voltage of a single-BJT amplifier. Again, the cascode presents an advantage for high-voltage applications.

Yet another shunt feedback cascode variation uses a single feedback resistor, as shown in figure 10.3.8 (a), along with a flow graph (for feedback analysis) of the dynamic model of the circuit (b). (Z\ :sub:`F` is R\ :sub:`F` in parallel with C\ :sub:`F` and Z\ :sub:`L` is R\ :sub:`L` in parallel with C\ :sub:`L`.) C\ :sub:`F` is added to provide an additional parameter for adjusting the dynamic amplifier response. The transistor gain bandwidth time constant, ?\ :sub:`T`, is related to f\ :sub:`T` by:

For Rf Cf >> τ\ :sub:`T1`, τ\ :sub:`T2`, then the poles of the amplifier response follow a circular s-plane locus as t\ :sub:`T2` is varied. As Q\ :sub:`2` is made a slower transistor, the closed-loop poles converge, then split off the real axis and follow a circular path to the origin. Variation of τ\ :sub:`T1`, Cf or C\ :sub:`L` follows a vertical locus. As any one of them increases in value, the poles move vertically toward the real axis, then split along the axis, heading for the origin and negative infinity.

The dynamic input impedance of this amplifier is interesting. For infinite Rf and ß\ :sub:`Q1`, the input resistance should appear to be infinite but it is not. The static input resistance is infinite, but not the dynamic resistance. This unusual phenomenon will be the subject of a future article. (Hint: apply a 1-V step to the input and trace through the effects. As the collector node responds to the input step (but not as a step, because of capacitance), then what is the current through Cf? If it is constant, then what impedance does a constant current due to a constant input voltage appear as at the input node?)

10.3.7 Cascode Review
~~~~~~~~~~~~~~~~~~~~~

The cascode amplifier, with its variations, is a key element in the circuit designer's tool kit of useful circuits. It has advantages for increasing bandwidth and for high-voltage amplifier applications.

-  A cascode amplifier consists of a common emitter stage loaded by the emitter of a common base stage.
-  The heavily loaded common emitter stage has a low gain of 1, overcoming the Miller effect
-  A cascode amplifier has a high gain, moderately high input impedance, a high output impedance, and a high bandwidth.

**Additional notes on Level Shifting in multi-stage amplifiers**

In multi-stage amplifiers on integrated circuits, coupling capacitors between stages are almost always not used because they cannot be made large enough for reasonable low-frequency operation. Thus, stages are DC-coupled. This means that voltage offsets like V\ :sub:`BE` drops between stages can start to add up... stages referred to as level shifters can be used to compensate where necessary. Emitter or source followers provide a DC level shift of V\ :sub:`BE` or V\ :sub:`GS` and can be inserted between stages with signal loss as their gain is very close to +1. By using PNP and NPN or PMOS and NMOS transistors, the direction of the level shift per shifter can be either up or down in voltage. Another typical level shifter might be simply a degenerated common emitter amplifier (it can provide gain or simply act as an inverting buffer if R\ :sub:`E` = R\ :sub:`C`). The choice of R\ :sub:`C` "programs" the quiescent collector voltage of the level shifter and can thus be used to "center" the output voltage of an op amp so that it can swing both positive and negative from its quiescent point.

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-9>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-11>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`
