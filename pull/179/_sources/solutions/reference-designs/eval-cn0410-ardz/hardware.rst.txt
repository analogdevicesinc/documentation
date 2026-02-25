.. _eval-cn0410-ardz hardware:

Hardware Guide
==============

This section describes the hardware configuration and connector settings for
the :adi:`EVAL-CN0410-ARDZ <CN0410>` evaluation board.

Connectors and Jumper Configurations
-------------------------------------

Chip Select (P21)
~~~~~~~~~~~~~~~~~

The chip select pin of the :adi:`AD5686` is hardware configurable and routed to
three general-purpose I/O pins on the board. Use the table below to change the
location of the chip select by moving the shunt on P21, and ensure the software
is configured accordingly. By default, the chip select is located on GPIO 8.
This feature allows multiple boards using SPI communications protocol to be
stacked on top of each other.

.. figure:: images/cn0410_cs.jpg
   :align: center
   :width: 400

   Chip Select Jumper Configuration

.. list-table::
   :header-rows: 1

   * - Chip Select (P21)
     - GPIO (P16)
   * - Pins 1 & Pin 2
     - GPIO 8
   * - Pins 3 & Pin 4
     - GPIO 9
   * - Pins 5 & Pin 6
     - GPIO 10

LED Connectors (P1, P6, P9)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LEDs can be connected through connectors P1, P6, and P9, where each channel can
independently source up to 1 A of current using the three channels of the DAC.
Pin 1 (labelled as **-ve**) of the terminal block is to be connected to the
cathode of the LED and Pin 2 (labelled as **+ve**) to the anode of the LED.

.. figure:: images/cn0410_led_connection.jpg
   :align: center
   :width: 400

   LED Connection Detail

**Recommended LEDs**

- Lumileds Red LED -- **LXM5-PD01**
- Lumileds Green LED -- **LXML-PM01-0080**
- Lumileds Blue LED -- **LXML-PB02**
- `Lumileds Datasheet <https://www.lumileds.com/uploads/265/DS68-pdf>`__

The circuit has been tested with the CFTL-LED-BAR with up to 500 mA of current,
which heats the board up to the rated temperature of the FR4 material used in
fabrication. It is recommended to use cooling fans when using currents above
500 mA per channel.

CFTL-LED-BAR Connections
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - EVAL-CN0410-ARDZ
     - CFTL-LED-BAR
   * - P1.1
     - P1.1
   * - P1.2
     - P1.2
   * - P6.1
     - P9.1
   * - P6.2
     - P9.2
   * - P9.1
     - P5.1
   * - P9.2
     - P5.2

Transmit/Receive Connector (isoSPI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`LT6820` allows for SPI communications protocol to be converted to
pulses for long-distance transmission. The transmit and receive connectors can
be used to connect boards for up to 100 meters in length. Multiple boards can
be connected with a single master using its multi-drop configuration, attaching
boards in series to each other.

.. figure:: images/cn0410_multidrop.jpg
   :align: center
   :width: 500

   Multi-Drop Configuration

Master Mode Settings
^^^^^^^^^^^^^^^^^^^^

Refer to the table below to set the board as a master/transmitter:

.. list-table::
   :header-rows: 1

   * - P2
     - P5
     - P7
     - S2
   * - Open
     - Shorted
     - Shorted
     - Master Position

.. figure:: images/cn0410_master_mode.jpg
   :align: center
   :width: 400

   Master Mode Jumper Settings

Slave Mode Settings
^^^^^^^^^^^^^^^^^^^

Refer to the table below to set the board as a slave:

.. list-table::
   :header-rows: 1

   * - P2
     - P5
     - P7
     - S2
   * - Shorted
     - Open
     - Open
     - Slave Position

.. figure:: images/cn0410_slave_mode.jpg
   :align: center
   :width: 400

   Slave Mode Jumper Settings

A transformer or a pair of transformers are used to isolate the signals between
the two LTC6820s and must be terminated by a resistor. Only the master and the
last slave on the transmission line must be terminated by shorting connectors
P5 and P7.
