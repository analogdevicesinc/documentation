Active Electronic Loads
=======================

Objective:
----------

The objective of this document is to demonstrate techniques that use the ADALM1000 (M1k) and ADALM2000 (M2k) modules as active electronic current sink loads for the characterization of power sources such as chemical batteries, solar panels and voltage regulators (power supplies).

Caution:
--------

Performing tests on circuits that generate, operate at, or use high voltages present a significant shock hazard and great care should be taken while working with such systems.

Note: Measuring Voltages Outside 0 to 5 V Range:
------------------------------------------------

Personal test instruments (USB based data acquisition systems) generally support voltages in the +5 V to -5 V range for signal generation, signal measurement and power supplies. Some may provide built-in resistor dividers that extend the input voltage measurement range to as much as +/- 25V for the M2k. However, an external resistor voltage divider can be used to extend any instrument’s input voltage measurement capability beyond its specified design range such as using a 10X passive scope probe. To keep production cost of the ADALM1000 board low, certain tradeoffs were made. One was to forego programmable input gain ranges that use resistor dividers and perhaps adjustable frequency compensation capacitors. This is a problematic limitation of the ADALM1000 limiting the input voltage range from 0 to +5 V. Users will come up against this restriction when testing circuits powered by (generally larger) supply voltages other than the built in supplies.

**One quick note of caution before proceeding!**

Before building or testing any circuits that generate or operate from power supplies outside the native 0 to 5 V range of the ADALM1000 you need to protect the analog inputs when in Hi-Z or Split I/O modes and extend the usable range of voltages. There are large protection diodes connected between the analog I/O pins and ground and the internal +5 volt power supply which are generally reverse biased when the voltage on the pins is in the range of 0 to 5 V. If the voltage on the pin were to go more than a forward diode voltage beyond this range the diodes will possibly conduct large currents.

Full details on how to construct and calibrate external voltage dividers can be found in this document: :doc:`Measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>` **It is highly recommended that you read and follow this document before attempting any experiments on circuits powered by voltage outside 0 to 5 V.**

Background:
-----------

In the following examples a solar panel is shown as the power source under test but any power sources such as chemical batteries, solar panels, DC-DC voltage converters, and power supplies can be tested using these methods. By using a transistor, either BJT or MOS, as a current sink, lower value resistors can be used in the emitter / source leg. Most of the power can be dissipated in the transistor rather than the resistor.

Thermal Resistance Primer:
~~~~~~~~~~~~~~~~~~~~~~~~~~

The current flowing through any "black box", multiplied by the voltage drop across that box, equals the power entering that will need to also leave somehow. In the case of an active load (or any load for that matter), the power leaves as heat. (If the "load" is an LED, some of that power would leave as light, if it is a motor, the power might leave as mechanical power through the rotating shaft.)

Before even starting to build any active load circuitry, we know that we're going to have to get rid of potentially a lot of heat. The power transistors and LT3080 regulator from the ALP2000 parts kit are in the very common T0-220 package, with a tab for mounting to a heat sink such as the ones shown below.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/actice-loads-fig0.png
   :align: center
   :width: 350px

.. container:: centeralign

   Heavy Duty TO-220 Heat sinks


Further defining terms:
^^^^^^^^^^^^^^^^^^^^^^^

**Thermal Resistance** - Resistance to the flow of heat, expressed as the temperature rise due to a given power flowing through the resistance.

**T\ J** - Junction Temperature - The temperature of the "important part" of the silicon die. The junction must be kept below a certain temperature in order for the part to function properly. It is mounted to the metal tab inside the part, and encased in plastic.

**T\ AMBIENT** - Ambient Temperature - the temperature of the environment, far away from the part.

**T\ C** - Case Temperature - Temperature of the interface between the package and heat sink or printed circuit board.

These seemingly simple terms are in reality quite difficult to measure. Measuring "ambient" is not that bad; an appropriate thermometer can be used to measure the temperature of the thermal mass that the part is dumping heat into, which is often the air in the room. But what about the "case"? The case temperature is defined as the temperature of a large block of metal (like copper or aluminum), to which the package is optimally mounted. It represents a theoretical minimum thermal resistance, not achievable in actual applications (for most device packages). So while the top of the device's package is literally part of the case, a measurement of its temperature is NOT the "case temperature".

This description from Vishay Application Note 827 illustrates this point: "For the MOSFET/heat sink assembly, a specially designed heat sink assembly of a copper block (4 in. x 4 in. x 0.75 in.) was used to simulate an infinite heat sink attached to the case of the TO-220 device."

Junction temperature is, as the name suggests, the temperature of the operational semiconductor junction in the device, which in reality may be many junctions in a complex circuit. And it is this temperature that must be kept below the maximum specified; if exceeded, the device is not guaranteed to function properly. But note that unless your device has a built-in temperature sensor (and some do), it is difficult to measure the junction temperature directly.

Note that the maximum junction temperature can be well above the boiling point of water - too hot to touch. So using your finger to test if a circuit is cool enough is not only dangerous, it is completely inaccurate. So how are these numbers used? The objective is to keep the junction below the maximum allowed. So we can use knowledge of how much power is dissipated in the part (near the junction), and the thermal resistance to the air, to calculate how hot the junction will get.

T\ :sub:`J` = T\ :sub:`AMBIENT` + P\ :sub:`D` \* Θ\ :sub:`JA`

Where P\ :sub:`D` is the power dissipation.

One very useful mental model is to think of thermal resistances as electrical resistances, such that:

1° C/W = 1 Ω

1 W of dissipation = 1 A of current being driven through the resistance

1 V = 1 °C temperature rise across the resistance.

Materials:
----------

| ADALM1000 hardware module (M1k)
| ADALM2000 hardware module (M2k)
| TIP31 power NPN transistor
| IRF510 power NMOS transistor
| 6.2 ohm power resistor and / or various other resistors
| TO-220 heat sink

Use Examples for M1k as an active load
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the following example scenarios, a solar panel is shown as the power source under test. Other power sources such as switch mode DC-DC converters or even chemical batteries can be tested.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/actice-loads-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Both Channels of M1k as BJT active current sink


Because the voltage of the power source under test is likely larger than the allowed 0 to 5 V input range of the M1k a voltage divider must be used when measuring the voltage. Resistor R\ :sub:`1` and R\ :sub:`2` used in combination with the 1 Meg Ω input resistance of the BIN input of the M1k (when in the split I/O mode). Using just one 1 Meg resistor R\ :sub:`1` and leaving out R\ :sub:`2` forms a divide by 2 voltage divider for a 0 to 10 V range. Including the second 1 Meg resistor, R\ :sub:`2`, forms a divide by 3 voltage divider for a 0 to 15 V range. Even lower values for R\ :sub:`2` will allow even larger voltages to be measured. See this page on :doc:`measuring voltages beyond 0 to 5V with the M1k </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>` for more examples.

Likewise the voltage of the power source under test is larger than the 0 to 5 volt output range of the Channel A voltage source. NPN transistor Q\ :sub:`1` (a TIP31 power device with an appropriate heat sink) connected as a common base amplifier is used to convey the emitter current from the load resistor, R\ :sub:`E1`, to the collector above the +5 volt rail (voltage at the base). This current from the collector flows out of the power source under test. The actual current supplied by the power source under test, the collector current, will be slightly smaller than the measured emitter current by the β of Q\ :sub:`1`. In most cases this will be a small error and can be ignored but a Darlington power NPN could be used to reduce the current lost even further. The precise value of R\ :sub:`E1` is not important in that the M1k internally measures the current in CHA directly. The current sink capability of one channel of the M1k is limited to 200 mA. If the second channel is used along with a second emitter resistor, R\ :sub:`E2`, in figure 1, the maximum sink current can be doubled to 400 mA.

Taking a few specifications from the TIP31 datasheet we know that the maximum collector current is 3 Amps, the maximum collector emitter voltage is 40 Volts. This implies a maximum power dissipation of 120 Watts. The maximum junction temperature is 150 C. Starting with a 25 C ambient temperature leaves a delta temperature of 125 degrees. The combined junction to ambient thermal resistance of the heat sink would need to be less than 1\ :sup:`o` C/W. In this particular application scenario, the current is limited to the 400 mA possible from the M1k, so the maximum power at 40 V would be 16 Watts. The combined junction to ambient thermal resistance of the heat sink would need to be less than 7.8125\ :sup:`o` C/W.

In figure 2 we have substituted a power NMOS device, M\ :sub:`1`, for the power NPN device. In an NMOS transistor there is no loss of current to the gate terminal so the actual current supplied by the power source under test, the drain current, will be the same as the measured source current. As in figure 1 the second channel can be connected in parallel using a second R\ :sub:`S` to double the maximum current.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/actice-loads-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, One channel of M1k as NMOS active current sink


When characterizing power sources such as solar panels, one of the characteristic specifications is short circuit current. While the test configurations of figures 1 and 2 allow for voltages greater than 5 volts they do not allow loading the panel at 0 volts (i.e. short circuit). In figure 3 the negative terminal of the panel is moved to the fixed +5 V output pf the M1k. Just as the adjustable AWG channels of the M1k the fixed 5 V output can both source and sink up to 200 mA. In this configuration the current in Channel A can be increased to the point where voltage measured at the positive terminal of the panel is also +5 V, the same as the negative terminal. Now there will be 0 V across the panel and this will be the short circuit current.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/actice-loads-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, By moving Negative terminal of solar panel to +5V rail, possible to measure 0 V short circuit current.


Use Examples for M2k as an active load
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a comparison, the M2k module can be used in a similar way as an active electronic load. The M2k cannot directly measure current so the differential inputs of channel 1 are used to measure the voltage across the emitter load resistor and thus calculate the current based on the known value of R\ :sub:`E`. Also, the AWG channels of the M2k include an internal 50 Ω resistor and can only supply up to 50 mA of current. This forces us to drive the base of power NPN device Q\ :sub:`1` with AWG source W1 rather than the emitter (as a common emitter amplifier). As shown in figure 4. The M2k provides a selectable 10X internal resistor divider so the external voltage divider R\ :sub:`1`/R\ :sub:`2` will not be needed here for voltages less than +25 V.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/actice-loads-fig4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, M2k driving BJT active current sink


In figure 5, as in figure2, we have substituted a power NMOS device, M\ :sub:`1`, for the power NPN device. In an NMOS transistor there is no loss of current to the gate terminal so the actual current supplied by the power source under test, the drain current, will be the same as the measured source current.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/actice-loads-fig5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, M2k as NMOS active current sink


Closed Loop Current Sink.
-------------------------

The examples shown so far are open loop in that a voltage is set (across a resistor) and the resulting current measured. In a closed loop current sink the set voltage is actively forced across a known resistor R\ :sub:`E`, such as 1 Ω, to result in a controlled current. An op-amp can be added to the previous examples to produce a controlled sink current as shown in figures 6 and 7. The output sink current will be equal to Vset / R\ :sub:`E`. The Rail-Rail input/output CMOS AD8542 is a good choice in this example. These examples show the use of an NPN power transistor but a power NMOS can be used just as well.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/actice-loads-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, M1k closed loop active current sink.


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/actice-loads-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, M2k closed loop active current sink.


Current Source for Negative Supplies.
-------------------------------------

To test negative power sources that are referenced to ground a current source active load is needed. To make any of these positive (voltage) current sink examples into a negative (voltage) current source simply swap out the NPN / NMOS transistor for a PNP / PMOS device. Figure 8 shows how figure 2 might be flipped around to test a negative power supply. Any of the previous N type examples can be converted in a similar way.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/actice-loads-fig8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, Negative active current source.


**For Further Reading:**

| `Active Load <https://en.wikipedia.org/wiki/Active_load>`__
| :adi:`A Closed-Loop, Wideband, 100A Active Load <media/en/technical-documentation/application-notes/an133f.pdf>`

**Return to Lab Activity Table of Contents**
