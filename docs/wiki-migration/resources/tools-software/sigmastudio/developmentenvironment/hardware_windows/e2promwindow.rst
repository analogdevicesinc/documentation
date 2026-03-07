E2Prom Read/Write Window
========================

| :doc:`Click here to return to the Hardware Windows page </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows>`
| The E2Prom Read/Write window allows you to read and write program data to an E2Prom IC. This tool can be used with your own hardware systems or with the E2Prom available on some SigmaDSP evaluation boards. It also supports saving and loading the program data to files.

--------------

E2Prom Configruation:
---------------------

-  To use the E2Prom, insert the E2Prom IC block into :doc:`Hardware Configuration Tab </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/hardwareconfigurationtab>` and connect it to the USB communication channel block as show in the figure below.

   -


   |e2prompic1.png|

-  Compile/Link/Download the project and verify that "Ready - Download" is displayed on the status bar.
-  To download the compiled project's program data to the E2Prom, Right-Click on the DSP block in the Hardware Configuration window and select*\* Write Latest Compilation to E2PROM*\* from the menu. Note if your E2Prom's size differs from the default 16kB size, you should first adjust the size setting in the Read/Write window (see below) before writing .

   -


   |e2prompic2.png|

-  If your hardware is setup correctly, you should see the Download E2Prom progress dialog.

   -


   |e2prompic3.png|

--------------

Using the E2Prom Read/Write window:
-----------------------------------

| To open the E2Prom Read/Write window, Click the WinE2PromLoader tab at the bottom of the Hardware Configuration window or Right-click on the E2Prom IC block and select Read/Write Window from the menu.
| |e2prompic5.png|

**Settings:**

+------------------+--------------------------------------------------------------------------------------------+
| Address Visible  | Check this box to see the memory address values in the right-hand display.                 |
+------------------+--------------------------------------------------------------------------------------------+
| byte(s) per line | Adjusts the number of bytes shown on each line of the right-hand display.                  |
+------------------+--------------------------------------------------------------------------------------------+
| Page Size        | Sets the page size for reading/writing to the E2Prom.                                      |
+------------------+--------------------------------------------------------------------------------------------+
| Mem Size         | The size of the E2Prom memory, verify this setting **before** attempting to read or write. |
+------------------+--------------------------------------------------------------------------------------------+
| Mem Usage        | Displays how much memory is used by the most recently downloaded/uploaded program.         |
+------------------+--------------------------------------------------------------------------------------------+

**Buttons:**

+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Download File to E2Prom | Downloads a previously uploaded program file to the E2Prom hardware (note this will overwrite the current E2Prom data). Click in the control at the top of the window to select a file prior to loading. |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Upload E2Prom To File   | Save the current E2Prom data to the file. Click in the bottom control to select a save filename before pressing this button.                                                                             |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Clear E2Prom            | Write '0' to the entire E2Prom memory overwriting any program data previously downloaded.                                                                                                                |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Display File            | This button will show the program data of the selected download or upload file in the right-hand display.                                                                                                |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Read E2Prom to Display  | Reads the current E2Prom data and shows it in the right-hand display.                                                                                                                                    |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Write Display to E2Prom | Writes all the data bytes shows in the right-hand display to the E2Prom.                                                                                                                                 |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Values Display:** In additional to displaying the data, the right-hand values display allows you to edit the program data bytes directly. Value changes can be written to the E2Prom using the "Write Display to E2Prom" button.

.. |e2prompic1.png| image:: https://wiki.analog.com/_media/e2prompic1.png
.. |e2prompic2.png| image:: https://wiki.analog.com/_media/e2prompic2.png
.. |e2prompic3.png| image:: https://wiki.analog.com/_media/e2prompic3.png
.. |e2prompic5.png| image:: https://wiki.analog.com/_media/e2prompic5.png
