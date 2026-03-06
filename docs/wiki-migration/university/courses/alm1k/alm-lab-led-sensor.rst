Activity: LED as light sensor, For ADALM1000
============================================

Objective:
----------

The objective of this Lab activity is to explore the use of LEDs as a photodiode light sensor and the use of NPN and Darlington connected NPN transistors as interface circuits for the light sensor.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

When exposed to light photodiodes produce a current that is directly proportional to the intensity of the light. This light generated current flows in the opposite direction to current in a normal diode or LED. As more photons hit the photodiode the current increases causing a voltage across the diode. As the voltage across the diode increases the linearity decreases.

In addition to emitting light, an LED can be used as a photodiode light sensor / detector. This capability may be used in a variety of applications including ambient light level sensor and bidirectional communications. As a photodiode, an LED is sensitive to wavelengths equal to or shorter than the predominant wavelength it emits. A green LED would be sensitive to blue light and to some green light, but not to yellow or red light. For example, a red LED will detect light emitted by a yellow LED and a yellow LED will detect light emitted by a green LED but a green LED will not detect light emitted by a red or yellow LED. All three LEDs will detect "white" light or light from a blue LED. White light contains a blue light component which can be detected by the green LED. Recall that visible light wavelengths can be listed from longest wavelength to shortest wavelength as Red, Orange, Yellow, Green, Blue, Indigo, Violet (remember the mnemonic "Roy G. Biv"). Violet is the shortest wavelength light with the most energetic photons and red has the longest wavelength light with the least energetic photons of all of the visible colors of light. LED's with clear plastic encapsulation will be more sensitive to broad-spectrum illumination (like general room lighting) than LED's with colored encapsulation (such as those included in the Analog Parts Kit).

To use the LED as an optical detector, do not forward bias the LED into quadrant # 1 of the current-voltage (I-V) curve. (Quadrant 1 is when the operating voltage and current are both positive.) Allow the LED to operate in the solar cell mode, quadrant #4 (operating voltage is positive, current is negative), or in the photodiode mode quadrant #3 (operating voltage is positive, current is negative). In the solar cell mode, no applied bias voltage is used. The solar cell (or LED in this case) generates its own current and voltage.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 2 - 2N3904 NPN transistors ( or SSM2212 NPN matched pair )
| 1 - 100KΩ resistor
| 1 - 2.2KΩ resistor
| 3 - LEDs ( multiple red, yellow and green colors )
| 1 - Infrared LED ( QED-123 )

Directions:
~~~~~~~~~~~

On your solder-less breadboard construct the LED light sensor circuit as shown in figure 1. Notice that the LED diode, D\ :sub:`1`, is reverse biased i.e. opposite to how it would be connected as a light emitter. The photo generated current will flow into Q\ :sub:`1` as base current and will appear in the collector multiplied by the current gain, ß of the transistor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-led-pd_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 LED and single common emitter NPN light sensor


Hardware Setup:
~~~~~~~~~~~~~~~

Use the fixed +5 V power supply from the ALM1000 module to power your circuit. You can use either scope channel A or B to monitor the voltage at the collector node of Q\ :sub:`1`.

Procedure:
~~~~~~~~~~

Insert a red, yellow or green LED into the circuit as shown one at a time. Try exposing the three different color LEDs from your Analog Parts Kit to different light sources such as standard incandescent, florescent and LED lights held at differing distances from the sensor LED. Observe the voltage waveform seen at the collector of Q\ :sub:`1`. Try inserting the infrared LED from your kit and observing how it responds to the light from the different sources. Try increasing the sensitivity or gain by increasing the value of R\ :sub:`L` to 200KΩ or 470KΩ.

Step 2 Directions:
------------------

Change the circuit on your breadboard to the `Darlington configuration <https://en.wikipedia.org/wiki/Darlington_transistor>`__ shown in figure 2. Be sure to turn off the power supply before making any changes to the circuit. With the Darlington connected transistors the emitter current of Q\ :sub:`2` becomes the base current of Q\ :sub:`1` such that the photo generated current from the LED D\ :sub:`1` is now multiplied by ß\ :sup:`2` and will appear in the load resistor R\ :sub:`L` from the collectors of Q\ :sub:`1` and Q\ :sub:`2`. Because of this much higher current gain we can use a much lower value load resistor.

Step 2 Procedure:
~~~~~~~~~~~~~~~~~

Repeat the same procedure of inserting the various LEDs into the circuit for D\ :sub:`1` and measuring the response to the various light sources and record them in your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-led-pd_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 LED and Darlington connected NPN light sensor


Questions:
~~~~~~~~~~

| How well does the red LED respond to the various light sources?
| Does it respond to another red or yellow or green LED used as a light emitter?
| How about the yellow and green LEDs?
| Is the infrared LED sensitive to the same or different wavelengths of light compared to the visible light LEDs?
| Which is the most sensitive to standard household lights such as incandescent and compact florescent bulbs?

| How does the sensitivity of the Darlington connected configuration compare to the single common emitter configuration?
| Are the minimum and maximum voltages the same for both configurations? If not why?

**For Further Reading:**

| `LEDs <https://en.wikipedia.org/wiki/LED>`__
| `LED circuits <https://en.wikipedia.org/wiki/LED_circuit>`__
| `Photo diodes <https://en.wikipedia.org/wiki/Photodiode>`__

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
