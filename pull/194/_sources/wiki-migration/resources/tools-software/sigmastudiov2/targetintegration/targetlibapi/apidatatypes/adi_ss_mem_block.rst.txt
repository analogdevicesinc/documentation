| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apidatatypes>`
| =====ADI_SS_MEM_BLOCK=====
| Structure

::

    typedef struct __MemBlock { int32_t nSize; 
                                int32_t nFlags; 
                                void *pMem; 
                              } ADI_SS_MEM_BLOCK;

| 
| Description
| The structure ADI_SS_MEM_BLOCK captures the information about the individual memory blocks in the ADI_SS_MEM_MAP structure.
| Fields
| • nSize Indicates the size of the memory block.
| • nFlags Flag indicating the status of the memory block. This field is reserved for future use.
| • pMem Pointer to the memory block.
