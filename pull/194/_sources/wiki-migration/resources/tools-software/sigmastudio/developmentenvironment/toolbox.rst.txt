Tree Toolbox and Toolbox Windows
================================

| :doc:`Click here to return to the Development Environment page </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment>`
| The Tree Toolbox and Toolbox windows contain the building blocks for constructing your design. For more information about the building blocks available in SigmaStudio and their usage, see the ToolBox topic.
| To show or hide the Toolbox windows select "Tree ToolBox" or "ToolBox" in the main application's View menu or by clicking the buttons on the Standard Toolbar. By default these windows are docked on the left side of the program window.
| |treetoolpic1.png|
| Select the Hardware Configuration tab to display Processor blocks (ICs and DSPs) and USB communication blocks. Selecting the Schematic tab will display system and DSP building blocks.

.. tip::

   Note: The "Tree ToolBox" and "ToolBox" windows offer the same functionality and building blocks, but present the data differently. While it is recommended that you first try the Tree Toolbox, as it is designed to simplify the design process, you should choose the toolbox window that best meets your needs and preferences.


--------------

Tree ToolBox
------------

| The Tree Toolbox window displays the available building blocks in a tree view. In the example below, the project contains is an ADAU1701 DSP named IC1. System blocks are arranged in a hierarchy of folders according to function and algorithm. Navigate the folders to find a desired algorithm block and drag and drop it into the schematic window.
| |treetoolpic2.png|
| --------------------------------------------------------------------------------

Toolbox
-------

| The Toolbox window is organized into a series or Tabs representing the different algorithm categories. Click a library topic to expand the list and see the blocks you can drop into your schematic. The available blocks depend on which IC(s) or DSP(s) are inserted in the Hardware Configuration tab.
| |treetoolpic3.png|
| Unlike the "Tree Toolbox", Toolbox blocks can represent more than one algorithm at a time (for example single or double precision filters) requiring an additional step of algorithm selection after dropping the block in the schematic. See the Adding and Growing Algorithms for more information.

.. |treetoolpic1.png| image:: https://wiki.analog.com/_media/treetoolpic1.png
.. |treetoolpic2.png| image:: https://wiki.analog.com/_media/treetoolpic2.png
.. |treetoolpic3.png| image:: https://wiki.analog.com/_media/treetoolpic3.png
