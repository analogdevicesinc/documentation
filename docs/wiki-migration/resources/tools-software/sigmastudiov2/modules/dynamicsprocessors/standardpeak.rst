.. warning:: Conversion failed for ``resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/standardpeak``

   Reason: pandoc error: Error at "/tmp/tmp0nw101re.txt" (line 36, column 1):
expecting inline
not found
^GUI Parameter Name^Default Value^Range^Function Description^
^

.. code-block:: text

   [[resources/tools-software/sigmastudiov2/modules/dynamicsprocessors|Click here to return to the Dynamic Processors page]]
   ====== Standard Peak======
   \\
   {{:resources:tools-software:sigmastudiov2:modules:dynamicsprocessors:standardpeak.png?nolink}}
   \\
   {{:resources:tools-software:sigmastudiov2:modules:dynamicsprocessors:standardpeakgraph.png?nolink&650}}
   ===== Variants =====
     - Standard Peak
     - Standard Peak with Ext Detect Input
   
   \\
   ===== Description =====
   The Standard Peak Compressor is a stereo compressor that allows direct control over threshold and ratio. In the pop-up GUI, graphical controls are given for threshold, ratio, and time constants. Also there are visual indicators showing input, output, and compression levels. The detection signal used for this Peak compressor is based on the sum of Left and Right channels.
   \\
   ===== Targets Supported =====
   ^ Name             ^ ADSP-214xx ^ ADSP-215xx/SC5xx ^ ADAU145x/146x ^ ADSP-218xx/SC8xx ^
   | Standard Peak | NA        | NA              | S           | NA |
   | Standard Peak with Ext Detect Input | NA        | NA              | S           | NA |
   
   \\
   ===== Pins =====
   ==== Input ====
   ^Name^Type^Description^
   |L_In| Audio | Left Channel Input |
   |R_In| Audio | RightChannel Input |
   |Ext_Det| Control| Ext Detector Input channel |
   |(Standard RMS with Ext Detect Input)|
   
   
   ==== Output ====
   ^Name^Type^Description^
   |L_Out| Audio | Left Channel Out|
   |R_Out| Audio | RightChannel Out|
   |Gain_Out| Control| Gain out channel|\\
   ===== Configurable Parameters =====
   ^GUI Parameter Name^Default Value^Range^Function Description^
   |Threshold (dB)|0|-96|Controls the threshold point of compression/expansion.|
   |Compression|100|100 - 1|Controls the ratio of Compression. The number selected in this box is interpreted as the ratio N:1 for compression above the threshold point.|
   |Expander|1|100 - 1|Controls the ratio of Downward Expansion. The number selected in this box is interpreted as the ratio N:1 for downward expansion below the threshold point.|
   |Knee|1|1 - 100|Controls the hard/soft knee relationship of the curve. A knee allows a more gradual calculation of the curve around the threshold point, with "1" being a hard knee, and "100" being the softest.|
   |InputGain (dB)|0|-96|Controls a gain that is applied to both Left and Right prior to the compression. Allows for the curve to be shifted left and right.|
   |Hold (ms)|0|0 - Attack|Controls the amount of time the compression level is held before reacting to a new change in input signal level. The max hold time is limited to the Attack time setting.|
   |Release (ms)|868|Jan-00|Controls the amount of time before the compressor reacts to an input signal that has dropped below the threshold point.|
   |IsLevelIndicatorsEnabled|off|on/off|Turns the Indicators on or off. There is no DSP function associated with this.|
   \\
   ===== DSP Parameters =====
   ^Parameter Name^Description^ADAU145x/146x^ 
   |points|When the Threshold, Compressor, Expander, or Knee values are changed, 34 parameters are written to the DSP to represent the gain curve displayed in the window.| 8.24 Format|
   |attenuation|When the Input Gain is changed, the dB value is converted to linear and written to the DSP.| 8.24 Format|
   |tc|When the Attack time is changed, a new value is calculated and written to the DSP to control the reaction time.| 8.24 Format|
   |hold|When the Hold time is changed, a new value is calculated and written tot he DSP to control the hold time.| 8.24 Format|
   |decay|When the Decay time is changed, a new value is calculated and written to the DSP to control the reaction time.| 8.24 Format|
   \\
