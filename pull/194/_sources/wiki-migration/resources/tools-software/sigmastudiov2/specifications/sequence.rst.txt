:doc:`Return to the specifications page </wiki-migration/resources/tools-software/sigmastudiov2/specifications>`

Sequence XML File
=================

The first line is the XML Prelog

::

   <?xml version="1.0" standalone="no"?>

| 
| **<ROM>** is the root element of the Sequence XML.
| Root element contains **<dateTime>**, **<version>**, **<schemaVersion>** and one or more **<page>** elements.

-  dateTime - Date and time of generation of the xml file.
-  version - Version of SigmaStudio+ used for generating the XML.
-  schemaVersion - Schema version of the XML generated from SigmaStudio+.
-  page - Contains a sequence of read, write and delay commands for a given mode.

.. note::

   Multiple sequences can be stored within one Sequence File. Each of the sequence of commands is a mode and is represented as **<page>** element. There can be multiple <page> elements in one Sequence File.


.. note::

   Sequence XMLs generated from SigmaStudio+ 2.3.0 version and beyond, have the sequence schema version as 2.0. Legacy SS/SS+ sequence XMLs do not have this schemaVersion element.


<page> Element
--------------

**modetype** attribute under <page> indicates the name of the mode. Each mode has multiple commands represented by **<action>** element.

Each **action** item represents a single sequence command. Each command can have different fields to represent different information of the sequence.

**instr** - Instruction for performing various operations with xml

-  For delay → instr=“delay”
-  For write → instr=“writeXbytes”
-  For read → instr=“read”

**SpiCmd** - Target specific SPI Command applicable to certain peripherals and transeivers. Applicable when protocol is "SPI".

**SpiCmdWidth** - Width of the SPI Command in bytes. Applicable when protocol is "SPI".

**addr_width** - Represents the width address in bytes.

**data_width** - Represents the width of data in words.

**len** - Represents the number of values to read/write including address width.

-  len = number of words to read/write + address width in bytes.

**addrformat** - Format of the address.

-  addrformat="hex" will be present when the addresses are represented in hexadecimal format. This attribute will not be present otherwise.

.. note::

   Check the "Address in hex" checkbox to store address in hexadecimal format.


**addr** - Represents the starting address to read/write registers.

**i2caddr** - Represents the I2C device address. Applicable when protocol is "I2C".

**SpiCS** - Represents the SPI chip select. Applicable when protocol is "SPI".

.. note::

   "Device ID" field in the Sequence Window is used for i2caddr and SpiCS depending on the protocol selected


**AddrIncr** - Register or Word length in Bytes. Applicable for memory writes (DSP, EEPROM etc).

**DataAlignment** - Specifies the alignment requirement in bytes for the start of the data following SPI Command and address. Applicable when protocol is "SPI".

.. note::

   Example: If SpiCmdWidth=1, addr_width=2, DataAlignment=4, then there will be an extra byte <zeros> added after command and address such that the data starts at a 4-byte aligned location.


**Protocol** - Represents the communication protocol.

-  For I2C protocol → Protocol=“I2C”.
-  For SPI protocol → Protocol=“SPI”.

.. note::

   When I2C protocol is selected, SPI related fields will be present in the command, but are ignored. Similarly, when SPI protocol is selected, I2C related fields will be present in the command, but are ignored.


**CellName** - Represents the component to which the sequence belongs to.

**ParamName** - Represents the name of the parameter or register being read/written.

**Data section** - The hexadecimal entries encapsulated in between the action tokens **<action></action>** represent the write/read values or delay duration time.

.. note::

   The **delay** commands will have **data_width**, **CellName**, **ParamName** and **data** fields in the sequence command. Since rest of the fields are not applicable for the delay command, they are not seen in the sequence XML.


.. note::

   Differences between traditional SigmaStudio XMLs and Sigmastudio+ 2.0 schema XMLs -

   
   -  **SpiCS** - This new field in the new scheme represents the SPI chip select. Applicable when protocol is "SPI".
   -  **DataAlignment** - This new field in the new scheme specifies the alignment requirement in bytes for the start of the data following SPI Command and address. Applicable when protocol is "SPI".
   -  **AddrIncr** - This field generated from SigmaStudio+ 2.0 schema version will always be non-zero.
   -  The new SigmaStudio+ 2.0 schema XMLs have their sequence fields re-arranged to align more towards the A2B command list XML format.
   


.. tip::

   Click here for A2B :doc:`Command List XML </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/cmdlistxml>` and :doc:`Peripheral xml </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/peripheralxml>` Specification

