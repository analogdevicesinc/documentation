:doc:`Click here to return to the Multiplexers and Demultiplexers page </wiki-migration/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes>`

Crossfade (Data-Controlled)
===========================

| |crossfade.png|
| ===== Description ===== This block creates a smooth transition between two input signals: the volume of one signal is decreased while the other input signal level increases, creating a gradual switch (cross-fade) between the inputs.
| ===== Usage ===== The output signal is selected by setting a value on the input control pin to the desired input's index, between 0.0 and 1.0. The control signal should be typically from a DC input block or RMS Table. 0.0 selects the lower input pin2, 1.0 selects the upper input pin1, and 0.5 mixes 0.5 times pin1 with 0.5 times pin2, etc. When the control input value changes, a cross fade is initiated between the current output and the newly selected input signal. The cross-fade transition rate (slew rate) can be adjusted using the numerical control on the block, (the maximum SW Slew Rate value is 23, which is a very slow fade). NumChannel controls the total number of output and input pairs (sharing the signal select control pin and SW slew).
| ===== Targets Supported =====

========= ========== ================ ============= ================
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========= ========== ================ ============= ================
Crossfade B          B                S             B
========= ========== ================ ============= ================

| 
| ===== Pins =====

Input
-----

======================= ======= ===============================
Name                    Type    Description
======================= ======= ===============================
SourceSelect            Control Controls the transition of data
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

+---------------+---------------+---------+-----------------------------------------------------------------------------------+
| GUI Parameter | Default Value | Range   | Function Description                                                              |
+===============+===============+=========+===================================================================================+
| Step          | 12            | 1 to 23 | Step size for transition from one input to other input                            |
+---------------+---------------+---------+-----------------------------------------------------------------------------------+
| NumChannels   | 1             | 1 to 20 | Number of input and output channels. Change in this value requires re-compilation |
+---------------+---------------+---------+-----------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+--------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                            | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+========================================================+========================+===============+
| Step           | Step size for transition from one input to other input | Float                  | FixPoint8d24  |
+----------------+--------------------------------------------------------+------------------------+---------------+

DSP Parameter Computation
~~~~~~~~~~~~~~~~~~~~~~~~~

Step = 2^(-1/Step)

.. |crossfade.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/muxesanddemuxes/crossfade.png
