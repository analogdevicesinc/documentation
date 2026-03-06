Multiple Volume Control
=======================

:doc:`Click here to return to the Volume Controls section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/volumecontrols>`

+---+---+
| The Multiple Volume Control permits gain adjustments to be made to each of the inputs individually. Every input pin has its own volume control. | |multiplevolumecontrol1.jpg| |
+---+---+

Algorithms:

-  Gain (no slew) - The "no slew" algorithm performs gain changes immediately with no transition (ramping), this algorithm requires much lower program and memory resources than the slew algorithms, but it can result in discontinuities (clicks and pops) when making volume changes in real time.
-  Gain (slew) - The AD1940 / 1941 includes support for volume controls that use a target/slew RAM hardware to slew (smoothly transition) from one volume level value to a another. For the Multiple Volume Control block, the slew curve is a linear-ramp with fixed time constant of 8.

| 
| By default the block's algorithm has one input and one output. To add additional channels (input, output, & slider) Right-click the block and select Add Algorithm from the menu.
| The Slider control's min/max value and step size can be customized. To modify the slider's settings, right-click on the control which will display the control pop-up window (shown below).

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/multiplevolumecontrol2.jpg
   :alt: multiplevolumecontrol2.jpg

.. |multiplevolumecontrol1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/multiplevolumecontrol1.jpg
