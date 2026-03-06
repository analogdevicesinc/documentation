:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Advanced Pooled Delay
=====================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/advancedpooleddelay1.png
   :alt: advancedpooleddelay1.png

Description
-----------

| This module helps add a certain amount of delay to the input signal and produces a delayed output signal. It also contains a common pool of delay buffers, which can be used to introduce delay in one or more channels, subject to a total maximum delay. Additionally, this module provides an option to select the memory where the user wishes to create the delay buffer. Based on the memory selection of **StateA** or **StateB**, the delay buffer will be created in L1 memory, and for the option **StateC**, the buffer will be created in L3 memory.
| Please refer the *Configurable Parameters* table for further details.

Pins
----

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

| Note: <fc #ff0000>X</fc> - Channel Index
| ===== Configurable Parameters =====

+-------------------------------------+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter                       | Default Value | Range                                   | Function Description                                                                                                                                                                                                                                                                                                                                                                                                |
+=====================================+===============+=========================================+=====================================================================================================================================================================================================================================================================================================================================================================================================================+
| Delay (in ms) <fc #ff0000>X</fc>    | 0             | 0 to MaxDelay_Channel<fc #ff0000>X</fc> | Delay values                                                                                                                                                                                                                                                                                                                                                                                                        |
+-------------------------------------+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MaxDelay (in ms) <fc #ff0000>X</fc> | 1             | 1 to 2000                               | Maximum allowed delays in milliseconds                                                                                                                                                                                                                                                                                                                                                                              |
+-------------------------------------+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels                         | 1             | 1 to 32                                 | Number of input channels. Change in this value requires re-compilation                                                                                                                                                                                                                                                                                                                                              |
+-------------------------------------+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Select Memory                       | StateA        | StateA/StateB/StateC                    | It allows the user to choose in which memory the delay buffer to be stored. If **StateA** is chosen, buffer **SS Buffer 4** (**Block1_L1_space**) will be used for storing module data. If **StateB** is chosen, buffer **SS Buffer 8** (**Block3_L1_space**) will be used for storing module data. If **StateC** is chosen, buffer **SS Buffer 9** (**Block_L3_data_space**) will be used for storing module data. |
+-------------------------------------+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Total Delay (in ms)                 | 1             | 64000                                   | Sum of MaxDelay of all channels in milliseconds and this is **NOT** user configurable                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note: <fc #ff0000>X</fc> - Channel Index

.. note::

   The individual maximum delays of channels is limited to 2000ms each and the sum of each channel's MaxDelay cannot exceed the total maximum delay of 64000ms.


| When the input channels are grown (max upto 32), the Total Delay (in ms) displayed will be the sum of individual delay assigned for each channel (which will be calculated internally) as shown below.
| |advancedpooleddelay2.png|

DSP Parameters
--------------

+-------------------------------------+-----------------------+------------------------+
| Parameter Name                      | Description           | ADSP-214xx/SC5xx/215xx |
+=====================================+=======================+========================+
| Delay_Channel <fc #ff0000>X</fc>    | Delay value           | Integer32              |
+-------------------------------------+-----------------------+------------------------+
| MaxDelay_Channel <fc #ff0000>X</fc> | Maximum allowed delay | Integer32              |
+-------------------------------------+-----------------------+------------------------+

| Note: <fc #ff0000>X</fc> - Channel Index
| ===== DSP Parameter Computation =====

=================================== =======================
Delay_Channel <fc #ff0000>X</fc>    = delay \* fs / 1000
MaxDelay_Channel <fc #ff0000>X</fc> = MaxDelay \* fs / 1000
=================================== =======================

.. |advancedpooleddelay2.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/advancedpooleddelay2.png
