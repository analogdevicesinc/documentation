`Click here to return to 'SigmaStudio for SHARC Host Controller' page. <https://wiki.analog.com/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller>`__

SigmaStudio Data Export
=======================

| The SigmaStudio Host application can export the code and parameters that are to be sent to the SHARC Target once it is booted. This section describes how to export and use the system files.
| =====Export Settings===== The export related settings can be configured through the SigmaStudio Settings window. The “Settings” window can be launched by selecting Tools -> Settings.
| ====Export Mode==== The user can select whether, on export, all files are to be generated or only the XML file is to be generated. ‘Export Mode’ is present in the ‘System Files Export’ tab of the Settings window. If ‘XML Only’ is checked, only the XML file is generated on export. Otherwise, all export system files including the XML file are generated.
| ====Auto Export Mode==== Export files can be automatically generated after a successful ‘Link-Compile-Download’ by enabling ‘Auto Export System Files’ in the SigmaStudio settings window. |image1|
| =====Exporting System Files===== The system files can be exported after a Schematic is successfully compiled. Once the ‘Link-Compile-Download’ action is complete, the system files can be exported by selecting Action -> Export System Files. |image2|
| Note: The Action -> Export System Files menu item is inactive if the Schematic is not compiled after any modifications.
| The name of system files and the folder to which it can be saved is to be decided by the user. The files contain code, parameter and version information to be sent to the SHARC Target. The files should be freshly generated every time the Schematic is modified.
| =====System File Contents and Usage===== Examples of the content of the exported files and associated descriptions are given in this section. Files that are named by the user are named “xxx” for ease of representation. The file name also contains information on the IC used and has a text of form “\_IC_1” for IC-1. The name can be modified by the user. For ease of representation this is indicated by “\_IC_y” in the document.
| ====defines.h==== <fc #6495ed>\ *Example Contents*\ </fc>

.. code:: csharp

   #define BufferSize_IC_1 9792
   #define NumTransactions_IC_1 4

| <fc #6495ed>\ *Description*\ </fc>
| The file contains definitions for the size of data in the system files. The macro BufferSize_IC_y gives the total size in bytes of reset, version, code and parameter data. Related data can be found in the file TxBuffer_IC_y.dat. The macro NumTransactions_IC_y contains the size of the data contained in NumBytes_IC_y.dat.
| ====xxx.hex==== <fc #6495ed>\ *Example Contents*\ </fc>

.. code:: csharp

   0x00 , 0x00 , 0x00 , 0x00 ,
   0x3F , 0x19 , 0x99 , 0x9A ,

| <fc #6495ed>\ *Description*\ </fc>
| This file contains the parameter data in 8-bit hexadecimal format. The order in the file is such that the most significant byte of a 32-bit hexadecimal word comes first.
| ====xxx.params==== <fc #6495ed>\ *Example Contents*\ </fc>

.. code:: csharp

   IC Name = IC 1
   Cell Name = Tone1
   Algorithm Index = ALG0
   Parameter Name = ToneGen1_cos
   Parameter Address = 1
   Parameter offset = 0
   Parameter Value = 0.997858837246895
   Parameter Data :
   0X3F , 0XDC , 0XEB , 0X50 ,

| <fc #6495ed>\ *Description*\ </fc>
| This file lists all parameters used by the individual Cells, the index of the Algorithm within the Cell, parameter name, address, parameter offset, value and 8-bit hexadecimal representation of the parameters. The entire parameter data in 8-bit hexadecimal and corresponding binary representation is also present in the file.
| ====xxx_IC_y.h==== <fc #6495ed>\ *Example Contents*\ </fc>

.. code:: csharp

   #include "SigmaStudioFW.h"
   #include "inout_IC_1_REG.h"
   #define DEVICE_ARCHITECTURE_IC_1 "ADSP-213xx"
   #define DEVICE_ADDR_IC_1 0x0
   #define PARAM_SIZE_IC_1 8192
   #define PARAM_ADDR_IC_1 0
   ADI_REG_TYPE Param_Data_IC_1[PARAM_SIZE_IC_1] = {
   0x00, 0x00, 0x00, 0x00,
   --, --, --, --, };

| <fc #6495ed>\ *Description*\ </fc>
| This file lists the IC used, size and offset address for writing code and parameters. Two files are included by this file. SigmaStudioFW.h has to be taken from the installation folder for SigmaStudio (E.g. “C:\\Program Files\\Analog Devices\\SigmaStudio 3.12”). The Program data and Param_Data buffers declared in the file can be directly used in the Application to access program data and parameter data respectively.
| ====xxx_IC_y_PARAM.h==== <fc #6495ed>\ *Example Contents*\ </fc>

.. code:: csharp

   #define MOD_TONE1_COUNT 3
   #define MOD_TONE1_DEVICE "IC1"
   #define MOD_TONE1_ALG0_COS_ADDR 1
   #define MOD_TONE1_ALG0_COS_VALUE SIGMASTUDIOTYPE_2_30_CONVERT(0.99785883763)
   #define MOD_TONE1_ALG0_COS_TYPE SIGMASTUDIOTYPE_2_30
   #define MOD_TONE1_ALG0_SIN_ADDR 2
   #define MOD_TONE1_ALG0_SIN_VALUE SIGMASTUDIOTYPE_2_30_CONVERT(0.06540443542)
   #define MOD_TONE1_ALG0_SIN_TYPE SIGMASTUDIOTYPE_2_30
   --, --, --, --, };

| <fc #6495ed>\ *Description*\ </fc>
| This file gives all the details regarding parameter data for the individual Cells in the form of macros. The macros used in this header file are defined in the SigmaStudioFW.h file. The file also lists the parameters to be sent to the SHARC Target processor, in 32-bit hexadecimal representation of floating point or fixed point values.
| Note: All the macros in SigmaStudioFW.h are not defined and therefore the user can customize and use the header file in the Application.
| ====xxx_IC_y_REG.h==== <fc #6495ed>\ *Description*\ </fc>
| This file does not convey any information as such in the current release of SigmaStudio for SHARC. This file can be ignored.
| ====NumBytes_IC_y.dat==== <fc #6495ed>\ *Example Contents*\ </fc>

.. code:: csharp

   6,
   6,
   1682,
   8194,

| <fc #6495ed>\ *Description*\ </fc>
| The file lists the number of bytes for reset, version information, SHARC Target code and parameters respectively in the file TxBuffer_IC_y.dat.
| ====TxBuffer_IC_y.dat==== <fc #6495ed>\ *Example Contents*\ </fc>

.. code:: csharp

   0x00, 0x00, /* (0) Reset */
   0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, /* (1) Version Info */
   0x20, 0x00, 0x00, 0x00,
   0x00, 0x00, /* (2) Program Data */
   0xFF, 0xFF, 0xFF, 0xFA,
   .
   .
   0x00, 0x00, /* (3) Parameter Data */
   0x00, 0x00, 0x00, 0x00,

| <fc #6495ed>\ *Description*\ </fc>
| The file lists all the parameters to be sent to the SHARC Target in 8-bit hexadecimal format. Note that two zeros each of 1 byte size are added before each new parameter. These two zeros are not required while sending the parameters from a SigmaStudio uC Host to the SHARC Target.
| ====TxMetaBuffer_IC_y.dat==== <fc #6495ed>\ *Example Contents*\ </fc>

.. code:: csharp

   0X00, 0X00, 0X00, 0X06, /* Size - Reset */
   0X00, 0X00, 0X00, 0X06, /* Size - Version Info */
   0X00, 0X00, 0X06, 0XDA, /* Size - Program Data */
   0X00, 0X00, 0X06, 0XDA, /* Size - Parameter Data */
   0X00, 0X00, 0X00, 0X25, /* Size - Parameter Metadata */
   0x00, 0x00, /* (0) Reset */
   0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, /* (1) Version Info */
   0x20, 0x00, 0x00, 0x00,
   0x00, 0x00, /* (2) Program Data */
   0x00, 0xFF, 0xFC, 0xFA,
   .
   0x00, 0x00, /* (2) Parameter Data */
   0x00, 0xFF, 0xFC, 0xFA,
   .
   0x00, 0x08, /* (2) Parameter Meta Data */

The format of the content can be represented as shown below

.. code:: csharp

   /* Beginning of file */
   Reset_Data_Size[4]
   Version_Data_Size[4]
   Program_Data_Size[4]
   Parameter_Data_Size[4]
   Tuning_Data_Size[4]
   Reset_Data[....]
   Version_Data[....]
   Program_Data[....]
   Parameter_Data[....]
   /* Tuning Data*/
   CellName_AlgoNo_String_Length1, CellName_AlgoNo_String1,Parameter_Base_Address1,
   CellName_AlgoNo_String_Length2, CellName_AlgoNo_String2,Parameter_Base_Address2,
   CellName_AlgoNo_String_LengthN, CellName_AlgoNo_StringN,Parameter_Base_AddressN
   /*End of file*/

| <fc #6495ed>\ *Description*\ </fc>
| The data in this file contain Reset, Version, Program Data, Parameter Data and information required for Tuning individual Cells. The data can be flashed or stored to a memory location and then accessed from there. The various fields in the header file are as follows:
| <fc #cd5c5c>\ *Name*\ </fc>:Reset_Data_Size
| <fc #cd5c5c>\ *Type*\ </fc>:4bytes, big endian unsigned integer
| <fc #cd5c5c>\ *Description*\ </fc>:Signifies the size of the Reset data.
| <fc #cd5c5c>\ *Name*\ </fc>:Version_Data_Size
| <fc #cd5c5c>\ *Type*\ </fc>:4bytes, big endian unsigned integer
| <fc #cd5c5c>\ *Description*\ </fc>:Signifies the size of the Version data.
| <fc #cd5c5c>\ *Name*\ </fc>:Program_Data_Size
| <fc #cd5c5c>\ *Type*\ </fc>:4bytes, big endian unsigned integer
| <fc #cd5c5c>\ *Description*\ </fc>:Signifies the size of the Program data.
| <fc #cd5c5c>\ *Name*\ </fc>:Parameter_Data_Size
| <fc #cd5c5c>\ *Type*\ </fc>:4bytes, big endian unsigned integer
| <fc #cd5c5c>\ *Description*\ </fc>:Signifies the size of the Parameter data.
| <fc #cd5c5c>\ *Name*\ </fc>:Tuning_Data_Size
| <fc #cd5c5c>\ *Type*\ </fc>:4bytes, big endian unsigned integer
| <fc #cd5c5c>\ *Description*\ </fc>:Signifies the size of the Tuning meta data.
| <fc #cd5c5c>\ *Name*\ </fc>:Reset_Data
| <fc #cd5c5c>\ *Type*\ </fc>:Byte array, big endian hexadecimal
| <fc #cd5c5c>\ *Description*\ </fc>:Data for Reset information. Note that first two bytes need not be sent to SHARC Target.
| <fc #cd5c5c>\ *Name*\ </fc>:Version_Data
| <fc #cd5c5c>\ *Type*\ </fc>:Byte array, big endian hexadecimal
| <fc #cd5c5c>\ *Description*\ </fc>:Data for Version information. Note that first two bytes need not be sent to SHARC Target.
| <fc #cd5c5c>\ *Name*\ </fc>:Program_Data
| <fc #cd5c5c>\ *Type*\ </fc>:Byte array, big endian hexadecimal
| <fc #cd5c5c>\ *Description*\ </fc>:Data for Program information. Note that first two bytes need not be sent to SHARC Target.
| <fc #cd5c5c>\ *Name*\ </fc>:Parameter_Data
| <fc #cd5c5c>\ *Type*\ </fc>:Byte array, big endian hexadecimal
| <fc #cd5c5c>\ *Description*\ </fc>:Data for Parameter information. Note that first two bytes need not be sent to SHARC Target.
| <fc #cd5c5c>\ *Name*\ </fc>:CellName_AlgoNo_String_Length1
| <fc #cd5c5c>\ *Type*\ </fc>:2bytes, big endian unsigned integer
| <fc #cd5c5c>\ *Description*\ </fc>:Number of bytes for string with Cell Name and Algorithm number of "Nth" tuneable block in Schematic.
| <fc #cd5c5c>\ *Name*\ </fc>:CellName_AlgoNo_String1
| <fc #cd5c5c>\ *Type*\ </fc>:Character array
| <fc #cd5c5c>\ *Description*\ </fc>:Character string without null containing the Cell Name and Algorithm number of "Nth" tuneable block in Schematic.
| <fc #cd5c5c>\ *Name*\ </fc>:Parameter_Base_Address1
| <fc #cd5c5c>\ *Type*\ </fc>:4bytes, big endian unsigned integer
| <fc #cd5c5c>\ *Description*\ </fc>:Offset address of the starting parameter of "Nth" tuneable block in the Schematic specified by the Cell Name and Algorithm number string.
| ====xxx.xml==== <fc #6495ed>\ *Example Contents*\ </fc>
| Only part of the output XML file is shown below in the example.
| ``<?xml version="1.0" encoding="utf-8"?>
  <Schematic>
      <IC>
          <Name>IC 1</Name>
             <Meta>
              <Name>SMAP</Name>
              <Size>240</Size>
              <Data>0x00, 0x00, 0x00, 0x12, 0x00, 0x00, 0x00, 0x04, 
             . . . . 
                   0x00, 0x2C, 0x8E, 0x54, </Data>
          </Meta>
          <Meta>
              <Name>Reset</Name>
              <Size>4</Size>
              <Data>0x00, 0x00, 0x00, 0x00, </Data>
          </Meta>
          <Meta>
              <Name>Version Info</Name>
              <Size>4</Size>
              <Data>0x21, 0x00, 0x00, 0x00, </Data>
          </Meta>
          <Program>
              <Name>Program Data</Name>
              <Address>0</Address>
              <Size>4580</Size>
              <Data>0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x07, 0x3E, 0x00, 0x01, 0x07, 
             . . . . 
             0x08, 0x3F, 0x00, 0x01, 0x00, 0x01, </Data>
          </Program>
          <Parameter>
              <Name>Parameter Data</Name>
              <Address>0</Address>
              <Size>376</Size>
              <Data>0x06, 0x0A, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3F, 0x73, 0xD5, 
             . . . .
             0x00, 0x00, </Data>
          </Parameter>
          <Module>
              <CellName>Gen Filter1</CellName>
              <Algorithm>
                  <AlgoName>ALG0</AlgoName>
                  <Description>1 Channel Single Precision Floating Point( 1 ) : Gain[ 0 ],Q[ 1.41 ],Boost1[ 0 ],Frequency1[ 1000 ],PhaseShifted[ False ],Type[ 0 ];</Description>
                  <Address>6</Address>
                  <ModuleParameter>
                      <Name>GenSecOrderFilt10B1</Name>
                      <Type>Float32</Type>
                      <Offset>0</Offset>
                      <Value>1.00494837760925</Value>
                      <Size>4</Size>
                      <Data>0x3F, 0x80, 0xA2, 0x26, </Data>
                  </ModuleParameter>
                  
           . . . .
           . . . .`` <fc #6495ed>\ *Description*\ </fc>
| The exported XML file contains SMAP (only in case ADSP-SC58x), Reset, Version, Program Data, Parameter Data and the information required for Tuning individual Cells. The information can be parsed using an xml parser. The XML file also includes the GUI parameter information of the Modules in the Schematic. The schema of the XML is illustrated below. |image3|
| <fc #cd5c5c>\ *IC*\ </fc>:Name of the Processor (ICs/DSPs) in the Hardware Configuration Window of the schematic. There can be more than one IC for a multiple SSn Schematic.
| Name:Name of the SSn (sub Schematics). Same as the Name of the IC. Default IC name is “IC 1”.
| <fc #cd5c5c>\ *Meta*\ </fc>:Meta information can be any value from { Reset, Version Info, SchematicVersionTag}
| Name:Name of the Meta information.
| Description:Meta information name can be any value from { Reset, Version Info, SchematicVersionTag}
| <fc #cd5c5c>\ *Program*\ </fc>:Program Memory
| Name:Name of the Program memory. This string can be from {Program Data, Program DataB}
| Address:Address offset to which the program has to be loaded. The start address is always the memory pointer pointed by Block 1/Block7 in ADI_SS_MEM_MAP respectively for Program Data/ Program DataB.
| Size:Size in Bytes (2 bytes less than the size reported in export file).
| Data:Data in Hexadecimal (Most significant byte comes first).
| <fc #cd5c5c>\ *Parameter*\ </fc>:Parameter Memory.
| Name:Name of the Parameter memory. This string can be from {Parameter Data}
| Address:Address offset to which the initial parameter has to be loaded. The start address is always the memory pointer pointed by Block 5 in ADI_SS_MEM_MAP. This is always 0.
| Size:Size in Bytes (2 bytes less than the size reported in export file)
| Data:Size in Bytes (2 bytes less than the size reported in export file).
| <fc #cd5c5c>\ *Module*\ </fc>:Details of individual Cells (A Cell is the basic graphical entity with one or more Algorithms).
| CellName:Name of the Cell
| <fc #cd5c5c>\ *Algorithm*\ </fc>:Details of individual Algorithm (An Algorithm is the basic processing entity with one or more Parameters associated to it)
| AlgoName:Index of the Algorithm within the Cell. There can be multiple Algorithms within a Cell.
| Description:Algorithm Description with Names of Algorithm and the GUI parameters.
| Address:Algorithm Starting address (offset from the beginning of the parameter memory)
| <fc #cd5c5c>\ *ModuleParameter*\ </fc>:Details of the individual parameter (Parameter is the basic Tuning entity with one or more data units).
| Name:Name of the parameter
| Type:Type of the parameter. Type can be {Int32, Float32, Hex}
| Offset:Offset from the Algorithm starting address
| Value:Value of the data element. Note: This is applicable only if the Parameter has a single data unit. In case of multiple data units, only the hexadecimal values are provided.
| For example,

.. code:: csharp

   <ModuleParameter>
   <Name>Taps</Name>
   <Type>Int32</Type>
   <Offset>0</Offset>
   <Value>5</Value>
   <Size>4</Size>
   <Data>0x00, 0x00, 0x00, 0x05, </Data>
   </ModuleParameter>
   <ModuleParameter>
   <Name>FIRFiltBlock1coeff</Name>
   <Type>HexArray</Type>
   <Offset>1</Offset>
   <Size>8</Size>
   <Data>0x3F, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, </Data>
   </ModuleParameter>

| 
| In the above example, the first parameter ‘Taps’ is a single data unit with a “Value” equal to 5. Whereas, the second parameter ‘FIRFiltBlock1coeff’ has multiple data units and hence, only hexadecimal values are provided.
| Size:Size in Bytes
| Data:Data in Hexadecimal (Most significant byte comes first)

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_2.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_3.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_4.jpg
