.. _adrd4161-01z software-guide:

ADRD4161-01Z Software Guide
===========================

This guide covers the software configuration for the ADRD4161-01Z carrier board.

Hardware Requirements
---------------------

* ADRD4161-01Z board
* Raspberry Pi 5 (or compatible)
* Optional: MAX32625PICO (or compatible) DAPLINK programmer for MCU reprogramming

Software Requirements
---------------------

* Raspberry Pi OS (64-bit recommended)
* ``can-utils`` package for CAN bus utilities
* ``libiio`` for IMU access via IIO subsystem

UART
----

Header P7 exposes the Raspberry Pi's UART4 interface as well as a switchable
5 V supply controlled by GPIO 24. In the AD-R1M robot, this is used to interface
with a CRSF receiver.

.. note::

   UART communication works regardless of the switchable supply state.

Usage:

.. code-block:: bash

   gpioset 0 24=0  # Turn off P7 power pin
   gpioset 0 24=1  # Turn on P7 power pin
   picocom -b 115200 /dev/ttyAMA4  # Interact with UART4

CAN Bus
-------

With the default firmware, the MAX32662 microcontroller on the ADRD4161-01Z
functions as a serial line CAN (slcan) adapter.

Configuration
~~~~~~~~~~~~~

Add the following to ``/boot/firmware/config.txt``:

.. code-block:: ini

   [all]

   # UART0 slcan
   dtoverlay=uart0,ctsrts

In ``/boot/firmware/cmdline.txt``, change the ``console=serial0,...`` option
to ``console=tty1``, disabling the Linux serial console that would otherwise
use UART0.

Starting the slcan Daemon
~~~~~~~~~~~~~~~~~~~~~~~~~

Optionally, you can use GPIO21 to reset the MCU:

.. code-block:: bash

   gpioset 0 21=0  # Assert MCU RST
   gpioset 0 21=1  # Deassert MCU RST

Start the slcan daemon:

.. code-block:: bash

   sudo slcand -o -c -f -t hw -S 2000000 -s 6 /dev/ttyAMA0 can0

Configure and bring up the CAN interface:

.. code-block:: bash

   ip link set can0 type can bitrate 500000
   ip link set can0 up

CAN Bitrate Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

To adjust the CAN bitrate, change the ``-s`` option according to the following
table:

============ ===================
CAN Bitrate  slcan Speed Option
============ ===================
10 kbit/s    ``-s 0``
20 kbit/s    ``-s 1``
50 kbit/s    ``-s 2``
100 kbit/s   ``-s 3``
125 kbit/s   ``-s 4``
250 kbit/s   ``-s 5``
500 kbit/s   ``-s 6``
800 kbit/s   ``-s 7``
1000 kbit/s  ``-s 8``
============ ===================

ADIS16xxx IMU
-------------

Configuration
~~~~~~~~~~~~~

Add the proper dtoverlay to ``/boot/firmware/config.txt``. For example, for
ADIS16470:

.. code-block:: ini

   [all]

   # ADIS16470 IMU
   dtoverlay=rpi-regulator
   dtoverlay=adis16475,device=adis16470,drdy_pin=4,reset_pin=25,sync_mode=0

Reboot the board after making changes.

Usage
~~~~~

After rebooting, you can interact with the IMU as an IIO device:

.. code-block:: bash

   iio_info -u local:
   iio_readdev -u local: adis16470 accel_x

GPIOs and Relays
----------------

Header P10 exposes a number of GPIOs. Header P12 exposes NC/NO/Common contacts
for two SPDT relays, controlled from Raspberry Pi GPIOs.

See :ref:`adrd4161-01z hardware-guide` for pinout details.

Example relay control:

.. code-block:: bash

   gpioset 0 17=1  # Activate relay K1
   gpioset 0 17=0  # Deactivate relay K1
   gpioset 0 18=1  # Activate relay K2
   gpioset 0 18=0  # Deactivate relay K2

WS2812 Addressable LEDs
-----------------------

Using the Raspberry Pi 5's RP1 PIO functionality, any exposed GPIO can be used
to generate WS2812 signals. The following example uses GPIO 23 (connector P10
pin 11) to control a WS2812 LED strip.

Build and run the piolib WS2812 example:

.. code-block:: bash

   # Install build dependencies
   sudo apt install build-essential cmake

   # Clone the piolib examples
   git clone https://github.com/raspberrypi/utils
   cd utils/piolib

   # Edit NUM_PIXELS in the ws2812 example to match your LED strip length
   nano examples/ws2812.c

   # Build the examples
   mkdir build
   cd build
   cmake ..
   make

   # Run ws2812 example on GPIO 23
   ./examples/ws2812 23

Reprogramming the Onboard Microcontroller
-----------------------------------------

Make sure solder jumpers R27, R28, R29 are bridged. See
:ref:`adrd4161_swd_jumpers` for details. In this configuration, the MAX32662
microcontroller's SWD signals are exposed on the Pi's GPIOs:

* GPIO 6: SWD_IO
* GPIO 20: SWD_CLK
* GPIO 21: SWD_RSTN

The microcontroller can be reprogrammed or debugged using SWD GPIO bitbanging
modes. With ``openocd``, use the following options:

.. code-block:: bash

   openocd -s /path/to/adrd4161-fw/openocd/ \
           -f raspberrypi5-gpiod.cfg \
           -f max32662.cfg \
           ...rest of openocd command...

Replace ``/path/to/adrd4161-fw/openocd/`` with the path to a local copy of the
`adrd4161-fw <https://github.com/analogdevicesinc/adrd4161-fw>`_ repository's
openocd folder.
