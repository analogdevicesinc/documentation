Where to find the example Code used in CN-0425
==============================================

After you have installed the evaluation software, the example firmware project used in CN-0425 is in the folder \\examples\\M355_RadiatedImmunity_Demo.


|image1|

Build, download and debug the example project to IAR via the Midas-Link:
------------------------------------------------------------------------

|image2|.png?600\|}}

What the M355_RadiatedImmunity_Demo project code does
=====================================================

The Project assumes a 3-lead EC sensor is connected to channel 0 of the LP Potentiostat loop - 0V bias between RE/WE with 1.1V common mode voltage.

The code has 2x modes of operation:
-----------------------------------

::

    Mode 1 (P1.3=1 JP1 2-3) - Sensor Measurements and log to flash
        First code will initialize the LPDAC, LP potentiostat/LPTIA amplifiers and associated sensors to bias the sensor.
        Next, it will calibrate the ADC offset error and calibrate the LPTIA0 channel gain error.
        Then it will enter normal EC sensor measurement mode  
        Once a second, ADC samples EC channel 0 - 10 samples taken @ 160KSPS, results averaged and sent to Flash page
           For debug purposes, results sent to the UART also
           UART Baud rate is 57600-N-8
           Maximum number of logs is 30720 (roughly 8x Hours)
           AFE Timer 0 used with a 1 second timeout to trigger samples and UART comms.
           A debug string is sent to the UART reporting the measured voltage (V), the calculated current (uA ) and ppm of gas (80nA/ppm assumed)
      
        ADC results are accumulated in 2x SRAM arrays. When either Array is full, it is moved into flash.

::

      Mode 2 (P1.3=0 JP1 2-1) - Read log from flash to UART
                Will read from flash location 0x10000 until 0xFFFF detected
                Values stored to flash are the averaged ADC codes
                Wait several seconds for the results to be transmitted - allowance for sensor to settle first
                

Mode 1 - output to UART debug terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In mode 1, debug text is sent periodically to the UART. When viewed in a terminal window like Realterm, it looks like this:


|image3|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_aducm355emcz/example_pathw.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_aducm355emcz/iar_debug1.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_aducm355emcz/capturemode.png
   :width: 600px
