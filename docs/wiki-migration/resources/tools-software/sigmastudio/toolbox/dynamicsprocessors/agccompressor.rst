| :doc:`Click here to return to the dynamics processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`

AGC compressor core
===================

| 
| This Module is the gain computation part of a compressor. Compression happens by taking the RMS of i/p samples i.e. by passing the input samples through a low-pass filter, converting this to dB scale and then looking up the corresponding gain value. There is a threshold set as a parameter in the Module, below which compression occurs.
| |image1|
| ====Input Pins====

============ ================================== ====================
Name         Format [int/dec] - [control/audio] Function Description
============ ================================== ====================
Pin 0: Input decimal - Audio                    Input
============ ================================== ====================

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

+-------------+------+--------------+-----------------------------------------------------------------------+
| Decay       | 20ms | 20 to 100ms  | Decay coefficient of the compressor                                   |
+-------------+------+--------------+-----------------------------------------------------------------------+
| Attack time | 20ms | 20 to 100ms  | Attack coefficient of the compressor                                  |
+-------------+------+--------------+-----------------------------------------------------------------------+
| ratio       | 1    | 1 to 100     | The ratio is ratio of the gain reduction below the threshold          |
+-------------+------+--------------+-----------------------------------------------------------------------+
| Gain        | 0dB  | -120 to 20dB | The make-up gain of the compressor, in dB                             |
+-------------+------+--------------+-----------------------------------------------------------------------+
| Thr         | 0dB  | -80 to 20dB  | The compression threshold, in dB, below which compression takes place |
+-------------+------+--------------+-----------------------------------------------------------------------+

| 
| ====DSP Parameter Information====

+------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                              | Function Description                                                  |
+==================+============================================================================================+=======================================================================+
| Decay            | <fc #008000>AGCCompressorCore_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Decay</fc>        | Decay coefficient of the compressor                                   |
+------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| SmoothDecay      | <fc #008000>AGCCompressorCore_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>SmoothDecay</fc>  | Decay smooth coefficient of the compressor                            |
+------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Attack           | <fc #008000>AGCCompressorCore_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Decay</fc>        | Attack coefficient of the compressor                                  |
+------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| SmoothAttack     | <fc #008000>AGCCompressorCore_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>SmoothAttack</fc> | Attack smooth coefficient of the compressor                           |
+------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| ratio            | <fc #008000>AGCCompressorCore_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>ratio</fc>        | The ratio is ratio of the gain reduction below the threshold          |
+------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Gain             | <fc #008000>AGCCompressorCore_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Gain</fc>         | The make-up gain of the compressor, in dB                             |
+------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Threshold        | <fc #008000>AGCCompressorCore_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Threshold</fc>    | The compression threshold, in dB, below which compression takes place |
+------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ==== Algorithm Description ==== This Module is the gain computation part of a compressor. Compression happens by taking the RMS of i/p samples i.e. by passing the input samples through a low-pass filter, converting this to dB scale and then looking up the corresponding gain value. There is a threshold set as a parameter in the Module, below which compression occurs.
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/agc_compressor_core-tbx.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/agccompressor-gui.jpg
