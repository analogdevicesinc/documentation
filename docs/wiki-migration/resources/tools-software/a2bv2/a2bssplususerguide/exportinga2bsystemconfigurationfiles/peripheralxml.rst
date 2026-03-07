:doc:`Return to the export specifications page </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`

Peripheral Xml Specification
============================

XML uses tags that are not predefined or standard, which means that they are created by the person who is writing the XML file. Usually, the first tag begins by specifying the XML version and the encoding being used. This is standard tag and is called prolog.

The XML Prelog is as below

::

   <?xml version="1.0" standalone="no"?>

| 
| **<ROM>** is the root element of the Sequence XML.
| Root element contains **<dateTime>**, **<version>** and one or more **<page>** elements.

-  dateTime - Date and time of generation of the xml file.
-  version - Version of SigmaStudio+ used for generating the XML.
-  page - Contains a sequence of read, write and delay commands for a given mode.

.. note::

   Multiple sequences can be stored within one Sequence File. Each of the sequence of commands is a mode and is represented as <page> element. There can be multiple <page> elements in one Sequence File.


<page> Element
--------------

**modetype** attribute under **<page>** indicates the name of the mode. Each mode has multiple commands represented by **<action>** element.. The attributes of the <action> element are given below.

\*\* instr \*\* - Instruction for performing various operations with xml

-   For delay -> instr="delay"
-   For write -> instr="writeXbytes"
-   For read -> instr="read"

\*\* SpiCmd \*\* – This field is reserved for future use and currently set as 0.

\*\* SpiCmdWidth \*\* – This field is reserved for future use and currently set as 0.

\*\* addr_width \*\* - Represents address width

-  For 1 byte address -> addr_width="1"
-  For 2 byte address -> addr_width="2"

\*\* data_width \*\* – Represents width of data in bytes

-  For 1 byte width -> data_width="1"
-  For 2 byte width -> data_width="2"

\*\* len \*\* - Represents the number of values to read/write including address width

-  len = “n” values to read / write + address width

\*\* addrformat \*\* - Format of the address.

-  addrformat=“hex” will be present when the addresses are represented in hexadecimal format. This attribute will not be present otherwise

\*\* addr \*\* - Represents the starting address to read/write registers in decimal

-  Ex: addr=”0”, It will start reading/writing the registers address from 0x00.

\*\* i2caddr \*\* - Represents the device address in decimal

-  Ex: For device address 0x50, -> i2caddr="80"

\*\* SpiCS \*\* - Represents the SPI chip select. For I2C commands, it is set as 0

\*\* addrincr \*\* - Register or Word length in Bytes. Applicable for memory writes (DSP, EEPROM etc).

-  For 1 byte addr increment -> addrincr = 1 or addrincr = 0
-  For n byte addr increment -> addrincr = n

\*\* DataAlignment \*\* - Specifies the alignment requirement in bytes for the start of the data following SPI Command and address. Applicable when protocol is “SPI”.

.. note::

   Example: If SpiCmdWidth=1, addr_width=2, DataAlignment=4, then there will be an extra byte <zeros> added after command and address such that the data starts at a 4-byte aligned location.


\*\* Protocol \*\* - Represents the communication protocol.

-  For I2C protocol -> Protocol="I2C"
-  For SPI protocol -> Protocol="SPI"

\*\* CellName \*\* – Represents the label name of platforms in SigmaStudio / SigmaStudio+

\*\* ParamName \*\* – Represents the register names of transceivers / peripherals

\*\* Data \*\* bytes are followed by ParamName

Table on Differences in xml specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following table represents the differences in command list xml format for different versions of A2B plugin

+-------------------------------------------------------+
| \*\* Xml Fields\ **\|** SigmaStudio+                  |
| (ADI_A2B-SSPlus_Software-Rel1.3.1) **\|** SigmaStudio |
| (ADI_A2B_Software-Rel19.10.x) **\|** SigmaStudio      |
| (ADI_A2B_Software-Rel19.4.5) \*\*                     |
+-------------------------------------------------------+

| Protocol                                              |

+-------------------------------------------------------+

| CellName(Peripheral)                                  |

+-------------------------------------------------------+

| SpiCmd                                                |

+-------------------------------------------------------+

| SpiCmdWidth                                           |

+-------------------------------------------------------+

| SpiCS                                                 |

+-------------------------------------------------------+

| DataAlignment                                         |

+-------------------------------------------------------+

| addrformat                                            |

+-------------------------------------------------------+

.. important::

   Refer :doc:`Sequence Window Specification </wiki-migration/resources/tools-software/sigmastudiov2/specifications/sequence>` for more details

