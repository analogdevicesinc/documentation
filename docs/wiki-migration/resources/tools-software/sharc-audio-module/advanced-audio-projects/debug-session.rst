Setting Up a Debug Session
==========================

*The following instructions will help you establish a debug session for the audio starter projects.*

Overview
--------

Once your audio starter project has been set up and you have started making
modifications to the software, you may want to load the software onto the target
and step through the code to view the code execution. Setting up a debug session
in Cross Core Embedded Studio will help with this.

*Note that these instructions are limited and only explain the setup items which are specific for the audio starter projects. For more in-depth Cross Core tutorials and how to use the full capabilities of the debugger, refer to the*\ :adi:`Documentation & Resources for CCES <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html#software-requirement>`

--------------

Debug Session - ADZS-SC584-EZLITE
---------------------------------

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 1. Open Cross Core Embedded Studio and select your preferred workspace.                                                                                                                                                                                                                                                               | |image19|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 2. Select the bug icon carrot and select *Debug Configurations*.                                                                                                                                                                                                                                                                      | |image20|\ |image21| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 3. Press the *New Launch Configuration* button in the upper left corner.                                                                                                                                                                                                                                                              | |image22|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 4. Under *Processor family*, select *SHARC* and under *Processor type*, select, // ADSP-SC584// and select *Next*.                                                                                                                                                                                                                    | |image23|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 5. Under *Select Connection Type*, choose *Emulator* and select *Next*.                                                                                                                                                                                                                                                               | |image24|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 6. Under *Select Platform*, choose *ADSP-SC584 via ICE-2000* and select *Finish* (Or select *ICE-1000* if using this debugger).                                                                                                                                                                                                       | |image25|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 7. Update the *Name* of your debug configuration to something useful.                                                                                                                                                                                                                                                                 | |image26|            |
| *Note that this debug configuration will be saved in your workspace as long as you reopen CCES using the same workspace. This is helpful so a new debug configuration does not need to be setup every time that CCES is closed/re-opened.*                                                                                            |                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 8. In the *Program window, Device 0 Core 0* (This is the ARM core), there will be **TWO** executables to load: The preload file which loads the startup code and the application file. Select the following (by double clicking->Program->Browse), with the following options:                                                        | |image27| |image28|  |
| **<project_location>/build/ezkitSC584_preload_core0_v10**                                                                                                                                                                                                                                                                             |                      |
| *Reset core before load - Checked*                                                                                                                                                                                                                                                                                                    |                      |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                      |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                      |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                      |
| **<project_location>/build/SAM-Audio-Starter-ARM.exe**                                                                                                                                                                                                                                                                                |                      |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                        |                      |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                      |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                      |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 9. In the *Program* window, *Device 0 Core 1* (This is the *first* SHARC core), there will be **ONE** executable to load: The *application* file. Select the following (by double-clicking->Program->Browse), with the following options:                                                                                             | |image29|            |
| **<project_location>/build/SAM-Audio-Starter-SHARC0.dxe**                                                                                                                                                                                                                                                                             |                      |
| *Reset core before load - Checked*                                                                                                                                                                                                                                                                                                    |                      |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                        |                      |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                      |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                      |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 10. In the *Program* window, *Device 0 Core 2* (This is the *second* SHARC core), there will be **ONE** executable to load: The *application* file. Select the following (by double-clicking->Program->Browse), with the following options:                                                                                           | |image30|            |
| **<project_location>/build/SAM-Audio-Starter-SHARC1.dxe**                                                                                                                                                                                                                                                                             |                      |
| *Reset core before load - Checked*                                                                                                                                                                                                                                                                                                    |                      |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                        |                      |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                      |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                      |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 11. Under *Automatic Breakpoints*, **DISABLE (Uncheck)** Enable semihosting*.                                                                                                                                                                                                                                                         | |image31|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 12. In order for audio input/output routing to function from a debug session, the breakpoints at *main* for *Core 1* and *Core 2 **MUST** be disabled. Otherwise, if you are debugging normally by stepping through code, these can remain enabled.                                                                                   | |image32|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 13. Assuming that your board is powered up (Green LED) and your debugger is connected to the board and to a USB slot on your PC (Green LED on debugger), you can hit *Apply* and *Debug* to start the debug session. If everything is functional, the debugger will halt the cores and start at the start of *main* for the ARM core. | |image33| |image34|  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 14. To run the code, press the *Resume (F5)* play button. Or to start stepping through the code, hit the *Step (F10)* button.                                                                                                                                                                                                         | |image35| |image36|  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

Debug Session - ADZS-SC589-MINI
-------------------------------

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 1. Open Cross Core Embedded Studio and select your preferred workspace.                                                                                                                                                                                                                                                               | |image55|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 2. Select the bug icon carrot and select *Debug Configurations*.                                                                                                                                                                                                                                                                      | |image56|\ |image57| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 3. Press the *New Launch Configuration* button in the upper left corner.                                                                                                                                                                                                                                                              | |image58|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 4. Under *Processor family*, select *SHARC* and under *Processor type*, select, // ADSP-SC589// and select *Next*.                                                                                                                                                                                                                    | |image59|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 5. Under *Select Connection Type*, choose *Emulator* and select *Next*.                                                                                                                                                                                                                                                               | |image60|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 6. Under *Select Platform*, choose *ADSP-SC589 via ICE-2000* and select *Finish* (Or select *ICE-1000* if using this debugger).                                                                                                                                                                                                       | |image61|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 7. Update the *Name* of your debug configuration to something useful.                                                                                                                                                                                                                                                                 | |image62|            |
| *Note that this debug configuration will be saved in your workspace as long as you reopen CCES using the same workspace. This is helpful so a new debug configuration does not need to be setup every time that CCES is closed/re-opened.*                                                                                            |                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 8. In the *Program window, Device 0 Core 0* (This is the ARM core), there will be **TWO** executables to load: The preload file which loads the startup code and the application file. Select the following (by double clicking->Program->Browse), with the following options:                                                        | |image63| |image64|  |
| **<CCES Installation Location>/SHARC/ldr/ezkitSC589_preload_core0_v01**                                                                                                                                                                                                                                                               |                      |
| *Reset core before load - Checked*                                                                                                                                                                                                                                                                                                    |                      |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                      |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                      |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                      |
| **<project_location>/build/SAM-Audio-Starter-ARM.exe**                                                                                                                                                                                                                                                                                |                      |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                        |                      |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                      |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                      |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 9. In the *Program* window, *Device 0 Core 1* (This is the *first* SHARC core), there will be **ONE** executable to load: The *application* file. Select the following (by double-clicking->Program->Browse), with the following options:                                                                                             | |image65|            |
| **<project_location>/build/SAM-Audio-Starter-SHARC0.dxe**                                                                                                                                                                                                                                                                             |                      |
| *Reset core before load - Checked*                                                                                                                                                                                                                                                                                                    |                      |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                        |                      |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                      |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                      |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 10. In the *Program* window, *Device 0 Core 2* (This is the *second* SHARC core), there will be **ONE** executable to load: The *application* file. Select the following (by double-clicking->Program->Browse), with the following options:                                                                                           | |image66|            |
| **<project_location>/build/SAM-Audio-Starter-SHARC1.dxe**                                                                                                                                                                                                                                                                             |                      |
| *Reset core before load - Checked*                                                                                                                                                                                                                                                                                                    |                      |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                        |                      |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                      |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                      |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 11. Under *Automatic Breakpoints*, **DISABLE (Uncheck)** Enable semihosting*.                                                                                                                                                                                                                                                         | |image67|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 12. In order for audio input/output routing to function from a debug session, the breakpoints at *main* for *Core 1* and *Core 2 **MUST** be disabled. Otherwise, if you are debugging normally by stepping through code, these can remain enabled.                                                                                   | |image68|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 13. Assuming that your board is powered up (Green LED) and your debugger is connected to the board and to a USB slot on your PC (Green LED on debugger), you can hit *Apply* and *Debug* to start the debug session. If everything is functional, the debugger will halt the cores and start at the start of *main* for the ARM core. | |image69| |image70|  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 14. To run the code, press the *Resume (F5)* play button. Or to start stepping through the code, hit the *Step (F10)* button.                                                                                                                                                                                                         | |image71| |image72|  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

Debug Session - EV-SC594-SOM + Carrier
--------------------------------------

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 1. Open Cross Core Embedded Studio and select your preferred workspace.                                                                                                                                                                                                                                                               | |image91|             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 2. Select the bug icon carrot and select *Debug Configurations*.                                                                                                                                                                                                                                                                      | |image92|\ |image93|  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 3. Press the *New Launch Configuration* button in the upper left corner.                                                                                                                                                                                                                                                              | |image94|             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 4. Under *Processor family*, select *SHARC* and under *Processor type*, select, // ADSP-SC594// and select *Next*.                                                                                                                                                                                                                    | |image95|             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 5. Under *Select Connection Type*, choose *Emulator* and select *Next*.                                                                                                                                                                                                                                                               | |image96|             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 6. Under *Select Platform*, choose *ADSP-SC594 via ICE-2000* and select *Finish* (Or select *ICE-1000* if using this debugger).                                                                                                                                                                                                       | |image97|             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 7. Update the *Name* of your debug configuration to something useful.                                                                                                                                                                                                                                                                 | |image98|             |
| *Note that this debug configuration will be saved in your workspace as long as you reopen CCES using the same workspace. This is helpful so a new debug configuration does not need to be setup every time that CCES is closed/re-opened.*                                                                                            |                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 8. In the *Program window, Device 0 Core 0* (This is the ARM core), there will be **TWO** executables to load: The preload file which loads the startup code and the application file. Select the following (by double clicking->Program->Browse), with the following options:                                                        | |image99| |image100|  |
| **<project_location>/build/ezkitSC594W_preload_core0**                                                                                                                                                                                                                                                                                |                       |
| *Reset core before load - Checked*                                                                                                                                                                                                                                                                                                    |                       |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                       |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                       |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                       |
| **<project_location>/build/EV-SC594-EZKIT-ARM.exe**                                                                                                                                                                                                                                                                                   |                       |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                        |                       |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                       |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                       |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 9. In the *Program* window, *Device 0 Core 1* (This is the *first* SHARC core), there will be **ONE** executable to load: The *application* file. Select the following (by double-clicking->Program->Browse), with the following options:                                                                                             | |image101|            |
| **<project_location>/build/EV-SC594-EZKIT-SHARC0.dxe**                                                                                                                                                                                                                                                                                |                       |
| *Reset core before load - Checked*                                                                                                                                                                                                                                                                                                    |                       |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                        |                       |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                       |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                       |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 10. In the *Program* window, *Device 0 Core 2* (This is the *second* SHARC core), there will be **ONE** executable to load: The *application* file. Select the following (by double-clicking->Program->Browse), with the following options:                                                                                           | |image102|            |
| **<project_location>/build/EV-SC594-EZKIT-SHARC1.dxe**                                                                                                                                                                                                                                                                                |                       |
| *Reset core before load - Checked*                                                                                                                                                                                                                                                                                                    |                       |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                        |                       |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                |                       |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                |                       |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                         |                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 11. Under *Automatic Breakpoints*, **DISABLE (Uncheck)** Enable semihosting*.                                                                                                                                                                                                                                                         | |image103|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 12. In order for audio input/output routing to function from a debug session, the breakpoints at *main* for *Core 1* and *Core 2 **MUST** be disabled. Otherwise, if you are debugging normally by stepping through code, these can remain enabled.                                                                                   | |image104|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 13. Assuming that your board is powered up (Green LED) and your debugger is connected to the board and to a USB slot on your PC (Green LED on debugger), you can hit *Apply* and *Debug* to start the debug session. If everything is functional, the debugger will halt the cores and start at the start of *main* for the ARM core. | |image105|            |
|                                                                                                                                                                                                                                                                                                                                       | |image106|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| 14. To run the code, press the *Resume (F5)* play button. Or to start stepping through the code, hit the *Step (F10)* button.                                                                                                                                                                                                         | |image107| |image108| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+

Debug Session - EV-SC598-SOM + Carrier
--------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 1. Open Cross Core Embedded Studio and select your preferred workspace.                                                                                                                                                                                                                                                                 | |image140|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 2. Select the bug icon carrot and select *Debug Configurations*.                                                                                                                                                                                                                                                                        | |image141|\ |image142| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 3. **Debug Configuration for ARM Preload Code**                                                                                                                                                                                                                                                                                         | |image143|             |
| Under *Application with GDB and OpenOCD (Emulator)* Press the *New Launch Configuration* button in the upper left corner.                                                                                                                                                                                                               |                        |
| Provide a useful name for the configuration (Preload) as it will be used in subsequent steps.                                                                                                                                                                                                                                           |                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 4. Select the *Target (processor)* box and choose *Analog Devices ADSP-SC59x (Cortex-A55)*.                                                                                                                                                                                                                                             | |image144|             |
| Under *Reset options* select *System Reset*.                                                                                                                                                                                                                                                                                            |                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 5. In the *Main* tab, point the // C/C++ Application// to *<build>\\ezkitSC598W_preload_core0*.                                                                                                                                                                                                                                         | |image145|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 6. In the *Startup* tab, delete the *monitor arm semihosting_fileio enable* from the *Initialization Commands.*                                                                                                                                                                                                                         | |image146|             |
| Select *Apply* to save the configuration.                                                                                                                                                                                                                                                                                               | |image147|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 7. **Debug Configuration for ARM Application Code**                                                                                                                                                                                                                                                                                     | |image148|             |
| Under *Application with GDB and OpenOCD (Emulator)* Press the *New Launch Configuration* button in the upper left corner.                                                                                                                                                                                                               |                        |
| Provide a useful name for the configuration (Application) as it will be used in subsequent steps.                                                                                                                                                                                                                                       |                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 8. Select the *Target (processor)* box and choose *Analog Devices ADSP-SC59x (Cortex-A55)*.                                                                                                                                                                                                                                             | |image149|             |
| Under *Reset options* select *Skip Reset*.                                                                                                                                                                                                                                                                                              |                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 9. In the *Main* tab, point the application to *<build>\\EV-SC598-EZKIT-ARM.exe*.                                                                                                                                                                                                                                                       | |image150|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 10. In the *Startup* tab, delete the *monitor arm semihosting_fileio enable* from the *Initialization Commands.*                                                                                                                                                                                                                        | |image151|             |
| Select *Apply* to save the configuration.                                                                                                                                                                                                                                                                                               |                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 11. **Debug Configuration for SHARC Code**                                                                                                                                                                                                                                                                                              | |image152|             |
| Under *Application with CrossCore Debugger* Press the *New Launch Configuration* button in the upper left corner.                                                                                                                                                                                                                       |                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 12. Under *Processor family*, select *SHARC* and under\ *Processor type*, select *ADSP-SC598* and select *Next*.                                                                                                                                                                                                                        | |image153|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 13. Under *Select Connection Type*, choose *Emulator* and select Next.                                                                                                                                                                                                                                                                  | |image154|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 14. Under *Select Platform*, choose *ADSP-SC598 via ICE-2000* and select *Finish* (Or select *ICE-1000* if using this debugger).                                                                                                                                                                                                        | |image155|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 15. Update the Name of your debug configuration to something useful (SHARCS).                                                                                                                                                                                                                                                           | |image156|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 16. In the *Program* window, *Device 0 Core 1* (This is the *first* SHARC core), there will be **ONE** executable to load: The application file. Select the following (by double-clicking→Program→Browse), with the following options:                                                                                                  | |image157|             |
| **<project_location>/build/EV-SC598-EZKIT-SHARC0.dxe**                                                                                                                                                                                                                                                                                  |                        |
| *Reset core before load - Unchecked*                                                                                                                                                                                                                                                                                                    |                        |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                          |                        |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                  |                        |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                  |                        |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                           |                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 17. In the *Session* tab, select the preload file in *Device 0 [Core 1]* and select *Remove*.                                                                                                                                                                                                                                           | |image158|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 18. In the *Program* window, *Device 0 Core 2* (This is the *second* SHARC core), there will be **ONE** executable to load: The application file. Select the following (by double-clicking→Program→Browse), with the following options:                                                                                                 | |image159|             |
| **<project_location>/build/EV-SC598-EZKIT-SHARC1.dxe**                                                                                                                                                                                                                                                                                  |                        |
| *Reset core before load - Unchecked*                                                                                                                                                                                                                                                                                                    |                        |
| *Check silicon revision before load - Checked*                                                                                                                                                                                                                                                                                          |                        |
| *Run immediately after load - Checked*                                                                                                                                                                                                                                                                                                  |                        |
| *All others unchecked*                                                                                                                                                                                                                                                                                                                  |                        |
| *Working Directory = Default*                                                                                                                                                                                                                                                                                                           |                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 19. In order for audio input/output routing to function from a debug session, the breakpoints at *main* for Core 1 and Core 2 **MUST** be disabled. Otherwise, if you are debugging normally by stepping through code, these can remain enabled.                                                                                        | |image160|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 20. **Set up configuration for multi-core launch group**                                                                                                                                                                                                                                                                                | |image161|             |
| Under *Application with CrossCore Launch Group*, Press the *New Launch Configuration* button in the upper left corner.                                                                                                                                                                                                                  |                        |
| When the *Select Processor* pops up, select *ADSP-SC598* under *Processor type*. Select *Next*.                                                                                                                                                                                                                                         |                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 21. In the *Select Interface* window, choose *Target (processor)* and *ICE-2000 Emulator* (Or *ICE-1000*) and select *Next*.                                                                                                                                                                                                            | |image162|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 22. In the *Select Debug Configurations* window, select *Skip Configuration* for **ARM**. For **SHARC**, select *Use an existing debug configuration* and choose your SHARC debug configuration from the previous steps and select *Finish*.                                                                                            | |image163|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 23. In the *Launches* tab, select *Add*. In the pop-up window, expand the *Application with GDB and OpenOCD (Emulator)* and select the ARM application debug configuration that was created earlier. Ensure that the ARM debug configuration comes before the SHARC configuration by selecting the *Up* or *Down* buttons. Select *OK*. | |image164|             |
|                                                                                                                                                                                                                                                                                                                                         | |image165|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 24. Assuming that your board is powered up (Green LED) and your debugger is connected to the board and to a USB slot on your PC (Green LED on debugger), select the preload debug configuration and select *Debug*.                                                                                                                     | |image166|             |
| *Note we will use the launch group next.*                                                                                                                                                                                                                                                                                               |                        |
| If everything is functional, the debugger will halt the cores and start at the start of main for the preload code.                                                                                                                                                                                                                      |                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 25. Run the code by pressing the Resume (F5) play button. Once the code hits the *exit* routine, end the debug session.                                                                                                                                                                                                                 | |image167|             |
|                                                                                                                                                                                                                                                                                                                                         | |image168|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 26. Select *Debug Configurations* and select the launch group that was created previously and select *Debug*. This will load your main ARM + SHARC application session.                                                                                                                                                                 | |image169|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| 27. If everything loaded correctly, the debugger will halt at ARM main and both ARM + SHARC processes will be visible in the Debug window.                                                                                                                                                                                              | |image170|             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+

.. important::

   Having trouble? Check out our list of :doc:`common issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`!

--------------

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces.png
   :width: 600
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces26.png
   :width: 200
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces1.png
   :width: 600
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces2.png
   :width: 600
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces3.png
   :width: 600
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces4.png
   :width: 600
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces5.png
   :width: 600
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces6.png
   :width: 600
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces7.png
   :width: 600
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces8.png
   :width: 600
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces9.png
   :width: 600
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces10.png
   :width: 600
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces11.png
   :width: 600
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces12.png
   :width: 600
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces13.png
   :width: 600
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces14.png
   :width: 400
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces24.png
   :width: 400
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces25.png
   :width: 400
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces.png
   :width: 600
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces26.png
   :width: 200
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces1.png
   :width: 600
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces2.png
   :width: 600
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces3.png
   :width: 600
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces4.png
   :width: 600
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces5.png
   :width: 600
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces6.png
   :width: 600
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces7.png
   :width: 600
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces8.png
   :width: 600
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces9.png
   :width: 600
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces10.png
   :width: 600
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces11.png
   :width: 600
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces12.png
   :width: 600
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces13.png
   :width: 600
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces14.png
   :width: 400
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces24.png
   :width: 400
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces25.png
   :width: 400
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces.png
   :width: 600
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces26.png
   :width: 200
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces1.png
   :width: 600
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces2.png
   :width: 600
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces15.png
   :width: 600
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces4.png
   :width: 600
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces16.png
   :width: 600
.. |image44| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces17.png
   :width: 600
.. |image45| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces18.png
   :width: 600
.. |image46| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces19.png
   :width: 600
.. |image47| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces20.png
   :width: 600
.. |image48| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces21.png
   :width: 600
.. |image49| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces22.png
   :width: 600
.. |image50| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces12.png
   :width: 600
.. |image51| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces23.png
   :width: 600
.. |image52| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces14.png
   :width: 400
.. |image53| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces24.png
   :width: 400
.. |image54| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces25.png
   :width: 400
.. |image55| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces.png
   :width: 600
.. |image56| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces26.png
   :width: 200
.. |image57| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces1.png
   :width: 600
.. |image58| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces2.png
   :width: 600
.. |image59| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces15.png
   :width: 600
.. |image60| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces4.png
   :width: 600
.. |image61| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces16.png
   :width: 600
.. |image62| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces17.png
   :width: 600
.. |image63| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces18.png
   :width: 600
.. |image64| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces19.png
   :width: 600
.. |image65| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces20.png
   :width: 600
.. |image66| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces21.png
   :width: 600
.. |image67| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces22.png
   :width: 600
.. |image68| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces12.png
   :width: 600
.. |image69| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces23.png
   :width: 600
.. |image70| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces14.png
   :width: 400
.. |image71| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces24.png
   :width: 400
.. |image72| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces25.png
   :width: 400
.. |image73| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces.png
   :width: 400
.. |image74| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces26.png
   :width: 200
.. |image75| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces1.png
   :width: 600
.. |image76| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces2.png
   :width: 600
.. |image77| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step1.jpg
   :width: 400
.. |image78| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces4.png
   :width: 600
.. |image79| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step2.jpg
   :width: 400
.. |image80| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step3.jpg
   :width: 400
.. |image81| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step4.jpg
   :width: 400
.. |image82| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step5.jpg
   :width: 400
.. |image83| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step6.jpg
   :width: 400
.. |image84| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step7.jpg
   :width: 400
.. |image85| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step9.jpg
   :width: 400
.. |image86| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step10.jpg
   :width: 400
.. |image87| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step8.jpg
   :width: 400
.. |image88| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces14.png
   :width: 400
.. |image89| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces24.png
   :width: 400
.. |image90| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces25.png
   :width: 400
.. |image91| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces.png
   :width: 400
.. |image92| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces26.png
   :width: 200
.. |image93| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces1.png
   :width: 600
.. |image94| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces2.png
   :width: 600
.. |image95| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step1.jpg
   :width: 400
.. |image96| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces4.png
   :width: 600
.. |image97| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step2.jpg
   :width: 400
.. |image98| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step3.jpg
   :width: 400
.. |image99| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step4.jpg
   :width: 400
.. |image100| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step5.jpg
   :width: 400
.. |image101| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step6.jpg
   :width: 400
.. |image102| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step7.jpg
   :width: 400
.. |image103| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step9.jpg
   :width: 400
.. |image104| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step10.jpg
   :width: 400
.. |image105| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step8.jpg
   :width: 400
.. |image106| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces14.png
   :width: 400
.. |image107| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces24.png
   :width: 400
.. |image108| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces25.png
   :width: 400
.. |image109| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces.png
   :width: 400
.. |image110| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces26.png
   :width: 200
.. |image111| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces1.png
   :width: 600
.. |image112| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug.jpg
   :width: 400
.. |image113| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug1.jpg
   :width: 400
.. |image114| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug2.jpg
   :width: 400
.. |image115| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug3.jpg
   :width: 400
.. |image116| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug4.jpg
   :width: 400
.. |image117| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug.jpg
   :width: 400
.. |image118| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug5.jpg
   :width: 400
.. |image119| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug6.jpg
   :width: 400
.. |image120| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug7.jpg
   :width: 400
.. |image121| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug9.jpg
   :width: 400
.. |image122| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug10.jpg
   :width: 400
.. |image123| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces4.png
   :width: 400
.. |image124| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug11.jpg
   :width: 400
.. |image125| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug12.jpg
   :width: 400
.. |image126| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug13.jpg
   :width: 400
.. |image127| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug14.jpg
   :width: 400
.. |image128| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug15.jpg
   :width: 400
.. |image129| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug16.jpg
   :width: 400
.. |image130| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug26.jpg
   :width: 400
.. |image131| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug27.jpg
   :width: 400
.. |image132| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug28.jpg
   :width: 400
.. |image133| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug20.jpg
   :width: 400
.. |image134| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug29.jpg
   :width: 400
.. |image135| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug22.jpg
   :width: 400
.. |image136| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces24.jpg
   :width: 400
.. |image137| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug23.jpg
   :width: 400
.. |image138| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug24.jpg
   :width: 400
.. |image139| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug25.jpg
   :width: 400
.. |image140| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces.png
   :width: 400
.. |image141| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces26.png
   :width: 200
.. |image142| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces1.png
   :width: 600
.. |image143| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug.jpg
   :width: 400
.. |image144| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug1.jpg
   :width: 400
.. |image145| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug2.jpg
   :width: 400
.. |image146| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug3.jpg
   :width: 400
.. |image147| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug4.jpg
   :width: 400
.. |image148| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug.jpg
   :width: 400
.. |image149| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug5.jpg
   :width: 400
.. |image150| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug6.jpg
   :width: 400
.. |image151| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug7.jpg
   :width: 400
.. |image152| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug9.jpg
   :width: 400
.. |image153| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug10.jpg
   :width: 400
.. |image154| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces4.png
   :width: 400
.. |image155| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug11.jpg
   :width: 400
.. |image156| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug12.jpg
   :width: 400
.. |image157| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug13.jpg
   :width: 400
.. |image158| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug14.jpg
   :width: 400
.. |image159| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug15.jpg
   :width: 400
.. |image160| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug16.jpg
   :width: 400
.. |image161| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug26.jpg
   :width: 400
.. |image162| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug27.jpg
   :width: 400
.. |image163| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug28.jpg
   :width: 400
.. |image164| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug20.jpg
   :width: 400
.. |image165| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug29.jpg
   :width: 400
.. |image166| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug22.jpg
   :width: 400
.. |image167| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces24.jpg
   :width: 400
.. |image168| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug23.jpg
   :width: 400
.. |image169| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug24.jpg
   :width: 400
.. |image170| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_debug25.jpg
   :width: 400
