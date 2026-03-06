:doc:`Click here to return to 'SigmaStudio for SHARC - Quick start guide' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide>`

Debugging Schematics using CCES
===============================

This section explains how to debug a schematic using CrossCore Embedded Studio.

Steps to be followed to Debug a function in the schematic
---------------------------------------------------------

| Follow the instructions given below to set up the CCES for debugging the schematic.
| \* Establish the hardware setup as described in Section 3.1.

-  Install all software and tools mentioned in Section 2.
-  The Default Application for ADSP-SC573, ADSP-SC584 and ADSP-SC589 are supplied with the package. The projects can be found inside “< Software Modules folder > \\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\Demo\\”. Launch CrossCore Embedded Studio on the SigmaStudio Host PC. Specify the workspace when prompted. Select FileImport. Import SS_App_Core0, SS_App_Core1 and SS_App_Core2 projects of appropriate target into CrossCore Embedded Studio.
-  Select all the 3 core applications and build in Debug Mode.\

|image1|

-  Uncheck “Build (if required) before launching” checkbox in Window->Preferences->Run/Debug->Launching.
-  Launch SigmaStudio.
-  Open any desired schematic that is required to be debugged.
-  Select the rebuilt Application DXE’s for both the SHARC’s by clicking on ‘Select Application DXE’ in SHARC0/SHARC1 tab of SigmaStudio IC control window.
-  Press Link-Compile-Download. This is a dummy download of the schematic for generating the schematic DXEs.
-  Open the IC 1\_<Schematic Name> and IC 2\_<Schematic Name> folders to find the IC_1_Diff.dxe and IC_2_Diff.dxe files. The symbols present in these DXEs are loaded on top of the target application DXEs as explained in further steps.
-  Select RunDebug Configurations in CCES. Create a new Debug configuration under ‘Application with CrossCore Debugger’. Select appropriate processor, connection type and platform. Click finish.
-  Load the DXE’s ‘SS_App_Core0’ on Core 0, ‘SS_App_Core1.dxe’ on Core 1 and ‘SS_App_Core2.dxe’ on Core 2. Now select the ‘SS_App_Core1.dxe’ in Core 1, press ‘Add’ and select the schematic DXE corresponding to Core 1 ( IC_1_Diff.dxe), select SS_App_Core2.dxe’ in Core 2, press ‘Add’ and select the schematic DXE corresponding to Core 2 ( IC_2_Diff.dxe) as shown in Figure 5.\

|image2|

-  Double click on ‘SS_App_Core1.dxe’ of Core 1 and uncheck ‘Run immediately after load’ option as shown in the Figure 6. Repeat the same for ‘SS_App_Core2.dxe’ for Core 2.\

|image3|

-  Double click on ‘IC_1_Diff.dxe’ of Core 1 and uncheck everything except ‘Load Symbols only’ after load’ option as shown in the Figure 6. Repeat the same for ‘IC_2_Diff.dxe’ for Core 2.\

|image4|

-  Link-Compile-Download the required schematic again in SigmaStudio.
-  A pop-up appears in CCES prompting the user to re-load the schematic DXEs. Select No.\

|image5|

-  Halt the target using MP Halt. Enter the required symbol name (byte addressed symbol followed by a ‘.’) which is to be debugged in the Disassembly window and put a breakpoint at the required instruction.\

|image6|

-  Press ‘MP Resume’ button and observe that the target halts at this breakpoint.\

|image7|

Step-in through the code and Debug the function.

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_9.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_10.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_11.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_12.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_13.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_14.jpg
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_15.jpg
