:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`

Compile, Download and Tune
==========================

| 
| Before a complete design can be evaluated, it must be linked, compiled, and downloaded to the hardware. Once the design is downloaded to the target and is executing, it can be further tuned or controlled from SigmaStudio+. SigmaStudio+ allows the user to perform the following actions:

-  **Link**
-  **Link + Compile**
-  **Link + Compile + Download**
-  **Clean + Link + Compile + Download**
-  **Link + Compile + Connect**

| 
| ===== Link ===== The link operation analyzes the signal flow (blocks and wires), checks for any in design errors, generates the program flow, and sets algorithm sampling rates and DSP associations. To link a project, press the ‘\ **Link**\ ’ button in the toolbar, select ‘\ **Action -> Link**\ ’ from the menu bar, or press **Ctrl+Shift+F7**.
| Any errors encountered during the link operation are shown in the Output window. You cannot compile a project until all link errors are resolved. Note that all block's input pins must be connected, or you will receive link errors. If linking is successful, '**LINKED**' is displayed in the application status bar.
| ===== Compile ===== Following the link step, compilation is performed. Compile generates the DSP program code and parameter data from the graphical schematic design. To compile a project, press the '**Link Compile**' toolbar button, select ‘\ **Action -> Link Compile**\ ’ from the menu bar, or press **Shift+F7**. This will first perform the link step and then compile the project.
| The output window will display link and compile errors, if any. If compilation is successful, '**COMPILED**' is displayed in the application status bar.
| ===== Download ===== Once a project is compiled, the program, parameter data and control information can be downloaded to the evaluation hardware for testing. To download your project, press the '**Link Compile Download**' toolbar button, select '**Action -> Link Compile Download**' from the main menu, or press **F7**. This performs the linking, compile the project, and send your design code from the schematic to the DSP hardware.
| If download is successful, '**ACTIVE**' is displayed in the application status bar. The system will be responsive to any real-time changes made to controls (sliders, knobs, etc.) in the schematic workspace.
| ===== Connect ===== Once a project is compiled, SigmaStudio+ can connect to the hardware for real-time changes by using the Connect feature. To connect to the hardware to tune or control the hardware using SigmaStudio, select '**Action -> Link Compile Connect**' from the main menu, or press **Alt+Shift+F7**. This performs the linking, compile the project, and connects to the DSP hardware for real-time tuning or control. This operation is exactly like link + compile + download, except it does not download the newly compiled program. This operation assumes that the downloaded program on the target exactly matches the schematic seen in the host, and no validation between the host and the target program is performed.
| If connect is successful, '**ACTIVE**' is displayed in the application status bar. The system will be responsive to any real-time changes made to controls (sliders, knobs, etc.) in the schematic workspace.
| ===== Clean (Link-Compile-Download) ===== This operation like Link-Compile-Download, except the fact that this action triggers a full rebuilt of the source files as part of the compile operation. All temporary files from the earlier compile operation will be removed and the entire portion will be recompiled even if there are no changes. This action is available only on selected DSPs. To perform clean link-compile-download of your project, press the '**Clean Link Compile Download**' toolbar button, select '**Action -> Clean Link Compile Download**' from the main menu, or press **F8**.

--------------

Application States
------------------

| 
| \* **DESIGN** - indicates that the schematic design has been modified and recompile is required to validate the current design.

-  **LINKED** - indicates that the schematic is linked.
-  **COMPILED** - indicates that the schematic is compiled.
-  **ACTIVE** - indicates that the schematic is linked and compiled. The state is the outcome of a successful “Link-Compile-Connect” or “Link-Compile-Download” operation. The system responds to the user's tuning input in this mode by giving appropriate output. The actual value of the output along with other packet details can be observed from Capture Window.
-  **PROCESSING** - indicates that the project is currently getting processed (linking or compilation is in-progress).
-  **ERROR** - indicates that the schematic linking, or compilation failed and that the program data was not downloaded on to the hardware. The error correction or necessary steps must be taken to ensure smooth compilation in the subsequent steps.

.. tip::

   Note: When working with evaluation hardware, any time you make edits in the schematic (e.g. add/remove blocks, add/remove wires, add/remove algorithms) you must recompile and download the project before these changes will take effect in the hardware program. If the application status bar does not indicate “ACTIVE”, the downloaded program and schematic design are out of sync

