Step 5. Downloading and Running
===============================

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


|image1|

.. container:: centeralign

   **Diagram 5-1** CCES Runner Available Commands


**Example and Command Syntax:**

.. code:: batch

   @TITLE Step 5 Downloading and Running
   @CD "C:\Analog Devices\CrossCore Embedded Studio 2.10.0"
   CCES_runner.exe^
       --target "Emulation Debug Target"^
       --platform "ADSP-SC589 via ICE-1000"^
       --processor "ADSP-SC589"^
       --cceshome "C:\Analog Devices\CrossCore Embedded Studio 2.10.0"^
       --core "0, CLEAR_SYMBOLS|RUN_AFTER_LOAD|SHARC\ldr\ezkitSC589_preload_core0_v01,C:\workspace\FRTOS_Demo_SC589_Core0\Debug\FRTOS_Demo_SC589_Core0"^
       --core "1,C:\workspace\FRTOS_Demo_SC589_Core1\Debug\FRTOS_Demo_SC589_Core1.dxe"
   @PAUSE

**CMD executable Command:**

.. code:: batch

   CCES_runner.exe --target "Emulation Debug Target" --platform "ADSP-SC589 via ICE-1000" --processor "ADSP-SC589" --cceshome "C:\Analog Devices\CrossCore Embedded Studio 2.10.0" --core "0, CLEAR_SYMBOLS|RUN_AFTER_LOAD|SHARC\ldr\ezkitSC589_preload_core0_v01,C:\workspace\FRTOS_Demo_SC589_Core0\Debug\FRTOS_Demo_SC589_Core0" --core "1,C:\workspace\FRTOS_Demo_SC589_Core1\Debug\FRTOS_Demo_SC589_Core1.dxe"

The console logs will be output via the CMD windows when the programs running successfully in target board:


|image2|

.. container:: centeralign

   **Diagram 5-2** Downloading and Running Results


**PREV:** :doc:`Step 4. Building the Projects </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/cces-tools/building-the-projects>` **HOME:** `Getting Started <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/tools/cces-tools/freertos-add-in-usage-with-cces-tools-from-command-line>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/005_1_cces_runner_available_commands.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/tools/cces-tools/005_2_downloading_and_running_with_console_output.png
