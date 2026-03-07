.. warning:: Conversion failed for ``resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/standardrms``

   Reason: pandoc error: Error at "/tmp/tmpr58z_2wq.txt" (line 37, column 1):
expecting inline
not found
^GUI Parameter Name^Default Value^Range^Function Description^
^

.. code-block:: text

   [[resources/tools-software/sigmastudiov2/modules/dynamicsprocessors|Click here to return to the Dynamic Processors page]]
   ====== Standard RMS ======
   \\
   {{:resources:tools-software:sigmastudiov2:modules:dynamicsprocessors:standardrms.png?nolink}}
   \\
   {{:resources:tools-software:sigmastudiov2:modules:dynamicsprocessors:standardrmsgraph.png?nolink&650}}
   \\
   ===== Variants =====
     - Standard RMS
     - Standard RMS with Ext Detect Input
   
   \\
   ===== Description =====
   This Module computes the Gain of the Compressor. Compression happens by taking the RMS of the Average or Max of all inputs, and then looking up for the Gain based on the Compressor Graph.
   \\
   ===== Targets Supported =====
   ^ Name             ^ ADSP-214xx ^ ADSP-215xx/SC5xx ^ ADAU145x/146x ^ ADSP-218xx/SC8xx ^
   | Standard RMS | NA        | NA              | S           | NA |
   | Standard RMS with Ext Detect Input | NA        | NA              | S           | NA |
   
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
   |R_Out| Audio | Right Channel Out|
   |Gain_Out| Control| Gain out channel|\\
   ===== Configurable Parameters =====
   ^GUI Parameter Name^Default Value^Range^Function Description^
   |Threshold (dB)|0|-96|Controls the threshold point of compression/expansion.|
   |Compression|100|100 - 1|Controls the ratio of Compression. The number selected in this box is interpreted as the ratio N:1 for compression above the threshold point.|
   |Expander|1|100 - 1|Controls the ratio of Downward Expansion. The number selected in this box is interpreted as the ratio N:1 for downward expansion below the threshold point.|
   |Knee|1|1 - 100|Controls the hard/soft knee relationship of the curve. A knee allows a more gradual calculation of the curve around the threshold point, with "1" being a hard knee, and "100" being the softest.|
   |InputGain (dB)|0|-96|Controls a gain that is applied to both Left and Right prior to the compression. Allows for the curve to be shifted left and right.|
   |Attack (ms)|72|1- 500|Controls the amount of time before the compressor reacts to an input signal that has exceeded the threshold point.|
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
