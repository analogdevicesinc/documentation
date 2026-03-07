:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

One Shot Rise
=============

| 
| |oneshotrise.png| |oneshotraisereset.png|

Description
-----------

| The One Shot Rise block outputs a trigger signal based upon the rising edge of the input signal. At the first non-zero rising edge of the input signal, the output signal will go high and remain high. For One Shot Raise Reset block the output signal will remain high until a non-zero input signal is seen on the rest pin. The reset pin clears the output back to zero and will maintain the output at zero while the signal on the reset pin is non-zero.
| If the input signal starts high, the output signal will start and remain high.
| ===== Variants =====

-  One Shot Rise
-  One Shot Rise Reset

| 
| ===== Targets Supported =====

+------------------+------------+------------------+---------------+------------------+
| Name             | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==================+============+==================+===============+==================+
| OneShotRise      | B/S        | B/S              | S             | B                |
+------------------+------------+------------------+---------------+------------------+
| OneShotRiseReset | B/S        | B/S              | S             | B                |
+------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+-------+---------+--------------------------------------------------------------------------+
| Name  | Type    | Description                                                              |
+=======+=========+==========================================================================+
| Input | Audio   | Input signal that is monitored for the first falling edge                |
+-------+---------+--------------------------------------------------------------------------+
| Reset | Control | Resets the output trigger signal back to zero(only for OneShotRiseReset) |
+-------+---------+--------------------------------------------------------------------------+

Output
~~~~~~

====== ======= ========================================
Name   Type    Description
====== ======= ========================================
Output Control Sets bit position of the output “1” flag
====== ======= ========================================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------+--------------------------------------+
| GUI Parameter Name | Default Value | Range  | Function Description                 |
+====================+===============+========+======================================+
| Selected Bit       | Bit:0         | Bit:30 | Sets bit position of Output'1' Flag. |
+--------------------+---------------+--------+--------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+--------------------------------------+------------------------+-------------+
| Parameter Name | Description                          | ADSP-214xx/215xx/SC5xx | ADAU145x/6x |
+================+======================================+========================+=============+
| BitVal         | Compute & set the bit position value | FixInt32               | FixInt32    |
+----------------+--------------------------------------+------------------------+-------------+

| 

.. |oneshotrise.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/oneshotrise.png
.. |oneshotraisereset.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/oneshotraisereset.png
