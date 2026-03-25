.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad4110

AD4110
======

Single-Channel, Universal Input Analog-to-Digital Front End for Industrial
Process Control.

Overview
--------

The :adi:`AD4110-1` is a complete, single-channel, universal input
analog-to-digital front end designed for industrial process control systems
where sensor type flexibility is required.

The high voltage input is fully software configurable for current or voltage
ranges and allows direct interface to all standard industrial analog signal
sources such as +/-20 mA, +/-4 mA to +/-20 mA, +/-10 V, and all thermocouple
types. Field power can be supplied for loop-powered current output sensors.
A range of excitation current sources for RTD sensors and other resistive
sensors are included. The integrated programmable gain amplifier (PGA) offers
sixteen gain settings from 0.2 to 24.

The :adi:`AD4110-1` provides internal front-end diagnostic functions to indicate
overvoltage, undervoltage, open wire, overcurrent, and overtemperature
conditions. The high voltage input is overcurrent limited and overvoltage
protected up to +/-35 V.

The :adi:`AD4110-1` incorporates a 24-bit sigma-delta analog-to-digital converter
offering conversion rates from 5 SPS to 125 kSPS with simultaneous 50 Hz and
60 Hz noise rejection.

Applications
~~~~~~~~~~~~

- Industrial process control (PLC, DCS)
- Data acquisition

Supported Devices
-----------------

- :adi:`AD4110-1`

Evaluation Board
----------------

- :adi:`EVAL-AD4110-1SDZ`

Operating Modes
---------------

The :adi:`AD4110-1` supports the following operating modes:

- **Voltage measurement** -- direct voltage input
- **Current measurement** -- direct current input
- **Field Power Supply** -- supplies power for loop-powered sensors
- **RTD** -- 2-wire, 3-wire, and 4-wire resistance temperature detector
  measurement
- **Thermocouple** -- thermocouple temperature sensing

No-OS Driver
------------

The no-OS driver provides bare-metal control of the :adi:`AD4110-1` via SPI.

The driver source code is available at
:git-no-OS:`drivers/afe/ad4110`.

The no-OS project is available at
:git-no-OS:`projects/ad4110`.

Functions
~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Function
     - Description
   * - ``ad4110_setup()``
     - Initialize the device.
   * - ``ad4110_spi_int_reg_read()``
     - SPI internal register read.
   * - ``ad4110_spi_int_reg_write()``
     - SPI internal register write.
   * - ``ad4110_spi_int_reg_write_msk()``
     - SPI write using a mask.
   * - ``ad4110_set_adc_mode()``
     - Set the ADC operating mode.
   * - ``ad4110_set_gain()``
     - Set the programmable gain.
   * - ``ad4110_set_op_mode()``
     - Set the operating mode (voltage, current, RTD, thermocouple, etc.).
   * - ``ad4110_spi_do_soft_reset()``
     - Perform a software reset.
   * - ``ad4110_compute_crc8()``
     - Compute CRC8 checksum.
   * - ``ad4110_compute_xor()``
     - Compute XOR checksum.

IIO Application (SDP-K1)
-------------------------

An IIO application is available for evaluating the :adi:`AD4110-1` using the
:adi:`SDP-K1` controller board with the :adi:`EVAL-AD4110-1SDZ` evaluation board.

The application firmware uses ADI's no-OS drivers and exposes the device through
the IIO ecosystem, enabling interaction via :ref:`iio-oscilloscope` or
:ref:`pyadi-iio`.

Features
~~~~~~~~

- Device attribute read/write access
- DMM tab for instantaneous voltage readings
- Real-time data visualization (time and frequency domains)
- Register-level device access
- Python-based data capture with CSV export via :ref:`pyadi-iio`

The firmware supports UART connectivity between the host PC and the SDP-K1
controller board.

Help and Support
----------------

For questions and more information, please visit the
:ez:`EngineerZone Support Community <reference-designs>`.

.. esd-warning::
