GMAP & SMAP
===========

GMAP
----

| GMAP is the **Global memory MAP**.
| This structure holds information corresponding to the available physical memory in each of the SHARC memory blocks. This information is communicated by the target library to the SigmaStudioPlus host. The figure below shows the arrangement of information within the GMAP structure.

| |image1|
| **Fig:** GMAP structure format

| The table below lists the blocks made available to host by target through GMAP ^ **Sl No** ^ **Physical Block** ^ **Description** ^ **Used for** ^ \| 1 \| Block 0 \| L1 block0 \| Allocation of SigmaStudioPlus schematic code \| \| 2 \| Block 1 \| L1 block1 \| Allocation of SigmaStudioPlus schematic 32-bit data (State) \| \| 3 \| Block 2 \| L1 block2 \| Allocation of SigmaStudioPlus schematic parameters (Coef) \| \| 4 \| Block 3 \| L1 block3 \| Allocation of SigmaStudioPlus schematic 48-bit data (data-48) and 32-bit data (State B) \| \| 5 \| Block L3 code \| L3 SW code memory block \| Allocation of SigmaStudioPlus schematic code (Code-B)(State) \| \| 6 \| Block L3 data \| L3 data memory block \| Allocation of SigmaStudioPlus schematic 32-bit data (State C) \| \| 7 \| Block L2 data \| L2 cached memory block \| For SSn-target library and for inter core communication in dual core mode \|
| **Table:** GMAP blocks

The GMAP structure values updated with memory blocks allocated in “adi_ss_app.ldf” file for each target application. The “adi_ss_app.ldf” available in respective target application source folder. For example, the “adi_ss_app.ldf” file for ADSP-2156x target can be found in *C:\\Analog Devices\\SigmaStudioPlus-Relx.x.x\\Target\\Examples\\Demo\\ADSP-2156x\\Source* folder.

.. code:: c

   /*
   ** SigmaStudioPlus for Griffin application linker description file for GMAP
   */


   /* Default for SSn code */
   SS4G_block0
   {
      RESERVE(_Block0_L1_space, _Block0_L1_space_length = 2, 2)
      RESERVE_EXPAND(_Block0_L1_space, _Block0_L1_space_length, 0, 2)      
   } > mem_block0_bw

   /* Default for SSn data */
   SS4G_block1
   {
      RESERVE(_Block1_L1_space, _Block1_L1_space_length = 2, 2)
      RESERVE_EXPAND(_Block1_L1_space, _Block1_L1_space_length, 0, 2)      
   } > mem_block1_bw

   /* Default for SSn parameter */
   SS4G_block2
   {
      RESERVE(_Block2_L1_space, _Block2_L1_space_length = 8, 8)
      RESERVE_EXPAND(_Block2_L1_space, _Block2_L1_space_length, 0, 8)      
   } > mem_block2_bw

   /* Default for SSn data B and extended precision */
   SS4G_block3
   {
      RESERVE(_Block3_L1_space, _Block3_L1_space_length = 2, 2)
      RESERVE_EXPAND(_Block3_L1_space, _Block3_L1_space_length, 0, 2)      
   } > mem_block3_bw

   #if defined(MY_SDRAM_SWCODE_MEM)
   /* Default for SSn code B */
   SS4G_L3_Code
   {
      RESERVE(_Block_L3_code_space, _Block_L3_code_space_length = 2, 2)
      RESERVE_EXPAND(_Block_L3_code_space, _Block_L3_code_space_length, 0, 2)      
   } > MY_SDRAM_SWCODE_MEM
   #else
   /* Default for SSn code B */
   SS4G_L2_Code
   {
      RESERVE(_Block_L3_code_space, _Block_L3_code_space_length = 2, 2)
      RESERVE_EXPAND(_Block_L3_code_space, _Block_L3_code_space_length, 0, 2)      
   } > mem_L2_bw_SS4G_Code
   #endif

   #if defined(MY_SDRAM_DATA1_MEM)
   /* Default for SSn data C */
   SS4G_L3_Data
   {
      RESERVE(_Block_L3_data_space, _Block_L3_data_space_length = 8, 8)
      RESERVE_EXPAND(_Block_L3_data_space, _Block_L3_data_space_length, 0, 8)      
   } > MY_SDRAM_DATA1_MEM
   #else
   /* Default for SSn data C */
   SS4G_L2_Data1
   {
      RESERVE(_Block_L3_data_space, _Block_L3_data_space_length = 8, 8)
      RESERVE_EXPAND(_Block_L3_data_space, _Block_L3_data_space_length, 0, 8)      
   } > mem_L2_bw_SS4G_Data
   #endif

   /* Default for SSn L2 data for buffer sharing */
   /* This is allocated from the cached portion of L2 */
   SS4G_L2_Data
   {
      RESERVE(_Block_L2_data_space, _Block_L2_data_space_length = 2, 2)
      RESERVE_EXPAND(_Block_L2_data_space, _Block_L2_data_space_length, 0, 2)      
   } > MY_L2_CACHED_MEM

   /* Sections for inter core handshaking */
   /* This is allocated from the uncached portion of L2 for core 1 (SHARC 0) */
   #if !defined(__ADSP2156x__)
   #if defined(__ADSPSC5xx__)
   SS4G_L2_Core0_Handshake BW
   {
      INPUT_SECTIONS($OBJS_LIBS(ss4g_l2_core0_handshake) )
   } > mem_L2B1P2_bw

   /* This is allocated from the uncached portion of L2 for core 1 (SHARC 0) */
   SS4G_L2_Core1_Handshake BW
   {
      INPUT_SECTIONS($OBJS_LIBS(ss4g_l2_core1_handshake) )
   } > mem_L2B1P4_bw

   /* This is allocated from the uncached portion of L2 for core 2 (SHARC 1) */
   SS4G_L2_Core2_Handshake BW
   {
      INPUT_SECTIONS($OBJS_LIBS(ss4g_l2_core2_handshake) )
   } > mem_L2B1P3_bw
   #elif defined(__ADSP215xx__) && (__NUM_ARM_CORES__==0)
   /* This is allocated from the uncached portion of L2 for core 1 (SHARC 0) */
   SS4G_L2_Core1_Handshake BW
   {
      INPUT_SECTIONS($OBJS_LIBS(ss4g_l2_core1_handshake) )
   } > mem_L2B1P2_bw

   /* This is allocated from the uncached portion of L2 for core 2 (SHARC 1) */
   SS4G_L2_Core2_Handshake BW
   {
      INPUT_SECTIONS($OBJS_LIBS(ss4g_l2_core2_handshake) )
   } > mem_L2B1P3_bw
   #endif
   #endif

The GMAP memory blocks start addresses and size of which are allocated by target application and the details of GMAP blocks can be seen in the generated linker map file (SS_App_Core1.map.xml) under corresponding build output folder (Release/Debug).

| |image2|
| **Fig:** GMAP block allocation in Map file
| ===== SMAP ===== SMAP is the **Schematic memory MAP**.
| This information is communicated to the target library by the SigmaStudioPlus host. SMAP contains information on certain framework parameters such as sampling rate, block size, Sport configuration etc. It also contains memory information for the SSn instances. The SMAP structure is detailed below.
| ``/* SMAP structure */
  struct SS_SMAP
  {
      SS_SMAP_FW_INFO         oFwInfo;      
      uint32_t                nNumSSn;      
          ADI_SS_FW_PROCESS_MODE  eProcessMode;
      SS_SMAP_SSN_INFO        oSSnInfo[ADI_SS_FW_MAX_PROC_BLOCKS];  
  };``
| The structure elements are described below:
| **-> oFwInfo :** Instance of framework structure.
| **-> nNumSSn :** Number of SSn instance.
| **-> eProcessMode :** SSn processing mode.
| **-> oSSnInfo :** Array of SSn info structure type.
| The SMAP buffer information for the target framework can be found in SigmaStudioPlus schematic compiler output window.
| |image3|
| \**Fig: \**SMAP block allocations in schematic compilation
| The SMAP buffer information and corresponding GMAP blocks are shown in below table.
| ^ **GMAP Blocks** ^ **SMAP Buffers** ^ **SMAP Memory Section Names** ^ **Purpose** ^ \| Block0_L1_space \| SS Buffer 1 \| Code \| SigmaStudio instance code memory \| \| Block1_L1_space \| FW Buffer 0 \| NA \| SigmaStudio framework buffers \| \| ::: \| SS Buffer 4 \| StateA \| SigmaStudio instance Data32 memory \| \| Block2_L1_space \| SS Buffer 5 \| Param \| SigmaStudio instance parameter memory \| \| Block3_L1_space \| SS Buffer 6 \| NA \| SigmaStudio instance extended precision state memory \| \| ::: \| SS Buffer 8 \| StateB \| SigmaStudio instance Data32 B memory \| \| Block_L3_code_space \| SS Buffer 7 \| CodeB \| SigmaStudio instance code B memory \| \| Block_L3_data_space \| SS Buffer 9 \| StateC \| SigmaStudio instance Data32 C memory \| \| ::: \| SS Buffer 5 \| ParamB \| SigmaStudio instance parameter B memory \| \| Block_L2_data_space \| SS Buffer 0 \| NA \| SigmaStudio instance handle \| \| ::: \| SS Buffer 10 \| NA \| Memory for inter core communication \|
| **Table:** SMAP buffer allocation in GMAP blocks

.. note::

   The target application doesn’t have any control other than GMAP section mapping, to create SMAP


SS_SMAP_FW_INFO
~~~~~~~~~~~~~~~

::

   typedef struct SS_SMAP_FW_INFO
   {
       ADI_SS_FW_HOST_CONFIG  oFwHostConfig;   
       uint32_t               nNumFwBuffers; 
       ADI_SS_MEM_BLOCK       oFwBuff[MAX_SMAP_FW_BUFFERS]; 
   }SS_SMAP_FW_INFO;

| 
| Framework info structure within SMAP. The structure elements are described below.
| **-> oFwHostConfig:** Structure instance for host configurable framework parameters.
| **-> nNumFwBuffers:** Part of memory required for the framework is provided by the host.
| This field indicates the number of buffers required for the framework.
| **-> oFwBuff:** Array of mem blocks for the framework buffers.
| === ADI_SS_FW_HOST_CONFIG ===

::

   typedef struct ADI_SS_FW_HOST_CONFIG
   {
       uint32_t                   nBlockSize; 
       uint32_t                   nInInterfaceBuffSz;         
       uint32_t                   nNumInInterfaceBuff;        
       uint32_t                   nOutInterfaceBuffSz;        
       uint32_t                   nNumOutInterfaceBuff;       
       uint32_t                   nOutputPreroll;             
       uint32_t                   nInSamplingRate;            
       uint32_t                   nOutSamplingRate;           
       ADI_SS_FW_AUDIOMODE        eAudioMode;                 
       ADI_SS_FW_MULTICORE_MODE   eFwMultiCoreMode;             
       uint32_t                   nPeripheralIOBuffSz;        
       uint32_t                   nNumPeripheralIOBuff;
       uint32_t                   nNumSources;
       ADI_SS_FW_DATA_PERI_TYPE   eSourcePeriType[ADI_SS_MAX_SOURCES];
       ADI_SS_FW_DATA_PERI_CONFIG oSourcePeriConfig[ADI_SS_MAX_SOURCES];
       uint32_t                   nNumSinks;
       ADI_SS_FW_DATA_PERI_TYPE   eSinkPeriType[ADI_SS_MAX_SINKS];
       ADI_SS_FW_DATA_PERI_CONFIG oSinkPeriConfig[ADI_SS_MAX_SINKS];

   }ADI_SS_FW_HOST_CONFIG;

| 
| The framework parameters in this structure may be configured by the host.
| The structure elements are described below:
| **-> nBlockSize:** Schematic processing block size.
| **-> nInInterfaceBuffSz:** Total input interface buffer size reserved by host for all pins.
| This has to be a multiple of nBlockSize. This field will be used for input buff size validation.
| **-> nNumInInterfaceBuff:** Number of input interface buffers of size nBlockSize for the i/o data buffering by the framework.
| **-> nOutInterfaceBuffSz:** Total output interface buffer size reserved by host for all pins.
| This has to be a multiple of nBlockSize. This field will be used for output buff size validation.
| **-> nNumOutInterfaceBuff:** Number of output interface buffers of size nBlockSize for the i/o data buffering by the framework.
| **-> nOutputPreroll:** Output preroll as a multiple of nBlockSize.
| **-> nInSamplingRate:** Input sampling rate.
| **-> nOutSamplingRate:** Output sampling rate.
| **-> eAudioMode:** Audio mode. (ADI_SS_FW_ADCOEXIST (Analog digital coexistence mode) or ADI_SS_FW_ADCOEXIST_DIGICLOCK (Analog digital coexistence digital clock mode)).
| **-> eFwMultiCoreMode:** Parameter for different types of signal flows designed in host for multicore mode.
| **-> nPeripheralIOBuffSz:** Total Peripheral i/o buffer size for all pins including input and output.
| This field is currently not used.
| **-> nNumPeripheralIOBuff:** Number of peripheral i/o buffers. This field is currently not used.
| **-> nNumSources:** Number of Data sources.
| **-> eSourcePeriType:** Source peripheral type enumeration for each of the sources.
| **-> oSourcePeriConfig:** SPORT configuration for each of the sources received from the host.
| **-> nNumSinks:** Number of Data sinks.
| **-> eSinkPeriType:** Sink peripheral type enumeration for each of the sinks.
| **-> eSinkPeriConfig:** SPORT configuration for each of the sinks received from the host.
| === ADI_SS_FW_DATA_PERI_CONFIG ===

::

   typedef struct ADI_SS_FW_DATA_PERI_CONFIG
   {
       ADI_SS_FW_DAI_PIN_GROUP      eDataDAIPinGroup
       ADI_SS_FW_DAI_PIN        eDataDAIPin;
       uint32_t             nEnSecChannel;
       ADI_SS_FW_DAI_PIN_GROUP  eDataDAIPinGroupSec;
       ADI_SS_FW_DAI_PIN        eDataDAIPinSec;
       uint32_t                 nChannels; 
       ADI_SS_FW_SPORT_CONFIG       oSPORTPeriConfig;
   }ADI_SS_FW_HOST_CONFIG;

| 
| The framework parameters in this structure may be configured by the host.
| The structure elements are described below:
| **-> eDataDAIPinGroup:** Primary in/out DAI pin group for a source or sink.
| **-> eDataDAIPin:** Primary in/out DAI pin number for a source or sink.
| **-> nEnSecChannel:** Flag indicating whether secondary channel of the peripheral is enabled or not.
| This field is currently unused.
| **-> eDataDAIPinGroupSec:** Secondary in/out DAI pin group for a source or sink. This field is currently unused.
| **-> eDataDAIPinSec:** Secondary in/out DAI pin number for a source or sink. This field is currently unused.
| **-> nChannels:** Number of audio channels from/to the peripheral.
| **-> oSPORTPeriConfig:** SPORT peripheral configuration.
| === ADI_SS_FW_SPORT_CONFIG ===

::

   typedef struct ADI_SS_FW_SPORT_CONFIG
   {
       ADI_SS_FW_SPORT_NUM         eSportNum;     /*!< SPORT number  */
       ADI_SS_FW_SPORT_HALF        eSportHalf;    /*!< SPORT Half */
       ADI_SS_FW_SPORT_CLK_FS_POL  eSportClkPol;  /*!< SPORT clock polarity */
       ADI_SS_FW_SPORT_CLK_FS_POL  eSportFsPol;   /*!< SPORT frame sync polarity */
       ADI_SS_FW_SPORT_MODE        eSportMode;    /*!< SPORT operation mode */
       uint32_t                    nSportWordLen; /*!< SPORT word length */
   }ADI_SS_FW_SPORT_CONFIG;

| 
| The structure elements are described below:
| **-> eSportNum:** Enumeration for SPORT number for a source or a sink.
| **-> eSportHalf:** Enumeration for SPORT half for a source or a sink.
| **-> eSportClkPol:** Enumeration for SPORT clock polarity. Rising/Falling.
| **-> eSportFSPol:** Enumeration for SPORT frame sync polarity. Rising/Falling.
| **-> eSportMode:** Enumeration for SPORT operation mode indicating I2S/TDM4/TDM8/TDM16.
| **-> nSportWordLen:** SPORT data word length.

SS_SMAP_SSN_INFO
~~~~~~~~~~~~~~~~

::

   typedef struct SS_SMAP_SSN_INFO
   {
       SMAP_HOST2TGT_INFO  oHostInfo;
       uint32_t            nNumSSnBuffers;
       ADI_SS_MEM_BLOCK          oSSnBuff[MAX_SMAP_SSN_BUFFERS];
   }SS_SMAP_SSN_INFO;

| 
| SSn info structure which provides SSn specific details including memory details for the target library.
| The structure elements are described below:
| **-> oHostInfo:** SSn information which has to be communicated to target framework from host.
| **-> nNumSSnBuffers:** Number of buffers required for SSn target library.
| **-> oSSnBuff:** Array of mem blocks for the SSn buffers.
| === SMAP_HOST2TGT_INFO ===

::

   typedef struct SMAP_HOST2TGT_INFO
   {
       uint32_t         nInPhyChannels;                            
       uint32_t         nOutPhyChannels;                           
       int32_t          aInChMap[ADI_SS_FW_MAX_NUM_IN_CHANNELS_SMAP];  
       int32_t          aOutChMap[ADI_SS_FW_MAX_NUM_OUT_CHANNELS_SMAP];
   }SMAP_HOST2TGT_INFO;

| 
| This structure provides SSn information which has to be communicated to target framework.
| The structure elements are described below:
| **-> nInPhyChannels:** Number of physical input channels configured from the IC control form of the SigmaStudio GUI.
| This field is used for total input channel count validation from within the framework.
| **-> nOutPhyChannels:** Number of physical output channels configured from the IC control form of the SigmaStudio GUI.
| This field is used for total output channel count validation from within the framework.
| **-> aInChMap:** Array indicating the indices of the input channels used within the SSn. Rest must be -1.
| **-> aOutChMap:** Array indicating the indices of the output channels used within the SSn. Rest must be -1.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/advanceddesign/gmap_structure_format.png
   :width: 250px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/advanceddesign/gmap_block_allocation_in_map_file.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/advanceddesign/smap_block_allocations_in_schematic_compilation.png
   :width: 400px
