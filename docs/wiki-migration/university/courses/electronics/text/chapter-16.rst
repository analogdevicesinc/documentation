Chapter 16: Advanced Amplifier topics:
======================================

In this chapter we will explore a few circuit techniques involving multiple transistors that are beyond the basic configurations we discussed in earlier chapters.

16.1 Improvements to the emitter follower
-----------------------------------------

The incremental voltage gain, A\ :sub:`V`, (V\ :sub:`OUT` / V\ :sub:`IN`) of the emitter follower should ideally be 1 but will always be slightly less than 1. The gain is generally given by the following equation:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_e1.png
   :align: center
   :width: 120px

From the equation we can see that in order to obtain a gain close to one we can either increase R\ :sub:`L` or decrease r\ :sub:`e`. We also know that r\ :sub:`e` is a function of I\ :sub:`E` and that as I\ :sub:`E` increases r\ :sub:`e` decreases. Also from the circuit, figure 16.1(a) we can see that I\ :sub:`E` is related to R\ :sub:`L` and that as R\ :sub:`L` increases I\ :sub:`E` decreases for a fixed supply voltage. These two effects work counter to each other in the simple resistively loaded emitter follower. Thus to optimize the gain of the follower we need to explore ways to either decrease r\ :sub:`e` or increase R\ :sub:`L` without effecting the other.

Looking at the follower in another way, because of the inherent DC shift due to the transistor's V\ :sub:`BE`, the difference between input and output should be constant over the intended signal swing. Due to the simple resistive load R\ :sub:`L`\ in figure 16.1(a), the emitter current I\ :sub:`E` increases and decreases as the output swings up and down. We know that V\ :sub:`BE` is an exponential function of I\ :sub:`E` and will change approximately 18 mV (at room temperature) for a factor of 2 change in I\ :sub:`E`. Given R\ :sub:`L` = 2.2KΩ and a +/- 2V swing and an 8V total supply voltage, ( V+ = +4V and V- = -4V ), the minimum I\ :sub:`E`\ = 2V/2.2KΩ or 0.91 mA and the maximum I\ :sub:`E`\ = 6V/2.2KΩ or 2.7 mA. This results in a difference of 1.8 mA and results in a 28 mV change in V\ :sub:`BE`. This observation leads us to the first possible improvement in the emitter follower shown in figure 16.1(b).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 16.1 Emitter follower with current source load.


The current mirror from chapter 11 can be substituted for the emitter load resistor to supply a fixed emitter current to the amplifier transistor, figure 16.1(b). A current mirror will sink a more or less constant current over a wide range of voltages. Ignoring any current in an external load on V\ :sub:`OUT`, this more or less constant current flowing in transistor Q\ :sub:`1` will result in a more or less constant V\ :sub:`BE`.

Viewed another way, the very high output resistance of the current source has effectively increased R\ :sub:`L` while r\ :sub:`e` remains at a low value set by the current I\ :sub:`E`. We saw in Chapter section 11.5.3 on the output resistance of the current mirror that the use of emitter degeneration resistors can greatly increase r\ :sub:`O`\ beyond that set by the transistor's Early voltage V\ :sub:`A`.

16.2 Complementary Feedback Pair Emitter Follower
-------------------------------------------------

An alternate approach to improving the emitter follower is to reduce the effective r\ :sub:`e` through negative feedback. Reducing r\ :sub:`e` can be addressed by adding a second transistor to increase the negative feedback factor by increasing the open-loop-gain. The single transistor is replaced by a pair of transistors with 100% voltage feedback to the emitter of the first transistor. This is often referred to as a complementary feedback pair as shown in figure 16.2.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 16.2 Complementary Feedback Pair Emitter Follower


The value of R\ :sub:`1` is crucial to good linearity, as it sets the I\ :sub:`C` of transistor Q\ :sub:`1`. The collector current of Q\ :sub:`1` will be approximately equal to the V\ :sub:`BE` of Q\ :sub:`2` divided by R\ :sub:`1`. This current in Q\ :sub:`1` will be relatively more constant than the current in R\ :sub:`L`. The majority of the variable current in R\ :sub:`L` (as V\ :sub:`OUT` changes) will flow in Q\ :sub:`2` rather than Q\ :sub:`1`. Resistor R\ :sub:`L` can of course be additionally replaced with a constant current source as a further improvement as we just saw in section 16.1.

An important consequence of adding the complementary transistor Q\ :sub:`2` is that it further limits the maximum positive output swing. In the simple emitter follower of figure 16.1(a) the output can swing no higher than V+ - V\ :sub:`BEQ1`. Whereas the output of the follower in figure 16.2 can swing no higher than V+ - V\ :sub:`BEQ1` - V\ :sub:`BEQ2` and have the collector base junctions of the transistors remain reverse biased.

16.2.1 FET Source Followers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is important to note that the gain equation for FET based source followers is much the same as for BJT based followers substituting the small signal source resistance r\ :sub:`s`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_e2.png
   :align: center
   :width: 125px

We also know that the small signal source resistance is a function of the DC drain current I\ :sub:`D` so using these same circuit techniques to keep I\ :sub:`D` more constant with changes in the load current will improve the performance of FET based followers as well.

16.2.2 The Body effect
~~~~~~~~~~~~~~~~~~~~~~

All MOS transistors have a fourth terminal which must be considered when designing circuits that use these devices. An additional effect that limits the gain accuracy of a FET based source follower comes from possible changes in the voltage on this fourth terminal, often called the body or back-gate, in cases where the body or substrate is connected to the fixed negative power supply ( for NMOS devices or positive supply for PMOS devices ) rather than the source.

The body effect refers to the change in the threshold voltage, V\ :sub:`th`, by the change in V\ :sub:`SB`, the source to back-gate voltage. Because the voltage on the back-gate influences the threshold voltage (when it is not tied to the source), it can be thought of as a second gate. The body effect is sometimes called the "back-gate effect".

For an enhancement mode, NMOS device the body effect upon threshold voltage is calculated by applying the Shichman-Hodges model using the following equation:

:math:`V_TB=V_TO +\\gamma (\sqrt {V_SB + 2\\phi _F}-\sqrt {2\\phi _F})`

| Where:
| V\ :sub:`TB` is the threshold voltage when substrate bias is present,
| V\ :sub:`SB` is the source-to-body substrate bias
| 2f\ :sub:`F` is the surface potential
| V\ :sub:`TO` is threshold voltage for zero substrate bias

The body effect parameter:

:math:`\displaystyle \\gamma = \frac{t_ox}{\\epsilon _ox} \sqrt {2q\\epsilon _si N_A}`

| Where:
| t\ :sub:`ox` is oxide thickness
| ε\ :sub:`ox` is oxide permittivity
| ε\ :sub:`si` is the permittivity of silicon
| N\ :sub:`A` is a doping concentration
| q is the charge of an electron

16.3 Improved series voltage regulator
--------------------------------------

Back in chapter 6 we briefly looked at the zener diode as a shunt regulator figure 16.3(a). If we incorporate an emitter follower transistor stage in place of the series resistor we can greatly improve the load regulation performance of the regulator. Adding an emitter follower stage to the simple Zener regulator as shown in figure 16.3(b) forms a simple series voltage regulator and substantially improves the regulation of the circuit. Here, the load current I\ :sub:`RL` is supplied by the transistor whose base is now connected to the Zener diode. Thus the transistor's base current (I\ :sub:`B`) is the only variable current flowing in the Zener diode and is smaller than the current through R\ :sub:`L` by the ß or current gain of the emitter follower. This regulator is classified as "series" because the regulating element, the transistor, appears in series with the load. R\ :sub:`1` sets the Zener current (I\ :sub:`Z`) and is determined as:

:math:`\displaystyle R_1=\frac{V_S-V_Z}{I_Z+KI_B }`

where, V\ :sub:`Z` is the Zener voltage, I\ :sub:`B` is the transistor's base current and K is a scaling factor of 1.2 to 2 to ensure that R\ :sub:`1` is low enough for the maximum I\ :sub:`B` under heavy output load currents.

:math:`I_B=I_L/ß`

| where:
| I\ :sub:`L` is the required load current, also the transistor's emitter current (assumed to be approximately equal to the collector current)
| ß\ :sub:`(min)` is the minimum acceptable DC current gain for the transistor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 16.3.1 Improved zener voltage regulator


This circuit has much better load regulation than the simple Zener shunt regulator, since the base current of the transistor forms a very light load on the Zener, thereby minimizing variation in the Zener voltage due to variation in the load. It is also useful to note here that the output voltage would now be about 0.65V less than V\ :sub:`Z` due to the transistor's V\ :sub:`BE` drop if we did not include the extra diode D\ :sub:`1` in series with the zener. The voltage drop across D\ :sub:`1` can be thought to be approximately the same as the V\ :sub:`BE` of Q\ :sub:`1`. A second diode connected NPN transistor similar to Q\ :sub:`1` used in place of D\ :sub:`1` would provide a better approximation. Although this circuit has good regulation, it is still somewhat sensitive to the load and supply variation. This can be further improved by incorporating negative feedback. This simple regulator is often used as a "pre-regulator" in more advanced linear voltage regulator circuits.

The circuit can be made adjustable by adding a variable resistor as a voltage divider across the Zener, moving the transistor base connection from the top of the Zener to the potentiometer wiper. Another way to make the output voltage adjustable in steps is by switching in Zeners with different breakdown voltages.

16.3.1 Transistor based Capacitance multiplier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a related power supply circuit shown in figure 16.3.2 the effective capacitance of capacitor C\ :sub:`1`\ is multiplied by the transistor's current gain (β).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 16.3.2 Transistor based Capacitance multiplier


R\ :sub:`1` and C\ :sub:`1` form a low-pass filter that helps smooth any ripple on V\ :sub:`S`\ such as from a full wave rectifier. R\ :sub:`1` supplies the charging current as well as the transistor's (Q\ :sub:`1`) base current. R\ :sub:`L` is the load on the circuit. Without Q\ :sub:`1`, R\ :sub:`L` would be the load on the capacitor and C\ :sub:`1` would have to be very large to maintain low ripple. With Q\ :sub:`1` in place, the loading imposed upon C\ :sub:`1` is simply the load current reduced by a factor of β. Conversely, C\ :sub:`1` appears "multiplied" by a factor of β to the load.

Note that this circuit is not a voltage regulator, since the output voltage varies directly with the input V\ :sub:`IN`. The output voltage is less than the base voltage by V\ :sub:`BE` (about 0.65V). The Base will be less than V\ :sub:`S` (when loaded) by the base current times R\ :sub:`1`. Larger values of R\ :sub:`1` (and C\ :sub:`1`) reduce the output ripple to almost negligible levels. On the downside this causes the output to rise slowly towards the required value (especially when the load is connected), due to the larger time constant of R\ :sub:`1` and C\ :sub:`1`. However the circuits of figure 16.3.1 and figure 16.3.2 could be combined to provide improved filtering and voltage regulation.

16.3.2 Adding an output current limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A current limiting circuit is an essential element of any power supply. There is always a risk that the load may draw too much current or the power supply rails may even get accidentally shorted. The inclusion of a current limiter circuit will prevent any further damage occurring to the external circuit as well as preventing damage to the power supply itself.

It is possible to implement a power supply current limiter with just diodes, but the one we will be looking at here uses a single transistor and a current sense resistor. This circuit forms the basis of most power supply current limiter designs used today and is commonly used to limit the current in the output stage of operational amplifiers. The limiting circuit consisting of Q\ :sub:`2` and R\ :sub:`2` is incorporated into the simple regulator circuit shown in figure 16.3.3.

The operation of the current limiter is very straightforward. When the power supply is supplying current below the maximum level, current flows through the sense resistor and a small potential difference develops across it. The value of the resistor is chosen so that when the maximum allowable current flows from the power supply, a voltage equal to the V\ :sub:`BE` of the current sense transistor, Q\ :sub:`2`, is developed across it. This is typically 0.6 volts, assuming that a silicon transistor is used.

As the voltage across the current sense resistor approaches 0.6 volts, the current sense transistor starts to turn on. When it does, the voltage at the base of the main power supply pass transistor is pulled down, thereby preventing any increase in the output current of the power supply. In this way it is very easy to calculate the value for the sense resistor using Ohms Law. It is simply V\ :sub:`BE` / I\ :sub:`Lmax`. The current sense transistor, Q\ :sub:`2`, should have a sufficiently large current capacity to be able to take away all the current from the base of the main series pass transistor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 16.3.3 Power supply regulator with feedback and transistor current limiting


In view of the fact that the regulator sense point occurs after the current sense resistor, any voltage drop across the resistor will not affect the output voltage of the circuit as this will be compensated for by the regulator. This assumes that the input supply voltage is sufficiently large enough for the circuit to regulate correctly. In this way the current sense resistor will not cause any reduction in the voltage output from the power supply regulator circuit.

The power supply current limiter circuit is shown within the circuit of a very simple regulator. However it can be placed within most regulator circuits made from discrete components with little change. For circuits using integrated circuit regulators, they are virtually certain to contain current limiter circuitry based around this principle.

16.4 Single Transistor high pass filter
---------------------------------------

It is sometimes desirable to design a simple active high pass filter using a single transistor amplifier stage. The transistor filter circuit shown in figure 16.4 provides a two pole filter with unity gain. This filter is convenient to place in a larger circuit because it contains few components and does not occupy much space.

The active high pass transistor circuit is quite straightforward, using just a total of four resistors, two capacitors and a single transistor. The operating conditions for the transistor are set up in the normal way. R\ :sub:`2` and R\ :sub:`3` are used to set up the bias point for the base of the transistor. The resistor R\ :sub:`L` is the emitter resistor and sets the current for the transistor.

The filter components are included in negative feedback from the output of the circuit to the input. The components that form the active filter network consist of C\ :sub:`1`, C\ :sub:`2`, R\ :sub:`1` and the combination of R\ :sub:`2` and R\ :sub:`3` in parallel, assuming that the input resistance to the emitter follower circuit are very high and can be ignored.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 16.4 Transistor active high pass filter circuit


:math:`C_1 = 2 \times C_2`

:math:`R_1 = R_2 \times R_3 /(R_2 + R_3)`

This is for values where the effect of the emitter follower transistor itself within the high pass filter circuit can be ignored, i.e.:

:math:`R_L (β+1) >> R_2 \times R_3 /(R_2 + R_3 )`

:math:`f_o = 1.414 / (4 π R_1 C_2)`

| Where:
| β = the forward current gain of the transistor
| f\ :sub:`o` = the cut-off frequency of the high pass filter
| π = equal to 3.14159

The equations for determining the component values provide a Butterworth response, which provides maximum flatness within the pass-band at the expense of achieving the ultimate roll off as quickly as possible. This has been chosen because this form of filter suits most applications and the mathematics works out easily.

16.5 Frequency Multiplication
-----------------------------

Frequency Multipliers are a special class of amplifiers that are biased at 3 to 10 times the normal cutoff bias. They are used to generate a frequency that is a multiple (harmonic) of a lower frequency. Such circuits are called frequency multipliers or harmonic generators.

Figure 16.5.1 illustrates a frequency multiplier known as a Frequency Doubler or Second Harmonic Generator. As illustrated, the input is 10 KHz and the output is 20 KHz, or twice the input frequency. In other words, the second harmonic of 10 KHz is 20 KHz. The third harmonic (frequency tripler) would be 30 KHz, or 3 times the input signal. The fourth harmonic (quadruplet) would be 40 KHz, or 4 times the 10 KHz input signal. The fifth harmonic (frequency quintupler) is normally as high in multiplication as is practical, because at harmonics higher than the fifth, the output diminishes to a very weak signal.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 16.5.1, Frequency multiplication using single transistor


Frequency multipliers are operated by the pulses of collector current produced by a class C amplifier. Although the collector current flows in pulses, the alternating collector voltage is sinusoidal because of the action of the tank circuit. With the output tank circuit tuned to the required harmonic, the tank circuit acts as a filter, accepting the desired frequency and rejecting all others.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_e4.png
   :align: center
   :width: 150px

The following circuit, figure 16.5.2, is a better frequency multiplier using an NPN differential amplifier with an LC resonate output load. With the component values shown in the figure, the output level is about 4V p-p at 33 KHz with a 1v p-p, 11 KHz input. Other frequencies and multiplication factors are possible by adjusting the resonate frequency of the L\ :sub:`1`,C\ :sub:`1`\ tank.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr16_f8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 16.5.2, Improved Frequency Multiplier.


Amplitude modulation may be applied to the output frequency by capacitor coupling the modulating (audio) signal to base of current source transistor Q\ :sub:`3`.

Figure 16.5.3 illustrates the waveforms in a typical circuit. You can see that the pulses of collector current are the same frequency as the input signal. These pulses of collector current energize the tank circuit and cause it to oscillate at twice the base signal frequency. Between the pulses of collector current, the tank circuit continues to oscillate. Therefore, the tank circuit receives a current pulse for every other cycle of its output

Figure 16.5.3

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-15>`

**Go to** :adi:`Next Chapter </media/en/training-seminars/design-handbooks/Basic-Linear-Design/Chapter9.pdf>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`
