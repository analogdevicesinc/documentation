.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029

.. _eval-adicup3029:

EVAL-ADICUP3029
================

Ultra-Low Power ARM Cortex-M3 IoT Development Platform.

Overview
--------

The :adi:`EVAL-ADICUP3029` is an Arduino Uno form factor compatible platform
based on the industry-leading ultra-low power :adi:`ADuCM3029 <ADUCM3029>`
32-bit ARM Cortex-M3 microcontroller. The platform is designed to be a
development and prototyping vehicle to get customer ideas from concept to
production with minimal risk and faster time to market.

The EVAL-ADICUP3029 is designed for IoT (Internet of Things) applications in
mind, and therefore comes with on-board **Wi-Fi** and **Bluetooth 5.0**
capabilities. A free version of CrossCore Embedded Studios (an Eclipse-based
Analog Devices Interactive Development Environment) is supplied to the
customer for debugging and application development. Add-on hardware modules,
MCU drivers, and software application examples help form a complete ecosystem
that customers can leverage into their final product.

.. figure:: adicup3029_ecosystem_collage.png
   :align: center

   EVAL-ADICUP3029 ecosystem with compatible shields and PMOD boards

Key Features
~~~~~~~~~~~~~

- :adi:`ADuCM3029 <ADUCM3029>` ultra-low power ARM Cortex-M3 microcontroller
- On-board **Bluetooth 5.0** module (EM9304)
- On-board **Wi-Fi** module (ESP8266)
- Arduino Uno Rev3 compatible connectors
- 12-pin SPI PMOD connector
- 8-pin I2C PMOD connector
- 4-pin I2C Grove connector
- DAPLink interface for drag-and-drop programming
- On-board SWD debugger (Freescale MK20DX128)
- DC power jack (7V to 12V) or USB powered
- Ultra-low power measurement capabilities

Base Board Hardware
--------------------

The EVAL-ADICUP3029 base board consists of two basic blocks:

- An ultra-low power, 32-bit ARM Cortex-M3 processor, on a single-chip
  **ADuCM3029 microcontroller**.
- An on-board serial wire download (SWD) interface, implemented with the
  **Freescale MK20DX128 microcontroller**. This block allows the Freescale
  device to act as an on-board debugger, so you do not need additional
  external hardware to program or debug your ADuCM3029 applications.

.. figure:: adicup3029_block_diagram.png
   :align: center

   EVAL-ADICUP3029 block diagram

Peripheral Connectors
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: adicup3029_layout_blank_revc.png
   :align: center

   EVAL-ADICUP3029 board layout showing peripheral connectors

The following standard connectors are provided on the base board for use with
external add-on modules:

- **DC Power Jack** -- Core positive, accepts +7V to +12V DC supply voltage
- **USB** -- Used for flash programming and debug interface; also provides a
  virtual serial port connection to ADuCM3029 microcontroller
- **PMOD_SPI** -- 12-pin SPI PMOD connector
- **PMOD_I2C** -- 8-pin I2C PMOD connector
- **Grove Connector** -- 4-pin I2C Grove connector
- **Arduino Connectors** -- Arduino Uno Rev3 compatible connectors

.. list-table:: Arduino DIO High Connector Pinout
   :header-rows: 1
   :widths: 10 15 35 15

   * - Pin
     - Pin Name
     - ADuCM3029 Pin Function
     - Port No.
   * - 1
     - SCL
     - I2C0_SCL/GPIO04
     - P0_04
   * - 2
     - SDA
     - I2C0_SDA/GPIO05
     - P0_05
   * - 3
     - AREF
     - VREF+
     -
   * - 4
     - AGND
     - AGND (Analog ground)
     -
   * - 5
     - SCLK
     - SPI0_CLK/SPT0_BCLK/GPIO00
     - P0_00
   * - 6
     - MISO
     - SPI0_MISO/SPT0_BD0/GPIO02
     - P0_02
   * - 7
     - MOSI
     - SPI0_MOSI/SPT0_BFS/GPIO01
     - P0_01
   * - 8
     - CS
     - SPI0_CS1/SYS_CLKIN/SPI1_CS3/GPIO26
     - P1_10
   * - 9
     - RDY
     - SPI0_RDY/GPIO30
     - P1_14
   * - 10
     - IO28
     - GPIO28
     - P1_12

.. list-table:: Arduino DIO Low Connector Pinout
   :header-rows: 1
   :widths: 10 15 35 15

   * - Pin
     - Pin Name
     - ADuCM3029 Pin Function
     - Port No.
   * - 1
     - IO08
     - BPR0_TONE_N/GPIO08
     - P0_08
   * - 2
     - IO27
     - TMR1_OUT/GPIO27
     - P1_11
   * - 3
     - IO33
     - XINT0_WAKE3/TMR2_OUT/GPIO33
     - P2_01
   * - 4
     - IO09
     - BPR0_TONE_P/SPI2_CS1/GPIO09
     - P0_09
   * - 5
     - IO13
     - XINT0_WAKE2/GPIO13
     - P0_13
   * - 6
     - IO15
     - XINT0_WAKE0/GPIO15
     - P0_15
   * - 7
     - TX
     - UART0_TX/GPIO10
     - P0_10
   * - 8
     - RX
     - UART0_RX/GPIO11
     - P0_11

Wireless Connectivity Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Bluetooth Low Energy Chipset**

The EVAL-ADICUP3029 has an on-board EM9304 Bluetooth 5.0 chipset. This
module enables Bluetooth Low Energy communication with smart devices for
data visualization and control.

.. figure:: adicup3029_ble_layout_revc.png
   :align: center

   EVAL-ADICUP3029 Bluetooth Low Energy (BLE) chipset layout

**Wi-Fi Module**

The EVAL-ADICUP3029 supports the ESP8266 Wi-Fi module, which connects via
the P1 connector. This enables MQTT-based communication over TCP/IP for
cloud connectivity applications.

.. figure:: adicup3029_wifi_connector_revc.png
   :align: center

   EVAL-ADICUP3029 Wi-Fi module connector (P1) layout

UART Switch (S2)
~~~~~~~~~~~~~~~~~

.. figure:: adicup3029_uart_switch_layout_revc.png
   :align: center

   EVAL-ADICUP3029 UART switch (S2) location on board

The S2 switch selects the UART routing on the board:

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Function
     - Position
     - Description
   * - USB Port
     - Left
     - Routes UART to the USB connector (P10) for virtual serial terminal
       communication with a PC
   * - Arduino Pins
     - Middle
     - Routes UART to the Arduino connector (P7) for interfacing with
       Arduino shields that communicate via UART
   * - Wi-Fi Module
     - Right
     - Routes UART to the Wi-Fi module connector (P1) for communicating
       with the ESP8266 Wi-Fi module

Power Switch (S1)
~~~~~~~~~~~~~~~~~~

The S1 switch selects the power source:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Position
     - Function
   * - USB
     - Board powered from USB connection
   * - DC
     - Board powered from DC power jack (7V to 12V)

Push Buttons
~~~~~~~~~~~~~

.. figure:: adicup3029_buttons_layout_revc.png
   :align: center

   EVAL-ADICUP3029 push button locations

The EVAL-ADICUP3029 base board provides three buttons:

- **3029_RESET** -- Provides a hardware reset to the ADuCM3029 microcontroller.
  Also used to invoke the debug emulator's Maintenance mode (hold during
  power cycle).
- **3029_BOOT** -- When held during reset, the ADuCM3029 enters UART download
  mode via P0_10 and P0_11, allowing programming via the CrossCore Serial
  Flash Programmer tool.
- **WIFI_RESET** -- Provides a hardware reset to the ESP8266 Wi-Fi module.

Power Consumption Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The board includes provisions for measuring the power consumption of the
ADuCM3029 microcontroller. By removing the shunt at jumper **P18**, a
current meter can be inserted into the power supply path to accurately
measure the current draw of all +3.3V rails on the board (including the
Arduino connectors, Grove connector, SPI PMOD, I2C PMOD, BLE, and Wi-Fi).

.. figure:: adicup3029_current_measure_with_meter_revc.png
   :align: center

   EVAL-ADICUP3029 power consumption measurement setup using jumper P18

.. note::

   The on-board debugger, level translator, USB connector, JTAG/SWD,
   external power connector, and power management devices are **not included**
   when measuring the current from jumper P18.

Programming Connectors
~~~~~~~~~~~~~~~~~~~~~~~~

There are three connectors on the EVAL-ADICUP3029 used for programming:

- **P11** -- JTAG interface used to program the MK20DX128VFM5 (debugger MCU)
- **P12** -- SWD interface used to program the ADuCM3029
- **P14** -- SWD interface used to program the ADuCM3029

.. figure:: adicup3029_jtag_swd_connectors_layout_revc.png
   :align: center

   EVAL-ADICUP3029 JTAG/SWD programming connector locations

All three connectors use the 10-pin ARM Cortex standard pinout (0.05" pin
spacing), common to both JTAG and SWD debug modes.

Stand-Alone Mode
~~~~~~~~~~~~~~~~~

The EVAL-ADICUP3029 can operate in stand-alone mode by snapping off the
debugger board along the perforation provided. In this mode, the board can
be powered from batteries connected to the BT1 connector on the back of
the board, and runs the last programmed application autonomously.

.. figure:: adicup3029_hw_whole_front_snap_point_revb.png
   :align: center

   EVAL-ADICUP3029 full board showing snap-off perforation point

.. figure:: adicup3029_hw_split_front_revb.png
   :align: center

   EVAL-ADICUP3029 debugger board (left) and node board (right) after
   separation

Once apart, the debugger board can be reconnected to the node board using a
standard 10-pin ARM JTAG/SWD ribbon cable through connector P14.

.. figure:: adicup3029_hw_split_ribboned_together_revb.png
   :align: center

   EVAL-ADICUP3029 debugger and node boards connected via ribbon cable

.. important::

   The debugger board must be plugged in via USB to program any board. The
   node board must be powered by two AAA batteries with the power switch in
   the BATT position. Once the two boards are split apart, they cannot be
   reconnected to their previous configuration.

Tools and Software
-------------------

CrossCore Embedded Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~

CrossCore Embedded Studio (CCES) is the primary development environment for
the EVAL-ADICUP3029. It is a free Eclipse-based IDE from Analog Devices that
provides:

- Project creation, build, and debug support
- ADuCM302x Device Family Pack (DFP) with on-chip peripheral drivers
- ADICUP3029 Board Support Package (BSP)
- Sensor application software driver packs

Required software versions:

- CrossCore Embedded Studio 2.6.0 or higher
- ADuCM302x DFP 2.0.0 or higher
- ADICUP3029 BSP 1.0.0 or higher

The EVAL-ADICUP3029 is also supported by third-party IDEs including IAR
Embedded Workbench and Keil MDK.

Programming Methods
~~~~~~~~~~~~~~~~~~~~

There are two ways to program the EVAL-ADICUP3029:

1. **Drag and Drop** -- The simplest method. Connect the board via USB and
   drag the prebuilt ``.hex`` file to the DAPLink drive that appears on your
   computer.
2. **Build, Compile, and Debug** -- Import the project into CrossCore
   Embedded Studio for full control over software customization and debugging.

Hardware Drivers and USB Storage Modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After connecting the EVAL-ADICUP3029 to a computer via USB, the DAPLink
interface provides:

- A mass storage device for drag-and-drop programming
- A serial port for UART communication
- An SWD debug interface for CrossCore Embedded Studio

Compatible Shield and PMOD Boards
-----------------------------------

The EVAL-ADICUP3029 supports a wide range of Arduino shield and PMOD
expansion boards. The following boards have demo software and documentation
available:

Accelerometer and Motion Sensing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`EVAL-ADXL362-ARDZ <eval-adxl362-ardz>` -- Ultralow power 3-axis
  MEMS accelerometer (Wi-Fi demo)
- :ref:`EVAL-ADXL372-ARDZ <eval-adxl372-ardz>` -- Ultralow power +/-200 g
  impact sensor (Bluetooth demo)
- :ref:`EVAL-ADXL313Z <eval-adxl313z>` -- Low power 3-axis accelerometer
- :ref:`EVAL-ADXRS290-PMDZ <eval-adxrs290-pmdz>` -- Dual-axis MEMS gyroscope
  (CLI demo)

Temperature and Environmental Sensing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`EVAL-ADT7420-PMDZ <eval-adt7420-pmdz>` -- High accuracy digital
  temperature sensor

Analog/Digital Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`EVAL-AD5592R-PMDZ <eval-ad5592r-pmdz>` -- Configurable 8-channel
  ADC/DAC
- :ref:`EVAL-AD5593R-PMDZ <eval-ad5593r-pmdz>` -- Configurable 8-channel
  ADC/DAC (I2C)
- :ref:`EVAL-AD5770R-PMDZ <eval-ad5770r-pmdz>` -- 6-channel DAC for
  photonics control
- :adi:`EVAL-AD7124-8-PMDZ <EVAL-AD7124-8PMDZ>` -- 8-channel 24-bit
  sigma-delta ADC

Gas and Chemical Sensing
~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`EVAL-CN0357-ARDZ <eval-cn0357-ardz>` -- CO toxic gas measurement
  (Bluetooth demo)
- :ref:`EVAL-CN0397-ARDZ <eval-cn0397-ardz>` -- Visible light
  detection/measurement
- :ref:`EVAL-CN0398-ARDZ <eval-cn0398-ardz>` -- Soil moisture and pH
  measurement (Wi-Fi demo)
- :ref:`EVAL-CN0428-EBZ <eval-cn0428-ebz>` -- Water conductivity and pH
  measurement
- :ref:`EVAL-CN0537-ARDZ <eval-cn0537-ardz>` -- UL 217 smoke detector

Industrial/PLC
~~~~~~~~~~~~~~~

- :ref:`EVAL-CN0410-ARDZ <eval-cn0410-ardz>` -- Programmable 3-channel LED
  driver
- :ref:`EVAL-CN0414-ARDZ <eval-cn0414-ardz>` -- PLC/DCS analog input module
  with HART
- :ref:`EVAL-CN0415-ARDZ <eval-cn0415-ardz>` -- Robust solenoid measurement
  system
- :ref:`EVAL-CN0418-ARDZ <eval-cn0418-ardz>` -- PLC/DCS analog output module
  with HART

Precision Measurement
~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`EVAL-CN0531-PMDZ <eval-cn0531-pmdz>` -- +/-5V 20-bit DC control
- :ref:`EVAL-CN0536-ARDZ <eval-cn0536-ardz>` -- Radiation measurement
- :ref:`EVAL-CN0503-ARDZ <eval-cn0503-ardz>` -- Optical liquid analysis

Design and Integration Files
------------------------------

- `EVAL-ADICUP3029 Schematics and Layout <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/eval-adicup3029-designsupport.zip>`__
- `EVAL-ADICUP3029 GitHub Repository <https://github.com/analogdevicesinc/EVAL-ADICUP3029>`__

Documents
---------

- :adi:`ADuCM3029 Datasheet <ADUCM3029>`
- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
