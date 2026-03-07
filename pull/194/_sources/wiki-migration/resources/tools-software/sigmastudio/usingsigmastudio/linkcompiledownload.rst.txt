Link/Compile/Download
=====================

| :doc:`Click here to return to the Using Sigma Studio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| Before a complete design can be evaluated, it must be linked, compiled, and downloaded to the hardware. To perform all these steps in a single operation, use the Link Compile Download command described below.

--------------

| Link:
| |linkcompilepic1.png|
| The link operation analyzes the schematic's signal flow (blocks and wires), checks for any in design errors, generates the program flow, and sets algorithm sampling rates and DSP associations. To link a project, press the **Link Project** toolbar button, select **Action - Link Project** from the main menu, or press **Ctrl+I**.

| When linking is complete, the Link Window opens, displaying the project's algorithm and node list information.
| |linkcompilepic2.png|

| Any errors encountered during the link operation are shown in the **Errors / Output** section of the Link Window. You cannot compile a project until all link errors are resolved. Note that all schematic block's pins must be connected or terminated or you will receive link errors.
| |linkcompilepic3.png|
| The linker generates a net list file, **net_list.cir2**, which contains the same information displayed in the Link Window's Node List pane.

--------------

| **Compile:**
| |linkcompilepic4.png|
| Following the link step, compilation is performed. Compile generates the DSP program code and parameter data from the graphical schematic design. To compile a project, press the **Link Compile Connect** toolbar button. This will first perform the link step and then compile the project. The link window will be displayed if there are link errors.

If compilation is successful, the schematic status bar turns green and **"100% Ready: Compiled"** is displayed in the application status bar.

Upon project compilation, several files are generated:

-  **hex_program_data.dat** - load file for downloading code using microcontroller in hex format
-  **program_data.dat** - load file for downloading code using ADI loader
-  **hex_program_simdata.dat** - load file for downloading code using microcontroller, with no commas, X'es, or spaces; this is a useful format for Verilog simulations
-  **spi_map.dat** - parameter RAM locations for each schematic instance
-  **compiler_output.txt** - SigmaStudio compiler output file
-  **trap.dat** - lists the values to enter in the trap registers to output a signal to the data-capture output pin.

These files are written into the project file's directory (\*.dspproj), or the active directory if the project has not been saved. The files are placed in an automatically generated sub-folder or folders named with the IC name followed by the project file name, for example **IC 1_Design 1**.

Awareness of these files, both their format and their contents, will prove useful. Also, it is helpful to archive and version these files during system design. SigmaStudio can minimize development time by avoiding the need to program in assembly code. Typically once the graphical SigmaStudio design is complete, these generated SigmaDSP code files must be integrated with an external microcontroller. See :doc:`System Implementation </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/systemimplementation>` for more information.

--------------

| **Download:**
| |linkcompilepic5.png|

Once a project is compiled, the program and parameter data can be downloaded to the evaluation hardware for testing. To download your project, press the **Link Compile Download** toolbar button, select **Action - Link Compile Download** from the main menu, or press **F7**. This perform the link step, compile the project, and send your design code from the schematic to the DSP hardware.

If download is successful, the schematic status bar below the workspace will turn green and **"100% Active: Downloaded"** is displayed in the application status bar. The system will be responsive to any real-time changes made to controls (sliders, knobs, etc.) in the schematic workspace.

--------------

**Schematic Status Bar:**

| The schematic status bar and application status bars display the state of the schematic design as well as indicating USB communication status. There are five status states:
| |linkcompilepic6.png|

.. tip::

   Note: When working with evaluation hardware, any time you make edits in the schematic (e.g. add/remove blocks, add/remove wires, add/remove algorithms) you must recompile and download the project before these changes will take effect in the hardware program. If the application status bar does not indicate "Active Downloaded", the downloaded program and schematic design are out of sync.


Download Options (ADAU145x)
---------------------------

Link Compile Download will download Regsiters, Program and Data from the schematic.

Register Download
~~~~~~~~~~~~~~~~~

Download of registers can be disabled upon download in the IC Context menu as shown below.


|image1|

PLL Reset
~~~~~~~~~

Sometimes user does not want the ADAU145x clock to be reset during download. This can be disabled through the IC Context menu as shown below. After disabling download will not reset the PLL.


|image2|

.. |linkcompilepic1.png| image:: https://wiki.analog.com/_media/linkcompilepic1.png
.. |linkcompilepic2.png| image:: https://wiki.analog.com/_media/linkcompilepic2.png
.. |linkcompilepic3.png| image:: https://wiki.analog.com/_media/linkcompilepic3.png
.. |linkcompilepic4.png| image:: https://wiki.analog.com/_media/linkcompilepic4.png
.. |linkcompilepic5.png| image:: https://wiki.analog.com/_media/linkcompilepic5.png
.. |linkcompilepic6.png| image:: https://wiki.analog.com/_media/linkcompilepic6.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/regdownload.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/regdownloadd.jpg
