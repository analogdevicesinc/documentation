Step 2. Adding the FreeRTOS Add-In
==================================

CCES Headless Builder also provides a way for the user to manage the Add-Ins (e.g. query the available Add-Ins, add, remove and upgrade them from projects in an automated fashion) via the Command Line. So we can use this approach to add the FreeRTOS Add-In to the project we created before to setup the FreeRTOS necessary configurations for this project.

--------------

Query the Available Add-Ins Information (Optional)
--------------------------------------------------

CCES have supported querying the add-ins that are allowed to be installed into an existing project. With this functionality, the user can easily get a list of add-ins which are available and so that help them to manage the add-ins better. The related options are:

+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name  | Description                                                                                                                                                          |
+==============+======================================================================================================================================================================+
| -command     | **``'availableaddins``'** for querying the available Add-Ins for a project.                                                                                          |
+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -project     | In this case, this option specifies the path of a project which we will query the available Add-Ins for.                                                             |
+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -output-file | [Optional] The local path of a file where the add-ins data is going to be emitted. If this option is not specified, the meta data will be print out to standard out. |
+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example and Command Syntax:**

Whit the early created CCES projects of ADSP-SC589-EZKIT and aiming to add the FreeRTOS Add-In for SHARC Core 1, now we query the available Add-Ins information of **FRTOS_Demo_SC589_Core1** via below command and save the result into "*C:\\freertos_command_line_examples\\cces_tools\\addins.json*":

.. code:: batch

   @ECHO --------------Querying the available Add-Ins for SHARC Core 1--------------
   @CD "C:\Analog Devices\CrossCore Embedded Studio 2.10.0\Eclipse"
   @SET project_path1="C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core1"
   @SET addins_json_file="C:\freertos_command_line_examples\cces_tools\addins.json"
   ccesc.exe^
       -nosplash^
       -application com.analog.crosscore.headlesstools^
       -command availableaddins^
       -data c:/workspace^
       -project %project_path1%^
       -output-file %addins_json_file%

**CMD executable Command:**

.. code:: batch

   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools  -command availableaddins -data c:/workspace -project "C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core1" -output-file "C:\freertos_command_line_examples\cces_tools\addins.json"

The headless builder will show below results information if our querying request has been executed successfully.


|image1|

.. container:: centeralign

   **Diagram 2-1** Querying the Available Add-Ins Information


   |image2|

.. container:: centeralign

   **Diagram 2-2** Available Add-Ins Information JSON File


The generated available add-ins' information is organized in JSON format. Each add-in entry uses its add-in Id as key. The values are [ status, name, version ]. An example:

.. code:: java

   {
      "add-ins" : {
         "com.analog.crosscore.ssldd.pinmux.component" : {
            "name" : "Pin Multiplexing",
            "version" : "1.0.0",
            "status" : "available"
         },
         "com.analog.crosscore.sru.component" : {
            "name" : "SRU Configuration",
            "version" : "1.0.0",
            "status" : "available"
         },
         "com.analog.crosscore.addins.sc58x_ez_kit.adau1979" : {
            "name" : "Quad Analog-to-Digital Converter (ADAU1979) Driver",
            "version" : "2.0.2",
            "status" : "available"
         },
         "com.analog.crosscore.addins.sc58x_ez_kit.adau1962a" : {
            "name" : "12-Channel, 192 kHz, 24-Bit DAC (ADAU1962A) Driver",
            "version" : "2.0.2",
            "status" : "available"
         },
         "com.analog.crosscore.addins.sc58x_ez_kit.ina3221" : {
            "name" : "Shunt and Bus Voltage Monitor (INA3221) Driver",
            "version" : "2.0.2",
            "status" : "available"
         },
         "com.analog.micrium.ucos3.sharc" : {
            "name" : "uCOS-III for SHARC",
            "version" : "2.9.0",
            "status" : "available"
         },
         "com.analog.crosscore.addins.sc58x_ez_kit.adau1977" : {
            "name" : "Quad ADC with Diagnostics (ADAU1977) Driver",
            "version" : "2.0.2",
            "status" : "available"
         },
         "com.analog.sourcegen.component.startup_ldf" : {
            "name" : "Startup Code/LDF",
            "version" : "1.0.0",
            "status" : "available"
         },
         "com.analog.crosscore.addins.freertos.sharc" : {
            "name" : "FreeRTOS for SHARC",
            "version" : "1.0.0",
            "status" : "available"
         },
         "com.analog.crosscore.addins.mcapi" : {
            "name" : "Analog Devices' MCAPI",
            "version" : "1.0.0",
            "status" : "available"
         }
      }
   }

--------------

Adding FreeRTOS Add-In to Project
---------------------------------

The Add-In management functionality of Headless Builder can be achieved by using the options as follows:

+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name  | Description                                                                                                                                                                                 |
+==============+=============================================================================================================================================================================================+
| -command     | Specify the action type.                                                                                                                                                                    |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | **``'addaddin``'** for adding an Add-in to a project;                                                                                                                                       |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | **``'overbidding``'** for removing an Add-in from a project;                                                                                                                                |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | **``'upgradeaddin``'** for upgrading an Add-in in a project;                                                                                                                                |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | **``'upgradeall``'** for upgrading all Add-ins which have been installed in the project to the latest supported versions.                                                                   |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -fromversion | [Optional] The installed addin version (only for command "upgradeaddin"). If it is not specified, the version of the Add-In that is installed in the project is regarded as '-fromversion'. |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -id          | The addin id                                                                                                                                                                                |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -toversion   | The to-be-upgraded addin version (only for command "upgradeaddin"). 'latest' can be selected to upgrade an Add-In to its latest version.                                                    |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -version     | The addin version (only for command "addaddin"). 'latest' can be selected to add an Add-In that has the latest version.                                                                     |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example and Command Syntax of adding the FreeRTOS Add-in:**

According to the about Add-Ins information, now we can add the FreeRTOS Add-Ins for SHARC Cores via below commands:

.. code:: batch

   @TITLE Step 2 Adding the FreeRTOS Add-In
   @CD "C:\Analog Devices\CrossCore Embedded Studio 2.10.0\Eclipse"
   @ECHO --------------Adding the FreeRTOS Add-In for SHARC Core 1--------------
   @SET project_path1="C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core1"
   ccesc.exe^
       -nosplash^
       -application com.analog.crosscore.headlesstools^
       -command addaddin^
       -data "c:/workspace"^
       -project %project_path1%^
       -id com.analog.crosscore.addins.freertos.sharc^
       -version 1.0.0
   @PAUSE

**CMD executable Command:**

.. code:: batch

   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools -command addaddin -data "c:/workspace" -project "C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core1" -id com.analog.crosscore.addins.freertos.sharc -version 1.0.0

The headless builder will show below results information if the Add-In has been installed successfully.


|image3|

.. container:: centeralign

   **Diagram 2-4** Adding FreeRTOS Add-Ins


And the Generated and cloned FreeRTOS Source can be found in the corresponding folder of SHARC Core 1 project:



|image4|

.. container:: centeralign

   **Diagram 2-5** Generated and cloned FreeRTOS Source


.. note::

   **To Do** add the examples of overbidding upgradeaddin upgradeall usage if necessary


--------------

**HOME:** `Getting Started <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/tools/cces-tools/freertos-add-in-usage-with-cces-tools-from-command-line>`__ **PREV:** :doc:`Step 1. Creating a New CCES Project </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/cces-tools/creating-a-new-cces-project>` **NEXT:** :doc:`Step 3. Customizing the Project </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/cces-tools/customizing-the-project>`

--------------

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/002-1_headless_tools_results_query_available_add-ins.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/002-2_json_file_of_querying_available_add-ins.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/002-3_headless_tools_results_add_freertos_add-in.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/002-4_generated_and_cloned_freertos_source_file.png
