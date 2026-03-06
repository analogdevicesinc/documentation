Hardware Setup Guide
====================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/mc2_system.jpg
   :width: 600px

Supported Carriers
------------------

-  `ZedBoard <http://zedboard.org/product/zedboard>`__

+---+
+---+

Required Hardware
-----------------

-  :doc:`AD-FMCMOTCON2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon2-ebz/hardware/controller_board>` - Controller board
-  :doc:`AD-DRVLV2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon2-ebz/hardware/lv_board>` - Low voltage drive board
-  :doc:`AD-DYNO2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon2-ebz/hardware/dyno>` - Dynamo-meter Drive System (Optional)
-  `ZedBoard <http://zedboard.org/product/zedboard>`__
-  12V - 48V capable DC power supply

+---+
+---+

Getting Started
---------------

-  Connect the hardware as shown in the picture below

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/test/connections.jpg
   :alt: connections
   :width: 600px

-  Make sure the **Emergency Stop** switch is pressed (more information about drive board buttons :doc:`here </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/lv_board>`)
-  Insert the DYNO sensor wire in the P3 connector on the controller board with the black wire towards the ZedBoad. In case an encoder is used there is a one to one correspondence of the encoder's pins to the pins of the P3 connector.
-  Insert the DYNO motor wire in the P2 connector on the Drive Board
-  Connect the power supply to the P1 connector and, if a second motor is used also on the P3 connector
-  Make sure the following LEDs are ON:

   -  DS1, DS2, DS3 and DS4 on the Controller Board
   -  DS1 and DS2 on the Drive Board

-  Insert the 5V supply in the left side of the DYNO
-  Power on the ZedBoard
-  After the ZedBoard is programmed, in order to start the motor, the **Emergency Stop** switch must be released and then the **Reset** switch must be pressed for a few seconds.

+---+
+---+

.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON2-EBZ#none#../
   :alt: Overview#zynq|Linux on ZYNQ
