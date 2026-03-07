| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apifuncs>`
| =====adi_ss_updateParam=====
| Prototype

::

    ADI_SS_RESULT adi_ss_updateParam(ADI_SS_SSN_HANDLE hSSn, 
                                     uint32_t *pParamDataAddr, 
                                     uint32_t nSSnParamMemOffset, 
                                     uint32_t nNumParams);

| 
| Description
| This function is used to update a single or a set SS+ parameters into the SS+ parameter memory space.
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

   Name: pParamDataAddr
   Type: uint32_t *
   Direction: Input
   Description: Pointer to memory holding the new parameter values.

   Name: nNumParams
   Type: uint32_t
   Direction: Input
   Description: Number of parameters that needs to be updated.

| 
| Return value
| An appropriate error code of type ADI_SS_RESULT is returned.
