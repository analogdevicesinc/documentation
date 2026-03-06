Interface Write
===============

:doc:`Click here to return to the Inputs and Outputs Toolbox page. </wiki-migration/resources/tools-software/sigmastudio/toolbox/io>`

|image1| |image2|

The Interface Write module writes the value of the parameter setting to the EEPROM when required, so that the parameter setting can be used after the power down(via selfboot).The module can write the value to EEPROM when the parameter value is changed or periodically or an external trigger(rising edge). The module supports writes through SPI or I2C protocols.

| The Interface Write module has the following properties which can be set by the user in the form to configure the I2C or SPI modes. |image3|

|

.. hint::

   NOTE:

   | Make sure that the interface read and interface write modules that are interacting with each other have the same **Interface number paramter**.


| ===== Input Pins =====

+--------------+------------------------------------------+-----------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description        |
+==============+==========================================+=============================+
| Pin 0: Input | decimal- audio                           | Input signal to be filtered |
+--------------+------------------------------------------+-----------------------------+

| 
| ===== Grow Algorithm ===== The module doesn't supports growth functionality. Add is not supported.

GUI Controls
------------

| 
| ^GUI Control Name^Default Value^Range^Function Description^

+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Protocol                       | 1      | 0-1                                        | The Protocol selected - I2C(0) or SPI(1)                                                                                                          |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Bitrate                        | 100kHz | 400/800/1000 kHz(I2C), 100-100000KHz (SPI) | I2C/ SPI Speed                                                                                                                                    |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Sub Address Bytes              | 3      | 1-3                                        | Length of the address for SPI/I2C                                                                                                                 |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Device Address                 | 0      | I2C: Slave address 0-127                   | Slave Adddress                                                                                                                                    |
|                                |        | SPI: Slave select 0-6                      |                                                                                                                                                   |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| SPI Mode                       | 1      | 0-1                                        | SPI Modes 0 or 3                                                                                                                                  |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Command Length                 | 1      | 0-255                                      | This is the SPI R/W instruction bytes                                                                                                             |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Write Instruction (SPI)        | 2      | 0-255                                      | SPI write command bytes                                                                                                                           |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Read Instruction(SPI)          | 3      | 0-255                                      | SPI read command bytes                                                                                                                            |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Write-Enable instruction (SPI) | 6      | 0-255                                      | Write enable for SPI                                                                                                                              |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Write mode                     | 1      | 0-2                                        | The triggering modes for Interface write module, 0- write on Value change, 1-write Periodically with set write interval, 2- write on GPIO trigger |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Write Interval                 | 50ms   | 50-5000ms                                  | Write interval for periodic mode                                                                                                                  |
+--------------------------------+--------+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameter Information =====

================ ============= ====================
GUI Control Name Compiler Name Function Description
================ ============= ====================
================ ============= ====================

+-------------------+-----------------------------------------+---------------------------------------------------------+
| slave select      | device\__Address\_                      | SPI,I2C chip address bytes                              |
+-------------------+-----------------------------------------+---------------------------------------------------------+
| interval          | InterfaceWrite300_Interval              | Write Interval for Periodic mode                        |
+-------------------+-----------------------------------------+---------------------------------------------------------+
| Write Address     | InterfaceWrite300_WriteAddress          | EEPROM location to which data is to be written          |
+-------------------+-----------------------------------------+---------------------------------------------------------+
| Data Length       | InterfaceWrite300_Data Bytes            | Length of the data to be written to the EEPROM in bytes |
+-------------------+-----------------------------------------+---------------------------------------------------------+
| SPI Mode          | InterfaceWrite300_SPI_Mode              | SPI mode select, Mode 0 or Mode3                        |
+-------------------+-----------------------------------------+---------------------------------------------------------+
| SPI Read Command  | InterfaceWrite300_SPI_read_instruction  | SPI read instruction bytes                              |
+-------------------+-----------------------------------------+---------------------------------------------------------+
| SPI write Command | InterfaceWrite300_SPI_write_instruction | SPI write instruction bytes                             |
+-------------------+-----------------------------------------+---------------------------------------------------------+
| SPI wren Command  | InterfaceWrite300_SPI_wren_instruction  | SPI write enable instruction bytes                      |
+-------------------+-----------------------------------------+---------------------------------------------------------+
| Sub Byte address  | address_Length\_                        | SPI/I2C address length                                  |
+-------------------+-----------------------------------------+---------------------------------------------------------+

|

.. hint::

   NOTE:


   | The Periodic mode of operation of interface write for SPI requires some delay to be inserted after the write, the default value of which is set to 1ms. Every successive instance of the module will have an increment in the delay given by (interface number*delay). This is available as a DSP parameter whose value can be set by writting the value to the particular memory location of the dsp parameter -**InterfaceWrite300_delayLoopCount**.


Algorithm Description
---------------------

|

| Interface write module allows the user to write data to a device(self-boot eeprom) over I2C or SPI. The cell has a form which allows the user to configure the modes and choose among the three write modes -write on 1.Value change 2.Periodic 3.GPIO trigger. The user can configure the I2C and SPI registers using the Interface Write properties form.
| ===== Example =====

Use Case 1
~~~~~~~~~~

|image4| The interface write module can be used an outpur moudule to the UPDown LUT. The Interface write module writes the output of the UPDown LUT parameter setting to the EEPROM if the conditions to write are satisfied.

Use Case 2
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/usecase2.png
   :align: center

The Interface write module can be used to store any the parameter setting to the EEPROM and read it back during the selfboot using the corresponding Interface read module. When the GPIO trigger is a rising edge signal, the Interface write module will write to the EEPROM. During the powerdown, a rising edge signal can be provided in the GPIO to store the interface value to EEPROM.

| 

Supported IC's
--------------

1. ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/interface_write_treetool.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/interfacewirte.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/interface_write_form_only.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/usecase1.png
