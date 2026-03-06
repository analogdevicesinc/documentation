====== Step 1. Creating a New CCES Project ====== CCES headless builder provides a way to create a project by command line with the parameters, i.g. We can specify the project name, the processor & silicon revision, the project type and core number of the project that is to be created. The related options we can use are:

+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name   | Description                                                                                                                                            |
+===============+========================================================================================================================================================+
| -command      | Create project by meta data file if 'projectcreate' is set                                                                                             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -type         | Project type ( Executable/Static Library )                                                                                                             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -data         | In this case, this option specifies the workspace path for headless builder tool                                                                       |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -project-name | The project name of the to be created project                                                                                                          |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -project      | In this case, this option specifies the local path where the newly created project will be resides                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -processor    | The processor of the to be created project ``ADSP-BF707`` ADSP-21569 ADSP-SC573 ADSP-SC584 ADSP-SC589 ADSP-SC594                                       |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -revision     | [Optional] If omitted, adopt the default silicon revision of the specified processor                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -core         | [Optional] If omitted, choose core 0                                                                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -noinit       | [Optional] If specified, the 'system' folder and its containing adi_initialize.{h/c} files will not be created                                         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -language     | [Optional] The language of the to be created project. 'C' or 'C++'. Defaults to 'C' if the option is omitted                                           |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| -nofpu        | [Optional] Disables the FPU for the to be created project. Only applies to Cortex-M parts. If the option is omitted, the processor default FPU is used |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example and Command Syntax:**

Take the ADSP-SC589-Ezkit as an example, we create to cces projects termed as "FRTOS_Demo_SC589_Core0" and "FRTOS_Demo_SC589_Core1" for Core0 and Core1 respectively:

.. code:: batch

   @TITLE Step 1 Creating a New CCES Project
   @CD "C:\Analog Devices\CrossCore Embedded Studio 2.10.0\Eclipse"
   @ECHO --------------Create a cces projcet for sc589  core 0 --------------
   @SET project_path0="C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core0"
   ccesc.exe^
       -nosplash^
       -application com.analog.crosscore.headlesstools^
       -command projectcreate^
       -type Executable^
       -data "C:\workspace"^
       -project %project_path0%^
       -project-name "FRTOS_Demo_SC589_Core0"^
       -processor ADSP-SC589^
       -revision any^
       -core 0^
       -language C

   @ECHO --------------Create a cces projcet for sc589  core 1 --------------
   @SET project_path1="C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core1"
   ccesc.exe^
       -nosplash^
       -application com.analog.crosscore.headlesstools^
       -command projectcreate^
       -type Executable^
       -data "C:\workspace"^
       -project %project_path1%^
       -project-name "FRTOS_Demo_SC589_Core1"^
       -processor ADSP-SC589^
       -revision any^
       -core 1^
       -language C
   @PAUSE

**CMD executable Command:**

.. code:: batch

   cd "C:\Analog Devices\CrossCore Embedded Studio 2.10.0\Eclipse"
   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools -command projectcreate -type Executable -data "C:\workspace" -project "C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core0" -project-name "FRTOS_Demo_SC589_Core0" -processor ADSP-SC589 -revision any -core 0 -language C
   ccesc.exe -nosplash -application com.analog.crosscore.headlesstools -command projectcreate -type Executable -data "C:\workspace" -project "C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core1" -project-name "FRTOS_Demo_SC589_Core1" -processor ADSP-SC589 -revision any -core 1 -language C

The headless builder will show below information if the target CCES projects have been created successfully.


|image1|

.. container:: centeralign

   **Diagram 1-1** Creating CCES Project for Core 0


   |image2|

.. container:: centeralign

   **Diagram 1-2** Creating CCES Project for Core 1


Then you can find the newly created CCES projects for adsp-sc589 core0 and Core1 revision at Any have been created at the specified path: *C:\\freertos_command_line_examples\\cces_tools*



|image3|

.. container:: centeralign

   **Diagram 1-3** Newly Created CCES Projects


--------------

**HOME:** `Getting Started <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/tools/cces-tools/freertos-add-in-usage-with-cces-tools-from-command-line>`__ **NEXT:** :doc:`Step2. Adding the FreeRTOS Add-In </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/cces-tools/adding-the-freertos-add-in>`

--------------

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/001-1_headless_tools_results_create_project_core0.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/001-2_headless_tools_results_create_project_core1.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/001-3_newly_created_cces_projects_with_command_line.png
