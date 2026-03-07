Activity: The Emitter follower (BJT) - ADALM1000
================================================

Objective:
----------

To investigate the simple NPN emitter follower amplifier also sometimes referred to as the common collector configuration.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 - 2.2KΩ Resistor ( R\ :sub:`L` )
| 1 - small signal NPN transistor ( 2N3904 Q\ :sub:`1` )

Directions:
~~~~~~~~~~~

The breadboard connections are shown in figure 1. The output of the channel A voltage generator, CA-V, is connected to the base terminal of Q\ :sub:`1`. The collector terminal is connected to the positive (+5 V) supply. The emitter terminal is connected to both the 2.2 KΩ load resistor and the channel B scope input CB-H. The other end of the load resistor is connected to ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Emitter Follower


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A voltage generator should be configured for a 100 Hz Sine wave with 4.6 volt Max and 2.6 V Min. The channel B scope input, CB-H, is used to measure the voltage at the emitter. To measure the input to output error or offset, the CA-V - CB-V Math waveform can be displayed. To measure the input to output gain, the CB-V / CA-V Math waveform can be displayed.

Procedure:
~~~~~~~~~~

The incremental Gain (Vout / Vin) of the emitter follower should ideally be 1 but will always be slightly less than 1. The gain is generally given by the following equation:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11_e1.png
   :align: center
   :width: 150px

From the equation we can see that in order to obtain a gain close to one we can either increase R\ :sub:`L` or decrease r\ :sub:`e`. We also know that r\ :sub:`e` is a function of I\ :sub:`E` and that as I\ :sub:`E` increases r\ :sub:`e` decreases. Also from the circuit we can see that I\ :sub:`E` is related to R\ :sub:`L` and that as R\ :sub:`L` increases I\ :sub:`E` decreases. These two effects work counter to each other in the simple resistive loaded emitter follower. Thus to optimize the gain of the follower we need to explore ways to either decrease r\ :sub:`e` or increase R\ :sub:`L` without effecting the other.

Looking at the follower in another way, because of the inherent DC shift due to the transistor's V\ :sub:`BE`, the difference between input and output should be constant over the intended swing. Due to the simple resistive load R\ :sub:`L`, the emitter current I\ :sub:`E` increases and decreases as the output swings up and down. We know that V\ :sub:`BE` is a (exponential) function of I\ :sub:`E` and will change approximately 18 mV (at room temperature) for a factor of 2 change in I\ :sub:`E`. In this +4V to +2V swing example the minimum I\ :sub:`E` = 2V / 2.2KΩ or 0.91 mA to a maximum I\ :sub:`E` = 4V / 2.2KΩ or 1.82mA. This results in about an 18 mV change in V\ :sub:`BE`. This observation leads us to the first possible improvement in the emitter follower.

The current mirror from activity 5 is now substituted for the emitter load resistor to fix the amplifier transistor emitter current. A current mirror will sink a more or less constant current over a wide range of voltages. This more or less constant current flowing in the transistor will result in a more or less constant V\ :sub:`BE`. Viewed another way, the very high output resistance of the current source has effectively increased R\ :sub:`L` while r\ :sub:`e` remains at a low value set by the current.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

| 1 - 1 KΩ Resistor
| 1 - small signal NPN transistor ( Q\ :sub:`1` 2N3904)
| 2 - small signal NPN transistors ( Q\ :sub:`2`, Q\ :sub:`3` SSM2212) selected for best V\ :sub:`BE` matching

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11_f2a.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Improved Emitter Follower


Emitter follower output impedance
---------------------------------

.. _objective-1:

Objective:
~~~~~~~~~~

An important aspect of the emitter follower is to provide power or current gain. That is to say drive a lower resistance (impedance) load from a higher resistance (impedance) source. Thus it is instructive to measure the emitter follower output impedance.

.. _materials-1:

Materials:
~~~~~~~~~~

| 1 - 2.2 KΩ Resistor
| 1 - 10 KΩ Resistor
| 1 - small signal NPN transistor ( Q\ :sub:`1` 2N3904 )

.. _directions-1:

Directions:
~~~~~~~~~~~

The circuit configuration shown in figure 3 adds a resistor R\ :sub:`2` to inject a test signal from channel A into the emitter (output) of Q\ :sub:`1`. The input, base of Q\ :sub:`1`, is tied to the fixed 2.5 V supply rail.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11_f3a.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Output impedance test


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz Sine wave with 2.8 volt Max and a 0.8 volt Min ( +/- 1 volt swing either side of the emitter voltage which should be around 1.8 V). This injects a +/- 0.1mA (1V/10KΩ) current into Q\ :sub:`1`'s emitter. Scope channel B measures the change in voltage seen at the emitter.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Plot the change in voltage measured at the emitter. The nominal emitter current in Q\ :sub:`1` is (2.5 - V\ :sub:`BE`) / 2.2 KΩ. We can calculate the small signal r\ :sub:`e`\ from this current as ohms. How does this r\ :sub:`e` compare to the value measured from the test data? Change the value of R\ :sub:`1` from 2.2 KΩ to 4.7 KΩ and re-measure the output impedance of the circuit. How has it changed and why?

Low Offset Follower
-------------------

All the follower circuits we have investigated so far have a built in offset of -V\ :sub:`BE`. The circuit shown next uses the V\ :sub:`BE` shift up of a PNP emitter follower to partially cancel the V\ :sub:`BE` shift down of an NPN emitter follower.

.. _materials-2:

Materials:
~~~~~~~~~~

| 1 - 6.8KΩ Resistor
| 1 - 10KΩ Resistor
| 1 - 0.01uF Capacitor
| 1 - small signal PNP transistor ( Q\ :sub:`1` 2N3906)
| 3 - small signal NPN transistors ( Q\ :sub:`2`, Q\ :sub:`3`, Q\ :sub:`4` 2N3904 or SSM2212)

.. _directions-2:

Directions:
~~~~~~~~~~~

The breadboard connections are shown in figure 4. The output of the channel A generator is connected to the base terminal of PNP transistor Q\ :sub:`1`. The collector terminal of Q\ :sub:`1` is connected to diode connected NPN Q\ :sub:`3` which is the input of a current mirror. The emitter terminal is connected to both resistor R\ :sub:`1`\ and the base terminal of NPN transistor Q\ :sub:`2`. Scope channel B is connected to both the emitter of Q\ :sub:`2` and the Collector of Q\ :sub:`4`. The emitters of both Q\ :sub:`3` and Q\ :sub:`4` are connected to ground. For best matching use the SSM2212 matched NPN pair for Q\ :sub:`3` and Q\ :sub:`4`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11_f4a.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Low offset follower


.. _hardware-setup-2:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz Sine wave with 3 volt Max and a 2 volt Min. Both Scope vertical ranges are set to 0.5V/Div.

.. _procedure-2:

Procedure:
~~~~~~~~~~

Without C\ :sub:`1` and R\ :sub:`2` connected, use the CA-V - CB-V Math trace to measure the input to output offset error for this circuit and compare it to the results you saw from the figure 1 and figure 2 circuits.

Now connect C\ :sub:`1` and R\ :sub:`2` and change the input wave shape of CA-V to a square wave. Measure the rise and fall times of the output signal. Note any differences in the rise and fall times and explain why.

Current Limit or Constant Current (Transistor Based)
----------------------------------------------------

This is a modification of the emitter follower to limit the current output. If the output stage of an amplifier is an emitter follower it may be necessary to limit the maximum current that can be supplied to the output load.

Circuit:
~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11_f5a.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 Emitter Current Limit


| Where:

-   R\ :sub:`1` base resistor limits base current to transistor Q\ :sub:`1`.
-   R\ :sub:`2` current sense resistor used to sense the current and turn on transistor Q\ :sub:`2`.
-   Q\ :sub:`1` main transistor supplying the load current.
-   Q\ :sub:`2` current sense transistor.

Discussion:
~~~~~~~~~~~

The concept in this circuit is that R\ :sub:`2` acts as current sense resistor. When the load current times R\ :sub:`2`, the sense voltage, reaches about 0.6 (for silicon transistors ) Q\ :sub:`2` begins to conduct and increases current in R\ :sub:`1` which limits the base drive to Q\ :sub:`1`\ reducing its output current. The maximum current from the circuit is reached when I\ :sub:`L`\ \*R\ :sub:`2` = 0.6. This circuit can be used to protect amplifiers (including push pull amplifiers.), power supplies and other circuits; or it can be used as a constant current circuit. This is not a precision circuit; however it is a simple and effective circuit.

**For Further Reading:**

http://en.wikipedia.org/wiki/Common_collector

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
