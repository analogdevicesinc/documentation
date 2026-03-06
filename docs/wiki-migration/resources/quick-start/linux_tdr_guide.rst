ADIN1100, ADIN1110 and ADIN2111 10BASE-T1L Linux TDR guide
==========================================================

Description
-----------

This guide details the steps required in order to use the TDR(time domain reflectometry) library on a hardware platform running Linux. The library may be used as part of a Linux user space sample application, or it may be linked against the user's specific code.

**Supported CPU architectures** (for the board running TDR): x86_64, aarch32/a32 (ARM32) and aarch64/a64 (ARM64)

The high level overview of the setup process is the following:

-  Setup an SD card with a Linux distribution that will work with your target board.
-  For the ADIN1110 and ADIN2111, compile the ADIN1110 Linux driver (with `this patch <https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net-next.git/commit/?id=2322467a0f5d>`__ applied). If you have a version 6.10 (or later) of the Linux kernel, you can skip this step.
-  For ADIN1100, no driver is required.
-  Replace your distribution's kernel.
-  Run the TDR example or your custom code using the TDR library on the target board (or your PC).

The Linux distribution setup and kernel compilation steps described in this guide should be executed from a PC running Linux.

.. note::

   The guide will focus on the following hardware setups:

   
   -  Raspberry Pi 4 (ARM32/ARM64) + :adi:`EVAL-ADIN1110 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adin1110.html>`
   -  Raspberry Pi 4 (ARM32/ARM64) + :adi:`EVAL-ADIN2111 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adin2111.html>`
   -  PC (x86_64) + :adi:`AD-T1LUSB2.0-EBZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-t1lusb20-ebz.html>`
   


Setting up the target platform
------------------------------

Setting up the Linux distribution - ARM32/ARM64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the ARM architecture, we'll be focused on running the TDR library example on a Raspberry Pi 4B+ board and we're going to use the Raspbian Linux distribution (with a custom kernel).

In order to setup an SD card with Raspbian follow these steps:

-  Download and install the `Raspberry Pi imager tool <https://www.raspberrypi.com/software/>`__.
-  Open the imager and choose Raspberry Pi 4 as the device and the **Raspberry Pi OS (32/64-bit)** version for Raspbian.
-  Choose an SD card on which to flash the OS and press **NEXT**.
-  Enter the settings menu by clicking the **EDIT SETTINGS** button in the pop-up window. Configure a name and password for your user and enable the **Set locale settings** checkbox. You can also enable SSH for a more convenient way of accessing the Pi's filesystem in case you don't want to connect an external display.
-  Click on the **YES** button in the pop-up window to apply the settings and then follow the instructions to write the Raspbian image to the SD card.
-  After the installation process is done, you need to expand the rootfs partition. You can do this by plugging the SD card in the Raspberry Pi board and booting the OS. At this point Raspbian should be fully functional. You can test this in the following ways:

   -  Connecting over SSH with the credentials you configured in imager. For this, your host PC should be in the same network as the Raspberry Pi. There are multiple ways of accessing your RPI remotely, and you can follow `this guide <https://www.raspberrypi.com/documentation/computers/remote-access.html>`__ to find what works for your situation.
   -  Connect a display to the Raspberry Pi's micro HDMI port and a mouse + keyboard to the USB A connectors. After this, you can power the board and check if Linux is booting.

-  Power off the Raspberry Pi and insert the SD card back in your host machine.

Setting up the Linux distribution - x86_64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We'll assume you have a PC running Linux. Any distribution should work, but for this guide we'll use `Debian 12 <https://www.debian.org/distrib/>`__.

Setup steps:

-  Download the `Debian ISO image <https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.8.0-amd64-netinst.iso>`__.
-  Burn the ISO image on an USB drive. You can do this from the terminal with the **dd** command or use a GUI application such as `Balena etcher <https://etcher.balena.io/>`__.
-  Insert the USB drive into the board/PC.
-  Reboot the board/PC into BIOS and select the USB drive as a boot media. Follow the Debian installer.

Compiling the kernel
--------------------

Depending on you target CPU's architecture, the process is the following

ARM32/ARM64
~~~~~~~~~~~

Open a terminal on your PC and run the following:

-  Install the kernel build prerequisites:

::

   sudo apt-get install git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison openssl device-tree-compiler

-  Install the GCC cross compiler:

   -  ARM32: sudo apt install gcc-arm-linux-gnueabihf -y
   -  ARM64: sudo apt install gcc-aarch64-linux-gnu -y

-  Set the ARCH and CROSS_COMPILE variables:

   -  ARM32: export ARCH=arm && export CROSS_COMPILE=arm-linux-gnueabihf-
   -  ARM64: export ARCH=arm64 && export CROSS_COMPILE=aarch64-linux-gnu-

-  Clone the Linux kernel repository

::

   git clone --depth=1 --branch rpi-6.12.y https://github.com/raspberrypi/linux
   cd linux

-  Compile the source code:

::

   make bcm2711_defconfig

Change the kernel configure with "make menuconfig" in order to enable the ADIN1110/ADIN2111 driver

-  Hit the search button (typically the slash "/" key)
-  Type ADIN1110, then hit Enter.
-  Press 1 (the key), then hit Enter
-  You should see the location + dependencies for enabling the driver
-  If the ADIN1110 symbol doesn't change to "y", make sure the drivers in the "Depends on:" list are also enabled. You will have to follow a similar process of enabling them.

::

   Symbol: ADIN1110 [=y]                                                                                                                                                                 
   Type  : tristate                                                                                                                                                                        
   Defined at drivers/net/ethernet/adi/Kconfig:20                                                                                                                                          
     Prompt: Analog Devices ADIN1110 MAC-PHY                                                                                                                                               
     Depends on: NETDEVICES [=y] && ETHERNET [=y] && NET_VENDOR_ADI [=y] && SPI [=y] && NET_SWITCHDEV [=y]                                                                               
     │   Location:                                                                                                                                                                           │  
     │     -> Device Drivers                                                                                                                                                                 │  
     │       -> Network device support (NETDEVICES [=y])                                                                                                                                     │  
     │         -> Ethernet driver support (ETHERNET [=y])                                                                                                                                    │  
     │           -> Analog Devices devices (NET_VENDOR_ADI [=y])                                                                                                                             │  
     │ (1)         -> Analog Devices ADIN1110 MAC-PHY (ADIN1110 [=y])                                                                                                                        │  
     │ Selects: CRC8 [=y] && PHYLIB [=y]

Exit menuconfig and go back to the Linux terminal.

::

   make -j8

   # This requires the SD card to be inserted
   sudo make modules_install INSTALL_MOD_PATH=/media/$USER/rootfs

-  Compile the device tree specific to your ADIN1110/ADIN2111 eval board:

::

   # ADIN1110
   wget https://raw.githubusercontent.com/analogdevicesinc/linux/refs/heads/rpi-6.6.y/arch/arm/boot/dts/overlays/rpi-adin1110-overlay.dts

   # ADIN2111
   wget https://raw.githubusercontent.com/analogdevicesinc/linux/refs/heads/rpi-6.6.y/arch/arm/boot/dts/overlays/rpi-adin2111-overlay.dts

   # Adapt the device tree overlay name if you're using ADIN2111 instead
   cpp -nostdinc -I include -I arch  -undef -x assembler-with-cpp rpi-adin1110-overlay.dts rpi-adin1110-overlay.dts.pre

   dtc -O dtb -o rpi-adin1110-overlay.dtbo rpi-adin1110-overlay.dts.pre

-  Copy the kernel image and the device tree to the SD card we flashed in the previous section:

::

   # For 64 bit
   cp arch/arm64/boot/Image /media/$USER/bootfs/kernel8.img

   # Adapt the device tree overlay name if you're using ADIN2111 instead
   cp rpi-adin1110-overlay.dtbo /media/$USER/bootfs/overlays/rpi-adin1110.dtbo

::

   # For 32 bit
   cp arch/arm/boot/zImage /media/$USER/bootfs/kernel7l.img

   # Adapt the device tree overlay name if you're using ADIN2111 instead
   cp rpi-adin1110-overlay.dtbo /media/$USER/bootfs/overlays

-  Edit the bootfs/config.txt file from the SD card to specify the device tree overlay. Add the following line:

::

   dtoverlay=rpi-adin2111

Or

::

   dtoverlay=rpi-adin1110

.. note::

   By default the Raspberry Pi 4 will boot the **kernel8.img** image (64 bit). If you want to use the 32 bit image, you'll have to add **kernel=kernel7l.img** to the config.txt file on the SD card.


x86_64
~~~~~~

If you want to use TDR with ADIN1100, no changes to the kernel are required.

Hardware setup
--------------

EVAL-ADIN1110 / EVAL-ADIN2111
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect the EVAL-ADIN1110-EBZ to the Raspberry Pi 4 (the wiring is identical for the EVAL-ADIN2111EBZ) as following:

=========================== ================
RPI                         EVAL-ADIN1110EBZ
=========================== ================
SPI_MOSI (GPIO 10) (Pin 19) T1L_MOSI
SPI_MISO (GPIO 9) (Pin 21)  T1L_MISO
SPI_CLK (GPIO 11) (Pin 23)  T1L_CLK
SPI_CEO_N (GPIO 8) (Pin 24) T1L_CS_N
GPIO 25 (Pin 22)            T1L_INT_N
GPIO 27 (Pin 13)            T1L_RESET_N
GND (Pin 6)                 GND
=========================== ================

EVAL-ADIN1110EBZ needs to operate in Generic SPI mode (see Datasheet) and with CRC protection enabled. In order to do this set every switch to the following table:

========= ========
SWITCH    POSITION
========= ========
SPI_CFG0  OFF
SPI_CFG1  ON
SWPD_N    ON
TX2V4_DIS OFF
MS_SEL    OFF
========= ========

For the EVAL-ADIN2111EBZ, the position of the switches should be the following:

========= ========
SWITCH    POSITION
========= ========
SPI_CFG0  ON
SPI_CFG1  OFF
P1_SWPD_N OFF
P2_SWPD_N OFF
========= ========

.. important::

   It's important to keep the microcontrollers on the ADIN1110/ADIN2111 eval boards in the reset state. Otherwise, the Raspberry Pi board won't be able to communicate with the MAC-PHY. For EVAL-ADIN1110EBZ, set the J301 jumper to the GND position. For the EVAL-ADIN2111EBZ, set the P8 jumper to the GND position


AD-T1LUSB2.0-EBZ
~~~~~~~~~~~~~~~~

Connect the AD-T1LUSB2.0-EBZ to your board using a micro USB cable.

TDR testing
-----------

.. _arm32arm64-1:

ARM32/ARM64
~~~~~~~~~~~

Copy the TDR library archive to the rootfs partition of the SD card. You can now insert the SD card in your target board and power it up. Once Raspbian booted run "ip a" in a terminal. The ADIN1110/ADIN2111 should have their own network interface (in this case eth0):

::

   analog@analog-desktop:~$ ip a
   1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
       link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
       inet 127.0.0.1/8 scope host lo
          valid_lft forever preferred_lft forever
       inet6 ::1/128 scope host 
          valid_lft forever preferred_lft forever
   2: dummy0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN group default qlen 1000
       link/ether 26:e1:6f:ab:e2:87 brd ff:ff:ff:ff:ff:ff
   3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
       link/ether ca:2f:b7:10:23:63 brd ff:ff:ff:ff:ff:ff
       inet6 fe80::af3b:584c:73b7:6c4c/64 scope link noprefixroute 
          valid_lft forever preferred_lft forever
   4: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
       link/ether 00:04:4b:ea:59:ee brd ff:ff:ff:ff:ff:ff
       inet 10.48.65.145/24 brd 10.48.65.255 scope global dynamic noprefixroute eth1
          valid_lft 21053sec preferred_lft 21053sec
       inet6 fe80::509a:e324:c836:2fa2/64 scope link noprefixroute 
          valid_lft forever preferred_lft forever
   5: l4tbr0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
       link/ether f2:79:c1:47:c6:11 brd ff:ff:ff:ff:ff:ff
   6: rndis0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast master l4tbr0 state DOWN group default qlen 1000
       link/ether f2:79:c1:47:c6:11 brd ff:ff:ff:ff:ff:ff
   7: usb0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast master l4tbr0 state DOWN group default qlen 1000
       link/ether f2:79:c1:47:c6:13 brd ff:ff:ff:ff:ff:ff

.. note::

   Using the ADIN2111 will result in 2 network interfaces being created, corresponding to each of the two ports.


Check if the port belongs to ADIN1110 with:

::

   analog@analog-desktop:~$ cat /sys/class/net/eth0/device/modalias
   spi:adin1110

Running the TDR example
^^^^^^^^^^^^^^^^^^^^^^^

The first step is to compile the TDR example application. he commands you'll have to run in a terminal are the following:

::

   cd /home/user
   unzip adin10spe-tdr -d adin10spe-tdr
   cd adin10spe-tdr
   wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/refs/heads/adin1100-add-additional-dbg-tools/linux/drivers/adin1100/adin10spe_phy.h
   make

After this, you may now run your application:

::

   sudo ./CableDiagTDR

.. _x86_64-1:

x86_64
~~~~~~

Power up the target PC and copy the TDR library archive in your user's home directory. If the AD-T1LUSB2.0-EBZ board is connected, you can then run "ip a" in a terminal. You should see an interface corresponding to the adapter.

::

   30: enx00e04c68045c: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
       link/ether 00:e0:4c:68:04:5c brd ff:ff:ff:ff:ff:ff
   31: eth2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
       link/ether 76:f2:44:3a:52:2f brd ff:ff:ff:ff:ff:ff
       
   $ cat /sys/class/net/eth2/device/modalias 
   usb:v0424p9E00d0300dcFFdsc00dpFFicFFisc00ipFFin00

.. _running-the-tdr-example-1:

Running the TDR example
^^^^^^^^^^^^^^^^^^^^^^^

The first step is to compile the TDR example application. Assuming you have the library archive in the /home/user directory, the commands you'll have to run in a terminal are the following:

::

   export CROSS_COMPILE=
   export ARCH=
   cd /home/user
   unzip adin10spe-tdr -d adin10spe-tdr
   cd adin10spe-tdr
   wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/refs/heads/adin1100-add-additional-dbg-tools/linux/drivers/adin1100/adin10spe_phy.h
   make

After this, you may now run your application:

::

   sudo ./CableDiagTDR
