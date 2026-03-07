:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Trigonometry
============

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/trigonometry.png
   :alt: trigonometry.png

Description
-----------

| This Module implements the basic trigonometric functions such as sine, cosine, tan, inverse sine, inverse cosine, inverse tan. This Module can be grown. When grown, both control and input, output pins are grown.

Targets Supported
-----------------

============ ========== ================ ============= ================
Name         ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============ ========== ================ ============= ================
Trigonometry B          B                NA            B
============ ========== ================ ============= ================

Pins
----

Input
~~~~~

===== ===== =============
Name  Type  Description
===== ===== =============
Input Audio Input channel
===== ===== =============

Output
~~~~~~

====== ===== ==============
Name   Type  Description
====== ===== ==============
Output Audio Output channel
====== ===== ==============

Configurable Parameters
-----------------------

================== ============= ========= ==========================
GUI Parameter Name Default Value Range     Function Description
================== ============= ========= ==========================
Operation          Sin           NA        Trigonometric Operation
Input Gain         1             -16 -> 16 Gain applied on the input
Phase              0             0 -> 360  Phase of the input
Output Gain        1             -16 -> 16 Gain applied on the output
Offset             0             -16 -> 16 Offset of the output
================== ============= ========= ==========================

DSP Parameters
--------------

============== ========================== ======================
Parameter Name Description                ADSP-214xx/SC5xx/215xx
============== ========================== ======================
Operation      Trigonometric Operation    Float
Input Gain     Gain applied on the input  Float
Phase          Phase of the input         Float
Output Gain    Gain applied on the output Float
Offset         Offset of the output       Float
============== ========================== ======================
