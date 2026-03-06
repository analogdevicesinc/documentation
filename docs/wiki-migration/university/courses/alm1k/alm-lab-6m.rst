Activity: NMOS as a Current Mirror - ADALM1000
==============================================

Objective:
----------

The purpose of this activity is to investigate the operation of the enhancement mode NMOS transistor as a current mirror.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 2 - small signal NMOS transistors (ZVN2110A or CD4007 NMOS array)

Directions:
~~~~~~~~~~~

The good way to measure the characteristics of the current mirror is to reuse the same basic configuration that was used in the common source FET curve tracer experiments. Diode connected transistor M\ :sub:`1` is connected across the gate and source terminals of M\ :sub:`2`. I\ :sub:`in` will be equal to the Channel A output current. Iout will be the current measured by channel B.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab6m_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 NMOS Current mirror test circuit


Hardware Setup:
~~~~~~~~~~~~~~~

In the current mirror configuration, generator Channel A is configured as SIMV (CA-I). The V\ :sub:`GS` of M\ :sub:`1` and M\ :sub:`2` will be the measured Channel A voltage (CA-V). The drain voltage is swept using a ramp from Channel B (SVMI) set to 4.5V Max and 0 V Min. The mirror output current is measured by the CB-I current measurement. You can use the X-Y mode displaying CA-I on the X axis (Iin) and CB-I (Iout) on the Y axis to plot the current mirror transfer function. You can use the CA-I - CB-I math waveform to plot the current mirror input to output error and offset. The CB-I/CA-I math waveform can be used to plot the current mirror Iout/Iin current gain.

Procedure:
~~~~~~~~~~

Two identical transistors with the same gate to source voltage will have the same drain current I\ :sub:`D`. The second transistor, M\ :sub:`2`, in effect mirrors the current in the first, M\ :sub:`1`. Remembering the drain current to gate source voltage relationship for a MOS transistor:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab6m_e1.png
   :align: center
   :width: 300px

where K =Mu\ :sub:`n`\ C\ :sub:`ox`/2<sub></sub>and Lamda can be taken as process technology constants.

Identical transistors by definition have the same W/L and process technology constants. In the simple current mirror, both transistors have the same V\ :sub:`GS`. Thus, both transistors will have the same I\ :sub:`D`. Since no current flows in the gate terminal of a FET I\ :sub:`in` = I\ :sub:`out`.

Questions:
~~~~~~~~~~

You are to measure I\ :sub:`in`, Rout seen into the drain of M\ :sub:`2`, the current mirror gain = I\ :sub:`out`/I\ :sub:`in` and determine the Norton and Thevenin equivalent circuits for this mirror.

Extra Credit activity
~~~~~~~~~~~~~~~~~~~~~

Try building a PMOS version of the current mirror from the PMOS devices in the CD4007 array or the ZVP2110A discrete transistors from the Parts Kit. How would you have to modify the circuit figure 1 to measure PMOS transistor?

**For Further Reading:**

| `The Current Mirror <https://en.wikipedia.org/wiki/Current_mirror>`__
| :doc:`/wiki-migration/university/courses/electronics/text/chapter-11`

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
