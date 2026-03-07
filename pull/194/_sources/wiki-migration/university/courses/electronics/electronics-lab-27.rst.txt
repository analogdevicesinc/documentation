Activity: TTL inverter and NAND gate, For ADALM2000
===================================================

Objectives:
-----------

A variety of digital logic circuit techniques have been in use since the 1960s, when integrated logic gates were first produced. In this Lab activity, the Transistor Transistor Logic (TTL) circuit inverter (NOT gate) and 2 input NAND gate configurations are examined.

Background:
-----------

The schematic of a Transistor Transistor Logic (TTL) inverter is shown in figure 1. This circuit overcomes the limitations of the single transistor inverter circuit. The basic TTL inverter consists of three stages. A current steering input, a phase splitting stage and an output driver stage.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a27_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 TTL Inverter


The input stage transistor Q\ :sub:`1` performs a current steering function. It can be thought of as a back-to-back diode arrangement. The transistor is operated in either forward or reverse mode to steer current to or from the second stage transistor's base, Q\ :sub:`2`. The forward current gain or ß\ :sub:`F`, is much larger than the reverse ß\ :sub:`R`. it provides a higher discharge current to discharge the base when turning it off.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a27_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Equivalent circuit of input current steering stage


Second stage transistor, Q\ :sub:`2` in figure 1, is a phase splitter transistor to drive both halves of the pull up and pull down output stage. It allows the input condition to be produced in opposite phases so that the output transistors can be driven in anti-phase. This allows Q\ :sub:`3` to be on when Q\ :sub:`4` is off and vice versa as shown in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a27_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Phase splitting stage


The output transistor pair, Q\ :sub:`3` and Q\ :sub:`4` along with diode D\ :sub:`1` are referred to as a totem-pole output as shown in figure 4. This output configuration provides the ability to both actively source or sink current and is useful for driving capacitive loads. Resistor R\ :sub:`4`, serves to limit the current available from V\ :sub:`CC`. Under steady-state conditions, only one transistor is on at a time.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a27_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Output Stage


The diode, D\ :sub:`1`, serves to increase the effective turn on voltage of Q\ :sub:`4` which allows it to be turned off before Q\ :sub:`3`\ turns fully on. This helps prevent potentially large surge currents from flowing in the output stage during transitions between logic states. Resistor R\ :sub:`4` also serves to limit the current that is allowed to flow in the output stage. The disadvantage is that the logic high voltage is reduced by an amount of the diode drop as shown in figure 7.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - 100 KΩ Resistor
| 1 - 2.2 KΩ Resistor
| 1 - 470 Ω Resistor
| 1 - 100 Ω Resistor
| 1 - small signal diode (1N914)
| 5 - small signal NPN transistors (2N3904)

TTL Inverter
------------

Directions:
~~~~~~~~~~~

Build the circuit shown in figure 5 on your solder-less bread board. The NPN transistors supplied with your ADALP2000 Parts Kit are limited to 5 2N3904 and 1 TIP31 power transistor. Use the 5 2N3904 transistors and a 1N914 diode. First, connect the TTL inverter circuit on your breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a27_f5a.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 5 TTL Inverter


Hardware Setup:
~~~~~~~~~~~~~~~

Connect your circuit to the ADALM2000 I/O connector as indicated by the green boxes. It is best to ground the unused negative scope inputs when not being used. The breadboard connections are shown in figure below.


|image1|

.. container:: centeralign

   Figure 6 TTL Inverter Breadboard Circuit


Procedure:
~~~~~~~~~~

Configure waveform generators, W1, with 100 Hz triangle wave with 0 V offset and 6 V amplitude peak-to-peak peak-to-peak values. Use the oscilloscope in the x-y mode to observe the voltage-transfer curve of the circuit.


|image2|

.. container:: centeralign

   Figure 7 TTL inverter transfer curve


TTL NAND Gate
-------------

.. _directions-1:

Directions:
~~~~~~~~~~~

By adding another input to the TTL inverter, a TTL NAND gate can be made. Connect the TTL inverter circuit, shown on figure 8.


|image3|

.. container:: centeralign

   Figure 8 TTL two input NAND Gate


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Connect your circuit to the ADALM2000 I/O connector as indicated by the green boxes. It is best to ground the unused negative scope inputs when not being used. The breadboard connections are shown in figure below.


|image4|

.. container:: centeralign

   Figure 9 TTL two input NAND Gate Breadboard Circuit


.. _procedure-1:

Procedure:
~~~~~~~~~~

Configure waveform generators, W1, with 100 Hz triangle wave with 0 V offset and 6 V amplitude peak-to-peak values and W2, 100 Hz triangle wave with 0 V offset and 6 V amplitude peak-to-peak values and 90° phase. Use the oscilloscope to observe the output of the circuit, CH2.


|image5|

.. container:: centeralign

   Figure 10 TTL NAND Gate Output Waveform


Measurements:
-------------



.. raw:: html

   <details><summary>Click to expand</summary>

**Transfer Characteristic:**

The transfer characteristic of a TTL inverter can be deduced by applying a slowly ramping input voltage and determining the sequence of events which takes place with respect to changes in the states of conduction of each transistor and the critical points at which the onset of these changes happen. Consider the circuit input vs. output transfer characteristic curve shown in figure 6.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a27_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6 TTL inverter input vs output transfer curve


**Break Point P1**

With the input near 0 volts and the base current supplied to Q\ :sub:`1`, this transistor can conduct in the forward mode. Since the only source of collector current is the leakage of Q\ :sub:`2`, Q\ :sub:`1` will be driven into saturation. This ensures that Q\ :sub:`2` is off which, in turn, means that Q\ :sub:`3` is off. While there is no load present, there are leakage currents flowing in the output stage which allow the transistor Q\ :sub:`4` and the diode D\ :sub:`1` to be barely conducting in the ON state.

| **V\ OUT = V\ CC - V\ BE4 - V\ D1**
| **V\ OUT = 5 - 0.6 - 0.6 = 3.8V**
| **Point P1: V\ IN = 0.5, V\ OUT = 3.8V**
| **Break Point P2**

As the input voltage is slightly increased, the above state continues until, with Q\ :sub:`1` on and in saturation, the voltage at the base of Q\ :sub:`2` rises to the point of conduction. Then:

| **V\ IN = V\ BE2 - V\ CE1(SAT) = 0.6 - 0.1 = 0.5**
| **Point P2: V\ IN = 0.5, V\ OUT = 3.8V**
| **Break Point P3**

As the input voltage is further increased, Q\ :sub:`2` becomes more conducting, turning fully ON. Base current to Q\ :sub:`2` is supplied by the now forward biased base-collector junction of Q\ :sub:`1` which is still in saturation. Eventually, Q\ :sub:`3` reaches the point of conduction. This happens when:

| **V\ IN = V\ BE2 + V\ BE3 - V\ CE1(SAT)**
| **V\ IN = 0.7 + 0.6 - 0.1 = 1.2V**
| Note that with transistor Q\ :sub:`3` just at turn on, V\ :sub:`BE3` = 0.6V which means that the current through R\ :sub:`3` is 0.6V/470Ω = 1.27mA. With operation in the linear active region, the collector current in Q\ :sub:`2` is 0.97 × 1.27mA = 1.23mA. ˜ a\ :sub:`F` I\ :sub:`E2`

The voltage drop across R\ :sub:`2` is then V\ :sub:`R2` = 1.23mA × 2.2 kΩ = 2.7V.

Under this condition the collector to emitter voltage drop across Q\ :sub:`2` is:

| **V\ CE2 = V\ CC - V\ R2 - V\ R3**
| **V\ CE2 = 5 - 2.7 - 0.6 = 1.7V**
| This confirms that Q\ :sub:`2` is still operating in the forward active mode.

With Q\ :sub:`3` beginning to conduct there is a conduction path for current through Q\ :sub:`4` and the diode, D\ :sub:`1`, which then turns fully ON. In this case:

| **V\ O = V\ CC - V\ R1 - V\ BE4 - V\ D1**
| **V\ O = 5 - 0.94 - 0.65 - 0.6 = 2.81V**
| **Point 3: V\ i = 1.2V, V\ O = 2.81V**
| **Break Point P4**

As the input voltage is further increased, Q\ :sub:`2` conducts more heavily, eventually saturating. Q\ :sub:`3` also conducts more heavily and eventually reaches the point of saturation also. As Q\ :sub:`2` becomes more conducting, its collector current increases. This in turn increases the voltage drop across R\ :sub:`1` which in turn means that the voltage across Q\ :sub:`2` i.e. V\ :sub:`CE2` drops. This falls below the requirement for conduction in Q\ :sub:`4` and the diode, D\ :sub:`1`, so that both of these turn OFF prior to the saturation of Q\ :sub:`3`.

When Q\ :sub:`3` reaches the edge of saturation:

| **V\ i = V\ BE2 + V\ BE3 - V\ CE1**
| **V\ i = 0.7 + 0.7 - 0.1 = 1.5V**
| **Point 4: V\ i = 1.4V, V\ O = 0.2V**
|

.. raw:: html

   </details>


Questions:
----------

The output circuitry of a typical TTL logic gate is commonly referred to a totem-pole output because the two output transistors are stacked one above the other like carvings on a totem pole. Is a gate circuit with a totem-pole output stage able to source load current, sink load current, or do both?

.. admonition:: Download
   :class: download

   \*Resources:\*

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/ttl_inv_and_nand_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/ttl_inv_and_nand_ltspice`
   


For Further Reading:
--------------------

http://en.wikipedia.org/wiki/Transistor-transistor_logic

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a27f6a.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a27_f7.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/a27_f5.png
   :width: 550px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/a27f9.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/a27_f10.png
   :width: 550px
