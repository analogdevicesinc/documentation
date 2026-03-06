:doc:`Return to parent page </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`

SigmaStudio+ Host Controller Guide
==================================

1. Introduction
===============

| SigmaStudio®+ is a development environment from Analog Devices for graphically programming ADI’s DSPs. Sigma Studio Plus includes an extensive library of algorithms to perform audio processing such as filtering, mixing, and dynamics processing, as well as basic low-level DSP functions and control blocks. The environment also extends parameter export and filter coefficient generation support for a host microcontroller. Automation scripting API support is provided to connect with many other tools in SigmaStudioPlus using APACHE thrift, which supports many languages such as Python, .NET application, Perl, Java script etc. An easy-to-use graphical interface allows users to create custom filters, compressors and other audio-shaping algorithms to improve or change the characteristics of the audio. SigmaStudio Plus Algorithm Designer is provided to convert existing Software Modules or other SHARC libraries into SigmaStudio Plus Plug-Ins. The environment is integrated with CrossCore® Embedded Studio. The production environment for a SigmaStudio Plus system is shown in below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/ssplushostcontrollerguide>`. |image1|

.. container:: centeralign

   \ **Figure 1:** Connecting SigmaStudio Plus uC Host with SHARC Target


As part of booting, the Target Application DXEs, which can initialize audio codec, set up required peripherals and communicate with the SigmaStudio Plus Host through SPI, is loaded in CCES Debug Configurations and run. After successful booting and initialization, the code corresponding to the Schematic and the parameters for the Modules are downloaded to the SHARC Target from the SigmaStudio Plus Host application through SPI. Once the code and parameters are available, the SHARC Target Application can call the API in SHARC’s Target Library to execute the received code. The code and parameters that are sent to the SHARC Target Application and the respective memory address offset can be exported from the SigmaStudio Plus development environment. The exported file can be used to program a micro-controller to send the code and parameter control information.
| This document describes how to package and send the data from the SigmaStudio Plus Host application so that it can be interpreted by the SHARC Target. Information on how to customize the data for Tuning and specific use cases is given in this document.
| ======2. SigmaStudio Plus Data Export====== The SigmaStudio Plus Host application can export the code and parameters that are to be sent to the SHARC Target once it is booted. This section describes how to export and use the system files.

2.1 Exporting System Files
--------------------------

| The export related settings can be configured through the SigmaStudio Plus Settings window. The “Settings” window can be launched by selecting **Tools -> Settings** as shown in the below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/ssplushostcontrollerguide>`.
| |image2|

.. container:: centeralign

   \ **Figure 2:** Tools -> Settings Option


| ====2.1.1 Auto Export Mode====

| Export files can be automatically generated after a successful **Link-Compile/Link-Compile-Download** by enabling ‘Auto Export System Files’ in the SigmaStudio Plus settings window.
| The files will be exported to a folder in the workspace where the particular SigmaStudioPlus schematic is saved.
| |image3|

.. container:: centeralign

   \ **Figure 3:** Auto Export option in Settings Window


| The Export Settings section mainly supports 3 types of naming conventions for the automatically exported files:
| a) **Processor Name:**
| The **Processor Name** option can be selected from **Tools -> Settings** as shown below. |image4|

.. container:: centeralign

   \ **Figure 4:** Auto Export option in Settings Window (Processor Name)


Upon Compilation, two folders with Schematic name will be generated in same workspace where the schematic is saved as shown below.



|image5|

.. container:: centeralign

   \ **Figure 5:** Auto generated export files (Processor Name)


Out of the two generated folders, the first folder with **Name of the schematic**, contains each SHARC Core DXE files of the schematic application.



|image6|

| The second folder with **Name of the schematic_Export**, contains exported source files with naming format **SigmaStudioPlus schematic name + Processor name + Core instance**. For instance, if the name of the schematic was **Example for ADSP-SC5xx Dual SH Processor Demo**, the exported files will be as shown below. |image7|

.. container:: centeralign

   \ **Figure 6:** Exported source files from SigmaStudioPlus with option **Processor Name**


| b) **Core Name:**
| The **Core Name** option can be selected from **Tools -> Settings** as shown below. |image8|

.. container:: centeralign

   \ **Figure 7:** Auto Export option in Settings Window (Core Name)


| The folder with **Name of the schematic_Export**, contains exported source files with naming format **SigmaStudioPlus schematic name + Core name + Core instance**. For instance, if the name of the schematic was **Example for ADSP-SC5xx Dual SH Core Demo**, the exported files will be as shown below. |image9|

.. container:: centeralign

   \ **Figure 8:** Exported source files from SigmaStudioPlus with option **Core Name**


c) **Schematic Name:**
| The **Schematic Name** option can be selected from **Tools -> Settings** as shown below. |image10|

.. container:: centeralign

   \ **Figure 9:** Auto Export option in Settings Window (Schematic Name)


| The folder with **Name of the schematic_Export**, contains exported source files with naming format **SigmaStudioPlus schematic name + Core instance**. For instance, if the name of the schematic was **Example for ADSP-SC5xx Dual SH Schematic Demo**, the exported files will be as shown below. |image11|

.. container:: centeralign

   \ **Figure 10:** Exported source files from SigmaStudioPlus with option **Schematic Name**


| Apart from the above mentioned use cases, user can export schematic files with two options together as per their requirement.
| Please refer the below figure to understand one such use-case. |image12|

.. container:: centeralign

   \ **Figure 11:** Exported source files from SigmaStudioPlus with multiple naming convention options


2.1.2 Exporting System files Manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The system files can be exported manually after a schematic is compiled. Once the **Link-Compile/Link-Compile-Download** action is complete, the system files can be exported by selecting **Action -> Export System Files**.
| |image13|

.. container:: centeralign

   \ **Figure 12:** Export System Files


.. note::

   The **Action -> Export System Files** menu item is inactive if the Schematic is not compiled after any modifications.


The name of system files and the folder to which it can be saved is to be decided by the user. The files contain code, parameter and version information to be sent to the SHARC Target. The files should be freshly generated every time the Schematic is modified.
| =====2.2 System File Contents and Usage===== Examples of the content of the exported files and associated descriptions are given in this section. Files that are named by the user are named “xxx” for ease of representation. The file name also contains information on the core’s instance used (indicated by ‘y’; where ‘y’ can be 0,1,2 etc. based on the number of core’s instances in the schematic) and has a text of form “\ **\_DiffDXESchematic_y**\ ”. The name can be modified by the user. For ease of representation, this is indicated by “\ **xxx_DiffDXESchematic_y**\ ” in the document.
| ====2.2.1 xxx_PrcessorSeries_y.json==== The file is of JSON format which contains all the schematic information with details about each module, compile buffers, all the meta data required by the target to execute.
| **Example Contents**
| Only part of the output XML file is shown below in the example.
| |image14|

.. container:: centeralign

   \ **Figure 13:** Contents of **xxx_PrcessorSeries_y**\


| ====2.2.2 xxx_PrcessorSeries_y_NetList==== Provides information about all the links present in the schematics and describes the source and destination of each link.
| **Example Contents**
| Only part of the output XML file is shown below in the example.
| |image15|

.. container:: centeralign

   \ **Figure 14:** Contents of **xxx_PrcessorSeries_y_NetList**\


| ====2.2.3 xxx_PrcessorSeries_y_Target==== The exported XML file contains SMAP, Reset, Version, Program Data, Parameter Data and the information required for Tuning individual Cells. This file contains the exact target level packets sent from host to target.
| **Example Contents**
| Only part of the output XML file is shown below in the example.
| |image16|

.. container:: centeralign

   \ **Figure 15:** Contents of **xxx_PrcessorSeries_y_Target**\


|

.. note::

   The *\**xxx_PrcessorSeries_y_Target.xml \*\** files contain various chunks of host packets, detailing how they should be sent due to the block buffer size limitations of the communication library.


| ====2.2.4 xxx_DiffDXESchematic_y_Defines.h==== The file contains definitions for the size of data in the system files. The macro **BufferSize_DIFFDXESCHEMATIC_y** gives the total size in bytes of SMAP, reset, version, code and parameter data packets. Related data can be found in the file DiffDXESchematic_y_TxBuffer.dat. The macro **NumTransactions_DIFFDXESCHEMATIC_y** contains the size of the data contained in DiffDXESchematic_y_NumBytes.dat. The “xxx_DiffDXESchematic_0.h” file also contains the packet data information.
| **Example Contents**
| |image17|

.. container:: centeralign

   \ **Figure 16:** Contents of **xxx_DiffDXESchematic_y_Defines.h**\


Please refer the **2.2.3 xxx_DiffDXESchematic_y.h** section for more information related to the exported Data.
| ====2.2.5 xxx_DiffDXESchematic_y.param==== This file lists all parameters used by the individual Cells, Module Name, parameter name, Parameter address, parameter offset, Parameter value and 8-bit hexadecimal representation of the parameters. The entire parameter data in 8-bit hexadecimal and corresponding binary representation is also present in the file. This Address and Offset data can be used to monitor a particular parameter’s updates during runtime.
| **Example Contents**
| |image18|

.. container:: centeralign

   \ **Figure 17:** Contents of **xxx_DiffDXESchematic_y.param**\


| ====2.2.6 xxx_DiffDXESchematic_y.h==== This file lists the IC used, size and offset address for writing code and parameters. Two files are included by this file. **SigmaStudioFW.h** must be taken from the installation folder for SigmaStudio Plus (E.g. *"C:\\Program Files\\Analog Devices\\SigmaStudioPlus"*). The *Program data* and *Param_Data* buffers declared in the file can be directly used in the Application to access program data and parameter data respectively.
| **Example Contents**
| |image19|

.. container:: centeralign

   \ **Figure 18:** Contents of **xxx_DiffDXESchematic_y.h**\


| ====2.2.7 xxx_DiffDXESchematic_y_PARAM.h==== This file gives all the details regarding parameter data for the individual Cells in the form of macros. The macros used in this header file are defined in the **SigmaStudioFW.h** file. The file also lists the parameters to be sent to the SHARC Target processor, in 32-bit hexadecimal representation of floating point or fixed point values.

.. note::

   All the macros in **SigmaStudioFW.h** are not defined and therefore the user can customize and use the header file in the Application.


**Example Contents**
| |image20|

.. container:: centeralign

   \ **Figure 19:** Contents of **xxx_DiffDXESchematic_y_PARAM.h**\


| ====2.2.8 xxx_DiffDXESchematic_y_NumBytes.dat==== The file lists the number of bytes for reset, version information, SHARC Target code and parameters respectively in the file **DiffDXESchematic_y_TxBuffer.dat**. Here, ‘y’ is the core’s instance number (0, 1, 2 etc).
| **Example Contents**
| |image21|

.. container:: centeralign

   \ **Figure 20:** Contents of **xxx_DiffDXESchematic_y_NumBytes.dat**\


| ====2.2.9 xxx_DiffDXESchematic_y_TxBuffer.dat==== The file lists all the parameters to be sent to the SHARC Target in 8-bit hexadecimal format. Note that two zeros each of 1-byte size are added before each new parameter. These two zeros are not required while sending the parameters from a Micro Controller(uC) Host to the SHARC Target. Here, ‘y’ is the core’s instance number (0, 1, 2 etc).
| **Example Contents**
| |image22|

.. container:: centeralign

   \ **Figure 21:** Contents of **xxx_DiffDXESchematic_y_TxBuffer.dat**\


| ====2.2.10 xxx_DiffDXESchematic_y_TxMetaBuffer.dat==== The format of the content can be represented as shown below:
| |image23|

.. container:: centeralign

   \ **Figure 22:** Contents of **xxx_DiffDXESchematic_yTxMetaBuffer.dat**\


The data in this file contain SMAP, Reset, Version, Program Data, Parameter Data and information required for Tuning Individual Cells. The data can be flashed or stored to a memory location and then accessed from there. The various fields in the header file are as follows:

+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| **Name**                                       | **Type**                            | **Description**                                                                                                                          |
+================================================+=====================================+==========================================================================================================================================+
| SMAP_Data_Size                                 | 4bytes, big endian unsigned integer | Signifies the size of the SMAP data                                                                                                      |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Reset_Data_Size                                | 4bytes, big endian unsigned integer | Signifies the size of the Reset data                                                                                                     |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Version_Data_Size                              | 4bytes, big endian unsigned integer | Signifies the size of the Version data                                                                                                   |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Program_Data_Size                              | 4bytes, big endian unsigned integer | Signifies the size of the Program data                                                                                                   |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter_Data_Size                            | 4bytes, big endian unsigned integer | Signifies the size of the Parameter data                                                                                                 |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter_MetaData_Size                        | 4bytes, big endian unsigned integer | Signifies the size of the Parameter meta data                                                                                            |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| SMAP_Data                                      | Byte array, big endian hexadecimal  | Data for SMAP information. Note that first two bytes need not be sent to SHARC Target                                                    |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Reset_Data                                     | Byte array, big endian hexadecimal  | Data for Reset information. Note that first two bytes need not be sent to SHARC Target                                                   |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Version_Data                                   | Byte array, big endian hexadecimal  | Data for Version information. Note that first two bytes need not be sent to SHARC Target                                                 |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Program_Data                                   | Byte array, big endian hexadecimal  | Data for Program information. Note that first two bytes need not be sent to SHARC Target                                                 |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter_Data                                 | Byte array, big endian hexadecimal  | Data for Parameter information. Note that first two bytes need not be sent to SHARC Target                                               |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Name_AlgoNo_String_LengthN (where N = 1,2 etc) | 2bytes, big endian unsigned integer | Number of bytes for string with Cell name and Algorithm number of "Nth" tuneable block in Schematic                                      |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Name_AlgoNo_StringN (where N = 1,2 etc)        | Character array                     | Character string without null containing the Cell name and Algorithm number of "Nth" tuneable block in Schematic                         |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter_Base_AddressN (where N = 1,2 etc)    | 4bytes, big endian unsigned integer | Offset address of the starting parameter of "Nth" tuneable block in the Schematic specified by the Cell name and Algorithm number string |
+------------------------------------------------+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

| Here, ‘y’ is the core’s instance number (0,1,2 etc).
| **Example Contents**
| |image24|

.. container:: centeralign

   \ **Figure 23:** SHARC0 related TxMetaBuffer data


| |image25|

.. container:: centeralign

   \ **Figure 24:** SHARC1 related TxMetaBuffer data


| ====2.2.11 ADSPSC5xx.xml/ADSP215xx.xml==== The exported XML file contains SMAP (only in case of ADSP-SC5xx/ADSP-215xx/ADSP-214xx), Reset, Version, Program Data, Parameter Data and the information required for Tuning individual Cells. The information can be parsed using an xml parser. The XML file also includes the GUI parameter information of the Modules in the Schematic.
| The schema of the XML is illustrated below: |image26|

.. container:: centeralign

   \ **Figure 25:** XML Export File Schema Specification


+------------+---------------------------------------------------------------------------------------------------------------+
| IC         | Name of the Processor (ICs/DSPs) in the schematic. There can be more than one IC for a multiple SSn Schematic |
+============+===============================================================================================================+
| Name       | Name of the SSn (sub Schematics). Same as the Name of the IC. Default IC name is “IC 1”                       |
+------------+---------------------------------------------------------------------------------------------------------------+
| PartNumber | Name of the exact target processor used (Eg: ADSP-SC594 etc)                                                  |
+------------+---------------------------------------------------------------------------------------------------------------+

====== ===========================================================
Core   Name of the SHARC core
====== ===========================================================
Name   Name of the SHARC Core as per the schematic
CoreID Exact Core number like 0 or 1 representing SHARC0 or SHARC1
====== ===========================================================

+-----------+------------------------------------------------------------------------------------------+
| Schematic | DXE based schematic name as per core                                                     |
+===========+==========================================================================================+
| Name      | DXE based schematic name as per each individual core (Eg: DiffDXESchematic_0 for SHARC0) |
+-----------+------------------------------------------------------------------------------------------+

+----------+------------------------------------------------------------------------------------+
| Meta     | Meta information can be any value from { Reset, Version Info, SchematicVersionTag} |
+==========+====================================================================================+
| Name     | Name of the Meta information                                                       |
+----------+------------------------------------------------------------------------------------+
| AddrIncr | Byte-wise Address Increment                                                        |
+----------+------------------------------------------------------------------------------------+
| Size     | Size in Bytes                                                                      |
+----------+------------------------------------------------------------------------------------+
| Data     | Data in Hexadecimal (Most significant byte comes first)                            |
+----------+------------------------------------------------------------------------------------+

+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Program  | Program Memory                                                                                                                                                                                |
+==========+===============================================================================================================================================================================================+
| Name     | Name of the Program memory. This string can be from {Program Data, Program DataB}                                                                                                             |
+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Address  | Address offset to which the program has to be loaded. The start address is always the memory pointer pointed by Block 1/Block7 in ADI_SS_MEM_MAP respectively for Program Data/ Program DataB |
+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AddrIncr | Byte-wise Address Increment                                                                                                                                                                   |
+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Size     | Size in Bytes (2 bytes less than the size reported in export file)                                                                                                                            |
+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Data     | Data in Hexadecimal (Most significant byte comes first)                                                                                                                                       |
+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter | Parameter Memory                                                                                                                                                       |
+===========+========================================================================================================================================================================+
| Name      | Name of the Parameter memory. This string can be from {Parameter Data}                                                                                                 |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Address   | Address offset to which the initial parameter has to be loaded. The start address is always the memory pointer pointed by Block 5 in ADI_SS_MEM_MAP. This is always 0. |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AddrIncr  | Byte-wise Address Increment                                                                                                                                            |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Size      | Size in Bytes (2 bytes less than the size reported in export file)                                                                                                     |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Data      | Data in Hexadecimal (Most significant byte comes first)                                                                                                                |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+--------+------------------------------------------------------------------------------------------------+
| Module | Details of individual Cells (A Cell is the basic graphical entity with one or more Algorithms) |
+========+================================================================================================+
| Name   | Name of the Module                                                                             |
+--------+------------------------------------------------------------------------------------------------+

+--------------+----------------------------------------------------------------------------------------------------------------------------+
| Algorithm    | Details of individual Algorithm (An Algorithm is the basic processing entity with one or more Parameters associated to it) |
+==============+============================================================================================================================+
| AlgoName     | Index of the Algorithm within the Cell. There can be multiple Algorithms within a Cell                                     |
+--------------+----------------------------------------------------------------------------------------------------------------------------+
| DetailedName | Mentions detailed information of algorithm used like version, to which plugin it belongs to etc                            |
+--------------+----------------------------------------------------------------------------------------------------------------------------+
| Description  | Algorithm Description with Names of Algorithm and the GUI parameters                                                       |
+--------------+----------------------------------------------------------------------------------------------------------------------------+
| Address      | Algorithm Starting address (offset from the beginning of the parameter memory)                                             |
+--------------+----------------------------------------------------------------------------------------------------------------------------+

+--------------------+--------------------------------------------------------------+
| Abstract parameter | Brief Description of the Parameter                           |
+====================+==============================================================+
| Name               | Name of Parameter                                            |
+--------------------+--------------------------------------------------------------+
| Type               | Name of the exact target processor used (Eg: ADSP-SC594 etc) |
+--------------------+--------------------------------------------------------------+
| Value              | Value of the data element                                    |
+--------------------+--------------------------------------------------------------+

+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ModuleParameter | Details of the individual parameter (Parameter is the basic Tuning entity with one or more data units)                                                                                                                                                                                                                                                                                                                 |
+=================+========================================================================================================================================================================================================================================================================================================================================================================================================================+
| Name            | Name of the parameter                                                                                                                                                                                                                                                                                                                                                                                                  |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type            | Type of the parameter. Type can be {Int32, Float32, Hex}                                                                                                                                                                                                                                                                                                                                                               |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Offset          | Offset from the Algorithm starting address                                                                                                                                                                                                                                                                                                                                                                             |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DataType        | Data type of the parameter {Eg: Single Precision Float etc}                                                                                                                                                                                                                                                                                                                                                            |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Value           | Value of the data element. Note: This is applicable only if the Parameter has a single data unit. In case of multiple data units, only the hexadecimal values are provided. |image28| In the above example, the first parameter ‘Taps’ is a single data unit with a “Value” equal to 5. Whereas, the second parameter ‘FIRFiltBlock1coeff’ has multiple data units and therefore, only hexadecimal values are provided |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Size            | Size in Bytes                                                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Data            | Data in Hexadecimal (Most significant byte comes first)                                                                                                                                                                                                                                                                                                                                                                |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| **Example Contents**
| Only part of the output XML file is shown below in the example.
| |image29|

.. container:: centeralign

   \ **Figure 26:** SHARC0 related schematic information in XML file


| |image30|

.. container:: centeralign

   \ **Figure 27:** SHARC1 related schematic information in XML file


| ======3. Packetizing Data====== The data received while exporting the code and parameters has to be packetized properly before sending it to the SHARC Target board.
| =====3.1 Communication Protocol===== All the communication between the SigmaStudio Plus Host PC/Micro Controller uC Host and the SHARC Target use the following protocol:
| |image31|

.. container:: centeralign

   \ **Figure 28:** Communication Protocol


Each packet contains a begin command, size of the packet, payload data, CRC value, SHARC Target memory type and an end command. The individual contents of the packet are listed below.
| ====3.1.1 SS_CMD_BEGIN: (32-bit word)==== This field indicates beginning of the packet. Refer to Table 2 for 32-bit hexadecimal value of this field. Bits 12-15 of “SS_CMD_BEGIN” is used for indicating the “Core Id” and “Instance Id” in SigmaStudio Plus (ADSP-SC5xx). The details of those bit fields are described in :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/ssplushostcontrollerguide>`. |image32|

.. container:: centeralign

   \ **Figure 29:** Core ID and Instance ID in SS_CMD_BEGIN


| The bit fields 15-14 (Y) is used to indicate the Core ID i.e., 00 – ARM Core0 (not used for Host communication), 01 – SHARC Core1 and 10 – SHARC Core2.
| The bit fields 13-12 (X) is used to indicate the Instance ID. For a single instance schematic, this fields shall be always 00.
| |image33|
| ====3.1.2 CMD: (32-bit word)==== The CMD field indicates the nature of payload in the packet. The value of this field can vary from packet to packet. Refer to Table 2 for possible 32-bit hexadecimal values of this field.
| ====3.1.3 Payload==== This contains the data to be transferred from the SigmaStudio Plus Host to the SHARC Target. The contents of payload are given below.
| ====3.1.4 PL_LEN: (32-bit word)==== This field indicates the total length of the payload, including CRC. The maximum payload length should be 1024 words (4096 Bytes) or less.
| ===3.1.4.1 PAYLOAD_DATA:=== Actual payload in the packet appears in this portion. The payload can be data/code/parameter.
| ===3.1.4.2 CRC: (32-bit word)=== The CRC field is used for protection. The current version uses simple checksum. The code used to compute CRC data is given below. Here **pData[ ]** is the buffer of type **unsigned int**.
| |image34|
| The SHARC Target can compute the CRC of the received packet either only on the payload or on the entire packet based on the configuration parameter. The above example shows CRC checksum computed only on the payload. Alternatively, the CRC checksum can also be computed on the entire packet.
| ===3.1.4.3 MEM_ADDR: (32-bit word)=== This field indicates the memory address to which the code/parameter should be loaded. This field is used only when the command is either **SS_CMD_BLOCK_SAFE** or **SS_CMD_PARAMETER_NO_SAFE**.
| ====3.1.5 SS_CMD_END: (32-bit word)==== This 32-bit word indicates the end of a communication packet. Refer to Table 2 for 32-bit hexadecimal value of the field.
| ====3.1.6 Capturing Packet Information using SigmaStudioPlus Capture Window==== Enable the Capture Window using View -> Capture Window option as shown below,
| |image35|

.. container:: centeralign

   \ **Figure 30:** SigmaStudioPlus Capture Window Selection


The capture window opens and there the user is provided with an option to select the type of Display they want to see during data transfer from SigmaStudioPlus. Please refer Figure: Packet Capture.
| |image36|

.. container:: centeralign

   \ **Figure 31:** Packet Capture


Option ‘RAW’ will only display the exact data content that is being passed from SigmaStudioPlus while the ‘Final’ option will display the entire packet data that was transferred.
| |image37|

.. container:: centeralign

   \ **Figure 32:** Complete Packet capture from SigmaStudioPlus capture window for SHARC-0


| |image38|

.. container:: centeralign

   \ **Figure 33:** Complete Packet capture from SigmaStudioPlus capture window for SHARC-1


| =====3.2 Commands for Communication===== All the commands and fields indicating begin/end with their 32-bit hexadecimal values are listed in Table 2.

+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| **Command**              | **Description**                                                                                                                                                                           | **Value**  | **Payload**                                                     |
+==========================+===========================================================================================================================================================================================+============+=================================================================+
| SS_CMD_BEGIN             | Signifies the beginning of packet                                                                                                                                                         | 0xF4190BE6 | None                                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_PROGRAM_SSN       | Indicates that the packet contains code                                                                                                                                                   | 0xFAAD0552 | SigmaStudio Plus generated code                                 |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_PARAMETER_SAFE    | Indicates that the packet contains safe-load parameters                                                                                                                                   | 0xA5015AFE | Up to 5 sets of safe-load parameters and respective addresses   |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_PARAMETER_NO_SAFE | Indicates that the packet contains a block of parameters that can be directly loaded on to the parameter memory. Used for initial parameter set and block parameter update during Tuning. | 0xFFA1F05E | Block of parameters                                             |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_BLOCK_SAFE        | Indicates that the packet contains a block of parameters to be safe-loaded. Used for block parameter update during Tuning.                                                                | 0x4EA5B15A | Block parameters                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD1              | Predefined command 1. Used for sending Reset.                                                                                                                                             | 0xF3F20C0D | Word and Block DMA receive mode flag                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD2              | Predefined command 2. Used for sending version information.                                                                                                                               | 0xF3E20C1D | Version information                                             |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD3              | Predefined command 3. Used for sending read request.                                                                                                                                      | 0xF3D20C2D | Read request                                                    |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD4              | Predefined command 4 that calls a call-back function with the payload as arguments.                                                                                                       | 0xF3C20C3D | User defined data that is interpreted by the call-back function |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD5              | Payload containing custom command that can be obtained by calling adi_ss_comm_GetProperties() function                                                                                    | 0xF3B20C4D | User defined command                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD6              | Predefined command 6. Used for sending Schematic bypass flag.                                                                                                                             | 0xF3A20C5D | Bypass flag                                                     |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD7              | Indicates that the packet contains SMAP data. This is applicable or used only when the IC is ADSP-SC5xx.                                                                                  | 0xF3920C6D | SMAP                                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_PARTIAL_END       | Partial end of current packet                                                                                                                                                             | 0xE1D21E2D | None                                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_END               | End of current packet                                                                                                                                                                     | 0xF1D20E2D | None                                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+

|

.. container:: centeralign

   \ **Table 2:** Communication Commands


| =====3.3 Read Request Payload===== PAYLOAD_DATA inside read request packets are of length 3 or 4 words depending on the read request type and is described below.
| |image39|

.. container:: centeralign

   \ **Figure 34:** Read Request Payload


| ====3.3.1 NUMBER_OF_REQUESTS: (32-bit word)==== The field indicates the number of read requests in the current read request packet. This should always be set to 1.
| ====3.3.2 READBACK_TYPE: (32-bit word)==== The field indicates the type of read request. Refer to the table below for more details.
| ^ **Command** ^ **Description** ^ **Value** ^

+-------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_MIPS_VALUE    | Indicates read request for MIPS                                                                                                 | 0x00CE6319U |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_DC_MIPS_VALUE | Indicates read request for Dual-Core MIPS                                                                                       | 0x00DC6239U |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_VERSION_INFO  | Indicates read request for Version                                                                                              | 0x003EDC12U |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_READ_VALUE    | Indicates read request from Parameter memory, Read back, Level Detector etc. Modules use this command to read value from memory | 0x00BC543AU |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_ERROR_CODE    | Indicates read request for code download status                                                                                 | 0x00F7E808U |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_ACKNOWLEDGE   | Indicates acknowledgement for successful read                                                                                   | 0x00000000  |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------+

|

.. container:: centeralign

   \ **Table 3:** Read-back Type


| ====3.3.3 NUMBER_OF_WORDS: (32-bit word)==== This field indicates the number of values to be read from the SHARC Target. This field is valid only when the read type is SS_CMD_BK_READ_VALUE. This field should be 0 for other read types. For memory read, the first 2 nibbles of the NUMBER_OF_WORDS field corresponding to read request payload must always be 0x30. Also, the last nibble must always be 0x0C. For parameter read, the first 2 nibbles of the NUMBER_OF_WORDS field corresponding to read request payload must be 0x00. The last 24-bits (remaining 6 nibbles) of the ‘NUMBER_OF_WORDS’ field indicate the number of words to be read from the parameter offset specified as part of the ‘ADDRESS’ field of the read request payload. The maximum number of words that can be requested to be read in a single read request is seven.
| ====3.3.4 ADDRESS: (32-bit word)==== This field indicates the offset, from the start of parameter memory to the memory location from where the value has to be read. This field is included in the payload only when the read type is SS_CMD_BK_READ_VALUE. Therefore, the payload size is 3 for other read types.
| ======4. Payload Types======

4.1 Code
--------

| ‘Code’ refers to the compiled binary code of the entire Schematic. SS_CMD_PROGRAM_SSN command indicates that the packet contains code payload. MEM_ADDR field is not used.
| |image40|

.. container:: centeralign

   \ **Figure 35:** SS_CMD_PROGRAM_SSN command packet capture


4.2 Initial Parameter
---------------------

| ‘Initial Parameter’ refers to the entire parameter set of the Schematic. SS_CMD_PARAMETER_NO_SAFE command indicates that the packet contains complete block parameter payload. MEM_ADDR field is not used.
| =====4.3 Block Parameter===== ‘Block Parameter’ refers to a block of parameters sent to the SHARC Target as part of Tuning the Schematic. The SS_CMD_PARAMETER_NO_SAFE command indicates that the packet contains block parameter payload. The MEM_ADDR field indicates the offset of the block from the start of the parameter buffer. When the block parameter is received on the SHARC Target, it is immediately copied to the parameter buffer.
| |image41|

.. container:: centeralign

   \ **Figure 36:** SS_CMD_PARAMETER_NO_SAFE command packet capture


| =====4.4 Safeload Parameter===== ‘Safeload Parameter’ refers to payload of up to 5 sets of parameter and address combination sent to the SHARC Target as part of Tuning the Schematic. The SS_CMD_PARAMETER_SAFE command indicates that the packet contains safeload parameter payload. MEM_ADDR field is not used. When safeload parameters are received on the SHARC Target, it is not immediately copied to the parameter buffer. Parameters are updated just before the execution of the Schematic code. This ensures that the parameter updates are not performed during the execution of the Algorithm.
| |image42|

.. container:: centeralign

   \ **Figure 37:** SS_CMD_PARAMETER_SAFE command packet capture


| =====4.5 Block Safeload Parameter===== ‘Block Safeload Parameter’ refers to a block of parameters sent to the SHARC Target as part of Tuning the Schematic. SS_CMD_BLOCK_SAFE command indicates that the packet contains block safeload parameter payload. MEM_ADDR field indicates the offset of the block from the start of the parameter buffer. When block safeload parameter is received on the SHARC Target, it is not immediately copied to the parameter buffer. Parameters are updated only after ensuring that the SigmaStudio Plus Schematic code is not being executed. If the code is being executed, the update waits until the code execution completes.
| |image43|

.. container:: centeralign

   \ **Figure 38:** SS_CMD_BLOCK_SAFE command packet capture


| ======5. Using Exported Data======

5.1 Deriving Payload Contents
-----------------------------

| The exported files **DiffDXESchematic_y_NumBytes.dat** and **DiffDXESchematic_y_TxBuffer.dat** need to be modified before directly including in the Application. A variable can be declared in such a manner that it contains all values in DiffDXESchematic_y_TxBuffer.dat. Thus, the content of DiffDXESchematic_y_TxBuffer.dat can be modified as given below.
| |image44|

.. container:: centeralign

   \ **Figure 39:** Declaring a variable which contains the contents of **DiffDXESchematic_y_TxBuffer.dat**\


| Similarly a variable of data type int can be used to modify **DiffDXESchematic_y_NumBytes.dat**. After the modifications are done, the files can be directly included in the Application source code.
| The “.h” files generated during export can be directly included in the Application. In addition, these header files include SigmaStudioFW.h. This has to be taken from the installation folder for SigmaStudio Plus (E.g. “\ **C:\\Analog Devices\\SigmaStudioPlus-Rel2.x.x**\ ”).
| Note that every parameter in **DiffDXESchematic_y_TxBuffer.dat** has two preceding bytes with zero value. These are not part of the parameter value and should be skipped before using data for communication. In addition, the file xxx_DiffDXESchematic_y.h contains code, reset version etc. in header file format. Alternately, the file “\ **DiffDXESchematic_y_TxMetaBuffer.dat**\ ” can be used to derive the start address of the parameter required by the SigmaStudio Plus Host for tuning the parameter based on its name. The parameter name can be obtained from the file “\ **DiffDXESchematic_y_TxMetaBuffer.dat**\ ”. The parameter name is a combination of “Name” and “Algorithm Index” which are present in the file “xxx.params”. The parameter name is nothing but “Name” + “\_” + “Algorithm Index” capitalized.
| ====5.1.1 SMAP==== Command: SS_CMD_CMD7
| This is applicable only when the IC used is ADSP-214xx/ADSP-SC5xx.
| The entire set of SMAP data is present in the file xxx_DiffDXESchematic_y.h in hexadecimal unsigned char format under the variable name SMAP_Data[]. The size of the SMAP structure can be taken from the macro SMAP_SIZE. Note that there are no dummy bytes when the data is taken from this header file.
| Alternatively, the parameter data can be taken from \_DiffDXESchematic_Y_TxBuffer.dat using the offset and size from DiffDXESchematic_y_NumBytes.dat file. Care should be taken to skip the initial two bytes in this case.
| |image45|

.. container:: centeralign

   \ **Figure 40:** SS_CMD_CMD7 command packet capture


| ====5.1.2 Reset==== Command: SS_CMD_CMD1
| The reset parameter consists of a 32-bit hexadecimal word with value 0 or 1. Sending this parameter with the associated command to the SHARC Target prepares the SHARC Target to receive new SSn code and parameter data. When the parameter is 0, the SHARC Target receives the data sent by SPI as single words and processes it. On sending a value of 1, the SHARC Target receives code and parameter as a block and processes the CRC check on the next call of *adi_ss_schematic_process()* function.
| |image46|

.. container:: centeralign

   \ **Figure 41:** SS_CMD_CMD1 command packet capture


| ====5.1.3 Version Information==== Command: SS_CMD_CMD2
| The version information is also a 32-bit hexadecimal value whose first 2 bytes give the version of the process API used in the Application. The version of the process API used in the Application for this release is latest 2.x.x. This data is present in \_DiffDXESchematic_Y_TxBuffer.dat with the most significant byte coming first. The offset to access the version information and its size can be obtained from the DiffDXESchematic_y_NumBytes.dat file. Although the size of the version information is given as 6 bytes, the first two bytes are dummy values and must be omitted to obtain the real version information value.
| |image47|

.. container:: centeralign

   \ **Figure 42:** SS_CMD_CMD2 command packet capture


| ====5.1.4 Read Command==== Command: SS_CMD_CMD3
| The "Read Request" command is utilized in data communication to signal a host's intent to retrieve specific parameters or data from a target device. When issued, this command prompts the target to provide the requested information, enabling the host to access essential data. This command has been captured in upcoming section A. Read-Back Communication, where the complete packet for read operation is described.
| ====5.1.5 Schematic Bypass Command==== Command: SS_CMD_CMD6
| The schematic bypass command SS_CMD_CMD6 consists of a 32-bit hexadecimal value that can be sent from the host to the target processor to inform the target whether further data processing needs to be carried out by bypassing the designed audio processing schematic.
| |image48|

.. container:: centeralign

   \ **Figure 43:** SS_CMD_CMD6 command packet capture


| ====5.1.6 Partial End Command==== Command: SS_CMD_PARTIAL_END
| The SS_CMD_PARTIAL_END command is used in data transmission to indicate the conclusion of a segment of a larger packet when the overall packet size exceeds transmission limits. This command signals that the current section has been completed, allowing the remaining data to be sent in subsequent packets. By utilizing this command, systems can efficiently manage large data transfers, ensuring that information is divided into manageable sections while maintaining the integrity of the overall transmission.
| |image49|

.. container:: centeralign

   \ **Figure 44:** SS_CMD_PARTIAL_END command packet capture


| ====5.1.7 Schematic Code==== Command: SS_CMD_PROGRAM_SSN
| The code for Schematic is present in \_DiffDXESchematic_Y_TxBuffer.dat as the third parameter. Its size and offset to access it can be obtained from \_DiffDXESchematic_Y_NumBytes.dat file. The Schematic code also has 2 dummy bytes in the beginning, and these have to be skipped to access the code. The size of the code varies for each Schematic and should be updated when a Schematic is modified. The data present is such that the most significant byte comes first.
| |image50|

.. container:: centeralign

   \ **Figure 45:** SS_CMD_PROGRAM_SSN command packet capture


| ====5.1.8 Parameters==== Command: SS_CMD_PARAMETER_NO_SAFE / SS_CMD_PARAMETER_SAFE / SS_CMD_BLOCK_SAFE
| The entire set of parameters is present in the file xxx_DiffDXESchematic_y.h in hexadecimal unsigned char format under the variable name Param_Data[]. The size of the parameter table can be taken from the macro PARAM_SIZE. Note that there are no dummy bytes when the data is taken from this header file.
| Alternatively the parameter data can be taken from \_DiffDXESchematic_Y_TxBuffer.dat using the offset and size from DiffDXESchematic_y_NumBytes.dat file. Care should be taken to skip the initial two bytes in this case.
| The default command used during SigmaStudioPlus schematic download or parameter update is SS_CMD_PARAMETER_NO_SAFE command. SS_CMD_PARAMETER_SAFE command is used mainly with Filters or modules that requires multiple parameter (upto 5) updates at the same time without affecting the current processing cycle.
| SS_CMD_PARAMETER_SAFE
| |image51|

.. container:: centeralign

   \ **Figure 46:** SS_CMD_PARAMETER_SAFE command packet capture


SS_CMD_PARAMETER_NO_SAFE
| |image52|

.. container:: centeralign

   \ **Figure 47:** SS_CMD_PARAMETER_NO_SAFE command packet capture


SS_CMD_BLOCK_SAFE
| |image53|

.. container:: centeralign

   \ **Figure 48:** SS_CMD_BLOCK_SAFE command packet capture


| =====5.2 Sending Schematic Code===== The Schematic code must be sent to the SHARC Target when a new Schematic is generated, or an existing Schematic is modified. In order to send the Schematic code to the SHARC Target, the following steps have to be executed.
| 1. Send SMAP for the schematic (applicable for ADSP-214xx/215xx/SC5xx). This reserves the necessary memory blocks in the Target.
| 2. Send Reset parameter: This prepares the SHARC Target for receiving the code.
| 3. Send Version Information: This ensures compliance between the SHARC Target and the SigmaStudio Plus Host.
| 4. Send Schematic Code: Algorithm code for the SHARC Target.
| 5. Send Parameters: Parameters for the code to work with.
| Once the entire data is sent to the SHARC Target running SigmaStudio Plus, the SHARC Target can start processing the data.

.. note::

   There should be some delay required between SMAP, Code and Parameter data when sending data from Microcontroller host. The SigmaStudio Plus host use 100 msec between SMAP, Code and Parameter data which is required for target framework initializations.


5.3 Parameter Reloading
-----------------------

| If the Schematic code and parameters are sent to the SHARC Target, then the block of parameters for the particular Schematic alone can be updated. A step-by-step procedure is given below.
| 1. Send Reset parameter: This prepares the SHARC Target for receiving the code.
| 2. Send Version Information: This ensures compliance between the SHARC Target and the SigmaStudio Plus Host.
| 3. Send Parameters: Parameters for the code to work with.
| Once the entire data is sent to the SHARC Target running SigmaStudio Plus, the SHARC Target can start processing the data.

.. note::

   The reload parameters should update before calling the schematic processing.


5.4 Sending Parameter for Tuning
--------------------------------

| To send a parameter for Tuning, both the parameter and its address offset need to be sent to the SHARC Target. The parameter data sent should be the 32-bit hexadecimal equivalent of floating point or fixed point value, followed by the offset address location of the parameter.
| Every single value to be written to the parameter memory during Tuning should be succeeded by the address location to which it is to be written. The values should then be packetized and sent to the SHARC Target. Hence the data to be packetized is of the form:
| 1. Parameter value in 32-bit hexadecimal
| 2. Offset address location in 32-bit hexadecimal.
| Please refer the Parameters [PARAM_SAFE, PARAM_NO_SAFE etc commands] for a better understanding of how the offset address location and parameter values are placed in the packet.
| ====5.4.1 Flashing Data and Accessing it for Tuning==== The file DiffDXESchematic_y_TxMetaBuffer.dat has a tune table which contains parameter data, its address and a string to uniquely identify the Algorithm. The file can be directly flashed to the memory of a micro-controller and can be directly accessed from there. This approach has the advantage that once the Schematic is frozen and only the Tuning has to be performed, a Tuning engineer can do so without modifying the micro-controller code.
| ====5.4.2 Using Header Files==== The parameter data and its offset location can be found as a macro in the file xxx_DiffDXESchematic_y_PARAM.h. The file xxx_DiffDXESchematic_y.h contains a parameter data buffer named \_DIFFDXESCHEMATIC_y_Data[] and a macro defining the size of the parameter data termed PARAM_SIZE. Since the data in the buffer \_DIFFDXESCHEMATIC_y_Data[] is given in bytes, the offset address can be multiplied with 4 to derive the address of the parameter data. An example use case is given below.
| Let the offset address of the Mute Algorithm in a Schematic be given by the macro MOD_MUTE_1_MUTE_ADDR, the value of parameter can be derived as
| |image54|

.. container:: centeralign

   \ **Figure 49:** Mute module used as an example to show how to derive parameter value


| ======6. Parameter Address Calculation======

6.1 IIR Filters
---------------

| Coefficient arrangement in SHARC memory of IIR fitters is different for Type 1 and Type 2 filters.
| Type1 Cascaded 3 stage filter:
| |image55|

.. container:: centeralign

   \ **Equation 1:** Type 1 Cascaded 3 Stage IIR Filter


| Type 1 Filter, nth stage (where n is 1, 2 or 3 for 3 stage cascaded filter)
| b2 -> GenSecondOrder_1 (Stage0_B2) -> c[n-1][0]
| b1 -> GenSecondOrder_1 (Stage0_B1) -> c[n-1][1]
| b0 -> GenSecondOrder_1 (Stage0_B0) -> c[n-1][2]
| a2 -> GenSecondOrder_1 (Stage0_A2) -> c[n-1][3]
| a1 -> GenSecondOrder_1 (Stage0_A1) -> c[n-1][4]
| Type2 Cascaded 3 stage filter:
| |image56|

.. container:: centeralign

   \ **Equation 2:** Type 2 Cascaded 3 Stage IIR Filter


| Type 2 Filter, nth stage (where n is 1, 2 or 3 for 3 stage cascaded filter)
| b’0 -> GenSecondOrder_0 (Stage0_B0) -> c[4*number of stages]
| b’1 -> GenSecondOrder_0 (Stage0_B1) -> c[n-1][3]
| b’2 -> GenSecondOrder_0 (Stage0_B2) -> c[n-1][2]
| a’1 -> GenSecondOrder_0 (Stage0_A1) -> c[n-1][1]
| a’2 -> GenSecondOrder_0 (Stage0_A2) -> c[n-1][0]
| For Type2 IIR, b0 coefficient is same for all the stages. The offset values for b0 is the same for all the stages.
| ^ **Implementation** ^ **0B** ^ **1B** ^ **2B** ^ **1A** ^ **2A** ^

+--------+--------------------------------------+-------------+-------------+----------+----------+
| Type 1 | b0                                   | b1          | b2          | -a1      | -a2      |
+--------+--------------------------------------+-------------+-------------+----------+----------+
| Type 2 | Product of b0 of all cascaded stages | b1’ = b1/b0 | b2’ = b2/b0 | a1’ = a1 | a2’ = a2 |
+--------+--------------------------------------+-------------+-------------+----------+----------+

|

.. container:: centeralign

   \ **Table 4:** Filter Coefficient Computation


| Parameter arrangement of Type1 cascaded filters in memory
| |image57|
| Parameter arrangement of Type2 cascaded filters in memory |image58|

.. container:: centeralign

   \ **Figure 50:** Parameter Arrangements


   |image59|

.. container:: centeralign

   \ **Figure 51:** Export Example Schematic


   |image60|

.. container:: centeralign

   \ **Figure 52:** Export Example Capture Window


7 Sending Custom Commands
=========================

| Custom commands can be sent from the SigmaStudio Plus Host to the SHARC Target in 2 different ways; using SS_CMD_CMD4 and SS_CMD_CMD5.
| =====7.1 Call-back Method===== A packet sent to the SHARC Target with SS_CMD_CMD4 as the command executes a call-back function with the payload information as the function arguments. The call-back function to be executed can be assigned through the configuration parameter pfCommCallBack in the communication configuration structure ADI_SS_COMM_CONFIG passed to adi_ss_comm_init().
| |image61|

.. container:: centeralign

   \ **Figure 53:** Configuring callback function of CMD4 command and function prototype


**Parameters**

=========== ======================
Name        pCommPayloadBuff
Type        Int \*
Direction   Input
Description Payload buffer pointer
=========== ======================

=========== ===================
Name        nPayloadCount
Type        Int
Direction   Input
Description Size of the payload
=========== ===================

+-------------+---------------------------------------------------------------------------+
| Name        | hSSn                                                                      |
+-------------+---------------------------------------------------------------------------+
| Type        | adi_ss_sample_t \*                                                        |
+-------------+---------------------------------------------------------------------------+
| Direction   | Input                                                                     |
+-------------+---------------------------------------------------------------------------+
| Description | Handle to the SigmaStudio Plus module instance which received the command |
+-------------+---------------------------------------------------------------------------+

7.2 Get Properties Method
-------------------------

| For the purpose of discussion, let's assume a generic use case where SS_CMD_CMD5 is used by the host to read the LED status of the target board. The Read request and response are shown in the figure below.
| |image62|

.. container:: centeralign

   \ **Figure 54:** SS_CMD_CMD5 LED status Read Request and Complete Response Packet


A packet sent to the SHARC Target with SS_CMD_CMD5 as the command is received by the SigmaStudio Plus instance on the SHARC Target. The received data/command is extracted by the Application from the SigmaStudio Plus instance using the adi_ss_comm_GetProperties() function. Data is available in oGetProperties.pSSnBuf, where oGetProperties is the properties structure of type ADI_SS_COMM_PROPERTIES passed to adi_ss_comm_GetProperties().
| |image63|

.. container:: centeralign

   \ **Figure 55:** Function adi_ss_comm_GetProperties() that handles data received through CMD5


.. note::

   This is just an example showing the packet format and data transfer of CMD5 command. It is up to the developer to implement their required logic inside adi_ss_comm_GetProperties()


Please refer Section **8.1 Back Channel Protocol (SHARC Target to SigmaStudio Plus Host)** to have better understanding of the format.
| =====7.3 Custom Command Example=====

7.3.1 Reset Communication Instance from SigmaStudio Plus Host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The custom command SS_CMD_CMD4 can be used to reset the communication instance from an error state. This is required to continue processing after encountering a communication error. The below code snippet shows how to trigger a communication reset from the SigmaStudio Plus Host with the help of a call-back function.
| |image64|

.. container:: centeralign

   \ **Figure 56:** SS_CMD_CMD4 Reset Communication Instance Request


   |image65|

.. container:: centeralign

   \ **Figure 57:** Contents of callback function app_ss_comm_callback_cmd4 () for CMD4 command


The default example demo application provided with the SigmaStudioPlus installer package already includes logic implemented in the app_ss_comm_callback_cmd4() function as a use case for CMD4, which reads the LED status of the ADI EVAL board.
| Please refer to the figure below: "CMD4 LED Status Read Request and Complete Response Packet" for a better understanding.
| |image66|

.. container:: centeralign

   \ **Figure 58:** SS_CMD_CMD4 LED status Read Request and Complete Response Packet


Please refer Section **8.1 Back Channel Protocol (SHARC Target to SigmaStudio Plus Host)** to have better understanding of the format.
| ======8. Read-Back Communication====== The source code to packetize and send the read-back information is available with the released Application. Refer to the files backchannel.c and backchannel.h for source code and further details (ADSP-214xx processor series).
| =====8.1 Back Channel Protocol (SHARC Target to SigmaStudio Plus Host)===== All communications from the SHARC Target to the SigmaStudio Plus Host PC application use a byte based protocol as shown below.
| |image67|

.. container:: centeralign

   \ **Figure 59:** Back Channel Communication SPI Packet Format


The lower 4 bits of each word enumerate each word. The words in the packet are enumerated in ascending order. The figure given above is used as a reference for listing individual content of packet.
| ====8.1.1 BEGIN: (32-bit)==== The BEGIN word of size 32-bit indicates the beginning of packet. This contains a BEGIN_CMD command, the size of sub packets in bytes, format of sub packet and word number.
| ===8.1.1.1 BEGIN_CMD: (16-bit)=== This 16-bit word indicates the beginning of a communication packet.
| ===8.1.1.2 SIZE: (8-bit)=== This indicates the total length of data in payload in bytes.
| ===8.1.1.3 FORMAT: (4-bit)=== This field designates the format of the packet contents. The packet contents can be in 8-bit format or 24-bit format. When the content of the packet is in 8-bit format, the MSB of the field is 1, else 0.
| ===8.1.1.4 NO: (4-bit)=== This field indicates the serial number of each 32-bit word.
| ====8.1.2 PAYLOAD: (32-bit)==== Data to be transferred from the SHARC Target to the SigmaStudio Plus Host is available in the payload. Each word contains 16-bit data, 4-bit command and 4-bit word number.
| ===8.1.2.1 DATA: (16-bit)=== The 16-bits in MSB of every payload contain actual payload data. Float values are split into two 32-bit payload words with each payload word containing 16-bits of data. When a 32-bit word is split into two 32-bit payload words, the LSB bits of the float word are put inside the first payload word. There is only one payload word in case of Version read and the 16 MSB of the version is inserted in the data field. nData element of the back channel information structure (pBkChnlInfo->nData) contains the Version and Code download status information. MIPS is computed by the Application. Other Read-back values are extracted from the memory using the offset and size.
| |image68|

.. container:: centeralign

   \ **Table 5:** Read-back Payload Data Field


8.1.2.2 CMD: (4-bit)
^^^^^^^^^^^^^^^^^^^^

| This field identifies the type of read back data in the packet. This is the 4 LSB bits of the read back type given in Table 3 associated with current packet.
| ===8.1.2.3 NO: (4-bit)=== This field indicates the serial number of each 32-bit word.
| ====8.1.3 END: (32-bit)==== The END word consists of the END_CMD command, which indicates the end of packet, the CRC checksum value for the packet and word number.
| ===8.1.3.1 END_CMD: (16-bit)=== This 16-bit word indicates the end of a communication packet.
| ===8.1.3.2 CRC: (8-bit)=== CRC field is used for protection. The current version uses a simple checksum of individual bytes of payload contents.
| For the read-back channel data, the CRC will be computed based on the payload data. This will be summed into an 8-bit value, and the two’s complement of this sum will be appended to the packet.
| Example:
| uint8_t compute_crc(uint32_t \*data, uint32_t length) {

::

     uint32_t nSum = 0U;

::

     // Sum all 32-bit words in the data array
     for (uint32_t i = 0; i < length; i++) {
         nSum += data[i];
     }

::

     uint32_t nFin = 0U;

::

     // Sum all 4 bytes of the 32-bit sum
     nFin += (nSum >> 24U) & 0xFFU;  // Extract most significant byte
     nFin += (nSum >> 16U) & 0xFFU;  // Extract 2nd byte
     nFin += (nSum >> 8U)  & 0xFFU;  // Extract 3rd byte
     nFin +=  nSum         & 0xFFU;  // Extract least significant byte

::

     // Calculate two's complement of the byte sum
     uint32_t nCRC = (~nFin) + 1U;

::

     // Return only the least significant byte as the checksum
     return (uint8_t)(nCRC & 0xFFU);

| }
| ===8.1.3.3 RSVD: (4-bit)=== This field is reserved.
| ===8.1.3.4 NO: (4-bit)=== This field indicates the serial number of each 32-bit word.
|

.. note::

   The first 4 bytes of Read Request’s MOSI and Read Response’s MISO are done to synchronize the SigmaStudioPlus Host with target. Hence, when a user is trying to implement the same by sending the command packet from a host microcontroller rather than SigmaStudioPlus, those 4 bytes can be ignored


   |image69|

.. container:: centeralign

   \ **Figure 60:** MIPS Read Request and Complete Response Packet


   |image70|

.. container:: centeralign

   \ **Figure 61:** Dual Core MIPS Read Request and Complete Response Packet


   |image71|

.. container:: centeralign

   \ **Figure 62:** Version Read Request and Complete Response Packet


   |image72|

.. container:: centeralign

   \ **Figure 63:** Read-back value Request and Complete Response Packet


   |image73|

.. container:: centeralign

   \ **Figure 64:** Error Code/ Code Download Status Request and Complete Response Packet


| **Terminology**

======== ============================================================
**Term** **Description**
======== ============================================================
ADI      Analog Devices Inc.
API      Application Program Interface
OBJ      Object file format in CrossCore Embedded Studio environment
SPI      Serial Peripheral Interface
SSn      SHARC machine code corresponds to SigmaStudio Plus Schematic
USB      Universal Serial Bus
XML      Extensible Markup Language
======== ============================================================

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ssplusuc_target_1.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/toolssettingsoption.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/auto_export_system_files.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/autoexport_processorname.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/autoexport_processorname_exported2.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/autoexport_processorname_exported3.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/autoexport_processorname_exported1.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/autoexport_corename.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/autoexport_corename_exported1.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/autoexport_schematicname.png
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/autoexport_schematicname_exported1.png
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/autoexport_processorcorename_exported1.png
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/exportsystemfiles.png
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/exportfiles_json.png
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/exportfiles_netlist.png
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/exportfiles_target.png
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/defines_h.png
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/param.png
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/schematic_y.h.png
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/param_h.png
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/numbytes.dat.png
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/txbuffer_dat.png
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/txmetabuffer_dat.png
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/txmeta_sh0.png
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/txmeta_sh1.png
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/xml_schema_updated.png
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/xml_schema_part.png
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/xml_schema_part.png
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/xml_sh0_v0.1.png
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/xml_sh1_v0.1.png
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/communicationprotocol.png
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/coreid_instanceid.png
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_begin.png
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/crc.png
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/view_capture.png
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/packet_capture.png
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/completepacket_sh0.png
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/completepacket_sh1.png
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/readrequestpayload.png
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_program_ssn_completed.png
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_parameter_no_safe_completed.png
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_parameter_safe_completed.png
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_block_safe_completed.png
.. |image44| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/declaringvarwithtxbuffdat.png
.. |image45| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_cmd7_completed.png
.. |image46| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_cmd1_completed.png
.. |image47| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_cmd2_completed.png
.. |image48| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_cmd6_completed.png
.. |image49| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_partial_end_completed.png
.. |image50| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_program_ssn_completed.png
.. |image51| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_parameter_safe_completed.png
.. |image52| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_parameter_no_safe_completed.png
.. |image53| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/ss_cmd_block_safe_completed.png
.. |image54| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/mutemodulederiveparamvalue.png
.. |image55| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/eq1.png
.. |image56| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/eq2.png
.. |image57| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/algo0.png
.. |image58| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/algo1.png
.. |image59| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/exportexampleschematic.png
.. |image60| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/exportexamplecapture.png
.. |image61| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/configcallbackcmd4.png
.. |image62| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/cmd5_led_status.png
.. |image63| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/getpropertiescmd5.png
.. |image64| image:: https://wiki.analog.com/_media/disablefetchtracking/cmd4_resetcommunicationerror.png
.. |image65| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/callbackresetcmd4.png
.. |image66| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/cmd4_led_status.png
.. |image67| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/backchannelspipacket.png
.. |image68| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/readbackpayloaddatafield.png
.. |image69| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/readmips_fullpackage.png
.. |image70| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/readdualcoremips.png
.. |image71| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/readversion_fullpackage.jpg
.. |image72| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/readbackvalue_fullpackage.jpg
.. |image73| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/readerrorcode_fullpackage.png
