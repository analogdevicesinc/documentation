Activity: Polyphase Filter Circuits
===================================

Objective:
----------

The objective of this lab activity is to examine polyphase filter circuits as a quadrature generation technique and to extend the differential tuned amplifier to create a polyphase amplifier or filter that can produce all four quadrature ( 90º increments ) phases of an input signal source.

Background:
-----------

The use of quadrature frequency conversion is common in modern wireless transceiver architectures, because both amplitude modulation and phase modulation are deployed in today's digital communication systems.

http://en.wikipedia.org/wiki/Quadrature_amplitude_modulation

Figure 1 shows a simplified first order polyphase circuit, as implemented in many quadrature demodulators such as the ADL5380. This simple polyphase circuit consists of complementary RC subcircuits. A low-pass transfer function from the input to one output shifts the phase by -45º at the corner frequency, and a high-pass transfer function to the other output shifts the phase by +45º at the corner frequency. The net phase difference between the two outputs will be 90º. If the R and C values of the two paths are matched, then both paths have the same corner frequency and, more importantly, the phase of one output tracks the other with a 90° phase shift for all frequencies. The relative amplitudes of the two output signals, ( LO I 0º and LO Q 90º ) will be only equal at the -3dB corner frequency of the two RC paths.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/appf_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1. Simplified First Order Polyphase Filter


Generation of quadrature local oscillator (LO) signals is an important functional block in sideband rejection heterodyne receivers. Quadrature accuracy, that is the phase accuracy of the in phase and quadrature 90º phase-shifted signals, directly determines the image reject ratio (IRR), an important specification determining the sensitivity of a receiver.

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 2 - 1 nF capacitors ( marked 102 )
| 2 - 1 KΩ resistors

Directions:
~~~~~~~~~~~

Build the polyphase filter circuit shown in figure 2 on your solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/appf_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 polyphase filter circuit


Hardware Setup:
~~~~~~~~~~~~~~~

The green squares indicate where to connect the ADALM2000 module AWG, and scope channels.


|image1|

.. container:: centeralign

   Figure 3. Simplified First Order Polyphase Filter Breadboard Connection


Open the Network Analyzer software tool in Scopy. Configure the frequency sweep to start at 10 KHz and stop at 30 MHz. Set the amplitude to 2 V and the offset to zero. Check the box "Use Channel 1 as reference" under the scope channels drop down menu to measure the phase of one output path with respect to the other.



|image2|

.. container:: centeralign

   Figure 4. Scopy Network Analyzer output


Procedure:
~~~~~~~~~~

Calculate the expected RC corner frequency based on the R and C values you used. Run a single sweep of the frequency and be sure to save your data to a .csv file for later use in either MatLAB or Excel.

Questions:
~~~~~~~~~~

Differential Polyphase Tuned Amplifier
--------------------------------------

By adding second order L-C and C-L low and high pass filter sections as differential output loads in a NPN differential amplifier we can generate all four 90º phases ( i.e. 0º, 90º, 180º and 270º ) of an input sine wave signal. Such a tuned amplifier is shown in figure 5.

.. _materials-1:

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - SSM2212 NPN matched transistor pair ( Q\ :sub:`1`, Q\ :sub:`2` )
| 2 - 2N3904 NPN transistors ( Q\ :sub:`3`, Q\ :sub:`4` )
| 2 - 100 uH inductor (Various other value inductors)
| 2 - 1 nF capacitors ( marked 102 )
| 2 - 0.1 uF capacitors ( marked 104 )
| 2 - 10 Ω resistors
| 2 - 150 Ω resistors
| 2 - 470 Ω resistors
| 3 - 1 KΩ resistors
| 1 - 10 KΩ resistor
| Other resistor and capacitors as needed

.. _directions-1:

Directions:
~~~~~~~~~~~

Build the circuit shown in figure 5 on your solder-less breadboard. Use the SSM2212 matched transistor pair for Q\ :sub:`1` and Q\ :sub:`2`. Transistors Q\ :sub:`3` and Q\ :sub:`4` can be 2N3904 devices. Set L\ :sub:`1` = L\ :sub:`2` = 100 uH and C\ :sub:`1` = C\ :sub:`2` = 1nF. R\ :sub:`1` should be equal to R\ :sub:`2` and use 470 Ω for their value. Likewise, R\ :sub:`3` should be equal to R\ :sub:`4` and use 150 Ω for their value.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/appf_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5 Polyphase Amplifier


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The green squares indicate where to connect the ADALM2000 module AWG, scope channels and power supplies. Be sure to turn on the power supplies only after you double check your wiring.


|image3|

.. container:: centeralign

   Figure 6. Polyphase Amplifier Breadboard Connection


Open the voltage supply control window to turn on and off the fixed +5 and -5 volt power supplies. Open the Network Analyzer software tool in Scopy. Configure the frequency sweep to start at 100 Hz and stop at 30 MHz. Set the amplitude to 1V and the offset to zero.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Calculate the expected LC corner frequency based on the L and C values used.

Turn on the power supplies. Connect scope input channel 2 through an AC coupling capacitor ( C\ :sub:`4` in figure 3 ) alternately to each of the four possible outputs at the ends of resistors R\ :sub:`1`, R\ :sub:`2`, R\ :sub:`3` and R\ :sub:`4`. Run a single frequency sweep and store each sweep in a waveform snapshot to compare each output's relative gain and phase response. Be sure to export all the frequency sweep data to a .csv file for further analysis in either Excel or Matlab.

Using the scope and function generator software instruments ( in the time domain ) set the AWG frequency to the resonate frequency with the amplitude set to 1V peak-to-peak. Trigger on scope channel 1. Observe the relative amplitudes and phases of the four outputs and store each waveform on channel 2 as a reference channel to compare the amplitude and phase of each output.


|image4|

.. container:: centeralign

   Figure 7. 0-degree Phase Shift


   |image5|

.. container:: centeralign

   Figure 8. 90-degree Phase Shift


   |image6|

.. container:: centeralign

   Figure 9. 180-degree Phase Shift


   |image7|

.. container:: centeralign

   Figure 10. 270-degree Phase Shift


.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/polyphase_filter_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/polyphase_filter_ltspice`
   


.. _questions-1:

Questions:
~~~~~~~~~~

**For Further Reading:**

http://www.microwavejournal.com/ext/resources/pdf-downloads/IQTheory-of-Operation.pdf

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/appf_nf3.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/appf_nf4.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/appf_nf6.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/appf_nf7.png
   :width: 500px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/appf_nf8.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/appf_nf9.png
   :width: 500px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/appf_nf10.png
   :width: 500px
