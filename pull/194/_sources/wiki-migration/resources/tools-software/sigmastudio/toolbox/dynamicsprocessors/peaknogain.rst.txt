Peak (No Gain)
==============

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| ----------------------------------------------------------------------------------------------------------------

|peaknogainpic1.png| This block functions exactly like the :doc:`Peak(gain) </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/peakgain>` block (see that topic for details) but does not include the Post Gain knob.

| 
| ===Controls===

+--------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)    | |peaknogainpic2.png| | Controls the time (in ms) the compressor maintains its current output gain setting after the input level decreases, before the gain starts increasing back to normal.                                                                                                                               |
+--------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (db/s) | |peaknogainpic3.png| | Controls the rate at which the compressor gain increases back to normal in response to decrease in the input signal level, e.g. the "Release" time. Larger values result in faster recoveries.                                                                                                      |
+--------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Soft Knee    | |peaknogainpic4.png| | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal. Typically it sounds better. If it is not activated, the default is hard-knee behavior, meaning compression reduces signal level immediately when the threshold is passed. |
+--------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show Graph   | |peaknogainpic5.png| | Opens the Compression Curve editor window.                                                                                                                                                                                                                                                          |
+--------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |peaknogainpic1.png| image:: https://wiki.analog.com/_media/peaknogainpic1.png
.. |peaknogainpic2.png| image:: https://wiki.analog.com/_media/peaknogainpic2.png
.. |peaknogainpic3.png| image:: https://wiki.analog.com/_media/peaknogainpic3.png
.. |peaknogainpic4.png| image:: https://wiki.analog.com/_media/peaknogainpic4.png
.. |peaknogainpic5.png| image:: https://wiki.analog.com/_media/peaknogainpic5.png
