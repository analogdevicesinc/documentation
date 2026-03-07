Chapter 3: Introduction and Chapter Objectives
==============================================

**After completing this chapter you should be able to:**

-   Define: open loop gain, closed loop gain, noise gain
-   Define Gain-Bandwidth Product
-   Define Phase Margin
-   Use Bode Plots
-   Define and measure: Input Offset voltage, Input Bias current, Input Offset current
-   Understand methods to adjust, trim and/or cancel these errors.

3.1 Departures from Ideal
-------------------------

It is not surprising that simplified models are not exact. On the other hand, they generally describe most, if not all, observed op amp behavior. The following are some ways actual Op Amps differ from ideal performance.

-   Finite open loop gain. It is impossible in an actual opamp for the open loop gain to be truly infinite. Most general purpose op amps have a gain of greater than 100,000 which is close enough to infinite for most calculations. Some simple amplifiers and many high bandwidth amplifies can have much smaller open loop gains which must be accounted for when designing with these amplifiers.
-   Offset voltage, VOS. The input stage of the op amp consists of a differential pair of transistors. If the two transistors are not perfectly matched, this mismatch will show up as a non-zero DC offset at the output. In some cases this can be adjusted to zero externally. This offset adjustment amounts to changing the ratio of the currents flowing in the two input transistors.
-   Bias current, Ibias. The transistor inputs actually do draw some current. Those which use bipolar input transistors (like the uA741) draw more current than those which use FETs (like the 411). The bias current is defined to be the average of the currents of the two inputs.
-   Offset current, IOS. This is the difference between the input bias currents. Each bias current, after passing through an input resistive network, will effectively offer a voltage to the op-amp input. Therefore, an offset of the two currents will show up as a voltage offset at the output.

3.2 The Non-Ideal Op Amp- Static Errors Due to Finite Amplifier Gain
--------------------------------------------------------------------

One of the most distinguishing features of op amps is their staggering magnitude of DC voltage gain. Even the least expensive devices have typical voltage gains of 100,000 (100dB), while the highest performance precision bipolar and chopper stabilized amplifiers can have gains as high 10,000,000 (140dB), or more. Negative feedback applied around this much voltage gain readily accomplishes the virtues of closed-loop performance, making the circuit dependent only on the feedback components.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.1: Non-ideal op amp stage for gain error analysis


As noted in the discussion of ideal op amp attributes in Chapter 2, the behavioral assumptions follow from the fact that negative feedback, coupled with high open-loop gain, constrains the amplifier input error voltage (and consequently the error current) to infinitesimal values. The higher this gain, the more valid these assumptions become.

But in reality, op amps do have finite gain, and errors exist in practical circuits. The op amp gain stage of figure 3.1 will be used to illustrate how these errors impact performance. In this circuit the op amp is ideal except for the finite open-loop DC voltage gain, A, which is usually stated as A\ :sub:`VOL`.

3.2.1 Noise Gain (NG)
~~~~~~~~~~~~~~~~~~~~~

The first aid to analyzing op amps circuits is to differentiate between noise gain and signal gain. We have already discussed the differences between non-inverting and inverting stages as to their signal gains, which are summarized in equations 3.1 and 3.2, respectively. But, as can be noticed from figure 3.1, the difference between an inverting and non-inverting stage can be as simple as just where the reference ground is placed. For a ground at point G1, the stage is an inverter; conversely, if the ground is placed at point G2 (with no G1) the stage is non-inverting.

| |image1|
| 3.1 |image2|
| 3.2

Note however that in terms of the feedback path, there are no real differences. To make things more general, the resistive feedback components previously shown are replaced here with the more general symbols Z\ :sub:`F` and Z\ :sub:`G`, otherwise they function as before. The feedback attenuation, β, is the same for both the inverting and non-inverting stages:

|image3| 3.3

Noise gain can now be simply defined as: The inverse of the net feedback attenuation from the amplifier output to the feedback input. In other words, the inverse of the β network transfer function. This can ultimately be extended to include frequency dependence (covered later in this chapter). Noise gain can be abbreviated as NG.

As noted, the inverse of ß is the ideal non-inverting op amp stage gain. Including the β effects of finite op amp gain, a modified gain expression for the non-inverting stage is:

|image4| 3.4

Where G\ :sub:`CL` is the finite-gain stage's closed-loop gain and A\ :sub:`VOL` is the op amp open-loop voltage gain for loaded conditions.

It is important to note that this expression is identical to the ideal gain expression of equation 3.2, with the addition of the bracketed multiplier on the right side. Note also that this right-most term becomes closer and closer to unity, as A\ :sub:`VOL` approaches infinity. Accordingly, it is referred to in some textbooks as the error multiplier term, when the expression is shown in this form.

It may seem logical here to develop another finite gain error expression for an inverting amplifier, but in actuality there is no need. Both inverting and non-inverting gain stages have a common feedback basis, which is the noise gain. So equation 3.4 will suffice for gain error analysis for both inverting and non-inverting stages. Simply use the β factor as it applies to the specific case.

It is useful to note some assumptions associated with the rightmost error multiplier term of equation 3.4. For A\ :sub:`VOL`\ β >> 1, one assumption is:

|image5| 3.5

This in turn leads to an estimation of the percentage error, β, due to finite gain A\ :sub:`VOL`:

|image6| 3.6

Again this error goes to zero as A\ :sub:`VOL` goes to infinity.

3.2.2 Gain Stability
~~~~~~~~~~~~~~~~~~~~

The closed-loop gain error predicted by these equations is not in itself tremendously important, since the ratio Z\ :sub:`F`/Z\ :sub:`G` could always be adjusted to compensate for this error. But note however that closed-loop gain stability is a very important consideration in most applications. Closed-loop gain instability is produced primarily by variations in open-loop gain due to changes in supply voltage, temperature, loading, etc.

|image7| 3.7

From equation 3.7, any variation in open-loop gain (βA\ :sub:`VOL`) is reduced by the factor A\ :sub:`VOL` β, insofar as the effect on closed-loop gain. This improvement in closed-loop gain stability is one of the important benefits of negative feedback.

3.2.3 Loop gain
~~~~~~~~~~~~~~~

The product A\ :sub:`VOL` β which appears in the above equations, is called loop gain, a well known term in feedback theory. The improvement in closed-loop performance due to negative feedback is, in nearly every case, proportional to loop gain.

The term "loop gain" comes from the method of measurement. This is done by breaking the closed feedback loop at the op amp output, and measuring the total gain around the loop. In figure 3.1 for example, this could be done between the amplifier output and the feedback path (see arrows). Approximately, closed-loop output impedance, linearity, and gain stability in errors reduce by the factor, A\ :sub:`VOL`\ β with the use of negative feedback.

Another useful approximation is developed as follows. A rearrangement of equation 3-4 is:

|image8| 3.8

So, for high values of A\ :sub:`VOL`\ β,

|image9| 3.9

Consequently, in a given feedback circuit the loop gain, A\ :sub:`VOL`\ β, is approximately the numeric ratio (or difference, in dB) of the amplifier open-loop gain to the circuit closed-loop gain.

This loop gain discussion emphasizes that indeed, loop gain is a very significant factor in predicting the performance of closed-loop operational amplifier circuits. The open-loop gain required to obtain an adequate amount of loop gain will, of course, depend on the desired closed-loop gain.

For example, using equation 3-9, an amplifier with A\ :sub:`VOL` = 20,000 will have an A\ :sub:`VOL`\ β ~ 2000 for a closed-loop gain of 10, but the loop gain will be only 20 for a closed-loop gain of 1000. The first situation implies an amplifier-related gain error the order of ~ 0.05%, while the second would result in about 5% of error. Obviously, the higher the required gain, the greater will be the required open-loop gain to support an A\ :sub:`VOL`\ β for a given accuracy.

**ADALM1000 Lab Activity** :doc:`Open Loop Gain </wiki-migration/university/courses/alm1k/alm-lab-olg>`

3.2.4 Frequency Dependence of Loop Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Thus far, it has been assumed that amplifier open-loop gain is independent of frequency. Unfortunately, this isn't the case at all. Leaving the discussion of the effect of open-loop response on bandwidth and dynamic errors until later, let us now investigate the general effect of frequency response on loop gain and static errors.

The open-loop frequency response for a typical operational amplifier with superimposed closed-loop amplifier response for a gain of 100 (40dB), illustrates graphically these results, in figure 3.2. In these Bode plots, subtraction on a logarithmic scale is equivalent to normal division of numeric data. Today, op amp open-loop gain and loop gain parameters are typically given in dB terms, thus this display method is convenient.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f2.png
   :align: center
   :width: 570px

.. container:: centeralign

   Figure 3.2: Op amp closed-loop gain and loop gain interactions with typical open-loop responses


A few key points evolve from this graphic figure, which is a simulation involving two hypothetical op amps, both with a DC/low frequency gain of 100dB (100kV/V). The first has a gain-bandwidth of 1MHz, while the gain-bandwidth of the second is 10MHz.

• The open-loop gain A\ :sub:`VOL` for the two op amps is noted by the two curves marked 1MHz and 10MHz, respectively. Note that each has a -3dB corner frequency associated with it, above which the open-loop gain falls at 6dB/octave. These corner frequencies are marked at 10Hz and 100Hz, respectively, for the two op amps.

• At any frequency on the open-loop gain curve, the numeric product of gain A\ :sub:`VOL` and frequency, f, is a constant (10,000V/V at 100Hz equates to 1MHz). This, by definition, is characteristic of a constant gain-bandwidth product amplifier. All voltage feedback op amps behave in this manner.

• A\ :sub:`VOL`\ β in dB is the difference between open-loop gain and closed-loop gain, as plotted on log-log scales. At the lower frequency point marked, A\ :sub:`VOL`\ β is thus 60dB.

• A\ :sub:`VOL`\ β decreases with increasing frequency, due to the decrease of A\ :sub:`VOL` above the open-loop corner frequency. At 100Hz for example, the 1MHz gain-bandwidth amplifier shows an A\ :sub:`VOL`\ β of only 80-40 = 40dB.

• A\ :sub:`VOL`\ β also decreases for higher values of closed-loop gain. Other, higher closed-loop gain examples (not shown) would decrease A\ :sub:`VOL`\ β to less than 60dB at low frequencies.

• G\ :sub:`CL` depends primarily on the ratio of the feedback components, Z\ :sub:`F` and Z\ :sub:`G`, and is relatively independent of A\ :sub:`VOL` (apart from the errors discussed above, which are inversely proportional to A\ :sub:`VOL`\ β). In this example 1/β is 100, or 40dB, and is so marked at 10Hz. Note that G\ :sub:`CL` is flat with increasing frequency, up until that frequency where G\ :sub:`CL` intersects the open-loop gain curve, and A\ :sub:`VOL`\ β drops to zero.

• At this point where the closed-loop and open-loop curves intersect, the loop gain is by definition zero, which implies that beyond this point there is no negative feedback. Consequently, closed-loop gain is equal to open-loop gain for further increases in frequency.

• Note that the 10MHz gain-bandwidth op amp allows a 10 fold increase in closed-loop bandwidth, as can be noted from the -3dB frequencies; that is 100kHz versus 10kHz for the 10MHz versus the 1MHz gain-bandwidth op amp.

Figure 3.2 illustrates that the high open-loop gain figures typically quoted for op amps can be somewhat misleading. As noted, beyond a few Hz, the open-loop gain falls at 6dB/octave. Consequently, closed-loop gain stability, output impedance, linearity and other parameters dependent upon loop gain are degraded at higher frequencies. One of the reasons for having DC gain as high as 100dB and bandwidth as wide as several MHz, is to obtain adequate loop gain at frequencies even as low as 100Hz.

A direct approach to improving loop gain at high frequencies other than by increasing open-loop gain is to increase the amplifier open-loop bandwidth. figure 3.2 shows this in terms of two simple examples. It should be borne in mind however that op amp gain-bandwidths available today extend to the hundreds of MHz, allowing video and high-speed communications circuits to fully exploit the virtues of feedback.

**ADALM1000 Lab Activity** :doc:`Gain Bandwidth Product </wiki-migration/university/courses/alm1k/alm-lab-gbw>`

3.2.5 The Bode Plot: Asymptotic And Actual Responses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The plot of open-loop gain vs. frequency on a log-log scale gives is what is known as a Bode (pronounced boh dee) plot. It is one of the primary tools in evaluating whether an op amp is suitable for a particular application.

If you plot the open-loop gain and then the noise gain on a Bode plot as shown in figure 3.3, the point where they intersect will determine the maximum closed-loop bandwidth of the amplifier system. This is commonly referred to as the closed-loop frequency (F\ :sub:`CL`). Remember that the actual response at the intersection is actually 3 dB down from this value. At frequencies beyond one octave above and one octave below F\ :sub:`CL`, the difference between the asymptotic response and the real response will be less than 1 dB.

The Bode plot is also useful in determining stability. As stated above, if the closed-loop gain (noise gain) intersects the open-loop gain at a slope of greater than 6 dB/octave (20 dB/decade) the amplifier may be unstable (depending on the phase margin).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.3: Bode Plot Showing Asymptotic and Actual Response


3.2.6 Gain-Bandwidth Product
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The open-loop gain falls at 6 dB/octave for a single-pole response. This means that if we double the frequency, the gain drops by a factor of two. Conversely, if the frequency is halved, the open-loop gain will double, as shown in figure 3.4. This gives rise to what is known as the Gain-Bandwidth Product. If we multiply the open-loop gain by the frequency, the product is always a constant. The caveat for this is that we have to be in the part of the curve that is falling at 6 dB/octave. This gives us a convenient figure of merit with which to determine if a particular op amp is useable in a particular application. Note that the gain-bandwidth product is meaningful only for voltage feedback (VFB) op amps.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.4: Gain-Bandwidth Product


For example, if we have an design which requires a closed-loop gain of 10 and a bandwidth of 100 kHz, we need an op amp with a minimum gain-bandwidth product of 1 MHz. This is a slight oversimplification, however, because of the part to part variability of the gain-bandwidth product and the fact that at the location where the closed-loop gain intersects the open-loop gain, the response is actually down 3 dB. In addition, some extra margin should be allowed.

In the case described above, an op amp with a gain-bandwidth product of 1 MHz would be marginal. A safety factor of at least 5 would be better insurance that the expected performance is achieved, and an op amp with a gain-bandwidth product of 5 MHz should therefore be selected.

3.2.7 Stability Criteria
~~~~~~~~~~~~~~~~~~~~~~~~

Feedback stability theory states that the closed-loop gain must intersect the open-loop gain at a slope no greater than 6 dB/octave (single pole response) for the system to be unconditionally stable. If the response is 12 dB/octave (two pole response), the op amp will oscillate. The easiest way to think of this is that each pole adds 90° of phase shift. Two poles yields 180° phase shift, and 180° of phase shift turns negative feedback into positive feedback which means oscillations.

The question could be asked - why would you want an amplifier that is not unity gain stable? The answer is that for a given amplifier, the bandwidth can be increased at higher gains if the amplifier is not designed to be unity gain stable. This type of op amp is sometimes referred to as a decompensated op amp. However, the stability criteria still must be met. This criteria is that the closed-loop gain must intercept the open-loop gain at a slope of 6 dB/octave (single pole response). If not, the amplifier will oscillate. Decompensated op amps will therefore only be stable at higher gains which are specified on the manufacturer's data sheet.

As an example, compare the open-loop gain graphs in figure 3.5. The three commercial op-amps shown, (AD847, AD848 and AD849) are basically the same design with different internal compensation. The AD847 is unity gain stable and has a specified gain-bandwidth of 50 MHz. The AD848 is stable for gains of 5 or more and has a gain-bandwidth of 175 MHz. The AD849 is stable for a gain of 25 or more and has a gain-bandwidth of 725 MHz. This illustrates how op amp internal compensation can be adjusted in the design to yield various gain-bandwidth products as a function of minimum stable gain for the same basic design topology.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.5: Gain of 1 stable, Gain of 5 stable, Gain of 25 Open-Loop Gain Characteristics, Gain-Bandwidth Products, and phase response


3.2.8 Phase Margin
~~~~~~~~~~~~~~~~~~

One measure of stability is phase margin. Just as the amplitude response doesn't stay flat and then change instantaneously, the phase response will also change gradually, starting approximately a decade before the corner frequency. Phase margin is the amount of phase shift that is left until you reach 180°, measured at the frequency at which the closed-loop gain intersects the open-loop gain.

The result of low phase margin is an increase in gain peaking just before the frequency at which the closed-loop gain intersects the open-loop gain. Figure 3.6 shows the gain and phase response for a typical (the AD8051) op amp. In this case the phase margin is 45° at the frequency of unity gain.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.6: Typical Op Amp (AD8051) Phase Margin


3.3 Op Amp Input Offset Voltage
-------------------------------

3.3.1 Definition Of Input Offset Voltage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ideally, if both inputs of an op amp are at exactly the same voltage, then the output should be at zero volts. In practice, a small differential voltage will need to be applied to the inputs to force the output to zero. This is known as the input offset voltage, V\ :sub:`OS`. Input offset voltage is modeled as a voltage source, V\ :sub:`OS`, in series with the inverting input terminal of the op amp as shown in figure 3.7.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.7: Op Amp Input Offset Voltage


-   Offset Voltage: The differential voltage which must be applied to the input of an op amp to produce zero output.
   \* Ranges:
   \* Chopper Stabilized / Auto-zeroed Op Amps:<1µV
   \* General Purpose Precision Op Amps:50-500µV
   \* Best Bipolar Op Amps:10-25µV
   \* Best JFET Input Op Amps:100-1,000µV
   \* High Speed Op Amps:100-2,000µV
   \* Untrimmed CMOS Op Amps: 5,000 - 50,000µV
   \* DigiTrim(tm) CMOS Op Amps: 100µV - 1,000µV

Chopper stabilized (also called auto-zero) op amps have a V\ :sub:`OS` which is less than 1 µV (examples, AD8538, AD8551, AD8571, AD8628, AD8630), and the best precision bipolar op amps (super-beta or bias stabilized) can have maximum offsets as low as 25 µV (OP177F). The very best trimmed JFET input types have about 100 µV of offset (AD8610B, AD8620B), and untrimmed CMOS op amps can range from 5 to 50 mV.

However, the ADI DigiTrim(tm) CMOS op amps have offset voltages less than 100 µV (e.g., AD8603, AD8607, AD8609, AD8605, AD8606, AD8608). Generally speaking, "precision" op amps will have V\ :sub:`OS` < 0.5 mV, although some high speed amplifiers may be a little worse than this. The DigiTrim process is explained later in this chapter.

3.3.2 Input Offset Voltage Drift And Aging Effects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Input offset voltage varies with temperature, and its temperature coefficient is known as TC\ :sub:`VOS`, or more commonly, drift. Offset drift is affected by offset adjustments to the op amp, but when the offset voltage of a bipolar input op amp has been minimized, the drift may be as low as 0.1 µV/°C (typical value for OP177F). More typical drift values for a range of general purpose precision op amps lie in the range 1-10 µV/°C. Most op amps have a specified value of TC\ :sub:`VOS`, but some, instead, have a second value of maximum V\ :sub:`OS` that is guaranteed over the operating temperature range. Such a specification is less useful, because there is no guarantee that TC\ :sub:`VOS` is constant or monotonic.

The offset voltage also changes as time passes, or ages. Aging is generally specified in µV/month or µV/1000 hours, but this can be misleading. Since aging is a "random walk" phenomenon, it is proportional to the square root of the elapsed time. An aging rate of 1 µV/1000 hour therefore becomes about 3 µV/year (not 9 µV/year).

Long-term stability of the OP177F is approximately 0.3 µV/month. This refers to a time period after the first 30 days of operation. Excluding the initial hour of operation, changes in the offset voltage of these devices during the first 30 days of operation are typically less than 2 µV.

Long-term stability of chopper-stabilized op amps is not specified because the auto-zero circuit removes any offset due to aging.

3.3.3 Measuring Input Offset Voltage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Measuring input offset voltages of a few microvolts requires that the test circuit does not introduce more error than the offset voltage itself. Figure 3.8 shows a standard circuit for measuring offset voltage. The circuit amplifies the input offset voltage by the noise gain of 1001. The measurement is made at the amplifier output using an accurate digital voltmeter. The offset referred to the input (RTI) is calculated by dividing the output voltage by the noise gain. The small source resistance seen by the inputs results in negligible bias current contribution to the measured offset voltage. For example, 2 nA bias current flowing through the 10O resistor produces a 0.02 µV error referred to the input.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.8: Measuring Input Offset Voltage


As simple as this circuit looks, it can give inaccurate results when testing precision op amps, unless care is taken in implementation. The largest potential error source comes from parasitic thermocouple junctions, formed where two different metals are joined. This thermocouple voltage can range from 2 µV/ºC to more than 40 µV/ºC. Note that in this circuit additional "dummy" resistors have been added to the non-inverting input, in order to exactly match/balance the thermocouple junctions in the inverting input path.

The accuracy of the measurement also depends on the mechanical layout of the components and exactly how they are placed on the PC board. Keep in mind that the two connections of a component such as a resistor create two equal, but opposite polarity thermoelectric voltages (assuming they are connected to the same metal, such as the copper trace on a PC board). These will cancel each other, assuming both are at exactly the same temperature. Clean connections and short lead lengths help to minimize temperature gradients and increase the accuracy of the measurement.

In the test circuit, airflow should be minimal so that all the thermocouple junctions stabilize at the same temperature. In some cases, the circuit should be placed in a small closed container to eliminate the effects of external air currents. The circuit should be placed flat on a surface so that convection currents flow up and off the top of the board, not across the components, as would be the case if the board were mounted vertically.

Measuring the offset voltage shift over temperature is an even more demanding challenge. Placing the printed circuit board containing the amplifier being tested in a small box or plastic bag with foam insulation prevents the temperature chamber air current from causing thermal gradients across the parasitic thermocouples. If cold testing is required, a dry nitrogen purge is recommended. Localized temperature cycling of the amplifier itself using a Thermostream-type heater/cooler may be an alternative, however these units tend to generate quite a bit of airflow that can be troublesome. Generally, the test circuit of figure 3.8 can be made to work for many amplifiers. Low absolute values for the small resistors (such as 10O) will minimize bias current induced errors.

An alternate V\ :sub:`OS` measurement method is shown in figure 3.9, and is suitable for cases of high and/or unequal bias currents (as in the case of current feedback op amps). In this measurement method, an instrumentation amplifier is connected to the op amp input terminals through isolation resistors, and provides the gain for the measurement. The offset voltage of the in-amp (measured with S closed) must then be subtracted from the final V\ :sub:`OS` measurement.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.9: Alternate Input Offset Voltage Measurement Using an Instrumentation Amp


3.3.4 Offset Voltage Adjustment Using "NULL" Pins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many single op amps have pins available for optional offset null. To make use of this feature, two pins are joined by a potentiometer, and the wiper goes to one of the supplies through a resistor, as shown generally in figure 3.10. Note that if the wiper is accidentally connected to the wrong supply, the op amp will probably be damaged - this is a common problem, when one op amp type is replaced by another. The range of offset adjustment in a well-designed op amp is no more than two or three times the maximum V\ :sub:`OS` of the lowest grade device, in order to minimize sensitivity. Nevertheless, the voltage gain of an op amp at its offset adjustment pins may actually be greater than the gain at its signal inputs! It is therefore very important to keep these pins noise-free. Note that it is never advisable to use long leads from an op amp to a remote nulling potentiometer.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.10: Offset Adjustment Pins


-   Wiper connection may be to either +V\ :sub:`S` or -V\ :sub:`S` depending on the op amp.
   \* Values for R\ :sub:`1` and R\ :sub:`2` depend on op amp, consult manufacturer's data sheet.
   \* Use to null out the op amp input offset voltage, not the overall system offsets.
   \* There may be high gain from offset pins to output - Keep them quiet!
   \* Nulling offset causes increase in offset temperature coefficient, approximately 4 µV/°C for 1mV offset null for FET input amplifiers

As was mentioned above, the offset drift of an op amp with temperature will vary with the setting of its offset adjustment. The internal adjustment terminals should therefore be used only to adjust the op amp's own offset, not to correct any system offset errors, since doing so would be at the expense of increased temperature drift. The drift penalty for a FET input op amp is in the order of 4 µV/°C for each millivolt of nulled offset voltage. It is generally better to control offset voltage by proper device/grade selection.

3.3.5 Offset Adjustment (External Methods)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If an op amp doesn't have offset adjustment pins (common duals and all quads do not), and it is still necessary to adjust the amplifier and system offsets, an external method can be used. This method is also most useful if the offset adjustment is to be done with a system programmable voltage, such as a Digital to Analog Converter (DAC).

With an inverting op amp configuration, injecting current into the inverting input is the simplest method, as shown in figure 3.11A. The disadvantage of this method is that there is some increase in noise gain possible, due to the parallel path of R\ :sub:`3` and the potentiometer resistance. The resulting increase in noise gain may be reduced by making ±V\ :sub:`R` large enough so that the R\ :sub:`3` value is much greater than R\ :sub:`1`\ IIR\ :sub:`2`. Note that if the power supplies are stable and noise-free, they can be used as ±V\ :sub:`R` otherwise separate regulated low noise (filtered) sources should be used.

Figure 3.11B shows how to implement offset trim by injecting a small offset voltage into the non-inverting input. This circuit is preferred over figure 3.11A, as it results in no noise gain increase (but it requires adding R\ :sub:`P`). If the op amp has matched input bias currents, then RP should equal R\ :sub:`1`\ II R\ :sub:`2` (to minimize the added offset voltage). Otherwise, R\ :sub:`P` should be less than 50Ω. For higher values, it may be advisable to bypass R\ :sub:`P` at high frequencies.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f11.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.11: Inverting Op Amp External Offset Trim Methods


The circuit shown in figure 3.12 can be used to inject a small offset voltage when using an op amp in the non-inverting mode. This circuit works well for small offsets, where R\ :sub:`3`\ can be made much greater than R\ :sub:`1`. Note that otherwise, the signal gain might be affected as the offset potentiometer is adjusted. The gain may be stabilized, however, if R\ :sub:`3` is connected to a fixed low impedance reference voltage sources, ±V\ :sub:`R`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.12: Non-Inverting Op Amp External Offset Trim Methods


3.3.6 Offset Voltage Trim Processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The DigiTrim(tm) CMOS op amp family exploits the advantages of digital technology, so as to minimize the offset voltage normally associated with CMOS amplifiers. Offset voltage trimming is done after the devices are packaged. A digital code is entered into the device to adjust the offset voltage to less than 1 mV, depending upon the grade. Wafer testing is not required, and the patented Analog Devices' technique called DigiTrim(tm) requires no extra pins to accomplish the function. These devices have rail-to-rail inputs and outputs, and the NMOS and PMOS parallel input stages are trimmed separately using DigiTrim to minimize the offset voltage in both pairs. A functional diagram of a typical DigiTrim CMOS op amp is shown in figure 3.13.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f13.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.13: Analog Devices' DigiTrim(tm) Process for Trimming CMOS Op Amps


DigiTrim adjusts the offset voltage by programming digitally weighted current sources. The trim information is entered through existing pins using a special digital sequence. The adjustment values can be temporarily programmed, evaluated, and readjusted for optimum accuracy before permanent adjustment is performed. After the trim is completed, the trim circuit is locked out to prevent the possibility of any accidental re-trimming by the end user.

The physical trimming, achieved by blowing polysilicon fuses, is very reliable. No extra pads or pins are required, and no special test equipment is needed to perform the trimming. The trims can be done after packaging so that assembly-related shifts can be eliminated. No testing is required at the wafer level because of high die yields.

The first devices to use this new technique are the Analog Devices' AD8601, AD8602, AD8604 (single, dual, quad) rail-to-rail CMOS amplifiers. The offset is trimmed for both high and low common-mode conditions so that the offset voltage is under 500 µV over the full common-mode input voltage range. The bandwidth of the op amps is 8 MHz, slew rate is 5 V/µs, and supply current is only 640 µA per amplifier.

The AD8603, AD8605, AD8607 (single, dual, quad) family have maximum offset voltages of 50 µV maximum over the full common-mode range. Gain-bandwidth is 400 kHz, and the supply current is only 50 µA per amplifier.

At this point it is useful to review the other common trim methods. Analog Devices pioneered the use of thin film resistors and laser wafer trimming for precision amplifiers, references, data converters, and other linear ICs. Up to 16-bit accuracy can be achieved with trimming, and the thin film resistors themselves are very stable with temperature and can add to the thermal stability and accuracy of a device, even without trimming. Thin film deposition and patterning are processes that must be tightly controlled. The laser trimming systems are also quite expensive. In-package trimming is not possible, so assembly-related shifts cannot be easily compensated. Nevertheless, thin film trimming at the wafer level provides continuous fine trim resolution in precision integrated circuits where high accuracy and stability are required.

Zener zapping uses a voltage to create a metallic short circuit across the base-emitter junction of a transistor to remove a circuit element. The base-emitter junction is commonly referred to as a zener, although the mechanism is actually avalanche breakdown of the junction. During the avalanche breakdown across the base-emitter junction, the very high current densities and localized heating generate rapid metal migration between the base and emitter connections, leading to a metallic short across the junction. With proper biasing (current, voltage, and time), this short will have a very low resistance value. If a series of these base-emitter junctions are arranged in parallel with a string of resistors, zapping selected junctions will short out portions of the resistor string, thereby adjusting the total resistance value.

It is possible to perform zener zap trimming in the packaged IC to compensate for assembly-related shifts in the offset voltage. However, trimming in the package requires extra package pins. Alternately, trimming at the wafer level requires additional probe pads. Probe pads do not scale effectively as the process features shrink. So, the die area required for trimming is relatively constant regardless of the process geometries. Some form of bipolar transistor is required for the trim structures, therefore a purely MOS-based process may not have zener zap capability. The nature of the trims is discrete since each zap removes a predefined resistance value. Increasing trim resolution requires additional transistors and pads or pins, which rapidly increase the total die area and/or package cost. This technique is most cost-effective for fairly large-geometry processes where the trim structures and probe pads make up a relatively small percentage of the overall die area.

It was in the process of creating the industry standard OP07 in 1975 that Precision Monolithics Incorporated pioneered zener zap trimming. The OP07 and other similar parts must be able to operate from over ±15 V supplies. As a result, they utilize relatively large device geometries to support the high voltage requirements, and extra probe pads don't significantly increase die area.

Link trimming is the cutting of metal or poly-silicon links to remove a connection. In link trimming, either a laser or a high current is used to destroy a "shorted" connection across a parallel resistive element. Removing the connection increases the effective resistance of the combined element(s). Laser cutting works similar to laser trimming of thin films. The high local heat from the laser beam causes material changes that lead to a non-conductive area, effectively cutting a metal or conductive poly-silicon connector.

The high-current link trim method works as an inverse to zener zapping-the conductive connection is destroyed, rather than created by a zener-zap.

Link trim structures tend to be somewhat more compact than laser trimmed resistor structures. No special processes are required in general, although the process may have to be tailored to the laser characteristics if laser cutting is used. With the high-current trimming method, testing at the wafer level may not be required if die yields are good. The laser cutting scheme doesn't require extra contact pads, but the trim structures don't scale with the process feature sizes. Laser cutting of links cannot be performed in the package, and requires additional probe pads on the die. In addition, it can require extra package pins for in-package high-current trims. Like zener zapping, link trimming is discrete. Resolution improvements require additional structures, increasing area and cost .

EEPROM trimming utilizes special, non-volatile digital memory to store trim data. The stored data bits control adjustment currents through on-chip D/A converters.

Memory cells and D/A converters scale with the process feature size. In-package trimming and even trimming in the customer's system is possible so that assembly-related shifts can be trimmed out. Testing at the wafer level is not required if yields are reasonable. No special hardware is required for the trimming beyond the normal mixed-signal tester system, although test software development may be more complicated.

Since the trims can be overwritten, it is possible to periodically reprogram the system to account for long-term drifts or to modify system characteristics for new requirements. The number of reprogram cycles possible depends on the process, and is finite. Most EEPROM processes provide enough rewrite cycles to handle routine re-calibration.

This trim method does require special processing. Stored trim data can be lost under certain conditions, especially at high operating temperatures. At least one extra digital contact pad/package pin is required to input the trim data to the on-chip memory.

This technique is only available on MOS-based processes due to the very thin oxide requirements. The biggest drawback is that the on-chip D/A converters are large-often larger than the amplifier circuits they are adjusting. For this reason, EEPROM trimming is mostly used for data converter or system-level products where the trim D/A converters represent a much smaller percentage of the overall die area.

Table 3.1 summarizes the key features of each manufacturing trim method. It can be seen that all trim methods have their respective uses in producing high performance linear integrated circuits.

============== =================== ========================== ==========
PROCESS        TRIMMED AT:         SPECIAL PROCESSING         RESOLUTION
============== =================== ========================== ==========
DigiTrim(tm)   Wafer or Final Test None                       Discrete
Laser Trim     Wafer               Thin Film Resistor         Continuous
Zener Zap Trim Wafer               None                       Discrete
Link Trim      Wafer               Thin Film or Poly Resistor Discrete
EEPROM Trim    Wafer or Final Test EEPROM                     Discrete
============== =================== ========================== ==========

Table 3.1: Summary of Typical Offset Trim Processes

3.4 Op Amp Input Bias Current
-----------------------------

3.4.1 Definition Of Input Bias Current
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ideally, no current flows into the input terminals of an op amp. In practice, there are always two input bias currents, I\ :sub:`B+` and I\ :sub:`B-` (see figure 3.14).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f14.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.14: Op Amp Input Bias Current


-   I\ :sub:`B` is a very variable parameter!
   \* I\ :sub:`B` can vary from 60 fA(1 electron every 3 µs) to many µA, depending on the device.
   \* Some structures have well-matched I\ :sub:`B`, others do not.
   \* Some structures' I\ :sub:`B` varies little with temperature, but a JFET op amp's I\ :sub:`B` doubles with every 10°C rise in temperature.
   \* Some structures have I\ :sub:`B` which may flow in either direction.

Values of I\ :sub:`B` range from 60 fA (about one electron every three microseconds) in an electrometer op amp (such as the AD549), to tens of microamperes in some high speed op amps. Op amps with simple input structures using bipolar junction transistors (BJT) or FET long-tailed pair have bias currents that flow in one direction. More complex input structures (bias-compensated and current feedback op amps) may have bias currents that are the difference between two or more internal current sources, and may flow in either direction.

Bias current is a problem for the op amp user because it flows in external impedances and produces voltages, which add to system errors. Consider a non-inverting unity gain buffer driven from a source impedance of 1MO. If I\ :sub:`B` is 10nA, it will introduce an additional 10mV of error. This degree of error is not trivial in any system.

Or, if the designer simply forgets about I\ :sub:`B` and uses capacitive coupling, the circuit will not work at all. Or, if I\ :sub:`B` is low enough, it may work momentarily while the capacitor charges, giving even more misleading results. The thing to remember here is not to neglect the effects of I\ :sub:`B`, in any op amp circuit. The same admonition goes for instrument amplifier circuits as well.

3.4.2 Input Offset Current
~~~~~~~~~~~~~~~~~~~~~~~~~~

The input offset current, I\ :sub:`OS`, is the difference between I\ :sub:`B-` and I\ :sub:`B+`, or I\ :sub:`OS` = I\ :sub:`B+` - I\ :sub:`B-`. Note also that I\ :sub:`OS` is only meaningful where the two individual bias currents are fundamentally reasonably well-matched, to begin with. This is true for most voltage feedback (VFB) op amps. However, it would not for example be meaningful to speak of I\ :sub:`OS` for a current feedback (CFB amplifiers are covered in more detail in a later chapter) op amp, as the currents are radically un-matched.

It should be noted that rail-to-rail input stages comprised of two complementary parallel stages have bias currents that change direction as the common-mode voltage passes through the transition region. Bias and offset currents for these devices are especially difficult to specify, other than simply giving a maximum positive/negative value.

3.4.3 Internal Bias Current Cancellation Circuits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By providing this necessary bias currents via an internal current source, as in figure 3.15 below, the only external current then flowing in the input terminals is the difference current between the base current and the current source, which can be quite small.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f15.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.15: A Bias Current Compensated Bipolar Input Stage


-   Pros
   \* Low Offset Voltage: As low as 10 µV
   \* Low Offset Drift: As low as 0.1 µV/ºC
   \* Temperature Stable I\ :sub:`Bias`
   \* Low Bias Currents: <0.5 - 10nA
   \* Low Voltage Noise: As low as 1nV/✔Hz
   \* Cons
   \* Poor Bias Current Match (Currents May Even Flow in Opposite Directions)
   \* Higher Current Noise
   \* Not Very Useful at high frequencies
   \* Matching source impedances makes offset error due to bias current worse because of additional impedance

Most modern precision bipolar input stage op amps use some means of internal bias current compensation, examples would be the familiar OP07 and OP27 series.

Bias current compensated input stages have many of the good features of the simple bipolar input stage, namely: low voltage noise, low offset, and low drift. Additionally, they have low bias current which is fairly stable with temperature. However, their current noise is not very good, and their bias current matching is poor.

These latter two undesired side effects result from the external bias current being the difference between the compensating current source and the input transistor base current. Both of these currents inevitably have noise. Since they are uncorrelated, the two noises add in a root-sum-of-squares fashion (even though the dc currents subtract).

Since the resulting external bias current is the difference between two nearly equal currents, there is no reason why the net current should have a defined polarity. As a result, the bias currents of a bias-compensated op amp may not only be mismatched, they can actually flow in opposite directions! In most applications this isn't important, but in some it can have unexpected effects (for example the droop of a sample-and-hold (SHA) built with a bias-compensated op amp may have either polarity).

In many cases, the bias current compensation feature is not mentioned on an op amp data sheet, and a simplified schematic isn't supplied. It is easy to determine if bias current compensation is used by examining the bias current specification. If the bias current is specified as a "±" value, the op amp is most likely compensated for bias current. Note that this can easily be verified, by examining the offset current specification (the difference in the bias currents). If internal bias current compensation exists, the offset current will be of the same magnitude as the bias current. Without bias current compensation, the offset current will generally be at least a factor of 10 smaller than the bias current. Note that these relationships generally hold, regardless of the exact magnitude of the bias currents.

As previously mentioned, rail-to-rail input stages have bias currents that change direction as the common-mode voltage passes through the transition region. Bias and offset currents for these devices are especially difficult to specify, other than simply giving a maximum positive/negative value.

3.4.4 Canceling The Effects Of Bias Current (External to the Op Amp)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the bias currents of an op amp are well matched (the case with simple bipolar input stage op amps, but not internally bias compensated ones, as noted previously), a bias compensation resistor, R\ :sub:`3`, (R\ :sub:`3`\ =R\ :sub:`1` \|\| R\ :sub:`2`) introduces a voltage drop in the non-inverting input to match and thus compensate the drop in the parallel combination of R\ :sub:`1` and R\ :sub:`2` in the inverting input. This minimizes additional offset voltage error, as in figure 3.16. Note that if R\ :sub:`3` is more than 1kΩ or so, it should be bypassed with a capacitor to prevent noise pickup. Also note that this form of bias cancellation is useless where bias currents are not well-matched, and will, in fact, make matters worse.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f16.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.16: Canceling the Effects of Input Bias Current within an Application


3.4.5 Measuring Input Offset And Input Bias Current
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Input bias current (or input offset voltage) may be measured using the test circuit of figure 3.17. To measure I\ :sub:`B`, a large resistance, R\ :sub:`S`, is inserted in series with the input under test, creating an apparent additional offset voltage equal to I\ :sub:`B`\ ×R\ :sub:`S`. If the actual V\ :sub:`OS` has previously been measured and recorded, the change in apparent V\ :sub:`OS` due to the change in R\ :sub:`S` can be determined, and I\ :sub:`B` is then easily computed. This yields values for I\ :sub:`B+` and I\ :sub:`B-` The rated value of I\ :sub:`B` is the average of the two currents, or I\ :sub:`B` = (I\ :sub:`B+` + I\ :sub:`B-`)/2.

Typical useful R\ :sub:`S` values vary from 100kΩ for bipolar op amps to 1000MΩ for some FET input devices.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f17.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3.17: Measuring Input Bias Current


Extremely low input bias currents must be measured by integration techniques. The bias current in question is used to charge a capacitor, and the rate of voltage change is measured. If the capacitor and general circuit leakage is negligible (this is very difficult for currents under 10 fA), the current may be calculated directly from the rate of change of the output of the test circuit. Figure 3.18 below illustrates the general concept. With one switch open and the opposite closed, either I\ :sub:`B+` or I\ :sub:`B-` is measured.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f18.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.18: Measuring Very Low Bias Currents


It should be noted that only a premium low leakage capacitor dielectric can be used for C, for example Teflon or polypropylene types.

3.5 Op Amp Total Output Offset Voltage Calculations
---------------------------------------------------

3.5.1 Calculating Total Output Offset Error Due To IB And VOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The equations shown in figure 3.19 below are useful in referring all the offset voltage and induced offset voltage from bias current errors to the either the input (RTI) or the output (RTO) of the op amp. The choice of RTI or RTO is a matter of preference.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-f19.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3.19: Op Amp Total Offset Voltage Model


The gain from node A to V\ :sub:`OUT` is the same as the noise gain:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e10.png
   :align: center
   :width: 140px

The gain from node B to V\ :sub:`OUT` is:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e11.png
   :align: center
   :width: 120px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e12.png
   :align: center
   :width: 600px

For bias current cancellation:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e13.png
   :align: center
   :width: 500px

If

**<fs large>I\ B+ = I\ B-\ </fs>**

And

:math:`\displaystyle R_3=[\frac{R_1 R_2}{R_1+R_2 }]`

The RTI value is useful in comparing the cumulative op amp offset error to the input signal. The RTO value is more useful if the op amp drives additional circuitry, to compare the net errors with that of the next stage.

In any case, the RTO value is simply obtained by multiplying the RTI value by the stage noise gain, which is 1 + R\ :sub:`2`/R\ :sub:`1`.

| Before departing the topic of offset errors, some simple rules towards minimization bear repeating:
| \* Keep input/feedback resistance values as low as practical, to minimize offset voltage due to bias current effects.
| \* Use a bias compensation resistance with VFB op amps not designed with internal bias compensation. Bypass this resistance, for lowest noise pickup.
| \* If a VFB op amp does use internal bias current compensation, don't use the compensation resistance.
| \* When necessary, use external offset trim networks, for lowest induced drift.
| \* Choose an appropriate precision op amp specified for low offset and drift, as opposed to trimming.
| \* For high performance, low drift circuitry, watch out for thermocouple effects (which occur when two dissimilar metals are used to make electrical connections) and use balanced, low thermal error PCB layouts.

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-2>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-4>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e1.png
   :width: 150px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e2.png
   :width: 80px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e3.png
   :width: 150px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e4.png
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e5.png
   :width: 200px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e6.png
   :width: 150px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e7.png
   :width: 200px
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e8.png
   :width: 170px
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr3-e9.png
   :width: 170px
