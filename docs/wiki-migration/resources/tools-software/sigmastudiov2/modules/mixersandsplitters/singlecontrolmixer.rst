:doc:`Click here to return to the Mixers and Splitters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mixersandsplitters>`

Single Control Mixer
====================

| 
| |scmixer.png|

Description
-----------

| The Single Control Mixer lets you mix multiple inputs down to one output, with a single knob to set the gain of all inputs.
| ===== Usage ===== To set the output gain, click the knob with the left mouse button and drag while holding down the button. The knob's range, value, and step size can be customized in the control pop-up window. To change the knob's settings, right-click on the knob control.
| ===== Varaints =====

::

   -Single Control Mixer (No Slew)
   -Single Control Mixer (SW Slew)
   -Single Control Mixer (HW Slew)
   -Complex Single Control Mixer

| 
| ===== Targets Supported =====

+--------------------------------+------------+------------------+---------------+------------------+
| Name                           | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================================+============+==================+===============+==================+
| Single Control Mixer (No Slew) | B/S        | B/S              | B/S           | B                |
+--------------------------------+------------+------------------+---------------+------------------+
| Single Control Mixer (SW Slew) | S          | B/S              | NA            | NA               |
+--------------------------------+------------+------------------+---------------+------------------+
| Single Control Mixer (HW Slew) | NA         | NA               | S             | NA               |
+--------------------------------+------------+------------------+---------------+------------------+
| Complex Single Control Mixer   | NA         | NA               | B             | NA               |
+--------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+--------------------------+--------------------------------------+-----------------+
| Name                     | Type                                 | Description     |
+==========================+======================================+=================+
| Input <fc #ff0000>X</fc> | Audio(ComplexPin for complex module) | Input channel X |
+--------------------------+--------------------------------------+-----------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

Output
~~~~~~

====== ====================================== ================
Name   Type                                   Description
====== ====================================== ================
Output Control(ComplexPin for complex module) Output channel 0
====== ====================================== ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+----------------+------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range          | Function Description                                                   |
+====================+===============+================+========================================================================+
| Gain               | 0 dB          | -200 to 200 dB | Gain factor                                                            |
+--------------------+---------------+----------------+------------------------------------------------------------------------+
| NumChannels        | 2             | 20             | Number of input channels. Change in this value requires re-compilation |
+--------------------+---------------+----------------+------------------------------------------------------------------------+
| SlewType           | RC Slew       | NA             | Slew type. Applicable to HW slew modules                               |
+--------------------+---------------+----------------+------------------------------------------------------------------------+
| CustomVal          | 0x208A        | NA             | Custom slew value. Applicable to HW slew modules                       |
+--------------------+---------------+----------------+------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+----------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                        | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+====================================================+========================+===============+
| Gain           | scaling of the inputs                              | Float                  | FixPoint8d24  |
+----------------+----------------------------------------------------+------------------------+---------------+
| slew_mode      | Slew mode and value for HW slew (only for HW slew) | NA                     | Integer       |
+----------------+----------------------------------------------------+------------------------+---------------+

| 

.. |scmixer.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/scmixer.png
