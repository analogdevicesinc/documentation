| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apifuncs>`
| =====adi_ss_getProperties=====
| Prototype

::

    ADI_SS_RESULT adi_ss_getProperties( ADI_SS_SSN_HANDLE hSSn, ADI_SS_SSNPROPERTIES *pProperties);

| 
| Description
| The function is to get the current state and other properties of SS+ instance from SigmaStudio+.
| Parameters
| Name: hSSn

::

   Type: ADI_SS_SSN_HANDLE 
   Direction: Input
   Description: Handle to the SS+ instance.

   Name: pProperties
   Type: ADI_SS_SSNPROPERTIES *
   Direction: Output
   Description: Used to pass properties from the SS+ to Application.

| 
| Return value
| An appropriate error code of type ADI_SS_RESULT is returned.
