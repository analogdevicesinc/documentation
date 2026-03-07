| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apifuncs>`
| =====adi_ss_comm_SetProperties=====
| Prototype

::

    ADI_SS_COMM_RESULT adi_ss_comm_SetProperties(ADI_SS_COMM_HANDLE hSSComm, 
                                                 ADI_COMM_PROPERTY_ID ePropId, 
                                                 ADI_SS_COMM_PROPERTIES *pCommProperties 
                                                 )

| 
| Description
| API for Setting communication properties.
| Parameters
| Name: pCommProperties

::

   Type: ADI_SS_COMM_PROPERTIES
   Direction: Input
   Description: Pointer to structure of type ADI_SS_COMM_PROPERTIES. The fields of this structure is updated by the 
                communication component.

   Name: ePropId
   Type: ADI_SS_PROPERTY_ID
   Direction: Input
   Description: Enumeration for Setting communication properties.

   Name: hSSComm
   Type: ADI_SS_COMM_HANDLE
   Direction: Input
   Description: Handle to communication component instance.

| 
| Return value
| An error code of type ADI_SS_COMM_RESULT is returned.
| • ADI_SS_COMM_SUCCESS : Communication init successful.
| • ADI_SS_COMM_FAILED : Communication init failed due to general error.
