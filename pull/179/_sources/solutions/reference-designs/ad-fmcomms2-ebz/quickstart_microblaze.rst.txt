.. _ad-fmcomms2-ebz-microblaze:

MicroBlaze Quick Start Guide
=============================

This guide provides instructions on how to set up the AD-FMCOMMS2-EBZ on
MicroBlaze-based FPGA carriers.

Supported Carriers
------------------

- :xilinx:`KC705 <products/boards-and-kits/ek-k7-kc705-g.html>`
- :xilinx:`VC707 <products/boards-and-kits/ek-v7-vc707-g.html>`

Required Hardware
-----------------

- Xilinx KC705 or VC707 FPGA board
- AD-FMCOMMS2-EBZ or AD-FMCOMMS3-EBZ FMC board
- Micro / Mini-USB cable

Required Software
-----------------

- Bitfile and Linux ELF image
- Xilinx XSCT/XSDB console (part of Vivado/Vitis)
- A UART terminal (Tera Term / PuTTY / Minicom), baud rate 115200 (8N1)

Hardware Setup
--------------

#. Connect the AD-FMCOMMS2-EBZ FMC board to the FPGA carrier:

   - **KC705**: LPC FMC connector
   - **VC707**: FMC1 HPC connector

#. Connect USB JTAG (Micro USB) to your host PC.
#. Turn on the power switch on the FPGA board.
#. Open the XSCT/XSDB console to configure the FPGA and download the ELF
   image.

Loading the Design
-------------------

Use the XSCT/XSDB console (included with Vivado/Vitis) to download the
bitstream and ELF image to the FPGA board.

.. code-block:: none

   # Connect to the target board
   connect

   # For KC705:
   targets -set -filter {name =~ "xc7k325t"}
   fpga -f system_top.bit
   after 2000
   targets -set -filter {name =~ "MicroBlaze*"}
   dow simpleImage.kc705_fmcomms2-3
   con

   # For VC707:
   targets -set -filter {name =~ "xc7vx485t"}
   fpga -f system_top.bit
   after 2000
   targets -set -filter {name =~ "MicroBlaze*"}
   dow simpleImage.vc707_fmcomms2-3
   con

.. note::

   Bitstream and ELF images can be obtained from the ADI Kuiper Linux
   release or built from source using the ADI HDL and Linux repositories.
   The ``simpleImage`` ELF files contain the Linux kernel, devicetree, and
   root filesystem in a single file.

Expected Boot Messages
----------------------

After loading, the UART terminal will display Linux kernel boot messages. Key
messages to look for:

- ``ad9361 spi0.0: ad9361_probe : AD936x Rev 2 successfully initialized``
  confirms the AD9361 device was detected and initialized.
- ``cf_axi_dds ... probed DDS AD9361`` confirms the AXI DAC DDS core is
  operational.
- ``cf_axi_adc ... probed ADC AD9361 as MASTER`` confirms the AXI ADC core is
  operational.
- ``axi_sysid ... [fmcomms2] on [kc705]`` confirms the correct HDL project
  was loaded.
- ``Starting IIO Server Daemon`` confirms the IIO daemon is running and ready
  for remote connections.

After boot completes, log in with username ``root`` (default password:
``analog``).

Networking
~~~~~~~~~~

The MicroBlaze platform uses the Xilinx EmaClite Ethernet controller. The
system is configured with DHCP by default. If a direct Ethernet connection is
used, a static IP can be set:

.. code-block:: bash

   ifconfig eth0 192.168.1.10 netmask 255.255.255.0

IIO Oscilloscope Remote
-----------------------

The :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application can
be used to connect remotely to the MicroBlaze platform from a network-enabled
Linux host.

#. Build and start the IIO Oscilloscope on your host PC.
#. Go to **Settings > Connect** and enter the IP address of the target in the
   popup window.
#. The FMCOMMS2 plugin will load, allowing control of the AD9361 transceiver.

.. figure:: quickstart/fmcomms2-osc-plugin.png
   :align: center

   IIO Oscilloscope FMCOMMS2 plugin

.. figure:: quickstart/fmcomms2-iio-osc.png
   :align: center

   IIO Oscilloscope capture display
