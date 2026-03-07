:doc:`Click here to return to the Gain page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gain>`

Multiple Volume Control
=======================

| 
| |multiplectrlvolume.png|
| ===== Varaints =====

::

   -Multiple Volume Control (HW Slew)
   -Multiple Volume Control (No Slew)
   -Multiple Volume Control (RC Slew)

Description
-----------

| The Multiple Volume Control block allows gain adjustment to be made to each of the inputs individually. Every input pin has its own volume control.
| ===== Usage ===== The Slider control's min/max value and step size can be customized. To modify the slider's settings, right-click on the control which will display the control pop-up window
| ===== Targets Supported =====

+-----------------------------------+------------+------------------+---------------+------------------+
| Name                              | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===================================+============+==================+===============+==================+
| Multiple Volume Control (HW Slew) | B/S        | B/S              | S             | B                |
+-----------------------------------+------------+------------------+---------------+------------------+
| Multiple Volume Control (No Slew) | NA         | NA               | S             | NA               |
+-----------------------------------+------------+------------------+---------------+------------------+
| Multiple Volume Control (RC Slew) | NA         | NA               | S             | NA               |
+-----------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======================= ===== ===============
Name                    Type  Description
======================= ===== ===============
Input<fc #ff0000>X</fc> Audio Input channel X
======================= ===== ===============

| 
| ==== Output ====

======================== ======= ================
Name                     Type    Description
======================== ======= ================
Output<fc #ff0000>X</fc> Control Output channel X
======================== ======= ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+----------------------------------+---------------+----------------------------------+-------------------------------------------------------------------------------+
| GUI Parameter Name               | Default Value | Range                            | Function Description                                                          |
+==================================+===============+==================================+===============================================================================+
| Gain_Channel<fc #ff0000>X</fc>   | 0 dB          | -200 to +200 dB                  | Increases/decreases the dB level of the input                                 |
+----------------------------------+---------------+----------------------------------+-------------------------------------------------------------------------------+
| IsDBps_Channel<fc #ff0000>X</fc> | True          | True/False                       | Allows to controls either in dBps/linear                                      |
+----------------------------------+---------------+----------------------------------+-------------------------------------------------------------------------------+
| Max_Channel<fc #ff0000>X</fc>    | 0             | Min_Channel < Max_Channel < 200  | Configure the maximum value of gain for X channel                             |
+----------------------------------+---------------+----------------------------------+-------------------------------------------------------------------------------+
| Min_Channel<fc #ff0000>X</fc>    | 0             | -200 < Min_Channel < Max_Channel | Configure the minimum value of gain for X channel                             |
+----------------------------------+---------------+----------------------------------+-------------------------------------------------------------------------------+
| NumChannels                      | 1             | 20                               | Num of input and output channels.Change in this value requires re-compilation |
+----------------------------------+---------------+----------------------------------+-------------------------------------------------------------------------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== DSP Parameters =====

+--------------------------------+---------------------------------------------------------------+------------------------+---------------+
| Parameter Name                 | Description                                                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================================+===============================================================+========================+===============+
| Gain_Channel<fc #ff0000>X</fc> | Increases/decreases the dB level of the input                 | Float                  | FixPoint8d24  |
+--------------------------------+---------------------------------------------------------------+------------------------+---------------+
| Slew_Channel<fc #ff0000>X</fc> | Smoothly transition of signal from one level to another level | Float                  | FixPoint8d24  |
+--------------------------------+---------------------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== Slew_Channel0 = 2^(-12)

.. |multiplectrlvolume.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/multiplectrlvolume.png
