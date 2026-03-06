:doc:`Click here to return to the Mixers and Splitters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mixersandsplitters>`

Multiple Control Splitter
=========================

| 
| |multctrlsplitter.png|

Description
-----------

| The Multiple Control Splitter allows an input signal to be split into two or more outputs with independent control of each output's gain.

Usage
-----

| There is a control knob for setting the gain or each output. To set the gain, click the knob with the left mouse button and drag while holding down the button. Each knob's range, value, and step size can be customized in the control pop-up window. To change the knob settings, right-click on the knob control
| ===== Varaints =====

::

   -Multiple Control Splitter (No Slew)
   -Multiple Control Splitter (SW Slew)
   -Multiple Control Splitter (HW Slew)

| 
| ===== Targets Supported =====

+-------------------------------------+------------+------------------+---------------+------------------+
| Name                                | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=====================================+============+==================+===============+==================+
| Multiple Control Splitter (No Slew) | B/S        | B/S              | S             | B                |
+-------------------------------------+------------+------------------+---------------+------------------+
| Multiple Control Splitter (SW Slew) | B/S        | B/S              | NA            | B                |
+-------------------------------------+------------+------------------+---------------+------------------+
| Multiple Control Splitter (HW Slew) | NA         | NA               | S             | NA               |
+-------------------------------------+------------+------------------+---------------+------------------+

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

======================== ===== ================
Name                     Type  Description
======================== ===== ================
Output<fc #ff0000>X</fc> Audio Output Channel X
======================== ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

Configurable Parameters
-----------------------

+--------------------------------+---------------+----------------+-------------------------------------------------------------------------+
| GUI Parameter Name             | Default Value | Range          | Function Description                                                    |
+================================+===============+================+=========================================================================+
| Gain_Channel<fc #ff0000>X</fc> | 0 dB          | -200 to 200 dB | Gain factor                                                             |
+--------------------------------+---------------+----------------+-------------------------------------------------------------------------+
| NumChannels                    | 2             | 20             | Number of output channels. Change in this value requires re-compilation |
+--------------------------------+---------------+----------------+-------------------------------------------------------------------------+
| SlewType                       | RC Slew       | NA             | Slew type. Applicable to HW slew modules                                |
+--------------------------------+---------------+----------------+-------------------------------------------------------------------------+
| CustomVal                      | 0x208A        | NA             | Custom slew value. Applicable to HW slew modules                        |
+--------------------------------+---------------+----------------+-------------------------------------------------------------------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== DSP Parameters =====

+--------------------------------+----------------------------------------------------+------------------------+---------------+
| Parameter Name                 | Description                                        | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================================+====================================================+========================+===============+
| Gain_Channel<fc #ff0000>X</fc> | Gain scaling for each output                       | Float                  | FixPoint8d24  |
+--------------------------------+----------------------------------------------------+------------------------+---------------+
| slew_mode                      | Slew mode and value for HW slew (only for HW slew) | NA                     | Integer       |
+--------------------------------+----------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== Gain= 10^(UIGainValue / 20)

.. |multctrlsplitter.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/multctrlsplitter.png
