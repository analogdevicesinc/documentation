:doc:`Return to the export specifications page </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`

Command List Xml Specification
==============================

XML uses tags that are not predefined or standard, which means that they are created by the person who is writing the XML file. Usually, the first tag begins by specifying the XML version and the encoding being used. This is standard tag and is called prolog.

**<Version_Info>** - Lists the version of A2B Plugin, Stack and SigmaStudio+ / SigmaStudio used

-  A2BDLL_Version
-  A2BStackDLL_Version
-  SigmaStudio_Version

\*\* <page modetype="Mode 0"> \*\* - indicates the name of the mode and lists the contents of the xml. Each mode has multiple commands represented by <action> element. Only one mode is supported for command list xml

::

   <action instr="writeXbytes" SpiCmd="0" SpiCmdWidth="1" addr_width="2" data_width="1" len="4" addr="62464" i2caddr="56" AddrIncr="0" Protocol="I2C" ParamName="IC 1.HIBERNATE">00 01</action>

\*\* instr \*\* - Instruction for performing various operations with xml

-   For delay -> instr="delay"
-   For write -> instr="writeXbytes"
-   For read -> instr="read"

\*\* SpiCmd \*\* – Spi command read /written

-  Available only for SPI commands. For I2C commands, it is set as 0.

.. note::

   Refer SPI Programming Concepts in :adi:`AD243x Programming Reference Manual <en/gated/a2b/a2b-technology.html>` for more details


\*\* SpiCmdWidth \*\* – Represents spi command width in bytes

-  Available only for SPI commands. For I2C commands, it is set as 0

\*\* addr_width \*\* - Represents address width

-  For 1 byte address -> addr_width="1"
-  For 2 byte address -> addr_width="2"

\*\* data_width \*\* – Represents width of data in bytes

-  For 1 byte width -> data_width="1"
-  For 2 byte width -> data_width="2"

\*\* len \*\* - Represents the number of values to read/write including address width

-  len = “n” values to read / write + address width

\*\* addr \*\* - Represents the starting address to read/write registers in decimal

-  Ex: addr=”0”, It will start reading/writing the registers address from 0x00.

\*\* i2caddr \*\* - Represents the device address in decimal

-  Ex: For device address 0x50, -> i2caddr="80"

.. note::

   i2caddr is ignored when SPI interface is used


\*\* addrincr \*\* - Register or Word length in Bytes. Applicable for memory writes (DSP, EEPROM etc).

-  For 1 byte addr increment -> addrincr = 1 or addrincr = 0
-  For n byte addr increment -> addrincr = n

\*\* Protocol \*\* - Represents the communication protocol.

-  For I2C protocol -> Protocol="I2C"
-  For SPI protocol -> Protocol="SPI"

\*\* CellName \*\* – Represents the label name of platforms in SigmaStudio / SigmaStudio+

\*\* ParamName \*\* – Represents the register names of transceivers / peripherals

Data bytes are followed by ParamName

Table on Differences in xml specification
-----------------------------------------

Following table represents the differences in command list xml format for different versions of A2B plugin

+----------------------------------------------------------+
| \*\* Xml Fields\ **\|** SigmaStudio+                     |
| (ADI_A2B-SSPlus_Software-Rel1.3.2) **\|** SigmaStudio    |
| (ADI_A2B_Software-Rel19.10.x) **\|** SigmaStudio         |
| (ADI_A2B_Software-Rel19.4.5) \*\*                        |
+----------------------------------------------------------+

| A2BDLL_Version (A2B Plugin Version)                      |

+----------------------------------------------------------+

| A2BStackDLL_Version (A2B Stack version)                  |

+----------------------------------------------------------+

| SigmaStudio_Version (SigmaStudio / SigmaStudio+ Version) |

+----------------------------------------------------------+

| Protocol                                                 |

+----------------------------------------------------------+

| CellName(Transceiver)                                    |

+----------------------------------------------------------+

| CellName(Peripheral)                                     |

+----------------------------------------------------------+

| SpiCmd                                                   |

+----------------------------------------------------------+

| SpiCmdWidth                                              |

+----------------------------------------------------------+
