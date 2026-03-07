:doc:`Click here to return to the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudiov2/modules/advanceddsp>`

Adaptive Mixer Dual Graph
=========================

| |mixershape.png|
| ===== Description ===== The Adaptive Mixer Dual (graph) is an advanced method of mixing two signals based on a third control signal.
| ===== Usage ===== The orange pin here indicates that the input control signal will be converted to a RMS average value, eliminating the need to use the RMS table for this application. The RMS table value is used to determine the scale factors for the signals to be mixed. Users can select and change the curves for both signals to be mixed.\|
| |mixerpopup.png|
| ===== Targets Supported =====

+---------------------------+------------+------------------+---------------+------------------+
| Name                      | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===========================+============+==================+===============+==================+
| Adaptive Mixer Dual Graph | NA         | NA               | S             | NA               |
+---------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

======== ======= ================================================
Name     Type    Description
======== ======= ================================================
Input0   Audio   Audio input
Input1   Audio   Audio input
Selector Control Calculates the RMS average for this input signal
======== ======= ================================================

Output
------

======= ===== ============================
Name    Type  Description
======= ===== ============================
Output0 Audio Compressed mono audio output
======= ===== ============================

| 
| ===== Configurable Parameters =====

+---------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter | Default Value | Range      | Function Description                                                                                                                                                                                                                                                                                          |
+===============+===============+============+===============================================================================================================================================================================================================================================================================================================+
| TimeConstant  | 150           | 1 - 1000   | Controls the Time Constant (TC) setting the attack time of the RMS average computation. The RMS time constant determines how rapidly the gain will adapt to abrupt changes in the input signal level                                                                                                          |
+---------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Step          | 8             | 1 to 23    | Controls the slew ram rate in terms of how quickly the algorithm ramps to the next value                                                                                                                                                                                                                      |
+---------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Smooth        | False         | True/False | This checkbox determines whether the ratio curve of the levels will be exactly linear from graph point to graph point, or if it will be smoothed out                                                                                                                                                          |
+---------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show Graph    |               |            | This button allows you to bring up the mix ratio window. You can change the curve by moving, adding, or removing graph points. The RMS table value gives you the x-value on this graph and the corresponding y-values will be the scale factors for the output levels of the mix between the 1st and 2nd pins |
+---------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TableMixer1   |               |            | Table corresponding to first graph                                                                                                                                                                                                                                                                            |
+---------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TableMixer2   |               |            | Table corresponding to second graph                                                                                                                                                                                                                                                                           |
+---------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== ============= =============
Parameter Name Description   ADAU145x/146x
============== ============= =============
tc             Time constant FixPoint8d24
step           step size     FixPoint8d24
points_ONE     First graph   FixPoint8d24
points_TWO     Second graph  FixPoint8d24
============== ============= =============

DSP Parameter Computation
~~~~~~~~~~~~~~~~~~~~~~~~~

step = 2 ^ (-1 / Step) tc = (10 ^ (TimeConstant / (10 \* FS))) - 1

.. |mixershape.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/advanceddsp/mixershape.png
.. |mixerpopup.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/advanceddsp/mixerpopup.png
