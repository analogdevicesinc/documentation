:doc:`Click here to return to the Multiplexers and Demultiplexers page </wiki-migration/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes>`

Index Selectable Demultiplexer
==============================

| |demuuxwslew.png|
| ===== Description ===== The Index Selectable Demultiplexer block route an input to one of many possible output pins. The output is selected based on a control signal value from an Index Lookup Table, RMS Table, or DC Input block. The slew variant of Index Selectable Demux allows smooth transition when switching outputs.
| ===== Variants =====

-  Mono (Configurable Slew Mode)
-  Stereo (Configurable Slew Mode)
-  Stereo (SW Slew)
-  Mono (No Slew)
-  Stereo (No Slew)

| 
| ===== Targets Supported =====

+---------------------------------+------------+------------------+---------------+------------------+
| Name                            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================================+============+==================+===============+==================+
| Mono (Configurable Slew Mode)   | NA         | NA               | S             | NA               |
+---------------------------------+------------+------------------+---------------+------------------+
| Stereo (Configurable Slew Mode) | NA         | NA               | S             | NA               |
+---------------------------------+------------+------------------+---------------+------------------+
| Stereo (SW Slew)                | B          | B                | NA            | NA               |
+---------------------------------+------------+------------------+---------------+------------------+
| Mono (No Slew)                  | S          | S                | NA            | B                |
+---------------------------------+------------+------------------+---------------+------------------+
| Stereo (No Slew)                | S          | S                | NA            | B                |
+---------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

======================= ======= ===============================
Name                    Type    Description
======================= ======= ===============================
InputSel_In             Control Channel selection control input
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

+-------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+
| GUI Parameter     | Default Value | Range   | Function Description                                                                                  |
+===================+===============+=========+=======================================================================================================+
| NumChannels       | 2             | 2 to 20 | Number of channels. Applicable to Mono modules. Change in this value requires re-compilation          |
+-------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+
| NumStereoChannels | 2             | 2 to 20 | Number of stereo channels. Applicable to Stereo modules. Change in this value requires re-compilation |
+-------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+
| StepSize          | 11            | 8 to 16 | Slew step size for SW slew modules                                                                    |
+-------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+
| SlewType          | RC Slew       | NA      | Slew type. Applicable to Configurable Slew Mode modules                                               |
+-------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+
| CustomVal         | 0x208A        | NA      | Custom slew value. Applicable to Configurable Slew Mode modules                                       |
+-------------------+---------------+---------+-------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                      | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==================================================================+========================+===============+
| slew_mode      | Slew mode and value for HW slew (Configurable Slew Mode modules) | NA                     | Integer       |
+----------------+------------------------------------------------------------------+------------------------+---------------+
| StepSize       | Slewing Step Size for SW Slew modules                            | Float                  | NA            |
+----------------+------------------------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== StepSize = 2^(-1 \* StepSize)

.. |demuuxwslew.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/demuuxwslew.png
