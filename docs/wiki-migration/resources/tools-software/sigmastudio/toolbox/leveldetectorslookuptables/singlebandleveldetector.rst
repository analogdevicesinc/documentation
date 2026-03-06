Single Band Level Detectors
===========================

:doc:`Click here to return to the Level Detectors/Lookup Tables page </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables>`

The Level Detector blocks calculate the input signal level, reading directly from the hardware in real time, and display the level graphically in meter displays. The level detector performs analysis only and does not modify the input signal. The signal at the output pin is identical to the input. The level detector will not function until the schematic design has been compiled and downloaded to the hardware and a USB communication channel is properly configured.

The refresh rate of the display is approximately 10 Hz, while the green cross-bar tracks the maximum rms value with a slight delay. Note that the display's performance is limited by your PC system and USB communication resources. Enabling multiple level detectors simultaneously may degrade responsiveness.

There are various types of single band level detectors as shown below

-  Single Level Detector w Numeric Display
-  Direct Read: Single Level Detector
-  Running Average: Single Level Detector
-  Level Detector W Numeric Display.Low DSP MIPS.AVerage Enable

| 
|

.. tip::

   Note that the pins on the Level Detectors act as a passthrough from input to output. In other words, the level detector is transparent to the signal flow.


| 
| ===== Single Level Detector w Numeric Display =====
| The Single-Level Detector w Numeric Display module calculates and displays the RMS level of the signal, shown in dB. Use the On / Off button to enable or disable the display. The Inv checkbox will show the level bars from top to bottom, rather than bottom to top.

| Here, the RMS calculations occur within the DSP. The RMS level is then read back from the DSP and displayed in SigmaStudio frequently enough that no peaks will be missed on the display (as long as the communications interface is not overloaded).
| |image1|
| ===== Direct Read: Single Level Detector =====
| The Direct Read Single Level Detector module is similar to the Single Level Detector w Numeric Display. However, the calculations are split between the DSP and SigmaStudio. The DSP calculates the level of the signal in dB, as dB = 20*Log(SampleValue), and then SigmaStudio reads back this value and averages according to y = tc*y(n-1) + (1-tc)x.

| Since SigmaStudio reads back the level much slower than the audio sample rate, some samples will be missed with this algorithm. In general, the Direct Read algorithm should only be used if the DSP is running very low on resources.
| |image2|
| ===== Running Average: Single Level Detector =====
| The Running Average Single Level Detector module calculates and displays the average level of the signal, shown in dB. Use the On / Off button to enable or disable the display.

| This algorithm is very similar to Single Level Detector w Numeric Display. The UI in SigmaStudio is the main difference.
| |image3|
| ===== Level Detector W Numeric Display.Low DSP MIPS.AVerage Enable =====
| The Low DSP MIPS block acts as an audio sample readback register. The DSP does not perform any level detector calculations. Instead, SigmaStudio reads back the sample, converts it to dB, and performs averaging. As with the Direct Read algorithm, transient peaks may be missed by this level detector.
| |image4|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/leveldetectorwnd.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/leveldetectoravgorrunn.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/leveldetectoravgorrunn.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/leveldetectorlowmips.png
