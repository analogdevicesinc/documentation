`Click here to return to 'SigmaStudio for SHARC Host Controller' page. <https://wiki.analog.com/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller>`__

Using Exported Data
===================

Deriving Payload Contents
-------------------------

| The exported files NumBytes_IC_y.dat and TxBuffer_IC_y.dat need to be modified before directly including in the Application. A variable can be declared in such a manner that it contains all values in TxBuffer_IC_y.dat. Thus, the content of TxBuffer_IC_y.dat can be modified as given below
| ``unsigned char aCodeParam[] = {
  0x00, 0x00, /* (0) Reset */
  0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, /* (1) Version Info */
  0x20, 0x00, 0x00, 0x00,
  0x00, 0x00, /* (2) Program Data */
  0xFF, 0xFF, 0xFF, 0xFA,
  ----------------------
  ----------------------
  };`` Similarly a variable of data type int can be used to modify NumBytes_IC_y.dat. After the modifications are done, the files can be directly included in the Application source code.
| The “.h” files generated during export can be directly included in the Application. In addition, these header files include SigmaStudioFW.h. This has to be taken from the installation folder for SigmaStudio (E.g. “C:\\Program Files\\Analog Devices\\SigmaStudio 3.12”)
| Note that every parameter in TxBuffer_IC_y.dat has two preceding bytes with zero value. These are not part of the parameter value and should be skipped before using data for communication. In addition, the file xxx_IC_y.h contains code, reset version etc. in header file format.
| Alternately, the file “TxMetaBuffer_IC_y.dat” can be used to derive the start address of the parameter required by the SigmaStudio Host for tuning the parameter based on its name. The parameter name can be obtained from the file “TxMetaBuffer_IC_y.dat”. The parameter name is a combination of “Cell Name” and “Algorithm Index” which are present in the file “xxx.params”. The parameter name is nothing but “Cell Name” + “\_” + “Algorithm Index” capitalized.
| ====SMAP==== Command used: SS_CMD_CMD7
| This is applicable only when the IC used is ADSP-SC58x.
| The entire set of SMAP data is present in the file xxx_IC_y.h in hexadecimal unsigned char format under the variable name SMAP_Data[]. The size of the SMAP structure can be taken from the macro SMAP_SIZE. Note that there are no dummy bytes when the data is taken from this header file.
| Alternatively the parameter data can be taken from TX_Buffer_IC_y.dat using the offset and size from NumBytes_IC_y.dat file. Care should be taken to skip the initial two bytes in this case.
| ====Reset==== Command used: SS_CMD_CMD1
| The reset parameter consists of a 32-bit hexadecimal word with value 0 or 1. Sending this parameter with the associated command to the SHARC Target prepares the SHARC Target to receive new SSn code and parameter data. When the parameter is 0, the SHARC Target receives the data sent by SPI as single words and processes it. On sending a value of 1, the SHARC Target receives code and parameter as a block and processes the CRC check on the next call of adi_ss_schematic_process() function.
| ====Version Information==== Command used: SS_CMD_CMD2
| The version information is also a 32-bit hexadecimal value whose first 2 bytes give the version of the process API used in the Application. The version of the process API used in the Application for this release is 2.1.0. This data is present in TX_Buffer_IC_y.dat with the most significant byte coming first. The offset to access the version information and its size can be obtained from the NumBytes_IC_y.dat file. Although the size of the version information is given as 6 bytes, the first two bytes are dummy values and have to be omitted to obtain the real version information value.
| ====Schematic Code==== Command used: SS_CMD_PROGRAM_SSN
| The code for Schematic is present in TX_Buffer_IC_y.dat as the third parameter. Its size and offset to access it can be obtained from NumBytes_IC_y.dat file. The Schematic code also has 2 dummy bytes in the beginning and these have to be skipped to access the code. The size of the code varies for each Schematic and should be updated when a Schematic is modified. The data present is such that the most significant byte comes first.
| ====Parameters==== Command used: SS_CMD_PARAMETER_NO_SAFE / SS_CMD_PARAMETER_SAFE / SS_CMD_BLOCK_SAFE
| The entire set of parameters is present in the file xxx_IC_y.h in hexadecimal unsigned char format under the variable name Param_Data[]. The size of the parameter table can be taken from the macro PARAM_SIZE. Note that there are no dummy bytes when the data is taken from this header file.
| Alternatively the parameter data can be taken from TX_Buffer_IC_y.dat using the offset and size from NumBytes_IC_y.dat file. Care should be taken to skip the initial two bytes in this case.
| =====Sending Schematic Code===== The Schematic code has to be sent to the SHARC Target when a new Schematic is generated or an existing Schematic is modified. In order to successfully send the Schematic code to the SHARC Target, the following steps have to be executed.
| \* Send SMAP for the schematic (applicable only for ADSP-SC58x). This reserves the necessary memory blocks in the Target.

-  Send Reset parameter: This prepares the SHARC Target for receiving the code
-  Send Version Information: This ensures compliance between the SHARC Target and the SigmaStudio Host.
-  Send Schematic Code: Algorithm code for the SHARC Target
-  Send Parameters: Parameters for the code to work with.

| 
| Once the entire data is sent to the SHARC Target running SigmaStudio, the SHARC Target can start processing the data.
| =====Parameter Reloading===== If the Schematic code and parameters are successfully sent to the SHARC Target then the block of parameters for the particular Schematic alone can be updated. A step-by-step procedure is given below.
| \* Send Reset parameter: This prepares the SHARC Target for receiving the code

-  Send Version Information: This ensures compliance between the SHARC Target and the SigmaStudio Host.
-  Send Parameters: Parameters for the code to work with.

| 
| Once the entire data is sent to the SHARC Target running SigmaStudio, the SHARC Target can start processing the data.
| =====Sending Parameter for Tuning===== To send a parameter for Tuning, both the parameter and its address offset need to be sent to the SHARC Target. The parameter data sent should be the 32-bit hexadecimal equivalent of floating point or fixed point value, followed by the offset address location of the parameter.
| Every single value to be written to the parameter memory during Tuning should be succeeded by the address location to which it is to be written. The values should then be packetized and sent to the SHARC Target. Hence the data to be packetized is of the form
| \* Parameter value in 32-bit hexadecimal

-  Offset address location in 32-bit hexadecimal.

| 
| Note that Reset and Version packets are not required during Tuning.
| ====Flashing Data and Accessing it for Tuning==== The file TxMetaBuffer_IC_y.dat has a tune table which contains parameter data, its address and a string to uniquely identify the Algorithm. The file can be directly flashed to the memory of a micro-controller and can be directly accessed from there. This approach has the advantage that once the Schematic is frozen and only the Tuning has to be performed, a Tuning engineer can do so without modifying the micro-controller code.
| ====Using Header Files==== The parameter data and its offset location can be found as a macro in the file xxx_IC_y_PARAM.h. The file xxx_IC_y.h contains a parameter data buffer named Param_Data_IC\_<y> [] and a macro defining the size of the parameter data termed PARAM_SIZE. Since the data in the buffer Param_Data_IC\_<y> [] is given in bytes, the offset address can be multiplied with 4 to derive the address of the parameter data. An example use case is given below.
| Let the offset address of the Mute Algorithm in a Schematic be given by the macro MOD_MUTE1_MUTE_ADDR, the value of parameter can be derived as

.. code:: csharp

   aParamMute[0] = Param_Data[MOD_MUTE1_MUTE_ADDR*4]<< 24;
   aParamMute[0] += Param_Data[MOD_MUTE1_MUTE_ADDR*4 + 1]<< 16;
   aParamMute[0] += Param_Data[MOD_MUTE1_MUTE_ADDR*4 + 2]<< 8;
   aParamMute[0] += Param_Data[MOD_MUTE1_MUTE_ADDR*4 + 3];

| 
