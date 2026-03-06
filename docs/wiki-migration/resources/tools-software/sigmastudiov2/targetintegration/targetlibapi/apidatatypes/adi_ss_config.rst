| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apidatatypes>`
| =====ADI_SS_CONFIG=====
| Structure

::

   typedef struct __SSnConfig { uint32_t nBlockSize; 
                                uint32_t nInChannels; 
                                uint32_t nOutChannels; 
                                uint32_t bSkipProcessOnCRCError; 
                                uint32_t bSkipInitialDownload; 
                                ADI_SS_COMM_HANDLE hSSComm; 
                                #if defined(__ADSP2158x__) 
                                  uint32_t nInitNoWait; 
                                  bool bClearUnusedOutput; 
                                #endif 
                              } ADI_SS_CONFIG;

| 
| Description
| The structure ADI_SS_CONFIG is used by the Application to configure the SS+.
| Fields
| • nBlockSize Size of the input sample block passed to the SS+ for processing. This is equal to the Application Block Size and is expressed in samples per channel.
| • nInChannels Indicates the number of input audio buffer passed to the SS+.
| • nOutChannels Indicates the number of output audio data received from the SS+.
| • bSkipProcessOnCRCError Indicates whether to skip further processing of audio upon encountering a CRC or packet error. 1 indicates skip and 0 indicates continue audio processing.
| • bSkipInitialDownload Set this to 1 if the code and parameters are not downloaded from the SigmaStudio Host through the communication channel. If this field is not set to ‘1’, the SS+ instance internally skips the process stage until the code and parameter are received through the communication channel.
| • hSSComm Handle to SigmaStudio communication instance.
| • nInitNoWait Flag indicating whether the adi_ss_Init() API needs to wait for the SS+ code and parameters to be received or not.
| • bClearUnusedOutput Boolean flag indicating whether the unused output channels need to be cleared or not.
