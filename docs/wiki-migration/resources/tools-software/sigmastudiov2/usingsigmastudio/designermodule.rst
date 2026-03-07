:doc:`Return to parent page </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`

Algorithm Designer
==================

Algorithm Designer offers the flexibility to create a custom SigmaStudio+ block with runtime control over the parameters. SigmaStudio+ Algorithm Designer has two use cases:

-  Algorithm Designer can be used as Designer Control module which could be inserted in the schematic as a generic module. Designer Control can implement any algorithm and offer provision for run-time parameter tuning. Since edits can be made to the source code as well as parameters in the Designer Control and the schematic can be immediately compiled and executed, this is useful during the development phase of the module.
-  Algorithm Designer can generate a reusable SigmaStudio+ block in the form of a DLL from an Algorithm using CrossCore Embedded Studio tools. The resulting SigmaStudio+ Add-In library file (Plug-In) can be reused and redistributed just like built-in SigmaStudio+ Algorithms.

| This page describes the steps required to use Algorithm Designer as Designer Control module as well as steps required to generate a custom SigmaStudio+ Plug-In using CrossCore Embedded Studio tools and Algorithm Designer.
|

.. note::

   The initial version of the Algorithm Designer supports only ADSP-215xx/ADSP-SC5xx series of processors. From SigmaStudioPlus 2.1.0 version onwards, the Algorithm Designer supports ADSP-214xx processors also.


Implementing Custom Algorithm using Algorithm Designer Module
-------------------------------------------------------------

| 
| Algorithm Designer Module is a generic module which can be inserted in the schematic. Once inserted in the schematic, this module can be used to directly implement custom block processing algorithms without the need of generating a Plug-In. Run-time control of parameters are also supported on the Algorithm Designer Module.
| |image1|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module in SigmaStudioPlus for Griffin processors


| |image2|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module in SigmaStudioPlus for Legacy SHARC processors


| ====Insert Module and Launch Designer==== This module is listed under “Designer” category in the tool-box as shown in the above two images. This module is available only on the block processing schematic. When inserted in the schematic, the module will have no input-output pins. The Algorithm Designer window can be launched by double clicking on the Algorithm Designer module inserted in the schematic.
| ====Configure the module using Algorithm Designer==== Algorithm Designer will be used to configure the algorithm source code and parameters of the Algorithm Designer Module. Steps involved are:

-  Define Source
-  Define Parameters
-  Define Pins
-  Define Memory
-  Define Runtime Variables
-  Assign Parameters

| Refer to `designing_module <https://wiki.analog.com/designing_module>`_ for more details.
| ====Compile the Schematic with Designer Control==== Once the above steps are completed, the input-output pins on the Algorithm Designer module can be connected to the schematic. The Algorithm Designer window can be either left open or closed before compiling the schematic. Ensure to save the Designer project before closing the Algorithm Designer window. Link-Compile-Download the schematic. Please refer the :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>` below.
| |image3|

.. container:: centeralign

   \ **Figure:** Schematic with Designer Module's Link-Compile-Download option in UI


| ====Tune Custom Algorithm using Algorithm Designer==== **Tune Parameters**
| Module parameters can be modified by changing the runtime variables and runtime buffers. Since the module parameters are assigned with the runtime parameters, changing the runtime parameters changes the module parameters. Runtime variables can be modified using the numeric up-down control. Runtime buffers can be modified using the ‘Edit” button. After the table entries and edited, press ‘Update’ to send the updated parameters to the target. The above mentioned variable value changes can be done in :doc:`Variables section </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designing_module>`.
| **Modify Source Code**
| Changes to the module source code can be made in the source editor (:doc:`Source and Libraries section </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designing_module>`) within Algorithm Designer. Note that it is required to recompile the schematic once the source code has been modified.
| **Modify Memory Requirements**
| Note that it is required to recompile the schematic once the memory requirements have been modified in the Algorithm Designer's :doc:`Memory section </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designing_module>`.
| ====Finalize the Module==== Once the module is finalized, it can be built as a Plug-In and distributed. Click here for instructions to `generate_plug-in_assembly <https://wiki.analog.com/generate_plug-in_assembly>`_.
| =====Generate Algorithm Plugin (DLL) using Algorithm Designer=====

Launch Algorithm Designer
~~~~~~~~~~~~~~~~~~~~~~~~~

Algorithm Designer can be launched in 2 ways.

-  Using the algorithm Designer module as mentioned in the :doc:`previous </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>` section.
-  Algorithm Designer can be also launched by selecting **Tools**\ ➔ **Algorithm Designer** from the menu bar as shown in below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>`.

| 
| |image4|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Launcher


| ====Configure the module using Algorithm Designer==== Algorithm Designer will be used to configure the source, pins, parameters, memory and UI of the new module. Refer to `designing_module <https://wiki.analog.com/designing_module>`_ for more details.
| ====Generate Plug-In Assembly==== Click here for instructions to `generate_plug-in_assembly <https://wiki.analog.com/generate_plug-in_assembly>`_
| =====Coding Conventions===== Click here for `algorithm_designer_coding_conventions <https://wiki.analog.com/algorithm_designer_coding_conventions>`_
| =====Algorithm designer Plug-In examples=====

-  `DLB Method Example: Mute (No Slew) Module <https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/mutenoslew.zip>`_
-  `Source Code Method Example: Simple Adder Module <https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/simpleadder.zip>`_
-  `Mute (No Slew) Module with Designer Module in SigmaStudioPlus project <https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/mutenoslew_designermodule.zip>`_

| For more details regarding how these DLL based **DLB Method** Example & **Source Code Method** examples were created, please refer :doc:`DLL based Custom Module Creation </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`
| Kindly follow the sections mentioned below to understand the procedure used to create the Designer module-based **Mute (No Slew) Example**:
| :doc:`Implementing Custom Algorithm using Algorithm Designer Module </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>`
| :doc:`Insert Module and Launch Designer </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>`
| :doc:`Configure the module using Algorithm Designer </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>`
| :doc:`Compile the Schematic with Designer Control </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>`
| :doc:`Tune Custom Algorithm using Algorithm Designer </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/algorithmdesignmodule.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/algorithmdesignmodule_legacy.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/lcd_algorithmdesigner.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/tools_algorithmdesigner.jpg
