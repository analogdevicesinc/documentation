Brushless DC Motor Control
==========================

Brushless DC motors windings generate a trapezoidal back EMF synchronized to the position of the rotor magnet. Hall effect sensors are used to detect the rotor magnet position and provide signals indicating the “flat top” portion for each winding’s back EMF.

**Star Connection Control**

-  For any one segment, two windings will be in the “flat top” portion of the back EMF and a third winding will be switching between a positive and negative output.
-  Electronic control leaves one winding open circuit, connects one winding to the lower dc rail, and controls the voltage applied to the third winding using PWM.
-  The fill factor of the applied PWM controls the speed of the motor.

|image1| |image2|

**Delta Connection Control**

-  For any one segment, two windings are connected to the positive voltage supply and a third winding is connected to the negative voltage supply.
-  The fill factor of the applied PWM controls the speed of the motor.

|image3| |image4|

**Sensorless control** can be achieved by detecting the zero crossings of the BEMF for each phase. *Benefits*: lower system cost, increased reliability. *Drawbacks*: BEMF zero crossings can’t be reliably detected at low motor speeds

.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#dc_control
   :alt: Brushed DC Motor Control#..:\|Overview#none

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/introduction/bldc_star.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/introduction/bldc_star_switching.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/introduction/bldc_delta.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/introduction/bldc_delta_switching.png
   :width: 300px
