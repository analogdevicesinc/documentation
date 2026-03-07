Programming Bare Metal Framework to Flash
=========================================

This section should be followed once your application is working as expected and have been fully verified within CrossCore Embedded Studio.

.. important::

   For more in depth knowledge on this subject it is recommended to go through the CCES Getting Started section on :doc:`Creating a Bootable Application </wiki-migration/resources/tools-software/crosscore/cces/getting-started/app>`\


Windows Batch Files
-------------------

2 Windows Batch files have been provided with the Bare Metal SDK install and can be found at ..\\SAM_BareMetal_SDK-Rel2.1.0\\extras\\flash-programmer. These batch files will aid in the process of getting the finalized application programmed to flash.

Open the appropriate batch file in a text editor for the emulator(ICE-1000 or ICE-2000) being used and be sure the CCES_HOME path is set according to the version of CCES under use. Save the changes.

Programming Flash
-----------------

This procedure will use the application name of **my_app** for the purpose of explaining the process of programming flash.

-  Place **my_app_Core0**, **my_app_Core1.dxe**, and **my_app_Core2.dxe** into the **Input_DXE_Files** folder
-  Open a *Windows Command Prompt*
-  Change directories to ..\\SAM_BareMetal_SDK-Rel2.1.0\\extras\\flash-programmer
-  On the command line type **prog_SAM_flash_ice1000.bat** *my_app* (do NOT add the core extension)
-  Execute the batch file to program flash on the SHARC Audio Module Main Board.

.. important::

   A binary file will be created and then programmed to flash. The resulting binary file can be found in Output_LDR_Files


--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#porting-to-new-hardware-tutorial
   :alt: Porting framework to different HW#.|Bare Metal Framework#troubleshooting|Trouble Shooting
