.. _adalm-lsmspg:

ADALM-LSMSPG
============

Active Learning Module for Low-Speed Mixed-Signal Playground

Overview
--------


.. figure:: adalm-lsmspg-top-angle.png
   :align: left

   ADALM-LSMSPG

The :adi:`ADALM-LSMSPG (Analog Devices Active Learning Module - Low-Speed Mixed-Signal Playground) <ADALM-LSMSPG>`
facilitates hands-on learning of concepts related to software interfacing to hardware peripherals.

It consists of two 8-channel multifunction ADC/DAC/digital GPIOs - :adi:`AD5592r` and :adi:`AD5593r`-
which have SPI and I2C interfaces, respectively.

The :adi:`AD5592r` includes a simple NPN transistor curve tracer circuit as a representative instrumentation
application.

The :adi:`AD5593r` includes a PNP curve tracer, and both devices include bi-color LEDs for "Hello, World!"
applications.

An :adi:`LM75` temperature sensor is also included as a "bare minimum" peripheral example.

The :adi:`ADALM-LSMSPG` is compatible with Raspberry Pi and Feather form factor hosts, and an
:adi:`ADALM2000` interface allows monitoring of the SPI and I2C busses for driver development and debug.

Features
++++++++

- Compatible with Raspberry Pi platforms
- Compatible with Feather platforms
   - :adi:`MAX32666FTHR`
   - :adi:`MAX32655FTHR`
   - Other Feather platforms supporting 3.3V I/O
- :adi:`ADALM2000` interface for digital debug
- :adi:`AD5592r` SPI 8-channel ADC/DAC/GPIO
- :adi:`AD5593r` I2C 8-channel ADC/DAC/GPIO
- NPN and PNP transistor curve tracer example application circuits
- :adi:`LM75` temperature sensor
- SPI and I2C Pmod expansion headers

Applications
++++++++++++

- Demonstrating peripheral interfacing and software for:
   - Embedded Linux
   - no-OS (Bare Metal)
   - Zephyr
   - Arduino

System Architecture
+++++++++++++++++++


.. figure:: ADALM-LSMSPG_block_diagram.png

   ADALM-LSMSPG System Architecture

What's Inside the Box?
++++++++++++++++++++++

Upon purchase of the ADALM-LSMSPG kit, the package comes with the following boards and accessories:

 A. ADALM-LSMSPG main board
 B. 40-pin, 15 cm ribbon cable for Raspberry Pi
 C. Jumpers for setting AD5592r and LM75 I2C address

.. figure:: adalm-lsmspg_package_contents.png

   ADALM-LSMSPG Kit Contents

Components and Connections
++++++++++++++++++++++++++

.. figure:: adalm-lsmspg_with_pin_labels.png

   ADALM-LSMSPG Hardware Components and Connections

+-----------------------+-----------------------+------------------------------------------------------+
| ADALM-LSMSPG Pins     | Functions             | Description                                          |
+=======================+=======================+======================================================+
| P31                   | Raspberry Pi interface| Connect to Raspberry Pi 4, 400, 5, 500 via supplied  |
|                       |                       | ribbon cable. Be sure to observe polarity / pin 1    |
|                       |                       | location.                                            |
+-----------------------+-----------------------+------------------------------------------------------+
| P1, P28               | Feather interface     | Pins or stacking headers must be installed on        |
|                       |                       | Feather platform board, with pins facing downward.   |
+-----------------------+-----------------------+------------------------------------------------------+

.. note::

   The Raspberry Pi and Feather interfaces are mutually exclusive.

+-----------------------+------------------------------+------------------------------------------------------+
| ADALM-LSMSPG Pins     | Functions                    | Description                                          |
+=======================+==============================+======================================================+
| P16                   | ADALM2000 interface          | Allows monitoring of digital traffic on the I2C, SPI,|
|                       |                              | and various GPIO signals.                            |
+-----------------------+------------------------------+------------------------------------------------------+
| P27                   | ADALM2000 through-connections| Allows monitoring of other signals via jumper wires. |
+-----------------------+------------------------------+------------------------------------------------------+

Refer to the table below for P16, P27 signal mapping.

.. csv-table:: P16 and P27 Signal Mapping
   :file: p16-p27_signal_mapping.csv
   :header-rows: 1
   :widths: 35, 65
   :class: fullwidth

+-----------------------+-----------------------+------------------------------------------------------+
| ADALM-LSMSPG Pins     | Functions             | Description                                          |
+=======================+=======================+======================================================+
| P31                   | AD5592r Connections   | Analog I/O (ADC/DAC), digital GPIO                   |
+-----------------------+-----------------------+------------------------------------------------------+
| P5                    | AD5593r Connections   | Analog I/O (ADC/DAC), digital GPIO                   |
+-----------------------+-----------------------+------------------------------------------------------+

Refer to the figure below for P2, P5 signal mapping.

.. figure:: ad559xr_gpio_pin.png

   P2 and P5 Signal Mapping

Address Selection Jumpers
+++++++++++++++++++++++++

.. csv-table:: P4 Address Selection Jumpers
   :file: ad5593r_i2c_address.csv
   :header-rows: 1
   :widths: 35, 65
   :class: fullwidth

.. csv-table:: P9 Address Selection Jumpers
   :file: lm75_i2c_address.csv
   :header-rows: 1
   :widths: 35, 65
   :class: fullwidth

System Monitor/Control
++++++++++++++++++++++

- DS1: Heartbeat LED
- S1 : Raspberry Pi Shutdown (set in config.txt), Feather reset

Curve Tracer Application Circuits
+++++++++++++++++++++++++++++++++

The :adi:`AD5592r` and :adi:`AD5593r` drive simple NPN and PNP (respectively) curve tracer circuits.
This represents a simple DC test instrument that involves the "set a current, set a voltage,
take a measurement, do some math, step, repeat" sequence of operations.
The details of the experiments are covered in the
:doc:`Tools for LSMSPG Lesson </learning/tools_for_ls/index>`.

.. figure:: ad5592r_npn_curve_tracer_connections.png

   AD5592r NPN Curve Tracer Connections

The PNP curve tracer has two options for the emitter drive: AD5593r CH3 (default), or the 3.3V
supply rail.

.. figure:: ad5593r_pnp_curve_tracer_connections.png

   AD5593r PNP Curve Tracer Connections

Hardware Setup
++++++++++++++

- **Raspberry Pi Setup**:

For Raspberry Pi Zero 2 W, 4, and 5, use the included ribbon cable to make the connection as shown
in the figure below.

.. figure:: rpi-4_5_w_with_lsmspg.png

   RPi Zero 2W/4/5 and ADALM-LSMSPG with 40-pin Ribbon Cable Connection


For Raspberry Pi 400 and 500, use the included ribbon cable to make the connection as shown in
the figure below.

.. figure:: rpi-400or500_with_lsmspg.png

   RPi 400/500 and ADALM-LSMSPG with 40-pin Ribbon Cable Connection

- **Feather Setup**:

Most Feather platform boards ship without peripheral headers installed. Refer to the board's
instructions, and install either:

 - Downward-facing 100-mil post headers
 - Stacking headers with posts extending from the reverse side of the board.
 - Install the Feather on P20 as shown in the Figure below.

.. figure:: max32666fthr_on_adalm-lsmspg.png

   Feather Mounted on ADALM-LSMSPG

Software Setup
++++++++++++++

Raspberry Pi Setup
^^^^^^^^^^^^^^^^^^

Prepare an SD card with ADI Kuiper Linux following the instructions at
:ref:`ADI Kuiper Linux Guide <kuiper>`.

Add the following to the end of ``/boot/config.txt``:

.. code-block:: none

   # config.txt additions

   dtoverlay=rpi-adalm-lsmspg

   # Heartbeat blinky:
   dtparam=act_led_gpio=20
   dtparam=act_led_trigger=heartbeat
   dtparam=i2c_arm=on

   # Short GPIO21 (pin 40) to ground for shutdown:
   dtoverlay=gpio-shutdown,gpio_pin=21,active_low=1,gpiopull=up

With the ADALM-LSMSPG connected, the heartbeat LED will begin beating on boot.
The shutdown button is a convenient means of shutting down the Raspberry Pi
properly in headless situations (no local monitor or keyboard). Press the
shutdown button, wait 5 seconds after the heartbeat LED stops blinking, and
then it is safe to remove power.

MAX32666FTHR Setup
^^^^^^^^^^^^^^^^^^

The :adi:`MAX32666FTHR` includes a :adi:`MAX32625PICO` debugger that can be used to load
the ADALM-LSMSPG firmware image. Prepare the MAX32625PICO itself with the
MAX32666FTHR-specific DAPLink image from:
:git-max32625pico-firmware-images:`MAX32625PICO firmware images <+>`

Leave the MAX32625PICO plugged in, and plug in the MAX32666FTHR using another
USB-Micro cable. Connect the debug interface to the MAX32666FTHR with the supplied
10-pin ribbon cable. Download the ADALM-LSMSPG tinyiiod firmware image
(filename ``adalm-lsmspg.zip``) from:
:git-no-os:`ADALM-LSMSPG firmware (no-OS releases) <releases/latest+>`

Unzip the archive, copy the ``adalm-lsmspg_maxim_iio.hex`` file, and paste it into
the DAPLINK mass storage device (typically ``D:`` or ``E:`` on Windows systems).
The DAPLINK drive will auto-eject, and the heartbeat LED on the ADALM-LSMSPG
will begin blinking.

Application Setup
^^^^^^^^^^^^^^^^^

Detailed instructions for various application software examples are included in the
:doc:`Tools for LSMSPG Lesson </learning/tools_for_ls/index>`,
as well as other supporting material. The underlying API for Raspberry Pi/Linux and
bare-metal tinyiiod servers is ``libiio``, which can be installed from:
:ref:`libiio`

Once installed, information about the ADALM-LSMSPG context can be displayed by
running ``iio_info`` and passing the URI argument.

For Kuiper Linux, the default hostname is ``analog``. Example:

.. code-block:: none

   iio_info -u ip:analog.local

For the MAX32666FTHR running the tinyiiod firmware, run:

.. code-block:: none

   iio_info -u serial:COM4

Replace ``COM4`` with the appropriate COM port number on Windows, or ``/dev/ttyX`` on Linux.

The :doc:`Tools for LSMSPG Lesson </learning/tools_for_ls/index>`
tutorial contains many additional examples of communicating with
the ADALM-LSMSPG.

Additional Resources
++++++++++++++++++++

- :doc:`Tools for LSMSPG Lesson </learning/tools_for_ls/index>`
- :adi:`AD5592R Product Page <ad5592r>`
- :adi:`AD5593R Product Page <ad5593r>`
- :adi:`LM75 Product Page <lm75>`

Design & Integration Files
++++++++++++++++++++++++++

.. admonition:: Download

   :download:`ADALM-LSMSPG Design & Integration Files <ADALM-LSMSPG-designsupport.zip>`

    - Schematic
    - PCB Layout
    - Bill of Materials
    - Allegro Project

Help and Support
----------------

For questions and more information, please visit the :ez:`EngineerZone Support Community </>`
or contact your local ADI representative.