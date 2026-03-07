=======High Resolution RMS======

| :doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| ----------------------------------------------------------------------------------------------------------------

|highrespic1.png| This block uses a high-resolution rms dynamics processor that lets you control the rms TC (time constant), Hold, Decay, and Soft Knee behavior, and displays the compression curve graph for your curve drawing.

Hi-Resolution RMS works on a longer average than peak processors, but, like them, it still won't allow fast loud transients to pass without compression.

Push Show Graph to open the Compression Curve window and drag, add and remove (right-click) control points to achieve your desired processing curve.

Controls
========

+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RMS TC (db/s) | |highrespic2.png| | Controls the time constant (TC) in dB/second that is used for calculating the RMS input value. The time constant determines how rapidly the compressor will respond to input signal level changes, e.g. the "Attack" time.                                                                          |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)     | |highrespic3.png| | Controls the time (in ms) the compressor maintains its current output  gain setting before it starts decreasing as the input level decrease.                                                                                                                                                        |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (db/s)  | |highrespic4.png| | Controls the rate at which the compressor gain decreases in response to decrease in the input signal level, e.g. the "Release" time.                                                                                                                                                                |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Soft Knee     | |highrespic5.png| | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal. Typically it sounds better. If it is not activated, the default is hard-knee behavior, meaning compression reduces signal level immediately when the threshold is passed. |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show Graph    | |highrespic6.png| | Opens the Compression Curve editor window.                                                                                                                                                                                                                                                          |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Shown below are the curves of the Hi-Resolution RMS dynamics processor (right) and the regular RMS processor (left). The number of data points in this block is double that in the ordinary one (66 instead of 33).
| |highrespic7.png|

.. |highrespic1.png| image:: https://wiki.analog.com/_media/highrespic1.png
.. |highrespic2.png| image:: https://wiki.analog.com/_media/highrespic2.png
.. |highrespic3.png| image:: https://wiki.analog.com/_media/highrespic3.png
.. |highrespic4.png| image:: https://wiki.analog.com/_media/highrespic4.png
.. |highrespic5.png| image:: https://wiki.analog.com/_media/highrespic5.png
.. |highrespic6.png| image:: https://wiki.analog.com/_media/highrespic6.png
.. |highrespic7.png| image:: https://wiki.analog.com/_media/highrespic7.png
