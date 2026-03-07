:doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>`

Coding Conventions
==================

| 
| SigmaStudio modules can be of two types: Modules supporting sample/stream processing and Modules supporting block processing. Algorithm Designer can generate both sample processing and block processing Plug-Ins, whereas Designer Control can be used only on block processing schematics and thus supports only block processing. Algorithm source used for implementing a Module using Algorithm Designer or for generating SigmaStudio Plug-Ins (\*.dll) has to be either DLBs generated using CrossCore Embedded Studio or C source code directly entered in the source editor of Algorithm Designer or a combination of both DLB and source code. Direct insertion of C source code in the Algorithm Designer source editor is supported only for block processing Modules. This section gives the general rules, guidelines and conventions to be followed while implementing modules compatible with the Algorithm Designer.
| ====Include File==== Include file ‘adi_ss_extmod.h’ should be included by the source files.
| ====Function Prototype====

Sample Processing
-----------------

The entry-point function must have a prefix ‘PROCESS\_’ to indicate that it is a sample processing Plug-In function for SigmaStudio. Sub-functions in the source file which are referenced only from the main Plug-In function or other sub-functions need not follow any convention. The general prototype of any Plug-In entry-point function performing sample processing is shown below.

::

   void PROCESS_<algorithm_name> (float pInput[], float pOutput[], float pState[], float pParameter[], int nRepCount) 

Assembly entry-point function names must have the ‘PROCESS’ prefix. The general template of any Plug-In sample processing assembly function should be as shown below. It is compulsory to end the function with ‘PROCESS\_<algorithm_name>..end’ in case of byte addressed Plug-Ins and ‘\_PROCESS\_<algorithm_name>.end’ in case of word addressed Plug-Ins.

::

   .section/pm seg_swco;
   .global PROCESS_<algorithm_name>.;
    
   PROCESS_<algorithm_name>.:
   modify(i7,0xfffffffc); /* offset depends on the required frame space */

   /* custom code */

   i12 = dm(0xffffffff,i6);
   jump (m9,i12)(db);
   rframe;
   nop;
   PROCESS_<algorithm_name>..end:

When word addressed mode is used, the template is as shown below.

::

   .section/pm seg_swco;
   .global _PROCESS_<algorithm_name>;
    
   _PROCESS_<algorithm_name>:
   modify(i7,0xfffffffc); /* offset depends on the required frame space */

   /* custom code */

   i12 = dm(0xffffffff,i6);
   jump (m9,i12)(db);
   rframe;
   nop;
   _PROCESS_<algorithm_name>.end:

General rules to be followed are:

-  Inputs samples, output samples, state buffer and parameter buffer should be accessed only through the pointers in the function arguments.
-  If there are multiple input or output channels for the Module, samples corresponding to these channels are interleaved within the input/output buffer.
-  The parameter/state buffer pointer is of type float. This pointer should be type casted to an integer pointer for accessing integer parameters/state variables.
-  The argument ‘nRepCount’ represents the growth count. Growth count is a common terminology used in SigmaStudio and each Module has a different interpretation of growth count. For example, in General Second Order Filter, the growth count represents the number of cascaded biquad filters, whereas in Mute Algorithm the growth count represents number of channels.

| 
| ===Block Processing=== The entry-point function must have a prefix ‘BPROCESS\_’ to indicate that it is a block processing Plug-In function for SigmaStudio. Sub-functions in the source file which are referenced only from the main Plug-In function or other sub-functions need not follow any convention. The general prototype of a block processing Plug-In entry-point function is as shown below.

::

   void BPROCESS_<algorithm_name> (SSBlockAlgo* pBlockAlgo)

Assembly entry-point function names must have the prefix ‘BPROCESS\_’. The general template of any Plug-In block processing assembly function should be as shown below. It is compulsory to end the function with ‘BPROCESS\_<algorithm_name>..end’ in case of byte addressed Plug-Ins and ‘\_BPROCESS\_<algorithm_name>.end’ in case of word addressed Plug-Ins.

::

   .section/pm seg_swco;
   .global BPROCESS_<algorithm_name>.;
    
   BPROCESS_<algorithm_name>.:
   modify(i7,0xfffffffc); /* offset depends on the required frame space */

   /* custom code */

   i12 = dm(0xffffffff,i6);
   jump (m9,i12)(db);
   rframe;
   nop;
   BPROCESS_<algorithm_name>..end:

Same function when implemented in word addressed mode must follow the below template.

::

   .section/pm seg_pmco;
   .global _BPROCESS_<algorithm_name>;
    
   _BPROCESS_<algorithm_name>:
   modify(i7,0xfffffffc); /* offset depends on the required frame space */

   /* custom code */

   i12 = dm(0xffffffff,i6);
   jump (m9,i12)(db);
   rframe;
   nop;
   _BPROCESS_<algorithm_name>.end:

In addition to the process function, block Algorithms can also have an initialization function. Initialization functions are used to initialize the Module in case of decoders and 3rd party post processing Modules. The function name must have the prefix ‘INIT\_’ to indicate that it is the initialization function of the Module. The general prototype of a block processing Plug-In initialization function is as shown below.

::

   void INIT_<algorithm_name> (SSBlockAlgo* pBlockAlgo)

| If a Module must process a specific number of samples that is different to what SigmaStudio passes in, then BPROCESS wrapper function should deal with it by internal buffering.
| ====Interface Structures====

SSBlockAlgo
-----------

::

   typedef struct _SSBlockAlgo
   {
       int32_t     nInputs;
       int32_t     nOutputs;
       Block      *pInputs;
       Block      *pOutputs;    
       int32_t     nGrowth;
       int32_t     nGrowthB;    
       void       *pParam;
       float32_t  *pState;
       float32_t  *pScratchDM;
       float32_t  *pScratchPM;
       float32_t  *pStateB;
       float32_t  *pStateC;
       float32_t  *pExtPreState;
       int32_t    *pExtSymbols;
           
   }SSBlockAlgo;

| 
| **Description**
| The structure SSBlockAlgo is used to pass Module properties as arguments to a block processing Plug-In.
| **Fields**

-  nInputs - Number of input pins/channels.
-  nOutputs - Number of output pins/channels.
-  pInputs - Pointer to the array of input block structure.
-  pOutputs - Pointer to the array of output block structure.
-  nGrowth - Growth count of the Module.
-  nGrowthB - Output growth count of the Module when 2D growth is enabled.
-  pParam - Pointer to the parameter memory to be used by the Module.
-  pState - Pointer to the primary state memory to be used by the Module.
-  pScratchDM - Pointer to the scratch memory in DM block to be used by the Module.
-  pScratchPM - Pointer to the scratch memory in PM block to be used by the Module.
-  pStateB - Pointer to the second state memory to be used by the Module.
-  pStateC - Pointer to the third state memory to be used by the Module.
-  pExtPreState - Pointer to the extended precision state memory to be used by the Module.
-  pExtSymbols - Not used.

| 
| ===Block===

::

   typedef struct _Block
   {
       BlockProperties *pBlockProperties;
       float           *pSamples;       
       
   } Block;
   \\

| **Description**
| The structure Block is used to define the properties of each input/output channel.
| **Fields**

-  pBlockProperties - Pointer to the block properties structure which defines the properties of the block input/output channel.
-  pSamples - Pointer to the block of samples.

| 
| ===BlockProperties===

::

   typedef struct _BlockProperties
   {
       int32_t     nSamplingRate;  
       int32_t     nBlockSize;     
       int32_t     nReserve0;      
       int32_t     nReserve1;      
       
   } BlockProperties;

| 
| **Description**
| The structure BlockProperties is used to define the properties of each memory block.
| **Fields**

-  nSamplingRate - Sampling rate of the input channel expressed in Hz.
-  nBlockSize - Module Block Size in number of samples.
-  nReserve0 - Reserved. Not supported in this version.
-  nReserve1 - Reserved. Not supported in this version.

| 
| ====Memory Types==== Four different types of data memory are used in the externally coded Algorithm. They are explained below.
| ===Parameters=== Parameters are data generated based on the control data received from the Cell. Runtime Tuning is achieved by modifying the parameter data. Parameters are stored in the parameter buffer and memory is allocated per instance of the Module. Memory for storing parameters in the parameter buffer is allocated by SigmaStudio and the pointer to the memory is passed as an argument to the Plug-In function.
| ===State=== State memory is used to store the internal state of the Algorithm. Every instance of the function/Algorithm has dedicated state memory. This memory is allocated by SigmaStudio and the pointer to the memory is passed as an argument to the Plug-In function. The size of the state memory required by the Algorithm should be mentioned in the Algorithm Designer. Refer to section 7.4 for more details. The state memory is initialized with zeros by SigmaStudio every time before downloading a new Schematic. Four state buffers (pointers) are available for the Plug-In to use.
| ===Constant Tables=== All global variables and global tables in the Module are treated as constant tables by SigmaStudio. In case of ADSP-SC5xx only one instance of this memory is allocated per schematic. This memory is mapped on to the parameter buffer. Note: Modification of this memory is allowed even though this is treated as constant table by SigmaStudio. This memory is shared across all modules in any given schematic.
| ===Scratch=== Temporary buffers or variables required by the Algorithm can be mapped to the scratch memory. This memory is shared by all the Modules in the Schematic. There are 2 types of Scratch memory; memory mapped to DM block and memory mapped to PM block. An Algorithm can choose to use either or both based on the requirement. Both scratch memories are allocated by SigmaStudio and the pointer to the memory is passed as a parameter to the Plug-In function. The size of the scratch memory required by the Algorithm should be specified in the Algorithm Designer. Scratch memory is available only for block processing Algorithms. Total amount of scratch Memory reserved by SigmaStudio is the maximum of scratch memory requirement by Modules that are part of the Schematic.
| ====General Guidelines====

-  All global variables/buffers/tables accessed from an Algorithm are shared across instances of all the Algorithms inserted in the schematic.
-  Code and data can be placed in any section.
-  Only extended precision state memory is supported. Tables or parameters cannot be in extended precision.
-  Extended precision access must be cleared at the beginning and restored before exiting if the Plug-In uses either State B or State C memory buffers. This is because Applications may place the 32-bit state memory buffers in the same block as the Extended Precision state memory buffer.
-  Since the input buffers of a Plug-In can be reused by many subsequent Modules in a Schematic, care should be taken to preserve the input buffers and to avoid overwriting of these buffers.
-  If there are 2 functions with the same name defined in a single file, the linker gives a “Multiply defined symbol” error when the schematic which uses the function is link-compile-downloaded. If the functions with same name are defined in different files, the linker doesn’t throw any error during the schematic compilation and linking. It uses whichever function definition it finds first during linking. Hence, it is advisable to use unique function names if it is not intended for the functions to be shared across modules or with the target application.

| 
| ====Example==== The example code below shows a block processing implementation of a volume control function.

::

   #include "adi_ss_extmod.h" 

   #pragma section("seg_pmco") 
   void BPROCESS_Scale (SSBlockAlgo* pBlkAlgoInfo) 
   { 
     int index, sample, gain, blockSize, repCount;
     float *pInput, *pOutput;
     
     repCount = pBlkAlgoInfo->nGrowth;
     
     for(index = 0; index < repCount; index++)
     {   
         blockSize = pBlkAlgoInfo->pInputs[index].pBlockProperties->nBlockSize;
         gain = ((float *)pBlkAlgoInfo->pParam)[index];
         
         pInput = pBlkAlgoInfo->pInputs[index].pSamples;
         pOutput = pBlkAlgoInfo->pOutputs[index].pSamples;   
     
         for(sample = 0; sample < blockSize; sample++)
         {
             pOutput[sample] = pInput[sample] * gain;
         }
     }
   }

| 
| The example code below shows a sample processing implementation of a volume control function.

::

   #include "adi_ss_extmod.h" 

   #pragma section("seg_pmco") 
   void PROCESS_Scale (float pInput[], float pOutput[], float pState[], float pParameter[], int nRepCount) 
   { 
     int index;
     float gain;
     
     for(index = 0; index < nRepCount; index++)
     {   
         gain = pParameter[index];
         pOutput[index] = pInput[index] * gain;
     }
   }
    
