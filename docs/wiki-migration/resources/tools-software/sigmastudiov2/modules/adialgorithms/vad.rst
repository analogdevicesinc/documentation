:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

Voice Activity Detector
=======================

| |vad.png| |vadaccelerator.png|
| ===== Description ===== Voice Activity Detector takes an input signal and tracks the signal level compared to the noise floor. The Modulation Index is then later used to determine if speech is present or not.
| The VAD w/ Accelerator provides extra conditions to accelerate or increase the time constants in voice detection. Either the Release time for TopTracker is affected or the Attack time for BottomTracker is affected when their corresponding conditions are met. Thus, if TopTracker has been in release mode for Top Wait time, then the Top Release time constant will be increased by a scalar of Top Factor. And if BottomTracker has been in attack mode for Bottom Wait time, then the Bottom Attack time constant will be increased by a scalar of Bottom Factor.
| ===== Variants =====

-  Voice Activity Detector
-  Voice Activity Detector with Accelerator

| 
| ===== Targets Supported =====

+----------------------+------------+------------------+---------------+------------------+
| Name                 | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+======================+============+==================+===============+==================+
| VAD                  | NA         | NA               | S             | NA               |
+----------------------+------------+------------------+---------------+------------------+
| VAD with Accelerator | NA         | NA               | S             | NA               |
+----------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

============= ===== ===================
Name          Type  Description
============= ===== ===================
Speech Signal Audio Speech Input signal
============= ===== ===================

Output
------

+-----------------+-------+---------------------------------------------------------------+
| Name            | Type  | Description                                                   |
+=================+=======+===============================================================+
| EnvelopeOut     | Audio | Smoothed envelope of input signal                             |
+-----------------+-------+---------------------------------------------------------------+
| TopTracker      | Audio | Signal tracker of the peak of the EnvelopeOut                 |
+-----------------+-------+---------------------------------------------------------------+
| BottomTracker   | Audio | Signal tracker of the noise floor of the EnvelopeOut          |
+-----------------+-------+---------------------------------------------------------------+
| ModulationIndex | Audio | Modulation level of input signal (TopTracker ? BottomTracker) |
+-----------------+-------+---------------------------------------------------------------+

| 
| ===== Configurable Parameters =====

+---------------+---------------+---------+----------------------------------------------------------------------------------------------------------------+
| GUI Parameter | Default Value | Range   | Function Description                                                                                           |
+===============+===============+=========+================================================================================================================+
| LPFSmoother   | 30            | 1-100   | 1st order LPF frequency cutoff in Hz for smoothing of input signal                                             |
+---------------+---------------+---------+----------------------------------------------------------------------------------------------------------------+
| TopAttack     | 1000          | 1-10000 | dB/sec attack time constant value for the TopTracker                                                           |
+---------------+---------------+---------+----------------------------------------------------------------------------------------------------------------+
| TopRelease    | 20            | 1-10000 | dB/sec release time constant value for the TopTracker                                                          |
+---------------+---------------+---------+----------------------------------------------------------------------------------------------------------------+
| BottomAttack  | 2             | 1-10000 | dB/sec attack time constant value for the BottomTracker                                                        |
+---------------+---------------+---------+----------------------------------------------------------------------------------------------------------------+
| BottomRelease | 500           | 1-10000 | dB/sec release time constant value for the BottomTracker                                                       |
+---------------+---------------+---------+----------------------------------------------------------------------------------------------------------------+
| TopWait       | 0.5           | 0-60    | Time in seconds to wait for TopTracker to be in release mode, before accelerating/increasing the release time  |
+---------------+---------------+---------+----------------------------------------------------------------------------------------------------------------+
| TopFactor     | 20            | 2-100   | Scalar used to accelerate the release time for TopTracker                                                      |
+---------------+---------------+---------+----------------------------------------------------------------------------------------------------------------+
| BottomWait    | 1             | 0-60    | Time in seconds to wait for BottomTracker to be in attack mode, before accelerating/increasing the attack time |
+---------------+---------------+---------+----------------------------------------------------------------------------------------------------------------+
| BottomFactor  | 8             | 2-100   | Scalar used to accelerate the attack time for BottomTracker                                                    |
+---------------+---------------+---------+----------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+-------------------+-------------------------------------------------------------+------------------------+---------------+
| Parameter Name    | Description                                                 | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+===================+=============================================================+========================+===============+
| LPF               | Low pass filter coefficient                                 | NA                     | 8.24 Format   |
+-------------------+-------------------------------------------------------------+------------------------+---------------+
| toptrackerHI      | TopTracker parameters                                       | NA                     | 8.24 Format   |
+-------------------+-------------------------------------------------------------+------------------------+---------------+
| AttackTop         | Attack time constant value for the TopTracker               | NA                     | 8.24 Format   |
+-------------------+-------------------------------------------------------------+------------------------+---------------+
| ReleaseTop        | Release time constant value for the TopTracker              | NA                     | 8.24 Format   |
+-------------------+-------------------------------------------------------------+------------------------+---------------+
| AttackBottom      | Attack time constant value for the BottomTracker            | NA                     | 8.24 Format   |
+-------------------+-------------------------------------------------------------+------------------------+---------------+
| ReleaseBottom     | Release time constant value for the BottomTracker           | NA                     | 8.24 Format   |
+-------------------+-------------------------------------------------------------+------------------------+---------------+
| TopWait           | TopTracker wait factor                                      | NA                     | Integer       |
+-------------------+-------------------------------------------------------------+------------------------+---------------+
| BottomWait        | BottomTracker wait factor                                   | NA                     | Integer       |
+-------------------+-------------------------------------------------------------+------------------------+---------------+
| ReleaseTopAccel   | Scalar used to accelerate the release time for TopTracker   | NA                     | 8.24 Format   |
+-------------------+-------------------------------------------------------------+------------------------+---------------+
| AttackBottomAccel | Scalar used to accelerate the attack time for BottomTracker | NA                     | 8.24 Format   |
+-------------------+-------------------------------------------------------------+------------------------+---------------+

.. |vad.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/vad.png
.. |vadaccelerator.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/vadaccelerator.png
