.. _eval-cn0590-ardz:

EVAL-CN0590-EBZ
================

Galvanic Isolation of USB High Speed Type-C.

.. figure:: eval-cn0590-ebz_angle.jpg
   :align: center

   EVAL-CN0590-EBZ evaluation board

Overview
--------

The :adi:`CN0590 <CN0590>` is a plug and play USB 2.0 high-speed isolator that
can be used with any modern Type-C device supporting USB 2 connectivity. The
circuit provides a completely isolated connection between a USB 2.0 host and a
USB 2.0 device.

.. figure:: cn0590_simplified_block_diagram.png
   :align: center

   CN0590 simplified block diagram

The CN0590 supports fully compatible power and signal isolation up to 2.5 W and
480 Mbps, respectively, as mandated by the USB 2 standard. The system is rated
up to 2.5 kVRMS isolation voltage per UL 1577 and features a system creepage
and clearance of 3.1 mm, limited by the :adi:`ADuM3070`. This system is
suitable for functional isolation or basic and reinforced 300 VRMS CAT II
isolation applications according to IEC 61010 and IEC 62368 standards in many
industrial, energy, and instrumentation applications.

The circuit uses the following key components:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Component
     - Function
   * - :adi:`ADuM3166`
     - USB 2.0 high-speed digital isolator for data isolation
   * - :adi:`ADuM3070`
     - Regulated DC-to-DC isolated power supply controller with external
       transformer for power isolation
   * - :adi:`MAX77958`
     - USB Type-C PD controller
   * - :adi:`MAX20333`
     - Power path selector
   * - :adi:`ADuM1252`
     - Bidirectional I2C isolator
   * - :adi:`MAX14606`
     - Dual power source management IC with reverse polarity, overvoltage, and
       overcurrent protections

Board Components
----------------

.. figure:: cn0590_board_image.png
   :align: center

   EVAL-CN0590-EBZ board component placement

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Designator
     - Description
   * - P1
     - USB Type-C connector --- USB host plug (connect host controller here)
   * - P2
     - USB Type-C connector --- auxiliary
   * - P4
     - USB Type-C connector --- secondary side
   * - P5
     - USB Type-C connector --- secondary side
   * - P6
     - USB Type-C connector --- USB peripheral port (connect peripheral here)
   * - P7
     - USB Type-C connector --- external battery / power input

Required Equipment
------------------

- EVAL-CN0590-EBZ evaluation board
- Host PC with High-Speed USB 2.0 support
- USB flash drive with High-Speed USB 2.0 support
- USB Type-C cable supporting both power and data signaling
- Type-C male to Type-A female adapter

Setup and Test
--------------

No evaluation software is required. The board operates transparently as a
USB 2.0 high-speed isolated retimer between host and device.

To test the USB 2.0 functionality of the EVAL-CN0590-EBZ, follow the steps
below:

.. figure:: high_speed_data_transfer_test_setup.png
   :align: center

   High-speed data transfer test setup

#. Using the Type-C to Type-A adapter, connect the USB flash drive to **P6** of
   the EVAL-CN0590-EBZ.
#. Connect the Type-C USB cable to **P1** of the EVAL-CN0590-EBZ and then the
   other end of the cable to the computer USB port. Wait for the USB flash
   drive to be detected on the computer.
#. Validate the speed of the USB flash drive using a USB device tree viewer.
   The screenshot below shows an example device tree of a high-speed USB
   device.

.. figure:: high-speed_device_connection_speed.png
   :align: center

   Example USB Device Tree Viewer screen for a high-speed USB device

Documents
---------

- :adi:`CN0590 Circuit Note <CN0590>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0590-EBZ Design & Integration Files
   <https://www.analog.com/cn0590-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information
----------------------

- :adi:`ADuM3166 Product Page <ADUM3166>`
- :adi:`ADuM3070 Product Page <ADUM3070>`
- :adi:`MAX77958 Product Page <MAX77958>`
- :adi:`MAX20333 Product Page <MAX20333>`
- :adi:`ADuM1252 Product Page <ADUM1252>`
- :adi:`MAX14606 Product Page <MAX14606>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
