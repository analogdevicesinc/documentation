| `Click here to return to the Custom Algorithms page <https://wiki.analog.com/resources/tools-software/sigmastudio/toolbox/customalgorithms>`__

Zoltzer Filter
==============

| 
| |image1|
| This is a parametric peaking equalizer filter based on the implementation of Udo Zölzer (sometimes spelled Zolzer or Zoelzer).

Variants
--------

-  1 channel single precision floating point (block)
   \* 2 channel single precision floating point (block)
   \* 8 channel single precision floating point (block)
   \* stereo single precision floating point (block)
   \* 1 channel extended precision floating point (block)
   \* 2 channel extended precision floating point (block)
   \* 8 channel extended precision floating point (block)
   \* 1 channel single precision floating point type 2 (block)
   \* 1 channel single precision floating point type 2 (block)
   \* 1 channel extended precision floating point type 2 (block)
   \* 1 channel extended precision floating point type 2(block)

Input Pins
~~~~~~~~~~

============ ================================== ====================
Name         Format [int/dec] - [control/audio] Function Description
============ ================================== ====================
Pin 0: Input decimal - Audio                    Audio Input
============ ================================== ====================

| 
| ====Output Pins====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - Audio                    Scaled Output
============= ================================== ====================

| 
| ==== Grow Algorithm ==== The module supports Growth up to 15 Pins. It also supports Add Algorithm.
| ===== Configurable Parameters =====

================== ============= ===========
GUI Parameter Name Default Value Range
================== ============= ===========
Freq               1000 Hz       1 to 30000
q                  0.71          0.001 to 20
gain               0 dB          -20 to 20
================== ============= ===========

Supported ICs
-------------

-  ADSP-214xx/SC5xx/215xx
   \* Sigma300/350

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/customalgorithms/zoltzer_filter.png
