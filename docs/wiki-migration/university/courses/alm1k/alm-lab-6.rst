Activity: BJT Current Mirror - ADALM1000
========================================

Objective:
----------

The goal of this activity is to study the BJT current source or current mirror. Important attributes for current sources include high output resistance with a wide range of voltage compliance and rejection of external variations such as power supply or temperature.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Simple Current Mirror
---------------------

Materials:
~~~~~~~~~~

| Analog Discovery Lab hardware
| Solder-less breadboard
| Jumper wires
| 2 - small signal NPN transistors (2N3904 or SSM2212)

Directions:
~~~~~~~~~~~

The good way to measure the characteristics of the current mirror is to reuse the same basic configuration that was used in the common emitter BJT curve tracer experiments. Diode connected transistor Q\ :sub:`1` is connected across the base and emitter terminals of Q\ :sub:`2`. I\ :sub:`in` will be equal to the Channel A output current. Iout will be the current measured by channel B.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab6_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Current mirror test circuit


Hardware Setup:
~~~~~~~~~~~~~~~

In the current mirror configuration, generator Channel A is configured as SIMV (CA-I). The V\ :sub:`BE` of Q\ :sub:`1` and Q\ :sub:`2` will be the measured Channel A voltage (CA-V). The collector voltage is swept using a ramp from Channel B (SVMI) set to 4.6V Max and 0.6 V Min. The mirror output current is measured by the CB-I current measurement. You can use the X-Y mode displaying CA-I on the X axis (Iin) and CB-I (Iout) on the Y axis to plot the current mirror transfer function. You can use the CA-I - CB-I math waveform to plot the current mirror input to output error and offset. The CB-I/CA-I math waveform can be used to plot the current mirror Iout/Iin current gain.

Procedure:
~~~~~~~~~~

Two identical transistors with the same base to emitter voltage will have the same collector current I\ :sub:`C`. The second transistor, Q\ :sub:`2`, in effect mirrors the current in the first, Q\ :sub:`1`. Remembering the collector current to base emitter voltage relationship for a bipolar transistor:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab6_e1.png
   :align: center
   :width: 150px

| where:
| Is = the saturation current, and is a constant
| V\ :sub:`BE` is the base emitter voltage
| The thermal voltage, KT/q = 25.8 mV at room temperature

Identical transistors by definition have the same I\ :sub:`S`. In the simple current mirror, both transistors have the same V\ :sub:`BE`. Thus, both transistors will have the same I\ :sub:`C` and if base currents are ignored, Iin = Iout. Actually I\ :sub:`C1`\ is I\ :sub:`in` - (I\ :sub:`B1` + I\ :sub:`B2`).

Questions:
~~~~~~~~~~

You are to measure I\ :sub:`in`, Rout seen into the collector of Q\ :sub:`2`, the current mirror gain = I\ :sub:`out`/I\ :sub:`in` and determine the Norton and Thevenin equivalent circuits for this mirror.

Current Mirror with Base Current Compensation
---------------------------------------------

Modify the simple mirror circuit by adding the base current compensation transistor Q\ :sub:`3` as shown below. Repeat the same procedure you followed for the simple mirror circuit. In addition to the same quantities and graphs, does your data indicate any advantage to this circuit? Any disadvantages?

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab6_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Current Mirror with Base Current Compensation


**For Further Reading:**

http://en.wikipedia.org/wiki/Current_mirror

Wilson Current Mirror
---------------------

Modify the simple mirror into a Wilson Mirror as shown below. Repeat the same procedure you followed for the simple mirror circuit. In addition to the same quantities and graphs, does your data indicate any advantage to this circuit? Any disadvantages?

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab6_f3.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3 Wilson current mirror


.. _questions-1:

Questions:
~~~~~~~~~~

**For Further Reading:**

http://en.wikipedia.org/wiki/Wilson_current_source

Widlar current mirror
---------------------

Modify the simple mirror into a Widlar Mirror as shown below. Repeat the same procedure you followed for the simple mirror circuit. In addition to the same quantities and graphs, does your data indicate any advantage to this circuit? Any disadvantages?

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab6_f4.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 4 Widlar current mirror


.. _questions-2:

Questions:
~~~~~~~~~~

| 1. Use the output impedance of the simple mirror to determine the Early voltage for the NPN transistor.
| 2. Build a mirror using PNP transistors and use the output impedance of the simple mirror to determine the Early voltage for the PNP transistor.
| 3. The output impedance of a Widlar current mirror is approximately,

:math:`R_out = r_o[1 + g_m R_3]`

| where: r\ :sub:`o` = V\ :sub:`AF`/I\ :sub:`C`
| V\ :sub:`AF` is the Early voltage.
| g\ :sub:`m` = I\ :sub:`C`/V\ :sub:`T` is the transconductance. And
| R\ :sub:`E` is the emitter resistor.

| How accurately does this formula predict the output impedance of the Widlar current mirror you constructed?
| 4. If base currents are not ignored, how is I\ :sub:`out` related to Iin in the simple current mirror?
| 5. If I need a second (or third) copy of I\ :sub:`in` how would I make it?

**For Further Reading:**

http://en.wikipedia.org/wiki/Widlar_current_source

low Input Headroom Mirror
-------------------------

.. _objective-1:

Objective:
~~~~~~~~~~

The goal of this activity is to study BJT current source or current mirror with lower input headroom requirements.

.. _materials-1:

Materials:
~~~~~~~~~~

| 1 - 150 KΩ Resistor (or a 100 KΩ in series with a 47 KΩ)
| 2 - small signal NPN transistor (2N3904 or SSM2212)
| 1 - small signal PNP transistor (2N3096)

.. _directions-1:

Directions:
~~~~~~~~~~~

The diode configuration with nearly zero turn on voltage from activity 2 is used here to make a current mirror. The current input node at the collector of Q\ :sub:`1` (base of PNP Q\ :sub:`3`) is now much closer to ground compared to the conventional current mirror. What advantages would this have over the conventional mirror?

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab6_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 Low input head room mirror


Ideally the collector of PNP Q\ :sub:`3` would be connected to some negative voltage with respect to ground. Try connecting the collector of Q\ :sub:`3` to a negative voltage supplied by a battery connected with its + terminal connected to ground (collector of Q3 connected to - terminal of battery). What happens? Can the input node of the mirror get even closer to ground now?

**For Further Reading:**

`The Current Mirror <https://en.wikipedia.org/wiki/Current_mirror>`__

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
