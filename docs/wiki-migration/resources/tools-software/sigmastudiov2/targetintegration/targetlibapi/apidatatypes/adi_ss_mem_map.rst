| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apidatatypes>`
| =====ADI_SS_MEM_MAP=====
| Structure

::

   typedef struct __MemMap { int32_t nMemBlocks; 
                             ADI_SS_MEM_BLOCK *pMemBlocks[ADI_SS_MAX_MEM_BLOCKS];                                                                             
                           } ADI_SS_MEM_MAP;

| 
| Description
| The ADI_MEM_MAP structure passes the memory blocks that can be used by the SS+ to the adi_ss_create function.
| Fields
| • nMemBlocks Indicates number of memory blocks.
| • pMemBlocks Array of pointers to the memory blocks.
