.. _ad_fmcmotcon1_ebz lv-board:

Low Voltage Drive Board
===============================================================================

.. warning::

   The :adi:`AD-FMCMOTCON1-EBZ` is a **legacy product** and is no longer
   actively supported. This documentation is provided for reference only.

Features and Block Diagram
-------------------------------------------------------------------------------

-  Drives BLDC, PMSM, Brushed DC, and Stepper motors
-  Drives motors up to 48 V at 18 A
-  Integrated over-current protection
-  Current measurement using isolated ADCs
-  Bus voltage, phase currents, and total current analog feedback signals
-  PGAs to maximize the current measurement input range
-  BEMF zero-crossing detection for sensorless control of PMSM or BLDC motors

.. figure:: ../images/lv_block_diagram_simplified.jpg
   :alt: AD-DRVLV1-EBZ simplified block diagram
   :align: center
   :width: 350

   Simplified block diagram

.. figure:: ../images/lv_block_diagram.jpg
   :alt: AD-DRVLV1-EBZ detailed block diagram
   :align: center
   :width: 500

   Detailed block diagram

Picture and Main Components
-------------------------------------------------------------------------------

.. figure:: ../images/ad-drvlv1-ebz_top_parts.jpg
   :alt: AD-DRVLV1-EBZ top view with main components labeled
   :align: center
   :width: 600

   AD-DRVLV1-EBZ top view

.. figure:: ../images/ad-drvlv1-ebz_bottom_parts.jpg
   :alt: AD-DRVLV1-EBZ bottom view with main components labeled
   :align: center
   :width: 600

   AD-DRVLV1-EBZ bottom view

Key Parts
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Part
     - Description
   * - **Measurement**
     -
   * - :adi:`AD7401A`
     - 5 kV rms, isolated 2nd order Sigma-Delta modulator
   * - :adi:`AD8207`
     - Zero drift, high voltage, bidirectional difference amplifier
   * - :adi:`AD8251`
     - 10 MHz, 2 nV/√Hz, programmable gain instrumentation amplifier
   * - :adi:`AD8630`
     - Zero drift, single-supply, rail-to-rail quad op amp
   * - **Power**
     -
   * - :adi:`ADuM5000`
     - isoPower® integrated isolated dc-to-dc converter
   * - :adi:`ADP1621`
     - Constant-frequency, current-mode step-up dc/dc controller
   * - :adi:`ADP2301`
     - 1.2 A, 20 V, 1.4 MHz non-synchronous step-down switching regulator
   * - :adi:`ADP7102`
     - 20 V, 300 mA, low noise, CMOS LDO
   * - **MOSFET Drivers**
     -
   * - :adi:`ADuM5230`
     - Isolated half-bridge driver with integrated high-side supply
   * - IRS2336DSTRPBF
     - High voltage 3-phase gate driver IC

Connectors
-------------------------------------------------------------------------------

.. figure:: ../images/lv_connectors.jpg
   :alt: AD-DRVLV1-EBZ connector locations
   :align: center
   :width: 400

   AD-DRVLV1-EBZ connector locations

Power connector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connector P4 supplies 12–48 VDC to the drive board.
-  The polarity is indicated in the picture above.

BLDC / Stepper motor connector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  For BLDC motors use connector P1 (Phase 1, 2, and 3).
-  For Stepper motors use connector P1 and pin 3 of P5 (Phase 1, 2, 3,
   and 4).

Switches
-------------------------------------------------------------------------------

.. figure:: ../images/lv_buttons.jpg
   :alt: AD-DRVLV1-EBZ button and switch locations
   :align: center
   :width: 600

   AD-DRVLV1-EBZ button and switch locations

Emergency Stop Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  S2 is a latching emergency stop switch.
-  If triggered, the supply for the power stage is turned off.
-  LED DS3 indicates the state of the power stage.

Reset Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  S1 is a reset switch for the emergency stop latch.
-  Pressing S1 when S2 is off turns the power stage on.

LEDs
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - LED
     - Description
   * - DS1
     - Vadj Power Good
   * - DS2
     - 12V Power Good
   * - DS3
     - Over Current
   * - DS4
     - Motor Fault
   * - DS5
     - PWM Enable
   * - DS6
     - Motor Power Good

Power Map
-------------------------------------------------------------------------------

.. figure:: ../images/lv_power_map.jpg
   :alt: AD-DRVLV1-EBZ power map
   :align: center
   :width: 400

   AD-DRVLV1-EBZ power map

Motor Driver Interface
-------------------------------------------------------------------------------

The IRS2336D three-phase gate driver IC provides the following interface
signals:

-  3 pairs of complementary PWM signals with inverted logic
-  PWM frequency up to 150 kHz
-  Hardware integrated dead-time protection
-  Enable signal to start / stop the driver
-  Fault signal from the driver
