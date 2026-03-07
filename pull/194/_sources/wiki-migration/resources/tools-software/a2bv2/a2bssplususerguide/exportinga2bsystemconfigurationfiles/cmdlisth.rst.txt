:doc:`Return to the export specifications page </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`

Command list .h Specification
=============================

Version
-------

| Details of A2B Stack and SigmaStudio version used during export is available in the Command list header file under copyright section.

.. tip::

   
   .. container:: left round

      \* @date: Thursday, 27 June 2024-17:20:07

         | \* I2C/SPI Command File Version - 1.0.0
         | \* A2B SDK DLL- 1.3.1.0
         | \* A2B Stack DLL version- 19.10.9.0
         | \* SigmaStudio version- 2.2.8879.30739
      |

   


+---+---+---+---+---+
| \*\* Field name\\A2B Software version **\|** ADI_A2B-SSPlus \_Software-Rel1.3.2 **\|** ADI_A2B_Software-Rel19.10.0 **\|** ADI_A2B_Software-Rel19.4.5 **\|** Comments **\| \|** Command list Header Schema Version **\|1.0.0|1.0.0|1.0.0|User defined version from GUI during export\| \|** A2B SDK DLL / A2B DLL **\| 1.3.1|19.10.0|19.4.5\| A2B Plugin Version \| \|** A2B Stack DLL **\| 19.10.9|19.10.0|19.4.5\| A2B Stack Version\| \|** SigmaStudio version \*\* | SigmaStudio+ v2.2.0 | SigmaStudio v4.06 | SigmaStudio v4.07 | SigmaStudio / SigmaStudio+ Version |
+---+---+---+---+---+

SPECIFICATION
-------------

Command list header file consists of the below specification

.. code:: c

   typedef struct 
    { 
   /*! Device address (size:1Byte) */
       unsigned char nDeviceAddr;

   /*! Operation code (size:1Byte) */
       unsigned char eOpCode;

   /*! SPI Command width (in bytes), For I2C it is 0 (size:1Byte) */
       unsigned char nSpiCmdWidth;

   /*! SPI Commands, For I2C it is 0 (size:4Bytes) */
       unsigned int nSpiCmd;

   /*! Reg address width (in bytes) (size:1Byte) */
       unsigned char nAddrWidth;

   /*! Reg address (size:4Bytes) */
       unsigned int nAddr;

   /*! Reg data width (in bytes) (size:1Byte) */
       unsigned char nDataWidth;

   /*! Reg data count (in bytes) (size:2Bytes) */
       unsigned short nDataCount;

   /*! Config Data - (size:4Bytes) */
       unsigned char* paConfigData;

   /*! Protocol (size:1Byte) */
       unsigned char eProtocol;

   } ADI_A2B_DISCOVERY_CONFIG;

MACROS
------

Following macros are defined for field "eOpcode"

.. code:: c

   #define WRITE   ((unsigned char) 0x00u)
   #define READ    ((unsigned char) 0x01u)
   #define DELAY   ((unsigned char) 0x02u)
   #define INVALID ((unsigned char) 0xffu)

Following macros are defined for field "eProtocol"

.. code:: c

   #define I2C     ((unsigned char) 0x00u)
   #define SPI     ((unsigned char) 0x01u)

Other Fields
------------

.. code:: c

   #define CONFIG_LEN (n) /* Specifies the "n" bytes to be written */

Following fields are not exported in A2B plugin v19.4.5 for SigmaStudio
-----------------------------------------------------------------------

+-------------------------------------------------------+
| \*\* Fields\ **\|** SigmaStudio+                      |
| (ADI_A2B-SSPlus_Software-Rel1.3.2) **\|** SigmaStudio |
| (ADI_A2B_Software-Rel19.10.0) **\|** SigmaStudio      |
| (ADI_A2B_Software-Rel19.4.5) \*\*                     |
+-------------------------------------------------------+

| nSpiCmdWidth                                          |

+-------------------------------------------------------+

| nSpiCmd                                               |

+-------------------------------------------------------+

| eProtocol                                             |

+-------------------------------------------------------+
