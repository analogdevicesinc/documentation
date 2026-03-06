:doc:`Click here to return to the Mixers and Splitters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mixersandsplitters>`

Single Control Splitter
=======================

| 
| |singlectrlsplitter.png|

Description
-----------

| This Single Control Splitter block splits one input into multiple outputs, with a single knob control for all the output gains.
| ===== Usage ===== To set the output gain, click the knob with the left mouse button and drag while holding down the button. The knob's range, value, and step size can be customized in the control pop-up window. To change the knob's settings, right-click on the knob control.
| ===== Varaints =====

::

   -Single Control Splitter (No Slew)
   -Single Control Splitter (SW Slew)
   -Single Control Splitter (HW Slew)

| 
| ===== Targets Supported =====

+-----------------------------------+------------+------------------+---------------+------------------+
| Name                              | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===================================+============+==================+===============+==================+
| Single Control Splitter (No Slew) | B/S        | B/S              | S             | B                |
+-----------------------------------+------------+------------------+---------------+------------------+
| Single Control Splitter (SW Slew) | S          | S                | NA            | B                |
+-----------------------------------+------------+------------------+---------------+------------------+
| Single Control Splitter (HW Slew) | NA         | NA               | S             | NA               |
+-----------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

===== ===== =============
Name  Type  Description
===== ===== =============
Input Audio Input channel
===== ===== =============

Output
~~~~~~

======================== ======= ================
Name                     Type    Description
======================== ======= ================
Output<fc #ff0000>X</fc> Control Output channel X
======================== ======= ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+----------------+-------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range          | Function Description                                                    |
+====================+===============+================+=========================================================================+
| Gain               | 0 dB          | -200 to 200 dB | Gain factor                                                             |
+--------------------+---------------+----------------+-------------------------------------------------------------------------+
| NumChannels        | 2             | 20             | Number of output channels. Change in this value requires re-compilation |
+--------------------+---------------+----------------+-------------------------------------------------------------------------+
| SlewType           | RC Slew       | NA             | Slew type. Applicable to HW slew modules                                |
+--------------------+---------------+----------------+-------------------------------------------------------------------------+
| CustomVal          | 0x208A        | NA             | Custom slew value. Applicable to HW slew modules                        |
+--------------------+---------------+----------------+-------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+----------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                        | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+====================================================+========================+===============+
| Gain           | scaling of the Gain                                | Float                  | FixPoint8d24  |
+----------------+----------------------------------------------------+------------------------+---------------+
| slew_mode      | Slew mode and value for HW slew (only for HW slew) | NA                     | Integer       |
+----------------+----------------------------------------------------+------------------------+---------------+

| 

.. |singlectrlsplitter.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/singlectrlsplitter.png
