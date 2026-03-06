:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gain>`

Gain
====

| 
| |gain.png|
| ===== Variants =====

-  Gain (No Slew)
-  Gain (Clickless SW Slew)
-  Gain (HW Slew)
-  Gain (RC Accurate)
-  Complex Gain (No Slew)
-  Multiple Control Gain

Description
-----------

| The Gain block scales the input signal by the specified value in the text field.
| The value (Linear) specified in the textbox is the multiplication factor. The value of “1” will not change the gain value and the value of “0” will mute the audio. The value of “2” will double the signal level (adds 6dB) and the value of “-2” will invert the polarity and double the signal level (adds -6dB). If the value is between 1 and 0, the signal level will decrease. You can choose a slew or no-slew algorithm. Using slew RAM gradually ramps the signal from original to target value, while using no-slew RAM jumps the signal immediately.
| The Multiple Control Gain module has separate gain for each of the inputs.
| ===== Usage ===== Linear or dB value can be entered by clicking on "Lin" or "dB" selection on the UI ( Multiple Control Gain has Linear input only)

Targets Supported
-----------------

+--------------------------+------------+------------------+---------------+------------------+
| Name                     | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==========================+============+==================+===============+==================+
| Gain (No Slew)           | B/S        | B/S              | B/S           | B                |
+--------------------------+------------+------------------+---------------+------------------+
| Gain (Clickless SW Slew) | B/S        | B/S              | NA            | B                |
+--------------------------+------------+------------------+---------------+------------------+
| Gain (HW Slew)           | NA         | NA               | S             | NA               |
+--------------------------+------------+------------------+---------------+------------------+
| Gain (RC Accurate)       | NA         | NA               | S             | NA               |
+--------------------------+------------+------------------+---------------+------------------+
| Complex Gain (No Slew)   | NA         | NA               | B             | NA               |
+--------------------------+------------+------------------+---------------+------------------+
| Multiple Control Gain    | NA         | NA               | S             | NA               |
+--------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+-------------------------+-------------------------------------+-----------------+
| Name                    | Type                                | Description     |
+=========================+=====================================+=================+
| Input<fc #ff0000>X</fc> | Audio(Complex pin for Complex Gain) | Input channel X |
+-------------------------+-------------------------------------+-----------------+

Output
~~~~~~

+--------------------------+-------------------------------------+------------------+
| Name                     | Type                                | Description      |
+==========================+=====================================+==================+
| Output<fc #ff0000>X</fc> | Audio(Complex pin for Complex Gain) | Output channel X |
+--------------------------+-------------------------------------+------------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------+----------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                                                                                     |
+====================+===============+==============+==========================================================================================================+
| Gain               | 1             | -128 to 128  | Scales the input signal by the specified gain                                                            |
+--------------------+---------------+--------------+----------------------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 1 to 20      | Number of input channels. Change in this value requires re-compilation(only for growth supported module) |
+--------------------+---------------+--------------+----------------------------------------------------------------------------------------------------------+
| IsDB               | True          | True / False | Controls the gain control is either in dB or linear scale                                                |
+--------------------+---------------+--------------+----------------------------------------------------------------------------------------------------------+
| SlewType           | RC Slew       | NA           | Slew type. Applicable to HW slew modules                                                                 |
+--------------------+---------------+--------------+----------------------------------------------------------------------------------------------------------+
| CustomVal          | 0x208A        | NA           | Custom slew value. Applicable to HW slew modules                                                         |
+--------------------+---------------+--------------+----------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+---------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===============================================================+========================+===============+
| Gain           | Scales the input signal by the specified gain                 | Float                  | FixPoint8d24  |
+----------------+---------------------------------------------------------------+------------------------+---------------+
| SlewStep       | Smoothness for scaling the signal (only in Clickless SW Slew) | Float                  | NA            |
+----------------+---------------------------------------------------------------+------------------------+---------------+
| slew_mode      | Slew mode and value for HW slew (only for HW slew)            | NA                     | Integer32     |
+----------------+---------------------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== Gain(Linear) = 10^(Gain(dB)/20)

.. |gain.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/gain.png
