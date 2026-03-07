Dynamics Processor Examples
===========================

:doc:`Click here to return to the Tutorials section. </wiki-migration/resources/tools-software/sigmastudio/tutorials>`

Example 1
---------

This design uses the RMS Detect (display) block, along with input/output blocks for audio flow. What is important to note about the example shown below are the Compression Curve window; the relative input/output levels on the display bars; and the Post Gain knob.

The threshold (level match point, where no dynamic processing takes place) is set at approximately 35 dB on the horizontal input level axis, as well as the same on the vertical output axis. The compression ratio above threshold has been drawn to approximate 2.7:1.

For all input signals below 35 dB, then, the output level will be unaffected. When the input exceeds this threshold, however, for every 2.7 dB it increases, the output will increase only 1 dB.

The display bars indicate the levels of the input and the compression respectively (greener = more compressed). The input green horizontal bar shows the level of the last value before the current level.

In this case the compression significantly lowered the output level, so to make it up, it was necessary to turn the output up an added 12 dB (Post Gain).

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/dynamicsprocessorexample1.jpg
   :alt: dynamicsprocessorexample1.jpg

.. important::

   While the interface lets you easily create complex dynamics processing curves (as shown above by the behavior below -55 dB), this example deals only with a linear ratio constructed using only one active graph point, the one at -35.


Example 2
---------

This design uses Tone (lookup/sine), Single Vol (shared), Limiter, DSP Readback, Terminal and output blocks. Here the threshold point for the input signal is set as -24 dB, and when the rms value of the input exceeds it, the gain is reduced per the ratio given on the Limiter help page.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/dynamicsprocessorexample2.jpg
   :alt: dynamicsprocessorexample2.jpg

Looking at the Limiter block, the blue pin outputs the dynamically limited signal. The first red pin (middle of three pins) outputs 1 (one), which can be read from the numeric box in the Readback block, indicating that the limiter is currently clamping the input per the instantaneous limiting ratio (Gn).

Example 3
---------

The following design uses RMS Detect (no: gain, hold, decay) and Single Level Detector, along with input/output blocks. This schematic shows the increase in the level of the output signal after processing. The threshold is set at -30 dB on the input axis. The output level is unaffected for inputs below -30 dB. However, when the input signal exceeds the threshold, the output increases steeply according to the expansion ratio of the curve shown (approximately 2.5:1 above threshold, which is strong expansion).

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/dynamicsprocessorexample3.jpg
   :alt: dynamicsprocessorexample3.jpg

Example 4
---------

This schematic uses Tone (lookup/sine), Linear Gain, T Connection, Multiply, Envelope and Output blocks. Here the Multiply block multiplies the output of Linear Gain, which has scaled the 1 kHz tone by 5, and Envelope detects the energy envelope of the Multiply output.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/dynamicsprocessorexample4.jpg
   :alt: dynamicsprocessorexample4.jpg
