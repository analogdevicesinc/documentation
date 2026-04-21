ADRD4161-01Z Hardware Guide
===========================

This guide covers the hardware features and connections of the ADRD4161-01Z
carrier board.

Connectors
----------

Power Input
~~~~~~~~~~~

The board accepts 9-70 V DC input through an isolated DC-DC converter, which
provides:

* 12 V at up to 3 A for system voltage
* 5 V at up to 5 A for the Raspberry Pi and USB peripherals

Raspberry Pi Header
~~~~~~~~~~~~~~~~~~~

Standard 40-pin Raspberry Pi header for connecting compatible embedded compute
platforms (Raspberry Pi 5, Nvidia Jetson/Orin/AGX, etc.).

IMU Connectors
~~~~~~~~~~~~~~

Two IMU connectors provide plug-and-play compatibility with ADIS16xxx series
IMU modules:

* 14-pin connector
* 16-pin connector

P7 - UART Header
~~~~~~~~~~~~~~~~

Exposes the Raspberry Pi's UART4 interface and a switchable 5 V supply
(controlled by GPIO 24).

.. todo:: P7 pinout diagram

P10 - GPIO Header
~~~~~~~~~~~~~~~~~

Exposes general-purpose I/O pins, including GPIO 23 for WS2812 LED control
(pin 11).

.. todo:: P10 pinout diagram

P12 - Relay Header
~~~~~~~~~~~~~~~~~~

Exposes contacts for two SPDT relays (K1, K2), each rated for 1 A:

* Pins 1-3: K1 (NC, Common, NO)
* Pins 4-6: K2 (NC, Common, NO)

CAN Connector
~~~~~~~~~~~~~

Isolated CAN 2.0B interface, directly connected to the onboard MAX32662
microcontroller running slcan firmware.

.. todo:: CAN cable diagram

Solder Jumpers
--------------

R27, R28, R29 - SWD Debug
~~~~~~~~~~~~~~~~~~~~~~~~~

When bridged, these jumpers expose the MAX32662 microcontroller's SWD signals
on the Raspberry Pi's GPIOs for programming and debugging:

.. list-table::
   :header-rows: 1

   * - Jumper
     - Signal
     - Pi GPIO
   * - R27
     - SWD_IO
     - 6
   * - R28
     - SWD_CLK
     - 20
   * - R29
     - SWD_RSTN
     - 21

Onboard Components
------------------

MAX32662 Microcontroller
~~~~~~~~~~~~~~~~~~~~~~~~

The MAX32662 handles CAN communication via the slcan protocol. It can be
reprogrammed through SWD when the appropriate solder jumpers are bridged.

See :doc:`software-guide` for reprogramming instructions.

Relays
~~~~~~

Two SPDT relays (K1, K2) rated for 1 A, controlled via Raspberry Pi GPIOs:

* K1: GPIO 17
* K2: GPIO 18
