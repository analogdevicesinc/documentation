.. warning:: Conversion failed for ``resources/tools-software/sigmastudio/toolbox/adialgorithms/enhancedstereocapture``

   Reason: pandoc error: Error at "/tmp/tmpie5o9wja.txt" (line 62, column 1):
expecting inline
not found
|Cores Supported|ADAU144x \\ ADAU176x \\ ADAU178x|
^

.. code-block:: text

   ======Enhanced Stereo Capture======
   
   [[resources/tools-software/sigmastudio/toolbox/adialgorithms|Click here to return to the ADI Algorithms page]]\\
   \\
   
   ^^^
   |The Enhanced Stereo Capture (ESC) algorithm takes a stereo record-signal and creates a wider stereo image. The ESC is meant as a record algorithm in order to capture an enhanced stereo image from two closely spaced microphones. [For stereo widening on the playback side, check [[resources/tools-software/sigmastudio/toolbox/adialgorithms/phatstereo|Phat-Stereo]]]|{{ESCpic1.png}}|
   \\
   
   ===Input Pins===
   ^Name^Format [int/dec] - [control/audio]^Function Description^
   |Pin 0: Audio In 1|decimal - audio|Left channel audio input (from mic)|
   |Pin 1: Audio In 2|decimal - audio|Right channel audio input (from mic)|
   
   ===Output Pins===
   ^Name^Format [int/dec] - [control/audio]^Function Description^
   |Pin 0: Audio Out 1|decimal - audio|Stereo enhanced left channel audio output|
   |Pin 1: Audio Out 2|decimal - audio|Stereo enhanced right channel audio output|
   
   ===GUI Controls===
   ^GUI Control Name^Default Value^Range^Function Description^
   |Stereo Balance Gain|0dB|[-20dB, 20dB]|This gain knob control adjusts how much stereo effect is achieved in the algorithm. Depending on the spacing of the microphones in the record environment, this value should be adjusted to obtain the best stereo perceptual results.|
   
   ===DSP Parameter Information===
   ^GUI Control Name^Compiler Name^Function Description^
   |Stereo Balance Gain|ESC1Alg1gain|The dB value in the control is converted to a linear gain value and written to the DSP.|
   
   ===Algorithm Description===
   The ESC algorithm accepts two input signals obtained from two closely spaced microphones. The algorithm separates these two signals and widens the stereo image. The end perceptual result is a widened stereo image as if the audio had been captured by microphones with greater L/R separation. The algorithm is based on proprietary filtering and a Stereo Balance Gain that adjusts how much stereo effect is archived in the algorithm.
   
    
   
   Depending on the spacing of the microphones in the record environment, a different Stereo Balance Gain should be selected. There are two recommended methods to do this required algorithm tuning.
   
   1) Simulated delay between the microphones to maximize the L/R separation (described below)
   
   2) Listening tests while adjusting the gain knob (shown in the Example section)
   
    
   
   The tuning required for method 1) can be done within SigmaStudio. The following schematic image shows how this is accomplished. The goal is to adjust the Stereo Balance Gain until the greatest visual difference in level is achieved between the left and right output signals.\\
   {{ ESCpic2.png }}\\
   
   
   The Tone block represents the signal being captured by the microphones. The tone frequency should be selected to maximize the L/R separation for a target frequency range. The Linear Gain block only serves to bring down the end level of the signal so that it is viewable on the visual Level Detectors. The Delay block works to simulate the delay difference between the microphones. Thus the left signal passes though with no delay. The right signal however, goes through 4 samples of delay to simulate a spacing difference of ~2.8cm between the left and right microphones. Change this delay value to match the corresponding distance between the microphones based on this formula:\\
   {{ ESCpic3.png }}\\
   
   
   
   Finally, adjust the Stereo Balance Gain to maximize the level difference between L and R on the Level Detectors. This will maximize the separation between the left and right capture signals.
    
   ===Example===
   The following schematic image shows the ESC being used to get a wider stereo capture image from an input. The stereo selection Mux allows selection for comparison between the direct input signal, versus the enhanced signal to archive better L/R separation between the mic inputs.\\
   {{ ESCpic4.png }}\\
   
   
   <WRAP round help>Note: In a full system level design the ESC block should be as close to the inputs as possible in the signal chain. This will ensure the optimal captured separation between the microphones and all resulting processing will be done in stereo.</WRAP> 
    
   ===Algorithm Details===
   ^^^
   |Toolbox Path|ADI Algorithms - Record Algorithms - Enhanced Stereo Capture (ESC)
   |Cores Supported|ADAU144x \\ ADAU176x \\ ADAU178x|
   |"Grow Algorithm" Supported|no|
   |"Add Algorithm" Supported|no|
   |Subroutine/Loop Based|no|
   |Program RAM|21|
   |Data RAM|12|
   |Parameter RAM|7|
   
   
