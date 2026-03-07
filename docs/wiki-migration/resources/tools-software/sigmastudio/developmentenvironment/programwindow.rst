Program Window
==============

| :doc:`Click here to return to the Development Environment page </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment>`
| When you start SigmaStudio, you will see the main Program Window. To get started, create a New Project by selecting File - New Project from the main menu or by pressing the new project button on the toolbar, or open an existing project file.
| The following screen will appear for a new project:
| |programpic1.png|
| The Program Window contains the main menu, toolbars, and the design workspace. The default design window is the Hardware Configuration tab and its toolbox to the left. This workspace lets you choose which DSP or IC to use.
| SigmaStudio is an MDI application (meaning more than one project file can be open at a time), but only a single instance of the SigmaStudio application can be running at any time. To toggle between open projects, select **Window** in the application main menu or press **ALT + TAB**.

.. tip::

   Note: You must select a "Processor" and insert it into the Hardware Configuration tab before you begin a design. See the Hardware Configuration Tab topic for more information.


Project Files
-------------

SigmaStudio projects are stored in files with a .dspproj extension. These files can be stored anywhere on the hard drive as well as removable or network media. In addition to project files, folders are automatically created for the compiled output of a project and for a projects settings. For more information see the settings topic and the Link/Compile/Download topic.

Arranging The Workspace
-----------------------

It is possible to modify the workspace configuration to best meet your needs.

-  Workspace windows can be docked around the perimeter of the main window, grouped together, or undocked/floated and moved anywhere on the screen. To toggle the docked state of a window, double-click the window's title bar or right click in the title bar. When a window is undocked/floating, dragging the window within the main program will display an outline of the location where it will be docked with dropped. If you want to position a floating window within the workspace without docking, click and hold the left mouse button in the title bar and then hold down the CTRL key.
-  Windows can be configured to automatically hide or "shrink" to the perimeter of the application until needed. Press the auto-hide button to toggle this mode.
-  Each pane can be resized using the splitters around the perimeter of each pane.
-  Windows can be closed by clicking the close button displayed in the upper right corner, or by right-clicking the title bar and selecting "Hide". To display a closed window, select in the in the View menu or use the buttons in the Standard Toolbar.

.. tip::

   Note: Workspace settings are stored in the "ToolbarLayout.dat" file which is located in the application's directory. Close SigmaStudio and delete this file and restart to restore the default layout.


.. |programpic1.png| image:: https://wiki.analog.com/_media/programpic1.png
