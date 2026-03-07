Binary to Decimal
=================

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| \|\| This module can be used to considers input signals are binary and gives a decimal output value.
| |image1|
| ===== Input Pins =====

============ ================================== ====================
Name         Format [int/dec] - [control/audio] Function Description
============ ================================== ====================
Pin 0: Bit 0 int- control                       Bit 0 of input
Pin 1: Bit 1 int- control                       Bit 1 of input.
============ ================================== ====================

| 
| ===== Output Pins =====

+---------------+------------------------------------+---------------------------------+
| Name          | Format [int/dec] - [control/audio] | Function Description            |
+===============+====================================+=================================+
| Pin 0: Output | int - control                      | Decimal value as integer (32.0) |
+---------------+------------------------------------+---------------------------------+

| 

Grow Algorithm
--------------

| The module supports growth of input Pins.

Example Usage
-------------

| This module can be used with GPIOs to convert the multiple GPIO's value into a single integer value.
| |image2| The table below shows the input and output value for the BinToDec module.

====== ====== ====================== ==========================
GPIO_0 GPIO_1 BinToDec Output (32.0) Lookup Table Output (8.24)
====== ====== ====================== ==========================
0      0      0                      0 db
1      0      1                      1 db
0      1      2                      2 db
1      1      3                      3 db
====== ====== ====================== ==========================

| 
| The output of BinToDec is used as an index for LookUp table. The output of the lookup table can be multiplied with the audio signal as the gain.

Using this schematic signal's volume can be changed through GPIO.

Supported ICs
-------------

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/bintodec.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/bintodec1.jpg
