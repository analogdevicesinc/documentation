Activity: IC temperature sensors
================================

Objective
---------

The objective of this lab activity is to measure ambiental temperature using integrated circuit temperature transducers that provide an output (current or voltage) proportional to absolute temperature.

Temperature measuring using AD22100
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Background
----------

The AD22100 is a monolithic temperature sensor with on-chip signal conditioning. Its operating temperature range is −50°C to +150°C, making it ideal for use in numerous applications. The signal conditioning eliminates the need for any trimming, buffering, or linearization circuitry, greatly simplifying the system design and reducing the overall system cost. The output voltage is proportional to the temperature and the supply voltage and it swings from 0.25 V at −50°C to +4.75 V at +150°C using a single +5.0 V supply.

Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| AD22100 temperature sensor
| ====Hardware Setup==== For temperature measuring is necessary to connect the sensor to the power supply and the output to the oscilloscope. In Figure 2 are presented the sensor connections on a solderless breadboard. |image1|

.. container:: centeralign

   Figure 1: AD22100 temperature sensor pinout


   |image2|

.. container:: centeralign

   Figure 2: Breadboard connections for AD22100 temperature sensor


Procedure
---------

| Open Scopy and enable the positive power supply to 5V. On the channel 1 of the oscilloscope you will see the output voltage of the sensor. To obtain the value of the temperature is necessary to refer to the sensor's :adi:`datasheet <media/en/technical-documentation/data-sheets/AD22100.pdf>` to get the output voltage function.
| :math:`V_out = (V_+/(5V)) \times (1.375 V + 22.5(mV/degC) \times TA)` (1)
| From the output voltage function given by equation (1) you can extract the equation for the ambiental temperature (TA).
| :math:`TA=( V_out/(V_+/(5V)) - 1.375V ) / (22.5 (mV/degC))` (2)
| Add a new math channel to the oscilloscope where you will see the value of the temperature. Insert equation (2) in the f(t) field and set the M1 channel resolution to 10 Volts/Div. Enable the Measure feature of the oscilloscope. The Mean measurement of M1 will display the actual ambiental temperature. |image3|

.. container:: centeralign

   Figure 3: Output voltage and temperature measurements


Temperature measuring using AD592
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _background-1:

Background
----------

The AD592 is a two terminal monolithic integrated circuit temperature transducer that provides an output current proportional to absolute temperature. For a wide range of supply voltages the transducer acts as a high impedance temperature dependent current source of 1 µA/K. with a single voltage supply (4V to 30 V) the AD592 offers 0.5°C measurement accuracy on a wide operating temperature range (–25°C to +105°C).

.. _materials-1:

Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| AD592 current temperature sensor
| 1 1kΩ resistor

Hardware Setup
--------------

In figure 4 is presented the sensor pinout. As you can only measure voltage with the ADALM2000, is necessary to connect a resistor at the sensor's output and apply Ohm's law to compute the current value.


|image4|

.. container:: centeralign

   Figure 4: AD592 current temperature sensor pinout


Make the connections as shown in figure 5.



|image5|

.. container:: centeralign

   Figure 5: AD592 breadboard connections


.. _procedure-1:

Procedure
---------

| Open Scopy and enable the positive power supply to 5V. On the channel 1 of the oscilloscope you will see the voltage on the resistor. To obtain the current apply Ohm's law.
| :math:`V=I \times R` (1)
| The current through the resistor is the voltage read on channel 1 divided to it's resistance value. Because the resistor used is 1kΩ, the numeric value of the current is the same as the voltage but in micro amperes. From the sensor's :adi:`datasheet <media/en/technical-documentation/data-sheets/AD592.pdf>` we know that it's output current increases with 1 µA/K and that the output at 0 °C is 273 µA. |image6|

.. container:: centeralign

   Figure 6: Output current vs Temperature for AD592


Knowing this we can apply the formula for conversion from K to °C:
| :math:`C=K-273.15` (2)
| To display the temperature on the oscilloscope tool, add a new math channel with equation 2 as a function. Keep in mind that Channel 1 voltage is in mV and the sensor's output current is in µA. This means that if you want to obtain the temperature on the channel M1 you have to subtract 0.273 from the value read on CH1. |image7|

.. container:: centeralign

   Figure 3: Resistor voltage and temperature measurements


Questions:
----------

-  What are the differences between the operation of AD22100 voltage ouptut temperature sensor and the AD592 current output temperature sensor?

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/IC_temperature_sensors_bb`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/ad22100_pinout.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/ad22100_bb.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/ad22100_scopy.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/pinout_ad592.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/ad592_bb.png
   :width: 900px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/linearity_1d592.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/ad592_temperature_measurement.png
   :width: 900px
