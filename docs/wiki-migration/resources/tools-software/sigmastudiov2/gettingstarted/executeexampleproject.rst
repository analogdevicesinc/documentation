:doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted>`

Execute Example Project
=======================

Download Example Projects
-------------------------

| Example projects can be downloaded from :doc:`Tutorials and Examples </wiki-migration/resources/tools-software/sigmastudiov2/tutorials>`
| ===== Load and Execute Target Application (ADSP-214xx / ADSP-215xx / ADSP-SC5xx) ===== Target application must be loaded on to the evaluation platform before executing the example applications on ADSP-214xx, ADSP-215xx and ADSP-SC5xx platforms. There are two options to load the application on the target platform.
| `flash_the_loader_file <https://wiki.analog.com/flash_the_loader_file>`__
| The first option is to program the flash on the target platform with the application loader(.ldr) file. Once flashed, application will be booted from the flash every time the target platform is reset.
|

.. note::

   Target framework and application don't support redownload of schematic once downloaded on to the running target application in case if there are any changes to FW configuration, block size change, FS change and mem map changes in the schematic or when adding or deleting modules that affect memory mapping during compilation. The target application should rerun by resetting the target platform to download the schematic again.


| `load_executable_using_cces <https://wiki.analog.com/load_executable_using_cces>`__
| Second option is to use CrossCore Embedded Studio and load the application DXEs for each of the cores through a debug session using debug agent (ICE-1000/ICE-2000). This process should be repeated after every target reset for running the target application.
|

.. note::

   Target framework and application don't support redownload of schematic once downloaded on to the running target application in case if there are any changes to FW configuration, block size change, FS change and mem map changes in the schematic or when adding or deleting modules that affect memory mapping during compilation. The target application should rerun by resetting the target platform to download the schematic again.


   | =====Download and Tune using SigmaStudio+=====

-  Double click on the downloaded project file to open it in SigmaStudio+.
-  Click 'Link-Compile-Download' from the Action menu to compile and download the project on to the target
-  Navigate to the schematic canvas by clicking on the schematic from the Schematic panel
-  Change the graphical controls

|

| Refer to :doc:`Development Environment </wiki-migration/resources/tools-software/sigmastudiov2/developmentenvironment>` for more details on the SigmaStudio+ development environment.

Refer to :doc:`Using SigmaStudio+ </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>` for more details on the usage of SigmaStudio+.


| Refer to :doc:`Target Integration </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration>` for details on modifying, rebuilding and debugging the target application that runs on ADSP-214xx, ADSP-215xx or ADSP-SC5xx.
|

.. note::

   Target framework and application is for ADSP-214xx, ADSP-215xx and ADSP-SC5xx

