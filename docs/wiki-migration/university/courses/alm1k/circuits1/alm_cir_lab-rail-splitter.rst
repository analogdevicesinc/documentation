Battery Voltage "Rail-Splitter"
===============================

Objective:
----------

The objective of this document is to examine switched capacitor DC-DC converter circuits as applied to splitting a single battery voltage into positive and negative voltages or "rails" with respect to a single common or "ground" node.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

There are a number of reasons why an engineer would want to “split” a voltage source such as a battery in their design. Sometimes parts of the circuit, like a sensor or an IC, require a bipolar supply. Other reasons are to make the best use of the dynamic range of an ADC if it has a bipolar input, or to generate a mid-rail bias voltage in a single supply system.

There are several different meanings of the phrase “rail splitter.” The usual meaning is creating a new “0V” reference point, usually the mid-point Vin/2 of a single supply voltage Vin.

The available total battery voltage remains the same as before, only you can view it as being distributed as a bipolar supply ±VBattery/2 about the new “0V” or common ground reference. The new “0V” or common voltage node can be called a “virtual ground”.

A rail splitter that creates a new common ground reference must be able to source or sink load current from either "rail" and into and out of the “virtual ground”. It must be stable with capacitive decoupling load on its output(s). A linear technique using a resistive voltage divider and buffer amplifier can be used to generate VBattery/2, but a switched-mode conversion can provide higher efficiency and be used for high output current.

Materials:
~~~~~~~~~~

| ADM660
| 1 – 10 uF capacitor C\ :sub:`1`
| 2 – 47 uF capacitor C\ :sub:`2,3`
| 1 – 9 V battery and connector

In Figure 1, a switched-capacitor voltage inverter, ADM660, is configured as a "rail-splitter". This configuration provides a bipolar, +/- 4.5 Volt, dual-rail power supply from a 9 V battery. The circuit is useful in battery powered systems that include one or more dual-supply ICs. After the power is applied, the flying capacitor, C\ :sub:`1`, is connected alternately across the storage capacitors, C\ :sub:`2` and C\ :sub:`3`. This switching operation equalizes the voltages across those capacitors and draws current from the battery as required to maintain the two output voltages with respect to ground (GND node) equal to the battery voltage divided by 2. Generally C\ :sub:`2` and C\ :sub:`3` are the same value.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm_cir_lab-rail-splitter-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, ADM660 Split 9 V battery voltage


If the loads across +4.5 V and -4.5 V with respect to ground are equal, the IC runs in a low current state and draws minimum current from the battery. To keep the battery centered around GND, the mid-rail level, the flying capacitor need only supply the difference current due to unbalanced load currents.

The 600 µA typical quiescent current of the ADM660 dominates the efficiency for load currents less than 600 µA, but for currents greater than 1 mA, the efficiency is greater than 90%--an important feature for low-power or battery-powered systems. The voltage error and efficiency vary with the load current.

This switched-capacitor circuit provides better regulation than that of a simple resistor voltage divider and better efficiency than that of a simple combination of a divider and an op-amp buffer. The circuit's main drawback is the increase in output noise due to the high frequency switching nature of the ADM660.

The maximum battery voltage is limited to twice the maximum voltage allowed between pins 8 and 3 or between pins 3 and 5; which is, 7 V. The minimum battery voltage is limited to twice the minimum voltage allowed between pins 8 and 3, which is 3.5 V with pin 6 (LV) not connected and 1.5 V with pin 6 (LV) connected to ground.

Note:
~~~~~

When using the ADALM1000 hardware module to measure nodes in a circuit with voltages outside the 0 to +5 V range with respect to "ground" be sure to use the voltage divider techniques outlined in this document on :doc:`measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>`.

Using the LT1054 from the ADALP2000 parts kit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _materials-1:

Materials:
~~~~~~~~~~

| LT1054
| 1 – 10 uF capacitor C\ :sub:`1`
| 2 – 47 uF capacitor C\ :sub:`2,3`
| 1 – 4.7 KΩ resistor R\ :sub:`1`
| 1 – 9 V battery and connector

The larger 3 mA typical quiescent current of the LT1054 flowing from pin 8 to pin 3 causes an imbalance in the charge (current) delivered from the flying capacitor C\ :sub:`1` to storage capacitor C\ :sub:`2`. This imbalance for small load currents on the negative rail to ground, i.e. less than the quiescent current, will cause an imbalance in the two output voltages with respect to ground. R\ :sub:`1` is added to set a minimum current from GND to the negative output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm_cir_lab-rail-splitter-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, LT1054 Split 9 V battery voltage


Other than the inclusion of R\ :sub:`1` the LT1054 circuit operates exactly like the ADM660 circuit. Like the ADM660, the maximum battery voltage is limited to twice the maximum voltage allowed between pins 8 and 3 or between pins 3 and 5; which is, 7 V for the LT1054L and 15 V the LT1054. The minimum battery voltage is limited to twice the minimum voltage allowed between pins 8 and 3, which is 3.5 V.

**For Further Reading:**

| :adi:`ADM660 Datasheet <media/en/technical-documentation/data-sheets/ADM660_8660.pdf>`
| :adi:`LT1054 Datasheet <media/en/technical-documentation/data-sheets/1054lfh.pdf>`

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
