RMS (gain)
==========

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| ---------------------------------------------------------------------------------------------------------------

|rmsgainpic1.png| This block uses an rms dynamics processor that lets you control the rms TC (time constant), Hold, Decay, and Soft Knee behavior, and opens the compression curve graph for your curve drawing.

RMS works on a longer average than peak processors, thus allowing some fast loud transients to pass without compression, but operating more on longer segments that exceed the threshold.

-  Drag the block into the workspace
-  Right-click it and select the algorithm for your application:

   -  **Mono RMS Ext. Detect (Post Gain)**
   -  **Mono RMS (Post Gain)**
   -  **Stereo RMS Ext. Detect (Post Gain)**
   -  **Stereo RMS (Post Gain)**

-  Set these parameters to fit your application and click Show Graph and drag, add and remove (right-click) control points to achieve your desired processing curve.


| 
|

.. hint::

   Note: For the picture above, the block was chosen to include the /Detect algorithm, shown by the red pin. For this compressor to be active, signal has to be connected to it.


Controls
--------

+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Post Gain     | |rmsgainpic2.png| | Post-processing gain, for increasing the overall signal level following dynamics processing.                                                                                                                                                                                                        |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RMS TC (db/s) | |rmsgainpic3.png| | Controls the time constant (TC) in dB/second that is used for calculating the RMS input value. The time constant determines how rapidly the compressor will respond to input signal level changes, e.g. the "Attack" time.                                                                          |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)     | |rmsgainpic4.png| | Controls the time (in ms) the compressor maintains its current output  gain setting before it starts decreasing as the input level decrease.                                                                                                                                                        |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (db/s)  | |rmsgainpic5.png| | Controls the rate at which the compressor gain decreases in response to decrease in the input signal level, e.g. the "Release" time.                                                                                                                                                                |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Soft Knee     | |rmsgainpic6.png| | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal. Typically it sounds better. If it is not activated, the default is hard-knee behavior, meaning compression reduces signal level immediately when the threshold is passed. |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show Graph    | |rmsgainpic7.png| | Opens the Compression Curve editor window.                                                                                                                                                                                                                                                          |
+---------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |rmsgainpic1.png| image:: https://wiki.analog.com/_media/rmsgainpic1.png
.. |rmsgainpic2.png| image:: https://wiki.analog.com/_media/rmsgainpic2.png
.. |rmsgainpic3.png| image:: https://wiki.analog.com/_media/rmsgainpic3.png
.. |rmsgainpic4.png| image:: https://wiki.analog.com/_media/rmsgainpic4.png
.. |rmsgainpic5.png| image:: https://wiki.analog.com/_media/rmsgainpic5.png
.. |rmsgainpic6.png| image:: https://wiki.analog.com/_media/rmsgainpic6.png
.. |rmsgainpic7.png| image:: https://wiki.analog.com/_media/rmsgainpic7.png
