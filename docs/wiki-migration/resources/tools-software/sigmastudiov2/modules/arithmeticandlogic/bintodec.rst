:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Binary to Decimal
=================

| |bintodec.png|
| ===== Description ===== The Absolute Value block coverts all input signals that are binary to decimal.
| ===== Targets Supported =====

+----------------+------------+------------------+---------------+------------------+
| Name           | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================+============+==================+===============+==================+
| Bin to Decimal | NA         | NA               | S/B           | NA               |
+----------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

====== =========== ===========
Name   Type        Description
====== =========== ===========
Input0 Int-Control Input Bit 0
Input1 Int-Control Input Bit 1
====== =========== ===========

Output
------

====== ======= ========================
Name   Type    Description
====== ======= ========================
Output Control Output Decimal(int 32.0)
====== ======= ========================

Configurable Parameters
~~~~~~~~~~~~~~~~~~~~~~~

| NumChannels: Module supports growth of input pins.
| ===== Example Usage ===== This module can be used with GPIOs to convert the multiple GPIO's value into a single integer value.
| ^GPIO_0 ^ GPIO_1^ BinToDec Output (32.0) ^ Lookup Table Output (8.24)^

= = = ====
0 0 0 0 db
1 0 1 1 db
0 1 2 2 db
1 1 3 3 db
= = = ====

| 
| ===== DSP Parameters ===== NO DSP parameters

.. |bintodec.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/bintodec.png
