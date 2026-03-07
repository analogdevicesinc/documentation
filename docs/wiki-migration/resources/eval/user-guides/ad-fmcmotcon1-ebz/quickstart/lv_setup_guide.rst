Hardware Setup Guide
====================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_


   |image1|

Supported Carriers
------------------

-  `ZedBoard <http://www.zedboard.org>`_

+---+
+---+

Required Hardware
-----------------

-  AD-FMCMOTCON1-EBZ - Controller board.
-  AD-DRVLV1-EBZ - Low voltage drive board.
-  AD-DYNO1-EBZ - Dynamo-meter Drive System (Optional).
-  `ZedBoard <http://www.zedboard.org>`_
-  24V 3A capable lab power supply.

+---+
+---+

Getting Started
---------------

-  Connect the Low voltage drive board to the Controller board.
-  Connect the Controller + Drive boards assembly to FMC connector of the ZedBoard
-  Insert the 6 pin Hall connector into P7 - pin 1 is the empty slot of the Hall connector. In case an encoder is used there is a one to one corespondence of the encoder's pins to the pins of the P7 connector.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/hall_connector.jpg
   :alt: Hall connector
   :align: center
   :width: 300px

-  Insert the 5V supply in the left side of the DYNAMO-METER DRIVE SYSTEM

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/dyno_supply.png
   :alt: Dynamo-meter Drive System
   :align: center
   :width: 300px

-  Ensure that the Emergency Stop button P2 is pressed (more information about drive board buttons :doc:`here </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/lv_board>`)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/emergency_stop.jpg
   :alt: Motor and Power connections
   :align: center
   :width: 300px

-  Insert the 3 pin motor connector into P1 and connect the lab power supply to P4 (more information about drive board connectors :doc:`here </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/lv_board>`)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/motor_power_connections.jpg
   :alt: Motor and Power connections
   :align: center
   :width: 300px

-  Power on the ZedBoard
-  After the board is programmed, in order to start the motor, the Emergency Stop button P2 must be released and then the Reset switch S1 must be pressed for a few seconds.

+---+
+---+

.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#none#../
   :alt: Overview#zynq|Linux on ZYNQ

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/mc_system.jpg
   :width: 600px
