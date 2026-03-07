HSDAC Calibration
=================

Overview
--------

The high speed DAC is not calibrated during production testing. This section describes the steps to calibrate the offset errors on the high speed DAC for all gain settings and in both high power and low power modes. The high speed DAC should be calibrated if it is intended to generate a precision excitation signal to a sensor. If an offset error exists on the excitation signal, and a current or voltage output is to be measured, the excitation signal may exceed the headroom of the selected TIA or ADC input buffer/PGA setting.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/calibration_routines/ad5940_hsdaccal.jpg
   :width: 600px

HSDAC Output Configurations
---------------------------

The HSDAC signal chain has Programmable Gain Amplifier and and Excitation Buffer with a programmable gain. The HSDAC also has 2 power modes and various calibration registers that correspond to selected gain and power mode setting. These settings are summarized in below table.

+--------------+-------------+--------------+----------------+------------------+---------+
| HSDACCON[12] | HSDACCON[0] | Output Range | Low Power Mode | High Power Mode  | Gain    |
+==============+=============+==============+================+==================+=========+
| 0            | 0           | ±607mV       | DACOFFSET      | DACOFFSETHP      | DACGAIN |
+--------------+-------------+--------------+----------------+------------------+---------+
| 1            | 0           | ±75mV        | DACOFFSET      | DACOFFSETHP      | DACGAIN |
+--------------+-------------+--------------+----------------+------------------+---------+
| 1            | 1           | ±15.14mV     | DACOFFSETATTEN | DACOFFSETATTENHP | DACGAIN |
+--------------+-------------+--------------+----------------+------------------+---------+
| 0            | 1           | ±121.2mV     | DACOFFSETATTEN | DACOFFSETATTENHP | DACGAIN |
+--------------+-------------+--------------+----------------+------------------+---------+

For each of the settings shown in the above table a seperate calibration sequence is required. For example if the DAC offset is calibrated in low power mode, if the DAC's power mode is changed to high power mode, the calibration will need to be redone writing to the relevant High Power Mode calibration register Note, the gain errors associated with the HSDAC are negligible and have not been calibrated in the HSDACCAL function provided in the SDK

Calibration Steps
-----------------

The HSDAC is a differential output DAC that swings on the voltage applied to the N terminal of the Excitation Amplifier which is connected to RCAL1 pin shown in the figure above. To calibrate the offset, the HSDAC is configured to midscale (0x800) which means there should be 0V voltage drop across RCAL. The P node and N node are connected to the ADC mux and the actual voltage across RCAL is measured. This measured voltage is the offset error. The relevant DACOFFSET register is written to to remove this error. It is important to ensure the offset error is calibrated out for the chosen HSDAC output range and power mode. The following are the steps involved for calibrating the HSDAC offset errors for all settings:

-  Calibrate the offset and gain errors on the ADC PGA for a gain of 1.
-  Calibrate the offset error on the ±607mV range firstly with the ADC PGA gain of 1.
-  Calibrate the ADC with a selected gain of 4. For the smaller DAC ranges the PGA is required on the ADC to amplify the

::

     signal
   * Calibrate remaining DAC ranges, ±121.2mV, ±75mV and 15.14mV.

Using the HSDAC Calibration Function in the AD5940 SDK
------------------------------------------------------

The AD5940 SDK contains an example project that demonstrates how to the use the HSDACCal function. The relevant project is AD5940_HSDACCal. The below function is an example on how to calibrate the HSDAC for ±607mV range.

::

   static AD5940Err AppHSDACCal(void)
   {
       HSDACCal_Type hsdac_cal;
       
       hsdac_cal.ExcitBufGain = EXCITBUFGAIN_2;  /**< Select from  EXCITBUFGAIN_2, EXCITBUFGAIN_0P25 */ 
       hsdac_cal.HsDacGain = HSDACGAIN_1;                /**< Select from  HSDACGAIN_1, HSDACGAIN_0P2 */ 
       hsdac_cal.AfePwrMode = AFEPWR_LP;
       hsdac_cal.ADCSinc2Osr = ADCSINC2OSR_1333;
       hsdac_cal.ADCSinc3Osr = ADCSINC3OSR_4;
       AD5940_HSDACCal(&hsdac_cal);
   }
