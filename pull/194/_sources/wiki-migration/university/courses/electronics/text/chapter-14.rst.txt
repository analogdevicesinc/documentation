Chapter 14: Voltage References
==============================

14.1 Introduction
-----------------

Voltage references and linear voltage regulators have much in common. In fact, the latter could be functionally described as a reference circuit, but at a greater current (or power) output level. Accordingly, many of the specifications of the two circuit types have great commonality (even though the output voltage tolerance of references is usually tighter with regard to temperature drift, accuracy, etc.).

Voltage references have a major impact on the performance and accuracy of analog systems. A ±5 mV tolerance on a 5 V reference corresponds to ±0.1% absolute accuracy which is only 1 part in a thousand or 10-bit accuracy. For a system with 12-bit accuracy, choosing a reference that has a ±1 mV tolerance may be far easier than manually calibrating a lower accuracy reference. Both high initial accuracy and calibration are likely to be necessary in a system making absolute 16-bit measurements. Note that many systems make relative or ratiometric measurements rather than absolute ones. In such cases the absolute accuracy of the reference is not as important, although noise and short-term stability may be.

Temperature drift or drift due to aging may be an even greater problem than absolute accuracy. The initial error can always be adjusted or calibrated, but compensating for drift over temperature or time is difficult. Where possible, references should be designed for low temperature drift and aging characteristics which preserve adequate accuracy over the operating temperature range and expected lifetime of the system. Noise in voltage references is often overlooked, but it can be very important in system design. Noise is an instantaneous change in the reference voltage. It is generally specified on component data sheets, but system designers frequently ignore the specification and mistakenly assume that their voltage reference does not contribute noise in their system.

There are two dynamic issues that must be considered with voltage references: their behavior at start-up, and their behavior with transient loads. With regard to the first, always bear in mind that voltage references do not power up instantly (this is true of references inside power supply regulators, ADCs and DACs as well as discrete designs). Thus it is rarely possible to turn on an ADC and reference, whether internal or external, make a reading, and turn off again within a relatively few microseconds, however attractive such a operation might be in terms of energy saving.

Regarding the second point, a given reference IC may or may not be well suited for pulse or fast transient loading conditions, dependent upon the specific architecture. Many references use low power, and therefore low bandwidth, output buffer amplifiers. This makes for poor behavior under fast transient loads, which may degrade the performance of high speed ADCs (especially capacitor based successive approximation and pipe-line ADCs). Suitable decoupling can ease the problem (but some references oscillate with large capacitive loads), or an additional external broadband buffer amplifier may be used to drive the part of the circuit where the transients occur.

14.2 Simple Diode References
----------------------------

In terms of the functionality of their circuit connection, standard reference ICs are often only available in series, or three-terminal form (V\ :sub:`IN`, Common, V\ :sub:`OUT`), and also in positive polarity only. The series types have the potential advantages of lower and more stable quiescent current, standard pre-trimmed output voltages, and relatively high output current without accuracy loss. Shunt, or two-terminal (i.e. diode-like) references are more flexible regarding operating polarity, but they are also more restrictive as to loading. They can in fact eat up excessive power with widely varying resistor-fed voltage inputs. Also, they sometimes come in non-standard voltages. All of these various factors tend to govern when one functional type is preferred over the other. By contrast, these most simple references (as well as all other shunt-type regulators) have a basic advantage, which is the fact that the polarity is readily reversible by flipping connections and reversing the drive current. However, a basic limitation of all shunt regulators is that load current must always be less (usually significantly less) than the driving current.

Some simple diode-based references are shown in Figure 14.1. In the first of these, a current driven forward biased diode (or diode-connected transistor) produces a voltage, V\ :sub:`f`\ = V\ :sub:`REF`. While the junction drop is somewhat decoupled from the raw supply, it has numerous deficiencies as a reference. Among them are a strong temperature coefficient (TC) of about -0.3%/°C, some sensitivity to loading, and a rather inflexible output voltage, it is generally only available in increments of 0.65V.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   (a) Forward-biased Diode (b) Zener (Avalanche) Diode


.. container:: centeralign

   Figure 14.1: Simple two terminal Diode Reference Circuits


The significant negative temperature coefficient of the forward biased emitter base junction of a diode connected transistor is dependent on V\ :sub:`BE`. To explore this let us first reexamine the V\ :sub:`BE` equation.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_e1.png
   :align: center
   :width: 150px

At first glance one sees that absolute temperature, T, appears in the equation and the quantity V\ :sub:`T`, the thermal voltage (kT/q), has a positive temperature coefficient. This would make V\ :sub:`BE` have a positive temperature coefficient if I\ :sub:`S,` the junction saturation current, was constant over temperature. I\ :sub:`S`\ in fact has a very strong temperature coefficient as seen in the following equation for I\ :sub:`S`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_e2.png
   :align: center
   :width: 220px

| Note: E\ :sub:`g`\ is the energy gap of Silicon
| M represents the temperature dependence of mobility

If we use this equation for I\ :sub:`S` and insert it in the V\ :sub:`BE` equation and then differentiate with respect to temperature we get the following relationship for a constant I\ :sub:`C`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_e3.png
   :align: center
   :width: 230px

Note:

|image1| and |image2|

We can see this in the temperature simulation plot shown in figure 14.2 where the current through a diode connected NPN transistor is set to 1mA, 2mA, 5mA and 10mA.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f2.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 14.2 V\ :sub:`BE` vs. Temperature at 1mA, 2mA, 5mA and 10mA


The slope of the 10 mA line is slightly less negative than the 1 mA line. In fact all the V\ :sub:`BE` vs. temperature lines would converge at absolute zero when projected back to the origin. The voltage they converge to is approximately the energy gap of Silicon or 1.2 volts. This property is not very helpful by itself but when combined with another property of BJTs can result in a low temperature coefficient reference as we will discuss in section 14.3 on the Bandgap reference.

The V\ :sub:`BE` voltage of the simple diode connected transistor of figure 14.1(a) can be used to generate a regulated current reference as well, as shown in figure 14.3. In this circuit the simple diode connection around Q\ :sub:`1`\ is replaced by emitter follower Q\ :sub:`2`. The V\ :sub:`BE` of Q\ :sub:`1` is impressed across R\ :sub:`2` and the resulting current flows through Q\ :sub:`2` to become I\ :sub:`REF`, neglecting the base currents of Q\ :sub:`1` and Q\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 14.3 V\ :sub:`BE` generated reference current.


The resulting reference current, I\ :sub:`REF`, will be equal to V\ :sub:`BE` divided by R\ :sub:`2` and have the strong negative temperature coefficient as we saw in figure 14.2. This negative temperature coefficient of the current is often referred to as CTAT or Complementary To Absolute Temperature. We can compensate for this negative temperature drift by summing this current with another current with an equally strong positive temperature coefficient. Remembering back to Chapter 11 Section 10 where we discussed the Peaking Current source, we have a circuit block that has such a positive temperature drift. We referred to this as a PTAT or Proportional To Absolute Temperature current. In figure 14.4 we combine the circuit from figure 14.3 (Q\ :sub:`1`, Q\ :sub:`2`, R\ :sub:`1`\ and R\ :sub:`2`) on the right with the peaking current source from figure 11.18 in Chapter 11 (Q\ :sub:`3`, Q\ :sub:`4`, R\ :sub:`3`\ and R\ :sub:`4`).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 14.4 Combining CTAT and PTAT currents to make a constant I\ :sub:`REF`


If we set the PTAT and CTAT currents to be roughly equal (70uA) at some nominal temperature then the sum of the two currents (140uA) will be approximately flat vs. temperature as we see in the simulation plot in figure 14.5.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f5.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 14.5 Combined CTAT and PTAT current sources makes a constant


It is also important to point out here that if the temperature independent I\ :sub:`REF` current were applied to a low temperature coefficient resistor a more or less temperature independent voltage reference would be the result. The need for a zero TCR resistor is not strictly required if all the resistors used in the circuit are at the same temperature and have identical TCR.

14.2.1 Zener diodes
~~~~~~~~~~~~~~~~~~~

In the second circuit of figure 14.1(b), a zener or avalanche diode is used, and an appreciably higher output voltage results. While true zener breakdown occurs below 5 V, avalanche breakdown occurs at higher voltages and has a positive temperature coefficient. Note that diode reverse breakdown is referred to almost universally today as zener, even though it is usually avalanche breakdown. With a D\ :sub:`1` breakdown voltage in the 5 to 8 V range, the net positive TC is approximately such that it equals the negative TC of forward-biased diode D\ :sub:`2`, yielding a small net TC of 100 ppm/°C or less when operated at the proper bias current. Combinations of such carefully chosen diodes formed the basis of the early single package "temperature-compensated zener" references, such as the 1N821-1N829 series.

The temperature-compensated zener reference is limited in terms of initial accuracy, since the best TC combinations fall at odd voltages, such as the 1N829's 6.2 V. And, the scheme is also limited for loading, since for best TC the diode current must be carefully controlled. Unlike a fundamentally lower voltage (<2 V) reference, zener diode based references must of necessity be driven from voltage sources appreciably higher than 6 V levels, so this precludes operation of zener references from 5 V or lower system supplies.

References based on low TC zener (avalanche) diodes also tend to be noisy, due to the basic noise of the breakdown mechanism. This has been improved greatly with monolithic zener types, as is described further in section 14.4.

14.3 Bandgap References
-----------------------

The development of voltage references with low output voltages (<5 V) based on the bandgap voltage of silicon has led to the introduction of various integrated circuits with low temperature drift. The bandgap reference technique is attractive in IC designs because of several reasons; among these are the relative simplicity, and the avoidance of zeners and their noise. However, very important in these days of ever decreasing system supplies is the fundamental fact that bandgap devices operate at low voltages down to 1.2V or less. Not only are they used for stand-alone IC references, but they are also used within the designs of many other linear ICs such as ADCs and DACs.

To understand the underlying concept of the Bandgap reference we first need to explore an important relationship involving bipolar transistors. Imagine that we have two identical transistors as shown in figure 14.6.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 14.6 A powerful relationship in circuit design


Let's assume that each of these devices is provided with voltages at the base and that the collector voltage (V+) is positive enough to avoid saturation, which is generally greater than V\ :sub:`BE`. In this experiment we will need to measure the two collector currents and the difference in base voltage. Since we can monitor the collector currents, it should be easy to constrain the range of the currents to a value where the collector current and base voltage are related by the now familiar relationship:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_e6.png
   :align: center
   :width: 200px

Where, I\ :sub:`C` is the collector current, V\ :sub:`BE` is the base-emitter voltage, I\ :sub:`S` is the saturation current for the transistor with a particular geometry and doping, and q/kT is the reciprocal of the thermal voltage. A fairly standard transistor operating at around 100uA may have a V\ :sub:`BE`\ of around 650mV at room temperature where q/kT is about 0.039/V. The exponential factor in the equation will be on the order of 10\ :sup:`11`. In this case we can safely drop the -1 term without serious error. Using this approximation we can now investigate the effect of operating the matched transistors at different currents. If we establish the two collector currents I\ :sub:`C1` and I\ :sub:`C2` by adjusting V\ :sub:`BE1` and V\ :sub:`BE2`, then we can take the ratio of the two currents and remembering that I\ :sub:`S1` is equal to I\ :sub:`S2`, as follows by rearranging the equation:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_e7.png
   :align: center
   :width: 200px

From this equation we get the expected result that V\ :sub:`BE1`-V\ :sub:`BE2`\ =0 when the ratio of I\ :sub:`C1` to I\ :sub:`C2` is equal to 1. We can get the equation for the difference in V\ :sub:`BE` (ΔV\ :sub:`BE`) by taking the natural logarithm:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_e8.png
   :align: center
   :width: 350px

From these equations we can see that the I\ :sub:`S` terms are gone so the strong negative temperature effect is now gone as well. So the ΔV\ :sub:`BE` now has a positive temperature coefficient and is in fact proportional to absolute temperature (PTAT).

We can now proceed to the next step in developing a voltage reference. We now extend this concept for transistors with equal base voltages but different emitter areas as shown in figure 14.7. The V\ :sub:`BE` of Q\ :sub:`1`\ equals the V\ :sub:`BE` of Q\ :sub:`2`, which results in a controlled current ratio between I\ :sub:`C1` and I\ :sub:`C2` of 1:8 based on their relative emitter areas.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 14.7 Different emitter areas results in controlled current ratio


We can now reduce the current in Q\ :sub:`2`\ back to be equal to that of Q\ :sub:`1` by inserting a resistor between the emitter of Q\ :sub:`2` and ground as in figure 14.8. I\ :sub:`C2` x R\ :sub:`1` reduces the V\ :sub:`BE` of Q\ :sub:`2` changing the I\ :sub:`C1` / I\ :sub:`C2` ratio. The voltage drop across the resistor, R\ :sub:`1` represents the ΔV\ :sub:`BE` at that particular current level. For a given value for R\ :sub:`1`, there will be one and only one value of V\ :sub:`BE`\ where the two collector currents are equal (other than I\ :sub:`C1`\ =I\ :sub:`C2`\ =0). This is shown in the simulation plot in figure 14.9 where for an emitter area ratio of 8 and a resistor value of 200 ohms.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 14.8 Inserting emitter resistor R\ :sub:`1`


At low currents where the voltage drop across R\ :sub:`1` is relatively small, I\ :sub:`C2` increases more or less exponentially at 8 times I\ :sub:`C1`. As the voltage drop across R\ :sub:`1` increases, the current I\ :sub:`C2` becomes less and less exponential and eventually the still exponential I\ :sub:`C1` catches up and passes I\ :sub:`C2`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f9.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 14.9 Plot of collector current vs. V\ :sub:`BE`


If we can configure a circuit, usually through negative feedback, that adjusts V\ :sub:`BE` in figure 14.8 such that I\ :sub:`C1`\ =I\ :sub:`C2` we can obtain a controlled value for ?V\ :sub:`BE`.

The basic principle of the Bandgap reference is examined here using the circuit originally proposed by Robert Widlar in 1971 and is shown in figure 14.10. The fundamental idea Widlar used was to compensate the negative TC of the base emitter voltage V\ :sub:`BE` by summing it with a second voltage V(R\ :sub:`2`) which has a positive TC.

| All Bandgap references use two basic elements:
| 1. Two BJT's working at different current densities
| 2. Adding a V\ :sub:`BE` (-TC) and a PTAT voltage drop (+TC)

The problem is that in order to compensate the large negative TC of V\ :sub:`BE` a rather large ΔV\ :sub:`BE` on the order of 600mV would be required. This cannot be done with the simple circuit of figure 14.8.

The first of these reference circuits was the LM109, and a basic bandgap cell is shown in Figure 14.10.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 14.10: Basic Bandgap Reference


This circuit is also called a "ΔV\ :sub:`BE`" reference. The differing current densities between matched transistors Q\ :sub:`1`-Q\ :sub:`2` produce a ΔV\ :sub:`BE` across R\ :sub:`3`. Because resistors R\ :sub:`1` and R\ :sub:`2` are in the ratio of 1:10 the current in Q\ :sub:`2` will be 1/10 that in Q\ :sub:`1` resulting in a smaller V\ :sub:`BE` for Q\ :sub:`2`. The output, V\ :sub:`Ref`, is produced by summing the V\ :sub:`BE` of Q\ :sub:`3` with the amplified ΔV\ :sub:`BE` of Q\ :sub:`1`-Q\ :sub:`2`, developed across R\ :sub:`2`. The ΔV\ :sub:`BE` and V\ :sub:`BE` components have opposite polarity TCs; ΔV\ :sub:`BE` is proportional-to-absolute-temperature (PTAT), while V\ :sub:`BE` is complementary-to-absolute-temperature (CTAT). When the summed output, V\ :sub:`Ref,` is equal to 1.205 V (silicon bandgap voltage), the TC is a minimum. I\ :sub:`IN` must be larger than the sum of I\ :sub:`C1` and I\ :sub:`C2` and the excess current will flow in Q\ :sub:`3` as I\ :sub:`C3`.

However, the basic designs of figure 14.10 suffer from load and current drive sensitivity, plus the fact that the output needs accurate scaling to more useful levels, i.e., 2.5 V, 5 V, etc. The load drive issue is best addressed with the use of a buffer amplifier, which can also provide convenient voltage scaling to standard levels.

An improved three-terminal bandgap reference, (the AD580 introduced in 1974) is shown in figure 14.11. Popularly called the "Brokaw Cell", this circuit provides on-chip output buffering, which allows good drive capability and standard output voltage scaling.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 14.11: Brokaw Cell Precision Bandgap Reference (AD580 1974)


The Brokaw Cell based AD580 was the first precision bandgap based IC reference, and variants of the topology have influenced further generations of industry standard references.

The popular design choice is two 8:1 emitter-scaled transistors Q\ :sub:`1`-Q\ :sub:`2` operating at identical collector currents (and thus 1/8 current densities), by virtue of matched load resistors R\ :sub:`3`,R\ :sub:`4` and a closed loop feedback around the buffer op amp. Due to the resultant smaller V\ :sub:`BE` of the 8× area Q\ :sub:`1`, R\ :sub:`2` in series with Q\ :sub:`1` drops the ΔV\ :sub:`BE` voltage, while R\ :sub:`1` (due to the current relationships) has a multiplied PTAT voltage V\ :sub:`R1`:

|image3| |image4|

The bandgap cell reference voltage V\ :sub:`BG` appears at the combined base of Q\ :sub:`1` and Q\ :sub:`2`, and is the sum of V\ :sub:`BE` (Q\ :sub:`2`) and V\ :sub:`R1`, or 1.205 V, the bandgap voltage:

However, because of the presence of the R\ :sub:`5`/R\ :sub:`6` resistor divider and the op amp, the actual voltage appearing at V\ :sub:`OUT` can be scaled higher, in this case 2.5 V. Following this general principle, V\ :sub:`OUT` can be raised to almost any other practical level, such as for example with selectable taps for precise 2.5, 5, 7.5, and 10 V output values. The buffer amplifier can often provide up to 10 mA output current while operating from supplies between 4.5 and 30 V. These kinds of references can have output tolerances as low as 0.4%, with TCs as low as 10 ppm/°C.

| **ADALM1000 Lab Activity 9,** :doc:`Bandgap reference </wiki-migration/university/courses/alm1k/alm-lab-9>`
| **ADALM1000 Lab Activity 10,** :doc:`Shunt Bandgap reference </wiki-migration/university/courses/alm1k/alm-lab-10>`

| **ADALM2000 Lab Activity 9,** :doc:`Bandgap reference </wiki-migration/university/courses/electronics/electronics-lab-9>`
| **ADALM2000 Lab Activity 10,** :doc:`Shunt Bandgap reference </wiki-migration/university/courses/electronics/electronics-lab-10>`

14.4 Buried (sub-surface) Zener References
------------------------------------------

In terms of the design approaches used within the reference core, the two most popular basic types of IC references consist of the bandgap and buried zener approaches. Bandgaps have been discussed, but zener based references warrant some further discussion.

In an IC chip, surface operated diode junction breakdown is prone to crystal imperfections and other contamination, thus zener diodes formed at the surface are more noisy and less stable than are buried (or sub-surface) ones (see figure 14.17). Analog Devices' zener-based IC references employ the much preferred buried zener. This improves substantially upon the noise and drift of surface-mode operated zeners (see Reference 4).

Buried zener references offer very low temperature drift, down to the 1-2 ppm/°C (AD588 and AD586), and the lowest noise as a percent of full-scale, i.e., 100 nV/√Hz or less. On the downside, the operating current of zener type references is usually relatively high, typically on the order of several mA. The zener voltage is also relatively high, typically on the order of 5V. This limit it's application in low voltage circuits. A block diagram of the AD586 is shown in Figure 15.8.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 14.17: Simple Surface Zener vs. a Buried Zener


.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_f13.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 14.18: Typical Buried Zener Reference (AD586)


An important general point arises when comparing noise performance of different references. The best way to do this is to compare the ratio of the noise (within a given bandwidth) to the dc output voltage. For example, a 10 V reference with a 100 nV/ sqrt Hz noise density is 6 dB more quiet in relative terms than is a 5 V reference with the same noise level.

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-13>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-15>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_e4.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_e5.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_e9.png
   :width: 150px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr14_e10.png
   :width: 150px
