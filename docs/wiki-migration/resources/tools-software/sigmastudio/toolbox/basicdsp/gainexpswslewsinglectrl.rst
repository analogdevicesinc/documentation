| :doc:`Click here to return to the basicdsp page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

Gain Exp SW slew Single Control
===============================

| 
| This gain module applies the specified gain to the input audio signal. When the gain value is changed the previously applied gain slews to the target value determined by the values of the Gain increment and the Gain decrement.
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
Pin 0: Output decimal - Audio                    Audio Output
============= ================================== ====================

| 
| ==== Grow Algorithm ==== This module shall support channel growth minimum of 1 and maximum of 12. Each growth will add 1 input and 1 output pin. Module shall support single control and common parameters for processing of each input signal.
| ====Configuration====
| |image2|
| ^GUI Control Name^Default Value^Range^Function Description^

+---------+-----------+----------+---------------------------------------------------+
| Gain    | 1         | 0 to 128 | input gain value in linear scale between 0 to 128 |
+---------+-----------+----------+---------------------------------------------------+
| G_Thres | 0.0000158 | 0 to 1   | input gain threshold value between 0 to 1         |
+---------+-----------+----------+---------------------------------------------------+
| G_Inc   | 1.0008    | 1 to 128 | input gain increment value between 1 to 128       |
+---------+-----------+----------+---------------------------------------------------+
| G_Dec   | 0.9992    | 0 to 1   | input gain decrement value between 0 to 1         |
+---------+-----------+----------+---------------------------------------------------+

| 
| ====DSP Parameter Information====

+------------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                             | Function Description                                                                                                                        |
+==================+===========================================================================================+=============================================================================================================================================+
| Gain             | <fc #008000>Gain_Exp_SW_Slew_SingleCtrlAlg</fc><fc #ff0000>1</fc><fc #000080>Gain</fc>    | Target gain set in the GUI, the value can be varied between 0 to 128.                                                                       |
+------------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| G_Thres          | <fc #008000>Gain_Exp_SW_Slew_SingleCtrlAlg</fc><fc #ff0000>1</fc><fc #000080>G_Thres</fc> | Threshold gain value to maintain current gain value close to zero, but not less than or equal zero. The value can be varied between 0 to 1. |
+------------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| G_Inc            | <fc #008000>Gain_Exp_SW_Slew_SingleCtrlAlg</fc><fc #ff0000>1</fc><fc #000080>G_Inc</fc>   | The gain increment factor for exponential slew,the value can be varied between 1 to 128.                                                    |
+------------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| G_Dec            | <fc #008000>Gain_Exp_SW_Slew_SingleCtrlAlg</fc><fc #ff0000>1</fc><fc #000080>G_Dec</fc>   | The gain decrement factor for exponential slew, the value can be varied between 0 to 1.                                                     |
+------------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000>Brown</fc> - Stage number

| 
| ==== Algorithm Description ==== This gain module applies the specified gain to the input audio signal. When the gain value is changed the previously applied gain slews to the target value determined by the values of the Gain increment and the Gain decrement. The Gain increment value determines the amount of time the module takes to reach a gain value greater than the current value, while the gain decrement value determines the amount of time the module takes to reach a gain value lesser than the current. The Gain threshold is used to specify the value below which the gain immediately reduces to 0.
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/gainslew-tbx.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/gainslew-gui.jpg
