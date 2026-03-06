ADC PGA Calibration
===================

Overview
--------

The AD5940 has a large number of possible current and gain stages to its SAR ADC. The ADC voltage input has 5x PGA gain settings. There are separate Offset and Gain calibration registers for each gain setting. The ADC can work in low power mode from 16MHz clock or in high power mode from 32MHz clock. Self-calibration code was developed so the ADC can self calibrate itself for all configuration without the need for an external precision voltage source. It uses the internal 1.82V reference. The accuracy of the reference is ±5 mV with only 20 ppm/ºC drift. This means it is suitable for self-calibration. The figure below displays the various current and voltage input options for the ADC.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/calibration_routines/adc_circuits.png
   :width: 600px

Calibration Steps
-----------------

The following are the steps involved for calibrating the ADC PGA offset and gain errors:

::

   *Calibrate ADC offset for each PGA gain setting by connecting the 1.11V ADC reference to the P mux and N mux of the ADC. The expected coded is 0x8000. The offset error is expected code - measured code. The ADCOFFSET registers have a resolution of 0.25 bits. 
   *For PGA gain of 1, 1.5 and 2 the gain calibration is done using the internal 1.82V reference. The precision reference is connected to the P mux and the 1.11V ADC reference is connected to the N mux.
   *For PGA gain of 4 and 9 the HSDAC is used to generate a voltage across the external RCAL resistor. The P-Node and N-Node are connected to the ADC mux.

Using the ADC Calibration Function in the SDK
---------------------------------------------

The ADC PGA calibration code is implemented in the AD5940 SDK. The function AD5940_ADCPGACal() is used. It accepts one input argument of type ADCPGACal_Type. The members of this datatype and their function are as follows:

-  SysClkFreq - defines the frequency of the system clock. Should be 16MHz
-  AdcClkFreq - defines the frequency of the ADC clock. Should be 16MHz or 32MHz.
-  Vref1p82 - The voltage of the 1.82 reference. Measured on Vfref1P82 pin
-  Vref1p11 - The actual voltage of 1.11V ADC reference. Measured on VBIAS_CAP pin
-  ADCSinc3Osr - Sinc3 Oversampling rate. Ideally 4.
-  ADCSinc2Osr - Sinc2 Oversampling rate. Should be a big value to remove noise from measurement
-  ADCPga - Selected PGA setting
-  PGACalType - type of calibration. Offset, gain or both.
-  TimeOut10us - Timeout for ADC measurement.

If the PGA needs to be calibrated for a gain of 9 the PGA gain of 1 must be calibrated first. The following is example code to calibrate the PGA offset and gain for all settings:

::

   static AD5940Err AppADCPgaCal(void)
   {
      ADCPGACal_Type pga_cal;
      
      /* Calibrate ADC PGA(offset and gain) */
      pga_cal.AdcClkFreq = AppAMPCfg.AdcClkFreq;
      pga_cal.SysClkFreq = AppAMPCfg.SysClkFreq;
      pga_cal.ADCPga = ADCPGA_1;
      pga_cal.ADCSinc2Osr = ADCSINC2OSR_1333;    /* 800kSPS/4/1333 = 150Hz,  T = 6.67ms*/
      pga_cal.ADCSinc3Osr = ADCSINC3OSR_4;
      pga_cal.TimeOut10us = 10*100;          /* 10ms max */
      pga_cal.VRef1p82 = AppAMPCfg.ADCRefVolt;  
      pga_cal.VRef1p11  = 1.0979f;
      pga_cal.PGACalType = PGACALTYPE_OFFSETGAIN; /* Calibrate Offset and Gain errors */
      AD5940_ADCPGACal(&pga_cal);
      /* Calibrate Offset and Gain for PGA = 1.5 */
      pga_cal.ADCPga = ADCPGA_1P5;
      AD5940_ADCPGACal(&pga_cal);
      /* Calibrate Offset and Gain for PGA = 2 */
      pga_cal.ADCPga = ADCPGA_2;
      AD5940_ADCPGACal(&pga_cal);
      /* Calibrate Offset and Gain for PGA = 4 */
      pga_cal.ADCPga = ADCPGA_4;
      AD5940_ADCPGACal(&pga_cal);
      /* Calibrate Offset and Gain for PGA = 9 */
      pga_cal.ADCPga = ADCPGA_9;
      AD5940_ADCPGACal(&pga_cal);
      return AD5940ERR_OK;
   }
