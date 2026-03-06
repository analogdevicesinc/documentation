3-Wire RTD Measurements with AD74413R
=====================================

Introduction
------------

| The AD74413R, software configure I/O IC is designed to interface with industrial, process & building control sensors and actuators. The IC comes with a range of programmable I/O capabilities, including analog output, analog input, digital input and temperature measurement. Temperature measurement is crucial in many industrial environments, with thermocouples and RTDs (Resistance Temperature Detectors) being the most commonly used temperature sensor types. The AD74413R has in-built thermocouple and 2-wire RTD measurement capability. 3-wire RTD measurements are not directly supported on chip but this Wiki page will show how to use the AD4413R to make 3-wire RTD measurements, while maintaining all of the existing functionality of the IC.

RTDs
----

| An RTD (Resistance Temperature Detector) is a sensor used to measure temperature. RTDs have a repeatable resistance vs temperature relationship which can be used to accurately determine the temperature. RTDs are used in a wide variety of applications and are particularly suitable for industrial applications due to their with wide operating temperature ranges and reliability.
| To measure temperature with an RTD, a small excitation current is passed through it and the corresponding voltage drop is measured. The corresponding resistance is calculated and used to determine the ambient temperature of the sensor.
| ===RTD Types=== 2-wire RTDs are typically used for low accuracy applications and when the distance to the sensor is short (lead lengths are short). Longer leads result in larger lead resistances, which add error to the overall resistance measurement. If long lead lengths are in use or higher accuracy is required, 3-wire RTDs are used. In this case, it is assumed that each of the leads are of similar length and resistance. A 3-wire RTD measurement allows for an estimate of this lead resistance to be made and this in turn is factored out of the overall resistance measurement. Finally, 4-wire RTDs provide the best accuracy - 2 wires are used to source the excitation current through the sensor while the remaining 2 wires are used to directly sense the voltage drop across the RTD sensor.

| 

External Component changes to AD74413R circuit to support 3-wire RTD
--------------------------------------------------------------------

| 
| Refer to figure 1 for a high level block diagram of the standard configuration for the AD74413R. The recommended external components and connections ensure that all of the features of the AD74413R are supported on the two external screw terminals I/OP and I/ON. |74413R_ext_components.png|
| Figure 1: Standard configuration to support all Ad74413R I/O functions

A single switch should be added to the circuit to support 3-wire measurements. See Figure 2 for the updated circuit drawing, showing the placement of the switch. The switch is controlled using a AD74413R GPO - no additional data lines are needed from the host microcontroller. The recommended switch for this function is ADG5436F. The ADG5436F has two independently selectable single-pole, double-throw switches. The device is fault protected, with pins protected against voltages greater than the supply rails, up to +/-55V. This dual device will support the switching required for 2 channels of the AD74413R. Two ADG5436Fs are required to support 3-wire RTD capability on all four channels of the AD74413R. Figure 2 also shows the additional third screw terminal, I/O AUX and the TVS recommended to protect this terminal.

| 
| |3w RTD extra components.png|
| Figure 2: Additional components required to support 3-wire RTD measurements

| 
| With the hardware configuration, as shown in figure 2, the AD74413R supports all of the existing I/O functions as well as the 3-wire RTD measurements. All functions can be programmed via the 4-wire SPI.

| 

Implementation
--------------

Figure 3 shows the steps required to make a 3-wire RTD measurement. The process uses existing capabilities available on the AD74413R to source a current to the RTD and measure the corresponding voltages on the RTD sensor.

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
| R\ :sub:`MEAS2` = R\ :sub:`RTD` + R\ :sub:`L` = V :sub:`(I/OP to I/O AUX)` / I\ :sub:`EXCITE`
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

| The following is an example set of register writes needed to make 3-wire RTD measurements on Channel A. The RTD used in this example is a Pt1000. The excitation current and voltage measurement range are set accordingly. The writes assume that the device is in a high impedance state, after power-up or reset.

-  Configure Channel A in Current Output mode via the CH_FUNC_SETUP register. (Address: 0x01, Data: 0x0002)
-  Set & measure the excitation current

::

     *Program current to 1.001 mA using the DAC_CODE register (Address: 0x16, Data: 0x0148)
     *Measure actual current 
        *Ensure external switch is set to connect SENSEHF is switched to the RSENSE resistor
        *Edit ADC_CONFIG register to configure ADC_MUX bits to measure voltage across RSENSE and RANGE bits to measure in the 0 V to 2.5 V range. (Address: 0x05, Data: 0x0041)
        *Write to the ADC_CONV_CTRL register to start ADC Conversions (Address: 0x23, Data: 0x0201)
        *Read ADC_RESULT register (Address: 0x26)
        *Measured excitation current calculation:
        *I<sub>EXCITE</sub> = (ADC_CODE/65535*2.5)/100
   * Measure Voltage between I/OP and I/ON, to determine R<sub>RTD</sub> + 2R<sub>L</sub>
     *Write to the ADC_CONV_CTRL register to stop conversions (Address: 0x23, Data: 0x0001)
     *Edit ADC_CONFIG register to configure ADC_MUX bits to measure voltage between I/OP and I/ON and RANGE bits to measure in the 0 V to 2.5 V range (Address: 0x05, Data: 0x0020)
     *Write to the ADC_CONV_CTRL register to start ADC Conversions (Address: 0x23, Data: 0x0201)
     *Read ADC_RESULT register (Address: 0x26)
   * Measure Voltage between I/OP and I/O DIFF, to determine R<sub>RTD</sub> + R<sub>L</sub>
     *Write to the ADC_CONV_CTRL register to stop Conversions (Address: 0x23, Data: 0x0001)
     *Edit ADC_CONFIG register to configure ADC_MUX bits to measure voltage between SENSELF and SENSEHF (Address: 0x05, Data: 0x0021)
     *Write to the ADC_CONV_CTRL register to re-start ADC Conversions (Address: 0x23, Data: 0x0201)
     *Read ADC_RESULT register (Address: 0x26)
   * Calculate R<sub>L</sub> and R<sub>RTD</sub> from the measurements

|

Open Wire Detect
----------------

The IOUT open circuit fault is asserted when an open wire is present on either I/OP or I/ON screw terminals. This open circuit fault is indicated on the ALERT pin, which can be used as an interrupt to the host microcontroller.

:doc:`Back to AD74412R/AD74413R Table of Contents </wiki-migration/resources/eval/user-guides/ad7441x>`

.. |74413R_ext_components.png| image:: https://wiki.analog.com/_media/74413R_ext_components.png
.. |3w RTD extra components.png| image:: https://wiki.analog.com/_media/3w RTD extra components.png
.. |3w RTD steps.png| image:: https://wiki.analog.com/_media/3w RTD steps.png
