This section presents the steps for developing a software application that will run on the **CED1Z** system and will be used for controlling and monitoring the operation of the ADI evaluation board.

Create a new project using the NIOS II Software Build Tools for Eclipse
=======================================================================

Launch the **Nios II SBT** from the **Start -> All Programs -> Altera -> Nios II EDS 11.0 -> Nios II 11.0 Software Build Tools for Eclipse (SBT)**.

.. tip::

   NOTE: Windows 7 users will need to right-click and select **Run as administrator**. Another method is to right-click and select **Properties** and click on the **Compatibility** tab and select the **Run This Program As An Administrator** checkbox, which will make this a permanent change.


1. Initialize Eclipse workspace
-------------------------------

-  When Eclipse first launches, a dialog box appears asking what directory it should use for its workspace. It is useful to have a separate Eclipse workspace associated with each hardware project that is created in SOPC Builder. Browse to the **ADIEvalBoard** directory and click **Make New Folder** to create a folder for the software project. Name the new folder “\ **eclipse_workspace**\ ”. After selecting the workspace directory, click **OK** and Eclipse will launch and the workbench will appear in the **Nios II** perspective.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/eclipseworkspace.png
   :alt: eclipseworkspace.png
   :align: center
   :width: 800px

2. Create a new software project in the SBT
-------------------------------------------

-  Select **File -> New -> Nios II Application and BSP from Template**.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image025.png
   :alt: image025.png
   :align: center
   :width: 600px

-  Click the **Browse** button in the **SOPC Information File Name** dialog box.
-  Select the **uC.sopcinfo** file located in the **ADIEvalBoard/FPGA** directory.
-  Set the name of the Application project to “\ **ADIEvalBoard**\ ”.
-  Select the **Blank Project** template under **Project template**.
-  Click the **Finish** button.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/eclipseblankproject.png
   :alt: eclipseblankproject.png
   :align: center
   :width: 600px

The tool will create two new software project directories. Each Nios II application has 2 project directories in the Eclipse workspace.

-  The application software project itself - this where the application lives.
-  The second is the **Board Support Package (BSP)** project associated with the main application software project. This project will build the system library drivers for the specific SOPC system. This project inherits the name from the main software project and appends “\ **\_bsp**\ ” to that.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipseprojects.png
   :alt: eclipseprojects.png
   :align: center
   :width: 300px

Since you chose the blank project template, there are no source files in the application project directory at this time. The BSP contains a directory of software drivers as well as a system.h header file, system initialization source code and other software infrastructure.

Configure the Board Support Package
===================================

-  Configure the board support package to specify the properties of this software system by using the **BSP Editor** tool. These properties include what interface should be used for *stdio* and *stderr* messages, the memory in which stack and heap should be allocated and whether an operating system or network stack should be included with this BSP.
-  Right click on the **ADIEvalBoard_bsp** project and select **Nios II -> BSP Editor…** from the right-click menu.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipsebspmenu.png
   :alt: eclipsebspmenu.png
   :align: center
   :width: 600px

The software project provided in this lab does not make use of an operating system. All *stdout*, *stdin* and *stderr* messages will be directed to the *jtag_uart*.

-  Select the **Common** settings view. In the **Common** settings view, change the following settings:

   -  Select the **jtag_uart_0** for *stdin*, *stdout* and *stderr* messages. Note that you have more than one choice.
   -  Select **none** for the *sys_clk_timer* and *timestamp_timer*.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/cedz/cedzmainsettings.png
   :alt: cedzmainsettings.png
   :align: center
   :width: 800px

The memory used by the design is should be changed from OnChip ram to SRAM for the .text region.

-  Select **Linker Script** tab.
-  Change .text region **Linker Region Name** from **onchip_mem** to **sram**.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/ced1zlinkersettings.png
   :alt: ced1zlinkersettings.png
   :align: center
   :width: 800px

-  Select **File -> Save** to save the board support package configuration to the *settings.bsp* file.
-  Click the **Generate** button to update the BSP.
-  When the generate has completed, select **File -> Exit** to close the BSP Editor.

Configure BSP Project Build Properties
======================================

In addition to the board support package settings configured using the **BSP Editor**, there are other compilation settings managed by the Eclipse environment such as compiler flags and optimization level.

-  Right click on the **ADIEvalBoard_bsp** software project and select **Properties** from the right-click menu.
-  On the left-hand menu, select **Nios II BSP Properties**.
-  During compilation, the code may have various levels of optimization which is a tradeoff between code size and performance. Change the **Optimization level** setting to **Level 2**
-  Since our software does not make use of C++, uncheck **Support C++**.
-  Check the **Reduced device drivers** option
-  Check the **Small C library** option
-  Press **Apply** and **OK** to regenerate the BSP and close the **Properties** window.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipsebspproperties.png
   :alt: eclipsebspproperties.png
   :align: center
   :width: 500px

Add source code to the project
==============================

In Windows Explorer locate the project directory which contains a directory called **Software**. In Windows Explorer select all the files and directories from the **Software** folder and drag and drop them into the Eclipse software project **ADIEvalBoard**.

-  Select all the files and folders and drag them over the **ADIEvalBoard** project in the SBT window and drop the files onto the project folder.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/eclipsecopyfiles.png
   :alt: eclipsecopyfiles.png
   :align: center
   :width: 800px

-  A dialog box will appear to select the desired operation. Select the option **Copy files and folders** and press **OK**.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image039.png
   :alt: image039.png
   :align: center

-  This should cause the source files to be physically copied into the file system location of the software project directory and register these source files within the Eclipse workspace so that they appear in the Project Explorer file listing.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/eclipseprojectfiles.png
   :alt: eclipseprojectfiles.png
   :align: center

Configure Application Project Build Properties
==============================================

Just as you configured the optimization level for the BSP project, you should set the optimization level for the application software project **ADIEvalBoard** as well.

-  Right click on the **ADIEvalBoard** software project and select **Properties** from the right-click menu.
-  On the left-hand menu, select the **Nios II Application Properties** tab
-  Change the **Optimization level** setting to **Level 2**.
-  Press **Apply** and **OK** to save the changes.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipseprojproperties.png
   :alt: eclipseprojproperties.png
   :align: center
   :width: 500px

Define Application Include Directories
======================================

Application code can be conveniently organized in a directory structure. This section shows how to define these paths in the makefile.

-  In the Eclipse environment double click on **my_include_paths.in** to open the file.
-  Click the **Ctrl** and **A** keys to select all the text. Click the **Ctrl** and **C** keys to copy all the text.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/eclipsemyinclude.png
   :alt: eclipsemyinclude.png
   :align: center
   :width: 500px

-  Double click on **Makefile** to open the file.
-  If you see the message shown here about resources being out of sync, right click on the **Makefile** and select **Refresh**.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipsemakefileoutofdate.png
   :alt: eclipsemakefileoutofdate.png
   :align: center

-  Select the line **APP_INCLUDE_DIRS :=**

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image049.png
   :alt: image049.png
   :align: center

-  Click the **Ctrl** and **V** keys to replace the selected line with the include paths.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/image051.png
   :alt: image051.png
   :align: center

-  Click the **Ctrl** and **S** keys to save the **Makefile**.

Compile, Download and Run the Software Project
==============================================

1. Build the Application and BSP Projects
-----------------------------------------

-  Right click the **ADIEvalBoard_bsp** software project and choose **Build Project** to build the board support package.
-  When that build completes, right click the **ADIEvalBoard** application software project and choose **Build Project** to build the Nios II application.

These 2 steps will compile and build the associated board support package, then the actual application software project itself. The result of the compilation process will be an *Executable and Linked Format (.elf)* file for the application, the **ADIEvalBoard.elf** file.

|eclipsebuildbsp.png| |eclipsebuildproj.png|

.. important::

   In case an error appears at compile time with a description like : **//section .rodata loaded at [00400164,00400477] overlaps section .text loaded at [00400164,004054d7] //** the enable_alt_load_copy_exceptions option must be unchecked from BSP Editor -> Main -> Settings -> Advanced-> hal.linker


2. Verify the Board Connection
------------------------------

The **CED1Z** hardware is designed with a *System ID* peripheral. This peripheral is assigned a unique value based on when the hardware design was last modified in the SOPC Builder tool. SOPC Builder also places this information in the *.sopcinfo* hardware description file. The BSP is built based on the information in the *.sopcinfo* file.

-  Select the **ADIEvalBoard** application software project.
-  Select **Run -> Run Configurations…**
-  Select the **Nios II Hardware** configuration type.
-  Press the **New** button to create a new configuration.
-  Change the configuration name to **CED1Z** and click **Apply**.
-  On the **Target Connection** tab, press the **Refresh Connections** button. You may need to expand the window or scroll to the right to see this button.
-  Select the **jtag_uart_0** as the **Byte Stream Device** for *stdio*.
-  Check the **Ignore mismatched system ID option**.
-  Check the **Ignore mismatched system timestamp option**.

|eclipserunconfig.png| |image059.png|

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/cedz/ignoreid.png
   :alt: ignoreid.png
   :align: center
   :width: 800px

3. Run the Software Project on the Target
-----------------------------------------

To run the software project on the Nios II processor:

-  Before running the the software project, the FPGA located on the CED1Z must be programmed with the Nios II system image. To program the FPGA run the **ADIEvalBoard/FPGA/program_fpga.bat** script.
-  Press the **Run** button in the **Run Configurations** window. This will re-build the software project to create an up–to-date executable and then download the code into memory on the **CED1Z** hardware. The debugger resets the Nios II processor, and it executes the downloaded code. Note that the code is verified in memory before it is executed

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/cedz/image063.png
   :alt: image063.png
   :align: center
   :width: 500px

.. hint::

   The code size and start address might be different than the ones displayed in the above screenshot.


.. |eclipsebuildbsp.png| image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipsebuildbsp.png
   :width: 400px
.. |eclipsebuildproj.png| image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipsebuildproj.png
   :width: 400px
.. |eclipserunconfig.png| image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipserunconfig.png
   :width: 400px
.. |image059.png| image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image059.png
   :width: 400px
