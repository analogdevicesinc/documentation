.. imported from: https://wiki.analog.com/resources/eval/user-guides/pzsdr/carriers/brk

.. _adrv1crr-bob:

ADRV1CRR-BOB Breakout Carrier
==============================

The :adi:`ADRV1CRR-BOB` is a breakout carrier board for the PicoZed SDR
System-On-Module (SOM) platform, providing a wide range of interfaces for
prototyping and evaluation. It is designed for use with the
:ref:`ADRV9361-Z7035 <adrv9361-z7035>` and :ref:`ADRV9364-Z7020 <adrv9364-z7020>`
RF SOMs.

.. figure:: picture.png
   :align: center
   :width: 600

   ADRV1CRR-BOB Breakout Carrier top view

Features
--------

.. list-table::
   :header-rows: 0
   :widths: 100

   * - 10/100/1000 Mbps Ethernet
   * - USB 2.0 OTG
   * - USB-UART
   * - PC4 JTAG interface
   * - 162 user I/O pins
   * - Two 60-pin (2x30) 0.1" footprints
   * - Four 32-pin (2x16) 0.1" footprints
   * - 4 user push buttons
   * - 4 user switches
   * - 4 user LEDs
   * - 5 V @ 2 A input
   * - Selectable 1.8 V, 2.5 V, or 3.3 V for SOM I/O (or external supply)
   * - Zynq PL I/O bank current measurement access points

Compatible SOMs
---------------

.. list-table::
   :header-rows: 1

   * - SOM
     - Compatibility
   * - :ref:`ADRV9361-Z7035 <adrv9361-z7035>`
     - Full -- all carrier features supported
   * - :ref:`ADRV9364-Z7020 <adrv9364-z7020>`
     - Recommended carrier for this SOM

.. note::

   Due to the fewer available user I/Os on the Zynq XC7Z020, the ADRV1CRR-BOB
   breakout carrier is the recommended carrier for the ADRV9364-Z7020.

Top Level BOM
-------------

.. list-table::
   :header-rows: 1

   * - Part Number
     - Description
   * - Molex 105263-0003
     - Cellular 6-band antenna, 200 mm cable length
   * - Pulse W1900
     - 3G pentaband 824--2170 MHz, right-angle SMA antenna

Schematics and Design Files
----------------------------

.. admonition:: Download

   Rev C design files for the :adi:`ADRV1CRR-BOB` breakout carrier:

   - :download:`Rev C2 Schematic (PDF) <02-039931-01-c2.pdf>`
   - :download:`Rev C BOM (XLS) <05-039931-c.xls>`
   - :download:`Rev C Gerbers (ZIP) <09-039931-01c.zip>`
   - :download:`Rev C Allegro Board File (ZIP) <08_039931c.zip>`

More Information
----------------

- :ref:`ADRV9361-Z7035 User Guide <adrv9361-z7035>`
- :ref:`ADRV9364-Z7020 User Guide <adrv9364-z7020>`
- :adi:`ADRV1CRR-BOB Product Page <ADRV1CRR-BOB>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.

.. esd-warning::
