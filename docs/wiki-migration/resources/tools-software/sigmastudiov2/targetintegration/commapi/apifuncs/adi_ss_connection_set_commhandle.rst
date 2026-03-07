| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apifuncs>`
| =====adi_ss_connection_set_CommHandle=====
| Prototype

::

    ADI_SS_CONNECTION_RESULT adi_ss_connection_set_CommHandle( ADI_SS_CONNECTION_HANDLE hSSConnection, 
                                                               ADI_SS_COMM_HANDLE hSSComm 
                                                             )

| 
| Description
| This API provides the communication handle to the connection component.
| Parameters
| Name: hSSComm

::

   Type: ADI_SS_COMM_HANDLE
   Direction: Input
   Description: Handle to the communication component which is to be passed to the connection component.
    
   Name: hSSConnection
   Type: ADI_SS_CONNECTION_HANDLE 
   Direction: Input
   Description: Handle to the connection component instance.

| 
| Return value
| An error code of type ADI_SS_COMM_RESULT is returned.
| • ADI_SS_COMM_SUCCESS : Communication init successful.
| • ADI_SS_COMM_FAILED : Communication init failed due to general error.
