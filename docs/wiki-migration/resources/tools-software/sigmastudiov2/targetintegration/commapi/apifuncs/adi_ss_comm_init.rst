| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apifuncs>`
| =====adi_ss_comm_init=====
| Prototype

::

    ADI_SS_COMM_RESULT adi_ss_comm_Init(ADI_SS_MEM_BLOCK *pMemBlk, 
                                        ADI_SS_COMM_CONFIG *pCommConfig, 
                                        ADI_SS_COMM_HANDLE *phSSComm)

| 
| Description
| This function creates an instance of SigmaStudio Communication Module and initializes it based on the config parameters supplied by the application.
| Parameters
| Name: pMemBlk

::

   Type: ADI_SS_MEM_BLOCK
   Direction: Input
   Description: Pointer to a memory block.

   Name: pCommConfig
   Type: ADI_SS_COMM_CONFIG
   Direction: Input
   Description: Pointer to communication config structure to be populated by the application.

   Name: phSSComm
   Type: ADI_SS_COMM_HANDLE
   Direction: Output
   Description: Pointer to communication handle.
   \\ 

| Return value
| An error code of type ADI_SS_COMM_RESULT is returned.
| • ADI_SS_COMM_SUCCESS : Communication init successful.
| • ADI_SS_COMM_INSUFFICIENT_MEMORY : Communication init failed due to insufficient memory.
| • ADI_SS_COMM_FAILED : Communication init failed due to general error.
