Voice Activity Detector
=======================

:doc:`Click here to return to the ADI Algorithms section of the toolbox. </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

Voice Activity Detector w/ Accelerator takes an input signal and tracks the signal level compared to the noise floor. The Modulation Index is then later used to determine if speech is present or not

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/voiceactivitydetector_006.jpg
   :align: center

Input:

-  Speech Signal (Rx or Tx)

Output:

-  EnvelopeOut: Smoothed envelope of input signal
-  TopTracker: Signal tracker of the peak of the EnvelopeOut
-  BottomTracker: Signal tracker of the noise floor of the EnvelopeOut
-  ModulationIndex: Modulation level of input signal (TopTracker ? BottomTracker)

Parameter Control:

-  LPF Smoother: 1st order LPF frequency cutoff in Hz for smoothing of input signal
-  Top Attack: dB/sec attack time constant value for the TopTracker
-  Top Release: dB/sec release time constant value for the TopTracker
-  Bottom Attack: dB/sec attack time constant value for the BottomTracker
-  Bottom Release: dB/sec release time constant value for the BottomTracker
-  Top Wait: Time in seconds to wait for TopTracker to be in release mode, before accelerating/increasing the release time
-  Top Factor: Scalar used to accelerate the release time for TopTracker
-  Bottom Wait: Time in seconds to wait for BottomTracker to be in attack mode, before accelerating/increasing the attack time
-  Bottom Factor: Scalar used to accelerate the attack time for BottomTracker

Description:
------------

The VAD w/ Accelerator provides extra conditions to accelerate or increase the time constants in voice detection. Either the Release time for TopTracker is affected or the Attack time for BottomTracker is affected when their corresponding conditions are met. Thus, if TopTracker has been in release mode for Top Wait time, then the Top Release time constant will be increased by a scalar of Top Factor. And if BottomTracker has been in attack mode for Bottom Wait time, then the Bottom Attack time constant will be increased by a scalar of Bottom Factor.
