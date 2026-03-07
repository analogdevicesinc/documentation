Low Voltage Drive Board
=======================

Features
--------

-  Connects to the Controller board and has a power stage that can drive motors up to 48V and 20A.
-  Drives 2 motors simultaneously
-  High frequency drive stage implemented with ADI isolated gate drivers
-  Supported motor types

   -  BLDC
   -  PMSM
   -  Brushed DC
   -  Stepper (bipolar / unipolar)

-  Integrated over current protection
-  Reverse voltage protection
-  Current and Voltage measurement using isolated ADCs

   -  Current measurement on 2 phases for 2 motors
   -  DC Link Voltage measurement

-  BEMF zero cross detection for sensorless control of PMSM or BLDC motors
-  Separate voltage supplies for the 2 motors so that the motors don’t influence each other

+---+
+---+

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/hardware/lv_block_diagram_simplified.png
   :width: 400px

+---+
+---+

Picture and Main Components
---------------------------

|AD-DRVLV2-EBZ Top| |AD-DRVLV2-EBZ Bottom|

+---+
+---+

Key Parts
---------

+------------------------------------------------+--------------------------------------------------------------------+
| Measurement                                    |                                                                    |
+================================================+====================================================================+
| :adi:`AD7403`                                  | 16 bit isolated 2nd order Sigma-Delta modulator                    |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`AD8207`                                  | Zero drift, high voltage, bidirectional difference amplifier       |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`CMP04`                                   | Quad low power, precision comparator                               |
+------------------------------------------------+--------------------------------------------------------------------+
| Power                                          |                                                                    |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`ADuM5000`                                | isoPower® integrated isolated dc-to-dc converter                   |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`ADP1621`                                 | Constant-frequency, current-mode step-up dc/dc controller          |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`ADP2301`                                 | 1.2 A, 20 V, 1.4 MHz non-synchronous step-down switching regulator |
+------------------------------------------------+--------------------------------------------------------------------+
| MOSFET Drivers                                 |                                                                    |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`ADuM5230`                                | Isolated half-bridge driver with integrated high-side supply       |
+------------------------------------------------+--------------------------------------------------------------------+
| :adi:`ADuM7223`                                | Isolated precision half-bridge driver, 4.0A output                 |
+------------------------------------------------+--------------------------------------------------------------------+

+---+
+---+

Switches
--------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/hardware/lv_reset.png
   :alt: Switches
   :width: 600px

**Emergency Stop** switch

-  S2 is a latching emergency stop switch.
-  If triggered the supply for the power stage is turned off.

**Reset** switch

-  S1 is a reset switch for the emergency stop latch.
-  By pressing S1 when S2 is not pressed the power stage is turned on.

+---+
+---+

Downloads
---------

.. admonition:: Download
   :class: download

   **AD-DRVLV2-EBZ**

   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/ad-drvlv2-ebz_schematics.pdf>`_
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/ad-drvlv2-ebz_bom.zip>`_
   -  `Allegro Board File <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/ad-drvlv2-ebz_layout.zip>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_ (You need 16.5 or higher).
   


.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON2-EBZ#controller_board
   :alt: Controller Board#..:\|Overview#signal_chain|Signal Measurement Chain

.. |AD-DRVLV2-EBZ Top| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/hardware/ad-drvlv2-ebz_top_parts.jpg
   :width: 600px
.. |AD-DRVLV2-EBZ Bottom| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/hardware/ad-drvlv2-ebz_bottom_parts.jpg
   :width: 450px
