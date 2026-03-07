Loudness (Lower End)
====================

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`
| The Loudness (Lower End) algorithm raises the amplitude of bass frequencies for low volume levels. The Gain values are derived from the Fletcher- Munson equal loudness curve. Note: Only the low frequency end of the Fletcher Munson curves are used for this algorithm. These sets of curves reveal that at low levels, lower frequencies need to be boosted relative to higher frequencies, in order to have the same apparent loudness to the human ear. It is also important to note that this algorithm is not dynamic and assumes that the input level is constant.
| |loudnesslowpic1.png|
| There are two default algorithms that can be used with this block:

-  **LF Loudness** (figure: top right)
-  **LF Loudness Control w/ 2 bypassed outputs** (figure: bottom right)

They both function the same, except the latter algorithm contains another pair of stereo outputs that allow the signal to pass through unaffected by the low-end loudness boost, but it will be affected by the overall volume level slider. The figure in the bottom right shows the two extra output pins below the standard output pins used for the bypassed connection.

| The parameters available for control on this block include the volume slider, LP Frequency, and Level.
| |loudnesslowpic2.png|

| 1) The volume slider controls the output gain of the entire signal and is also the control factor for the loudness algorithm. At low levels, the loudness algorithm needs to boost the low frequencies more than at higher frequencies. Note that at 0dB despite what the Level for the loudness algorithm may be, there will be no additional low-frequency boost.
| |loudnesslowpic3.png|

| 2) The LP Frequency control knob allows you to edit the cutoff frequency of the low-pass filter. The default value of 10 Hz approximates the Fletcher-Munson curve. Increased frequency values will provide greater bass frequency bandwidth gain.
| |loudnesslowpic4.png|

| 3) The Level edit box allows you to control the bass frequency boost. The higher value entered, the larger bass frequency gain there will be. The value for level is correlated with the volume slider value because the amount of boost id dependant on the signal level.
| |loudnesslowpic5.png|
| |loudnesslowpic6.png|

.. |loudnesslowpic1.png| image:: https://wiki.analog.com/_media/loudnesslowpic1.png
.. |loudnesslowpic2.png| image:: https://wiki.analog.com/_media/loudnesslowpic2.png
.. |loudnesslowpic3.png| image:: https://wiki.analog.com/_media/loudnesslowpic3.png
.. |loudnesslowpic4.png| image:: https://wiki.analog.com/_media/loudnesslowpic4.png
.. |loudnesslowpic5.png| image:: https://wiki.analog.com/_media/loudnesslowpic5.png
.. |loudnesslowpic6.png| image:: https://wiki.analog.com/_media/loudnesslowpic6.png
