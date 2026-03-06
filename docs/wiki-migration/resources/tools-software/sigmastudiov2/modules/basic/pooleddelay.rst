:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Pooled Delay
============

| 
| |pooleddelay.png|

Description
-----------

This Module contains a common pool of delay buffer, which can be used for introducing delay in one or more channels subject to a total maximum delay of 120 ms. When the sum of the individual maximum delays of channels exceed 120 ms, only the first N channels whose delays can be accommodated would be applied. The rest of the channels are bypassed without any delay.

| 
| ===== Targets Supported =====

============ ========== ================ ============= ================
Name         ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============ ========== ================ ============= ================
Pooled Delay NA         B                NA            B
============ ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

======================= ===== ===============
Name                    Type  Description
======================= ===== ===============
Input<fc #ff0000>X</fc> Audio Input Channel X
======================= ===== ===============

Output
~~~~~~

======================== ===== ================
Name                     Type  Description
======================== ===== ================
Output<fc #ff0000>X</fc> Audio Output Channel X
======================== ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+-------------------------------------+---------------+-----------------------------------------+------------------------------------------------------------------------+
| GUI Parameter                       | Default Value | Range                                   | Function Description                                                   |
+=====================================+===============+=========================================+========================================================================+
| Delay_Channel <fc #ff0000>X</fc>    | 0             | 0 to MaxDelay_Channel<fc #ff0000>X</fc> | Delay values                                                           |
+-------------------------------------+---------------+-----------------------------------------+------------------------------------------------------------------------+
| MaxDelay_Channel <fc #ff0000>X</fc> | 1             | 1 to 120                                | Maximum allowed delays in ms                                           |
+-------------------------------------+---------------+-----------------------------------------+------------------------------------------------------------------------+
| NumChannels                         | 1             | 1 to 20                                 | Number of input channels. Change in this value requires re-compilation |
+-------------------------------------+---------------+-----------------------------------------+------------------------------------------------------------------------+
| FixedAddress                        | False         | True / False                            | Enable or disable Fixed address mode                                   |
+-------------------------------------+---------------+-----------------------------------------+------------------------------------------------------------------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== DSP Parameters =====

+-------------------------------------+-----------------------+------------------------+---------------+
| Parameter Name                      | Description           | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+=====================================+=======================+========================+===============+
| Delay_Channel <fc #ff0000>X</fc>    | Delay value           | Integer32              | NA            |
+-------------------------------------+-----------------------+------------------------+---------------+
| MaxDelay_Channel <fc #ff0000>X</fc> | Maximum allowed delay | Integer32              | NA            |
+-------------------------------------+-----------------------+------------------------+---------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== DSP Parameter Computation =====

=================================== =======================
Delay_Channel <fc #ff0000>X</fc>    = delay \* fs / 1000
MaxDelay_Channel <fc #ff0000>X</fc> = MaxDelay \* fs / 1000
=================================== =======================

.. |pooleddelay.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/pooleddelay.png
