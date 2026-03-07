:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

xSPI Index Selectable Delay
===========================

| |xspi_is_delay.png|
| **Please find the prerequisite for running the xSPI index selectable delay modules using external RAM** :doc:`xSPI Integration </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic/xspiintegration>`

Description
-----------

| The xSPI Index Selectable Delay block outputs a delayed version of the input signal using external RAM connected via xSPI. The delay is determined by the number of samples specified in a set of numeric text boxes, with the active value selected through a control input. The 'Max' numeric text box defines the maximum delay that can be applied to the input signal. Changing the 'Max' value via the drop-down menu requires recompilation.
| The maximum delay supported by a voltage-controlled delay block depends on the total available external RAM, as specified in the RAM's datasheet. Setting the 'Max' control value allocates a portion of this memory, reserving it exclusively for the block's use.
| ===== Pins =====

Input
~~~~~

======================== ======= ===============
Name                     Type    Description
======================== ======= ===============
Input <fc #ff0000>0</fc> Control Input channel 0
Input <fc #ff0000>1</fc> Audio   Input channel 1
======================== ======= ===============

Output
~~~~~~

========================= ===== ================
Name                      Type  Description
========================= ===== ================
Output <fc #ff0000>0</fc> Audio Output channel 0
========================= ===== ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                                                              | Function Description                                                                                                                                        |
+====================+===============+====================================================================+=============================================================================================================================================================+
| MaxDelay           | 8             | 8 to 480000 (Depends on Size of the external RAM Memory available) | This control specifies the maximum delay supported for the current instance in samples (32-bit word). Change in this value requires a re-compilation        |
+--------------------+---------------+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Delays             | 8             | 8 to 480000                                                        | A set of delay controls defines the possible delay values for the delay line, with the active delay selected dynamically based on an external control input |
+--------------------+---------------+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DelayCount         | 1             | 32                                                                 | The number of delay controls added to the block is determined by the value of 'DelayCount'                                                                  |
+--------------------+---------------+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameters
--------------

+----------------+-------------------------------------------------+------------+
| Parameter Name | Description                                     | ADSP-21568 |
+================+=================================================+============+
| Delays         | Current Delay value in Words. (DelayCount \* 4) | Integer32  |
+----------------+-------------------------------------------------+------------+
| MaxDelay       | Maximum number of Delay value                   | Integer32  |
+----------------+-------------------------------------------------+------------+

| 
|

.. note::

   The delays control value will be capped at the maximum allowable Max delay value.


   | ===== Memory =====

============ ================================= =========================
Code (Bytes) Coeff(Bytes)                      Data32(Bytes)
============ ================================= =========================
1998         4 + 4\*DelayCount + 132(Framework) 296 + 256(internal state)
============ ================================= =========================

|

| ===== MIPS (Delay = Block size )=====

===================== ============ =============
Default(2 DelayCount) 3 DelayCount 32 DelayCount
===================== ============ =============
6.2                   7.3          7.3
===================== ============ =============

| 
|

.. note::

   To enhance performance, the Max or delay values can be increased in steps of 8 samples. Optimal performance is typically achieved when these values are divisible by the schematic block size.

   
   | If additional delay is required in the range of 1 to 7 samples, we can insert internal delay modules, as the main delay module only supports increments of 8 samples.


| ====== Example Schematic ====== |xspi_is_delayschema.png|

Supported Processor
===================

-  ADSP-21568

.. |xspi_is_delay.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspi_is_delay.png
.. |xspi_is_delayschema.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspi_is_delayschema.png
