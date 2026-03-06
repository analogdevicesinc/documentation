Square Wave
===========

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

+---+---+
| The Square Wave block generates a square wave at a constant level and frequency. The output frequency is adjustable. Use the edit control or arrows to set the desired frequency; the checkbox control turns the signal on and off. | |image2| |
+---+---+

| 
| |image3|
| To change the source's Sampling Rate, Right-click in the block and select Set Sampling Rate, which will open the Sampling Rate window (default is 44.1 kHz).

.. note::

   Note: The square wave is digitally generated and is **non-bandlimited**. This waveform is suitable for use as an internal control signal, but will produce aliasing distortion if used directly for audio output. If this configuration is desired, it is recommended that you apply a low-pass filter to the block's output before routing the signal to hardware outputs.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/squarewave012.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/squarewave012.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/squarewave013.jpg
