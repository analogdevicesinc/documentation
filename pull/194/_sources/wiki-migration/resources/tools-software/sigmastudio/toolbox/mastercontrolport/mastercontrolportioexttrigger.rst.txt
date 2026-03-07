Master Control Port Runtime Sequential Write (ADAU145x)
=======================================================

| :doc:`Click here to return to the Master Control Port page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mastercontrolport>`

| The master control port Runtime Sequential Write block allows communication with external devices during audio processing. Typically this block is used to transfer data to an external device like a converter or codec. Communication over the master control port bus (I2C or SPI) occurs once per external trigger. The data transferred between host and device is defined in a SigmaStudio sequence file which can be generated using the :doc:`SigmaStudio sequence window </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/workspacewindows>`.
| |image1|

Input Pins
----------

+----------------+------------------------------------+-------------------------------------------------------------------+
| Name           | Format [int/dec] - [control/audio] | Function Description                                              |
+================+====================================+===================================================================+
| Pin 0: Trigger | decimal - control                  | Rising edge in the trigger signal, initiates the sequential write |
+----------------+------------------------------------+-------------------------------------------------------------------+

Output Pins
-----------

+---------------------+------------------------------------+--------------------------------------------------------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description                                                     |
+=====================+====================================+==========================================================================+
| Pin 0: Write Status | decimal - control                  | Outputs 1 while the sequential write is in progress. otherwise outputs 0 |
+---------------------+------------------------------------+--------------------------------------------------------------------------+

Configuration
-------------

Click on |image2| to configure the parameters.

I2C configuration
~~~~~~~~~~~~~~~~~

| |image3|
| ===GUI Control===

+-------------------+---------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name  | Default Value | Range            | Function Description                                                                                                                                                                                                            |
+===================+===============+==================+=================================================================================================================================================================================================================================+
| Bitrate           | 400 kHz       | 20 kHZ - 400 kHZ | I2C Speed                                                                                                                                                                                                                       |
+-------------------+---------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Device Address    | 0             | 0 – 127          | I2C Slave Device Address                                                                                                                                                                                                        |
+-------------------+---------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sub-Address Bytes | 2             | 1-4              | Length of the sub address                                                                                                                                                                                                       |
+-------------------+---------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sequence file     | -             | -                | Device write/read sequence to execute at boot time.This file can be defined and saved from :doc:`SigmaStudio's sequence window </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/workspacewindows>`. |
+-------------------+---------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 

SPI configuration
~~~~~~~~~~~~~~~~~

| |image4|

GUI Control
^^^^^^^^^^^

+--------------------------+---------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| GUI Control Name         | Default Value                               | Range                | Function Description                                                                                |
+==========================+=============================================+======================+=====================================================================================================+
| Bitrate                  | 100 kHz                                     | 100 kHZ - 100000 kHZ | SPI Speed                                                                                           |
+--------------------------+---------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| SS_M Pin                 | 0                                           | 0                    | SPI Slave Select                                                                                    |
+--------------------------+---------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| MP Slave Select Channel  | Disabled (Enabled by click on radio button) | 0 – 7                | SPI Slave Select Channel                                                                            |
+--------------------------+---------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| Sub-Address Bytes        | 2                                           | 1-4                  | Length of the sub address                                                                           |
+--------------------------+---------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| Command Length           | 1                                           | 1-4                  | Length of the command sent in bytes                                                                 |
+--------------------------+---------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| Write Instruction        | 0                                           | 0-255                | Instruction value for a write operation (0x0 for ADI audio devices, typically 0x2 for eeprom/flash) |
+--------------------------+---------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+
| Write-Enable instruction | 6                                           | 0 - 255              | Instruction value for device write-enable operation (ignored for Master Control Port I/O Boot)      |
+--------------------------+---------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------+

| 

Steps to Configure
~~~~~~~~~~~~~~~~~~

-   Drag the block into a schematic design.
-   Open the control port property window by clicking on |image5| image and configure all the required properties.
-   Ensure that the 'Sub-Address Bytes:' and the 'Device Address' are entered correctly.
-   Select a "Sequence File" that defines the desired communication with the device.
-   Click "OK". The control port data will be embedded in the DSP program. **This step is necessary whenever the sequence file is modified.**
-   Connect the trigger signal to the input pin.
-   Add multiple instances to configure multiple slaves during the runtime.

| 
| ===== Support for Multiple Slaves ===== Multiple external devices can be configured by creating multiple instances of the Runtime Sequential Write module and selecting appropriate slave select pins in the configuration parameters as detailed below.
| ===== Support for Different SPI Slave Select ===== If the device to be programmed is selected through MP0 (the /SS_M pin), no configuration is required in the register controls. Otherwise, the multipurpose pin must be configured to act as the slave select in the Register Window. (Hardware Configuration → ICx - ADAU145x Register Controls → MULTIPURPOSE/AUXADC)

| |image6|
| \* Slave Select Channel -> 'Slave Select Channel x'

-  MPx pin mode -> 'Slave Select for Master SPI port'
-  MPx pin function -> 'Multipurpose function'

| 
| The following table shows the mapping between the module's parameter and the register control window. Please note that for some other blocks, there is an offset of 1 between the module parameter and the register control window.

+----------------------------------------+-------------------------------------------------------+
| 'Slave Select' in Configuration Window | 'Slave Select Channel' in the Register Control Window |
+========================================+=======================================================+
| 0                                      | Slave Select Channel 0                                |
+----------------------------------------+-------------------------------------------------------+
| 1                                      | Slave Select Channel 1                                |
+----------------------------------------+-------------------------------------------------------+
| 2                                      | Slave Select Channel 2                                |
+----------------------------------------+-------------------------------------------------------+
| 3                                      | Slave Select Channel 3                                |
+----------------------------------------+-------------------------------------------------------+
| 4                                      | Slave Select Channel 4                                |
+----------------------------------------+-------------------------------------------------------+
| 5                                      | Slave Select Channel 5                                |
+----------------------------------------+-------------------------------------------------------+

| 

Creating Sequence File for SPI/I2C slave not supported by SigmaStudio
---------------------------------------------------------------------

Use the following file and edit for your slave.

.. code:: xml

   <?xml version="1.0" standalone="no"?>
   <ROM IC="ADAU1361" IC_Address="112" Address_byte_length="2">
     <dateTime>2017-03-16T05:12:14.2859851Z</dateTime>
     <version>3.14.1.1593</version>
     <page modetype="Mode 0">
       <action instr="writeXbytes" len="3" addr="16384" ParamName="Reg1" DspName="IC 1">0F</action>
       <action instr="writeXbytes" len="8" addr="16386" ParamName="Reg2" DspName="IC 1">00 FD 00 0C 20 01</action>
       <action instr="delay" ParamName="IC 1.Delay" DspName="IC 1">00 64</action>
       <action instr="writeXbytes" len="3" addr="16405" ParamName="IC 1.Serial Port Control Registers.Serial Port Control 0" DspName="IC 1">00</action>
     </page>
   </ROM>

Please follow the steps below to edit the XML for your Slave.

-  Edit IC, IC_Address and Address_byte_length fields in xml. Please note that IC_Address should be an 8-bit I2C address in decimal format. Address_byte_length refers to the length, in bytes, of the external IC's address space.

.. code:: xml

   <ROM IC="ADAU1361" IC_Address="112" Address_byte_length="2">

-  Add your register writes as shown below.

.. code:: xml

   <action instr="writeXbytes" len="8" addr="16386" ParamName="Reg2" DspName="IC 1">00 FD 00 0C 20 01</action>

::

   Please match all the fields as follows. 
         instr => "writeXBytes" 
         len => Data Length in bytes+ Address_byte_length
         addr => Register Address in decimal (not hexadecimal)
         Then the value part should have the register values in Hexadecimal. A space should separate each data as shown in the example.   In this example len => 6 (data length)  + 2 (Address_byte_length) = 8

-  You can add delays as shown below.

.. code:: xml

   <action instr="delay" ParamName="IC 1.Delay" DspName="IC 1">00 64</action>

Delay is in milliseconds (Hexadecimal Format)

Supported ICs
-------------

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/mcpruntime.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/i2c_spi.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/masterbooti2cconfig.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/masterbootspiconfig.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/i2c_spi.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/mp5_slaveselect.jpg
