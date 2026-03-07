:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Signal Multiply
===============

| 
| |mult.png|

Description
-----------

| The Signal Multiply block multiplies two incoming signals together. This can be used for modulation or other design situations where multiply operation is needed.

Variants
--------

-  Signal Multiply
-  Scalar Multiply
-  Complex Signal Multiply

Targets Supported
-----------------

+-------------------------+------------+------------------+---------------+------------------+
| Name                    | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=========================+============+==================+===============+==================+
| Signal Multiply         | B/S        | B/S              | B/S           | B                |
+-------------------------+------------+------------------+---------------+------------------+
| Scalar Multiply         | NA         | NA               | B             | NA               |
+-------------------------+------------+------------------+---------------+------------------+
| Complex Signal Multiply | NA         | NA               | B             | NA               |
+-------------------------+------------+------------------+---------------+------------------+

Pins
----

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input channel 0
Input1 Audio Input channel 1
====== ===== ===============

Output
~~~~~~

====== ===== ==========================================
Name   Type  Description
====== ===== ==========================================
Result Audio Multiplication result of all input signals
====== ===== ==========================================

Configurable Parameters
-----------------------

No configurable parameters

DSP Parameters
--------------

No DSP parameters

.. |mult.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/mult.png
