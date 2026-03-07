Activity: Making a full Operational Amplifier from previous blocks - ADALM1000
==============================================================================

Objective:
----------

By combining some of the circuit blocks already explored, the goal of this lab activity is to build a complete three stage operational amplifier from a few discrete devices. The differential amplifier used as the first stage is combined with a Miller compensated common emitter second stage and a class A-B push-pull output third stage.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Three stage operational amplifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and Jumper wire kit
| 12 – Resistors, various values
| 2 – Capacitors
| 1 – 1N914 or similar diode
| 5 – 2N3904 NPN transistors, for Q\ :sub:`1`,Q\ :sub:`2`, Q\ :sub:`3`, Q\ :sub:`4` and Q\ :sub:`5`
| 4 – 2N3906 PNP transistors for Q\ :sub:`6`, Q\ :sub:`7`, Q\ :sub:`10` and Q\ :sub:`11`
| 1 – TIP31 NPN power transistor Q\ :sub:`8` (or 2N3904)
| 1 – TIP32 PNP power transistor Q\ :sub:`9` (or 2N3906)

Directions:
~~~~~~~~~~~

The object here is to construct the circuits shown in figures 1 and 2 using only the various transistors available in the ADALP2000 Analog Parts Kit. You should build the circuit on your solder-less breadboard. The values of the input and feedback resistors are shown as 4.7kΩ but can be changed to produce other gains. The amplifier is shown connected as a non-inverting amplifier but inverting configurations are also possible.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-13-f1.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 1, Three Stage Operational Amplifier with resistive load.


The class AB push-pull output stage is biased by PNP V\ :sub:`BE` multiplier Q\ :sub:`7` and resistors R\ :sub:`4` and R\ :sub:`5`. The ratio of R\ :sub:`4` and R\ :sub:`5` sets the steady-state bias current point for NPN Q\ :sub:`8` and PNP Q\ :sub:`9`. Since the two output transistors are NPN and PNP an NPN transistor would work equally well in place of PNP Q\ :sub:`7`. (A PNP was chosen for Q\ :sub:`7` because there are a limited number of 2N3904 NPNs in the Parts Kit and the TIP31 and TIP32 power transistors are used for the output stage rather than 2N3904 and 2N3906).

Hardware Setup:
~~~~~~~~~~~~~~~

Connect your circuit to the ALM1000 analog I/O connector as indicated by the green boxes.

Procedure:
~~~~~~~~~~

Configure the channel A generator output CA-V for a 500 Hz sine wave with Min value of 1.5 V and Max value of 3.5 V. With channel B in Split I/O mode use scope BIN to observe the output of the amplifier, record the input to output amplitude and phase relationship.

Lower the Min value until the amplifier output clips on the negative peaks of the sine wave. Record this value and explain. Increase the Max value until the amplifier output clips on the positive peaks of the sine wave. Record this value and explain.

Increasing open loop gain
~~~~~~~~~~~~~~~~~~~~~~~~~

The amplifier in figure 1 uses a simple resistive load for the NPN differential input stage. The gain of the amplifier can be increased by using a PNP current mirror as the load for the input stage as shown in figure 2. With the addition of the resistively degenerated current mirror the ability to null out or adjust the input offset is possible. Add the current mirror to your circuit and repeat the test you just did.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-13-f4.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 2, Three Stage Operational Amplifier with current mirror load.


**Frequency compensation**

C\ :sub:`1` provides frequency compensation in order to reduce the gain at high frequencies where it may be subject to oscillation (instability). It also sets the amplifier slew-rate. Change the shape of channel A to square wave. Set the frequency to 2000 Hz. Change the value of C\ :sub:`1` to 4.7nF (marked 472) and measure the positive and negative slew rate of the amplifier. The DC current supplied by Q\ :sub:`5` determines how fast the compensation capacitor C\ :sub:`1` can be charged. Using the calculated current in Q\ :sub:`5` and the value of C\ :sub:`1` estimate what the slew rate should be and compare this with what you measured.

**Shortcomings**

While there are no perfect op amps, some monolithic devices are very, very good. This circuit has some real shortcomings as follows:

| No provision for thermal stability – operate at room temperature only.
| Relatively high input offset voltage, but can be nulled.
| Lack of output overcurrent protection.
| Limited open loop voltage gain – the open loop voltage gain of a monolithic device is at least an order of magnitude higher.
| Potentially high crossover distortion

Questions:
~~~~~~~~~~

Measure quiescent power supply current.

Null input offset voltage – set up with a voltage gain of 100, ground input and adjust R\ :sub:`2` or R\ :sub:`3` so that the output voltage is zero

Observe thermal stability – after the input offset voltage has been nulled, blow hot air on different devices in the circuit and watch the output voltage shift (carefully use a hair dryer)

Measure input bias current – add high value 100K resistor in series with input terminals, measure voltage drop across resistor, then calculate the current.

Plot frequency response at 0.5 Vp-p output and at full output voltage (use large value for C\ :sub:`1`)

Measure open loop gain – set up as an inverting amplifier – with full output voltage, measure input node voltage – divide AC output voltage by AC input node voltage (note, this cannot be done with a monolithic op amp due to its extremely high open loop gain).

Determine maximum slew rate in both polarities (positive going and negative going)

Here is a good technical paper on how to make :adi:`Simple Op Amp Measurements <en/analog-dialogue/articles/simple-op-amp-measurements.html>`.

Perhaps you can experiment upon and improve this relatively simple circuit design

PCB Construction
----------------

PC board design files for this experiment, and other related extensions, can be found on the ADI GitHub education tool repository. The PCB schematic is shown in figure 3 and a photo of the board is shown in figure 4. Component placement is shown in figure 5.

Power and bias rail decoupling capacitors C2, C3 and C4 are optional. Pin sockets are best used for Frequency compensation capacitor C1 to allow for experimenting with different values.

Resistor R4 sets the bias current for the first and second stages based on the power supply voltage. The value can be adjusted based on the range of supply voltages the amplifier will be operating. For +5 operation 1.5kΩ is a good working value. For 10 V (+/- 5V) a 3.3kΩ is a good working value.

Resistors R5 and R6 set the steady state bias current in the output stage. Using 2N3904 and 2N3906 in the output stage, R5 = 6.8kΩ and R6 = 10kΩ is a good safe starting point.

Output emitter resistors R7 and R8 can be any small value in the range of 2.7 to 10 ohms.

:git-education_tools:`Experiment board design files <experiment-boards>`

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-13-f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Operational Amplifier PCB schematic.


The PC Board version with the standard 8 pin DIP single op-amp footprint is shown in figure 4. A version with all the pins in a single row (SIP) footprint is shown in figure 5. Either version can be inserted into a solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/trabsistor-op-amp-pcb.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Example constructed Operational Amplifier PC Board, DIP version.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/transistor-op-amp-pcb2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, Example constructed Operational Amplifier PC Board, SIP version.


To make it somewhat easier to install the components, figure 6 for the DIP version and figure 7 for the SIP version are provided.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/transistor-op-amp-placement.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, DIP PC Board component placement.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/transistor-op-amp-placement2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, SIP PC Board component placement.


For Further Reading:
--------------------

:adi:`Increase amplifier output drive using a push-pull stage <en/technical-articles/increase-amplifier-output-drive-using-a-push-pull-amplifier-stage.html>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/electronics>`
