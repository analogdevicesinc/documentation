.. warning:: Conversion failed for ``resources/tools-software/sigmastudiov2/modules/adialgorithms/esc``

   Reason: pandoc error: Error at "/tmp/tmp4iccsqpy.txt" (line 34, column 1):
expecting inline
not found
\\
^

.. code-block:: text

   [[resources/tools-software/sigmastudiov2/modules/adialgorithms|Click here to return to the ADI Algorithms page]]
   ====== Enhanced Stereo Capture ======
   
   {{:resources:tools-software:sigmastudiov2:modules:adialgorithms:esc.png}}
   \\
   ===== Description =====
   The Enhanced Stereo Capture (ESC) algorithm takes a stereo record-signal and creates a wider stereo image. The ESC is meant as a record algorithm in order to capture an enhanced stereo image from two closely spaced microphones. 
   \\
   \\
   ===== Usage =====
   The ESC algorithm accepts two input signals obtained from two closely spaced microphones. The algorithm separates these two signals and widens the stereo image. The end perceptual result is a widened stereo image as if the audio had been captured by microphones with greater L/R separation. The algorithm is based on proprietary filtering and a Stereo Balance Gain that adjusts how much stereo effect is archived in the algorithm.
   
   Depending on the spacing of the microphones in the record environment, a different Stereo Balance Gain should be selected. There are two recommended methods to do this required algorithm tuning (shown in the Example section).
   
     - Simulated delay between the microphones to maximize the L/R separation
     - Listening tests while adjusting the gain knob 
   
   The tuning required for method 1) can be done within SigmaStudio. The schematic image in example section shows how this is accomplished. The goal is to adjust the Stereo Balance Gain until the greatest visual difference in level is achieved between the left and right output signals..
   \\
   \\
   ===== Targets Supported =====
   ^ Name            ^ ADSP-214xx ^ ADSP-215xx/SC5xx ^ ADAU145x/146x ^ ADSP-218xx/SC8xx ^
   | Enhanced Stereo Capture   | NA          | NA                | S              | NA              |
   \\
   ===== Pins =====
   ==== Input ====
   ^ Name        ^ Type    ^ Description ^
   |LeftIn| Audio | First input channel |
   |RightIn| Audio | Second input channel |
   
   ==== Output ====
   ^ Name        ^ Type    ^ Description ^
   |LeftOut| Audio | First output channel |
   |RightOut| Audio | Second output channel 
   \\
   ===== Configurable Parameters =====
   ^ GUI Parameter        ^ Default Value ^ Range     ^ Function Description ^
   | LRValue | 0dB | -20 - 20dB  | This gain knob control adjusts how much stereo effect is achieved in the algorithm. Depending on the spacing of the microphones in the record environment, this value should be adjusted to obtain the best stereo perceptual results |
   \\
   ===== DSP Parameters =====
   ^ Parameter Name       ^ Description ^ ADAU145x/146x ^
   | gain | Linear gain value | 8.24 Format |
   | a1hpf | High pass filter coefficients | 8.24 Format Array |
   | a1lpf | Low pass filter coefficients | 8.24 Format Array |
   \\
