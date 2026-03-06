:doc:`Click here to return to 'SigmaStudio for SHARC - Quick start guide' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide>`

DemoUc application
==================

| The DemoUc application demonstrates the usage of ARM core of ADSP-SC5xx as microcontroller in the final deployment mode of the application developed using SigmaStudio. The DemoUc applications for ADSP-SC573 can be found in “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\DemoUc\\ADSP-SC57xii\\” and those of ADSP-SC584 and ADSP-SC589 can be found in “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\DemoUc\\ADSP-SC58xiii\\”.
| The DemoUc application provided with the package uses the code and parameters exported for the “Volume_Mute_Block_SC5xx.dspproj” schematic located in “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Host\\Examples\\Sample Schematics\\ADSP-SC5xx\\”. The application configures push buttons PB1 and PB2 on the EZ-Board which can be used to alter certain parameters of the “Volume_Mute_Block_SC5xx.dspproj” schematic. PB1 is used to change the “Enable/Disable” parameter of the “Master Mute” cell of “Volume_Mute_Block_SC5xx.dspproj” schematic running on SHARC Core 1. PB2 is used to change the “Enable/Disable” parameter of the “General Filter” cell of “Volume_Mute_Block_SC5xx.dspproj” schematic running on SHARC Core 2. Similar mechanisms may be used to tune the parameters of a custom schematic in the final deployment mode using ARM core as microcontroller.
| The sections below describe the steps for running this example application and updating this application for a custom schematic.
| =====Running the default DemoUc application===== Follow the steps below for running the default DemoUc application with code and parameters from “Volume_Mute_Block_SC5xx.dspproj”.
| \* Launch CrossCore Embedded Studio on the SigmaStudio Host PC. Specify the workspace when prompted.

-  Select FileImport. Import SS_uC_App_Core0, SS_uC_App_Core1 and SS_uC_App_Core2 projects of appropriate target located in subfolders inside “< Software Modules folder >\\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\DemoUc\\” into CrossCore Embedded Studio.
-  Uncheck “Build (if required) before launching” checkbox in Window->Preferences->Run/Debug->Launching.
-  Select RunDebug Configurations. Create a new Debug configuration under ‘Application with CrossCore Debugger’. Select appropriate processor, connection type and platform. Click finish.
-  Load the prebuilt DXE’s SS_uC_App_Core0‘on Core 0, ‘SS_uC_App_Core1.dxe’ on Core 1 and ‘SS_uC_App_Core2.dxe’ on Core 2. Prebuilt DXEs of each project can be found inside the respective ‘Release’ folders of each of the projects.
-  Connect the audio inputs to the EZ-BOARD and play audio on PC.
-  Follow steps 7 and 8 of section 6.1 for setting the options of the “Debug Configurations” and running the application.
-  The output audio will be heard through speakers/headphones connected to the EZ-BOARD.

| 
| =====Running the DemoUc application with a custom schematic===== Follow the steps below for running the DemoUc application with code and parameters exported from a custom schematic.
| \* Open SigmaStudio and then open the schematic which should be executed in the deployment mode using ARM core as Microcontroller.

-  Select the rebuilt/prebuilt Application DXE’s of appropriate target from “< Software Modules folder >\\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\DemoUc\\” for both the SHARC cores by clicking on ‘Select Application DXE’ in SHARC0/SHARC1 tab of SigmaStudio IC control window.
-  Export the system files as detailed in section “System Files Export” of [4]. Ensure that the “Export XML only” option is unchecked.
-  Copy all the exported files into “< Software Modules folder >\\SigmaStudioForSHARC-SH-Rel3.9.0\\ Target\\utilities\\exportCodeParam” folder.
-  Run the “exportCodeParam” utility as detailed in Annexure A for all the ICs in the schematic.
-  Copy the generated ‘.c’ and ‘.h’ files into “< Software Modules folder >\\SigmaStudioForSHARC-SH-Rel3.9.0\\ Target\\DemoUc\\ADSP-SC58x\\Source” folder or “< Software Modules folder >\\SigmaStudioForSHARC-SH-Rel3.9.0\\ Target\\DemoUc\\ADSP-SC57x\\Source” folder depending on the target.
-  Launch CrossCore Embedded Studio on the SigmaStudio Host PC. Specify the workspace when prompted.
-  Select FileImport. Import SS_uC_App_Core0, SS_uC_App_Core1 and SS_uC_App_Core2 projects of appropriate target located in subfolders inside “< Software Modules folder >\\SigmaStudioForSHARC-SH-Rel3.9.0\\ Target\\DemoUc\\” into CrossCore Embedded Studio.
-  Remove the ‘.c’ files related to “Volume_Mute_Block_SC5xx.dspproj” schematic from the ARM core application and add the new ‘.c’ files generated for the custom schematic.
-  Open file ‘adi_ss_uc_app_arm.c’ and include the generated ‘.h’ file in place of the existing ‘.h’ files in line 25 and 26.
-  Ensure that the names of the SMAP, Code and parameter arrays in function ‘PopulateSsnConfig()’ are in accordance with the arrays within the newly created ‘.c’ file.
-  Rebuild the application for ARM core
-  Select RunDebug Configurations. Create a new Debug configuration under ‘Application with CrossCore Debugger’. Select appropriate processor, connection type and platform. Click finish.
-  Load the DXEs SS_uC_App_Core0‘on Core 0, ‘SS_uC_App_Core1.dxe’ on Core 1 and ‘SS_uC_App_Core2.dxe’ on Core 2. Application DXEs can be found inside the respective ‘Release’ or ‘Debug’ folders of each of the projects based on the chosen active configuration in CCES.
-  Connect the audio inputs to the EZ-BOARD and play audio on PC.
-  Follow steps 7 and 8 of section 6.1for setting the options of the “Debug Configurations” and running the application.
-  The output audio will be heard through speakers/headphones connected to the EZ-BOARD as per the connections in the custom schematic.

| 
| Note: The example microcontroller application provided with the package only supports single instance running on each of the SHARC cores. The application source files are required to be modified for executing multi-instance schematics.
