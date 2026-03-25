.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup360

.. _eval-adicup360:

EVAL-ADICUP360
===============

Precision Analog Microcontroller Development Platform with Dual 24-Bit ADCs.

Overview
--------

The :adi:`EVAL-ADICUP360` is an Arduino-like platform based on the
:adi:`ADuCM360 <ADUCM360>` fully integrated, 3.9 kSPS, 24-bit data
acquisition system that incorporates dual high-performance, multichannel
sigma-delta analog-to-digital converters (ADCs), a 32-bit ARM Cortex-M3
processor, and Flash/EE memory on a single chip. The platform has an
Arduino-Due compatible form factor and has two additional PMOD connectors.
It is accompanied by an Eclipse-based development environment.

.. figure:: eval-adicup360_ecosystem.png
   :align: center

   EVAL-ADICUP360 ecosystem overview showing the platform board, compatible
   shields, GitHub repository, and development environment

Key Features
~~~~~~~~~~~~~

- :adi:`ADuCM360 <ADUCM360>` precision analog microcontroller
- Dual 24-bit sigma-delta ADCs at 3.9 kSPS
- 32-bit ARM Cortex-M3 processor
- 128 KB Flash / 8 KB SRAM
- Arduino-Due compatible form factor
- Two PMOD connectors (SPI and I2C)
- On-board SWD debugger (OpenSDA platform, Freescale K20DX128)
- **DEBUG USB** -- For flash programming and debug interface
- **USER USB** -- Virtual serial port connection to ADuCM360
- DC power jack (7V to 12V) or USB powered

Base Board Hardware
--------------------

The EVAL-ADICUP360 base board consists of two basic blocks:

- A fully integrated, 3.9 kSPS, 24-bit data acquisition system with dual
  high-performance sigma-delta ADCs, a 32-bit ARM Cortex-M3 processor, and
  Flash/EE memory, realized on a single-chip **ADuCM360 microcontroller**.
- An on-board SWD interface, based on the OpenSDA platform, implemented with
  the **Freescale K20DX128 microcontroller**. This block allows using a free
  software development toolchain to program and debug the ADuCM360
  microcontroller part.

.. figure:: eval-adicup360_board.png
   :align: center

   EVAL-ADICUP360 base board layout (Rev 1.1) showing all components,
   connectors, and key functional blocks

Connectors
~~~~~~~~~~~

The following connectors are populated on the base board:

- **DC Power Jack** -- Core positive, accepts +7V to +12V DC supply voltage
- **DEBUG USB** -- Used for flash programming and debug interface
- **USER USB** -- Provides a virtual serial port connection to ADuCM360
  microcontroller
- **PMOD_SPI** -- 12-pin SPI PMOD connector
- **PMOD_I2C** -- 8-pin I2C PMOD connector
- **Six Arduino connectors** -- Arduino-Due compatible headers

.. figure:: eval-adicup360_connectors.png
   :align: center

   EVAL-ADICUP360 connector locations -- Arduino PWMH, PWML, Communication,
   Power, ADCL, ADCH headers, PMOD_SPI, PMOD_I2C, DEBUG USB, USER USB, and
   DC power jack

.. list-table:: PWMH Connector Pinout
   :header-rows: 1
   :widths: 10 15 40 15

   * - Pin
     - Pin Name
     - ADuCM360 Pin Function
     - Arduino Pin
   * - 10
     - SCL
     - P2.0/SCL/UARTCLK
     - SCL1
   * - 9
     - SDA
     - P2.1/SDA/UARTDCD
     - SDA1
   * - 8
     - AREF
     - VREF+
     - AREF
   * - 7
     - GND
     - AGND (Analog ground)
     - GND
   * - 6
     - SCK
     - P0.1/SCLK1/SCL/SIN
     - PWM13
   * - 5
     - MISO
     - P0.0/MISO1
     - PWM12
   * - 4
     - MOSI
     - P0.2/MOSI1/SDA/SOUT
     - PWM11
   * - 3
     - SS
     - P0.3/IRQ0/CS1
     - PWM10
   * - 2
     - P0.4
     - P0.4/RTS/ECLKO
     - PWM9
   * - 1
     - P0.5
     - P0.5/CTS/IRQ1
     - PWM8

.. list-table:: PWML Connector Pinout
   :header-rows: 1
   :widths: 10 15 40 15

   * - Pin
     - Pin Name
     - ADuCM360 Pin Function
     - Arduino Pin
   * - 8
     - PWM5
     - P2.2/BM
     - PWM7
   * - 7
     - PWM4
     - P1.4/PWM2/MISO0
     - PWM6
   * - 6
     - PWM3
     - P1.3/PWM1/DSR
     - PWM
   * - 5
     - PWM2
     - P1.2/PWM0/RI
     - PWM4
   * - 4
     - PWM1
     - P1.1/IRQ4/PWMTRIP/DTR
     - PWM3
   * - 3
     - PWM0
     - P1.0/IRQ3/PWMSYNC/EXTCLK
     - PWM2
   * - 2
     - TX
     - P0.7/POR/SOUT
     - TX0
   * - 1
     - RX
     - P0.6/IRQ2/SIN
     - RX0

Jumper Configuration
~~~~~~~~~~~~~~~~~~~~~

The board has several configurable jumpers. The image below highlights their
locations on the PCB.

.. figure:: eval-adicup360_jumpers.png
   :align: center

   EVAL-ADICUP360 jumper locations -- P12, REFnSel, J1, J2, J3, J4, and J5

**Jumper P12**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Configuration
     - Function
   * - Pin 1-2
     - ADuCM360 receives power from USB supply
   * - Pin 2-3
     - ADuCM360 receives power from external power supply through the DC
       power jack

**Jumper REFnSel**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Configuration
     - Function
   * - Installed
     - External VREF is connected to an on-board 2.5V reference
   * - Not Installed
     - External VREF can be applied via the Arduino connector

USB/Connector Multiplexer (Switches S1-S4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The four DIP switches (S1, S2, S3, S4) control how various pins from the
ADuCM360 are connected either to the Arduino headers or to the USB/serial
interface. This provides maximum flexibility for different shield
configurations.

.. figure:: eval-adicup360_switches.png
   :align: center

   EVAL-ADICUP360 DIP switch locations (S1, S2, S3, S4) for USB/connector
   multiplexing

The schematic below shows the signal routing architecture of the four
multiplexer switches. S1 and S3 route the UART0 RX/TX signals (P0.1, P0.2)
between the Arduino PWMH/SPI header and the DEBUG USB. S2 and S4 route the
UART1 TX/RX signals (P0.6, P0.7) between the Arduino PWML header and the
USER USB.

.. figure:: eval-adicup360_switch_schematic.png
   :align: center

   Switch multiplexer schematic -- S1/S3 route UART0 between Arduino PWMH
   and DEBUG USB; S2/S4 route UART1 between Arduino PWML and USER USB

Buttons
~~~~~~~~

The EVAL-ADICUP360 has two push buttons:

.. figure:: eval-adicup360_buttons.png
   :align: center

   EVAL-ADICUP360 button locations -- RESET and BOOT (user) buttons

- **RESET** -- Resets the ADuCM360 microcontroller
- **USER** -- User-configurable button connected to P0.5/CTS/IRQ1 (active
  low, directly tied to ADuCM360)

Getting Started
~~~~~~~~~~~~~~~~

To begin using the EVAL-ADICUP360, connect the DEBUG USB port to your
computer. The board will enumerate as a mass storage device (MBED drive) and
a debug COM port.

.. figure:: eval-adicup360_setup.png
   :align: center

   EVAL-ADICUP360 hardware setup -- connect via DEBUG USB for programming
   and debugging

Tools and Software
-------------------

CrossCore Embedded Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~

CrossCore Embedded Studio (CCES) is the primary development environment for
the EVAL-ADICUP360. It is a free Eclipse-based IDE from Analog Devices that
provides:

- Project creation, build, and debug support
- ADuCM36x Device Family Pack (DFP) with on-chip peripheral drivers
- CMSIS ARM Pack for Cortex-M3 support

Required software versions:

- CrossCore Embedded Studio 2.7.0 or higher
- ADuCM36x DFP 1.0.2 or higher
- CMSIS ARM Pack 4.3.0 or higher

The EVAL-ADICUP360 is also supported by third-party IDEs including IAR
Embedded Workbench and Keil MDK.

Programming Methods
~~~~~~~~~~~~~~~~~~~~

There are two ways to program the EVAL-ADICUP360:

1. **Drag and Drop** -- The simplest method. Connect the board via DEBUG USB
   and drag the prebuilt ``.bin`` file to the MBED drive that appears on your
   computer.
2. **Build, Compile, and Debug** -- Import the project into CrossCore
   Embedded Studio for full control over software customization and debugging.

Compatible Shield and PMOD Boards
-----------------------------------

The EVAL-ADICUP360 supports a wide range of Arduino shield and PMOD expansion
boards. The following boards have demo software and documentation available:

Accelerometer and Motion Sensing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`EVAL-ADXL362-ARDZ <eval-adxl362-ardz>` -- Ultralow power 3-axis
  MEMS accelerometer

Temperature Sensing
~~~~~~~~~~~~~~~~~~~~

- :ref:`EVAL-ADT7420-PMDZ <eval-adt7420-pmdz>` -- High accuracy digital
  temperature sensor

Weigh Scale
~~~~~~~~~~~~

- :ref:`EVAL-CN0216-ARDZ <eval-cn0216-ardz>` -- Weigh scale measurement

Gas and Chemical Sensing
~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`EVAL-CN0336-ARDZ <eval-cn0336-ardz>` -- Data acquisition for input
  current
- :ref:`EVAL-CN0338-ARDZ <eval-cn0338-ardz>` -- CO2 gas measurement
- :ref:`EVAL-CN0357-ARDZ <eval-cn0357-ardz>` -- CO toxic gas measurement
- :ref:`EVAL-CN0395-ARDZ <eval-cn0395-ardz>` -- Volatile organic compound
  (VOC) gas detection
- :ref:`EVAL-CN0396-ARDZ <eval-cn0396-ardz>` -- Dual toxic gas measurement
- :ref:`EVAL-CN0409-ARDZ <eval-cn0409-ardz>` -- Turbidity measurement
- :ref:`EVAL-CN0411-ARDZ <eval-cn0411-ardz>` -- Total dissolved solids
  measurement

Environmental and Agricultural Sensing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`EVAL-CN0397-ARDZ <eval-cn0397-ardz>` -- Visible light
  detection/measurement
- :ref:`EVAL-CN0398-ARDZ <eval-cn0398-ardz>` -- Soil moisture and pH
  measurement

Thermocouple Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`EVAL-CN0394-ARDZ <eval-cn0394-ardz>` -- Universal multichannel
  thermocouple measurement (analog output)

Design and Integration Files
------------------------------

- :adi:`EVAL-ADICUP360 Product Page <EVAL-ADICUP360>`
- `EVAL-ADICUP360 GitHub Repository <https://github.com/analogdevicesinc/EVAL-ADICUP360>`__
- `EVAL-ADICUP360 Schematics and Layout <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/eval-adicup360-designsupport.zip>`__

Documents
---------

- :adi:`ADuCM360 Datasheet <ADUCM360>`
- :adi:`EVAL-ADICUP360 Product Page <EVAL-ADICUP360>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
