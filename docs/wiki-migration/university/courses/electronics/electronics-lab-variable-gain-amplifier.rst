Activity: Variable Gain Amplifiers
==================================

Objective
---------

In this laboratory we continue our discussion on operational amplifiers (see the previous lab here: :doc:`Activity 1. Simple Op Amps </wiki-migration/university/courses/electronics/electronics-lab-1>`) focusing on variable gain / voltage-controlled amplifiers.

Most operational amplifier or op-amp circuits have a fixed level of gain. However it is often useful to be able to vary the gain. This can be done simply by using a potentiometer on the output of a fixed gain op-amp circuit, but sometimes it may be more useful to vary the actual gain of the amplifier circuit itself.

A variable-gain or voltage-controlled amplifier is an electronic amplifier that varies its gain depending on a control voltage. This type of circuit has many applications, including audio level compression, synthesizers and amplitude modulation. It can be realized by first creating a voltage-controlled resistor, which is used to set the amplifier gain. The voltage-controlled resistor is one of the numerous interesting circuit elements that can be produced by using a transistor with simple biasing. Another approach is to use potentiometers to vary the value of the resistors that set the gain of the amplifier.

Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 2 1 kΩ resistor
| 1 4.7 kΩ resistors
| 3 10 kΩ resistors
| 1 10 kΩ potentiometer
| 1 OP97 operational amplifier
| 1 2N3904 npn transistor

Voltage Controlled Amplifier using transistor
---------------------------------------------

Background
~~~~~~~~~~

Consider the circuit schematic presented in Figure 1.

.. container:: centeralign


   ..

|image1|

.. container:: centeralign

   Figure 1. Voltage control using transistor


The configuration of the circuit is similar to a basic non-inverting amplifier. The only addition consists of a transistor and a resistor in parallel with resistor R2. The transistor works as a switch that allows 2 gain settings, based on its current state (on/off).

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for the voltage-controlled amplifier using transistors.

.. container:: centeralign


   ..

|image2|

.. container:: centeralign

   Figure 2. Voltage control using transistor breadboard circuit


Procedure
~~~~~~~~~

Use the first waveform generator as source Vin to provide a 2V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit. Use the second waveform generator for controlling the transistor, providing a 2V amplitude, 1Hz square wave excitation. Supply the op amp to +/- 5V from the power supply. Configure the scope so that the input signal is displayed on channel 1 and the output signal is displayed on channel 2.

An animated plot is presented in Figure 3.

.. container:: centeralign


   ..

|image3|

.. container:: centeralign

   Figure 2. Voltage control using transistor waveforms


The output signal varies between two values, determined by the two gain settings, based on the state of the controlled transistor.

Variable Gain Inverting Amplifier using potetiometer
----------------------------------------------------

.. _background-1:

Background
~~~~~~~~~~

Consider the circuit schematic presented in Figure 4.

.. container:: centeralign


   ..

|image4|

.. container:: centeralign

   Figure 4. Variable Gain Inverting Amplifier using potetiometer


On the inverting amplifier a potentiometer is used to control manually the output voltage, replacing the standard feedback resistor.

.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for the voltage-controlled amplifier using transistors.

.. container:: centeralign


   ..

|image5|

.. container:: centeralign

   Figure 5. Variable Gain Inverting Amplifier using potetiometer - breadboard circuit


.. _procedure-1:

Procedure
~~~~~~~~~

Use the first waveform generator as source Vin to provide a 2V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit. Supply the op amp to +/- 5V from the power supply. Configure the scope so that the input signal is displayed on channel 1 and the output signal is displayed on channel 2.

By varying the value of the potentiometer, an animated plot is presented in Figure 6.

.. container:: centeralign


   ..

|image6|

.. container:: centeralign

   Figure 6. Variable Gain Inverting Amplifier using potetiometer - waveforms


Using this type of configuration, the output is inverted and amplified based on the feedback resistance value.

Variable Gain Inverting/Non-Inverting Amplifier using potetiometer
------------------------------------------------------------------

.. _background-2:

Background
~~~~~~~~~~

Consider the circuit schematic presented in Figure 7.

.. container:: centeralign


   ..

|image7|

.. container:: centeralign

   Figure 7. Variable Gain Inverting/Non-Inverting Amplifier using potetiometer


In this amplifier configuration a potentiometer is used to control manually the output voltage, being able to invert the input by adjusting properly the potentiometer.

.. _hardware-setup-2:

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for the voltage-controlled amplifier using transistors.

.. container:: centeralign


   ..

|image8|

.. container:: centeralign

   Figure 8. Variable Gain Inverting/Non-Inverting Amplifier using potetiometer - breadboard circuit


.. _procedure-2:

Procedure
~~~~~~~~~

Use the first waveform generator as source Vin to provide a 2V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit. Supply the op amp to +/- 5V from the power supply. Configure the scope so that the input signal is displayed on channel 1 and the output signal is displayed on channel 2.

By varying the value of the potentiometer, an animated plot is presented in Figure 9.

.. container:: centeralign


   ..

|image9|

.. container:: centeralign

   Figure 9. Variable Gain Inverting/Non-Inverting Amplifier using potentiometer - waveforms


Using this configuration, the output is amplified varying between +-Vin.

Questions
---------

1. Which are the gain values for each of the circuits used in this lab activity?

2. Based on the input signals and the computed gains, which are the expected output values? Compute and compare them with the measured values.

3. Considering the circuit in Figure 7, how can you increase the output range above +-Vin?

Further Reading
---------------

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/var_gain_amp_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/var_gain_amp_ltspice`
   


Some additional resources:

-  :adi:`X-Amp™, A New 45-dB, 500-MHz Variable-Gain Amplifier (VGA) Simplifies Adaptive Receiver Designs <en/analog-dialogue/articles/x-amp-45-db-500-mhz-variable-gain-amplifier.html>`
-  :adi:`Two New Devices Help Reinvent the Signal Generator <en/analog-dialogue/articles/reinvent-the-signal-generator.html>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/vctrl_amp_transistor.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/var_gain_amp_crl-bb.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/var_gain_amp_crl-wav.gif
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/var_g_invert_amp_pot.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/var_gain_amp_pot2-bb.png
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/var_gain_amp_pot2-wav.gif
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/var_gain_inv_noninv.png
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/var_gain_amp_pot-bb.png
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/var_gain_amp_pot-wav.gif
