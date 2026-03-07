| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/developmentenvironment>`

Parameter Window
================

| The Parameter Window shows the data SigmaStudio+ is sending to the hardware for a given address. This includes data sent during compile/link/download, register read/write operations, and changes to schematic block controls. The update does not happen real-time unlike the Capture window. Refresh button at the top left corner updates the changed values as and when requested for. The following image shows the data displayed in the Parameter window.
| |image1|
| SS+ supports multiple schematics to co-exist in a single project. The first drop-down lets the user to choose the desired schematic whose parameters are to be displayed on the parameter window. Similarly, the DM0/DM1 drop-down option gets enabled if the processor has that feature. Display options lets the user to choose the columns that needs to be displayed on the window at any given point.
| Display the Parameter Window by selecting View - Parameter Window in the application's main menu or by clicking the button on the Side toolbar. Select the Schematic tab and compile/link/download the project. The compiled data is downloaded to the hardware and displayed in the Parameter Window as shown above.
| \* **Address** is the target hardware address.

-  **Hex Data** is the raw hexadecimal byte values written to the hardware.
-  **Data 8.24** shows the data in 8.24 format.
-  **Data 32.0** shows the data in 32.0 format.
-  **Parameter Name** represents the name of the algorithms variable, register name, or memory location depending on the message type.
-  **Module UID** is the UID of the schematic block sending a message.

| 
| ===Parameter Read=== Parameter read pop-up could be launched by clicking on the Param Read - button on the Parameter window. Currently, User can use 5 instances of this window to independently read 5 different parameter values together either in continuous or discrete format. Details of this is given below.
| |image2|
| \* Module - Same name as appears on the visual block in the SigmaStudio schematic tab.

-  Parameter Name - Indicates the parameter to be read from the given module/algorithm block.
-  Address Enable - The address where data are being read from. Enabled when the respective box is checked.
-  Parameter Length - Allows the user to choose the length of the parameter to be read.
-  Continuous Readback - Enables the user to readback a parameter continuously according to the given Readback period(ms).
-  Readback Period(ms) - Interval at which continuous readback happens.
-  Output to file - The readback parameter could be written onto a file using this option.
-  File Path (Browse button)- This gets enabled if the user chooses Output to File option.
-  Read - The button to trigger Read action. The read back value gets displayed in terms of byte array format in the text box.
-  Stop - This button allows the user to trigger stop-readback action.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/developmentenvironment/parameterwindow/parameterwindow.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/developmentenvironment/parameterwindow/paramwindow.png
   :width: 600px
