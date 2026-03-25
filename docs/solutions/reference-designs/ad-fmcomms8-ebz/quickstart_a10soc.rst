.. _ad-fmcomms8-ebz-a10soc:

Arria 10 SoC Quick Start Guide
===============================

This guide provides instructions on how to set up the AD-FMCOMMS8-EBZ on
the :intel:`Arria 10 SoC Development Kit
<content/www/us/en/products/details/fpga/arria/10/sx.html>` (Rev. C or later).

.. figure:: quickstart/fmcomms8_a10soc.jpeg
   :align: center
   :width: 600

   AD-FMCOMMS8-EBZ on the Arria 10 SoC Development Kit

Required Hardware
-----------------

- :intel:`Arria 10 SoC Development Kit
  <content/www/us/en/products/details/fpga/arria/10/sx.html>` Rev. C or later
- AD-FMCOMMS8-EBZ evaluation board
- Mini-USB cable
- Ethernet cable
- Optionally: USB keyboard, mouse, and a DisplayPort compatible monitor

Required Software
-----------------

- SD card (16 GB or larger) imaged with the latest
  :doc:`Kuiper Linux </linux/kuiper/index>` release
- Copy the following boot files from the ``socfpga_arria10_socdk_fmcomms8``
  directory into the SD card **BOOT** partition:

  - ``socfpga_arria10_socdk.rbf``
  - ``socfpga_arria10_socdk_sdmmc.dtb``
  - ``zImage`` (from ``socfpga_arria10-common`` folder)

- Write ``preloader_bootloader.bin`` from the
  ``socfpga_arria10_socdk_fmcomms8`` folder to the third SD card partition:

  .. code-block:: bash

     dd if="./preloader_bootloader.bin" of="/dev/sdX3" bs=512

- A UART terminal (PuTTY / Tera Term / Minicom), baud rate 115200 (8N1)

FMC Pin Connection Rework
-------------------------

To be compatible with the AD-FMCOMMS8-EBZ, the Arria 10 SoC Development Kit
requires a minor rework. In the default configuration, some of the FMC header
pins are connected to a dedicated clock chip. These pins need to be connected
directly to the FPGA instead.

The connection of those pins can be changed by moving the position of six
zero-ohm resistors:

.. list-table::
   :header-rows: 1

   * - Remove
     - Install
   * - R575
     - R574
   * - R576
     - R577
   * - R612
     - R610
   * - R613
     - R611
   * - R621
     - R620
   * - R633
     - R632

These resistors can be found on the backside of the Arria 10 SoC Development
Kit underneath the FMC A connector (J29).

.. figure:: quickstart/a10soc_fmc_rework_6r.jpg
   :align: center
   :width: 400

   Required resistor configuration for AD-FMCOMMS8-EBZ compatibility

Hardware Setup
--------------

#. Connect the AD-FMCOMMS8-EBZ board to the **FMC A** carrier socket.
#. Connect USB UART (Mini USB) to your host PC.
#. Insert the SD card.
#. Configure the Arria 10 SoC Development Kit for SD card booting (set the
   jumpers and switches accordingly).
#. Turn on the power switch on the FPGA board.
#. Observe kernel and serial console messages on your terminal.

Expected Boot Messages
----------------------

After power-on, the UART terminal will display U-Boot and Linux kernel boot
messages. Key messages to look for:

- ``adrv9009 spi0.1: adrv9009_info: adrv9009 Rev 192, ... successfully initialized via jesd204-fsm``
  confirms ADRV9009 initialization.
- ``adrv9009 spi0.0: adrv9009_info: adrv9009-x2 Rev 192, ... successfully initialized via jesd204-fsm``
  confirms the second ADRV9009 (x2) initialization.
- ``cf_axi_adc ... probed ADC ADRV9009-X2 as MASTER`` confirms the AXI ADC
  core is operational.

After boot completes, log in with:

- Username: ``analog``
- Password: ``analog``
