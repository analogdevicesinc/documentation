:doc:`Click here to return to the Master Control Port page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mastercontrolport>`

SPI Read
========

| 
| |spi_read_ssp.jpg|

Description
-----------

| 
| There are two different versions of the SPI Read module.

-  SPI Periodic Read
-  SPI Read with External Trigger

SPI Periodic Read
-----------------

| The 'SPI Periodic Read' block reads a particular sub address from any SPI slave periodically and sends the value read in the output pin.
| ===== Usage =====
| Click on Settings to configure the parameters for SPI read.
| |spi_read_wndw_ssp.jpg|
| To monitor multiple registers in the same slave, create multiple instances of the cell.
| === Support for Different Slave Select=== If the device to be programmed is selected through MP0 (the /SS_M pin), no configuration is required in the register controls. Otherwise, the multipurpose pin must be configured to act as the slave select in the Register Window. (Hardware Configuration → ICx - ADAU145x Register Controls → MULTIPURPOSE/AUXADC) |image1|
| \* Slave Select Channel -> 'Slave Select Channel x'

-  MPx pin mode -> 'Slave Select for Master SPI port'
-  MPx pin function -> 'Multipurpose function'

| 
| The following table shows the mapping between the module's parameter and the register control window. Please note that for some other blocks, there is an offset of 1 between the module parameter and the register control window.

+----------------------------------------+------------------------------------------------+
| 'Slave Select' in Configuration Window | 'Slave Select Channel' in the Register control |
+========================================+================================================+
| 0                                      | Slave Select Channel 0                         |
+----------------------------------------+------------------------------------------------+
| 1                                      | Slave Select Channel 1                         |
+----------------------------------------+------------------------------------------------+
| 2                                      | Slave Select Channel 2                         |
+----------------------------------------+------------------------------------------------+
| 3                                      | Slave Select Channel 3                         |
+----------------------------------------+------------------------------------------------+
| 4                                      | Slave Select Channel 4                         |
+----------------------------------------+------------------------------------------------+
| 5                                      | Slave Select Channel 5                         |
+----------------------------------------+------------------------------------------------+

| 
| ===== Targets Supported =====

+-------------------+------------+-----------------------+---------------+------------------+
| Name              | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===================+============+=======================+===============+==================+
| SPI Periodic Read | NA         | NA                    | S             | NA               |
+-------------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====
| ====Output Pins====

======== ======= ==========================
Name     Type    Description
======== ======= ==========================
SPI Data Control Outputs data read over SPI
======== ======= ==========================

| 
| ===== Configurable Parameters =====

+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| GUI Control Name      | Default Value | Range                           | Function Description                                                                               |
+=======================+===============+=================================+====================================================================================================+
| SPIBitrate            | 100 kHz       | 100 kHZ - 100000 kHZ            | SPI Speed                                                                                          |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| SPISlaveSelectChannel | 0             | 0 – 6                           | SPI Slave Select Channel                                                                           |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| SPIMode               | SPI Mode 3    | Mode 0/ Mode 3                  | SPI protocol mode                                                                                  |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| DataLength            | 4             | 1-4                             | Length of the data to be read                                                                      |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| AddressLength         | 2             | 1-4                             | Length of the sub address                                                                          |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| Read Interval         | 50 ms         | 50 - 5000 ms                    | Interval between 2 consecutive SPI Read                                                            |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| AddressToRead         | 0             | 0 to Pow(2, Address Length) - 1 | Address to be read from                                                                            |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| SPIReadInstruction    | 1             | 0-255                           | Instruction value for a read operation (0x1 for ADI audio devices, typically 0x3 for eeprom/flash) |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| SPICommandLength      | 1             | 1-4                             | Length of the command sent in bytes                                                                |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| InitialOutputValue    | 0             | -2147483648 to 2147483647       | Value in the output pin till the first read is complete.                                           |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters=====
| ^ Parameter Name ^ Description^ ADAU145x/146x ^

+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| spiSpeed        | SPI Speed                                                                                          | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| spiMode         | SPI Protocol Mode                                                                                  | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| slaveSelect     | SPI Slave Select Channel                                                                           | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| readAddress     | Address to be read from                                                                            | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| addressLength   | Length of the sub address                                                                          | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| dataLength      | Length of the data to be read                                                                      | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| commandLength   | Length of the command sent in bytes                                                                | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| readInstruction | Instruction value for a read operation (0x1 for ADI audio devices, typically 0x3 for eeprom/flash) | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+

| 
| ===== DSP Parameter Computation =====
| readAddress = AddressToRead < <(8\* (4 - (AddressLength + SPICommandLength))
| readInstruction = SPIReadInstruction < < (8\* AddressLength)+  [1]_

SPI Read with external Trigger
------------------------------

| The 'SPI Read with external Trigger' block reads a particular sub address from any I2C slave when a rising edge is detected in the input pin.
| ===== Usage =====
| Click on |image2| to configure the parameters for SPI read.
| |image3| To monitor multiple registers in the same slave, create multiple instances of the cell.
| === Support for Different Slave Select=== If the device to be programmed is selected through MP0 (the /SS_M pin), no configuration is required in the register controls. Otherwise, the multipurpose pin must be configured to act as the slave select in the Register Window. (Hardware Configuration → ICx - ADAU145x Register Controls → MULTIPURPOSE/AUXADC) |image4|
| \* Slave Select Channel -> 'Slave Select Channel x'

-  MPx pin mode -> 'Slave Select for Master SPI port'
-  MPx pin function -> 'Multipurpose function'

| 
| The following table shows the mapping between the module's parameter and the register control window. Please note that for some other blocks, there is an offset of 1 between the module parameter and the register control window.

+----------------------------------------+------------------------------------------------+
| 'Slave Select' in Configuration Window | 'Slave Select Channel' in the Register control |
+========================================+================================================+
| 0                                      | Slave Select Channel 0                         |
+----------------------------------------+------------------------------------------------+
| 1                                      | Slave Select Channel 1                         |
+----------------------------------------+------------------------------------------------+
| 2                                      | Slave Select Channel 2                         |
+----------------------------------------+------------------------------------------------+
| 3                                      | Slave Select Channel 3                         |
+----------------------------------------+------------------------------------------------+
| 4                                      | Slave Select Channel 4                         |
+----------------------------------------+------------------------------------------------+
| 5                                      | Slave Select Channel 5                         |
+----------------------------------------+------------------------------------------------+

| 
| ===== Targets Supported =====

+--------------------------------+------------+-----------------------+---------------+------------------+
| Name                           | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================================+============+=======================+===============+==================+
| SPI Read with External Trigger | NA         | NA                    | Sample        | NA               |
+--------------------------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====
| ====Input Pins====
| ^Name^Type^Description^

======= ======= =========================================
Trigger Control Rising edge in this signal initiates read
======= ======= =========================================

| 
| ====Output Pins====
| ^Name^Type^Description^

======== ======= ==========================
SPI Data Control Outputs data read over SPI
======== ======= ==========================

| 
| ===== Configurable Parameters =====

Configurable Parameters
-----------------------

+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| GUI Control Name      | Default Value | Range                           | Function Description                                                                               |
+=======================+===============+=================================+====================================================================================================+
| SPIBitrate            | 100 kHz       | 100 kHZ - 100000 kHZ            | SPI Speed                                                                                          |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| SPISlaveSelectChannel | 0             | 0 – 6                           | SPI Slave Select Channel                                                                           |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| SPIMode               | SPI Mode 3    | Mode 0/ Mode 3                  | SPI protocol mode                                                                                  |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| DataLength            | 4             | 1-4                             | Length of the data to be read                                                                      |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| AddressLength         | 2             | 1-4                             | Length of the sub address                                                                          |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| AddressToRead         | 0             | 0 to Pow(2, Address Length) - 1 | Address to be read from                                                                            |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| SPIReadInstruction    | 1             | 0-255                           | Instruction value for a read operation (0x1 for ADI audio devices, typically 0x3 for eeprom/flash) |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| SPICommandLength      | 1             | 1-4                             | Length of the command sent in bytes                                                                |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+
| InitialOutputValue    | 0             | -2147483648 to 2147483647       | Value in the output pin till the first read is complete.                                           |
+-----------------------+---------------+---------------------------------+----------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters=====
| ===== DSP Parameters=====
| ^ Parameter Name ^ Description^ ADAU145x/146x ^

+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| spiSpeed        | SPI Speed                                                                                          | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| spiMode         | SPI Protocol Mode                                                                                  | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| slaveSelect     | SPI Slave Select Channel                                                                           | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| readAddress     | Address to be read from                                                                            | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| addressLength   | Length of the sub address                                                                          | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| dataLength      | Length of the data to be read                                                                      | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| commandLength   | Length of the command sent in bytes                                                                | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+
| readInstruction | Instruction value for a read operation (0x1 for ADI audio devices, typically 0x3 for eeprom/flash) | Integer32 |
+-----------------+----------------------------------------------------------------------------------------------------+-----------+

| 
| ===== DSP Parameter Computation =====
| readAddress = AddressToRead < <(8\* (4 - (AddressLength + SPICommandLength))
| readInstruction = SPIReadInstruction < < (8\* AddressLength)+  [2]_

.. [1]
   8\* (4 - (AddressLength + SPICommandLength

.. [2]
   8\* (4 - (AddressLength + SPICommandLength

.. |spi_read_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/spi_read_ssp.jpg
.. |spi_read_wndw_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/spi_read_wndw_ssp.jpg
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/slave_selection_mpx_ssp.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/spi.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/spi_read_wndw_ssp.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/slave_selection_mpx_ssp.jpg
   :width: 400px
