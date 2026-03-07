| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apifuncs>`
| =====adi_ss_connection_Enable=====
| Prototype

::

   ADI_SS_CONNECTION_RESULT adi_ss_connection_Enable( ADI_SS_CONNECTION_HANDLE hSSConnection )

| 
| Description
| This API to enable the physical connection.
| Parameters

::

    Name: hSSConnection
    Type: ADI_SS_CONNECTION_HANDLE 
    Direction: Input
    Description: Handle to the connection component instance.

| 
| Return value
| An error code of type ADI_SS_COMM_RESULT is returned.
| • ADI_SS_COMM_SUCCESS : Communication init successful.
| • ADI_SS_COMM_FAILED : Communication init failed due to general error.
