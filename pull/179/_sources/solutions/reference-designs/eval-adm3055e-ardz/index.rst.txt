.. _eval-adm3055e-ardz:

EVAL-ADM3055E-ARDZ
===================

Isolated CAN FD Arduino Shield.

.. figure:: img_20191202_092114.jpg
   :align: center

   EVAL-ADM3055E-ARDZ board (top and bottom view)

Overview
--------

The :adi:`CN0401 Circuit Note <CN0401>` is an Arduino Uno compatible isolated
controller area network with flexible data rate (CAN FD) communications port.
The board interfaces via SPI to development platforms and is built around the
:adi:`ADM3055E` CAN FD transceiver with integrated isolated DC-to-DC converter.

Key features:

- CAN FD data rates up to 8 Mbps
- Reinforced signal and power isolation between node and CAN FD bus
- Switchable 120 ohm split termination with common-mode filtering
- Reduced power standby mode with remote wake-up notification capability
- Backwards compatible with classical CAN networks
- Screw terminal or CiA 303-1 male 9-pin sub-D port for CAN bus connection
- No external bus power required (integrated DC-to-DC converter)

.. figure:: cn0401_silkscreen.png
   :align: center

   EVAL-ADM3055E-ARDZ board silkscreen and component layout

Required Equipment
------------------

- EVAL-ADM3055E-ARDZ evaluation board (Arduino shield)
- :adi:`EVAL-ADICUP3029` development board or Arduino Uno compatible platform
- CAN FD capable devices for bus communication
- USB cable

Hardware Setup
--------------

.. admonition:: Important

   There should always be a shunt in jumper headers P2, P11, P19, and P20
   for the board to function properly.

Power Supply Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

The board power can be sourced from the Arduino host or from external supplies
via the P6 terminal block.

**P6 -- External Supply Terminal Block:**

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Pin
     - Function
   * - 1
     - External DC-to-DC converter supply (5 V)
   * - 2
     - External logic supply (2.7 V to 5.5 V)
   * - 3
     - Ground

**P20 -- DC-to-DC Converter Power Source:**

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Jumper Position
     - Description
     - Image
   * - Pins 1-2
     - Sources 5 V from Arduino Uno header
     - .. image:: p20v1.png
   * - Pins 2-3
     - Sources from external supply terminal block (P6, Pin 1)
     - .. image:: p20v2.png

**P11 -- Logic Supply Source:**

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Jumper Position
     - Description
     - Image
   * - Pins 1-2
     - Sources from IOREF Arduino Uno header pin
     - .. image:: p11v1.png
   * - Pins 2-3
     - Sources from external supply terminal block (P6, Pin 2, 2.7 V to 5.5 V)
     - .. image:: p11v2.png

CAN Bus Connections
~~~~~~~~~~~~~~~~~~~

The CAN bus can be connected via the screw terminal block or the CiA 303-1
male 9-pin sub-D connector.

**Terminal Block Pin Assignment:**

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Pin
     - Signal
   * - 1
     - CANL
   * - 2
     - CANH
   * - 3
     - GND2

**CiA 303-1 Male 9-Pin Sub-D Pin Assignment:**

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Pin
     - Signal
   * - 2
     - CANL
   * - 3
     - GND2
   * - 7
     - CANH

.. note::

   Pins 5 and 6 of the sub-D connector can optionally be configured to GND2
   via resistors R2 and R4.

SPI Chip Select Configuration (P2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SPI chip select signal can be routed to one of four Arduino digital pins
through the P2 header.

.. list-table::
   :header-rows: 1
   :widths: 25 50 25

   * - Jumper Position
     - Arduino Pin
     - Image
   * - Pins 1-2
     - D10
     - .. image:: p2v1.png
   * - Pins 3-4
     - D9
     - .. image:: p2v2.png
   * - Pins 5-6
     - D8
     - .. image:: p2v3.png
   * - Pins 7-8
     - D7
     - .. image:: p2v4.png

Mode Control
~~~~~~~~~~~~

**P5 -- Silent Mode:**

Installing a shunt on P5 allows the platform to set the :adi:`ADM3055E`
transceiver to silent mode (receive-only operation) via Arduino Uno header
pin D4.

.. figure:: p5.png
   :align: center

   P5 jumper (silent mode enable)

**P7 -- Interrupt:**

A shunt must be installed on P7 to detect received CAN frames and
notification that the remote wake-up pattern has been received. The interrupt
signal is routed to Arduino Uno header pin D2.

.. figure:: p7.png
   :align: center

   P7 jumper (interrupt enable)

**P19 -- Operating Mode Selection:**

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Jumper Position
     - Description
     - Image
   * - Pins 1-2
     - Full speed mode (supports all data rates up to maximum)
     - .. image:: p19v1.png
   * - Pins 2-3
     - Slope control mode (reduced slew rate for lower speeds)
     - .. image:: p19v2.png

.. note::

   Removing the P19 shunt places the transceiver into standby mode.

Software Setup
--------------

Demo software is available for the :adi:`EVAL-ADICUP3029` platform with
CN0401 CAN FD communication support.

Documents
---------

- :adi:`CN0401 Circuit Note <CN0401>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-ADM3055E-ARDZ Design & Integration Files
   <https://www.analog.com/cn0401-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information
----------------------

- :adi:`ADM3055E Product Page <ADM3055E>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
