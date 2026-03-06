CrossCore Embedded Studio Quick Start User Guide For Linux
==========================================================

This page describes how to use the ADuCM4x50 Device Family Pack (DFP) and Board Support Package (BSP) with CrossCore Embedded Studio (CCES) to create, import, build and debug applications for the ADuCM4x50 processor. Additional help documentation can be found by opening CCES and selecting *Help Contents* from the CCES *Help* menu. This page covers:

-  CrossCore Embedded Studio 2.6.0
-  Attach the ADZS-ADuCM4050 EZ-KIT
-  Start CCES and configure Workspace
-  How to install or upgrade the ADuCM4x50 DFP, BSP, and ARM.CMSIS software for CCES
-  How to create a new project for the ADuCM4050
-  How to add startup code and core components to a new project for the ADuCM4050
-  How to import existing projects into a workspace
-  How to build projects for programming the ADuCM4050
-  How to configure the Tools Settings used by an ADuCM4050 project
-  How to configure the debug session for an ADuCM4050 application
-  How to start and stop debugging an ADuCM4050 application
-  POST Example Tutorial

CrossCore Embedded Studio 2.6.0
===============================

CCES 2.6.0 must be installed and configured. Please refer to the :doc:`CCES Download & Installation Guide </wiki-migration/resources/eval/user-guides/adzs-aducm4050/crosscore_download_install_guide>`.

.. important::

   The ADZS-ADuCM4050 **requires** the use of Crosscore Embedded Studio version **2.6.0 or higher**. Do not attempt to use earlier versions of the CrossCore tools, due to compatibility issues with the ADZS-ADuCM4050.



Attach the ADZS-ADuCM4050 EZ-KIT
================================

Using a USB A to USB Mini B cable, attach the Mini B end of the cable to the usb port (P11) labeled "mbed" (ADZS-ADuCM4050LF-EZ-KIT) or "MBED" (ADZS-ADuCM4050WL-EZK-IT). Attach the USB A end of the cable to the PC. After the USB drivers have been updated, the EZ-KIT board will be listed under *Devices*. It will be labeled "**DAPLINK**".

Start CrossCore Embedded Studio 2.6.0 and configure Workspace
=============================================================

Start CCES from *However you start CCES in Linux*. Upon starting, CCES first requires that a Workspace be configured. A CCES Workspace is a folder (e.g. /home/cces/2.6.0) that contains project resources and metadata. When projects are created or imported, details about that project are stored in the workspace. The workspace metadata also includes preferences set through the CCES **Preferences** dialog box and IDE window layouts. By default, CCES creates new projects within the Workspace folder. To default to a Workspace directory, check *Use this as the default and do not ask again* and click *OK*. The prompt to configure a Workspace will not appear again the next time CCES is opened.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg1workspaceandprojects.png

.. note::

   To reset the default Workspace setting, within CCES go to *Window \| Preferences \| General \| Startup and Shutdown \| Workspaces* and check *Prompt for workspace on startup*.



How to install or upgrade the ADuCM4x50 Device Family Pack, Board Support Package, and ARM.CMSIS software for CrossCore Embedded Studio
=======================================================================================================================================

The ADuCM4x50 DFP and BSP and the ARM.CMSIS software must be installed after CCES 2.6.0 is installed. To install or update the DFP, BSP, or ARM.CMSIS software, open the **CMSIS Pack Manager** perspective in CCES. Go to *Window \| Perspective \| Open Perspective \| Other…* In the **Open Perspective** window select **CMSIS Pack Manager** and click *OK*. Next, select **Check for Updates on Web**.

.. note::

   The **Welcome** view may need to be minimized.



.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg2install1.png

.. tip::

   If prompted to accept a License Agreement, read the License Agreement and check **I agree to all the terms of the preceding License Agreement** and click *OK*. All subsequent License Agreements will also need to be agreed to.



In the **Devices** view of CMSIS Pack Manager, expand **Analog Devices**, **ADuCM4x50 Series**, and select **ADuCM4050**. In the **Packs** view, expand the **Device Specific** section and select the *Install* Action next to the **AnalogDevices.ADuCM4x50_DFP** Pack. The DFP is installed.

-  Do the same process for the BSP; select the *Install* Action next to the **AnalogDevices.ADuCM4x50_EZ_KIT_BSP** Pack. The BSP is installed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg2install2.png

In the **Packs** view, expand the **Generic** section and select the *Install* Action next to the **ARM.CMSIS** Pack. The ARM.CMSIS software is installed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg2install3.png

With the DFP, BSP, and ARM.CMSIS software installed, the **POST** Example can be copied into the CCES Workspace by going to the **Examples** view and clicking the *Copy* Action next to the **POST (ADuCM4050 EZ-KIT)** Example.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg2install4.png

Click *Copy* to confirm the **Copy Example to Eclipse Workspace** dialog. The POST Example will open in the **C/C++** perspective. If prompted, click *Yes* to allow any missing packs to be installed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg2install5.png

Alternatively, the ADuCM4050 DFP and BSP files can be installed using a local download.

Download the pack files from the Analog.com website:

.. admonition:: Download
   :class: download

   **Device Family Pack** (http://download.analog.com/tools/EZBoards/ADuCM4050/Releases/DeviceFamilyPack/Release_1.0.0/ADuCM4x50_Device_Family_Pack-Rel1.0.0.zip)

   
   **Board Support Pack** (http://download.analog.com/tools/EZBoards/ADuCM4050/Releases/BSP/Release_1.0.0/ADuCM4x50_Board_Support_Pack-Rel1.0.0.zip)


Extract the compressed files to a local directory (e.g. **/home/cces/2.6.0/DFP**). Select the *Import Existing Packs* button in the CMSIS Pack Manager's **Packs** view, choose the .pack file as shown in the screenshot below, and click *OK*.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg2install6.png

Follow the steps above to install the required ARM.CMSIS software.

How to create a new project for the ADuCM4050
=============================================

A project for the ADuCM4050 can be created using the New CrossCore Project wizard. Use the wizard to complete the steps to create a new project.

-  To create a new project, go to the menu bar and select *File \| New \| CrossCore Project*.
-  Provide a **Project name**.\

|image1|

-  Choose **Processor family** **ARM** and select **Processor type** **ADuCM4050**.
-  Choose the **Silicon revision** (default is **0.1**).

   #.  A **SILICON_REVISION** macro will be set in the project's *Properties \| Settings*. The macro can be used to conditionally check the silicon revision in the source code.\


   |image2|

-  Project configuration allows additional Add-ins to the project, such as Pin Multiplexing and changing the template language for a generated main function.
-  Finally, press *Finish* and the project will be created and programs can be written.\

|image3|

How to add startup code and core components to a new project for the ADuCM4050
==============================================================================

An out-of-the-box ADuCM4050 project does not have startup code or a linker description file that maps code and data. It is necessary to add these components using the Run-time Environment (RTE) Configuration Editor.

CrossCore Projects created for Analog Devices' Cortex-M based processors, such as ADuCM4050 include a system.rteconfig file. Opening this file within the IDE will open the RTE Configuration Editor. Components from the CMSIS-Pack, such as drivers and services, can be added to a project by selecting them in the editor and clicking Save.

At a minimum, a new ADuCM4050 project will require the **CMSIS::CORE**, **Device::Global Configuration**, and **Device::Startup** components to be added to the project.

-  If a new project has just been created, use the **system.rteconfig** view, otherwise Double-click on **system.rteconfig** to open the RTE Configuration Editor
-  Select **CMSIS::Core**, **Device::Global Configuration**, and **Device::Startup**
-  Click Save (Ctrl+S)
-  *You can also choose* **Device::Startup** *and click the* Resolve *button to add dependant components*\

|image4|

How to import existing projects into a workspace
================================================

There are 3 methods for importing existing projects:

-  How to Import Existing Projects Saved to a Local Drive.
-  How to Import Examples listed in CMSIS Pack Manager.
-  How to Import Examples listed in Help \| Browse Examples.

.. note::

   For the remainder of this guide, the Power On Self Test (POST) Example will be used.



How to Import Existing Projects Saved to a Local Drive
------------------------------------------------------

-  Select *File \| Import…* from the CCES menu.
-  The **Import** window will appear with several project importing options. Choose the **General \| Existing Projects into Workspace** option, and click *Next*.
-  Select *Browse* in the dialog window and search for the saved project on the local drive.
-  (Optional) If the **Copy projects into workspace** option is checked, the project will be copied to the workspace folder and the newly copied project will be opened and used. This preserves the original version of the project.
-  Click *Finish*.


\



|image5|

How to Import Examples listed in CMSIS Pack Manager
---------------------------------------------------

Examples are provided with the ADuCM4050 DFP and BSP and can be displayed in the **CMSIS Pack Manager** perspective's **Examples** view.

-  Open **CMSIS Pack Manager** perspective by clicking the *Open Perspective* icon on the tool bar and selecting *CMSIS Pack Manager* in the **Open Perspective** window (or choose **CMSIS Pack Manager** perspective if already open).
-  From the **Examples** view, determine the example(s) to be copied.
-  Click the *Copy* Action button.
-  A dialog will pop-up showing the location where the example is to be copied. Click *Copy* to copy and open the example project in the **C/C++** perspective.\

|image6|

How to Import Examples listed in Help \| Browse Examples
--------------------------------------------------------

-  In CCES click on *Help \| Browse Examples*.
-  Filter examples by **Product** and choose either the **DFP** or **BSP** set of examples.
-  Select an example and click *Open example*.\

|image7|

How to build projects for programming the ADuCM4050
===================================================

-  Open the **C/C++** perspective by clicking the *Open Perspective* icon on the tool bar and selecting *C/C++* in the **Open Perspective** window (or choose the **C/C++** perspective if already open).
-  Right click on the project and select *Build Project*.

   -  Or click the Hammer icon from the toolbar.\ **build image image**

How to configure the Tool Settings used by an ADuCM4050 project
===============================================================

-  Select the project in the **Project Explorer** view.
-  Select the Cog icon from the view's toolbar.

   -  Or right-click on the project, select *Properties* and choose *C/C++ Build \| Settings*.

-  After configuring the project, click *Apply* and/or *OK*.\ **configure tools image**

How to configure the debug session for an ADuCM4050 application
===============================================================

A launch configuration will need to be created to debug the ADuCM4050 program.

::

   -If a project has already been built, select that project in the **Project Explorer** view.
   -Right-click on the project and choose //Debug As | Application with GDB and OpenOCD (Emulator)//
     -In the **Confirm Perspective Switch** window click //Yes//.
   -In the **Target** tab, choose **Target (processor)** and in the drop-down select **Analog Devices ADuCM4050**.
   -In the **Target** tab, choose **Interface** and in the drop-down select **ARM CMSIS-DAP compliant adapter**.
   -In the **Main** tab, ensure the project is selected in the **Project** entry box.
     -If the correct project is not populated, click the //Browse…// button and choose the project.  Note that this is optional and a project only needs to be chosen if the IDE will be used to search a project for the built binaries (programs), otherwise leave this entry blank.
   -In the **Main** tab, ensure the binary (program) is selected in the **Application** entry box.
     -If the correct binary (program) is not populated, click on //Search Project…// and choose the binary (program) from those available in the chosen project.
     -If the binary (program) is not populated and it was not built from a project in the workspace (i.e. there is a pre-built binary), then click the //Browse…// button and search for the pre-built binary (program).  When the file has been found and the pre-built binary (program) selected, click //Open//.
   -Click //Debug//.**debug configuration image**

How to start and stop debugging an ADuCM4050 application
========================================================

::

   -Ensure the ADZS-ADuCM4050 EZ-KIT is connected to the computer.
     -Via the **mbed** (LF board) or **MBED** (WL board) USB port (P11).
     -Via the **USB TO UART** USB port (P6).
   -If the **Debug Configurations** dialog is open, click //Debug//.
   -If the **C/C++** perspective is open, launch the last debug session by clicking the Beetle //Debug// button on the toolbar.{{:resources:eval:user-guides:adzs-aducm4050:aducm4050linuxqsg13startdebug.png?direct|}}
   -Confirm to switch perspective to the **Debug** perspective.  Click //Yes//.  Checking //Remember my decision// will cause this dialog to not display again.\\ {{:resources:eval:user-guides:adzs-aducm4050:aducm4050linuxqsg14confirmperspectiveswitch.png?direct|}}
   -If the binary (program) was built with Semihosting enabled, then CCES will warn about the need to re-build the program when the program is run without a debugger attached.{{:resources:eval:user-guides:adzs-aducm4050:aducm4050linuxqsg15semihostingenabled.png?direct&720|}}

.. warning::

   
   If the POST project is built with Semihosting enabled, POST will only run while the EZ-KIT is attached to CCES. The EZ-KIT can run POST "stand-alone" by setting the following properties:
   
   -   **POST_COMMON_USES_UART** macro is **added** to **Preprocessor definitions (-D)**
   
      -  *Properties \| Settings \| Tool Settings \| CrossCore GCC ARM Embedded C Compiler \| Preprocessor*
   
   -  **Semihosting** is disabled
   
      -  *Properties \| Settings \| Tool Settings \| CrossCore GCC ARM Embedded C Linker \| Libraries \| Semhosting support* is set to **None**.
   
   Connect the EZ-KIT's USB TO UART (P6) connector to the PC with the USB cable and use a terminal emulation program to view the POST console.


::

   -If everything goes fine, the CCES **Console** window will display a report without errors.

.. note::

   
   **As a reference, the text should be similar to:**
   
   ::
   
              o Open On-Chip Debugger (Analog Devices CCES 2.6.0 OpenOCD 0.9.0-g21dc5ad) 0.9.0
              o Licensed under GNU GPL v2
              o Report bugs to <processor.tools.support@analog.com>
              o 0
              o Info : select transport "swd"
              o adapter speed: 1000 kHz
              o cortex_m reset_config sysresetreq
              o Info : CMSIS-DAP: SWD  Supported
              o Info : CMSIS-DAP: Interface Initialised (SWD)
              o Info : CMSIS-DAP: FW Version = 1.0
              o Info : SWCLK/TCK = 0 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1
              o Info : CMSIS-DAP: Interface ready
              o Info : clock speed 1000 kHz
              o Info : SWD IDCODE 0x6ba02477
              o Info : aducm4050.cpu: hardware has 6 breakpoints, 4 watchpoints
              o Info : aducm4050.cpu: but you can only set 1 watchpoint
              o Info : CHIPID 0x02a0
              o memory bus access delay set to 6 tck
              o adapter speed: 1000 kHz
   


::

   -The program's execution is stopped automatically at the first breakpoint which is at the beginning of the main() loop.  The debug functions and features of the CCES environment such as stepping through, breakpoints, register reads, variable values, and others can be used.{{:resources:eval:user-guides:adzs-aducm4050:aducm4050linuxqsg17debuggingpost.png?direct|}}
   -To terminate a debug session, click on the red Stop button on the toolbar.{{:resources:eval:user-guides:adzs-aducm4050:aducm4050linuxqsg18stopdebug.png?direct|}}

POST Example Tutorial
=====================

Now that the POST example has been copied to the CCES IDE, please refer to the POST example Readme_Power_On_Self_Test.html file in the **Linux path to the directory containing the POST readme** directory for more information and instructions on running POST on the ADZS-ADuCM4050LF and ADZS-ADuCM4050WL EZKITs.

`Compressed HTML Readme file <https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/readme_power_on_self_test.zip>`__

*End of document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg4newproject1.png
   :width: 720px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg5newproject2.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg6newproject3.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg6newproject4.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg7importexisting.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg8importcmsis.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adzs-aducm4050/aducm4050linuxqsg9importhelp.png
