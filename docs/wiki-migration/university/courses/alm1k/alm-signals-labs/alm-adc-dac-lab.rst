Activity: Analog to Digital and Digital to Analog Conversion
============================================================

Objective:
----------

The objective of this exercise is to explore the concepts of analog to digital (ADC) and digital to analog (DAC) conversion making use of the CMOS inverter as an analog voltage comparator (used in ADC) and as reference switches for a resistor ladder divider (used in DAC).

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage/measure current –V is added as in CA-V or when configured to force current /measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

Background:
-----------

Let’s first examine the simple CMOS inverter logic gate. In the simplest form, it consists of one PMOS device, M1 and one NMOS device M2. Generally the CMOS fabrication process is designed such that the magnitude of the threshold voltage, VTH, of the NMOS and PMOS devices are roughly equal i.e. complementary. The designer of the inverter then adjusts the width to length ratio, W/L, of the NMOS and PMOS devices such that their respective transconductance is also equal. This results in the input threshold of the gate being very close to one half of the supply voltage VDD.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, CMOS Inverter


In addition to its use as a logic gate, we can also make use of this circuit as a high gain analog amplifier / voltage comparator. We can also view this circuit as a pair of complementary analog switches that alternately connect the output pin to either the VSS pin, through M2, or the VDD pin through M1.

Materials:
~~~~~~~~~~

| ADALM1000 Lab module
| Solder-less breadboard
| Jumper wires
| 1 – 860 Ω Resistor
| 1 – 500 Ω variable resistor / potentiometer
| 7 – 50 Ω Resistors (47 Ω or 68 Ω will also work as long as all resistors are same value)
| 8 – 10 KΩ Resistors
| 8 – LEDs (easier to use ones with built in current limit resistors)
| 1 – 10 uF Capacitor
| 1 – 74HC04 Hex inverter (standard 74HC parts include output buffers whereas the 74HCU parts are un-buffered and have lower gain)
| 1 – 74HC273 Octal D-type FF
| 2 – small signal NPN transistors (2N3094)

Directions:
~~~~~~~~~~~

First build the simple example shown here to test the input threshold of the simple CMOS inverter. Connect +5V power to VCC (pin 14) and ground to GND (pin 7). Connect the output of the waveform generator channel A to one of the 74HC04 inverter inputs (pin 1) and connect the inverter output (pin 2) to channel B input in Hi-Z mode.


|image1|

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Logic gate (74HC04) package pinout


Hardware Setup:
~~~~~~~~~~~~~~~

Configure AWG A output for a 100 Hz triangle wave with 0.0 Min value and 5V Max value. Both scope channels should be set to 0.5 V/Div.

Procedure:
~~~~~~~~~~

Measure the point on the triangle wave input where the inverter output changes from high to low and where the output changes from low to high as well.

Disconnect the VCC pin from the fixed +5 V and connect it to the second waveform generator output, CH B, and set the waveform to DC and the Max value to different values from 1.5 V to the maximum of 5 V in 0.5 V steps. You should adjust the Max value of waveform generator CH A so that it does not swing beyond the value you have set CH B to. Measure the threshold point for each value of the voltages that VCC was set to.

Questions:
~~~~~~~~~~

| How does the voltage on VCC affect the threshold point?
| Is the low to high threshold the same as the high to low threshold?
| Check the other five inverters in the same package. How different are their thresholds?
| If other devices are available (such as 74HC08 and 74HC32), check their input thresholds and how does the threshold vary package to package?

Flash Analog to Digital converter (Quantizer)
---------------------------------------------

.. _directions-1:

Directions:
~~~~~~~~~~~

Now using the 74HC273 Octal D Type register we will build the 9 level “Flash” ADC shown in the figure 4 schematic. Alternatively, a 7 level ADC could be constructed from the 74HC04 hex inverter used above and actually almost any CMOS logic inverter / buffer IC could be used.

An input reference resistor ladder is formed by 7 equal value (50Ω or similar) resistors, R2-R8. Each CMOS input is connected to a different tap on the ladder. Transistors Q1 and Q2 form a constant reference current source to drive the resistor ladder. R9 is chosen such that the voltage from the top of the ladder to the bottom of the ladder is about 2 Volts. A current of about 5 mA or 4.3 Volts/860Ω should be about right. The output of the Channel A generator drives the top of the reference ladder. The digital outputs from the FFs each drive an LED (D1 – D8). Four of the digital outputs can also optionally be connected to the four digital input lines on the ADALM1000 and be observed on the computer screen. The Master Reset input, pin 1 is tied to +5V. Pin 10 of the 74HC273 is connected to ground and Pin 20 (VCC) can be connected to +5 Volts. The input threshold will be affected depending on what supply voltage is used.

**74HC273 functional block diagram**

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-lfsr-fig_6.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 3 74HC273 Pinout


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-adc-dac-f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, 9 level “Flash” ADC


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Configure the waveform generator for DC values and use the Max value to adjust the output between 0 and 5 Volts. Use the CHA Avg to measure the average value where each LED turns on as the DC value is adjusted from 0 to 5 Volts. If the digital input connections are used, then open the digital I/O screen and configure the bits for input and proceed as with the LEDs.

.. _procedure-1:

Procedure:
~~~~~~~~~~

With the waveform generator shape, DC the Max value is first adjusted such that all of the LEDs are just off. Mark down that value as negative full scale. Next DC the Max value is adjusted such that half of the LEDs are on (D1-4) and half are off (D5-8). Mark down that value as mid-scale. Next DC the Max value is adjusted such that all of the LEDs are on (D1-8). Mark down that value as positive full scale. The value you found for mid-scale should be half way between the negative and positive full scale values.

For AWG A, set the Min value to the negative full scale value and set Max value to the positive full scale value. Set the shape to Triangle and the frequency to 2 Hz. Fow AWG B set the Min value tp 0 and the Max value to 5. Shape set to Square and the frequency to 10 KHz (frequency does not really matter as long as it is much higher than the frequency of the analog signal at the input of the ADC)

.. _questions-1:

Questions:
~~~~~~~~~~

Resistor divider Digital to Analog converter
--------------------------------------------

.. _directions-2:

Directions:
~~~~~~~~~~~

Again using the 74HC273 Octal FF build the 9 level “thermometer” DAC shown in the figure 5 schematic. Alternatively, a 7 level DAC could be constructed from the 74HC04 hex inverter used above and actually almost any CMOS logic inverter / buffer IC could be used.

An output reference resistor ladder is formed by 8 10KΩ resistors (R9-R16). Each CMOS output is connected to a different resistor tap on the ladder. The combined analog output is the common connection of all 8 resistors and can be measured by the BIN (channel B in Split I/O mode). The CMOS FF inputs are connected to either GND or +5 V to turn them on or off. The 4 ALM1000 digital I/O pins can be used to drive four of the CMOS inputs and controlled through the computer.

The Master reset input, pin 1 is tied to +5V. Pin 10 of the 74HC273 is connected to ground and Pin 20 (VCC) should be connected to +5 Volts. The maximum analog output voltage, full scale, will be affected depending on what supply voltage is used.

.. _hardware-setup-2:

Hardware Setup:
~~~~~~~~~~~~~~~

Open the digital I/O screen and configure the bits for output. Use the Channel A Avg measurement to measure the analog output value as different numbers (combinations) of the digital bits are turned on and off.

.. _procedure-2:

Procedure:
~~~~~~~~~~

All of the resistors used in this example are of the same value and thus all digital bits have the same weight. If resistors of different values were used such that each bit had a weight of ½ with respect to next most significant higher bit i.e. the resistor doubled in value, then many more analog output values could be generated and with higher resolution. If we were to start with 1KΩ as the resistor for the most significant bit and went up by 2 from there the values would be, 1KΩ, 2KΩ, 4KΩ, 8KΩ, 16KΩ, 32KΩ, 64KΩ and 128KΩ for the least significant bit. The first few resistors in this sequence could be created by using multiple 1K resistors in series. When the required value becomes 8KΩ or higher, it becomes obvious that creating weighted resistor values in this fashion has some drawbacks.

The R/2R ladder DAC shown in the next figure overcomes this drawback. Only one value of resistor is required. The second resistor value can be created by either combining 2 resistors in either series or parallel.

.. _questions-2:

Questions:
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-adc-dac-f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, 9 level “thermometer” DAC


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-adc-dac-f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, 8 bit R/2R ladder DAC


Combine both ADC and DAC
------------------------

.. _directions-3:

Directions:
~~~~~~~~~~~

Build the circuit as shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-adc-dac-f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Combined sampling ADC and DAC


.. _hardware-setup-3:

Hardware Setup:
~~~~~~~~~~~~~~~

.. _procedure-3:

Procedure:
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-adc-dac-f8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, Input / Output using triangle wave


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-adc-dac-f9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, unfiltered / filtered output using sine wave input


.. _questions-3:

Questions:
~~~~~~~~~~

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f2.png
   :width: 400px
