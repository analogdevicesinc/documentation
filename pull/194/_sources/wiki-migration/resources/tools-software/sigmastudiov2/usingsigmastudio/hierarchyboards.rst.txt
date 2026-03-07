:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`

Hierarchy Boards
================

For complex system designs, it can become difficult to manage a large number schematic block's in a single design window and it is desirable to have additional schematic workspace and the ability to organize design components. Schematic Hierarchy Boards allows you to create multiple layers within the schematic design window expanding the schematic workspace.

-  Create Hierarchy Boards
-  Create/Load Board files
-  Lock/Unlock Hierarchy Board

| A schematic Hierarchy Board consists of a Hierarchy Board Block and an associated schematic tab (or layer), that can be opened by double clicking on the hierarchy board or on double clicking the respective block in the modules list on the project window. Hierarchy boards support Copy/Paste, schematic settings, and Undo operations. All projects include the Main tab by default. The Main hierarchy board is the root layer for any additional user defined Hierarchy boards and cannot be renamed.
| |image1|
| ===Create a Hierarchy Board:===

| Select the Schematic Design category in the Tree ToolBox window (or the System Category in the ToolBox), and drag-and-drop a Hierarchy Board block into the schematic workspace.
| |image2|
| Along with the hierarchy board block, a hierarchy tab is created, that could be opened by simply double clicking on the block. The default name is Board_0 and the corresponding tab has the same name as the board block.
| Note: It is possible to create nested hierarchy boards (a hierarchy board with-in another hierarchy board's tab). To create a nested board, first open a hierarchy block tab by double clicking on that, then drag-and-drop a hierarchy board block. If you hover the mouse button over a board tab, the tool-tip will display the "path" of the board (the location of the board block relative to Main). This is helpful when several board's have the same name, which is common when using board files.

| 
| ===Hierarchy Board Files===
| The entire contents of a Hierarchy Board layer (inputs, outputs, blocks, wires, and nested hierarchy boards) along with the board's Lock/Unlock state can be saved to a Hierarchy Board File (\*.ssbrd). This allows you to create reusable design components and import then into new SigmaStudio projects.

To Create and Load Board Files:
-------------------------------

| Right-Click on the hierarchy board block and select Save Board from the pop-up menu. SigmaStudio board files use the \*.ssbrd file extension.
| |image3|
| To Load a board file,

-  Insert a new hierarchy board block into the Schematic window.
-  Right-Click the hierarchy board block and select File - Load Board... from the menu.
-  Navigate to a previously saved board file (\*.ssbrd) and press Open.

The loaded board will be name is changed to match the saved board name, and all the blocks contained in the hierarchy board's layer are loaded into a new tab.

To Lock or Unlock Boards:
-------------------------

| Right-Click on the hierarchy board block and select Lock Board from the context menu, and give a lock password or a key.
| |image4| |image5|
| This will encrypt the board contents for any user and user will not be able to view the contents inside the board. Even the project file would not show the contents of the locked hierarchy board once it is locked using a key.
| Similarly, to unlock the board, right-Click on the hierarchy board block and select Unlock Board from the context menu, and give the lock password or key associated with that board. This will result in decryption of the board contents and project file would start showing the contents of the given hierarchy board

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/hierarchyboardngss.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/hierarchyboardngss_1.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/hierarchyboardngss_2.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/hierarchyboardngss_3.jpg
   :width: 500px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/hierarchyboardngss_4.jpg
   :width: 200px
