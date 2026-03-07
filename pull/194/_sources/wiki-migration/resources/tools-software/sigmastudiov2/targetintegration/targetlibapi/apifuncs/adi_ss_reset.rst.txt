| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apifuncs>`
| =====adi_ss_reset=====
| Prototype

::

    ADI_SS_RESULT adi_ss_reset( ADI_SS_COMM_HANDLE hSSComm, ADI_SS_COMM_CONFIG *pConf);

| 
| Description
| The function is to get the reset the SS+ instance to its initial state.
| Parameters
| Name: phSSn

::

   Type: ADI_SS_SSN_HANDLE *
   Direction: Output
   Description: Pointer to handle of SS+ instance.

   Name: pConf
   Type: ADI_SS_COMM_CONFIG *
   Direction: Input
   Description: Used to pass the configuration parameters to the communication module.

| 
| Return value
| An appropriate error code of type ADI_SS_RESULT is returned.
