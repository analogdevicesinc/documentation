Activity: The Wien Bridge Oscillator
====================================

Objective
---------

The objective of this exercise is to understand the operation of a Wien bridge
oscillator, including a thorough understanding of the individual components:

* Frequency selective feedback network
* Gain element
* Gain control

Here is a complete video run-through of the experiment, including theory,
construction, and measurements:

.. video:: https://www.youtube.com/watch?v=-FxNJlDDGIs

Background
The Wien bridge oscillator was originally developed for telephony applications.
The circuits in this exercise are modern adaptations of one described by a
Stanford University student, William R. Hewlett,4 in his 1939 masters thesis
(see Linear Technology Application Note 43, Appendix C, “The Wien Bridge and
Mr. Hewlett”).

Oscillators are circuits that generate periodic waveforms without any input
signal. They generally include some form of amplifier stage like transistors or
OP-AMPs with a feedback network consisting of passive devices such as
resistors, capacitors, or inductors. In order to oscillate, a linear circuit
must satisfy the Barkhausen_stability_criterion, which in simple terms states
that at the frequency of oscillation:

The loop gain is equal to unity in absolute magnitude
The phase shift around the loop is zero or an integer multiple of 2π
Consider the first one, and its consequences in an oscillator: If the loop gain
is less than unity, the oscillations will die out. If the loop gain is greater
than unity, the oscillations will increase in amplitude, either forever (which
is possible in a simulation), or until something limits the amplitude
(hopefully gracefully, and not as the result of a catastrophic failure.) If the
end application is not very sensitive to distortion (output frequencies at
multiples of the desired fundamental frequency), then simple gain limiting
methods can be employed - this could be as simple as allowing the amplifier
output to “clip” at the supply voltage. But if the application requires a
pure sine wave, then carefully controlling the amplifier's gain is absolutely
critical.
There are various feedback elements employed to generate the required
frequency-dependent phase shift - quartz crystals, mechanical resonators, L-C
(inductor-capacitor) networks. The Wien_bridge was developed by Max Wien in
1891, as an extension of the Wheatstone_bridge. Whereas the Wheatstone bridge
consists of purely resistive elements, the Wien bridge can be used to measure
capacitors. While initially intended as a measurement circuit, at balance, the
phase shift of a Wien bridge is zero, so including a gain element with a phase
shift of zero will satisfy one of the Barkhausen criterion.
(It would have been impossible to make an oscillator in 1891 as no linear
electronic gain elements existed - the audion tube was invented in 1906.)
There are several advantages to using a Wien bridge as the feedback element in
an oscillator:

Simplicity
Low distortion
Either the resistances or capacitances can be adjustable
With the phase shift satisfied, the other half of the Barkhausen criterion is a
loop gain of unity. At resonance, the reactive arm of the Wien bridge has an
attenuation of 1/3, so the amplifier must have a gain of 3. The circuit shown
in :numref:`fig-wien_simple` is a simple Wien bridge oscillator with a 1.0kHz
output that illustrates this principle.

.. _fig-wien_simple:

.. figure:: williams_simple_wien_bridge_osc.png
   :align: center
   :width: 600

   1.0kHz Wien Bridge Oscillator


Gain control is achieved with an  incandescent light bulb (as it is in Bill
Hewlett's configuration.) An incandescent bulb's resistance increases with
power dissipation, and as a rough rule of thumb the hot resistance is often
about 10 times the cold resistance. The #327 lamp shown has an operating
voltage of 28V and operating current of 40mA, for a hot resistance of about 700
ohms, and an estimated cold resistance of around 70 ohms. In order to achieve a
non inverting gain of 3, the lamp's resistance must be half of the feedback
resistance, or about 215 ohms.

Once the circuit is oscillating, the amplitude control can be described as
follows:

* If the gain is a little bit less than 3, the lamp cools down, its resistance
  drops, tending to increase the gain.
* If the gain is higher than 3, the lamp heats up, its resistance increases,
  tending to reduce the gain.

Materials
---------

* ADALM2000 (M2K) Active Learning module OR:

  * Two-channel oscilloscope, signal generator, and / or network analyzer
    functionality

* ADALP2000 Parts Kit Items:

  * Solderless Breadboard
  * Jumper Wire Kit
  * 2 – 10nF Capacitor
  * 2 – 1 µF Capacitor
  * 3 – 10 kΩ Resistor
  * 2 – 4.7 kΩ Resistor
  * 1 – 5 kΩ Single-turn potentiometer
  * 2 – 1N4148 Silicon Diode

Directions
----------
Wheatstone Bridge Simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to become familiar with the operation of a bridge circuit, open the
**wheatstone_bridge.asc** LTspice simulation shown in
:numref:`fig-wheatstone_ltspice`.

.. _fig-wheatstone_ltspice:

.. figure:: wheatstone_ltspice.png
   :align: center
   :width: 600

   Wheatstone Bridge Simulation

Note that the bridge is initially unbalanced, and a small, but nonzero voltage
appears at Vcd. (A Voltage-controlled voltage source with a gain of unity is a
convenient way to measure the difference between two nodes such that it appears
in the simulation results.) Experiment with different values for R3, noting
that a value of 10k should balance the bridge and give a zero output. Try
reducing R1 and R2 to 1k - does this have any effect on the output voltage?

AC Wien Bridge Simulation
~~~~~~~~~~~~~~~~~~~~~~~~~

Open the **basic_wein_bridge.asc** LTspice simulation shown in
:numref:`fig-basic_wien_ltspice`. The simulation is set up as an AC sweep from
100Hz to 10kHz, with the result shown in
:numref:`fig-basic_wien_ltspice_result`. (Note that a DC bridge supply would
produce a fairly predictable output - node C would be at ground potential, and
node D would be at 1/3 of the supply.) Run the simulation and probe node C, the
output of the reactive arm of the bridge. Notice the "Gentle" hump in response,
peaking somewhere slightly less than 2kHz. Probe node Vcd next. Notice the
extremely sharp null in response, making it very easy to locate the exact
resonant frequency of 1.59kHz.

.. _fig-basic_wien_ltspice:

.. figure:: basic_wien_ltspice.png
   :align: center
   :width: 400

   Wein Bridge Frequency Response Simulation

.. _fig-basic_wien_ltspice_result:

.. figure:: basic_wien_ltspice_result.png
   :align: center
   :width: 400

   Frequency Response Simulation Result

Simulated Wien Bridge Oscillator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the **wien_bridge_vcvs_gain.asc** LTspice simulation shown in
:numref:`fig-wien_bridge_vcvs_gain`. This is a circuit that is impossible to
build in real-life - the gain stage is essentially perfect - infinite input
impedance, zero output impedance, and no offset or gain error. But it allows us
to experiment with ideal cases, to gain some intuition into the Barkhausen
criterion and test out some assertions made in the background information.

.. _fig-wien_bridge_vcvs_gain:

.. figure:: wien_bridge_vcvs_gain.png
   :align: center
   :width: 400

   Wien Bridge Oscillator with Ideal Gain Stage

Ignoring V1 for the moment, note that when this simulation is started, all
voltages are zero. There is no reason for it to do anything other than stay at
zero forever. V1 is there to "kick" the circuit into operation by providing a
step to the gain stage when the simulation is first started, then it ramps back
to zero and has no further effect on the circuit's operation.
Run the simulation, and probe the output node. Results should look similar to
:numref:`fig-wien_bridge_vcvs_g_2p97`.

.. _fig-wien_bridge_vcvs_g_2p97:

.. figure:: wien_bridge_vcvs_g_2p97.png
   :align: center
   :width: 400

   Ideal Wien Oscillator, G=2.97

Note that the circuit oscillates a for a few milliseconds, but the amplitude
exponentially decays to zero. This is because the gain is set 1% too low (as
you might expect if you built an amplifier with 1% resistors.) Next, set the
value for E2 to 2.997, or about 0.1% too low, as shown in
:numref:`fig-wien_bridge_vcvs_g_2p997`. Oscillations continue longer, but still
decay.

.. _fig-wien_bridge_vcvs_g_2p997:

.. figure:: wien_bridge_vcvs_g_2p997.png
   :align: center
   :width: 400

   Ideal Wien Oscillator, G=2.997

Since we know that the gain needs to be exactly 3 to sustain oscillation, set
the gain to 3.0 as shown in :numref:`fig-wien_bridge_vcvs_g_3p0` and run the
simulation.

.. _fig-wien_bridge_vcvs_g_3p0:

.. figure:: wien_bridge_vcvs_g_3p0.png
   :align: center
   :width: 400

   Ideal Wien Oscillator, G=3.0

Notice that the operation is exactly as predicted, with a steady amplitude for
the entire 250ms simulation time. This would never happen in real life, or even
with simulations using a model of a real amplifier - the finite gain, finite
input impedance, would cause the gain to be slightly more or less than 3.

As a final illustration that simulations can model situations that would be
impossible in the real world, set the gain to 3.03 (1% too high) as shown in
:numref:`fig-wien_bridge_vcvs_g_3p03` and run the simulation.

.. _fig-wien_bridge_vcvs_g_3p03:

.. figure:: wien_bridge_vcvs_g_3p03.png
   :align: center
   :width: 400

   Ideal Wien Oscillator, G=3.03

The output amplitude hits 15 **TERAVOLTS** after 250ms, with no end in sight.
Again, this simulation is only to build intuition about the Barkhausen
criterion and has no basis in reality. If you were to build this circuit with
an op-amp configured with a gain of 3.03 and powered by +/-5V, oscillations
would build until they approached 5V amplitude, then simply "clip" (producing a
distorted waveform).

Complete Wien Bridge Oscillator
-------------------------------------------------------------------------------

The circuit shown in :numref:`fig-wien_bridge_osc_complete_ltspice` is a
complete (and practical) Wein bridge oscillator circuit that can be built on a
breadboard and run as a simulation (**wien_bridge_osc_complete.asc**). Rather
than using an incandescent bulb (which has a positive coefficient of
resistance) for the amplifier's input resistor, this circuit shunts part of the
feedback resistance with diodes, which have a negative coefficient of
resistance. Ignoring the diodes, the gain would be 1+(10k+4.7k)/(4.7k+2k)), or
about 3.19. But as the voltage across D1 and D2 approaches 600mV or so, the
effective resistance of R2 is reduced, dropping the gain.

.. _fig-wien_bridge_osc_complete_ltspice:

.. figure:: wien_bridge_osc_complete_ltspice.png
   :align: center
   :width: 600

   Complete, Practical Wien Bridge Oscillator

Run the simulation; the output should resemble
:numref:`fig-wien_bridge_osc_complete_result`. The "kick" circuit is not
necessary to get the simulation to start... eventually. But the amplifier's
offset in the model is quite low, so the kick helps the simulation start up
much faster. Startup time is also a concern in some real-world applications,
and circuits similar to V3, such as a pulse generator made from logic gates can
be employed. Experiment with different values for vkick (including zero).

.. _fig-wien_bridge_osc_complete_result:

.. figure:: wien_bridge_osc_complete_result.png
   :align: center
   :width: 400

   Wien Bridge Oscillator Simulation Result

Next, construct the circuit as shown in :numref:`fig-wien_bridge_layout`.

**To Do:** Needs Update - V- not connected

.. _fig-wien_bridge_layout:

.. figure:: wien_bridge_layout.jpg
   :align: center
   :width: 800

   Complete Wien Bridge Oscillator


Note that R5 is a potentiometer, allowing the gain of the circuit to be "dialed
in" to where oscillation just starts. Measure the output with Scopy's
oscilloscope, results should be similar to
:numref:`fig-wien_bridge_osc_complete_scopy`.


**To Do:** Take nicer Scopyshot

.. _fig-wien_bridge_osc_complete_scopy:

.. figure:: wien_bridge_osc_complete_scopy.png
   :align: center
   :width: 600

   Wien Bridge Oscillator Measured Output

** To Do:** Frequency Domain measurements, Distortion vs. potentiometer setting

Questions:

What is the relationship between the gain control elements and distortion?


**Resources:**
  * Fritzing files: (To Do)
  * `Wien Bridge Lab LTspice files <https://analogdevicesinc.github.io/DownGit/#/home?url=https://github.com/analogdevicesinc/education_tools/tree/master/m2k/ltspice/wien_bridge_osc>`_

Further Reading
---------------

* `"Thank You, Bill Hewlett", Jim Williams, EDN Magazine Feb. 2001 <https://m.eet.com/media/1146147/22254-61856.pdf>`_
* `U.S. Patent 2,268,872: Variable Frequency Oscillation Generator <https://web.archive.org/web/20211006041636/https://www.hp.com/us-en/pdf/002pate nt_tcm_245_921599.pdf>`_
* :adi:`Linear Technology Application Note 43 <media/en/technical-documentation/application-notes/an43f.pdf>`
* `Wien_bridge_oscillator <https://en.wikipedia.org/wiki/Wien_bridge_oscillator>`_
* `Using lamps for stabilizing oscillators <http://www.tronola.com/moorepage/Lamps.html>`_

Warning
-------

.. esd-warning::
