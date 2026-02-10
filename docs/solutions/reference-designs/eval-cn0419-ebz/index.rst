.. _eval-cn0419-ebz:

EVAL-CN0419-EBZ
===============

Universal Serial Bus (USB) Peripheral Isolator Circuit
""""""""""""""""""""""""""""""""""""""""""""""""""""""

Overview
--------

The :adi:`CN0419` is a circuit that isolates a peripheral device that
already implements a USB interface by using the :adi:`ADuM4160`, a USB port isolator
based on Analog Devices iCoupler® technology. It is bus-powered by pairing it
with a small isolated DC-to-DC converter such as the :adi:`ADuM5020`. The application
circuit shown is typical of many medical and industrial applications.

The :adi:`ADuM4160` is a USB port isolator, based on Analog Devices,
Inc., iCoupler® technology. Combining high speed CMOS and monolithic air core
transformer technology, these isolation components provide outstanding
performance characteristics and are easily integrated with low and full speed
USB-compatible peripheral devices.

The :adi:`ADuM5020` is an isoPower®, integrated, isolated DC-to-DC
converter. Based on the Analog Devices, Inc., iCoupler® technology, this
DC-to-DC converter provides regulated, isolated power that is below CISPR22
Class B limits at full load on a 2-layer printed circuit board (PCB) with
ferrites.

The :adi:`EVAL-CN0419-EBZ <CN0419>` board connects through a USB Type A Plug
and is powered by the bus voltage from the USB port.

.. figure:: figure_7.png

   CN0419 circuit block diagram

General Setup
-------------

Block assignments
~~~~~~~~~~~~~~~~~

.. figure:: block_assign.png

- Terminal block **P1** is the USB Male plug to be inserted to USB port
- Terminal block **P2** is the USB Female receptacle for the peripheral
- Terminal block **S1** is the switch for selection of speed operation
  (Full speed or Low speed)

Speed selection
~~~~~~~~~~~~~~~~

Peripheral devices run at one of three speeds, low (1.5 Mbps), full (12 Mbps),
and high (480 Mbps). The :adi:`EVAL-CN0419-EBZ Evaluation Board <CN0419>` can
accommodate the low and full speed operations. Listed below are some examples
of peripheral devices for each speed.

#. Low speed devices

   - Examples: keyboards, mice, and game peripherals
   - Bus rate: 1.5 Mb/s

#. Full speed devices

   - Examples: phones, audio devices, and compressed video
   - Bus rate: 12 Mb/s

The isolator is hardwired for the desired speed setting, either full speed or
low speed. A switch at the upstream side allows the user to select between these
speeds. To switch between the two modes, flip the actuator of S1 switch to FS
mode as indicated in silkscreen for full speed operation and LS mode otherwise.

.. grid::
   :widths: 50 50

   .. figure:: ls_mode.png

      Low speed operation

   .. figure:: fs_mode.png

      Full speed operation

Required Equipment
~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-CN0419-EBZ Evaluation Board <CN0419>`
- PC with the following *minimum requirements*:

   - PC, Mac, Linux computer, or other host that supports USB
   - Peripheral Device (USB Flash drive, keyboard, evaluation board, etc.)
   - USB Extender (Optional)

Test Setup
~~~~~~~~~~

.. figure:: setup_diagram2.png

#. Set the switch S1 to full speed or low speed operation depending on the
   peripheral specifications.
#. Connect the peripheral to P2 of the :adi:`EVAL-CN0419-EBZ <CN0419>` board.
#. Plug P1 of the :adi:`EVAL-CN0419-EBZ <CN0419>` board into the USB port of the
   PC/host

Running the System
~~~~~~~~~~~~~~~~~~

#. Make sure the setting for S1 is correct based on the peripheral device.
#. Plug P1 of the board into the PC/host, the :adi:`EVAL-CN0419-EBZ <CN0419>` is
   automatically turned on and providing isolation. DS1 will light up as an indication
   that the board is delivering power to the peripheral device.
#. The PC/host must recognize the peripheral connected to make sure the setup is working.
#. Upon successful connection, you can now provide your peripheral the isolated power.

More Information and Useful Links
---------------------------------

- :adi:`CN0419 Circuit Note Page <CN0419>`
- :adi:`CN0419 Design Support Package <CN0419-DesignSupport>`
- :adi:`ADuM4160 Product Page <ADuM4160>`
- :adi:`ADuM5020 Product Page <ADuM5020>`

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   :adi`EVAL-CN0419-EBZ Design & Integration Files <CN0419-DesignSupport>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project
