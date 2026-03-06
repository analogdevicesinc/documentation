Activity: Transformers, For ADALM1000
=====================================

Objective:
----------

The objective of this Lab Activity is to investigate transformer characteristics in various configurations.

Background:
-----------

AC Transformer:
~~~~~~~~~~~~~~~

Transformers only work with alternating current, AC. For example transformers reduce the 120V wall power by stepping the voltage down to more convenient levels for most consumer electronic applications (only a few volts) or for other low power applications (typically 12V). Transformers also step the voltage up for long distance transmission, and down for safe distribution. Without transformers, the waste of electric power in distribution networks, already significant, would be enormous. It is possible to step up or down DC voltages, but the techniques are more complicated than with AC transformers and actually involve turning the DC voltage into some form of AC signal in the process. Further, such conversions are often inefficient and/or expensive. AC has the further advantage that it can be used to drive AC motors, which are usually preferable to DC motors for high power applications. While transformers are most visible in power applications, they serve important roles in many other communications related signal paths at audio and RF frequencies.

The transformer core has high magnetic permeability, i.e. a material that forms a magnetic field much more easily than in free space, due to the orientation of atomic dipoles. In figure 1, the core is made of laminated soft iron but at higher frequencies ferrite is more common. The result is that the magnetic field is concentrated inside the core, and almost no field lines leave the core.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/atrans_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Simple Transformer


It follows that the magnetic flux φ through the primary and secondary are approximately equal, as shown. From Faraday's law, the emf in each turn, whether in the primary or secondary coil, is the negative of the derivative of the magnetic flux with respect to time or, -dφ/dt. Neglecting the winding resistance and other losses in the transformer, the terminal voltage equals the emf. For the N\ :sub:`p` turns of the primary, this gives:

:math:`V_p = -N_p dφ/dt`

For the N\ :sub:`s` turns of the secondary, this gives:

:math:`V_s = -N_s dφ/dt`

Dividing these equations gives the transformer equation:

:math:`V_s / V_p = N_s / N_p = r`

Where r is the turns ratio.

What about the current? Again, neglecting losses in the transformer, and if assuming that the voltage and current have similar phase relationships in the primary and secondary, then from conservation of energy we can write, in steady state:

Power in = power out,

:math:`V_p I_p = V_s I_s`

so:

:math:`I_s / I_p = N_p / N_s = 1/r`

You never get something for nothing. For a step up transformer, if you increase the voltage, you decrease the current by (at least) the same factor or turns ratio. Note that, in the figure, the coil with more turns has thinner wire, because it is designed to carry less current than that with fewer turns.

http://en.wikipedia.org/wiki/Transformer

Impedance matching:
~~~~~~~~~~~~~~~~~~~

In communications related applications, transformers are most often used between sections of the circuits to match impedances. As we just saw a transformer converts alternating current at one voltage amplitude seen at the primary to another voltage amplitude at the secondary. The total power input to the primary and output from the secondary is the same ( except for internal losses ). The side with the lower voltage is at lower impedance (because this has the lower number of turns), and the side with the higher voltage is at a higher impedance (as it has more turns in its coil).

One example of this impedance matching is a television balun (short for balanced-unbalanced) transformer. This transformer converts a balanced signal from the antenna (via 300 Ω twin-lead) into an unbalanced signal (75 Ω coaxial cable such as RG-6). To match the antenna's 300 Ω source resistance, R\ :sub:`S`, to the 75 Ω coax load resistance, R\ :sub:`L`, a ratio of 4:1, a matching transformer with a turns ratio of 2 is used. The formula for calculating the transformer turns ratio for this example is:

Turns ratio :math:`r = sqrt(R_S / R_L)`

| http://en.wikipedia.org/wiki/Maximum_power_transfer_theorem
| http://en.wikipedia.org/wiki/Impedance_matching

Frequency range:
~~~~~~~~~~~~~~~~

The lower limit on the usable frequency range of a transformer is generally set by the impedance level of the circuit in question and the inductance of the transformer windings. If we assume the common 50 Ω standard as our starting point we can calculate the lower frequency bound based on the published winding inductance from the manufacturer's datasheets. The upper limit on the usable frequency range of a transformer is generally set by the parasitic inter-winding capacitance and the self resonance. In some cases the datasheets will specify the usable frequency range. In general it is common practice to pick the reactive component, in this case the inductance, at the lowest frequency of interest, to be at least 4 times the resistive component, in this case the 50 Ω source resistance.

Formulas used to calculate electrical characteristics of multi-winding transformers:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Manufacturer datasheets list certain electrical characteristics for the devices. Probably the most important for our purposes is the winding inductance. For power conversion applications the DC resistance (DCR), the maximum rms current (I\ :sub:`rms`), and saturation current I\ :sub:`sat` are also specified.

**Connecting windings in series:**

For higher inductance, multiple windings (W\ :sub:`N`) can be connected in series. As the inductance increases, energy storage and I\ :sub:`rms` remain the same, but DCR increases and I\ :sub:`sat` decreases.

Inductance = Inductance\ :sub:`table` × (W\ :sub:`N`)\ :sup:`2`

Note: this Wn\ :sup:`2` factor is only valid when the coupling factor between windings is exactly ( or very nearly ) one. A more general formula is L\ :sub:`T` = L\ :sub:`1` + L\ :sub:`2` + 2M

| DCR = DCR\ :sub:`table` × W\ :sub:`N`
| I\ :sub:`sat` = (I\ :sub:`sattable` × 6) ÷ W\ :sub:`N` (connected in series)
| I\ :sub:`rms` = I\ :sub:`rmstable`

Where Inductance\ :sub:`table`, DCR\ :sub:`table`, I\ :sub:`sattable`\ and I\ :sub:`rmstable`\ come from the manufacturer's datasheet.

**Connecting windings in parallel:**

To increase current ratings, multiple windings (W\ :sub:`N`) can be connected in parallel. DCR decreases, current ratings increase, and inductance remains the same.

| Inductance = Inductance\ :sub:`table`
| DCR = 1 ÷ [W\ :sub:`N` × (1 ÷ DCR\ :sub:`table`)]
| I\ :sub:`sat` = (I\ :sub:`sattable` × 6) ÷ W\ :sub:`N` ( connected in parallel )
| I\ :sub:`rms` = I\ :sub:`rmstable` × W\ :sub:`N`

Pre Lab Simulations
~~~~~~~~~~~~~~~~~~~

Before measuring the frequency response of the transformers supplied in your parts kit, create a simulation schematic similar to figure 2 and perform an AC sweep from 10 KHz to 10 MHz. Use the manufacturer's datasheet to set the values for the winding inductance ( mutual inductance for an ideal transformer ) and resistance. Assume that the coupling factor is 1. For this analysis we will assume that the parasitic turn to turn capacitance is small enough to ignore.

Materials:
----------

| ADALM1000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 HPH1-1400L 6 winding transformer
| 1 100 Ω resistor (brown black brown)
| 2 47 Ω resistors (yellow purple black)

Directions:
-----------

The first step is to measure the winding inductance of the HPH1-1400L.

Wire the HPH1-1400L 6 winding Inductor as shown in figure 1 with the 6 windings connected in series. To use the ALICE desktop Impedance Analyzer tool to measure the inductance an external reference resistor is used. Connect the CHA pin of the ALM1000 to one end of R\ :sub:`EXT` and the other end of R\ :sub:`EXT` to the CHB pin of the ALM1000 and to pin 1 of the HPH1-1400L.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-transformers-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Winding Inductance measurement setup


Set AWG Channel A Max to 3.5, Min to 1.5, Freq to 6250 Hz. When you open the Impedance Analyzer window for the first time it automatically sets Channel A to SVMI mode, Shape to Sine and Channel B to Hi-Z mode.

One at a time connect the fixed 2.5 V pin on the ALM1000 to pins 2, 3, 6, 10, 11 and 12 of the HPH1-1400L. Record the measured inductance when 1, 2, 3, 4, 5 and 6 windings are connected in series.

The second step is to measure the frequency response of the HPH1-1400L configures as a 1:1 transformer with different numbers of windings connected in series and compare these measurements to the calculated frequency response based on the impedances you just measured.

Modify the circuit on your solder-less breadboard to look as shown in figure 3. You will be using this setup to measure the frequency response of in three different configurations with 1:1 primary to secondary turns ratios. The two red arrows indicate where to connect the source and load resistors for the configuration where one winding is used for the primary and secondary. The blue arrows are for the configuration where two coils in series are used for the primary and secondary. The green arrows are for the configuration where three coils in series are used for the primary and secondary.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-transformers-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Transformer test circuit


Hardware Setup:
---------------

Open the Bode Plotter tool from the ALICE main window and set the sweep to start at 100 Hz and stop at 25 KHz. Set the AWG Channel A Min value to 1.1 and the Max value to 3.9 volts. Under channels click on Sweep channel A. Set the number of steps to 300.

Procedure:
----------

Run a single sweep for each 1:1 winding configuration (i.e. 1:1, 2:2 and 3:3 windings) for the transformer in the ADALP2000 kit of parts. You should see amplitude and phase vs frequency plots that look very similar to your simulation results. Be sure to export the data to a .csv file for further analysis in either Excel or Matlab.

Questions:
----------

How do your measurements compare to the winding inductance specified in the manufacturer's datasheet?

How do does the measured frequency response compare to your calculated response based on the measured winding inductance?

Step Up and Step Down Configurations
------------------------------------

Connect to the transformer for a 1:2 step up configuration (red arrows) and a 2:1 step down configuration as shown in figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-transformers-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Step Up (red) and Step Down (blue) connections


Use the impedance matching formula to calculate the appropriate value for R\ :sub:`L` in both cases. Repeat the same frequency sweeps using the Network Analyzer tool. Be sure to export the data to a .csv file for further analysis in either Excel or Matlab. Compare the measured low frequency roll off points with those measures in the 1:1 configurations from figure 3.

For additional credit calculate the correct R\ :sub:`L` for other possible step up and step down ratios possible with these 6 winding transformers such as 1:3, 2:3, 3:1, 3:2 etc. Measure and report the data for as many different configurations as you have time for.

**For Further Reading:**

| :adi:`Transformers: They’re Not All Boat Anchors <en/analog-dialogue/raqs/raq-issue-82.html>`
| `Electromagnetic coil <https://en.wikipedia.org/wiki/Electromagnetic_coil>`__
| `Signal Transformer Application and Specification <http://www.coilcraft.com/pdfs/doc157_SigXfrmApp.pdf>`__
| `Simulating Non-linear Transformers in LTspice <https://www.allaboutcircuits.com/technical-articles/simulating-non-linear-transformers-in-ltspice/>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`\ **.**
