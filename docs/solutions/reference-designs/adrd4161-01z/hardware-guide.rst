.. _adrd4161-01z hardware-guide:

ADRD4161-01Z Hardware Guide
===========================

.. TODO: Add annotated board image
   .. figure:: res/adrd4161-01z-annotated.svg
      :align: center
      :width: 40em

      ADRD4161-01Z Perception Carrier Board

.. TODO: Add component annotation table
   ========== ========= ==================================================================
   Annotation Component Function
   ========== ========= ==================================================================
   1          P1        Power input, 9-70 V DC
   2          J1        Raspberry Pi 40-pin header
   3          P7        UART header (UART4 + switchable 5 V)
   4          P8, P9    CAN bus connections
   5          P10       GPIO header
   6          P12       Relay header (2x SPDT)
   7          J2        14-pin IMU connector
   8          J3        16-pin IMU connector
   ========== ========= ==================================================================

Block Diagram
-------------

.. TODO: Add block diagram
   .. figure:: res/hw_block_diagram.png
      :align: center
      :width: 40em

      ADRD4161-01Z hardware block diagram.

Connectors
----------

Power Input
~~~~~~~~~~~

The board accepts 9-70 V DC input through an isolated DC-DC converter, which
provides:

* 12 V at up to 3 A for system voltage
* 5 V at up to 5 A for the Raspberry Pi and USB peripherals

Raspberry Pi Header (J1)
~~~~~~~~~~~~~~~~~~~~~~~~

Standard 40-pin Raspberry Pi header for connecting compatible embedded compute
platforms (Raspberry Pi 5, Nvidia Jetson/Orin/AGX, etc.).

IMU Connectors (J2, J3)
~~~~~~~~~~~~~~~~~~~~~~~

Two IMU connectors provide plug-and-play compatibility with ADIS16xxx series
IMU modules:

* J2: 14-pin connector
* J3: 16-pin connector

.. _adrd4161_header_p7:

UART Header (P7)
~~~~~~~~~~~~~~~~

Exposes the Raspberry Pi's UART4 interface and a switchable 5 V supply
(controlled by GPIO 24).

.. TODO: Add P7 pinout diagram

GPIO Header (P10)
~~~~~~~~~~~~~~~~~

Exposes general-purpose I/O pins, including GPIO 23 (pin 11) for WS2812 LED
control.

.. TODO: Add P10 pinout diagram

Relay Header (P12)
~~~~~~~~~~~~~~~~~~

Exposes contacts for two SPDT relays (K1, K2), each rated for 1 A:

========== ====== ============ ============== ===========
Relay      GPIO   P12 NC Pin   P12 Common Pin P12 NO Pin
========== ====== ============ ============== ===========
K1         17     1            2              3
K2         18     4            5              6
========== ====== ============ ============== ===========

.. _adrd4161_cable_can:

CAN Cable
---------

The ADRDx161 board family communicates via CAN bus. The CAN interface on the
ADRD4161-01Z is directly connected to the onboard MAX32662 MCU running slcan
firmware.

.. TODO: Add CAN cable diagram
   .. image:: res/cable-can.lfs.svg

Solder Jumpers
--------------

.. _adrd4161_swd_jumpers:

R27, R28, R29 - SWD Debug
~~~~~~~~~~~~~~~~~~~~~~~~~

When bridged, these jumpers expose the MAX32662 microcontroller's SWD signals
on the Raspberry Pi's GPIOs for programming and debugging:

======= ======== ========
Jumper  Signal   Pi GPIO
======= ======== ========
R27     SWD_IO   6
R28     SWD_CLK  20
R29     SWD_RSTN 21
======= ======== ========

Onboard Components
------------------

MAX32662 Microcontroller
~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`MAX32662` handles CAN communication via the slcan protocol. It can be
reprogrammed through SWD when the appropriate solder jumpers are bridged.

See :doc:`software-guide` for reprogramming instructions.

Relays
~~~~~~

Two SPDT relays (K1, K2) rated for 1 A, controlled via Raspberry Pi GPIOs:

* K1: GPIO 17
* K2: GPIO 18

Design Support Files
--------------------

A design support package consisting of the board schematic, layout, assembly
and fabrication files, and more, can be downloaded from the :adi:`ADRD4161-01Z`
page.
