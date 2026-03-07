| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apifuncs>`
| =====adi_ss_clearState=====
| Prototype

::

    ADI_SS_RESULT adi_ss_clearState(ADI_SS_SSN_HANDLE hSSn);

| 
| Description
| The function is to clear the state memory buffers used by the SS+ instance.
| Parameters
| Name: hSSn

::

   Type: ADI_SS_SSN_HANDLE 
   Direction: Input
   Description: Handle to the SSn instance.

| 
| Return value
| An appropriate error code of type ADI_SS_RESULT is returned.
