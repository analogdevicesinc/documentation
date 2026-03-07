Voltage Controlled SPI Delay (ADAU145X)
=======================================

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| \|\| This module can be used to implement off-chip delay using the SPI interface.
| |image1|
| ===== Input Pins =====

+----------------------+------------------------------------+----------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description |
+======================+====================================+======================+
| Pin 0: Input Data    | decimal - audio                    | Input audio signal   |
+----------------------+------------------------------------+----------------------+
| Pin 1: Current Delay | int - control                      | Current Delay value  |
+----------------------+------------------------------------+----------------------+

| 
| ===== Output Pins =====

+--------------------+------------------------------------+----------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description |
+====================+====================================+======================+
| Pin 0: Output Data | decimal - audio                    | Delayed audio signal |
+--------------------+------------------------------------+----------------------+

| 
| ===== GUI Controls =====

+------------------+---------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range                                | Function Description                                                                                                                                                                                                             |
+==================+===============+======================================+==================================================================================================================================================================================================================================+
| Max              | 1             | 1 - (Depends on Size of the SPI RAM) | This control specifies the maximum delay supported for the current instance in samples (32-bit word). Maximum value of this is calculated depends on the SPI RAM's configuration. Change in this value requires a re-compilation |
+------------------+---------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== Grow Algorithm ===== The module support grow functionality upto four channels and multiple instance is supported.
| ===== Configurations ===== Click on the image |image2| to configure the SPI interface for the module.

| |image3|
| ^GUI Control Name^Default Value^Range^Function Description^

+--------------------------------+--------+----------------------+---------------------------------------------------------------------------------------------------------------------+
| Bit Rate                       | 100kHZ | 100 kHZ - 100000 kHZ | SPI Speed                                                                                                           |
+--------------------------------+--------+----------------------+---------------------------------------------------------------------------------------------------------------------+
| Default Chip/ Device Address   | 1      | 1-7                  | Slave Select for the SPI. Register window should be configured to match this selection.Please refer the note below. |
+--------------------------------+--------+----------------------+---------------------------------------------------------------------------------------------------------------------+
| Sub-Address Bytes              | 2      | 1-4                  | Number of address bytes excluding the read/write command                                                            |
+--------------------------------+--------+----------------------+---------------------------------------------------------------------------------------------------------------------+
| Ram Size                       | 128KB  | 0-32MB               | Total Size of RAM used for delay buffer                                                                             |
+--------------------------------+--------+----------------------+---------------------------------------------------------------------------------------------------------------------+
| SPI Mode                       | Mode 3 | Mode0/Mode3          | SPI operation mode                                                                                                  |
+--------------------------------+--------+----------------------+---------------------------------------------------------------------------------------------------------------------+
| R/W (Chip Address) Bytes       | 1      | 0-255                | Command Bytes (Number of bytes required for command)                                                                |
+--------------------------------+--------+----------------------+---------------------------------------------------------------------------------------------------------------------+
| Write Instruction (SPI)        | 2      | 0-255                | Instruction value for a write operation (0x0 for ADI audio devices, typically 0x2 for eeprom/flash)                 |
+--------------------------------+--------+----------------------+---------------------------------------------------------------------------------------------------------------------+
| Read Instruction (SPI)         | 3      | 0-255                | Instruction value for a read operation (0x1 for ADI audio devices, typically 0x3 for eeprom/flash)                  |
+--------------------------------+--------+----------------------+---------------------------------------------------------------------------------------------------------------------+
| Write-Enable instruction (SPI) | 6      | 0-255                | Instruction value for device write-enable operation                                                                 |
+--------------------------------+--------+----------------------+---------------------------------------------------------------------------------------------------------------------+

| Any change in these SPI configuration parameters requires a recompilation.
| **Note:**\ If the Default Chip/ Device Address is 1 and MP0 is used as chip select, no configuration is required in the register controls. Otherwise particular multipurpose pin should be configured act as the slave select in the register window. (Hardware Configuration -> ICx - ADAU145x Register Controls -> MULTIPURPOSE/ AUXADC)

| |image4|
| \* Slave Select Channel -> 'Slave Select Channel x'

-  MPx pin mode -> 'Slave Select for Master SPI port'
-  MPx pin function -> 'Primary clock or control port function'

| 
| There is some inconsistency between register control and the 'Default chip/Device Address' in the module. The following table shows the mapping between module's parameter and the register control window.

+--------------------------------+------------------------------------------------+
| ' Default chip/Device Address' | 'Slave Select Channel' in the Register control |
+================================+================================================+
| 2                              | Slave Select Channel 0                         |
+--------------------------------+------------------------------------------------+
| 3                              | Slave Select Channel 1                         |
+--------------------------------+------------------------------------------------+
| 4                              | Slave Select Channel 2                         |
+--------------------------------+------------------------------------------------+
| 5                              | Slave Select Channel 3                         |
+--------------------------------+------------------------------------------------+
| 6                              | Slave Select Channel 4                         |
+--------------------------------+------------------------------------------------+
| 7                              | Slave Select Channel 5                         |
+--------------------------------+------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/vco.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/zn.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/spiconfig.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/mp5_slaveselect.jpg
