Introduction to the FreeRTOS Add-In
===================================

The **FreeRTOS Add-In** for CrossCore Embedded Studio (**CCES**) has been developed by Analog Devices to provide a user-friendly programming enviroment for FreeRTOS applications running on **Analog Devices Blackfin**, **SHARC** and **Cortex-A** processors. The **FreeRTOS Add-In** seamlessly integrates with **CCES** and provides a user interface for configuration of FreeRTOS macros.

--------------

Release Dependencies
====================

FreeRTOS Add-In requires CrossCore® Embedded Studio version 2.10.0 or greater. Support for ADSP-BF70x is not available in CrossCore® Embedded Studio version 3.0.0 or greater. Support for ADSP-2183x/ADSP-SC83x is only available in CrossCore® Embedded Studio version 3.0.0 or greater.

--------------

Supported Boards
================

Currently the **FreeRTOS Add-In** by **Analog Devices** can be used with the **215xx \| SC5xx \| 2183x \| SC83x \| BF7xx** series boards.

If you want to use UART/ CCES System Services and Device Drivers with the FreeRTOS Add-In, then you must follow the instructions in the section :doc:`UART functionality </wiki-migration/resources/tools-software/freertos/freertos-addin/uart>`, to enable the functionality within the project, as this is not currently possible to automate with the Add-In.

--------------

Get Started
===========

To get started using the FreeRTOS Add-In, please follow in order the sections below.

-  Follow instruction at the section "Installing the Add-In"
-  Create a new Project in CCES
-  Follow instruction at the section "Adding The FreeRTOS Add-In"

--------------

Installing the Add-In
=====================

The **FreeRTOS Add-In** will be available to install via the built in **Install new Software** functionality in **CCES**. In order to access this, you must follow the steps below

-  Launch **CCES**
-  Click **Help**
-  Click **Install New Software**
-  In the "**Work with** drop-down field, select **CrossCore Embedded Studio Software and Documentation -** http://www.analog.com/static/ccesupdatesite
-  Expand **CrossCore Embedded Studio Add-Ins**
-  Check the box of **FreeRTOS Add-In**
-  Proceed by Clicking **Next** and Reading/Accepting the terms of the license agreement
-  Click **Finish** to start installing the Add-In
-  You should see down the bottom right of CCES a progress bar for the installation
-  A pop up Should appear to restart CCES after a successful installation

--------------

Uninstalling the Add-In
=======================

The **FreeRTOS Add-In** can be uninstalled in **CCES**. you must follow the steps below

-  Launch **CCES**
-  Click **Help**
-  Click **About CrossCore Embedded Studio**
-  Click the **Installation Details** on the bottom left
-  Select the **FreeRTOS Add-In**
-  Click **Uninstall** to start uninstalling the Add-In
-  Click the **Finish**
-  A pop up Should appear to restart CCES after a successful uninstallation

--------------

Adding The FreeRTOS Add-In
==========================

Adding ADI's implementation of FreeRTOS to a CrossCore project adds the following:

-  Required includes
-  Any tool chain options required
-  :doc:`Generated Files </wiki-migration/resources/tools-software/freertos/freertos-addin/generated-files>` based on the configuration defaults for relevant processor
-  Source files downloaded from Analog Devices implementation of FreeRTOS repository
-  :doc:`Calls to multiple functions placed in main </wiki-migration/resources/tools-software/freertos/freertos-addin/added-functions>`

**Tip:** You can also add the FreeRTOS Add-In at project creation.

It is assumed that the project is expanded in the **Project Explorer** view.

To add the FreeRTOS Add-In to the project:

-  Double-click the system.svc file of the project. The System Configuration utility appears.
-  Click **Add**. The Add New Add-ins wizard appears.
-  In **Available Add-Ins**, expand the **RTOS** node.
-  In RTOS, select **FreeRTOS for Processor-Family(Version Number)** for example FreeRTOS for Blackfin(1.0.0). The add-in's description appears in the **Selected Add-Ins** tab to the right of the **Available Add-ins** control.
-  Check the **Warnings** tab for potential issues.
-  Click **Finish**. The newly configured add-in appears on the Overview tab of the **System Configuration** utility.

.. note::

   If there are issues, you can highlight the affected add-in on the **Selected Add-Ins** tab and click Remove or **Quickfix**.


--------------

Upgrading The FreeRTOS Add-In
=============================

In order for the user to upgrade the version of the addin they are using, they will have to use the CCES Feature "Check For Updates"

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/image2019-9-30_14-20-11.png

if there is any updates to the addin then these will appear to the user so that they can accept the license agreement.

as shown below, there is no upgrade button available

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/image2019-9-30_14-11-13.png

See :doc:`version history </wiki-migration/resources/tools-software/freertos/freertos-addin/version-history>` for details of changes between releases. We always recommend using the latest release.

--------------

Removing The FreeRTOS Add-In
============================

Any code associated with FreeRTOS will be removed from a CrossCore project.

It is assumed that the project is expanded in the Project Explorer view.

To remove the FreeRTOS add-in from the project:

-   Double-click the system.svc file. The System Configuration utility appears.
-   In **Installed Add-Ins**, select at least one add-in.
-   Click **Remove**. The Remove Add-Ins Confirmation dialog box appears. The name and software version of the add-in(s) selected for removal appear in the table.
-  Do the following: (a) Verify the add-in(s) to be removed. (b) In **Warnings**, observe whether it is safe to proceed.
-  Click **Remove**. The progress bar starts indicating completion of the requested actions.
-  Generated files that have been added to the system directory of your project will be removed, but the files in src/CustomizableFreeRTOSSources/ will remain in your project. See the :doc:`Generated Files </wiki-migration/resources/tools-software/freertos/freertos-addin/generated-files>` section for full details.
-  A pop up will appear notifying the user that functions related to the FreeRTOS add-in will be removed from the main file. This can be rejected if the user wants to keep the code.

.. note::

   Completion of some actions may require your clicking **Yes** in response to a message about removing files from the project.


--------------

FreeRTOS Add-In Examples
========================

Example projects for each of the supported EZ-Kits can be found at ` <https://github.com/analogdevicesinc/freertos-examples/>`__

--------------

FreeRTOS Add-In Performance
===========================

The FreeRTOS Add-In has several different benchmark example projects that are available to download. Documentation has been created for these :doc:`FreeRTOS Add-In Performance </wiki-migration/resources/tools-software/freertos/freertos-addin/performance>`

The currently supported boards for benchmark data are as follows

-  ADSP-BF707
-  ADSP-21569
-  ADSP-SC573 (Cortex_a5 and SHARC)
-  ADSP-SC584 (Cortex_a5 and SHARC)
-  ADSP-SC589 (Cortex_a5 and SHARC)

--------------

Supported Macros
================

The **FreeRTOS Add-In** contains a custom built **UI** that users can easily use to configure values for `Supported FreeRTOS Configuration Macros <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/supported-macros>`_, this can be seen in the image below.

--------------

Migration Guide
===============

The following pages provide the migration guide for users to conveniently use.

-  µC/OS-III to FreeRTOS: :doc:`µC/OS-III® to FreeRTOS Migration Guide </wiki-migration/resources/tools-software/freertos/migration-guide/ucos-to-freertos-migration-guide>`

--------------

Command Line Build Support
==========================

we also provide an approach of using the FreeRTOS Add-In with command line for users who prefer to create, build, run the FreeRTOS applications via CCES tools from the command line or use a Makefile and call the compiler directly.

-  `FreeRTOS Add-In From the Command Line <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-from-the-command-line>`_

--------------
