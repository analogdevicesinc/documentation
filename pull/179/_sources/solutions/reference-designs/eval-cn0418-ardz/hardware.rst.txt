.. _eval-cn0418-ardz hardware:

Hardware Guide
==============

This section describes the hardware configuration and connector settings for
the :adi:`EVAL-CN0418-ARDZ <CN0418>` evaluation board.

Required Equipment
------------------

- :adi:`EVAL-CN0418-ARDZ <CN0418>` evaluation board
- :adi:`EVAL-ADICUP3029` base board
- PC with a USB port and Windows 7 (32-bit) or higher
- Serial terminal software (PuTTY, Tera Term, or similar)
- DC power supply (+12 V to +24 V / 1 A) or equivalent bench supply (optional)
- Precision voltage and current source (for output measurement)
- USB type A to micro-USB cable

.. figure:: images/cn0418_hw_setup.png
   :align: center
   :width: 600

   Board Setup of CN0418 and ADICUP3029

Connection Details
~~~~~~~~~~~~~~~~~~

- The EVAL-CN0418-ARDZ connects to the :adi:`EVAL-ADICUP3029` via Arduino
  headers.
- The EVAL-ADICUP3029 connects to the PC via USB cable.
- Terminal block **P1** is the power supply input (+24 V DC).
- Terminal blocks **P6** provide the quad-channel voltage output (-10 V to
  +10 V), current output (0 mA to 24 mA), and standard 4 mA to 20 mA HART
  compatible current outputs.

Power Supply Considerations and Configuration (P17)
-----------------------------------------------------

Terminal block **P17** is the power supply input (input range: +12 V to +36 V
DC). The EARTH terminal can be connected to an external earth connection, to
the GND terminal, or left floating if an external earth connection is not used.
The green power LED should light up when connected to a power supply.

.. figure:: images/cn0418_power_led.png
   :align: center
   :width: 500

   Power LED and Connector

Default Jumper and DIP Switch Configuration
--------------------------------------------

The default jumper position for **P9** and **P10** are shorted at position 1
and 2 while the two DIP switches **S3** and **S4** should be in the **ON**
state.

.. figure:: images/cn0418_switches.png
   :align: center
   :width: 500

   Default Switches Configuration

DAC and HART Chip Select Configuration (P9 and P10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Single Board
^^^^^^^^^^^^

If only a single board is used, connect jumpers P9 and P10 as shown below.

.. list-table::
   :header-rows: 1

   * - P9 Position (HART EN)
     - P9 Description
     - P9 Mode
     - P10 Position (DAC SYNC)
     - P10 Description
     - P10 Mode
   * - Pin 1 & Pin 2
     - Skip decoder
     - Single
     - Pin 1 & Pin 2
     - Skip decoder
     - Single

Multiple Boards
^^^^^^^^^^^^^^^

If more than one board is stacked (up to four), each board must be set to a
different DAC and HART select address. Connect jumpers P9 and P10 as shown
below, and ensure that the software is configured accordingly. On a given board,
set the DAC and HART address to the same position.

.. list-table::
   :header-rows: 1

   * - P9 Position
     - P9 Address
     - P10 Position
     - P10 Address
   * - Pin 4 & Pin 6
     - AIN2:AIN3 = 00
     - Pin 4 & Pin 6
     - AIN0:AIN1 = 00
   * - Pin 3 & Pin 5
     - AIN2:AIN3 = 01
     - Pin 3 & Pin 5
     - AIN0:AIN1 = 01
   * - Pin 7 & Pin 5
     - AIN2:AIN3 = 10
     - Pin 7 & Pin 5
     - AIN0:AIN1 = 10
   * - Pin 8 & Pin 6
     - AIN2:AIN3 = 11
     - Pin 8 & Pin 6
     - AIN0:AIN1 = 11

EEPROM Address Configuration (JP2, JP3, JP4)
----------------------------------------------

The EEPROM default address configuration of the board is "000". The EEPROM
I2C address can be configured from 000 to 111.

.. figure:: images/cn0418_eeprom_addr.png
   :align: center
   :width: 500

   Default EEPROM Address Configuration

EEPROM Write Protection (JP1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EEPROM WP (write protect) pin can be configured for single or multi-board
operation. The default connection of the WP pin is shorted to GND.

.. figure:: images/cn0418_eeprom_wp.png
   :align: center
   :width: 500

   EEPROM Write Protection Mode

.. list-table::
   :header-rows: 1

   * - JP1 Position
     - Description
   * - Pin 2 & Pin 3 (default)
     - Enable write protection (WP) -- single board operation
   * - Pin 2 & Pin 1
     - Control write protection (WP) -- multi-board operation

Analog Output Connection (P6)
-------------------------------

.. figure:: images/cn0418_output_terminals.png
   :align: center
   :width: 400

   16-Bit Voltage and Current Analog Output Terminals

Peripheral Connectors
----------------------

All connector pinouts for the EVAL-CN0418-ARDZ are described in the table
below.

.. list-table::
   :header-rows: 1
   :widths: 15 5 10 20 20

   * - Connector
     - Pin
     - Pin Name
     - ADuCM3029 Function
     - CN0418 Function
   * - Arduino DIO High
     - 1
     - SCL
     - I2C0_SCL / GPIO04
     - SCL (EEPROM)
   * -
     - 2
     - SDA
     - I2C0_SDA / GPIO05
     - SDA (EEPROM)
   * -
     - 3
     - AREF
     - VREF+
     - NC
   * -
     - 4
     - AGND
     - AGND
     - DGND
   * -
     - 5
     - SCLK
     - SPI0_CLK / GPIO00
     - DAC_SCLK (AD5755-1)
   * -
     - 6
     - MISO
     - SPI0_MISO / GPIO02
     - DAC_MISO_BUFF (AD5755-1)
   * -
     - 7
     - MOSI
     - SPI0_MOSI / GPIO01
     - DAC_MOSI (AD5755-1)
   * -
     - 8
     - CS
     - SPI0_CS1 / GPIO26
     - DAC_SYNC (AD5755-1)
   * -
     - 9
     - RDY
     - SPI0_RDY / GPIO30
     - HART_MULT_A0 (AD5700-1)
   * -
     - 10
     - IO28
     - GPIO28
     - HART_MUL_A1 (AD5700-1)
   * - Arduino DIO Low
     - 1
     - IO08
     - GPIO08
     - DAC_FAULT (AD5755-1)
   * -
     - 2
     - IO27
     - TMR1_OUT / GPIO27
     - AD5700_RTS (AD5700-1)
   * -
     - 3
     - IO33
     - TMR2_OUT / GPIO33
     - AD5700_CD_BUFF (AD5700-1)
   * -
     - 4
     - IO09
     - GPIO09
     - SW_TXD (AD5700-1)
   * -
     - 5
     - IO13
     - GPIO13
     - HW RXD (AD5700-1)
   * -
     - 6
     - IO15
     - GPIO15
     - NC
   * -
     - 7
     - TX
     - UART0_TX / GPIO10
     - NC
   * -
     - 8
     - RX
     - UART0_RX / GPIO11
     - NC
   * - Arduino Analog
     - 1
     - AIN0
     - ADC0_VIN0 / GPIO35
     - HART_COM_A0
   * -
     - 2
     - AIN1
     - ADC0_VIN1 / GPIO36
     - HART_COM_A1
   * -
     - 3
     - AIN2
     - ADC0_VIN2 / GPIO37
     - DAC_COM_A0
   * -
     - 4
     - AIN3
     - ADC0_VIN3 / GPIO38
     - DAC_COM_A1
   * -
     - 5
     - AIN4
     - ADC0_VIN4 / GPIO39
     - NC
   * -
     - 6
     - AIN5
     - ADC0_VIN5 / GPIO40
     - NC
   * - Arduino Power
     - 1
     - NC
     - --
     - NC
   * -
     - 2
     - IOREF
     - +3.3 V
     - IO_VREF (+3V3)
   * -
     - 3
     - RESET
     - SYS_HWRST_N
     - NC
   * -
     - 4
     - 3.3 V
     - +3.3 V
     - NC
   * -
     - 5
     - 5 V
     - +5 V
     - 5 V
   * -
     - 6
     - GND
     - DGND
     - GND
   * -
     - 7
     - GND
     - DGND
     - GND
   * -
     - 8
     - Vin
     - DC Barrel Jack (+7 V to +12 V)
     - +7.5 V

Advanced Setup -- Multiple Boards
----------------------------------

Up to four EVAL-CN0418-ARDZ boards can be controlled by a single Arduino or
EVAL-ADICUP3029 base board by using a simple control scheme. This control
scheme manages the SYNC, CD, and RX signals to avoid data conflicts.
