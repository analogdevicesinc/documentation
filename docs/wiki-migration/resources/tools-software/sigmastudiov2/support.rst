:doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2>`

Support and FAQ
===============

| If you have a technical problem and you can't find a solution, you can contact for Technical Support by email: **ssplus_support@analog.com**
| =====FAQ=====
| ====Communication====
| **Q: Why does the readback from target fails even though the download is successful and there is audio playback?**
| A: When USBi is used as the communication device, the "FirmwareVersion" property of the USBi in SigmaStudio+ project should be set based on the version of the hardware. "FirmwareVersion" should be set as "v1.5" when the version of the USBi board is 1.5 or later and "Pre v1.5" should be used for 1.4 or earlier versions. This property can be updated using the SigmaStudio+ Property Window. Failure to set the proper version number can affect the readback operation.
| ====Download====
| **Q: Why does SigmaStudio+ throw "Target execution could not be verified" error while downloading a project, even though my target is active?**
| A: "Target execution could not be verified" indicates that SigmaStudio+ could not verify that the code has been downloaded on to the target and the target is running. This can happen primarily due to below reasons:

-  Target application is not loaded properly.
-  Target is executing properly. However, SigmaStudio+ is not able to read the status of the target.

| When USBi is used as the communication device, the "FirmwareVersion" property of the USBi in SigmaStudio+ project should be set based on the version of the hardware. "FirmwareVersion" should be set as "v1.5" when the version of the USBi board is 1.5 or later and "Pre v1.5" should be used for 1.4 or earlier versions. This property can be updated using the SigmaStudio+ Property Window. Failure to set the proper version number can affect the readback operation and target verification.
| |image1|
| If we are using SOM-Carrier board, below settings should be configured properly.

-  Please check whether the USBi connection is as per the below image which is connected to carrier board (brown

| color wire should be connected near the Starting letter of SigmaStudio “S”).
| |image2|

-  “SW1” switches should be in off condition on carrier board as shown in the below image.

| 
| |image3|
| For custom applications, please uncheck the target verification option in the Settings window of SigmaStudioPlus (**Tools** menu => **Settings** button => **Processor** Group => uncheck **Target Verification** checkbox) as shown in the below image
| |image4|
| **<fc #ff0000>Note</fc>:** Even after confirming the above-mentioned configuration, If we are still facing an issue, please select the arm core and suspend all the cores in CrossCore Embededd Studio and check the status if any target exception is showing in the console window.

Platform
--------

| 
| **Q: Project download on to ADSP-21489 fails when the target application is loaded from serial (SPI) flash. What is the reason?**
| A: On ADSP-21489, SPI Flash and USBi shares the same SPI lines. As a result, the SPI boot fails when USBi is connected.

-  When SPI boot fails, LED 1-8 will be ON
-  When SPI boot succeeds, LED 1 will be ON. LED 2-8 will be OFF.

| Workaround is to disconnect the USBi, reset the board (then successful boot happens and LED1 will be ON). Now connect the USBi and download the project from SigmaStudio+. Upon successful download, you will find LED 1-4 ON.

--------------

| **Q: What is the clocking scheme in the Demo and DemoUc example applications for each processor?**
| **A:** The current setup of the Demo and DemoUc example applications configures the BCLK and FS clocking scheme as follows.
| ^ **Processor** ^ **BCLK and LRCLK Source** ^ **DAI Pin** ^ **Description** ^

+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
| ADSP-21568, ADSP-21569             | PCG-C: BCLK  | DAI0_PB07            | PCG-C BCLK available at specified pin for the SPORT BCLK (For TDM8 - 12.288MHz) |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB05            | PCG-C BCLK available at specified pin for DAC BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB08            | PCG-C BCLK available at specified pin for A2B BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB12            | PCG-C BCLK available at specified pin for ADC BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-C: LRCLK | DAI0_PB19            | PCG-C LRCLK available at specified pin for the SPORT LRCLK (48KHz)              |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB04            | PCG-C LRCLK available at specified pin for the DAC LRCLK (48KHz)                |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB09            | PCG-C LRCLK available at specified pin for the A2B LRCLK (48KHz)                |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB20            | PCG-C LRCLK available at specified pin for the ADC LRCLK (48KHz)                |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-A: BCLK  | DAI0_PB03            | PCG-A BCLK available at specified pin for the A2B BCLK (For I2S- 3.072MHz)      |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB07            | PCG-A BCLK available at specified pin for the SPORT BCLK (For I2S- 3.072MHz)    |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-A: LRCLK | DAI0_PB04            | PCG-A LRCLK available at specified pin for the A2B LRCLK (48KHz)                |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB19            | PCG-A LRCLK available at specified pin for the SPORT BCLK (48KHz)               |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
| ADSP-21573, ADSP-SC573, ADSP-SC589 | PCG-B: BCLK  | DAI0_PB02            | PCG-B BCLK available at specified pin for DAC BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI0_PB12            | PCG-B BCLK available at specified pin for ADC BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI0_PB13            | PCG-B BCLK available at specified pin for A2B BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-B: LRCLK | DAI0_PB04            | PCG-B LRCLK available at specified pin for DAC LRCLK (48KHz)                    |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI0_PB14            | PCG-B LRCLK available at specified pin for A2B LRCLK (48KHz)                    |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI0_PB20            | PCG-B LRCLK available at specified pin for ADC LRCLK (48KHz)                    |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
| ADSP-SC589-SAM                     | PCG-C: BCLK  | DAI0_PB10            | PCG-C BCLK available at specified pin for SPORT BCLK (For TDM8 - 12.288MHz)     |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB02            | PCG-C BCLK available at specified pin for DAC BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB12            | PCG-C BCLK available at specified pin for ADC BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-C: LRCLK | DAI0_PB12            | PCG-C LRCLK available at specified pin for SPORT LRCLK (48KHz)                  |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB04            | PCG-C LRCLK available at specified pin for DAC LRCLK (48KHz)                    |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB20            | PCG-C LRCLK available at specified pin for ADC LRCLK (48KHz)                    |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-A: BCLK  | DAI1_PB11            | PCG-A BCLK available at specified pin for SPORT BCLK (For I2S- 3.072MHz)        |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-A: LRCLK | DAI1_PB19            | PCG-A LRCLK available at specified pin for SPORT LRCLK (48KHz)                  |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
| ADSP-21584, ADSP-SC584             | PCG-C: BCLK  | DAI0_PB03, DAI0_PB10 | PCG-C BCLK available at specified pin for SPORT BCLK (For TDM8 - 12.288MHz)     |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB02            | PCG-C BCLK available at specified pin for DAC BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB12            | PCG-C BCLK available at specified pin for ADC BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-C: LRCLK | DAI0_PB04, DAI0_PB12 | PCG-C LRCLK available at specified pin for SPORT LRCLK (48KHz)                  |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB04            | PCG-C LRCLK available at specified pin for the DAC LRCLK (48KHz)                |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB20            | PCG-C LRCLK available at specified pin for the ADC LRCLK (48KHz)                |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-A: BCLK  | DAI1_PB11            | PCG-A BCLK available at specified pin for SPORT BCLK (For I2S- 3.072MHz)        |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-A: LRCLK | DAI1_PB19            | PCG-A LRCLK available at specified pin for SPORT LRCLK (48KHz)                  |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
| ADSP-21593, ADSP-SC594             | PCG-C: BCLK  | DAI0_PB07            | PCG-C BCLK available at specified pin for the SPORT BCLK (For TDM8 - 12.288MHz) |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB05            | PCG-C BCLK available at specified pin for DAC BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB12            | PCG-C BCLK available at specified pin for ADC BCLK (For TDM8 - 12.288MHz)       |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-C: LRCLK | DAI0_PB19            | PCG-C LRCLK available at specified pin for the SPORT LRCLK (48KHz)              |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB04            | PCG-C LRCLK available at specified pin for DAC LRCLK (48KHz)                    |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    |              | DAI1_PB20            | PCG-C LRCLK available at specified pin for ADC LRCLK (48KHz)                    |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-A: BCLK  | DAI1_PB07            | PCG-A BCLK available at specified pin for the SPORT BCLK (For I2S- 3.072MHz)    |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+
|                                    | PCG-A: LRCLK | DAI1_PB19            | PCG-C LRCLK available at specified pin for the SPORT LRCLK (48KHz)              |
+------------------------------------+--------------+----------------------+---------------------------------------------------------------------------------+

.. note::

   
   -  The BCLK and LRCLK routing for SPORT will be automatically configured in the Demo/DemoUc framework based on the SPORT selection made in the SigmaStudio+ schematic configuration.
   -  The user must assign the DATA pin for the SPORT in the SigmaStudio+ schematic configuration. The DATA pin routing will then be automatically handled by the Demo/DemoUc framework.
   -  The user must route BCLK and LRCLK to the external audio peripheral using the **system.svc – SRU Routing** and **adi_ss_fw_sport.c** option.
   -  Any modification to the DAI pin or PCG clock requires corresponding pin assignment and signal routing within the default framework.
   


--------------

| 
| **Q: How to integrate a new SPORT interface for audio input/output streams in default target framework?**
| **A:** In order to integrate a new SPORT interface for audio input/output streams into the default target framework, changes must be made both in the **SigmaStudio+ schematic** and in the **target application**, as described below.
| **1. SigmaStudio+ Schematic Changes**
| \**Adding a Source SPORT in the SigmaStudio+ schematic SPORT Configuration: \*\*
| \* Open the schematic in SigmaStudio+ and go to **SPORT Configuration** in the **Project window**.

-  Increase the **Number of Sources** from the default value of 2 to 3, as shown in the image.

| |image5|
| **<fc #ff0000>Note</fc>:** The newly added SPORT number needs to be selected according to the chosen DAI pin. Please make sure not to change the SPORT configuration of any existing SPORTs.

-  The audio data pin used, data format (operation mode: I2S / TDM4 / TDM8 / TDM16), number of active channels, serial word length (8 / 16 / 24 / 32) and clock polarity can be configured in the **Configure SPORT** section based on the requirements.

| 
| \**Adding a Sink SPORT in the SigmaStudio+ schematic SPORT Configuration: \*\*
| \* Open the schematic in SigmaStudio+ and go to **SPORT Configuration** in the **Project window**.

-  Increase the **Number of Sinks** from the default value of 1 to 2, as shown in the image.

| |image6|
| **<fc #ff0000>Note</fc>:** The newly added SPORT number needs to be selected according to the chosen DAI pin. Please make sure not to change the SPORT configuration of any existing SPORTs.

-  The audio data pin used, data format (operation mode: I2S / TDM4 / TDM8 / TDM16), number of active channels, serial word length (8 / 16 / 24 / 32) and clock polarity can be configured in the **Configure SPORT** section based on the requirements.

| 
| \* First, delete the Input module from the schematic. Then, modify the number of input/output channels as required under **SHARCXICore_C1/SHARCXICore_C2 -> Settings** (based on the processor). The schematic-side I/O channel configuration needs to be modified based on the number of active channels selected in the SPORT configuration. Then drag and drop the modules again with the updated I/O channel count.
| Using the SigmaStudio+ schematic shown in the images here as a reference:

-  Adding a source SPORT configured for TDM8 with 8 active channels increases the total input channels to 16: 6 from SPORT4A, 8 from the newly added SPORT1A, and 2 from SPORT0A. In this configuration, SPORT4A data is available on channels 0–5, SPORT1A data on channels 6–13, and SPORT0A data on channels 14–15.
-  Adding a source SPORT configured for I2S with 2 active channels increases the total input channels to 10: 6 from SPORT4A, 2 from the newly added SPORT1A, and 2 from SPORT0A. In this configuration, SPORT4A data is available on channels 0–5, SPORT1A data on channels 6–7, and SPORT0A data on channels 8–9.
-  Adding a sink SPORT configured for TDM8 with 8 active channels increases the total output channels to 16: 8 channels from SPORT5A and 8 from the newly added SPORT2A. In this configuration, SPORT5A data is available on channels 0–7, and SPORT2A data on channels 8–15.
-  Adding a sink SPORT configured for I2S with 2 active channels increases the total output channels to 10: 8 channels from SPORT5A and 2 from the newly added SPORT2A. In this configuration, SPORT5A data is available on channels 0–7, and SPORT2A data on channels 8–9.

| 
| **<fc #ff0000>Note</fc>:** The order in which SPORTs are configured with active channels in the UI defines how input channels are mapped within the input block.
| \* Once the SPORT configuration and channel numbers are modified, the user needs to regenerate the configuration files as shown below, since there is a difference from the default framework.

-  Navigate to the **Project Window -> Settings -> Framework** section in order to generate new framework configuration files.

| |image7|
| \* Replace **adi_ss_fw_config** or **adi_ss_fw_config_2156x** (based on the processor) in the **C:\\Analog Devices\\SigmaStudioPlus-Relx.x.x\\Target\\Examples\\Framework\\Include** directory.
| ===2. Target Application Changes===

-  Change the value of the macro **SOURCE_SPDIF**, defined in the **adi_ss_fw_dataHandle_Sh.c** file, from the default value of 1 to another value (e.g., 3). This is necessary because the target, by default, considers the second source SPORT as SPDIF, and the data shift occurs based on this macro value; therefore, it needs to be incremented.
-  Rebuild and run the application. Download the schematic from SigmaStudio+ UI.

|

.. note::

   A) The above-mentioned changes for supporting additional source and sink SPORTs apply only to the Demo and DemoUc applications with TDM8 or I2S formats.

   | B) If a clocking change is required to support formats other than TDM8 and I2S, the PCG configuration in the framework must be updated.
   | C) If the existing ADC and DAC need to support other formats (such as TDM4, TDM16, etc.), then the following changes are required:
   
   -  SRU routing changes to receive the BCLK and FS from the generated PCG.
   -  Updating the ADC and DAC configuration registers for the required format.
   


--------------

| 
| **Q: How to integrate a new SPORT interface for audio input/output streams in default LibraryIntegration Example?**
| **A:** Please refer to this :ez:`Ezone Link <dsp/software-and-development-tools/sigmastudio-for-sharc/w/documents/33914/integrating-additional-input-output-sport-interfaces-in-the-adsp-2156x-library-example>`, which provides a ZIP file containing the example project (using ADSP-2156x) and a document outlining the required changes. The changes mentioned are generic and applicable to the LibraryIntegration examples for other processors as well.

--------------

| 
| **Q: How can the audio module be tuned using the ADSP-SC573 DemoUc application available with the installation package from the UI?**
| **A:** When it comes to the ADSP-SC573 DemoUc example, the application, by default, is designed for audio module tuning using the EZLITE on-board push buttons (for Mute Enable/Disable and Filter Enable/Disable). However, if you want to perform tuning from the SigmaStudio+ UI, you need to disable the push buttons, since the push buttons and SPI1 (used for SigmaStudio+ schematic download and tuning) share the same pins. The push buttons can be disabled in the target application by navigating to **SS_Uc_App_Core0-> Source -> Framework -> adi_ss_uc_app_softconfig_SC573.c** file, as shown below.
| |image8|
| Afterwards, use the **Link-Compile-Connect** option in SigmaStudio+ for runtime tuning from the UI.

--------------

| \**Q: What is the maximum number of words that can be read back from the SHARC target using a read request command? \*\*
| A: The maximum number of words that can be requested to be read in a single read request is seven.

--------------

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/USBiFirmwareVersionSettings.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/USBiConnection.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/CarrierBoardSwitchSettings.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/Custom_App_Host_Settings.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/ajaxperflookupdelay/sourceonly_tdm.png
.. |image6| image:: https://wiki.analog.com/_media/ajaxperflookupdelay/sinkonly_tdm.png
.. |image7| image:: https://wiki.analog.com/_media/ajaxperflookupdelay/generateconfigfile.png
.. |image8| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/adsp_sc573_demouc_ui_tune.png
   :width: 600px
