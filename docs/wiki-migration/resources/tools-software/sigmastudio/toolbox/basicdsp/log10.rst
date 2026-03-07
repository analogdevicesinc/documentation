Log10
=====

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| There are 2 versions of Log10 module.

-  Log10 (Linear Interpolation)
-  Log10 Accurate (Binary Algorithm)

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/log10.jpg
   :align: center

Log10 (Linear Interpolation)
----------------------------

This Log10 algorithm computes the integral part of Log2 accurately. Fractional part of the Log is calculated using Linear interpolation. Then the Log2 is multiplied with Log10(2)to get the Log10. This algorithm takes less cycles and less accurate.

| 
| ====Input Pins====

+-------------------+------------------------------------+-------------------------------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description                      |
+===================+====================================+===========================================+
| Pin 0: Input Data | decimal - audio                    | Input data to be converted to Log base 10 |
+-------------------+------------------------------------+-------------------------------------------+

| 
| ====Output Pins====

================ ================================== ====================
Name             Format [int/dec] - [control/audio] Function Description
================ ================================== ====================
Pin 0: Log value decimal - control                  log10(input)
================ ================================== ====================

Log10 Accurate (Binary Algorithm)
---------------------------------

This module uses a binary algorithm to compute the Log2. Then the Log2 is multiplied with Log10(2)to get the Log10. This is more accurate and takes more cycle. Number of iterations in the algorithm can be configured. Accuracy of the algorithm increases when the number of iterations is increased.

| 
| ====Input Pins====

+-------------------+------------------------------------+-------------------------------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description                      |
+===================+====================================+===========================================+
| Pin 0: Input Data | decimal - audio                    | Input data to be converted to Log base 10 |
+-------------------+------------------------------------+-------------------------------------------+

| 
| ====Output Pins====

================ ================================== ====================
Name             Format [int/dec] - [control/audio] Function Description
================ ================================== ====================
Pin 0: Log value decimal - control                  log10(input)
================ ================================== ====================

| 
| ====Configuration==== Right Click on the module to configure the number of iterations.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/log10_2.jpg
   :align: center
