EVAL-ADPAQ3029 - UART(Arduino) demo
===================================

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   \ `UART (Arduino) Firmware <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/uart.zip>`_

   
   `Tile GUI application <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/moduware.tile.example-uart.zip>`_
   
   `Arduino code <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/Uart.ino.zip>`_\


-  Follow the same steps as given `here <https://wiki.analog.com/../first_app>`_
-  In this project, an Arduino board has been used.

|image1|

-  Upload the ``Arduino code`` into ``Arduino Uno`` board using Arduino IDE.
-  The connections between the Arduino and ADPAQ Board are made as described below.

.. container:: round box

   
   =================== ============== =================
   Arduino Pins        GPIO port used ADPAQ Header Pins
   =================== ============== =================
   Digital pin 10 (RX) UART0_TX       P2-2
   Digital pin 11 (TX) UART0_RX       P2-3
   GND                 GND            P2-10
   =================== ============== =================
   


-  Apart from these connections, an led along with a 10k resistor has to be connected between the Digital pin 12 of Arduino and Ground.

   


|image2|

-  Build and run the project
-  The tile has 2 buttons “On” and “Off” buttons. By clicking on those buttons, we can control the led that is connected to the pin 12 of Arduino. `image <https://wiki.analog.com/resources/eval/user-guides/eval-adpaq3029/tile15.png>`_

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/tile16.png
   :align: center
   :width: 400px

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app11.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app12.png
   :width: 400px
