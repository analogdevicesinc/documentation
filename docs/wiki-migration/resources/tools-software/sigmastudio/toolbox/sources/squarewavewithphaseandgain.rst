Square wave With Phase and Gain
===============================

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

The Square Wave block generates a square wave at a constant level and frequency. The output frequency is adjustable. Use the edit control or arrows to set the desired frequency; the checkbox control turns the signal on and off.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sourcewithgain.jpg
   :align: center
   :width: 100px

| 
| |image1|
| To change the source's Sampling Rate, Right-click in the block and select Set Sampling Rate, which will open the Sampling Rate window (default is 44.1 kHz).

GUI Control
-----------

+------------------+---------------+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range                    | Function Description                                                                                              |
+==================+===============+==========================+===================================================================================================================+
| on/off           | off           | on/off                   | Turns the output of the cell on or off. When the output is off, the output pin will output a constant value of 0. |
+------------------+---------------+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| Frequency        | 500.01        | 0.01 to 0.5\*Sample Rate | The sets the frequency of the square wave that is output from the cell.                                           |
+------------------+---------------+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| Initial Phase    | 0             | 0 to 360                 | Initial Phase of the square wave.                                                                                 |
+------------------+---------------+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| Gain             | 0             | -144 to 42 dB            | The gain to be multiplied on the square wave                                                                      |
+------------------+---------------+--------------------------+-------------------------------------------------------------------------------------------------------------------+

.. note::

   Note: The square wave is digitally generated and is **non-bandlimited**. This waveform is suitable for use as an internal control signal, but will produce aliasing distortion if used directly for audio output. If this configuration is desired, it is recommended that you apply a low-pass filter to the block's output before routing the signal to hardware outputs.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/squarewave013.jpg
