This section presents the steps for developing a software application that will run on the **Renesas Demo Kit for RX62N** for controlling and monitoring the operation of the ADI part.

-  Run the **High-performance Embedded Workshop** integrated development environment.
-  A window will appear asking to create or open project workspace. Choose “Create a new project workspace” option and press *OK*.
-  From “\ *Project Types*\ ” option select “\ *Application*\ ”, name the Workspace and the Project “\ *ADIEvalBoard*\ ”, select the “\ *RX*\ ” CPU family and “\ *Renesas RX Standard*\ ” tool chain. Press *OK*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rx62n_01.png
   :align: center

-  A few windows will appear asking to configure the project:

   -  In the "*Select Target CPU*" window, select “\ *RX600*\ ” CPU series, “\ *RX62N*\ ” CPU Type and press *Next*.
   -  In the “\ *Option Setting*\ ” windows keep default settings and press *Next*.
   -  In the “\ *Setting the Content of Files to be generated*\ ” window select "*None*" for the "*Generate main() Function*" option and press *Next*.
   -  In the “\ *Setting the Standard Library*\ ” window press “Disable all” and then *Next*.
   -  In the “\ *Setting the Stack Area*\ ” window check the "*Use User Stack*" option and press *Next*.
   -  In the “\ *Setting the Vector*\ ” window keep default settings and press *Next*.
   -  In the “\ *Setting the Target System for Debugging*\ ” window choose “\ *RX600 Segger J-Link*\ ” target and press *Next*.
   -  In the “\ *Setting the Debugger Options*\ ” and “\ *Changing the Files Name to be created*\ ” windows keep default settings, press *Next* and *Finish*.

-  The workspace is created.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rx62n_02.png
   :align: center

-  The RPDL (Renesas Peripheral Driver Library) has to integrated in the project. Unzip the RPDL files (double-click on the file “\ *RPDL_RX62N.exe*\ ”). Navigate to where the RPDL files were unpacked and double-click on the “\ *Copy_RPDL_RX62N.bat*\ ” to start the copy process. Choose the LQFP package, type the full path where the project was created and after the files were copied, press any key to close the window.
-  The new source files have to be included in the project. Use the key sequence *Alt, P, A* to open the “\ *Add files to project ‘ADIEvalBoard’*\ ” window. Double click on the RPDL folder. From the “\ *Files of type*\ ” drop-down list, select “\ *C source file (\*.C)*\ ”. Select all of the files and press *Add*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rx62n_04.png
   :align: center

-  To avoid conflicts with standard project files remove the files “\ *intprg.c*\ ” and “\ *vecttbl.c*\ ” which are included in the project. Use the key sequence *Alt, P, R* to open the “\ *Remove Project Files*\ ” window. Select the files, click on Remove and press *OK*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rx62n_05.png
   :align: center

-  Next the new directory has to be included in the project. Use the key sequence *Alt, B, R* to open the “\ *RX Standard Toolchain*\ ” window. Select the C/C++ tab, select “\ *Show entries for: Include file directories*\ ” and press *Add*. Select “\ *Relative to: Project directory*\ ”, type “\ *RPDL*\ ” as sub-directory and press *OK*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rx62n_03.png
   :align: center

-  The library file path has to be added in the project. Select the Link/Library tab, select “\ *Show entries for: Library files*\ ” and press *Add*. Select “\ *Relative to: Project directory*\ ”, type “\ *RPDL\\RX62N_library*\ ” as file path and press *OK*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rx62n_06.png
   :align: center

-  Because the “\ *intprg.c*\ ” file was removed the “\ *PIntPrg*\ ” specified in option “\ *start*\ ” has to be removed. Change “\ *Category*\ ” to “\ *Section*\ ”. Press "*Edit*\ ”, select “\ *PIntPRG*\ ” and press “\ *Remove*\ ”. From this window the address of each section can be also modified. After all the changes are made press *OK* two times.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rx62n_07.png
   :align: center

-  At this point the files extracted from the zip file located in the “\ *Software Tools*\ ” section have to be added into the project. Copy all the files from the archive into the project folder.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rx62n_08.png
   :align: center

-  Now, the files have to be included in the project. Use the key sequence *Alt, P, A* to open the “\ *Add files to project ‘ADIEvalBoard’*\ ” window. Navigate into ADI folder. From the “\ *Files of type*\ ” drop-down list, select “\ *Project Files*\ ”. Select all the copied files and press *Add*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rx62n_09.png
   :align: center

-  Now, the project is ready to be built. Press *F7*. The message after the Build Process is finished has to be “\ *0 Errors, 0 Warnings*\ ”. To run the program on the board, you have to download the firmware into the microprocessor’s memory.
