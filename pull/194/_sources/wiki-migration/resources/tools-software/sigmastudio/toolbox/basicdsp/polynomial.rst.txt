Polynomial
==========

:doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

| 
| |polynomial.png|

Description
-----------

| The Polynomial block computes the polynomial equation of (N - 1)th order.Where N specifies in the text field.
| ===== Usage ===== Enter the order of the equation in the text field and to open the table editor to enter the coefficients, click on the table button. if N = 5, This block computes the polynomial equation of 4th order.The table editor contains 5 coefficients and those are in the order of a0,a1,a2,a3, and a4 respectively.
| ===== Variants ===== 1. SinglePrecision
| 2. ExtendedPrecision

Targets Supported
-----------------

================= =============== ================ =============
Name              ADSP-214xx      ADSP-215xx/SC5xx ADAU145x/146x
================= =============== ================ =============
SinglePrecision   Block/Schematic Block/Schematic  NA
ExtendedPrecision Block/Schematic Block/Schematic  NA
================= =============== ================ =============

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

+--------------------+-----------------+-----------------+--------------------------------------------------------+
| GUI Parameter Name | Default Value   | Range           | Function Description                                   |
+====================+=================+=================+========================================================+
| NumofTableValues   | 2               | 2 to 1000       | N -1 order of the equation                             |
+--------------------+-----------------+-----------------+--------------------------------------------------------+
| TableValues        | 1 and 2         |                 | coefficients values a0,a1                              |
+--------------------+-----------------+-----------------+--------------------------------------------------------+
| PrecsisonType      | SinglePrecision | Single/Extended | Changes the algorithm type and requires re-compilation |
+--------------------+-----------------+-----------------+--------------------------------------------------------+

DSP Parameters
--------------

================ ========================== ======================
Parameter Name   Description                ADSP-214xx/SC5xx/215xx
================ ========================== ======================
NumofTableValues N -1 order of the equation Float
TableValues      coeffcients values a0,a1   Float
================ ========================== ======================

.. |polynomial.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/polynomial.png
