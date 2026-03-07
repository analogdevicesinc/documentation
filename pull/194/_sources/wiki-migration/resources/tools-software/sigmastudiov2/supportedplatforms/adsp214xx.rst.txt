| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/supportedplatforms>`
| =====ADSP-214xx=====
| This processor can be inserted on to the custom platform as ADSP-214xx target processor. This is configured by default as ADSP-21489.

Processor Settings
==================

-  **Build Mode (Release/Debug)** - This field is an input to the CCES compiler, indicating whether the code should be compiled in Debug or Release mode.
-  **Enable IPA** - Inter-procedural optimization can be enabled to reduce the MIPS consumption for a schematic. This will affect the time taken to compile and link the schematic.
-  **I/O Channels** - This field indicates whether the input and output audio buffers passed to the SigmaStudio+ process module on the Target are in Block or Interleaved format. ‘Block’ indicates that each channel is placed as a block in the input/output buffer. ‘Interleaved’ indicates that the samples of each channel are interleaved. The Default Application uses ‘Block’ audio samples.
-  **Target Data Reception** - This field configures the Target to receive the data sent through SPI as words or as a Block. ‘Block’ indicates that the code and parameters are received by the DMA as a block of data and ‘Word’ indicates that the Target receives and processes the SPI data as individual words. The default settings use ‘Word’ Data Reception.
-  **VISA Mode** - When this field is enabled, SigmaStudio+ generates short word codes (VISA). The Application must be compiled with VISA enabled mode, to use the enable option for VISA. Prebuilt application provided in the package is with VISA mode enabled.
-  **Audio Mode** - Input/Output mode of the application.
-  **CCES Version** - All the supported tool-chains which are installed on the PC are listed in this drop-down box. The user can select a tool-chain from this drop-down box for every Schematic. The latest installed version of CrossCore Embedded Studio is the default selection. The selected tool-chain is used by SigmaStudio+ to compile the Schematics and process the Plug-Ins.

| 
| ==Core Settings==

-  **Application DXE** - The Application DXE can be loaded to the core using this ‘Open’ button. SigmaStudio+ uses the Application DXE to read the Global Memory map (GMAP). GMAP contains information corresponding to available physical memory for the core (remaining unused memory on a per block basis after consumption by the application)
