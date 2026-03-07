| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apidatastructures>`
| =====ADI_SS_COMM_BACKCH_INFO=====
| Structure
| typedef struct ADI_SS_COMM_BACKCH_INFO { uint32_t nProc;

::

                                             uint32_t nCommandName; 
                                             uint32_t *pInData; 
                                             uint32_t nInDataSize; 
                                             uint32_t *pOutPacket; 
                                            }ADI_SS_COMM_BACKCH_INFO;

| 
| Description
| Backchannel information structure which needs to be populated by the function which calls adi_ss_comm_Packetize().
| Fields
| • nProc Processor ID for which this back channel data belongs. This field is currently ignored.
| • nCommandName Back channel command.
| • pInData Pointer to payload data which needs to be sent back to the host (backchannel data).
| • nInDataSize Size of the back channel payload data in words.
| • pOutPacket Pointer to back channel packet which should be transmitted.
