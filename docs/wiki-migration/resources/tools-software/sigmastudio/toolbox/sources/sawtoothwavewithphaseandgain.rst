Sawtooth With Phase and Gain
============================

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

The Sawtooth Wave block generates a sawtooth wave (or saw wave) at a constant level and frequency. The output frequency is adjustable. Use the edit control or arrows to set the desired frequency; the checkbox control turns the signal on and off.. The gain and the initial phase of the algorithm can be configured.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sourcewithgain.jpg
   :align: center
   :width: 100px

To change the source's Sampling Rate, Right-click in the block and select Set Sampling Rate, which will open the Sampling Rate window (default is 44.1 kHz).

GUI Control
-----------

+------------------+---------------+--------------------------------+-------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range                          | Function Description                                                                                              |
+==================+===============+================================+===================================================================================================================+
| on/off           | off           | on/off                         | Turns the output of the cell on or off. When the output is off, the output pin will output a constant value of 0. |
+------------------+---------------+--------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Frequency        | 500.01        | 0.01 to 0.5\*Sample Rate       | The sets the frequency of the sawtooth that is output from the cell.                                              |
+------------------+---------------+--------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Initial Phase    | 0             | 0 to 360                       | Initial Phase of the sawtooth signal.                                                                             |
+------------------+---------------+--------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Gain             | 0             | -144 to 42 dB / -134 to 24 db  | The gain to be multiplied on the sawtooth wave                                                                    |
+------------------+---------------+--------------------------------+-------------------------------------------------------------------------------------------------------------------+

Growth
------

This module can be grown to support multiple phase/gain values for a single sawtooth wave.


|image1|

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sawtooth_plot.jpg
   :align: center

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sawto.jpg
