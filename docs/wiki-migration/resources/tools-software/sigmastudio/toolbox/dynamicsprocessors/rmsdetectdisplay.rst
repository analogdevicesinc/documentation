RMS (Display)
=============

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| ---------------------------------------------------------------------------------------------------------------

|rmsdisplaypic1.png| This block functions exactly like :doc:`RMS (gain) </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/rmsgain>` with the Stereo 1 RMS algorithm, except that it comes with a signal level display.

| The left bar shows the input level and the right bar the compression ratio. The On button toggles the level display on and off.
| For a sample design using this block, see the :doc:`Dynamics Processor Example </wiki-migration/resources/tools-software/sigmastudio/tutorials/dynamicsprocessorexamples>`.

Controls
--------

+---------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Post Gain     | |rmsdisplaypic2.png| | Post-processing gain, for increasing the overall signal level following dynamics processing.                                                                                                                                                                                                        |
+---------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RMS TC (db/s) | |rmsdisplaypic3.png| | Controls the time constant (TC) in dB/second that is used for calculating the RMS input value. The time constant determines how rapidly the compressor will respond to input signal level changes, e.g. the "Attack" time.                                                                          |
+---------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)     | |rmsdisplaypic4.png| | Controls the time (in ms) the compressor maintains its current output  gain setting before it starts decreasing as the input level decrease.                                                                                                                                                        |
+---------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (db/s)  | |rmsdisplaypic5.png| | Controls the rate at which the compressor gain decreases in response to decrease in the input signal level, e.g. the "Release" time.                                                                                                                                                                |
+---------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Soft Knee     | |rmsdisplaypic6.png| | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal. Typically it sounds better. If it is not activated, the default is hard-knee behavior, meaning compression reduces signal level immediately when the threshold is passed. |
+---------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show Graph    | |rmsdisplaypic7.png| | Opens the Compression Curve editor window.                                                                                                                                                                                                                                                          |
+---------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |rmsdisplaypic1.png| image:: https://wiki.analog.com/_media/rmsdisplaypic1.png
.. |rmsdisplaypic2.png| image:: https://wiki.analog.com/_media/rmsdisplaypic2.png
.. |rmsdisplaypic3.png| image:: https://wiki.analog.com/_media/rmsdisplaypic3.png
.. |rmsdisplaypic4.png| image:: https://wiki.analog.com/_media/rmsdisplaypic4.png
.. |rmsdisplaypic5.png| image:: https://wiki.analog.com/_media/rmsdisplaypic5.png
.. |rmsdisplaypic6.png| image:: https://wiki.analog.com/_media/rmsdisplaypic6.png
.. |rmsdisplaypic7.png| image:: https://wiki.analog.com/_media/rmsdisplaypic7.png
