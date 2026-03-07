:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

Beam Forming Designer
=====================

|beamforming.jpg| |beamforminggraph.jpg|

Description
-----------

| Beam-former algorithm with fractional delay combines signals in a manner which increases the signal strength to/from a chosen direction. Signals to/from other directions are combined in a benign or destructive manner, resulting in degradation of the signal to/from the undesired direction.
| ===== Targets Supported =====

==================== ========== ================ =============
Name                 ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
==================== ========== ================ =============
Beamforming Designer Block      Block            Sample
==================== ========== ================ =============

| 
| ===== Pins =====

Input
~~~~~

================ ===== ==============
Name             Type  Description
================ ===== ==============
Rear Microphone  Audio Input Channel0
Front microphone Audio Input Channel1
================ ===== ==============

Output
~~~~~~

======= ===== ===============
Name    Type  Description
======= ===== ===============
Output0 Audio Output channel0
======= ===== ===============

| 
| ===== Grow & Add Algorithm ===== The module does not support both Grow and Add Algorithm.
| ===== Configurable Parameters =====

+--------------------+---------------+-----------+--------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range     | Function Description                                                                             |
+====================+===============+===========+==================================================================================================+
| Max Delay          | 1             | 1 to 5000 | Maximum Delay Supported                                                                          |
+--------------------+---------------+-----------+--------------------------------------------------------------------------------------------------+
| Current Delay      | 3             | 0 to 100  | Delay as % of Maximum Delay                                                                      |
+--------------------+---------------+-----------+--------------------------------------------------------------------------------------------------+
| Show Design Window | NA            | NA        | Launches the “Beam Former Designer”. The settings on the Designer doesn’t impact the parameters. |
+--------------------+---------------+-----------+--------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+--------------------------------------+---------------------------------+
| Parameter Name | Description                          | ADSP-214xx/SC5xx/215xx/ADAU1466 |
+================+======================================+=================================+
| Slope          | Length of the delay buffer= MaxDelay | Integer                         |
+----------------+--------------------------------------+---------------------------------+
| Delay          | Current Delay= CurrentDelay/100      | Float                           |
+----------------+--------------------------------------+---------------------------------+

| 

.. |beamforming.jpg| image:: https://wiki.analog.com/_media/beamforming.jpg
.. |beamforminggraph.jpg| image:: https://wiki.analog.com/_media/beamforminggraph.jpg
