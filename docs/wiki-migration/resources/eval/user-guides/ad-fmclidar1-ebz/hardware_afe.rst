AFE Board Hardware Overview
===========================

|image1| |image2|

The AFE board receives the optical reflected signal, converts it to an electrical signal and transfers it to the ADC on the DAQ board. The optical signal is converted using a 16 channel `APD array from First Sensor <https://www.first-sensor.com/en/products/optical-sensors/detectors/avalanche-photodiode-arrays-apd-arrays/>`_. The 16 current outputs are fed to four :adi:`LTC6561 <en/products/ltc6561.html>`, low-noise four-channel, transimpedance amplifiers (TIA)with 220MHz bandwidth. They feature 74kΩ transimpedance gain and 30µA linear input current range. The measurement range can be increased from 30µA to at least 3mA. However, in saturation the pulse width widens (in a predictable manner). An internal 4-to-1 MUX is used to select the output channel. The output voltage is single-ended and swings 2Vpp.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/AD-FMCLIDAR1-EBZ/AFE Board.png
   :alt: AFE Block Diagram
   :align: left
   :width: 500px

The single-ended output is converted to a differential voltage using an :adi:`ADA4950 <en/products/ada4950-1.html>`. The differential gain is set to 1 and the appropriate common mode voltage Vcm is applied. In case there is no signal at the input, the output differential voltage should be zero, otherwise there would be excessive current at the ADA4950 output. The no signal differential voltage is reduced using a negative feedback circuit featuring the :adi:`LT6016 <en/products/lt6016.html>` rail-to-rail input operational amplifiers and the :adi:`ADR3525 <en/products/adr3525.html>`, a low power, high precision CMOS voltage reference. Also, a programmable voltage at the inverting inputs of the ADA4950 ICs contributes to the proper functioning of this negative feedback circuit. The Vcm is set by using the dedicated common mode voltage pins on the ADA4950 and the AD9094 on the DAQ board, respectively. The :adi:`LT8331 <en/products/lt8331.html>` is used to generate the bias voltage for the APD, which is programmable between -120V and -300V. Additionally, the APD temperature is measured, which enables the adjustment of the bias voltage for maximum APD SNR regardless of temperature. The APD bias voltage can be set according to the following formula:

:math:`\displaystyle N = \frac{(-122V-Vbias) \times 4096}{5V \times 18.18},` where N is the DAC code and Vbias is the desired APD bias voltage in volts. If N = 0, Vbias is around -122V.

At the single ended output, the resting voltage is approximately 1.0V. Loaded with 100Ω or higher load, the output can swing to 3V. This is equivalent to a 2VP-P swing. However, in case there is low frequency noise at the input current, the resting voltage is no longer a constant of approximately 1.0V. In order to mitigate this problem, a negative feedback circuit is used. The loop bandwidth must be low such that it doesn’t affect the useful narrow signal pulses received from the APD.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmclidar1-ebz/lidar_tia_signal_chain.jpg
   :alt: AFE board signal chain
   :align: center
   :width: 600px

The TIA output is fed to the ADA4950, a buffer which converts the signal from single-ended to differential. The differential gain is 1 and the output common mode voltage is set to about 1.4V via an input. The buffer inverting input *Vtilt*, which is programmable, must be set equal to *Vrest*, otherwise the difference between the two will be repeated at the output as a differential voltage. *Vtilt* can be set using the following formula:

:math:`\displaystyle N = \frac{Vtilt \times 4096}{5V},` where N is the DAC code and *Vtilt* is the desired tilt voltage in volts. For *Vtilt* = 1V, N = 819.

--------------

.. admonition:: Download
   :class: download

   `Rev B Design Files(Schematics, Layout, BOM) <https://wiki.analog.com/_media/resources/eval/user-guides/AD-FMCLIDAR1-EBZ/revb_afe.zip>`_


--------------

.. image:: https://wiki.analog.com/_media/navigation AD-FMCLIDAR1-EBZ#none#./
   :alt: Overview#none#

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/AD-FMCLIDAR1-EBZ/AFE top pic.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/AD-FMCLIDAR1-EBZ/AFE bot pic.jpg
   :width: 300px
