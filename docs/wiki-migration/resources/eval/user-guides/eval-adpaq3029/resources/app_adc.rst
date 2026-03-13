EVAL-ADPAQ3029 - ADC demo
=========================

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   \ `ADC Firmware <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/adc.zip>`_

   
   `Tile GUI application <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/moduware.tile.example-adc.zip>`_\

-  Follow the same steps as given `here <https://wiki.analog.com/../first_app>`_
-  A potentiometer has been used in this project to modify the analog voltage
   values.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app3.png
   :align: center
   :width: 200

-  The potentiometer has to be interfaced with the ADPAQ module. The connections
   between the potentiometer and the ADPAQ module are described in the table
   below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app4.png
   :align: center
   :width: 300

.. container:: round box

   
   ================== ============== =================
   Potentiometer Pins GPIO port used ADPAQ Header Pins
   ================== ============== =================
   A                  VCC            P1-3.3V
   B                  ADC0_Vin0      P1-ADC0_Vin0
   C                  GND            P1-GND_POWER
   ================== ============== =================
   

-  Build and run the project
-  If the knob of the potentiometer is rotated, the ADC value should vary
   between 0-4095 for the corresponding analog voltage variations from 0 to
   3.3V.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/tile12.png
   :align: center
   :width: 300
