.. _eval-cn0550-ebz:

EVAL-CN0550-EBZ
===============

Low/Full/High-Speed USB 2.0 Isolator with Isolated Power
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

General Description
-------------------

The :adi:`EVAL-CN0550-EBZ <CN0550>` is a 4-layer printed circuit board (PCB)
that allows evaluation of the :adi:`CN0550 <CN0550>` High Speed USB 2.0
Peripheral Isolator circuit. The board is fabricated with a ``0.5oz./1oz.``
copper cladding and IPC-4101 (or IPC-4103) laminates and bonding materials.

Designed to be connected between a host controller and a USB peripheral
device, the :adi:`EVAL-CN0550-EBZ <CN0550>` features a small form-factor
with dimensions of 2.315in ×1.335in x 0.062mm (PCB only).
The evaluation board uses standard Type-A USB connectors for its
signal path — for easy integration with USB systems, a male connector is used
for the host side and a female connector is used for the peripheral side.
Straight headers on each side allow the users to use an external power supply
for high current applications.

Evaluation Board Hardware
-------------------------

.. figure:: cn0550-top.jpg

  Top View of EVAL-CN0550-EBZ

USB Host Plug and LED Indicator (P1, BUS1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The USB host controller must be connected to the male USB-A connector (P1).

*The yellow-green LED (BUS1) lights up to indicate the presence of 5V power
from the USB host.*

.. figure:: cn0550-p1-bus1.jpg

USB Peripheral Port and LED Indicator (P2, BUS2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The USB peripheral device must be connected to the female USB-A connector
(P2).

*The yellow-green LED (BUS2) lights up to indicate the presence of 5V power
for the USB peripheral device.*

.. figure:: cn0550-p2-bus2.jpg

Host Side Power Connector and LED Indicator (P3, EXT1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The onboard regulator circuit of the CN0550 can typically
supply a maximum current of 440mA to the peripheral side when powered from
the VCC pin of the USB host. For applications that require higher current,
the CN0550 output can be increased by moving the J1 solder jumper to the ‘B’
position, and connecting an external >5VDC power supply across the P3
header.

.. figure:: cn0550-p3-ext1.jpg

*The red LED (EXT1) lights up to indicate the presence of an external DC power
supply.*

============ ==========================================
JP1 Position Power Source for the Onboard Regulator
============ ==========================================
A            VCC pin of USB host (Default).
B            External power supply connected across P3.
============ ==========================================

.. figure:: cn0550-p3-connections.jpg

.. tip::

   The maximum voltage that can be safely applied at
   P3 is 32 V. Connect the (+) and (-) pins of the external power supply
   respectively to pins 1 and 2 of P3.

Peripheral Side Power Connector and LED Indicator (P4, EXT2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For applications where 5V power is already available on the peripheral side,
the onboard regulator can be bypassed by moving the J2 solder jumper to the
‘B’ position, and connecting the external 5V peripheral power across the P3
header.

.. figure:: cn0550-p4-ext2.jpg

*The red LED (EXT2) lights up to indicate the presence of an external DC power
supply.*

============ ==========================================
JP2 Position 5 V Power Source for the Peripheral Side
============ ==========================================
A            Onboard regulator circuit (Default)
B            External power supply connected across P4
============ ==========================================

.. figure:: cn0550-p4-connections.jpg

.. tip::

   The voltage applied at P3 should be limited to
   the normal operating VCC range for USB (4.75V to 5.25V). Connect the (+)
   and (-) pins of the external power supply respectively to pins 1 and 2 of P4.

Schematic, Layout and Bill of Materials
---------------------------------------

.. admonition:: Download

  :adi:`EVAL-CN0550-EBZ Design & Integration Files <CN0550-DesignSupport>`

  - Schematic
  - Bill of Materials
  - Gerber Files
  - Allegro Layout Files
  - Assembly Drawing

More Information and Useful Links
---------------------------------

- :adi:`CN0550 Circuit Note Page <CN0550>`
- :adi:`ADuM3165 Product Page <ADuM3165>`
- :adi:`LT8301 Product Page <LT8301>`
