Low Power TIA Gain Resistor Calibration
=======================================

Overview
--------

The LPTIA channel has a programmable gain resistor to scale the input current from the SE0 pin to a voltage that the ADC can measure. The programmable Rtia has an initial accuracy range as specified in the AD5940 data sheet. The Rtia also varies with temperature as specified in the AD5940 data sheet. If uncalibrated, an error is present if trying to measure an absolute input current.

Calibration Steps
-----------------

The following are the steps involved for calibrating the LPTIA Gain resistor:

-  Configure the switch matrix as per the diagram below. Vzero is connected to the non-inverting input of the HSTIA. A precision calibration resistor is connected between RCAL0 and RCAL1. RCAL0 is connected to the HSTIA inverting input through DR0. RCAL1 is connected to the LPTIA inverting input via DR0 and D7. A differential voltage is created across RCAL by adjusting VBIAS and VZERO.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/calibration_routines/lprtia_cal.jpg
   :align: center
   :width: 600px

-  The differential voltage generates a precision calibration current that is fed into the LPTIA gain resistor highlighted in red in above diagram.
-  The P_Node and N_Node are connected to the ADC mux to determine the voltage across RCAL and therefore, the calibration current.
-  Then the LPTIA_P and LPTIA_N inputs are connected to the ADC mux and the current is measured.
-  This current reading is compared to the precision calibration current to determine the actual value of the Rtia.
-  This value of Rtia is then saved by the host controller and used for calculating impedance's.

Using the LPTIA Rtia Calibration Function in the SDK
----------------------------------------------------

The AD5940 SDK provides a function to calibrate the LPTIA gain resistor. The function is located in the AD5940.c file. The following is an example code on how to use the function.

::

   static AD5940Err AppLPRtiaCal(void)
   {
      fImpPol_Type RtiaCalValue;  /* Calibration result */
      LPRTIACal_Type lprtia_cal;
      AD5940_StructInit(&lprtia_cal, sizeof(lprtia_cal));
      lprtia_cal.bPolarResult = bTRUE;                /* Magnitude + Phase */
      lprtia_cal.AdcClkFreq = AppAMPCfg.AdcClkFreq;
      lprtia_cal.SysClkFreq = AppAMPCfg.SysClkFreq;
      lprtia_cal.ADCSinc3Osr = ADCSINC3OSR_4;
      lprtia_cal.ADCSinc2Osr = ADCSINC2OSR_22;        /* Use SINC2 data as DFT data source */
      lprtia_cal.DftCfg.DftNum = DFTNUM_2048;       
      lprtia_cal.DftCfg.DftSrc = DFTSRC_SINC2NOTCH;   
      lprtia_cal.DftCfg.HanWinEn = bTRUE;
      lprtia_cal.fFreq = AppAMPCfg.AdcClkFreq/4/22/2048*3;  /* Sample 3 period of signal, 13.317Hz here.
      lprtia_cal.fRcal = AppAMPCfg.RcalVal;
      lprtia_cal.LpTiaRtia = AppAMPCfg.LptiaRtiaSel;
      lprtia_cal.LpAmpPwrMod = LPAMPPWR_NORM;
      lprtia_cal.bWithCtia = bFALSE;
      AD5940_LPRtiaCal(&lprtia_cal, &RtiaCalValue);
      AppAMPCfg.RtiaCalValue = RtiaCalValue;
      printf("Rtia,%f,%f\n", RtiaCalValue.Magnitude, RtiaCalValue.Phase);
      return AD5940ERR_OK;
   }
