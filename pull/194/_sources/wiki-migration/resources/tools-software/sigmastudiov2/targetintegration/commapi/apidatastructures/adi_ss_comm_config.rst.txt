| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apidatastructures>`
| =====ADI_SS_COMM_CONFIG=====
| Structure
| typedef struct ADI_SS_COMM_CONFIG { bool bCRCBypass;

::

                                        bool bFullPacketCRC; 
                                        ADI_SS_COMM_CMD4_CB pfCommCmd4CallBack; 
                                        ADI_SS_COMM_APP_ISR_CB pfSPIRxIsrCallBack; 
                                        ADI_SS_COMM_APP_ISR_CB pfSPITxIsrCallBack; 
                                        ADI_SS_COMM_SMAP_CB pfCommSMAPCallBack; 
                                        void* hConnectionHandle; 
                                        ADI_SS_MEM_SMAP *pMemSMap[MAX_NUMBER_OF_PROCESSORS]; 
                                        ADI_SS_BACKCH_INFO *pBkChnlInfo[MAX_NUMBER_OF_PROCESSORS]; 
                                       }ADI_SS_COMM_CONFIG;

| 
| Description
| The communication component configuration structure to be populated by the application.
| Fields
| • bCRCBypass A boolean flag to indicate bypassing of CRC check.
| • bFullPacketCRC A boolean flag to indicate whether CRC check is required for the entire packet.
| • pfCommCmd4CallBack Command 4 callback function pointer.
| • pfSPIRxIsrCallBack ISR callback for Rx. The callback won’t be registered if this is NULL.
| • pfSPITxIsrCallBack ISR callback for Tx. The callback won’t be registered if this is NULL.
| • pfCommSMAPCallBack Application callback on receiving SMAP.
| • hConnectionHandle Handle to connection component.
| • pMemSMap SMAP pointers for each of the cores.
| • pBkChnlInfo Pointers to Backchannel info structure for each of the cores.
