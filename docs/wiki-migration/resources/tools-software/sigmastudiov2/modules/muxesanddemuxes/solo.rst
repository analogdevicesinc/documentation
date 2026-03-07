:doc:`Click here to return to the Multiplexers and Demultiplexers page </wiki-migration/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes>`

Solo
====

| |solo.png|
| ===== Description ===== If module is enabled, the selected input signal is passed to the selected output channel and rest are muted. In disable state signals get bypassed.
| ===== Usage ===== Select the radio button to route the particular input to output.
| ===== Targets Supported =====

==== ========== ================ ============= ================
Name ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
==== ========== ================ ============= ================
Solo B          B                NA            B
==== ========== ================ ============= ================

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

+-------------------+---------------+---------------+-----------------------------------------------------------------------------------+
| GUI Parameter     | Default Value | Range         | Function Description                                                              |
+===================+===============+===============+===================================================================================+
| NumChannels       | 1             | 1 to 20       | Number of input and output channels. Change in this value requires re-compilation |
+-------------------+---------------+---------------+-----------------------------------------------------------------------------------+
| SlewType          | NoSlew        | NoSlew/SWSlew | Enable or disable SWSlew                                                          |
+-------------------+---------------+---------------+-----------------------------------------------------------------------------------+
| StepSize (SWSlew) | 10            | 1 to 24       | Step size for transition from one input to other input                            |
+-------------------+---------------+---------------+-----------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+---------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                       | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===================================================+========================+===============+
| StepSize       | Step size for transition from one input to output | Float                  | NA            |
+----------------+---------------------------------------------------+------------------------+---------------+
| IsEnable       | Enable or disable the control                     | Float                  | NA            |
+----------------+---------------------------------------------------+------------------------+---------------+
| SelectedIndex  | Selected channel index                            | Float                  | NA            |
+----------------+---------------------------------------------------+------------------------+---------------+

DSP Parameter Computation
~~~~~~~~~~~~~~~~~~~~~~~~~

Step = 2^(-1/Step)

.. |solo.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/solo.png
