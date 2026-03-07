| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apifuncs>`
| =====adi_ss_init=====
| Prototype

::

    ADI_SS_RESULT adi_ss_init( ADI_SS_SSN_HANDLE hSSn, ADI_SS_CONFIG *pConfig );

| 
| Description
| The function adi_ss_init initializes an instance of the SS+ with the specified configuration.
| This function also performs other initializations such as:
| - Validate the configuration parameters against the configure information in SSn block.
| - Set the function pointer for SS+ process.
| - Set status to ADI_SSN_STATE_INITED.
| - Listen in communication ISR.
| Once the initialization is completed, the function either waits for the code and data to be received or immediately comes out depending upon the communication configuration. When data and code are received, they are placed in appropriate locations based on the memory locations specified by adi_ss_create.
| Parameters
| Name: hSSn

::

   Type: ADI_SS_SSN_HANDLE *
   Direction: Input
   Description: Handle to the SS+ instance.

   Name: pConfig
   Type: ADI_SS_CONFIG *
   Direction: Input
   Description: Used to pass configuration parameters to the SS+.

| 
| Return value
| An appropriate error code of type ADI_SS_RESULT is returned.
