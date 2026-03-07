:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

One Shot Fall
=============

| 
| |oneshotfall.png| |oneshotfallreset.png|

Description
-----------

| The One Shot Fall block outputs a trigger signal based upon the falling edge of the input signal. At the first falling edge of the input signal, the output signal will go high and remain high.In One Shot Fall Reset The output signal will remain high until a non-zero input signal is seen on the reset pin. The falling edge of the input signal is defined as any input signal level value changing to a lower signal level value.
| ===== Variants =====

-  OneShotFall
-  OneShotFallReset

| 
| ===== Targets Supported =====

+------------------+------------+------------------+---------------+------------------+
| Name             | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==================+============+==================+===============+==================+
| OneShotFall      | B/S        | B/S              | S             | B                |
+------------------+------------+------------------+---------------+------------------+
| OneShotFallReset | B/S        | B/S              | S             | NA               |
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
| Reset | Control | Resets the output trigger signal back to zero(only for OneShotFallReset) |
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

.. |oneshotfall.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/oneshotfall.png
.. |oneshotfallreset.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/oneshotfallreset.png
