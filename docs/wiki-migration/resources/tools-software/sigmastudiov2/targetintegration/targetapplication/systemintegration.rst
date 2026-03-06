| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication>`
| =======System Integration======= The SigmaStudio+ application integrated with Target application using separate application space allocated for the SigmaStudio+ application. The target application is responsible to allocate required memory which are left free by the target application. The memory block allocated from target application is called GMAP and SigmaStduio+ schematic uses the target allocated memory space to allocate memory for code, parameter and state data for running SigmaStudio+ application over target platform.
| ======GMAP and SMAP====== The **Global Memory map** (GMAP) contains information about the available physical memory for the schematic, specifically the unused memory on a per-block basis after consumption by the Target application. The SigmaStudio+ schematic application reads the GMAP information when the corresponding Target application ".dxe" file for the SHARC core is selected.
| SMAP stands for **Schematic Memory MAP**. This information is communicated to the target library by the SigmaStudio+ host. SMAP includes details on various framework parameters such as sampling rate, block size, SPORT configuration, memory-mapped information code, parameters, and state data. It also contains memory information for the SigmaStudio+ schematic (SSn) instances.
| Before delving into GMAP and SMAP, it is essential to understand some basic files related to them.
| The **adi_ss_gmap.asm** file, included in the target application, defines the **GMAP structure** used to assign the start address and length of each memory block. There are seven memory blocks defined to allocate memory from the target application. The linker file **adi_ss_app.ldf** is used along with the applications .ldf file to reserve memory sections for GMAP. The GMAP linker file includes comments indicating which memory block will be used for schematic application data.

| The **adi_ss_smap.h** file, included in the target application, defines the **SMAP structure** used to assign the start address and length of each memory buffer reserved for code, parameters, and state data. These SMAP buffers are called **SS buffers**, and the utilization of each memory buffer in the SigmaStudio+ schematic will be printed in the **Output Window**.
| =====Application DXE===== The GMAP information is available in the SHARC core Application DXE. You can load the Application DXE into the schematic using the ‘Select Application DXE’ button for the selected core in the corresponding SHARC core settings tab, as shown below. :doc:`Figure </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/systemintegration>`.
| |image1|

.. container:: centeralign

   \ **Figure:** SigmaStudioPlus UI where DXE is selected


| =====Global Memory Map (GMAP)=====
| This structure contains information about the available physical memory in each of the SHARC memory blocks. This information is read by the SigmaStudioPlus host using application DXE. The :doc:`Figure </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/systemintegration>` below shows the arrangement of information within the GMAP structure.

|image2|

.. container:: centeralign

   \ **Figure:** GMAP structure format


| The table below lists the blocks made available to the host by the target through GMAP. ^ **Sl No** ^ **Physical Block** ^ **Description** ^ **Used for** ^ \| 1 \| Block 0 \| L1 block0 \| Allocation of SigmaStudioPlus schematic code \| \| 2 \| Block 1 \| L1 block1 \| Allocation of SigmaStudioPlus schematic 32-bit data (State) \| \| 3 \| Block 2 \| L1 block2 \| Allocation of SigmaStudioPlus schematic parameters (Coeff) \| \| 4 \| Block 3 \| L1 block3 \| Allocation of SigmaStudioPlus schematic 48-bit data (data-48) and 32-bit data (State B) \| \| 5 \| Block L3 code \| L3 SW code memory block \| Allocation of SigmaStudioPlus schematic code (Code-B) \| \| 6 \| Block L3 data \| L3 data memory block \| Allocation of SigmaStudioPlus schematic 32-bit data (State C) \| \| 7 \| Block L2 data \| L2 cached memory block \| For SSn-target library and for inter core communication in dual core mode \|
|

.. container:: centeralign

   \ **Table:** GMAP blocks


The GMAP structure allocates memory for each of the memory blocks to be shared with the SigmaStudioPlus host.

.. code:: c

   #define NUM_BLOCKS 7
   #define SIZE_GMAP (NUM_BLOCKS*2 + 1)
   .global _GMAP;

   .ALIGN 4;
   _GMAP:
   /* Number of memory blocks */
       .var = NUM_BLOCKS;
   /* Mem Block 0 L1 in LDF */ 
       .var = _Block0_L1_space;
   /* Total Mem Size available for SigmaStudioPlus Host from L1 Block0 */  
       .var = _Block0_L1_space_length;
   /* Currently not used */    
       .var = _Block0_L1_space_flag;
   /* Mem Block 1 L1 in LDF */ 
       .var = _Block1_L1_space;
   /* Total Mem Size available for SigmaStudioPlus Host from L1 Block1 */  
       .var = _Block1_L1_space_length;
   /* Currently not used */    
       .var = _Block1_L1_space_flag;
   /* Mem Block 2 L1 in LDF */ 
       .var = _Block2_L1_space;    
   /* Total Mem Size available for SigmaStudioPlus Host from L1 Block2 */
       .var = _Block2_L1_space_length;
   /* Currently not used */    
       .var = _Block2_L1_space_flag;
   /* Mem Block 3 L1 in LDF */ 
       .var = _Block3_L1_space;
   /* Total Mem Size available for SigmaStudioPlus Host from L1 Block3 */  
       .var = _Block3_L1_space_length;
   /* Currently not used */    
       .var = _Block3_L1_space_flag;
   /* Mem L3 Code (external) in LDF */ 
       .var = _Block_L3_code_space;
   /* Total Mem Size available for SigmaStudioPlus Host from L3 code */        
       .var = _Block_L3_code_space_length; 
   /* Currently not used */
       .var = _Block_L3_code_space_flag;
   /* Mem L3 Data (external) in LDF */ 
       .var = _Block_L3_data_space;
   /* Total Mem Size available for SigmaStudioPlus Host from L3 data */        
       .var = _Block_L3_data_space_length; 
   /* Currently not used */
       .var = _Block_L3_data_space_flag;   
   /* Mem L2 Data (data cache) in LDF */
       .var = _Block_L2_data_space;
   /* Total Mem Size available for SigmaStudioPlus Host from L2 data cache */      
       .var = _Block_L2_data_space_length;
   /* Currently not used */    
       .var = _Block_L2_data_space_flag;   
   ._GMAP.end:

| 
| The GMAP structure values are updated with memory blocks allocated in the **adi_ss_app.ldf** file for each target application. The LDF file is available in the respective target application's source folder. For example, the **adi_ss_app.ldf** file for the ADSP-2156x target can be found in **C:\\Analog Devices\\SigmaStudioPlus-Relx.x.x\\Target\\Examples\\Demo\\ADSP-2156x\\Source** folder.

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

The start addresses and sizes of the GMAP memory blocks are allocated by the target application. The details of the GMAP blocks can be found in the generated linker map file **(SS_App_Core1.map.xml)** located in the corresponding build output folder **(Release/Debug)**.

| |image3|

.. container:: centeralign

   \ **Figure:** GMAP block allocation in Map file


Schematic Memory Map (SMAP)
===========================

| The SMAP information is communicated to the target library by the SigmaStudio+ host when the schematic link compile download is completed. The SMAP information is sent as a separate packet to the target application to initialize the SigmaStudio+ application instance with the SMAP data. The packet information can be viewed in the capture window. SMAP contains details on various framework parameters such as sampling rate, block size, SPORT configuration, etc. It also includes memory information for the SSn instances. The SMAP data can be mapped to the **SMAP structure (SS_SMAP)** defined in **adi_ss_smap.h**. The SMAP structure is detailed below.
| ``/* SMAP structure */
  struct SS_SMAP
  {
      SS_SMAP_FW_INFO         oFwInfo;      
      uint32_t                nNumSSn;      
          ADI_SS_FW_PROCESS_MODE  eProcessMode;
      SS_SMAP_SSN_INFO        oSSnInfo[ADI_SS_FW_MAX_PROC_BLOCKS];  
  };``
| The structure elements are described below:
| ^ **Element** ^ **Description** ^

============ ================================
oFwInfo      Instance of framework structure
nNumSSn      Number of SSn instance
eProcessMode SSn processing mode
oSSnInfo     Array of SSn info structure type
============ ================================

| ADI_SS_FW_PROCESS_MODE is an enumeration defined in *adi_ss_smap.h* file.
| Following are the different processing modes for the different process blocks.
| ^ **Enumerator** ^

+--------------------------------+


| ADI_SS_FW_PROCESSMODE_SINGLE   |

+--------------------------------+

| ADI_SS_FW_PROCESSMODE_SERIAL   |

+--------------------------------+

| ADI_SS_FW_PROCESSMODE_PARALLEL |

+--------------------------------+

| ADI_SS_FW_PROCESSMODE_HYBRID1  |

+--------------------------------+

| ADI_SS_FW_PROCESSMODE_HYBRID2  |

+--------------------------------+

| 
| The SMAP buffer information for the target framework can be found in SigmaStudioPlus schematic **compiler output** window.
| |image4|

.. container:: centeralign

   **Figure: \**SMAP block allocations in schematic compilation


| The SMAP buffer information and corresponding GMAP blocks are shown in below table.
| ^ **GMAP Blocks** ^ **SMAP Buffers** ^ **SMAP Memory Section Names** ^ **Purpose** ^ \| Block0_L1_space \| SS Buffer 1 \| Code \| SigmaStudio+ schematic instance code memory \| \| Block1_L1_space \| FW Buffer 0 \| NA \| SigmaStudio+ framework buffers for I/O Data \| \| ::: \| SS Buffer 4 \| StateA \| SigmaStudio+ schematic instance Data32 memory \| \| Block2_L1_space \| SS Buffer 5 \| Param \| SigmaStudio+ schematic instance parameter memory \| \| Block3_L1_space \| SS Buffer 6 \| NA \| SigmaStudio+ schematic instance extended precision state memory \| \| ::: \| SS Buffer 8 \| StateB \| SigmaStudio+ schematic instance Data32 B memory \| \| Block_L3_code_space \| SS Buffer 7 \| CodeB \| SigmaStudio+ schematic instance code B memory \| \| Block_L3_data_space \| SS Buffer 9 \| StateC \| SigmaStudio+ schematic instance Data32 C memory \| \| ::: \| SS Buffer 5 \| ParamB \| SigmaStudio+ schematic instance parameter B memory \| \| Block_L2_data_space \| SS Buffer 0 \| NA \| SigmaStudio+ schematic instance handle \| \| ::: \| SS Buffer 2 \| NA \| Memory for Block communication processing \| \| ::: \| SS Buffer 3 \| NA \| Memory for Param safe load communication processing \| \| ::: \| SS Buffer 10 \| NA \| Memory for inter core communication \|
|

.. container:: centeralign

   \ **Table:** SMAP buffer allocation in GMAP blocks


.. note::

   In order to create SMAP, the target application has no control other than GMAP section mapping.


====SS_SMAP_FW_INFO====

::

   typedef struct SS_SMAP_FW_INFO
   {
       ADI_SS_FW_HOST_CONFIG  oFwHostConfig;   
       uint32_t               nNumFwBuffers; 
       ADI_SS_MEM_BLOCK       oFwBuff[MAX_SMAP_FW_BUFFERS]; 
   }SS_SMAP_FW_INFO;

| 
| Framework info structure within SMAP. The structure elements are described below.
| ^ **Element** ^ **Description** ^

+---------------+-----------------------------------------------------------------------+
| oFwHostConfig | Structure instance for host configurable framework parameters         |
+---------------+-----------------------------------------------------------------------+
| nNumFwBuffers | Part of memory required for the framework is provided by the host.    |
|               | This field indicates the number of buffers required for the framework |
+---------------+-----------------------------------------------------------------------+
| oFwBuff       | Array of mem blocks for the framework buffers                         |
+---------------+-----------------------------------------------------------------------+

| 
| ====ADI_SS_FW_HOST_CONFIG====

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
| ^ **Element** ^ **Description** ^

+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nBlockSize           | Schematic processing block size                                                                                                                                    |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nInInterfaceBuffSz   | Total input interface buffer size reserved by host for all pins. This has to be a multiple of nBlockSize. This field will be used for input buff size validation   |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nNumInInterfaceBuff  | Number of input interface buffers of size nBlockSize for the i/o data buffering by the framework                                                                   |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nOutInterfaceBuffSz  | Total output interface buffer size reserved by host for all pins. This has to be a multiple of nBlockSize. This field will be used for output buff size validation |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nNumOutInterfaceBuff | Number of output interface buffers of size nBlockSize for the i/o data buffering by the framework                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nOutputPreroll       | Output preroll as a multiple of nBlockSize                                                                                                                         |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nInSamplingRate      | Input sampling rate                                                                                                                                                |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nOutSamplingRate     | Output sampling rate                                                                                                                                               |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| eAudioMode           | Audio mode. (ADI_SS_FW_ADCOEXIST (Analog digital coexistence mode) or ADI_SS_FW_ADCOEXIST_DIGICLOCK (Analog digital coexistence digital clock mode))               |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| eFwMultiCoreMode     | Parameter for different types of signal flows designed in host for multicore mode                                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nPeripheralIOBuffSz  | Total Peripheral i/o buffer size for all pins including input and output. This field is currently not used                                                         |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nNumPeripheralIOBuff | Number of peripheral i/o buffers. This field is currently not used                                                                                                 |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nNumSources          | Number of Data sources                                                                                                                                             |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| eSourcePeriType      | Source peripheral type enumeration for each of the sources                                                                                                         |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| oSourcePeriConfig    | SPORT configuration for each of the sources received from the host                                                                                                 |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nNumSinks            | Number of Data sinks                                                                                                                                               |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| eSinkPeriType        | Sink peripheral type enumeration for each of the sinks                                                                                                             |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| eSinkPeriConfig      | SPORT configuration for each of the sinks received from the host                                                                                                   |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ADI_SS_FW_AUDIOMODE is an enumeration for audio mode defined in *adi_ss_smap.h* file.
| ^ **Enumerator** ^^

+-------------------------------+-----------------------------------------------+
| ADI_SS_FW_ADCOEXIST           | Analog digital coexistence mode               |
+-------------------------------+-----------------------------------------------+
| ADI_SS_FW_ADCOEXIST_DIGICLOCK | Analog digital coexistence digital clock mode |
+-------------------------------+-----------------------------------------------+

| 
| ADI_SS_FW_MULTICORE_MODE is an enumeration for different types of signal flows designed in Host for multicore mode. It is defined in *adi_ss_smap.h* file.
| ^ **Enumerator** ^

+-------------------------------------+


| ADI_SS_FW_MULTICOREMODE_INDEPENDENT |

+-------------------------------------+

| ADI_SS_FW_MULTICOREMODE_DUAL        |

+-------------------------------------+

| 
| ADI_SS_FW_DATA_PERI_TYPE is an enumeration for data peripheral type defined in *adi_ss_smap.h* file.
| ^ **Enumerator** ^^

+-----------------------------+------------------------------------------------------------------------------------+
| ADI_SS_PERI_TYPE_SPORT_PCM  | Pin configured to use SPORT for I/O operation. PCM type of data is Tx/Rx by SPORT  |
+-----------------------------+------------------------------------------------------------------------------------+
| ADI_SS_PERI_TYPE_SPORT_PCMX | Pin configured to use SPORT for I/O operation. PCMx type of data is Tx/Rx by SPORT |
+-----------------------------+------------------------------------------------------------------------------------+
| ADI_SS_PERI_TYPE_SM         | Pin configured to use Shared Memory for I/O operation                              |
+-----------------------------+------------------------------------------------------------------------------------+
| ADI_SS_PERI_TYPE_LP         | Pin configured to use Link Port for I/O operation                                  |
+-----------------------------+------------------------------------------------------------------------------------+

| 
| ====ADI_SS_FW_DATA_PERI_CONFIG====

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

+---------------------+---------------------------------------------------------------------------------------------------------------+
| **Element**         | **Description**                                                                                               |
+=====================+===============================================================================================================+
| eDataDAIPinGroup    | Primary in/out DAI pin group for a source or sink                                                             |
+---------------------+---------------------------------------------------------------------------------------------------------------+
| eDataDAIPin         | Primary in/out DAI pin number for a source or sink                                                            |
+---------------------+---------------------------------------------------------------------------------------------------------------+
| nEnSecChannel       | Flag indicating whether secondary channel of the peripheral is enabled or not. This field is currently unused |
+---------------------+---------------------------------------------------------------------------------------------------------------+
| eDataDAIPinGroupSec | Secondary in/out DAI pin group for a source or sink. This field is currently unused                           |
+---------------------+---------------------------------------------------------------------------------------------------------------+
| eDataDAIPinSec      | Secondary in/out DAI pin number for a source or sink. This field is currently unused                          |
+---------------------+---------------------------------------------------------------------------------------------------------------+
| nChannels           | Number of audio channels from/to the peripheral                                                               |
+---------------------+---------------------------------------------------------------------------------------------------------------+
| oSPORTPeriConfig    | SPORT peripheral configuration                                                                                |
+---------------------+---------------------------------------------------------------------------------------------------------------+

| 
| ====ADI_SS_FW_SPORT_CONFIG====

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
| ^ **Element** ^ **Description** ^

+---------------+---------------------------------------------------------------------+
| eSportNum     | Enumeration for SPORT number for a source or a sink                 |
+---------------+---------------------------------------------------------------------+
| eSportHalf    | Enumeration for SPORT half for a source or a sink                   |
+---------------+---------------------------------------------------------------------+
| eSportClkPol  | Enumeration for SPORT clock polarity. Rising/Falling                |
+---------------+---------------------------------------------------------------------+
| eSportFSPol   | Enumeration for SPORT frame sync polarity. Rising/Falling           |
+---------------+---------------------------------------------------------------------+
| eSportMode    | Enumeration for SPORT operation mode indicating I2S/TDM4/TDM8/TDM16 |
+---------------+---------------------------------------------------------------------+
| nSportWordLen | SPORT data word length                                              |
+---------------+---------------------------------------------------------------------+

| 
| ====SS_SMAP_SSN_INFO====

::

   typedef struct SS_SMAP_SSN_INFO
   {
       SMAP_HOST2TGT_INFO  oHostInfo;
       uint32_t        nNumSSnBuffers;
       ADI_SS_MEM_BLOCK    oSSnBuff[MAX_SMAP_SSN_BUFFERS];
   }SS_SMAP_SSN_INFO;

| 
| SSn info structure which provides SSn specific details including memory details for the target library.
| The structure elements are described below:
| ^ **Element** ^ **Description** ^

+----------------+----------------------------------------------------------------------------+
| oHostInfo      | SSn information which has to be communicated to target framework from host |
+----------------+----------------------------------------------------------------------------+
| nNumSSnBuffers | Number of buffers required for SSn target library                          |
+----------------+----------------------------------------------------------------------------+
| oSSnBuff       | Array of mem blocks for the SSn buffers                                    |
+----------------+----------------------------------------------------------------------------+

| 
| ====SMAP_HOST2TGT_INFO====

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
| ^ **Element** ^ **Description** ^

+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nInPhyChannels  | Number of physical input channels configured from the IC control form of the SigmaStudio+ GUI. This field is used for total input channel count validation from within the framework   |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nOutPhyChannels | Number of physical output channels configured from the IC control form of the SigmaStudio+ GUI. This field is used for total output channel count validation from within the framework |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| aInChMap        | Array indicating the indices of the input channels used within the SSn. Rest must be -1                                                                                                |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| aOutChMap       | Array indicating the indices of the output channels used within the SSn. Rest must be -1                                                                                               |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| =====Memory Allocations=====
| For target processors without an L3 memory section, the L3 data and code sections must be mapped from the L2 section. For example, in the ADSP-21569 target app.ldf, the memory start address for the L2 code section is 0x200C0000 and the end address is 0x200D7FFF (96 kB), while for the L2 data section, the start address is 0x200D8000 and the end address is 0x200F9FFF (160 kB). Therefore, users must set the memory ranges for the mem_L2_bw memory section in the app.ldf file accordingly. If L3 memory is present, the start address for the mem_L2_bw section is 0x20000000 and the end address is 0x200F9FFF. If L3 memory is not present, the end address of the mem_L2_bw section must be set to 0x200BFFFF.
| |image5| |image6|

.. container:: centeralign

   \ **Figure:** Memory Sections


| =====Memory Block Customization in Case of Insufficient L1 Blocks=====
| Any L1 memory blocks can be assigned to code, parameter, and data buffers based on the requirement and availability. The available memory can be found in the generated target application map file, and the required memory can be found in the SigmaStudio+ schematic compilation output window.

The best practice for designing a schematic is to know the MIPS and memory requirements of the modules used in the schematic. This way, the memory requirements will be easily known for our design. In some scenarios, the internal framework memory requirements may not be known, leading to memory insufficiency errors. In such cases, the memory requirements can be easily determined by mapping code, parameter, and state memory to the L3 buffer. The code and data buffers can be mapped to L3 memory using the schematic settings section map, as shown in the image.

| |image7|

.. container:: centeralign

   \ **Figure:** Memory Section Map Code and Data


| The parameter buffer can be mapped to L3 memory using the “adi_ss_app.ldf” file as shown in the image.

|image8|

.. container:: centeralign

   \ **Figure:** Memory Section Map Parameter


| **Note:**
| 1. The L3 section map is recommended only for identifying the memory requirements of the schematic when there is a memory insufficiency error.
| 2. The code, parameter, and DataC buffers can be mapped to L2 using the **adi_ss_app.ldf** file.
| 3. MIPS consumption will be higher when the schematic code, parameter, and data are mapped to L2 or L3. Therefore, it is recommended to use L1 memory for optimal performance.
| 4. If the memory requirements are mostly clear but there is a slight memory insufficiency, we can swap the L1 memory blocks between code, parameter, and data, or free up some data allocation of the target application using the **app.ldf** file.
| =====Memory Block Customization without L3 Memory=====
| Based on the use case, if the target processor does not have L3 memory (SDRAM) or if the user prefers not to include L3 memory, they can modify the LDF file of each SHARC core's project to map the memory allocation of the target application to L2 memory to support the SigmaStudio+ application.
| Below are the steps to move memory allocations from L3 to L2 memory:
| 1. Back up the default “app.ldf” file.
| 2. In the System.svc, navigate to the "startup code/LDF" plugin if it is already present; if not, install the "startup code/LDF" add-in from the System Configuration Overview tab. This step is not required if the target processor lacks L3 controller support, such as the ADSP-SC571 or ADSP-21565 etc.
| 3. In the "startup code/LDF" under the LDF menu, uncheck the "Use external memory (SDRAM)" option and save the configuration settings to generate the "app.ldf" file without L3 support. Note that this step is not required if the target processor does not have L3 controller support, such as the ADSP-SC571 or ADSP-21565, as these processors already generate an "app.ldf" without L3 support.
| |image9|

.. container:: centeralign

   \ **Figure:** LDF Settings


| 4. Compare the default "app.ldf" file with the newly generated one and copy the required sections into the new "app.ldf" file. For example, include the following sections:

::

       INPUT_SECTIONS( $OBJECTS(ss_fw_constdata_fast) )
       INPUT_SECTIONS( $OBJECTS(ss_app_data0_fast) )
       INPUT_SECTIONS( $OBJECTS(ss_app_data_ipc_fast) )
       INPUT_SECTIONS( $OBJECTS(ss_app_data0_fast_uncached) )

| For some processors, these sections may already be preserved, so no changes will be necessary. Additionally, ensure the inclusion of the symbol KEEP(\_GMAP) and the line #include "adi_ss_app.ldf" if they are not already present in the new "app.ldf" file.
| 5. In case of DemoUc application the memory section “ss_app_uc_data” can be moved to L2 general data section.
| 6. The SigmaStudio+ L3 code section can be mapped to “mem_L2_bw_SS4G_Code” of L2 and L3 data section can be mapped to “mem_L2_bw_SS4G_Data” of L2. For this memory allocation the L2 memory block need to be adjusted for end address to align with mem_L2_bw_SS4G_Code. For example in if the “mem_L2_bw_SS4G_Code” and “mem_L2_bw_SS4G_Data” defined as below,
| |image10|

.. container:: centeralign

   \ **Figure:** SHARC Core1 app.ldf file (L2 Memory Section)


| |image11|

.. container:: centeralign

   \ **Figure:** SHARC Core2 app.ldf file (L2 Memory Section)


   | By observing the **start** and **end** addresses of the Code and Data sections for the SS schematic, the memory should be re-aligned in other L2 memory sections. For the ADSP-SC573, the memory blocks **mem_L2B7B8_bw** (in SHARC Core1) and **mem_L2B5B6_bw** (in SHARC Core2) need to be re-aligned, as highlighted by "2" in both SHARC Core1 and SHARC Core2’s app.ldf files.
|

.. note::

   Proper memory address boundary alignment is crucial for SHARC processors to ensure efficient data access and avoid exceptions. Misaligned memory accesses can cause core exceptions, leading to application failures


| 7. If the target processor does not have L3 controller support, then we need to follow only step 6 to make required code and dada memory mapping and boundary adjustment for SigmaStudio+ application.
| 8. Once L2 memory blocks aligned for the SigmaStudio+ code and data memory, rebuild the target application project and run the schematic applications.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/dxe.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/gmap_structure_format.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/gmap_block_allocation_in_map_file.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/smap_block_allocations_in_schematic_compilation.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/memalloc1.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/memalloc2.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/sectionmap.png
   :width: 1080px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/sectionmapparam.png
   :width: 1080px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/Systemsvc.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/SHARC Core1 app.ldf file.png
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/5.png
