RMS (no gain)
=============

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| ---------------------------------------------------------------------------------------------------------------

.. image:: https://wiki.analog.com/_media/rmsnopic1.png
   :alt: rmsnopic1.png
   :align: right

--------------

This block functions exactly like :doc:`RMS (gain) </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/rmsgain>` but does not include the knob for post gain.

For the block picture at right, the Mono Algorithm was chosen, meaning there is only one set of input/output pins.

| Push **Show Graph** to open the Compression Curve window. Right-click along the curve to add or remove control points according to your needs.
| |rmsnopic2.png|
| This block uses an rms dynamics processor that can control the rms TC (time constant), Hold, Decay, and Soft Knee behavior, and also lets you open the compression curve graph for your curve creation.

RMS works on a longer average than peak processors, thus allowing some fast loud transients to pass without compression, operating more on longer segments that exceed the threshold.

To use this block:

-  Drag and drop into the workspace
-  Right-click the block and select the algorithm for your application:

   -  \**Mono RMS Full Range (No Post Gain) \*\*
   -  **Mono RMS Full Range with Gain Output (No Post Gain)**
   -  \**Mono RMS with Ext. Detect (No Post Gain) \*\*
   -  **Mono RMS with Ext. Detect and Gain Output (No Post Gain)**
   -  \**Mono RMS (No Post Gain) \*\*
   -  \**Mono RMS with Gain Output (No Post Gain) \*\*
   -  **Stereo RMS Full Range with Ext. Detect (No Post Gain)**
   -  **Stereo RMS Full Range with Ext. Detect and Gain Output (No Post Gain)**
   -  \**Stereo RMS Full Range (No Post Gain) \*\*
   -  **Stereo RMS Full Range with Gain Output (No Post Gain)**
   -  \**Stereo RMS with Ext. Detect (No Post Gain) \*\*
   -  **Stereo RMS with Ext. Detect and Gain Output (No Post Gain)**
   -  \**Stereo RMS (No Post Gain) \*\*
   -  **Stereo RMS with Gain Output (No Post Gain)**

-  Set these parameters to fit your application and click Show Graph and drag, add and remove (right-click) graphical points to draw your desired processing curve.

Controls
--------

+---------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RMS TC (db/s) | |rmsnopic3.png| | Controls the time constant (TC) in dB/second that is used for calculating the RMS input value. The time constant determines how rapidly the compressor will respond to input signal level changes, e.g. the "Attack" time. Larger values result in faster response times.                           |
+---------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)     | |rmsnopic4.png| | Controls the time (in ms) the compressor maintains its current output gain setting after the input level decreases, before the gain starts increasing back to normal.                                                                                                                               |
+---------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (db/s)  | |rmsnopic5.png| | Controls the rate at which the compressor gain increases back to normal in response to decrease in the input signal level, e.g. the "Release" time. Larger values result in faster recoveries. Cannot be higher than the RMS TC rate.                                                               |
+---------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Soft Knee     | |rmsnopic6.png| | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal. Typically it sounds better. If it is not activated, the default is hard-knee behavior, meaning compression reduces signal level immediately when the threshold is passed. |
+---------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show Graph    | |rmsnopic7.png| | Opens the Compression Curve editor window.                                                                                                                                                                                                                                                          |
+---------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Examples
========

RMS compressor with no external detector input
----------------------------------------------

| 
| |image1|
| \* The waveform in plum is the input signal. The signal is a sine tone of 500 Hz initially with an amplitude of -10dB.

-  When the input signal is at -10dB, the compression gain from the below plot is 6dB. This compression gain is applied to same signal as seen from the output waveform in dark red.
-  When the input signal level changes to -32dB by moving the Single1 volume slider, the compression gain is unchanged for 100ms because of the set hold time, after which the compression gain transitions to 0dB with the rate controlled by the release time set.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/rms_no_ext_example1.png
   :align: left

RMS compressor with external detector input
-------------------------------------------

| 
| |image2|

-  The waveform in plum is the control signal. The signal is a sine tone of 500 Hz initially with an amplitude of 0dB.
-  When the control signal is at 0dB, the compression gain from the below plot is 16dB. This compression gain is applied to the input waveform( sine tone of 1000 Hz, 0dB) the resultant output waveform is shown in blue.
-  When the control signal level changes to -32dB by moving the Single1 volume slider, the compression gain is unchanged for 100ms because of the set hold time, after which the compression gain transitions to 0dB with the rate controlled by the release time set.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/rms_ext_example1.png
   :align: left

.. |rmsnopic2.png| image:: https://wiki.analog.com/_media/rmsnopic2.png
.. |rmsnopic3.png| image:: https://wiki.analog.com/_media/rmsnopic3.png
.. |rmsnopic4.png| image:: https://wiki.analog.com/_media/rmsnopic4.png
.. |rmsnopic5.png| image:: https://wiki.analog.com/_media/rmsnopic5.png
.. |rmsnopic6.png| image:: https://wiki.analog.com/_media/rmsnopic6.png
.. |rmsnopic7.png| image:: https://wiki.analog.com/_media/rmsnopic7.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/rms_no_ext_example1_schematic.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/rms_ext_example3_schematic.png
