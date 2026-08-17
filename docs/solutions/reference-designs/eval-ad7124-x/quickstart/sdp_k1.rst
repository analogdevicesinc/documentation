.. _eval-ad7124-x quickstart sdp_k1:

SDP-K1 Quick Start (Mbed)
===============================================================================

.. esd-warning::

This guide describes how to use the
:adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124>` or
:adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124>` evaluation board with
the :adi:`SDP-K1` controller board using Mbed-based firmware.
The ASDZ boards connect to the SDP-K1 via the on-board Arduino
connectors.

Two firmware applications are available:

- **AD7124 Console Application** -- general-purpose console interface for
  channel configuration, sampling, and register access
- **AD7124 Temperature Measurement Demo** -- specialized firmware for
  temperature sensing with RTDs, thermocouples, and thermistors

Prerequisites
-------------------------------------------------------------------------------

See :ref:`eval-ad7124-x prerequisites` for the full list.

**Hardware:**

- :adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124>` or
  :adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124>` evaluation board
- :adi:`EVAL-SDP-CK1Z <SDP-K1>` controller board
- USB cable
- PC or laptop with a USB port

.. note::

   No external DC power supply is required. The SDP-K1 provides power to the
   evaluation board through the Arduino/SDP connector. Connect the VIO_ADJUST
   jumper on the SDP-K1 board to the 3.3 V position to drive SDP-K1 GPIOs at
   3.3 V.

**Software:**

- `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`_
- Serial terminal program configured for 230400 baud, 8N1

AD7124 Console Application
-------------------------------------------------------------------------------

Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD7124 Console Application firmware provides a console-based user
interface to interact with the :adi:`AD7124-4` / :adi:`AD7124-8`. The firmware
comprises three layers:

#. **Console Application Layer** -- user interface using ADI Console Libraries
#. **Device No-OS Layer** -- device-specific APIs for AD7124 register and data
   access
#. **Platform Drivers (Mbed-OS)** -- low-level peripheral access (GPIO, SPI,
   I2C) via Mbed-OS libraries

Hardware connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board is connected to the :adi:`SDP-K1` through the Arduino
connectors. The 120-pin SDP connector can also be used.

.. note::

   Connect the VIO_ADJUST jumper on the SDP-K1 board to the 3.3 V position to
   drive SDP-K1 GPIOs at 3.3 V.

   For AD7124 evaluation board connections and jumper settings, refer to the
   :ref:`ASDZ hardware guide <eval-ad7124-4-8asdz_hardware>`. The Arduino
   connector is used as the default interface type.

Analog inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The screw terminal connections on J1 and J2 of the evaluation board can be used
to connect analog input signals.

Two configurations are provided:

**Configuration A:**

- AIN0/AIN1 are used for channel 0, simple voltage measurement

**Configuration B:**

- AIN2/AIN3 connect to the A2 thermocouple connector (channel 0, internal
  reference, bias voltage on AIN2)
- AIN4/AIN5 are an RTD1000 measurement on channel 1 (excitation from AIN1,
  requires external RTD and reference resistor)

Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   Source code:

   - `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`_

   Build guide:

   - `Precision Converters MBED Firmware Build Guide <https://wiki.analog.com/resources/tools-software/product-support-software/pcg-fw-mbed-build-guide>`_ <web>

Quick start
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Connect the evaluation board to the :adi:`SDP-K1` via the Arduino
   connectors or 120-pin SDP connector.
#. Connect the :adi:`SDP-K1` to your computer over USB.
#. Import the firmware code into the Mbed online compiler.
#. Ensure the :adi:`SDP-K1` is selected as the target board.
#. Compile the code.
#. Drag and drop the resulting binary (.BIN) to the SDP-K1 USB drive.
#. Open a serial terminal (e.g., Tera Term) with the following settings:

   - **Baud rate:** 230400
   - **Data bits:** 8
   - **Parity:** None
   - **Stop bits:** 1

#. Reset the controller board and connect.

Using the firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The console menu provides the following features:

- Enable/disable individual ADC channels (0--15)
- Connect analog input pins to individual channels
- Configure device setups (0--7) and assign to individual channels
- Display device and channel setup
- Perform internal device calibration
- Read die temperature (using internal temperature sensor)
- Read/write device registers

.. tip::

   The firmware is designed to be intuitive. Simply enter a number
   corresponding to the required command and follow the on-screen prompts.

AD7124 Temperature Measurement Demo
-------------------------------------------------------------------------------

Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The temperature measurement firmware example supports multiple sensor types
on the evaluation board with the :adi:`SDP-K1` controller board. The firmware
provides a console-based menu for selecting and configuring temperature sensors.

.. important::

   This code has been developed and tested on the :adi:`SDP-K1` controller board
   using the on-board Arduino/SDP-120 headers. The same code can be used with
   little modification on other Mbed-supported boards with Arduino header
   support (e.g., STM32-Discovery, STM32-Nucleo).

Hardware connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   Connect the VIO_ADJUST jumper on the SDP-K1 board to the 3.3 V position to
   drive SDP-K1 GPIOs at 3.3 V.

   For AD7124 evaluation board connections and jumper settings, refer to the
   :ref:`ASDZ hardware guide <eval-ad7124-4-8asdz_hardware>`. The Arduino
   connector is used as the default interface type.

Quick start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the evaluation board to the :adi:`SDP-K1` via the Arduino
   connectors.
#. Connect the SDP-K1 to your computer over USB.
#. Import the firmware code from the
   `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`_
   repository.
#. Ensure the SDP-K1 is selected as the target.
#. Compile and download the binary to the SDP-K1.
#. Open a serial terminal configured for **230400 baud, 8N1**.
#. Reset the controller board and connect.

Supported sensors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The firmware supports the following sensor types:

- Single or multiple 2/3/4-wire RTDs (default: PT100)
- Single or multiple thermocouples (default: T-type)
- Single or multiple NTC thermistors (default: 10K NTC)

.. tip::

   In order to use analog inputs AIN4 and AIN5 on the legacy AD7124 eval board
   (with SDP-120 interface only), make sure to route the sensor connections
   directly through LK6 link instead of the physical screw-terminal connector.
   Make sure LK6 link is removed for the same purpose.

Multiple RTD configurations (2/3/4-wire)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reference: :adi:`CN0383 <en/design-center/reference-designs/circuits-from-the-lab/CN0383.html>`

Multiple thermocouple configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reference: :adi:`CN0384 <en/design-center/reference-designs/circuits-from-the-lab/CN0384.html>`

Multiple NTC thermistor configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reference: :adi:`CN0545 <en/design-center/reference-designs/circuits-from-the-lab/cn0545.html>`

Calibrating 3-wire RTDs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The firmware provides an option to perform calibrated measurement on 3-wire
RTD sensors. Two types of calibration options are available. Based on the
selected calibration type, the sensors are first calibrated and then 3-wire
RTD measurement is performed.

For more information on the calibration scheme, refer to the
:adi:`CN0383 design note <en/design-center/reference-designs/circuits-from-the-lab/CN0383.html>`.

.. tip::

   Calibration is allowed only on multiple RTD sensors, not on a single RTD
   sensor.

ADC calibration (internal and system)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The firmware allows ADC calibration on the current sensor configuration. ADC
calibration removes offset or gain errors on the input channels.

The updated device coefficients (gain and offset) are applied during sensor
measurement. After calibration, the user must return to the previously selected
demo mode to perform measurements. If a new demo mode is selected after
calibration, the coefficients are reset and calibration must be performed again.

Internal ADC calibration is straightforward, but system calibration requires
user inputs (typically after applying full-scale/zero-scale voltages on
selected analog inputs).

Modifying the firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The firmware can be customized through the following files:

- **app_config.h** -- Select active device (AD7124-4 or AD7124-8) and
  interface type (Arduino or SDP-120)
- **ad7124_regs_configs.h** -- Define analog inputs, excitation sources, PGA,
  reference sources, and power mode for all sensor configurations
- **ad7124_regs_config_rtd.c / thermocouple.c / thermistor.c** -- AD7124
  register configurations for each sensor type
- **ad7124_user_config.c** -- SPI parameters and init parameters for device
  power-up
- **ad7124_console_app.c** -- Sensor selection, ADC sampling, and temperature
  display functionality
- **ad7124_temperature_sensor.cpp** -- Wrapper for calling tempsensor library
  functions (NTC 10K, T-type thermocouple, PT100/PT1000 RTD)
