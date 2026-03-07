| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apifuncs>`
| =====adi_ss_comm_Parse=====
| Prototype

::

    ADI_SS_COMM_RESULT adi_ss_comm_Parse(ADI_SS_COMM_HANDLE hSSComm, 
                                         uint32_t nData 
                                        )

| 
| Description
| This function calls the library parse function to parse a single word from the host.
| Parameters
| Name: nData

::

   Type: uint32_t
   Direction: Input
   Description: 32bit received word

   Name: hSSComm
   Type: ADI_SS_COMM_HANDLE
   Direction: Input
   Description: Handle to communication component instance.

| 
| Return value
| An error code of type ADI_SS_COMM_RESULT is returned.
| • ADI_SS_COMM_SUCCESS : Communication init successful.
| • ADI_SS_COMM_FAILED : Communication init failed due to general error.
