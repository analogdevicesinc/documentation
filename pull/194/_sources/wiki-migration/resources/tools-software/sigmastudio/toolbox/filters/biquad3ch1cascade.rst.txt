| :doc:`Click here to return to the filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`

Biquad 3 channel 1 cascade
==========================

| 
| This 3 channel Infinite Impulse Response (IIR) filter consists of a single Biquad section, five coefficients, and Direct-Form-2 implementation.
| |image1|
| ====Input Pins====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Input1 decimal - Audio                    Audio ch1 Input
Pin 1: Input1 decimal - Audio                    Audio ch2 Input
Pin 2: Input1 decimal - Audio                    Audio ch3 Input
============= ================================== ====================

| 
| ====Output Pins====

============== ================================== ====================
Name           Format [int/dec] - [control/audio] Function Description
============== ================================== ====================
Pin 0: Output  decimal - Audio                    Filtered ch1 Output
Pin 1: Output1 decimal - Audio                    Filtered ch2 Output
Pin 2: Output2 decimal - Audio                    Filtered ch3 Output
============== ================================== ====================

| 
| ==== Grow Algorithm ==== The module does not support Add and Growth.
| ====Configuration====
| |image2|
| ^GUI Control Name^Default Value^Range^Function Description^

+--------------+-----+--------+-------------------------------------------------------------------------------------------+
| Enable       | off | on/off | Enables filtering, when disabled audio output is 0                                        |
+--------------+-----+--------+-------------------------------------------------------------------------------------------+
| Coefficients | NA  | NA     | A table containing the user entered IIR filter coefficients (in order d1, d2, n0, n1, n2) |
+--------------+-----+--------+-------------------------------------------------------------------------------------------+

| 
| ====DSP Parameter Information====

+------------------+-------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                             | Function Description                                        |
+==================+===========================================================================================+=============================================================+
| Coefficients     | <fc #008000>BiquadCascade3ch1_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Coeffs_3ch1</fc> | IIR filter coefficients entered in the order b1,b2,a0,a1,a2 |
+------------------+-------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| Enable           | <fc #008000>BiquadCascade3ch1_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Enable</fc>      | Enables filtering                                           |
+------------------+-------------------------------------------------------------------------------------------+-------------------------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ==== Algorithm Description ==== 3 channel Infinite Impulse Response (IIR) filter consists of a single Biquad section, five coefficients, and Direct-Form-2 implementation. The transfer function is as shown below
| |image3|
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/biquad3ch1-tbx.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/biquad3ch1-gui.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/biquad3ch1-tf.jpg
