Master Control Port Boot Time I/O (ADAU145x)
============================================

| :doc:`Click here to return to the Master Control Port page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mastercontrolport>`
| |image1|
| The master control port boot time I/O block allows communication with multiple external devices during DSP program initialization. Typically this block is used to configure an external device like a converter or codec. Communication (read or write) over the master control port bus (i2c or SPI) occurs only once at start-up of the DSP program, and prior to audio processing. Note that currently the module supports only I2C. The data transferred between host and device is defined in a SigmaStudio sequence file which can be generated using the :doc:`SigmaStudio sequence window </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/workspacewindows>`.

How to configure the Control Port I/O block:
--------------------------------------------

| 1) Drag the block into a schematic design.
| 2) Click the Configure... button and select the required protocol and settings for the external device.
| 3) Select a "Sequence File" that defines the desired communication with the device.
| 4) Click "OK". The control port data will be embedded in the DSP program.
| 5) Add multiple instances to configure multiple slaves during the initialization.
| 6) Change the Slave Number in the module to configure the sequence in which the instances are executed.

Control Port Properties
-----------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/bootio_config.jpg
   :align: center

**Protocol:** The master control port bus protocol (SPI or I2C) of the slave device.

**Bitrate:** The master control port bus speed (I2C max 1000kHz, SPI max 20MHz).

**Device Address:**\ *Chip address for I2C.*

**Sub-Address Bytes:** External devices address size, for example 16-bit addressing 2-byte, 24-bit addressing 3-byte.

**(SPI) R/W (Chip Address) Bytes:** Command bytes is applicable, usually a 1-byte instruction for read, write, erase, etc.

**(SPI) Write instruction:** Instruction value for a write operation (0x0 for ADI audio devices, typically 0x2 for eeprom/flash)

**(SPI) Read instruction:** Instruction value for a read operation (0x1 for ADI audio devices, typically 0x3 for eeprom/flash)

**(SPI) Write-Enable instruction:** Instruction value for device write-enable operation (*ignored for Master Control Port I/O Boot*)

**(SPI) Chip Erase instruction:** Instruction value for device chip erase operation (*ignored for Master Control Port I/O Boot*)

**(SPI) Chip Erase Time:** Time delay required for chip erase to complete (*ignored for Master Control Port I/O Boot*)

--------------

**Sequence File:** Device write/read sequence to execute at boot time, define and save this file from :doc:`SigmaStudio's sequence window </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/workspacewindows>`. //

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/bootio.jpg
