FreeRTOS Add-In Generated Files
===============================

Project Structure
-----------------

The first time the FreeRTOS add-in is added to a users project, several folders and files will be generated into the project.

See the image below for an example of the Project Structure using the BF707 board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/freertos-addin-structure.png

--------------

CustomizableFreeRTOSSources
---------------------------

All of the files within this folder are generated when the add-in is added to a project, they will **NOT** be regenerated (if they already exist in the project), and the user is free to edit them as required.

This folder is **NOT** removed when the add-in is removed from the project, this is to protect any code modifications that have been made to the contained files.

Moving or renaming these files will result in one with the original name being regenerated.

This folder with containing files will be added under "project/src..."

-  **FreeRTOSConfigExtend.h** *(Extends the base FreeRTOSConfig.h, user can override macros defs in here)*
-  **FreeRTOSHooks.h** *Basic Setup for all of the relevant hook functions that can be used in FreeRTOS*
-  **FreeRTOSMemory.h** *Basic Setup for all of the relevant memory functions that can be used in FreeRTOS*
-  **FreeRTOSUserApplication.c** *(basic task implementation for user)*
-  **FreeRTOSUserApplication.h** *(prototype functions for main file)*

--------------

GeneratedSources
----------------

This folder will be generated when the add-in is added to a project. These files will be regenerated whenever the project is saved, so that they change according to the UI settings that the user has applied. The user should not in any circumstance edit these files manually, since any added code will be overwritten.

-  **FreeRTOSConfig.h** *(The FreeRTOS configuration file, generated via the system.svc options for FreeRTOS)*

--------------

FreeRTOS/Source
---------------

This folder, contains all of the FreeRTOS source files that are cloned from the Analog Devices port of FreeRTOS. These sources are relative to the processor that is being used by the project so that you only get the files that you need, this greatly improves the clone time for the project.

More information about the repository that is used to clone these files in is available the section :doc:`FreeRTOS Add-In GIT Sources </wiki-migration/resources/tools-software/freertos/freertos-addin/freertos-repo>`.
