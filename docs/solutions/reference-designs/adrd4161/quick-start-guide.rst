ADRD4161-01Z Quick Start Guide
==============================

This guide will help you get started with the ADRD4161-01Z carrier board.

Prerequisites
-------------

* ADRD4161-01Z board
* Raspberry Pi 5
* MicroSD card (16 GB or larger recommended)
* 9-70 V DC power supply
* Compatible ADIS16xxx IMU module (optional)

Step 1: Prepare the Raspberry Pi
--------------------------------

1. Download the latest Raspberry Pi OS image
2. Flash the image to the MicroSD card using Raspberry Pi Imager or similar tool
3. Insert the MicroSD card into the Raspberry Pi

Step 2: Connect the Hardware
----------------------------

1. Mount the Raspberry Pi 5 onto the ADRD4161-01Z 40-pin header
2. Connect an ADIS16xxx IMU module to the 14-pin or 16-pin connector (optional)
3. Connect the CAN bus cable if using CAN communication
4. Connect the 9-70 V DC power supply

Step 3: Configure the System
----------------------------

Boot the Raspberry Pi and configure the required device tree overlays.

For CAN bus support, add to ``/boot/firmware/config.txt``:

.. code-block:: ini

   [all]
   dtoverlay=uart0,ctsrts

For IMU support (example for ADIS16470), add:

.. code-block:: ini

   [all]
   dtoverlay=rpi-regulator
   dtoverlay=adis16475,device=adis16470,drdy_pin=4,reset_pin=25,sync_mode=0

Disable the serial console in ``/boot/firmware/cmdline.txt`` by changing
``console=serial0,...`` to ``console=tty1``.

Step 4: Verify the Setup
------------------------

After rebooting, verify the components:

**CAN bus:**

.. code-block:: bash

   sudo slcand -o -c -f -t hw -S 2000000 -s 6 /dev/ttyAMA0

**IMU (if connected):**

.. code-block:: bash

   iio_info -u local:

Next Steps
----------

* See :doc:`hardware-guide` for detailed connector and jumper information
* See :doc:`software-guide` for advanced configuration options
