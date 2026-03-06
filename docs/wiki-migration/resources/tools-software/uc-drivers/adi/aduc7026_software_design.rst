ADuC7026 Software Design
========================

This section presents the steps for developing a software application that will run on the **ADuC7026 Eval Board** for controlling and monitoring the operation of the ADI part.

-  Run the **Keil uVision 4** integrated development environment.

-  Select *Create a new project* option (*Project – New uVision Project…*). A window will appear and will ask to save the project. Give it a name and press *Save* (for example “ADIEvalBoard.uvproj”). Another window will appear and will ask to select the device. Choose **ADuC7026**, from Analog Devices.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/adi/aduc7026_01.png
   :align: center

-  The message *“Copy ‘ADuC702x.s’ to Project Folder and Add File to Project?”* will appear. Select *No* not to include automatically the startup file “ADuC702x.s” into the project.

-  To configure the settings of this project, press *Alt + F7*.

-  In the “Output” panel select *“Create HEX File”*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/adi/aduc7026_02.png
   :align: center

-  In the “Linker” panel check *“Use Memory Layout from Target Dialog”*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/adi/aduc7026_03.png
   :align: center

-  Copy the files extracted from the zip file into the project’s directory.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/adi/aduc7026_04.png
   :align: center

-  The new files have to be included into the project. To add the files to the project right click on the “Source Group 1” folder in the “Project Workspace” and select //Add Files to Group ‘Source Group 1’… //. Choose *“All files”* type, select all new files, click *Add* and then *Close*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/adi/aduc7026_05.png
   :align: center

-  Now, the project is ready to be compiled and downloaded on the board. Press the *F7* key to compile it.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/adi/aduc7026_06.png
   :align: center

-  The HEX file can be downloaded into the on-chip Flash/EE program memory with the **Windows Serial Downloader for ARM** application (*ARMWSD*).
