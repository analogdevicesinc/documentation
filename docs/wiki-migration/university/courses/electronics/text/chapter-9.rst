Chapter 9: Single Transistor Amplifier Stages:
==============================================

9.1 Basic Amplifiers
--------------------

The term amplifier as used in this chapter means a circuit (or stage) using a single active device rather than a complete system such as an integrated circuit operational amplifier. An amplifier is a device for increasing the power of a signal. This is accomplished by taking energy from a power supply and controlling the output to duplicate the shape of the input signal but with a larger (voltage or current) amplitude. In this sense, an amplifier may be thought of as modulating the voltage or current of the power supply to produce its output.

The basic amplifier, figure 9.1, has two ports and is characterized by its gain, input impedance and output impedance. An ideal amplifier has infinite input impedance (R\ :sub:`in` = ∞), zero output impedance (R\ :sub:`out` = 0) and infinite gain (A\ :sub:`vo` = ∞) and infinite bandwidth if desired.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.1 Basic Amplifier Model


The transistor, as we have seen in the previous chapter, is a three-terminal device. Representing the basic amplifier as a two port network as in figure 9.1, there would need to be two input and two output terminals for a total of four. This means one of the transistor terminals must be common to both the input and output circuits. This leads to the names common emitter, etc. for the three basic types of amplifiers. The easiest way to determine if a device is connected as common emitter/source, common collector/drain, or common base/gate is to examine where the input signal enters and the output signal leaves. The remaining terminal is what is thus common to both input and output. In this chapter we will primarily be using n-type transistors (NPN, NMOS) in the example circuits. The same basic amplifier stages can just as easily be implemented using p-type transistors (PNP, PMOS). When larger multi-stage amplifiers are assembled, both types of transistors are often interspersed with each other.

Building-block amplifier stages:

-   Inverting voltage amplifier (also called Common emitter or Common source amplifier)
   \* Current Follower (also called Common base or Common gate or cascode)
   \* Voltage Follower (also called Common collector or Common drain amplifier)
   \* Series feedback (more commonly: emitter/source degeneration)
   \* Shunt feedback

9.2 The inverting voltage amplifier or Common emitter/source
------------------------------------------------------------

The common emitter/source amplifier is one of three basic single-stage amplifier topologies. The BJT and MOS versions function as an inverting voltage amplifier and are shown in figure 9.2. The base or gate terminal of the transistor serves as the input, the collector or drain is the output, and the emitter or source is common to both input and output (it may be tied to the ground reference or the power supply rail), which gives rise to its common name.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.2: Basic n-type inverting voltage amplifier circuit (neglecting biasing details)


The common emitter or source amplifier may be viewed as a transconductance amplifier (i.e. voltage in, current out) or as a voltage amplifier (voltage in, voltage out). As a transconductance amplifier, the small signal input voltage, v\ :sub:`be` for a BJT or v\ :sub:`gs` for a FET, times the device transconductance g\ :sub:`m`, modulates the amount of current flowing through the transistor, i\ :sub:`c` or i\ :sub:`d`. By passing this varying current through the output load resistance, R\ :sub:`L` it will be converted back into a voltage V\ :sub:`out`. However, the transistor’s small signal output resistance, r\ :sub:`o`, is not typically high enough for a reasonable transconductance amplifier (ideally infinite). Nor is the output load, R\ :sub:`L`, low enough for a decent voltage amplifier (ideally zero). Another major drawback is the amplifier’s limited high-frequency response due in part to the built in collector base or drain gate capacitance inherent to the transistor. More on how this capacitance effects the frequency response in a later section of this chapter. Therefore, in practice the output often is routed through either a voltage follower (common collector or drain stage), or a current follower (common base or gate stage), to obtain more favorable output and frequency characteristics. This latter combination is called a cascode amplifier as we will see later in the chapter on multi-stage amplifiers.

In comparison to the BJT common emitter amplifier, the FET common source amplifier has higher input impedance. The generally lower g\ :sub:`m`\ of the FET vs. the BJT at equal current levels leads to lower voltage gain for the MOS version.

9.2.1 DC Bias techniques, common emitter/source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order for the common emitter or source amplifier to provide the largest output voltage swing, the voltage at the Base or Gate terminal of the transistor is offset in such a way that the transistor is nominally operating halfway between its cut-off and saturation points. Note the NMOS (a) and NPN (b) characteristic curves in figure 9.2.1. This allows the amplifier stage to more accurately reproduce the positive and negative halves of the input signal superimposed upon the DC Bias voltage. Without this offsetting Bias Voltage only the positive half of the input waveform would be amplified.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   (a) NMOS


.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   (b) NPN


.. container:: centeralign

   Figure 9.2.1 (a) I\ :sub:`D` vs. V\ :sub:`DS`\ curves and (b) I\ :sub:`C` vs. V\ :sub:`CE` curves


The red line superimposed on the two sets of curves represents the DC load line of a 400 ohm R\ :sub:`L`. To maximize the output swing it is desirable to set the operating point of the transistor, with a zero input signal, at a drain or collector voltage of one half the supply voltage, which would be 4 volts in this case. Finding the corresponding drain or collector current along the load line gives us the target current level. This is around 10mA for R\ :sub:`L` equal to 400 ohms. The next step is to determine the corresponding V\ :sub:`GS` or I\ :sub:`B` for a 10mA I\ :sub:`D` or I\ :sub:`C`. In the NMOS example each curve represents a different V\ :sub:`GS` from 0.9 volts to 1.5 volts in 0.1 volt steps. The NMOS device used in this example has a transconductance of about 40mA/V. The I\ :sub:`D` equal to 10mA point on the load line falls between the 1.4V and 1.3V curves or a V\ :sub:`GS` of 1.32V. In the NPN example each curve represents a different I\ :sub:`B` from 10uA to 100uA in 10uA steps. The 50uA curve happens to cross the load line at I\ :sub:`C` =10mA. The β of the transistor must therefore be about 200. The task now is to somehow provide this DC offset or bias at the Gate or Base of the transistor.

The first bias technique we will explore is called voltage divider bias and is shown in figure 9.2.2. If we choose the correct resistor values for R\ :sub:`1` and R\ :sub:`2` that will result in a collector or drain current such that one half of the supply voltage, V+ appears across R\ :sub:`L` we should have our desired value of V\ :sub:`GS` or V\ :sub:`BE` (I\ :sub:`B`) for biasing with no signal input. For the MOS case we know that no current flows into the gate so the simple voltage divider ratio can be used to pick R\ :sub:`1` and R\ :sub:`2`. If V+ = 8V and we want V\ :sub:`GS` to equal 1.32 V then:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e1.png
   :align: center
   :width: 180px

The actual values of R\ :sub:`1` and R\ :sub:`2` are not so important just their ratio. However, the divider ratio we choose will be correct for only one set of conditions of power supply voltage, transistor threshold voltage and transconductance, and temperature. Actual designs often use more involved bias schemes.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.2.2 Voltage divider bias


For the NPN case the calculation is somewhat more involved. We know we want I\ :sub:`B` to be equal to 50uA. The current that flows in R\ :sub:`1` is the sum of the current in R\ :sub:`2` and I\ :sub:`B` which puts an upper bound on R\ :sub:`1` when R\ :sub:`2` is infinite and no current flows in R\ :sub:`2`. If we assume a nominal V\ :sub:`BE` of 0.65 volts then R\ :sub:`1` must be no larger than 7.35V/50uA or 147KΩ. The purpose of the voltage divider is to attenuate the variations in V+ and thus make the DC operating point of the transistor less sensitive to V+. To that end we need to make the current in R\ :sub:`2` many times larger than I\ :sub:`B`. If we, for example, choose to make I\ :sub:`R2` 9 times I\ :sub:`B` then the current in R\ :sub:`1` will be 10*I\ :sub:`B` or 500uA. R\ :sub:`1` will be 1/10 what we just calculated as the upper bound or 14.7KΩ. R\ :sub:`2` will be V\ :sub:`BE` divided by 450uA or 1.444KΩ which is a divider ratio of 0.8921. If we had simply used 8V-V\ :sub:`BE`/8V as the ratio (assume V\ :sub:`BE` = 0.65V) the divider ratio would have been 0.8125. Taking I\ :sub:`B` into account shifted the required ratio. These values would need to be adjusted slightly if the actual V\ :sub:`BE` was not the 0.65 volts (or β was not 200) we used in this calculation. This points out a major limitation of this bias scheme as we pointed out in the MOS example above. That is the sensitivity to device specific characteristics like V\ :sub:`BE` and β as well as supply voltage and temperature.

A consequence of including this bias scheme is a lowering of the input impedance. The input now includes the parallel combination of R\ :sub:`1` and R\ :sub:`2` across the input. For the MOS case this now sets the input resistance. For the BJT case we now have R\ :sub:`1`\ \||R\ :sub:`2`\ \||r\ :sub:`π` as the effective input resistance.

There is another minor inconvenient problem with this bias scheme when it is connected to a prior stage in the signal path. This bias configuration places the AC input signal source directly in parallel with R\ :sub:`2` of the voltage divider. This may not be acceptable, as the input source may tend to add or subtract from the DC voltage dropped across R\ :sub:`2`.

One way to make this scheme work, although it may not be obvious why it will work, is to place a coupling capacitor between the input voltage source and the voltage divider as in figure 9.2.3 below.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.2.3 Coupling capacitor C\ :sub:`C` prevents voltage divider bias current from flowing into the input signal source.


The capacitor forms a high-pass filter between the input source and the DC voltage divider, passing almost the entire AC portion of the input signal on to the transistor while blocking all the DC bias voltage from being shorted through the input signal source. This makes much more sense if you understand the superposition theorem and how it works. According to superposition, any linear, bilateral circuit can be analyzed in a piecemeal fashion by only considering one power source at a time, then algebraically adding the effects of all power sources to find the final result. If we were to separate the capacitor and the R\ :sub:`1`/R\ :sub:`2`\ voltage divider circuit from the rest of the amplifier, it might be easier to understand how this superposition of AC and DC would work.

With only the AC signal source in effect, and a capacitor with an arbitrarily low impedance at the input signal frequency, almost all the AC voltage appears across R\ :sub:`2`.

9.2.2 Small signal voltage gain, common emitter or source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To calculate the small signal voltage gain of the common emitter or source amplifier we need to insert a small signal model of the transistor into the circuit. The small signal models of the BJT and MOS FET are actually very similar so the gain calculation for either version is much the same. The small signal hybrid-π models for the BJT and MOS amplifiers are shown in figure 9.2.4.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.2.4 Common emitter or source small signal models.


The following are some of the key model equations we will need to calculate the amplifier stage voltage gain. These equations are used for the other amplifier configurations that we will discuss in following sections as well.

(BJT)\ |image1| (MOS)\


|image2|

|image3| |image4|

The small signal voltage gain A\ :sub:`v` is the ratio of the input voltage to the output voltage:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e6.png
   :align: center
   :width: 100px

The input voltage V\ :sub:`in` (v\ :sub:`be` for the BJT and v\ :sub:`gs` for the MOS) times the transconductance g\ :sub:`m` is equal to the small signal output current, i\ :sub:`o` in the collector or drain. V\ :sub:`out` will be simply this current times the load resistance R\ :sub:`L,`\ neglecting the small signal output resistance r\ :sub:`o` for the moment. Notice the minus sign because of the direction of the current i\ :sub:`o`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e7.png
   :align: center
   :width: 250px

Rearranging for the gain we get:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e8.png
   :align: center
   :width: 200px

Substituting the BJT and MOS g\ :sub:`m` equations we get:

(BJT)\ |image5| (MOS)\


|image6|

Comparing these two gain equations we see that they both depend on the DC collector or drain currents. The BJT gain is inversely proportional to V\ :sub:`T` (the Thermal Voltage) which is approximately 26mV at room temperature. The Thermal Voltage, V\ :sub:`T` increases with increasing temperature so from the equation we see that the gain will actually decrease with increasing temperature. The MOS gain is inversely proportional to the over drive voltage, V\ :sub:`ov` (V\ :sub:`GS` – V\ :sub:`th`) which is often much larger than V\ :sub:`T` at similar drain currents leading to the lower gain for the MOS stage vs. the BJT stage for approximately equal bias currents.

If R\ :sub:`L` is relatively large when compared to the small signal output resistance then the gain will be reduced because the actual output load is the parallel combination of R\ :sub:`L` and r\ :sub:`o`. In fact r\ :sub:`o` puts an upper bound on the possible gain that can be achieved with a single transistor amplifier stage.

9.2.3 Small signal input impedance, common emitter or source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again looking at the small signal models in figure 9.2.4 we see that for the BJT case the input V\ :sub:`in` will see r\ :sub:`π` as a load. For the MOS case V\ :sub:`in` will see basically an open circuit (for low frequencies anyway). This will of course be the case absent any Gate or Base bias circuitry.

9.2.4 Small signal output impedance, common emitter or source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again looking at the small signal models in figure 9.2.4 we see that for both the BJT case and the MOS case the output impedance is the parallel combination of R\ :sub:`L` and r\ :sub:`o`. For most practical applications we can ignore r\ :sub:`o` because it is very often much larger than R\ :sub:`L`. Below are the BJT and MOS r\ :sub:`o` equations.

(BJT)\ |image7| (MOS)\


|image8|

9.2.5 common emitter and source Lab Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **ADALM1000 Lab Activity 5,** :doc:`Common emitter amplifier </wiki-migration/university/courses/alm1k/alm-lab-5>`
| **ADALM1000 Lab Activity 5M,** :doc:`Common source amplifier </wiki-migration/university/courses/alm1k/alm-lab-5m>`

| **ADALM2000 Lab Activity 5,** :doc:`Common emitter amplifier </wiki-migration/university/courses/electronics/electronics-lab-5>`
| **ADALM2000 Lab Activity 5M,** :doc:`Common source amplifier </wiki-migration/university/courses/electronics/electronics-lab-5m>`
| **ADALM2000 Lab Activity 5FR,** :doc:`Amplifier Frequency Response </wiki-migration/university/courses/electronics/electronics-lab-5fr>`

9.3 The Current Follower also known as Common base or gate amplifier
--------------------------------------------------------------------

The Current Follower or Common base/gate amplifier has a high voltage gain, relatively low input impedance and high output impedance compared to the voltage follower or common collector/drain amplifier. The BJT and MOS versions are shown in figure 9.3

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.3: Basic n-type current follower or common base/gate circuit (neglecting biasing details)


9.3.1 DC Biasing techniques, current follower or common base/gate amplifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In applications where only a positive power supply voltage is provided some means of providing the necessary DC voltage level for the common gate or base terminal is required. This might be as simple as a voltage divider between ground and the supply. In applications where both positive and negative supply voltages are available, ground is a convenient node to use for the common gate or base terminal.

The common gate or base stage is most often used in combination with the common emitter or source amplifier in what is known as the cascode configuration. The cascode will be covered in the next chapter on multi stage amplifiers in greater detail.

9.3.2 Small signal voltage gain, current follower or common base/gate amplifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To calculate the small signal voltage gain of the common base or gate amplifier we insert the small signal model of the transistor into the circuit. The small signal models for the BJT and MOS amplifiers are shown in figure 9.3.1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.3.1 Current follower or Common base/gate small signal models.


Much like in the common emitter/source amplifier stage the small signal input voltage, V\ :sub:`in` (v\ :sub:`be` for the BJT and v\ :sub:`gs` for the MOS) times the transconductance g\ :sub:`m` is equal to the small signal output current, i\ :sub:`o` in the collector or drain. V\ :sub:`out` will be simply this current times the load resistance R\ :sub:`L,`\ neglecting the small signal output resistance r\ :sub:`o` for the moment.

It is perhaps more useful to consider the current gain of the current follower stage rather than its voltage gain. In the case of the MOS version we know that I\ :sub:`S` = I\ :sub:`D`\ because I\ :sub:`G`\ = 0. Thus the MOS stage current gain is exactly 1. In the case of the BJT version we know that the ratio of I\ :sub:`C` to I\ :sub:`E`\ is equal to α and thus will be slightly less than 1.

9.3.3 Input impedance, current follower or common base/gate amplifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again looking at the small signal models in figure 9.3.1 we see that for the BJT case the input V\ :sub:`in` will see r\ :sub:`π`\ in parallel with the series combination of g\ :sub:`m` and R\ :sub:`L` as a load. For the MOS case V\ :sub:`in` will see basically just the series combination of g\ :sub:`m` and R\ :sub:`L`. The equation below (from the BJT small signal T model) relates g\ :sub:`m` and the resistance seen at the emitter r\ :sub:`E`. We can also use this relationship to give us the resistance seen at the source r\ :sub:`S`.

|image9| (also r\ :sub:`S` for MOS)

It is also important to note here that 100% (neglecting I\ :sub:`B` in the BJT case) of the current from the input source flows through the transistor and becomes the output current. Thus the name current follower.

9.3.4 Output impedance, current follower or common base/gate amplifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again looking at the small signal models in figure 9.3.1 we see that for both the BJT case and the MOS case the output impedance is the parallel combination of R\ :sub:`L` and r\ :sub:`o`. We can generally assume this is true if we consider that V\ :sub:`in` is driven from a low impedance (nearly ideal) voltage source. If this is not the case then the finite output impedance must be added in series with r\ :sub:`o`. If the input of the current follower is driven by the relatively high output impedance of a transconductance amplifier such as the common emitter or source amplifier from earlier then the output impedance for the combined amplifier can be very high. For most practical applications we can ignore r\ :sub:`o` because it is very often much larger than R\ :sub:`L`.

| **ADALM1000 Lab Activity,** :doc:`BJT Common Base Amplifier </wiki-migration/university/courses/alm1k/alm-lab-cb>`
| **ADALM1000 Lab Activity,** :doc:`BJT Common Gate Amplifier </wiki-migration/university/courses/alm1k/alm-lab-cg>`
| **ADALM1000 Lab Activity,** :doc:`Folded Cascode Amplifier </wiki-migration/university/courses/alm1k/alm-lab-fca>`

9.4 Voltage followers (also called Emitter or Source follower or Common collector or drain amplifiers)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Emitter or Source follower is often called a common Collector or Drain amplifier because the collector or drain is common to both the input and the output. This amplifier configuration, figure 9.4, has its output taken from the emitter/source resistor and is useful as an impedance matching device since its input impedance is much higher than its output impedance. The voltage follower is also termed a "buffer" for this reason.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f10.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.4:Basic n-type Voltage follower or common collector/drain circuit (neglecting biasing details)


The gain of the voltage follower is always less than one since r\ :sub:`E`\ and R\ :sub:`L`\ or r\ :sub:`S` and R\ :sub:`L` form a voltage divider. The input to output offset is set by the V\ :sub:`BE` drop of about 0.65 volts below the base for the BJT and V\ :sub:`GS` below the gate for the MOS. This configuration’s function is not voltage gain but current or power gain and impedance matching. The input impedance is much higher than its output impedance so that a signal source does not have to supply as much power to the input. This can be seen from the fact that the base current is on the order of 100 times (β) less than the emitter current. The low output impedance of the emitter follower matches a low impedance load and buffers the signal source from that low impedance.

9.4.1 DC Biasing techniques, Voltage Follower or common collector/drain amplifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The collector/source current is basically determined by the emitter/source resistor so the main design variables in this case is simply R\ :sub:`L` and the power supply voltage.

9.4.2 Voltage gain, common collector or drain amplifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To calculate the small signal voltage gain of the voltage follower configuration we insert the small signal model of the transistor into the circuit. The small signal models for the BJT and MOS amplifiers are shown in figure 9.4.1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f11.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.4.1 Voltage Follower small signal models.


.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e14.png
   :align: center
   :width: 300px

Example 9.4.2 Calculating the Voltage Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the circuit in figure 9.4.2 calculate the voltage gain A\ :sub:`V` = V\ :sub:`out`/V\ :sub:`in`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.4.2 BJT Voltage gain example


To use the voltage gain formula we just obtained using the small signal models we need to first calculate r\ :sub:`E`. From section 9.3.3 we are given the equation for r\ :sub:`E`:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e13.png
   :align: center
   :width: 150px

To use this formula we need to know I\ :sub:`E`. We know that the voltage across R\ :sub:`L` is V\ :sub:`out`. We also know that V\ :sub:`out` = V\ :sub:`in` - V\ :sub:`BE`. If we use an estimate of V\ :sub:`BE` to be 0.6 volts, we get V\ :sub:`out` = 5.6 - 0.6 or 5 volts. If R\ :sub:`L` is 1KΩ then I\ :sub:`E` is 5mA. Using a room temperature value for V\ :sub:`T` = 25mV, we get r\ :sub:`E` is equal to 5Ω. Substituting these values into our gain equation we get:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e15.png
   :align: center
   :width: 400px

9.4.3 Input impedance, Voltage Follower (common collector or drain)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(BJT)\


|image10|

9.4.4 Output impedance, Voltage Follower (common collector or drain)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output impedance is simple the parallel combination of the Emitter (Source) resistor R\ :sub:`L` and the small signal emitter (source) resistance of the transistor r\ :sub:`E`. Again from section 9.3.3, the equation for r\ :sub:`E` is as follows:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e13.png
   :align: center
   :width: 150px

Similarly, the small signal source resistance, r\ :sub:`S`, for a MOS FET is 1/g\ :sub:`m`.

Referring back to our gain example in figure 9.4.2, we can also calculate the output resistance, which will be the parallel combination of the 1KΩ R\ :sub:`L` and the 3Ω r\ :sub:`E` or 2.99Ω.

9.4.5 Voltage Follower (common collector or drain) Lab Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **ADALM1000 Lab Activity 11,** :doc:`BJT Emitter follower </wiki-migration/university/courses/alm1k/alm-lab-11>`
| **ADALM1000 Lab Activity 11M,** :doc:`MOS Source follower </wiki-migration/university/courses/alm1k/alm-lab-11m>`

| **ADALM2000 Lab Activity 11,** :doc:`BJT Emitter follower </wiki-migration/university/courses/electronics/electronics-lab-11>`
| **ADALM2000 Lab Activity 11m,** :doc:`MOS Source follower </wiki-migration/university/courses/electronics/electronics-lab-11m>`

9.5 Series Feedback: emitter/source degeneration
------------------------------------------------

Common emitter/source amplifiers give the amplifier an inverted output and can have a very high gain and can vary widely from one transistor to the next. The gain is a strong function of both temperature and bias current, and so the actual gain is somewhat unpredictable. Stability is another problem associated with such high gain circuits due to any unintentional positive feedback that may be present. Other problems associated with the circuit are the low input dynamic range imposed by the small-signal limit; there is high distortion if this limit is exceeded and the transistor ceases to behave like its small-signal model. When negative feedback is introduced, many of these problems are reduced, resulting in improved performance. There are several ways to introduce feedback in this simple amplifier stage, the easiest and most reliable of which is accomplished by introducing a small value resistor in the emitter circuit (R\ :sub:`E`). This is also referred to as series feedback. The amount of feedback is dependent on the relative signal level dropped across this resistor. The signal seen across R\ :sub:`E` is out of phase with the signal seen at V\ :sub:`out` and thus subtracts from V\ :sub:`out` reducing its amplitude. When the emitter resistor value approaches that of the collector load resistor (R\ :sub:`L`), the gain will approach unity (A\ :sub:`v` ~ 1).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f16.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.5: Adding an emitter/source resistor decreases gain. However, with increased linearity and stability


It is much less common to include a degeneration resistor in MOS designs. This is because, in microelectronic integrated circuits, the gain (g\ :sub:`m`) of the device can be adjusted by changing the W/L ratio. This degree of design freedom is not generally available in Bipolar (BJT) processes.

**DC Biasing example with emitter degeneration**

There are some BJT biasing rules of thumb:

| 1. Set I\ :sub:`E` not I\ :sub:`B` or V\ :sub:`BE` : less dependence on β and temperature (V\ :sub:`T`)
| 2. Allow 1/3V\ :sub:`CC` across R\ :sub:`C`, V\ :sub:`CE` and R\ :sub:`B2`
| 3. Save power by allowing only 10% of I\ :sub:`E` in R\ :sub:`B`

We are given the following for circuit in figure 9.5.1, V\ :sub:`CC` = 20V ; I\ :sub:`E` = 2mA ; β = 100. From our rules of thumb we set V\ :sub:`B` = 1/3*V\ :sub:`CC` = 6.7 V.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f17.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.5.1 DC Biasing example


V\ :sub:`B` = (R\ :sub:`B2`/(R\ :sub:`B1`\ +R\ :sub:`B2`))*V\ :sub:`CC` => 6.7V = (R\ :sub:`B2`/(R\ :sub:`B1`\ +R\ :sub:`B2`))*20 (1)

V\ :sub:`CC` /(R\ :sub:`B1` + R\ :sub:`B2` ) = 0.1*I\ :sub:`E` => 20/(R\ :sub:`B1` + R\ :sub:`B2`) = 200 μA (2)

Solving equations (1) and (2) we get:

R\ :sub:`B1`\ =2R\ :sub:`B2` then from (2)

3R\ :sub:`B2` = 20/200 μA = 100kΩ

So, R\ :sub:`B2` = 33kΩ and R\ :sub:`B1` = 66kΩ

Now we have V\ :sub:`E` = V\ :sub:`B` – V\ :sub:`BE` = 6.7 – 0.7 = 6 V and I\ :sub:`E` is 2 mA: R\ :sub:`E` = V\ :sub:`E`/I\ :sub:`E` = 6/2mA = 3kΩ.

I\ :sub:`C` = (β/(β+1))*I\ :sub:`E` = (100/101)*2mA = 1.98 mA and I\ :sub:`B` = I\ :sub:`C`/β = 1.98mA/100 = 19.8μA.

From our rules of thumb we know that V\ :sub:`C` = 2/3*20V = 13.3 V

So to find R\ :sub:`L` we have: R\ :sub:`L` = (V\ :sub:`CC` – V\ :sub:`C`)/I\ :sub:`C` = (20 – 13.3)/1.98mA = 3.4kΩ

9.5.1 Small signal voltage gain with emitter/source degeneration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To calculate the small signal voltage gain of the common emitter/source amplifier with the addition of emitter/source degeneration we again insert the small signal model of the transistor into the circuit. The small signal models for the BJT and MOS amplifiers are shown in figure 9.5.1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f18.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.5.1 Common emitter/source with degeneration


The impedance R\ :sub:`E` reduces the overall transconductance g\ :sub:`m` of the circuit by a factor of g\ :sub:`m`\ R\ :sub:`E` + 1, which makes the voltage gain:

|image11| (when g\ :sub:`m`\ R\ :sub:`E` >> 1)

So the voltage gain depends almost exclusively on the ratio of the resistors R\ :sub:`L` / R\ :sub:`E` rather than the transistor’s intrinsic and unpredictable characteristics. The distortion and stability characteristics of the circuit are thus improved at the expense of a reduction in gain.

Going back to our earlier biasing example, figure 9.5.1, values for I\ :sub:`C` = 2mA, R\ :sub:`L` = 3.4KΩ and R\ :sub:`E` = 3KΩ to calculate the small signal gain we first find g\ :sub:`m` = I\ :sub:`C`/V\ :sub:`T` = 2mA/25mV = 0.08. Using our formula for A\ :sub:`V`:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e18.png
   :align: center
   :width: 300px

9.5.2 Small signal input impedance with emitter/source degeneration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again looking at the small signal models in figure 9.4.1 we see that for the BJT case the input V\ :sub:`in` see r\ :sub:``\ in series with degeneration resistor R\ :sub:`E` as a load. For the MOS case V\ :sub:`in` see basically an open circuit.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e19.png
   :align: center
   :width: 200px

9.5.3 Small signal output impedance with emitter/source degeneration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again looking at the small signal models in figure 9.5.1 we see that for both the BJT case and the MOS case, much like in the earlier common emitter/source stage, the output impedance is the parallel combination of R\ :sub:`L` and r\ :sub:`o` but now degeneration resistor R\ :sub:`E` is in series with r\ :sub:`o`. For most practical applications we can ignore r\ :sub:`o` because it is very often much larger than R\ :sub:`L`.

9.5.4 DC Biasing techniques with emitter/source degeneration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basically the same techniques used in the simple common emitter/source amplifier stage, which were discussed in section 9.2.1, can be used when the emitter degeneration resistor is added. The added voltage across the R\ :sub:`E` (R\ :sub:`E`\ \*I\ :sub:`E`) must be added to the bias level. This added voltage drop actually make the operating point (I\ :sub:`C`) much less sensitive to the bias level.

The small signal voltage gain of the common emitter amplifier with the emitter resistance is approximately R\ :sub:`L` / R\ :sub:`E`. For cases when a gain larger than 5-10 is needed, R\ :sub:`E` may be become so small that the necessary good biasing condition, V\ :sub:`E` = R\ :sub:`E`\ \*I\ :sub:`E` > 10\* V\ :sub:`T` cannot be achieved. A way to restore the small signal voltage gain while maintaining the desired DC operating bias is to use a by-pass capacitor as is figure 9.5.4. The small AC signal sees an emitter resistance of just R\ :sub:`E1` while for DC bias the emitter resistance is the series combination of R\ :sub:`E` = R\ :sub:`E1`\ +R\ :sub:`E2`. Calculations for the common emitter amplifier with emitter degeneration can be applied here by replacing R\ :sub:`E` with R\ :sub:`E1` when deriving the amplifier gain, and input and output impedances, because a sufficiently large bypass capacitor in effects shorts R\ :sub:`E2`\ and is effectively removed from the circuit for sufficiently high frequency inputs.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f19.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.5.4 addition of emitter by-pass capacitor


Using our earlier biasing exercise in figure 9.5.1 as an example but splitting the 3KΩ R\ :sub:`E` into two resistors as in figure 9.5.4 with R\ :sub:`E1`\ = 1KΩ and R\ :sub:`E2` = 2KΩ with C\ :sub:`1` = 1uF we can recalculate the small signal gain for high frequencies, where C\ :sub:`1` effectively shorts out R\ :sub:`E2`, to be:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e20.png
   :align: center
   :width: 300px

The addition of by-pass capacitor C\ :sub:`1`, however, modifies the low frequency response of the circuit. We know from our two gain calculations that the DC gain of the circuit is -1.13 and the gain increases to -3.36 for high frequencies. We can therefore assume that the frequency response consists of a relatively low frequency zero followed by a somewhat higher frequency pole. The formulas for the zero and pole are as follows:

:math:`F_Z = 1/(2 \pi R_E2 C_1)`

:math:`F_P = 1/(2R prime _E C_1)`

where R’\ :sub:`E`\ = R\ :sub:`E2` \|\| (R\ :sub:`E1` + r\ :sub:`e`)

For our example problem with R\ :sub:`E1` = 1K , R\ :sub:`E2` = 2K and C\ :sub:`1` = 1uF we get the frequency for the zero equal to 80 Hz and the frequency for the pole equal to 237 Hz. The simulated frequency response from 1 Hz to 100 KHz for the example circuit is shown in figure 9.5.5.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f20.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.5.5 simulated frequency response


9.5.5 Summary - performing small-signal analyses:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 1. Find DC operating point.
| 2. Calculate small-signal parameters: g\ :sub:`m`, r\ :sub:``, r\ :sub:`e` etc.
| 3. Replace DC voltage sources with AC grounds and DC current sources with open circuits.
| 4. Replace transistor with small-signal model (hybrid-π model or T model)

9.6 Miller’s Theorem
--------------------

At this point we are going to take a diversion to discuss Miller’s Theorem. While the methods we have been using up to this point are completely general, there are certain configurations that lend themselves to be analyzed more simply by Miller’s Theorem. Miller’s theorem states that in a linear circuit, if there is a branch where an impedance Z, connects two nodes with node voltages V\ :sub:`1`\ and V\ :sub:`2`, this branch can be replaced by two other branches connecting the corresponding nodes to ground by impedances respectively Z / (1-K) and KZ / (K-1), where the gain from node 1 to node 2 is K = V\ :sub:`2` / V\ :sub:`1`.

|image12| |image13|

.. container:: centeralign

   Figure 9.6.1 Miller’s Theorem


At this point we will go through the steps that show how the Miller impedances are arrived at. We can use the equivalent two-port network technique to replace the two-port represented in figure 9.6.1(a) to its equivalent in figure 9.6.2.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f23.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 9.6.2


Replacing the voltage sources in figure 9.6.2 with their Norton equivalent current sources we get figure 9.6.3.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f24.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.6.3


Using the source absorption theorem (see the Appendix at the end of this chapter), we get figure 9.6.4.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f25.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.6.4


Which gives us figure 9.6.5 (which is figure 9.6.1(b) ) when we parallel combine the two impedances.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f26.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.6.5


9.7 Shunt feedback:
-------------------

Another biasing technique for the common emitter or source amplifier, called shunt feedback, is accomplished by the introduction of some fraction of the collector or drain signal back to the input at the base or gate. This is done via the biasing resistor (R\ :sub:`F`), as shown in figure 9.7.1. Resistor R\ :sub:`F` connects between two nodes that have gain, A\ :sub:`V` (K), between them and thus the application of Miller’s theorem is the best way analyze the small signal characteristics of this circuit.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f27.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.7.1 Drain-to-Gate (a) and Collector-to-Base (b) shunt feedback


9.7.1 MOS version
~~~~~~~~~~~~~~~~~

Figure 9.7.1(a) shows a common source NMOS amplifier using drain feedback biasing. This type of biasing is often used with enhancement mode MOSFETS and can be useful when operating with a low voltage power supply (V\ :sub:`+`). If Vin is AC coupled, the voltage on the gate is equal to the voltage on the drain (V\ :sub:`GS` = V\ :sub:`DS`) since no gate current flows through R\ :sub:`F`. If Vin is DC coupled then a voltage divider is formed by R\ :sub:`F` and R\ :sub:`S` and V\ :sub:`GS` will be less than V\ :sub:`DS`. It is useful to note that the transistor is always in saturation when V\ :sub:`GS` = V\ :sub:`DS`. If the drain current increases for some reason, such as a change in V\ :sub:`+`, the gate voltage drops. The decreased gate voltage in turn causes the drain current to decreases which causes the gate voltage to increase. The negative feedback loop reaches an equilibrium that is the bias point for the circuit.

Some data sheets for enhancement MOSFETS give a value for I\ :sub:`D`\ (on), where V\ :sub:`GS` = V\ :sub:`DS` lf I\ :sub:`D`\ (on) is known, the circuit component can be easily calculated as shown in Example 9.3. The input impedance of a circuit using drain feedback biasing is equal to the value of R\ :sub:`F` divided by the voltage gain plus one.

9.7.2 BJT Version DC Biasing techniques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This configuration employs negative feedback to stabilize the operating point. In this form of biasing, the base feedback resistor R\ :sub:`F` is connected to the collector instead of connecting it to the DC source V\ :sub:`+`. So any large increase in the collector current will induce a voltage drop across the R\ :sub:`L` resistor that will in turn reduce the transistor’s base current.

If we assume that the input source Vin is AC coupled and no DC bias current flows in R\ :sub:`S`, from Kirchhoff’s voltage law, the voltage V\ :sub:`RF`\ across the base resistor R\ :sub:`F` is:

:math:`V_RF = V_+ - (I_c + I_b )R_L - V_BE`

By the Ebers–Moll model, I\ :sub:`c` = βI\ :sub:`b`, and so:

:math:`V_RF = V_+ - (βI_b + I_b )R_L - V_BE = V_+ - I_b (β + 1 )R_L - V_BE`

From Ohm’s law, the base current I\ :sub:`b`\ =V\ :sub:`RF`/R\ :sub:`F`, and so:

:math:`I_b R_F = V_+ - I_b (β + 1 )R_L - V_BE`

Hence, the base current I\ :sub:`b` is:

:math:`I_b = (V_+ - V_BE ) / (R_F + (β + 1 )R_L )`

If V\ :sub:`BE` is held constant and temperature increases, then the collector current I\ :sub:`c` increases. However, a larger I\ :sub:`c` causes the voltage drop across resistor R\ :sub:`L` to increase, which in turn reduces the voltage V\ :sub:`RF` across the base resistor R\ :sub:`F`. A lower base-resistor voltage drop reduces the base current I\ :sub:`b`, which results in less collector current I\ :sub:`c`. Because an increase in collector current with temperature is opposed, the operating point is kept more stable.

**Pros:**

-   Circuit stabilizes the operating point against variations in temperature and β (ie. Transistor process variations)

**Cons:**

-   In this circuit, to keep I\ :sub:`c` independent of β, the following condition must be met:

:math:`\displaystyle I_c = βI_b = (βV_+ - βB_BE ) / (R_F +(β+1)R_L) approx \frac{V_+ - V_BE}{R_L}`

which is the case when:

:math:`βR_L >> R_F`

-   As β is fixed (and generally not known precisely) for a given transistor, this relation can be satisfied either by keeping R\ :sub:`L` fairly large or making R\ :sub:`F` very low.
   \* If R\ :sub:`L` is large, a high V\ :sub:`+` is necessary, which increases cost as well as precautions necessary while handling.
   \* If R\ :sub:`F` is low, the reverse bias of the collector–base region is small, which limits the range of collector voltage swing that leaves the transistor in active mode.
   \* The resistor R\ :sub:`F` causes an AC feedback, reducing the voltage gain of the amplifier. This undesirable effect is a trade-off for greater quiescent operating point stability.

**Usage:** The feedback also decreases the input impedance of the amplifier as seen from the base, which can be advantageous. Due to the gain reduction from feedback, this biasing form is used only when the trade-off for stability is warranted.

Example 9.7.2 Using Miller’s Theorem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the amplifier shown in figure 9.7.2(a) with a DC coupled input source V\ :sub:`in` calculate the input and output resistance and voltage gain A\ :sub:`V`. We first need to start with some preliminary DC analysis to determine the operating point of Q\ :sub:`1`. For this we set V\ :sub:`in` to zero volts, i.e. short it out. If we assume a V\ :sub:`BE` of 0.65 volts we will have 65 uA flowing in the 10K resistor R\ :sub:`S`. Given that V\ :sub:`+` is 10V, we would like V\ :sub:`out` to be 5 volts. The current in R\ :sub:`L` is equal to 500uA and will split between the collector of Q\ :sub:`1` and the feedback resistor R\ :sub:`F`. The voltage across the 62.7KΩ feedback resistor is 5-0.65 or 4.35 volts. The current in R\ :sub:`F` splits between the current in R\ :sub:`S` and I\ :sub:`B`. The base current I\ :sub:`B` is equal to 4.35/62.7KΩ – 65uA or 4.3 uA. We should get a collector current of 500uA - 69.3uA or 430.3uA with a β of about 100.

If we use Miller’s theorem to replace the feedback resistor R\ :sub:`F` with its two equivalent impedances we get figure 9.7.2(b). Assuming that the voltage gain from base to collector A\ :sub:`V` is significantly greater than 1 we can make the simplification that A\ :sub:`V`/(A\ :sub:`V`-1) is close to 1. The effective load resistance, R\ :sub:`Leq` we will use to calculate the gain will be 10KΩ||62.7KΩ or 8.62KΩ. Now we can use the same common emitter or source small signal gain equations we used in section 9.2.2. The 430uA collector currents gives us a g\ :sub:`m` of 430uA/25mV or 0.0172. We know that A\ :sub:`V` = -g\ :sub:`m`\ R\ :sub:`Leq` or A\ :sub:`V` = -0.0172*8.62K = -148 which is >> 1. The input resistance seen at the base of Q\ :sub:`1` will be the r\ :sub:`π`\ of Q\ :sub:`1`, which is equal to β/g\ :sub:`m` or 100/0.0172 = 5.814KΩ, in parallel with the Miller resistance 62.7KΩ/149 = 421Ω thus the effective input resistance, R\ :sub:`base` will be about 392.5Ω.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f28.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.7.2 Example using Miller’s theorem


The input source resistance R\ :sub:`S` and the equivalent resistance at the base, R\ :sub:`base` form a voltage divider. To calculate the overall voltage gain from voltage source V\ :sub:`in` to V\ :sub:`out` we multiply this divider ratio times the base to collector gain, A\ :sub:`V` we just calculated.

:math:`\displaystyle R_base / (R_S + R_base ) A_V = (392.\frac{5}{10392}.5) \times 148 = 5.6`

From our investigation of the inverting op amp configuration in Chapter 3 we learned that for amplifiers with less than infinite gain the actual gain will be less than the ideal gain equation, Gain = -R\ :sub:`F`/R\ :sub:`S` predicts. If our single transistor amplifier had infinite gain the gain from V\ :sub:`in` to V\ :sub:`out` would be 62.7KΩ/10KΩ or 6.27. In Chapter 3 we got an estimation of the percentage error, ε, due to finite gain A\ :sub:`V` (remember β in this equation is the feedback factor not the current gain of the transistor):

:math:`\epsilon(%) approx 100/(A_V \beta ) = 100/(148 \times 6.2) = 10.7%`

The actual gain of 5.6 is about 10% smaller than the ideal gain of 6.27.

Exercise 9.7
~~~~~~~~~~~~

Part 1 DC operating point:

For the circuit in figure 9.7.3 calculate the required R\ :sub:`F` to bias the DC operating point such that V\ :sub:`out` is equal to ½ the supply voltage or +5V when Vin = 0. Assume V\ :sub:`BE` = 0.65V and β = 200.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f29.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 9.7.3


Part 2 Small signal gain and impedance:

Given the value for R\ :sub:`F` calculated in part 1 calculate the voltage gain A\ :sub:`V`, the input resistance R\ :sub:`base` and the output resistance R\ :sub:`out`. Also calculate the overall voltage gain V\ :sub:`out`/V\ :sub:`in` and explain why this is different than the ideal value of –R\ :sub:`F`/R\ :sub:`S`.

9.7.5 The Miller Effect
~~~~~~~~~~~~~~~~~~~~~~~

The Miller effect is key to predicting the frequency response of an inverting amplifier stage where capacitive feedback is included. Typically there’s a low-pass pole in the voltage gain stage created by R\ :sub:`S` of the signal source and a feedback capacitor C\ :sub:`C`. But, the low pass cutoff is not simply determined by R\ :sub:`S` and C\ :sub:`C`. The Miller effect creates an effective capacitance at the base/gate of the transistor that appears as C\ :sub:`C` scaled by the amplifier’s voltage gain.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f30.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.7.3 Miller feedback capacitor


The Miller effect is especially useful when you’re trying to produce a low-pass filter on an IC op amp with a relatively low frequency cut-off. The difficulty is that large capacitors are difficult to make because they take up so much space on the IC. The solution is to make a small capacitor and then scale up its behavior using the Miller effect.

Equivalent Circuit

Here’s a simplified version of the circuit above.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f31.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.7.4 Miller feedback equivalent circuit


Miller said that you can approximate the input capacitance by replacing C\ :sub:`C` with a different capacitance C\ :sub:`M` across the R\ :sub:`IN`. How much bigger is C\ :sub:`M`? C\ :sub:`C` is multiplied by the voltage gain (A\ :sub:`V` = g\ :sub:`m`\ R\ :sub:`L`) of the amplifier. Miller’s theorem also states there will be a capacitor C’\ :sub:`C` across R\ :sub:`L` that is equal to C\ :sub:`C` times (A\ :sub:`V`\ +1)/A\ :sub:`V` which for large values of A\ :sub:`V` we assume to be 1.

:math:`C_M = C_C · (1+A_V) , C’_C ~ C_C`

How does this work? Well, we know that forcing a voltage across a capacitor causes a current to flow. How much current depends on the capacitance: I = C\ :sub:`C` · ΔV/Δt. However, in this circuit, the voltage gain at R\ :sub:`L` causes a much larger ΔV across C\ :sub:`C` - causing an even larger current to flow through C\ :sub:`C`. Therefore, it looks like a much larger capacitance from the point of view of V\ :sub:`IN`.

Example 9.7.3 Miller Capacitance Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example we will use the circuit shown in figure 9.7.5 to illustrate the Miller multiplication of the feedback capacitor C\ :sub:`C`. Bias resistors R\ :sub:`1` and R\ :sub:`S` are chosen to set the DC operating point such that V\ :sub:`out` is at a DC value of approximately V+/2 or 5V. With the given R\ :sub:`L` of 10KΩ the low frequency small signal voltage gain A\ :sub:`V` is approximately 80.

We can now calculate the -3 dB frequency and unity gain (0dB) frequency for a feedback capacitor, C\ :sub:`C`, of 0.001 uF. The frequency where the gain from V\ :sub:`in` to V\ :sub:`out` falls by -3 dB from its DC values is approximately equal to:

The unity gain frequency is approximately equal to :

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f32.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.7.5 Miller Capacitance Example


The circuit in figure 9.7.5 was simulated and the AC frequency response from 1 Hz to 1 MHz is plotted in figure 9.7.6. The gain from V\ :sub:`in` to V\ :sub:`out` in dB is 20Log(A\ :sub:`V`) or about 38 dB. The -3 dB frequency in this case would be where the gain curve crosses 35 dB (~263 Hz) and the unit gain frequency would be where the gain curve crosses the 0 dB line (~21.7 KHz ). The simulation results are in reasonably close agreement with our approximate hand calculations. For our hand calculations we assumed that R\ :sub:`1` was sufficiently larger than R\ :sub:`S` so it could be ignored and likewise the r\ :sub:`π` of Q\ :sub:`1` was large enough to not materially affect R\ :sub:`S`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f33.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9.7.6 Frequency sweep simulation


Chapter Summary:
----------------

-   The Common Emitter stage has high gain but low input and high output impedance.
   \* R\ :sub:`E` emitter degeneration improves input impedance and provides negative feedback to stabilize DC operating point but with some loss in gain.
   \* The Common Base stage has low input, high output impedance but is good at high frequencies. Good current buffer sometimes called the current follower.
   \* The Common Collector or Emitter follower can be biased with large input impedance, low output impedance but has approximately unity gain. Good voltage buffer.

Appendix: Source absorption theorem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The source absorption theorem has two dual forms: the voltage source absorption and the current source absorption theorems.

The voltage source absorption theorem states that if, in one branch of the circuit with current I, there is a voltage source controlled by I, the source can be replaced by a simple impedance with value equal to the source controlling factor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f34.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9A.1


The proof is trivial. An impedance Z where a current I flows has the same voltage drop the I controlled source generates at its terminals.

The current source absorption theorem states that if, in one branch of the circuit there is a current source controlled by a voltage V, the source can be replaced by a simple admittance with value equal to the source controlling factor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f35.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9A.2


The proof is again trivial. An admittance Y submitted to a voltage V imposes the same current that the source Y V provides.

Example A1: Finding the Emitter Resistance using Source absorption theorem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Figure A9.3 shows the small signal equivalent circuit model of a transistor. Find the resistance Rin looking into the emitter (with base and collector at small signal AC grounds).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f36.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9A.3


Using what we just learned about the source absorption theorem for current sources we know we can replace the controlled source with a resistance equal to 1/g\ :sub:`m`\ its transconductance.

Advanced Topics:
----------------

AT1 Diode bias generation
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f37.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure AT1.1 Inserting a Diode connected device in the bias divider


.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f38.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure AT1.2 Inserting R\ :sub:`2`\ increases the input resistance


**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-8>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-10>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e2.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e3.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e4.png
   :width: 100px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e5.png
   :width: 150px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e9.png
   :width: 200px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e10.png
   :width: 200px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e11.png
   :width: 200px
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e12.png
   :width: 200px
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e13.png
   :width: 200px
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e16.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-e17.png
   :width: 290px
.. |image12| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f21.png
   :width: 350px
.. |image13| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr9-f22.png
   :width: 350px
