:doc:`Click here to return to the Multiplexers and Demultiplexers page </wiki-migration/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes>`

Switch Demultiplexer
====================

| |switch1xn.png| |switch2xn.png|
| ===== Description ===== The Demux Switch block routes an input signal to one of many possible outputs. The strip of radio buttons is used to select an output.
| ===== Variants =====

-  1xN (No Slew)
-  1xN (SW Slew)
-  1xN (HW Slew)
-  2xN (No Slew)
-  2xN (SW Slew)
-  2xN (HW Slew)

| 
| ===== Targets Supported =====

============= ========== ================ ============= ================
Name          ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============= ========== ================ ============= ================
1xN (No Slew) B/S        B/S              S             B
1xN (SW Slew) B/S        B/S              NA            NA
1xN (HW Slew) NA         NA               S             NA
2xN (No Slew) S          S                S             NA
2xN (SW Slew) S          S                NA            NA
2xN (HW Slew) NA         NA               S             NA
============= ========== ================ ============= ================

| 
| ===== Pins =====

Input
-----

======================= ===== ===============
Name                    Type  Description
======================= ===== ===============
Input<fc #ff0000>X</fc> Audio Input Channel X
======================= ===== ===============

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

+-------------------+---------------+---------+----------------------------------------------------------------------------------------------------+
| GUI Parameter     | Default Value | Range   | Function Description                                                                               |
+===================+===============+=========+====================================================================================================+
| NumChannels       | 2             | 2 to 20 | Number of channels. Applicable to 1xN modules. Change in this value requires re-compilation        |
+-------------------+---------------+---------+----------------------------------------------------------------------------------------------------+
| NumStereoChannels | 2             | 2 to 20 | Number of stereo channels. Applicable to 2xN modules. Change in this value requires re-compilation |
+-------------------+---------------+---------+----------------------------------------------------------------------------------------------------+
| SelectedVal       | 0             | NA      | Selected output index                                                                              |
+-------------------+---------------+---------+----------------------------------------------------------------------------------------------------+
| SlewType          | RC Slew       | NA      | Slew type. Applicable to HW slew modules                                                           |
+-------------------+---------------+---------+----------------------------------------------------------------------------------------------------+
| CustomVal         | 0x208A        | NA      | Custom slew value. Applicable to HW slew modules                                                   |
+-------------------+---------------+---------+----------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+---------------------------------+------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name                  | Description                                                                  | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+=================================+==============================================================================+========================+===============+
| Index_Channel<fc #ff0000>X</fc> | 0 or 1 depending on whether the input channel <fc #ff0000>X</fc> is selected | Float                  | FixPoint8d32  |
+---------------------------------+------------------------------------------------------------------------------+------------------------+---------------+
| slew_mode                       | Slew mode and value for HW slew (only for HW slew)                           | NA                     | Integer       |
+---------------------------------+------------------------------------------------------------------------------+------------------------+---------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

.. |switch1xn.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/switch1xn.png
.. |switch2xn.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/switch2xn.png
