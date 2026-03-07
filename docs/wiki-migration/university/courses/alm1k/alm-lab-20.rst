Activity: CMOS Amplifier stages - ADALM1000
===========================================

Objective:
----------

The goal is to explore a high gain inverting amplifier constructed from complementary MOS devices (CMOS).

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

1 High gain inverting amplifier
-------------------------------

Background:
~~~~~~~~~~~

A CMOS inverter can also be viewed as a high gain amplifier. It consists of one PMOS device, M\ :sub:`1` and one NMOS device M\ :sub:`2`. Generally the CMOS fabrication process is designed such that the threshold voltage, V\ :sub:`TH`, of the NMOS and PMOS devices are roughly equal i.e. complementary. The designer of the inverter then adjusts the width to length ratio, W/L, of the NMOS and PMOS devices such that their respective transconductance is also equal.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 CMOS Inverting amplifier


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 3 - 100KΩ Resistors
| 1 - 10KΩ Resistor
| 1 - 4.7KΩ Resistor
| 2 - 47 KΩ Resistors
| 2 - 1uF capacitor
| 1 - 10 pF capacitor
| 1 - CD4069A, CD4069UB or 74HCU04 unbuffered hex inverter (be sure not to use the buffered 74HC04 version) Alternatively a simple CMOS inverter can be built using the CD4007 transistor array. Note the appendix at the end.

Directions:
~~~~~~~~~~~

First build the simple example shown figure 2 to test the input to output transfer function of the simple CMOS amplifier. The green boxes indicate connections to the connector on ALM1000. Connect +5V power supply to V\ :sub:`CC` (pin 14) and ground to GND (pin 7). Connect the output of the channel A voltage generator to one of the inverter inputs (pin 1) and connect the inverter output (pin 2) to channel B scope input CB-H in Hi-Z mode.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2 amplifier transfer function


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 74HCU04 and CD4069A share the same package pinouts


Hardware Setup:
~~~~~~~~~~~~~~~

Configure the channel A voltage generator CA-V for a 200 Hz triangle wave with 0 V Min value and 5V Max value. Both scope channels should be set to 0.5V/Div.

Procedure:
~~~~~~~~~~

Measure the DC input offset where the gain in the highest. Measure the slope of the output and calculate the DC gain of the amplifier as the ratio of the change in the output voltage to the change in input voltage at the center of the output swing (i.e. approx. around 2.5V). Remember the answer should be a negative number because the amplifier inverts.

2 Adding negative feedback
--------------------------

On your solder-less breadboard construct the amplifier circuit shown in figure 4 below.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 single stage amplifier


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Configure the channel A voltage generator for a 200 Hz sine wave with 2 V Min value and 3 V Max value. Both scope channels should be set to 0.5V/Div.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Apply a sinusoidal signal (best to center the DC average of the signal on the nominal offset measured previously) to the input and measure the gain of the entire system from 10 Hz to 10 KHz.

Questions:
~~~~~~~~~~

What is the DC voltage seen at the input and output of the inverter? What sets this DC level?

What is the gain from the input source, CV-A, to the output CV-B seen at the inverter output? Which components set this gain and why?

3 Adding more stages for higher gain
------------------------------------

On your solder-less breadboard construct the amplifier circuit shown in figure 5 below.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 three stage amplifier


.. _hardware-setup-2:

Hardware Setup:
~~~~~~~~~~~~~~~

Configure the channel A voltage generator for a 200 Hz sine wave with 2 V Min value and 3 V Max value. Both scope channels should be set to 0.5V/Div.

.. _procedure-2:

Procedure:
~~~~~~~~~~

Apply a sinusoidal signal (best to center the DC average of the signal on the nominal offset measured previously) to the input and measure the gain of the entire system from 10 Hz to 10 KHz.

.. _questions-1:

Questions:
~~~~~~~~~~

What is the DC voltage seen at the input and output of the inverter? What sets this DC level?

What is the gain from the input source, CV-A, to the output CV-B seen at the inverter output? Which components set this gain and why?

Appendix: Making an inverter with the CD4007 transistor array
-------------------------------------------------------------

Below is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 420px

.. container:: centeralign

   CD4007 CMOS transistor array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one to configure as shown below is by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f6.png
   :align: center
   :width: 500px

The second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input.

The third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

These three inverters can be used to construct the three stage amplifier in section 20.3 for example.

**For Further Reading:**

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
