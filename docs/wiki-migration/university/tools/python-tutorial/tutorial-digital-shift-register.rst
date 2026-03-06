Activity : Using the CD4094 Shift Register for More Digital Inputs/Outputs
==========================================================================

Objective:
----------

The goal of this tutorial is to examine how to expand the number of digital outputs in systems with as few as 3 available outputs through the use of shift registers, the serial to parallel conversion process.

Common Notes:
-------------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The blue shaded rectangles indicate connections to the M1000 digital I/O connector.

The digital I/O channel pins are referred to as D0 through D3. These correspond to the pins labeled PIO 0 - PIO 3 on the ALM1000 board silkscreen.

The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Background:
-----------

The ALM1000 has 4 digital input/output pins. If more than 4 digital inputs/outputs are needed, one solution is to use an 8-bit shift and store register such as the CD4094 integrated circuit. This chip has 8 output pins that can be set to high or low depending on the value of an 8-bit number stored in the chip's 8-bit storage register.

Importantly, this 8-bit number can be sent in serially to the chip in the form of a binary number via an 8-bit shift register and the chip converts this serial input to a parallel output. For example, if the number 197 is sent serially to the chip, LSB first, (binary 11000101) then output pins Q1, Q2, Q6, and Q8 will be set high while output pins Q3, Q4, Q5 and Q7 will be set low. A way of thinking about the serial to parallel process is that on every rising edge of the serial clock pin, the bits in the shift register shift one place to the right and the least significant bit drops off. The most significant bit is set to whatever the serial data input pin is set to. So if the number in the shift register is 01110001, with the serial input pin is set high (1), and the serial clock is toggled high, the number stored in the shift register becomes 10111000.

The chip includes a strobe pin. Data from each stage of the shift register is latched on a negative transition of the strobe input. The output data latch is transparent when strobe is high. By holding the strobe pin low we can change the shift register and hide the changes until we are finished, making it appear like we have individual control over all of the outputs. After new data has been shifted in we bring the strobe pin high to transfer the contents of the shift register to the eight parallel output pins.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| CD4094 8 bit shift and store CMOS logic device
| 8 LEDs
| 8 100 Ω resistors

Directions:
~~~~~~~~~~~

Below is the pinout diagram for the CD4094 IC. Notice that pin OUTPUT ENABLE must be connected to V\ :sub:`DD` (3.3 V) for normal operation.

**CD4094 Pinout Diagram:**

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial-sreg_f1.png
   :align: center
   :width: 300px

| Q1-Q8 - Output Pins
| V\ :sub:`DD` - 3.3 V
| V\ :sub:`SS` - 0 V
| STROBE - storage register clock pin
| CLOCK - shift register clock pin
| OUTPUT ENABLE - enables outputs if set high (must be connected to 5 V for normal operation)
| DATA - serial data input pin
| QS, Q'S - allows more than one chip to be daisy-chained together by sending the least significant bit to another CD4094's DATA pin allowing for the effective creation of 16-bit (2 chips), 24-bit (3 chips), or larger shift and store registers.

It is a fairly simple matter to connect the shift register to three of the general purpose digital I/O pins on the ALM1000. We can use PIO 0 for the CLOCK input, PIO 1 for the serial DATA input and PIO 2 for the STROBE input. Using Python we can step through the necessary sequence to serially shift an 8 bit number into the register and then set the STROBE bit high transferring the data in the register to the output pins.

Use the CD4094 to Light Up LEDs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Insert a CD4094 shift register in your solder-less breadboard. Connect the chip V\ :sub:`DD` to power (3.3V) and V\ :sub:`SS` to ground. Connect LEDs to output pins Q1 to Q8 (don't forget to use current limiting resistors). Connect OUTPUT ENABLE to 3.3 V (high). Connect the CLOCK, DATA and STROBE pins to PIO 0,1,2 on the ALM1000 digital connector as shown in figure 1. Note that all the LED cathodes are tied to ground.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial-sreg_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 8 bit shift register connections


Hardware Setup:
~~~~~~~~~~~~~~~

Plug the USB cable into the ALM1000.

Procedure:
~~~~~~~~~~

Open the shift_register.py Python program in your favorite editor. The IDLE that comes with Python is handy because you can run the program directly from there. Scroll down to the ShiftOut() function. The first thing the function does is convert the number into an eight character string of 1's and 0's representing the number in binary form. The while loop generates a series of eight low to high to low pulses on the CLOCK output while setting the DATA output to high or low based on the character in the binary string. At the end the STROBE output is set high and then back low to transfer the newly shifted data to the output pins on the CD4094.

Use the CD4094 to Control a Seven-Segment LED Display
-----------------------------------------------------

.. _objective-1:

Objective:
~~~~~~~~~~

Use a 7-Segment LED (Light Emitting Diode) display to output a numeric integer (and a few letters as well) using the digital outputs on your ALM1000 module. Many digital systems use seven segment displays for displaying digital values in a form that can be understood by the user. This information is often numerical data in the form of numbers, characters and symbols. Seven-segment displays produce the required number or symbol by illuminating the individual segments in various combinations.

.. _background-1:

Background:
~~~~~~~~~~~

The 7-Segment LED is an extension of the basic LED that uses 8 pins to control, 7 segments and 1 decimal point. 7-Segment displays are used in many electronic devices such as home appliances like microwaves, alarm clocks, and many other numeric display applications such as laboratory instruments. It is important to note that a 7-Segment LED behaves exactly the same as a basic single LED, which is a diode that only allows current to flow in one direction and we will need to limit the current by connecting a resistor in series. 7-segment displays come in two connection configurations, common anode and common cathode. As the names imply, in each case either all the LED cathodes or all the LED anodes share a common connection in the package. Common cathode means that the negative side of all the LEDs are connected together. Common anode means that the positive side of all the LEDs are connected together.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial-sreg_f3.png
   :align: center
   :width: 150px

.. container:: centeralign

   Figure 2 Typical 7 segment LED display


Each of the 7 segments is identified by a letter as can be seen in figure 3 as well as the pinout and schematic for reference.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial-sreg_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, schematic and example pinout


.. _materials-1:

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 7 - 100Ω Resistors
| 1 - 7 segment display

.. _directions-1:

Directions:
~~~~~~~~~~~

As stated in the datasheet for most displays each LED segment can handle a typical current up to 20 mA, and is recommended to be used with 16 to 18 mA; so at 15.15 mA we will be safe. Starting with the circuit connections from figure 1, substitute the individual LEDs for the segments in your display. This will be simple if your 7 segment display is a common cathode type. Be sure to make any changes if your 7 segment display is a common anode type i.e. move the common anode to the 3.3 V supply.

.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Plug the USB cable into the ALM1000.

.. _procedure-1:

Procedure:
~~~~~~~~~~

======= == == == == == == == ==
Segment A  B  C  D  E  F  G  DP
======= == == == == == == == ==
Output  Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8
0       X  X  X  X  X  X     
1          X  X              
2       X  X     X  X     X  
3       X  X  X  X        X  
4          X  X        X  X  
5       X     X  X     X  X  
6       X     X  X  X  X  X  
7       X  X  X              
8       X  X  X  X  X  X  X  
9       X  X  X  X     X  X  
======= == == == == == == == ==

Table 1 segment configurations for decimal numbers

Questions:
~~~~~~~~~~

In addition to the 10 decimal numbers what letters of the alphabet can you form using the seven segments?

Extra Credit Assignment:
~~~~~~~~~~~~~~~~~~~~~~~~

Use two CD4094 shift registers, two 7-segment displays, and modify the ShiftOut() function to make a circuit and program that counts from zero to 99 then repeats. Use the time.sleep() function to configure the program to take about one second per count.

To accomplish this the two shift registers must be daisy chained together.

**For Further Reading:**

| https://en.wikipedia.org/wiki/Shift_register
| http://en.wikipedia.org/wiki/Seven-segment_display

Where to get a 7 segment display:

| http://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_24782\_-1
| https://www.sparkfun.com/products/8546

**Return to Python Tutorial** :doc:`Table of Contents </wiki-migration/university/tools/python-tutorial/table-of-contents>`\ **.**
