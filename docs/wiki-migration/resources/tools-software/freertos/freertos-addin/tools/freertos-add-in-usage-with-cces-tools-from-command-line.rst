FreeRTOS Add-In Usage with CCES Tools From Command Line
=======================================================

This page provides a approach to use FreeRTOS Add-In with CCES Toos from command lines.

::

   ;
   :
   ; **''FreeRTOS Add-In''**
   : Get the FreeRTOS Source Code and setup the FreeRTOS Configuration for a project
   ; **''Headless Builder''**
   : Create a CCES Project for a specified processor
   : Add and Remove the FreeRTOS Add-In to a CCES project
   : Build the CCES project
   ; **''CCES Runner Tool''**
   : Load and Run the compiled binaries generated from the Target Project with FreeRTOS.

**Home Page**: `FreeRTOS Add-In From the Command Line <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-from-the-command-line>`__

--------------

Environment Setup
-----------------

-  `Install CCES and setup Configuration </>`__ CCES Headless builder is available after CCES installation
-  :doc:`Install the FreeRTOS-Addin </wiki-migration/resources/tools-software/freertos/freertos-addin>`
-  `Install the CCES runner </>`__ TO DO

--------------

Getting Started
---------------

Please follow below steps to Create, manage and build the CCES project with FreeRTOS-Addin.

-  Creating a New CCES Project
-  Adding the FreeRTOS Add-In
-  Customizing the Project
-  Building the Projects
-  Downloading and Running
-  Quick Start Demo

--------------

Create a New CCES Project
-------------------------

CCES headless builder provides a way to create a project by command line with the parameters, i.g. We can specify the project name, the processor & silicon revision, the project type and core number of the project that is to be created. The related options we can use are:

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Available Option | Description                                                                                                                                            |
+==================+========================================================================================================================================================+
| -project         | In this case, this option specifies the local path where the newly created project will be resides                                                     |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -command         | Create project by meta data file if 'projectcreate' is set                                                                                             |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -type            | Project type ( Executable/Static Library )                                                                                                             |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -project-name    | The project name of the to be created project                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -processor       | The processor of the to be created project ``ADSP-BF707`` ADSP-21569 ADSP-SC573 ADSP-SC584 ADSP-SC589 ADSP-SC594                                       |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -revision        | [Optional] If omitted, adopt the default silicon revision of the specified processor                                                                   |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -core            | [Optional] If omitted, choose core 0                                                                                                                   |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -noinit          | [Optional] If specified, the 'system' folder and its containing adi_initialize.{h/c} files will not be created                                         |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -language        | [Optional] The language of the to be created project. 'C' or 'C++'. Defaults to 'C' if the option is omitted                                           |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -nofpu           | [Optional] Disables the FPU for the to be created project. Only applies to Cortex-M parts. If the option is omitted, the processor default FPU is used |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example and Command Syntax:**

.. code:: batch

   @cd "C:\Analog Devices\CrossCore Embedded Studio 2.10.0\Eclipse"
   ccesc.exe
       -nosplash
       -application com.analog.crosscore.headlesstools
       -command projectcreate
       -data "C:\worksapce"
       -project "C:\worksapce\project\FRTSO_ADSP589_Test"
       -project-name FRTOS_ADSP589_Test
       -processor ADSP-SC589
       -revision any
       -core 1
       -type Executable
       -language C
   @pause

\**CMD executable Command: :-D \*\*

.. code:: batch

   cd "C:\Analog Devices\CrossCore Embedded Studio 2.10.0\Eclipse"
   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools -command projectcreate -data "C:\workspace" -project "C:\workspace\project\FRTSO_ADSP589_Test" -project-name FRTOS_ADSP589_Test -processor ADSP-SC589 -revision any -core 1 -type Executable  -language C

The headless builder will show below result information if the project has been created successfully.


|image1|

Then you can find a new cces project for adsp-sc589 core1 revision any has been created at the specified path: *C:\\workspace\\project*


|image2|

**PREV:** :doc:`Getting Started </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-usage-with-cces-tools-from-command-line>` **NEXT:** :doc:`Add FreeRTOS Add-In to the Project </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-usage-with-cces-tools-from-command-line>`

--------------

Add FreeRTOS Add-In to the Project
----------------------------------

CCES Headless Builder also provides a way for the user to manage the Add-Ins (e.g. add, remove and upgrade them from projects in an automated fashion) via the Command Line. So we can use this approach to add the FreeRTOS Add-In to the project we created before to setup the FreeRTOS necessary configurations for this project. The Add-In management functionality of Headless Builder can be achieved by using the options as follows:

+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name  | Description                                                                                                                                                                                                                                                                                                        |
+==============+====================================================================================================================================================================================================================================================================================================================+
| -command     | Specify the action type. ``'addaddin``' for adding an Add-in to a project; ``'overbidding``' for removing an Add-in from a project; ``'upgradeaddin``' for upgrading an Add-in in a project; ``'upgradeall``' for upgrading all Add-ins which have been installed in the project to the latest supported versions. |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -fromversion | [Optional] The installed addin version (only for command "upgradeaddin"). If it is not specified, the version of the Add-In that is installed in the project is regarded as '-fromversion'.                                                                                                                        |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -id          | The addin id                                                                                                                                                                                                                                                                                                       |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -toversion   | The to-be-upgraded addin version (only for command "upgradeaddin"). 'latest' can be selected to upgrade an Add-In to its latest version.                                                                                                                                                                           |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -version     | The addin version (only for command "addaddin"). 'latest' can be selected to add an Add-In that has the latest version.                                                                                                                                                                                            |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example and Command Syntax of adding the FreeRTOS Add-in:**

.. code:: batch

   @cd "C:\Analog Devices\CrossCore Embedded Studio 2.9.1\Eclipse"
   ccesc.exe^
       -nosplash^
       -application com.analog.crosscore.headlesstools^
       -data "c:/workspace"^
       -project "C:\workspace\project\FRTSO_ADSP589_Test"^
       -command addaddin^
       -id com.analog.crosscore.addins.freertos^
       -version 1.0.0

**CMD executable Command:** :-D

.. code:: batch

   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools -data "c:/workspace" -project "C:\workspace\project\FRTSO_ADSP589_Test" -command addaddin -id com.analog.crosscore.addins.freertos -version 1.0.0

The headless builder will show below results information if the Add-In has been installed successfully.


|image3|

.. note::

   **To Do** add the examples of overbidding upgradeaddin upgradeall usage if necessary


**PREV:** :doc:`Create a New CCES Project </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-usage-with-cces-tools-from-command-line>` **NEXT:** :doc:`Customize the Project </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-usage-with-cces-tools-from-command-line>`

--------------

Customize the Project
---------------------

With the CCES headless builder tool, we can modify the code and customize the project, such as link some codes/files into the projects, change project settings, modify the searching paths of the headerfiles, libraries or some other additional settings.

**1. Creating links**

We can create some link files that are linked to any files or folders (usually source files, header files or configuration files) that reside in local file system.

+------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name                              | Description                                                                                                                                                                                                                                                                                                                              |
+==========================================+==========================================================================================================================================================================================================================================================================================================================================+
| -link [ ``Source'' ] [ ''Destination`` ] | ''**:math:`Source**'' specifies the file in the local file system that is going to be created link from. **''`\ Destination''** specifies where the link file should be created. It should be a relative path to the project base path. Destination is optional and if it's omitted, the link file will be created at project base path. |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**2. Changing Tool Options for Projects**

The headless builder provides a couple of options used to append/remove/change tool switches of a project. Here are these options:

+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name                                   | Description                                                                                                                                               |
+===============================================+===========================================================================================================================================================+
| -cfg [ configName ][Optional]                 | If set, selects the configuration whose tool options to modify. Note: If not set, all configurations are affected.                                        |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| -append-switch [ toolname ] [ switch=value ]  | [Optional] Append value to a tool option. Whitespace is not allowed to be in the middle of the switch name. ( e.g. -D=MACRO1, additionaloption=OPTION1 ). |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| -remove-switch [ toolname ] [ switch=value ]  | [Optional] Remove a tool option. Whitespace is not allowed to be in the middle of the switch name. ( e.g. -D=MACRO1, additionaloption=OPTION1 ).          |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| -replace-switch [ toolname ] [ switch=value ] | [Optional] Replace a tool option value. Whitespace is not allowed to be in the middle of the switch name. ( e.g. -D=MACRO1, additionaloption=OPTION1 )    |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| -processor [ processorModel ]                 | [Optional] This option can be specified to change processor for a project                                                                                 |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| -revision [ siliconRevision ]                 | [Optional] This option can be specified to change silicon revision for a project                                                                          |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   TO DO: add the examples


**PREV:** :doc:`Add FreeRTOS Add-In to the Project </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-usage-with-cces-tools-from-command-line>` **NEXT:** :doc:`Building Projects </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-usage-with-cces-tools-from-command-line>`

--------------

Building the Project
--------------------

**1. Importing & Copying Projects to Workspace**

Example and Command Syntax:

.. code:: batch

   ccesc.exe
        -nosplash
        -application com.analog.crosscore.headlesstools
        -data c:/workspace
        -project "C:\cces_projects\project\FRTSO_ADSP589_Test"
        -copy 

CMD executable Command: :-D

.. code:: batch

   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools -data c:/workspace -project "C:\cces_projects\project\FRTSO_ADSP589_Test" -copy 

The headless builder will show below results information if the project is successfully.


|image4|

\**2. Building Projects \*\*

Example and Command Syntax:

.. code:: batch

   ccesc.exe
         -nosplash
         -application com.analog.crosscore.headlesstools
         -data "c:\workspace"
         -project "C:\workspace\FRTOS_ADSP589_Test"
         -regensrc 
         -cleanBuild Debug
         -consoleLog

CMD executable Command: :-D

.. code:: batch

   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools -data "c:\workspace" -project "C:\workspace\FRTOS_ADSP589_Test" -cleanBuild Debug -consoleLog -regensrc

The headless builder will show below results information if the project is successfully.


|image5|

Also, you can check the target binary file "FRTOS_ADSP589_Test.dxe" has been build successfully in the Debug/Release folder.


|image6|

.. note::

   TO confirm: could we build the Three-core project in one command?


**PREV:** :doc:`Customize the Project </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-usage-with-cces-tools-from-command-line>` **NEXT:** :doc:`Downloading and Running </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-usage-with-cces-tools-from-command-line>` **CATALOGUE:** :doc:`Getting Started </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-usage-with-cces-tools-from-command-line>`

--------------

Downloading and Running
-----------------------

CCES Runner is a command-line utility which lets users load programs, set breakpoints and run programs from outside CrossCore Embedded Studio's graphical environment, e.g. as part of a continuous-integration and testing setup. The following is a brief explanation of the purpose of the basic commands:

+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name | Description                                                                                                                                                                                                                                                                  |
+=============+==============================================================================================================================================================================================================================================================================+
| --target    | The session's target. This command must be followed by a string specifying the target. --target "Emulation Debug Target"                                                                                                                                                     |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --processor | The session's processor. This command must be followed by a string specifying the processor. --processor "ADSP-SC589"                                                                                                                                                        |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --platform  | The session’s platform. This command must be followed by a string specifying the platform. --platform "ADSP-SC589 via ICE-1000"                                                                                                                                              |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --cceshome  | The CCES installation home path, his command must be followed by a string specifying the cceshome. --cceshome "C:\\Analog Devices\\CrossCore Embedded Studio 2.10.0"                                                                                                         |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --core      | The core as well as its prerequisites (programs that initialize memory and/or set up the system) and program to load and run. The core ID, prerequisites, and program must be separated by a comma. The prerequisite options and program must be separated by a vertical bar |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For the detail explanations of the all available commands and parameters please use **CCES_runner.exe --help** in CCES Home


|image7|

**Example and Command Syntax:**

.. code:: batch

   CCES_runner.exe^
       --target "Emulation Debug Target"
       --platform "ADSP-SC573 via ICE-1000"
       --processor "ADSP-SC573"
       --cceshome "C:\Analog Devices\CrossCore Embedded Studio 2.10.0" 
       --core "0, CLEAR_SYMBOLS|RUN_AFTER_LOAD|SHARC\ldr\ezkitSC573_preload_core0,C:\workspace\RTOSDemo_SHARC_SC573_CCES_Core0"
       --core "1,C:\workspace\RTOSDemo_SHARC_SC573_CCES_Core1.dxe"

**CMD executable Command:** :-D

.. code:: batch

   cd "C:\Analog Devices\CrossCore Embedded Studio 2.10.0"
   CCES_runner.exe --target "Emulation Debug Target" --platform "ADSP-SC573 via ICE-1000" --processor ADSP-SC573 --cceshome "C:\Analog Devices\CrossCore Embedded Studio 2.10.0"  --core "CLEAR_SYMBOLS|RUN_AFTER_LOAD|SHARC\ldr\ezkitSC573_preload_core0_v01,C:\Analog Devices\FreeRTOS\FreeRTOS_GLXP\FreeRTOSv10.3.1\FreeRTOS\Demo\SHARC_ADSP_SC573_CCES\RTOSDemo_CCES_SHARC_Core0\Debug\RTOSDemo_SHARC_SC573_CCES_Core0" --core "1,C:\Analog Devices\FreeRTOS\FreeRTOS_GLXP\FreeRTOSv10.3.1\FreeRTOS\Demo\SHARC_ADSP_SC573_CCES\RTOSDemo_CCES_SHARC_Core1\Debug\RTOSDemo_SHARC_SC573_CCES_Core1.dxe"

.. note::

   TO update the example


--------------

Reference
---------

--------------

**Home Page**: `FreeRTOS Add-In From the Command Line <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/tools/freertos-add-in-from-the-command-line>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/001_headless_tools_results_create_project.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/001_creat_a_new_cces_project_with_command_line.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/003_headless_tools_results_add_freertos_add-in.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/004_headless_tools_results_import_project_to_workspace.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/005_headless_tools_results_build_the_project.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/005_1_headless_tools_results_build_the_project.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/006_cces_runner_available_commands.png
