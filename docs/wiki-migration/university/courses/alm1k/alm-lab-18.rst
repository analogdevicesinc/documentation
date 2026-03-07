Activity: The CMOS Analog Switch - ADALM1000
============================================

Objective:
----------

The objective of this exercise is to explore the use of complementary MOS transistors as an analog voltage switch.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Concept:
--------

The ideal analog switch has no on-resistance, infinite off-impedance and zero time delay, and can handle large signal and common-mode voltages. Real analog switches made with MOS transistors meet none of these criteria, but if we understand the limitations of analog switches, most of these limitations can be overcome. The on-resistance is one of these limitations and this lab activity will attempt to characterize this switch specification.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and Jumper wire kit
| 1 - CD4007 CMOS transistor array
| 2 - NPN transistors (2N3904 or equivalent)
| 1 – 4.7 KΩ resistor

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 400px

.. container:: centeralign

   CD4007 CMOS transistor array pinout


NMOS Directions:
~~~~~~~~~~~~~~~~

Construct the test circuit shown in figure 1. The green boxes indicate connections to the analog I/O connector on the ALM1000. NMOS and PMOS devices M\ :sub:`1` and M\ :sub:`2` are contained in the CD4007 package. All un-used pins can be left floating. To measure the resistance (Ron) of the MOS transistors we first need to force a known current through the resistance and then measure the voltage across the resistance. The two NPN devices Q\ :sub:`1` and Q\ :sub:`2` along with resistor R\ :sub:`1` form a current source with an output current of approximately 1 mA. The exact magnitude of this current is not important in that we are mainly interested in the change in the Ron of the MOS devices as the voltage at their source/drain varies over the range between ground (0V) and positive power supply (5V).

In this first test only NMOS device M\ :sub:`1` is turned on and PMOS device M\ :sub:`2` is turned off.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab18_f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1, NMOS Ron test circuit


Procedure:
~~~~~~~~~~

Configure channel A AWG output as a 100 Hz triangle wave with a Min value of 0.5 volts and a Max value of +5V. This will swing the source and drain voltages of the NMOS switch transistor from +0.5 volts to +5 volts. We cannot swing the voltage all the way to 0 volts because of the NPN current source Q\ :sub:`2`. Channel B should be set to the High-Z mode to just measure voltage. Open the XY plotter screen. Set the X axis to Math with the following formula:

(VBuffA[t] - CHAOffset)

And set Math on the Y axis with the following formula:

(VBuffA[t]-VBuffB[t])-CHBOffset

The voltage across the switch. You could also use the Y axis math function to calculate the resistance but if the current is 1 mA then we can just convert the displayed volts to KΩ since 1V / 1mA is 1 KΩ. Note: You can get a more precise estimate of the current source by measuring the voltage across R\ :sub:`1` and its actual resistance or use the current trace of channel A to measure the current ( it should be a more or less constant 1 mA ).

Questions:
~~~~~~~~~~

At what voltage does the NMOS devices turn off and on? How does this voltage relate to the threshold voltage of M\ :sub:`1`?

What happens to the source to drain voltage as the NMOS transistor turns off?

How does this affect the display on the XY plot screen?

PMOS Directions:
~~~~~~~~~~~~~~~~

Now modify your circuit to look like figure 2 by connecting the gates of both M\ :sub:`1` and M\ :sub:`2` to ground (most negative voltage). In this second test only PMOS device M\ :sub:`2` is turned on and NMOS device M\ :sub:`1` is turned off.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab18_f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2 PMOS Ron test circuit


.. _procedure-1:

Procedure:
~~~~~~~~~~

Repeat the sweep of the voltage from channel A AWG and plot the on-resistance of just the PMOS transistor.

.. _questions-1:

Questions:
~~~~~~~~~~

At what voltage does the PMOS devices turn off and on? How does this voltage relate to the threshold voltage of M\ :sub:`2`?

What happens to the source to drain voltage as the PMOS transistor turns off?

How does this affect the display on the scope screen?

CMOS Directions:
~~~~~~~~~~~~~~~~

Now modify your circuit to look like figure 3 by connecting the gate of M\ :sub:`1` to the positive power supply +5V and the gate of M\ :sub:`2` to ground. In this last test both the NMOS device M\ :sub:`1` and the PMOS device M\ :sub:`2` are turned on.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab18_f3.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3 CMOS Ron test circuit


.. _procedure-2:

Procedure:
~~~~~~~~~~

Repeat the sweep of the voltage and plot the on resistance of the combined NMOS and PMOS transistors.

Compare the traces you got for just the NMOS, just the PMOS and the combined NMOS and PMOS cases. Where do they overlap and what does that tell you about the relative on resistance of the two devices vs the voltage on the switch?

.. _questions-2:

Questions:
~~~~~~~~~~

Do either the NMOS or PMOS transistors ever turn off?

Are both the NMOS and PMOS ever off at the same time?

If an NMOS switch is used to connect two signal nodes that can have analog voltages that vary from 0 to 1V, what must be the value of the bulk and gate voltages for the switch to work properly?

What are the conditions for a PMOS switch?

Extra Challenge Activity:
~~~~~~~~~~~~~~~~~~~~~~~~~

Try measuring the Ron vs input voltage for other CMOS analog switches such as the CD4016, CD4066 quad switches or the CD4051, CD4052, and CD4053 analog multiplexers or the ADG608/609 analog switch (MUX) or ADG333 quad SPDT switch. Compare your results to the Ron specified in the manufacturer product datasheets.

**For Further Reading:**

| :adi:`Switches and Multiplexers <library/analogdialogue/archives/45-05/switch_mux.html>`
| :adi:`On Building Physically Accurate Analog Switch Macromodels <media/en/analog-dialogue/raqs/raq-issue-173.pdf>`

**Return to the ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
