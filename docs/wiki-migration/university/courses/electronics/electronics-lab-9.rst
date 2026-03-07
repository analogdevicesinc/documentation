Activity: Regulated Voltage Reference - ADALM2000
=================================================

Version 1
=========

Objective:
----------

The zero gain amplifier (Q\ :sub:`1`, R\ :sub:`2`) and stabilized current source (Q\ :sub:`2`, R\ :sub:`3`) from activities 10 and 11 can be used in conjunction with a PNP current mirror stage (Q\ :sub:`3`,Q\ :sub:`4`) in negative feedback to build a circuit which provides a constant or regulated output voltage over a range of input voltages.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| 1 - 2.2KΩ Resistor ( or any similar value )
| 1 - 100Ω resistor
| 2 - small signal NPN transistors (2N3904 or SSM2212)
| 2 - small signal PNP transistors (2N3906 or SSM2220)

Directions:
-----------

The breadboard connections are as shown in the diagram below. The output of the AWG1 drives the emitters of both PNP transistors Q\ :sub:`3` and Q\ :sub:`4`. Q\ :sub:`3` and Q\ :sub:`4` are wired as a current mirror with their bases connected together with the collector of Q\ :sub:`3`. The collector of Q\ :sub:`4` connects to resistor R\ :sub:`1`. Resistors R\ :sub:`1`, R\ :sub:`2` and transistor Q\ :sub:`1` are connected as in the previous zero gain amplifier section. Since the V\ :sub:`BE` of Q\ :sub:`2` is always smaller than the V\ :sub:`BE` of Q\ :sub:`1`, You should select Q\ :sub:`1` and Q\ :sub:`2` from your inventory of devices such that (at the same collector current) Q\ :sub:`2`'s V\ :sub:`BE` is less than Q\ :sub:`1`'s V\ :sub:`BE`. The base of transistor Q\ :sub:`2` is connected to the zero gain output at the collector of Q\ :sub:`1`. The collector of Q\ :sub:`2` connects to the input side of the PNP current mirror at the base - collector of Q\ :sub:`3`. The 2+ (Single Ended) scope input is used to measure the output voltage at the collector of Q\ :sub:`4`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a9_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Regulator Version 1


Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/regulator_v1-bb.png

.. container:: centeralign

   Figure 2 Regulator Version 1 Breadboard Circuit


Waveform generator 1 should be configured for a 1 KHz triangle wave with 4 volt amplitude peak-to-peak and 2V offset. The Single ended input of scope channel 2 (2+) is used to measure the stabilized output voltage at the collector of Q\ :sub:`4` ( negative inputs 1= and 2- should be connected to ground).

Procedure:
----------

Plot the output voltage (as measured at the collector of Q\ :sub:`4`) vs. the input voltage. At what input voltage level does the output voltage stop changing i.e. regulate? This is called the "drop out" voltage. For input voltages above the drop out voltage, how much does the output voltage change for each volt of change at the input? The change in Vout / change in Vin is called line regulation. Connect a variable resistor from the output node to ground. With the input voltage fixed (i.e. connected to the fixed Vp board power supply), measure the output voltage for various settings of the resistor. Calculate the current in the resistor for each setting. How does the output voltage vary vs. output current? This is called load regulation.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 3 Regulator Version 1 Waveform


Version 2:
==========

.. _objective-1:

Objective:
----------

The problem with the circuit in regulator version 1 is that the current available to an output load is limited by the feedback current supplied from NPN Q\ :sub:`2` mirrored through PNPs Q\ :sub:`3` and Q\ :sub:`4`. It would be desirable to build a circuit which provides a constant or regulated output voltage over not only a range of input voltages but also output load currents. This second circuit utilizes an emitter follower output stage to provide the current to the output.

.. _materials-1:

Materials:
----------

| 1 - 2.2KΩ Resistor
| 1 - 100Ω resistor
| 1 - 10KΩ variable resistor (potentiometer)
| 1 - 4.7KΩ resistor (resistors can any similar value selected for desired circuit operation)
| 4 - small signal NPN transistors (2N3904 and SSM2212)

.. _directions-1:

Directions:
-----------

The breadboard connections are as shown in the diagram below. As before transistor Q\ :sub:`1` and resistors R\ :sub:`1` and R\ :sub:`2` are configured as a zero gain amplifier. Transistor Q\ :sub:`2` and variable resistor R\ :sub:`3`\ form a stabilized current source. If the SSM2212 matched NPN pair is used it is best that it be used for devices Q\ :sub:`1` and Q\ :sub:`2`. Common emitter stage Q\ :sub:`3` along with its collector load R\ :sub:`4` provide gain. Emitter follower Q\ :sub:`4` drives the output node and closes the negative feedback loop.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a9_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Regulator Version 2


.. _hardware-setup-1:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/regulator_v2-bb.png

.. container:: centeralign

   Figure 5 Regulator Version 2 Breadboard Circuit


Waveform generator W1 should be configured for a 1 KHz triangle wave with 4 volt amplitude peak-to-peak and 2V offset. Scope channel 2 (2+) is used to measure the stabilized output voltage at the emitter of Q\ :sub:`4`.

.. _procedure-1:

Procedure:
----------

Repeat the drop out voltage, line and load regulation measurements for this circuit. How are they different than the first regulator circuit?

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 6 Regulator Version 2 Waveform


For Further Study:
~~~~~~~~~~~~~~~~~~

ADI Mini Tutorial on :adi:`Voltage references <static/imported-files/tutorials/MT-087.pdf>`

Using an NPN transistor array:
==============================

The CA3045,46 ( LM3045, 46 ) NPN transistor array is a good alternate choice for building this example circuit. See pinout below.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a9_f3.png
   :align: center
   :width: 400px

All the emitters can be tired to ground ( pins 3,7,10,13 ). Devices Q\ :sub:`1`, Q\ :sub:`2` and Q\ :sub:`3` can be connected in parallel and serve as Q\ :sub:`2` in figure 2. Q\ :sub:`4` and Q\ :sub:`5`\ can be used for Q\ :sub:`1` and Q\ :sub:`3`\ in figure 2. An individual device such as a 2N3904 etc. can be used for Q\ :sub:`4` in figure 2. The 3 to 1 emitter area ratio will result in an output voltage very nearly 1.2 volts if R\ :sub:`1` and R\ :sub:`3` are both equal to 2KΩ (when R\ :sub:`2` is 100Ω).

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/regulated_voltage_reference_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/regulated_voltage_reference_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/regulator_v1-wav.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/regulator_v2-wav.png
   :width: 500px
