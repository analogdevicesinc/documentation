| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apifuncs>`
| =====adi_ss_connection_Reconfigure=====
| Prototype

::

    ADI_SS_CONNECTION_RESULT adi_ss_connection_Reconfigure( ADI_SS_CONNECTION_HANDLE hSSConnection, 
                                                            ADI_SS_CONNECTION_CONFIG_ITEM eConfigItem, 
                                                            ADI_SS_CONNECTION_CONFIG *pConnectionConfig 
                                                          )

| 
| Description
| This API reconfigures the connection component based on the chosen config item.
| Parameters
| Name: eConfigItem

::

   Type: ADI_SS_CONNECTION_CONFIG_ITEM
   Direction: Input
   Description: Configuration parameter to be reconfigured.

   Name: pConnectionConfig
   Type: ADI_SS_CONNECTION_CONFIG*
   Direction: Input
   Description: Configuration structure populated by the application.

   Name: hSSConnection
   Type: ADI_SS_CONNECTION_HANDLE 
   Direction: Input
   Description: Handle to the connection component instance.

| 
| Return value
| An error code of type ADI_SS_COMM_RESULT is returned.
| • ADI_SS_COMM_SUCCESS : Communication init successful.
| • ADI_SS_CONNECTION_INVALID_CONFIG : Connection Init failed due to invalid config.
| • ADI_SS_COMM_FAILED : Communication init failed due to general error.
