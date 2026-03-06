:doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/executeexampleproject>`

Load Application using CCES
===========================

| 
| ===ADSP-SC573 / ADSP-SC584 / ADSP-SC589 / ADSP-SC594 Target===

-  Establish the hardware setup as described in :doc:`ADSP-215xx/ADSP-SC5xx Hardware Setup </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/adsp-215xx_and_adsp-sc5xx>`.
-  Launch CrossCore Embedded Studio.
-  Uncheck “Build (if required) before launching” checkbox in Window->Preferences->Run/Debug->Launching.
-  Select Run->Debug Configurations. The procedure debug session creation is different for SC598 compared to other SC5xx target platforms which is shown in below section. Create a new Debug configuration under ‘Application with CrossCore Debugger’. Select appropriate processor, connection type (to use On-board Debug Agent, please refer `Using SOM + SOM-CRR On-Board Debug Agent <https://wiki.analog.com/resources/tools-software/sigmastudiov2/gettingstarted/load_executable_using_cces_>`__ section) and platform. Click finish.
-  Load the prebuilt DXE’s for appropriate target ‘SS_App_Core0’ on Core 0, ‘SS_App_Core1.dxe’ on Core 1 and ‘SS_App_Core2.dxe’ on Core 2 as shown below figure. Prebuilt DXEs of each project can be found inside the respective ‘Release’ folders of each of the projects (under 'SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Demo' folder).

|image1|

-  Double click on ‘SS_App_Core1.dxe’ of Core 1 and uncheck ‘Run immediately after load’ option as shown in the below figure. Repeat the same for ‘SS_App_Core2.dxe’ for Core 2.

|image2|

-  Reset the board and press ‘Debug’ to launch the debug session. Click on “MP Resume” to run Core 0 (ARM). This enables the Core 1 and 2 (SHARC). Then individually select and run Core 1 and Core 2 by clicking on “Resume” as shown in below figure.

|image3|

-  Open SigmaStudio+ schematic.
-  Select SHARC core DXE's what is running on the target processor.

|image4|

   |image5|
-  Link compile download the SigmaStudio+ schematic if Demo or Lib integration application is used.

| 
| ===ADSP-21573 / ADSP-21584 / ADSP-21593 Target===

-  Establish the hardware setup as described in :doc:`ADSP-215xx/ADSP-SC5xx Hardware Setup </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/adsp-215xx_and_adsp-sc5xx>`.
-  Launch CrossCore Embedded Studio.
-  Uncheck “Build (if required) before launching” checkbox in Window->Preferences->Run/Debug->Launching.
-  Select Run->Debug Configurations. Create a new Debug configuration under ‘Application with CrossCore Debugger’. Select appropriate processor, connection type and platform. Click finish.
-  Load the prebuilt DXE’s for appropriate target ‘21584_preload_Core1.dxe” and “21573_preload_Core1.dxe” for 21584 and 21573 respectively, and “SS_App_Core1.dxe” on Core 1 and ‘SS_App_Core2.dxe’ on Core 2 as shown in below figure. Prebuilt DXEs of each project can be found inside the respective ‘Release’ folders of each of the projects (under 'SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Demo' folder).

|image6|

-  Double click on ‘SS_App_Core2.dxe’ of Core 2 and uncheck ‘Run immediately after load’ option as shown in below figure.

|image7|

-  Reset the board and press ‘Debug’ to launch the debug session. Click on “Resume” to run Core 1(SHARC). This enables the Core 2 (SHARC). Then individually select and run Core Core 2 by clicking on “Resume” as shown in below figure.

|image8|

-  Open SigmaStudio+ schematic.
-  Select SHARC core DXE's what is running on the target processor.

|image9|

   |image10|
-  Link compile download the SigmaStudio+ schematic if Demo or Lib integration application is used.

| 
| ===ADSP-21568 / ADSP-21569 Target===

-  Establish the hardware setup as described in :doc:`ADSP-215xx/ADSP-SC5xx Hardware Setup </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/adsp-215xx_and_adsp-sc5xx>`.
-  Launch CrossCore Embedded Studio.
-  Uncheck “Build (if required) before launching” checkbox in Window->Preferences->Run/Debug->Launching.
-  Select Run->Debug Configurations. Create a new Debug configuration under ‘Application with CrossCore Debugger’. Select appropriate processor, connection type and platform. Click finish.
-  The prebuilt DXE’s for the target ‘ezkit21569_preload.dxe” is automatically loaded on Core1. Load the prebuilt “SS_App_Core1.dxe” on Core 1. Prebuilt DXEs of each project can be found inside the respective ‘Release’ folders of each of the projects (under 'SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Demo' folder).

|image11|

-  Double click on ‘SS_App_Core1.dxe’ of Core 1 and uncheck ‘Run immediately after load’ option as shown in below figure.

|image12|

-  Reset the board and press ‘Debug’ to launch the debug session. Click on “Resume” to run Core 1(SHARC) as shown in below figure.

|image13|

-  Open SigmaStudio+ schematic.
-  Select SHARC core DXE what is running on the target processor.

|image14|

-  Link compile download the SigmaStudio+ schematic if Demo or Lib integration application is used.

| 
| ===ADSP-SC598 EV-SOM Target===

-  Establish the hardware setup as described in :doc:`ADSP-215xx/ADSP-SC5xx Hardware Setup </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/adsp-215xx_and_adsp-sc5xx>`.
-  Launch CrossCore Embedded Studio.
-  Uncheck “Build (if required) before launching” checkbox in Window->Preferences->Run/Debug->Launching.
-  Select Core0 CCES Project and go to Run->Debug Configurations. Create a new Debug configuration under ‘Application with GDB and OpenOCD(Emulaotr)’.

|image15|

-  Select appropriate emulator in "Target" Tab.

|image16|

-  Select appropriate build mode executable in the "Main" Tab and click on "Apply" and "Close".

|image17|

-  Select Core1 CCES Project and go to Run->Debug Configurations. Create a new Debug configuration under ‘Application with CrossCore Debugger’, select appropriate processor and click on Next.

|image18|

-  Select connection type as "Emulator" click on "Next" and in next window select appropriate emulator click on "Finish".

|image19|

-  Load the prebuilt DXE’s for appropriate target ‘SS_App_Core1.dxe’ on Core 1 and ‘SS_App_Core2.dxe’ on Core 2 as shown below figure. Prebuilt DXEs of each project can be found inside the respective ‘Release’ folders of each of the projects (under 'SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Demo' folder).

|image20|

-  Since ARM is main core the SC598 preload .dxe can be removed from Core1 by selecting the preload .dxe and using "Remove" option on the right-side.
-  Double click on ‘SS_App_Core1.dxe’ of Core 1 and "Check" reset Core option, since preload .dxe file removed from Core1. Now click on "Apply" and "Close".

|image21|

-  Select the Core0 CCES Project again and go to Run->Debug Configurations. Create a new Debug launch group under ‘Application with CrossCore Launch Group’.

|image22|

-  Add the ‘Application with GDB and OpenOCD(Emulaotr)’ and ‘Application with CrossCore Debugger’ debug configuration one after other one using "Add.." button on the right and clicking on "OK".

|image23|

   |image24|
-  Reset the board, Apply and click on "Debug" button to start debug session. Select "OK" to open the debug window which will open a window on left side of Project explorer.

|image25|

-  Click on “Resume(F5)” to run Core 0 (ARM). This enables the Core 1 and 2 (SHARC).

|image26|

-  Then individually select and run Core 1 and Core 2 by clicking on “Resume(F5)” as shown in below figure.

|image27|

-  Open SigmaStudio+ schematic.
-  Select SHARC core DXE's what is running on the target processor.

|image28|

   |image29|
-  Link compile download the SigmaStudio+ schematic if Demo or Lib integration application is used.

.. note::

   Link compile download schematic not required if DemoUc application is used, since the schematic source code already included in the target application. Also target framework and application don't support redownload of schematic, once downloaded on to the running target application. The target application should be rerun by resetting the target platform to download the schematic again.


Using SOM + SOM-CRR On-Board Debug Agent
----------------------------------------

-  Powering Up the Boards:

   -  Provide a 12V supply to the P8 port on both the SOM and SOM-CRR boards.
   -  Connect the USBi to the P3 port on the SOM-CRR board.

-  Configuring the Switches:

   -  On the SOM-CRR board, locate SW1 (the mini switches).
   -  Switch all six mini switches on SW1 from their default OFF position to the ON position.

-  Connecting USB Cables:

   -  Connect the micro-USB end of the cable to the USB DA (P2) port on the SOM-CRR board.

-  Launch CrossCore Embedded Studio:

   -  Open CrossCore Embedded Studio on your development machine.

-  Adjust Preferences (Optional Step):

   -  Navigate to Window → Preferences → Run/Debug → Launching.
   -  Uncheck the "Build (if required) before launching" checkbox to prevent automatic builds before launching.

-  Configure Debug Settings:

   -  From the top menu, select Run → Debug Configurations.
   -  In the Debug Configurations window, create a new Debug configuration under the ‘Application with CrossCore Debugger’ section.
   -  Select the appropriate processor for your setup in the configuration settings.

   |image30|

-  Select EZ-Kit Lite Option:

   -  In the Debug Configurations window, select the EZ-Kit Lite option.


   |image31|

   -  Click "Next" to proceed to the next step.

-  Enable Debug Agent:

   -  The option to use the Debug Agent will be visible.


   |image32|

   -  Click "Finish" to confirm and exit the configuration window.

-  Load Prebuilt DXEs for Each Core:

   -  The prebuilt DXEs for each project can be found in the respective ‘Release’ folders (SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Demo) of each project.
   -  ‘SS_App_Core0’ (Core 0), ‘SS_App_Core1.dxe’ (Core 1) and ‘SS_App_Core2.dxe’ (Core 2) as shown below.

   |image33|

-  Apply and Start Debugging:

   -  After selecting the correct DXE files for each core, click "Apply" to save the configuration.
   -  Finally, click "Debug" to begin running the application.

| 
| ===Using SC598 SOM + SOM-CRR On-Board Debug Agent===

-  Powering Up the Boards:

   -  Provide a 12V supply to the P8 port on both the SOM and SOM-CRR boards.
   -  Connect the USBi to the P3 port on the SOM-CRR board.

-  Configuring the Switches:

   -  On the SOM-CRR board, locate SW1 (the mini switches).
   -  Switch all six mini switches on SW1 from their default OFF position to the ON position.

-  Connecting USB Cables:

   -  Connect the micro-USB end of the cable to the USB DA (P2) port on the SOM-CRR board.

-  Launch CrossCore Embedded Studio:

   -  Open CrossCore Embedded Studio on your development machine.

-  Adjust Preferences (Optional Step):

   -  Navigate to Window → Preferences → Run/Debug → Launching.
   -  Uncheck the "Build (if required) before launching" checkbox to prevent automatic builds before launching.

-  ARM Core Debug Configuration:

   -  Right-click on the ARM project and select Debug Configurations.
   -  Create a new debug configuration under ‘Application with GDB and OpenOCD (Emulator)’.
   -  Select the appropriate processor for your ARM core.
   -  In the Target tab, under the Interface dropdown, select “Analog Devices Onboard Debug Agent”.

   |image34|

   -  In the Main tab, select the ARM core DXE file.

   |image35|

   -  Click "Apply" to save the configuration and then "Close" to exit the debug configuration window.

-  SHARC Core Debug Configuration:

   -  Right-click on the SHARC project and select Debug Configurations.
   -  Create a new debug configuration under ‘Application with CrossCore Debugger’
   -  Select the appropriate processor for the SHARC core.
   -  In the Connection settings, select ‘EZ-Kit Lite’ as the connection type.

   |image36|

   -  Click "Next" to proceed.
   -  The option to use the Debug Agent will be visible.

   |image37|

   -  Click "Finish" to finalize the SHARC configuration.

-  Load Prebuilt DXEs for Each SHARC Core:

   -  The prebuilt DXEs for each project can be found in the respective ‘Release’ folders (SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Demo) of each project.
   -  ‘SS_App_Core1.dxe’ (Core 1) and ‘SS_App_Core2.dxe’ (Core 2).
   -  Remove the ‘ezkitSC598W_preload_core1.dxe’ from SHARC Core1 Debug Configs.

-  Start Debugging the ARM and SHARC Cores:

   -  In the ARM Core project, right-click and select Debug As → ‘Application with CrossCore Launch Group’.
   -  Select the processor and then choose the ‘Onboard Debug Agent’ option.

   |image38|

   -  The previously selected Debug Configuration for both ARM and SHARC cores will appear under ‘Use an existing debug configuration’.

   |image39|

   -  Click "Finish" to apply the settings.
   -  The final window will display the selected debug configurations for both the ARM and SHARC cores.

   |image40|

   -  Click "Debug" to start the debugging session.

| 
| ===Downloading Schematic from SigmaStudioPlus UI to Target=== Once the above-mentioned steps for loading the DXE are completed, the target application will be up and running, waiting to receive schematic data (SMAP) from the SigmaStudioPlus UI.
| Let’s take an example case with a dual-core processor:

-  Open the SigmaStudioPlus schematic and navigate to the Project window.
-  For SHARC Core1, navigate to *SharcXICore_C1 -> Settings*. An option to browse and select the target application's SHARC Core1 DXE can be seen.

|image41|

| 
| \* For SHARC Core2, navigate to *SharcXICore_C2 -> Settings*. An option to browse and select the target application's SHARC Core2 DXE can be seen.
| |image42|
| \* Once the paths to both DXEs are specified, click the *Link Compile Download* button to compile the schematic using the selected DXEs and download the schematic data to the target application.
| |image43|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/584_1.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/584_2.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/584_3.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sharc1_core_dxe.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sharc2_core_dxe.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/21573_1.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/21573_2.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/21573_3.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sharc1_core_dxe.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sharc2_core_dxe.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/569_1.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/569_2.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/569_3.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sharc1_core_dxe.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_select_debugconfig.png
   :width: 1080px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_select_ice_emulator.png
   :width: 1080px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_select_core_exe.png
   :width: 1080px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_sh0_select_debugconfig.png
   :width: 1080px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_select_sh_emulator.png
   :width: 1080px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_sh0_select_exe.png
   :width: 1080px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_sh0_select_reset.png
   :width: 1080px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_select_launch_group.png
   :width: 1080px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_select_lg_core0debug.png
   :width: 1080px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_select_lg_core1debug.png
   :width: 1080px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_select_lg_debug_final.png
   :width: 1080px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_run_core0.png
   :width: 1080px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_run_core1_core2.png
   :width: 1080px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sharc1_core_dxe.png
   :width: 600px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sharc2_core_dxe.png
   :width: 600px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/debug1.png
   :width: 1080px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/debug2.png
   :width: 650px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/debug3.png
   :width: 650px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/debug4.png
   :width: 650px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_debug1.png
   :width: 650px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_debug2.png
   :width: 650px
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_debug3.png
   :width: 650px
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_debug5.png
   :width: 650px
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_debug4.png
   :width: 650px
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_debug8.png
   :width: 650px
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/sc598_debug7.png
   :width: 650px
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/ss_sh0_dxe.png
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/ss_sh1_dxe.png
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/ss_schemadownload.png
