Log2
====

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| This module computes the log to base 2 of the incoming data.

There are 2 versions of Log2 module on ADAU144x processors.

-  Log2 (Linear Interpolation)
-  Log2 Accurate (Binary Algorithm)

ADAU145x, ADSP-214xx and ADSP-SC5xx/215xx processors support a single version of the Log2 implementation.


|image1|

Log2 (Linear Interpolation)
---------------------------

This Log2 algorithm computes the integral part of Log2 accurately. Fractional part of the Log is calculated using Linear interpolation. This algorithm takes very less cycles and less accurate.

| 
| ====Input Pins====

+-------------------+------------------------------------+------------------------------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description                     |
+===================+====================================+==========================================+
| Pin 0: Input Data | decimal - audio                    | Input data to be converted to Log base 2 |
+-------------------+------------------------------------+------------------------------------------+

| 
| ====Output Pins====

================ ================================== ====================
Name             Format [int/dec] - [control/audio] Function Description
================ ================================== ====================
Pin 0: Log value decimal - control                  log2(input)
================ ================================== ====================

Log2 Accurate (Binary Algorithm)
--------------------------------

This module uses a binary algorithm to compute the Log2. This is more accurate and takes more cycle. Number of iterations in the algorithm can be configured. Accuracy of the algorithm increases when the number of iterations is increased.

| 
| ====Input Pins====

+-------------------+------------------------------------+------------------------------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description                     |
+===================+====================================+==========================================+
| Pin 0: Input Data | decimal - audio                    | Input data to be converted to Log base 2 |
+-------------------+------------------------------------+------------------------------------------+

| 
| ====Output Pins====

================ ================================== ====================
Name             Format [int/dec] - [control/audio] Function Description
================ ================================== ====================
Pin 0: Log value decimal - control                  log2(input)
================ ================================== ====================

| 
| ====Configuration==== Right Click on the module to configure the number of iterations.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/log10_2.jpg
   :align: center

Log2 on ADSP-213xx, ADSP-214xx, ADSP-215xx and ADSP-SC5xx processors
--------------------------------------------------------------------

Input Pins
~~~~~~~~~~

+-------------------+--------------------------------------+------------------------------------------+
| Name              | Format [int/dec] - [control/audio]   | Function Description                     |
+===================+======================================+==========================================+
| Pin 0: Input Data | decimal(ADAU145x) - audio            | Input data to be converted to Log base 2 |
|                   | float(ADSP-214xx/ADSP-215xx) - audio |                                          |
+-------------------+--------------------------------------+------------------------------------------+

Output Pins
~~~~~~~~~~~

+------------------+----------------------------------------+----------------------+
| Name             | Format [int/dec] - [control/audio]     | Function Description |
+==================+========================================+======================+
| Pin 0: Log value | decimal(ADAU145x) - control            | log2(input)          |
|                  | float(ADSP-214xx/ADSP-215xx) - control |                      |
+------------------+----------------------------------------+----------------------+

Grow Algorithm
~~~~~~~~~~~~~~

The module supports Add functionality. Growth is not supported.

GUI Controls
~~~~~~~~~~~~

None

DSP Parameter Information
~~~~~~~~~~~~~~~~~~~~~~~~~

None

Algorithm Description
~~~~~~~~~~~~~~~~~~~~~

log2(x) is implemented as (ln(x) / ln(2)) using the change of base formula. ln(x) is implemented using the taylor series expansion.

Supported IC's
~~~~~~~~~~~~~~

| 1. ADSP-213xx
| 2. ADSP-214xx
| 3. ADSP-SC5xx
| 4. ADSP-215xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/log2.jpg
