| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apidatastructures>`
| =====ADI_SS_CONNECTION_CONFIG=====
| Structure
| typedef struct ADI_SS_CONNECTION_CONFIG {

::

                                             /* One time configurable items */ 
                                             ADI_SS_CONNECTION_TYPE eConnectionType; 
                                             uint32_t nDevId; 
                                             ADI_SS_PROC_ID eProcID; 
                                             CONN_ISR pfISRRx; 
                                             CONN_ISR pfISRTx; 
                                             /* Reconfigurable items */ 
                                             uint32_t *pRxAddr; 
                                             uint32_t nRxPayloadCnt; 
                                             uint32_t *pTxAddr; 
                                             uint32_t nTxPayloadCnt; 
                                            }ADI_SS_CONNECTION_CONFIG;

| 
| Description
| Configuration structure for connection component. This must be populated by the application before calling adi_ss_connection_init()API.
| Fields
| • eConnectionType Type of the physical connection. The supported physical connections are defined by the ADI_SS_CONNECTION_TYPE enumeration
| • nDevId Device number (id) of the physical connection.
| • eProcID Processor ID on which the connection component must execute from.
| • pfISRRx Rx interrupt service routine function pointer. Currently unused.
| • pfISRTx Tx interrupt service routine function pointer. Currently unused.
| • pRxAddr Payload receive address. This pointer is a reconfigurable parameter. It can be reconfigured and used along with adi_ss_connection_Reconfigure() API.
