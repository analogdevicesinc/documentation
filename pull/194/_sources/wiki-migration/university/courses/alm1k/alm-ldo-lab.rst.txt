Activity: Linear Low Dropout Voltage Regulators - ADALM1000
===========================================================

Objective:
----------

The objective of this Lab Activity is to explore Low Dropout (LDO) Linear Voltage regulators and examine both bipolar and MOS circuit implementations.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage/measure current –V is added as in CA-V or when configured to force current/measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage/current. Such as CA-V, CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

Background:
-----------

The Dropout voltage of a linear regulator is defined as the minimum input to output voltage difference where the output voltage of the low dropout regulator (LDO) remains regulated (constant as the input voltage changes). The working region for LDO is the “regulation region”, where it can provide a steady output voltage, over a wide range of input voltages and load currents.

An LDO consists of a voltage reference, an error amplifier, a feedback voltage divider, and a series pass element, usually a bipolar or CMOS transistor (see Figure 1). The output current is supplied, in the case of figure 1(b), by the PMOS transistor, which in turn is controlled by the error amplifier. The error amplifier compares the reference voltage with the feedback voltage from the output and amplifies the difference. If the feedback voltage is lower than the reference voltage, the gate of the PMOS device is pulled lower, allowing more current to pass and increasing the output voltage. If the feedback voltage is higher than the reference voltage, the gate of the PMOS device is pulled higher, allowing less current to pass and decreasing the output voltage. This is a closed-loop system based around two main poles, the internal pole of the error amplifier/pass transistor and the external pole (figure 1(a)) of the output capacitor's equivalent series resistance (ESR).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ldo-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 LDO block diagram


LDO regulators are used to generate lower output voltages from a main power supply or battery. The output voltage is ideally stable with variations in the line or input voltage and output load current, immune to changes in the ambient temperature, and stable over time. LDOs should continue regulating with as low a difference between the input and output voltage as possible, called the dropout voltage. For example, in a battery-powered design using a lithium-ion cell connected to a 2.8 V LDO, the battery voltage can drop from 4.2 V (fully charged) to 3.0 V (battery empty) and provide a constant 2.8 V output provided the LDO's dropout voltage is less than 200 mV. In some systems LDOs are used for what is sometimes called post-regulation. The LDO is connected to the output of a primary high-efficiency switching regulator. The secondary LDO provides noise filtering from the switching regulator, as well as a stable output voltage.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ldo-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 output voltage vs input voltage


Characterize Integrated Circuit LDO
-----------------------------------

The first part of this Lab activity will be to characterize the :adi:`ADP3300 <media/en/technical-documentation/data-sheets/ADP3300.pdf>` 3.3 volt LDO IC included in the ADALP2000 parts kit. You will measure the dropout voltage as well as the line and load regulation.

On your solder-less breadboard, based on the Typical Application Circuit, figure 1 of the :adi:`ADP3300 datasheet <media/en/technical-documentation/data-sheets/ADP3300.pdf>`, build the test circuit shown in figure 3.

Resistor R1 provides a pull up for the open collector ERR/bar output. Resistor R2 (2.2K) provides a minimum load current on the output. Capacitor C1 is the recommended 0.47uF output capacitor from the datasheet. Resistor RL is used along with the channel B voltage source to provide a variable load on the LDO output (max possible current could be up to 3.3V/10ohms or 330 mA when CB set to 0 V).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ldo-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, characterization schematic


Using the Channel A voltage output as the Vin supply and using Channel B either in Hi-Z mode to measure the voltage at Vout or in source voltage (measure current) as a variable load try to recreate as many of the Typical Performance Characteristic curves, in the datasheet starting on page 4, as you can. Curves vs. Temperature are probably not possible to create so they can be skipped. Include the curves you generate in your lab report and comment on any differences you see compared to the datasheet.

**Test technique Hints:**

When doing load regulation tests connect Vin to fixed +5 V supply and use channel A in Hi-Z mode to measure the voltage seen at Vout on pin 4 while sweeping the voltage on channel B.

When testing the turn on /off transient response use the Trapezoid or SSQ waveform shapes and adjust the rise/fall times as needed.

To measure the Quiescent Current in ground, connect Vin to fixed +5 V supply and use channel A to measure voltage drop across small value resistor placed in series with the ground pin. Choose a resistor value large enough to measure the expected current but small enough not to affect the output voltage in a significant way.

To test the ERR/bar output use channel B to monitor the voltage on the pin while sweeping Vin using the channel A voltage source.

To test operation of the SD/bar input, disconnect it from Vin and use channel A as a square wave input while Vin is connected to the fixed +5 V supply.

Extra Bonus Activity
--------------------

Add an external PNP pass transistor to build the High Output Current Linear Regulator shown on page 7, figure 5 of the ADP3300 datasheet. Use a 2N3906 PNP transistor. Choose a value for R1 such that the PNP turns on when 50 mA flows into the Vin pin (5) of the ADP3300.

Perform as many of the same characterization tests as you can on the high output current circuit and compare the new results to the simple version in figure 3.

LTC1541 based LDO
-----------------

The LTC1541 micropower op amp comparator and reference, from the ADALP2000 part kit, contains two of the main building blocks of an LDO. Along with an external pass transistor (PNP or PMOS) the op amp and 1.2 volt reference blocks can be configured as shown in figure 3A to make an LDO according to the block diagram from figure 1b. In this characterization example a 2N3906 PNP pass transistor is chosen. Feedback resistors R1 and R2 are set equal which results in an output voltage equal to twice the 1.2 V Vref output. Different output voltages can be generated using different resistor ratios. Even output voltages less than 1.2 V can be generated by adding a voltage divider at the Vref output, however the Vin supply voltage will still need to be generally greater than 1.2V plus the V\ :sub:`BE` of Q1.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ldo-fig3a.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3A, LTC1541 LDO characterization schematic


Characterize this circuit using the same steps and test techniques you used with the ADP3300 circuit in figure 3. Be sure to experiment with different output decoupling capacitors to test the stability of the circuit.

Design LDO circuit using transistors
------------------------------------

The next step in this lab activity is to explore a transistor level design of the LDO linear voltage regulator. Enter the LTSpice simulation schematic as shown in figure 4. The simulation model for the TIP32 transistor can be downloaded from `here <https://wiki.analog.com/_media/university/courses/alm1k/tip32a.lib.zip>`_:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ldo-fig4.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 4 LTSpice Simulation schematic


Change the settings for the input source V1 and the output load source V3 to simulate as many of the characterization tests as you can. Record your results for comparison later to the as constructed hardware results.

Materials:
~~~~~~~~~~

| ADALM1000 Lab hardware module
| Solder-less breadboard, and jumper wire kit
| 1 – 47 Ω resistor
| 1 – 4.7 KΩ resistor
| 3 – 10 KΩ resistors
| 1 – 15 KΩ resistor
| 3 – small signal NPN transistors (2N3904)
| 5 – small signal PNP transistors (2N3906)
| 1 – power PNP transistor (TIP32)
| 1 – 100 pF capacitor
| 1 – 470 pF capacitor
| 1 – 1.0 uF capacitor

Directions:
~~~~~~~~~~~

Build the simulation circuit from figure 4 as shown in figure 5 on your solder-less breadboard. Use the power PNP (TIP32) for the output transistor Q9.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ldo-fig5.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 5 Hardware schematic


Hardware Setup:
~~~~~~~~~~~~~~~

Use the same combinations of the AWG output and input channels you did when you characterized the ADP3300. The fixed 2.5V supply is used as the Vref for the circuit. Resistors R5 and R6 can be changed to adjust the output voltage or a potentiometer can be substituted.

Procedure:
~~~~~~~~~~

Again measure as many of the typical LDO regulator characteristic curves as you can.

To measure drop-out voltage and line regulation use AWG channel A as the positive input supply and ramp the voltage from 0 to +5V. Use channel B in Hi-Z mode to measure the output voltage.

To measure load regulation use variable user supply set to +5 V ( or any other voltage higher than the drop out voltage ) and use one of the AWG channels to vary the output current through the RL 10Ω resistor.

Questions:
~~~~~~~~~~

How do the results of your transistor based design compare to the results you measured for the ADP3300 IC voltage regulator?

Bonus Construction Activity
---------------------------

Substitute an enhancement mode PMOS (ZVP2110A) for the output pass transistor (PNP TIP32) Q9 in your circuit. Does the circuit work the same? Has the drop-out voltage increased, decreased or stayed the same compared to the PNP as the pass transistor?

For Further Reading:
~~~~~~~~~~~~~~~~~~~~

| :adi:`References and Low Dropout Linear Regulators <static/imported-files/tutorials/ptmsect2.pdf>`
| :adi:`The Fundamentals of LDO Design and Application <static/imported-files/pwr_mgmt/PM_ldo_design_08451b.pdf>`
| :adi:`Understand Low-Dropout Regulator (LDO) Concepts to Achieve Optimal Designs <en/analog-dialogue/articles/understand-ldo-concepts.html>`
| :adi:`Basic Concepts of Linear Regulator and Switching Mode Power Supplies <media/en/technical-documentation/application-notes/AN140.pdf>`
| `Low Dropout Regulators <https://en.wikipedia.org/wiki/Low-dropout_regulator>`_
| `Linear Regulators <https://en.wikipedia.org/wiki/Linear_regulator>`_
| `Low Dropout Linear Regulator Frequently asked Questions <http://electronicdesign.com/power/low-dropout-ldo-linear-regulators>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
