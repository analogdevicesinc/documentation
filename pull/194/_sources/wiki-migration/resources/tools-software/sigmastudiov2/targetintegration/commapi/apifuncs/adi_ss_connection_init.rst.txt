| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apifuncs>`
| =====adi_ss_connection_Init=====
| Prototype

::

    ADI_SS_CONNECTION_RESULT adi_ss_connection_Init(ADI_SS_MEM_BLOCK *pMemBlk, 
                                                    ADI_SS_CONNECTION_CONFIG *pConnectionConfig, 
                                                    ADI_SS_CONNECTION_HANDLE *phSSConnection 
                                                   )

| 
| Description
| Connection component API for creating and initializing a physical connection.
| Parameters
| Name: pMemBlk

::

   Type: ADI_SS_MEM_BLOCK
   Direction: Input
   Description: Pointer to a block of memory.

   Name: pConnectionConfig
   Type: ADI_SS_CONNECTION_CONFIG*
   Direction: Input
   Description: Configuration structure populated by the application.

   Name: phSSConnection
   Type: ADI_SS_CONNECTION_HANDLE *
   Direction: Input
   Description: Pointer to the Handle to the Connection Component populated by this function.

| 
| Return value
| An error code of type ADI_SS_COMM_RESULT is returned.
| • ADI_SS_COMM_SUCCESS : Communication init successful.
| • ADI_SS_CONNECTION_INSUFF_MEM : Connection Init failed due to insufficient memory.
| • ADI_SS_CONNECTION_INVALID_CONFIG : Connection Init failed due to invalid config.
| • ADI_SS_COMM_FAILED : Communication init failed due to general error.
