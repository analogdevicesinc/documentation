:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

xSPI Pooled Delay
=================

| |xspi_pooleddelay.png|
| **Please find the prerequisite for running the xSPI Pooled delay modules using external RAM** :doc:`xSPI Integration </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic/xspiintegration>`

Description
-----------

| The xSPI Pooled Delay block generates a delayed version of the input signal by utilizing external RAM connected via xSPI. The delay duration is determined by the number of samples specified in the 'Cur' numeric text box. The 'Max' numeric text box defines the maximum allowable delay that can be applied to the input signal. Memory for the delay line is allocated based on the 'TotalDelay' parameter, which sets the size of the memory pool shared across different delay lines. If you change the 'Max' value using the drop-down menu, recompilation will be required.
| The maximum delay that a specific delay block can support depends on the total available external RAM, as detailed in the external RAM's datasheet. When you set the 'Max' control value, a corresponding amount of memory is allocated on the external RAM, reserving it exclusively for that delay block.
| ===== Pins =====

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

+--------------------+---------------+------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                                                      | Function Description                                                                                                                       |
+====================+===============+============================================================+============================================================================================================================================+
| TotalDelay         | 1             | 1 to 64000(Sum of Max Delay in ms)                         | This control is read-only and displays the total delay allocated to this block                                                             |
+--------------------+---------------+------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| MaxDelay           | 1             | 1 to 2000 (Max delay allocation for particular delay line) | This control defines the maximum delay, in milliseconds, supported by the current delay line. Modifying this value requires recompilation. |
+--------------------+---------------+------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| CurDelay           | 0             | 0 to MaxDelay                                              | Current Dalay Value                                                                                                                        |
+--------------------+---------------+------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 32                                                         | Number of input and output channels. Change in this value requires re-compilation                                                          |
+--------------------+---------------+------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameters
--------------

+----------------+----------------------------------------------------+------------+
| Parameter Name | Description                                        | ADSP-21568 |
+================+====================================================+============+
| Delay          | Current Delay value in Words. (Cur \* 4)           | Integer32  |
+----------------+----------------------------------------------------+------------+
| MaxDelay       | Maximum number of Delay value                      | Integer32  |
+----------------+----------------------------------------------------+------------+
| TotalDelay     | Sum of Maximum number of Delay value in this block | Integer32  |
+----------------+----------------------------------------------------+------------+

| 
| ===== Memory =====

============ ================== ==========================
Code (Bytes) Coeff(Bytes)       Data32(Bytes)
============ ================== ==========================
2256         12 + 84(Framework) 296 + 256 (internal state)
============ ================== ==========================

| 
| ===== MIPS (Delay = Block size )=====

============= ============== ================
Default(1 Ch) 2 Growth(2 Ch) 32 Growth(32 Ch)
============= ============== ================
5.8           12.3           270.1
============= ============== ================

| 
|

.. note::

   To enhance performance, the Max or Current (Cur) delay values can be increased in steps of 0.5 millisecond. Optimal performance is typically achieved when the equivalent millisecond to sample values are divisible by the schematic block size.

   
   | If additional delay is required in the range of 1 to 24 samples, we can insert internal delay modules, as the main delay module only supports increments of 0.5 millisecond (24 samples if sampling rate is 48000).


| ====== Example Schematic ====== |xspi_pooleddelayschema.png|

Supported Processor
===================

-  ADSP-21568

.. |xspi_pooleddelay.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspi_pooleddelay.png
.. |xspi_pooleddelayschema.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspi_pooleddelayschema.png
