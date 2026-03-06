Loudness (Low and High) External Control
========================================

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

--------------

The Loudness (Low and High) External Control block like the Loundess (Low and High) block enhances the perceived loudness of a signal by raising the bass (<60 Hz) and the treble (>7kHz) level. Unlike the Loundess (Low and High) block, the loudness level parameter of the Loudness (Low and High) External Control block is controlled by an external signal instead of a volume slider.

The boost values are derived from the well-known equal-loudness curves of Fletcher and Munson and others. This research revealed that at low levels, lows and highs need to be considerably louder in order for the tonal balance to sound correctly proportioned and the overall sound to have the same apparent loudness to the human ear. Note that this algorithm is fixed, not dynamic: it assumes the input level is constant.

**External Control Pin:**

The external control pin is used to set the loudness volume parameter for the algorithm. This should be a 5.23 value between 0.0 and 1.0 which represents the desired volume (for example 0.5 for a level of -6dB). This controls the output volume of the entire block, and more importantly, it is also sets the threshold for the loudness algorithm. At low levels, the loudness algorithm boosts the low frequencies somewhat more than it does the high frequencies. For a control input of 1.0 (0dB), no matter what the input level is, there is no boost, LF or HF (See the Loundess (Low and High) level slider as it performs a similar function).

.. hint::

   Note: The example below can be used to test the algorithm's functionality, but it is for demonstration purposes only. See below for a practical design example.


| |loudnessextpic1.png|

**Controls:**

-  **LP Knob** The LP gain knob controls the relative amount of low frequency boost that is applied 0% - 100%.
-  **LP Frequency** The LP frequency spin control lets you change the cutoff frequency of the lowpass filter. The default value approximates the Fletcher-Munson curve. Higher-frequency values provide greater bass-bandwidth gain.
-  **HF Knob** The LP gain knob controls the relative amount of high frequency boost that is applied 0% - 100%.
-  **HP Frequency** The HF frequency spin control lets you change the cutoff frequency of the highpass filter. The default value of 7kHz approximates the Fletcher-Munson curve.
-  **SW Slew Rate** Adjusts the external volume parameter's slew rate (controls how quickly the algorithm responds to changes in the control signal).
-  in the right click context menu, An option to select the filter type is present. The option allows

::

     selection bewteen General first order filter and Butter worth first order filter. 

| 
| |image1|

**Example:**

The following example shows how a rotary encoder could be used to control the loudness level.

.. |loudnessextpic1.png| image:: https://wiki.analog.com/_media/loudnessextpic1.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/loudness_ext_control_gui.png
