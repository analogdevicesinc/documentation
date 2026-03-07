Beep
====

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| This block uses an internal oscillator to generate tones. Set the frequency in the text field or using the arrows. Click click Beep button to enable the tone generation. This source is only active while the beep button is pressed. | |image2| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

| 
| You can add algorithms to the Beep blocks after the default has been established (if you're using more than one DSP processor, you'll need to add the initial default algorithm for the desired IC). Right-click the block to select Add Algorithm > IC # > Beep variable gain and add another output pin.
| To change the source's Sampling Rate, Right-click in the block and select Set Sampling Rate, which will open the Sampling Rate window (default is 44.1 kHz).

Usage
-----

| For most applications we recommend using Tone (Lookup/Sine) instead of Beep. The Beep block output level is inconsistent, the oscillator tends toward instability above 6-7 kHz and, most importantly, the output is never limited. This means that in certain circumstances downstream audio circuits can be overdriven (e.g., 12kHz beep combined with input audio to a mixer module). If you do use the Beep algorithm, be sure to add a limiter (see the Dynamics Processors topics).
| Beep is most valuable for schematic testing as it produces less THD than the Tone (lookup/sine) block.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/beep032.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/beep032.jpg
