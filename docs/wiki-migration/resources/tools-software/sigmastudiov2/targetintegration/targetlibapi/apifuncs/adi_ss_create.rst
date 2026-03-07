| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apifuncs>`
| =====adi_ss_create=====
| Prototype

::

    ADI_SS_RESULT adi_ss_create( ADI_SS_SSN_HANDLE *phSSn, ADI_SS_MEM_MAP *pMemMap );

| 
| Description
| The function adi_ss_create creates an instance of the SS+ module, with the memory blocks passed to the function, using the memory map structure.
| Parameters
| Name: phSSn

::

   Type: ADI_SS_SSN_HANDLE *
   Direction: Output
   Description: Pointer to the handle of SS+ instance.

   Name: pMemMap
   Type: ADI_SS_MEM_MAP *
   Direction: Input
   Description: Used to pass information regarding the memory blocks that can be used by the SS+ module.

| 
| Return value
| An appropriate error code of type ADI_SS_RESULT is returned.
