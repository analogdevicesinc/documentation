:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

Loudness With Filter
====================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/loudnesswfilter.png
   :alt: loudnesswfilter.png

Description
-----------

| 
| The Loudness with filter block applies the filter to the input signal and loudness will apply to the filtered signal. The loudness with the filter block gives access to a variety of filter algorithms. The available filter types are

-  Second-Order Low Shelf
-  Second-Order High Shelf
-  Second-Order Parametric
-  First-Order Low Shelf
-  First-Order High Shelf
-  Peaking

| 
| ===== Usage ===== To access the filter click on the icon button and icon button image will change to reflect the selected filter type
| ===== Targets Supported =====

+----------------------+------------+------------------+---------------+------------------+
| Name                 | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+======================+============+==================+===============+==================+
| Loudness With Filter | B          | B                | NA            | B                |
+----------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+--------------+---------+----------------------------------------------------------------------------+
| Name         | Type    | Description                                                                |
+==============+=========+============================================================================+
| ControlInput | Control | External volume controls the loudness applied to the filtered input signal |
+--------------+---------+----------------------------------------------------------------------------+
| Input0       | Audio   | Input Channel0                                                             |
+--------------+---------+----------------------------------------------------------------------------+

Output
~~~~~~

====================== ============== ======================
Name                   Type           Description
====================== ============== ======================
---------------------- -------------- ----------------------
Output0                Audio          Output channel0
====================== ============== ======================

| 
| ===== Configurable Parameters =====

+--------------------+------------------+---------------+-----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value    | Range         | Function Description                                                              |
+====================+==================+===============+===================================================================================+
| Boost              | 0dB              | -20 to 20 dB  | Set the boost value for a particular filter curve                                 |
+--------------------+------------------+---------------+-----------------------------------------------------------------------------------+
| Frequency          | 1000Hz           | 20 to 20000Hz | The cutoff frequency of the filter                                                |
+--------------------+------------------+---------------+-----------------------------------------------------------------------------------+
| Q                  | 1.4              | 0 to 15       | Q Factor of the filter                                                            |
+--------------------+------------------+---------------+-----------------------------------------------------------------------------------+
| Gain               | 0dB              | -15 to 15dB   | Gain used to calcualte the filter coefficnets                                     |
+--------------------+------------------+---------------+-----------------------------------------------------------------------------------+
| EnabledorBypassed  | True             | True/False    | Enabled/Disabled the the algorithm                                                |
+--------------------+------------------+---------------+-----------------------------------------------------------------------------------+
| Phase              | False            | False/True    | Change the phase of the filter coefficients                                       |
+--------------------+------------------+---------------+-----------------------------------------------------------------------------------+
| FilterType         | Low Shelf Filter | -             | Selects the desired filter type                                                   |
+--------------------+------------------+---------------+-----------------------------------------------------------------------------------+
| NumChannels        | 1                | 20            | Number of input and output channels. Change in this value requires re-compilation |
+--------------------+------------------+---------------+-----------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== ============== ======================
Parameter Name Description    ADSP-214xx/SC5xx/215xx
============== ============== ======================
A1             Coefficient A1 Float
A2             Coefficient A2 Float
B0             Coefficient B0 Float
B1             Coefficient B1 Float
B2             Coefficient B2 Float
============== ============== ======================
