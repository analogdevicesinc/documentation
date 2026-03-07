:doc:`Click here to return to the Mixers and Splitters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mixersandsplitters>`

Simple Router
=============

| 
| |simplerouter.png|
| |simplerouterform.png|

Description
-----------

| The Simple Router block routes the N different inputs to M different Outputs with multiplied by respective gains. This module supports multiple router configurations. Any input can be routed to any output pin. A separate post gain is available for each of the output. All the gains has a corresponding mute control to quickly mute the particular gain. The current router/mixer(Mix #) can be changed during the runtime by changing the Tab in the mixer window. RC slew is applied for any change in the inputs/gains.
| ===== Usage ===== Click on the icon to open the Router window to configure the gain for respective input channels for respective outputs.
| ===== Variants =====

-  Simple Router
-  Simple Router (Slew)

Targets Supported
-----------------

+----------------------+------------+------------------+---------------+------------------+
| Name                 | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+======================+============+==================+===============+==================+
| Simple Router        | B          | B                | S             | B                |
+----------------------+------------+------------------+---------------+------------------+
| Simple Router (Slew) | NA         | NA               | S             | NA               |
+----------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======================== ===== ===============
Name                     Type  Description
======================== ===== ===============
Input <fc #ff0000>X</fc> Audio Input channel X
======================== ===== ===============

Output
~~~~~~

========================= ===== ================
Name                      Type  Description
========================= ===== ================
Output <fc #ff0000>X</fc> Audio Output channel X
========================= ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+------------------------------------------------------------+---------------+-------------+-----------------------------------------------------------------------------+
| GUI Parameter Name                                         | Default Value | Range       | Function Description                                                        |
+============================================================+===============+=============+=============================================================================+
| SlectedInputTab<fc #ff0000>M</fc>_Output<fc #ff0000>N</fc> | 0 dB          | -30 to 6 dB | Gain factor                                                                 |
+------------------------------------------------------------+---------------+-------------+-----------------------------------------------------------------------------+
| GainDB_Output<fc #ff0000>M</fc>_Input<fc #ff0000>N</fc>    | 0 dB          | -30 to 6 dB | Gain factor                                                                 |
+------------------------------------------------------------+---------------+-------------+-----------------------------------------------------------------------------+
| ISDb_Output<fc #ff0000>M</fc>_Input<fc #ff0000>N</fc>      | True          | True/False  | Decides the Gain control in db/linear                                       |
+------------------------------------------------------------+---------------+-------------+-----------------------------------------------------------------------------+
| NumInputs                                                  | 2             | 2 to 20     | Number of input channels. Change in input channels requires re-compilation  |
+------------------------------------------------------------+---------------+-------------+-----------------------------------------------------------------------------+
| NumOutputs                                                 | 1             | 1 to 20     | Number of input channels. Change in output channels requires re-compilation |
+------------------------------------------------------------+---------------+-------------+-----------------------------------------------------------------------------+
| Slew                                                       | 12            | 1 to 24     | Slew Step Size. Applicable to SW Slew modules                               |
+------------------------------------------------------------+---------------+-------------+-----------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------------------------------------------+------------------------+
| Parameter Name | Description                                               | ADSP-214xx/SC5xx/215xx |
+================+===========================================================+========================+
| GainArray      | Scaling of the gain values                                | Float                  |
+----------------+-----------------------------------------------------------+------------------------+
| OutputArray    | Input channels routing with respect to the output channel | Float                  |
+----------------+-----------------------------------------------------------+------------------------+
| Alpha          | Scaling of the Stepsize                                   | NA                     |
+----------------+-----------------------------------------------------------+------------------------+

| 
| ===== DSP Parameters Computation===== Alpha= Math.Exp( -1 / ( ( 0.04 \* 2^(SlewStep-1) / 1000 )*FS)

.. |simplerouter.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/simplerouter.png
.. |simplerouterform.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/simplerouterform.png
