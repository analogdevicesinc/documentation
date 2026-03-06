3-Wire RTD Measurements with AD74115H
=====================================

Introduction
------------

| The AD74115H, software configure I/O IC is designed to interface with industrial, process & building control sensors and actuators. The IC comes with a range of programmable I/O capabilities, including analog output, analog input, digital input and temperature measurement. Temperature measurement is crucial in many industrial environments, with thermocouples and RTDs (Resistance Temperature Detectors) being the most commonly used temperature sensor types. The AD74115R has in-built thermocouple and 2-wire RTD measurement capability. 3-wire RTD measurements are not directly supported on chip but this Wiki page will show how to use the AD4115H to make 3-wire RTD measurements, while maintaining all of the existing functionality of the IC.

RTDs
----

| An RTD (Resistance Temperature Detector) is a sensor used to measure temperature. RTDs have a repeatable resistance vs temperature relationship which can be used to accurately determine the temperature. RTDs are used in a wide variety of applications and are particularly suitable for industrial applications due to their with wide operating temperature ranges and reliability.
| To measure temperature with an RTD, a small excitation current is passed through it and the corresponding voltage drop is measured. The corresponding resistance is calculated and used to determine the ambient temperature of the sensor.
| ===RTD Types=== 2-wire RTDs are typically used for low accuracy applications and when the distance to the sensor is short (lead lengths are short). Longer leads result in larger lead resistances, which add error to the overall resistance measurement. If long lead lengths are in use or higher accuracy is required, 3-wire RTDs are used. In this case, it is assumed that each of the leads are of similar length and resistance. A 3-wire RTD measurement allows for an estimate of this lead resistance to be made and this in turn is factored out of the overall resistance measurement. Finally, 4-wire RTDs provide the best accuracy - 2 wires are used to source the excitation current through the sensor while the remaining 2 wires are used to directly sense the voltage drop across the RTD sensor.

| 

Further Notes
-------------

| 
| Refer to figure 1 for a high level block diagram of the standard configuration for the AD74115H. The AD7115H does not require external components such as switches to operate in 3 wire RTD mode. The measurement path is taken between SENSE_EXT1 and SENSELF pins. The current path is on SENSEH pin. Rref of 2.1k ohms generates voltage going into the ADC. These 3 pins allow the user to connect 3 wire RTD with no external components.

| |AD74115H_UseCase_3wireRTD.png|
| Figure 1: Standard configuration to support all Ad74413R I/O functions

| 
| |3w RTD extra components.png|
| Figure 2: Additional components required to support 3-wire RTD measurements

| 
| With the hardware configuration, as shown in figure 2, the AD74115H supports all of the existing I/O functions as well as the 3-wire RTD measurements. All functions can be programmed via the 4-wire SPI.

| 

Implementation
--------------

Connect positive lead to I/OP terminal. Connect any negative lead to I/ON and to EXT1 terminal. Connect SDP-K1 microcontroller to the computer via usb cable. Open AD74115x evaluation software and wait for the microcontroller to connect AD74115H to the computer. When the board is connected, open the evaluation software and select resistance measurement. Select Resistance Measurement 3/4 Wire mode. In the settings, select excitation current of 1mA and ADC range of 0v to 12v. The equation for calculating RTD resistance is given below.

R\ :sub:`RTD`\ =(((ADC_CODE)/65536)*R\ :sub:`REF`)/(ADC_GAIN )

Rref is 2.1k ohms. ADC_GAIN is depended on the ADC range that is chosen by the user. Recommended ADC range is 0v to 12v which constitutes a gain 1/4.8. If a multimeter is present, measure the voltage drop across I/OP and I/ON terminal. Divide that voltage by excitation current to calculate the RTD resistance.

R\ :sub:`RTD`\ =V\ :sub:`MEAS`/I\ :sub:`EXCITE`

| 
| |3w RTD steps.png|
| Figure 3: Steps required to make a 3-wire RTD measurement
| The RTD measurement is done with the following steps:

Step 1 (as shown in Red)
~~~~~~~~~~~~~~~~~~~~~~~~

A current is sourced from the DAC to the RTD. The red path in figure 3 shows the current path from the DAC to the RTD sensor. For best accuracy, this excitation current can be measured with the onboard 16-bit ADC. The switch should connect the SENSEHF pin to the 100Ω R\ :sub:`SENSE` resistor to allow the ADC to measure the drop across the resistor. The excitation current can be calculated using the following equation:

| 
| I\ :sub:`EXCITE` = ((ADC_CODE/65536)*2.5)/100

| 
| RTD calculations should use this measured current value.

Step 2 (as shown in Green)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| When the excitation current is sourced to the RTD, a voltage drop is generated between I/OP and I/ON, V :sub:`(I/OP to I/ON)`. This voltage can be measured as shown by the green path in figure 3. The voltage measured between I/OP and I/ON can be calculated according to the following equation:
| V :sub:`(I/OP to I/ON)` = (ADC_CODE/65536)*RANGE - V\ :sub:`MIN`
| Where
| ADC_CODE is the code read back from the ADC
| RANGE is the full voltage span of the selected ADC range
| V\ :sub:`MIN` is the minimum voltage of the selected ADC range
| V :sub:`(I/OP to I/ON)` and I\ :sub:`EXCITE` are used to determine the combined resistance of the RTD and the two connected lead wires according to the following equation:
| R\ :sub:`MEAS1` = R\ :sub:`RTD` + 2R\ :sub:`L` = V :sub:`(I/OP to I/ON)` / I\ :sub:`EXCITE`

Step 3 (as shown in Blue)
~~~~~~~~~~~~~~~~~~~~~~~~~

The voltage between I/OP and I/O AUX, V :sub:`(I/OP to I/O AUX)` is also measured, as shown by the blue path in figure 3. This voltage, along with the excitation current value are used to determine the resistance of the RTD and a single lead wire, R<subL</sub (I/O AUX is a sense point only, so no current flows in this lead. As a result, the effect of this RL is not seen in the measurements). Use the following equation to determine the voltage:

| 
| V :sub:`(I/OP to I/O AUX)` = (ADC_CODE/65536)*RANGE - V\ :sub:`MIN`
| Where
| ADC_CODE is the code read back from the ADC
| RANGE is the full voltage span of the selected ADC range
| V\ :sub:`MIN` is the minimum voltage of the selected ADC range
| V :sub:`(I/OP to I/O AUX)` and I\ :sub:`EXCITE` are used to determine the combined resistance of the RTD and one R\ :sub:`L` according to the equation:
| R\ :sub:`MEAS2` = R\ :sub:`RTD` + 2R\ :sub:`L` = V :sub:`(I/OP to I/O AUX)` / I\ :sub:`EXCITE`
| ===RTD Calculations===
| These 3 measurements are then used to determine the lead resistance and as a result, the RTD resistance
| R\ :sub:`L` = R\ :sub:`MEAS1` - R\ :sub:`MEAS2`
| R\ :sub:`RTD` = R\ :sub:`MEAS2` - R\ :sub:`L`

Conversion Rates
~~~~~~~~~~~~~~~~

A choice of conversion rates is available for these measurements. See the AD74413R datasheet for the full range of conversion rates. To minimize the time taken for these measurements, it would be possible to only make one measurement continuously, as the RL resistance is not expected to change over time. The second measurement can be made less often to spot check that no significant changes have occurred to the RL value.

| 

Register Writes
---------------

| The following is an example set of register writes needed to make 3-wire RTD measurements on a channel. The RTD used in this example is a Pt1000. The excitation current and voltage measurement range are set accordingly. The writes assume that the device is in a high impedance state, after power-up or reset.

::

   *Configure Channel in Resistance Measurement mode via the CH_FUNC_SETUP0 register. (Address: 0x01, Data: 0x0007) Then set RTD3W4W_CONFIG register to measure resistance with 3 wire RTD. (Address: 0x07, Data: 0x0013) 
   *The last two bits of RTD3W4W_CONFIG register configures RTD_CURRENT to source 1mA    
   *Program current to 1.001 mA using the DAC_CODE register (Address: 0x16, Data: 0x0148)
   *Edit ADC_CONFIG register to configure CONV1_MUX and CONV2_MUX bits to measure voltage across SENSELF and SENSE_EXT1 bits to measure in the 0 V to 12 V range. (Address: 0x02, Data: 0x0083) 
   *Write to the ADC_CONV_CTRL register to enable continuous ADC conversions. (Address: 0x3b, Data: 0x2201)
   *Disable the continuous ADC conversion in the ADC_CONV_CTRL register. (Address: 0x3b, Data: 0x3201)
   *Read ADC_RESULT register (Address: 0x44)
   *Convert ADC_RESULT code from hex to decimal.
   *Place the ADC code into the equation to calculate 3 wire RTD resistance.  

|

Open Wire Detect
----------------

An open circuit detect feature is available on the leads of the 3-wire RTD. The combination of excitation current & RTD and lead resistances will generate voltages on the SENSEH and SENSE_EXT1 pins. If the voltage on either of these pins exceeds the short circuit detect voltage, an open circuit signal is asserted in the ALERT_STATUS register. This will happen if one of the leads are disconnected from the terminals.

:doc:`Back to AD74412R/AD74413R Table of Contents </wiki-migration/resources/eval/user-guides/ad7441x>`

.. |AD74115H_UseCase_3wireRTD.png| image:: https://wiki.analog.com/_media/AD74115H_UseCase_3wireRTD.png
.. |3w RTD extra components.png| image:: https://wiki.analog.com/_media/3w RTD extra components.png
.. |3w RTD steps.png| image:: https://wiki.analog.com/_media/3w RTD steps.png
