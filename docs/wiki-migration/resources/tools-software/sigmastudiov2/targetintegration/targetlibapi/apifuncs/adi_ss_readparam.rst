| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apifuncs>`
| =====adi_ss_readParam=====
| Prototype

::

    ADI_SS_RESULT adi_ss_readParam(ADI_SS_SSN_HANDLE hSSn, 
                                   uint32_t *pBuffer, 
                                   uint32_t nSSnParamMemOffset, 
                                   uint32_t nNumParams);

| 
| Description
| This function is used to read a single or a set of parameters from the SS+ parameter memory space.
| Parameters
| Name: hSSn

::

   Type: ADI_SS_SSN_HANDLE 
   Direction: Input
   Description: Handle to the SSn instance.

   Name: nSSnParamMemOffset
   Type: uint32_t
   Direction: Input
   Description: Offset from the parameter memory base into which the new parameters need to be updated.

   Name: pBuffer
   Type: uint32_t *
   Direction: Input
   Description: Pointer to memory into which the SS+ parameters are read.

   Name: nNumParams
   Type: uint32_t
   Direction: Input
   Description: Number of parameters that needs to be read.

| 
| Return value
| An appropriate error code of type ADI_SS_RESULT is returned.
