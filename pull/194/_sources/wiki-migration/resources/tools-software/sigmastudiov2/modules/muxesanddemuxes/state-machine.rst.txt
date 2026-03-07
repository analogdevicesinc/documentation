:doc:`Click here to return to the Multiplexers and Demultiplexers page </wiki-migration/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes>`

State Machine
=============

| |statemachine.png|
| ===== Description ===== This block outputs the input signal from the input pin, if and only if the control signal falls within the range specified in the numerical controls (>) and (<). If the control signal is out of range, the input is disabled and a zero value is output. The control pin can be sourced by a DC Input Entry, Counter, or an Index Lookup Table block.
| ===== Targets Supported =====

============= ========== ================ ============= ================
Name          ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============= ========== ================ ============= ================
State Machine S/B        S/B              S             B
============= ========== ================ ============= ================

| 
| ===== Pins =====

Input
-----

+-------------------------+---------+----------------------------------------------------------+
| Name                    | Type    | Description                                              |
+=========================+=========+==========================================================+
| ControlInput            | Control | Control input value checked with the specified condition |
+-------------------------+---------+----------------------------------------------------------+
| Input<fc #ff0000>X</fc> | Audio   | Input Channel X                                          |
+-------------------------+---------+----------------------------------------------------------+

Output
------

======================== ===== ================
Name                     Type  Description
======================== ===== ================
Output<fc #ff0000>X</fc> Audio Output Channel X
======================== ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+---------------------------------------+---------------+---------+------------------------------------------------------------------+
| GUI Parameter                         | Default Value | Range   | Function Description                                             |
+=======================================+===============+=========+==================================================================+
| NumChannels                           | 1             | 1 to 20 | Number of channels. Change in this value requires re-compilation |
+---------------------------------------+---------------+---------+------------------------------------------------------------------+
| HighControl_Channel<fc #ff0000>X</fc> | 0             | N/A     | Maximum value to compare with control input                      |
+---------------------------------------+---------------+---------+------------------------------------------------------------------+
| LowControl_Channel<fc #ff0000>X</fc>  | 0             | N/A     | Minimum value to compare with control input                      |
+---------------------------------------+---------------+---------+------------------------------------------------------------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== DSP Parameters =====

+---------------------------------------+---------------------------------------------+------------------------+---------------+
| Parameter Name                        | Description                                 | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+=======================================+=============================================+========================+===============+
| HighControl_Channel<fc #ff0000>X</fc> | Maximum value to compare with control input | Float                  | FixPoint8d24  |
+---------------------------------------+---------------------------------------------+------------------------+---------------+
| LowControl_Channel<fc #ff0000>X</fc>  | Minimum value to compare with control input | Float                  | FixPoint8d24  |
+---------------------------------------+---------------------------------------------+------------------------+---------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

.. |statemachine.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/statemachine.png
