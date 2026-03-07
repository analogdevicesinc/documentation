:doc:`Click here to return to the Mixers and Splitters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mixersandsplitters>`

Audio Signal Router
===================

| 
| Audio Signal Router
| |audiosignalrouter.png|
| Audio Signal Router Ext-Index
| |audiosignalrouterextindex.png|
| Audio Signal Router with Index Selectable
| |audiosignalrouterwithtab.png|
| |audiosignalrouterwindow.png|

Description
-----------

| Audio Signal router mixes M different inputs to N different outputs with various gains. The number of input and output pins are configurable.
| ===== Usage ===== Audio Signal Router module supports multiple mixer configurations. Each mixer configuration has gains for all the inputs and outputs. A separate gain is available for each of input output combination also. All the gains has a corresponding mute control to quickly mute the particular gain. The current Tab selected (Tab #) in the mixer window is downloaded to the target and used for mixing.
| Audio Signal Router ExtIndex functionality is same as audio signal router except that the current mixer (Tab #) is selected through an external input. The control pin expects the input in (32.0) format for ADAU145x processors and (28.0) format for other Sigma DSPs. The maximum number of tabs that can be added are 16.
| Audio Signal Router with Index Selectable- The current mixer (Table Mix) can be changed during the runtime.

Variants
--------

-  Audio Signal Router
-  Audio Signal Router ExtIndex
-  Audio Signal Router - Control Index

| 
| ===== Targets Supported =====

+--------------------------------------+------------+------------------+---------------+------------------+
| Name                                 | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+======================================+============+==================+===============+==================+
| Audio Signal Router                  | B          | B                | S             | B                |
+--------------------------------------+------------+------------------+---------------+------------------+
| Audio Signal Router ExtIndex         | B          | B                | S             | B                |
+--------------------------------------+------------+------------------+---------------+------------------+
| Audio Signal Router Index Selectable | NA         | NA               | S             | NA               |
+--------------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+-------------------------+---------+----------------------------------------------------------+
| Name                    | Type    | Description                                              |
+=========================+=========+==========================================================+
| ExtIndex                | Control | External Index input(Only for AudioSignalRouterExtIndex) |
+-------------------------+---------+----------------------------------------------------------+
| Input<fc #ff0000>X</fc> | Audio   | Input channel X                                          |
+-------------------------+---------+----------------------------------------------------------+

| 
| ==== Output ====

======================== ===== ================
Name                     Type  Description
======================== ===== ================
Output<fc #ff0000>X</fc> Audio Output Channel X
======================== ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

Configurable Parameters
-----------------------

+----------------------------------------------------------------+---------------+------------+-------------------------------------------------------------------------+
| GUI Parameter Name                                             | Default Value | Range      | Function Description                                                    |
+================================================================+===============+============+=========================================================================+
| InputGain_InputChannel<fc #ff0000>0</fc>                       | 0             | -138 to 24 | Scales the input Gain in dB                                             |
+----------------------------------------------------------------+---------------+------------+-------------------------------------------------------------------------+
| InputGainMute_InputChannel<fc #ff0000>0</fc>                   | false         | true/false | Input gain enable or mute                                               |
+----------------------------------------------------------------+---------------+------------+-------------------------------------------------------------------------+
| OutputGain_OutputChannel<fc #ff0000>0</fc>                     | 0             | -138 to 24 | Scales the output Gain in dB                                            |
+----------------------------------------------------------------+---------------+------------+-------------------------------------------------------------------------+
| OutputGainMute_OutputChannel<fc #ff0000>0</fc>                 | false         | true/false | output gain enable or mute                                              |
+----------------------------------------------------------------+---------------+------------+-------------------------------------------------------------------------+
| CrossGain_Input<fc #ff0000>0</fc>_Output<fc #ff0000>0</fc>     | 0             | -138 to 24 | Scales cross Gain in dB                                                 |
+----------------------------------------------------------------+---------------+------------+-------------------------------------------------------------------------+
| CrossGainMute_Input<fc #ff0000>0</fc>_Output<fc #ff0000>0</fc> | false         | true/false | Cross gain enable or mute                                               |
+----------------------------------------------------------------+---------------+------------+-------------------------------------------------------------------------+
| NumInputs                                                      | 2             | 20         | Number of input channels. Change in this value requires re-compilation  |
+----------------------------------------------------------------+---------------+------------+-------------------------------------------------------------------------+
| NumOutputs                                                     | 1             | 20         | Number of Output channels. Change in this value requires re-compilation |
+----------------------------------------------------------------+---------------+------------+-------------------------------------------------------------------------+
| SlewRate                                                       | 12            | 1 to 24    | Scales the Step size                                                    |
+----------------------------------------------------------------+---------------+------------+-------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+------------------------+-----------------------------+------------------------+---------------+
| Parameter Name         | Description                 | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+========================+=============================+========================+===============+
| SlewStep               | Slew rate                   | Float                  | FixPoint8d24  |
+------------------------+-----------------------------+------------------------+---------------+
| InputGainArray         | Input linear gain values    | Float                  | FixPoint8d24  |
+------------------------+-----------------------------+------------------------+---------------+
| OutputGainArray        | Output linear gain values   | Float                  | FixPoint8d24  |
+------------------------+-----------------------------+------------------------+---------------+
| CrossGainArray         | Cross linear gain values    | Float                  | FixPoint8d24  |
+------------------------+-----------------------------+------------------------+---------------+
| TableIndex             | Current selected tab index  | NA                     | Int32         |
+------------------------+-----------------------------+------------------------+---------------+
| TableIndexMax/TabCount | Number of tab count         | NA                     | Int32         |
+------------------------+-----------------------------+------------------------+---------------+
| NumCoeffs              | Total number of coefficient | NA                     | Int32         |
+------------------------+-----------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== LinearGain= 10^(GainArray[i] / 20)
| NumCoeffs=(NumInputs\* NumOutputs+ NumInputs+ NumOutputs)
| tc = 0.04 \* Math.Pow(2, SlewRate- 1) / 1000
| Alpha = Math.Exp(-1 / (tc \* fs))
| Om_Alpha = 1 - Alpha

.. |audiosignalrouter.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/audiosignalrouter.png
.. |audiosignalrouterextindex.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/audiosignalrouterextindex.png
.. |audiosignalrouterwithtab.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/audiosignalrouterwithtab.png
.. |audiosignalrouterwindow.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/audiosignalrouterwindow.png
   :width: 600px
