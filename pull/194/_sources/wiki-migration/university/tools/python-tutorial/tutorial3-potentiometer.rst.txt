Activity: Reading a Potentiometer, For ADALM1000
================================================

Objective:
----------

Potentiometers vary in resistance as the shaft is turned and are commonly used in things like volume controls and light dimmers. In this activity you will learn how to read an analog voltage from a potentiometer.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The blue shaded rectangles indicate connections to the M1000 digital I/O connector.

The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Background:
~~~~~~~~~~~

Through Python we can acquire a number of analog values or samples from either channel A or B.

To measure an input voltage on a channel first we must set the mode to high impedance: CHA.mode = Mode.HI_Z # set channel to high impedance mode, measure voltage

| Then we can acquire some number of input samples to a list ( in variable ADsignal1 ):
| ADsignal1 = devx.read(20, -1, True) # get 20 readings

It will then be possible to add the 20 values and calculate an average for example.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 - 5KΩ Potentiometer

Directions:
~~~~~~~~~~~

On your solderless breadboard connect the potentiometer or variable resistor to the ALM1000 analog input connector as shown in figure 1. You will connect three wires to the ALM1000 board. The first goes to ground from one of the outer pins of the potentiometer. The second goes from +5 volts to the other outer pin of the potentiometer. The third goes from analog input CA-H to the middle pin of the potentiometer.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial3_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Potentiometer as voltage divider


Hardware Setup:
~~~~~~~~~~~~~~~

Plug the USB cable into the ALM1000.

Procedure:
~~~~~~~~~~

By turning the shaft of the potentiometer, you are changing the amount of resistance on either side of the wiper or the center pin of the potentiometer. This changes how close the wiper is to 5 volts and ground, producing a different analog voltage at the CA_H input. When the shaft is turned all the way in one direction, there is 0 volts on the wiper, and we read 0 V. When the shaft is turned all the way in the other direction, there is +5 volts on the wiper and we read +5V. In between, returns a numeric string between 0 V and +5V.

Open the potentiometer_1.py Python program in your favorite editor (from this archive `potentiometers.zip <https://wiki.analog.com/_media/university/tools/python-tutorial/potentiometers.zip>`_). The IDLE that comes with Python is handy because you can run the program directly from there. Scroll down to the Analog_in() function. You will see a while loop that run as long as the "Run" button is selected. Inside the while loop we use the devx.read(20, -1, True) function to return 20 samples from the analog imputs into variable ADsignal1. The devx.read(20, -1, True) functions returns a list of values for voltage and current. We use a for loop to go through the list skipping the first 10 samples because they might not be as accurate. We copy a list entry into a temporary variable, DCVA = ADsignal1[index+10][0][0], to extract just the voltage value with, We sum the voltage values and take the average. And finally display the measured value. (For completeness the channel B voltages are in DCVB = ADsignal1[index+10][1][0])

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial3_f2.png
   :align: center
   :width: 175px

Close the potentiometer_1.py program and open the potentiometer_gauge.py program. In this program we use the same Analog_in() function but display the measured voltage in a simulated analog meter or gauge.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial3_f3.png
   :align: center
   :width: 250px

Questions:
~~~~~~~~~~

Are there any other ways you might think of to display the measured analog voltage or position of the potentiometer?

Challenge:
~~~~~~~~~~

Modify the program(s) to display both the Channel A and B inputs. Connect a second potentiometer to channel B.

**For Further Reading:**

`Potentiometer <https://en.wikipedia.org/wiki/Potentiometer>`_

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to Python Tutorial** :doc:`Table of Contents </wiki-migration/university/tools/python-tutorial/table-of-contents>`
