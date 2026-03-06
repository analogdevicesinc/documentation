Chapter 2: Introduction and Chapter Objectives
==============================================

2.1 The Ideal Voltage Feedback Op Amp
-------------------------------------

The operational amplifier (op amp) is one of the basic building blocks of linear design. In its basic form it consists of two input terminals, one of which inverts the phase of the signal, the other preserves the phase, and an output terminal. The standard symbol for the op amp is shown in figure 2.1. This ignores the two power supply terminals, which are obviously required for operation. Op amps are often divided into two types, those that use both a positive and negative power supply and those that use only a single, usually positive power supply. Since all op amps have only two supply pins this distinction is often unnecessary.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2.1: Standard Op Amp Symbol


The name "op amp" is the standard abbreviation for operational amplifier. This name comes from the early days of amplifier design, when the op amp was used in analog computers. (Yes, the first computers were analog in nature, rather than digital). When the basic amplifier was used with a few added external components, various mathematical "operations" could be performed, such as addition, subtraction, integration, etc. One of the primary uses of analog computers was during World War II, when they were used for plotting ballistic trajectories.

**After completing this chapter you should be able to:**

-   List the properties of the ideal voltage feedback op amp
-   Draw the Inverting and Non-Inverting configurations
-   Derive the gain equations for the Inverting and Non-Inverting configurations
-   Draw the inverting summing amplifier configuration
-   Draw the op amp differential gain configuration
-   Derive the gain equations for the Instrumentation Amplifier configuration

2.2 Ideal Voltage Feedback (VFB) Model
--------------------------------------

The most basic model of the ideal voltage feedback op amp has the following characteristics:

-   Infinite input impedance
-   Infinite bandwidth
-   Infinite voltage gain
-   Zero output impedance
-   Zero power consumption

None of these can be actually realized, of course. How close a real implementation comes to these ideals determines the quality of the op amp. Since not all of these ideal characteristics can be maximized at the same time many real op amp designs trade one or more characteristics for the others. This is referred to as the voltage feedback model. This type of op amp comprises nearly all op amps below 10 MHz bandwidth and on the order of 90% of those with higher bandwidths. Another type of op amp architecture is Current Feedback and is discussed in a separate chapter.

The attributes of an ideal VFB op amp are summarized in figure 2.2.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2.2: The Attributes of an Ideal Voltage Feedback Op Amp


2.3 Basic Operation
-------------------

The basic operation of the ideal op amp can be easily summarized. First, we assume that there is a portion of the output that is fed back to the inverting terminal to establish the fixed gain for the amplifier. This is negative feedback. Any differential voltage across the input terminals of the op amp is multiplied by the amplifier's open loop gain which is infinite for the ideal op amp. If the magnitude of this differential voltage is more positive on the inverting (-) terminal than on the non-inverting (+) terminal, the output will swing toward the negative supply. If the magnitude of the differential voltage is more positive on the non-inverting (+) terminal than on the inverting (-) terminal, the output voltage will swing toward the positive supply. The infinite open loop gain of the amplifier along with the external negative feedback will attempt to force the differential input voltage to zero. As long as the inputs and output stays in the operational range of the amplifier, typically bounded by the positive and negative power supply voltages, it will keep the differential input voltage at zero, and the output will be the input voltage multiplied by the gain determined by the feedback network. Note that the output responds to differential-mode voltage and not the common-mode input voltage.

2.4 Inverting and Non-inverting Configurations
----------------------------------------------

There are two basic ways to configure the ideal voltage feedback op amp as an amplifier. These are shown in figure 2.3 and figure 2.4.

Figure 2.3 shows what is known as the inverting configuration. With this circuit, the output is 180º out of phase with the input. The signal gain of this circuit is determined by the ratio of the resistors used and is given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e1.png
   :align: center
   :width: 120px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2.3: Inverting Mode Op Amp Stage


In the figure the inverting (-) input terminal is referred to as the Summing Junction. Since the inputs to the op amp have infinite impedance and thus no current will flow in them, the sum of the current from the input in R\ :sub:`G` and the current from the output in R\ :sub:`F` must be zero. If we suppose that a second resistor (R\ :sub:`G2`) were to be connected from a second input voltage (V\ :sub:`IN2`) to the summing junction, then the current in R\ :sub:`F` would be equal to the sum of the two input currents in R\ :sub:`G`\ and this new R\ :sub:`G2`.

The input impedance, as always, is the impedance to ground for an input signal. The //- //input is at the same voltage as the + input which is ground. We can thus consider the - input to be at what is referred to as virtual ground. The input impedance for the overall amplifier will be simply R\ :sub:`G`:

:math:`Zin = R_G`

Figure 2.4 shows what is known as the non-inverting configuration. With this circuit the output is in phase with the input. The signal gain of the circuit is also determined by the ratio of the resistors used and is given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e2.png
   :align: center
   :width: 120px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2.4: Non-Inverting Mode Op Amp Stage


Note that since the output drives a voltage divider (the gain-setting network) the maximum voltage available at the inverting terminal is the full output voltage, when the circuit is configured for a minimum gain of 1 (R\ :sub:`G` = ∞).

The input impedance, as always, is the impedance to ground for an input signal. Since no current can flow into or out of the //+ //input, the input impedance is infinite:

:math:`Zin = infty`

Also note that in both inverting and non-inverting configurations the feedback is from the output to the inverting terminal. This is negative feedback and has many advantages for the designer. These will be discussed more in detail.

It should also be noted that the gain is based on the ratio of the resistors, not their actual values. This means that the designer can choose from a wide range of values, within certain practical limits.

However, if the values of the resistors are too low, a great deal of current is required from the op amp output for proper operation. This causes excessive power dissipation in the op amp itself, which has many disadvantages. The increased dissipation leads to self-heating of the integrated circuit, which can cause a change in the dc characteristics of the op amp itself. Also, the heat generated can eventually cause the junction temperature to rise above 150º C, the commonly accepted maximum limit for most semiconductors. The junction temperature is the temperature at the silicon chip itself. On the other end of the spectrum, if the resistor values are too high, there is an increase in noise and the susceptibility to parasitic capacitances, which can limit bandwidth and possibly cause instability and oscillation.

From a practical sense, resistors below 10 Ω and above 1 MegΩ are more difficult to produce, especially if precision resistors are required.

2.5 Inverting Op Amp Gain Derivation
------------------------------------

Let us look at the case of an inverting amp in a little more detail. Referring to figure 2.5, the non-inverting terminal is connected to ground. We are assuming a bipolar (both positive and negative) power supply. Since the op amp will force the differential voltage across the inputs to zero, the inverting input will also appear to be at ground. In fact, this node is often referred to as a virtual ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2.5: Inverting Amplifier Gain


If there is a voltage V\ :sub:`IN` applied to the input resistor, It will set up a current I\ :sub:`1` through the resistor R\ :sub:`G` so that:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e3.png
   :align: center
   :width: 120px

Since the input impedance of the ideal op amp is infinite, no current will flow into the inverting input. Therefore, this same current I\ :sub:`1` must flow through the feedback resistor R\ :sub:`F` (I\ :sub:`2` = I\ :sub:`1`). Since infinite open loop gain of the amplifier will force the difference between the inverting terminal and the non-inverting terminal to zero, the output will assume a voltage V\ :sub:`OUT` such that:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e4.png
   :align: center
   :width: 120px

Doing some simple arithmetic we then can come to the conclusion that:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e5.png
   :align: center
   :width: 140px

2.6 Non-inverting Op Amp Gain Derivation
----------------------------------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2.6: Non-Inverting Amplifier gain


Now we examine the non-inverting case in more detail. Referring to figure 2.6, the input voltage is applied to the non-inverting terminal. The output voltage drives a voltage divider consisting of R\ :sub:`F` and R\ :sub:`G`. The voltage at the inverting terminal V\ :sub:`A`, which is at the junction of the two resistors, is equal to:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e6.png
   :align: center
   :width: 140px

The negative feedback action of the op amp will force the differential voltage to 0, so:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e7.png
   :align: center
   :width: 100px

Applying a little simple arithmetic we obtain:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e8.png
   :align: center
   :width: 200px

which is what we specified in figure 2.3

In all of the discussions above, we referred to the gain setting components as resistors. In fact, they are impedances, not just resistances. This allows us to build frequency dependent amplifiers and will be covered in more detail in later chapters.

2.7 Inverting Summing Op Amp Stage
----------------------------------

Multiple input voltages can be summed by the addition of multiple input resistors to the simple inverting op amp configuration as shown in figure 2.7.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2.7: Summing Amplifier


.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e9.png
   :align: center
   :width: 220px

If all the input resistors R\ :sub:`1`, R\ :sub:`2`, ... R\ :sub:`n` are equal but not equal to R\ :sub:`f` then from the equation we can see that it can be simplified such that the output will be equal to the algebraic sum of the inputs times a common gain factor of -R\ :sub:`f`/R\ :sub:`1`. If all the resistors are made equal including R\ :sub:`f` then the output will be simply the negative sum of the inputs.

| **ADALM1000 Lab Activity 1.** :doc:`Simple Op Amps </wiki-migration/university/courses/alm1k/alm-lab-1>`
| **ADALM2000 Lab Activity 1.** :doc:`Simple Op Amps </wiki-migration/university/courses/electronics/electronics-lab-1>`
| **ADALM1000 Lab Activity** :doc:`Summing Amplifier </wiki-migration/university/courses/alm1k/alm-lab-vectrosumamp>`

2.8 The Differential Op Amp Stage
---------------------------------

The op amp differential gain stage (also known as a differential amplifier, or subtractor) is shown in figure 2.7.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2.8: The differential amplifier stage (subtractor)


Paired input and feedback network resistances set the gain of this stage. These resistors, R\ :sub:`F`-R\ :sub:`G` and R\ :sub:`F`'-R\ :sub:`G`', must be matched as noted, for proper operation. Calculation of individual gains for inputs V\ :sub:`1` and V\ :sub:`2` and their linear combination derives the stage gain.

Note that the stage is intended to amplify the difference of voltages V\ :sub:`1`\ and V\ :sub:`2`, so the net input is V\ :sub:`IN` = V\ :sub:`1` - V\ :sub:`2` . The general gain expression is then:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e10.png
   :align: center
   :width: 150px

For an ideal op amp and the resistor ratios matched as noted, the gain of this differential stage from V\ :sub:`IN` to V\ :sub:`OUT` is:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e11.png
   :align: center
   :width: 100px

The great fundamental utility that an op amp stage such as this allows is the property of rejecting voltages common to V\ :sub:`1` -V\ :sub:`2`, i.e., common-mode (CM) voltages. For example, if noise voltages appear between grounds G\ :sub:`1` and G\ :sub:`2`, the noise will be suppressed by the common-mode rejection (CMR) of the differential amp. The CMR is however only as good as the matching of the resistor ratios allows, so in practical terms it implies precisely trimmed resistor ratios are necessary.

A disadvantage of this stage is that the resistor networks load the V\ :sub:`1`-V\ :sub:`2` sources, potentially leading to additional errors if the driving impedance is not low compared to R\ :sub:`G`. A solution to this problem is to insert unity gain (non-inverting) follower stages before the input resistors as shown in figure 2.8.1

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f9.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2.8.1: Buffered differential amplifier stage


| **ADALM1000 Lab Activity** :doc:`Difference Amplifier </wiki-migration/university/courses/alm1k/alm-lab-diffamp>`
| **ADALM1000 Lab Activity** :doc:`Current Sensing Difference Amplifier </wiki-migration/university/courses/alm1k/alm-lab-current-sense>`

2.9 The Instrumentation Amplifier
---------------------------------

Instrumentation Amplifiers are high gain differential amplifiers with high input impedance and a single ended output. They are mainly used to amplify very small differential signals from certain kinds of transducers or sensors such as strain gauges, thermocouples or current sensing resistors in motor control systems. They also have very good common mode rejection (zero output when V\ :sub:`1` = V\ :sub:`2`) in excess of 100dB at DC. A typical example of an instrumentation amplifier with a high input impedance (Zin) is shown in figure 2.9. As you can see it is very similar to the configuration of figure 2.8.1 but with the two input buffers now serving as non-inverting gain stages.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f10.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2.9 High Input impedance Instrumentation Amplifier


The negative feedback of the top op amp causes the voltage at the negative input of amplifier A\ :sub:`1` to be equal to the input voltage V\ :sub:`1`. Likewise, the voltage at the negative input of A\ :sub:`2` is equal to the value of V\ :sub:`2`. This produces a voltage drop across R\ :sub:`1` which is equal to the voltage difference between V\ :sub:`1` and V\ :sub:`2`. This voltage drop causes a current to flow through R\ :sub:`1`, and as the two inputs of the buffer op-amps draw no current, the same amount of current flowing through R\ :sub:`1` must also be flowing through the two resistors R\ :sub:`2`. This then produces a voltage drop between points V\ :sub:`a` and V\ :sub:`b`\ equal to:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e12.png
   :align: center
   :width: 200px

This voltage drop between points V\ :sub:`a` and V\ :sub:`b` is connected to the inputs of the differential amplifier which amplifies it by a gain of 1 (assuming that all the "R" resistors are of equal value). Then we have a general expression for overall voltage gain of the instrumentation amplifier circuit as:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e13.png
   :align: center
   :width: 280px

To change the differential gain of the circuit we simply change the value of R\ :sub:`1`. An instrumentation amplifier can also be made from two op amps; this is shown in figure 2.10.

**<fs large>R\ 1 = R\ 4 (matched)
R\ 2 = R\ 3 (matched)
Gain = 1 + R\ 1/R\ 2\ </fs>**

This assumes Vin- and Vin+ are referenced to Vcc/2 in the case of single supply op amps.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f11.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2.10: Instrumentation amplifier using two Op Amps


However, this topology is not as desirable because the first op amp is operated at less than unity gain, so it may be unstable. In addition, the signal path from Vin- to the output has a longer propagation delay than the signal path from Vin+ to the output. This can lead to less than the exact difference for the highest output frequencies at the bandwidth limits of the amplifiers.

Section Summary
~~~~~~~~~~~~~~~

The basic model of the ideal voltage feedback op amp has the following characteristics:

-   Infinite input impedance
-   Infinite bandwidth
-   Infinite voltage gain
-   Zero output impedance
-   Zero power consumption

The gain equation for the inverting configuration is given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e5.png
   :align: center
   :width: 150px

The gain equation for the non-inverting configuration is given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e8.png
   :align: center
   :width: 250px

The gain equation for the three op amp instrumentation amplifier configuration is given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e13.png
   :align: center
   :width: 250px

2.10 Integration and differentiation
------------------------------------

By introducing a reactance into the feedback loop of an op-amp amplifier circuit rather than a pure resistance, we can make an output that responds to changes in the input voltage over time. The two circuits we will be exploring derive their names from their respective calculus functions, the integrator produces a voltage output proportional to the product (multiplication) of the input voltage and time; and the differentiator (not to be confused with the differential amplifier we just covered) produces a voltage output proportional to the input voltage's rate of change.

2.10.1 The Ideal Inverting Integrator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An integrator is a circuit which has an output voltage that is proportional to the time integral of its input voltage. Figure 2.11 shows the configuration of an ideal op amp integrator. The circuit is similar to the inverting amplifier in figure 2.3 with the exception that resistor R\ :sub:`F` is replaced by a capacitor. The voltage gain transfer function is obtained from the equation we derived in section 2.5 by replacing R\ :sub:`F` with the complex impedance of the capacitor C to obtain:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e17.png
   :align: center
   :width: 300px

Remembering that division by s in the complex frequency domain is equivalent to an integration in the time domain, it follows from this equation that the time domain output voltage is given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e18.png
   :align: center
   :width: 300px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2.11 Inverting integrator


Thus the circuit has the transfer function of an inverting integrator with the gain constant 1/RC. Because RC has the units of seconds, it is called the integrator time constant. The input resistance to the circuit is R. The output resistance is zero.

Note that this configuration can also be viewed as a low-pass filter. It is a filter with a single pole at DC (i.e., where angular frequency ? = 0 radians).

There are several potential problems with this circuit. It is usually assumed that the input V\ :sub:`in` has zero DC component (i.e., has a zero average value). Otherwise, unless the capacitor is periodically discharged, the output will drift outside of the operational amplifier's operating range. Even when V\ :sub:`in` has no offset, the leakage or bias currents into the operational amplifier inputs can add an unexpected offset voltage to V\ :sub:`in` that causes the output to drift off in one or the other direction toward a supply rail. Balancing input currents and replacing the non-inverting (+) short-circuit to ground with a resistor with resistance R can reduce the severity of this problem.

Because this circuit provides no DC feedback (i.e., the capacitor appears like an open circuit to signals with ? = 0), the offset of the output may not agree with expectations (i.e., V\ :sub:`initial` may be out of the designer's control with the present circuit).

Many of these problems can be made less severe by adding a large resistor R\ :sub:`F` ( greater than 1 megaohm for example) in parallel with the feedback capacitor. At significantly high frequencies, this resistor will have negligible effect. However, at low frequencies where there are drift and offset problems, the resistor provides the necessary DC feedback to hold the output steady at the correct value. In effect, this resistor reduces the DC gain of the "integrator", it goes from infinite to some finite value R\ :sub:`F`/R.

To illustrate the operation of this integrator circuit we simulated the circuit with the input resistor R = 2.5 KΩ and the feedback capacitor C = 0.1µF. The input voltage V\ :sub:`in`, shown in green in figure 2.12 is a -1 volt to +1 volt square wave with a 1mSec period ( high for 500 µSec and low for 500 µSec). The integrator output voltage V\ :sub:`out` is shown in blue in figure 2.12. The simulation starts when the output voltage is zero and thus the voltage across the capacitor, C is also zero (V\ :sub:`initial` = 0). As we can see the output waveform is a triangle wave with a slope determined by the integrator time constant RC and V\ :sub:`in`. The RC time constant (250 mSec) was chosen such that given the -1 to +1 volt input V\ :sub:`in` the output will ramp up and down 2 volts in each of the 500 mSec half cycles of the input square wave.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f13.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2.12 Ideal integrator simulation


The negative input terminal of the op amp is also plotted (V\ :sub:`sumjnc` red waveform) in figure 2.12. It is at 0 volts as it should be. The "constant" +/- 1 volt V\ :sub:`in` appears across the input resistor making a "constant" current flow in the feedback capacitor. We get a linearly changing voltage across the capacitor because we know that the time rate of change of the voltage on a capacitor is linearly proportional to the current.

2.10.2 The Ideal Differentiator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A differentiator is a circuit which has an output voltage that is proportional to the time derivative of its input voltage. Figure 2.13 shows the configuration of an op amp differentiator. The circuit is similar to the inverting amplifier in figure 2.3 with the exception that resistor R\ :sub:`G` is replaced by a capacitor. It follows that the gain equation we derived in section 2.5 can be used to solve for the voltage gain transfer function of the differentiator by replacing R\ :sub:`G` with the complex impedance of the capacitor. The voltage gain transfer function is given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e14.png
   :align: center
   :width: 300px

Again remembering that multiplication by s in the complex frequency domain is equivalent to a differentiation in the time domain, it follows from the above equation that the time domain output voltage is given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e15.png
   :align: center
   :width: 230px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f14.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2.13 Inverting differentiator


Thus the circuit has the transfer function of an inverting differentiator with the gain constant RC. Because the gain constant has the units of seconds, it is called the differentiator time constant. The output resistance of the circuit is zero. The input impedance transfer function is that of the capacitor C to virtual ground given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-e16.png
   :align: center
   :width: 150px

With s = jω, it follows that \|Zin\| --> 0 as ω becomes large. This is a disadvantage because a low input impedance can cause large currents to flow in the input circuit. Often this differentiator is modified by inserting some relatively small resistance in series with the input capacitor.

Note that this configuration can also be viewed as a high-pass filter. It is a filter with a single zero at DC (i.e., where angular frequency ω = 0 radians). The high-pass characteristics of a differentiating amplifier (i.e., the low-frequency zero) can lead to stability challenges when the circuit is used in an analog servo loop (e.g., in a PID controller with a significant derivative gain). In particular, as a root locus analysis would show, increasing feedback gain will drive a closed-loop pole toward marginal stability at the DC zero introduced by the differentiator.

To illustrate the operation of this differentiator circuit we simulated the circuit with the feedback resistor R = 2.5 KΩ and the input capacitor C = 0.1µF. The input voltage V\ :sub:`in`, shown in green in figure 2.14 is a -1 volt to +1 volt triangle wave with a 1mSec period ( ramp up for 500 µSec and ramp down for 500 µSec). The differentiator output voltage V\ :sub:`out` is shown in blue in figure 2.14. The simulation starts when the input voltage is zero and thus the voltage across the capacitor, C is also zero (V\ :sub:`initial` = 0). As we can see the output waveform is a square wave with an amplitude determined by the differentiator time constant RC and the slope (volts/sec) of V\ :sub:`in`. The RC time constant (250 mSec) was chosen such that given the -1 to +1 volt ramp of input V\ :sub:`in` the output will be + and - 1volt for each of the 500 mSec half cycles of the input square wave.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr2-f15.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2.14 Ideal differentiator simulation


The negative input terminal of the op amp is also plotted (V\ :sub:`sumjnc` red waveform) in figure 2.14. It is at 0 volts as it should be. The linear +/- 1 volt ramp from V\ :sub:`in` appears across the input capacitor. We know that the time rate of change of the voltage on a capacitor is linearly proportional to the current thus making a "constant" current flow in the feedback resistor and we get a constant voltage on the output.

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-1>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-3>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`
