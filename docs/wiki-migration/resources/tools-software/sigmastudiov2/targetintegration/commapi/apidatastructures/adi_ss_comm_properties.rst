| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apidatastructures>`
| =====ADI_SS_COMM_PROPERTIES=====
| Structure
| typedef struct ADI_SS_COMM_PROPERTIES { bool bCommError;

::

                                            bool bCustomCmdRcvd; uint32_t *pSSnBuf; 
                                            ADI_SS_MEM_SMAP *pMemSMap; 
                                            /* Fileds used for adi_ss_comm_SetProperties() API */ 
                                            uint32_t nProcId; 
                                            uint32_t nNumProcBlocks; 
                                            void* hasSSnHandle[MAX_NUMBER_OF_PROCESSORS] [ADI_SS_FW_MAX_PROC_BLOCKS] 
                                          }ADI_SS_COMM_PROPERTIES;

| 
| Description
| Properties structure which provides information about the Communication component.
| Fields
| • bCommError Flag indicating communication error.
| • bCustomCmdRcvd This flag indicates that a custom command is received.
| • pSSnBuf This pointer contains the data received via custom command.
| • pMemSMap Pointer to SMAP structure.
| • nProcId This field is used to specify the Processor ID
| • nNumProcBlocks This field is used to specify the number of Process Blocks running on a processor.
| • haSSnHandle SSn handle for each of the Process blocks.
