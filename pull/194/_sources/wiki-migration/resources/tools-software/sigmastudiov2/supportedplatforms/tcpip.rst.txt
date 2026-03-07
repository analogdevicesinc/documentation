:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/supportedplatforms>`

TCP/IP
======

| The TCP/IP communication adaptor can be used to connect with a target in case the target is present at a different location and cannot be physically connected the the PC that is running SigmaStudio+. SigmaStudio+ communicates with a server connected to the target using TCP/IP. The TCP/IP is present under the Communication Adaptors tree within the toolbox.
| ===== Settings ===== Following options are available on the settings window, which can be launched by double clicking on the TCP/IP shape in canvas

-  IP Address - IP address on which the server connected to target is listening
-  Port - Port number on which the server connected to target is listening
-  Close Connection - Close the connection
-  Open Connection - Open Connection
-  Register ASAP Connection - Establish connection without performing the background operations
-  Max Buffer Size - Maximum data buffer size

| Once the server is connected, SigmaStudio is free to send and receive data to and from the server.
| ===== Write Data Format ===== SigmaStudio+ sends the code and parameter information to the server connected to target in the following format:

| |image1|
| ^Field ^Description ^

+----------------------------------------+------------------------------------------------------------------------------------------------+
| -------------------------------------- | ---------------------------------------------------------                                      |
+----------------------------------------+------------------------------------------------------------------------------------------------+
| Control                                | This is the control bit that is used to indicate that it is a write packet. Its value is 0x09  |
+----------------------------------------+------------------------------------------------------------------------------------------------+
| Block / safeload write bit             | This field indicates whether the write packet is a block write or a safeload write             |
+----------------------------------------+------------------------------------------------------------------------------------------------+
| Channel number                         | This indicates the channel number                                                              |
+----------------------------------------+------------------------------------------------------------------------------------------------+
| Total length                           | This indicates the total length of the write packet. It is 4 bytes long                        |
+----------------------------------------+------------------------------------------------------------------------------------------------+
| Chip address                           | This is the address of the chip to which the data has to be written                            |
+----------------------------------------+------------------------------------------------------------------------------------------------+
| Data Length                            | This is the length of the data. This is 4 bytes long                                           |
+----------------------------------------+------------------------------------------------------------------------------------------------+
| Address                                | This is the address of the module whose data is being written to the DSP. This is 2 bytes long |
+----------------------------------------+------------------------------------------------------------------------------------------------+
| Data                                   | This is the data to be written                                                                 |
+----------------------------------------+------------------------------------------------------------------------------------------------+

| 
| ===== Read Request format ===== In order to achieve readback, SigmaStudio+ send a read request. The read request format is as shown

| |image2|
| ^Field ^Description ^

+----------------------------------------+-----------------------------------------------------------------------------------------------+
| -------------------------------------- | ---------------------------------------------------------                                     |
+----------------------------------------+-----------------------------------------------------------------------------------------------+
| Control                                | This is the control bit that is used to indicate that it is a read packet. Its value is 0x0A  |
+----------------------------------------+-----------------------------------------------------------------------------------------------+
| Total length                           | This indicates the total length of the read packet. It is 4 bytes long                        |
+----------------------------------------+-----------------------------------------------------------------------------------------------+
| Chip address                           | This is the address of the chip for which the data has to be read from                        |
+----------------------------------------+-----------------------------------------------------------------------------------------------+
| Data Length                            | This is the length of the data to read. This is 4 bytes long                                  |
+----------------------------------------+-----------------------------------------------------------------------------------------------+
| Address                                | This is the address of the module whose data is being read from the DSP. This is 2 bytes long |
+----------------------------------------+-----------------------------------------------------------------------------------------------+
| Reserved                               | There are two fields reserved for future use.                                                 |
+----------------------------------------+-----------------------------------------------------------------------------------------------+

| 
| ===== Read Response Format ===== The server connected to target must respond to the read request with a read response in the following format:

| |image3|
| ^Field ^Description ^

+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ---------------------------------- | ---------------------------------------------------------                                                                              |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Control                            | This is the control bit that is used to indicate that it is a read response packet. Its value is 0x0B                                  |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Total length                       | This indicates the total length of the read response packet. It is 4 bytes long                                                        |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Chip address                       | This is the address of the chip to which the data has been read from                                                                   |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Data Length                        | This is the length of the data. This is 4 bytes long                                                                                   |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Address                            | This is the address of the module whose data has been read from the DSP. This is 2 bytes long                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Success / Failure                  | This byte indicates whether the read operation was a success or failure. It should be populated with a 0 for success and 1 for failure |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Reserved                           | This field is reserved for future use                                                                                                  |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Data                               | This is the data read from the address                                                                                                 |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/writeformat.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/readresponseformat.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/readresponse2.jpg
