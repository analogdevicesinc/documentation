Scopy Power Supply
==================

Video
-----

.. image:: https://wiki.analog.com/_media/youtube>kohIqwrlmjI
   :alt: youtube>kohIqwrlmjI

Introduction
------------

The Power Supply instrument is the last item in the Scopy instrument menu list, by default, displayed at the far left of the Scopy window.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply1.png
   :width: 200px

The small white squares to the right of the instrument names control the run/stop functions of the instruments, allowing the user to run and stop an instrument without having to have that instrument in the current display. Clicking on the Power Supply name displays the top level of the Scopy power supply, which appears as in the following illustration.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply2.png
   :alt: powersupply2.png
   :align: center

This instruments allows you to control the voltage output of the V+ (positive output) and V- (negative output) pins of the M2K.

In the central part of the window, the values of the positive and negative outputs are shown. When each output is enabled, Scopy will continuously measure back the voltages applied on the V- and V+ pins.

For the positive output, two orange LCD numbers represent the value in Volts currently being set and the value in Volts that is measured back. For the negative output, these LCD numbers are purple.

Below the LCD numbers for each output, a scale will display in a graphical way the measured value.

Controls
--------

Tracking Ratio Control
~~~~~~~~~~~~~~~~~~~~~~

Independent Controls
^^^^^^^^^^^^^^^^^^^^

|image1| By selecting the "Independent controls" mode in the top of the right-side menu, the positive and negative outputs can be independently controlled, by setting their values on the right-side menu then clicking their corresponding Enable green button.

When enabled, the Enabled green buttons will turn into Disable red/orange buttons. Then, the corresponding output is active, until the Disable button is clicked again.

| 
| === Tracking === |image2| The "Tracking" option allows you to express the negative output (V- pin) as a function of the positive output: V- = -(ratio \* V+). For instance, for a positive output of 1.0 Volts and a tracking ratio of 70%, the negative output will be -0.7 Volts.

In this mode, the Enable button of the negative output channel is disabled; the channel is enabled and disabled dynamically at the same time as the positive channel.

| 
| ==== Positive/Negative Output Control ==== |image3| In the “Positive output” control, the output can be set from 0 to 5 V, whereas, in the Negative output control, the output can be set from -5 to 0 V. You can select units for the value, Volts or mVolts. You can either input the value directly or use the +/- control to change the voltage output value. The increment/decrement value can be changed by doing the following: The default increment/decrement value is 1 V. You can change it to 100 mV by clicking inside the circle, the small black dot should change to orange/red. |image4|

| 
| **Return to** :doc:`Scopy Main Page </wiki-migration/university/tools/m2k/scopy>`

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply3.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply4.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply5.png
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply-circle.png
