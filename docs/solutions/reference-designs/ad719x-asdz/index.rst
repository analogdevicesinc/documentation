.. imported from: https://wiki.analog.com/resources/tools-software/product-support-software/ad719x_mbed_iio_application

.. _ad719x-asdz:

AD719x-ASDZ User Guide
=======================

Introduction
------------

The AD719x-ASDZ evaluation boards enable evaluation of the :adi:`AD7190`,
:adi:`AD7192`, :adi:`AD7193`, and :adi:`AD7195` precision sigma-delta
analog-to-digital converters. These ADCs provide 24-bit resolution with low
noise performance, making them ideal for bridge sensor, temperature
measurement, and precision instrumentation applications.

The evaluation system uses an :adi:`SDP-K1` controller board running IIO
firmware to provide device configuration, data capture, and analysis through
the IIO ecosystem.

.. figure:: app_interface.png
   :width: 400 px
   :align: center

   AD719x IIO application interface

Supported Devices
-----------------

- :adi:`AD7190`
- :adi:`AD7192`
- :adi:`AD7193`
- :adi:`AD7195`

Evaluation Boards
-----------------

- :adi:`EVAL-AD7190`
- :adi:`EVAL-AD7192`
- :adi:`EVAL-AD7193`
- :adi:`EVAL-AD7195`

Hardware Setup
--------------

Required Components
~~~~~~~~~~~~~~~~~~~

- :adi:`SDP-K1` controller board
- EVAL-AD719x evaluation board (AD7190, AD7192, AD7193, or AD7195)
- USB cable for power and communication

Connections
~~~~~~~~~~~

.. figure:: evb_connection_diagram.png
   :width: 400 px
   :align: center

   SDP-K1 and EVAL-AD719x connection diagram

.. figure:: ad719x_hardware_connection.png
   :width: 600 px
   :align: center

   AD719x hardware connection setup

1. Stack the EVAL-AD719x board onto the Arduino connectors of the SDP-K1
2. Connect a male-to-male jumper wire between D8 and D12
3. Configure jumper headers LK7 and LK8 to the 3.3 V position
4. Set the VIO_ADJUST jumper on the SDP-K1 to 3.3 V
5. Connect the USB cable to the SDP-K1

Software Overview
-----------------

The evaluation system consists of three software components:

.. figure:: ad719x_firmware_structure.png
   :width: 300 px
   :align: center

   AD719x firmware architecture

Firmware
~~~~~~~~

The IIO firmware runs on the SDP-K1 and uses No-OS drivers to control the
AD719x device. The firmware is hosted in the
:git-precision-converters-firmware:`projects/ad719x_iio` repository.

Key firmware configuration options (defined in ``app_config.h``):

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Macro
     - Description
   * - ACTIVE_PLATFORM_MBED
     - Selects the Mbed platform
   * - IIO_UART_BAUD_RATE
     - Serial communication speed (default: 230400)
   * - DATA_CAPTURE_MODE
     - Burst or continuous data capture mode
   * - DEV_AD7193
     - Selects the active device (change to match your board)
   * - BIPOLAR_MODE
     - Optional: enables bipolar input mode
   * - DIFFERENTIAL_INPUT
     - Optional: enables differential input configuration

Communication Interface
~~~~~~~~~~~~~~~~~~~~~~~

The firmware communicates with host applications through a UART or Virtual COM
port serial interface at up to 1 Mbps. The default baud rate is 230400.

IIO Oscilloscope
~~~~~~~~~~~~~~~~

The IIO Oscilloscope application provides a graphical interface for device
configuration and data visualization. It connects to the AD719x firmware
through the libiio library.

Key capabilities:

- **DMM Tab**: reads instantaneous voltage on input channels using single
  conversion mode
- **Data Capture**: visualizes raw ADC values in both time and frequency
  domains (maximum 4096 samples for FFT analysis)
- **Device Attributes**: provides access to global and per-channel
  configuration parameters

Python Support
~~~~~~~~~~~~~~

The pyadi-iio library enables automated testing, calibration, and data
analysis through Python scripts. Install the required dependencies and
configure the serial COM port for communication.

Building the Firmware
---------------------

Clone the precision-converters-firmware repository and build the project
for the target platform:

.. code-block:: bash

   git clone https://github.com/analogdevicesinc/precision-converters-firmware.git
   cd precision-converters-firmware/projects/ad719x_iio

Refer to the project documentation for detailed build instructions for the
Mbed platform.

Software Source Code
--------------------

- :git-precision-converters-firmware:`projects/ad719x_iio`
- :git-no-OS:`drivers/adc/ad719x`

More Information
----------------

- :adi:`AD7190 Product Page <AD7190>`
- :adi:`AD7192 Product Page <AD7192>`
- :adi:`AD7193 Product Page <AD7193>`
- :adi:`AD7195 Product Page <AD7195>`

Support
-------

For questions and more information, please contact us on the :ez:`/`.

- :ez:`EngineerZone Precision ADCs <precision-adcs>`
