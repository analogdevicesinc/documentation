:doc:`Click here to return to SigmaStudio documentation Homepage. </wiki-migration/resources/tools-software/sigmastudio>`

SigmaStudio and SigmaStudio For SHARC
=====================================

Welcome to the SigmaStudio and SigmaStudio For SHARC FAQ documentation home page.

Introduction
============

This FAQ document prepared based on recent release of SigmaStudio 4.7 and SigmaStudio for SHARC 4.7.0 software. The documents or folder path referenced may be same for the older/newer version of SigmaStudio and SigmaStudio for SHARC package.

General Q & A
=============

**Q: What are the prerequisites for installing SigmaStudio and SigmaStudio for SHARC? What is the minimum RAM and processor requirements?**

A: Please refer release note in :adi:`SigmaStudio® \| Analog Devices <en/design-center/evaluation-hardware-and-software/software/ss_sigst_02.html>` page for prerequisites for installing SigmaStudio. Please find the prerequisites for installing SigmaStudio For SHARC.

+--------------------------------------------------+---------------------------------------------------------+
| Pre-Requisite                                    | Details                                                 |
+==================================================+=========================================================+
| **Hardware Platform**                            | ADSP-SC573 EZ-BOARD                                     |
|                                                  | Revision No 1.0, Silicon Revision 0.0, BOM Revision 1.5 |
|                                                  | ADSP-SC584 EZ-BOARD                                     |
|                                                  | Revision No 1.4, Silicon Revision 1.0, BOM Revision 2.4 |
|                                                  | ADSP-SC589 EZ-BOARD                                     |
|                                                  | Revision No 1.2, Silicon Revision 1.0, BOM Revision 1.8 |
|                                                  | ADSP-21569 EZ-Kit                                       |
|                                                  | Revision B, Silicon Revision 0.0, BOM Revision B        |
|                                                  | EV-21569-SOM Revision A, Silicon Revision 0.2           |
|                                                  | EV-SOMCRR-EZKIT Revision A                              |
|                                                  | ADZS-SC589-Mini board (SHARC Audio Module)              |
|                                                  | Revision 1.5 Silicon Revision 1.0                       |
|                                                  | EV-21593-SOM Revision A, Silicon Revision 0.0           |
|                                                  | EV-SOMCRR-EZKIT Revision A                              |
|                                                  | EV-SC594-SOM Revision B, Silicon Revision 0.0           |
|                                                  | EV-SOMCRR-EZKIT Revision A                              |
+--------------------------------------------------+---------------------------------------------------------+
| **Processor & Silicon**                          | ADSP-SC5xx or ADSP-215xx processor family               |
+--------------------------------------------------+---------------------------------------------------------+
| **ICE-2000/ICE-1000**                            | ADZS-ICE-2000 Revision No 1.3 or higher                 |
|                                                  | ADZS-ICE-1000 Revision No 1.1 or higher                 |
+--------------------------------------------------+---------------------------------------------------------+
| **CrossCore Embedded Studio**                    | Version 2.10.1 and above                                |
+--------------------------------------------------+---------------------------------------------------------+
| **ADSP-SC5xx EZ-Kit Lite Board Support package** | Version 2.0.2                                           |
+--------------------------------------------------+---------------------------------------------------------+
| **SigmaStudio**                                  | Version 4.7                                             |
+--------------------------------------------------+---------------------------------------------------------+
| **EVAL-ADUSB2EBZ (USBi)**                        | Version 1.3 and above                                   |
+--------------------------------------------------+---------------------------------------------------------+

**Q: Do we need Admin permission to install SigmaStudio and SigmaStudio for SHARC in Windows OS?**

A: Yes, admin permission is required for SigmaStudio and SigmaStudio for SHARC installation in Windows OS.

**Q: Does SigmaStudio supports MAC, Linux Operating System?**

A: No, SigmaStudio supports only in Windows Operating System

**Q: What is SigmaStudio for SHARC? Why SigmaStudio for SHARC is a separate package?**

A: SigmaStudio for SHARC package is to add support for SHARC and SHARC+ processors to SigmaStudio. Customer can get the SigmaStudio for SHARC package by contacting regional ADI representative. The latest version of SigmaStudio for SHARC version is 4.7.0 or customer can get any specific version based on the requirement. The package will have two major components,

**Target:** The target component consists of different target applications based on EZ Kit evaluation boards.

**Host:** schematic examples, custom Plug-in modules examples and Plug-in files for SigmaStudio for SHARC modules. Both target and host component support different SHARC+ DSP processor of ADSP-214xx/ADSP-2156x/ADSP-2157x/ADSP-2158x/ADSP-2159x/ADSP-SC57x/ ADSP-SC58x and ADSP-SC59x family.

**Q: Where can I get information about latest release package?**

A: For latest SigmaStudio release please refer in :adi:`SigmaStudio® \| Analog Devices <en/design-center/evaluation-hardware-and-software/software/ss_sigst_02.html>` page. SigmaStudio for SHARC releases are not available at ADI website, Customer can get the SigmaStudio for SHARC package by contacting regional ADI representative.

**Q: What is the maximum path length allowed in SigmaStudio for saving the projects?**

A: As we know 248 is the maximum path length supported by windows, the path length for SigmaStudio project should be within 248. In some cases, we have seen the CCES project in SigmaStudio for SHARC examples does not compile when project path length is more than 128. For CCES project we recommend keeping the project path length within 128.

**Q: How can I export system files?**

A: Please refer :doc:`Export Program and Parameters [Analog Devices Wiki </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/exportprogramandparameterdata>`] link for SigmaStudio schematic system files export.

**Q: How can I integrate A2B stack into the SigmaStudio for SHARC target applications?**

A: Please refer to “AE_09_A2B_Stack_UserGuide.pdf” available in A2B software “C:\\Analog Devices\\ADI_A2B_Software-Rel19.x.x\\Docs” for A2B stack integration. Please note that the a2b network discovery will be successful only when frame sync is available over the network. Hence, call the A2B discovery function after “AudioIoPcgInit()” function in SigmaStudio for SHARC target applications which will get called after SigmaStudio for SHARC schematic download.

**Q: How can I modify the SS4G target application as A2B Slave application?**

A: Please refer to the documents and examples available in A2B software “C:\\Analog Devices\\ADI_A2B_Software-Rel19.x.x\\” for better understanding and this will give better insights about the modifications to be done in SS4G target application as A2B slave application.

**Q: Is there any debugging tool available for SigmaDSP?**

A: Yes, SigmaDSP simulator is available for ADAU145x/ADAU146x processors. Please contact your regional ADI representative.

**Q: Where can I get details about custom module(plugin) development?**

A:\*\* SHARC:\*\* Refer to “AE_42_SS4G_AlgorithmDesignerGuide.pdf” which is present in the following installation path “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”

**SigmaDSP:** There is SigmaDSP custom module designer available for ADAU145x/ADAU146x processors. Please contact your regional ADI representative.

Hardware Setup Q & A
====================

**Q: There is no audio output after downloading the schematic. What could be the issue?**

A: **SigmaDSP:** Please refer to SigmaDSP user guides for hardware setup and getting started with SigmaStudio schematic.

:adi:`EVAL-ADAU1452REVBZ User Guide (Rev. 0) (analog.com) <media/en/technical-documentation/user-guides/EVAL-ADAU1452REVBZ-UG-1662.pdf>`

:adi:`EVAL-ADAU1466Z User Guide (Rev. 0) (analog.com) <media/en/technical-documentation/user-guides/EVAL-ADAU1466Z_UG-1135.pdf>`

:adi:`EVAL-ADAU1467Z (Rev. 0) (analog.com) <media/en/technical-documentation/user-guides/EVAL-ADAU1467Z-UG-1134.pdf>`

Please find the steps to be verified,

-  Check whether the Eval board connected with USBi and powered On.
-  Check whether the Input/Output channels are properly assigned in the schematic.
-  Check whether any tuning to be done like disabling mute.
-  Check whether the clock, SPORT, other register settings are correct.
-  Check whether the audio input is connected to ADC (Line In) and DAC output (Line Out) connected to

::

     speakers/headset from appropriate channels.

**SHARC:**

-  Check whether target hardware is connected with USBi, powered On and the target application is running.

Please refer to “AE_42_SS4G_QuickStartGuide.pdf” document available in "C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs" folder.

-  Check whether the correct SHARC core application DXE is selected.
-  Check whether there are any changes to default schematic settings like block size, input/output channels, sample rate, SPORT configurations etc. If there are any changes in the default settings, the framework config file is required to be regenerated using “Generate config file” option. Additionally, target application framework should be updated if sample rate is changed.
-  Check whether the Input/Output channels in schematic are properly assigned.
-  Check whether any tuning to be done like disabling mute.
-  Check whether the clock, SPORT, other register settings are fine.
-  Check whether the audio input is connected to ADC (Line In) and DAC output (Line Out) connected to

::

     speakers/headset from appropriate channels.

**Q: How can I access external volume input through GPIO?**

A: There are various options:

-  First option would be to use two pushbuttons as volume up and volume down buttons.
-  Second option is to use a potentiometer for analog control of the audio level.
-  Third option is to use a rotary encoder as a volume control.
-  For more details, refer the following link

:ez:`how-do-i-implement-external-volume-control-using-gpios-or-aux-adcs <dsp/sigmadsp/w/documents/5188/how-do-i-implement-external-volume-control-using-gpios-or-aux-adcs>`.

**Q: Does ADSP-21569 support USB data transmission? Or What are the debug options available for USB data transmission?**

A: USB data transmission is not supported. SigmaStudio for SHARC will support only I2S or TDM data for audio signals. Customers should contact a 3rd party for the USB data transmission support. Please refer below pages for more information, :adi:`HCC Embedded USB Device and Host Stacks \| Analog Devices <en/design-center/evaluation-hardware-and-software/software/hcc-embedded-usb-device-host-stacks.html#software-overview>`

**Q: In PDM microphone input, 120dB SPL is not getting 0dB FS, how can I resolve?**

A: SigmaStudio handles the digital data for audio processing, so please refer to the data sheet of PDM microphone vender.

**Q: How can I set up the evaluation board for executing the example?**

A:**SHARC:** Please refer to “AE_42_SS4G_QuickStartGuide.pdf” document which is present in the path “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”

**SigmaDSP:** Please refer to the user guides available in the corresponding product page in

:adi:`ADAU1452 Datasheet and Product Info \| Analog Devices <en/products/adau1452.html>`

:adi:`ADAU1466 Datasheet and Product Info \| Analog Devices <en/products/adau1466.html>`

:adi:`ADAU1467 Datasheet and Product Info \| Analog Devices <en/products/adau1467.html>`

**Q: SigmaStudio crashes while loading an application dxe. What could be the reason?**

A: This occurs when CrossCore Embedded Studio (CCES) is not installed. Customers should have a CCES installation and a valid license to work with SigmaStudio for SHARC.

**Q: Is it possible to generate an application LDR with schematic code and parameters embedded in ADSP-21569?**

A: We have demoUc example in the SigmaStudio for SHARC installation folder which uses generated schematic files with the target supplication.

You can refer to the section "Loader file Flashing and Generation" in "AE_42_SS4G_QuickStartGuide.pdf" for more details.

**Q: What is 0dB Boost Bypass with SigmaStudio app settings?**

A: The filter modules in SigmaStudio when using filtertypes like Peaking, PeakingZolzer, FirstOrderFilterLowShelf and FirstOrderFilterHighShelf are enabled with a bypass mode when the boost gain of the filter is set to 0 dB. This bypass mode which is enabled by default in SigmaStudio may cause pop sound when changing the boost from a non-zero value to 0 dB and vice-versa. The flag “Disable-Boost-Bypass” is used to disabled bypass mode for 0 dB Boost gain. The default settings may change in future releases.

| The SS app settings config file “SStudio.exe.config” available in following location, “C:\\Program Files\\Analog Devices\\SigmaStudio x.x”. For disabling the 0 dB boost bypass mode, please update the “SStudio.exe.config” settings as below.
| |image1|
| ====== Framework and Schematic Configurations Q & A ====== **Q: What is the default sample rate supported in SigmaStudio? How can I change the sample rate to a value other than the default value (Example like 96KHz)?**

A: The default SigmaStudio sample rate support is 48 kHz.

**SigmaDSP:**

Sample rate of SigmaDSP schematics can be modified by changing the sample rates of input and source modules present in the schematic. The SigmaDSP Eval board by default supports standalone mode for 44.1kHz and 48 kHz sample rate. The codec should be reconfigured using I2C master control port to support other sample rates. Please refer to corresponding SigmaDSP Eval board user manual for more details.

:adi:`EVAL-ADAU1467Z (Rev. 0) (analog.com) <media/en/technical-documentation/user-guides/EVAL-ADAU1467Z-UG-1134.pdf>`

:adi:`EVAL-ADAU1466Z User Guide (Rev. 0) (analog.com) <media/en/technical-documentation/user-guides/EVAL-ADAU1466Z_UG-1135.pdf>`

:adi:`EVAL-ADAU1452REVBZ User Guide (Rev. 0) (analog.com) <media/en/technical-documentation/user-guides/EVAL-ADAU1452REVBZ-UG-1662.pdf>`

**SHARC:**

The change in sample rate will be supported by changing the sample rate in the SigmaStudio schematic and target application. The SHARC target application by default supporting 44.1kHz and 48 kHz sample rate, for other sample rates the target application needs to be modified. Please refer Ezone links below, where the information’s regarding the sample rate change for the example target applications provided in the SigmaStudio for SHARC package.

:ez:`Building a 96k / 192k version of SS_App_Core for ADSP-SC58x EZ board - Q & A - SigmaStudio for SHARC - EngineerZone (analog.com) <dsp/software-and-development-tools/sigmastudio-for-sharc/f/q-a/120756/building-a-96k-192k-version-of-ss_app_core-for-adsp-sc58x-ez-board>`

:ez:`SigmaStudio 4 SharC ADSP-21569 sample rate - Q & A - SigmaStudio for SHARC - EngineerZone (analog.com) <dsp/software-and-development-tools/sigmastudio-for-sharc/f/q-a/168207/sigmastudio-4-sharc-adsp-21569-sample-rate>`

**Q: How can I create multi-instances of a module for SHARC?**

A: Multiple instances of one or more modules can be dragged into schematic (if module support multiple instances). Additionally, we could use add algorithm feature (if supported) to insert multiple instances of any module. When added, the multiple instances of the module may share the same GUI control.

**Q: How can I create multi-instance schematic for SHARC?**

A: The SigmaStudio for SHARC target application can support up to 3 SigmaStudio schematic instances on a single SHARC core. Steps to be followed:

-  Drag multiple ADSP-SC5xx/215xx IC’s and connect with USBi as shown in below image

| 
| |image2|
| \* Select the same SHARC core (Either Core 1 or Core 2) for all instances in “IC x - ADSP-SC5xx Control à Hardware Configuration à Main” window.
| |image3|
| \* Change the instance ID of each instance in the order 0, 1, and 2.
| |image4|
| \* Select the application DXE in 0th instance of each SHARC core.

-  Create schematic to all IC instance of each SHARC core.
-  As usual run target and perform link compile download for the schematic.

For more information on the ADSP-SC5xx/ADSP-215xx multi-instancing support, please refer to “AE_42_SS4G_IntegrationGuide.pdf” document available in “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.

For more information on the ADSP-214xx/ADSP-213xx multi-instancing support, please refer to “SigmaStudio_for_SHARC_Users_Guide.pdf” document available in “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.

**Q: What could be the reason for compilation failure with "schematic DXE generation failed" message? How can I resolve compilation error with "schematic DXE generation failed" message?**

A: There could be different reasons for “schematic DXE Generation failed” error message:

-  SHARC core DXE’s are not selected in the “IC Control – Hardware Configuration”.
-  One or more referenced libraries or symbols are not found. Example: missing library file when using plug-ins, FIR/IIR hardware accelerator libraries etc.
-  Insufficient memory for Code, Parameter and state.

The resolution steps are,

-  Select the correct application DXE’s in the “IC Control – Hardware Configuration”.
-  The referenced libraries should be present in correct location. Refer to the plug-in module user guides for more details.
-  The developer should be aware of Memory and MIPS before adding any modules to the schematic. Refer to the “AE_42_SS4G_IntegrationGuide.pdf” document available in “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-x.x\\Docs” folder for more information about GMAP and SMAP block use in SigmaStudio.

**Q: How can I get the details of selected CCES tool chain in SigmaStudio for SHARC?**

A: The following steps will guide to figure out the CCES tool chain in SigmaStudio for SHARC,

-  Open SigmaStudio and go to “Tools”
-  Select Settings
-  Select SHARC – “Tool chain”

| 
| |image5|
| **Q: What is the difference between Demo, Demo uC and Library integration examples?**

A: **Demo:** The demo is the target application example for EZ kit evaluation board for different processors, which will help customers to get started with SigmaStudio applications and do customizations to meet their requirements. Additionally, this application will help customer to tune their audio processing application with the help of SigmaStudio host. This is a component-based target application for SigmaStudio schematic applications to achieve the audio signal processing. Some of the important components are,

-  System components
-  IPC
-  Connecting and communication
-  Control framework
-  Audio process framework

The demo application has dependency with SigmaStudio. The dependencies are,

-  Framework configurations – I/O channels, I/O buffers, block size, processing mode, processing cores, serial sport configurations, sample rate etc.
-  Schematic application – SMAP, Code, Parameter, version info, tuning, readback info etc.

For more details, please refer to the section “Target Framework” in “AE_42_SS4G_IntegrationGuide.pdf” available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.

**DemoUc:** The demoUc is the example application for the final product version of SigmaStudio schematic which is fine tuned with the demo application. The demoUc application has the schematic code and parameters embedded as a C source file using “Export system files” option. Please refer to the section “Utility for formatting Exported data from SigmaStudio” in “AE_42_SS4G_QuickStartGuide.pdf” available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”. While using this application, there is no need of SigmaStudio for performing the initial download. However, tuning is possible from SigmaStudio or Micro controller over SPI. The DemoUc considers ARM as a microcontroller, controls mute and filter enable through push buttons on the EZ Kit board.

**Library Integration:** The library integration is the example for simple BareMetal application to show SigmaStudio library integration. The library integration doesn’t have many components as demo or demoUc but can work with SigmaStudio for schematic design and tuning.

**Q: How to resolve the Linker warning as shown below in SigmaStudio for SHARC examples framework?**

\**[Warning li2074] "C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Rel4.7.0\\Target\\Examples\\DemoUc\\ADSP-SC58x\\ADSP-SC589\\SS_uC_App_Core1\\system\\startup_ldf\\app.ldf":1780 RESERVE_EXPAND command on line 10 of file "..\\..\\..\\Source\\adi_ss_uc_app.ldf" might claim the remainder of 'mem_block0_bw' memory, leaving no space for 'dxe_block0_stack_and_heap_expand' output section.

[Warning li2074] "C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Rel4.7.0\\Target\\Examples\\DemoUc\\ADSP-SC58x\\ADSP-SC589\\SS_uC_App_Core1\\system\\startup_ldf\\app.ldf":1792 RESERVE_EXPAND command on line 71 of file "..\\..\\..\\Source\\adi_ss_uc_app.ldf" might claim the remainder of 'mem_L2B7B8_bw' memory, leaving no space for 'dxe_l2_stack_and_heap_expand' output section.

Linker finished with 2 warnings.*\*

A: Please refer the Ezone thread which we have already addressed this query :ez:`building-the-example-uc-project-for-adsp-sc589-ez-in-cces-warnings <dsp/software-and-development-tools/sigmastudio-for-sharc/f/q-a/565549/building-the-example-uc-project-for-adsp-sc589-ez-in-cces-warnings>`.

**Q: How can I use the lib integration as demo uC application?**

A: Lib integration example can be used as demoUc by generating the SigmaStudio schematic source files from the exported system files. Please refer to the section “Utility for formatting Exported data from SigmaStudio” in “AE_42_SS4G_QuickStartGuide.pdf” available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.

**Q: How can I change the Block Size?**

| A: Please find the steps to change the block size in the SigmaStudio for SHARC schematic.
| |image6|
| \* The main window shown in above image for setting the block size for the schematic.

-  The maximum block size value set in the target application needs to be changed when the SigmaStudio schematic block size is changed. The maximum block size “ADI_SS_FW_MAX_PROCESS_BLOCKSIZE” needs to be updated in “adi_ss_fw_common.h” file “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-x.x\\Target\\Examples\\Framework\\Include” folder.

| 
| |image7|
| \* The input modules block size can be updated using “Set Block size” option shown in above image.

**Q: How can I configure the SPORT for IO in SigmaStudio for SHARC application?**

| A: The SPORT configurations are received from the SigmaStudio host to SHARC target application. The SPORT configurations can be assigned in “IC 1 ADSP-SC5xx Control à Framework Config” window. For more details about the default SPORT configuration please refer section “Audio Input-Output Modes” in “AE_42_SS4G_IntegrationGuide.pdf” document available in “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.
| |image8|
| **Q: How can I configure the memory mapping for code, parameter, and state memory?**

A: Please refer to section “GMAP and SMAP” in “AE_42_SS4G_IntegrationGuide.pdf” document available in “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.

**Q: What is ‘Single Core’ and ‘Dual Core’ in IC control window? Is there any example schematic?**

A: SHARC+ DSP’s has maximum of two SHARC+ cores and each of the cores can have up to three SigmaStudio schematic instances. SHARC core selection for each of the instances need to be done in Default SHARC Core setting. The core instance should be in specific order, i.e. SHARC core 1 and followed by SHARC core 2.

| **Single Core:**
| |image9|
| In ‘Single Core’ mode, the schematic instance runs on any one of the SHARC+ core. Multiple schematic instances are possible only when ‘Single Core’ mode is set. A dual SHARC+ core DSP is supported with two “IC” instance as shown below.
| |image10|
| The separate “IC” instance for each core helps to design the schematic for each core separately by dragging the modules from corresponding “IC” instance. The single core option is used to make the core processing mode as Serial or Parallel.
| |image11|
| The example schematic for Single core is available in “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Host\\Examples\\Sample Schematics” folder.

**Dual Core:**

| In ‘Dual Core’ mode, the schematic modules are processed using both the SHARC+ core. Thus, the SHARC core selection is not possible in Dual core mode. Multiple schematic instances are also not supported in this mode.
| |image12|
| A dual SHARC+ core DSP can be supported with only one “IC” as shown below.
| |image13|
| The single “IC” instance for designing the schematic using the modules dragged from the same.
| |image14|
| The schematic processing is always serial and the modules to be processed on each of the cores can be assigned by the user using “Change Core” selection on the module.
| |image15|
| **Q: What is memory insufficiency error while compiling the SS Schematic? How to resolve it?**

| A: The memory insufficiency error can get reported due to the insufficiency of Code, Parameter or Data memory required by the modules used in SigmaStudio schematic. The developer should be aware of Memory and MIPS before adding any modules to the schematic. Refer to “AE_42_SS4G_IntegrationGuide.pdf” document available in “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs” folder for more information about GMAP and SMAP block use in SigmaStudio. If there is any memory insufficiency, the Code/Parameter/Data memory requirements can be verified by mapping all the memory to L3 buffers. Please follow the below steps for L3 memory mapping to find the actual memory requirements of the schematic.
| |image16|
| **Code Memory mapping to Code B(L3):**

-  Select the code memory tab in “Memory Sections”
-  Click on load Section Map
-  By default, the memory mapped to Code buffer.
-  Change the Code buffer to “Code B”
-  Click on Update Section Map to change the code memory mapping

| 
| |image17|
| **State Memory mapping to State C(L3):**

-  Select the State memory tab in “Memory Sections”
-  Click on load Section Map
-  By default, the memory mapped to “State A” buffer.
-  Change all the memory sections from “State A” buffer to “State C”
-  Click on Update Section Map to change the state memory mapping

| 
| |image18|
| **Parameter Memory mapping to State C(L3):**

-  Select the Parameter memory tab in “Memory Sections”
-  Click on load Section Map
-  By default, the memory mapped to “Param” buffer.
-  Change the memory section from “Param” buffer to “Param B”
-  Click on Update Section Map to change the parameter memory mapping

| 
| |image19|
| Once Code/Parameter/Data memory are mapped to L3, perform link compile to see the memory requirements. The memory requirement information will help to modify the default SS buffers allocated in the target application. Please refer to section “GMAP and SMAP” in “AE_42_SS4G_IntegrationGuide.pdf” document available in “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”. Mapping schematic memory to L3 memory may cause a lot of overhead on MIPS consumption. The user doesn’t have any control on splitting the memory mapping but can only change the default sections to be mapped.

**Q: Is it possible to allocate more memory for Param B when using a custom algorithm?**

| A: The SigmaStudio framework supports either Param (L1) or ParamB (L3) memory mapping, as all parameters must reside within a single memory block. Therefore, Param and ParamB cannot be used simultaneously. Additionally, these memory blocks cannot be assigned through custom memory section mapping, since SigmaStudio internally determines the memory sections during compile time. If MIPS consumption is not a concern, the entire parameter block can be mapped to ParamB memory using the “Load Memory” and “Update Memory” options available in the Memory section tab.
| |image20|
| The other options are:

1) Global parameters can be mapped to any of the L1, L2, or L3 memory sections in the target application. These parameter buffers can then be accessed in custom modules as extern variables. To ensure they are retained during linking, you can preserve these buffers using the KEEP command in the target application's LDF file.

      Define the global parameter buffer in target application.

| 
| |image21|
| >> Preserve global parameter buffer symbol in ldf file
| |image22|
| >> Define the global parameter buffer as extern and use it in custom module.
| |image23|
| 2) The ParamB memory block, which is mapped to L3 by default, can be redirected to L2 memory if there are MIPS constraints. For L2 memory mapping please modify the “adi_ss_app.ldf” as shown below (Half of the memory will be reserved for StateC data buffer) .
| |image24|
| **Q: How can I configure register window in SigmaDSP?**

A: Register Control Window allows access to internal registers and DSP core Registers. Launch the Register Control Window by clicking on the Hardware Configuration tab at the top of the workspace, and then clicking on the Register Controls tab at the bottom of the Configuration workspace. Users can configure the SigmaDSP register on this window by referring to the corresponding IC data sheet which can be downloaded from:

:adi:`ADAU1452 Datasheet and Product Info \| Analog Devices <en/products/adau1452.html>`

:adi:`ADAU1466 Datasheet and Product Info \| Analog Devices <en/products/adau1466.html>`

:adi:`ADAU1467 Datasheet and Product Info \| Analog Devices <en/products/adau1467.html>`

| 
| |image25|
| **Q: Where can I get ADAU1466 register config details? Or where can I get hardware setup details for ADAU1467 EVAL board?**

A: The ADAU1466 register configuration details can be referred from the data sheet and user guide. Refer :adi:`ADAU1466 Datasheet and Product Info \| Analog Devices <en/products/adau1466.html>`.

**Q: What is the maximum speed supported for EEPROM Read/Write operation? or What is Flash boot? Where can I get details?**

A: Refer data sheet and user guide of “ADAU14xx” user can see the EEPROM Read/Write and flash boot related information’s.

**Q: How can I configure the peripheral through SigmaDSP?**

A: The Master control port in SigmaStudio for ADAU145x/ADAU146x can be used to configure the peripherals. Please refer the link for more information.

:doc:`Master Control Port Boot time I/O (ADAU145x) [Analog Devices Wiki </wiki-migration/resources/tools-software/sigmastudio/toolbox/mastercontrolport/mastercontrolportio>`]

**Q: How can I add serial port details in custom schematic?**

A: **SigmaDSP:**

Please refer to the user guide available on the ADI website :adi:`https://www.analog.com/ <en/index.html>`. For example,

:adi:`ADAU1452 Datasheet and Product Info \| Analog Devices <en/products/adau1452.html>`

:adi:`ADAU1467 Datasheet and Product Info \| Analog Devices <en/products/adau1467.html>`

:adi:`ADAU1466 Datasheet and Product Info \| Analog Devices <en/products/adau1466.html>`

The :ez:`Q&A - SigmaDSP Processors and SigmaStudio Development Tool - EngineerZone (analog.com) <dsp/sigmadsp/f/q-a>` threads can also be referred by searching the serial port.

**SHARC:**

Please refer to the “AE_42_SS4G_IntegrationGuide.pdf” available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.

**Q: How many I/O buffers are declared in ADSP-215xx SigmaStudio for SHARC Framework?**

| A: The number of I/O buffers for each channel is declared in the “IC control – Hardware Configuration – Framework Config” window.
| |image26|
| **Q: Can customers use any unused framework buffer defined in the target firmware?**

A: Yes, if customers are sure that one or more of the defined buffers are unused, those buffers can be reused in the target firmware.

**Q: Where can I get Serial port details of SigmaStudio for SHARC framework?**

| A: Hardware schematic of the target hardware gives the information of the DAI pins used for I/O data. Configuration for the Serial port can be found in “IC control – Hardware Configuration – Framework Config” window.
| |image27|
| For more details, please refer to the “AE_42_SS4G_IntegrationGuide.pdf” available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.

**Q: How can I update SRU Routing for specific requirements in SigmaStudio for SHARC target application?**

| A: SRU routing can be updated using CrossCore Embedded Studio project under the “system.svc” settings.
| |image28|
| **Q: Why does ADSP-215xx wait indefinitely for SSn code?**

A: Sometime communication error occurs while downloading code from SigmaStudio using USBi. This error may cause an indefinite wait. Please check the USBi or AARDVARK interface to the EZ Kit evaluation board.

**Q: Does SigmaStudio for SHARC support SPDIF In/Out for SOM board? or where can I get more details about SPDIF interface for SOM board?**

A: Yes, the SigmaStudio for SHARC version 4.7.0 onwards supported SPDIF In/Out on SOM boards. The earlier versions supported only SPDIF In. Please refer section “Enabling S/PDIF Transmitter Feature support In Example Demo applications” in “AE_42_SS4G_QuickStartGuide.pdf” document which is present in the following installation path “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Rel4.7.0\\Docs”

**Q: How to integrate 3rd party algorithm having higher block size?** A:

-  Third party algorithms can be added to target application directly or by using algorithm designer as a custom plug into SigmaStudio.
-  Increase the number input and output buffers to 5 or 7 from the ‘Framework Config’ tab of the IC control window of the SigmaStudio schematic. A minimum of 5 or 7 buffers are recommended for SigmaStudio Block size of 64. Regenerate the framework config file by clicking on “Generate Config File” button within the ‘Framework Config’ tab of the IC control window and save the config file “adi_ss_fw_config.h” within “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-x.x\\Target\\Examples\\Framework\\Include” folder.
-  Increase the IPC FIFO Depth (ADI_SS_IPC_FIFO_DEPTH) to the same value as that of ADI_SS_FW_MAX_NUM_BUFFERS.
-  Increase in the number of input and output buffers may cause memory overflow issues. For ADSP-SC5xx processors, adjust the memory configuration by modifying the “ss4s.ld” linker description file (ensure that the MMU mappings defined in MMUConfig.c file matches the “ss4s.ld” changes). For ADSP-215xx processors, adjust the memory configuration by modifying the “app.ldf” linker description file.
-  There may be a need to map some of the data buffers to L3 sections so that there is space available for SigmaStudio code, data and parameters in L1 memory.
-  Disabling cache in the SHARC cores is observed to reduce MIPS. This can be done doing the following changes in adi_ss_cache_config.c file:

Change pREG_SHL1C0_CFG = ENABLE_I_D_CACHE;

To pREG_SHL1C0_CFG = DISABLE_I_D_CACHE;

-  Define SYNCHRONIZE_SH_CORES in the preprocessor definitions for the SHARC Core projects. This make sure that there is proper synchronization between cores.
-  The FIFO logic need to be implemented for accumulating required number of samples for calling 3rd party algorithm.
-  Regenerate the .ldr file after making the above changes

Modules Q & A
=============

**Q: How can I get details of the modules present in SigmaStudio?**

A: The steps to be followed for finding the list of modules supported for the selected IC,

-  Open SigmaStudio and select new project
-  Drag the IC to Hardware config window

| 
| |image29|
| \* Select the “Block Schematic” or “Schematic”

-  Enable the ToolBox view as shown in image to get details of modules supported in SigmaStudio

| 
| |image30|
| **Q: How can I add the custom plug in to SigmaStudio?**

A: The following step can be used to add the custom plug-in to SigmaStudio,

-  Open SigmaStudio and go to Tools
-  Select “Add Ins Browser.”
-  Add the plug-in dll using “Add Dll” option.

| 
| |image31|
| **Q: Do you have a separate Audio toolbox for SHARC?**

A: Yes, there is a separate audio toolbox for SHARC ADSP-214xx processors with some special modules. The customers should separately request for SHARC audio toolbox for ADSP-214xx. The SHARC+ already have the modules of SHARC audio toolbox within SigmaStudio for SHARC package and there is no need of any separate SHARC audio toolbox for SHARC+ processors.

**Q: Where can I get the list of modules supported on SHARC?**

A: The modules available in the SigmaStudio for SHARC package can be viewed in two steps,

-  Open SigmaStudio and verify whether SigmaStudio for SHARC plugins are added in “Add Ins Browser…” list of dlls.
-  Create new project and select required SHARC DSP ADSP-214xx or ADSP-215xx/ADSP-SC5xx
-  Click on Block schematic/schematic
-  On the left side “tree toolbox” shown which will have list of modules
-  Drag the module to Block schematic/Schematic window
-  Select the module and press “F1” to go to module help page.

| 
| |image32|
| **Q: How to update parameter or coefficient for custom module?**

A: Please refer to the “AE_42_SS4G_AlgorithmDesignerGuide.pdf” document available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.

**Q: How are memory mapping done for custom plugin created using Algorithm Designer?**

A: Please refer to the “AE_42_SS4G_AlgorithmDesignerGuide.pdf” under section “SigmaStudio Memory Type”. The data defined in the global space are mapped to selected parameter memory in the schematic.

**Q: What are the modules available for Frequency domain analysis?**

A: Refer the Wiki page link :doc:`frequencydomain </wiki-migration/resources/tools-software/sigmastudio/toolbox/frequencydomain>`

**Q: What are the standard audio modules ( e.g. Dolby, DTS etc.) available for SHARC?**

A: Please refer “\ :adi:`SigmaStudio for SHARC \| Analog Devices <en/design-center/evaluation-hardware-and-software/software/sh_sigst_00.html#software-overview>`\ ” or contact regional ADI representative for SHARC algorithms related queries.

**Q: How can I get MIPS and memory requirements for custom schematic? Or How can I detect MIPS and memory overflow without downloading the schematic?**

A: **SigmaDSP:** SigmaStudio display MIPS and memory details in the output window, which is at the right side of the tool. Output window also shows memory required for each of the modules in the schematic. User can get memory and MIPS requirements for each module by adding the module into to the simple schematic. The difference in MIPS and memory before and after adding the module will give the MIPS and memory requirement for the given module. Once the memory and MIPS of the modules are known, user can add the module into the original custom schematic under design. Good practice is that the user can add the memory and MIPS details into the Microsoft excel to keep track of memory and MIPS overflow.

**SHARC:** SigmaStudio displays the memory details in the output window, which is at the right side of the tool. Output window also shows memory required for each of the modules in the schematic. The MIPS information of SHARC ADSP-214xx/ADSP-215xx schematic modules can be generated using “IC Control – Hardware Configuration” window, please refer the below images. User should know the memory and MIPS requirements of each module by adding the module into to the simple schematic. The difference in MIPS and memory before and after adding the module will give the MIPS and memory requirement for the given module. Once the memory and MIPS of the module known, user can add the module into the original custom schematic under design. Good practice is that the user can add the memory and MIPS details into the Microsoft excel to keep track of memory and MIPS overflow.

| **Read MIPS ADSP-215xx:**
| |image33|
| **Read MIPS ADSP-214xx:**
| |image34|
| **Q: Is there any example for custom plugin?**

A: The custom plugin example for ADSP-215xx processors is available in “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Host\\Examples\\Sample Plug-Ins\\ADSP-SC5xx” folder. Please refer to the “AE_42_SS4G_AlgorithmDesignerGuide.pdf” available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs” for more details.

The custom plugin example for ADSP-214xx processors is available in “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Rel2.2.0\\Target\\ExtModules” folder. Please refer to the “SigmaStudio_for_SHARC_AlgorithmDesigner.pdf” available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Rel2.2.0\\Docs” for more details.

**Q: Do we support ADI surround block in ADSP-215xx?**

A:No, there is no plan for supporting ADI surround block in ADSP-215xx.

**Q: How do we get delay details for a given module?**

A:Overall delay for the schematic processing is equal to the schematic block size i.e., 64 by default. If there is any module specific delay, user can get the details from Wiki help page for the module. Follow the steps,

-  Drag the module to Block schematic/Schematic window
-  Select the module and press “F1” to go to module help page.

**Q: How can I update FIR Filter coefficients in SigmaStudio for SHARC?** FIR filter coefficients can be updated using following steps:

-  Click on the Table
-  Enter the floating-point coefficient values in the form
-  Click on the Update button to write the coefficients

| 
| |image35|
| **Q: How can I extend the filter order with available blocks in SigmaStudio?**

A: User can cascade the filters for required order or by using the “Nth order filter”. Please find the Wiki help page :doc:`NthOrderFilter. </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/nthorderfilter>`

**Q: How does the FIR Filter pool work?**

A: Refer Wiki page :doc:`FIRFilterPool. </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/firfilterpool>` Additionally, user can go to SigmaStudio module related help content by following below steps,

-  Drag the module to Block schematic/Schematic window
-  Select the module and press “F1” to go to module help page.

| 
| |image36|
| **Q: How can I add anti-aliasing filter IIR Up and Down sampler?**

| A: Anti-aliasing IIR filters need to be added after up sampling module and before Down sampling module.
| |image37|
| **Q: Does SigmaStudio for SHARC supports FIR/IIR accelerator for SOM boards? or How can I use FIR/IIR accelerator support for ADSP-SC598 SOM Board?**

| A: Yes, the modules for FIR/IIR accelerators are available in SigmaStudio for SHARC. Please refer to the below tree tool path.
| |image38|
| **FIR Accelerator:**
| |image39|
| Please refer to section “FIR/IIR Hardware Accelerator Multi-Instance support on ADSP-2159x/ADSP-SC59x” in “AE_42_SS4G_QuickStartGuide.pdf” document which is present in the following installation path “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.

**Q: How can I link the library function in SigmaStudio schematic process for SHARC?**

A: Algorithm Designer can be used to create custom plugin module to link the 3rd party library modules by writing the wrapper functions for accessing the library function.

**Q: Why the “Generate Assembly” buttons not working in SigmaStudio for SHARC Algorithm Designer for Custom plugin generation?**

A: The Algorithm design form should have at least 1 control to generate the assembly. We should at least add a label control into the Algorithm design form.

**Q: Why is parameter tuning not working for custom plugin?**

A:

-  Default parameters should be added into the custom plugin .xml file
-  Runtime parameters should be added in algorithm designer

| 
| |image2023-1-5_11-32-46.png|
| \* The runtime parameter should be assigned to default parameters as shown below,
| |image40|
| \* The runtime parameter should be assigned to UI controls as shown below, Step 1: Select and right click on the UI control, click on “Assign” option
| |image41|
| Step 2: In Control Action drop down select “ValueChanged”
| |image42|
| Step 3: Select the runtime parameter for corresponding UI control and click on apply
| |image43|
| Step 4: Review the UI control settings in properties window for Minimum, Maximum, Values
| |image44|
| These steps to be followed for every UI control to avoid runtime parameter tuning issues.

SigmaStudio for SHARC Host Packeting Q & A
==========================================

**Q: How target packet created in SigmaStudio for SHARC?**

A: Please refer to the “AE_42_SS4G_HostControllerGuide.pdf” document under “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Rel4.7.0\\Docs” folder.

**Q: What is the default SPI and I2C speed on USBi?**

A: The default SPI speed on USBi in SigmaStudio host is approximately 732 kHz. The default I2C speed on USBi in SigmaStudio host is approximately 84 kHz.

**Q: Whether the default SPI or I2C speed on USBi configurable?**

A: No the speed can't be configured for SPI or I2C on USBi.

**Q: What is the SPI baud rate supported by SigmaStudio Host?**

A: SPI speed is tested with SigmaStudio Host using Aardvark up to ~12 MHz. The limitation is due to time spent on packet data parsing and processing of the command and payload at the target side.

**Q: What is the maximum data length which can be read from target to SS Host?**

A: Seven words of data can be read in single param read. One payload word will have 16-bit of parameter data word. Please refer to the section A.1 Back Channel Protocol (SHARC Target to SigmaStudio Host) in “AE_42_SS4G_HostControllerGuide.pdf” document under “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs” folder.

**Q: How can I get checksum details?**

A: Please refer to the section “Packetizing Data” in “AE_42_SS4G_HostControllerGuide.pdf” available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”.

**Q: How can I do Block Safe load write for FIR Filter in SigmaStudio for SHARC framework?**

A: SigmaStudio host does not support block safeload write for FIR filter, since the block is configured for safeload write by default. Block safeload write for FIR filter can be achieved from microcontroller host. Please refer to the section “Packetizing Data” and “Block Safeload Parameter” in “AE_42_SS4G_HostControllerGuide.pdf” available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”

SigmaStudio Scripting Q & A
===========================

**Q: What are the automation scripts supported in SigmaStudio? Do you have example codes for automation?**

A: Please refer to :doc:`SigmaStudio Scripting [Analog Devices Wiki </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`] link for SigmaStudio automation script related information and examples.

**Q: Do SigmaStudio for SHARC modules support automation scripts supported in SigmaStudio? Do you have example codes for automation?**

A: Yes, SigmaStudio for SHARC modules support automation scripts supported in SigmaStudio. Please refer to “AE_42_SS4G_ScriptingGuide.pdf” available in the SigmaStudio for SHARC installation folder “C:\\Analog Devices\\SoftwareModules\\SigmaStudioForSHARC-SH-Relx.x.x\\Docs”. Additionally, the :doc:`SigmaStudio Scripting [Analog Devices Wiki </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`] link can be referred for more examples, since SigmaStudio for SHARC modules also supports the SigmaStudio scripting API’s.

**Q: How can I tune Custom modules through script?**

| A: The control parameter names for custom modules can be seen after enabling “View Control Parameter Names”, please refer the below image.
| |image45|
| Just hover on the custom modules to see the control parameter names. Refer to the below image.
| |image46|
| The control parameters can be used to tune the parameters using SigmaStudio script. For example:

object[] output; ss.ObjectSetProperties("setControlValue", "BiquadCascade1", 0, 0, "checkBox1_Checked", 0 );

ss.ObjectGetProperties("getControlValue", "BiquadCascade1", out output, 0, 0, " checkBox1_Checked");

ss.PrintLine(output[0].ToString());

ss.PrintLine("BiquadCascade1 is in OFF");

ss.ScriptDelay(500);

ss.ObjectSetProperties("setControlValue", "BiquadCascade1", 0, 0, "checkBox1_Checked", 1 );

ss.ObjectGetProperties("getControlValue", "BiquadCascade1", out output, 0, 0, "checkBox1_Checked"); ss.PrintLine(output[0].ToString());

ss.PrintLine("BiquadCascade1 is in ON");

| To change the name of the control parameter, refer below image,
| |image47|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/1.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/2.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/3.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/4.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/5.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/6.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/7.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/8.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_2-10-34.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_2-10-15.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_2-5-51.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_2-0-44.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_2-0-23.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_2-0-2.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_1-59-41.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_13-6-7.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_13-5-30.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_13-4-42.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_13-4-17.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/MemorySections.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/ParamBufferDefination.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/KeepSymbol.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/ExternDeclaration.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/l2mapping.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_13-3-44.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_13-3-13.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_13-2-48.png
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-12_12-59-5.png
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_14-30-25.png
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_14-31-32.png
   :width: 400px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_14-32-53_1_.png
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-15-53.png
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-20-34_2_.png
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-21-4.png
   :width: 400px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-23-34.png
   :width: 400px
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-24-54.png
   :width: 400px
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-25-39.png
   :width: 400px
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-26-26.png
   :width: 400px
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-26-51.png
   :width: 400px
.. |image2023-1-5_11-32-46.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2023-1-5_11-32-46.png
   :width: 400px
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2023-1-5_11-51-58.png
   :width: 400px
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2023-1-5_11-52-38.png
   :width: 400px
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2023-1-5_11-53-54.png
   :width: 400px
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2023-1-5_11-54-38.png
   :width: 400px
.. |image44| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2023-1-5_11-55-35.png
   :width: 400px
.. |image45| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-33-7.png
   :width: 400px
.. |image46| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-33-33.png
   :width: 400px
.. |image47| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/image2022-12-13_18-34-22.png
   :width: 400px
