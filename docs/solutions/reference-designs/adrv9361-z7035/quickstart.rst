Quick Start
===========

Required Software
-----------------

- A 16 GB (minimum) SD card imaged with
  :doc:`Kuiper Linux </linux/kuiper/index>`.
- Copy the following boot files from the ``zynq-adrv9361-z7035-fmc``
  directory to the SD card ``BOOT`` partition:

  - ``BOOT.bin``
  - ``devicetree.dtb``

- Copy ``uImage`` from the ``zynq-common`` directory to the SD card
  ``BOOT`` partition.
- A UART terminal (PuTTY, Tera Term, Minicom, etc.) configured for
  115200 baud, 8N1.

Required Hardware
-----------------

- :adi:`ADRV9361-Z7035 <ADRV9361-Z7035>` SOM
- :adi:`ADRV1CRR-FMC <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-FMC.html>`
  carrier board
- Micro-USB 2.0 UART cable
- Ethernet cable
- Power supply
- Host PC or laptop

Hardware Setup
--------------

.. image:: adrv9361-z7035-fmc-setup_quickstart.png
   :align: center
   :alt: ADRV9361-Z7035 FMC Quick Start Setup

#. Connect the ADRV1CRR-FMC carrier board to the ADRV9361-Z7035 SOM FMC
   socket.
#. Connect the Micro-USB UART cable between the carrier board and your
   host PC.
#. Connect an Ethernet cable to the **ETHERNET 1** port on the FMC carrier
   and attach it to your network.
#. Insert the prepared micro SD card into the ADRV9361-Z7035 SD card slot.
#. Optionally connect an HDMI monitor and USB OTG peripherals.
#. Connect the power supply and turn on the power switch on the FMC board.
#. Open your terminal emulator and select the correct serial port at
   115200 baud.

Upon successful boot the terminal displays the Kuiper Linux login prompt.
The default credentials are:

- **User:** analog
- **Password:** analog

Verifying the Design
--------------------

After logging in, verify the FPGA system ID:

.. code-block:: bash

   root@analog:~# dmesg | grep sysid
   [    1.595804] axi_sysid 45000000.axi-sysid-0: AXI System ID core version (1.01.a) found
   [    1.602488] axi_sysid 45000000.axi-sysid-0: [adrv9361z7035_ccfmc] on [lvds] ...

Check for errors in the kernel log:

.. code-block:: bash

   root@analog:~# dmesg -l err

Verify that the expected IIO devices are present:

.. code-block:: bash

   root@analog:~# iio_info | grep iio:device
           iio:device0: ad7291
           iio:device1: ad9361-phy
           iio:device2: xadc
           iio:device3: ad9517-3
           iio:device4: cf-ad9361-dds-core-lpc (buffer capable)
           iio:device5: cf-ad9361-lpc (buffer capable)

IIO Oscilloscope
----------------

The :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application
can be used locally (via HDMI display) or remotely over the network. To use
it remotely:

#. Determine the board's IP address using ``ifconfig`` on the target.
#. Launch IIO Oscilloscope on the host PC.
#. Go to **Settings > Connect** and enter the board's IP address.

The AD9361 plugins (formerly FMComms2/3/4 plugins) provide basic and advanced
control of the transceiver, including frequency, gain, bandwidth, and filter
configuration.

Shutting Down
-------------

This platform uses a persistent file system. To avoid file system corruption,
always perform a clean shutdown before removing power:

.. code-block:: bash

   root@analog:~# sudo shutdown -h now
