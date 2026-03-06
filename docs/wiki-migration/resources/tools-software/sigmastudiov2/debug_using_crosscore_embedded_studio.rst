:doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration>`

Debug Using CCES
================

Follow the instructions given below to set up the CCES for debugging the schematic.

-  Establish the hardware setup as described in :doc:`ADSP-215xx/ADSP-SC5xx Hardware Setup </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/adsp-215xx_and_adsp-sc5xx>`.
-  Install all software and tools mentioned in :doc:`PC Software Setup </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/swsetup>`.
-  The Default Application for ADSP-SC573, ADSP-SC584 and ADSP-SC589 are supplied with the package. The projects can be found inside “SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Demo”. Launch CrossCore Embedded Studio on the SigmaStudio Host PC. Specify the workspace when prompted. Select File->Import. Import SS_App_Core0, SS_App_Core1 and SS_App_Core2 projects of appropriate target into CrossCore Embedded Studio.
-  Select all the 3 core applications and build in Debug Mode.

|image1|

-  Uncheck “Build (if required) before launching” checkbox in Window->Preferences->Run/Debug->Launching.
-  Launch SigmaStudio.
-  Open any desired schematic that is required to be debugged.
-  Make sure that the custom module going to be debugged was created with library file built in debug configuration.
-  Select the rebuilt Application DXE’s for both the SHARC’s by clicking on ‘Select Application DXE’ in SHARC0/SHARC1 tab of SigmaStudio IC control window.
-  Press Link-Compile-Download. This is a dummy download of the schematic for generating the schematic DXEs.
-  Open the IC 1\_<Schematic Name> and IC 2\_<Schematic Name> folders to find the IC_1_Diff.dxe and IC_2_Diff.dxe files. The symbols present in these DXEs are loaded on top of the target application DXEs as explained in further steps.
-  Select Run->Debug Configurations in CCES. Create a new Debug configuration under ‘Application with CrossCore Debugger’. Select appropriate processor, connection type and platform. Click finish.
-  Load the DXE’s ‘SS_App_Core0’ on Core 0, ‘SS_App_Core1.dxe’ on Core 1 and ‘SS_App_Core2.dxe’ on Core 2. Now select the ‘SS_App_Core1.dxe’ in Core 1, press ‘Add’ and select the schematic DXE corresponding to Core 1 ( IC_1_Diff.dxe), select SS_App_Core2.dxe’ in Core 2, press ‘Add’ and select the schematic DXE corresponding to Core 2 ( IC_2_Diff.dxe) as shown in below figure.

|image2|

-  Double click on ‘SS_App_Core1.dxe’ of Core 1 and uncheck ‘Run immediately after load’ option. Repeat the same for ‘SS_App_Core2.dxe’ for Core 2.

|image3|

-  Double click on ‘IC_1_Diff.dxe’ of Core 1 and uncheck everything except ‘Load Symbols only’ after load’ option. Repeat the same for ‘IC_2_Diff.dxe’ for Core 2.

|image4|

-  Click on “MP Resume” to run Core 0 (ARM). This enables the Core 1 and 2 (SHARC).
-  Select main () function in Debugger window of corresponding SHARC core, the SigmaStudio schematic module to be debugged.

|image5|

-  Enter “adi_ss_schematic_process.” symbol name in the Disassembly window and press enter to get Disassembly function.

|image6|

-  Scroll down in the Disassembly function and set breakpoint in the instruction shown in below figure. There will be a pop up when breakpoint set, just select “Don’t show me again” and press “OK”.

|image7|

-  The steps 17 to 19 needs to be followed for SHARC core2 if any module to be debugged on SHARC core2.
-  Then individually select and run Core 1 and Core 2 by clicking on “Resume”.
-  Link-Compile-Download the required schematic again in SigmaStudio.
-  A pop-up appears in CCES prompting the user to re-load the schematic DXEs. Select No.

|image8|

-  Observe that the target halts at the breakpoint set as shown in below figure.

|image9|

-  Select “Mask interrupts during step” in target option and press “OK” as shown in below figure.

|image10|

-  Step-in 2 times using disassembly step in to enter “SSSharcSSn.” disassembly function.

|image11|

-  The source files (.c) of custom module can be dragged to CCES source window and set breakpoint on the source file module functions directly. Step-in through the code using debugger window Step In options and debug the module function.
-  The other way is, enter the required symbol name of module function (byte addressed symbol followed by a ‘.’) which is to be debugged in the Disassembly window and set a breakpoint at the required instruction. For example debugging Biquad Cascade module enter “BPROCESS_BiquadCascade.” symbol and set a breakpoint as shown in below figure. Run the core by clicking on “Resume”. The core halts at module function where the breakpoint is set.

|image12|

-  Step-in through the code using disassembly step and debug the module function.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_1.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_2.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_3.jpg.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_4.jpg
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_5.jpg.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_6.jpg.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_7.jpg.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_8.jpg
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_9.jpg.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_10.jpg.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_11.jpg.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/debug_12.jpg.png
   :width: 600px
