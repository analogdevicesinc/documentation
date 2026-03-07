Running a Stand-alone Application on the SHARC Audio Module
===========================================================

After using CCES to debug and finalize an application, it can be programmed to flash so that it can run stand-alone. The SHARC Audio Module Bare Metal SDK makes this process easy.

-  Browse to where the BM SDK was installed.
-  Now browse to ..\\extras\\flash-programmer.
-  Here you will see 2 .bat files that are used to easily program flash as well as a few other folders.

   -  prog_SAM_flash_ice1000.bat
   -  prog_SAM_flash_ice2000.bat

-  Place the 3 core applications that were created in the Input_DXE_Files folder.

.. note::

   For this exercise the application was named my_test_app

   
   -  Core 0: my_test_app_Core0
   -  Core 1: my_test_app_Core1.dxe
   -  Core 2: my_test_app_Core2.dxe
   


-  In a text editor, open the .bat file with the name that matches the emulator being used(ice1000 or ice2000).
-  Be sure that CCES_HOME is pointing to the CCES installation that is on the PC being used, save the changes.
-  Open a command prompt to ..\\SAM_BareMetal_SDK-Rel2.1.0\\extras\\flash-programmer.
-  Type **prog_SAM_flash_ice1000.bat <app name with no extention>**.
-  In the case of our app the command line would be: **prog_SAM_flash_ice1000.bat my_test_app**.
-  This will not only create the ldr file but also program it to flash.
