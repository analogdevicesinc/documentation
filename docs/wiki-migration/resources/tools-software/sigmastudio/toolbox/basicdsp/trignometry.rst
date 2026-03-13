:doc:`Click here to return to the basic dsp page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

Trignometry
===========

This Module implements the basic trigonometric functions such as sine, cosine,
tan, inverse sine, inverse cosine, inverse tan. This Module can be grown. When
grown, both control and input, output pins are grown.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/trignometry-tbx.jpg

Input Pins
----------

============ ================================== ====================
Name         Format [int/dec] - [control/audio] Function Description
============ ================================== ====================
Pin 0: Input decimal - Audio                    Audio input
============ ================================== ====================

| ====Output Pins====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - Audio                    Transformed Output
============= ================================== ====================

| ==== Grow Algorithm ==== The module does not support Add and Growth.

Configuration
-------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/trignometry-gui.jpg

+------------------+---------------+-------------------+--------------------------------------------+
| GUI Control Name | Default Value | Range             | Function Description                       |
+==================+===============+===================+============================================+
| IndexIn          | 0(Sinx)       | 0 to 5            | Index of the trigonometric function needed |
+------------------+---------------+-------------------+--------------------------------------------+
| Input Gain       | 1             | -100000 to 100000 | Gain applied on the input                  |
+------------------+---------------+-------------------+--------------------------------------------+
| phase            | 0             | -100000 to 100000 | phase of the input                         |
+------------------+---------------+-------------------+--------------------------------------------+
| Output Gain      | 1             | -100000 to 100000 | Gain applied on the output                 |
+------------------+---------------+-------------------+--------------------------------------------+
| Offset           | 0             | -10000 to 10000   | Offset of the output                       |
+------------------+---------------+-------------------+--------------------------------------------+

| 

DSP Parameter Information
-------------------------

+------------------+-----------------------------------+----------------------------+
| GUI Control Name | Compiler Name                     | Function Description       |
+==================+===================================+============================+
| IndexIn          | Trignometry_SC5xxAlg1IndenIn1     | function index selected    |
+------------------+-----------------------------------+----------------------------+
| Input Gain       | Trignometry_SC5xxAlg1Input Gain1  | Gain applied on the input  |
+------------------+-----------------------------------+----------------------------+
| Phase            | Trignometry_SC5xxAlg1Phase1       | phase of the input         |
+------------------+-----------------------------------+----------------------------+
| Output Gain      | Trignometry_SC5xxAlg1Output Gain1 | Gain applied on the output |
+------------------+-----------------------------------+----------------------------+
| Offset           | Trignometry_SC5xxAlg1Offset1      | Offset of the output       |
+------------------+-----------------------------------+----------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name
-   Brown - Stage number

Algorithm Description
---------------------

This Module implements the basic trigonometric functions such as sine, cosine,
tan, inverse sine, inverse cosine, inverse tan. This Module can be grown. When
grown, both control and input, output pins are grown.

Supported ICs
-------------

-  ADSP215xx
-  ADSPSC5xx
