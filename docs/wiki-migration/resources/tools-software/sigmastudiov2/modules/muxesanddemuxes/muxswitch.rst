:doc:`Click here to return to the Multiplexers and Demultiplexers page </wiki-migration/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes>`

Switch Multiplexer
==================

| |nx1mux.png| |nx2mux.png| |nx3mux.png| |nx4mux.png| |nx6mux.png| |nx8mux.png|
| ===== Description ===== The Mux Switch block routes one of many possible input signals to the output. The strip of radio buttons is used to select the input signal.
| ===== Variants =====

-  Nx1 Switch
-  Nx2 Switch
-  Nx4 Switch
-  Nx6 Switch
-  Nx8 Switch
-  Nx12 Switch

| Note: \* <fc #ff0000>Slew Type</fc> - Slew type can be selected for each of the above Switches
| ===== Targets Supported =====

+----------------+------------+------------------+---------------+------------------+
| Name           | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================+============+==================+===============+==================+
| Nx1 (No Slew)  | S/B        | S/B              | S             | B                |
+----------------+------------+------------------+---------------+------------------+
| Nx1 (SW Slew)  | S/B        | S/B              | NA            | NA               |
+----------------+------------+------------------+---------------+------------------+
| Nx1 (HW Slew)  | NA         | NA               | S             | NA               |
+----------------+------------+------------------+---------------+------------------+
| Nx2 (No Slew)  | S/B        | S/B              | S             | B                |
+----------------+------------+------------------+---------------+------------------+
| Nx2 (SW Slew)  | S/B        | S/B              | NA            | NA               |
+----------------+------------+------------------+---------------+------------------+
| Nx2 (HW Slew)  | NA         | NA               | S             | NA               |
+----------------+------------+------------------+---------------+------------------+
| Nx4 (No Slew)  | NA         | NA               | S             | NA               |
+----------------+------------+------------------+---------------+------------------+
| Nx6 (No Slew)  | S/B        | S/B              | S             | B                |
+----------------+------------+------------------+---------------+------------------+
| Nx8 (No Slew)  | S/B        | S/B              | S             | B                |
+----------------+------------+------------------+---------------+------------------+
| Nx12 (No Slew) | B          | B                | NA            | B                |
+----------------+------------+------------------+---------------+------------------+

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

+---------------------------+---------------+---------+---------------------------------------------------------------------------------------------------------+
| GUI Parameter             | Default Value | Range   | Function Description                                                                                    |
+===========================+===============+=========+=========================================================================================================+
| NumChannels               | 2             | 2 to 20 | Number of channels. Applicable to Nx1 modules. Change in this value requires re-compilation             |
+---------------------------+---------------+---------+---------------------------------------------------------------------------------------------------------+
| NumStereoChannels         | 2             | 2 to 20 | Number of stereo channels. Applicable to Nx2 modules. Change in this value requires re-compilation      |
+---------------------------+---------------+---------+---------------------------------------------------------------------------------------------------------+
| NumSources                | 2             | 2 to 20 | Number of channel group. Applicable to Nx4/6/8/12 modules. Change in this value requires re-compilation |
+---------------------------+---------------+---------+---------------------------------------------------------------------------------------------------------+
| SelectedVal/SelectedIndex | 0             | NA      | Selected input index                                                                                    |
+---------------------------+---------------+---------+---------------------------------------------------------------------------------------------------------+
| StepSize                  | 10            | 8 to 16 | Slew Step Size. Applicable to SW Slew modules                                                           |
+---------------------------+---------------+---------+---------------------------------------------------------------------------------------------------------+
| SlewType                  | RC Slew       | NA      | Slew type. Applicable to HW slew modules                                                                |
+---------------------------+---------------+---------+---------------------------------------------------------------------------------------------------------+
| CustomVal                 | 0x208A        | NA      | Custom slew value. Applicable to HW slew modules                                                        |
+---------------------------+---------------+---------+---------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                 | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=============================================================+========================+===============+
| Index          | Selects the input channel to route the input through output | Integer                | Integer       |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| slew_mode      | Slew mode and value for HW slew (only for HW slew)          | NA                     | Integer       |
+----------------+-------------------------------------------------------------+------------------------+---------------+

.. |nx1mux.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/nx1mux.png
.. |nx2mux.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/nx2mux.png
.. |nx3mux.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/nx3mux.png
.. |nx4mux.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/nx4mux.png
.. |nx6mux.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/nx6mux.png
.. |nx8mux.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/nx8mux.png
