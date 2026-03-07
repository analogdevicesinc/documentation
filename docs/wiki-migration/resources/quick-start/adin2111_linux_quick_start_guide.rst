ADIN2111 10BASE-T1L SWITCH Linux Driver Quick Start
===================================================

Description
-----------

This is a Quick Start Guide on how to properly connect and use the EVAL-ADIN1110EBZ on multiple platforms in a Linux environment.

RPI 3
~~~~~

================================ ===================================
RPI 3 to EVAL-ADIN2111EBZ Wiring EVAL-ADIN2111EBZ Switches positions
================================ ===================================
|image1|                         |image2|
================================ ===================================

Wiring and software is similar for RPI 4.

Wiring
^^^^^^

=========================== ================
RPI 3                       EVAL-ADIN2111EBZ
=========================== ================
SPI_MOSI (GPIO 10) (Pin 19) SDI
SPI_MISO (GPIO 9) (Pin 21)  SDO/SPI
SPI_CLK (GPIO 11) (Pin 23)  SCLK
SPI_CEO_N (GPIO 8) (Pin 24) CS_N
GPIO 25 (Pin 22)            INT_N
GND                         AGND
=========================== ================

Connect both grounds (AGND) (idealy) to the most accessible ground to you on the RPI 3.

Board settings
^^^^^^^^^^^^^^

ADIN2111 needs to operate in Generic SPI mode (see Datasheet) and with CRC protection disabled. You may enable the CRC but that needs a change in the DT also. See :git-linux:`adin1110.yaml <Documentation/devicetree/bindings/net/adi%2Cadin1110.yaml>`.

In order to do this find S201 and set every switch to the following table:

========= ========
SWITCH S1 POSITION
========= ========
SPI_CFG1  OFF
SPI_CFG0  ON
========= ========

========= ========
SWITCH S4 POSITION
========= ========
1         OFF
2         ON
3         OFF
4         OFF
========= ========

Software Setup
^^^^^^^^^^^^^^

Getting a Raspbian Image
""""""""""""""""""""""""

Download an SD Card Image: `ADI Kuiper <:doc:`/wiki-migration/resources/tools-software/linux-software/embedded_arm_images`>`_ or other Raspbian Linux Image.

Preparing the SD card
"""""""""""""""""""""

Write the image to the sd card: <code> sudo dd status=progress if=2022-05-29-ADI-Kuiper-full.img of=/dev/mmcblk0 bs=4M conv=fsync </code>

Setup RPI to use the ADIN1110 overlay. To do this go to the boot partition of the SD card and write in the config.txt file:

::

   [all]
   dtoverlay=rpi-adin2111

After the change above, reboot.

Testing
^^^^^^^

If everything worked out fine, you should be able to see after typing `ip a <https://linux.die.net/man/8/ip>`_ or ifconfig:

::

   root@analog:~# ip a
   1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
       link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
       inet 127.0.0.1/8 scope host lo
          valid_lft forever preferred_lft forever
   2: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
       link/ether ca:2f:b7:10:23:63 brd ff:ff:ff:ff:ff:ff
   3: eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
       link/ether ca:2f:b7:10:23:63 brd ff:ff:ff:ff:ff:ff
   4: eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
       link/ether b8:27:eb:04:14:01 brd ff:ff:ff:ff:ff:ff
       inet 10.48.65.160/24 brd 10.48.65.255 scope global dynamic noprefixroute eth2
          valid_lft 19413sec preferred_lft 16713sec

Check if the port belongs to ADIN2111 with:

::

   root@analog:~# cat /sys/class/net/eth1/device/modalias
   spi:adin2111

Check if port if p0 or p1:

::

   root@analog:~# cat /sys/class/net/eth0/phys_port_name
   p0

NXP 8MMINI-BB
~~~~~~~~~~~~~

==================================== ===================================
8MMINI-BB to EVAL-ADIN2111EBZ Wiring EVAL-ADIN2111EBZ Switches positions
==================================== ===================================
|image3|                             |image4|
==================================== ===================================

.. _wiring-1:

Wiring
^^^^^^

==================== ================
8MMINI-BB            EVAL-ADIN1110EBZ
==================== ================
ECSPI2_MOSI (Pin 19) SDI
ECSPI2_MISO (Pin 21) SDO/SPI
ECSPI2_SCLK (Pin 23) SCLK
GPIO 24 (Pin 35)     CS_N
GPIO 25 (Pin 37)     INT_N
GND                  AGND
==================== ================

Connect both grounds (idealy) to the most accessible ground to you on the 8MMINI-BB.

.. _board-settings-1:

Board settings
^^^^^^^^^^^^^^

ADIN2111 needs to operate in Generic SPI mode (see Datasheet) and with CRC protection enabled.

In order to do this find S201 and set every switch to the following table:

========= ========
SWITCH S1 POSITION
========= ========
SPI_CFG1  OFF
SPI_CFG0  OFF
========= ========

========= ========
SWITCH S4 POSITION
========= ========
1         OFF
2         ON
3         OFF
4         OFF
========= ========

Make sure IMX8MM-BB is set to boot from the SD Card, for more details go to `Boot Switch Setup <https://www.nxp.com/document/guide/get-started-with-the-i-mx-8m-mini-evkb:GS-iMX-8M-Mini-EVK>`_.

.. _software-setup-1:

Software Setup
^^^^^^^^^^^^^^

Preparing an SD Card
""""""""""""""""""""

You need a SD Card with a NXP Linux image on it, more details `here <https://www.nxp.com/document/guide/get-started-with-the-i-mx-8m-mini-evkb:GS-iMX-8M-Mini-EVK>`_. From NPX `Software Downloads <https://www.nxp.com/design/software/embedded-software/i-mx-software/embedded-linux-for-i-mx-applications-processors:IMXLINUX>`_ page, download the `L5.15.52_2.1.0 SD card image <https://www.nxp.com/webapp/sps/download/license.jsp?colCode=L5.15.52_2.1.0_MX8MM&appType=file1&DOWNLOAD_ID=null>`_. In case of broken link/missing image, try any other that is at least 5.10. Extract the archive and find the SD Card image file:

::

   6,8G imx-image-full-imx8mmevk.wic

This you can directly write to an SD Card in order to get a functional 8MMINI-BB system:

::

   sudo dd status=progress if=imx-image-full-imx8mmevk.wic of=/dev/mmcblk0 bs=4M conv=fsync

At this point you can insert the card in the 8MMINI-BB, power it, connect the UART and you should be able to login.

::

   NXP i.MX Release Distro 5.15-kirkstone imx8mmevk ttymxc1

   imx8mmevk login: [   12.063688] fec 30be0000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx
   [   12.071502] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready

   imx8mmevk login: root
   root@imx8mmevk:~#

Setting up Linux
""""""""""""""""

Get the latest branch from NXP: `linux-fslc <https://github.com/Freescale/linux-fslc>`_. At this moment `5.19.x+fslc <https://github.com/Freescale/linux-fslc/tree/5.19.x+fslc>`_ is the latest. The reason is that ADIN1100, the 10-BaseT1L PHY already is added here.

Add the `ADIN1110 <https://github.com/torvalds/linux/blob/master/drivers/net/ethernet/adi/adin1110.c>`_ driver from torvalds git. You can also apply these two patches bellow: `net-adin1110-5-19-add-support.zip <https://wiki.analog.com/_media/resources/quick-start/net-adin1110-5-19-add-support.zip>`_

Compiling Linux
"""""""""""""""

::

   sudo apt-get install gcc-aarch64-linux-gnu
   export ARCH=arm64
   export CROSS_COMPILE=/usr/bin/aarch64-linux-gnu-
   cp arch/arm64/configs/defconfig .config
   make menuconfig

Enable ADIN1100 and ADIN1110 from the make menuconfig. Note: ADIN2111 is supported by the adin1110.c Linux driver.

::

   make -j 8 Image modules dtbs
   sudo make modules_install INSTALL_MOD_PATH=/media/<user>/rootfs
   cp arch/arm64/boot/Image /media/<user>/boot/Image
   cp arch/arm64/boot/dts/freescale/imx8mm-evk.dtb /media/<user>/BOOT

You also need to add ADIN2111 to the device tree. You can add the following line at the end of arch/arm64/boot/dts/freescale/imx8mm-evk.dts. Recompile after DT changes:

::

   make -j 8 dtbs

::

   &iomuxc {
           pinctrl_ecspi2: ecspi2-grp {
           fsl,pins = <
                   MX8MM_IOMUXC_ECSPI2_MISO_ECSPI2_MISO    0x00000116
                   MX8MM_IOMUXC_ECSPI2_MOSI_ECSPI2_MOSI    0x00000116
                   MX8MM_IOMUXC_ECSPI2_SCLK_ECSPI2_SCLK    0x00001916
                   MX8MM_IOMUXC_SAI5_RXD3_GPIO3_IO24   0x00000116
                   MX8MM_IOMUXC_SAI5_RXD1_GPIO3_IO22   0x00000116
                   >;
       };
   };

   &ecspi2 {
       pinctrl-names = "default";
       pinctrl-0 = <&pinctrl_ecspi2>;
       cs-gpios = <&gpio3 24 GPIO_ACTIVE_LOW>;
       dmas = <0>;
       dma-names = <0>;
       status = "okay";

       ethernet@0 {
           compatible = "adi,adin2111";

           /* SPI CS number */
           reg = <0>;

           /* will need 23 MHz for 10 Mbps, lower speeds will result in lower bandwidth */
           spi-max-frequency = <10000000>;

           /* optional, will check all control read/writes over SPI */
           adi,spi-crc;

           #address-cells = <1>;
           #size-cells = <0>;

           /* an IRQ is required, INT_N pin is configured to signal RX/TX frames */
           interrupt-parent = <&gpio3>;
           interrupts = <22 IRQ_TYPE_LEVEL_LOW>;

           /* This is the host MAC address, by default ADIN2111 will also accept broadcast frames */
           mac-address = [ CA 2F B7 10 23 63 ];

           phy@0 {
               compatible = "ethernet-phy-id0283.bc91";
               phy-10base-t1l-2.4vpp = <1>;
               reg = <0x0>;
           };

                   phy@1 {
               compatible = "ethernet-phy-id0283.bc91";
               phy-10base-t1l-2.4vpp = <1>;
               reg = <0x0>;
           };
       };
   };

Copy the modified DT on the boot partition of the SD Card:

::

   cp arch/arm64/boot/dts/freescale/imx8mm-evk.dtb /media/<user>/BOOT

.. _testing-1:

Testing
^^^^^^^

If everything worked fine when typing `ip a <https://linux.die.net/man/8/ip>`_ you should see:

::

   root@imx8mmevk:~# ip a
   1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
       link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
       inet 127.0.0.1/8 scope host lo
          valid_lft forever preferred_lft forever
   2: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
       link/ether ca:2f:b7:10:23:63 brd ff:ff:ff:ff:ff:ff
   3: eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
       link/ether ca:2f:b7:10:23:63 brd ff:ff:ff:ff:ff:ff
   4: eth2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
       link/ether 00:04:9f:05:fa:1d brd ff:ff:ff:ff:ff:ff

To figure out which one is the ADIN2111:

::

   root@imx8mmevk:~# cat /sys/class/net/eth0/device/modalias
   spi:adin2111

To figure out which one is port 0 or 1:

::

   root@imx8mmevk:~# cat /sys/class/net/eth0/phys_port_name
   p0
   root@imx8mmevk:~# cat /sys/class/net/eth1/phys_port_name
   p1

NVIDIA Jetson Nano
~~~~~~~~~~~~~~~~~~

+----------------------------------------+-------------------------------------+
| Jetson Nano to EVAL-ADIN2111EBZ Wiring | EVAL-ADIN2111EBZ Switches positions |
+========================================+=====================================+
| |image7|                               | |image8|                            |
+----------------------------------------+-------------------------------------+

.. _wiring-2:

Wiring
^^^^^^

============================ ================
Jetson Nano                  EVAL-ADIN2111EBZ
============================ ================
SPI0_MOSI (GPIO 16) (Pin 19) SDI
SPI0_MISO (GPIO 17) (Pin 21) SDO/SPI
SPI0_CLK (GPIO 18) (Pin 23)  SCLK
SPI0_CS0 (GPIO 19) (Pin 24)  CS_N
GPIO 13 (Pin 22)             INT_N
GND                          AGND
============================ ================

Connect both grounds (AGND) (idealy) to the most accessible ground to you on the Jetson Nano. Also, avoid powering the EVAL-ADIN2111EBZ from the USB of Jetson Nano, driver won't probe correctly because power to the USB is given too late in boot stage. (Try powering from 5V pins or externally if possible).

.. _board-settings-2:

Board settings
^^^^^^^^^^^^^^

ADIN2111 needs to operate in Generic SPI mode (see Datasheet) and with CRC protection disabled. You may enable the CRC but that needs a change in the DT also. See :git-linux:`adin1110.yaml <Documentation/devicetree/bindings/net/adi%2Cadin1110.yaml>`.

In order to do this find S201 and set every switch to the following table:

========= ========
SWITCH S1 POSITION
========= ========
SPI_CFG1  OFF
SPI_CFG0  ON
========= ========

========= ========
SWITCH S4 POSITION
========= ========
1         OFF
2         ON
3         OFF
4         OFF
========= ========

Getting your Jetson Nano flashed with the SDK Manager
"""""""""""""""""""""""""""""""""""""""""""""""""""""

Here we are flashing the Jetson Nano P3448. In this case we have the production kit that boots from an eMMC and not the one with the SD Card reader.

.. note::

   Skip this step if you have already flashed the Jetson Nano and have the 4.9 Kernel installed. Go to Changing the Kernel and DT step.


Setup for NVIDIA Jetson Nano and ADIN2111 (8 Nov 2022)

Download and load the Docker version of SDK Manager from NVIDIA. Power NVIDIA Jetson Nano board in recovery mode. (By connecting pin 9 and 10). Connect the UART.

Launch the SDK Manager Docker:

::

   sudo docker run -it --rm  --privileged -v /dev/bus/usb:/dev/bus/usb/ -v /dev:/dev -v /media/$USER:/media/nvidia:slave --name JetPack_NX_Devkit --network host 77ae6063b39c \
   --cli install --logintype devzone --product Jetson --version 4.6.2 --targetos Linux --host --target JETSON_NANO_TARGETS --flash all --additionalsdk 'DeepStream 6.0.1'

Where 77ae6063b39c is the id of the docker loaded previously.

Follow the instructions provided in the GUI of the SDK Manager.

At the end of this process you should now have an NVIDIA Jetson Nano flashed with the 4.9 Linux Kernel Version. Make sure you can access the board via ssh, you will need it later.

Changing the Kernel and DT
^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to build the 4.9 Kernel and DTs from NVIDIA you need to setup the environment.

1. Install the Linaro 7.3.1 2018.05 toolchain:

::

   mkdir $HOME/linaro-2018-gcc
   cd $HOME/linaro-2018-gcc
   wget http://releases.linaro.org/components/toolchain/binaries/7.3-2018.05/aarch64-linux-gnu/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.tar.xz
   tar xf gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.tar.xz

2. Download the public NVIDIA Jetson Nano sources:

::

   wget https://developer.download.nvidia.com/embedded/L4T/r32-3-1_Release_v1.0/Sources/T210/public_sources.tbz2
   tar -xvf public_sources.tbz2
   cd Linux_for_Tegra/source/public
   NVIDIA_JETSON_NANO_KERNEL=$(pwd)
   tar -xf kernel_src.tbz2

After following the guide above, you should have the following directories:

::

   user$ ~/Linux_for_Tegra/source/public  ls -la | grep -ie drwx
   drwxr-xr-x  7 <user> <user>      4096 nov 18 19:23 .
   drwxr-xr-x  4 <user> <user>      4096 nov 16 13:28 ..
   drwxrwxr-x  3 <user> <user>      4096 nov 15 21:06 hardware
   drwxrwxr-x  5 <user> <user>      4096 nov 18 19:23 kernel

By default the 4.9 Kernel does not have the ADIN1100 driver nor the ADIN1110. You will need to download the kernel sources, add the adin1100/adin1110 drivers.

Extract this archive `4.9.253-adin1110_tegra_files.zip <https://wiki.analog.com/_media/resources/quick-start/4.9.253-adin1110_tegra_files.zip>`_ in Linux_for_Tegra/source/public path. This archive contains:

+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| File                                                         | Description                                                                                                                                                          |
+==============================================================+======================================================================================================================================================================+
| kernel/kernel-4.9/driver/drivers/net/phy/Kconfig             | Linux 4.9 PHY Kconfig with the necessary adjustments                                                                                                                 |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kernel/kernel-4.9/driver/drivers/net/phy/Makefile            | Linux 4.9 PHY Makefile with the necessary adjustments                                                                                                                |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kernel/kernel-4.9/driver/drivers/net/phy/adin1100.c          | Linux 4.9 adin1100 PHY                                                                                                                                               |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kernel/kernel-4.9/driver/drivers/net/ethernet/adi/adin1110.c | Linux 4.9 adin1110/2111 MAC/SWITCH                                                                                                                                   |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kernel/kernel-4.9/driver/drivers/net/ethernet/adi/Makefile   | Linux 4.9 ethernet Makefile with the necessary adjustments                                                                                                           |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kernel/kernel-4.9/driver/drivers/net/ethernet/adi/Kconfig    | Linux 4.9 ethernet Kconfig with the necessary adjustments                                                                                                            |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kernel/kernel-4.9/arch/arm64/configs/adi_tegra_defconfig     | A modified tegra_defconfig with PHY + MAC + SWITCHDEV enabled                                                                                                        |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kernel/kernel-4.9/scripts/Kbuild.include                     | Original Kbuild.include with a small bugfix see `here details <https://wiki.analog.com/https/forums.developer.nvidia.com/t/failed-to-make-l4t-kernel-dts/116399/9>`_ |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kernel/kernel-4.9/include/uapi/linux/types.h                 | Original types.h with a compile error fixed.                                                                                                                         |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------+-------------------------------------------------+
| hardware/nvidia/platform/t210/porg/kernel-dts/tegra-jetson-nano-adin1110.dtsi                 | ADIN1110 dtsi connected to Jetson Nano DT       |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------+
| hardware/nvidia/platform/t210/porg/kernel-dts/tegra-jetson-nano-adin2111.dtsi                 | ADIN2111 dtsi connected to Jetson Nano DT       |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------+
| hardware/nvidia/platform/t210/porg/kernel-dts/tegra210-p3448-0002-p3449-0000-b00-adin1110.dts | dts for ADIN1110 with the rest of includes      |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------+
| hardware/nvidia/platform/t210/porg/kernel-dts/tegra210-p3448-0002-p3449-0000-b00-adin2111.dts | dts for ADIN2111 with the rest of includes      |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------+
| hardware/nvidia/platform/t210/porg/kernel-dts/Makefile                                        | Original Makefile with added compile directives |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------+

On ADI repo there is a branch with both :git-linux:`ADIN1100 and ADIN1110 backported <tree/adi-4.9.0-adin1100-adin1110>`. See last two commits.

Building the Kernel and DT
^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the commands bellow in order to build the kernel and the dtbs. No need to also build/install the modules at this point.

::

   NVIDIA_JETSON_NANO_KERNEL=$(pwd)
   LINARO_TOOLCHAIN=$HOME/linaro-2018-gcc/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-
   TEGRA_KERNEL_OUT=$NVIDIA_JETSON_NANO_KERNEL/build
   make -C kernel/kernel-4.9/ ARCH=arm64 O=$TEGRA_KERNEL_OUT LOCALVERSION=-tegra CROSS_COMPILE=${LINARO_TOOLCHAIN} adi_tegra_defconfig
   make -C kernel/kernel-4.9/ ARCH=arm64 O=$TEGRA_KERNEL_OUT LOCALVERSION=-tegra CROSS_COMPILE=${LINARO_TOOLCHAIN} -j 8 --output-sync=target Image
   make -C kernel/kernel-4.9/ ARCH=arm64 O=$TEGRA_KERNEL_OUT LOCALVERSION=-tegra CROSS_COMPILE=${LINARO_TOOLCHAIN} -j 8 --output-sync=target dtbs

After running the commands above you should have the following resources:

::

   ./build/arch/arm64/boot/dts/tegra210-p3448-0002-p3449-0000-b00-adin2111.dtb
   ./build/arch/arm64/boot/dts/tegra210-p3448-0002-p3449-0000-b00-adin1110.dtb
   ./build/arch/arm64/boot/Image

.. note::

   If using a make newer than 4.3, there is a BUG, workaround is to: To make it working you must edit the file: scripts/Kbuild.include Then change lines:

   
   ::
   
      the-space :=
      the-space +=
   
   To:
   
   ::
   
      E =
      the-space = $E $E
   


Installing the Kernel and DT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copy the binaries to the board:

::

   scp build/arch/arm64/boot/Image <user>@<jetson-nano-ip>:.
   scp ./build/arch/arm64/boot/dts/tegra210-p3448-0002-p3449-0000-b00-adin2111.dtb <user>@<jetson-nano-ip>:.

Login on the board and copy these files to the /boot folder. Boot partion should be mounted there:

::

   analog@analog-desktop:~$ sudo cp Image /boot/
   analog@analog-desktop:~$ sudo cp tegra210-p3448-0002-p3449-0000-b00-adin2111.dtb /boot/

Make extlinux.conf point to the newly added dt:

::

   analog@analog-desktop:~$ cat /boot/extlinux/extlinux.conf
   TIMEOUT 30
   DEFAULT primary

   MENU TITLE L4T boot options

   LABEL primary
         MENU LABEL primary kernel
         LINUX /boot/Image
         FDT /boot/tegra210-p3448-0002-p3449-0000-b00-adin2111.dtb
         INITRD /boot/initrd
         APPEND ${cbootargs} quiet root=/dev/mmcblk0p1 rw rootwait rootfstype=ext4 console=ttyS0,115200n8 console=tty0 fbcon=map:0 net.ifnames=0 sdhci_tegra.en_boot_part_access=1

Reboot the Jetson Nano.

.. _testing-2:

Testing
^^^^^^^

If everything worked out fine, you should be able to see after typing `ip a <https://linux.die.net/man/8/ip>`_ or ifconfig:

::

   analog@analog-desktop:~$ ip a
   1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
       link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
       inet 127.0.0.1/8 scope host lo
          valid_lft forever preferred_lft forever
       inet6 ::1/128 scope host
          valid_lft forever preferred_lft forever
   2: dummy0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN group default qlen 1000
       link/ether 5a:7e:b8:4d:77:6c brd ff:ff:ff:ff:ff:ff
   3: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
       link/ether ca:2f:b7:10:23:63 brd ff:ff:ff:ff:ff:ff
   4: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
       link/ether ca:2f:b7:10:23:63 brd ff:ff:ff:ff:ff:ff
       inet6 fe80::1c77:3948:e800:fc83/64 scope link noprefixroute
          valid_lft forever preferred_lft forever
   5: eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
       link/ether 00:04:4b:ea:59:ee brd ff:ff:ff:ff:ff:ff
       inet 10.48.65.145/24 brd 10.48.65.255 scope global dynamic noprefixroute eth2
          valid_lft 21579sec preferred_lft 21579sec
       inet6 fe80::7a63:79a1:e82a:2d6d/64 scope link noprefixroute
          valid_lft forever preferred_lft forever
   6: l4tbr0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
       link/ether f2:79:c1:47:c6:11 brd ff:ff:ff:ff:ff:ff
   7: rndis0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast master l4tbr0 state DOWN group default qlen 1000
       link/ether f2:79:c1:47:c6:11 brd ff:ff:ff:ff:ff:ff
   8: usb0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast master l4tbr0 state DOWN group default qlen 1000
       link/ether f2:79:c1:47:c6:13 brd ff:ff:ff:ff:ff:ff

Check if the port belongs to ADIN2111 with:

::

   root@analog:~# cat /sys/class/net/eth1/device/modalias
   spi:adin2111

Check if port if p0 or p1:

::

   analog@analog-desktop:~$ cat /sys/class/net/eth0/phys_port_name
   p0
   analog@analog-desktop:~$ cat /sys/class/net/eth1/phys_port_name
   p1

More Info
^^^^^^^^^

Ask a question: :ez:`Engineer Zone Linux <linux-software-drivers/f/q-a>`.

Details about the `ADIN1100 Linux Driver <:doc:`/wiki-migration/resources/tools-software/linux-drivers/net-phy/adin1100`>`_.

Details about the `ADIN2111 Linux Driver <https://wiki.analog.com/https/wiki.analog.com/resources/tools-software/linux-drivers/net-mac-phy/adin2111>`_.

.. |image1| image:: https://wiki.analog.com/_media/resources/quick-start/rpi3-adin2111.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/quick-start/rpi-3-adin2111-board-switches.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/quick-start/8mmini-adin2111-wiring.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/quick-start/rpi-3-adin2111-crc-enabled.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/quick-start/jetson-nano-adin2111-wiring.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/quick-start/jetson-nano-adin2111-board-switches.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/quick-start/jetson-nano-adin2111-wiring.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/quick-start/jetson-nano-adin2111-board-switches.jpg
   :width: 400px
