Activity: Audio Amplifier with Electret Microphone
==================================================

Objective
---------

The objective of this lab activity is to design and build an audio amplifier that takes the small output voltage from an electret microphone and amplifies it such that it can drive a small loudspeaker.

Background
----------

| An electret microphone is a type of condenser (capacitor) microphone that has an essentially permanent charge on the capacitor plates, eliminating the requirement of external phantom power that is used to bias the capacitor in traditional condenser microphones. Most commercially available electret microphones, however, contain an integrated preamplifier – often an open-drain FET circuit – and therefore require a small amount of low-voltage power.
| Simple audio amplifiers can be designed using transistors, with or without negative feedback. Negative feedback, however, provides a very important improvement in distortion performance. In this experiment we design and build an AC-coupled non-inverting operational amplifier with a desired voltage gain of ten, with an inside-the-loop emitter-follower on its output with AC-coupling to the loudspeaker. The op-amp section provides voltage gain, and the emitter-follower functions as a buffer, providing the current required to drive the loudspeaker. Placing the emitter-follower inside the feedback loop improves its overall performance.
| ===Amplifier Design=== The electret microphone includes an open-drain FET preamplifier, and requires a drain resistor, R\ :sub:`D`, with value between 680 Ω and 2.2 KΩ, connected between its output and the +5V supply as shown in Figure 1. The drain resistor is set at 2.2 KΩ in this design which places the drain voltage at approximately +4.5 V with a +5.0 V supply.
| |audio_amplifier_theory_1.png|

|

.. container:: centeralign

   Figure 1. Electret Microphone Output Stage


| The design goal is to drive a nominally 400 mVP-P signal into an eight ohm loudspeaker, following AC-coupling referenced to ground, requiring about ±25 mA. The amplifier is designed to operate from a single 5V supply. Because of this, the op-amp DC levels are biased to a mid-supply voltage of +2.5 V and input, output, and feedback signals are AC-coupled. AC-coupling of the input signal allows the DC level out of the microphone to differ from the DC level into the amplifier. For the opamp portion of the circuit you can use OP484 quad op-amp provided in the ADALP2000 parts kit and for the emitter follower portion of the circuit you can use the 2N3904 NPN transistor contained in the kit.

| A detailed description of the design and analysis of the audio amplifier is provided in the Audio Amplifier Experiment article. Please refer to the handout for the details of the amplifier theory, available at the link below:
| :doc:`Audio Amplifier with Electret Microphone - Theory </wiki-migration/university/courses/engineering_discovery/lab_4/theory>`

| 
| |audio_amplifier_theory_2.png|

.. container:: centeralign

   Figure 2. Overall Amplifier Schematic Diagram


Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - OP484 rail-to-rail amplifier
| 1 - Electret microphone
| 1 - 2N3904 NPN transistor
| 1 - 8 Ω loudspeaker 1 - 47 Ω resistor
| 1 - 68 Ω resistor
| 1 - 100 Ω resistor
| 1 - 1 KΩ resistor
| 1 - 2.2 KΩ resistor
| 1 - 20 KΩ resistors
| 1 - 4.7 μF capacitor
| 1 - 47 μF capacitor
| 1 - 220 μF capacitor

Hardware setup
--------------

Build the circit presented in Figure 3 on your solderless breadboard.


|image1|

.. container:: centeralign

   Figure 3. Audio Amplifier with electret microphone schematic diagram


   |image2|

.. container:: centeralign

   Figure 4. Audio Amplifier with electret microphone breadboard connections


If you want to check the amplifier functioning you can remove the microphone and the speaker from the circuit and use the oscilloscope tool. For this, the breadboard connections are presented in figure 5.



|image3|

.. container:: centeralign

   Figure 5. Audio Amplifier oscilloscope breadboard connections


Procedure
---------

If you want to check the amplifier gain, build the setup presented in figure 5. Open Scopy and enable the positive power supply to 5V. Set the signal generator channel 1 to a sine waveform with 50 mV amplitude peak-to-peak, 200 Hz frequency and 2.5 V offset. You can increase the amplitude of the sine wave until clipping is observed. In the Oscilloscope monitor the input signal on channel 1 and the amplifier output signal on channel 2. Set the Vertical resolution to 100mV/Div and the postion to -2.5 V so you can see the signals in the oscilloscope window as in figure 6.


|image4|

.. container:: centeralign

   Figure 6. Amplifier input and output waveforms


Connect the electret microphone and the loudspeaker in the circuit as shown in figure 4. Move the loudspeaker directly in front of the microphone until audible feedback occurs.

Questions
---------

-  Explain why the clipping occurs when the amplitude of the sine wave is increased.
-  Explain why there occurs audibe feedback when the loudspeaker and the microphone are close to each other.

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files::git-education_tools:`m2k/fritzing/audio_amplifier_with_electret_microphone_bb`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |audio_amplifier_theory_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_4/audio_amplifier_theory_1.png
   :width: 250px
.. |audio_amplifier_theory_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_4/audio_amplifier_theory_2.png
   :width: 800px
.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/audio_amplifier_circuit.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/electret_audio_amplifier_bb.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/electret_audio_amplifier_gain_test_bb.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/gain_check.png
   :width: 900px
