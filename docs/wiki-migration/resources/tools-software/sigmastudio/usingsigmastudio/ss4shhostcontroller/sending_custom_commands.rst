`Click here to return to 'SigmaStudio for SHARC Host Controller' page. <https://wiki.analog.com/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller>`__

Sending Custom Commands
=======================

| Custom commands can be sent from the SigmaStudio Host to the SHARC Target in 2 different ways; using SS_CMD_CMD4 and SS_CMD_CMD5.
| =====Call-back Method===== A packet sent to the SHARC Target with SS_CMD_CMD4 as the command executes a call-back function with the payload information as the function arguments. The call-back function to be executed can be assigned through the configuration parameter pfCommCallBack in the communication configuration structure ADI_SS_COMM_CONFIG passed to adi_ss_comm_init().
| ``/* Parameters for SigmaStudio communication instance initialization */
  oCommConfig.baudRateTx = 0x100; /* currently not used */
  oCommConfig.nSelectSPI = SELECT_SPI0; /* SELECT_SPI0 : Primary SPI */
  oCommConfig.bCRCBypass = 0; /* Bypass CRC check */
  oCommConfig.pfCommCallBack = app_ss_comm_callback_cmd4;
  /* SigmaStudio for SHARC communication instance initialization */
  eCommResult = adi_ss_comm_init(hSSComm, &oCommConfig);
  Prototype of the call-back function is shown below.
  void app_ss_comm_callback_cmd4(int *pCommPayloadBuff,
  int nPayloadCount,
  ADI_SS_SSN_HANDLE hSSn)
  {
  .................
  .................
  .................
  }``
| <fc #6495ed>\ *Parameters*\ </fc>
| <fc #cd5c5c>\ *Name*\ </fc>:pCommPayloadBuff
| <fc #cd5c5c>\ *Type*\ </fc>:Int \*
| <fc #cd5c5c>\ *Direction*\ </fc>:Input
| <fc #cd5c5c>\ *Description*\ </fc>:Payload buffer pointer.
| <fc #cd5c5c>\ *Name*\ </fc>:nPayloadCount
| <fc #cd5c5c>\ *Type*\ </fc>:int
| <fc #cd5c5c>\ *Direction*\ </fc>:Input
| <fc #cd5c5c>\ *Description*\ </fc>:Size of the payload.
| <fc #cd5c5c>\ *Name*\ </fc>:hSSn
| <fc #cd5c5c>\ *Type*\ </fc>:adi_ss_sample_t \*
| <fc #cd5c5c>\ *Direction*\ </fc>:Input
| <fc #cd5c5c>\ *Description*\ </fc>:Handle to the SigmaStudio module instance which received the command.
| =====Get Properties Method===== A packet sent to the SHARC Target with SS_CMD_CMD5 as the command is received by the SigmaStudio instance on the SHARC Target. The received data/command is extracted by the Application from the SigmaStudio instance using the adi_ss_comm_GetProperties()function. Data is available in oGetProperties.pSSnBuf, where oGetProperties is the properties structure of type ADI_SS_COMM_PROPERTIES passed to adi_ss_comm_GetProperties().
| ``adi_ss_comm_GetProperties(hCommHandle, &oGetSSCommProp);;
  if(oGetSSCommProp.bCustomCmdRcvd)
  {
  /* data is available in oGetSSCommProp.pSSnBuf */
  oGetSSCommProp.bCustomCmdRcvd = false;
  }``
| =====Custom Command Example=====

Reset Communication Instance from SigmaStudio Host
--------------------------------------------------

| The custom command SS_CMD_CMD4 can be used to reset the communication instance from an error state. This is required to continue processing after encountering a communication error. The below code snippet shows how to trigger a communication reset from the SigmaStudio Host with the help of a call-back function.
| ``ADI_SS_COMM_HANDLE hSSComm = 0;
  ADI_SS_COMM_CONFIG oCommConfig;

  void app_ss_comm_callback_cmd4(int               *pCommPayloadBuff, 
                                 int                nPayloadCount, 
                                 ADI_SS_SSN_HANDLE  hSSn)
  {
        int payLoadHdr = pCommPayloadBuff[0];

      switch(payLoadHdr)
      {
            /* SigmaStudio Host should send cmd4 with payload as 2 to reset the comm */   
            case 2: 
          if(hSSComm != NULL)
          {
                adi_ss_comm_Reset (hSSComm, &oCommConfig);
          }
          break;          
      }
  }``
