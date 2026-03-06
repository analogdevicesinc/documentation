`Click here to return to 'SigmaStudio for SHARC Host Controller' page. <https://wiki.analog.com/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller>`__

Packetizing Data
================

| The data received while exporting the code and parameters has to be packetized properly before sending it to the SHARC Target board.
| =====Communication Protocol===== All the communication between the SigmaStudio Host PC and the SHARC Target use the following protocol: |image1| Each packet contains a begin command, size of the packet, payload data, CRC value, SHARC Target memory type and an end command. The individual contents of the packet are listed below.
| ====SS_CMD_BEGIN: (32-bit word)==== The field indicates beginning of the packet. Refer to Table 2for 32-bit hexadecimal value of the field.
| ====CMD: (32-bit word)==== The CMD field indicates the nature of payload in the packet. The value of this field can vary from packet to packet. Refer to Table 2 for possible 32-bit hexadecimal values of this field.
| ====Payload==== This contains the data to be transferred from the SigmaStudio Host to the SHARC Target. The contents of payload are given below.
| ====PL_LEN: (32-bit word)==== This field indicates the total length of the payload, including CRC.
| ===PAYLOAD_DATA:=== Actual payload in the packet appears in this portion. The payload can be data/code/parameter.
| ===CRC: (32-bit word)=== The CRC field is used for protection. The current version uses simple checksum. The code used to compute CRC data is given below. Here pData[] is the buffer of type unsigned int.
| ``for (i = 0; i < nSizeBytes/4; i++)
  {
  nSum += pData[i];
  }
  nCRC = ~nSum + 1;`` The SHARC Target can compute the CRC of the received packet either only on the payload or on the entire packet based on the configuration parameter. The above example shows CRC checksum computed only on the payload. Alternatively, the CRC checksum can also be computed on the entire packet.
| ===MEM_ADDR: (32-bit word)=== This field indicates the memory address to which the code/parameter should be loaded. This field is used only when the command is either SS_CMD_BLOCK_SAFE or SS_CMD_PARAMETER_NO_SAFE.
| ===SS_CMD_END: (32-bit word)=== This 32-bit word indicates the end of a communication packet. Refer to Table 2 for 32-bit hexadecimal value of the field.
| =====Commands for Communication===== All the commands and fields indicating begin/end with their 32-bit hexadecimal values are listed in Table 2.
| ^ Command ^ Description ^ Value ^ Payload ^

+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_BEGIN             | Signifies the beginning of packet                                                                                                                                                         | 0xf4190be6 | None                                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_PROGRAM_SSN       | Indicates that the packet contains code                                                                                                                                                   | 0xfaad0552 | SigmaStudio generated code                                      |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_PARAMETER_SAFE    | Indicates that the packet contains safe-load parameters.                                                                                                                                  | 0xa5015afe | Up to 5 sets of safe-load parameters and respective addresses   |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_PARAMETER_NO_SAFE | Indicates that the packet contains a block of parameters that can be directly loaded on to the parameter memory. Used for initial parameter set and block parameter update during Tuning. | 0xffa1f05e | Block of parameters                                             |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_BLOCK_SAFE        | Indicates that the packet contains a block of parameters to be safe-loaded. Used for block parameter update during Tuning.                                                                | 0x4ea5b15a | Block parameters                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD1              | Predefined command 1. Used for sending Reset.                                                                                                                                             | 0xf3f20c0d | Word and Block DMA receive mode flag                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD2              | Predefined command 2. Used for sending version information.                                                                                                                               | 0xf3e20c1d | Version information                                             |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD3              | Predefined command 3. Used for sending read request.                                                                                                                                      | 0xf3d20c2d | Read request                                                    |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD4              | Predefined command 4 that calls a call-back function with the payload as arguments.                                                                                                       | 0xf3c20c3d | User defined data that is interpreted by the call-back function |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD5              | Payload containing custom command that can be obtained by calling adi_ss_comm_GetProperties () function                                                                                   | 0xf3b20c4d | User defined command                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD6              | Predefined command 6. Used for sending Schematic bypass flag.                                                                                                                             | 0xf3a20c5d | Bypass flag                                                     |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_CMD7              | Indicates that the packet contains SMAP data. This is applicable or used only when the IC is ADSP-SC58x.                                                                                  | 0xf3920c6d | SMAP                                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_PARTIAL_END       | Partial end of current packet                                                                                                                                                             | 0xe1d21e2d | None                                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+
| SS_CMD_END               | End of current packet                                                                                                                                                                     | 0xf1d20e2d | None                                                            |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------------------------------------------------------+

| Table 2: Communication Commands
| =====Read Request Payload===== PAYLOAD_DATA inside read request packets are of length 3 or 4 words depending on the read request type and is described below. |image2|
| ====NUMBER_OF_REQUESTS: (32-bit word)==== The field indicates the number of read requests in the current read request packet. This should always be set to 1.
| ====READBACK_TYPE: (32-bit word)==== The field indicates the type of read request. Refer to the table below for more details.
| ^ Command ^ Description ^ Value ^

+-------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_MIPS_VALUE    | Indicates read request for MIPS                                                                                                  | 0x00CE6319U |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_DC_MIPS_VALUE | Indicates read request for Dual-Core MIPS                                                                                        | 0x00DC6239U |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_VERSION_INFO  | Indicates read request for Version                                                                                               | 0x003EDC12U |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_READ_VALUE    | Indicates read request from Parameter memory. Read back, Level Detector etc. Modules use this command to read value from memory. | 0x00BC543AU |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_ERROR_CODE    | Indicates read request for code download status.                                                                                 | 0x00F7E808U |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------+
| SS_CMD_BK_ACKNOWLEDGE   | Indicates acknowledgement for successful read.                                                                                   | 0x00000000  |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------+

| Table 3: Read-back Type
| ====NUMBER_OF_WORDS: (32-bit word)==== This field indicates the number of values to be read from the SHARC Target. This field is valid only when the read type is SS_CMD_BK_READ_VALUE. This field should be 0 for other read types.
| ====ADDRESS: (32-bit word)==== This field indicates the offset, from the start of parameter memory, to the memory location from where the value has to be read. This field is included in the payload only when the read type is SS_CMD_BK_READ_VALUE. Therefore the payload size is 3 for other read types.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_5.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_6.jpg
