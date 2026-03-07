Adaptive Beam Forming
=====================

:doc:`Click here to return to the ADI Algorithms section of the toolbox. </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| The 2-channel SigmaDSP Beamformer uses a modified version of the so-called “Griffiths-Jim” Beamformer (1). This beamformer can track a single source of off-axis interference and place a null in the directional pattern, pointed at the source of the interference. The Block Diagram of this beamformer is shown below. | |image2| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

The left/right microphone inputs are first applied to a highpass filter to remove DC components. The filter cutoff frequency is 15Hz for Fs = 24KHz.

The “steering direction” is set by the difference in delays between the two inputs. The right channel contains a fixed input delay of 8 samples, and the left channel has a variable delay from 0 to 16 samples, allowing the left channel to either lead or lag the right channel by up to 8 samples. The directional pattern has maximum sensitivity when the outputs of the two delay blocks are the same. The corresponding source angle can be computed based on the sample-rate and microphone spacing. The pin “intermic_delay” should be connected to an external DC source, and is designed so that with 0 input the left-channel delay is equal to the right-channel delay (8 samples). This pin has a sensitivity of 1 LSB per sample delay. If this pin is connected to an external DC source, the numeric format of the DC block can be set to “28.0” so that the inter-mic delay can be entered directly in samples, with values between -8 and +8.

The outputs of the delay blocks are summed in the upper path, and differenced in the lower path. Before the difference operation, a microphone matching algorithm is used that attempts to match the amplitudes of the two microphones. This will result in reduced sensitivity to microphone gain tolerances, but it should be noted that the microphones still need to be tightly matched in terms of phase response.

The difference signal is then applied to an IIR lowpass filter which attempts to pre-compensate the expected rising response of the microphone difference signal, and then applied to an normalized adaptive filter which attempts to remove any L-R components that are present in the L+R signal. In theory the L-R signal should go to zero for signals in the “look” direction, but in practice this does not occur due largely to room acoustics. This can potentially allow the adaptive filter to also eliminate the desired signal. To prevent this, a limit is placed on the maximum mean-square value of the filter coefficients. Since the value of this parameter depends on room acoustics, it is made adjustable by the user. In practice this parameter controls how close the adaptive null direction can be relative to the “look direction”. Smaller values should be used in highly reverberant environments to prevent accidental cancellation of the desired signal. For off-axis interfering signals, the L-R signal is large enough due to the left/right phase differences that the adaptive filter does not need to have a large gain in order to cancel the L-R component, and therefore the mean-square coefficient limit is never reached. A typical value for this parameter is around 0.02.

The normalized adaptive filter also exposes parameters for “alpha”, which controls adaptation speed, “leak”, which controls the LMS coefficient leakage factor, and the filter length which can be set to 32, 64, or 128. These parameters are well-covered in the literature on adaptive filters. Note that the default parameters are set with an assumed sample-rate of 24KHz, and for other sample-rates the value for alpha should be adjusted inversely to the sample-rate. If the “leak” factor is set to 1.0, then the null that forms in a particular direction will persist even when the input signal goes away, whereas if the leak factor is set to, for example, 0.99999, the filter will slowly decay to zero after the signal has gone away. If the leak factor is set too low, the depth of the directional null will be poor.

A pin is also provided to turn on and off the adaptive algorithm. Applying a 0 to this pin turns the adaptive filter off, and “1.0” enables the adaptive filter.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/adaptivebeamforming_002.jpg
   :align: center
   :width: 800px

To extend this algorithm to more than two microphones, you can cascade systems as shown below. Note that one microphone (mic 2) has a fixed delay in both upper and lower paths, and the other 2 mics are adjusted relative to mic2 in order to steer the beam. Note that for a 4-microphone systems, up to 3 independent off-axis interfering sources can be tracked and canceled.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/adaptivebeamforming_003.jpg
   :align: center
   :width: 800px

The details of the mic matching algorithm are shown below. Note that the goal of this algorithm is to minimize the correlation between L-R and L+R. For closely-spaced mics this amounts to compensating for gain mismatch, but for larger mic spacing (or for very high frequencies) where the phase difference between the mics becomes large, it may not yield the same result as simple gain mismatch reduction.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/adaptivebeamforming_004.jpg
   :align: center
   :width: 800px

Here is an example of the beamformer in a SigmaStudio project:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/adaptivebeamforming_005.jpg
   :align: center

A downloadable version of this project for the ADAU1761 is available `here <https://wiki.analog.com/_media/resources/tools-software/sigmastudio/adau1761_adaptivebeamformingexample.zip>`_.

Pins
----

-  Mic In (top pin): Left channel input (5.23 audio)
-  Mic In (2nd pin): Right channel input (5.23 audio)
-  Start/Stop (3rd pin): Turn this on to adapt the target direction of the beamforming. Turn it off to “lock” the directionality at its most recent value. (5.23 logic)
-  Inter-microphone delay (bottom pin): (28.0 integer, one sample per LSB, between -8 and +8)
-  Output: The resulting audio output after beam-forming (5.23 audio)

GUI Controls
------------

-  LMS alpha (adaptation speed)
-  Max MS (maximum mean-square value limit for filter coefficients, typically 0.02)
-  LMS leak (controls the "leakage" of the filter when the input signal goes away. Set slightly below 1)
-  FIR length (length of the filter)

Resource Requirements
---------------------

-  Instruction RAM: 189 words
-  Instructions executed per sample: 189
-  Data RAM: 175 words
-  Coefficient RAM: 177 words

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/adaptivebeamforming_001.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/adaptivebeamforming_001.jpg
