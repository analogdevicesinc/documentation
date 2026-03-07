Midnight Mode
=============

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`
| Our Midnight Mode block is a dynamic-processing algorithm designed primarily for handling explosive movie soundtracks or similar material (video games, e.g.) to make them less obtrusive. A typical example would be quiet night-time environments where loud transients and similar sounds would disturb people (not to mention sleeping children and babies) in a room adjacent to or near the home theater or gaming area.

| With Midnight Mode, high-level passages are attenuated and very quiet levels are readily raised into audibility, while dialog remains unchanged and intelligible. This permits higher overall levels with better clarity for the intended active listeners, with much less chance of disturbing nearby non-listeners.
| |midnightpic1.png|

*Notes*

-  This compressor block defaults to a bypassed state. Click the toggle switch to enable Midnight Mode.
-  The Input slider works as a volume control, changing the level into the Midnight Mode algorithm. If the block is bypassed, the slider is throughput volume control.
-  The Output slider adjusts the output level post-compressor.

*How It Works*

Source material with a very wide dynamic range -- the "distance" from the very quietest to the very loudest levels -- must have its dynamics reduced for comfortable domestic playback, especially at night or similar times when high movie (or music) levels are inappropriate and undesirable. If the source material has a dynamic range of 60dB, say, the output dynamic range will be compressed to more comfortable 40dB.

| The processing is centered on a nominal source level. Signals louder than this normal-level transition point get reduced in level, or made quieter, and the signals below this point get boosted in level, made louder. Refer to the figure below, which shows, along the horizontal axis, the input range from -10 (20 above the nominal -30dB input) to 20 below it (= -50dB) — with the compressor action demonstrated by the vertical axis, which shows outputs at -28, -40, and -50dB levels.
| |midnightpic2.png|

*Gating*

| Now, very quiet sound is treated differently; see the figure below. The block is able to avoid such side effects as can occur with advanced compression, like modulation of the noise floor by very loud signals. The oval portion shows a noise gate (a downward expander), a function that sharply reduces low-level hum and other noise.
| |midnightpic3.png|
| *Gain structure*

| The enabled input slider works as a volume control, changing the input gain to the Midnight Mode processing, and moves the point where the nominal signal lands on the curve, up or down. The output slider moves the entire curve up or down.
| |midnightpic4.png|

*Recommendation*

-  Input set to -6dB
-  Output set to +14dB

| Below is a figure showing a clip from a movie soundtrack, with Midnight Mode bypassed (top) and enabled (bottom). Notice not only the control of the FX scene but the unchanged processing (volume) of the low-level voice signal.
| |midnightpic5.png|

.. |midnightpic1.png| image:: https://wiki.analog.com/_media/midnightpic1.png
.. |midnightpic2.png| image:: https://wiki.analog.com/_media/midnightpic2.png
.. |midnightpic3.png| image:: https://wiki.analog.com/_media/midnightpic3.png
.. |midnightpic4.png| image:: https://wiki.analog.com/_media/midnightpic4.png
.. |midnightpic5.png| image:: https://wiki.analog.com/_media/midnightpic5.png
