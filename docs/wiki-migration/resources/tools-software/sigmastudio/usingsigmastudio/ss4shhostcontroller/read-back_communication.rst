`Click here to return to 'SigmaStudio for SHARC Host Controller' page. <https://wiki.analog.com/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller>`__

Read-Back Communication
=======================

| The source code to packetize and send the read-back information is available with the released Application. Refer to the files backchannel.c and backchannel.h for source code and further details.
| =====Back Channel Protocol (SHARC Target to SigmaStudio Host)===== All communications from the SHARC Target to the SigmaStudio Host PC application use a byte based protocol as shown below.
| |image1| The lower 4 bits of each word enumerate each word. The words in the packet are enumerated in ascending order. The figure given above is used as a reference for listing individual content of packet.
| ====BEGIN:(32-bit)==== The BEGIN word of size 32-bit indicates the beginning of packet. This contains a BEGIN_CMD command, the size of sub packets in bytes, format of sub packet and word number.
| ====BEGIN_CMD:(16-bit)==== This 16-bit word indicates the beginning of a communication packet.
| ====SIZE:(8-bit)==== This indicates the total length of data in payload in bytes.
| ====FORMAT:(4-bit)==== This field designates the format of the packet contents. The packet contents can be in 8-bit format or 24-bit format. When the content of the packet is in 8-bit format, the MSB of the field is 1, else 0.
| ====NO:(4-bit)==== This field indicates the serial number of each 32-bit word.
| =====PAYLOAD:(32-bit)===== Data to be transferred from the SHARC Target to the SigmaStudio Host is available in the payload. Each word contains 16-bit data, 4-bit command and 4-bit word number.
| ====DATA:(16-bit)==== The 16-bits in MSB of every payload contain actual payload data. Float values are split into two 32-bit payload words with each payload word containing 16-bits of data. When a 32-bit word is split into two 32-bit payload words, the LSB bits of the float word are put inside the first payload word. There is only one payload word in case of Version read and the 16 MSB of the version is inserted in the data field. nData element of the back channel information structure (pBkChnlInfo->nData) contains the Version and Code download status information. MIPS is computed by the Application. Other Read-back values are extracted from the memory using the offset and size.
| ^ Command ^ Number of 16-bit Data Words in the Response ^ Response data ^^^^

+------------------------+--------------------------------------+-------------------------------------+----------------------------+-----------------------------+-----------------------------+
| :::                    | :::                                  | Word 1                              | Word 2                     | Word 3                      | Word 4                      |
+========================+======================================+=====================================+============================+=============================+=============================+
| SS_CMD_BK_MIPS_VALUE   | 4                                    | 16 LSB bits of MIPS                 | 16 MSB bits of MIPS        | 16 LSB bits of Peak MIPS    | 16 MSB bits of Peak MIPS    |
+------------------------+--------------------------------------+-------------------------------------+----------------------------+-----------------------------+-----------------------------+
| SS_CMD_BK_VERSION_INFO | 1                                    | 16 MSB bits of 32 bit Version Value | :::                        | :::                         | :::                         |
+------------------------+--------------------------------------+-------------------------------------+----------------------------+-----------------------------+-----------------------------+
| SS_CMD_BK_READ_VALUE   | 2 \* Number of Read-back Values      | 16 LSB bits of first value          | 16 MSB bits of first value | 16 LSB bits of second value | 16 MSB bits of second value |
+------------------------+--------------------------------------+-------------------------------------+----------------------------+-----------------------------+-----------------------------+
| SS_CMD_BK_ERROR_CODE   | 2                                    | 16 LSB bits of error code           | 16 MSB bits of error code  | :::                         | :::                         |
+------------------------+--------------------------------------+-------------------------------------+----------------------------+-----------------------------+-----------------------------+
| SS_CMD_BK_ACKNOWLEDGE  | No return for acknowledgement packet | :::                                 | :::                        | :::                         | :::                         |
+------------------------+--------------------------------------+-------------------------------------+----------------------------+-----------------------------+-----------------------------+

| 
| Table 5: Read-back Payload Data Field
| ====CMD:(4-bit)==== This field identifies the type of read back data in the packet. This is the 4 LSB bits of the read back type given in Table 3 associated with current packet.
| ====NO:(4-bit)==== This field indicates the serial number of each 32-bit word.
| =====END:(32-bit)===== The END word consists of the END_CMD command, which indicates the end of packet, the CRC checksum value for the packet and word number.
| ====END_CMD:(16-bit)==== This 16-bit word indicates the end of a communication packet.
| ====CRC:(8-bit)==== CRC field is used for protection. The current version uses a simple checksum of individual bytes of payload contents.
| ====RSVD:(4-bit)==== This field is reserved.
| ====NO:(4-bit)==== This field indicates the serial number of each 32-bit word.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_10.jpg
