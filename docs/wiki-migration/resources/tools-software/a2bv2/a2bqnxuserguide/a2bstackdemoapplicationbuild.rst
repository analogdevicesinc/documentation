:doc:`Click here to return to A2B QNX User Guide Homepage. </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide>`

A2B Stack and Demo application build instructions
=================================================

After completing the System Setup as explained in :doc:`System Setup </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide/systemsetup>`, the A2B stack demo application on QNX can be built using a Momentics IDE or Makefile project.

Build for BeagleBone Black
--------------------------

Momentics based build
~~~~~~~~~~~~~~~~~~~~~

Open Momentics 7.0 in Windows host. Import the A2B QNX app project from ADI_A2B_Software- QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/. To build the project, either right click on the project and select “Build Project”, or click on the Build icon in the toolbar. The executable ‘a2bapp-qnx’ is created in Debug/Release folder depending on the build configuration chosen.

.. note::

   When building for the first time, a pop to select target or create might appear as shown in below Figure. To proceed with the build click cancel.


.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/target_selector.png
   :align: center
   :width: 400px

Makefile Based build
~~~~~~~~~~~~~~~~~~~~

Following are the steps to build the Makefile project

-  Open command prompt
-  Modify PATH variable to include QNX CC Toolchain provided by QNX ``>PATH = %PATH%;<<qnx installation path>>\host\win64\x86_64\usr\bin``
-  Navigate to the ADI_A2B_Software-QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx/Makefiles-Windows folder which contains the relevant Makefiles for building the stack and demo application.\ ``>cd << ADI_A2B_Software-QNX-RelX.Y.Z folder>>/ Target/examples/demo/a2b-qnx/Makefiles-Windows``
-  Execute the following command to build the application. ``> make -f Makefile-BBB.qnx``
-  To clean previous build artifacts, execute the following command ``> make -f Makefile-BBB.qnx clean``
-  The various build artifacts and temporary folders are created in the folder as explained in below Table.

+-------------------+-------------------------------------------------------------+
| **Output Folder** | **Purpose**                                                 |
+===================+=============================================================+
| build             | Intermediate build objects placed here                      |
+-------------------+-------------------------------------------------------------+
| staging/bin       | Contains the demo application a2bapp-qnx                    |
+-------------------+-------------------------------------------------------------+
| staging/include   | All Stack include files are placed here                     |
+-------------------+-------------------------------------------------------------+
| staging/lib       | All static libraries built for the Stack can be found here. |
+-------------------+-------------------------------------------------------------+

Build for a different platform
------------------------------

Building QNX A2B Stack for a different platform involves minimal modifications to the PAL layer alone. The default settings for the standard QNX PAL are configured in files in ADI_A2B_Software- QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/a2bstack-pal/platform/a2b/ folder.

While most of the settings are quite suitable for nearly all QNX platforms, these files shall be inspected and adapted as necessary for a different QNX system. For e.g., the path for the I2C device connected to the A2B chip can be specified in the macro A2B_CONF_DEFAULT_I2C_DEVICE_PATH in platform.h.

.. _momentics-based-build-1:

Momentics based build
~~~~~~~~~~~~~~~~~~~~~

In addition to inspecting and making necessary configuration changes in ADI_A2B_Software-QNX- RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/a2bstack-pal/platform/a2b/ folder, the target settings for custom platform must also be configured.

The specifics of the target on the custom platform must be specified in the Target settings in the properties of the project as shown in the below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/target_cpu_selcetor.png
   :align: center
   :width: 600px

.. _makefile-based-build-1:

Makefile based build
~~~~~~~~~~~~~~~~~~~~

The steps to build the makefile project are as mentioned in previous sections. Guidelines to modify the makefiles for a different platform are described here.

-  The top level Makefile Makefile-BBB.qnx and associated component Makefiles are available in the in ADI_A2B_Software-QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx /Makefiles- Windows folder from where the make based build is triggered. This top level Makefile is used for building the A2B stack and associated libraries, plugins, and applications. The top level Makefile invokes other component Makefiles namely Makefile.qnx for every component to be built. The various component Makefiles folders and the sources they build is explained below to facilitate easy porting to a new platform.

   -  a2bstack

      -  Contains the Makefile to build the generic or target agnostic portions of the A2B Software Stack. The sources for the same are located in ADI_A2B_Software- QNX-RelX.Y.Z/Target/a2bstack/a2bstack/src.
      -  a2bstack-pal

         -  Contains the Makefile to build the platform abstraction layer (PAL) for the QNX A2B Software Stack Implementation. The sources for the same are located in ADI_A2B_Software-QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/a2bstack-pal.

      -  a2bstack-protobuf

         -  Contains the Makefile to build the a2bstack-protobuf component containing the source code for the A2B Bus Description Data (BDD) schema and the Google Protobuf implementation called Nanopb. It also contains routines to parse bus configuration format generated from Sigma Studio to BDD structure. The sources for the same are located in ADI_A2B_Software-QNX-RelX.Y.Z/Target/a2bstack/a2bstack-protobuf/src.

      -  a2bplugin-master

         -  Contains the Makefile to build the sources for the A2B Software Stack master node plugin. The A2B network discovery algorithms and line fault diagnostics are encapsulated within these sources. The sources are located in ADI_A2B_Software-QNX-RelX.Y.Z/Target/a2bstack/a2bplugin-master/src.

      -  a2bplugin-slave

         -  Contains the Makefile to build the sources for a simple A2B Software Stack slave node plugin. These sources are a trivial example of a slave plugin for use as a launching pad for developing custom plugins. The sources are located in ADI_A2B_Software-QNX-RelX.Y.Z/Target/a2bstack/a2bplugin-slave/src

      -  a2bapp-qnx

         -  Contains the Makefile to build the sources for a sample A2B application for QNX. This application performs discovery of the A2B network depending on the network configuration provided. This application utilizes both the A2B Stack Software (a2bstack), QNX PAL (a2bstack-pal). The sources for the same are located in ADI_A2B_Software-QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp- qnx/app/.

-  By default, the top level Makefile Makefile-BBB.qnx is configured to use the qcc cross compiler provided by QNX. Modify the same and provide the compiler for your platform. Also, the Makefiles by default use GNU tools for various commands. The important parameters in the top level Makefile that need to be commonly modified are listed in below table.

+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Parameter**           | **Explanation**                                                                                                                                                                                                                                                                                |
+=========================+================================================================================================================================================================================================================================================================================================+
| INSTALL_TOP             | Default: $(CURDIR)/staging Defines where to install the various build artifacts (libraries, executables, etc.).                                                                                                                                                                                |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| STACK_ROOT              | Default: $(CURDIR)/../../../../a2bstack Defines where the sources for the various components of the core A2B stack are available. By default available in ADI_A2B_Software-QNX-RelX.Y.Z/Target/a2bstack/                                                                                       |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| APP_ROOT                | Default: $(CURDIR)/../ a2bapp-qnx Defines where the sources for the a2b demo application, a2bstack PAL on QNX and platform specific A2B stack configuration for the platform are available. By default available in ADI_A2B_Software-QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/app/ |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BUILD_DIR               | Default: $(CURDIR)/build Defines where various intermediate build objects are placed (objects, libraries, etc.).                                                                                                                                                                               |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| QNX_HOST                | Default: <<qnx installation path>>\\host\\win64\\x86_64 Defines the path to QNX installation Target folder                                                                                                                                                                                     |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| QNX_TARGET              | Default: <<qnx installation path>>\\target\\qnx7 Defines the path to QNX installation Target folder                                                                                                                                                                                            |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PLAT                    | Default: ntoarmv7 Defines the target architecture                                                                                                                                                                                                                                              |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| QCCTARGET               | Default: 5.4.0,gcc_ntoarmv7le_gpp Defines the QCC version(5.4.0) and the target platform. List of supported platforms will be maintained in <<qnx installation path>>\\host\\win64\\x86_64\\etc\\qcc\\gcc\\5.4.0                                                                               |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| QNX_BSP_I2C_INCLUDE_DIR | Default: <<qnx installation path>>\\target\\qnx7\\usr\\include\\hw This points to the path containig the i2c header include directory.                                                                                                                                                         |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CFLAGS                  | Compiler flags                                                                                                                                                                                                                                                                                 |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CC                      | Target Compiler                                                                                                                                                                                                                                                                                |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AR                      | Target Compiler                                                                                                                                                                                                                                                                                |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MKDIR                   | This value should point to an appropriate utility that can build a recursive directory structure similar to the GNU “mkdir -p”command.                                                                                                                                                         |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RM                      | This value should point to an appropriate utility that can recursively remove directories and files like the GNU “rm” command.                                                                                                                                                                 |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| INSTALL                 | This value should point to an appropriate utility that can install files like the GNU “install -p” command                                                                                                                                                                                     |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| INSTALL_DATA            | This value should point to an appropriate utility that can install files with write permissions disabled like the GNU “install -p -m 0644” command.                                                                                                                                            |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| INSTALL_EXEC            | This value should point to an appropriate utility that can install files with execute permissions set like the GNU “install –p -m 0755” command.                                                                                                                                               |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SUBDIRS                 | Provides the path to the various components built by this Makefile.                                                                                                                                                                                                                            |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  The Stack must be built and installed in a particular order to satisfy include dependencies components. The top level Makefile establishes this order. Even if some artefact is to be removed user must ensure the following build order.
   a2bstack> a2bstack-protobuf> a2bplugin-master> a2bplugin-slave> a2bstack-pal> a2bapp- qnx
