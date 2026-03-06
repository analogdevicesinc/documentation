Activity: Phase Splitter Circuit - ADALM1000
============================================

Objective:
----------

The objective of this activity is to investigate the simple NPN noninverting emitter follower configuration in combination with the inverting common emitter configuration to provide two equal-amplitude, opposite-phase outputs.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

The Basic concept:
------------------

In this activity you will combine the common-collector configuration from :doc:`this Activity </wiki-migration/university/courses/alm1k/alm-lab-11>` with the common-emitter configuration from :doc:`this Activity </wiki-migration/university/courses/alm1k/alm-lab-5>` in the same amplifier to produce both in-phase and inverted ( 180 degree phase shifted ) outputs. From these two previous activities we know that the input to output gain of the common-collector or emitter follower is 1 if R\ :sub:`E` is much larger than r\ :sub:`E`. We also learned that the gain of the common emitter is R\ :sub:`C`/R\ :sub:`E` is -1 again if R\ :sub:`E` is much larger than r\ :sub:`E`.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 2 – 1.0 KΩ Resistor ( R\ :sub:`E` and R\ :sub:`C` )
| 1 – small signal NPN transistor ( 2N3904 Q\ :sub:`1` )

Directions:
~~~~~~~~~~~

The breadboard connections are shown in figure 1. The single transistor combines common-emitter and emitter follower configurations to provide two equal amplitude, opposite phase outputs. By choosing R\ :sub:`C` = R\ :sub:`E` (and both much less than r\ :sub:`E`), the absolute gain to each output is 1, but the collector and emitter voltages will vary out of phase with each other. Shown here using the single (+5 V) power supply, the voltage swing from either output can nearly reach one half of the power supply p-p as the transistor operating condition varies from cutoff to saturation. Of course, the base bias voltage ( DC offset of CH-A output ) must be chosen to set the base voltage swing to be between a little more than + V\ :sub:`BE` of Q\ :sub:`1` and one half of the power supply ( 2.5V ) + V\ :sub:`BE`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-phase-split_f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, Phase splitter. Outputs are 180° out of phase.


Hardware Setup:
~~~~~~~~~~~~~~~

The CH A AWG generator should be configured for a 500 Hz Sine Shape with the Max value set to approximately 2.5 V + VBE and the Min value set to approximately +VBE. AWG channel A should be set to SVMI, Split I/O Mode and the AWG B channels should also be in Split I/O Mode (SVMI or Hi-Z does not matter in this case). The Sync AWG box must be checked.

The AIN and BIN input pins, are used to measure the voltage at the emitter or the voltage at the collector. To also display the AWG channel A output waveform we can use the X Math trace. From the Curves drop down menu select CA-V, CB-V and X Math traces. Open the Math controls screen and enter AWGAwaveform[t] in the X Math Formula entry. The Units can be V and the X Axis can be V-A.

To measure the input to output gain compare the p-p voltage measurements at the emitter and collector to the AWG A p-p setting (Max – Min). You can also display the differential voltage (DC part cancels) between the two outputs by clicking on the CBV-CAV Built In Expression on the Math controls.

Be sure to save a copy of the scope screen to be included in your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-phase-split_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Phase splitter. Outputs at emitter and collector are 180° out of phase.


Procedure:
~~~~~~~~~~

Adjust the Min and Max values of the Channel A output such that the signal seen at the emitter swings from nearly 0 V to slightly less than 2.5 V and the signal seen at the collector swings from nearly 5 V to slightly more than 2.5 V and is not clipped. The incremental Gain (Vout / Vin) of the noninverting emitter follower path and inverting path to the collector should be 1 and -1 respectively.

Removing the differing DC levels at the outputs:
------------------------------------------------

The DC or average values of the two output waveforms are not the same. It is often desirable to produce outputs centered on the same DC value. Next you will investigate two techniques to do this.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

| 2 – 0.1 uF capacitors ( C\ :sub:`1` and C\ :sub:`2` )
| 2 – 10 KΩ resistors ( R\ :sub:`1` and R\ :sub:`2` )
| 2 – 1N914 small signal diodes ( D\ :sub:`1` and D\ :sub:`2` )

.. _directions-1:

Directions:
~~~~~~~~~~~

Add the two DC blocking capacitors and resistors tied to +2.5 V as shown in figure 2 to the circuit from figure 1. The capacitors remove or block the DC or average part of the signals and pass the AC part of the signals. The resistors tied to the +2.5 V supply set the new DC or average values for the signals seen at the outputs by charging the capacitors such that the outputs will be centered on +2.5 V. The value of the coupling capacitors set the circuit’s low-frequency cutoff point.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-phase-split_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Outputs centered on +2.5 V


Another technique to set the DC level after the capacitors is to replace the two 10 KΩ resistors with diodes as shown in figure 3. The diodes charge the capacitors to a value such that the negative peaks of the waveforms will be clamped to a voltage equal to the forward biased voltage drop of the diodes below the +2.5 V supply.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-phase-split_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Diode Clamp DC restoration


Try revering the direction of diodes D\ :sub:`1` and D\ :sub:`2` to see what happens. What is the new DC level?

**For Further Reading:**

`Phase splitter <https://en.wikipedia.org/wiki/Phase_splitter>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
