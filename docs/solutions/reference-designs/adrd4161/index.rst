ADRD4161-01Z
============

Perception Carrier Board
""""""""""""""""""""""""""

Overview
--------

The ADRD4161-01Z is a carrier board for embedded compute platforms
(e.g. Raspberry Pi 5, Nvidia Jetson/Orin/AGX), featuring the Raspberry Pi
40-pin header. It provides isolated power supplies and a number of connectivity
options: ADI IMU, CAN 2.0B, UART, GPIOs, and two SPDT relays.

Its isolated DC-DC converter can be powered from 9-70 V DC, which it then
converts to 12 V (3 A limit) system voltage and 5 V (5 A limit) for the
Raspberry Pi and power-hungry USB peripherals. 14-pin and 16-pin IMU connectors
allow for plug-and-play interoperability with compatible IMU modules in the
ADIS16xxx series.

Specifications
--------------

.. list-table::
   :header-rows: 1

   * - Parameter
     - Value
   * - Input Voltage
     - 9-70 V DC (isolated)
   * - 12 V Output
     - 3 A max
   * - 5 V Output
     - 5 A max
   * - Compute Header
     - Raspberry Pi 40-pin
   * - IMU Connectors
     - 14-pin and 16-pin (ADIS16xxx compatible)
   * - CAN Interface
     - Isolated CAN 2.0B (slcan firmware)
   * - Relays
     - 2x SPDT, 1 A

Required Hardware
-----------------

* ADRD4161-01Z board
* Raspberry Pi 5 (or compatible embedded compute platform)
* Compatible ADIS16xxx IMU module (optional)
* 9-70 V DC power supply
* MicroSD card with Raspberry Pi OS

User Guides
-----------

.. toctree::

   quick-start-guide
   hardware-guide
   software-guide

Help and Support
----------------

For questions and support, visit the
`EngineerZone <https://ez.analog.com/>`_.
