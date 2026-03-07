Activity: Diode Ring Modulator - ADALM2000
==========================================

Objective
---------

| The objective of this activity is to describe the operation of a diode ring mixer, to identify some of its applications, and to learn the basics of the produces double-sideband suppressed-carrier (DSBSC) signals.

Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| 4 - 100Ω Resistors
| 2 – 1kΩ Resistors
| 4 – 1N914 Diodes
| 2 - Two-triflar-winding Transformers (if available)

Background
----------

In electronic communications, a balanced modulator is a circuit that produces double-sideband suppressed-carrier (DSBSC) signals: It suppresses the radio frequency carrier thus leaving the sum and difference frequencies at the output. The output waveform lacks the carrier, but still contains all the information a traditional AM signal has. This results in power saving during signal transmission.

One of the most prevalent balanced modulators is the Diode Ring Modulator, otherwise known as Lattice Modulator. It comprises of four diodes originally fashioned as a “ring”, thus the moniker, and input and output transformers. The modulator has two inputs: a single frequency carrier and a modulating signal, which can be a single frequency or a complex waveform. The carrier is applied at the center taps of the input and output transformers and the modulating signal at the primary of the input transformer. The output, however, is measured at the secondary of the output transformer. Figure 1 shows the diode ring modulator in two different circuit orientations.


|Diode Ring Modulator|

.. container:: centeralign

   *Figure 1. Diode Ring Modulator*


Also, the diode ring modulator is one of the most extensively used circuits in electronic communications. In addition to producing DSBSC signals, it is also used in frequency and phase modulation systems as well as in digital modulation systems, such as PSK and QAM.



| The orientation of the diodes in a ring modulator must not be mistaken with that of a diode bridge rectifier. They may take the similar “ring” shape; however, the ring modulator has all its diodes face either clockwise or counterclockwise while the bridge rectifier has its diodes facing either left or right.

Operation
---------

The diodes used in the diode ring modulator can either be silicon, silicon Schottky-barrier or gallium-arsenide. They serve as switches that control whether the input signal is passed with or without a 180° phase reversal. The carrier signal is the one that sets the diodes on and off at a high rate of speed. It is important to know that for the modulator to operate, the carrier’s amplitude must be adequately greater than the modulating signal’s, about six to seven times greater.

|

| |Positive Half-cycle Operation|

.. container:: centeralign

   *Figure 2. Positive Half-cycle Operation*


During the positive half-cycle, D1 and D2 are forward biased and on, and D3 and D4 are reverse biased and act as open circuits. The carrier current is then equally divided at the center tap of the input transformer’s secondary and flows in opposite directions through the upper and lower halves of the winding. The currents in the upper and lower parts each produce a magnetic field that is both equal and opposite with each other therefore, the magnetic fields produced cancel out and the carrier is suppressed. Thus, the modulating signal is passed from the input to the output transformers through D1 and D2 without phase reversal. Figure 2 shows the positive half-cycle operation of the modulator.

| 
| |Negative Half-cycle Operation|

.. container:: centeralign

   *Figure 3. Negative Half-cycle Operation*


Figure 3 illustrates the negative half-cycle operation of the diode ring modulator. Diodes D1 and D2 are reversed biased and off while D3 and D4 are forward biased and on. Again, the same thing happens to the carrier current. It splits equally in the primary of the output transformer and both current produce magnetic fields equal and opposite with one another. The two currents merge in the secondary of the input transformer and the magnetic fields are canceled out, and the carrier is suppressed. The modulating signal passes through the input transformer and undergoes a 180° phase reversal before reaching the output transformer.

The figure below shows the waveforms of the diode ring modulator in a timing diagram.

| 
| |Timing Diagram|

.. container:: centeralign

   //Figure 4. Diode Ring Modulator Waveforms: (A) Modulating Signal, (B) Carrier Signal, (C) DSBSC signal at the primary of the output transformer, (D) DSBSC waveform after filtering //


The output waveform of the diode ring modulator has the carrier signal suppressed and is made up of the sum and difference of the input frequencies. They are RF pulses that takes the shape and amplitude of the modulating signal at the rate of the carrier signal. Ideally, the carrier signal is totally suppressed, however, this doesn’t really happen. A small carrier component always goes with the output signal and this is called a **carrier leak**. This happens for a few reasons: First, if the transformers are not exactly center tapped; and second, if the diodes are not perfectly matched.

Hardware Setup
--------------

| 
| |Diode Ring Modulator Circuit|

.. container:: centeralign

   *Figure 5. Diode Ring Modulator Breadboard Circuit*


Construct the circuitry shown in Figure 5 on a solderless breadboard. Use the 1N914 fast switching diode for the diode ring. Set W1 as a 1kHz sine modulating signal with 1V amplitude peak-to-peak and set W2 as a 10kHz sine carrier with a 3V amplitude peak-to-peak. For the input and output transformers, a 1:2 turns ratio is needed. You can experiment with other transformer turns ratio and compare the output results. For this activity, a Hexa-Path Magnetics transformer with either HP3, HP4, HP5, or HP6 winding layout is needed. If not available, you can proceed with the LTspice simulations.

Procedure
---------

| 
| |DSBSC Waveform|

.. container:: centeralign

   //Figure 6. DSBSC Waveform //


Observe the output waveform of the circuit. It should have a similar waveform shown in the simulated waveform above.

Questions
---------

| 1. Change the turns ratio of both the input and output transformers. Observe and compare the output waveforms.
| 2. Interchange the position of W1 and W2 in the circuit. Compare it with the original output waveform. What happens to the output waveform?

Simplified Diode Ring Modulator
===============================

| 
| |Simplified Diode Ring Modulator|

.. container:: centeralign

   //Figure 7. Simplified Transformerless Diode Ring Modulator //


By taking out the transformers, Figure 7 takes a more simplified approach on the traditional diode ring modulator. Both the sum and the difference of the carrier and the modulating signal is fed to opposite junctions of the diode ring by using the ADALM2000 through two low resistance input resistors, R1 and R2, thus taking out the input transformer. The output can be measured across the high resistance output resistors R3 and R4. These resistors then replace the output transformer.

.. _hardware-setup-1:

Hardware Setup
--------------

| 
| |Breadboard Connections|

.. container:: centeralign

   *Figure 8. Simplified Transformerless Diode Ring Modulator breadboard connection*


These transformerless version of the diode ring modulator can be easily supplied with the sum of the carrier and modulating signals at one junction and the difference of the signals at other using the ADALM2000’s signal generators. Set up the breadboard with the output of the first waveform generator, W1, to the other end of R1, and the second waveform generator, W2, at the other end of R2. Connect scope input 1+ in the junction of D1, D3, and R4. Attach scope input 1- to the node that links D2, D4, and R3. Finally, connect the node between R3 and R4 to ground. See Figure 8 for connections.

.. _procedure-1:

Procedure
---------

| In this activity, we will utilize a carrier with a waveform equation of *f\ c = 3sin(10kt)* and a modulating signal with an equation of // f\ :sub:`m` = 0.5sin(1kt)//. Originally, the two waveforms are multiplied together and the output signal is their product. This contains the upper sideband frequency, f\ :sub:`usf`, and the lower sideband frequency, f\ :sub:`lsf`. Their definitions being:

.. container:: centeralign

   :math:`f_usf =f_c + f_m`


.. container:: centeralign

   :math:`f_lsf =f_c - f_m`


where:

-  f\ :sub:`c` = carrier signal
-  f\ :sub:`m` = modulating signal

In this simplified approach, we will directly feed the sidebands to the inputs. Taking note of the carrier and the modulating signals, we will have *f(t) = 3sin(10kt) + 0.5sin(1kt)* for the upper sideband and *f(t) = 3sin(10kt) - 0.5sin(1kt)* for the lower sideband.

In the signal generator, set the equation *f(t) = (3\*sin(10\*t)) + (0.5\*sin(t))* with a 1 kHz frequency for W1 (Ch1), and *f(t) = (3\*sin(10\*t)) - (0.5\*sin(t))* with the same 1 kHz frequency for W2. In the oscilloscope, set the horizontal at 200 us/div and the vertical at 500 mV/div. Run the signal generator and the oscilloscope and observe the waveform. It should have a similar result with the waveform below.

|

| |image1|

.. container:: centeralign

   *Figure 9. Simplified Transformerless Diode Ring Modulator*


Question
--------

| 1. What happens if the resistor values of Figure 7 are changed? Change R1 and R2 with 1 kΩ resistors, what happens to the amplitude of the output waveform? Revert back R1 and R2 to their previous values. Change R3 and R4 with 1 kΩ resistors and again, observe the output waveform.
|

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/diode_ring_mod_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/diode_ring_mod_ltspice`
   


Further Reading
===============

Some additional resources:

-  :adi:`RF/IF Circuits <media/en/training-seminars/design-handbooks/Basic-Linear-Design/Chapter4.pdf>`
-  `A Simple Digital Model of the Diode-Based Ring-Modulator <http://recherche.ircam.fr/pub/dafx11/Papers/66_e.pdf>`_. Parker, J. Aalto University, Finland
-  `Analog Communication – DSBSC Modulators <https://www.tutorialspoint.com/analog_communication/analog_communication_dsbsc_modulators.htm>`_
-  `Ring Modulator for the Double Sideband Suppressed Carrier Generation <https://electronicspost.com/ring-modulator-for-the-double-sideband-suppressed-carrier-generation/>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |Diode Ring Modulator| image:: https://wiki.analog.com/_media/university/courses/electronics/drm_f1.png
   :width: 500px
.. |Positive Half-cycle Operation| image:: https://wiki.analog.com/_media/university/courses/electronics/drm_f2.png
   :width: 500px
.. |Negative Half-cycle Operation| image:: https://wiki.analog.com/_media/university/courses/electronics/drm_f3.png
   :width: 500px
.. |Timing Diagram| image:: https://wiki.analog.com/_media/university/courses/electronics/drm_f4.png
   :width: 500px
.. |Diode Ring Modulator Circuit| image:: https://wiki.analog.com/_media/university/courses/electronics/drm_f5.png
   :width: 700px
.. |DSBSC Waveform| image:: https://wiki.analog.com/_media/university/courses/electronics/drm_f6.png
   :width: 500px
.. |Simplified Diode Ring Modulator| image:: https://wiki.analog.com/_media/university/courses/electronics/drm_f7.png
   :width: 500px
.. |Breadboard Connections| image:: https://wiki.analog.com/_media/university/courses/electronics/drm_f8.png
.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/drm_f9.png
