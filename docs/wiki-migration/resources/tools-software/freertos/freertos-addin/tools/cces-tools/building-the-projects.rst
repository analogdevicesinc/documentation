Step 4. Building the Projects
=============================

Analog Devices' CCES headless builder provides a couple of options to support building projects and changing tool options from command line with better usability. Users could specify the building configuration (e.g. specify the mode is **``DEBUG``**, **``RELEASE``** or **``ALL``** ) according their own requirements.

--------------

Importing & Copying Projects to Workspace (Optional)
----------------------------------------------------

This is an Optional step for users who would like to import or copy the existing projects to the specified workspace.

+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name                    | Description                                                                                                                                                            |
+================================+========================================================================================================================================================================+
| -copy                          | Specify whether project copying is required, which is used to allow user to copy a project to the current workspace                                                    |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -data                          | Specify the path of workspace where to store the to-be-imported projects                                                                                               |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -project                       | Specify the local path of a project that is going to be imported or copied to the workspace. **Note:** This path can be either absolute or relative                    |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -example [ examples.xml path ] | This option is used when copying an example project. It specify the local path of a examples.xml that usually contains <copy-actions /> node which defines finer-grain |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example and Command Syntax:**

.. code:: batch

   @CD "C:\"
   rd /s/q worksapce
   @CD "C:\Analog Devices\CrossCore Embedded Studio 2.10.0\Eclipse"
   @ECHO -------------- Importing and Copying the project into workspace --------------
   @SET project_path0="C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core0"
   ccesc.exe^
        -nosplash^
        -application com.analog.crosscore.headlesstools^
        -copy^
        -data c:/workspace^
        -project %project_path0%
   @SET project_path1="C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core1"
   ccesc.exe^
        -nosplash^
        -application com.analog.crosscore.headlesstools^
        -copy^
        -data c:/workspace^
        -project %project_path1%
   @PAUSE

**CMD executable Command:**

.. code:: batch

   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools  -copy  -data "c:/workspace" -project "C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core0"
   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools  -copy  -data "c:/workspace" -project "C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core1"

The headless builder will show below results information if the projects have been importing and copying into specified workspace successfully.


|image1|

.. container:: centeralign

   **Diagram 4-1** Importing Core 0 Project Into Workspace


   |image2|

.. container:: centeralign

   **Diagram 4-2** Importing Core 1 Project Into Workspace


And also we can check the Importing results in the path of the specified workspace.



|image3|

.. container:: centeralign

   **Diagram 4-3** Importing Projects Into Workspace


--------------

Building Projects
-----------------

the Options and descriptions of building projects feature in CCES headless builder are shown below:

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name                       | Description                                                                                                                                           |
+===================================+=======================================================================================================================================================+
| -build [ all or configName ]      | Builds all configurations or the named configuration of the project.Generally, this config name can be **``Debug``**, **``Release``** or **``All``**. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| -cleanOnly [ all or configName ]  | Cleans all configurations or the named configuration of the project.                                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| -cleanBuild [ all or configName ] | Cleans and builds all configurations or the named configuration of the project.                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| -regensrc                         | Forces all system add-ins to recreate generated files. Add-ins that have already been installed in this project.                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example and Command Syntax:**

.. code:: batch

   @TITLE Step 4 Building the FreeRTOS Add-In Projects
   @CD "C:\Analog Devices\CrossCore Embedded Studio 2.10.0\Eclipse"
   @ECHO --------------Building the the project of Core 0 --------------
   ccesc.exe^
       -nosplash^
       -application com.analog.crosscore.headlesstools^
       -cleanBuild Debug^
       -regensrc^
       -data "c:\workspace"^
       -project "c:\workspace\FRTOS_Demo_SC589_Core0"^
       -consoleLog
   @ECHO --------------Building the the project of Core 1 --------------
   ccesc.exe^
       -nosplash^
       -application com.analog.crosscore.headlesstools^
       -cleanBuild Debug^
       -regensrc^
       -data "c:\workspace"^
       -project "c:\workspace\FRTOS_Demo_SC589_Core1"^
       -consoleLog
   @PAUSE

**CMD executable Command:**

.. code:: batch

   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools -cleanBuild Debug -consoleLog -regensrc -data "c:\workspace" -project "c:\workspace\FRTOS_Demo_SC589_Core0"
   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools -cleanBuild Debug -consoleLog -regensrc -data "c:\workspace" -project "c:\workspace\FRTOS_Demo_SC589_Core1"

The headless builder will show below results information if the project is successfully.


|image4|

.. container:: centeralign

   **Diagram 4-4** Building Core 0 project


   |image5|

.. container:: centeralign

   **Diagram 4-5** Building Core 1 Project


Also, you can check the target binary file "FRTOS_ADSP589_Test.dxe" has been build successfully in the Debug/Release folder.



|image6|

.. container:: centeralign

   **Diagram 4-6** Result of Building Core 0 Project


   |image7|

.. container:: centeralign

   **Diagram 4-7** Result of Building Core 1 Project


.. note::

   TO confirm: could we build the Three-core project in one command?


--------------

**HOME:** `Getting Started <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/tools/cces-tools/freertos-add-in-usage-with-cces-tools-from-command-line>`__ **PREV:** :doc:`Step 3. Customizing the Project (optional) </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/cces-tools/customizing-the-project>` **NEXT:** :doc:`Step 5. Downloading and Running </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/cces-tools/downloading-and-running>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/004-1_headless_tools_results_import_project_to_workspace_core0.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/004-2_headless_tools_results_import_project_to_workspace_core1.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/004-3_importing_projects_into_workspace.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/004-4_headless_tools_results_build_the_project_core0.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/004-5_headless_tools_results_build_the_project_core1.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/004-6_building_the_project_core0.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/004-7_building_the_project_core1.png
