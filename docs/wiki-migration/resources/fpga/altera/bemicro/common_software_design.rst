This section presents the steps for developing a software application that will run on the **BeMicroSDK** system and will be used for controlling and monitoring the operation of the ADI evaluation board.

Create a new project using the NIOS II Software Build Tools for Eclipse
=======================================================================

Launch the **Nios II SBT** from the **Start -> All Programs -> Altera 12.0sp2-> Nios II EDS 12.0sp2 -> Nios II 12.0sp2 Software Build Tools for Eclipse (SBT)**.

.. tip::

   NOTE: Windows 7 users will need to right-click and select **Run as administrator**. Another method is to right-click and select **Properties** and click on the **Compatibility** tab and select the **Run This Program As An Administrator** checkbox, which will make this a permanent change.


1. Initialize Eclipse workspace
-------------------------------

-  When Eclipse first launches, a dialog box appears asking what directory it should use for its workspace. It is useful to have a separate Eclipse workspace associated with each hardware project that is created in SOPC Builder. Browse to the **ADIEvalBoardLab** directory and click **Make New Folder** to create a folder for the software project. Name the new folder “\ **eclipse_workspace**\ ”. After selecting the workspace directory, click **OK** and Eclipse will launch and the workbench will appear in the **Nios II** perspective.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipseworkspace.png
   :alt: eclipseworkspace.png
   :align: center
   :width: 500px

2. Create a new software project in the SBT
-------------------------------------------

-  Select **File -> New -> Nios II Application and BSP from Template**.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image025.png
   :alt: image025.png
   :align: center
   :width: 400px

-  Click the **Browse** button in the **SOPC Information File Name** dialog box.
-  Select the **uC.sopcinfo** file located in the **ADIEvalBoardLab/FPGA** directory.
-  Set the name of the Application project to “\ **ADIEvalBoard**\ ”.
-  Select the **Blank Project** template under **Project template**.
-  Click the **Finish** button.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipseblankproject.png
   :alt: eclipseblankproject.png
   :align: center
   :width: 400px

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
   :width: 400px

The software project provided in this lab does not make use of an operating system. All *stdout*, *stdin* and *stderr* messages will be directed to the *jtag_uart*.

-  Select the **Common** settings view. In the **Common** settings view, change the following settings:

   -  Select the **jtag_uart** for *stdin*, *stdout* and *stderr* messages. Note that you have more than one choice.
   -  Select **none** for the *sys_clk_timer* and *timestamp_timer*.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image033.png
   :alt: image033.png
   :align: center
   :width: 500px

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

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipsecopysources.png
   :alt: eclipsecopysources.png
   :align: center
   :width: 600px

-  A dialog box will appear to select the desired operation. Select the option **Copy files and folders** and press **OK**.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/copyfileconfirmation.png
   :alt: copyfileconfirmation.png
   :align: center
   :width: 400px

-  This should cause the source files to be physically copied into the file system location of the software project directory and register these source files within the Eclipse workspace so that they appear in the Project Explorer file listing.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipseprojectstructure.png
   :alt: eclipseprojectstructure.png
   :align: center
   :width: 300px

Configure Application Project Build Properties
==============================================

Just as you configured the optimization level for the BSP project, you should set the optimization level for the application software project **ADIEvalBoard** as well.

-  Right click on the **ADIEvalBoard** software project and select **Properties** from the right-click menu.
-  On the left-hand menu, select the **Nios II Application Properties** tab
-  Change the **Optimization level** setting to **Level 2**.
-  Press **Apply** and **OK** to save the changes.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/eclipseprojectproperties12.png
   :alt: eclipseprojectproperties12.png
   :align: center
   :width: 500px

Compile, Download and Run the Software Project
==============================================

1. Build the Application and BSP Projects
-----------------------------------------

-  Right click the **ADIEvalBoard_bsp** software project and choose **Build Project** to build the board support package.
-  When that build completes, right click the **ADIEvalBoard** application software project and choose **Build Project** to build the Nios II application.

These 2 steps will compile and build the associated board support package, then the actual application software project itself. The result of the compilation process will be an *Executable and Linked Format (.elf)* file for the application, the **ADIEvalBoard.elf** file.

|eclipsebuildbsp.png| |eclipsebuildproj.png|

2. Verify the Board Connection
------------------------------

The **BeMicroSDK** hardware is designed with a *System ID* peripheral. This peripheral is assigned a unique value based on when the hardware design was last modified in the SOPC Builder tool. SOPC Builder also places this information in the *.sopcinfo* hardware description file. The BSP is built based on the information in the *.sopcinfo* file.

-  Select the **ADIEvalBoard** application software project.
-  Select **Run -> Run Configurations…**
-  Select the **Nios II Hardware** configuration type.
-  Press the **New** button to create a new configuration.
-  Change the configuration name to **BeMicroSDK** and click **Apply**.
-  On the **Target Connection** tab, press the **Refresh Connections** button. You may need to expand the window or scroll to the right to see this button.
-  Select the **jtag_uart** as the **Byte Stream Device** for *stdio*.
-  Check the **Ignore mismatched system ID option**.
-  Check the **Ignore mismatched system timestamp option**.

|eclipserunconfig.png| |image059.png|

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/ignoreid.png
   :alt: ignoreid.png
   :align: center
   :width: 500px

3. Run the Software Project on the Target
-----------------------------------------

To run the software project on the Nios II processor:

-  Press the **Run** button in the **Run Configurations** window.

This will re-build the software project to create an up–to-date executable and then download the code into memory on the **BeMicroSDK** hardware. The debugger resets the Nios II processor, and it executes the downloaded code. Note that the code is verified in memory before it is executed.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image063.png
   :alt: image063.png
   :align: center
   :width: 400px

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
