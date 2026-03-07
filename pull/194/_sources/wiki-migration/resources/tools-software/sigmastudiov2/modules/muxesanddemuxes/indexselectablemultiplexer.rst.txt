:doc:`Click here to return to the Multiplexers and Demultiplexers page </wiki-migration/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes>`

Index Selectable Multiplexer
============================

| |indxselnx1mux.png| |indxselnx2mux.png| |indxselnx2muxslew.png|
| ===== Description ===== The Index Selectable Multiplexer block route one of the inputs to the output pins. The input is selected based on a control signal value from an Index Lookup Table, RMS Table, or DC Input block. The slew variant of Index Selectable Mux allows smooth transition when switching inputs.
| ===== Variants =====

-  Mono (No Slew)
-  Mono (HW Slew)
-  Mono (SW Slew)
-  Stereo (No Slew)
-  Stereo (HW Slew)
-  Stereo (SW Slew)

| 
| ===== Targets Supported =====

+------------------+------------+------------------+---------------+------------------+
| Name             | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==================+============+==================+===============+==================+
| Mono (No Slew)   | S/B        | S/B              | S             | B                |
+------------------+------------+------------------+---------------+------------------+
| Mono (HW Slew)   | NA         | NA               | S             | NA               |
+------------------+------------+------------------+---------------+------------------+
| Mono (SW Slew)   | S/B        | S/B              | NA            | NA               |
+------------------+------------+------------------+---------------+------------------+
| Stereo (No Slew) | S/B        | S/B              | S             | B                |
+------------------+------------+------------------+---------------+------------------+
| Stereo (HW Slew) | NA         | NA               | S             | NA               |
+------------------+------------+------------------+---------------+------------------+
| Stereo (SW Slew) | B          | B                | NA            | B                |
+------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

======================= ======= ===============================
Name                    Type    Description
======================= ======= ===============================
Index                   Control Channel selection control input
Input<fc #ff0000>X</fc> Audio   Input Channel X
======================= ======= ===============================

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

+--------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+
| GUI Parameter      | Default Value | Range   | Function Description                                                                                  |
+====================+===============+=========+=======================================================================================================+
| NumChannels        | 2             | 2 to 20 | Number of channels. Applicable to Mono modules. Change in this value requires re-compilation          |
+--------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+
| NumChannels_Stereo | 2             | 2 to 20 | Number of stereo channels. Applicable to Stereo modules. Change in this value requires re-compilation |
+--------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+
| StepSize           | 11            | 8 to 16 | Slew step size for SW slew modules                                                                    |
+--------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+
| SlewType           | RC Slew       | NA      | Slew type. Applicable to Configurable Slew Mode modules                                               |
+--------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+
| CustomVal          | 0x208A        | NA      | Custom slew value. Applicable to Configurable Slew Mode modules                                       |
+--------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                      | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==================================================================+========================+===============+
| slew_mode      | Slew mode and value for HW slew (Configurable Slew Mode modules) | NA                     | Integer       |
+----------------+------------------------------------------------------------------+------------------------+---------------+
| StepSize       | Slewing Step Size for SW Slew modules                            | Float                  | NA            |
+----------------+------------------------------------------------------------------+------------------------+---------------+

.. |indxselnx1mux.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/indxselnx1mux.png
.. |indxselnx2mux.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/indxselnx2mux.png
.. |indxselnx2muxslew.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/indxselnx2muxslew.png
