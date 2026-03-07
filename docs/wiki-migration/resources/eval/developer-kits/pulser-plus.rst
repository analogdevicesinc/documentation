Pulser Plus Reference Design for GaN PA Biasing and Sequencing (ADPULSERPLUSEBZ)
================================================================================

Features
========

-  Complete Bias Control and Sequencing Solution for Pulsed GaN Radar Power Amplifiers
-  Pin Compatible with ADI's existing Pulser Board and with ADI's GaN Power Amplifier Evaluation Boards
-  Operation in Drain Pulsed Mode or Gate Pulsed Mode
-  Optional Crowbar Circuit for Fast Turn Off in Drain Pulsed Mode
-  Single 24 V to 50 V Power Supply with on-board Negative Gate Voltage Generation.
-  Drain Current Monitoring Circuit

General Description
===================

*Pulser Plus* is a reference design for biasing Gallium Nitride RF Power Amplifiers. It plugs directly into Analog Devices’ GaN PA evaluation boards such as ADPA1106 and ADPA1107. The only input signals required to control and operate the board are a power supply voltage between 24 V and 50V and a 0V/3V signal on the Drain Pulse Enable or Gate Pulse Enable digital inputs. The Pulser Plus board can be ordered from Analog Devices using the part number ADPULSERPLUSEBZ (www.analog.com/adpulserplusebz).

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulserpulsangleviewwithpaevalmounted.jpg
   :align: center
   :width: 600px

The Pulser Plus reference design was specifically designed to enable fast pulsing of GaN Radar Power Amplifiers. It can support RF pulses as short as 1us and with rise and fall times of 200 ns. Figure 1 shows a simplified block diagram of the board. The circuit has two main branches, the Drain Voltage Generator and the Gate Voltage generator. The Drain Voltage Generator circuitry consists of a fast switching MOSFET (Infineon P/N BSC340N08NS3) and the LTC7000 FET driver. On the Drain/Supply side of the FET, there is bank of capacitors which store charge and facilitate fast on/off switching when the FET is switched on and off. There is also a 10 mΩ series resistor on the Drain side of the FET. Both sides of this resistor are connected to the LTC7000 SNS+ and SNS- pins for current sensing and current limiting. This resistor is also connected to the LT1999 current sense amplifier which provides a current monitoring signal which is faster than the LTC7000’s IMON function. The Drain Voltage Generator branch also includes a crowbar circuit (AON7296 (Alpha and Omega Semiconductor) and ADP3625 FET driver). This optional circuit can be used to provide very fast turn off of the drain voltage when operating in Drain Pulsed Mode. The Gate Voltage Generator circuitry consists of a negative voltage generator and LDO which create a -5.5V supply. This -5.5V powers a single supply op-amp (0V and -5.5V). A derived -5.0V signal also drives a resistor divider whose other side is connected ADG1401, a Single Pole Single Throw (SPST) switch. When the switch is open, the op-amp input and output voltage is -5V. This gate voltage is intended to put the GaN PA in pinch-off mode. When the SPST is closed, the resistor divider is active and the op-amp is driven by a voltage that can be varied from -0.7V to -3.3V using the potentiometer. The Source pin of the FET and the op-amp output are connected to a pair of 24 pin headers. Various ADI GaN PA evaluation boards can be plugged into this header pair and operated in Drain Puled Mode or Gate Pulsed Mode.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulserplustopview.jpg
   :align: center

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser_plus_block_diagram.png
   :align: center

Specifications
==============

+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Specifications*                 | *Target*         | *Notes*                                                                                                                                                                                                                                                                                                                                                                                                           |
+==================================+==================+===================================================================================================================================================================================================================================================================================================================================================================================================================+
| Drain Voltage Range              | 24 V to 50 V     | With the default values on R14, R15 and R18 (845K, 33.2K and 20K), ADPULSERPLUSEBZ will stop operating at around 20V. By adjusting the values of R14, R15 and R18, operation at lower drain voltages is possible. At the target VDD, the voltage at the RUN pin must be greater than 1.21V and the voltage on the OVLO pin must be less than 1.21V. For example, to operate with a VDD of 12V, reduce R14 to 392K |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Gate Voltage Range               | -0.7 V to -3.3 V |                                                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pinchoff Voltage                 | -5 V             |                                                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Maximum Drain Current            | 5 A              |                                                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Maximum Gate Current             | +/-10 mA         |                                                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Rise Time (Drain Pulsed Mode)    | 65 ns            | 10% to 90% of Drain Voltage (VDD_PA)                                                                                                                                                                                                                                                                                                                                                                              |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fall Time (Drain Pulsed Mode)    | 85 ns            | 90% to 10% of Drain Voltage (VDD_PA)                                                                                                                                                                                                                                                                                                                                                                              |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Turn On Time (Drain Pulse Mode)  | 150 ns           | 50% of Drain Pulse Enable to 90 % of Drain Voltage (VDD_PA)                                                                                                                                                                                                                                                                                                                                                       |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Turn On Time (Drain Pulse Mode)  | 150 ns           | 50% of Drain Pulse Enable to 1dB Settling of RF output                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Turn Off Time (Drain Pulse Mode) | 160 ns           | 50% of Drain Pulse Enable to 10 % of Drain Voltage (VDD_PA)                                                                                                                                                                                                                                                                                                                                                       |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Turn Off Time (Drain Pulse Mode) | 130 ns           | 50% of Drain Pulse Enable to 1dB Settling of RF output                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Rise Time (Gate Pulsed Mode)     | 35 ns            | 10% to 90% of Gate Voltage (VGG1)                                                                                                                                                                                                                                                                                                                                                                                 |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fall Time (Gate Pulsed Mode)     | 150 ns           | 90% to 10% of Gate Voltage (VGG1)                                                                                                                                                                                                                                                                                                                                                                                 |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Turn On Time (Gate Pulse Mode)   | 270 ns           | 50% of Drain Pulse Enable to 90 % of Gate Voltage (VGG1)                                                                                                                                                                                                                                                                                                                                                          |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Turn On Time (Gate Pulse Mode)   | 340 ns           | 50% of Gate Pulse Enable to 1dB Settling of RF output                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Turn Off Time (Gate Pulse Mode)  | 370 ns           | 50% of Gate Pulse Enable to 10 % of Gate Voltage (VGG1)                                                                                                                                                                                                                                                                                                                                                           |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Turn Off Time (Gate Pulse Mode)  | 240 ns           | 50% of Gate Pulse Enable to 1dB Settling of RF output                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Performance Plots
=================

The performance plots shown here were measured with the ADPA1116 connected to the Pulser Plus board. Gate and Drain capacitances on the evaluation board were removed as necessary to ensure a fast response in Gate Pulsed and Drain Pulsed mode.

:doc:`Performance Plots </wiki-migration/resources/eval/developer-kits/pulser-plus/performanceplots>`

Power Amplifier Evaluation Board Compatibility
==============================================

Compatibility of power amplifiers with the Pulser Plus board is primarily a function of the pinout of the header(s) on the PA evaluation board. Where the header is not pin-compatible, it should be still possible to wire the two boards together. When doing this, try to keep wire lengths as short as possible and make sure that the VDD lines are thick enough to handle the expected current.

+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Part Number* | *Description*                                            | *Notes*                                                                                                                                                                                                                                                                                                                                               |
+===============+==========================================================+=======================================================================================================================================================================================================================================================================================================================================================+
| ADPA1105      | 46 dBm (40 W), 0.9 GHz to 1.6 GHz, GaN Power Amplifier   |                                                                                                                                                                                                                                                                                                                                                       |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ADPA1106      | 46 dBm (40 W), 2.7 GHz to 3.5 GHz, GaN Power Amplifier   |                                                                                                                                                                                                                                                                                                                                                       |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ADPA1107      | 45.0 dBm (35 W), 4.8 GHz to 6.0 GHz, GaN Power Amplifier |                                                                                                                                                                                                                                                                                                                                                       |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ADPA1113      | 46 dBm (40W), 2 GHz to 6 GHZ, GaN Power Amplifier        | Not suitable for fast Gate Pulsing due to internal capacitance on ADPA1113's VGG1 pin                                                                                                                                                                                                                                                                 |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ADPA1116      | 37 dBm (5 W), 0.3 GHz to 6 GHz, GaN Power Amplifier      | ADPA1116 eval board header is not pin-compatible with Pulser Plus but operation was verified by wiring the two boards together. To achieve fast turn-on and turn-off times, remove the 0.1uF capacitors from the ADPA1116's evaluation board VDD line if pulsing on the drain. If pulsing on the gate, remove the 4.7 uF capacitor from the VGG1 line |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ADPA1122      | 43 dBm, 20 W, GaN Power Amplifier, 8.2 GHz to 11.8 GHz   |                                                                                                                                                                                                                                                                                                                                                       |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HMC8415       | 40 W (46 dBm), 9 GHz to 10.5 GHz, GaN Power Amplifier    |                                                                                                                                                                                                                                                                                                                                                       |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HMC8205BF10   | 0.3 or 0.4 GHz to 6 GHz, 35 W, GaN Power Amplifier       | not compatible due to pinout of eval board header                                                                                                                                                                                                                                                                                                     |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HMC7885       | 2 GHz to 6 GHz, 45 dBm Power Amplifier                   | not compatible due to pinout of eval board header                                                                                                                                                                                                                                                                                                     |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HMC8500PM5E   | 10 W (40 dBm), 0.01 GHz to 2.8 GHz, GaN Power Amplifier  | not compatible due to pinout of eval board header                                                                                                                                                                                                                                                                                                     |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HMC1114PM5E   | >10 W (42 dBm), 2.7 GHz to 3.8 GHz, GaN Power Amplifier  | not compatible due to pinout of eval board header                                                                                                                                                                                                                                                                                                     |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HMC1099PM5E   | 10 W (40 dBm), 0.01 GHz to 1.1 GHz, GaN Power Amplifier  | not compatible due to pinout of eval board header                                                                                                                                                                                                                                                                                                     |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HMC1086F10    | 25 Watt Flange Mount GaN MMIC Power Amplifier, 2 - 6 GHz | not compatible due to pinout of eval board header                                                                                                                                                                                                                                                                                                     |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HMC1087F10    | 8 Watt GaN Flange Mount MMIC Power Amplifier, 2 - 20 GHz | not compatible due to pinout of eval board header                                                                                                                                                                                                                                                                                                     |
+---------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Theory Of Operation
-------------------

Circuit description and operation can be found here:

`Theory Of Operation subpage <https://wiki.analog.com/~/theoryofoperation>`_

-  `Input caps - bulk <https://wiki.analog.com/~/theoryofoperation>`_
-  `Drain Pulse Generator <https://wiki.analog.com/~/theoryofoperation>`_

   -  `VDD_PA voltage sense <https://wiki.analog.com/~/theoryofoperation>`_

-  `PA Drain Current Sense <https://wiki.analog.com/~/theoryofoperation>`_
-  `Electronic Circuit Breaker <https://wiki.analog.com/~/theoryofoperation>`_
-  `PA Gate Pulse Generator <https://wiki.analog.com/~/theoryofoperation>`_

   -  `Negative converter <https://wiki.analog.com/~/theoryofoperation>`_
   -  `Gate pulse generation <https://wiki.analog.com/~/theoryofoperation>`_
   -  `Gate pulse generation circuit when drain pulsing <https://wiki.analog.com/~/theoryofoperation>`_

-  `Sequencing <https://wiki.analog.com/~/theoryofoperation>`_

Drain Pulsed Mode Operation
---------------------------

The figure below shows the recommended bench setup for operation in Drain pulsed mode.


|image1|

Setup
~~~~~

-  Setup the power supply voltages before attaching the PA board to the underside of the Pulser Plus board
-  Set up the power supply's output voltage somewhere between 22V to 50V based on the requirements of the power amplifer being used. With the supply voltage turned off, connect the power supply cables to the red and black banana connectors (black=GND). Leave this voltage off for now.
-  Set up a 3V dc supply to drive the Gate Pulse Enable SMA connector. This voltage will be used to switch the gate voltage between its pinch off level of -5V (Gate Pulse Enable = 0V) and its bias level that was set by the potentiometer (Gate Pulse Enable = +3V). Leave this voltage off for now.
-  Before attaching the PA evaluation board to the underside of the Pulser Plus board, turn on the main supply and set the Gate Pulse Enable voltage to +3V.
-  Connect a Digital Volt Meter (DVM) to the VGG1 and GND clip leads and adjust the blue potentiometer(R48) until the desired gate voltage is set. This voltage will generally be set in the -0.5 to -2.5V range. Consult the IDQ vs VGG1 plot in the PA datasheet for further guidance. Once this step is complete turn off the Gate Pulse Enable voltage and the main power supply.
-  Carefully plug the PA evaluation board into the underside of the Pulser Plus board. Make sure that the pins are correctly aligned and that RFOUT is towards the front of the Pulser Plus board, aligned with the Drain Pulse Enable and VDD_PA SENSE SMA connectors.
-  Connect an RF Signal Generator and Spectrum Analyzer to the RFIN and RFOUT SMA connectors of the PA evaluation board. Set the RF input power level and frequency according to the PA datasheet. Ensure that the RF output power from the signal generator is off for now.
-  In general an attenuator will be required between RFOUT and the input of the spectrum analyzer to avoid damage to the spectrum analyzer. Typically a 20-30 dB of attenuator with adequate heat sinking will be used. Most spectrum analyzers have a "Reference Level Offset" function. By typing in the loss of the attenuator and cables between the PA evaluation board and the spectrum a analyzer, the displayed power on screen will indicate the power at the PA eval board output.
-  Set the spectrum analyzer center frequency, attenuation and reference level based on the expected input frequency and power level.
-  Care should be taken in setting the attenuation level of the spectrum analyzer. To maximize the dynamic range of the measurement, set the attenuation of the spectrum analyzer to the minimum that the spectrum analyzer will accept (this will maximize the range of the instrument's internal RF power detectors). Setting the spectrum analyzer's input attenuation level too high may result in an slow observed response time, particularly on its falling edge.
-  Switch the operating mode to Zero Span. Set the Resolution Bandwidth (RBW) and Video Bandwidth (VB) to the highest available values (ideally 10 MHz or greater). Set the sweep trigger to "External"
-  Connect a digital pulse generator to the Drain Pulse Enable SMA connector. The high level on this pulse should be between 3V and 5V. Note the Drain Pulse Enable input is terminated with a 50 ohm resistor (R13) on the Pulser Plus Board. Set up the digital pulser generator so that it is expecting to be driving a 50 ohm load.
-  The sync output of the pulse generator should be connected to the trigger input of the spectrum analyzer. This signal will provide the trigger to the spectrum analyzer to start its zero span sweep.
-  If the PA evaluation board is not connected to a heat sink, operation at a very low duty cycle is recommended. A starting pulse profile of 10 us high and 10 ms low is recommended (i.e. 0.1% duty cycle). For PAs operating up to 47 dBm output power, this duty cycle has been observed to result in negligible self-heating.

Turn On
~~~~~~~

-  Ensure that the voltage on Gate Pulse Enable is low
-  Turn on the main VDD supply volage (24V to 50V)
-  Set Gate Pulse Enable to high (3V)
-  Turn on the RF Signal Generator
-  Turn on the input pulse to Drain Pulse Enable

The signal on the spectrum analyzer should be similar to the trace below.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/pulser_plus_drain_pulsed_mode_1us_pulse.jpg
   :align: center
   :width: 600px

Turn Off
~~~~~~~~

-  Turn off the RF Signal Generator
-  Set Gate Pulse Enable to low
-  Turn off the pulse to Drain Pulse Enable (set to low)
-  Turn off the main VDD supply volage

Gate Pulsed Mode Operation
--------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/gate_pulsed_mode_block_diagam.jpg
   :align: center

.. _setup-1:

Setup
~~~~~

-  The setup for Gate Pulsed Mode operation is very similar to Drain Pulsed Mode. The main difference is that the connection of the pulse source and the dc source to Drain Pulse Enable and Gate Pulse Enable connectors respectively, is flipped, that is a fixed logic 1 is placed on the Drain Pulse Enable input and a 0/3V pulse is placed on the Gate Pulse Enable input.
-  Most of ADI's GaN PA evaluation boards ship with significant capacitance connected to the VGG1 pin. To operate in Drain Pulsed Mode, most of these capacitors must be removed. In general 100pF or 1nF of capacitance should be left in place.
-  Setup up the power supply voltages before attaching the PA board to the underside of the Pulser Plus board
-  Set the power supply's output voltage somewhere between 22V to 50V based on the requirements of the power amplifier being used. With the supply voltage turned off, connect the power supply cables to the red and black banana connectors (black=GND). Leave this voltage off for now.
-  Set up a 3V dc supply to drive the Drain Pulse Enable SMA connector. Leave this voltage off for now.
-  Set up a 3V dc supply to drive the Gate Pulse Enable SMA connector Leave this voltage off for now.
-  Before attaching the PA evaluation board to the underside of the Pulser Plus board, turn on the main supply and set the Gate Pulse Enable voltage to +3V.
-  Connect a Digital Volt Meter (DVM) to the VGG1 and GND clip leads and adjust the blue potentiometer(R48) until the desired gate voltage is set. This voltage will generally be set in the -0.5 to -2.5V range. Consult the IDQ vs VGG1 plot in the PA datasheet for further guidance on what value to choose for VGG1. Once this step is complete turn off the Gate Pulse Enable voltage and the main power supply.
-  Remove the dc supply connected to Gate Pulse Enable and replace it with a digital pulse generator. The high level on this pulse should be between 3V and 5V. Note the Gate Pulse Enable input is terminated with a 200 ohm resistor (R49) on the Pulser Plus Board. If Drain Pulse Enable is going to be driven from a 50 ohm source, replace R49 with a 50 ohm resistor and set up the digital pulser generator so that it is expecting to be driving a 50 ohm load. Set the Drain Pulse Enable pulse to 0V for now.
-  Connect an RF Signal Generator and Spectrum Analyzer to the RFIN and RFOUT SMA connectors of the PA evaluation board.
-   Carefully plug the PA evaluation board into the underside of the Pulser Plus board. Make sure that the pins are correctly aligned and that RFOUT is towards the front of the Pulser Plus board, aligned with the Drain Pulse Enable and VDD_PA SENSE SMA connectors.
-   Set the RF input power level and frequency according to the PA datasheet. Ensure that the RF output power from the signal generator is off for now.
-  In general an attenuator will be required between RFOUT and the input of the spectrum analyzer to avoid damage to the spectrum analyzer. Typically a 20-30 dB of attenuator with adequate heat sinking will be used.
-  Set the spectrum analyzer center frequency, attenuation and reference level based on the expected input frequency and power level.
-  Care should be taken in setting the attenuation level of the spectrum analyzer. To maximize the dynamic range of the measurement, set the attenuation of the spectrum analyzer to the minimum that the spectrum analyzer will accept (this will maximize the range of the instrument's internal RF power detectors). Setting the spectrum analyzer's input attenuation level too high may result in an slow observed response time, particularly on its falling edge.
-  Switch the operating mode to Zero Span. Set the Resolution Bandwidth (RBW) and Video Bandwidth (VB) to the highest available values (ideally 10 MHz or greater). Set the sweep trigger to "External"
-  Switch the operating mode to Zero Span. Set the Resolution Bandwidth (RBW) and Video Bandwidth (VB) to the highest available values (ideally 10 MHz or greater). Set the sweep trigger to "External" and connect the pulse generator's sync or trigger output to the external trigger input of the spectrum analyzer. This signal will trigger input will be used to start the spectrum analyzer's zero span sweep
-  If the PA evaluation board is not connected to a heat sink, operation at a very low duty cycle is recommended. A starting pulse profile of 10 us high and 10 ms low is recommended (i.e. 0.1% duty cycle). For PAs operating up to 47 dBm output power, this duty cycle has been observed to result in negligible self-heating.

.. _turn-on-1:

Turn On
~~~~~~~

-  Ensure that the voltage on Gate Pulse Enable is low (pulse generator output disabled)
-  Turn on the main VDD supply volage (24V to 50V)
-  Turn on Drain Pulse Enable (3V dc)
-  Turn on the RF Signal Generator
-  Turn on the output of the pulse generator driving Gate Pulse Enable

.. _turn-off-1:

Turn Off
~~~~~~~~

-  Turn off the output of the pulse generator driving Gate Pulse Enable
-  Turn off the RF Signal Generator
-  Turn off Drain Pulse Enable (0V dc)
-  Turn off the main VDD supply volage (24V to 50V)

Resources
---------

`pulserplus_schematic_02-072726-01-c.pdf <https://wiki.analog.com/_media/resources/eval/developer-kits/pulserplus_schematic_02-072726-01-c.pdf>`_

`pulserplus_cadence_brd_file_08_072726b.zip <https://wiki.analog.com/_media/resources/eval/developer-kits/pulserplus_cadence_brd_file_08_072726b.zip>`_

`pulser_plus_bom_05-072726-01-c.xlsx <https://wiki.analog.com/_media/resources/eval/developer-kits/pulser_plus_bom_05-072726-01-c.xlsx>`_

`pulserplusgerberfiles.zip <https://wiki.analog.com/_media/resources/eval/developer-kits/pulserplusgerberfiles.zip>`_

Support
-------

| For support on this reference design, please contact us through our technical support portal at the follow link: :adi:`technical-support.html <en/support/technical-support.html>`. Alternatively, you can log on to the RF & Microwave Community on Engineerzone (` <https://ez.analog.com/rf/>`__) and post a question that contains the Keywords "PulserPlus" or "Pulser Plus" and we will get back to you.

.. |image1| image:: https://wiki.analog.com/_media/drain_pulsed_mode_block_diagam.jpg
