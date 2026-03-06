DYNO test procedure
===================

Required hardware
-----------------

-  ZedBoard with mouse and keyboard
-  SD card with ADI Linux image
-  HDMI monitor
-  AD-FMCMOTCON1-EBZ
-  AD-DYNO1-EBZ

Test Procedure
--------------

-  Connect the hardware as shown in this video: `Hardware Connection <https://www.youtube.com/watch?v=eGYjnbYDiWg>`__

-  In the Linux IIO scope go to the// Motor Control// tab and select the following configuration:

   -  **Delta**: ON
   -  **Direction**: Clockwise
   -  **Sensors**: hall
   -  **Controller type**: Manual PWM
   -  **PWM**: 90.96%

-  Set **Run** to ON

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/s1.png
   :alt: Motor Control Tab
   :width: 400px

-  Make sure that there are no vibrations in the DYNO system.

-  On the DYNO board open the *Measurements* menu
-  Check the speed & current displayed under *Measurements* on the DYNO LCD to see if it reads 5300rpm +/- 250rpm for speed and 0.3A for current

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/s2.png
   :alt: Motor Control Tab
   :width: 200px

-  Set the load to 100%
-  Check the speed & current displayed under *Measurements* on the DYNO LCD to see if it reads 3900rpm +/- 250rpm for speed and 1.5A +/- 0.1A for current

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/s3.png
   :alt: Motor Control Tab
   :width: 200px
