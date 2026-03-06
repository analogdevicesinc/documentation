VAD Flag
========

:doc:`Click here to return to the ADI Algorithms section of the toolbox. </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

+---+---+
| VAD Flag takes the Modulation Index and compares it to a threshold value. If the threshold value is met for the designated amount of time, the output flag is set high, otherwise it is low. | |image2| |
+---+---+

Input:

-  Unordered List ItemModulationIndex

Output

-  Unordered List ItemConditionFlag: 0 or 1 output determining if speech is present or not

Parameter Control:

-  Threshold: dB value for comparison with Modulation Index
-  Count: Time value in (ms) for condition to be met before setting flag high

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/voiceactivitydetector_007.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/voiceactivitydetector_007.jpg
