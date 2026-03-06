Low Power TIA Offset Calibration
================================

Overview
--------

The LPTIA channel has dedicated Offset and Gain calibration registers to remove any errors. The following sections describe the calibration method and gives an example on how to calibrate the errors using the AD5940 SDK.

Calibration Steps
-----------------

The following are the steps involved for calibrating the LPTIA offset error:

-  Disconnect any sensor attached so that there is no current flowing into SE0.
-  Connect LPTIA_P and LPTIA_N inputs to the ADC mux.
-  Configure the power mode of the LPTIA amplifier. The offset error will vary depending on power mode selected.
-  Take a measurement using the ADC. Since there is no current flowing into the TIA the measured ADC value should be zero or ADC code of 0x8000.
-  Adjust the ADCOFFSETLPTIA0 register based on result.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/calibration_routines/lptia_offset.jpg
   :align: center
   :width: 600px

Using the LPTIA Rtia Calibration Function in the SDK
----------------------------------------------------

The AD5940 SDK provides a function to calibrate the LPTIA offset error. The function is located in the AD5940.c file. The following is an example code on how to use the function.

::

   static AD5940Err AppLPTIAOffsetCal(void)
   {
      AD5940Err error = AD5940ERR_OK;
      LPTIAOffsetCal_Type lptiaoffset_cal;
      uint32_t lpdac6bit, lpdac12bit;
      /* LP Loop  */
      lpdac6bit = (uint32_t)((AppAMPCfg.Vzero-200)/DAC6BITVOLT_1LSB)+1;
      if(lpdac6bit > 0x3f)lpdac12bit = 0x3f;
      lpdac12bit = (uint32_t)(lpdac6bit * 64 + AppAMPCfg.SensorBias/DAC12BITVOLT_1LSB);
      if(lpdac12bit > 0xfff)lpdac12bit = 0xfff;
      if(lpdac12bit < (lpdac6bit * 64))
         lpdac12bit --;
      /* calibration LPTIA offset */
      lptiaoffset_cal.AdcClkFreq = 16e6;
      lptiaoffset_cal.SysClkFreq = 16e6;
      lptiaoffset_cal.ADCSinc2Osr = ADCSINC2OSR_1333;
      lptiaoffset_cal.ADCSinc3Osr = ADCSINC3OSR_4;
      lptiaoffset_cal.ADCPga = AppAMPCfg.ADCPgaGain;
      lptiaoffset_cal.DacData6Bit = lpdac6bit;
      lptiaoffset_cal.DacData12Bit = lpdac12bit;
      lptiaoffset_cal.LpDacVzeroMux = LPDACVZERO_6BIT;
      lptiaoffset_cal.LpAmpPwrMod = AppAMPCfg.LpAmpPwrMod;
      lptiaoffset_cal.LpTiaRtia = AppAMPCfg.LpTiaRtia;
      lptiaoffset_cal.LpTiaSW = LPTIASW(13)|LPTIASW(12)|LPTIASW(8)|LPTIASW(5);  
      lptiaoffset_cal.SettleTime10us = 5000*100;        /* 1000ms, the time needed for RTIA//CTIA settlling. */
      lptiaoffset_cal.TimeOut10us = 10*100;     /* 10ms. */
      error = AD5940_LPTIAOffsetCal(&lptiaoffset_cal);
      if(error != AD5940ERR_OK)
     {
         printf("ERR: LPTIA Offset calibration error! %d\n", error);
         return error;
     }
      return AD5940ERR_OK;
   }
