.. _pmd-ard-intz:

PMD-ARD-INTZ
=============

Arduino PMOD Adapter Board.

Overview
--------

Arduino interface is found on many development platforms and is used on many
prototype designs. The Pmod standard is a 6, 8, or 12-pin standard that carries
GPIO and/or serial communication protocols. PMD-ARD-INTZ enables four Pmod
modules to interface with :adi:`EVAL-ADICUP3029` / :adi:`EVAL-ADICUP360`
development boards or any equivalent Arduino MCU boards. Out of the four Pmod
ports, two are configured as SPI Pmod, one is I2C Pmod, and the other one can
be configured as either SPI or UART Pmod.

.. figure:: board.png
   :align: center
   :width: 650px

   PMD-ARD-INTZ adapter board

General Setup
-------------

Power Source Settings
~~~~~~~~~~~~~~~~~~~~~

The circuit is powered either by the voltages coming from the Arduino headers
or the input DC voltage supplied from the barrel jack of the MCU baseboard.
Switch S1 is used to choose where the system voltages (3.3 V and 5 V) are
sourced from.

Positioning S1 to **ARD** will cause the board to use voltage supplied from the
MCU baseboard headers. Positioning S1 to **LDO** uses the DC voltage supplied
from the barrel jack of the MCU baseboard, then regulated by
:adi:`LT1763`-3.3 and :adi:`LT1763`-5 to provide the 3.3 V and 5 V system
voltage respectively.

A green LED (labeled DS1) should be lit to indicate that the board is powered
up.

.. important::

   Recommended external supply voltage is 7 to 13 volts.

.. figure:: powersource.png
   :align: center
   :width: 200px

   Power source switch S1

Logic Voltage Settings
~~~~~~~~~~~~~~~~~~~~~~

Each Pmod port has bidirectional voltage level translators. This enables
compatibility with Pmod modules and MCU baseboards that have different logic
voltage levels.

.. figure:: logic_voltage.png
   :align: center
   :width: 300px

   Bidirectional voltage level translators

The logic voltage level of each Pmod port can be set to either 3.3 V or 5 V
using the shunt connectors P4, P5, P6, and P7.

.. figure:: vlogic.png
   :align: center
   :width: 250px

   Pmod port logic voltage selection shunts

Meanwhile, the logic voltage source of the MCU baseboard can be chosen from the
IOREF from the MCU baseboard header and the 3.3 V and 5 V system voltages
using the shunt connector between P22 and P21 (encircled blue in Fig D).
Preferably, this should be set to IOREF to ensure a proper voltage setting.

.. figure:: ioref.png
   :align: center
   :width: 200px

   MCU baseboard IOREF selection

Reset Logic Active State
~~~~~~~~~~~~~~~~~~~~~~~~

The reset button (S2) on PMD-ARD-INTZ resets the MCU baseboard and all of the
Pmod ports simultaneously. By default, the reset pins are **Active Low** and
can be changed to **Active High** using solder jumpers JP1, JP2, JP3, JP4 for
the Pmod ports and JP5 for the MCU.

.. figure:: reset.png
   :align: center
   :width: 400px

   Reset logic solder jumper configuration

Pmod Interface Types
--------------------

The Pmod connectors on the PMD-ARD-INTZ follow the latest
`Digilent Pmod Interface Specifications 1.2.0 <https://reference.digilentinc.com/_media/reference/pmod/pmod-interface-specification-1_2_0.pdf>`__.
Pin assignments are adapted from Arduino UNO pin assignments. Different MCU
baseboards have different pinouts. If a different MCU baseboard is used, use the
Arduino UNO pinout as a reference to determine the proper pin number for your
MCU baseboard.

SPI Ports
~~~~~~~~~

Pmod ports (P11, P12, and P13) follow the expanded SPI interface. P11 and P12
are dedicated SPI ports while P13 can be configured to either expanded SPI or
expanded UART. To configure P13 as expanded SPI, set the shunt connectors P8,
P9, and P10 as shown below.

.. list-table:: SPI Port Pinout
   :header-rows: 1
   :widths: 10 20 20 20

   * - Pin No.
     - P11: SPI 0
     - P12: SPI 1
     - P13: SPI 2
   * - 1
     - D10 (CS)
     - D9 (CS)
     - D8 (CS)
   * - 2
     - D11 (MOSI)
     - D11 (MOSI)
     - D11 (MOSI)
   * - 3
     - D12 (MISO)
     - D12 (MISO)
     - D12 (MISO)
   * - 4
     - D13 (SCK)
     - D13 (SCK)
     - D13 (SCK)
   * - 5
     - GND
     - GND
     - GND
   * - 6
     - VCC
     - VCC
     - VCC
   * - 7
     - D6 (GPIO/INT)
     - D5 (GPIO/INT)
     - D4 (GPIO/INT)
   * - 8
     - RST
     - RST
     - RST
   * - 9
     - A5 (GPIO/CS2)
     - A3 (GPIO/CS2)
     - A1 (GPIO/CS2)
   * - 10
     - A4 (GPIO/CS3)
     - A2 (GPIO/CS3)
     - A0 (GPIO/CS3)
   * - 11
     - GND
     - GND
     - GND
   * - 12
     - VCC
     - VCC
     - VCC

.. figure:: p13_spi.png
   :align: center
   :width: 200px

   P13 configured as SPI (shunt connector positions)

I2C Port
~~~~~~~~

Pmod port (P16) is designed to interface with both old and new I2C modules. The
older versions of I2C Pmod (2x4 connector) should be attached to pins 3--4 and
9--10 of P16 and new versions of I2C Pmod (1x6 connector) should be attached
to pins 1--6 or pins 7--12 of P16 as shown in the table below.

.. list-table:: I2C Port Pinout (P16)
   :header-rows: 1
   :widths: 10 20 20

   * - Pin No.
     - P16: New I2C
     - P16: Old I2C
   * - 1
     - D3 (INT)
     - \-
   * - 2
     - RST
     - \-
   * - 3
     - D19 (SCL)
     - D19 (SCL)
   * - 4
     - D18 (SDA)
     - D18 (SDA)
   * - 5
     - GND
     - GND
   * - 6
     - VCC
     - VCC
   * - 7
     - D3 (INT)
     - \-
   * - 8
     - RST
     - \-
   * - 9
     - D19 (SCL)
     - D19 (SCL)
   * - 10
     - D18 (SDA)
     - D18 (SDA)
   * - 11
     - GND
     - GND
   * - 12
     - VCC
     - VCC

Pull-up resistors (4.7 kOhm) for SCL and SDA lines are also provided. Apply a
short on solder jumpers P14, P15, P17, and P18 to use the pull-up resistors.

.. figure:: i2c_pullup.png
   :align: center
   :width: 300px

   I2C pull-up resistor solder jumpers

UART Port
~~~~~~~~~

Pmod port (P13) can be reconfigured between an expanded SPI and expanded UART.
To configure P13 as expanded UART, set the shunt connectors P8, P9, and P10.

.. list-table:: UART Port Pinout (P13)
   :header-rows: 1
   :widths: 10 30

   * - Pin No.
     - P13: UART
   * - 1
     - D8 (CTS)
   * - 2
     - D1 (RX)
   * - 3
     - D0 (TX)
   * - 4
     - D2
   * - 5
     - GND
   * - 6
     - VCC
   * - 7
     - D4 (GPIO/INT)
   * - 8
     - RST
   * - 9
     - A1 (GPIO)
   * - 10
     - A0 (GPIO)
   * - 11
     - GND
   * - 12
     - VCC

.. figure:: p13_uart.png
   :align: center
   :width: 200px

   P13 configured as UART (shunt connector positions)

Schematic, PCB Layout, Bill of Materials
-----------------------------------------

`PMD-ARD-INTZ Design & Integration Files <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/pmd-ard-intz-designsupport.zip>`__

- Schematic
- PCB Layout
- Bill of Materials
- Allegro Project

Additional Information
----------------------

- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`
- :adi:`EVAL-ADICUP360 Product Page <EVAL-ADICUP360>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
