.. _eval-cn0416-ardz:

EVAL-CN0416-ARDZ
================

Isolated and Non-Isolated RS-485 Transceiver.

Overview
--------

:adi:`CN0416` is an isolated and non-isolated RS-485 transceiver board which
allows easy implementation of asynchronous serial (UART) data transmission
between multiple Arduino form factor systems or nodes, especially over long
distances.

The circuit uses the :adi:`ADM2682E` RS-485 transceiver for isolated
communications and the :adi:`LTC2865` for non-isolated RS-485 communications.
Both can be configured for either full-duplex or half-duplex operation with
open or terminated transmission lines. The circuit has on-board RJ-45 ports
which allow the use of common CAT5 cable for fast physical wiring of nodes.
The termination resistance defaults to the CAT5 cable characteristic impedance
of 100 ohms but can be configured to support the standard RS-485 cable
impedance of 120 ohms.

The cable also carries power supply lines which are unpowered by default but
can be connected to a 3.3 V supply from the board's low-dropout voltage
regulator, :adi:`ADP7102`. The system has an on-board 10-pin connector
compatible with the :adi:`ADALM-UARTJTAG` for serial connections to a PC or
other device.

.. figure:: cn0416_board.jpg
   :width: 600 px
   :align: center

   EVAL-CN0416-ARDZ Evaluation Board

Key Specifications
~~~~~~~~~~~~~~~~~~

- **ADM2682E** -- Up to 16 Mbps data rate, true fail-safe receiver inputs,
  5 kV signal isolation using iCoupler data channel and 5 kV power isolation
  using isoPower integrated DC-to-DC converter.
- **LTC2865** -- Up to 20 Mbps data rate, full fail-safe receiver inputs with
  internal window comparator for fail-safe condition detection.

RS-485 Configuration
--------------------

The EVAL-CN0416-ARDZ can be configured using multiple on-board physical
switches for both isolated and non-isolated RS-485 operations.

Switch Functions
~~~~~~~~~~~~~~~~

+--------+---------------------------------------------------------------+
| Switch | Function                                                      |
+========+===============================================================+
| S1     | Configures address of the RS-485 node                         |
+--------+---------------------------------------------------------------+
| S2     | Selects isolated vs non-isolated part and half/full duplex    |
+--------+---------------------------------------------------------------+
| S4     | Selects physical layer half/full duplex of LTC2865            |
+--------+---------------------------------------------------------------+
| S5     | Selects physical layer half/full duplex of ADM2682E           |
+--------+---------------------------------------------------------------+
| S6     | Selects termination resistance of LTC2865                     |
+--------+---------------------------------------------------------------+
| S7     | Selects termination resistance of ADM2682E                    |
+--------+---------------------------------------------------------------+

Summary of Switch Configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------+----+----+----+----+----+
| RS-485 Configuration                      | S2 | S4 | S5 | S6 | S7 |
+===========================================+====+====+====+====+====+
| Isolated, Full Duplex, Terminated         | 2  | NA | 2  | NA | 2  |
+-------------------------------------------+----+----+----+----+----+
| Isolated, Full Duplex, Open               | 2  | NA | 2  | NA | 1  |
+-------------------------------------------+----+----+----+----+----+
| Isolated, Half Duplex, Terminated         | 1  | NA | 1  | NA | 2  |
+-------------------------------------------+----+----+----+----+----+
| Isolated, Half Duplex, Open               | 1  | NA | 1  | NA | 1  |
+-------------------------------------------+----+----+----+----+----+
| Non-Isolated, Full Duplex, Terminated     | 3  | 2  | NA | 2  | NA |
+-------------------------------------------+----+----+----+----+----+
| Non-Isolated, Full Duplex, Open           | 3  | 2  | NA | 1  | NA |
+-------------------------------------------+----+----+----+----+----+
| Non-Isolated, Half Duplex, Terminated     | 4  | 1  | NA | 2  | NA |
+-------------------------------------------+----+----+----+----+----+
| Non-Isolated, Half Duplex, Open           | 4  | 1  | NA | 1  | NA |
+-------------------------------------------+----+----+----+----+----+

Isolated vs Non-Isolated Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+--------------+-------------------------------------+
| S2 Position   | Duplex Mode  | Part Used                           |
+===============+==============+=====================================+
| Position 1    | Half Duplex  | :adi:`ADM2682E` (Isolated)          |
+---------------+--------------+-------------------------------------+
| Position 2    | Full Duplex  | :adi:`ADM2682E` (Isolated)          |
+---------------+--------------+-------------------------------------+
| Position 3    | Full Duplex  | :adi:`LTC2865` (Non-Isolated)       |
+---------------+--------------+-------------------------------------+
| Position 4    | Half Duplex  | :adi:`LTC2865` (Non-Isolated)       |
+---------------+--------------+-------------------------------------+

.. important::

   When S4 and S5 are in switch position 1, S2 **must** be placed in switch
   position 1 or 4 depending on the part being used. When S4 and S5 are in
   switch position 2, S2 **must** be placed in switch position 2 or 3.

Cable Length and Termination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data rate of RS-485 communications varies with cable length. The CAT5/CAT5E
cable has a characteristic impedance of 100 ohms, while the RS-485 standard
cable has 120 ohms.

By default, the parallel termination resistance is 100 ohms supporting
CAT5/CAT5E cables. This can be reconfigured to 120 ohms by disconnecting
solder jumpers JP4, JP6, JP8, and JP10 and shorting solder jumpers JP3, JP5,
JP7, and JP9.

Switch S6 and S7 control the type of termination:

- **Position 1 (OPEN)** -- No line termination. Suitable for low-power, short
  transmissions over distances less than 0.78 m.
- **Position 2 (TERM)** -- Parallel resistance termination. Suitable for long
  distance, high power transmissions not exceeding 4000 ft.

Hex Switch Addressing
~~~~~~~~~~~~~~~~~~~~~

The hex switch S1 can be used to set up node addressing when the CN0416 is
connected to a microcontroller via the Arduino headers. Bits are connected to
analog inputs A0-A3 by default. The switch provides 16 unique address positions
(0-F) mapping to GPIO/Arduino pin connections.

RJ-45 Connection and Multi-Node Wiring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0416-ARDZ has four RJ-45 ports: P4 and P5 for isolated
communications, and P6 and P24 for non-isolated communications. Each pair has
a cross-over connection with each other.

- **Straight-through connection** -- Connect two boards using the same port
  (e.g., P4 of a master node to P4 of a slave node in isolated mode).
- **Crossover connection** -- Connect two boards using opposite ports (e.g.,
  P6 of a master node to P24 of a slave node in non-isolated mode).

ADALM-UARTJTAG Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0416-ARDZ has a 10-pin 5x2 connector to interface with the
:adi:`ADALM-UARTJTAG`. The yellow LED DS2 indicates a live connection between
the two devices. For half-duplex setups, the ADALM-UARTJTAG needs to be
configured for RS-485 communications.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0416-ARDZ Design & Integration Files <https://www.analog.com/cn0416-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

More Information and Useful Links
---------------------------------

- :adi:`CN0416 Circuit Note Page <CN0416>`
- :adi:`ADM2682E Product Page <ADM2682E>`
- :adi:`LTC2865 Product Page <LTC2865>`
- :adi:`ADP7102 Product Page <ADP7102>`
- :adi:`ADALM-UARTJTAG Product Page <ADALM-UARTJTAG>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`ez/reference-designs`.
