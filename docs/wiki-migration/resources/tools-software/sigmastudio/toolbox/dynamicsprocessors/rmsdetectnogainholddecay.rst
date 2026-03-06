RMS (no:gain, hold, decay)
==========================

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| -----------------------------------------------------------------------------------------------------------------

|rmsnogainholdpic1.png| This block uses an rms dynamics processor that lets you control the rms TC (time constant) and Soft Knee behavior, and opens the compression curve graph for your curve drawing.

RMS works on a longer average than peak processors, thus allowing some fast loud transients to pass without compression, but operating more on longer segments that exceed the threshold.

-  Drag the block into the workspace
-  Right-click it and select the algorithm for your application:

   -  **Stereo 1 RMS (NO: gain, hold, decay)**
   -  **Stereo 1 RMS/Detect (NO: gain, hold, decay)**
   -  **Mono 1 RMS (NO: gain, hold, decay)**
   -  **Mono 1 RMS/Detect (NO: gain, hold, decay)**

-  Click Show Graph and drag, add and remove (right-click) control points to achieve your desired processing curve.

For a sample design using this block, see the :doc:`Dynamics Processor Example </wiki-migration/resources/tools-software/sigmastudio/tutorials/dynamicsprocessorexamples>`.

Controls
--------

+---+---+---+
| RMS TC (db/s) | |rmsnogainholdpic2.png| | Controls the time constant (TC) in dB/second that is used for calculating the RMS input value. The time constant determines how rapidly the compressor will respond to input signal level changes, e.g. the "Attack" time. Larger values result in faster response times.                           |
+---+---+---+
| Soft Knee     | |rmsnogainholdpic3.png| | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal. Typically it sounds better. If it is not activated, the default is hard-knee behavior, meaning compression reduces signal level immediately when the threshold is passed. |
+---+---+---+
| Show Graph    | |rmsnogainholdpic4.png| | Opens the Compression Curve editor window.                                                                                                                                                                                                                                                          |
+---+---+---+

.. |rmsnogainholdpic1.png| image:: https://wiki.analog.com/_media/rmsnogainholdpic1.png
.. |rmsnogainholdpic2.png| image:: https://wiki.analog.com/_media/rmsnogainholdpic2.png
.. |rmsnogainholdpic3.png| image:: https://wiki.analog.com/_media/rmsnogainholdpic3.png
.. |rmsnogainholdpic4.png| image:: https://wiki.analog.com/_media/rmsnogainholdpic4.png
