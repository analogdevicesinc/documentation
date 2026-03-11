:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

Pink Noise Generator
====================

This Module generates white noise and passes it through a sixth-order IIR filter with a 1/f power response.Pink noise has a power falloff of 1/f.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/pinknoisegen-tbx.jpg

Input Pins
----------

========= ================================== ====================
Name      Format [int/dec] - [control/audio] Function Description
========= ================================== ====================
Pin 0: NA NA                                 NA
========= ================================== ====================


| ====Output Pins====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - Audio                    Output
============= ================================== ====================


| ==== Grow Algorithm ==== The module does not support Add and Growth.

Configuration
-------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/pinknoisegen-gui2.jpg

+------------------+---------------+-------------+---------------------------------------+
| GUI Control Name | Default Value | Range       | Function Description                  |
+==================+===============+=============+=======================================+
| Gain             | 0dB           | 0dB to 20dB | Gain applied on the pink noise signal |
+------------------+---------------+-------------+---------------------------------------+

| 
| ====DSP Parameter Information====

+------------------+-------------------------+---------------------------------------+
| GUI Control Name | Compiler Name           | Function Description                  |
+==================+=========================+=======================================+
| Gain             | PinkNoise_SC5xxAlg1Gain | Gain applied on the pink noise signal |
+------------------+-------------------------+---------------------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name

Algorithm Description
---------------------

This Module generates white noise and passes it through a sixth-order IIR filter with a 1/f power response.Pink noise has a power falloff of 1/f.

Supported ICs
-------------

-  ADSP215xx
-  ADSPSC5xx
