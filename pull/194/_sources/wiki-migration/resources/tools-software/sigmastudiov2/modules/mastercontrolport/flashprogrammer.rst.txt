:doc:`Click here to return to the Master Control Port page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mastercontrolport>`

Flash Programmer
================

| 
| |fp_ssp.jpg|
| ===== Description =====
| This module provides support to write raw data to the external flash memory using I2C/SPI. The I2C/SPI write is performed during the initialization before the audio processing in the schematic is started.
| ===== Usage =====
| ==== Writing a Wav file to SPI EEPROM using Flash Programmer (ADAU1452) ====

-  Add Flash Programmer module to the schematic.
-  Configure SPI parameters in the Control Port Properties window. (Below window shows SPI configuration required to write to EEPROM in EVAL-ADAU1452MINIZ board)

| 
| |fp_window_ssp.jpg|
| \* Select Binary mode

-  Select the Wav file to be written (Make sure size of the wav file is not greater than the size of EEPROM. In the case of EVAL-ADAU1452MINIZ, size of wav file should not be greater than 128 KB)
-  Press OK. Then Link compile download.
-  Press Write to write the data to the EEPROM
-  The Output window indicates the progress of writing to the EEPROM

| 
| |image1|
| \* To verify the data written to the flash, click on the read button. The output window will indicate the verification status
| |image2|
| ===== Targets Supported =====

+------------------+------------+-----------------------+---------------+------------------+
| Name             | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==================+============+=======================+===============+==================+
| Flash Programmer | NA         | NA                    | S             | NA               |
+------------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====
| None
| ===== Configurable Parameters =====

+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name                    | Default Value | Range                                                             | Function Description                                                                                                                                                 |
+=====================================+===============+===================================================================+======================================================================================================================================================================+
| Protocol                            | SPI           | SPI/I2C                                                           | Master Control Port Protocol                                                                                                                                         |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPIBitrate                          | 100kHZ        | 100 kHZ - 100000 kHZ (for SPI)/ 400 or 800 or 1000 kHz (for I2C)  | SPI/I2C Speed                                                                                                                                                        |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPISlaveSelect                      | 0             | 0-6                                                               | Slave Select for the SPI. Register window should be configured to match this selection.Please refer the note below.                                                  |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SubAddressBytes                     | 2             | 1-4                                                               | Number of address bytes excluding the read/write command                                                                                                             |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PageSize                            | 128KB         | 0-32MB                                                            | Page Size of Flash                                                                                                                                                   |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPIMode                             | Mode 3        | Mode0/Mode3                                                       | SPI operation mode                                                                                                                                                   |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPICommandLength                    | 1             | 0-255                                                             | Command Bytes (Number of bytes required for command)                                                                                                                 |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPIWriteInstruction                 | 2             | 0-255                                                             | Instruction value for a write operation (0x0 for ADI audio devices, typically 0x2 for eeprom/flash)                                                                  |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPIReadInstruction                  | 3             | 0-255                                                             | Instruction value for a read operation (0x1 for ADI audio devices, typically 0x3 for eeprom/flash)                                                                   |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPIWriteEnableInstrcution           | 6             | 0-255                                                             | Instruction value for device write-enable operation                                                                                                                  |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IsSPIBlockProtectionUnlockEnabled   | false         | true/false                                                        | Block Protection Unlock enable                                                                                                                                       |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPIBlockProtectionUnlockInstruction | 152           | 0-255                                                             | Block Protection Unlock command for SPI falsh devices. This is an optional command. This can be disabled.                                                            |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPIChipEraseInstruction             | 96            | 0-255                                                             | Instruction value for device erase operation                                                                                                                         |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPIChipEraseTime                    | 5 sec         | 1-600 sec                                                         | Time required for chip erase operation                                                                                                                               |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IsSPIBlockEraseInstructionEnabled   | false         | true/false                                                        | Block erase enable                                                                                                                                                   |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPIBlockEraseInstruction            | 216           | 0-255                                                             | Block/Sector erase command for SPI falsh devices. This is an optional command. This can be disabled.                                                                 |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPIBlockAddressToErase              | 0             | 0-16777215                                                        | Block/Sector address to erase SPI falsh devices by block/section. This is an optional command. This can be disabled by disabling the Block/Sector Ersae Insutruction |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FilePath_File<fc #ff0000>X</fc>     | NA            | NA                                                                | Raw data to be written to the flash (Can be ascii text file/ binary files like wav file)                                                                             |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DataFileType                        | ASCII         | ASCII/Binary                                                      | Mode to write the file. Audio files like .wav should be written in binary mode                                                                                       |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IsConfigurableAddress               | Disabled      | Enable/Disable                                                    | Enable/Disable the start address for each files                                                                                                                      |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| StartAddress_File<fc #ff0000>X</fc> | 0             | 0 - Maximum of FLASH/EEPROM Size in bytes(Increment by page size) | Write the data in the flash/e2prom from the specified address                                                                                                        |
+-------------------------------------+---------------+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Any change in these SPI/I2C configuration parameters requires a recompilation.

| 
| ===== DSP Parameters=====
| Not applicable
| ===== DSP Parameter Computation =====
| Not applicable

.. |fp_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/fp_ssp.jpg
.. |fp_window_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/fp_window_ssp.jpg
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/fp_op_wnd_ssp.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/fp_verify_op_wnd_ssp.jpg
   :width: 400px
