| :doc:`Click here to return to the basic dsp page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

Scaler
======

| 
| This Module applies linear amplitude scaling to an input mono signal and multiplies the input signal by a scaling parameter as in equation: Yn= amp.Xn
| |image1|
| ====Input Pins====

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
| ==== Grow Algorithm ==== The module supports Growth. The module does not support Add.
| ====Configuration====
| |image2|
| ^GUI Control Name^Default Value^Range^Function Description^

=== = ======= ==========================================
Amp 1 -1 to 1 liner amplitude gain applied on the signal
=== = ======= ==========================================

| 
| ====DSP Parameter Information====

+------------------+------------------------------------------------------------------------------------------+---------------------------------------+
| GUI Control Name | Compiler Name                                                                            | Function Description                  |
+==================+==========================================================================================+=======================================+
| Amp              | <fc #008000>Scaler_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Amp</fc><fc #800000>1</fc> | Gain applied on the pink noise signal |
+------------------+------------------------------------------------------------------------------------------+---------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000>Brown</fc> - Stage number

| 
| ==== Algorithm Description ==== This Module applies linear amplitude scaling to an input mono signal and multiplies the input signal by a scaling parameter as in equation: Yn= amp.Xn
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scaler-tbx.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scaler-gui.jpg
