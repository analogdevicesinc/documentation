Low Voltage Drive Board
=======================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



Features and Block Diagram
--------------------------

-  Drives BLDC / PMSM / Brushed DC / Stepper motors
-  Drives motors up to 48V at 18A
-  Integrated over current protection
-  Current measurement using isolated ADCs
-  Bus voltage, phase currents and total current analog feedback signals
-  PGAs to maximize the current measurement input range
-  BEMF zero cross detection for sensorless control of PMSM or BLDC motors

============================ ==========================
**Simplified Block Diagram** **Detailed Block Diagram**
============================ ==========================
============================ ==========================

|image1| |image2|

+---+
+---+

Picture and Main Components
---------------------------

|AD-DRVLV1-EBZ Top| |AD-DRVLV1-EBZ Bottom|

+---+
+---+

Key Parts
---------

+------------------------------------------------+--------------------------------------------------------------------+
| Measurement                                    |                                                                    |
+================================================+====================================================================+
| :adi:`AD7401A`                                 | 5 kV rms, isolated 2nd order Sigma-Delta modulator                 |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`AD8207`                                  | Zero drift, high voltage, bidirectional difference amplifier       |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`AD8251`                                  | 24 MHz rail-to-rail dual op amp                                    |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`AD8630`                                  | Zero drift, single-supply, rail-to-rail quad op amp                |
+------------------------------------------------+--------------------------------------------------------------------+
| Power                                          |                                                                    |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`ADuM5000`                                | isoPower® integrated isolated dc-to-dc converter                   |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`ADP1621`                                 | Constant-frequency, current-mode step-up dc/dc controller          |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`ADP2301`                                 | 1.2 A, 20 V, 1.4 MHz non-synchronous step-down switching regulator |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`ADP7102`                                 | 20 V, 300 mA, low noise, CMOS LDO                                  |
+------------------------------------------------+--------------------------------------------------------------------+
| MOSFET Drivers                                 |                                                                    |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`ADuM5230`                                | Isolated half-bridge driver with integrated high-side supply       |
+------------------------------------------------+--------------------------------------------------------------------+
| **IRS2336DSTRPBF**                             | High voltage 3 phase gate driver IC                                |
+------------------------------------------------+--------------------------------------------------------------------+

+---+
+---+

Connectors
----------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/LV_connectors.jpg
   :alt: AD-FMC-MOTCON1-EBZ Connectors
   :width: 400px

Power connector
~~~~~~~~~~~~~~~

-  The connector P4 is used to supply 12...48 VDC to the drive board
-  The polarity is indicated in the picture above

BLDC / Stepper motor connector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  For BLDC motors use connector P1 (Phase 1, 2 and 3)
-  For Stepper motors use connector P1 and pin 3 of P5 (Phase 1, 2, 3 and 4)

+---+
+---+

Switches
--------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/LV_buttons.jpg
   :alt: AD-FMC-MOTCON1-EBZ Buttons
   :width: 600px

Emergency Stop Switch
~~~~~~~~~~~~~~~~~~~~~

-  S2 is a latching emergency stop switch.
-  If triggered the supply for the power stage is turned off.
-  Led DS3 indicates the state of the power stage.

Reset switch
~~~~~~~~~~~~

-  S1 is a reset switch for the emergency stop latch.
-  By pressing S1 when S2 is off the power stage is turned on.

+---+
+---+

LEDs
----

=== ================
LED Description
=== ================
DS1 Vadj Power Good
DS2 12V Power Good
DS3 Over Current
DS4 Motor Fault
DS5 PWM Enable
DS6 Motor Power Good
=== ================

+---+
+---+

Power Map
---------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/lv_power_map.png
   :width: 400px

+---+
+---+

Motor Driver Interface
----------------------

The IRS2336D Three Phase Gate Driver IC has the following interface signals features:

-  3 pairs of complementary PWM signals with inverted logic
-  PWM frequency up to 150 kHz
-  Hardware integrated dead-time protection
-  Enable signal to start / stop the driver
-  Fault signal from the driver

+---+
+---+

Downloads
---------

.. admonition:: Download
   :class: download

   **AD-DRVLV1-EBZ**

   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-drvlv1-ebz_schematics.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-drvlv1-ebz_bom.pdf>`__
   -  `Allegro Board File <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-drvlv1-ebz_layout.zip>`__ (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__ (You need 16.5 or higher).
   


.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#controller_board
   :alt: Controller Board#..:\|Overview#signal_chain|Signal Measurement Chain

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/lv_block_diagram_simplified.png
   :width: 350px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/lv_block_diagram.png
   :width: 500px
.. |AD-DRVLV1-EBZ Top| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-drvlv1-ebz_top_parts.jpg
   :width: 600px
.. |AD-DRVLV1-EBZ Bottom| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-drvlv1-ebz_bottom_parts.jpg
   :width: 600px
