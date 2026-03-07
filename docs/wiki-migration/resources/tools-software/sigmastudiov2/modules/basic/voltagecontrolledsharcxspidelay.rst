:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

xSPI Voltage Controlled Delay
=============================

| |xspi_vcdelay.png|
| **Please find the prerequisite for running the xSPI voltage controlled delay modules using external RAM** :doc:`xSPI Integration </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic/xspiintegration>`

Description
-----------

| The xSPI Voltage Controlled Delay block outputs a delayed version of the input signal using external RAM connected with xSPI. The input is delayed by the number of samples given in the control input. The Max numeric text box represents the largest amount of delay that could be applied to the input signal. If you select a new Max value in the drop-down menu, you will be forced to recompile.
| The maximum delay available for a particular voltage controlled delay block depends on the total available external RAM memory, which is specified in external RAM datasheet. Setting the Max control's value, allocates memory on the external RAM, reserving that memory for use by this particular block.
| ===== Pins =====

Input
~~~~~

======================== ======= ===============
Name                     Type    Description
======================== ======= ===============
Input <fc #ff0000>0</fc> Audio   Input channel 0
Input <fc #ff0000>X</fc> Control Input channel X
======================== ======= ===============

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

+--------------------+---------------+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                                                              | Function Description                                                                                                                                 |
+====================+===============+====================================================================+======================================================================================================================================================+
| MaxDelay           | 8             | 8 to 480000 (Depends on Size of the external RAM Memory available) | This control specifies the maximum delay supported for the current instance in samples (32-bit word). Change in this value requires a re-compilation |
+--------------------+---------------+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 32                                                                 | Number of input and output channels. Change in this value requires re-compilation                                                                    |
+--------------------+---------------+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameters
--------------

============== ======================================== ==========
Parameter Name Description                              ADSP-21568
============== ======================================== ==========
Delay          Current Delay value in Words. (Cur \* 4) Integer32
MaxDelay       Maximum number of Delay value            Integer32
============== ======================================== ==========

| 
|

.. note::

   The current delay control input will be capped at the maximum allowable delay value.


   | ===== Memory =====

============ ================= =========================
Code (Bytes) Coeff(Bytes)      Data32(Bytes)
============ ================= =========================
2202         4 + 94(Framework) 296 + 256(internal state)
============ ================= =========================

|

| ===== MIPS (Delay = Block size )=====

============= ============== ================
Default(1 Ch) 2 Growth(2 Ch) 32 Growth(32 Ch)
============= ============== ================
7.3           7.9            25.3
============= ============== ================

| 
|

.. note::

   To enhance performance, the Max or Current (Cur) delay values can be increased in steps of 8 samples. Optimal performance is typically achieved when these values are divisible by the schematic block size.

   
   | If additional delay is required in the range of 1 to 7 samples, we can insert internal delay modules, as the main delay module only supports increments of 8 samples.


| ====== Example Schematic ====== |xspi_vcdelayschema.png|

Supported Processor
===================

-  ADSP-21568

.. |xspi_vcdelay.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspi_vcdelay.png
.. |xspi_vcdelayschema.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspi_vcdelayschema.png
