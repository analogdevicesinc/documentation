Activity: Photocell
===================

Objective:
----------

Photocells vary in resistance with changes in light intensity and are commonly used for detecting ambient light levels for things like street lights and automatic car headlights. In this activity you will learn how to measure ambient light and plot the light intensity on a graph.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The blue shaded rectangles indicate connections to the M1000 digital I/O connector.

The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Background:
~~~~~~~~~~~

Through Python we can acquire a number of analog values or samples from either channel A or B.

To measure an input voltage on channel first we must set the mode to high impedance:

CHA.set_mode('d') # 'D' or 'd' set channel to high impedance mode, measure voltage

Then we can acquire some number of input samples to a list ( in variable AnalogInA ):

AnalogInA = CHA.get_samples(20) # get 20 readings

It will then be possible to add the 20 values and calculate an average for example.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 - CdS Photo Cell
| 1 - 6.8 KΩ resistor

Directions:
~~~~~~~~~~~

On your solder-less breadboard connect the photo cell ( photo resistor ) and fixed resistor to the ALM1000 analog input connector as shown in figure 1. The resistance of the photo resistor changes with light level. This change in resistance along with the fixed resistor changes the voltage divider ratio.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial4_f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1, Photocell as voltage divider


Hardware Setup:
~~~~~~~~~~~~~~~

Plug the USB cable into the ALM1000.

Procedure:
~~~~~~~~~~

For this activity we can reuse the same programs we saw in the Potentiometer tutorial. Open the potentiometer_1.py Python program in your favorite editor. The IDLE that comes with Python is handy because you can run the program directly from there.

Place the photo cell under a light source. Observe changes in the measured voltage as you either move the light source or the photo cell or the shadow of your hand passes over the sensor.

Questions:
~~~~~~~~~~

What are the minimum and maximum voltages you observed? Under what conditions was the voltage at the minimum and maximum. Is there a way you could calibrate the measurements you made to standard units of light level such as Lux or Lumen

Challenges:
~~~~~~~~~~~

Modify the program to graph the voltage measured, which represents the ambient light level, vs time. By placing the light sensor near a window you will graph the changes in light as the sun moves across the window over time for example.

**For Further Reading:**

| `Photoresistor <https://en.wikipedia.org/wiki/Photoresistor>`__
| `Lux <https://en.wikipedia.org/wiki/Lux>`__

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to Python Tutorial** :doc:`Table of Contents </wiki-migration/university/tools/python-tutorial/table-of-contents>`
