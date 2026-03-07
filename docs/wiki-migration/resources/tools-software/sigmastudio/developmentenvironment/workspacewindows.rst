Workspace Windows
=================

| :doc:`Click here to return to the Development Environment page </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment>`
| The Workspace windows display important project information including available resources, compiler output, and hardware communication. To show or hide the workspace windows select them in the application's main View menu or by clicking the buttons on the Standard Toolbar.

-  DSP Resources
-  Output
-  Capture Window
-  Sequence Window

Each window is described below:

--------------

DSP Resources:
--------------

| The DSP Resources window lets you view the resources available in your design, depending on your project complexity. You are able to monitor program RAM, parameter RAM, and other hardware-specific resources. By default this window is docked on the right side of the program window.
| |workspacewinpic1.png|
| --------------------------------------------------------------------------------

Output:
-------

| The Output window is a quick way to view the files generated upon linking, compiling, and other actions in the Schematic workspace. By default this window is docked on the right side of the program window. Note, you can also find this information by locating the project's output folder and reading the compiler output files. For more information about those files, see Compile/Downloading Your Project.
| |workspacewinpic2.png|
|

.. tip::

   Note: The DSP Resources and Output windows are not fully functional for all SigmaDSP IC types.


--------------

Capture Window:
---------------

| The capture window lets you see, in real time, the exact data that SigmaStudio is sending to the hardware. This window is only active when a USB communication channel is inserted in the project and the project has been compiled and downloaded. This window is un-docked/floating by default.
| The window is empty when it opens initially, but after you press Link-Compile-Download you will see the data that is downloaded to the board: coefficients, parameter addresses, and parameter data. Whenever you make adjustments to sliders or control in a compiled and downloaded schematic, you can see the data that is sent.
| |workspacewinpic3.png|
|

.. tip::

   Watch this `video tutorial about the Capture Window <http://videos.analog.com/video/applications/automotive/756712926001/SigmaStudio-C2-Capture-Window/>`_.


See Capture Output Data for a detailed explanation of the data displayed in the Capture Window.

--------------

Parameters Window:
------------------

.. note::

   Under Construction


.. tip::

   Watch this `video tutorial about the Parameters Window <http://videos.analog.com/video/756712925001/SigmaStudio-C3-Parameters-Window/>`_.


--------------

Sequence Window:
----------------

| Use the sequence window to define a custom sequence of data read/write operations between SigmaStudio and a target hardware device connected via USB. Commands can be dragged from the capture window or created manually. Sequences are independent of the SigmaStudio project file and can be saved and recalled to files.
| The sequence window is part of the Capture window, to view the sequence window open the capture window and click the arrow button in the upper right corner.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/sequencewnd.png

| |image1|

Define a sequence
~~~~~~~~~~~~~~~~~

1. Drag and drop data directly from the capture window.


|image2|

| 2. Right-click in the sequence window to define an operation manually. |image3|

Execute a sequence
~~~~~~~~~~~~~~~~~~

Click the download Mode to Hardware button to execute sequence commands.


|image4|

.. |workspacewinpic1.png| image:: https://wiki.analog.com/_media/workspacewinpic1.png
.. |workspacewinpic2.png| image:: https://wiki.analog.com/_media/workspacewinpic2.png
.. |workspacewinpic3.png| image:: https://wiki.analog.com/_media/workspacewinpic3.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/sequencewnd2.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/sequencedd.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/sequencemenu.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/developmentenvironment/sequencedownload.png
