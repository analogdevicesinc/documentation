EVAL-ADPAQ3029 - HC-SR04 demo
=============================

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   \ `HC-SR04 Firmware <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/hc-sr04.zip>`_

   
   `Tile GUI application <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/moduware.tile.example-hcsr04.zip>`_\


-  Follow the same steps as given `here <https://wiki.analog.com/../first_app>`_
-  In this project, an Ultrasonic Sensor – HC-SR04 has been used.\

|image1|

-  The connections between the Ultrasonic Sensor and ADPAQ module are made as described in the table below.\

|image2|

.. container:: round box

   
   ============ ============== =================
   HC-SR04 Pins GPIO port used ADPAQ Header Pins
   ============ ============== =================
   Vcc          3.3V           P1-3.3V
   Trig         P0_0           P2-5
   Echo         P2_1           P3-1
   Gnd          GND            P1-GND_POWER
   ============ ============== =================
   


-  Build and run the project
-  The Ultrasonic Sensor measurement is displayed on tile in “cm”.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/tile10.png
   :align: center
   :width: 400px

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app5.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app6.png
   :width: 400px
