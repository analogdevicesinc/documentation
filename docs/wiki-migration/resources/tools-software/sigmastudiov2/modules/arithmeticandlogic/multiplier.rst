:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Multiplier
==========

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/multiplier.png
   :alt: multiplier.png

Description
-----------

| The Signal Multiply block multiplies the incoming signal with a control signal. Similarly Complex Real multiply multiplies the complex signal with the real input. This can be used for modulation or other design situations where multiply operation is needed.
| ===== Variants =====

-  Multiplier
-  Complex Real Multiply

| 
| ===== Targets Supported =====

+-----------------------+------------+------------------+---------------+------------------+
| Name                  | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=======================+============+==================+===============+==================+
| Multiplier            | B/S        | B/S              | S             | B                |
+-----------------------+------------+------------------+---------------+------------------+
| Complex Real Multiply | NA         | NA               | B             | NA               |
+-----------------------+------------+------------------+---------------+------------------+

Pins
----

Input
~~~~~

========== ======= =================================
Name       Type    Description
========== ======= =================================
Multiplier Control Control signal for multiplication
Input0     Audio   Input channel 0
========== ======= =================================

Output
~~~~~~

======= ===== ===================================================
Name    Type  Description
======= ===== ===================================================
Output0 Audio Multiplication result of corresponding input signal
======= ===== ===================================================

Configurable Parameters
-----------------------

No configurable parameters

DSP Parameters
--------------

No DSP parameters
