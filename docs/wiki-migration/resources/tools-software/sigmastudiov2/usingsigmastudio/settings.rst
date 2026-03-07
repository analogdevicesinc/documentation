:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`

SigmaStudio+ Settings
=====================

| This section provides the brief overview of SigmaStudio+ settings. Select '**Tools -> Settings**' from the main menu to navigate to the SigmaStudio+ settings page.
| The settings in this page are grouped under \**6 categories \*\*
| ===== Application =====

-  **Launch State (Maximized)** - Enable this to launch SigmaStudio+ application in maximized state.
-  **Display 'Help' During Startup** - Choose whether to display the 'Help' page during the application startup

Canvas
------

-  **Show Rulers** - Enable this to show rulers on the canvas. The below image shows the canvas when the option is enabled.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/settings4.png
   :align: center
   :width: 400px

-  **Enable Resize** - Enable this to support resizing the shapes on canvas.
-  **Enable Rotate** - Enable this to support rotating the shapes on canvas.
-  **Mouse Drag** - Select one of the canvas operations when mouse is dragged. "Drag to move canvas" - Mouse drag scrolls the canvas; "Drag to select items" - Mouse drag selects shapes. When either of the option is selected. use Ctrl+Drag to perform the other operation.

Scripting
---------

-  **Port Number** - Port number to be used while connecting from a scripting client. Use different port numbers when multiple instances of SigmaStudio+ are running on the same PC.
-  **Configure Port** - Click to reconfigure using the new port number

In this section the port number can be specified which will be used by the scripting tool and also provides an option to configure the port.

Processor
---------

-  **Target Verification** - When enabled, the target execution will be verified after download. Error notification will be displayed if the verification fails. Verification is typically performed by reading the status register or one of the performance parameters from the target.

Export
------

-  **Auto Export System Files** - When enabled, system files are automatically exported after compilation.
-  **Naming Convention** - Determines the naming convention of the exported files. The name will be based on the Export name (given by user at the time of exporting) and 'Processor Name' and/or 'Core Name' and/or 'Schematic Name'.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/settings_export.png
   :align: center
   :width: 600px

Custom Platforms
----------------

| This section provides an option to specify the Custom Platforms folder location. SigmaStudio+ uses this location to load newly defined platforms and list them in the toolbox.
| |image1|
| Refer to :doc:`Defining new Platforms </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/defineplatforms>` for more details on defining new platforms.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/settings6.png
   :width: 500px
