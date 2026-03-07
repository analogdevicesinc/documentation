Theory Of Operation
===================

Input caps – bulk
-----------------

The two large, polarized capacitors placed close to the *<fc #008080>VDD</fc>* terminal act up as a close-by charge reservoir when a voltage source with long cables is being utilized. For most applications, these large caps would not be necessary.


|Input bulk capacitors|

The amount of capacitance needed is function of numerous factors:

-  *<fc #008080>VDD</fc>* power line noise,
-  Min/max allowable *<fc #008080>VDD</fc>* voltage deviation,
-  Power supply response time,
-  Etc.

In other words, the capacitors network is optimized when designing the *<fc #008080>VDD</fc>* power supply. Tools such as :adi:`LTpowerCAD <en/design-center/ltpowercad.html>` and :adi:`LTspice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>` can help with the supply optimization.

|

.. important::

   <fc #ff0000>\ **DO NOT HOT PLUG THE <fc #008080>VDD</fc> POWER SOURCE !** </fc>

   | To power-up the circuit safely via the *<fc #008080>VDD</fc>* power socket, it is strongly recommended to follow the steps below.


The bulk capacitors can remain charged for a significant amount of time after power down. <fc #ff0000>To avoid injuries and/or damage to the board , it is important to</fc>:

-  Leave the <fc #008080>VDD</fc> terminal of the `ADPULSERPLUS evaluation board <https://wiki.analog.com/\>`_ floating
-  Ensure external power source is set to 0V.
-  Make sure the input caps are fully discharged by measuring the *<fc #008080>VDD</fc>* voltage. It should read close to 0V. If charged still, you may connect a power resistor, 500Ω-1kΩ, between *<fc #008080>VDD</fc>* and GND to provide a quicker discharge.
-  Connect *<fc #008080>VDD</fc>* source to the *<fc #008080>VDD</fc>* connector.
-  Gradually increase *<fc #008080>VDD</fc>* voltage to desired value.
-  Note for power-down: It is preferable to ramp-down the *<fc #008080>VDD</fc>* power supply to 0V before turning off or disconnecting it. It will help discharge the bulk capacitors.

Drain Pulse Generator
---------------------

.. image:: https://wiki.analog.com/_media/\drain_pulser_circuit.png
   :alt: Drain pulser circuit
   :align: left
   :width: 1200px

The drain pulse generator comprises of the :adi:`LTC7000A`, a FET and the crowbar circuit (:adi:`ADP3625` + FET). To pulse the drain, apply a 0-3.3V pulse onto the *<fc #008080>DRAIN_PULSE_ENABLE</fc>* SMA connector. The pulse modulates the INP pin of the :adi:`LTC7000A` which, in turn, drives Q1 on and off. A high on *<fc #008080>DRAIN_PULSE_ENABLE</fc>* turns on the FET and applies *<fc #008080>VDD</fc>* onto the PA drain.

The turn-on time is controlled by the :adi:`LTC7000A`.TGUP signal and the amount of capacitance connected to the PA drain (*<fc #008080>VDD_PA</fc>* signal). Too much capacitance on the PA drain rail can not only slow down the turn-on edges but also create large input current spikes on the line. To avoid such issues, it is recommended to keep the total amount of capacitance at the PA drain to less than 10nF.

The :adi:`LTC7000A`.TGDN pin controls the time it takes to turn off Q1. As for the time it takes to transition the PA drain from on to off, it is dependent on the amplifier itself unless the “crowbar circuit” is used. If not used, the “turn-off time” is function of the power amplifier itself. The amplifier acts as a resistive load. As soon as Q1 is off, the PA starts draining the capacitors on the rail. How fast is function of the drain voltage, PA IDD, PA off threshold and a few other parameters. It is preferable to test this behavior with the right PA. For a more predictable turn-off time, it is recommended to use the “crowbar circuit”. As the name implies, the “crowbar circuit” forces a fast discharge of the PA drain voltage by connecting it to ground via a low-resistance switch. Turn off times <1μs can be achieved with the crowbar circuit.

The selection of Q1 and Q2 could be optimized for a certain application type. Various characteristics would need to be consider such as drain voltage/current, max gate voltage, Vgs(th), etc.

The R3 placeholder can be used for evaluation of the drain pulser circuit without connecting a power amplifier. The DC power that can be dissipated from R3 is limited. It is important to operate the circuit in pulsed mode only. It is also recommended to use a pulse proof power resistor.

VDD_PA voltage sense
~~~~~~~~~~~~~~~~~~~~

The PA drain voltage can be monitored via the *<fc #008080>VDD_PA_SENSE</fc>* SMA connector (refer to `"Drain pulser circuit" <\drain_pulser_circuit.png>`_ ). To measure, the test equipment connected can be terminated to either 50Ω or high-Z with limitations for each.

-  50Ω terminated: <fc #ff0000>50Ω termination must not be used when the drain pulser is set to stay on for relatively long periods of time</fc> (ex. Gate pulsing). It will damage resistor R28 and the PCB. To use when drain pulsing with pulse width <300μs per recommended operating conditions.
   The conversion factor when 50Ω terminated is:

.. container:: centeralign

   V\ :sub:`<fc #008080>VDD_PA_SNS</fc>` = V\ :sub:`<fc #008080>VDD_PA</fc>` × R\ :sub:`TERMINATION` / (R\ :sub:`TERMINATION` + R28)

   
   V\ :sub:`<fc #008080>VDD_PA_SNS</fc>` = V\ :sub:`<fc #008080>VDD_PA</fc>` × 47.6mV/V


-  High-Z termination: Careful with added capacitance that form an R-C filter with R28. It may affect measurement accuracy.

PA Drain Current Sense
----------------------

.. image:: https://wiki.analog.com/_media/\power_amplifier_drain_current_sense_circuits.png
   :alt: Power amplifier drain current sense circuits
   :align: center
   :width: 1000px

There are two means of measuring the PA drain current on this evaluation board.

-  Via the :adi:`LTC7000A`.IMON pin. It has the advantage of not requiring any additional circuitry for monitoring the current. However, its response time can be significantly slower and is limited to pulses with on-times greater than 20-30μs. The :adi:`LTC7000A`.IMON response can be faster than the 20-30us depending on the operating conditions.
   The :adi:`LTC7000A`.IMON voltage can be measured differentially across the *<fc #008080>IMONP</fc>* and *<fc #008080>IMONN</fc>* terminals with a high-impedance probe. To estimate the drain current from *<fc #008080>IMONP/N</fc>* terminals:

.. container:: centeralign

   V\ :sub:`<fc #008080>IMONP</fc>` − V\ :sub:`<fc #008080>IMONN</fc>` = (I\ :sub:`DRAIN` × 10mΩ × 200μA/V) × (100kΩ ⁄⁄ R56)

   I\ :sub:`DRAIN` = (V\ :sub:`<fc #008080>IMONP</fc>` − V\ :sub:`<fc #008080>IMONN</fc>`) × 33A/V


Removing the 20kΩ resistor connected to :adi:`LTC7000A`.IMON pin, R56, allows a larger signal to be measured across *<fc #008080>IMONP/N</fc>* at the expense of a slower response. The :adi:`LTC7000A`.IMON pin has 100kΩ of ROUT.
-  Using the :adi:`LT1999-10 <LT1999>` current sense amplifier. It provides significantly faster response (<1μs) than the :adi:`LTC7000A`.IMON circuit but requires an additional IC. It can measure drain currents pulses down to the recommended 10μs on-time minimum.
   The measurement is done differentially across the *<fc #008080>ISNSP</fc>* and *<fc #008080>ISNSN</fc>* terminals using a high-impedance probe. Don’t try using a single-ended probe with ground terminal attached to *<fc #008080>ISNSN</fc>*, *<fc #008080>ISNSN</fc>* is NOT grounded. To convert:

.. container:: centeralign

   V\ :sub:`<fc #008080>ISNSP</fc>` − V\ :sub:`<fc #008080>ISNSN</fc>` = I\ :sub:`DRAIN` × 10mΩ × 10V/V

   I\ :sub:`DRAIN` = (V\ :sub:`<fc #008080>ISNSP</fc>` − V\ :sub:`<fc #008080>ISNSN</fc>`) × 10A/V


For more signal at the *<fc #008080>ISNSP/N</fc>* terminals, the gain of the LT1999 can be increased by selecting either the :adi:`LT1999-20 <LT1999>`, gain of 20, or :adi:`LT1999-50 <LT1999>`), gain of 50. The gain increase comes at the expense of a slower response time.

To improve measurement accuracy, it is preferable to calibrate the current monitoring path. One approach would be to connect an electronic load on *<fc #008080>VDD_PA</fc>* and setting the *<fc #008080>DRAIN_PULSE_ENABLE</fc>* voltage to 3.3V to turn-on the <fc #008080>\ *VDD*\ </fc> drain path.

The gain of both current sense paths gain be increased by substituting R9 for a higher value. R9 also controls the current limit of the circuit via the ECB function of the :adi:`LTC7000A`. Hence, it is appropriate to design the ECB first, then the current sense monitor circuit(s).

It is worth noting, neither current sense methods can accurately detect drain current during ON → OFF and OFF → ON transitions when drain pulsing. The current required to transition the *<fc #008080>VDD</fc>* power path FET, Q1, is summed to the PA drain current. Only when the FET is fully on or off will the results be precise.

Electronic Circuit Breaker
--------------------------

|Electronic circuit breaker| The :adi:`LTC7000A`, in combination with R9 and Q1, has the capability to turn off the *<fc #008080>VDD</fc>* power path if the current exceeds 6A typical for about 10-15μs. The circuit will automatically retry to start after a brief cooling period. The resistor off the :adi:`LTC7000A`.ISET pin can be substituted to modify the overcurrent protection threshold. Refer to the :adi:`LTC7000A` datasheet for details. The purpose of diode D1 is to clamp inductive kickbacks that may be seen when the ECB turns off Q1.

PA Gate Pulse Generator
-----------------------

The PA gate pulser consists of a negative supply, a level on/off gate level adjustment circuit and a driving amplifier.


|Gate pulse generator diagram|

Negative converter
~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/\negative_power_conversion_circuit.png
   :alt: Negative power conversion circuit
   :align: center
   :width: 1000px

There are three key stages to the negative converter:

-  The :adi:`LT8618` step-down converter is setup as a buck-boost inverter to generate a negative power rail from the main input power feed, *<fc #008080>VDD</fc>*.
-  The bead+ cap filter. This filter has two purposes:

   -  It helps attenuate the higher frequencies, outside of the rejection capability of the downstream linear regulator.
   -  The bead being highly inductive at frequencies below 10MHz, the bead-cap network acts up like a damp LC filter at lower frequencies. So, the bead-cap filter increases the power supply noise rejection capability at frequencies around Fsw.

.. container:: OUTDENT

   
   .. container:: OUTDENT

         
         .. container:: OUTDENT

            The series resistance, R32, is present to damp the quality factor of the bead+cap filter

         

   


-  The linear regulator, :adi:`LT3093`, provides excellent supply noise rejection while keeping the noise it generates to a minimum (<1μVrms). Due to the wide range of use cases, it is important to keep noise on the power rail as small as it could.

| 
| Noise creation and rejection was a key aspect of the component selection. Similarly, various bypass options were included to allow users to better optimize the DC-DC conversion circuit for their use case. As example:

-  To bypass the LDO, populate R59 and R60 with jumpers. No need to depopulate :adi:`LT3093`. Although preferred, disabling the LDO by tying the :adi:`LT3093`.EN/UV pin to ground is optional.

Gate pulse generation
~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/\gate_pulse_generation_circuit.png
   :alt: Gate pulse generation circuit
   :align: center
   :width: 1000px

| 
| The dual opamps along with the SPST analog switch, :adi:`ADG1401`, form the gate pulse circuit. A logic low at the <fc #008080>\ *GATE_PULSE_ENABLE*\ </fc> SMA connector forces a voltage equivalent to the desired pinch-off gate voltage at the PA gate signal. A logic 1, 3.3V, sets the PA gate voltage to the desired bias-voltage. And a pulse train on the *<fc #008080>GATE_PULSE_ENABLE</fc>* SMA connector would generate pulses at the PA VGG signal between PA on (V\ :sub:`BIAS`) and PA off (V\ :sub:`PINCH_OFF`) PA gate voltage thresholds.

Amplifier A1a, :adi:`ADA4896-2`, is used as a buffer/level-shifter amplifier for the pinch-off threshold reference voltage. To set the pinch-off voltage, adjust R42 and R43 per equation:

.. container:: centeralign

   V\ :sub:`PINCH_OFF` = V\ :sub:`<fc #008080>LT3093_VEE</fc>` \* R42 / (R42 + R43)


The eval is set to -5.0V V\ :sub:`PINCH_OFF`.

The on threshold, V\ :sub:`BIAS`, is controlled via the resistor divider network R45, R47 and potentiometer R46. It can be estimated using the following equation:

.. container:: centeralign

   V\ :sub:`BIAS` = V\ :sub:`PINCH_OFF` × (R46 ⁄⁄ R47) / (R45 + R46 ⁄⁄ R47)


R46 is a 2k potentiometer. With the -5.0V default pinch-off voltage, the bias voltage can be adjusted over the range [-3.33V, -0.9V]. The upper limit is defined by the input common-mode voltage range of the buffer amplifier.

The :adi:`ADG1401` state is controlled via the *<fc #008080>GATE_PULSE_ENABLE</fc>* SMA connector. A logic 1 connects the resistor divider to ground, generating V\ :sub:`BIAS` which then is applied to the input of the gate driver amplifier. A logic 0 floats the resistor divider, connecting the output of amplifier A1a to the input of the gate driver and generating V\ :sub:`PINCH_OFF`.

Amplifier A1b, :adi:`ADA4896-2`, acts up as a buffer/driver between the capacitance that’s located on the PA VGG (*<fc #008080>VGG1</fc>*) signal and the pulsed resistor network. The 50Ω output resistance is to help stabilize the buffer amplifier when capacitively loaded.

Gate pulse generation circuit when drain pulsing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When drain pulsing, the gate remains at V\ :sub:`BIAS`. A constant 3.3V can be applied to the *<fc #008080>GATE_PULSE_ENABLE</fc>* connector. Another method would be to drive the gate signal directly from the :adi:`LT3093` output. To do so:

-  R61 must be populated with a short circuit,
-  R54 uninstalled,
-  *<fc #008080>LT3093_VEE</fc>* power rail (:adi:`LT3093` LDO output) adjusted to meet the desired V\ :sub:`BIAS` voltage. Refer to the :adi:`LT3093` datasheet on how to set the output voltage.

Sequencing
----------

The actual sequencing of the power rails at the PA, drain and gate, are mainly controlled via state of the pulse SMA connectors, *<fc #008080>GATE_PULSE_ENABLE</fc>* and *<fc #008080>DRAIN_PULSE_ENABLE</fc>*. Despite that fact, the circuit is designed to follow a certain sequence if the two SMA connectors are left floating and power applied on *<fc #008080>VDD</fc>* . The sequence is as follow:

-  *<fc #008080>VDD</fc>* ramps up.
-  At *<fc #008080>VDD</fc>* ≈ 2.9V, the negative converter turns on.
-  *<fc #008080>GATE_PULSE_ENABLE</fc>* defaults to a logic 0 when floating. That sets the gate voltage to V\ :sub:`PINCH_OFF`.
-  At *<fc #008080>VDD</fc>* ≈ 20V, the :adi:`LTC7000A` turns the power FET, Q1, fully on, connecting *<fc #008080>VDD</fc>* to the PA drain.

The board was setup to facilitate gate pulsing usage by enabling the *<fc #008080>VDD</fc>*/drain power path by default. If the preferred method is to keep the PA drain path off on start-up, either set *<fc #008080>DRAIN_PULSE_ENABLE</fc>* to a logic 0 or, for a more permanent change, depopulate the pull-up resistor R12 and populate the termination resistor R13 off the INP pin.


|LTC7000A automatic turn-on circuit|

.. |Input bulk capacitors| image:: https://wiki.analog.com/_media/\input_bulk_capacitors.png
   :width: 400px
.. |Electronic circuit breaker| image:: https://wiki.analog.com/_media/\electronic_circuit_breaker.png
   :width: 1000px
.. |Gate pulse generator diagram| image:: https://wiki.analog.com/_media/\gate_pulse_generator_diagram.png
   :width: 1000px
.. |LTC7000A automatic turn-on circuit| image:: https://wiki.analog.com/_media/\ltc7000a_automatic_turn-on_circuit.png
   :width: 1000px
