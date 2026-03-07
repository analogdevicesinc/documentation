Low Frequency Oscillator Calibration
====================================

Overview
--------

The low frequency oscillator is used to control the sleep/wakeup timer. The sleep/wakeup timer controls the measurement frequency i.e. how often the AD5940 wakes up to run a measurement sequence. Refer to the Sleep/Wakeup Timer chapter in the AD5940 datasheet for further details. For applications requiring a highly accurate measurement sample rate, the sleep/wakeup timer needs to be calibrated. The calibration function uses two measurement sequences. The first sequence starts the timeout counter and second sequence stops the timeout counter and generates an interrupt to the MCU to read back the timeout value. The second sequence is then modified to reset the timer so the length of time required for the MCU to read back the timeout value can be measured. It is important that SPI speed is fast, ideally 16MHz. Slower SPI speeds will reduce calibration accuracy. Also using an external 16MHz crystal will increase calibration accuracy.

Calibration Steps
-----------------

The following are the steps required to calibrate the LFOSC:

-  Configure Sequence A. Sequence A should have one sequencer command that sets the time-out timer - SEQ_TOUT(0x3fffffff)
-  Configure Sequence B. Sequence B should have one sequence command which generates the END_SEQ interrupt- SEQ_STOP(). This interrupt informs the MCU to read current time count from SEQTIMEOUT register.
-  Write the two sequences to SRAM. Sequence A should be written to Sequence ID 0 and Sequence B should be written to Sequence ID 1.
-  Configure the sleep/wakeup timer. The wakeup timer order should be configured to end on sequence B.
-  Enable the wakeup timer. Sequence A runs and starts the timeout timer, After CalDuration time has elapsed sequence B is executed which generates an ENDSEQ interrupt. The host reads timer count register and TimerCount is stored. TimerCount value includes the WuptPeriod plus the time taken to read timer count register.
-  Sequence B is reconfigured to reset the time out counter and then generates END_SEQ interrupt. The host reads back the timeout value to calculate the length of time it takes to read the register, TimerCount2. The WuptPeriod is TimerCount – TimerCount2.
-  The frequency of the low frequency oscillator is calculated using the following equation:

::

        Frequency =  (SystemClkFreq ×WuptPeriod) / (TimerCount2-TimerCount)
        where,
        Frequency = Low Frequency Oscillator Frequency
        SystemClkFreq  = Frequency of AD5940 system clock (Ideally 16MHz using external crystal)
        WuptPeriod = Period of the wakeup timer

Using the LFOSC Function in the SDK
-----------------------------------

The code to carry out the low frequency oscillator calibration is included in the AD5940 SDK. The function AD5940_LFOSCMeasure() is used. The function takes two input parameters. THe fist parameter is a pointer to the data structure LFOSCMeasure_Type that contains the measurement parameters. The second argument is a pointer to a variable that stores the result of the calibration. This structure contains the following paramteres:

-  CalSeqAddr - this sets the start address in SRAM for the first sequence used.
-  CalDuration - this parameter sets the length of the calibration routine. 1000ms is advisable
-  SystemClkFreq - this parameter sets the system clock frequency. It should be 16MHz.

The result of the calibration is then used in the calculation for the period of the sleep/wakeup timer. The sleep/wakeup timer configures the sampling frequency of measurements so after this calibration a high level of accuracy is achieved. For highest accuracy it is best to use a precision 16MHz crystal connected to the AD5940.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/bia_terminal.png
   :align: center
   :width: 400px
