:doc:`Click here to return to 'SigmaStudio for SHARC - Quick start guide' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide>`

Demo application
================

| This section explains the following
| \* Loader File Flashing and Generation

-  How to run the Example Schematics which are provided with this package using the pre-built executables of the Demo application.
-  Rebuilding the demo Application.
-  Creating and running new schematics.

| 
| =====Loader file Flashing and Generation=====

Programming the flash
---------------------

| Run the Flash_ADSPSC5xx.bat batch file present in “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\utilities\\FlashProgrammer\\” folder to program the flash on ADSP-SC5xx EZ-Board using the pre-built SS_App_SC5xx.ldr loader file present in “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR” folder.
| Use the following command to program the flash on ADSP-SC584 EZ-Board using the pre-built SS_App_SC584.ldr loader file present in “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR” folder.
| <fc #cd5c5c>\ *Flash_ADSPSC5xx.bat 584 XXXX “<Software Modules folder>\\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR\\ SS_App_SC584.ldr”*\ </fc>
| Use the following command to program the flash on ADSP-SC589 EZ-Board using the pre-built SS_App_SC589.ldr loader file present in “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR” folder.
| <fc #cd5c5c>\ *Flash_ADSPSC5xx.bat 589 XXXX “<Software Modules folder>\\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR\\ SS_App_SC589.ldr”*\ </fc>
| Use the following command to program the flash on ADSP-SC573 EZ-Board using the pre-built SS_App_SC573.ldr loader file present in “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR” folder.
| <fc #cd5c5c>\ *Flash_ADSPSC5xx.bat 573 XXXX “<Software Modules folder>\\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR\\ SS_App_SC573.ldr”*\ </fc>
| XXXX stands for 1000 or 2000 based on the emulator used for flashing.
| The boot switch is set to ‘1’ and a hard reset has to be given to run the demo.
| ====Loader file generation==== The following command is used to generate a loader file for ADSP-SC584 processor.
| <fc #cd5c5c>\ *"C:\\Analog Devices\\CrossCore Embedded Studio 2.4.0\\elfloader.exe" -proc ADSP-SC584 -core0= SS_App_Core0.exe -init ezkitSC584_initcode_core0_v10.exe -core1= SS_App_Core1.dxe -core2= SS_App_Core2.dxe -NoFinalTag= SS_App_Core0.exe -NoFinalTag= SS_App_Core1.dxe -b SPI -f BINARY -Width 8 -bcode 0x1 -verbose -o SS_App_SC584.ldr*\ </fc>
| The above command will generate a loader file by the name SS_App_SC584.ldr. Copy the application DXEs of all the three cores of ADSP-SC584 processor to the “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR” folder. In case, ARM Core executable is missing .exe at the end, add the .exe to the name of ARM executable. The file “ezkitSC584_initcode_core0_v10.exe” is a part of CCES. It can be found at “Analog Devices\\CrossCore Embedded Studio 2.4.0\\SHARC\\ldr. Copy this file to “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR” folder.
| The following command is used to generate a loader file for ADSP-SC589 processor.
| <fc #cd5c5c>\ *"C:\\Analog Devices\\CrossCore Embedded Studio 2.4.0\\elfloader.exe" -proc ADSP-SC589 -core0= SS_App_Core0.exe -init ezkitSC589_initcode_core0_v10.exe -core1= SS_App_Core1.dxe -core2= SS_App_Core2.dxe -NoFinalTag= SS_App_Core0.exe -NoFinalTag= SS_App_Core1.dxe -b SPI -f BINARY -Width 8 -bcode 0x1 -verbose -o SS_App_SC589.ldr*\ </fc>
| The above command will generate a loader file by the name SS_App_SC589.ldr. Copy the application DXEs of all the three cores of ADSP-SC589 processor to the “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR” folder. In case, ARM Core executable is missing .exe at the end, add the .exe to the name of ARM executable. The file “ezkitSC589_initcode_core0_v10.exe” is a part of CCES. It can be found at “Analog Devices\\CrossCore Embedded Studio 2.4.0\\SHARC\\ldr. Copy this file to “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR” folder.
| The following command is used to generate a loader file for ADSP-SC573 processor.
| <fc #cd5c5c>\ *"C:\\Analog Devices\\CrossCore Embedded Studio 2.4.0\\elfloader.exe" -proc ADSP-SC573 -core0= SS_App_Core0.exe -init ezkitSC573_initcode_core0.exe -core1= SS_App_Core1.dxe -core2= SS_App_Core2.dxe -NoFinalTag= SS_App_Core0.exe -NoFinalTag= SS_App_Core1.dxe -b SPI -f BINARY -Width 8 -bcode 0x1 -verbose -o SS_App_SC573.ldr*\ </fc>
| The above command will generate a loader file by the name SS_App_SC573.ldr. Copy the application DXEs of all the three cores of ADSP-SC573 processor to the “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR” folder. In case, ARM Core executable is missing .exe at the end, add the .exe to the name of ARM executable. The file “ezkitSC573_initcode_core0.exe” is a part of CCES. It can be found at “Analog Devices\\CrossCore Embedded Studio 2.4.0\\SHARC\\ldr. Copy this file to “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\LDR” folder.
| =====Getting Started with Example Schematics===== Example Schematics for ADSP-SC5xx are provided in “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Host\\Examples\\Sample Schematics\\ADSP-SC5xx” folder. Follow the instructions given below to execute the example Schematics on the ADSP-SC573/ ADSP-SC584/ADSP-SC589 Target.
| \* Establish the hardware setup as described in Section 3.1.

-  Install all software and tools mentioned in Section 2.
-  Launch CrossCore Embedded Studio.
-  Uncheck “Build (if required) before launching” checkbox in Window->Preferences->Run/Debug->Launching.
-  Select RunDebug Configurations. Create a new Debug configuration under ‘Application with CrossCore Debugger’. Select appropriate processor, connection type and platform. Click finish.
-  Load the prebuilt DXE’s for appropriate target ‘SS_App_Core0’ on Core 0, ‘SS_App_Core1.dxe’ on Core 1 and ‘SS_App_Core2.dxe’ on Core 2 as shown in Figure 5. Prebuilt DXEs of each project can be found inside the respective ‘Release’ folders of each of the projects.\

|image1|

-  Double click on ‘SS_App_Core1.dxe’ of Core 1 and uncheck ‘Run immediately after load’ option as shown in the Figure 6. Repeat the same for ‘SS_App_Core2.dxe’ for Core 2.\

|image2|

-  Reset the board and press ‘Debug’ to launch the debug session. Click on “MP Resume” to run Core 0 (ARM). This enables the Core 1 and 2 (SHARC). Then individually select and run Core 1 and Core 2 by clicking on “Resume” as shown in Figure 7\

|image3|

-  Launch SigmaStudio.
-  Open Volume_Mute_Block_SC5xx.dspproj from “< Software Modules install folder > \\ SigmaStudioForSHARC-SH-Rel3.9.0\\Host\\Examples\\Sample Schematics\\ADSP-SC5xx” folder.
-  Select the prebuilt Application DXE’s for both the SHARC’s by clicking on ‘Select Application DXE’ in SHARC0/SHARC1 tab of SigmaStudio IC control window.
-  Connect the audio inputs to the EZ-BOARD and play audio on PC.
-  Press Link-Compile-Download.
-  The output audio will be heard through speakers/headphones connected to the EZ-BOARD.
-  The checkbox inside the mute cells in the schematic can be checked/unchecked to mute/unmute any channel.

| 
| =====Rebuilding the Demo Application===== The Default Application for ADSP-SC573, ADSP-SC584 and ADSP-SC589 are supplied with the package. Follow the steps given below to rebuild the Application. The projects can be found under target specific subfolders inside “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\Demo\\”.
| \* Launch CrossCore Embedded Studio on the SigmaStudio Host PC. Specify the workspace when prompted.

-  Select File->Import. Import SS_App_Core0, SS_App_Core1 and SS_App_Core2 projects into CrossCore Embedded Studio.
-  Select all the three projects (SS_App_Core0, SS_App_Core1 and SS_App_Core2). Clean and rebuild the projects in the required configuration (Release/Debug).
-  The newly generated executables will be present in “Debug” or “Release” folder based on the chosen configuration.

| 
| ====Launching Debug Configuration and Booting the Target==== Follow steps 5 to 8 from section 6.1 to launch debug configuration and to boot the Target.
| Note: Select the rebuilt DXE’s in step 6 of section 6.1 instead of prebuilt DXE’s
| =====Creating and Running a New simple Schematic using the Demo application=====

Creating a New Schematic
------------------------

| Follow the steps below to create a SigmaStudio for SHARC Schematic for ADSP-SC5xx.
| \* Launch SigmaStudio and open a new project. The ‘Tree ToolBox’ on the left side displays all the supported processors and communication channels.

-  Drag two ‘ADSP-SC5xx’ from the ‘Processor’ tree and drop it into the ‘Hardware Configuration’ design window. This block is referred to in this document, as the ‘IC’.
-  Drag ‘USBi’ from the ‘Communication Channels’ tree and drop it into the ‘Hardware Configuration’ design window. If the USBi driver is installed properly and the USBi is connected to the PC, the word “USB” is in a green box. If there is a problem with driver installation or connection, the box with text “USB” is shown in red. In such a case, remove the USBi from the ‘Hardware Configuration’ design window, verify the USB connection, and repeat this step.
-  Connect the first blue (output) pin of the ‘USBi’ to the green (input) pin of the ‘IC 1’ block. Connect the second blue (output) pin of the ‘USBi’ to the green (input) pin of the ‘IC 2’ block as shown in Figure 8
-  A drop down menu is enabled adjacent to the connected pin of ‘USBi’. Select ‘SPI 0x1 ADR0’ from the drop down menu for both the ICs.
-  An IC control window is created for every IC dragged as part of step 2. Select “Core 1” in the “Default SHARC Core” section of the "Main” tab of IC control window for “IC 1”. Select “Core 2” in the “Default SHARC Core” section of the "Main” tab of IC control window for “IC 2”. Leave the other settings unchanged.
-  Go to the ‘Block Schematic’ tab. The toolbox on the left side lists the Modules available for the SHARC DSP.
-  Drag and drop the desired Modules in the Schematic workspace and interconnect the Modules to form a DSP design.

| |image4|
| ====Running the New Schematic====

-  Refer to section 6.4.1 for creating a schematic for ADSP-SC5xx.
-  Refer to section 6.3 for rebuilding the Application (if required) and booting the Target.
-  Select the rebuilt/prebuilt Application DXE’s for both the SHARC’s by clicking on ‘Select Application DXE’ in SHARC0/SHARC1 tab of SigmaStudio IC control window.
-  Connect the audio inputs to the EZ-BOARD and play audio on PC.
-  Press Link-Compile-Download.
-  The output audio will be heard through speakers/headphones connected to the EZ-BOARD.

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_5.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_6.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_7.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_8.jpg
