TCP/IP Channels (ADAU144x / ADAU145x / ADAU146x)
================================================

| :doc:`Click here to return to the Using SigmaStudio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| The TCP/IP channel can be used to connect with the SigmaDSP in case the SigmaDSP is present at a different location and cannot be physically connected the the PC that is running SigmaStudio. SigmaStudio communicates with a server connected to the SigmaDSP using TCP/IP.

The TCPIP channel is present under the Communication Channels tree as shown in the figure below:


|image1|

Drag and Drop the channel onto the configuration tab and connect it to the IC. An option to open a TCPIP form will appear in the context menu as shown below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/context_menu.jpg
   :align: center

A TCPIP from is launched when Show TCPIP form is clicked. The form is as shown in the figure below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/tcpip_form.jpg
   :align: center

Enter the IP address and the port number on which the server connected to SigmaDSP is listening on in the TCPIP form. Click on Open connection to open the connection with the server.

Once the server is connected, SigmaStudio is free to send and receive data to and from the server.

Write Data Format
-----------------

SigmaStudio sends the code and parameter information to the server connected to SigmaDSP in the following format:

| |image2|
| ====Fields ====

+----------------------------+------------------------------------------------------------------------------------------------+
| Field                      | Description                                                                                    |
+============================+================================================================================================+
| Control                    | This is the control bit that is used to indicate that it is a write packet. Its value is 0x09  |
+----------------------------+------------------------------------------------------------------------------------------------+
| Block / safeload write bit | This field indicates whether the write packet is a block write or a safeload write             |
+----------------------------+------------------------------------------------------------------------------------------------+
| Channel number             | This indicates the channel number                                                              |
+----------------------------+------------------------------------------------------------------------------------------------+
| Total length               | This indicates the total length of the write packet. It is 4 bytes long                        |
+----------------------------+------------------------------------------------------------------------------------------------+
| Chip address               | This is the address of the chip to which the data has to be written                            |
+----------------------------+------------------------------------------------------------------------------------------------+
| Data Length                | This is the length of the data. This is 4 bytes long                                           |
+----------------------------+------------------------------------------------------------------------------------------------+
| Address                    | This is the address of the module whose data is being written to the DSP. This is 2 bytes long |
+----------------------------+------------------------------------------------------------------------------------------------+
| Data                       | This is the data to be written                                                                 |
+----------------------------+------------------------------------------------------------------------------------------------+

Readback from the DSP
---------------------

In order to achieve readback, SigmaStudio send a read request. The server connected to SigmaDSP must respond to the read request with a read response.

Read Request format
~~~~~~~~~~~~~~~~~~~

The read request format is as shown

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/readresponseformat.jpg
   :align: center

Fields
^^^^^^

+--------------+-----------------------------------------------------------------------------------------------+
| Field        | Description                                                                                   |
+==============+===============================================================================================+
| Control      | This is the control bit that is used to indicate that it is a read packet. Its value is 0x0A  |
+--------------+-----------------------------------------------------------------------------------------------+
| Total length | This indicates the total length of the read packet. It is 4 bytes long                        |
+--------------+-----------------------------------------------------------------------------------------------+
| Chip address | This is the address of the chip for which the data has to be read from                        |
+--------------+-----------------------------------------------------------------------------------------------+
| Data Length  | This is the length of the data to read. This is 4 bytes long                                  |
+--------------+-----------------------------------------------------------------------------------------------+
| Address      | This is the address of the module whose data is being read from the DSP. This is 2 bytes long |
+--------------+-----------------------------------------------------------------------------------------------+
| Reserved     | There are two fields reserved for future use.                                                 |
+--------------+-----------------------------------------------------------------------------------------------+

Read Response Format
~~~~~~~~~~~~~~~~~~~~

The server connected to SigmaDSP has to respond to the read request in the following format:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/readresponse2.jpg
   :align: center

| 
| ===Fields ===

+-------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Field             | Description                                                                                                                            |
+===================+========================================================================================================================================+
| Control           | This is the control bit that is used to indicate that it is a read response packet. Its value is 0x0B                                  |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Total length      | This indicates the total length of the read response packet. It is 4 bytes long                                                        |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Chip address      | This is the address of the chip to which the data has been read from                                                                   |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Data Length       | This is the length of the data. This is 4 bytes long                                                                                   |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Address           | This is the address of the module whose data has been read from the DSP. This is 2 bytes long                                          |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Success / Failure | This byte indicates whether the read operation was a success or failure. It should be populated with a 0 for success and 1 for failure |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Reserved          | This field is reserved for future use                                                                                                  |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Data              | This is the data read from the address                                                                                                 |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/tcpip_146x_support.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/writeformat.jpg
