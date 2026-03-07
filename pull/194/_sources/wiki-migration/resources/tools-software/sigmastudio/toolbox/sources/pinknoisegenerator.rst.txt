| :doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

Pink Noise Generator
====================

| 
| This Module generates white noise and passes it through a sixth-order IIR filter with a 1/f power response.Pink noise has a power falloff of 1/f.
| |image1|
| ====Input Pins====

========= ================================== ====================
Name      Format [int/dec] - [control/audio] Function Description
========= ================================== ====================
Pin 0: NA NA                                 NA
========= ================================== ====================

| 
| ====Output Pins====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - Audio                    Output
============= ================================== ====================

| 
| ==== Grow Algorithm ==== The module does not support Add and Growth.
| ====Configuration====
| |image2|
| ^GUI Control Name^Default Value^Range^Function Description^

==== === =========== =====================================
Gain 0dB 0dB to 20dB Gain applied on the pink noise signal
==== === =========== =====================================

| 
| ====DSP Parameter Information====

+------------------+----------------------------------------------------------------------------+---------------------------------------+
| GUI Control Name | Compiler Name                                                              | Function Description                  |
+==================+============================================================================+=======================================+
| Gain             | <fc #008000>PinkNoise_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Gain</fc> | Gain applied on the pink noise signal |
+------------------+----------------------------------------------------------------------------+---------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ==== Algorithm Description ==== This Module generates white noise and passes it through a sixth-order IIR filter with a 1/f power response.Pink noise has a power falloff of 1/f.
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/pinknoisegen-tbx.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/pinknoisegen-gui2.jpg
