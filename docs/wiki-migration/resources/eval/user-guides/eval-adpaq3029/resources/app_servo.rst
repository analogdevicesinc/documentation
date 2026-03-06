EVAL-ADPAQ3029 - Servo motor demo
=================================

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   \ `Servo motor Firmware <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/servo.zip>`__

   
   `Tile GUI application <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/moduware.tile.example-servo.zip>`__\


-  Follow the same steps as given `here <https://wiki.analog.com/../first_app>`__
-  In this project, a Servo motor is used.

|image1|

-  The connections between the Servo Motor and the ADPAQ module are made as shown below.

|image2|

.. container:: round box

   
   ================ ============== =================
   Servo motor Pins GPIO port used ADPAQ Header Pins
   ================ ============== =================
   A                5V             P2-1
   B                P0_1           P2-5
   C                GND            P2-10
   ================ ============== =================
   


-  Build and run the project
-  The tile has a “Freq” button and an input value option. We can set the frequency of the servo any value between 0-100 and the servo motor rotates accordingly.\ `image <https://wiki.analog.com/resources/eval/user-guides/eval-adpaq3029/tile13.png>`__

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/tile14.png
   :align: center
   :width: 400px

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app9.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app10.png
   :width: 300px
