Activity: The MOS transistor connected as a diode, For ADALM1000
================================================================

Objective:
----------

The purpose of this activity is to investigate the forward current vs. voltage characteristics of a MOS field effect transistor (NMOS and PMOS) connected as a diode.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

The Diode Connected NMOS transistor
-----------------------------------

Materials:
~~~~~~~~~~

| ADALM1000 Hardware Module
| Solder-less Breadboard
| 1 - 100 Ω Resistor
| 1 - Small signal enhancement mode NMOS transistor (CD4007 CMOS array)
| 1 - Small signal enhancement mode PMOS transistor (CD4007 CMOS array)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 300px

.. container:: centeralign

   CD4007 CMOS array pinout


NMOS Directions:
~~~~~~~~~~~~~~~~

The current vs. voltage characteristics of the gate source of an enhancement mode NMOS transistor can be measured using the ALM1000 hardware and the following connections. Set up the breadboard with the channel A generator attached to one end of resistor R\ :sub:`1`. Connect the Gate and Drain of M\ :sub:`1` to the opposite end of R\ :sub:`1` as shown in the diagram. The Source of M\ :sub:`1` is connected to GND (V\ :sub:`SS` pin 7). Connect scope channel B to the gate - drain node of M\ :sub:`1` (pins 6 and 8 for example). Remember to ensure that both power supply pins (device backgates), V\ :sub:`SS` pin 7 and V\ :sub:`DD` pin 14 are connected appropriately to GND and +5 V respectively. All other pins can be left floating. Be sure that the power supply is not connected while you build your circuit. Once you are sure all your connections are correct then connect the supply last.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab3m_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 NMOS diode connection diagram


Hardware Setup:
~~~~~~~~~~~~~~~

The waveform generator should be configured for a 100 Hz triangle wave with 5 volt Max and 0 V Min. The CA-I signal trace measures the current in the resistor (and in the transistor). Scope channel B is connected to measure the voltage across the transistor. The current flowing through the transistor is the current measured in channel A (CA-I) or the Math trace voltage difference between CB-V - CA-V divided by the resistor value (100 Ω).

Procedure:
~~~~~~~~~~

Load the captured data into Excel and calculate the current. Calculate and plot the current vs. the voltage across the transistor (V\ :sub:`GS`). No current should flow in the reverse direction. In the forward conduction region, the voltage, current relationship should be quadratic. Also calculate and plot the square root of the current vs. the voltage across the transistor (V\ :sub:`GS`). Compare the shape of the two plots and comment.

Questions:
~~~~~~~~~~

| By plotting the data measured for I\ :sub:`D` vs V\ :sub:`GS`, find and report values of V\ :sub:`TH` and K (W/L).
| Are these V\ :sub:`TH` and K (W/L) values consistent with your measurements on the other two NMOS transistors on the chip?

PMOS Directions:
~~~~~~~~~~~~~~~~

Repeat the experiment using one of the PMOS devices in the CD4007. The connections are similar and as shown on figure 2 below. The Source of M\ :sub:`1` is connected to +5V (V\ :sub:`DD` pin 14). Connect scope input B to the gate - drain node of M1 (pins 6 and 13 for example). Remember to ensure that both supply pins (device backgates), V\ :sub:`SS` pin 7 and V\ :sub:`DD` pin 14 are connected appropriately to ground and +5 V respectively. All other pins can be left floating. Be sure that the power supply is not connected while you build your circuit. Once you are sure all your connections are correct then connect the supply.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab3m_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 PMOS diode connection diagram


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 5 volt Max and 0 V Min. The CA-I signal trace measures the current in the resistor (and in the transistor). The scope channel B is connected to measure the voltage across the transistor. The current flowing through the transistor is the current measured in channel A (CA-I) or the Math trace voltage difference between CB-V - CA-V divided by the resistor value (100 Ω).

.. _procedure-1:

Procedure:
~~~~~~~~~~

Load the captured data in to Excel and calculate the current. Calculate and plot the current vs. the voltage across the transistor (V\ :sub:`GS`). No current should flow in the reverse direction. In the forward conduction region, the voltage, current relationship should be quadratic. Also calculate and plot the square root of the current (I\ :sub:`D`) vs. the voltage across the transistor (V\ :sub:`GS`). Compare the shape of the two plots and comment.

.. _questions-1:

Questions:
~~~~~~~~~~

| By plotting the data measured for I\ :sub:`D` vs V\ :sub:`GS`, find and report values of V\ :sub:`TH` and K (W/L).
| Are these V\ :sub:`TH` and K (W/L) values consistent with your measurements on the other two PMOS transistors on the chip?
| How do the V\ :sub:`TH` and K (W/L) values for the NMOS and PMOS compare?

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/mos_as_diode_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/mos_as_diode_bb`

**For Further Reading:**

| http://en.wikipedia.org/wiki/Field-effect_transistor
| http://en.wikipedia.org/wiki/MOSFET

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
