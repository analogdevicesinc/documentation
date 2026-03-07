Activity: The Band-Gap Voltage Reference
========================================

Objective:
----------

The objective of this Lab activity is to investigate the band-gap voltage reference.

Background:
-----------

The principal behind the band-gap voltage reference is to sum a voltage which is proportional to absolute temperature (PTAT) with a voltage that has an equal but opposite ( complementary) negative temperature drift (CTAT) to produce a voltage which has effectively zero temperature drift. The zero gain amplifier and stabilized current source combination produces a PTAT current at its output. This current will produce a PTAT voltage when flowing through a resistor. The V\ :sub:`BE` of a BJT has a well defined negative temperature drift which when summed with a properly scaled PTAT voltage will result in a near zero drift output voltage. This combined voltage is approximately 1.2 Volts which is very nearly the band-gap voltage of silicon hence the name.

In the first version shown in figure 1, A PTAT current source (Q\ :sub:`1`, Q\ :sub:`2A,B`, R\ :sub:`2`) can be used in conjunction with a PNP current mirror stage (Q\ :sub:`3`,Q\ :sub:`4A,B`) in negative feedback to build a circuit which provides an output voltage which is the sum of a PTAT voltage (R\ :sub:`1`) and the V\ :sub:`BE` of Q\ :sub:`1` which is constant or regulated over a range of input voltages and over temperature. There is a problem with the circuit in version 1. The current available to an output load is limited by the feedback current supplied from NPN Q\ :sub:`2` mirrored through PNPs Q\ :sub:`3` and Q\ :sub:`4`. Any current that is diverted into an external load would reduce the current in R\ :sub:`1` and change the scaling of the PTAT voltage with respect to the voltage of the V\ :sub:`BE`. It would be desirable to build a circuit which provides a constant or regulated output voltage over not only a range of input voltages but also output load currents. A second circuit, shown in figure 2 utilizes an emitter follower output stage to provide the current to the output.

Materials:
----------

| Analog Discovery Lab hardware
| Solder-less breadboard
| 1 - 2.2 KΩ Resistor ( or any similar value )
| 1 - 100 Ω resistor
| 3 - small signal NPN transistors (2N3904 or SSM2212)
| 3 - small signal PNP transistors (2N3906 or SSM2220)

Directions:
-----------

The breadboard connections are as shown in the diagram below. The output of the AWG1 serves as the positive power supply and drives the emitters of both PNP transistors Q\ :sub:`3` and Q\ :sub:`4A,B`. Q\ :sub:`3` and Q\ :sub:`4A,B` are wired as a gain of two current mirror with their bases connected together with the collector of Q\ :sub:`3`. The collector of Q\ :sub:`4A,B` connects to resistor R\ :sub:`1`. Resistors R\ :sub:`1`, R\ :sub:`2` and transistor Q\ :sub:`1` are connected as a zero gain amplifier section. The V\ :sub:`BE` of the two parallel connected transistors Q\ :sub:`2,A,B` is smaller than the V\ :sub:`BE` of Q\ :sub:`1` by the voltage drop across R\ :sub:`2`. The base of transistor Q\ :sub:`2A,B` is connected to the zero gain output at the collector of Q\ :sub:`1`. The collector of Q\ :sub:`2` connects to the input side of the PNP current mirror at the base - collector of Q\ :sub:`3`. The channel 2+ (Single Ended) scope input is used to measure the output voltage at the collector of Q\ :sub:`4`.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_band-gap-f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1 Voltage reference, Version 1


Hardware Setup:
---------------

Waveform generator 1 should be configured for a 1 KHz triangle wave with 2 volt amplitude and 2V offset. The Single ended input of scope channel 2 (2+) is used to measure the stabilized output voltage at the collector of Q\ :sub:`4`.

Procedure:
----------

Plot the output voltage (as measured at the collector of Q\ :sub:`4`) vs. the input voltage. At what input voltage level does the output voltage stop changing i.e. regulate? This is called the "drop out" voltage. For input voltages above the drop out voltage, how much does the output voltage change for each volt of change at the input? The change in Vout / change in Vin is called line regulation. Connect a variable resistor from the output node to ground. With the input voltage fixed (i.e. connected to the fixed Vp board power supply), measure the output voltage for various settings of the resistor. Calculate the current in the resistor for each setting. How does the output voltage vary vs. output current? This is called load regulation.

Version 2:
----------

.. _background-1:

Background:
-----------

Looking at the circuit in figure 2 we see many of the same basic components from figure 1. Q\ :sub:`1`,Q\ :sub:`2`, R\ :sub:`1` and R\ :sub:`2` serve the same basic functions as before. However rather than use the PNP current mirror to provide negative feedback to regulate the circuit, a common emitter amplifier consisting of Q\ :sub:`3` and R\ :sub:`4` driving emitter follower Q\ :sub:`4` closes the feedback to the top of resistor R\ :sub:`3`. The output voltage will be the sum of a PTAT voltage across R\ :sub:`3` and the V\ :sub:`BE` of Q\ :sub:`3`. Emitter follower Q\ :sub:`4` supplies any varying load current that might be taken from the output node.

.. _materials-1:

Materials:
----------

| 1 - 2.2 KΩ Resistor
| 1 - 100 Ω resistor
| 1 - 10 KΩ variable resistor (potentiometer)
| 1 - 4.7 KΩ resistor
| 1 - 1.0 nF capacitor (102)
| (resistors can be any similar value selected for desired circuit operation)
| 4 - small signal NPN transistors (2N3904, SSM2212, CA3045)

.. _directions-1:

Directions:
-----------

The breadboard connections are as shown in figure 2. As before transistor Q\ :sub:`1` and resistors R\ :sub:`1` and R\ :sub:`2` are configured as a zero gain amplifier. Transistor Q\ :sub:`2` and variable resistor R\ :sub:`3`\ form a stabilized PTAT current source. If the SSM2212 matched NPN pair is used it is best that it be used for devices Q\ :sub:`1` and Q\ :sub:`2`. Common emitter stage Q\ :sub:`3` along with its collector load R\ :sub:`4` provide gain. Emitter follower Q\ :sub:`4` drives the output node and closes the negative feedback loop.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_band-gap-f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2 Regulator Version 2


.. _hardware-setup-1:

Hardware Setup:
---------------

Waveform generator W1 should be configured for a 1 KHz triangle wave with 2 volt amplitude and 2V offset. Scope channel 2 (2+) is used to measure the stabilized output voltage at the emitter of Q\ :sub:`4`.

.. _procedure-1:

Procedure:
----------

Repeat the drop out voltage, line and load regulation measurements for this circuit. How are they different than the Version 1 regulator circuit?

Questions:
----------

In the Version 1 circuit the net effective emitter ratio between Q\ :sub:`1` and Q\ :sub:`2` is four ( 2:1 for the NPNs and 2:1 in the PNP current mirror). How would the value for R\ :sub:`1` need to change if the combined ratio was reduced to 2:1 by removing one or the other of the parallel transistors, Q\ :sub:`2B` or Q\ :sub:`4B`? Would the circuit still function if the NPN and PNP emitter ratios were both 1:1?

**For Further Reading:**

| http:*en.wikipedia.org/wiki/Bandgap_voltage_reference
  http:*\ en.wikipedia.org/wiki/Brokaw_bandgap_reference
| http://www.analog.com/static/imported-files/tutorials/MT-087.pdf

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/eps/main-page>`\ **.**

Using an NPN transistor array:
------------------------------

The CA3045,46 ( LM3045, 46 ) NPN transistor array is a good alternate choice for building this example circuit. See pinout below.

.. image:: https://wiki.analog.com/_media/university/courses/eps/ca3046.png
   :align: center
   :width: 400px

All the emitters can be tired to ground ( pins 3,7,10,13 ). Devices Q\ :sub:`1`, Q\ :sub:`2` and Q\ :sub:`3` can be connected in parallel and serve as Q\ :sub:`2` in figure 2. Q\ :sub:`4` and Q\ :sub:`5`\ can be used for Q\ :sub:`1` and Q\ :sub:`3`\ in figure 2. An individual device such as a 2N3904 etc. can be used for Q\ :sub:`4` in figure 2. The 3 to 1 emitter area ratio will result in an output voltage very nearly 1.2 volts if R\ :sub:`1` and R\ :sub:`3` are both equal to 2K? (when R\ :sub:`2` is 100?).
