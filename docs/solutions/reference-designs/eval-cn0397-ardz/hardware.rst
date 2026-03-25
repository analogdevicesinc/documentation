.. _eval-cn0397-ardz-hardware:

Hardware Guide
==============

The EVAL-CN0397-ARDZ shield connects to the :adi:`EVAL-ADICUP360 <ADICUP360>`
or :adi:`EVAL-ADICUP3029 <ADICUP3029>` base board using the Arduino mating
headers.

.. figure:: cn0397_chip_select.jpg
   :align: center
   :width: 400

   EVAL-CN0397-ARDZ board layout

Connectors and Jumper Configurations
-------------------------------------

Chip Select
~~~~~~~~~~~

The chip select is configurable to be routed to 3 general purpose I/O pins of
the board (digital pins 8, 9, and 10), allowing multiple boards using SPI
communications protocol to be stacked up.

.. figure:: cn0397_cs_config.jpg
   :align: center
   :width: 300

   Chip select jumper configuration

The chip select pin of the :adi:`AD7798` is routed by CS1 to GPIO pin 10, CS2
to GPIO 9, and CS3 to GPIO 8, which can be configured by placing the shunt
across the corresponding CS on connector **P1**.

The shunt is placed across **CS1** by default, however it can be configured to
any of the 3 chip selects in the software.

Sensor Footprint
~~~~~~~~~~~~~~~~

Two types of photodiodes can be used with the EVAL-CN0397-ARDZ, with provisions
for two different footprints:

**Recommended Sensors:**

- Everlight Photodiode -- COLOR SENSOR 620NM CLS15-22C/L213R/TR8 (Red)
- Everlight Photodiode -- COLOR SENSOR 550NM CLS15-22C/L213G/TR8 (Green)
- Everlight Photodiode -- COLOR SENSOR 470NM CLS15-22C/L213B/TR8 (Blue)
- Hamamatsu Photodiode -- 3 CHANNEL RGB COLOR SENSOR S7505-01

The Everlight photodiodes are installed on the board as default and were used
during testing and programming. A provision for the Hamamatsu S7505-01 is also
available. All Everlight photodiodes must be removed before replacing with the
Hamamatsu photodiode.

Spacers
~~~~~~~

Spacers that can accommodate various surface mount and through-hole packages are
available on the board.

**Resistor spacers** (RB_SPACER, RG_SPACER, RR_SPACER) are gain resistors for
each corresponding channel (Blue, Green, Red). The value can be calculated
using:

.. code-block:: none

   RGAIN = IdMAX / VFS

Where ``IdMAX`` is the maximum diode current and ``VFS`` is the full scale
voltage.

**Capacitor spacers** (CB_SPACER, CG_SPACER, CR_SPACER) are used as filtering
for each channel and can be calculated as:

.. code-block:: none

   C = 1 / (2 * pi * RGAIN * fc)

Where ``RGAIN`` is the gain resistor for the corresponding channel and ``fc``
is the target cut-off frequency.
