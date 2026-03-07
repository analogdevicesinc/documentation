:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Delay
=====

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/delay.png
   :alt: delay.png

Description
-----------

| The Delay block outputs a delayed version of the input signal. The input is delayed by the number of samples reflected in the Cur numeric text box. The top drop-down menu labeled Max represents the largest amount of delay that could be applied to the input signal. If you select a new Max value in the drop-down menu, you will be forced to recompile.
| The maximum delay available for a particular delay block depends on the total available system data RAM, which is specified in the DSP processor datasheet. Setting the Max control's value, allocates memory on the DSP, reserving that memory for use by this particular block only, and reducing the available memory for all other delay blocks in the design. This is a compiler directive and modifies the assembly code, so any time you change the Max setting you must recompile and download the program. The maximum delay value range is limited to the remaining unallocated memory of the RAM.
| ===== Targets Supported =====

===== ========== ================ ============= ================
Name  ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
===== ========== ================ ============= ================
Delay B/S        B/S              S             B
===== ========== ================ ============= ================

Pins
----

Input
~~~~~

======================== ===== ===============
Name                     Type  Description
======================== ===== ===============
Input <fc #ff0000>X</fc> Audio Input channel X
======================== ===== ===============

Output
~~~~~~

========================= ===== ================
Name                      Type  Description
========================= ===== ================
Output <fc #ff0000>X</fc> Audio Output channel X
========================= ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                                               | Function Description                                                                                                                                               |
+====================+===============+=====================================================+====================================================================================================================================================================+
| IsSample           | True          | True / False                                        | Allows the Max and Cur delay controls either in Samples or milliseconds                                                                                            |
+--------------------+---------------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MaxDelay           | 1             | 1 to 1500 (Depends on Size of the Memory available) | This control specifies the maximum delay supported for the current instance in samples (32-bit word). Change in this value requires a re-compilation               |
+--------------------+---------------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CurDelay           | 1             | 1 to MaxDelay                                       | Current Daly Value                                                                                                                                                 |
+--------------------+---------------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Memory             | DM1           | NA                                                  | It allows the user to choose in which memory the delay buffer to be stored ( Not for ADSP-214xx, ADSP-215xx/SC5xx ) Change in this value requires a re-compilation |
+--------------------+---------------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 20                                                  | Number of input and output channels. Change in this value requires re-compilation                                                                                  |
+--------------------+---------------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameters
--------------

+----------------+------------------------------------------+------------------------+---------------+
| Parameter Name | Description                              | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==========================================+========================+===============+
| Delay          | Current Delay value in bytes. (Cur \* 4) | Integer32              | Integer32     |
+----------------+------------------------------------------+------------------------+---------------+
| MaxDelay       | Maximum number of Delay value            | Integer32              | NA            |
+----------------+------------------------------------------+------------------------+---------------+

| 
