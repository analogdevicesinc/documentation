:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

Pitch Transposer
================

| |pitch.png| |pitchdatacontrolled.png|
| ===== Description ===== Pitch Transposer algorithm shifts the frequency of an incoming signal. There are two versions of the algorithm. The first version allows the user to manually set the pitch shift amount by entering it in the GUI (or writing a value directly to RAM). In the data controlled variant, the frequency shift is “voltage-controlled”, meaning that there is an input pin that controls the pitch shift amount based on its value.
| ===== Variants =====

-  Pitch Transposer
-  Pitch Transposer Data Controlled

| 
| ===== Targets Supported =====

+----------------------------------+------------+------------------+---------------+------------------+
| Name                             | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==================================+============+==================+===============+==================+
| Pitch Transposer                 | S          | S                | S             | NA               |
+----------------------------------+------------+------------------+---------------+------------------+
| Pitch Transposer Data Controlled | S          | S                | S             | NA               |
+----------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

+--------------------+---------+----------------------------------------------------------------------------------------------+
| Name               | Type    | Description                                                                                  |
+====================+=========+==============================================================================================+
| Input0/InputSignal | Audio   | Input signal that will have its frequency shifted                                            |
+--------------------+---------+----------------------------------------------------------------------------------------------+
| Frequency          | Control | Frequency shift amount (percentage/sampling-rate). Available only in Data Controlled variant |
+--------------------+---------+----------------------------------------------------------------------------------------------+

Output
------

======= ===== ============================
Name    Type  Description
======= ===== ============================
Output0 Audio Outputs the processed signal
======= ===== ============================

| 
| ===== Configurable Parameters =====

+---------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter | Default Value | Range      | Function Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+===============+===============+============+=====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| Frequency     | 100           | 0 - 4000   | Maximum Percentage (%) change of input frequency, controlled by the Frequency shift slider. The actual percentage of frequency shift is dependent on the “Delay Reserved” amount                                                                                                                                                                                                                                                                                                                                                                    |
+---------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Delay         | 300           | 1 - 4000   | This control sets the number of samples of audio delay that are reserved in memory as a buffer used for the pitch shifting algorithm. Smaller delay buffers result in more discontinuities in the pitch shifted output signal, which causes some harmonic distortion. Setting this delay buffer to a very large size will result in less distortion, but at the cost of increased delay memory usage                                                                                                                                                |
+---------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Multiplier    | 1             | -100 - 100 | The slider in the middle of the cell sets the amount of pitch shift. When the slider is exactly in the middle, there will be no pitch shift. When the slider is to the right of the center, the pitch of the input signal will be shifted up in frequency. When the slider is to the left of the center, the pitch of the input signal will be shifted down in frequency. When the slider is all the way to the left or right, the pitch will be shifted by the maximum amount (down or up), as determined by the setting of the Max Shift control. |
+---------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== =================== ============= ================
Parameter Name Description         ADAU145x/146x ADSP215x/SC5xx
============== =================== ============= ================
freq           Change in frequency 8.24 Format   Single Precision
scalingfactor  pitch change factor Integer       Target Defined
============== =================== ============= ================

| 

.. |pitch.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/pitch.png
.. |pitchdatacontrolled.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/pitchdatacontrolled.png
