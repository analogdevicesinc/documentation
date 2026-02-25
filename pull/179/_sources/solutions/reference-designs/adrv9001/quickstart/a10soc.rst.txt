.. _adrv9001-a10soc:

ADRV9002 Arria 10 SoC Quick Start Guide
=========================================

This guide provides step by step instructions on how to set up the
:adi:`EVAL-ADRV9002` (ADRV9002NP/W1/PCBZ and ADRV9002NP/W2/PCBZ) on:

- :intel:`Arria 10 SoC Development Kit
  <content/www/us/en/products/details/fpga/development-kits/arria/10-sx.html>`
  Rev C or later

Required Software
-----------------

- 16 GB SD card imaged using :doc:`/linux/kuiper/index`. Use the 2020_R1 or
  later release.
- Copy the boot files from the ``socfpga_arria10_socdk_adrv9002`` directory
  directly on the SD card ``BOOT`` partition:

  - ``socfpga_arria10_socdk.rbf``
  - ``socfpga_arria10_socdk_sdmmc.dtb``
  - ``zImage`` (from ``socfpga_arria10-common`` folder)

- Write ``preloader_bootloader.bin`` from the
  ``socfpga_arria10_socdk_adrv9002`` folder to the third SD card partition:

  .. code-block:: console

     root@host:~# dd if="./preloader_bootloader.bin" of="/dev/sdX3" bs=512

- A UART terminal (PuTTY/Tera Term/Minicom, etc.), baud rate 115200 (8N1).

Required Hardware
-----------------

- :intel:`Arria 10 SoC Development Kit
  <content/www/us/en/products/details/fpga/development-kits/arria/10-sx.html>`
  Rev C or later
- :adi:`EVAL-ADRV9002` FMC board
- Reference clock source
- Mini-USB cable
- Ethernet cable
- Optionally USB keyboard, mouse and a DisplayPort compatible monitor

.. warning::

   ESD precautions should be taken when handling evaluation boards.

FMC Pin Connection Rework
--------------------------

To be compatible with the :adi:`EVAL-ADRV9002`, the Arria 10 SoC Development
Kit requires a minor rework.

In the default configuration, some of the FMC header pins are connected to a
dedicated clock chip. To be compatible with the :adi:`EVAL-ADRV9002`, these
pins need to be connected directly to the FPGA.

The connection of those pins can be changed by moving the position of four
zero Ohm resistors:

- R612 to R610
- R613 to R611
- R621 to R620
- R633 to R632

These resistors can be found on the backside of the Arria 10 SoC Development
Kit underneath the FMC A connector (J29).

.. image:: a10soc_fmc_rework.jpg
   :align: center
   :width: 400

Testing
-------

.. warning::

   Before executing below steps, **VADJ for FMCA must be set to 1.8V**.
   This can be done by changing VADJ FMCA Voltage using J42.

On the ADRV9002 card, there is a red LED close to the FMC connector. This LED
indicates if VADJ voltage exceeded 2.0V. If the LED does not turn off after a
few seconds after boot, VADJ is exceeding the recommended level, decreasing
board lifetime and potentially causing permanent damage to the IC.

.. image:: adrv9002_a10soc_vadj_jumper.png
   :align: center

- Connect the :adi:`EVAL-ADRV9002` FMC board to the FMCA carrier socket.
- On the FMC card, set the switch to select clock source between:

  - an on-board 38.4 MHz VCTCXO (default)
  - external (via J501) 10 MHz to 1000 MHz / +13 dBm

- Connect USB UART (Mini-USB) to your host PC.
- Insert SD card into socket.
- Configure the Arria 10 SoC Development Kit for SD card booting (set the
  jumpers and switches accordingly).
- Turn on the power switch on the FPGA board.
- Observe kernel and serial console messages on your terminal.

Expected IIO Devices
~~~~~~~~~~~~~~~~~~~~

These devices should be present after a successful boot:

.. code-block:: console

   root@analog:~# iio_info | grep ':device'
           iio:device0: adrv9002-phy
           iio:device1: axi-adrv9002-rx-lpc (buffer capable)
           iio:device2: axi-adrv9002-tx-lpc (buffer capable)

.. note::

   The Arria 10 SoC configuration uses a single R1T1 interface. For more
   details on device modes, see the
   :git-linux:`ADRV9002 Linux driver documentation <drivers/iio/adc/navassa>`.

pyadi-iio
~~~~~~~~~

`pyadi-iio <https://github.com/analogdevicesinc/pyadi-iio>`__ is a Python
abstraction module for ADI hardware with IIO drivers. An ADRV9002 example
can be found
`here <https://github.com/analogdevicesinc/pyadi-iio/blob/main/examples/adrv9002_example.py>`__.

IIO Oscilloscope
~~~~~~~~~~~~~~~~

The :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application
can be used to connect to another platform that has a connected device in
order to configure the device and read data from it.

Build and start osc on a network-enabled Linux host. Once the application is
launched, go to Settings > Connect and enter the IP address of the target.

.. note::

   Even though this is Linux, this is a persistent file system. Care should
   be taken not to corrupt the file system --- please shut down properly.
   Use ``sudo shutdown -h now`` from the terminal.
