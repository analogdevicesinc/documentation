| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication>`
| =====Microcontroller Mode Support===== In microcontroller mode, the Target Framework shall process the incoming audio data based on the exported set of code and parameters from SigmaStudio+. The ARM core of ADSP-SC5xx processor acts as a microcontroller, downloading the SMAP, SS+ code and parameters on to the SHARC cores of ADSP-SC5xx. Example micro controller mode applications are available in "C:\\Analog Devices\\SigmaStudioPlus-Relx.y.z\\Target\\Examples\\DemoUc" folder.
| A utility is provided with the package using which the code and parameters exported by SigmaStudio+ can be converted into a ‘C’ source files. This utility creates arrays of SMAP, SS+ code and parameters as part of a ‘C’ file which can be directly included in the SigmaStudio+ ARM application for ADSP-SC5xx. The export param utility is available in "C:\\Analog Devices\\SigmaStudioPlus-Relx.y.z\\Target\\Utilities\\ExportCodeParam" folder.

Please find the steps to export the schematic source files to use with micro controller application:

-  Open SigmaStudio+, design the schematic application and compile the schematic.
-  Upon successful compilation of schematic use "Export System Files" option to generate schematic export files.

|image1|

   \* Copy the "ExportCodeParam.exe" utility available in installation package to the folder where the schematic export files are generated.
-  Open Windows Command Prompt and change the working directory to this folder.
-  Run the utility as below:

| ExportCodeParam.exe <SWC/NWC> <ExportName> <SchematicName> <ProcessorFamily>
| example:
| //ExportCodeParam.exe "SWC" "Example" "DiffDXESchematic_1" “SC5xx” *
  or
  *\ ExportCodeParam.exe "SWC" "Example" "DiffDXESchematic_1" “215xx” //

  | This generates C source file and header file in the same folder. This utility must be run multiple times corresponding to the number of schematics within the core. Use the generated schematic source files to micro controller mode application and rebuild the application.
|

.. note::

   The schematic source files should be regenerated when there is change in target application and/or SigmaStudio+ schematic.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/export_system_files.png
   :width: 400px
