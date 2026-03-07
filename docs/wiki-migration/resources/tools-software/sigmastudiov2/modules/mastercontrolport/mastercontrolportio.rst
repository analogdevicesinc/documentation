:doc:`Click here to return to the Master Control Port page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mastercontrolport>`

Master Control Port IO
======================

| 
| |mcp_selfboot_ssp.jpg|
| ===== Description =====
| The master control port I/O block allows communication with one external device during DSP program initialization. Typically this block is used to configure an external device like a converter or codec. Communication (read or write) over the master control port bus (I2C or SPI) occurs only once at start-up of the DSP program, and prior to audio processing. The data transferred between host and device is defined in a SigmaStudio sequence file which can be generated using the sequence window.
| ===== Usage =====
| Click on Settings to configure the parameters.
| ===== Targets Supported =====

+------------------------+------------+-----------------------+---------------+------------------+
| Name                   | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+========================+============+=======================+===============+==================+
| Master Control Port IO | NA         | NA                    | S             | NA               |
+------------------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====
| None
| ===== Configurable Parameters =====

I2C configuration
-----------------

| 
| |mcp\_.wnd.jpg|
| ===GUI Control=== ^GUI Control Name^Default Value^Range^Function Description^ \|Bitrate|400 kHz\| 20 kHZ - 400 kHZ|I2C Speed\| \|Device Address|0|0 – 127|I2C Slave Device Address\| \|Sub-Address Bytes|2|1-4\| Length of the sub address\| \|Sequence file\|-\|-\|Device write/read sequence to execute at boot time.This file can be defined and saved from

SPI configuration
-----------------

| 
| |mcp_spi_wnd_ssp.jpg|

GUI Control
~~~~~~~~~~~

+--------------------------+--------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| GUI Control Name         | Default Value                              | Range                | Function Description                                                                                |
+==========================+============================================+======================+=====================================================================================================+
| Bitrate                  | 100 kHz                                    | 100 kHZ - 100000 kHZ | SPI Speed                                                                                           |
+--------------------------+--------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| SS_M Pin                 | 0                                          | 0                    | SPI Slave Select Channel                                                                            |
+--------------------------+--------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| MP Slave Select Channel  | Disabled(enabled by click on radio button) | 0 - 7                | SPI Slave Select Channel                                                                            |
+--------------------------+--------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| Sub-Address Bytes        | 2                                          | 1-4                  | Length of the sub address                                                                           |
+--------------------------+--------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| Command Length           | 1                                          | 1-4                  | Length of the command sent in bytes                                                                 |
+--------------------------+--------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| Write Instruction        | 0                                          | 0-255                | Instruction value for a write operation (0x0 for ADI audio devices, typically 0x2 for eeprom/flash) |
+--------------------------+--------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| Write-Enable instruction | 6                                          | 0 - 255              | Instruction value for device write-enable operation (ignored for Master Control Port I/O Boot)      |
+--------------------------+--------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters=====
| Not applicable
| ===== DSP Parameter Computation =====
| Not applicable

.. |mcp_selfboot_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/mcp_selfboot_ssp.jpg
.. |mcp\_.wnd.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/mcp_.wnd.jpg
.. |mcp_spi_wnd_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/mcp_spi_wnd_ssp.jpg
