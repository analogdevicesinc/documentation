| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/supportedplatforms>`
| =====ADSP-SC5xx=====

| 
| This processor can be inserted on to the custom platform and configured as one of the supported SHARC processor with two SHARC+ core.
| ==Configurable Targets==

-  ADSP-21571
-  ADSP-21573
-  ADSP-SC571
-  ADSP-SC573
-  ADSP-21583
-  ADSP-21584
-  ADSP-21587
-  ADSP-SC582
-  ADSP-SC583
-  ADSP-SC584
-  ADSP-SC587
-  ADSP-SC589
-  ADSP-21593
-  ADSP-21594
-  ADSP-SC594
-  ADSP-SC598

| 
| ==Processor Settings==

-  **Build Mode (Release/Debug)** - This field is an input to the CCES compiler, indicating whether the code should be compiled in Debug or Release mode.
-  **Enable IPA** - Inter-procedural optimization can be enabled to reduce the MIPS consumption for a schematic. This will affect the time taken to compile and link the schematic.
-  **Input Buffers** - This field indicates the number of input buffers each of size “BlockSize” which the SigmaStudio+ Target Framework will use for input data buffering. By default, the number of Input buffers is set to 3. If a user enters a value which is more than the default value in SigmaStudio+ GUI, then the Audio control framework needs to be rebuilt.
-  **Output Buffers** - This field indicates the number of output buffers each of size “BlockSize” which the SigmaStudio+ Target Framework will use for output data buffering. By default, the number of Output buffers is set to 3. If a user enters a value which is more than the default value in SigmaStudio+ GUI, then the Audio control framework needs to be rebuilt
-  **CCES Version** - All the supported tool-chains which are installed on the PC are listed in this drop-down box. The user can select a tool-chain from this drop-down box for every Schematic. The latest installed version of CrossCore Embedded Studio is the default selection. The selected tool-chain is used by SigmaStudio+ to compile the Schematics and process the Plug-Ins.
-  **Schematic Mode (Single Core/Dual Core)** - This field indicates whether the schematic is required to have a single signal chain for both the SHARC cores (Dual Core Mode) or the schematic is required to have two independent signal chains for each of the SHARC cores (Single Core Mode).

| 
| ==Core Settings==

-  **Process Mode** - This field indicates as to how the signal block instances are connected and processed on the SHARC+ core. This field is not applicable in case of a dual-core schematic. The following Process Modes are supported:

   -  Single
   -  Serial
   -  Parallel

-  **Schematics** - Number of instances of schematic on the core
-  **Application DXE** - The Application DXE can be loaded to the core using this ‘Open’ button. SigmaStudio+ uses the Application DXE to read the Global Memory map (GMAP). GMAP contains information corresponding to available physical memory for the core (remaining unused memory on a per block basis after consumption by the application)
