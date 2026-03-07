A Simple Light Detector
=======================

.. image:: https://wiki.analog.com/_media/analogTV>5040287147001
   :alt: analogTV>5040287147001
   :align: right

Introduction
------------

Light detectors are used in many diverse applications. In automobiles, solar sensors mounted in the dash pad are used to detect the intensity and angle of the sunlight passing through the windshield in order to provide information that is used to turn the headlights on and off and operate automatic climate control systems. Systems can be galvanically isolated from each other by using light to transmit signals from one system to another; dedicated devices for this application are available that are called "opto-isolators" and "opto-couplers." Solar sensors placed on the tops of streetlights and near lamp posts are used to turn the lights on and off as a function of ambient outdoor sunlight level. In these applications it's important to point the sensor away from the light source in order to prevent positive feedback, which results in an unstable oscillation. In these unstable situations the sensor receives too much light from the light source. When the light turns on, the sensor indicates a high light level (incorrectly interpreted as a high sunlight level) and thus sends a command to turn the light off. If it is dark out, the sensor indicates a low light level when the light is off and thus sends a command to turn the light on. This oscillatory behavior continues until somebody corrects the situation or the light bulb burns out. Have you ever seen a light on a lamp post rapidly turning on and off in the evening?

In this lab we use an infrared LED as a light source and a phototransistor to detect the light emitted by the LED. Infrared light is composed of light radiation with wavelengths in the 700 nm to 1000 nm range, a little longer than visible red light, and therefore infrared light cannot be seen by the naked eye. The phototransistor operates as a bipolar transistor with light as the effective input to its base. The phototransistor can respond to wavelengths contained in sunlight and ambient room light, and these can interfere with the its desired operation. An optical daylight filter is placed around the phototransistor in order to precvent this unwanted interference.

Objective
---------

To learn how a phototransistor works and how to use it to make a light detector with a continuously variable output voltage. To learn how to convert the continuously variable output to a binary output using a comparator. To see how signals can be converted to light and transmitted from one system to another without the need for a galvanic connection between the two systems (ours will have a common ground, but this is not necessary). Upon completion of this lab you should be able to understand the basic operation of light detectors and describe how signals can be communicated among systems using light in place of galvanic connections.

Materials and Apparatus
-----------------------

-  Data sheet handout for the QED123 infrared LED
-  Data sheet handout for the QSD123 infrared phototransistor
-  Data sheet handout for AD8561 voltage comparator
-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (1) QED123 from the ADALP2000 Analog Parts Kit
-  (1) QSD123 from the ADALP2000 Analog Parts Kit
-  (1) AD8561 from the ADALP2000 Analog Parts Kit
-  (1) Red LED from the ADALP2000 Analog Parts Kit
-  (1) 100 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 470 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 1.0 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 2.2 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 4.7 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 6.8 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 10 μF capacitor from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Construct the following LED transmitter and phototransistor receiver circuitry on the solderless breadboard\


|lab_7_image_1.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard (note that the LED and phototransistor must face each other)\

|lab_7_assembly_image_1.png|

-  Run PixelPulse on the computer and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Connect the M1K to the circuit as indicated in the schematic
-  Set up PixelPulse to measure voltage on Channel A
-  Measure and record the voltage on Channel A
-  Move a ruler or similar opaque object between the LED and the phototransistor and record the voltage on Channel A
-  Move the object very slowly back and forth from completely between the LED and phototransistor to completely away from the LED and phototransistor and observe and record the behavior of the voltage on Channel A
-  Add the following comparator circuit to the breadboard (note that this is the same comparator with hysteresis that was used in the Simple Proximity Sensor lab)\

|lab_7_image_2a.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_7_assembly_image_2a.png|

-  Move the object very slowly back and forth from completely between the LED and phototransistor to completely away from the LED and phototransistor and observe and record the behavior of the Red LED
-  Modify the infrared LED and phototransistor circuit as shown in the following schematic\

|lab_7_image_3.png|

-  Refer to the illustration below for one way to make the modifications to the LED and phototransistor circuits\

|lab_7_assembly_image_3a.png|

-  Set up Channel B to source voltage and measure current
-  Generate a 0.0 V to 5.0 V 1 KHz square wave on Channel B
-  Observe and describe the waveform on Channel A and describe the changes observed on Channel A
-  Explain the behavior of the signal observed on Channel A

Theory
------

The QED123 LED converts electric current into infrared light and the phototransistor converts the photons impinging onto its base area into an effective base current that controls its collector current. In this lab, the phototransistor is connected in a common-emitter configuration with a 1.0 KΩ collector resistor. Phototransistors can also be operated in common-collector configurations. As the power of the light impinging on the phototransistor increases, the collector current increases, causing the collector voltage to drop due to the voltage drop across the collector resistor. The collector current reaches an upper limit when the phototransistor enters its saturation region in which the collector-emitter voltage V\ :sub:`CE` reaches approximately 0.2 V and the remaining voltage drop from the 5.0 V power supply appears across the collector resistor. Any further increase in light power applied to the phototransistor will not increase the collector current any more beyond this point. The phototransistor includes a dark plastic daylight filter that filters out most visible lignt, allowing it to operate in environments with considerable ambient visible light without producing a significant DC current error. The photodiode also has a very low "dark current," which is defined as its collector current with zero light applied light power. When the light form the QED123 LED is blocked from being applied to the phototransistor, the collector current becomes negligible and the voltage drop across the collector resistor is zero for the practical purposes of this lab, and the entire supply voltage appears at the collector.

With the QED123 LED and phototransistor positioned as shown in the drawing, the phototransistor is in full saturation when nothing is blocking the light path between the two. By slowly inserting a light blocker between the QED123 LED and the phototransistor, the light power impinging on the phototransistor slowly decreases, thereby decreasing the collector current. This causes the collector voltage to slowly rise until the light is totally blocked and the collector voltage goes to the full supply voltage. Therefore, with no blocker the collector voltage should be approximately 0.2 V and with the blocker fully in place it should be approximately equal to the supply voltage.

The comparator converts the continuously variable output voltage from the phototransistor into a binary signal that drives a red LED. The comparator circuit is the same that is used in the Simple Proximity Sensor lab, and its operation is describe in detail there. The red LED should be off when there is no blocker in place and the phototransistor is fully saturated, and should be on when the blocker is fully in place and the phototransistor is in cutoff mode.

In the final part of the lab we apply a square wave current through the QED123 LED to chop its emitted light. The phototransistor has a similar response for square waves, but its response is out-of-phase with the light emitted from the LED due to the common-emitter phototransistor configuration used in the lab. An in-phase output can be achieved using a common-collector phototransistor configuration.

Going Further
-------------

Light sensors are also used to detect light reflected from objects. One example is an automotive fog sensor in which an infrared LED emits light toward the rear window of an automobile, and an optical receiver is placed near the LED to receive any light that is reflected off of the window. When there is negligible fog on the rear window, the optical receiver receives a small reflection from the glass and indicates a "fog free" condition by producing a small voltage on its output. When fog is present, the reflected light increases significantly and the optical receiver produces a large output signal. The decision of when to automatically turn on the rear window defogger is made either in hardware (comparator) or software, based on the voltage output from the optical receiver. This is the basic principal on which many automatic rear window defoggers work.

Keeping the original lab configuration, bend the LED and phototransistor upward such that they are both facing vertically. Place a small mirror above the LED and phototransistor and observe the phototransistor output as the mirror is moved up and down. Try changing the spacing between the LED and phototransistor, as well as the angles of the LED and phototransistor with respect to vertical and see how these changes affect the phototransistor output. Try the same experiment using a small piece of clear plastic as a reflector, then fog up the plastic to see how much the phototransistor output level increases relative to its output with just the plastic as the reflector.

Observations and Conclusions
----------------------------

-  Infrared light has wavelengths a little longer than those of visible red light
-  LEDs can emit infrared light radiation and phototransistors can be used to detect the radiation
-  A phototransistor operates in a similar fashion as a traditional bipolar transistor with light as an input to its base, and can be used in common-emitter and common-collector configurations
-  Signals can be sent between LEDs and phototransistors without a galvanic connection between the two (in this lab we had a common ground, but this is not necessary)
-  A comparator can be used to convert the continuously variable phototransistor output voltage to a binary output
-  A LED and phototransistor can be used to detect when an opaque object is placed between them

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`

.. |lab_7_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_7_image_1.png
   :width: 600px
.. |lab_7_assembly_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_7_assembly_image_1.png
   :width: 1000px
.. |lab_7_image_2a.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_7_image_2a.png
   :width: 1000px
.. |lab_7_assembly_image_2a.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_7_assembly_image_2a.png
   :width: 1200px
.. |lab_7_image_3.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_7_image_3.png
   :width: 600px
.. |lab_7_assembly_image_3a.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_7_assembly_image_3a.png
   :width: 1000px
