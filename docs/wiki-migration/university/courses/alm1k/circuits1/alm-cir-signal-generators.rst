How to Generate External Signal Sources
=======================================

Objective:
----------

The objective of this document is to present a number of options for the generation of external square wave (clock) and other signal sources to be used in conjunction with the ADALM1000 (M1k) or ADALM2000 (M2k) while performing certain Lab activities where the built-in AWG sources are being used for other purposes and may not be available or provide a high enough clock frequency.

General Notes:
--------------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CH A and CH B. The analog input only pins are referred to as AIN and BIN.

External Signal Source Options:
-------------------------------

If you are using one of the older model (D) ALM1000 boards with the 6 pin analog I/O connector you can only use the I/O channels as either an output or an input. This makes it very hard to simultaneously drive more than one input of the circuit being investigated while observing more than one other circuit node. If you are using one of the new model (F) ALM1000 boards with the 8 pin analog I/O connector then you can use the Split I/O modes in ALICE 1.2. This will allow you to use both AWG output pins, CHA and CHB, while observing other signal nodes with the AIN and BIN scope input pins.

Beyond using the split I/O mode, sometimes even 2 signal sources is not enough. The following are some options for generating additional signals using components found in the ADALP2000 Analog Parts Kit.

Option 0, Computer sound card outputs:
--------------------------------------

One alternative would be to use some other signal generator. A possible source for the analog input and square wave drive signals might be the stereo audio (headphone) output from a computer, laptop, tablet, or smart phone. There are a number of function generator programs or apps available for download on the web. The ADALP2000 Analog Parts Kit contains an audio connector adapter break out board (BOB) that can be used with a male to male headphone extension cable (not part of the kit) to connect to the breadboard as shown in figure 1. The left and right outputs need to be AC coupled by two capacitors. Any value around 1 uF or larger should work. The DC level is biased to the center of the 0-5 V range of the ALM1000 by connecting the resistors to the fixed 2.5V supply. 47 KΩ is a good starting value for the resistors. If the caps are polarized the + end should be connected to the resistors that set the DC level equal to +2.5 V.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, stereo audio output connector


It is important to note that the ground of the audio connector will likely be shorted to the USB ground that the ALM1000 uses if both are connected to the same computer. So be careful how you connect the ground.

The ADALP2000 Analog Parts Kit includes a 3.5 mm audio connector break-out-board, figure 1a, that can be inserted in a solderless breadboard. The board pins are numbered 1-5. Pin 1 is the sleeve (ground), Pin 2 is the tip (left audio) and Pin 3 is the ring (right audio).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig1a.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1a, stereo audio connector break-out-board


Adjustable DC source:
~~~~~~~~~~~~~~~~~~~~~

The ADALP2000 Analog Parts Kit also includes an AD5626 12 bit DAC break-out-board, figure 1b, that can be used to provide an adjustable DC voltage source. The 0 to 4 V output of the AD5626 serial interface DAC can be programed through the built-in interface in ALICE 1.2. The SCLK, SDIN and LDAC BAR inputs are controlled by three of the digital outputs from the ADALM1000 digital connector, figure 1c.

To use the AD5626 to set the DC offset of the audio signals, simply connect the end of the resistors in figure 1 to the DAC output rather than the fixed 2.5V.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig1b.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1b, AD5626 DAC break-out-board


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig1c.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1c, AD5626 DAC interface connections


Option 1, AD654:
----------------

The ADALP2000 Analog Parts Kit includes an AD654 voltage to frequency converter chip. This IC can be configured to generate an adjustable output frequency based on a timing resistor and capacitor and the voltage applied to the +V\ :sub:`IN` pin.

Materials:
~~~~~~~~~~

| 1 – 10Ω resistor
| 2 – 220 Ω resistors
| 1 – 1.5 KΩ resistor
| 1 – 4.7 KΩ resistor
| 1 – 5 KΩ potentiometer
| 1 – 2.2 nF capacitor (222)
| 1 – 0.56 uF capacitor (564)
| 1 – 10 uF capacitor
| 1 – AD654 Voltage-to-frequency Converter

Directions:
~~~~~~~~~~~

Figure 2 shows a typical configuration where the frequency control voltage on pin 4 is supplied from the fixed +2.5 V supply and adjusted by potentiometer R\ :sub:`2`. Alternately, the frequency could be adjusted by using the output of the AD5626, figure 1c, in place of the fixed supply. Timing resistor R\ :sub:`5` and timing capacitor C\ :sub:`2` set the overall frequency.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Voltage-to-frequency Converter square wave source


The square wave output of the AD654 on pin 1 is an open collector. In the schematic the collector load resistor R\ :sub:`4` is shown connected to +5 V to give a 0 to 5 V swing. R\ :sub:`4` could be connected to another voltage such as the +3.3 V supply on the digital connector or the +2.5 V supply. Pin 2 is the output or Logic common. It is normally connected directly to ground but could be connected to another node more positive than ground or through a resistor to make an output voltage of opposite phase.

Triangle Wave Generator
~~~~~~~~~~~~~~~~~~~~~~~

The AD654 voltage-to-frequency converter IC can also be the basis of a triangle wave generator. The normal output of the AD654 is an open collector digital square wave signal. The internal timing circuit of the AD654 however uses a ramp generator and this internal ramp waveform is available in differential form across the external timing capacitor connected to pins 6 and 7 in figure 2. We cannot use this triangle wave signal directly without disturbing the internal timing of the AD654. We can use the AD8226 instrumentation amplifier from the parts kit to buffer and convert the differential signal to a single ended signal. By adjusting the amplitude and offset of this triangle wave signal, it can be used to drive other test circuits.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

| 1 – 68 KΩ or 100 KΩ gain set resistor (and optional 50 KΩ pot)
| 1 – AD8226 instrumentation amplifier

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, V-to-F triangle wave generator


The output triangle wave will be centered on +2.5 V (voltage on pin 6) and the amplitude is set by the value of R\ :sub:`7`. Leaving R\ :sub:`7` open, sets the AD8226 gain to 1 and makes the smallest amplitude. A 100 KΩ resistor sets the gain to about 1.5 and 68 KΩ sets the gain to about 1.7. Using a 68 KΩ resistor (or any fixed resistor) in series with a 50 KΩ pot would allow the amplitude to be adjustable.

Option 2, AD8561:
-----------------

The ADALP2000 Analog Parts Kit includes two AD8561 high speed differential comparators. This IC can be configured as a Schmitt trigger oscillator circuit to generate an adjustable output frequency based on a timing resistor and capacitor. The AD8561 provides true and complement open collector outputs.

.. _materials-1:

Materials:
~~~~~~~~~~

| 3 – 1.0 KΩ resistors
| 1 – 20 KΩ resistor
| 1 – 47 KΩ resistor
| 1 – 5 KΩ potentiometer
| 1 – 4.7 nF capacitor (472)
| 1 – AD8561 Voltage Comparator

.. _directions-1:

Directions:
~~~~~~~~~~~

Shown in figure 4, R\ :sub:`1` provides positive feedback to the positive differential input to set the magnitude of the hysteresis. R\ :sub:`2` also influences the hysteresis and by connecting it to +2.5 sets the input common mode level. The combined series resistance of R\ :sub:`3` and the pot R\ :sub:`4` adjust the frequency. The minimum and maximum frequency can be set by changing capacitor C\ :sub:`1` and choosing different values for the resistors.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Relaxation oscillator using a Schmitt trigger


The voltage seen at the timing capacitor, C\ :sub:`1`, approximates a triangle wave. The LATCH control input, pin 5, can be used to gate the oscillator on and off. The state of the output when off can be either high or low and depends on where in the output waveform the rising edge of the LATCH signal occurred.

Option 3, LTC1485:
------------------

The ADALP Analog Parts Kit includes an LTC1485 high speed differential line driver/receiver. The differential receiver part can be configured as a Schmitt trigger oscillator circuit to generate an adjustable output frequency based on a timing resistor and capacitor.

.. _materials-2:

Materials:
~~~~~~~~~~

| 1 – 4.7 KΩ resistors
| 1 – 20 KΩ resistor
| 1 – 47 KΩ resistor
| 1 – 5 KΩ potentiometer
| 1 – 0.1 uF capacitor (104)
| 1 – LTC1485 differential receiver

.. _directions-2:

Directions:
~~~~~~~~~~~

Shown in figure 5, R\ :sub:`1` provides positive feedback to the positive differential input to set the magnitude of the hysteresis. R\ :sub:`2` also influences the hysteresis and by connecting it to +2.5 sets the input common mode level. The combined series resistance of R\ :sub:`3` and the pot R\ :sub:`4` adjust the frequency. The minimum and maximum frequency can be set by changing capacitor C\ :sub:`1` and choosing different values for the resistors.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Relaxation oscillator using a Schmitt trigger


The voltage seen at the timing capacitor, C\ :sub:`1`, approximates a triangle wave. The RE and DE control inputs, pins 2 and 3 tied together, can be used to gate the oscillator on and off. The state of the output when off can be either high or low depending on the state of the Din input, pin 4. If Din is low the output will be high when stopped and low if Din is high.

Option 4, LT1054:
-----------------

The CAP+ pin of the LT1054 switches between ground and the V+ supply voltage at the switching frequency of the DC-DC converter. This signal could be used as a square wave signal source. The internal oscillator runs at a nominal frequency of 25 KHz. The oscillator pin can be used to adjust the switching frequency. Oscillator pin 7 can be used to raise or lower the oscillator frequency or to synchronize the device to an external clock. Internally pin 7 is connected to the oscillator timing capacitor (Ct ≈ 150pF) which is alternately charged and discharged by current sources of ±7μA so that the duty cycle is ≈50%. The frequency can be raised, lowered, or synchronized to an external system clock if necessary. The frequency can be lowered by adding an external capacitor (C\ :sub:`1`, figure 6) from Pin 7 to ground. This will increase the charge and discharge time, which lowers the oscillator frequency.

The frequency can be increased by adding an external capacitor (C\ :sub:`2`, figure 6, in the range of 5pF to 20pF) from Pin 2 to Pin 7. This capacitor will couple charge into Ct at the switch transitions, which will shorten the charge and discharge time, raising the oscillator frequency. Synchronization can be accomplished by adding an external resistive pull-up from Pin 7 to the reference pin (Pin 6). A 20k pull-up is recommended. An open collector/drain logic gate or an NPN/NMOS transistor can then be used to drive the oscillator pin at the external clock frequency. Pulling up Pin 7 to an external voltage or driving with an external logic level is not recommended.

.. _materials-3:

Materials:
~~~~~~~~~~

| 1 – LT1054 Switch Cap DC-DC converter
| 1 – 5 KΩ potentiometer (optional for frequency adjustment)
| 2 – 39 pF capacitors (or other values for optional frequency adjustment)

.. _directions-3:

Directions:
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Using Internal Oscillator of LT1054


Option 5, LTC1043:
------------------

The LTC1043 is a monolithic, charge-balanced, dual switched capacitor building block. The internal oscillator of the LTC1043 runs at a nominal frequency of 190 KHz and its frequency can be adjusted with an external capacitor connected between the oscillator pin and ground.

The Cosc pin can be used with an external capacitor, Cosc, connected from Pin 16 to Pin 17, to modify the internal oscillator frequency. If Pin 16 is floating, the internal 24pF capacitor, plus any external interpin capacitance, set the oscillator frequency around 150 kHz with +5V supply.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig1043.png
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-osc-graph.png
   :align: center
   :width: 300px

There are four single-pole-double-throw (SPDT) switches in the LTC1043. By connecting the two ends of a switch to two different voltages, ground and +5 V for example, a square wave swinging between the two voltage levels will appear at the switch pole (center terminal) as shown in figure 7. The frequency of the output will of course be set by the value of C\ :sub:`OSC`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Configuration for 0 to 5 V square wave output


The phase of the square wave can be inverted by swapping the voltages connected to switch pins, 15 and 18 in the above example. Other voltage swings such as 0 to 2.5 V or 2.5 V to 5 V etc. are possible by selecting other voltage supplies for the switch pins.

Filtering a square wave to make a sine wave:
--------------------------------------------

The ADAPL2000 kit contains a number of inductors and capacitors that could be used to filter out the harmonics of a square wave to provide a sine wave at the same fundamental frequency as the square wave. The harmonic distortion level of the resultant sine wave will depend on how steep the filter cut off is and how close the square wave is to a 50% duty cycle.

In figure 8 is an example 1.5 KHz 5th order LC low pass filter. In this Pi configuration the two inductors, L\ :sub:`1` and L\ :sub:`2`, are the same value. For this example the 10 mH inductors from the kit are used. Capacitors C\ :sub:`1` and C\ :sub:`3` are the same value and two 1 uF caps are used. Capacitor C\ :sub:`2` needs to be about 2.4 uF so two 4.7 uF caps connected in series are used. With a 1.5 KHz square wave from the oscillator in figure 5 as the input, the harmonic distortion of the output sine wave is less than 2%. The second harmonic was the largest harmonic at about -32dB with respect to the amplitude of the fundamental.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, 5th order LC low pass filter


**For Further Reading:**

| :adi:`AD5626 datasheet <AD5626>`
| :adi:`AD654 datasheet <AD654>`
| :adi:`AD8561 datasheet <AD8561>`
| :adi:`LTC1485 datasheet <LTC1485>`
| :adi:`LT1054 datasheet <en/products/power-management/inductorless-charge-pump-dc-dc-converters/regulated-step-up-charge-pumps/lt1054.html>`
| :adi:`LTC1043 datasheet <LTC1043>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
