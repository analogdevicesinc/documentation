.. _dc2903a:

DC2903A User Guide
==================

Introduction
------------

The :adi:`DC2903A` is a fully featured evaluation board for the :adi:`LTC2672`,
a five-channel, 16-bit, current source output digital-to-analog converter (DAC).
The DC2903A is controlled through a serial peripheral interface (SPI) from the
J1 connector. The SPI signals are sent from the :adi:`DC2026C` controller board
(Linduino) through the ribbon cable connected to the DC2903A.

The LTC2672 is used for various current-mode biasing applications such as
tunable lasers or resistive heaters. The output current ranges are software
selectable, and each channel is routed to the DC2903A MUX pin for external
monitoring.

.. image:: dc2903_ltc2672_eval.png
   :align: center

Supported Devices
-----------------

- :adi:`LTC2672`

Hardware Specifications
-----------------------

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

The DC2903A board has provision for dual supply operation. The positive voltage
supply (VCC) can range from 2.8 V to 5.5 V, while the negative supply voltage
(VEE) can handle voltages from -5.5 V up to 0 V (GND).

To ensure proper operation, the supply must be able to source at least the total
maximum current expected from all channels. For example, if the maximum current
output from each channel is 300 mA, the supply should source at least 1500 mA
(300 mA x 5 channels) to operate the device properly across all available span
and current levels.

Digital Interface (QuikEval)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QuikEval system is a USB-based product demonstration and data acquisition
system. Its interface is a 14-pin connection that allows the :adi:`DC2026C`
(Linduino) to connect with Analog Devices daughter boards.

The specific interface used for the DC2903A is SPI.

.. list-table::
   :header-rows: 1

   * - P1 Pin Number
     - Pin Function
     - Mnemonic
   * - Pin 1
     - +7 V Unregulated
     - 7V
   * - Pin 2
     - I/O Voltage
     - IOVDD
   * - Pin 3
     - Board Ground
     - GND
   * - Pin 4
     - Serial Clock [#f1]_
     - SCLK
   * - Pin 5
     - Master In Slave Out
     - MISO
   * - Pin 6
     - Chip Select
     - CS
   * - Pin 7
     - Master Out Slave In [#f1]_
     - MOSI
   * - Pin 8
     - Board Ground
     - GND
   * - Pin 9
     - EEPROM SDA (I2C)
     - EESDA
   * - Pin 10
     - EEPROM VCC
     - EEVCC
   * - Pin 11
     - EEPROM SCL (I2C)
     - EESCL
   * - Pin 12
     - EEPROM Ground
     - GND
   * - Pin 13
     - Board Ground
     - GND
   * - Pin 14
     - Free GPIO
     - GPIO

.. [#f1] Pin has alternate function. Serial Clock is for either SPI or I2C.
   Master Out Slave In (MOSI) also acts as SDA pin for I2C mode.

.. figure:: dc2903_ltc2672_quikeval_pins.png
   :align: center

   DC2903A QuikEval connector pinout

No-OS Software Support
----------------------

The goal of ADI Microcontroller No-OS is to provide reference projects for lower
end processors which cannot run Linux or are not running a specific operating
system, and to help customers using microcontrollers with ADI parts. ADI No-OS
offers generic drivers, which can be used as a base for any microcontroller
platform, and example projects which use these drivers on various microcontroller
platforms.

LTC2672 Driver
~~~~~~~~~~~~~~

The LTC2672 No-OS driver source code and documentation can be found at:

- :git-no-OS:`drivers/dac/ltc2672`

No-OS Project
~~~~~~~~~~~~~

The No-OS example project source code can be found at:

- :git-no-OS:`projects/dc2903a`

Supported Platforms
~~~~~~~~~~~~~~~~~~~

- :adi:`MAX32666FTHR`

Hardware Setup
~~~~~~~~~~~~~~

Required Hardware
^^^^^^^^^^^^^^^^^

- :adi:`DC2903A`
- :adi:`MAX32666FTHR`
- Dual power supply

.. figure:: dc2903_ltc2672_hardware_setup.png
   :align: center

   DC2903A and MAX32666FTHR hardware setup

Required Connections
^^^^^^^^^^^^^^^^^^^^

The :adi:`MAX32666FTHR` does not have a PMOD interface, but Dupont
female-female cables can be used to make the required connections.

The table below shows the connections between the DC2903A and MAX32666FTHR:

.. list-table::
   :header-rows: 1

   * - DC2903A Pin Number
     - MAX32666 Pin Number
     - Function
     - Mnemonic
   * - Pin 1
     - 3V3
     - 3.3 V Supply (for IO)
     - 3V3
   * - Pin 3
     - GND
     - Board Ground
     - GND
   * - SCK
     - AIN3
     - Serial Clock
     - SCLK
   * - SDI
     - AIN1
     - Master In Slave Out
     - MISO
   * - CS/LO
     - AIN0
     - Chip Select
     - CS
   * - SDO
     - AIN2
     - Master Out Slave In
     - MOSI

After connecting the pins from the DC2903A QuikEval interface to the
MAX32666FTHR, connect the corresponding pins to VCC, VEE, and GND. Make sure
that the voltages to these pins are within the normal operating range. Power up
the supplies in any order as the device does not require any sequencing.

Building the No-OS Project
~~~~~~~~~~~~~~~~~~~~~~~~~~

The path of the project is ``no-OS/projects/dc2903a/``.

For instructions on cloning and building the No-OS project, refer to the
:dokuwiki:`No-OS Build Guide <resources/no-os/build>`.

Make sure to select the MAXIM platform when following the build prerequisites.

Example Project
~~~~~~~~~~~~~~~

The basic example project contains the generic HAL initialization of the
MAX32666FTHR platform, together with the SPI and UART driver configuration and
initialization.

The SPI driver is used to communicate with the LTC2672 and change its settings.
The UART driver is used to display the device configuration on the host machine.

The example performs the following operations in a continuous loop:

#. Sets the current span to 3.125 mA on all channels.
#. Steps through a series of current values on all channels
   (0.21 mA, 0.41 mA, 1.21 mA, 1.41 mA).
#. Configures the MUX pin to output the internal VREF measurement (~1.25 V).
#. Issues a chip power-down command (all outputs and VREF go to 0).
#. Demonstrates the toggle function on OUT3, alternating between two current
   levels.

.. figure:: dc2903_ltc2672_serial_output.png
   :align: center

   Serial output when running the basic example project

Hardware Output Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To verify the hardware output when running the example:

#. Connect the DC2903A to the MAX32666FTHR by following the connections in
   `Required Connections`_.
#. Build and load the example ``.hex`` file to the microcontroller board.
#. Reset or reconnect the microcontroller board to the computer or a power
   supply.
#. Using a DC ammeter, check all channels (OUT0 through OUT3) for current
   readings.
#. Using a DC voltmeter, measure the voltage on the MUX pin; it should read
   approximately 1.25 V.
#. Using a DC ammeter, measure the current changes on OUT3; it should
   sequentially read approximately 0.21 mA, 0.41 mA, 1.21 mA, and 1.41 mA.
#. A power-down command follows the above sequence. During this state, all
   outputs should read approximately 0 A.
#. A toggle command executes after powering down. During this state, OUT3 should
   sequentially read approximately 0.4 mA and 0.1 mA.
#. Repeat the process to confirm functionality.

The example project runs sequentially and continuously repeats until power is
removed.

Linux IIO Driver
-----------------

The :adi:`LTC2672` is supported by a Linux IIO DAC driver. The driver exposes
five current output channels with per-channel scale, offset, raw, and power-down
attributes. Toggle mode can be configured on individual channels for fast
switching between two DAC codes without SPI transactions.

.. list-table::
   :header-rows: 1

   * - Function
     - File
   * - Driver
     - :git-linux:`drivers/iio/dac/ltc2664.c`
   * - Devicetree binding
     - :git-linux:`Documentation/devicetree/bindings/iio/dac/adi,ltc2672.yaml`

Devicetree Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

Required devicetree properties:

- ``compatible``: Must be ``"adi,ltc2672"``.
- ``reg``: The SPI chip select number.
- ``spi-max-frequency``: Maximum SPI clock frequency.
- ``vcc-supply``: Analog supply voltage input.
- ``iovcc-supply``: Digital input/output supply voltage.
- ``v-neg-supply``: Negative supply voltage input.
- Channel nodes with ``reg``, ``output-range-microamp``, and optionally
  ``adi,toggle-mode`` properties.

Optional devicetree properties:

- ``ref-supply``: External reference voltage supply regulator. Only set if an
  external reference voltage is connected to the REF pin.

IIO Sysfs Attributes
~~~~~~~~~~~~~~~~~~~~~

When the driver is loaded, the following per-channel attributes are available
for each of the five current output channels:

``out_currentY_raw``
   Raw (unscaled) output current value for channel Y.

``out_currentY_scale``
   Scale factor in microamps per LSB. The output current is computed as:
   ``I = (out_currentY_raw + out_currentY_offset) * out_currentY_scale`` (uA).

``out_currentY_offset``
   Offset to be applied to the raw value before scaling.

``out_currentY_powerdown``
   Writing 1 causes channel Y to enter power-down mode. Writing 0 restores
   normal operation.

``out_currentY_powerdown_mode``
   The power-down mode (e.g. ``42kohm_to_gnd``).

For channels configured in toggle mode, additional attributes
``out_currentY_raw0``, ``out_currentY_raw1``, ``out_currentY_toggle_en``, and
``out_currentY_symbol`` are available.

More Information
----------------

- :adi:`DC2903A`
- :adi:`LTC2672`
- :git-no-OS:`DC2903A No-OS Project <projects/dc2903a>`
- :git-no-OS:`LTC2672 No-OS Driver <drivers/dac/ltc2672>`
- :git-linux:`LTC2672 Linux Driver <drivers/iio/dac/ltc2664.c>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`EngineerZone <data-converters>`.
