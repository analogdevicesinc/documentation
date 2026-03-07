Hierarchy Boards
================

| :doc:`Click here to return to the Using Sigma Studio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| For complex system designs, it can become difficult to manage a large number schematic block's in a single design window and it is desirable to have additional schematic workspace and the ability to organize design components. Schematic Hierarchy Boards allows you to create multiple layers within the schematic design window expanding the schematic workspace.

-  Create Hierarchy Boards
-  Hide, Freeze, and Navigation
-  Hierarchy Board Files

| A schematic Hierarchy Board consists of a :doc:`Hierarchy Board Block </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/hierarchyboard>` and an associated schematic tab (or layer), located at the bottom of the schematic window. Hierarchy boards support Copy/Paste, schematic settings, and Undo operations. All projects include the Main tab by default. The **Main** hierarchy board is the root layer for any additional user defined Hierarchy boards and cannot be renamed.
| |hierarchypic1.png|

--------------

Create a Hierarchy Board:
-------------------------

| Select the Schematic Design category in the Tree ToolBox window (or the System Category in the ToolBox), and drag-and-drop a **Hierarchy Board** block into the schematic workspace.
| |hierarchypic2.png|
| Along with the hierarchy board block, a hierarchy tab is created, located at the bottom of the Schematic design window. The default name is *Board1* and the corresponding tab has the same name as the board block.

|

.. hint::

   Note: It is possible to create nested hierarchy boards (a hierarchy board with-in another hierarchy board's tab). To create a nested board, first select a hierarchy tab at the bottom of the Schematic window, then drag-and-drop a hierarchy board block. If you hover the mouse button over a board tab, the tool-tip will display the "path" of the board (the location of the board block relative to Main). This is helpful when several board's have the same name, which is common when using board files.


   |hierarchypic3.png|

See the :doc:`Hierarchy Board </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/hierarchyboard>`, :doc:`Hierarchy Input </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/hierarchyinput>`, and :doc:`Hierarchy Output </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/hierarchyoutput>` topics for more information.

--------------

Hide, Freeze, and Navigation
----------------------------

To locate the hierarchy board block for a particular hierarchy tab, select the hierarchy tab at the bottom of the Schematic window, then double click the tab. This will display the design layer that contains the associated Hierarchy board block. Similarly, you can double click a hierarchy board block to display its design layer.

| Right-click the hierarchy block to display the block's context menu. This menu includes commands for view the board layer, hiding the board's tab, and freezing the board design.
| |hierarchypic4.png|

--------------

Hierarchy Board Files
---------------------

The entire contents of a Hierarchy Board layer (inputs, outputs, blocks, wires, and nested hierarchy boards) along with the board's Hide/Freeze state can be saved to a Hierarchy Board File (\*.dspbrd). This allows you to create reusable design components and import then into new SigmaStudio projects.

**To Create a Board File:**

| Right-Click on the hierarchy board block and select **File - Save Board** from the pop-up menu. SigmaStudio board files use the \*.dspbrd file extension.
| |hierarchypic5.png|

**To Load a Board File:**

-  Insert a new hierarchy board block into the Schematic window.
-  Right-Click the hierarchy board block and select **File - Load Board**... from the menu.
-  Navigate to a previously saved board file (\*.dspbrd) and press **Open**.

| |hierarchypic6.png|
| The loaded board name is changed to match the saved board name, and all the blocks contained in the hierarchy board's layer are loaded into a new tab. In the example below, the Mixer block was saved to a file and then loaded into a new hierarchy board block, Mixer_2.
| |hierarchypic7.png|
| Note, the *Mixer* and *Mixer_2* schematic layers are identical.
| |hierarchypic8.png|

.. |hierarchypic1.png| image:: https://wiki.analog.com/_media/hierarchypic1.png
.. |hierarchypic2.png| image:: https://wiki.analog.com/_media/hierarchypic2.png
.. |hierarchypic3.png| image:: https://wiki.analog.com/_media/hierarchypic3.png
.. |hierarchypic4.png| image:: https://wiki.analog.com/_media/hierarchypic4.png
.. |hierarchypic5.png| image:: https://wiki.analog.com/_media/hierarchypic5.png
.. |hierarchypic6.png| image:: https://wiki.analog.com/_media/hierarchypic6.png
.. |hierarchypic7.png| image:: https://wiki.analog.com/_media/hierarchypic7.png
.. |hierarchypic8.png| image:: https://wiki.analog.com/_media/hierarchypic8.png
