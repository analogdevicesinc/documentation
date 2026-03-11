:doc:`Click here to return to the filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`

Biquad 3 channel 1 cascade
==========================

This 3 channel Infinite Impulse Response (IIR) filter consists of a single Biquad section, five coefficients, and Direct-Form-2 implementation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/biquad3ch1-tbx.jpg

Input Pins
----------

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Input1 decimal - Audio                    Audio ch1 Input
Pin 1: Input1 decimal - Audio                    Audio ch2 Input
Pin 2: Input1 decimal - Audio                    Audio ch3 Input
============= ================================== ====================


| ====Output Pins====

============== ================================== ====================
Name           Format [int/dec] - [control/audio] Function Description
============== ================================== ====================
Pin 0: Output  decimal - Audio                    Filtered ch1 Output
Pin 1: Output1 decimal - Audio                    Filtered ch2 Output
Pin 2: Output2 decimal - Audio                    Filtered ch3 Output
============== ================================== ====================


| ==== Grow Algorithm ==== The module does not support Add and Growth.

Configuration
-------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/biquad3ch1-gui.jpg

+------------------+---------------+--------+-------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range  | Function Description                                                                      |
+==================+===============+========+===========================================================================================+
| Enable           | off           | on/off | Enables filtering, when disabled audio output is 0                                        |
+------------------+---------------+--------+-------------------------------------------------------------------------------------------+
| Coefficients     | NA            | NA     | A table containing the user entered IIR filter coefficients (in order d1, d2, n0, n1, n2) |
+------------------+---------------+--------+-------------------------------------------------------------------------------------------+

| 
| ====DSP Parameter Information====

+------------------+----------------------------------------+-------------------------------------------------------------+
| GUI Control Name | Compiler Name                          | Function Description                                        |
+==================+========================================+=============================================================+
| Coefficients     | BiquadCascade3ch1_SC5xxAlg1Coeffs_3ch1 | IIR filter coefficients entered in the order b1,b2,a0,a1,a2 |
+------------------+----------------------------------------+-------------------------------------------------------------+
| Enable           | BiquadCascade3ch1_SC5xxAlg1Enable      | Enables filtering                                           |
+------------------+----------------------------------------+-------------------------------------------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name

Algorithm Description
---------------------

3 channel Infinite Impulse Response (IIR) filter consists of a single Biquad section, five coefficients, and Direct-Form-2 implementation. The transfer function is as shown below

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/biquad3ch1-tf.jpg

Supported ICs
-------------

-  ADSP215xx
-  ADSPSC5xx
