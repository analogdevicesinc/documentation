EVAL-ADPAQ3029 - SHT20 [I2C] demo
=================================

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   \ `SHT20 Firmware <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/sht20.zip>`__

   
   `Tile GUI application <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/moduware.tile.example-i2c.zip>`__\


-  Follow the same steps as given `here <https://wiki.analog.com/../first_app>`__
-  In this project, SHT20 (Temperature and Humidity Sensor) is used.\

|image1|

-  The connections between the SHT20 and the ADPAQ module are made as described below.\

|image2|

.. container:: round box

   
   ========== ============== =================
   SHT20 Pins GPIO port used ADPAQ Header Pins
   ========== ============== =================
   Vcc        3.3V           P1-1
   SCL        I2C_SCL        P2-9
   SDA        I2C_SDA        P2-8
   Gnd        GND            P1-10
   ========== ============== =================
   


-  Build and run the project
-  The Sensor will give the Temperature value in ``degree celsius`` and Humidity in ``%RH``.\ `image <https://wiki.analog.com/resources/eval/user-guides/eval-adpaq3029/tile11.png>`__

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/tile12.png
   :align: center
   :width: 400px

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app7.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app8.png
   :width: 200px
