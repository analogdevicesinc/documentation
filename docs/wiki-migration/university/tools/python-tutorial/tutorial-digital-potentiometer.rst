Activity: Digital Potentiometers
================================

Objective:
----------

Potentiometers vary in resistance as the shaft is turned and are commonly used in things like volume controls and light dimmers. In a digitally controlled potentiometer the mechanical wiper is replaced with a set of analog switches. A digital number is used to select the tap point along the resister. In this activity you will learn how to control a digital potentiometer though a serial data port.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The blue shaded rectangles indicate connections to the ALM1000 digital I/O connector.

The digital I/O channel pins are referred to as D0 through D3. These correspond to the pins labeled PIO 0 - PIO 3 on the ALM1000 board silkscreen.

The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Background:
-----------

In this tutorial we will be using the AD8402 dual digital potentiometer in the 14 pin DIP package. It contains two 10 KΩ resistor strings with 256 tap points that can be digitally selected through a 3 wire serial data port. The pin out is shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial-dig-pot_f1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1, AD8402 dual digital potentiometer


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 - AD8042 10 KΩ dual digital potentiometer (14 pin DIP package)

Directions:
~~~~~~~~~~~

On your solderless breadboard connect the AD8042 digital variable resistor to the ALM1000 analog input connector and digital output connector as shown in figure 2. Refer to figure 1 for the pin numbers on the AD8042 14 pin DIP package.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial-dig-pot_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Potentiometer as programmable voltage divider


Hardware Setup:
~~~~~~~~~~~~~~~

After carefully checking the connections, plug the USB cable into the ALM1000.

Procedure:
~~~~~~~~~~

By changing the digital setting of the potentiometer, you are changing the amount of resistance on either side of the wiper or the W pin of the potentiometer. This changes how close the wiper is to 5 volts (A pin) or ground (B pin), producing a different analog voltage at the CA_H and CB_H inputs. When the all the way in one direction, there is 0 volts on the wiper, and we read 0 V. When the all the way in the other direction, there is +5 volts on the wiper and we read +5V. In between, returns a value between 0 V and +5V.

Open the ad8402_dual_pot.py Python program in your favorite editor. The IDLE that comes with Python is handy because you can run the program directly from there. Scroll down to the Send() function. This function gets the two 8 bit numbers entered and calls the ShiftOut() function twice. The first time sends the value for Pot1 and the second time sends the value for Pot2 plus 256 which tells the AD8402 which register gets the data.

The ShiftOut() function converts the integer number into a string of binary (0,1) characters and extends the string to 10 digits. It set the CS pin low. It then loops through the string toggling the serial clock and serial data pins to shift the data into the AD8402. Finally, it sets the CS pin high to transfer the new data to the Pot.

Scroll down to the Analog_in() function. You will see a while loop that run as long as the "Run" button is selected. Inside the while loop we first use the send() function to set the two digital potentiometers based on the number ( 0 to 255 ) in the two Entry widgets. The .get_samples() function is then used to return 20 samples from channel A into variable ADsignal1. The get_samples() functions returns a list of values for voltage [0] and current [1]. We use a for loop to go through the list skipping the first 10 samples because they might not be as accurate. We copy a list entry into a temporary variable, SPA = ADsignal1[index+10][0], to extract just the voltage value with, VAdata = float(SPA). We sum the voltage values and take the average. And finally display the measured value. This same process is then repeated for Channel B.

Run the program and make note of the measured voltages as you change the number entered for each pot.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial-dig-pot_f3.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 3 ad8402 dual pot controller


Close the ad8402_dual_pot.py program and open the ad8402_dual_slider.py program. This program is essentially the same as the previous program except the Entry widgets have been replaced with slider widgets to set the digital values for the pot.

Run the program and make note of the measured voltages as you slide the controls back and forth for each pot.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial-dig-pot_f4.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 4 ad8402 dual pot slider controller


Questions:
~~~~~~~~~~

What happens if you swap the A and B connections of the resistors?

Challenge:
----------

As a challenge build a variable frequency square wave generator with programmable pulse width (PWM) based on the NE555 timer chip and the AD8402.

.. _materials-1:

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 - AD8042 10 KΩ dual digital potentiometer (14 pin DIP package)
| 1 - NE555 Timer (8 pin DIP)
| 2 - 0.1 uF capacitors (104)
| 2 - 220 Ω resistors
| 2 - 1N914 small signal diodes

.. _directions-1:

Directions:
~~~~~~~~~~~

Before making any additions to your breadboard circuit it is probably best to un-plug the ALM1000 from the USB cable. Starting with the circuit from figure 2 on your solderless breadboard remove the connections from the A1, B1, W1 and A2, B2, W2 pins on the AD8402. Add the 555 timer circuit as shown in figure 5 and connect the A1, B1, W1 and A2, B2, W2 pins as indicated by the blue arrows.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial-dig-pot_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, 555 timer PWM circuit


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

After carefully checking the connections, plug the USB cable into the ALM1000.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Use the alice-1.0-plugins.pyw oscilloscope program with the ad8402_slider_plugin.py program. Set ALICE to observe the voltages on the 555 timer output at pin 3 and the timing capacitor on pins 2,6. Adjust the value of the Pot2 slider to produce the highest output frequency. Now slide the Pot 1 slider back and forth observing the output pulse width or duty-cycle. What is the minimum and maximum pulse width ( range of the duty-cycle )?

Change the setting of Pot2 to lower the output frequency. How has this effected the range of possible pulse widths and why?

Also explain the charging and discharging waveform on C\ :sub:`2` as the setting of Pot1 is changed.

**For Further Reading:**

| http://www.analog.com/media/en/technical-documentation/data-sheets/AD8400_8402_8403.pdf
| https://en.wikipedia.org/wiki/555_timer_IC

**Return to Python Tutorial** :doc:`Table of Contents </wiki-migration/university/tools/python-tutorial/table-of-contents>`
