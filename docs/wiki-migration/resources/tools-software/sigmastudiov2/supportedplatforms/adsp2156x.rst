| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/supportedplatforms>`
| =====ADSP-215xx=====
| This processor can be inserted on to the custom platform and configured as one of the supported SHARC processor with a single SHARC+ core.
| ==Configurable Targets==

-  ADSP-SC570
-  ADSP-SC572
-  ADSP-21560
-  ADSP-21561
-  ADSP-21562
-  ADSP-21563
-  ADSP-21565
-  ADSP-21566
-  ADSP-21567
-  ADSP-21568
-  ADSP-21569
-  ADSP-SC591
-  ADSP-SC592
-  ADSP-SC592W
-  ADSP-SC595
-  ADSP-SC595W
-  ADSP-SC596
-  ADSP-SC596W

| 
| ==Processor Settings==

-  **Build Mode (Release/Debug)** - This field is an input to the CCES compiler, indicating whether the code should be compiled in Debug or Release mode.
-  **Enable IPA** - Inter-procedural optimization can be enabled to reduce the MIPS consumption for a schematic. This will affect the time taken to compile and link the schematic.
-  **Input Buffers** - This field indicates the number of input buffers each of size “BlockSize” which the SigmaStudio+ Target Framework will use for input data buffering. By default, the number of Input buffers is set to 3. If a user enters a value which is more than the default value in SigmaStudio+ GUI, then the Audio control framework needs to be rebuilt.
-  **Output Buffers** - This field indicates the number of output buffers each of size “BlockSize” which the SigmaStudio+ Target Framework will use for output data buffering. By default, the number of Output buffers is set to 3. If a user enters a value which is more than the default value in SigmaStudio+ GUI, then the Audio control framework needs to be rebuilt
-  **CCES Version** - All the supported tool-chains which are installed on the PC are listed in this drop-down box. The user can select a tool-chain from this drop-down box for every Schematic. The latest installed version of CrossCore Embedded Studio is the default selection. The selected tool-chain is used by SigmaStudio+ to compile the Schematics and process the Plug-Ins.

| 
| ==Core Settings==

-  **Process Mode** - This field indicates as to how the signal block instances are connected and processed on the SHARC+ core. This field is not applicable in case of a dual-core schematic. The following Process Modes are supported:

   -  Single
   -  Serial
   -  Parallel

-  **Schematics** - Number of instances of schematic on the core
-  **Application DXE** - The Application DXE can be loaded to the core using this ‘Open’ button. SigmaStudio+ uses the Application DXE to read the Global Memory map (GMAP). GMAP contains information corresponding to available physical memory for the core (remaining unused memory on a per block basis after consumption by the application)
