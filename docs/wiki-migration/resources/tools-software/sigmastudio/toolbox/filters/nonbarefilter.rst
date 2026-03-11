:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`

Non Bare Filter
===============

NonBare filters are second order filters which take the parameters directly. The filter parameters are converted to filter coefficients by the Module itself. Regalia-Mitra algorithm is used for this implementation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/nonbare-tbx.jpg

Input Pins
----------

============ ================================== ====================
Name         Format [int/dec] - [control/audio] Function Description
============ ================================== ====================
Pin 0: Input decimal - Audio                    Audio input
============ ================================== ====================


| ====Output Pins====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - Audio                    Filtered output
============= ================================== ====================


| ==== Grow Algorithm ==== The module does not support Add and Growth.

Configuration
-------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/nonbare-gui.jpg

+------------------+---------------+---------------+----------------------------------------+
| GUI Control Name | Default Value | Range         | Function Description                   |
+==================+===============+===============+========================================+
| Gain             | 0dB           | -15 to 15dB   | Gain of the filter in DB               |
+------------------+---------------+---------------+----------------------------------------+
| Qvalue           | 1.71          | 0.04 to 16    | Quiscent factor of the filter          |
+------------------+---------------+---------------+----------------------------------------+
| K                | 1             | 0.04 to 16    | K values as described in the algorithm |
+------------------+---------------+---------------+----------------------------------------+
| fc               | 100           | 1 to 24000 Hz | Cut-off frequency of the filter        |
+------------------+---------------+---------------+----------------------------------------+

| 
| ====DSP Parameter Information====

+------------------+------------------------+----------------------------------------+
| GUI Control Name | Compiler Name          | Function Description                   |
+==================+========================+========================================+
| fc               | NonBare_SC5xxAlg1fc    | Cut-off frequency of the filter        |
+------------------+------------------------+----------------------------------------+
| Omega            | NonBare_SC5xxAlg1Omega | Quiscent factor of the filter          |
+------------------+------------------------+----------------------------------------+
| Gain             | NonBare_SC5xxAlg1Gain  | Gain of the filter in DB               |
+------------------+------------------------+----------------------------------------+
| K                | NonBare_SC5xxAlg1K     | K values as described in the algorithm |
+------------------+------------------------+----------------------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name
-   Brown - Stage number

Algorithm Description
---------------------

NonBare filters are second order filters which take the parameters directly. The filter parameters are converted to filter coefficients by the Module itself. Regalia-Mitra algorithm is used for this implementation.

Supported ICs
-------------

-  ADSP215xx
-  ADSPSC5xx
