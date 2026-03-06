FAQs on SigmaStudio+ and A2B:
=============================

General Q & A
=============

**1. What is SigmaStudio+ software for A2B?**

The SigmaStudio®+ is a graphical development tool for programming, development, and tuning the software for ADI A2B® transceivers. It is mainly used to create a schematic, Design and Validate the A2B network.

**Note:** Future A2B plugins update will be available for SigmaStudio+ only.

**2. What is A2B Plugin for SigmaStudio+?**

The A2B Plugin Software is an add-on to SigmaStudio+ that enables the user to graphically model an A2B network, which facilitates quick evaluation and bring-up of the network with audio routing. Once the network is stabilized, the configuration can be exported into an embedded platform. The A2B stack uses this configuration and manages the A2B network.

**3. Where can I download SigmaStudio+?**

The latest SigmaStudio+ release package can be downloaded from :adi:`SigmaStudio®+ \| Analog Devices. <en/design-center/evaluation-hardware-and-software/software/sigmastudio-plus.html#software-relatedsoftware>`

**Note:** If you are using SigmaStudio+ 2.0.0, Please update the software to Update1(2.0.1) which is required for A2B -SigmaStudio+ Plugin 1.2.0. The SigmaStudio+ software update is available in “Help → Check For Updates”

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/checkupdate.png
   :align: center

**4. Where can I download the latest A2B plugin for SigmaStudio+?**

Latest version of A2B plugin for SigmaStudio+ for Windows/BareMetal can be found on the Analog Devices Gated website under Software section :adi:`A²B Technology \| Analog Devices <en/gated/a2b/a2b-technology.html>`

**5. Where can I find an example schematic for an A2B network?**

Example Schematics can be used to run a quick demo on PC using SigmaStudio+ and it is available in the following Path: C:\\Analog Devices\\ADI_A2B-SSPlus_Software-#version\\Schematics\\PC. The XML files to configure the Audio host and codecs can be found in C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Schematics\\PC\\xml

**6. Where can I find the installation folders for A2B software, SigmaStudio+ on my PC?**

For A2B Plugin Software: C:\\Analog Devices\\ADI_A2B-SSPlus_Software-#version For SigmaStudio+: C:\\Analog Devices\\SigmaStudioPlus-RelX.Y.Z

**7. Where can I find User Guides for setting up of A2B Network and SigmaStudio+?**

Starting Guide for Setting up of A2B system using SigmaStudio+ quickly can be found in the installation path “C:\\Analog Devices\\ADI_A2B-SSPlus_Software-#version\\Docs”. Soon it will be available part of analog.com

**Note:** Release notes for A2B plugin and license agreement documents (Click Thru ELA/SLA) can be found in C:\\Analog Devices\\ADI_A2B-SSPlus_Software-#version

**8. Is A2B SigmaStudio+ support migration of A2B Schematic from SigmaStudio to SigmaStudio+?**

Migration of A2B Schematic from SigmaStudio to SigmaStudio+ will be supported in future releases.

**9. Can we import busconfig.xml file from SigmaStudio to SigmaStudio+?**

Importing of busconfig.xml from SigmaStudio to SigmaStudio+ will be supported in future releases.

**10. How to set the order of programming of I2C peripherals while using SigmaStudio+?**

The order of peripheral programming depends on which peripheral is dragged and dropped first from the toolbox. The order can be changed in the Project Tree by selecting the peripheral and moving it using the arrow. For example, if we have two peripherals Codec and EEPROM, the peripheral used for EEPROM is dragged and dropped first into the schematic, and the peripheral used for Codec is dragged and dropped later into the schematic, then EEPROM will be programmed first and followed by Codec.

**11. How do I open a SigmaDSP project from within the A2B project? This was easily done in SigmaStudio from the peripheral properties window, but I cannot seem to figure out how to do so in SigmaStudio+?**

The idea with SigmaStudio+ is not to have a separate project for SigmaDSP but integrate the SigmaDSP schematic and configuration in the same project. So, there is no need to track it as a separate SigmaDSP project. If there is an integrated SigmaDSP schematic, then you can right click and select open schematic to see the SigmaDSP schematic. The xml generated for the SigmaDSP will be part of the settings of the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/opendspschematic.png
   :align: center

**12. How to ensure that Link Compile Download is successful or not?**

You will the see A2B nodes turn green, and discovery successful message will be notified. Similarly when the platforms are double clicked the status is updated for Peripherals as well.

|image1| |image2|

**13. When to Use the Standard Platform vs. the Custom Platform?**

If a standard platform, such as evaluation boards, is not available in SigmaStudio+, customers can use the custom platform. They can drag and drop the custom platform into their project and include the respective transceivers or peripherals as needed.For more information, visit :doc:`Custom Platform vs Standard Platforms </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/customvsstandard>`.

**14. Platform Abstraction Layer Changes for DAT File Parsing/Read from EEPROM**

To enable DAT file parsing and support for reading configurations from EEPROM, the following modifications are required in the Platform Abstraction Layer (PAL):

-  **Add Macros for EEPROM Address Offset:** In conf.h, define the starting address for the local EEPROM: <code> #define A2B_EEPROM_ADDR_OFFSET (0u)</code>
-  **Define Macros for 16-bit Integer Manipulation:** In ctypes.h, include macros for handling 16-bit integers in big-endian format: ``#define A2B_GET_UINT16_BE(n,b,i) \
   do { (n) = ((a2b_UInt16)(b)[(i)] << 8u) | ((a2b_UInt16)(b)[(i) + 1u]); } while(0)
   #define A2B_PUT_UINT16_BE(n,b,i) \
   do { (b)[(i)] = (a2b_UInt8)((n) >> 8u); (b)[(i) + 1u] = (a2b_UInt8)((n)); } while(0)``
-  **Enable Features for File and EEPROM Operations:** In features.h, add macros to enable processing configurations from EEPROM or files: ``#define A2B_BCF_FROM_SOC_EEPROM
   #define A2B_BCF_FROM_FILE_IO``
-  **Update PAL Structure for EEPROM and File Operations:** In palecb.h, add the following members to the a2b_PalEcb structure: ``a2b_Handle fp;
   a2b_UInt8* pEepromAudioHostConfig;``
-  **Declare APIs for File and EEPROM Handling:** In adi_a2b_externs.h, declare the necessary APIs: ``#if defined(A2B_BCF_FROM_FILE_IO)
   a2b_HResult a2b_pal_FileOpen(A2B_ECB* ecb, char* url);
   a2b_HResult a2b_pal_FileRead(a2b_Handle hnd, a2b_UInt16 offset, a2b_UInt16 nRead, a2b_Byte* rBuf);
   a2b_HResult a2b_pal_FileClose(A2B_ECB* ecb);
   #endif
   a2b_HResult a2b_EepromWriteRead(a2b_Handle hnd, a2b_UInt16 addr, a2b_UInt16 nWrite, const a2b_Byte* wBuf, 
   a2b_UInt16 nRead, a2b_Byte* rBuf);``
-  **Specify Binary File Path:** In a2bapp_defs.h, define the path for the binary BCF file: ``#define A2B_CONF_BINARY_BCF_FILE_URL "../adi_a2b_busconfig.dat"``
-  **Implement File Handling Functions:** In adi_a2b_pal.c, implement functions for file operations and integrate them into the a2b_palInit() function: ``#if defined A2B_BCF_FROM_FILE_IO
   pal->fileRead = a2b_pal_FileRead;
   #endif``
-  **Add Definitions for File Handling APIs:** Define a2b_pal_FileRead, a2b_pal_FileOpen, and a2b_pal_FileClose in adi_a2b_pal.c.

To obtain the comprehensive document with detailed instructions, please contact A2B Software Support at: `a2bsoftwaresupport@analog.com <https://wiki.analog.com/a2bsoftwaresupport@analog.com>`__.

**15. List the Possible Causes for the Node Not Being Discovered**

-  Incorrect bus or transceiver configuration.
-  Power supply or cable connection issues.
-  Wrong I2C address settings.
-  Software or firmware version mismatch.
-  Faulty hardware components.

For further assistance, contact `a2bsoftwaresupport@analog.com <https://wiki.analog.com/a2bsoftwaresupport@analog.com>`__.

**16. How to Deselect the Older Plugins and Add New Plugins in SigmaStudio+ (When Multiple A2B Plugins Are Installed)**

To manage A2B plugins in SigmaStudio+:

-  Go to Tools > Add-In Browser.
-  In the Add-In Browser window, select or deselect the required A2B plugins from the list.
-  Restart SigmaStudio+ for the changes to take effect.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2b_plugin_select.png
   :align: center

**17. Open Source Software Used in A2B Software**

The Open Source software used in the A2B Stack is documented in the click-thru SLA document, located at:**C:\\Analog Devices\\ADI_A2B-SSPlus_Software-RelX.Y.Z.**


|image3|

**18. Explain How Auto Rediscovery Will Be Initiated and for Which Faults**

The application detects node drops by frequently reading the Vendor ID register and sets the **bFaultDone** and **bRetry** flags if unexpected values are found. When Line Fault Diagnostics and Auto-Rediscovery are enabled in SigmaStudio/SigmaStudio+, any power fault interrupt triggers the **a2bapp_onPowerFault()** function, where these flags are set. The **a2b_fault_monitor()** function then monitors these flags and initiates auto-rediscovery to restore the A2B network.

**19. Bit Error Rate Report Time Increases in the Long Run; Does It Have an Effect on the Error?**

No, the increase in Bit Error Rate (BERT) report time during long runs does not affect the actual error rate. It only impacts the reporting interval, not the accuracy or occurrence of errors in the system.

**20. When the Basic Authentication Error Occurs**

In A2B, a Basic Authentication error occurs when there is a failure in validating the Vendor ID register, which does not read the expected value of **0xAD**.

**21. Register Settings to Enable Microphone on AD2428WB1BZ and AD2433WB1BZ**

For the **EVAL-AD2428WB1BZ** board, configure it as a microphone node by setting the following registers:

-  **PDMCTL (0x47) to 0x1C**
-  **PDMCTL2 (0x5D) to 0x10**

These settings enable and configure the PDM microphones for proper operation.

For the **EVAL-AD2433WB1BZ** board, configure it as a microphone node by setting the following registers:

-  **PDMCTL (0x47) to 0x1C**
-  **PDMCTL2 (0x5D) to 0x1C**

These settings enable and configure the PDM microphones for proper operation.

**22. EEPROM Size Limitation on Eval Board for Self-Boot Functionality**

The **EVAL-AD2428WD1BZ** main node uses a 64KB EEPROM, which may cause the self-boot process to fail due to size limitations. To store large data, upgrading to a larger EEPROM is recommended to ensure the self-boot functionality works properly.

**23. Where Can I Find the Self-Boot Support DLL and Related Documents?**

The A2B SelfBoot DLL for SigmaStudio/SigmaStudio+ and related documentation can be found on the following gated website: :adi:`A2B technology \| Analog Devices <en/gated/a2b/a2b-technology.html>`

**24. Which Registers Are Used to Generate or Raise the Interrupts in A2B Transceiver?**

The register used to generate or raise interrupts in an A2B transceiver is the **RAISE (0x54)** register.

**25. Crystal Clock Change Update for ADSP-SC589-MINI Platform and What Necessary Changes to Be Done in Application**

To update the clock frequency and PLL settings for the **ADSP-SC589-MINI Rev 2.1**, modify the **FSDIV** value to 512 and update the **Clock Control 1 Register** as shown below in the **adi_a2b_InitPCGForAD24xx()** function in adi_a2b_sportdriver.c. |image4| Additionally, change the **R** value in the **ADAU1761 PLL control register** to 2 in ADAU1761 schematic. Ensure to perform a power cycle before downloading the code to the hardware. These updates account for the change in clock frequency from **12.288 MHz (Rev 1.5)** to **24.576 MHz (Rev 2.1)**, and the PLL configuration will be applied accordingly.


|image5|

**26. Which Registers Are Not Exported to BusConfigurationFile?**

All A2B registers are exported to the Bus Configuration file.

**27. Why Do the Read Values in the Command List Don't have the Correct Value?**

The read values in the command list may not be accurate because they are not retrieved from the actual hardware.

**28. Cable Length Exported in BCF.xml File but Not Exported in BCF.c**

The cable length is included in the BCF .xml file, allowing the schematic to be recreated from the XML. In the BCF .c file, the cable length is not directly included but is used internally to calculate the Response Cycle, which is then exported.

**29. I2STEST Register Not Exported in the Command List File**

Only the discovery sequence is exported in the command list file. The **I2STEST** register, being a debugging register, it is not included in the command list file. If writing to the **I2STEST** register is required, it can be handled directly within the application.

Common Errors:
==============

**1. Why am I getting project invalid error while opening SigmaStudio+ project?**

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/projectinvalid.png
   :align: center

Please ensure that you have installed A2B Plugins before opening SigmaStudio+ Projects for A2B.

**2. Why am I getting “Unable to detect valid SigmaStudio+ version” error while installing A2B plugin even though the SigmaStudio+ software is installed?**

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2b_plugin_install_err.png
   :align: center

Please ensure that you have the compatible version of SigmaStudio+ installed before installing A2B plugin. To Check for updates, go to “Help → Check For Updates”.

**3. Why am I getting “Target communication failed” error while downloading from SigmaStudio+?**


|image6|

Ensure the Target board is connected to the host (PC) through USBi properly and the local powered nodes are connected to power supply.

**4. What is “Authentication failure Error” during discovery of default schematic?**


|image7|

The error may occur due to the ‘Silicon Revision’ mismatch of the transceiver, you can update the settings of silicon revision or you can enable ‘Disable transceiver authentication’ option.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/disable_auth.png
   :align: center

**5. After clicking the ‘Link-Compile’ button, Link-Compile-Download button is disabled, how to enable it?**

Click anywhere in the SigmaStudio+ window to enable the button again.

**6. Why do we get the “Unknown error found during discovery” error while downloading the Schematic in SigmaStudio+?**


|image8|

This error occurs for the following scenarios,

• If the schematic is not saved before proceeding to download it to the target. Do Save the Schematic before downloading it to the target.

• If the peripherals connected to main node does not have the right address.

Check the output window for more details.

**7. What is “Main Running Interrupt Not Detected” error?**

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/main_running_not_detected.png
   :align: center

This error could be occurring due to below reasons:

• Please ensure that you have selected the proper XML file for the Audio host and that ‘Program during discovery ‘is enabled.

**8. What is the “I2C error at Main Node” error during discovery?**

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/i2c_err.png
   :align: center

Please check the ‘Main Address(I2C)” in the Main Node and check the Jumper setting, which can be found in ‘A2B-SSPlus_Quick_Start_Guide’ available in the path “C:\\Analog Devices\\ADI_A2BSSPlus_Software-Relx.y.z\\Docs”.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/main_node_add.png
   :align: center

**9. Bandwidth Overshoot Error**

A Bandwidth Overshoot Error happens when the configured channels exceed the 1024-bit limit of the A2B superframe. To stay within this limit, ensure the bandwidth does not exceed 1024 bits. For instance, if configuring 32 channels for upstream/downstream, consider reducing the data width to 16 bits or 8 bits per channel instead of using higher data widths. The Bandwidth Calculation Spreadsheet is available in the Application Notes section at the following link: :adi:`A2B technology \| Analog Devices <en/gated/a2b/a2b-technology.html>`


|image9|

**10. SigmaStudio+ GUI is frozen when settings tab is accessed for an A2B node from Custom Platform Design?**

This issue is specific to 1.2.1 release of A2B. Instead of adding sub shapes like main node, generic device in custom node, Export the shape contents of standard Nodes.

• Drag & drop required A2B nodes on the design canvas and save shape contents of standard platform to a file.

• Create custom platform and load shape contents (of standard platform) onto custom platform and then make required settings.

**11. I am getting “I2C Transaction error” during discovery with a .dat file generated for A2B Network containing 2433 main and sub nodes from SigmaStudio+?**

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/i2c_to_spi_err.png
   :align: center

In the A2B schematic, If the USBi is connected to the 2433 main node through I2C and if the 2433 sub-node contains SPI peripheral (EEPROM) then the above-mentioned error will be notified. I2C to remote SPI peripheral programming is not supported.

**12. After attempting SigmaStudio+ window open and close, main GUI has disappeared and only project window remains. When tried to open SigmaStudio+, only project window appears.**

Please go to the folder "C:\\Users\\<your user name>\\AppData\\Roaming\\SigmaStudio" and delete all the xml files starting with layoutDefault (layoutDefault\*.xml). Now restart SigmaStudio+.

**13. Why am I getting “Custom Node Authentication failure” Error?**

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/custom_auth_failure.png
   :align: center

During A2B discovery process, the stack will read the Custom Identifier value from the remote memory device via I2C at the specified address/ read the GPIO status / read the custom node identifier value via mailbox registers and validate it against the assigned value. If there is a match, then the node will be successfully configured otherwise the discovery will be aborted.

**14. Where can I extract .dat file from SigmaStudio+, It is not found under export configuration?**

The option to export the bus configuration dat file is under “EEPROM DUMP” tab of Export Import Settings window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/eeprom_dump.png
   :align: center

**15. After docking any window to title bar, it is unable to close the window.**

Under View -> Layout -> Reset Layout can be provided. If this does not work, then delete layout file from "C:\\Users\\<your user name>\\AppData\\Roaming\\SigmaStudio". Delete all the xml files starting with layoutDefault (layoutDefault\*.xml). Now restart SigmaStudio+.

**16. What is the below error on I2C Error Notification?**

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/peripheral_prog_fail.png
   :align: center

There is no Peripheral with Address 0x40 connected to sub node 1.

**17. What is the “active”, “error” and “design” indicated at the right end of SigmaStudio+ screen.**

This is the current state of schematic where,

Active → Indicates Successful download

Error → Indicates there is failure during download

Design → Indicates the schematic is being currently updated

**18. How can one access the A2B registers?**

All the registers of A2B can only be accessed using 8-bit addresses. To access PWM/VMTR registers, you need to update the MMRPAGE register value to 0x01 and then access using the last 8-bit register address. The transceiver will internally handle this correctly.

**19. What is the procedure to do A2B I2S loopback test when SigmaStudioPlus/PC is acting as the host? And how is it different when we are running with on board microcontroller as host?**

While SigmaStudioPlus/PC is the host, after discovery, the customer can use the I2STEST register that is available in the Register view in A2B Plugin 1.3.0, to enable loopback test. Setting the register value to 0x10 enables Bus loopback feature.

While running target application, the I2STEST register is exported to BCF (Bus Config File), but it is not used in the A2B Stack. Thus, the customer must write to this register after discovery from the application to enable loopback testing feature.

**20. What is the approximate time taken for the entire A2B Discovery process?**

Please find the discovery timing details below

.. image:: https://wiki.analog.com/_media/resources/tools-software/discovry_timing.png
   :align: center

.. note::

   The above details are measured with One Main and 2 Sub node Configurations on ADSP-SC594 and these are reference timing details and will vary based on the number of register configurations for each node and no of peripheral configurations.


**21. Is it possible to switch multiple stream definition during runtime without re-discovery?**

No. As of now, such feature has not been implemented in A2B stack or in SigmaStudioPlus.

\**22. \*\*

.. image:: https://wiki.analog.com/_media/resources/tools-software/linefaultsettings.png
   :align: center

**a) Is 'Line Fault settings' applicable for post discovery or initialization discovery or both**

Line fault settings are only applicable for post-discovery.

**b) If Auto-Rediscovery upon Faults option is the only enabled, How will this work functionality vice and what are the critical faults applicable?**

If Auto-Rediscovery upon Faults is only enabled - When a fault occurs, the system will attempt to rediscover the entire A2B network from the last LPS node(main node, if the main node is the last Local powered node) to the last sub-node, using the number of attempts configured. This functionality applies to all types of faults including critical faults and non-critical faults.

**c) If Auto-Rediscovery upon Faults and Partial Discovery both enabled, How will this work functionality vice and what are the faults applicable?**

If Auto-Rediscovery upon Faults and Partial Discovery are both enabled - The system will rediscover the A2B network from the node where the fault occurred to the last sub-node, using the number of attempts configured.

If the faults are not critical fault (open wire), in this case, it will retry the discovery of the dropped nodes without disturbing the discovered nodes.

If the faults are critical faults (Power faults), the fault will propagate back to the next upstream local powered node in this case, it will retry the discovery of the network after upstream local powered without disturbing the other nodes.

During this partial rediscovery of the network, the previous nodes before the fault occurrence are not affected. This functionality applies to all types of critical faults.

**23. “Main Running Interrupt Not Detected” error found during Link Compile Download of A2B schematic in SigmaStudioPlus. What could be the root cause?**

The occurrence of the "Main running interrupt not detected" error is attributed to the Host processor (in most cases is ADAU1452) failing to provide sync to the transceiver.

To resolve this issue, you can address it by selecting an appropriate configuration xml file for host processor by double clicking on the main node and then right click on ADAU1452 Generic Devices to open settings. In settings, option to add the path for Peripheral programming file can be seen. Select the appropriate configuration xml file from the path

::

      “C:\Analog Devices\ADI_A2B-SSPlus_Software-Relx.x.x\Schematics\PC\xml” 

and enable the **Program during discovery** option, as mentioned in the image below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/programduringdiscovery.png
   :align: center

**24. A2B stack and FreeRTOS, when used together, a conflict arises because both contains ‘queue.h’ files in them and build fails. What could be a solution to this?**

The file ‘queue.h’ is an open-source component (not authored by ADI) and we have it mentioned in the appendix of the license agreement. This is an integration issue at the user’s end since they are using FreeRTOS.

One solution is that, since the source code of A2B stack is available with the user and currently ‘queue.h’ is placed in the same folder along with source code, the user can place the header file in another folder and change the include directory.

**25. How to use the Sequence window in Sigma Studio Plus to obtain ‘.h’ file?**

**Step 1:** Open a Sigma StudioPlus project and you can find the Sequence window at the very bottom along with Output and Capture Window. If it is not visible, kindly Select the **Sequence window** from **View** option.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sequencewindow1.png
   :align: center

**Step 2:** In the Sequence window, you can find an option to **Open Sequence File**. A new window pops up where you must provide the path to the exported command list '.xml' file and select it.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sequencewindow2.png
   :align: center

**Step 3:** Once the xml file is loaded, please select the **Export** option in Sequence window. A new window pops up asking you the path to save the file in '.h' format.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sequencewindow3.png
   :align: center

**Step 4:** When you exported the files from Sequence window, you will get 3 files. One '.c' file and two '.h' file. In one of the files, you must be able to see all the register write related information.

**26. Can the A2B stack be used to frequently clear the BECNT? If yes, can the time between the clearings be set freely?**

| In the *a2bapp_onDiscoveryComplete()* function, we clear the **BECNT** register by invoking the callback function *a2b_app_handle_becovf()* after a 1000ms delay, as defined in the **A2B_APP_TMRTOHANDLE_BECOVF_AFTER_INTERVAL** macro. Additionally, to repetitively clear the **BECNT** register every 1000ms, you can configure the **A2B_APP_TMRTOHANDLE_BECOVF_REPEAT_INTERVAL** macro. You can change the time freely according to your preferences. Please ensure that the LineFaultDiagnostics settings are enabled to utilize this functionality effectively.
| **27. How do I install the A2B Plugin X.Y.Z for SigmaStudio+ on Windows 11, and what should I do if issues arise?**

To install the A2B Plugin X.Y.Z for SigmaStudio+, follow these steps:

**Install Prerequisites:**

-  `Microsoft SQL Server 2014 SP2 Feature Pack <https://www.microsoft.com/en-us/download/details.aspx?id=42295&msockid=1dca99ea8d9f62fb361e8c9c8cc16326>`__ (SQLSysClrTypes.msi) – Download and install the correct version (32-bit or 64-bit) from the Microsoft website.
-  `Microsoft Report Viewer 2015 Runtime <https://www.microsoft.com/en-us/download/details.aspx?id=45496>`__ (ReportViewer.msi) – Download and install the required package.
-  Restart your system after installing these prerequisites.
-  After installation, verify that Microsoft System CLR Types for SQL Server 2014 and Microsoft Report Viewer 2015 Runtime appear in the Control Panel → Programs and Features.\

|image10|

**Install A2B Plugin:**

-  Download the A2B Plugin X.Y.Z from the :adi:`A2B Software <en/resources/evaluation-hardware-and-software/software/a2b-software.html#software-overview>`.
-  Run the installer and follow the on-screen instructions.
-  Verify that the plugin appears within SigmaStudio+.

**Troubleshooting:**

-  If prerequisite installation fails, ensure you have administrator rights, Windows 11 is fully updated, and the correct system architecture version is selected.
-  If the A2B Plugin does not appear in SigmaStudio+ after installation, restart your system and run SigmaStudio+ as an administrator.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/downloadschmetic_1.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/downloadschmetic_2.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/click_thru_sla.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/clock_control_register_sc589_mini.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/r_value_1761_sc589_mini.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/target_comm_failed.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/basic_auth_failed.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/unknown_err.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/bandwidth_overshoot_error.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/sqlslrtypes_report_viewer.png
