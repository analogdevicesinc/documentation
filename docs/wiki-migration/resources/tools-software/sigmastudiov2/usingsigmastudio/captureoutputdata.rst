:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`

Capture Output Data
===================

| The Capture Window shows, in real time, the data SigmaStudio is sending to the hardware. This includes data sent during compile/link/download, register read/write operations, and changes to schematic block controls. The following example provides an explanation of the data displayed in the capture window.
| **Output Capture Example :**
| This example uses the SHARC XI Core and the sample schematic shown at the right: utilizing a White-Noise Source, Medium Size EQ Filter (single precision), and Output block.
| |image1|
| Display the Capture Window by selecting View - Capture Window in the application's main menu or by clicking the button on the Side toolbar. Select the Schematic tab and compile/link/download the project. The compiled program data is downloaded to the hardware and displayed in the Capture Window.
| |image2|
| \* **Mode** column denotes whether an entry represents a read or write message and whether or not writing utilizes Safeload. Mode is also represented by different text colors.

-  **Name** is the UID of the schematic block sending a message.
-  **Parameter Name** represents the name of the algorithms variable, register name, or memory location depending on the message type.
-  **Address** is the target hardware address.
-  **Value** displays the floating point representation of the Data column.
-  **Data** is the raw hexadecimal byte values written to the hardware.
-  **Bytes** shows the total number of bytes written or read.
-  **Time** is the time stamp which indicates the time at which the corresponding packet was sent to the target
-  **Sender** displays the destination of the data packets

| 
| At this point you can click Clear All Output Data button to empty the capture window. Now try moving the EQ slider to see that as the values are changed they are sent to the DSP.
| |image3|
| \* Cell Name - Same name as appears on the visual block in the SigmaStudio schematic tab.

-  Parameter Name - Describes the algorithm, IC type, number of inputs, and for this example the filter coefficient.
-  Parameter Address - The address where data are being sent.
-  Parameter Value - The decimal equivalent value for filter coefficient.
-  Parameter Data - 4-byte hex representation of the filter coefficient. The DSP takes data in 5.23 format, 5 bits to the left of the decimal point and 23 bits to the right. The hex values listed here are the 4 bytes necessary to store the 28 bits. Only 28 bits of the 32 available are used, so the 4 most significant bits of the first hex value are sign-extended from the 4th bit.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/captureoutputdata.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/captureoutputdata_1.jpg
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/captureoutputdata_2.jpg
   :width: 800px
