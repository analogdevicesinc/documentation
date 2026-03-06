| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/developmentenvironment>`

Sequence Window
===============

| |image1|
| The Sequence window in SigmaStudio+ allows the users to define custom sequence of data read/write actions between SigmaStudio+ and the hardware device connected via USB. User can either send commands from the capture window to sequence window or create them manually. These sequences are separate from user's SigmaStudio+ project and can be saved for later use.
| By default, the Sequence window is docked at the bottom. Users can create a distinct packet, specifying the address where the data packet should be written and the protocol to be used (typically SPI or I2C). The left tab in the Sequence window represents a sequence mode or group, and users can rename it to organize their sequences. Once the sequence is set up, clicking the download button in the Sequence window will send the packet to the target device.
| Following options are present on the sequence window. Right clicking in the sequence window opens a context menu with options similar to the utility buttons. The description of each button is given below:
| \* **New Sequence** - Clears all the content of the current sequence tab and creates a fresh sequence file

-  **Open Sequence File** - Opens the selected sequence file of xml format
-  **Save Sequence File** - Saves the contents of the sequence window modes as an xml file
-  **Add Mode** - Adds a new sequence mode (tab). Each mode contains a sequence of read/write/delay packs which can be downloaded to the target
-  **Remove Mode** - Removes the selected sequence mode (tab) from the sequence window
-  **Import Mode** - Imports a specific mode of a sequence xml file into the selected mode (tab)
-  **Export Mode** - Exports a selected mode (tab) in the sequence window as a separate file
-  **Add Command** - Adds a new read/write/delay pack to the selected sequence mode
-  **Cut Command** - Cuts a read/write/delay pack and stores it onto the sequence window clipboard allowing it to be pasted to any mode in the sequence tab
-  **Copy Command** - Copies selected read/write/delay packs and stores it onto the sequence window clipboard allowing it to be pasted to any mode in the sequence window
-  **Paste** - Pastes the packs present in the clipboard to the sequence mode selected
-  **Export** - Exports the contents of the sequence window into .c and .h files for standalone mode of operation
-  **Download** - downloads the entire sequence file or the selected mode (tab) to the target connected in the system tab. This choice of type of download is provided in the Download combobox.
-  **Move Up** - Reorders the sequence entry or tab up the list. The choice of type of sequence entry or mode is decided by the Reorder combobox.
-  **Move Down** - Reorders the sequence entry or tab down the list. The choice of type of sequence entry or mode is decided by the Reorder combobox.
-  **Address in hex** - ticking this checkbox displays the device address and register address in hex format. This also saves the addresses in hex in the export file.
-  **Force Download** - When the sequence download aborts midway due to an error, this flag can be used to push through the error and download the entire sequence list. The individual error can be seen in the capture window.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/developmentenvironment/sequencewindow/sequencewindow.png
