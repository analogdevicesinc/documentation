Activity: Generating a Negative Voltage Reference
=================================================

Objective:
----------

The objective of this lab activity is to investigate ways to produce negative reference voltages. Positive voltage references or regulator configurations are more commonly available. Conventional methods of generating a negative reference voltage from a positive voltage involve inverting op-amp stages which tend to rely on precision matched resistors for accuracy.

Background:
-----------

In figure 1(a) the simple zener diode circuit, consisting of R\ :sub:`Z` and D\ :sub:`Z` from the zener diode regulator lab activity[1], is used to produce a positive reference voltage, +V\ :sub:`REF`. In a positive voltage reference a non-inverting op-amp buffer is often included to scale the output voltage and supply any current needed in the load. The obvious method for generating a negative reference voltage is to instead use an inverting op-amp stage as shown in the figure. This approach requires two precision matched resistors, R\ :sub:`1` and R\ :sub:`2`. Errors in the matching, in addition to any offset voltage in the op-amp, will produce errors at the negative output -V\ :sub:`REF`. However, one potential side benefit of this inverting amplifier configuration is that -V\ :sub:`REF` need not have the same absolute value as +V\ :sub:`REF`. The negative reference voltage can be scaled up or down by altering the ratio of R\ :sub:`1` and R\ :sub:`2`. The alternate configuration we will be investigating in this lab activity is shown in figure 1(b). It generates a negative reference voltage without the dependence on ratio matched resistors, potentially providing higher accuracy with fewer components.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/anr_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Generating a negative voltage reference


By examining figure 1(a) we see that, by the virtual ground nature of the inverting op amp configuration, the zener voltage +V\ :sub:`REF` is impressed across resistor R\ :sub:`1`. If R\ :sub:`2` is exactly equal to R\ :sub:`1` this same voltage V\ :sub:`REF` will also appear across R\ :sub:`2` but with the sign reversed with respect to ground. Since the voltage across R\ :sub:`2` is the same as that across the zener diode we can in effect replace R\ :sub:`2` with the diode in the feedback loop as in figure 1(b) and still produce the same voltage at -V\ :sub:`REF`. R\ :sub:`Z` simply sets the bias current level in the zener much as R\ :sub:`Z` in 1(a). In 1(b) I\ :sub:`Z` is equal to V\ :sub:`DD`/R\ :sub:`Z` where in 1(a) I\ :sub:`Z` is equal to (V\ :sub:`DD` - +V\ :sub:`REF`)/R\ :sub:`Z`. To design for the same I\ :sub:`Z` in both cases we simply change the value of R\ :sub:`Z`. Capacitor C\ :sub:`1` decouples the reference diode between its ground and output terminals. In addition low inductance 0.1 µF supply decoupling capacitors (not shown in the figure) are often connected to +V\ :sub:`DD` and -V\ :sub:`SS` very close to the op-amp.

Circuit Description
~~~~~~~~~~~~~~~~~~~

In theory this circuit can be built using almost any three terminal voltage reference circuit and a low noise, low offset operational amplifier. The lab activities on band-gap reference circuits [2] [3] [4] use NPN transistors to build positive voltage references. To build a negative reference based on the band-gap concept we would require high quality PNP transistors and the PNPs generally available in IC processes are not as high quality as the available NPN devices. These NPN based band-gap circuits will provide a couple of examples we can used to explore this negative reference configuration. The first circuit iteration in step 1 of this lab will use a diode as a reference and further iterations will substitute NPN transistor based two terminal ( shunt ) and three terminal ( series ) circuits as the reference element.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 4.7 KΩ resistor
| 2 - 1.5 KΩ resistors
| 2 - 20 KΩ resistors
| 1 - 2.2 KΩ resistor
| 1 - 100 Ω resistor
| 1 - 10 KΩ variable resistor (potentiometer)
| 4 - small signal NPN transistors (2N3904 and SSM2212)
| 2 - LEDs (any color will do)
| 1 - OP482 or OP484 quad op-amp
| 1 - 1 nF Capacitor
| 2 - 0.01 uF Capacitors
| 2 - 0.1uF Capacitors ( supply decoupling capacitors for + and - 5 V supplies )

Directions Step 1:
------------------

The zener diode ( 1N4735 ) supplied in the ADALP2000 Analog Parts Kit is a 6.1 volt diode. 6.1 volts is much too high a reverse breakdown voltage to build this circuit using the fixed +/- 5 volt power supplies of the ADALM2000 hardware. The forward voltage of an LED is in the range of 1.6 to 2.0 volts depending on the color of the diode. While not a proper reference diode, we can build the circuit for instructional purposes using the LEDs from the ADALP2000 Analog Parts Kit.

Build both of the versions of the circuits in figure 1(a) and 1(b) as shown in figure 2 on your solder-less breadboard. Use two LEDs preferably of the same color. Green LEDs will have a higher forward voltage drop than red or yellow. We want the diode current, I\ :sub:`D`, to be about 1 mA and the as close to this same value in both versions of the circuit. In the case (b) I\ :sub:`D` will be +5/R\ :sub:`4` so a 4.7 KΩ resistor would give about 1 mA. In case (a) I\ :sub:`D` will be (+5-V\ :sub:`D`)/R\ :sub:`3`. If we use 2 V as an estimate for V\ :sub:`D`, then R\ :sub:`3` would be around 3 KΩ. You can get 3 KΩ by connecting two 1.5 KΩ resistors from the Parts Kit in series. Also for case (a) we need to pick values for R\ :sub:`1` and R\ :sub:`2`. We want the current in R\ :sub:`1` to be much smaller than the current in R\ :sub:`3`. So setting R\ :sub:`1` and R\ :sub:`2` to a much higher value such as 20 KΩ should satisfy that condition.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/anr_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, LED based volt regulator example


Hardware setup:
---------------

Open the voltage supply control and the voltmeter instrument windows from the Scopy software. A DMM, if available, could be useful to more accurately measure the DC voltages in the circuit than the Scopy voltmeter instrument.


|image1|

.. container:: centeralign

   Figure 3 LED based volt regulator breadboard connections


Procedure:
----------

Turn on both the positive and negative power supplies. Observe the two voltages at -V\ :sub:`REF`, pins 8 and 14 of the op amp and at +V\ :sub:`REF` on the LED.


|image2|

.. container:: centeralign

   Figure 4 Scopy voltmeter


Questions:
----------

What voltage did you measure at -V\ :sub:`REF`\ for the circuits (a) and (b)? What voltage did you measure at the LED? Are these the correct expected values and why?

Directions Step 2:
------------------

Modify your breadboard setup from step 1 as shown in figure 3. Be sure to turn off the power supplies before making any modifications to your breadboard. Replace the LED diode with the shunt regulator stage from earlier lab [3]. Resistors R\ :sub:`1`, R\ :sub:`2` and transistor Q\ :sub:`1` are connected as the zero gain amplifier from the earlier lab [5]. Resistor R\ :sub:`3` and transistor Q\ :sub:`2` are added as in the stabilized current source lab [6]. If the SSM2212 matched NPN pair is used it is best that it be used for devices Q\ :sub:`1` and Q\ :sub:`2`. Q\ :sub:`3`\ is added as common emitter stage, its base connected to the collector of Q\ :sub:`2` and collector connected to the combined node of R\ :sub:`1`, R\ :sub:`3` R\ :sub:`4`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/anr_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5 NPN shunt band-gap reference example


.. _hardware-setup-1:

Hardware setup:
---------------

The setup is the same as step 1.


|image3|

.. container:: centeralign

   Figure 6 LED based volt regulator example


.. _procedure-1:

Procedure:
----------

Turn on both the positive and negative power supplies. Observe the voltage at -V\ :sub:`REF`, pin 14 of the op amp and across the band-gap shunt regulator (collector and emitter of Q\ :sub:`3`) . You can adjust potentiometer R\ :sub:`3` to produce a -1.25V reference voltage.

Testing supply headroom
~~~~~~~~~~~~~~~~~~~~~~~

To test the headroom requirements for +V\ :sub:`DD`, disconnect the fixed positive power supply from +V\ :sub:`DD` and remove any supply decoupling capacitors. Be sure to turn off the power supplies before making any changes or additions to your breadboard. Now connect +V\ :sub:`DD` to AWG 1. Set AWG 1 to trapezium (trapezoid) waveform at 100 Hz. Set the amplitude to 5V peak-to-peak with a 2.5V offset for a 0 to +5V swing. Connect scope channel 1 to the output of AWG1 and connect scope channel 2 to -V\ :sub:`REF` of the first example circuit at pin 14 of the OP482. Use the oscilloscope instrument in the XY mode, scope channel for X and scope channel 2 for Y. Start AWG 1 and turn on the fixed negative 5V power supply. Record the minimum +V\ :sub:`DD` voltage where -V\ :sub:`REF` starts to remain constant at -1.25V.

To test the headroom requirements for -V\ :sub:`SS`, reconnect +V\ :sub:`DD` to the fixed positive power supply. Disconnect the fixed negative power supply from -V\ :sub:`SS` and remove any supply decoupling capacitors. Now connect -V\ :sub:`SS` to AWG 1. Set the amplitude to 5V peak-to-peak with a -2.5V offset for a 0 to -5V swing. Start AWG 1 and turn on the fixed positive 5V power supply. Repeat your measurements of pins 14 of the OP482 recording the lowest value for -V\ :sub:`SS` where the reference voltage is constant.

Directions Step 3:
------------------

Modify your breadboard setup from step 1 as shown in figure 4. Be sure to turn off the power supplies before making any modifications to your breadboard. Change the two terminal, shunt, regulator used in step 2 to the three terminal reference [2] by adding emitter follower stage Q\ :sub:`4`, and compensation capacitor C\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/anr_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7 NPN three terminal band-gap reference example


.. _hardware-setup-2:

Hardware setup:
---------------

The setup is the same as step 1.


|image4|

.. container:: centeralign

   Figure 8 LED based volt regulator example


.. _procedure-2:

Procedure:
----------

Turn on both the positive and negative power supplies. Observe the voltage at -V\ :sub:`REF`, pin 14 of the op amp and across the band-gap three terminal regulator (emitter of Q\ :sub:`4` and emitter of Q\ :sub:`3`).

Repeat the supply headroom tests you did in Step 2 for this configuration. Are there any differences?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/neg_voltage_ref_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/neg_voltage_ref_ltspice`
   


For further reading:
~~~~~~~~~~~~~~~~~~~~

| [1] :doc:`Activity: Zener Diode Regulator </wiki-migration/university/courses/electronics/electronics-lab-26>`, :doc:`EPS Activity: Zener Diode Regulator </wiki-migration/university/courses/eps/zener-regulator>`
| [2] :doc:`Activity 9. Regulated Voltage Reference </wiki-migration/university/courses/electronics/electronics-lab-9>`
| [3] :doc:`Activity 10. Shunt regulator </wiki-migration/university/courses/electronics/electronics-lab-10>`
| [4] :doc:`EPS Activity: The Band-Gap Voltage Reference </wiki-migration/university/courses/eps/band-gap-regulator>`
| [5] :doc:`Activity 7. Zero gain amplifier (BJT) </wiki-migration/university/courses/electronics/electronics-lab-7>`
| [6] :doc:`Activity 8. Stabilized current source (BJT) </wiki-migration/university/courses/electronics/electronics-lab-8>`
| :adi:`OP482` datasheet

Return to Lab Activity :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

Appendix:
~~~~~~~~~

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/anr_f2bb.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/anr_f2ss.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/anr_f6.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/anr_f8.png
