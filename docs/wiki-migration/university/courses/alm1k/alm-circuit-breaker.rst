Activity: Electronic Circuit Breaker - ADALM1000
================================================

Objective:
----------

The electronic circuit breaker uses a MOSFET switch to interrupt power to a sensitive electronic load in the event of an over-current condition. Electronic solid-state circuit breakers improve upon the traditional electromechanical circuit breakers by offering faster switching times. In the circuit examples examined in this Lab activity the voltage across the drain and source On resistance of the MOSFET switch device is sensed rather than a separate current shunt resistor. The advantages of this arrangement are a lower cost and reduced voltage and power loss in the switch path.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

Historically few alternatives to electromechanical and magnetic circuit breakers have been available. Designers were forced to live with such undesirable characteristics as arcing and switch bounce (with corresponding noise and wear), while accommodating large unwieldy packages in their power control and protection systems.

Applying solid state technology to this traditional device results in circuit breakers free from arcing and switch bounce. Solid state circuits offer correspondingly higher reliability and longer lifetimes as well as potentially faster switching times. A typical solid state circuit breaker will switch in a matter of microseconds, as opposed to milliseconds or even seconds for a mechanical version.

The electronic circuit breaker combines several analog building blocks: a current-sense or shunt resistor, a differential amplifier with accurate scaling resistors for measuring and scaling the voltage across this resistor; a comparator circuit to trigger a latch at a preset current value, and a FET switch in series with the current path in the power supply line being monitored, figure 1. There is usually a Reset Input of some sort to reset the circuit breaker. Some designs automatically reset when over current fault is removed.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Electronic circuit breaker block diagram


The current to be monitored passes through the sensor resistor, and the voltage across this resistor is sensed and scaled by the difference amplifier. Since the resistor value is known, it's easy to set a threshold or trip current level using basic Ohm's Law: I = V/R. If the threshold is exceeded, the comparator output which drives the MOSFET gate turns the device off, so that the current is interrupted. Response time can be on the order of microseconds, far faster than a traditional thermal fuse with a typical response time of tens and hundreds of milliseconds.

A Simple Example to start:
--------------------------

A very simple example circuit, LTspice simulation shown in figure 2, uses the R\ :sub:`DS` on-resistance of the PMOS FET M1 as the current sensor. Normally the gate of M1 is pulled to ground by resistor R3 turning it on. When the voltage drop across R\ :sub:`DS` is greater than the V\ :sub:`BE` required for PNP transistor Q1 to turn on, the voltage at the collector of Q1 pulls the gate of MOS switch M1 high enough to turn it off. Now the R\ :sub:`DS` of M1 is very large. The load will pull the end of base resistor R2 even lower turning Q1 on even harder. This acts effectively as a latch keeping M1 off.

The circuit is reset by removing the input power supply or the load. The circuit draws essentially no current until it is tripped.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Simple example simulation schematic


Before starting the Lab look up the R\ :sub:`DS(on)` - Drain Source On Resistance for VGS of -5V from the chart in the ZVP2110A datasheet (see Appendix below). Based on the R\ :sub:`DS` value, calculate an estimate of the trigger current.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Jumper wire set
| 1 - ZVP2110A enhancement mode PMOS
| 1 - 2N3906 PNP transistor
| 1 – 47 Ω resistor
| 1 - 1 KΩ resistor
| 1 - 10 KΩ resistor

Directions:
~~~~~~~~~~~

On your solder-less bread board construct the circuit as shown in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Electronic Circuit Breaker


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-4.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 4, ZVP2110A pinout


Hardware Setup:
~~~~~~~~~~~~~~~

Set AWG Channel A to SVMI mode. Set the Shape to Ramp. Set Min value to 5, set Max value to 1.5. Set Freq to 40 Hz, set Slope time to 20 mS and the Duty cycle to 90%. Set Channel B to Hi-Z, Split I/O mode.

Select CA-V, CA-I and CB-V traces. With the Horizontal scale set to 5 mS/Div you should be displaying 2 cycles of the AWG waveform. Adjust the vertical scales as needed.

Procedure:
~~~~~~~~~~

When the channel A voltage is equal to 5 V no current flows in the load resistor. As the channel A voltage ramps down the load current increases until the current trip level is reached. Q1 turns on and drives Vgate high (to 5 V) turning off MOS switch M1.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Example traces


The trigger point can be adjusted (reduced) by pre-biasing the base of Q1 slightly below the supply voltage. This can be done by adding an adjustable resistance between the base and ground as shown in figure 6. Add a 10 KΩ resistor R3 and 10 KΩ pot R4 as shown. Monitor the trip current level as you adjust the pot.

Connect a second ZVP2110A transistor in parallel with M1. Be careful to connect S to S, G to G and D to D. The current level where the circuit trips should now be approximately doubled. Why? Depending on the On resistance of your FETs you may need to reduce the value of R\ :sub:`LOAD` slightly to reach the trigger current point.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Adjusting current trigger point


The simple PNP based current sensor trips when a voltage greater than V\ :sub:`BE` is dropped across M1. This will be about 600 mV at room temperature and will change over temperature. The temperature coefficient of the V\ :sub:`BE` of a silicon BJT transistor is about -2 mV/°C. The trip current will not be very predictable, stable or accurate. To improve on this design we and add a more complex and accurate sense amplifier and comparator as shown in the LTspice simulation schematic in figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Simulation schematic


The first half of the AD8542 dual op-amp, U1A, along with resistors R4,5,6,7 form a difference amplifier with a gain of 470/20 or 23.5. The amplified voltage difference across the PMOS FET is then compared to the voltage from the resistor divider R2/R3 by the second half of the AD8542, U1B. When the output of U1A is greater than the level set by the voltage divider the output of U1B, Vgate, goes to the supply voltage turning off the switch.

Add the difference amplifier and comparator to you breadboard circuit as shown in figure 8. Use a 10 KΩ pot as the voltage divider.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, Breadboard schematic


Using NMOS as the Switch:
-------------------------

The example circuits so far have used PMOS devices for the switch. NMOS power devices are more common and generally have lower R\ :sub:`DS` ON resistance compared to similar PMOS power transistors. Figure 9 shows the LTspice simulation schematic for the simple circuit breaker using and NMOS switch. The gate of the NMOS device requires a positive voltage with respect to the source to turn on. This means that for cases with positive supply voltages the switch must be placed in the ground leg of the circuit. Current in NMOS devices generally flows from drain to source so in this case the source terminal is connected to ground such that the load current flowing out the negative side of the load flows into the drain terminal.

As with the PMOS version the base of the NPN transistor Q1 is slightly pre-biased by the adjustable R4,5 combination.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, NMOS simulation schematic


.. _directions-1:

Directions:
~~~~~~~~~~~

Using a ZVN2110A and 2N3904 from the ALP2000 part kit, construct the circuit in figure 9 on your solderless bread board. The direction of the current from the active load channel B is different compared to the PMOS circuits.

.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

For the CHA AWG, set Min value to 0, set Max value to 4 such that the load current starts at zero and ramps up.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Requiring that the NMOS switch be in the ground leg is very inconvenient, but needing to drive the gate more positive than the supply voltage is also an added problem. Figure 10 is an LTspice simulation schematic of a version with the switch again in the supply leg of the circuit. Note that an extra power supply voltage, Vboost, that is more positive than the input supply is needed to drive the gate positive enough with respect to the input supply voltage to turn on the NMOS transistor.

Be careful to also note that the source and drain orientation of the switch device is now reversed compared to the version when the switch is in the ground leg. Current generally flows from drain to source in NMOS devices.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10, Boosted NMOS switch


.. _directions-2:

Directions:
~~~~~~~~~~~

To generate a higher voltage for the gate we can use a diode voltage "booster". Diodes D\ :sub:`1` and D\ :sub:`2` along with capacitors C\ :sub:`1` and C\ :sub:`2` form a voltage booster with respect to the +5 V supply. A square wave from AWG channel B drives the bottom of capacitor C\ :sub:`1`. The boosted voltage will be equal to +5 V plus the peak-to-peak voltage of the square wave minus the diode drops of D\ :sub:`1` and D\ :sub:`2`. The current needed to drive the gate is very small so there should be minimal loss across the diodes.

Build the circuit shown in figure 11 on your solderless breadboard. Because the boosted voltage is higher than +5 V and will be above the maximum allowed input voltage of the ALM1000 a 1 megaOhm resistor, R4 is included in series with the AIN input pin. This external resistor along with the internal 1 megaOhm resistor provides a divide by 2 attenuation of the Vboost voltage. To correct for the voltage division, set the channel A V gain to 2 (rather than 1). The channel A voltage trace will now read the correct measured voltage level.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, Breadboard schematic


As with the PMOS design in figures 7 and 8 we can add the difference amplifier for sensing the current and the comparator stages for better accuracy and control of the trigger current level. Note the simulation and breadboard schematic in figures 12 and 13.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-12.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 12, Simulation schematic.


Note the use of an additional NMOS transistor, M2, that level shifts and inverts the output signal of the comparator before driving the gate of the switch.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-13.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 13, Breadboard schematic.


Conclusions:
~~~~~~~~~~~~

In this activity we covered the circuits necessary to implement an electronic circuit breaker. This function is often integrated with other power management functions such as soft start, power on reset, voltage and current read back monitoring, current limit and over/under voltage protection.

Appendix:
~~~~~~~~~

PMOS and NMOS On resistance curves.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-a1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure A1, ZVP2110A On-resistance vs drain current


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuit-breaker-fig-a1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure A2, ZVN2110A On-resistance Gate-Source voltage


\**For Further Reading: \*\*

| No R\ :sub:`SENSE`\ ™ :adi:`Electronic Circuit Breaker <media/en/technical-documentation/data-sheets/4213f.pdf>`
| :adi:`Electronic Circuit Breaker in Small DFN Package Eliminates Sense Resistor <media/en/reference-design-documentation/design-notes/dn402.pdf>`
| :adi:`LT1153 Auto-Reset Electronic Circuit Breaker <media/en/technical-documentation/data-sheets/lt1153.pdf>`
| :adi:`ADM1177 digital power monitor <media/en/technical-documentation/data-sheets/ADM1177.pdf>`

**Return to Lab Activity Table of Contents**
