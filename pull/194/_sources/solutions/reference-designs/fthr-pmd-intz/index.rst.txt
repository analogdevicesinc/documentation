.. _fthr-pmd-intz:

FTHR-PMD-INTZ
=============

Feather to PMOD Adaptor Board.

Overview
--------

The :adi:`FTHR-PMD-INTZ` is an add-on adapter board especially built for the
MAXIM MCU boards. Maxim Feather Boards, namely the :adi:`MAX32630FTHR`,
:adi:`MAX32650FTHR`, :adi:`MAX32655FTHR`, :adi:`MAX32666FTHR`, and
:adi:`MAX78000FTHR`, are very small form factors called “feathers”, and they
require special connectors to be used with other Pmod boards.

This interposer board provides such solution and allows interfacing with
up to two Pmod boards via SPI or I2C interface. Furthermore, this add-on
adapter board adheres to the standards, such as the Digilent Pmod™
Interface Specification and Adafruit Feather Specification.

.. figure:: fthr_pmd_intz.png
   :align: center

   FTHR-PMD-INTZ

.. important::

   **Evaluation Kit Contents:**

   - :adi:`FTHR-PMD-INTZ` Adapter Board
     (`Buy <https://shoppingcart.analog.com/AddModel.aspx?locale=en&ACTION=BUY_BUNDLES&modelNbr=FTHR-PMD-INTZ>`__)

Adapter Board Hardware
----------------------

.. figure:: fthr-pmd-intz_hardware.png
   :align: center

   Hardware Parts

Power Configuration
~~~~~~~~~~~~~~~~~~~

The circuit is powered by the voltage coming from the
Maxim Featherheaders.

.. figure:: power_jumpers_with_label.png
   :align: center

   Power Jumpers


The table below lists the power configuration for this interposer
board. The default voltage configuration for all is 3V3.

+-----------------+-----------------+-----------------+-----------------+
| **Part**        | **Description** | **Left          | **Right         |
|                 |                 | Connection**    | Connection**    |
+-----------------+-----------------+-----------------+-----------------+
| P2              | Feather Voltage | 3V3             | 1V8             |
|                 | Selector        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| P4              | I2C PMOD        | 3V3             | VBUS (5 V)      |
|                 | Voltage         |                 |                 |
|                 | Selector        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| P5              | SPI PMOD        | 3V3             | VBUS (5 V)      |
|                 | Voltage         |                 |                 |
|                 | Selector        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

SPI Pmod Connector (P6)
~~~~~~~~~~~~~~~~~~~~~~~

Connect Pmod devices that use SPI interface to the left-hand side Pmod
connector, as shown below.

.. figure:: spi.png
   :align: center

   SPI PMOD Connector

The table below lists the corresponding pin assignment.

+-----------------+-----------------+-----------------+-----------------+
|      **SPI Pmod Connector (P6) Pinout**                               |
+=================+=================+=================+=================+
| **Pin Number**  | **Pin Function  | **Pin Number**  | **Pin Function  |
|                 | on              |                 | on              |
|                 | FTHR-PMD-INTZ** |                 | FTHR-PMD-INTZ** |
+-----------------+-----------------+-----------------+-----------------+
| 1               | **CS**. SPI     | 7               | **SPI_GPIO0**.  |
|                 | Chip select #1  |                 | Interrupt       |
|                 | from MAXFTHR to |                 | Signal from the |
|                 | the Pmod        |                 | Pmod device to  |
|                 | device.         |                 | the MAXFTHR     |
+-----------------+-----------------+-----------------+-----------------+
| 2               | **MOSI_GPIO1**. | 8               | **SPI_GPIO1**.  |
|                 | SPI data from   |                 | Reset Signal    |
|                 | MAXFTHR to the  |                 | from MAXFTHR to |
|                 | Pmod device.    |                 | Pmod device     |
+-----------------+-----------------+-----------------+-----------------+
| 3               | **MISO**. SPI   | 9               | **SPI_GPIO2**.  |
|                 | data from       |                 | SPI Chip select |
|                 | MAXFTHR to the  |                 | #2 from MAXFTHR |
|                 | Pmod device.    |                 | to the Pmod     |
|                 |                 |                 | device.         |
+-----------------+-----------------+-----------------+-----------------+
| 4               | **SCLK**. SPI   | 10              | **SPI_GPIO3**.  |
|                 | Clock from      |                 | SPI Chip select |
|                 | MAXFTHR to the  |                 | #3 from MAXFTHR |
|                 | Pmod device.    |                 | to the Pmod     |
|                 |                 |                 | device.         |
+-----------------+-----------------+-----------------+-----------------+
| 5               | **GND**. Ground | 11              | **GND**. Ground |
+-----------------+-----------------+-----------------+-----------------+
| 6               | **VCC**.        | 12              | **VCC**.        |
|                 | Connected to    |                 | Connected to    |
|                 | 3V3 or VBUS     |                 | 3V3 or VBUS     |
|                 | from MAXFTHR    |                 | from MAXFTHR    |
|                 | (shorted in P5) |                 | (shorted in P5) |
+-----------------+-----------------+-----------------+-----------------+

I2C Pmod Connector (P7)
^^^^^^^^^^^^^^^^^^^^^^^

Pmod devices that use I2C interface should be connected to the right
Pmod connector.

.. figure:: i2c.png
   :align: center

   I2C PMOD Connector

The table below lists the corresponding pin assignment.

+-----------------+-----------------+-----------------+-----------------+
| **I2C Pmod Connector (P7) Pinout**                                    |
+=================+=================+=================+=================+
| **Pin Number**  | **Pin Function  | **Pin Number**  | **Pin Function  |
|                 | on              |                 | on              |
|                 | FTHR-PMD-INTZ** |                 | FTHR-PMD-INTZ** |
+-----------------+-----------------+-----------------+-----------------+
| 1               | **I2C_GPIO0**.  | 7               | **I2C_GPIO0**.  |
|                 | Interrupt       |                 | Interrupt       |
|                 | Signal from the |                 | Signal from the |
|                 | Pmod device to  |                 | Pmod device to  |
|                 | the MAXFTHR.    |                 | the MAXFTHR.    |
+-----------------+-----------------+-----------------+-----------------+
| 2               | **I2C_GPIO1**.  | 8               | **I2C_GPIO1**.  |
|                 | Reset Signal    |                 | Reset Signal    |
|                 | from the        |                 | from the        |
|                 | MAXFTHR to the  |                 | MAXFTHR to the  |
|                 | Pmod device.    |                 | Pmod device.    |
+-----------------+-----------------+-----------------+-----------------+
| 3               | **SCL**. I2C    | 9               | **SCL**. I2C    |
|                 | Clock from the  |                 | Clock from the  |
|                 | MAXFTHR to the  |                 | MAXFTHR to the  |
|                 | Pmod device.    |                 | Pmod device.    |
+-----------------+-----------------+-----------------+-----------------+
| 4               | **SDA**. I2C    | 10              | **SDA**. I2C    |
|                 | Data from the   |                 | Data from the   |
|                 | MAXFTHR to the  |                 | MAXFTHR to the  |
|                 | Pmod device.    |                 | Pmod device.    |
+-----------------+-----------------+-----------------+-----------------+
| 5               | **GND**. Ground | 11              | **GND**. Ground |
+-----------------+-----------------+-----------------+-----------------+
| 6               | **VCC**.        | 12              | **VCC**.        |
|                 | Connected to    |                 | Connected to    |
|                 | 3V3 or VBUS     |                 | 3V3 or VBUS     |
|                 | from MAXFTHR    |                 | from MAXFTHR    |
|                 | (shorted in P4) |                 | (shorted in P4) |
+-----------------+-----------------+-----------------+-----------------+


Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :download:`FTHR-PMD-INTZ Design & Integration Files <fthr-pmdz-intz-designsupport.zip>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project
   - LTspice Simulation File


Additional Information and Useful Links
---------------------------------------

- :adi:`FTHR-PMD-INTZ Product Page <FTHR-PMD-INTZ>`
- :adi:`MAX32630FTHR Product Page <MAX32630FTHR>`
- :adi:`MAX32650FTHR Product Page <MAX32650FTHR>`
- :adi:`MAX32655FTHR Product Page <MAX32655FTHR>`
- :adi:`MAX32666FTHR Product Page <MAX32666FTHR>`
- :adi:`MAX78000FTHR Product Page <MAX78000FTHR>`

Reference Demos & Software
--------------------------

- :dokuwiki:`EVAL-ADXL355-PMDZ User Guide </resources/eval/user-guides/circuits-from-the-lab/eval-adxl355-pmdz>`
- :dokuwiki:`EVAL-ADT7420-PMDZ Digital Temperature PMOD User Guide </resources/eval/user-guides/circuits-from-the-lab/eval-adt7420-pmdz>`
- :dokuwiki:`MAX31855PMB1 Thermocouple-to-Digital PMOD User Guide </resources/eval/user-guides/circuits-from-the-lab/max31855pmb1>`
