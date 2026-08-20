Hardware Setup Guide
====================

.. warning::

   Analog Devices uses six designations to inform our customers where a
   semiconductor product is in its
   :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`.
   From emerging innovations to products which have been in production for
   twenty years, we understand that insight into life cycle status is important.
   Device life cycles are tracked on their individual product pages on
   `analog.com <https://www.analog.com/>`_, and should always be consulted
   before making any design decisions.

   This particular article/document/design has been retired or deprecated,
   which means it is no longer maintained or actively updated, even though the
   devices themselves may be Recommended for New Designs or in
   Production. This page is here for historical/reference purposes only.

.. image:: ../images/mc_system.jpg
   :width: 600

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
-  Insert the 6 pin Hall connector into P7 - pin 1 is the empty slot of the Hall
   connector. In case an encoder is used there is a one to one corespondence of
   the encoder's pins to the pins of the P7 connector.

.. image:: ../images/hall_connector.jpg
   :alt: Hall connector
   :align: center
   :width: 300

-  Insert the 5V supply in the left side of the DYNAMO-METER DRIVE SYSTEM

.. image:: ../images/dyno_supply.png
   :alt: Dynamo-meter Drive System
   :align: center
   :width: 300

-  Ensure that the Emergency Stop button P2 is pressed (more information about drive board buttons :doc:`here </solutions/reference-designs/ad-fmcmotcon1-ebz/hardware/lv_board>`)

.. image:: ../images/emergency_stop.jpg
   :alt: Motor and Power connections
   :align: center
   :width: 300

-  Insert the 3 pin motor connector into P1 and connect the lab power supply to P4 (more information about drive board connectors :doc:`here </solutions/reference-designs/ad-fmcmotcon1-ebz/hardware/lv_board>`)

.. image:: ../images/motor_power_connections.jpg
   :alt: Motor and Power connections
   :align: center
   :width: 300

-  Power on the ZedBoard
-  After the board is programmed, in order to start the motor, the Emergency
   Stop button P2 must be released and then the Reset switch S1 must be pressed
   for a few seconds.

+---+
+---+
