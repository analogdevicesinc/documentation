**====== DC2847A-KIT ====== ====== EVAL-ADL5920-ARDZ ====== ADL5920 Linduino Shield**

**DESCRIPTION**

Demonstration kit DC2847A(EVAL-ADL5920-ARDZ) is a dual RMS power detector with integrated directional bridge featuring the ADL5920 IC. The ADL5920 arudino shield enables the evaluation of the device with the Linduino board. Together with the GUI, forward, reverse power can be measured and monitored on PC. Return Loss is calculated and displayed. The ADL5920 with integrated bridge simultaneously measure forward power and reverse RMS power up to 7GHz, and provides return loss results. The detector has 50dB of dynamic range at 1GHz. The demo board requires external power supply that connects to the Linduino board, by setting JP1.

**Test Setup, Figure 1**

.. image:: https://wiki.analog.com/_media/resources/eval/figure1.jpg
   :width: 600px

**QUICK START PROCEDURE**

-  Remove the DC2847A from its protective packaging in an ESD-safe working area (see Figure 1).
-  Connect external wall wart power supply to J2 on Linduino board DC2026C. with AC/DC 9V, 1500mA adaptor for Arduino boards or equivalent. Set JP1.
-  Connect USB cable to PC and J5 on Linduino board.
-  Connect signal generator to RF_IN(J1) on the ADL5920 shield.
-  Connect RF load to RF_OUT.
-  Turn on signal generator, set frequency between 9KHz and 7 GHz. Set RF power below 30dBm.
-  Go to www.analog.com and download and install quikeval.
-  Open quikeval, set frequency, click “READ” to measure forward and reverse RMS power using default calibration. See Figure 2.
-  User calibration can be performed to improve accuracy. Click “Calibrate” to calibrate the device across frequency. Linear interpolation is used to calculate the slope and intercept for frequencies between the calibration points. The calibration coefficients are stored in the GUI that can be re-used later. See figure 3.

**GUI, Figure 2**

.. image:: https://wiki.analog.com/_media/resources/eval/figure2.jpg
   :width: 600px

**Calibration, Figure 3**

.. image:: https://wiki.analog.com/_media/resources/eval/figure3.jpg
   :width: 600px

**DEMO BOARD USAGE NOTES**

-  C3 and C4 are highpass capacitors for internal offset compensation loop, they are necessary for low frequency operation. They are removed for 2Ghz and above for improved directivity.
-  Return loss=(Pforward-Preverse)-insertion loss with passive load.
-  Default calibration use the typical slope and intercept value which introduce error due to part to part variations. The calibration function uses 3-point calibration which makes the power measurement highly accurate.
-  Demo kit comes with Linduino board which is pre-loaded with the firmware that is required for the ADL5920 shield kit. Contact factory for missing firmware

**Schematic** `sch_dc2847a-1_adl5920.pdf <https://wiki.analog.com/_media/resources/eval/sch_dc2847a-1_adl5920.pdf>`_
