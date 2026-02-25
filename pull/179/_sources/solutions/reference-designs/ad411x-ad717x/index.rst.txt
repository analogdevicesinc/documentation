.. _ad411x-ad717x:

AD411x/AD717x Console Application
==================================

Mbed-Based Firmware for AD411x and AD717x Sigma-Delta ADC Evaluation Boards

Introduction
------------

The AD717x/AD411x console application provides a firmware example for
interacting with the :adi:`AD4111`, :adi:`AD4112`, :adi:`AD4114`,
:adi:`AD4115`, :adi:`AD4116`, :adi:`AD7172-2`, :adi:`AD7172-4`,
:adi:`AD7173-8`, :adi:`AD7175-2`, :adi:`AD7175-8`, :adi:`AD7176-2`, and
:adi:`AD7177-2` evaluation boards. The firmware runs on the
:adi:`SDP-K1 <EVAL-SDP-CK1Z>` controller board and communicates with the ADC
evaluation board via SPI through the 120-pin SDP connector.

The application uses a three-layer software architecture:

- **Console Application Layer** -- Uses ADI Console Libraries for user
  interaction via a serial terminal
- **Device No-OS Layer** -- Provides device-specific APIs for register access
  and control
- **Platform Drivers (Mbed-OS) Layer** -- Handles low-level peripheral access
  (GPIO, SPI, I2C) using Mbed-OS

.. figure:: ad717x_architecture.jpg
   :align: center
   :width: 500

   AD717x/AD411x firmware software architecture

Supported Devices
-----------------

**AD411x Family:**

- :adi:`AD4111`
- :adi:`AD4112`
- :adi:`AD4114`
- :adi:`AD4115`
- :adi:`AD4116`

**AD717x Family:**

- :adi:`AD7172-2`
- :adi:`AD7172-4`
- :adi:`AD7173-8`
- :adi:`AD7175-2`
- :adi:`AD7175-8`
- :adi:`AD7176-2`
- :adi:`AD7177-2`

Supported Evaluation Boards
----------------------------

- :adi:`EVAL-AD4111SDZ <EVAL-AD4111>`
- :adi:`EVAL-AD4112SDZ <EVAL-AD4112>`
- :adi:`EVAL-AD4114/15SDZ <EVAL-AD4115>`
- :adi:`EVAL-AD4116 <EVAL-AD4116>`
- :adi:`EVAL-AD7175-2SDZ <EVAL-AD7175-2>`
- :adi:`EVAL-AD7175-8SDZ <EVAL-AD7175-8>`
- :adi:`EVAL-AD7176-2SDZ <EVAL-AD7176-2>`
- :adi:`EVAL-AD7177-2SDZ <EVAL-AD7177-2>`
- :adi:`EVAL-AD7172-2SDZ <EVAL-AD7172-2>`
- :adi:`EVAL-AD7172-4SDZ <EVAL-AD7172-4>`
- :adi:`EVAL-AD7173-8SDZ <EVAL-AD7173-8>`

Hardware Requirements
---------------------

- :adi:`SDP-K1 <EVAL-SDP-CK1Z>` controller board (Mbed-enabled)
- One of the supported EVAL-AD411x or EVAL-AD717x evaluation boards
- USB cable (Micro-B to A)
- PC with a serial terminal application (Tera Term, PuTTY, or CoolTerm)

Hardware Setup
--------------

.. figure:: ad717x_hw_connection.jpg
   :align: center
   :width: 500

   AD717x/AD411x evaluation board connected to SDP-K1 controller

#. Set the VIO_ADJUST jumper on the SDP-K1 board to the **3.3 V** position.
#. Connect the evaluation board to the SDP-K1 via the 120-pin SDP connector.
   Secure with the provided screws.
#. For the EVAL-AD4111SDZ (AD4111/AD4112): set the PWR (LK3) connector to the
   **USB_SUPP (B)** position for USB power from the SDP-K1. Other evaluation
   boards may require an external DC supply; consult the respective evaluation
   board user guide.
#. Connect the SDP-K1 to the PC using a USB cable. The board enumerates as a
   USB serial (COM) port.

Serial Terminal Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the serial terminal with the following settings:

.. list-table::
   :header-rows: 1

   * - Parameter
     - Value
   * - Baud rate
     - 230400
   * - Data bits
     - 8
   * - Parity
     - None
   * - Stop bits
     - 1

Software Setup
--------------

Building the Firmware
~~~~~~~~~~~~~~~~~~~~~

The firmware source code is hosted in the precision-converters-firmware
repository:

- `AD717x IIO Project
  <https://github.com/analogdevicesinc/precision-converters-firmware/tree/main/projects/ad717x_iio>`__

To build and deploy the firmware:

#. Open the `Mbed Online Compiler <https://studio.keil.arm.com/>`__.
#. Import the precision-converters-firmware repository.
#. Edit ``app_config.h`` to select the target device by uncommenting the
   appropriate ``#define DEV_ADxxxx`` line (for example, ``DEV_AD4111`` for the
   AD4111).
#. Edit the pin mapping section in ``app_config.h`` if using a non-default
   controller board.
#. Select the **SDP-K1** as the target platform in the compiler.
#. Compile the project to generate a binary file.
#. Drag and drop the binary file onto the USB drive presented by the SDP-K1
   controller board.
#. Open the serial terminal with the settings listed above.
#. Press the reset button on the SDP-K1 to start the application.

Using the Application
~~~~~~~~~~~~~~~~~~~~~

After reset, the firmware displays a menu-driven console interface through the
serial terminal. Navigate by entering the number corresponding to the desired
menu option.

.. figure:: ad4111_console_menu.png
   :align: center
   :width: 500

   AD4111 console application main menu

The console application provides access to core device functionality including
register read/write, channel configuration, and data acquisition.

Software Support
----------------

No-OS Driver
~~~~~~~~~~~~

The AD717x no-OS driver provides low-level register access and device control:

- :git-no-OS:`drivers/adc/ad717x`

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The AD7173 Linux IIO driver supports the AD717x and AD411x families:

- :git-linux:`drivers/iio/adc/ad7173.c`

More Information
----------------

- :adi:`AD4111 Product Page <AD4111>`
- :adi:`AD7173-8 Product Page <AD7173-8>`
- `Precision Converters Firmware Build Guide
  <https://analogdevicesinc.github.io/precision-converters-firmware/source/build/project_build.html>`__
- `AD717x IIO Application User Guide
  <https://analogdevicesinc.github.io/precision-converters-firmware/source/projects/ad717x_iio/ad717x_iio.html>`__
- `SDP-K1 Platform Page <https://os.mbed.com/platforms/SDP_K1/>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`Precision Converters Forum <precision-converters>`.
