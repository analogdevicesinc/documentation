3-Wire RTD Measurements with AD74115H
=====================================

Introduction
------------

| The AD74115H is a single-channel software configurable input/output device for industrial control applications. AD74115H provides analog output, analog input, digital output, digital input, 2-, 3- and 4– wire resistance temperature detector (Resistance Temperature Detectors) and thermocouple measurements integrated into a single chip solution with a serial peripheral interface (SPI).

RTDs
----

| An RTD (Resistance Temperature Detector) is a sensor used to measure temperature. RTDs have a repeatable resistance vs temperature relationship which can be used to accurately determine the temperature. RTDs are used in a wide variety of applications and are particularly suitable for industrial applications due to their with wide operating temperature ranges and reliability.
| To measure temperature with an RTD, a small excitation current is passed through it and the corresponding voltage drop is measured. The corresponding resistance is calculated and used to determine the ambient temperature of the sensor.
| ===RTD Types=== 2-wire RTDs are typically used for low accuracy applications and when the distance to the sensor is short (lead lengths are short). Longer leads result in larger lead resistances, which add error to the overall resistance measurement. If long lead lengths are in use or higher accuracy is required, 3-wire RTDs are used. In this case, it is assumed that each of the leads are of similar length and resistance. A 3-wire RTD measurement allows for an estimate of this lead resistance to be made and this in turn is factored out of the overall resistance measurement. Finally, 4-wire RTDs provide the best accuracy - 2 wires are used to source the excitation current through the sensor while the remaining 2 wires are used to directly sense the voltage drop across the RTD sensor. AD74115H can also support 3 and 4 wire RTD measurements.

| 

3 Wire RTD Implementation
-------------------------

| 
| The AD74115H does not require additional external components such as switches to operate in 3 wire RTD mode. Matched excitation currents, I1 and I2 are sourced to two of the RTD leads. The third lead is connected to ground. One of the excitation currents, I1 generates a voltage across the RTD and lead resistance RL1. The second excitation current, I2 generates a drop across RL2. The resultant voltage across terminals T1 and T2 is equivalent to the voltage drop across the RTD (It is assumed that the lead resistances are matched i.e. RL1 = RL2 = RL3). The voltage between terminal T1 and terminal T2 is measured by the ADC using the SENSELF and SENSE_EXT1 pins. The full-scale range of the ADC is determined by the voltage across the reference resistor, RREF, guaranteeing a fully ratio metric measurement.

| |ad74115h_usecase_3wirertd.png|
| Figure 1: Diagram of AD74115H in 3 wire RTD mode

Connections & Register Writes
-----------------------------

| 
| Connect the positive lead to T1 terminal. Connect any negative leads to T2 and to T3 terminals. This is demonstrated in figure 2 below.

| |rtd_lead_setup.png|
| Figure 2: RTD lead setup

| 

| The following is an example set of register writes needed to make 3-wire RTD measurements on a channel. The RTD used in this example is a Pt1000. The excitation current and voltage measurement range are set accordingly. The writes assume that the device is in a high impedance state, after power-up or reset.

-  Configure Channel in Resistance Measurement mode via the CH_FUNC_SETUP0 register. (Address: 0x01, Data: 0x0007) Then set RTD3W4W_CONFIG register to measure resistance with 3 wire RTD. (Address: 0x07, Data: 0x0013)

   -  The last two bits of RTD3W4W_CONFIG register configures RTD_CURRENT to source 1mA

-  Write to the ADC_CONV_CTRL register to enable continuous ADC conversions. (Address: 0x3b, Data: 0x2201)
-  Disable the continuous ADC conversion in the ADC_CONV_CTRL register. (Address: 0x3b, Data: 0x3201)
-  Read ADC_RESULT register. (Address: 0x44)
-  Convert ADC_RESULT code from hex to decimal.
-  Place the ADC code into the equation to calculate 3 wire RTD resistance.

| 
| Use equation below to calculate resistance of the 3 wire RTD.

R\ :sub:`RTD`\ =(((ADC_CODE)/65536)*R_REF)/(ADC_GAIN)

Rref is 2.1k ohms. ADC_GAIN is depended on the ADC range that is chosen by the user. Recommended ADC range is 0v to 12v which constitutes a gain of 1/4.8. If a multimeter is present, measure the voltage drop across T1 and T2 terminals (across positive lead and negative lead). Divide that voltage by excitation current to calculate the RTD resistance.

| R\ :sub:`RTD`\ =V\ :sub:`MEAS`/I\ :sub:`EXCITE`

Open Wire Detect
----------------

An open circuit detect feature is available on the leads of the 3-wire RTD. The combination of excitation current & RTD and lead resistances will generate voltages on the SENSEH and SENSE_EXT1 pins. If the voltage on either of these pins exceeds the short circuit detect voltage, an open circuit signal is asserted in the ALERT_STATUS register. This will happen if any one of the leads are disconnected from the terminals.

:doc:`Back to AD74115H Table of Contents </wiki-migration/resources/eval/user-guides/ad7411x_user_guide>`

.. |ad74115h_usecase_3wirertd.png| image:: https://wiki.analog.com/_media/ad74115h_usecase_3wirertd.png
.. |rtd_lead_setup.png| image:: https://wiki.analog.com/_media/rtd_lead_setup.png
   :width: 500px
   :height: 294px
