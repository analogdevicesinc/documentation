Activity: 2-axis tilt sensor
============================

Objective
---------

The objective of this activity is to build a simple tilt sensor using ADXL327 and observe how the output voltage varies with inclination on X and Y axes.

Tilt sensor using ADXL327
~~~~~~~~~~~~~~~~~~~~~~~~~

Background
----------

A tilt sensor is used for measuring the tilt in multiple axes of a reference plane. They produce an electric signal which is proportional to the degree of inclination with respect to the axes. The tilting position is measured with reference to gravity and enables the easy detection of orientation or inclination.

In this activity we will monitor the tilt in 2 axis, X and Y, using the ADXL327 accelerometer. The functional block diagram of this integrated circuit is presented in Figure 1.


|image1|

.. container:: centeralign

   Figure 1. Functional block diagram of ADXL327


The ADXL327 is a small, low power, complete 3-axis accelerometer with signal conditioned voltage outputs. It can measure the static acceleration of gravity in tilt-sensing applications, as well as dynamic acceleration, resulting from motion, shock, or vibration. The output signals are analog voltages that are proportional to acceleration. The ADXL327 uses a single structure for sensing the X, Y, and Z axes. As a result, the three axes sense directions are highly orthogonal with little cross-axis sensitivity.



|image2|

.. container:: centeralign

   Figure 2. Axes of acceleration sensitivity


Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 ADXL327 accelerometer
| 2 0.047 uF capacitors
| 1 0.1 uF capacitor
| 2 AD8561 comparators
| 4 LEDs
| 4 100 Ω resistors

Hardware setup
--------------

Start with building on the solderless breadboard the circuit presented in the block diagram from Figure 1. C\ :sub:`DC` capacitor placed close to the ADXL327 supply pins adequately decouples the accelerometer from noise on the power supply. For most applications is suitable a single 0.1 μF capacitor. On X\ :sub:`OUT`, Y\ :sub:`OUT` pins capacitors must be added to implement low-pass filtering for antialiasing and noise reduction. Refer to the datasheet of ADXL327 to see how to choose the values of these capacitors. For this application 0.047uF capacitors can be used. In figure 3 are presented the breadboard conections.


|image3|

.. container:: centeralign

   Figure 3. ADXL327 tilt sensor breadboard connections


Procedure
---------

Turn on the positive power supply at 3V and monitor X\ :sub:`OUT` on channel 1 of the oscilloscope and Y\ :sub:`OUT` on the channel 2. The zero g bias output is nominally equal to VS/2 at all supply voltages. In this case you should see an offset signal at around 1.5V. If you tilt the breadboard at different angles on X or Y axes, the output voltage will increase or decrease proportionally.


|image4|

.. container:: centeralign

   Figure 4. Zero g bias output


Tilt sensor with LED indicators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _background-1:

Background
----------

We monitored the output voltage of the ADXL327 accelerometer on the oscilloscope but using AD8561 comparators and LEDs is possible to make the tilt sensor send light signals when the the degree of inclination changes or when a vibration is sensed. We use one AD8561 comparator for each axis. The zero g bias output is similar on both axes and will be the reference of both comparators. On each of the two outputs of the comparator a LED will be connected. The two output signals are opposite so only one LED will be active at a time.

.. _hardware-setup-1:

Hardware setup
--------------

On the solderless breadboard you will add two comparators and two LEDs ( with the corresponding current limiting resistor) for each. In Figure 5 you can see the circuit schematic and the breadboard connections are shown in Figure 6.


|image5|

.. container:: centeralign

   Figure 5. Circuit schematic of tilt sensor with LEDs


   |image6|

.. container:: centeralign

   Figure 6. Breadboard connections for tilt sensor with LEDs


.. _procedure-1:

Procedure
---------

In this case we need the power supplies V+ and V- set at +-5 V for the two comparators. The signal generator channel 1 W1 will be set to a constant 3 V waveform and used as Vs for the ADXL327. The second channel of the signal generator W2 will be the reference input of the comparators. Its value must be set approximately equal with the zero g output bias previously obtained for the two accelerometer outputs (Figure 4). In this way, everytime a change of tilting degree is sensed and the voltage varies, the comparators outputs will change their state, turning the LEDs on accordingly. Since the oscilloscope has only two channels available we can analyze one output voltage of the accelerometer at a time, but the LEDs will be on and signal the changes in both X and Y axes. On Channel 1 is connected Xout and on channel 2 is connected the reference voltage generated with W2.


|image7|

.. container:: centeralign

   Figure 7. Zero g bias Xout and reference


If you tilt the breadboard to the right on X axis, the input voltage of the comparator will go below the reference voltage so the /OUT pin will be high turning the corresponding LED on.



|image8|

.. container:: centeralign

   Figure 8. X axis right tilt corresponding voltage


If the tilt is in the opposite direction, to the left, the input voltage of the comparator is higher than the reference turning high the OUT pin and the LED connected to it.



|image9|

.. container:: centeralign

   Figure 9. X axis left tilt corresponding voltage


Questions
---------

• How will C\ :sub:`DC` influence the circuit if its value is changed?

• Why should the user limit the bandwidth and what are the criteria for band limiting Xout, Yout, Zout?

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/tilt_sensor_bb`
   


Further Readings
~~~~~~~~~~~~~~~~

Some additional resources:

-  :adi:`ADXL327 Datasheet <media/en/technical-documentation/data-sheets/ADXL327.pdf>`
-  :adi:`AD8561 Datasheet <media/en/technical-documentation/data-sheets/AD8561.pdf>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/labs/functional_diagram_adxl327.png
   :width: 550px
.. |image2| image:: https://wiki.analog.com/_media/university/labs/axes_adxl327.png
   :width: 350px
.. |image3| image:: https://wiki.analog.com/_media/university/labs/tilt_sensor_adxl327_bb.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/labs/output_adxl327.png
   :width: 900px
.. |image5| image:: https://wiki.analog.com/_media/university/labs/adxl_accelerometer.png
   :width: 900px
.. |image6| image:: https://wiki.analog.com/_media/university/labs/tilt_sensor_led_bb.png
   :width: 900px
.. |image7| image:: https://wiki.analog.com/_media/university/labs/zerog_bias_xout_and_reference.png
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/university/labs/xaxis_right_tilt.png
   :width: 800px
.. |image9| image:: https://wiki.analog.com/_media/university/labs/xaxis_left_tilt.png
   :width: 800px
