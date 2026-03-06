Activity: The Switched Capacitor
================================

Objective:
----------

The objective of this exercise is to explore the concepts of Switched Capacitor based circuits.

Concept:
--------

A switched capacitor is an electronic circuit element used in discrete time signal processing systems. It works by transferring charge into and out of a capacitor when switches are opened and closed. Usually, non-overlapping signals are used to control the switches, often termed Break before Make switching, so that all switches are open for a very short time during the switching transitions. Filters implemented with these elements are termed 'switched-capacitor filters'. Unlike analog filters, which must be constructed with resistors, capacitors and sometimes inductors whose values are accurately known, switched capacitor filters depend only on the ratios between capacitances and the switching frequency. This makes them much more suitable for use within integrated circuits, where the accurately specified absolute value of components such as resistors and capacitors are not economical to construct.

The switched capacitor resistor:
================================

The most simple switched capacitor circuit is shown in figure 1, the switched capacitor resistor. It consists of one capacitor C\ :sub:`1` and two switches S\ :sub:`1` and S\ :sub:`2` which connect the capacitor alternately to the input, V\ :sub:`IN` and the output, V\ :sub:`OUT`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a19_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Basic Switched Capacitor circuit


| Each switching cycle transfers a charge Δq from the input to the output at the switching frequency F. Recall that the charge q on a capacitor C with a voltage V between the plates is given by:
| q = CV
| Where V is the voltage across the capacitor. Therefore, when S\ :sub:`1` is closed while S\ :sub:`2` is open, the charge transferred from the input source to C is:
| q\ :sub:`IN` = C\ :sub:`1`\ V\ :sub:`IN`
| And when S\ :sub:`2` is closed while S\ :sub:`1` is open, the charge transferred from C\ :sub:`1` to the output is:
| q\ :sub:`OUT` = C\ :sub:`1` V\ :sub:`OUT`
| The charge transferred in each cycle is:
| Δq = q\ :sub:`OUT` - q\ :sub:`IN`\ = C\ :sub:`1`\ ( V\ :sub:`OUT` - V\ :sub:`IN` )
| Since a charge Δq is transferred at a rate F, the rate of transfer of charge per unit time is:
| I = ΔqF
| Note that I is used, the symbol for electric current, for this quantity. This is to demonstrate that a continuous transfer of charge from one node to another is the same as current. Substituting for Δq in the equation above, we get:
| I = C\ :sub:`1`\ ( V\ :sub:`OUT` - V\ :sub:`IN` ) F
| We define ΔV, the voltage across the circuit from input to output, as:
| ΔV = V\ :sub:`OUT` - V\ :sub:`IN`
| We now have a relationship between I and V, which we can rearrange to give an equivalent resistance R:
| R = V / I = 1 / (C\ :sub:`1` F)
| Thus, the circuit behaves like a resistor whose value depends on C\ :sub:`1` and F.

The Switched Capacitor resistor is often used as a replacement for simple resistors in integrated circuits because it is easier to fabricate reliably with a wide range of values. It also has the benefit that the equivalent resistor value can be adjusted by changing the switching frequency.

This same circuit can be used in discrete time systems (such as analog to digital converters) as a track and hold circuit. During the appropriate clock phase, the capacitor samples the analog voltage through switch one and in the second phase presents this held sampled value to an electronic circuit for processing.

For further reading on switched capacitors:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://en.wikipedia.org/wiki/Switched_capacitor

Example Circuit
===============

The next step is to build an example circuit using the Switched Capacitor as a resistor. By adding a second capacitor C\ :sub:`2` across the output of figure 1, we get the RC low pass circuit shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a19_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Switched Capacitor RC low pass filter


Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - CD4007 ( configured as SPDT analog switch )
| 1 - 0.0047uF capacitor
| 1 - 100pF capacitor
| Below in figure 3 is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/cd4007.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 3 CD4007 CMOS transistor array pinout


Directions:
-----------

The breadboard connections are as shown in figure 4. If you are using the power supplies from the ADALM2000 hardware be sure that they are turned off or disconnected while you construct the circuit. The scope inputs should be connected to measure the input and output of the RC filter. The circuit will operate from the +/- 5V supplies provided from the ADALM2000 board but better performance will be observed if a +/- 5V bench power supply is used. A +/- 5V square wave digital signal from AWG2 drives the CD4007 inverter input at pin 6 and the gate of switch devices M\ :sub:`5` and M\ :sub:`6`. The inverted output at pins 8,13 drives the gates of switch devices M\ :sub:`3` and M\ :sub:`4`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a19_f4.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 4 Switched capacitor RC low pass filter


Hardware Setup:
---------------

Waveform generator W1 should be configured as a 100 Hz sine wave with a 1 mV amplitude peak-to-peak and zero offset to start out. Waveform generator W2 should be configured as a 100 KHz square wave with a 10 V amplitude peak-to-peak and zero offset. Scope channel 1 should be connected to the input of the filter and Scope channel 2 should be connected to the output of the filter.

Procedure:
----------

Turn on the power supplies and enable both AWG channels. Using the oscilloscope display observe the output amplitude of the filter relative to the input as you change the input frequency, AWG1. Also note any changes in the output amplitude as you change the switching frequency by adjusting the frequency of AWG2. Stop and close the Oscilloscope screen and now open the Network Analyzer instrument ( Bode plotter ). You will need to disable AWG channel 1 on the waveform generator screen but keep channel 2 enabled and set to 100 KHz, 10 V amplitude peak-to-peak, zero offset as it was previously. Set up the Analyzer to sweep the filter input from 100 Hz to 10 KHz. Run sweeps with AWG2 set to 100 KHz, 200 KHz and 500 KHz. Export the data for each sweep to a .csv file and using a spreadsheet program like Excel make plots of the amplitude and phase vs. frequency similar to the plots in figure 5 and 6.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a19_f5.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 5 Amplitude plot


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a19_f6.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 6 Phase plot


Note that the amplitude curve for 200 KHz switching frequency crosses the -5 dB line at exactly twice the input frequency as the 100 KHz curve. And that the 500 KHz curve crosses at a frequency 2.5 times the frequency of the 200 KHz curve.

Questions:
----------

Determine the equivalent resistance and RC time constant for each switching frequency, 100HKz, 200KHz and 500KHz.

How well do these Bode plot curves match a simple RC low pass filter response?

Switched capacitor differencing circuit
=======================================

.. _objective-1:

Objective:
----------

The objective of this activity is to extend the switched capacitor concept beyond the single capacitor and switches circuit that can be built around the CD4007 transistor array. More complex configurations require multiple capacitors and switches. Analog switches and multiplexers such as the CD4066 and CD4053 can be used.

.. _materials-1:

Materials:
----------

| 1 - CD4053B triple analog SPDT switch
| 2 - 1 nF capacitors (102 )
| |image1|

.. container:: centeralign

   Figure 7 CD4053 Block diagram / Pinout


Description:
------------

A switched capacitor differential to single ended configuration is shown in figure 8. Build this circuit on your solder-less breadboard using two of the three SPDT analog switches in the CD4053. V\ :sub:`DD` of the CD4053 should be connected to the +5 V power supply ( Vp ) and V\ :sub:`EE` connected to the -5 V power supply ( Vn ) and finally with V\ :sub:`SS` connected to ground. The differential inputs, V\ :sub:`IN+` and V\ :sub:`IN -` should be connected to the waveform generator outputs AWG1 and AWG2 respectively. The single ended output, V\ :sub:`OUT` should be connected to scope channel 1+.

Switch control signals for both switches A and B should both be connected to digital pin DIO 0. Be sure to connect the inhibit input ( pin 6 ) to ground to enable all the switches. It is probably also a good idea to ground the unused C control input as well.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a19_f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8 differential to single ended circuit


.. _hardware-setup-1:

Hardware setup:
---------------

Open up the Digital Patterns screen. Click on the green plus sign to add signals. Select DIO 0 and click on the ADD button. Open the edit parameters screen for DIO 0. The output should be set for PP (for push-pull), type should be set as clock, duty cycle set to 50% and set the frequency for 100 KHz. Close the edit window. Lastly, hit the Run button

.. _procedure-1:

Procedure:
----------

Start with AWG1 and AWG2 both set up for sine waves with equal amplitudes of 500 mV peak-to-peak and zero offset but with AWG2 set with 180 degree phase. This will result with a differential signal with 2 V amplitude peak-to-peak. Observe the signal at the output and record the minimum and maximum values along with the DC ( average ) value of the output.

Repeat these measurements with the DC offset of both AWG1 and AWG2 set to 250 mV, 500 mV, -250 mV and -500 mV.

.. _questions-1:

Questions:
----------

Add questions here:

For Further Reading
-------------------

http://en.wikipedia.org/wiki/Switched_capacitor

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/cd4053.png
   :width: 550px
