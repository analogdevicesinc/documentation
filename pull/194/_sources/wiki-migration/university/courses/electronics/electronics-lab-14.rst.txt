Activity:Digital to analog conversion
=====================================

R-2R Resistor Ladder Digital to Analog Converter
------------------------------------------------

Objective:
~~~~~~~~~~

The objective of this exercise is to explore the concepts of digital to analog conversion making use of the CMOS inverter as reference switches for a resistor ladder divider (used in DAC).

Background:
~~~~~~~~~~~

We will exploit the simple CMOS inverter logic gate as a pair of switches. The digital I/O signals of the ADALM2000 module can be configured as standard CMOS dividers with a +3.3 Volt supply (push-pull mode). In the simplest form, a CMOS output consists of one PMOS device, M\ :sub:`1` and one NMOS device M\ :sub:`2`. Generally the CMOS fabrication process is designed such that the threshold voltage, V\ :sub:`TH`, of the NMOS and PMOS devices are roughly equal i.e. complementary. The designer of the inverter then adjusts the width to length ratio, W/L, of the NMOS and PMOS devices such that their respective transconductance and thus their R\ :sub:`ON`, is also equal. Only one of the two transistors is ever on at the same time connecting the Output to either V\ :sub:`DD` or V\ :sub:`SS`. We can consider these two voltages to be the reference for out DAC.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a14_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 CMOS output driver


When used in what is referred to as "voltage mode" legs the R-2R resistor ladder, figure 2, are alternately driven to either of 2 reference voltage levels based on the digital code (D0-7). Digital 0 for V\ :sub:`REF`- and digital 1 for V\ :sub:`REF`\ +. Depending on the digital input code V\ :sub:`LADDER` ( in figure 2 ) will be some fraction of the difference between the two reference levels. The negative of the two reference voltages (V\ :sub:`REF`-) is often ground (V\ :sub:`SS`). The positive reference voltage (V\ :sub:`REF`\ +) in our case here will be the positive supply (V\ :sub:`DD`) for the CMOS driver.

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 9 - 20 KΩ Resistors
| 9 - 10 KΩ Resistors
| 1 - OP27 amplifier

Directions:
~~~~~~~~~~~

Build the 8 bit resister ladder circuit shown in figure 2, preferably on your solder-less breadboard. The number of resistors normally supplied in the Analog Parts Kit is not sufficient to build the full 8 bit ladder. It is best to use 1% resistors for this project if you have access to them.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/r_2r_ladder_dac.png

.. container:: centeralign

   Figure 2 R-2R Resistor Ladder circuit


Connect the 8 digital outputs designated by the blue boxes, and the scope channel and AWG output designated by the green boxes to the resistor ladder circuit as shown. Remember to connect power to the op amp supply pins.

Hardware Setup:
~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a14_f2_bb.JPG
   :align: center

.. container:: centeralign

   Figure 3 R-2R Resistor Ladder Circuit Breadboard Connections


Procedure:
~~~~~~~~~~

With both R\ :sub:`1` and R\ :sub:`2` installed, set AWG1 to a DC voltage equal to the V\ :sub:`REF`\ + of the DAC which will be the +3.3 Volt supply voltage of the CMOS digital outputs. This will produce a bipolar output voltage which will swing from -3.3V to +3.3V. Disconnect AWG1 and remove resistor R\ :sub:`1` for a unipolar output voltage which will swing from 0 to +3.3V. Start the Scopy software. Open up the Pattern Generator screen. Select and group DIO 0 - 7. Now edit the parameters. Set pattern to Binary counter. The output should be PP (for push-pull) and set the frequency for 256 KHz. You should see something that looks like the screen below shown in figure 4. Lastly, hit the Run button.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/dac_pg_setup.png
   :align: right

.. container:: centeralign

   Figure 4 Pattern Generator screen


Open the Scope screen, turn channel 2 on, and set the time base for 200us/div. Be sure to hit the green Run button. You may also need to adjust the vertical range for the channel 1 V/div is probably good to start with. You should see (figure 4) the voltage ramp up from 0 volts to 3.3 volts. The period of the ramp should be 1mSec.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a14_f4.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5 Scope screen


Change the digital pattern. Try the Random pattern and open the FFT window on the scope. You can also load custom patterns by making a plain text csv file with a column of numbers ranging from 0 to 255 (for the 8 bit wide bus). Load your custom pattern and see what happens.

Here are some pre-made waveform files you can try: Sine, Triangle, Gaussian pulse etc. :git-education_tools:`m2k/import_waveforms/waveforms_pg`

AD5626 12-bit nanoDAC
---------------------

.. _background-1:

Background
----------

AD5626 is a vltage output digital-to-analog converter that can operate from a single 5V supply. It contains the DAC, input shift register and latches, reference, and a rail to-rail output amplifier which can swing to either rail and is set to a range of 0 V to 4.095 V for a one-millivolt-per-bit resolution. This part features a serial interface that is high speed, threewire, DSP compatible with data in (SDIN), clock (SCLK), and load strobe (LDAC). There is also a chip-select pin for connecting multiple DACs. The CLR input sets the output to zero scale at power on or upon user demand.


|image1|

.. container:: centeralign

   Figure 6. functional block diagram of AD5626


The AD5626 has a separate serial input register from the 1-bit DAC register and it allows preloading of a new data value into the serial register without disturbing the present DAC output voltage. the loaded value can be transferred to the DAC register by strobing the LDAC pin.

Unipolar output operation
-------------------------

This mode of operation is the basic mode for AD5626. You can verify the god functionality AD5626 according to the unipolar code table of the digital to analog convertor.


|image2|

.. container:: centeralign

   Figure 7. Unipolar code table of AD5626


.. _materials-1:

Materials
~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - AD5626 12-bit nanoDAC
| 1 - 2.2 KΩ resistor
| 1 - 0.001 uF capacitor
| 1 - 0.1 uF capacitor
| 1 - 10 uF capcitor

.. _hardware-setup-1:

Hardware setup
~~~~~~~~~~~~~~

Connect the pins of AD5626 as shown in figure 8.


|image3|

.. container:: centeralign

   Figure 8. Connections for Unipolar operation AD5626


   |image4|

.. container:: centeralign

   Figure 9. AD5626 breadboard connections


.. _procedure-1:

Procedure
~~~~~~~~~

Open Scopy and enable the positive power supply to 5V. in Pattern generator you should configure the DAC input signals according to the timing diagram of AD5626 presented in datasheet. Start by configuring SPI signals. Create a group channel with DIO0, DIO1 and DIO2. If the connections were done as in figure 8 then DIO1 is the clock signal, DIO2 the data signal and DIO0 the /CS signal. Pay attention that the digital channels are in the right order when grouped as SPI (see figure 11). It is specified in datasheet that the clock width for both high and low states should be at least 30 ns. From this you can compute the clock period and therefore maximum frequency. Set the clock frequency to 1Mhz. Set CLK Polarity and CLK Phase to 1.

As the AD5626 is a 12-bit DAC, the data sent through SPI should be aleast 12 bits long. Set the number of Bytes per frame to 2 and it will send 16 bits when the conversion is initiated. In the Data text box you can enter the value to be sent to the ADC. The signals of the SPI group channel should resemble the timing diagram of the AD5626 digital to analog converter.


|image5|

.. container:: centeralign

   Figure 10. AD5626 SPI timing diagram


Now you should configure /LDAC and /CLR signals. From the datasheet we know that the shift register contents are updated on the rising edge of /LDAC if /CLR is high. Set the pattern of DIO4 (/CLR) as "Number" and enter the value 1. /LDAC signal(DIO3) should have a rising edge before /CS falling egde and should be high as long as bits are transmitted serially. In order to fulfill tre previoulsy stated conditions, DIO3 signal can be set at 13kHz frequency and 160 degrees phase. In figure 10 are presented all the input signals needed for AD5626 digital to analog conversion.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/07ff.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 11. Pattern generator signals setup


The last step is to open oscilloscope and connect channel 1 to the output of AD5626. Enable channel 1 measurements and enter a value in the "Data" area of SPI. In figure 12 you can see the output voltage if the data sent through SPI is 7FF.



|image6|

.. container:: centeralign

   Figure 12. AD5626 output voltage for 7FF input.


Bipolar output operation
------------------------

Although the AD5626 has been designed for single-supply operation, bipolar operation is achievable using the circuit illustrated in Figure 13.


|image7|

.. container:: centeralign

   Figure 13. Bipolar output operation without trim


   | This circuit can be used for applications that do not require high accuracy. The output voltage is coded in offset binary and is given by:
|

.. container:: centeralign

   :math:`Vo = 1mV \times Digital Code \times (R4/(R3+R4)) \times (1+R2/R1)-2.5 \times (R2/R1)`


| 
| For the ±5V output range and the circuit values shown in the table in figure 13 the transfer equation becomes:
|

.. container:: centeralign

   :math:`Vo=2.44 mV \times Digital Code- 5V`


.. _materials-2:

Materials
~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - AD5626 12-bit nanoDAC
| 1 - 0.1 uF capacitor
| 1 - 1 KΩ resistor
| 1 - 20 KΩ resistor
| 2 - 10 KΩ resistors
| 1 - 47 KΩ resistor
| 1 - 470 KΩ resistor
| ====Hardware setup==== Build the circuit presented in figure 13 on your solderless breadboard. |image8|

.. container:: centeralign

   Figure 14. AD5626 Bipolar output operation breadboard connections


.. _procedure-2:

Procedure
~~~~~~~~~

You can configure the DAC for unipolar output operation as described above. For the voltage reference use the channel 1 of the Signal generator set for constant 2.5V . On the second channel of the oscilloscope visualize the voltage at the output of the opamp. You can visualize both the voltages for unipolar operation and bipolar operation at the same time on the oscilloscope.


|image9|

.. container:: centeralign

   Figure 15. Unipolar and Bipolar output voltage for 000 input


   |image10|

.. container:: centeralign

   Figure 16. Unipolar and Bipolar output voltage for 800 input


   |image11|

.. container:: centeralign

   Figure 17. Unipolar and Bipolar output voltage for FFF input


Questions:
----------

1. Using Ohm's law and the formula for resistors in parallel, what is the output voltage of the R-2R DAC when inputs D7 and D6 are connected to each combination of ground and 3.3 volts? Please present the results as a table.

2. How much current will flow through this resistor network when input D6 is connected to 3.3 volts and D7 to ground?

3. Discuss which DAC topology had better linearity, and why you would (or would not) expect this to be the case.

4. How would you expect these DACs to perform for high frequency inputs? For better high frequency components, would you want smaller or larger resistor values? Discuss the relative merits of choosing large or small resistors for the DAC.

5. One of the effects of reducing the size of the resistors is that the parasitic switch resistances could start to become significant relative to the resistors. What would the output levels be for a 3-bit Binary-Weighted Resistor DAC where the switch resistance in figure 1 was 0.25R?

6. If you were going to design a 16-bit DAC for audio purposes (for a mp3 player output), how would the resistor tolerances affect the errors in the output for an R-2R ladder DAC?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/dac_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/dac_ltspice`
   


For further reading:
~~~~~~~~~~~~~~~~~~~~

Analog Devices Mini Tutorial 015 http://www.analog.com/static/imported-files/tutorials/MT-015.pdf

http://en.wikipedia.org/wiki/Resistor_ladder

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/functional_block_diagram_ad5626.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/unipolar_code_table.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/connections_ad5626.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/ad5626_bb_bb.png
   :width: 6900px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/timing_diagram.png
   :width: 900px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/vout_ad5626.png
   :width: 900px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/bipolar_output_circuit.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/ad5626_bipolar_bb.png
   :width: 900px
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/output_for_000.png
   :width: 900px
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/output_for_800.png
   :width: 900px
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/output_for_fff.png
   :width: 900px
