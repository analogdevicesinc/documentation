Activity: Poly Phase Filter Circuits - ADALM1000
================================================

Objective:
----------

The objective of this lab activity is to examine poly phase filter circuits as a quadrature generation technique and to extend the differential tuned amplifier to create a poly phase amplifier or filter that can produce all four quadrature ( 90º increments ) phases of an input signal source.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

The use of quadrature frequency conversion is common in modern wireless transceiver architectures, because both amplitude modulation and phase modulation, `Quadrature Amplitude Modulation <https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation>`_, (QAM) are deployed in today's digital communication systems.

Figure 1 shows a simplified first order poly phase circuit, as implemented in many quadrature demodulators such as the ADL5380. This simple poly phase circuit consists of complementary RC subcircuits. A low-pass transfer function from the input to one output shifts the phase by -45º at the corner frequency, and a high-pass transfer function to the other output shifts the phase by +45º at the corner frequency. The net phase difference between the two outputs will be 90º. If the R and C values of the two paths are matched, then both paths have the same corner frequency and, more importantly, the phase of one output tracks the other with a 90° phase shift for all frequencies. The relative amplitudes of the two output signals, ( LO I 0º and LO Q 90º ) will be only equal at the -3dB corner frequency of the two RC paths.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig1.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 1. Simplified First Order Poly phase Filter


Generation of quadrature local oscillator (LO) signals is an important functional block in sideband rejection heterodyne receivers. Quadrature accuracy, that is the phase accuracy of the in phase and quadrature 90º phase-shifted signals, directly determines the image reject ratio (IRR), an important specification determining the sensitivity of a receiver.

Materials:
~~~~~~~~~~

| ADALM1000 module
| Solder-less breadboard, and jumper wire kit
| 2 – 0.1 uF capacitors (marked 104)
| 2 – 1 KΩ resistors

Directions:
~~~~~~~~~~~

Build the poly phase filter circuit shown in figure 2 on your solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2, poly phase filter circuit


Hardware Setup:
~~~~~~~~~~~~~~~

The green squares indicate where to connect the ALM1000 module AWG, and scope channels. Open the Bode Plotting software tool in ALICE. Configure the frequency sweep to start at 100 Hz and stop at 20 KHz. Set CHA AWG Max value to 4.0 and the Min value to 1.0.

Check the box to sweep Channel A as in the Bode plotting window to measure the phase of one output path with respect to the other.

Procedure:
~~~~~~~~~~

Calculate the expected RC corner frequency based on the R and C values you used. Run a single sweep of the frequency and be sure to save your data to a .csv file for later use in Excel or other data analysis software.

Questions:
~~~~~~~~~~

Making all four quadrature phases:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One copy of the quadrature filter generates one pair of outputs 90 degrees apart, plus and minus 45 degrees with respect to AWG A. If we build a second quadrature phase filter and drive its input with the output of AWG B but set AWG B to be the complement, that is 180 degrees shifted with respect to AWG A, the quadrature filter generates a second pair of outputs plus and minus 45 degrees with respect to AWG B or plus and minus 135 degrees with respect to AWG A.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig2-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Two filters generate all four quadrature phases


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, AWG settings for generating a differential signal


The AIN and BIN scope input channels can be used to display two of the quadrature output at the same time but only 2. If we use an external 4 into 1 analog multiplexer to expand the BIN input we can display the AWG A input waveform and all four of the quadrature outputs.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, Using analog Mux to display all four quadrature phases


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig7.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 6, Analog Mux controls


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, All four quadrature phases plotted using Phase Analyzer


Effect of Component tolerance:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _questions-1:

Questions:
^^^^^^^^^^

| How do small differences in the component values change the relative phases?
| How would you tune or trip the circuit to account for these variations?

Single-ended to Differential conversion:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transformers are often used at high frequencies to convert a single ended, ground referenced, signal to a differential signal. The LTspice schematic shown in figure 8 shows a simulation using the HPH1-1400L 6 winding inductor as a 1:2 transformer with a center tapped secondary. The differential output of the transformer is connected to the same quadrature filter from figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, LTspice simulation schematic


Additional Materials:

| 1 HPH1-1400L 6 winding transformer
| 1 47 Ω resistor
| 4 470 Ω resistors
| 4 47 nF capacitors
| Using the HPH1-1400L six winding inductor we can connect it as a 1:2 center tapped transformer as shown in figure 9. The HPH1-1400L has a lower useable frequency limit and the values of the R and C in the quadrature filters needs to be scaled to a higher frequency.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, Using BALUN transformer, single ended to differential conversion


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10, Time display of quadrature outputs


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, Phase display of quadrature outputs


Differential Poly Phase Tuned Amplifier
---------------------------------------

By adding second order L-C and C-L low and high pass filter sections as differential output loads in a NPN differential amplifier we can generate all four 90º phases ( i.e. 0º, 90º, 180º and 270º ) of an input sine wave signal. Such a tuned amplifier is shown in figure 12.

.. _materials-1:

Materials:
~~~~~~~~~~

| ADALM1000 Lab module
| Solder-less breadboard, and jumper wire kit
| 4 – 2N3904 NPN transistors (Q\ :sub:`1`, Q\ :sub:`2` Q\ :sub:`3`, Q\ :sub:`4`)
| 2 – 10 mH inductor (Various other value inductors)
| 2 – 0.56 uF capacitors (marked 564)
| 1 – 0.1 uF capacitor (marked 104)
| 1 – 1 uF capacitor (marked 105)
| 2 - 10 Ω resistors
| 2 - 100 Ω resistors
| 1 - 470 Ω resistor
| 4 – 1 KΩ resistors
| 1 – 10 KΩ resistor
| Other resistors and capacitors as needed

| Negative 5 V power source (use one of the following options)
| \* LTM8067 uPower DC-DC converter Module
| \* LT1054 DC-DC Inverter
| \* 3 – 1.5 V AA Cells (or AAA cells) in battery holder for -4.5 V

.. _directions-1:

Directions:
~~~~~~~~~~~

Build the circuit shown in figure 12 on your solder-less breadboard. Set L\ :sub:`1` = L\ :sub:`2` = 10 mH and C\ :sub:`1` = C\ :sub:`2` = 0.56uF. R\ :sub:`1` should be equal to R\ :sub:`2` and use 1 KΩ for their value. Likewise, R\ :sub:`3` should be equal to R\ :sub:`4` and use 100 Ω for their value.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 12, Poly Phase Amplifier


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The green squares indicate where to connect the ALM1000 module AWG, scope channels and power supplies. The analog input Mux can again be used to display all four output phases.

Be sure to turn on the power supplies only after you double check your wiring. Be careful to never connect CHB to the -4.5 V supply or any other negative voltage node without using :doc:`a resistor divider/attenuator </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>`. Open the Bode Plotting tool in ALICE. Configure the frequency sweep to start at 100 Hz and stop at 20 KHz. Set the CHA Max value to 4.0 and the Min value to 1.0.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Calculate the expected LC corner frequency based on the L and C values used.

Turn on the power supplies. Connect CHB scope input alternately to each of the four possible outputs at the ends of resistors R\ :sub:`1`, R\ :sub:`2`, R\ :sub:`3` and R\ :sub:`4`. Run a single frequency sweep and store each sweep in a trace snapshot to compare each output's relative gain and phase response. Be sure to export the data from each frequency sweep to a .csv file for further analysis in either Excel or other analysis software.

Using the scope and waveform generator controls ( in the time domain ) set the CHA frequency to the resonate frequency. Observe the relative amplitudes and phases of the four outputs on channel B and store each trace as a reference to compare the amplitude and phase of each output.

.. _questions-2:

Questions:
~~~~~~~~~~

Appendix: External Analog Multiplexer
-------------------------------------

The use of just about any generic analog multiplexer integrated circuit is possible with the ADALM1000 to extend the number of voltage input channels. Here are two examples. The first example uses the common CD4052 (or 74HC4052) dual 4:1 analog switch. In addition the PDIP versions of the MAX4618 and MAX4582 are pin compatible with the industry-standard 74HC4052.

While the mux can be simply included on your solderless breadboard alongside the rest of the experiment it is often much more convenient to have it on an accessory plug in board as shown. Information and design files for this accessory board can be found in this web page and on GitHub, :doc:`M1k Accessory Board, Dual 4:1 Analog Input Multiplexer </wiki-migration/university/tools/adalm1000/accessory-boards-index>`.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/analog-mux-2.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure A1, M1k Mux accessory board


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/accesory-mux.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure A2, M1k Mux accessory board attached to poly phase filter and an M1k


Another analog mux board is this one based on the 16:1 CD74HC4067 from `SparkFun Analog/Digital MUX Breakout <https://www.sparkfun.com/products/9056>`_. A similar 8:1 analog multiplexer break-out board using the 74HC4051 circuit is also available from `SparkFun <https://www.sparkfun.com/products/13906>`_. It does not come with header connectors so they would need to be added. The pins on the connector do not line up with the M1k connectors so male to male jumpers would be needed as shown in the next figure.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/sparkfun-mux-1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure A3, SparkFun Analog Mux break-out board


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/sparkfun-mux.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure A4, CD4067 mux break out board attached to poly phase filter and an M1k


Appendix: Negative Power Supply Option, LT1054
----------------------------------------------

Refer to the :adi:`LT1054 datasheet <en/products/power-management/inductorless-charge-pump-dc-dc-converters/regulated-step-up-charge-pumps/lt1054.html>` for complete application information.

.. _materials-2:

Materials:
~~~~~~~~~~

| 1 – LT1054 Switch Cap DC-DC converter (or ADM660)
| 1 – 10 uF capacitor
| 1 – 22 uF capacitor

.. _directions-2:

Directions:
~~~~~~~~~~~

The simplest configuration for the LT1054 is the voltage inverter shown in figure A5. It can generate -5 V from the +5 volt power supply using just two capacitors. C\ :sub:`1` is typically 10 uF and C\ :sub:`2` can be anything larger than 10uF. When using electrolytic capacitors be sure to observe the polarity and connect the capacitor with the correct polarity. If connected backward, at best the circuit won't work, at worst you can damage either the capacitor or LT1054.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-poly-phase-fig4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure A5, Voltage Inverter to generate -5 V


**For Further Reading:**

http://www.microwavejournal.com/ext/resources/pdf-downloads/IQTheory-of-Operation.pdf

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**
