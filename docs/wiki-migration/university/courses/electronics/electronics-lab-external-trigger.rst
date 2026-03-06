Activity: Adjustable External Triggering Circuit
================================================

Objective:
----------

The objective of this lab activity is to investigate a circuit to interface analog signals to the digital external trigger input(s) of the ADALM2000 module.

Background:
-----------

The ADALM2000 scope module is most often triggered from one of the analog input channels. This will display stable waveforms with the horizontal time scale ( align zero time point ) based on whichever channel is selected as the trigger source. It is sometimes desirable to trigger the display ( zero time point reference ) using a third signal from some other point in the circuit being tested. The ADALM2000 hardware provides two external digital inputs, T1 and T2, which can be selected as trigger inputs. Using these digital inputs the displayed waveforms will align ( set the zero time point ) with the rising edge of the applied signal. These are however digital inputs and only allow input voltages between 0 and +5V and have a fixed threshold voltage. In order to use these external trigger inputs with analog input signals, that is to say between -5 V and +5 V, a voltage comparator circuit along with a adjustable voltage source to set the trigger voltage level are needed. In this lab activity an example circuit will be explored

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - AD8561 comparator ( or AD790 alternate with slightly different pinout )
| 1 - 74HC04 Hex CMOS inverter ( or CD4007 see Appendix )
| 3 - 1 KΩ resistors
| 1 - 1 megaΩ resistor
| 1 - 10 KΩ potentiometer
| 1 - 0.1 uF capacitor
| 1 - 0.0047 uF capacitor

Directions:
-----------

Build the circuit shown in figure 1 on your solder-less breadboard. The AD8561 analog comparator has non-inverted (true) and inverted (complement) outputs. The input of the first inverter can be alternately connected to either the pin 7 output, for a rising edge, or the pin 8 output, for a falling edge trigger. Start with it connected to pin 7. The 74HC04 hex inverter is suggested but a CD4069 hex inverter may be substituted or the two inverters can be built using the CD4007 transistor array supplied in the Parts Kit ( see Appendix ).

The AD8561 has a very high bandwidth and will respond to any high frequency noise that might be present on the input signal. This will cause its output(s) to switch back and forth multiple times very quickly if the input signal is near the threshold voltage (V\ :sub:`TH`). This noise will cause the waveform displayed on the screen to jump or "jitter" back and forth and look unstable. Resistor R\ :sub:`5` and capacitor C\ :sub:`1` form a low pass filter and are inserted between the two inverter stages to reduce these very fast switching spikes. The time constant of this filter would be adjusted based on the nature of the signal being used as the external trigger.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/aet_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Analog trigger circuit


Hardware Setup:
---------------

Waveform generator AWG1 should be set up as a triangle wave with a 8 Volt amplitude peak-to-peak and 0 V offset and a frequency of 5 KHz. Set the horizontal and vertical scales of the scope to display at least one complete cycle of the input triangle waveform. Turn on the power supplies only after double checking your circuit connections.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/adjustableexternaltriggering_hardwaresetup1.png
   :align: center

.. container:: centeralign

   Figure 2: Analog trigger circuit Breadboard Circuit


Procedure:
----------

To start, set the scope trigger source to Channel 1, rising edge, with the level set to 0 V. You should see the rising edge of the triangle wave on channel 1 centered on the 0 time point along the horizontal axis. The rising edge of the digital output of the second inverter on channel 2 should occur at different times along the horizontal axis depending on the setting of the potentiometer, R\ :sub:`3`. Adjust R\ :sub:`3` up and down from one end of its range to the other and observe where the rising edge of the pulse on channel 2 occurs with respect to the voltage (vertical axis) of the triangle wave at that time point.


|image1|

.. container:: centeralign

   Figure 3: Scope Shot at oscilloscope Channel 1's rising edge trigger on different potentiometer value


Now switch the scope trigger source to external 1 (T1 input) and repeat the sweep of R\ :sub:`3` from one end of its range to the other. You should be able to align the 0 time point anywhere along the rising edge.



|image2|

.. container:: centeralign

   Figure 4: Scope Shot at oscilloscope External Trigger's rising edge on different potentiometer value


Now move the input of the first inverter to pin 8 of the AD8561. The 0 time point should now align with the falling edge of the input triangle wave. Again repeat the sweep of R\ :sub:`3` to confirm that you are able to align the 0 time point anywhere along the falling edge.

Questions:
----------

What is the purpose of the 1 megOhm resistor connected from the non-inverting input of the AD8561 to ground? What other components could you add to the input to allow input voltages beyond the +/- 5 volt power supply limits?

What methods, other than the RC filter, could be used to remove the noise jitter from the comparator? (Hint: see the For Further Reading section) Are there any advantages or disadvantages with using one method or the other?

For Further Reading:
~~~~~~~~~~~~~~~~~~~~

:adi:`Ask The Applications Engineer <media/en/technical-documentation/frequently-asked-questions/vol23n4.pdf>` - High-speed comparators provide many useful circuit functions when used correctly.

:adi:`Curing Comparator Instability with Hysteresis <library/analogDialogue/archives/34-07/comparators/comparators.pdf>`

**Return to Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

Appendix: Making an inverter with the CD4007 transistor array
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/cd4007.png
   :align: center
   :width: 400px

.. container:: centeralign

   CD4007 CMOS transistor array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one to configure as shown below is by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f8.png
   :align: center
   :width: 550px

The second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input. The third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/adjust_ext_trigger_bb`
   


.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/adjustableexternaltriggering_scopeshot1.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/adjustableexternaltriggering_scopeshot2.png
