:doc:`Click here to return to the filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`

Biquad Cascade 8 channel 4 cascade
==================================

This Infinite Impulse Response (IIR) filter consists of a cascade of 4 Biquad sections and 8 audio input channels.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/biquad8ch4-tbx.jpg

Input Pins
----------

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Input1 decimal - Audio                    Audio ch1 Input
Pin 1: Input2 decimal - Audio                    Audio ch2 Input
Pin 2: Input3 decimal - Audio                    Audio ch3 Input
Pin 3: Input4 decimal - Audio                    Audio ch4 Input
Pin 4: Input5 decimal - Audio                    Audio ch5 Input
Pin 5: Input6 decimal - Audio                    Audio ch6 Input
Pin 6: Input7 decimal - Audio                    Audio ch7 Input
Pin 7: Input8 decimal - Audio                    Audio ch8 Input
============= ================================== ====================


| ====Output Pins====

============== ================================== ====================
Name           Format [int/dec] - [control/audio] Function Description
============== ================================== ====================
Pin 0: Output1 decimal - Audio                    Filtered ch1 Output
Pin 1: Output2 decimal - Audio                    Filtered ch2 Output
Pin 2: Output3 decimal - Audio                    Filtered ch3 Output
Pin 3: Output4 decimal - Audio                    Filtered ch4 Output
Pin 4: Output5 decimal - Audio                    Filtered ch5 Output
Pin 5: Output6 decimal - Audio                    Filtered ch6 Output
Pin 6: Output7 decimal - Audio                    Filtered ch7 Output
Pin 7: Output8 decimal - Audio                    Filtered ch8 Output
============== ================================== ====================


| ==== Grow Algorithm ==== The module does not support Add and Growth.

Configuration
-------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/biquad8ch4-gui.jpg

+------------------+---------------+--------+------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range  | Function Description                                                                                 |
+==================+===============+========+======================================================================================================+
| Enable           | off           | on/off | Enables filtering, when disabled audio output is 0                                                   |
+------------------+---------------+--------+------------------------------------------------------------------------------------------------------+
| Coefficients     | NA            | NA     | A table containing the user entered IIR filter coefficients (in order d11,d12,n10,n11,n12,d21...n42) |
+------------------+---------------+--------+------------------------------------------------------------------------------------------------------+

| 
| ====DSP Parameter Information====

+------------------+----------------------------------------+----------------------------------------------------------------------------+
| GUI Control Name | Compiler Name                          | Function Description                                                       |
+==================+========================================+============================================================================+
| Coefficients     | BiquadCascade8ch4_SC5xxAlg1Coeffs_8ch4 | IIR filter coefficients entered in the order d11,d12,n10,n11,n12,d21...n42 |
+------------------+----------------------------------------+----------------------------------------------------------------------------+
| Enable           | BiquadCascade8ch4_SC5xxAlg1Enable      | Enables filtering                                                          |
+------------------+----------------------------------------+----------------------------------------------------------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name

Algorithm Description
---------------------

This Infinite Impulse Response (IIR) filter consists of a cascade of 4 Biquad sections and 8 audio input channels. The transfer function is as shown below

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/biquad8ch4-tf.jpg

Supported ICs
-------------

-  ADSP215xx
-  ADSPSC5xx
