| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apifuncs>`
| =====adi_ss_comm_Packetize=====
| Prototype

::

    ADI_SS_COMM_RESULT adi_ss_comm_Packetize(ADI_SS_COMM_HANDLE hSSComm, 
                                             ADI_SS_COMM_BACKCH_INFO *pBkChInfo, 
                                             uint32_t *pPacketSzInWords
                                            )

| 
| Description
| This API packetizes the back-channel data for transmission..
| Parameters
| Name: pPacketSzInWords

::

   Type: uint32_t
   Direction: Output
   Description: Pointer holding the size of the packet in words.

   Name: pBkChInfo
   Type: ADI_SS_COMM_BACKCH_INFO
   Direction: Input
   Description: Pointer to backchannel information structure.

   Name: hSSComm
   Type: ADI_SS_COMM_HANDLE
   Direction: Output
   Description: Handle to communication component instance
   \\ 

| Return value
| An error code of type ADI_SS_COMM_RESULT is returned.
| • ADI_SS_COMM_SUCCESS : Communication init successful.
| • ADI_SS_COMM_FAILED : Communication init failed due to general error.
