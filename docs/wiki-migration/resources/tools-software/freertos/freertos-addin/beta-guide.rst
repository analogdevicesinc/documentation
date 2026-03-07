Welcome to the Beta for the FreeRTOS Add-In for CrossCore Embedded Studio.

For any questions, feedback or support contact Murray Anderson (murray.anderson@analog.com).

Software Dependencies
=====================

Requires CrossCore Embedded Studio version 2.10.1 or 2.11.0 (http://analog.com/cces/)

FreeRTOS sources are self-contained so there’s no dependency on external sources.

--------------

Supported Hardware
==================

This release supports the following hardware:

-  ADSP-BF70x
-  ADSP-215xx
-  ADSP-SC5xx (ARM and SHARC+)

--------------

Supported FreeRTOS Kernel
=========================

The Add-In currently only supports a Kernel based on FreeRTOS version 10.4.3 LTS Patch 2. You may be able to use the generated configuration files with other versions of FreeRTOS but this is not officially supported.

--------------

Installing the Add-In
=====================

The Add-In can be installed via the **Install New Software functionality** from within CrossCore Embedded Studio. This is available under **Help** > **Install New Software**.

In the **Work With** field, select **CrossCore Embedded Studio Software and Documentation -** http://www.analog.com/static/ccesupdatesite. Expand the **CrossCore Embedded Studio Add-Ins** section, select **FreeRTOS Add-in (Beta)** and click on **Next**, Read and agree to the license text, and then click **Finish**


|image1|

--------------

Adding the FreeRTOS Add-In to an existing project
=================================================

Double click on the **system.svc** in the top level of your project.

Click on the **Add** button to the right of the list of already installed Add-Ins.

Expand **Middleware** then select **FreeRTOS for <core type>** and click **Finish**.

The Add-In will want to modify the main() source with some code to create a task and start the scheduler. To prevent these changes being made, deselect your project from the list of Changes to be performed. Click Finish to Add the Add-In to your project. Sources files will be downloaded and created in your project so this may take a few moments.

--------------

Adding the FreeRTOS Add-In to a new project
===========================================

Create a new project as normal, and when you get to the Projects and Settings page, click on configure for each project which you want to install FreeRTOS in.

Click on the **Add** button to the right of the list of already installed Add-Ins.

Expand **Middleware** then select F\ **reeRTOS for <core type>** and click **Finish**.

The Add-In will want to modify the main() source with some code to create a task and start the scheduler. To prevent these changes being made, deselect your project from the list of Changes to be performed. Click Finish to Add the Add-In to your project.

--------------

Configuring the FreeRTOS Add-In
-------------------------------

Double click on the system.svc in the top level of your project.

Click on the **FreeRTOS** tab along the bottom of the Configuration page:

The tabs along the left contain options within different categories. Making a change and saving the configuration (CTRL + S) will regenerate the appropriate files within your project.

--------------

Modifying your application
==========================

The FreeRTOS Add-In makes 3 modifications to your project: Main, user modifiable sources and system sources.

Main
----

The FreeRTOS Add-In will add code to your applications main function, which will create a task userStartupTask and then start the scheduler. You can either modify userStartupTask or create your own task(s). 

User Modifiable Sources
-----------------------

A directory, **CustomizableFreeRTOSSources** will be added to your project, which contain generated code which can be modified by the user. **FreeRTOSUserApplication.c** contains the code for **userStartUpTask**, the default task created by main.

System Sources
--------------

Another directory, **FreeRTOS** will be added to your project under **system**. This directory contains both the FreeRTOS Kernel and a generated configuration which is not user modifiable. You should not need to modify anything within the system directory, though it can be stepped through with the debugger or viewed for reference. 

Status View
===========

A Status view is available from within CrossCore Embedded Studio when connected to a debug session with a FreeRTOS project. It can be accessed via **\*Window > Show View > Other > Debug > RTOS Status**\ \* Currently it'll present information about all of the created tasks. Note: This is only currently available when debugging using the CCES Debugger and not OpenOCD

Known issues
============

-  The Status view isn't available via OpenOCD

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/freertos-addin-download-p2.jpg
   :width: 400px
