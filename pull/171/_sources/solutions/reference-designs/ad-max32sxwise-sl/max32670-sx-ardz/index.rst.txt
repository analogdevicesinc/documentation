.. _max32670-sx-ardz:

MAX32670-SX-ARDZ
================

Long Range Wireless Radio Development Platform
"""""""""""""""""""""""""""""""""""""""""""""""

Overview
--------

The :adi:`MAX32670-SX-ARDZ` base board features the MAX32670 high-reliability,
ultralow power microcontroller based on Arm Cortex-M4 processor, and
the SX1261 long range RF transceiver module.

The integrated RF transceiver supports a frequency range from 800 MHz
up to 960 MHz, making it suitable for high-performance flexible
platforms that wirelessly transmit encrypted data at long-range;
enabling a wide range of IoT applications using ADI sensing solutions.

Due to its low power consumption, this module is ideal for devices
running on small-sized batteries. The integrated Arm Cortex®-M4 32-bit
microcontroller can run entire RF stacks and has sufficient resources
available to run user applications.

.. figure:: max32670-sx-ardz_base_board.png

Features
~~~~~~~~

+-----------------------------------------------------------------------+
| MCU                                                                   |
+-----------------------------------------------------------------------+
| Arm Cortex-M4 core with FPU up to 100 MHz                             |
+-----------------------------------------------------------------------+
| 384 kB flash memory with error correction                             |
+-----------------------------------------------------------------------+
| 160 kB SRAM (128 kB with ECC enabled), optionally preserved in lowest |
| power modes                                                           |
+-----------------------------------------------------------------------+
| Compatible RTC resolution for long range wireless radio application   |
| for protocol timeout management                                       |
+-----------------------------------------------------------------------+
| Security                                                              |
+-----------------------------------------------------------------------+
| Available secure boot                                                 |
+-----------------------------------------------------------------------+
| Support cryptographic algorithms, including AES-128/192/256           |
+-----------------------------------------------------------------------+
| Power                                                                 |
+-----------------------------------------------------------------------+
| Ultralow power real time clock with integrated power switch           |
+-----------------------------------------------------------------------+
| With 300 nA power consumption during sleep mode                       |
+-----------------------------------------------------------------------+
| Long Range Radio                                                      |
+-----------------------------------------------------------------------+
| Supports FSK, GFSK, MSK, GMSK, and long range FHSS modulations        |
+-----------------------------------------------------------------------+
| Power output: +15 dBm transmit peak power                             |
+-----------------------------------------------------------------------+
| Programmable bit rate up to 62.5 kbps and 300 kbps                    |
+-----------------------------------------------------------------------+
| Supports sub-GHz ISM bands from 800 MHz to 960 MHz                    |
+-----------------------------------------------------------------------+
| High sensitivity: down to -148 dBm                                    |
+-----------------------------------------------------------------------+

Applications
~~~~~~~~~~~~

- Smart meters
- Supply chain and logistics
- Building automation
- Agricultural sensors
- Smart cities
- Retail store sensors
- Asset tracking
- Streetlights
- Parking sensors
- Environmental sensors

System Architecture
~~~~~~~~~~~~~~~~~~~

.. figure:: max32670-sx-ardz_block_diagram.png

Hardware Design
---------------

In order to use this base board, all hardware settings such as the
hardware peripheral connections, jumpers and UART switch configurations,
power configurations, connectivity options, and the USB and programming
connections are provided in this page. Links to the schematics and the
layout files are also available below.

Components and Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~

Peripheral Connectors
^^^^^^^^^^^^^^^^^^^^^

The following standard connectors are provided on the base board for
customer to use with external add-on modules:

.. figure:: max32670-sx-ardz_hardware_peripherals_top_view.png

+-----------------------------------+-----------------------------------+
| Connector Name                    | Function                          |
+-----------------------------------+-----------------------------------+
| DC Power Connector Header         | Input range from +4 V to +6 V DC  |
|                                   | supply voltage                    |
+-----------------------------------+-----------------------------------+
| Battery Holder                    | Battery holder for CR123A         |
+-----------------------------------+-----------------------------------+
| Cortex SWD Header                 | Used for flash programming and    |
|                                   | debug interface; also, provides a |
|                                   | virtual serial port connection to |
|                                   | MAX32670 microcontroller          |
+-----------------------------------+-----------------------------------+
| PMOD_SPI                          | 12-pin SPI PMOD connector         |
+-----------------------------------+-----------------------------------+
| PMOD_I2C                          | 8-pin I2C PMOD connector          |
+-----------------------------------+-----------------------------------+
| ESP32 Connector                   | ESP32 Devkit V1 connector         |
+-----------------------------------+-----------------------------------+
| Arduino Connectors                | Arduino Uno Rev3 compatible       |
|                                   | connectors                        |
+-----------------------------------+-----------------------------------+

MAX32670 MCU Pin Map
^^^^^^^^^^^^^^^^^^^^^

The pin map for the :adi:`MAX32670` is described in the table and its schematic diagram below.

.. csv-table::
   :file: MAX32670-MCU-Pin-Map.csv

.. figure:: max32670_mcu_pin_map.png

ESP32 Connector Pin Map
^^^^^^^^^^^^^^^^^^^^^^^^

All connector pinouts for the ESP32 Development Board are described in
the table and its schematic diagram below.

============ ============== ========================
**Pin Name** **Pin Number** **Pin Description**
EN           1              P0_27_32670
GPIO         2              P0_21_32670
GPIO         3              P0_23_32670
GPIO         4              P0_24_32670
GPIO         5              P0_25_32670
GPIO         6              P0_26_32670
GPIO         7              I2C2_SDA_32670
GPIO         8              I2C1_SCL_32670
GPIO         9              I2C1_SDA_32670
GPIO         10             I2C2_SCL_32670
HSPI CLK     11             SPI0_SCK_32670
HSPI MISO    12             SPI0_MISO_32670
HSPI MOSI    13             SPI0_MOSI_32670
GPIO         14
GPIO         15
GPIO         16
GND          17             GND
VIN          18             VOUT_3130(def)/VCC_31334
============ ============== ========================

============ ============== ===================
**Pin Name** **Pin Number** **Pin Description**
VSPI MOSI    1              SPI1_MOSI_32670
I2C SCL      2              I2C0_SCL_32670
UART 0 TX    3              UART0A_TX_32670
UART 0 RX    4              UART0A_RX_32670
I2C SDA      5              I2C0_SDA_32670
VSPI MISO    6              SPI1_MISO_32670
VSPI CLK     7              SPI1_SCK_32670
VSPI CS0     8              SPI1_SS0_32670
UART 2 TX    9              UART1A_TX_32670
UART 2 RX    10             UART1A_RX_32670
RTC          11             UART0A_CTS_32670
RTC          12             UART0A_RTS_32670
RTC          13             SPI0_SS0_32670
RTC          14             UART1A_CTS_32670
SDI          15
SDO          16
SCK          17
3V3          18             VOUT_3130
============ ============== ===================

.. figure:: max32670_esp32_connectors_pin_map.png

Arduino Connector Pin Map
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: arduino-pin-map.csv

.. figure:: max32670_arduino_connectors_pin_map.png

PMOD Connector Pin Map
^^^^^^^^^^^^^^^^^^^^^^

================================== ============== ============
**Net Name**                       **Pin Number** **Pin Name**
**SPI PMOD**
SPI0_SS0_32670(def)/SPI1_SS0_32670 1              SS
SPI0_MOSI_32670                    2              MOSI
SPI0_MISO_32670                    3              MISO
SPI0_SCK_32670                     4              SCK
GND                                5              GND
1V8_SSB3/3V3_SSB3(def)/VOUT_3130   6              VCC
P0_21_32670                        7              INT
P0_26_32670                        8              RST
SWDIOB_32670                       9              IO7
P0_23_32670                        10             IO8
GND                                11             GND
1V8_SSB3/3V3_SSB3(def)/VOUT_3130   12             VCC
================================== ============== ============

================================ ============== ============
**Net Name**                     **Pin Number** **Pin Name**
**I2C PMOD**
I2C1_SCL_32670/I2C2_SCL_32670    1              SCL
I2C1_SCL_32670/I2C2_SCL_32670    2              SCL
I2C1_SDA_32670/I2C2_SDA_32670    3              SDA
I2C1_SDA_32670/I2C2_SDA_32670    4              SDA
GND                              5              GND
GND                              6              GND
1V8_SSB3/3V3_SSB3(def)/VOUT_3130 7              VCC
1V8_SSB3/3V3_SSB3(def)/VOUT_3130 8              VCC
================================ ============== ============

.. figure:: max32670_pmod_connectors_pin_map.png

Wireless Connectivity Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This board has two wireless connectivity options available to use for
Internet of Things (IoT) applications:

1. On-board Chip Antenna

2. External Antenna connected through SMA connector

.. figure:: max32670_pmod_connectors_pin_map.png

.. figure:: max32670-sx-ardz_wireless_antenna.png

These options can be configured by populating C63 with 39 pF for the
external antenna or R156 with 0 Ω for on-board RF chip antenna with the
center frequency tuned at 915 MHz.

Long Range Radio Connectivity Chipset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The MAX32670-SX-ARDZ utilizes the SX1261 long range radio connectivity
chipset from Semtech. This chipset comes complete with the full
low-power, wide area networking protocol built on top of the long range
radio modulation technique.

.. figure:: max32670-sx-ardz_lora_chipset.png

The :adi:`MAX32670` communicates to the SX1261 using the SPI bus,
so the users will need to send long range commands and data over SPI bus.
Library functions calls have been specifically designed to be used with
the MAX32670 and SX1261 using SPI bus.

The pins that connect the MAX32670 and the SX1261 are as follows:

.. csv-table::
   :file: max32670-sx1261-connection.csv

.. figure:: sx1261_pins.png

Input Power Source Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two (2) ways of powering the eval board, and user may use any
combination of power sources.

1. Terminal Block - can be used when an external supply is connected to
   the Terminal block connector P11.

2. Battery Powered - can be used when batteries are connected to BT1
   connector on the back of the board.

   .. figure:: power_source_options.png

Each of the different power modes, provides a different level of control
and flexibility. You can find a matrix table of the different power
modes and their general function here:

+-----------------+-----------------+-----------------+-----------------+
| Power Source    | Voltage Rails   | Peripherals     | Function        |
|                 | Provided        | Powered         |                 |
+-----------------+-----------------+-----------------+-----------------+
| Terminal Block  | 3 V to 6 V      | MAX32670,       | able to supply  |
| (P11)           |                 | SPI and I2C     | ALL voltages    |
|                 |                 | PMODs, ESP32    | any peripheral  |
|                 |                 | connectors,     | might need      |
|                 |                 | Arduino         |                 |
|                 |                 | connectors,     |                 |
|                 |                 | SX1261 chip     |                 |
+-----------------+-----------------+-----------------+-----------------+
| Battery Power   | 3 V and 6 V     | MAX32670,       | able to supply  |
| (BT1)           |                 | SPI and I2C     | ALL voltages    |
|                 |                 | PMODs, ESP32    | any peripheral  |
|                 |                 | connectors,     | might need      |
|                 |                 | Arduino         |                 |
|                 |                 | connectors,     |                 |
|                 |                 | SX1261 chip     |                 |
+-----------------+-----------------+-----------------+-----------------+

Reset Button
^^^^^^^^^^^^

.. figure:: max32670-sx-ardz_reset.png

====== ======================================================
Button Function
S1     provides a hardware RESET to MAX32670 microcontroller.
====== ======================================================

LED Indicators
^^^^^^^^^^^^^^

The base board has five LEDs: **DS1**, **DS2**, **DS3**, **DS4**, and
**DS5**.

.. figure:: max32670-sx-ardz_led_indicator.png

+-----------------------------------+-----------------------------------+
| Button                            | Function                          |
+-----------------------------------+-----------------------------------+
| DS1                               | used as a LED indicator to one of |
|                                   | the GPIO of the MAX32670, P0.28.  |
+-----------------------------------+-----------------------------------+
| DS2                               | used as a LED indicator to one of |
|                                   | the GPIO of the MAX32670, P0.29.  |
+-----------------------------------+-----------------------------------+
| DS3                               | used as a LED indicator for the   |
|                                   | voltage output from the power     |
|                                   | supply.                           |
+-----------------------------------+-----------------------------------+
| DS4                               | used as a LED indicator for the   |
|                                   | voltage output from the MAX31334. |
+-----------------------------------+-----------------------------------+
| DS5                               | used as a LED indicator for the   |
|                                   | 3.3 V voltage output from the     |
|                                   | MAX3130.                          |
+-----------------------------------+-----------------------------------+

Programming Connectors
^^^^^^^^^^^^^^^^^^^^^^

This board uses SWD Interface and uses the :adi:`MAX32625PICO` board for
programming the on-board MCUs. See the `MAX32625PICO <https://www.analog.com//media/en/technical-documentation/data-sheets/MAX32625PICO.pdf>`__
page for more details.

- P1 - SWD Interface used to program the MAX32670

.. figure:: max32670-sx-ardz_swd_connector.png

.. figure:: max32670-sx-ardz_swd_connector.png

====================== ==============
**Connected to**       **Pin Number**
1V8_SSB0/3V3_SSB3(def) 1
SWDIO_32670            2
GND                    3
SWDCLK_32670           4
GND                    5
UART0A_TX_32670        6
-                      7
UART0A_RX_32670        8
-                      9
RSTN_32670             10
====================== ==============

The connector used are based off the 10-pin ARM Cortex standard pinout
(0.05“ pin spacing). That pinout is common to both JTAG and SWD debug
modes and is depicted in the following image.

.. figure:: jtag_swd_10_connector.png

The debugger board will need to be **plugged in via the USB port** in
order to program any board.

In order to program the MAX32670 node board, that board must be
powered by one (1) CR123A battery or by an external power supply
through P11. Otherwise, there will be no connection between the two
boards.

Applications
------------

The :adi:`MAX32670-SX-ARDZ` Base Board can be used with the compatible ADI-developed
sensor nodes such as the:

- :adi:`EV-STRUCTURAL-ARDZ` for Structural Monitoring
- :adi:`EV-FLOWMETER-ARDZ` for Flow Rate Metering
- :adi:`EV-ADE9000SHIELDZ` for Electric Metering

Using these platforms together enables users to design solutions based
on low-power, long range proprietary radio communication technique.

To learn more about the Long Range Wireless Radio solution developed
by Analog Devices, visit the AD-MAX32SXWISE-SL Long Range Wireless
Radio Development Kit User Guide.

System Setup
------------

PHASE 1: Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~

Note that this setup only applies for MAX32670-SX-ARDZ Base Board. Users may use
a different base board or microcontroller, however the firmware built for this
demo application cannot be used as this is specifically designed for the
MAX32670-SX-ARDZ.

Equipment Needed
^^^^^^^^^^^^^^^^

- One (1) :adi:`MAX32670-SX-ARDZ` Base Board
- One (1) Sensor Node, any of these:
    - :adi:`EV-STRUCTURAL-ARDZ`, :adi:`EV-FLOWMETER-ARDZ`, :adi:`EV-ADE9000SHIELDZ`
- One (1) MAX32625PICO Rapid Development Platform with 10-pin ribbon cable
  with :git-max32625pico-firmware-images:`firmware image <raw+master:bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin>`
- One (1) CR123A Battery or any equivalent external DC power supply (+3V to +4.7V).
  **Note that this is not included in the kit**
- One (1) Micro USB to USB cable
- Host PC (Windows 10 or later)

.. figure:: hardware_setup.png

#.  Insert one CR123A battery (3V to 4.7V) into the battery holder
    (BT1 connector) of the :adi:`MAX32670-SX-ARDZ` Base Board.

    **Make sure to check for the battery polarity in
    the BT1 connector, refer to the figure below. The DS3 LED will light up
    indicating that you have inserted the battery correctly and that power is
    provided in the base board.**

    .. figure:: base_board_with_battery.png

#.  Connect one **Sensor Node** to the :adi:`MAX32670-SX-ARDZ` Base Board
    by aligning the corresponding Arduino headers on each board.

    You do not have to set up the three sensor nodes altogether, just choose **one**
    from the available sensors in the kit:

    - :adi:`EV-STRUCTURAL-ARDZ` for Structural Monitoring
    - :adi:`EV-FLOWMETER-ARDZ` for Flow Rate Metering
    - :adi:`EV-ADE9000SHIELDZ` for Electric Metering

    .. tip::

      Make sure that the MAX32625PICO programming adapter has been flashed with
      the correct image before connecting it to the MAX32670-LR-ARDZ Base
      Board.

**How to flash the firmware image in the MAX32625PICO**

#. Download the firmware image:
   :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32670 <raw+master:bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin>`
#. Do not connect the MAX32625PICO to the :adi:`MAX32670-LR-ARDZ` Base Board yet.
#. Connect the MAX32625PICO to the Host PC using the micro USB to USB cable.
#. Press the button on the MAX32625PICO. **(Do not release the button until the
   MAINTENANCE drive is mounted)**.
#. Release the button once the MAINTENANCE drive is mounted.
#. Drag and drop (to the MAINTENANCE drive) the firmware image.
#. After a few seconds, the MAINTENANCE drive will disappear and be replaced by
   a drive named DAPLINK. This indicates that the process is complete, and the
   MAX32625PICO can now be used to flash the firmware of the
   :adi:`MAX32670-LR-ARDZ` Base Board.

#. Connect the :adi:`MAX32625PICO` programming adapter to the
   Host PC using the micro USB to USB cable.

   .. figure:: max32670-sx-ardz_to_maxpico.png

**Once you have completed this setup, proceed to PHASE 2 found in**
:dokuwiki:`ADI Long Range Wireless Radio Software User Guide </resources/eval/user-guides/longrangewirelessradio/software>`.

Resources
---------

- :adi:`MAX32670 Product Page <MAX32670>`
- :adi:`MAX77675 Product Page <MAX77675>`
- :adi:`MAX31334 Product Page <MAX31334>`
- :adi:`LTC3130 Product Page <LTC3130>`
- :ref:`AD-MAX32SXWISE-SL: Long Range Wireless Radio Development Kit based on
  MAX32670 MCU and SX1261 RF Transceiver <ad-max32sxwise-sl>`
- :ref:`EV-STRUCTURAL-ARDZ Sensor for Structural Monitoring <ev-structural-ardz>`
- :ref:`EV-FLOWMETER-ARDZ Sensor for Flow Rate Metering <ev-flowmeter-ardz>`
- :dokuwiki:`EV-ADE9000-SHIELDZ Sensor for Electric Metering </resources/eval/user-guides/eval-ade9000shieldz/sensor_node/demo>`

Design and Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   :download:`MAX32670-SX-ARDZ Design Support Package Rev. C <max32670-sx-ardz-designsupport.zip>`

   - Schematic
   - Bill of Materials
   - Layout
   - Fabrication Files

Help and Support
~~~~~~~~~~~~~~~~

For questions and more information about this product, connect with us through
the :ez:`Analog Devices Engineer Zone </>`.
