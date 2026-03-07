System Configuration File (system.svc)
======================================

Every CCES project contains a *system configuration* file. The file is the IDE's interface for adding to and managing pre-written software components in a project's configuration, such as system services, device drivers, add-ins, and LDF/startup code. The system configuration file is named **system.svc**, and it resides in the root of each project or the root of each core (for multi-core processors). The IDE provides the System Configuration Utility for maintaining the system.svc file. Double-clicking the system.svc file in the*\* Project Explorer*\* view opens the file in the utility editor, as shown in Figure 1.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/system.svc.png
   :width: 400px

*Figure 1. System Configuration Utility*

The **System Configuration Overview** window lists all the installed add-ins that you selected when creating the project. Here, you can also add more add-ins, remove them, or upgrade them if your application was created with an older version of the add-ins. In CCES, **Add-Ins** are additional tools that allow for things such as code generation to facilitate your code development process. If you create a new project using the default selections, you will have two or three default add-ins – **Analog Devices’ MCAPI** (only available for multi-core processors), **Startup Code/LDF** and **Pin Multiplexing** (only available for Blackfin projects) – which are accessible via the tabs along the bottom of the **System Configuration Overview**.

The **Analog Devices’ MCAPI** add-in provides Analog Devices’ implementation of Multicore Association’s Multicore Communications API (MCAPI™). Documentation can be found in CCES Online Help under **CrossCore® Embedded Studio 2.x.x → System Run-Time Documentation → Multicore Communications API (MCAPI) Specification**.

The **Startup Code/LDF** add-in automatically generates the necessary startup code for the processor. This code is executed before the application’s main function to perform required processor initialization based on user input. The GUI available via the configuration tab allows the user to select Cache and Memory Protection, configure how memory is initialized, setup external memory, and allocate stacks and heaps. It also generates/updates the project-required Linker Description File (LDF), which defines the full memory system available to the processor and instructs the tool chain how/where to resolve the various sections of code and data that comprise the full application.

The **Pin Multiplexing** add-in provides a GUI to configure pin usage to support the various peripheral interface combinations (SPI, SMC, CAN, TWI, etc.) available on the target processor. The GUI provides all the information necessary to properly configure general-purpose ports on the processor to support the required peripherals and identify/configure pins that are available for GPIO use, including identifying pin conflicts. When the **system.svc** file is saved, this add-in generates all the required code to properly configure the processor ports to support the specific combination designated by the user and updates the initialization code to call this newly generated code.

To install additional add-ins, click **Add…** and the selection window in Figure 19 will appear.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/add-ins.png
   :width: 600px

*Figure 2. Add New Add-ins*

There are also add-ins for the various system services (e.g., RTC and GPIO) and device drivers (for supported peripherals such as PPI, SPI, SPORT, etc.).

System Services and Device Drivers (SSDD)
=========================================

System Services and Device Drivers provide easy-to-use C/C++ APIs to expedite application development. Device drivers are available for most on-chip infrastructure blocks/peripherals and for several external system components, such as flash memory, converters, audio/video codecs, etc. These drivers leverage the underlying System Services, which provide the same high-level APIs to work with power/clocks, DMA, interrupts, etc., and oftentimes the Device Drivers make the calls into the System Services automatically, removing the developer from bit-level concerns in configuration registers that may be required as a result of changes made at a high level. For example, if a change is made to the clock settings, the properly-used drivers and services will make sure that clock specifications are being met and that system-level adjustments such as DDR refresh rate are automatically checked and corrected, as needed.

With the introduction of CCES, the System Services and Devices Drivers have been upgraded to SSDD 2.0 from the 1.0 version that was available in VisualDSP++®. The System Services and Device Drivers provide easy-to-use C/C++ APIs to expedite application development. The documentation for these APIs is available via Online Help under **CrossCore Embedded Studio 2.x.x → System Run-Time Documentation → System Services and Device Drivers**.

Project Properties
==================

Each project or core (for multi-core processors) contains properties that control the build of the program, processor settings, linker and loader options, etc. To access the **Properties**, go to the **Project Explorer** view, right-click on your main project or core folder, and select **Properties**. The Properties window will appear, giving you many options to choose from. The most commonly accessed options are the **Processor Settings** and **Tool Settings** tabs located on **C/C++ Build → Settings** page, as shown in Figure 3.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/properties.png
   :width: 600px

*Figure 3. Settings Properties of Project*

Within this Property Settings window, you can modify the Tool Settings, such as for the assembler, compiler, linker and loader. You can also modify Processor Settings, such as changing the silicon revision or the target processor. This window is also where you can configure your application to generate an executable (DXE) or loader (LDR) file, accessible via the **Artifact Type** pull-down on the **Build Artifact** tab.

-  The **Tool Settings** tab is where all the tool chain components (compiler, assembler, linker and loader) can be configured. Each unique sub-page provides access to and descriptions for many of the supported command-line switches that can be invoked during the build process, giving the user quick control over things such as optimization settings.

-  The **Processor Settings** tab describes the processor type and silicon revision, as setup during project creation. This is where an existing project can be modified to target a new processor and/or silicon revision after evaluation is complete (i.e., an application developed during evaluation on an ADSP-BF707 EZ-Kit needs to migrate to a custom target board designed around the lower-cost ADSP-BF704).

-  The **Build Steps** tab provides a means of adding command-line directives before and after those defined by the Tool Settings tab to be invoked automatically when the project is built. For example, launching the Command-Line Device Programmer to program the flash automatically after the loader file is generated by the build is supported in the Post-build steps on this tab.

-  The **Build Artifact** tab gives the flexibility to modify the output file type for the project to generate a processor executable (DXE), a bootable loader image (LDR), or a static library to be included as part of other projects (DLB), controlled via the **Artifact Type** pull-down. For example, a DXE is what is needed to debug the code in a simulator or emulator session, which employs the tool chain up to and including the linker. Once fully debugged, the DXE needs to be made into a defined boot stream, which requires the Loader component of the tool chain as well. Changing the Artifact type to **Loader File** and setting the appropriate fields in the Loader property pages on the Tool Settings tab is all that is required.

--------------

.. image:: https://wiki.analog.com/_media/navigation CCES Getting Started#create
   :alt: Creating & Importing Projects#.|CCES Getting Started#view|Perspectives & Views
