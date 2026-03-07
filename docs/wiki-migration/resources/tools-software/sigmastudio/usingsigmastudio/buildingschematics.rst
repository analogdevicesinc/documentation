Building Schematics
===================

| :doc:`Click here to return to the Using Sigma Studio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| This section present the fundamental concepts of the SigmaStudio System. For a brief overview of creating a SigmaStudio project, refer to the `Quick Start <https://wiki.analog.com/resources/tools-software/sigmastudio/gettingstarted/quickstart>`_. You can also find more information in the :doc:`tutorials </wiki-migration/resources/tools-software/sigmastudio/tutorials>` section.

-  :doc:`Schematic Blocks </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schematicblocks>`
-  :doc:`Algorithms: Add/Remove, Grow/Reduce </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/algorithms>`
-  :doc:`Wires and Aliases </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/wiresandaliases>`

--------------

Following are the steps required to create a new SigmaStudio schematic:

**Step 1: Create a New Project File** SigmaStudio starts with no project files loaded. To create a new project, select **File - New Project** from the application's main menu or click the New Project button on the application toolbar. A new project is created, with the default project name "Design 1". New projects are blank and the Hardware Configuration tab is displayed.

**Step 2: Choose a Processor (ICs/DSPs)**

-  Processors (ICs and DSPs) are managed in the :doc:`Hardware Configuration tab </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/hardwareconfigurationtab>`.

Before you can begin a system design, you must select at least one IC block in the Toolbox's **Processors (ICs/DSPs)** category and drag and drop it into the Hardware Configuration tab. The available algorithm blocks differ for each SigmaDSP product, so it is important to select the DSP IC that you intend to use in your final design from the beginning. Note that It is possible to create designs with more than one processor.

To communicate with evaluation hardware, you must also insert a USB block from the Toolbox's **Communication Channels** category into the Hardware Configuration tab and connect it to the processor block. Refer to the :doc:`USB Communication Channels </wiki-migration/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces/usbserialconverter>` section for more information.

**Step 3: Inputs and Sources**

-  Inputs and Sources are located in the Schematic tab

Once a Processor block is added to the project, the Schematic tab is displayed. Select the schematic tab and add Inputs or Sources by dragging and dropping blocks from the Toolbox's IO and Sources categories.

.. hint::

   Note: Every schematic MUST contain either an :doc:`Input block </wiki-migration/resources/tools-software/sigmastudio/toolbox/io>` or a :doc:`Source block </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`. If no inputs are present in the schematic design, you will receive the compiler error: <blockquote>Error - No Inputs are Defined for IC. </blockquote>


| **Step 4: Create a Signal Processing Design**
| Algorithm/Function blocks are managed in the :doc:`Schematic tab </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/schematictab>`

Drag and drop blocks from the ToolBox or Tree ToolBox pane into the schematic tab to create your design. Note that in additional to advanced signal processing blocks, there are a variety or low level building blocks available (delay, multiply, and addition, feedback) allowing you to implement custom algorithms to fulfill your specific design requirements.

**Step 5: Outputs** To output processed signals from the SigmaDSP hardware, you will need to insert an :doc:`Output block </wiki-migration/resources/tools-software/sigmastudio/toolbox/io>` into the schematic design. Drag and drop output blocks from the ToolBox or Tree ToolBox pane into the schematic tab. The output blocks represent the hardware's physical analog and digital output pins.

**Step 6: Wire Inputs to Outputs** Each schematic block has input and output pins which can be :doc:`wired </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/wiresandaliases>` together to create the system's signal flow. All block's input pins must be connected to a source or another block's output pin and all block's output pins must be connected or :doc:`terminated </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/schematicterminal>`.

.. hint::

   Note: If there are unconnected pins in the schematic you will receive the compiler error: <blockquote>Fatal Error: Unconnected pins found in cell. </blockquote>


| **Step 7: Link and Compile the Project**
| Once the schematic is complete and all blocks are correctly wired together, you can :doc:`link and compile </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/linkcompiledownload>` the project. If any errors are encountered during compilation, the Link Window will open and display the error information. If compilation is successful you will see a green bar directly below the schematic tab window and **Ready - Download** is displayed in the application's status bar.

| **Step 8: Adjust Controls in Real-time**
| Once your schematic is compiled and downloaded to the hardware, you can adjust the schematic's controls (knobs, sliders, and spin boxes) to change algorithm parameters in real time. This allows you to tune your design's settings before implementing the final system.

Some controls adjust compile-time parameters. Changes to these controls will not update the connected SigmaDSP instantly. If a compile-time control is changed, text in the bottom right corner of the SigmaStudio window will change from "Active: Downloaded" to "Design Mode", indicating SigmaStudio has stopped synchronizing the schematic with the DSP. To implement changes to compile-time parameters, recompile and download the program to the DSP, at which time the "Design Mode" text will change back to "Active: Downloaded".

See :doc:`System Implementation </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/systemimplementation>` for more information about how to integrate a schematic design into your end system.
