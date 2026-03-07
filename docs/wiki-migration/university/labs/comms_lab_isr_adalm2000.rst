Activity: Inductor Self Resonance
=================================

Objective:
----------

The objective of this Lab activity is to measure the self resonance frequency of an inductor and from the measured data determine the parasitic capacitance.

Background:
-----------

The inductors supplied in your parts kit, like all non-ideal electrical components, are not perfect. The schematic in figure 1 shows the most common simple model of a real inductor. In addition to the desired inductance L, the real component also has loss ( modeled as a series resistance, shown in the schematic as R ) and a parallel parasitic capacitance, shown as C. The smaller the resistance i.e. close to 0 Ω and the smaller the capacitance i.e. close to 0 F, the more ideal the inductor becomes.

.. image:: https://wiki.analog.com/_media/university/labs/aisr_f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, Three Element LRC Inductor Model


**Inter-winding Capacitance and Self-Resonant Frequency**

The classical description of C is that it represents the turn-to-turn distributed capacitance of the inductor (and turn-to-core, etc.). At some frequency, the "self-resonant frequency" or SRF, this turn-to-turn capacitance forms a parallel resonance with the inductance L and the inductor becomes a tuned circuit.

**Three Element LRC Model Impedance versus Frequency**

At frequencies below the Self Resonate Frequency, the model appears to be inductive; at frequencies above the SRF it appears to be capacitive and at the SRF it is resistive, as the inductive and capacitive reactance are equal in magnitude but opposite in sign and thus cancel.

| At the SRF of an inductor, all of the following conditions are met:
| •The input impedance is at its peak.
| •The phase angle of the input impedance is zero, crossing from positive (inductive) to negative (capacitive).
| •Since the phase angle is zero, the Q is zero.
| •The effective inductance is zero, since the negative capacitive reactance (X\ :sub:`C`\ =1/jωC) just cancels the positive inductive reactance (X\ :sub:`L`\ = jωL).
| •The 2-port insertion loss (S21 dB) is a maximum, which corresponds to the minimum in the plot of frequency vs. S21 dB.
| •The 2-port phase (S21 angle) is zero, crossing from negative at lower frequencies to positive at higher frequencies.
| The following equation shows how the SRF is related to inductance and capacitance in the inductor model circuit.

:math:`F_SR = 1/(2 \pi sqrt(LC_p))` in Hz

| where :
| L is the inductance in Henries
| C\ :sub:`p` is the parasitic capacitance in Farads

From this equation, it is clear that increasing inductance or capacitance lowers the measured SRF. Reducing inductance or capacitance raises the SRF.

Pre-Lab Simulation of Three Element LRC Inductor Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The schematic in figure 2 shows the simulation test circuit for the three element LRC model of the inductor. L, R and C\ :sub:`P` are used to model the inductor. V1 is the ideal AC test voltage source and resistor RS serves as the source resistance for V1. CL and RL are the components of the load with CL set equal to the typical input capacitance of the ADALM2000 scope input channel. RL is either set equal to RS or can be set to some higher value such as the 1 MegΩ input resistance of the scope channel.

.. image:: https://wiki.analog.com/_media/university/labs/aisr_f2.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 2 Simulation Schematic


You should simulate the circuit shown in figure 2 before building the actual inductor test circuit.

Two frequency sweep simulations were run from 10KHz to 10MHz as an example of a 1mH inductor, L, with C\ :sub:`P` set to 15pF and R set to 100mΩ. The red curve is with RL set to the same 200Ω as RS. The amplitude seen at RL has a sharp dip at the self resonance frequency when the impedance of the inductor is at its maximum. The blue curve is with RL set to the 1 MegΩ of the scope input. Again we see the sharp null when the impedance is maximum. We also see a sharp peak in the amplitude seen at RL about one octave below the notch. This peaking occurs when the source and load resistances are not matched.

.. image:: https://wiki.analog.com/_media/university/labs/aisr_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Simulation results Red curve RL=200Ω, Blue Curve RL=1MegΩ


Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 1 mH inductor
| Various other value inductors
| 2 - 200 Ω resistors ( may be made from 2 100 Ω resistors in series )

Directions:
-----------

Build the Inductor test circuit as shown in figure 4 on your solder-less breadboard. The green squares indicate where to connect the ADALM2000 AWG and scope channels.

.. image:: https://wiki.analog.com/_media/university/labs/aisr_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Inductor test circuit


Hardware Setup:
---------------

The connections to the ADALM2000 AWG output and scope channel inputs are as indicated by the green boxes in figure 4. Your parts kit should contain a number of inductors with different values. Insert each inductor, one at a time into your test circuit.


|image1|

.. container:: centeralign

   Figure 5 Inductor test circuit breadboard connections


Procedure:
----------

Open the network analyzer software instrument from the Scopy window. Configure the sweep to start at 100 KHz and stop at 30 MHz. Set the Amplitude to 1V and the Offset to zero volts. Under the Bode scale set the magnitude top to 40 dB and bottom to -60 dB. Set the phase top to 180º and bottom to -180º. Under scope channels click on use channel 1 as reference. Set the number of steps to 100.

Run a single sweep for each inductor in your kit of parts. You should see amplitude and phase vs frequency plots that look very similar to your simulation results. Be sure to export the data to a .csv file for further analysis in either Excel or Matlab.


|image2|

.. container:: centeralign

   Figure 6 Scopy Shot, L=100uH, RL=200ohms


   |image3|

.. container:: centeralign

   Figure 7 Scopy Shot, L=100uH, RL=1Mohms


Questions:
----------

Use the formula for the self resonance to calculate a value for the turn-to-turn parasitic capacitance of each of your inductors. Plug these calculated values in to your simulation schematic and run AC sweeps to confirm that the actual and simulated frequency response plots are similar for each inductor.

Extra Credit experiments:
~~~~~~~~~~~~~~~~~~~~~~~~~

To further explore this resonance, connect external 39 pF and/or 100 pF capacitors in parallel with the inductor and re-measure the frequency response. You will now have additional resonance frequencies that you can use to also calculate and confirm the inductance L as well as C\ :sub:`P` in our simple model by using the resonance formula.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/inductor_self_resonance_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/inductor_self_resonance_ltspice`
   


**For Further Reading:**

| http:*en.wikipedia.org/wiki/Inductor
  http:*\ en.wikipedia.org/wiki/Self-resonant_frequency
| http:*www.coilcraft.com/pdfs/Doc363_MeasuringSRF.pdf
  http:*\ www.coilcraft.com/pdfs/doc671_Selecting_RF_Inductors.pdf
| http://www.coilcraft.com/pdfs/doc119_TestAppFreq.pdf

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/labs/aisr_f4bb.png
.. |image2| image:: https://wiki.analog.com/_media/university/labs/aisr_f6.png
.. |image3| image:: https://wiki.analog.com/_media/university/labs/aisr_f7.png
