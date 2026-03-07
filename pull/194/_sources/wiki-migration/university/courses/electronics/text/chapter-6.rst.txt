Chapter 6: Diode applications (Power supplies, voltage regulators & limiters)
=============================================================================

6.1 Rectifier
-------------

A rectifier is an electrical device that converts alternating current (AC) to direct current (DC), a process known as rectification. Rectifiers have many uses including as components of power supplies and as amplitude modulation detectors (envelope detectors) of radio signals. Rectifiers are most commonly made using solid state diodes but other type of components can be used when very high voltages or currents are involved. When only a single diode is used to rectify AC (by blocking the negative or positive portion of the waveform), the difference between the term diode and the term rectifier is simply one of usage. The term rectifier describes a diode that is being used to convert AC to DC. Most rectifier circuits contain a number of diodes in a specific arrangement to more efficiently convert AC power to DC power than is possible with only a single diode.

6.1.1 Half-wave rectification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In half wave rectification, either the positive or negative half of the AC wave is passed, while the other half is blocked. Because only one half of the input waveform reaches the output, it is only 50% efficient if used for power transfer. Half-wave rectification can be achieved with a single diode in a single phase supply as shown in figure 6.1, or with three diodes in a three-phase supply.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6.1 Half wave rectifier using one diode


The output DC voltage of a half wave rectifier, given a sinusoidal input, can be calculated with the following ideal equations:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-e1.png
   :align: center
   :width: 400px

6.1.2 Full-wave rectification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A full-wave rectifier converts both the positive and negative halves of the input waveform to a single polarity (positive or negative) at its output. By using both halves of the AC waveform full-wave rectification is more efficient than half wave.

When a simple transformer with out a center tapped secondary is used, four diodes are required instead of the one needed for half-wave rectification. Four diodes arranged this way are called a diode bridge or bridge rectifier as shown in figure 6.2. The bridge rectifier can also be used for translating a DC input of unknown or arbitrary polarity into an output of known polarity. This is generally required in electronic telephones or other telephony devices where the DC polarity on the two phone wires is unknown. There are also applications for protecting against accidental battery reversal in battery-powered circuits.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6.2 Bridge rectifier: a full-wave rectifier using 4 diodes.


For single-phase AC, if the transformer is center-tapped, then two diodes back-to-back (i.e. anode-to-anode or cathode-to-cathode) can form a full-wave rectifier. Twice as many windings are required on the transformer secondary to obtain the same output voltage compared to the bridge rectifier above. This is not as efficient from the transformer perspective because current flows in only one half of the secondary during each positive and negative half cycle of the AC input.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6.3 Full-wave rectifier using a center tapped transformer and 2 diodes.


If a second pair of diodes is included as in figure 6.4 then both positive and negative polarity voltages with respect to the transformer center tap can be generated. One can also view this arrangement to be the same as adding a center tap to the secondary winding in the full-wave bridge rectifier from figure 6.2.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-f8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6.4 Dual polarity Full-wave rectifier using a center tapped transformer and 4 diodes.


**ALM1000 Lab Activity** :doc:`Diode Rectifiers </wiki-migration/university/courses/alm1k/circuits1/alm-cir-diode-rectifier>`

6.1.3 Rectifier output smoothing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Half-wave or full-wave rectification does not produce a constant-voltage DC as we have seen in the previous figures. In order to produce a steady DC voltage from a rectified AC source, a filter or smoothing circuit is needed. In the simplest form this can be just a capacitor placed across the DC output of the rectifier. There will still remain an amount of AC ripple voltage where the voltage is not completely smoothed. The amplitude of the remaining ripple depends on how much the load discharges the capacitor between the peaks of the waveform.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-f10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6.5(a) Half-wave Rectifier RC-Filter


.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-f12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6.5(b) Full-wave Rectifier RC-Filter


Sizing of the filter capacitor, C\ :sub:`1`, represents a tradeoff. For a given load, R\ :sub:`L`, a larger capacitor will reduce ripple but will cost more and will create higher peak currents in the transformer secondary and in the supply feeding it. In extreme cases where many rectifiers are loaded onto a power distribution circuit, it may prove difficult for the power distribution grid to maintain a correctly shaped sinusoidal voltage waveform.

For a given tolerable ripple the required capacitor size is proportional to the load current and inversely proportional to the supply frequency and the number of output peaks of the rectifier per input cycle. The load current and the supply frequency are generally outside the control of the designer of the rectifier system but the number of peaks per input cycle can be affected by the choice of rectifier design. The maximum ripple voltage present for a Full Wave Rectifier circuit is not only determined by the value of the smoothing capacitor but by the frequency and load current, and is calculated as:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-e2.png
   :align: center
   :width: 200px

| Where:
| V\ :sub:`ripple`\ is the maximum ripple voltage on the DC output
| I\ :sub:`Load` is the DC load current
| F is the frequency of the ripple (generally 2X the AC frequency)
| C is the smoothing capacitor

A half-wave rectifier, figure 6.5(a) will only give one peak per cycle and for this and other reasons is only used in very small power supplies and where cost and complexity are of concern. A full wave rectifier, figure 6.5(b) achieves two peaks per cycle and this is the best that can be done with single-phase input. For three-phase inputs a three-phase bridge will give six peaks per cycle and even higher numbers of peaks can be achieved by using transformer networks placed before the rectifier to convert to a higher phase order.

To further reduce this ripple, an LC π-filter (pi-filter) such as shown in figure 6.6 can be used. This complements the reservoir capacitor, C\ :sub:`1`, with a series inductor, L\ :sub:`1`, and a second filter capacitor, C\ :sub:`2` so that a steadier DC output can be obtained across the terminals of the final filter capacitor. The series inductor presents a high impedance at the ripple current frequency.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-f13.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6.6 LC π-filter (pi-filter)


A more usual alternative to a filter, and essential if the DC load requires a very smooth supply voltage, is to follow the filter capacitor with a voltage regulator which we will discuss in section 6.3. The filter capacitor needs to be large enough to prevent the troughs of the ripple getting below the drop-out voltage of the regulator being used. The regulator serves both to remove the last of the ripple and to deal with variations in supply and load characteristics. It would be possible to use a smaller filter capacitor (which can be large for high-current power supplies) and then apply some filtering as well as the regulator, but this is not a common design strategy. The extreme of this approach is to dispense with the filter capacitor altogether and put the rectified waveform straight into an inductor input filter. The advantage of this circuit is that the current waveform is smoother and consequently the rectifier no longer has to deal with the current as a large current pulse just at the peaks of the input sine wave, but instead the current delivery is spread over more of the cycle. The downside is that the voltage output is much lower - approximately the average of an AC half-cycle rather than the peak.

6.2 Voltage-doubling rectifiers
-------------------------------

The simple half wave rectifier can be built in two versions with the diode pointing in opposite directions, one version connects the negative terminal of the output direct to the AC supply and the other connects the positive terminal of the output direct to the AC supply. By combining both of these with separate output smoothing capacitors it is possible to get an output voltage of nearly double the peak AC input voltage, figure 6.7. This also provides a tap in the middle, which allows use of such a circuit as a split rail (positive and negative) supply.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-f14.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6.7 Simple voltage doubler.


A variant of this is to use two capacitors in series for the output smoothing on a bridge rectifier then place a switch between the midpoint of those capacitors and one of the AC input terminals. With the switch open this circuit will act like a normal bridge rectifier with it closed it will act like a voltage doubling rectifier. In other words this makes it easy to derive a voltage of roughly 320V (+/- around 15%) DC from any mains supply in the world, this can then be fed into a relatively simple switched mode power supply.

Section Review:
~~~~~~~~~~~~~~~

-   Rectification is the conversion of alternating current (AC) to direct current (DC).
   \* A half-wave rectifier is a circuit that allows only one half-cycle of the AC voltage waveform to be applied to the load, resulting in one non-alternating polarity across it. The resulting DC delivered to the load "pulsates" significantly.
   \* A full-wave rectifier is a circuit that converts both half-cycles of the AC voltage waveform to an unbroken series of voltage pulses of the same polarity. The resulting DC delivered to the load doesn't "pulsate" as much.
   \* Capacitors are used to smooth out or filter the ripple present in the rectified DC, and sometimes more complex filters using inductors as well as capacitors are used.

6.3 Zener Diode as Voltage Regulator
------------------------------------

Zener diodes are widely used as voltage references and as shunt regulators to regulate the voltage across small circuits. When connected in parallel with a varying voltage source, such as the diode rectifier we just discussed, so that it is reverse biased, the zener diode conducts when the voltage reaches the diode's reverse breakdown voltage. From that point on, the relatively low impedance of the diode keeps the voltage across the diode at that value.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-f15.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 6.8 Zener Diode Voltage Reference


In the circuit shown in figure 6.8, a typical shunt regulator, an input voltage, V\ :sub:`IN`, is regulated down to a stable output voltage V\ :sub:`OUT`. The reverse bias breakdown voltage of diode D\ :sub:`Z` is stable over a wide current range and holds V\ :sub:`OUT` relatively constant even though the input voltage may fluctuate over a fairly wide range. Because of the low impedance of the diode when operated like this, series resistor R\ :sub:`S` is used to limit current through the circuit.

In the case of this simple reference, the current flowing in the diode is determined using Ohm's law and the known voltage drop across the resistor R\ :sub:`S`.

:math:`I_Diode = (V_IN - V_OUT) / R_S`

The value of R\ :sub:`S` must satisfy two conditions:

-   R\ :sub:`S` must be small enough that the current through D\ :sub:`Z` keeps D\ :sub:`Z` in reverse breakdown. The value of this current is given in the manufacturer's data sheet for D\ :sub:`Z`. For example, the common BZX79C5V6 device, a 5.6 V 0.5 ? zener diode, has a recommended reverse current of 5 mA. If insufficient current exists through D\ :sub:`Z`, then V\ :sub:`OUT` will be unregulated, and less than the nominal breakdown voltage. When calculating R\ :sub:`S`, allowance must be made for any current through any external load that might be connected to V\ :sub:`OUT`, not shown in this diagram.
-   R\ :sub:`S` must be large enough that the current through D\ :sub:`Z` does not exceed the rated maximum and destroy the device. If the current through D\ :sub:`Z` is I\ :sub:`D`, its breakdown voltage V\ :sub:`B` and its maximum power dissipation P\ :sub:`MAX`, then:

:math:`I_D \times V_B < P_MAX`

A load may be placed across the diode in this reference circuit, and as long as the zener stays in reverse breakdown, the diode will provide a stable voltage source to the load. Zener diodes in this configuration are often used as stable references for more complicated voltage regulator circuits involving buffer amplifier stages to supply large currents to the load.

Shunt regulators are simple, but the requirements that the ballast resistor, R\ :sub:`S`, be small enough to avoid excessive voltage drop during worst-case operation (low input voltage concurrent with high load current) tends to leave a lot of current flowing in the diode much of the time, making for a fairly inefficient regulator with high quiescent power dissipation, only suitable for smaller loads.

These devices are also encountered, typically in series with a base-emitter junction, in transistor stages where selective choice of a device centered around the avalanche or zener point can be used to introduce compensating temperature co-efficient balancing of the transistor PN junction. An example of this kind of use would be a DC error amplifier used in a regulated power supply circuit feedback loop system.

As a side note: zener diodes are also used in surge protectors to limit transient voltage spikes. Another notable application of the zener diode is the use of noise caused by its avalanche breakdown in a random number generator that never repeats.

Regulator Design Example:
~~~~~~~~~~~~~~~~~~~~~~~~~

An output voltage of 5V is required and the output current required is 60mA.

We first must choose a zener diode, V\ :sub:`Z` = 4.7V which is the nearest value available.

We need to determine the nominal input voltage and it must be a few volts greater than V\ :sub:`Z`. For this example we will use V\ :sub:`IN` = 8V.

As a rule of thumb we choose the nominal current through the zener to be 10% of the required output load current or 6mA. This then determines the current I\ :sub:`max` = 66mA which will flow through R\ :sub:`S` (output current plus 10%).

The series resistor R\ :sub:`S` = (8V - 4.7V) / 66mA = 50Ω, we would choose R\ :sub:`S` = 47Ω which is the nearest standard value.

The resistor power rating P\ :sub:`RS` > (8V - 4.7V) × 66mA = 218mW, so we choose P\ :sub:`RS` = 0.5W

The maximum power that could be dissipated in the zener when there is zero current in the output load can be calculated as P\ :sub:`Z` > 4.7V × 66mA = 310mW, so we would choose P\ :sub:`Z` = 400mW.

\**ADALM2000 Lab Activity: :doc:`Zener Diode Regulator </wiki-migration/university/courses/electronics/electronics-lab-26>` \*\*

**Exercise 6.3.1**

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr6-f16.png
   :align: center
   :width: 400px

| For the circuit shown, if the power supply voltage V\ :sub:`IN` increases, the voltage across the load resistor R\ :sub:`L` will:
| \* increase
| \* decrease
| \* remain the same

| For the circuit shown, if the power supply voltage V\ :sub:`IN` decreases, the voltage across the load resistor R\ :sub:`L` will:
| \* increase
| \* decrease
| \* remain the same

| For the circuit shown, if the power supply voltage V\ :sub:`IN` increases, the voltage across the series resistor R\ :sub:`S` will:
| \* increase
| \* decrease
| \* remain the same

| For the circuit shown, if the power supply voltage V\ :sub:`IN` increases, the current through the load resistor R\ :sub:`L` will:
| \* increase
| \* decrease
| \* remain the same

| For the circuit shown, if the power supply voltage V\ :sub:`IN` decreases, the current through the zener diode D\ :sub:`Z` will:
| \* increase
| \* decrease
| \* remain the same

| For the circuit shown, if the power supply voltage V\ :sub:`IN` increases, the current through the series resistor R\ :sub:`L` will:
| \* increase
| \* decrease
| \* remain the same

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-5>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-7>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`
