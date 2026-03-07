Activity: BJT Characteristic Curves, For ADALM1000
==================================================

Objective:
----------

The purpose of this activity is to investigate the collector current, I\ :sub:`C` vs. collector voltage, V\ :sub:`CE` characteristics of the BJT. The ADALP2000 kit of parts will contain a number of transistors, both NPN and PNP devices of various types, that can be used.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

The variable analog outputs supplied by the ALM1000 hardware are voltages but can also measure current at same time. The Bipolar Junction Transistor can be modeled as a current controlled current source. The BJT collector current, I\ :sub:`C`, is controlled by the much smaller base current, I\ :sub:`B`. The generator output voltage must be converted into a suitable small current to drive the base terminal of the device under investigation. A simple high value resistor can be used to convert this voltage into a current, as shown in figure 1. However, only if the voltage across the resistor is known or controlled in some way. In this simple circuit, the base current I\ :sub:`B` = (CB-V - V\ :sub:`BE`)/10KΩ. We can set CB-V to known values but we don't know the exact value of V\ :sub:`BE`. We can of course remove an estimate of the V\ :sub:`BE` mathematically. This is still only an estimate but close enough for our purposes here.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 NPN I\ :sub:`C` vs. V\ :sub:`CE` characteristic curve measurements


If we sweep the voltage on the collector, V\ :sub:`CE`, while changing the voltage on the resistor in a step wise fashion for each sweep cycle of the collector voltage, we can generate a set of characteristic curves of the collector current vs collector emitter voltage for a set of base currents.

Materials:
~~~~~~~~~~

| ADALM1000 Hardware module
| Solder-less Breadboard
| 1 - 10KΩ Resistor
| 1 - small signal NPN transistor (2N3904, SSM2212)

NPN device Directions:
~~~~~~~~~~~~~~~~~~~~~~

Build the simple characteristic curve measurement circuit shown in figure 1 on your solder-less breadboard. The green boxes indicate where to connect the ALM1000.

Hardware Setup:
~~~~~~~~~~~~~~~

Set the Channel B generator shape to the 10 level stair-step waveform. Set the frequency to 20Hz, the Max to 4.6 V and the Min to 0.6 V. The extra 0.6 volts is an initial estimate of V\ :sub:`BE`. The waveform in the display should start at 0.6V and increase in 0.4 V increments to 4.6 V. Set the channel A generator shape to a triangle wave with a Max of 5.0 V and a Min of 0 V (wave should swing from 0 to 5V). Set the frequency to 200 Hz ( 10 times the 20 Hz of channel B). Comparing the waveforms in channel A and channel B, the triangle wave in channel A should go through one cycle from 0 to 5 V and back to zero during the time of one step in the waveform in channel B. Adjust the phases of channel A and/or channel B to make them line up in this way if they do not.

Procedure:
~~~~~~~~~~

The 0.4 V steps in the voltage driving the 10 KΩ base resistor will produce approximately 0.4 V/10 KΩ or 40 uA steps in the base current. Using the scope in XY mode plot channel CA-V on the horizontal axis (V\ :sub:`CE`) and channel CA-I (I\ :sub:`C`) on the vertical axis. You should see a set of 10 curves of I\ :sub:`C` vs. V\ :sub:`CE`, one for each of the 10 different base current levels. These base current levels should be approximately 0, 40uA, 80uA, 120uA ... 360uA. It may be necessary to slightly adjust the 0.6V offset level of the first step of channel B up or down slightly to insure it is right at the initial turn on value ( I\ :sub:`B`\ =0 and I\ :sub:`C`\ =0) of the transistor you are testing.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4_f5.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1A, Example NPN I\ :sub:`C` vs. V\ :sub:`CE` characteristic curves.


Questions:
~~~~~~~~~~

| From the measured data calculate the current gain Beta ( ß=I\ :sub:`C`/I\ :sub:`B` ) for each device.
| Using the curve for the highest base current step, calculate the early voltage (VA) for each device.
| Calculate the Beta Early voltage product ( ß\*VA) for each device.
| Compare your results with manufacturer specifications for each device measured.

PNP device Directions:
~~~~~~~~~~~~~~~~~~~~~~

To measure the PNP device, alter the characteristic curve measurement circuit as shown in figure 2. The connections are not very different but the polarity of the voltage waveforms generated by channel A and channel B must now be negative with respect to the PNP emitter. To accommodate this the emitter is now connected to +5 V.

You can use the same step staircase waveform you used for the NPN device to drive the base current for the PNP device. However, you will need to set the Max to +5 V - V\ :sub:`BE` or 4.4 V and set the Min to 0.4 V. The waveform in the display should now start at 4.4 V and decrease in 0.4 V increments to 0.4 V. The channel A triangle wave can have the same 5.0 V Max and 0 V Min. Check to make sure that the triangle wave in channel A goes through one cycle from 5 V to 0 and back to 5 V during the time of one step in the waveform in channel 2. Change the phase of channel A and/or B as necessary.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 PNP I\ :sub:`C` vs. V\ :sub:`CE` characteristic curve measurements


NPN Beta vs Collector Voltage Directions:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Beta (β) is defined as the ratio of the collector current, I\ :sub:`C`, to the base current, I\ :sub:`B`. Beta is not constant and varies as the operating conditions of the transistor changes. In this experiment we will be plotting β vs V\ :sub:`CE`.

Change the 10 KΩ resistor in figure 1 to 1 KΩ. Change the shape of Channel B to DC. Change the Channel B Max to 1.5 V, the Min and Freq setting are ignored for the DC shape. Change the Channel A Max to 2 volts. Under the curves drop down select all four traces to be displayed. The current in channel B, the base current, will be small and will be rather noisy so turning on trace averaging is a good idea. You should see something like the time display in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4_f3.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 3 NPN V\ :sub:`CE`, I\ :sub:`C`, I\ :sub:`B` Time display


In the time display of the base current, yellow trace, we see that it increases slightly when the V\ :sub:`CE`, green trace, falls below about 0.5 volts. The collector current, light blue trace, also falls rapidly at this same time.

To calculate and plot β vs V\ :sub:`CE`, open the X-Y Pot window. Select Math for both the X and Y axis. Set the X axis math formula to display the V\ :sub:`CE` which is the channel A voltage:

VBuffA[t]

Set the Y axis math formula to calculate β which is the channel A current divided by the channel B current:

IBuffA[t]/IBuffB[t]

Set the Math X axis to V-A. Set the Math Y axis to I-B. Adjust the range and position controls for CA-V to 0.2 V/Div and 1.0 V. Adjust the range and position controls for CB-I to 10.0 mA/Div and 50.0 mA. You should now see something like the X-Y plot shown in figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4_f4.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 4 NPN Beta vs V\ :sub:`CE` X-Y plot


As we can see the β falls off rapidly as the V\ :sub:`CE` drops below 0.5 volts. At this point the collector base junction is starting to become forward biased (i.e. no longer reversed biased) and the transistor is entering into what is called the saturation region. In the saturation the β or current gain of the transistor is significantly smaller than in the so called linear region (i.e. collector base junction reversed biased).

.. _questions-1:

Questions:
~~~~~~~~~~

| Again, from the measured data calculate the current gain Beta ( ß=I\ :sub:`C`/I\ :sub:`B` ) for each device.
| Using the curve for the highest base current step, calculate the early voltage (VA) for each device.
| Calculate the Beta Early voltage product ( ß\*VA) for each device.
| Compare your results with manufacturer specifications for each device measured.

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/bjt_char_curves_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/bjt_char_curves_bb`

**For Further Reading:**

| `Bipolar junction transistor <https://en.wikipedia.org/wiki/Bipolar_junction_transistor>`_
| http://www.physics.csbsju.edu/trace/NPN.CC.html

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
