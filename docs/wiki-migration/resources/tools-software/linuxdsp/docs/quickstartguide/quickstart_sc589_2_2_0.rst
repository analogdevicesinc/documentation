Yocto Linux 2.2.0 Quickstart Guide for ADSP-SC589 (EZKIT & MINI)
================================================================

.. important::

   This version is under development


.. important::

   The following instructions are for the ADSP-SC589-EZKIT and ADSP-SC589-MINI development boards. For instructions for other processors and development boards please refer to :doc:`Linux for ADSP-SC5xx Processors 2.2.0 (develop) </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/2.2.0>`\


Setting Up Your Host PC
=======================

The build system is currently supported on host PCs running Ubuntu 20.04 LTS 64-bit.

| 
| ==== Installing Required Packages ==== In order to build and deploy Linux to your ADSP-SC589-EZKIT or ADSP-SC589-MINI development board you will need to install the following packages on your host PC.

::

   $ sudo apt-get update
   $ sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm u-boot-tools openssl curl tftpd-hpa python

| 
| ==== Installing CrossCore Embedded Studio ==== CrossCore Embedded Studio contains OpenOCD which is used to transfer U-Boot into RAM for the first initial boot of the device. The tools are created for 32-bit architecture and therefore requires a 32-bit libz package to run. Download and install it.

::

   $ wget http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.10.0/adi-CrossCoreEmbeddedStudio-linux-x86-2.10.0.deb
   $ sudo dpkg -i ./adi-CrossCoreEmbeddedStudio-linux-x86-2.10.0.deb
   $ sudo apt install lib32z1

| 
| ==== Configuring TFTP Service==== A TFTP server on the host is used to transfer images to the development board. Install and configure.

::

   $ sudo vi /etc/default/tftpd-hpa

   #Replace the existing file with the following
   TFTP_USERNAME="tftp"
   TFTP_DIRECTORY="/tftpboot"
   TFTP_ADDRESS="0.0.0.0:69"
   TFTP_OPTIONS="--secure"
   #End of File

   $ sudo mkdir /tftpboot
   $ sudo chmod 777 /tftpboot
   $ sudo service tftpd-hpa restart

| 
| ==== Configure Minicom ==== In order to communicate with the U-Boot bootloader, a UART connection must be made between the host PC and the development board. It is recommended that you use minicom to do this. Minicom must be configured to connect to U-Boot correctly.

On the host PC open a terminal and execute the following commands:

::

   $ sudo apt-get install -y minicom
   $ sudo minicom -s

               +-----[configuration]------+


               | Filenames and paths      |

               | File transfer protocols  |
               | Serial port setup        |
               | Modem and dialing        |
               | Screen and keyboard      |
               | Save setup as dfl        |
               | Save setup as..          |
               | Exit                     |
               | Exit from Minicom        |
               +--------------------------+


   # Select Serial port setup
        Set Serial Device to /dev/ttyUSB0
        Set Bps/Par/Bits to 115200 8N1
        Set Hardware Flow Control to No
        
        Close the Serial port setup option by press Esc
    Select Save setup as dfl
    Select Exit

.. note::

   \ ``/dev/ttyUSB0`` might not correspond to the serial port of the board on every system. You can determine which ``/dev`` entry your board uses by running ``ls -l /dev/ttyUSB*`` twice, once when the serial port of the board is plugged in, and once when it isn't.


| 
| ==== Installing the Sources ==== The example is fully contained in the Analog Devices Yocto Linux github repositories.

To install the sources: 

::

   $ mkdir ~/griffin
   $ cd ~/griffin
   $ mkdir bin
   $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ./bin/repo
   $ chmod a+x ./bin/repo
   $ ./bin/repo init \
      -u https://github.com/analogdevicesinc/lnxdsp-repo-manifest.git \
      -b develop/yocto-2.2.0 \
      -m develop-yocto-2.2.0.xml
   $ ./bin/repo sync

| 
| ===== Building the Image =====

Preparing the buildtool
-----------------------

Yocto requires the environment to be configured before building is possible.  A setup-environment script in the griffin folder contains all the required environment settings for your build target. Source the setup script for your board:

::

   $ source setup-environment -m adsp-sc589-ezkit

or

::

   $ source setup-environment -m adsp-sc589-mini

Sourcing the script will configure your build environment and create a build folder along with a local build configuration file.  See the Yocto Manual for further details.

.. important::

   Note that the build environment needs to be sourced once only before building.  If later working in a different terminal the setup-environment script should be sourced again.  If sourcing the setup-environment script is done without specifying the machine Yocto will reuse the previous configuration settings and retain any changes made to the files in the conf folder.


| 
| ==== Building the example ==== You can build three different versions of the root file system; minimal, ramdisk and full. To build the example images invoke bitbake from within the build directory created previously.

::

   $ bitbake adsp-sc5xx-minimal
   $ bitbake adsp-sc5xx-ramdisk
   $ bitbake adsp-sc5xx-full

When the build completes you will see a warning that the ELF binary has relocations in .text. It is OK to ignore this warning

.. note::

   Building a Linux distribution with Yocto is a significantly demanding process, both in CPU and network usage. A full build from scratch is estimated to take around 170 minutes for an 11th Gen Intel Core i5-11500T with 16 GB of RAM and a stable, fast Internet connection. This estimate can go up significantly for a poorer Internet connection or CPU resources, so set aside plenty of time for a clean build.


Copy the U-Boot binary files to the tftp directory:

::

   $ cp tmp/deploy/images/adsp-sc589-ezkit/init-sc589-ezkit.elf /tftpboot 
   $ cp tmp/deploy/images/adsp-sc589-ezkit/u-boot-sc589-ezkit /tftpboot 
   $ cp tmp/deploy/images/adsp-sc589-ezkit/u-boot-sc589-ezkit.ldr /tftpboot 

or

::

   $ cp tmp/deploy/images/adsp-sc589-mini/init-sc589-mini.elf /tftpboot 
   $ cp tmp/deploy/images/adsp-sc589-mini/u-boot-sc589-mini /tftpboot 
   $ cp tmp/deploy/images/adsp-sc589-mini/u-boot-sc589-mini.ldr /tftpboot 

| 
| ==== Running U-Boot on the Board for the first time====

.. note::

   It's always good practice to erase the contents of ``/tftpboot/`` before running and/or flashing a new build of U-Boot or Linux. You can do so by executing ``rm /tftpboot/*`` before proceeding


Before installing the software on to the development board, ensure that the following cables are connected:

-  Board connected to network via ethernet cable using J14 connector.
-  Board connected to host PC using USB micro cable, connected to USB/UART port on the development board
-  Board connected to the ICE 1000 or ICE 2000 via the DEBUG port on the board
-  ICE is also connected to host PC via USB mini cable

|image1| |image2|

-  **ADSP-SC589-EZKIT only:** The BOOT MODE selector on the board should be turned to "0".

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc589-ezkit_boot_selector.jpg
   :width: 400px

The console output from U-Boot and later on Linux will appear on the USB serial port configured in minicom earlier so open up minicom.

::

   ;''**Terminal1: minicom**''
   :<code>$ sudo minicom </code>

In a separate console launch OpenOCD and connect to the development board

::

   ;''**Terminal2: OpenOCD**''
   :<code>

$ cd /opt/analog/cces/2.10.0/ARM/openocd/share/openocd/scripts $ sudo /opt/analog/cces/2.10.0/ARM/openocd/bin/openocd -f interface/<ICE>.cfg -f board/adspsc589_ezbrd.cfg</code> Where <ICE> should be replaced with ice1000 or ice2000 depending on your hardware. When successful you should see a message similar to the console output below

::

       Open On-Chip Debugger (Analog Devices CCES 2.10.0 OpenOCD 0.9.0-ga8d0a22) 0.9.0 
       Licensed under GNU GPL v2 
       Report bugs to <processor.tools.support@analog.com>
       adapter speed: 1000 kHz 
       Info : transports supported by the debug adapter: "jtag", "swd"
       Info : auto-select transport "jtag"
       halt and restart using CTI
       trst_only separate trst_push_pull
       Info : ICE-1000 firmware version is 1.0.2
       Info : clock speed 1000 kHz
       Info : JTAG tap: adspsc58x.adjc tap/device found: 0x228080cb (mfg: 0x065, part: 0x2808, ver: 0x2)
       Info : JTAG tap: adspsc58x.dap enabled
       Info : adspsc58x.dap: hardware has 3 breakpoints, 2 watchpoints
       Info : adspsc58x.dap: but you can only set 1 watchpoint

In a third console window launch GDB and type ``target extended-remote :3333``. This will make GDB to connect to the gdbserver on the local host using port 3333. Then, load the init file into RAM by typing ``load init-sc589-ezkit.elf`` or ``load init-sc589-mini.elf`` and run it by typing ``c``. Hit Ctrl+C to interrupt thereafter.

::

   ;''**Terminal3: GDB (sc589-ezkit)**''
   : <code>

$ cd /tftpboot $ /opt/analog/cces/2.10.0/ARM/arm-none-eabi/bin/arm-none-eabi-gdb u-boot-sc589-ezkit ... (gdb) target extended-remote :3333 Remote debugging using :3333 0x00004884 in ?? () (gdb) load init-sc589-ezkit.elf Loading section .text, size 0xa70 lma 0x20080000 Start address 0x20080028, load size 2672 Transfer rate: 25 KB/sec, 2672 bytes/write. (gdb) c Continuing. ^C Program received signal SIGINT, Interrupt. 0x20080024 in ?? () </code>

::

   ;''**Terminal3: GDB (sc589-mini)**''
   : <code>

$ cd /tftpboot $ /opt/analog/cces/2.10.0/ARM/arm-none-eabi/bin/arm-none-eabi-gdb u-boot-sc589-ezkit ... (gdb) target remote :3333 Remote debugging using :3333 0x00004884 in ?? () (gdb) load init-sc589-mini.elf Loading section .text, size 0xa70 lma 0x20080000 Start address 0x20080028, load size 2672 Transfer rate: 25 KB/sec, 2672 bytes/write. (gdb) c Continuing. ^C Program received signal SIGINT, Interrupt. 0x20080024 in ?? () </code>

Now, load U-Boot into RAM.

::

   ;''**Terminal3: GDB (sc589-ezkit)**''
   :

::

   (gdb) load
   Loading section .text, size 0x3a8 lma 0x89200000
   Loading section .efi_runtime, size 0xe30 lma 0x892003a8
   Loading section .text_rest, size 0x4dd10 lma 0x892011e0
   Loading section .rodata, size 0xfbe0 lma 0x8924eef0
   Loading section .hash, size 0x18 lma 0x8925ead0
   Loading section .dtb.init.rodata, size 0x360 lma 0x8925eaf0
   Loading section .data, size 0x3468 lma 0x8925ee50
   Loading section .got.plt, size 0xc lma 0x892622b8
   Loading section .u_boot_list, size 0xe80 lma 0x892622c4
   Loading section .efi_runtime_rel, size 0xd0 lma 0x89263144
   Loading section .rel.dyn, size 0xb180 lma 0x89263214
   Loading section .dynsym, size 0x30 lma 0x8926e394
   Loading section .dynstr, size 0x1 lma 0x8926e3c4
   Loading section .dynamic, size 0x90 lma 0x8926e3c8
   Loading section .gnu.hash, size 0x18 lma 0x8926e458
   Start address 0x89200000, load size 451677
   Transfer rate: 31 KB/sec, 11581 bytes/write.
   (gdb) c
   Continuing.

::

   ;''**Terminal3: GDB (sc589-mini)**''
   :

::

   (gdb) load
   Loading section .text, size 0x3a8 lma 0xc2200000
   Loading section .efi_runtime, size 0xe30 lma 0xc22003a8
   Loading section .text_rest, size 0x4f4a0 lma 0xc22011e0
   Loading section .rodata, size 0xff43 lma 0xc2250680
   Loading section .hash, size 0x18 lma 0xc22605c4
   Loading section .dtb.init.rodata, size 0x360 lma 0xc22605e0
   Loading section .data, size 0x3390 lma 0xc2260940
   Loading section .got.plt, size 0xc lma 0xc2263cd0
   Loading section .u_boot_list, size 0xe80 lma 0xc2263cdc
   Loading section .efi_runtime_rel, size 0xd0 lma 0xc2264b5c
   Loading section .rel.dyn, size 0xb218 lma 0xc2264c2c
   Loading section .dynsym, size 0x30 lma 0xc226fe44
   Loading section .dynstr, size 0x1 lma 0xc226fe74
   Loading section .dynamic, size 0x90 lma 0xc226fe78
   Loading section .gnu.hash, size 0x18 lma 0xc226ff08
   Start address 0xc2200000, load size 458512
   Transfer rate: 30 KB/sec, 11462 bytes/write.
   (gdb) c
   Continuing.

At this point U-Boot will now be running in RAM on your target board. You should see U-Boot booting in the minicom console (Terminal 1). Press a key to interrupt the boot process before the countdown terminates:

::

   ;''**Terminal1: minicom (sc589-ezkit)**''
   :  <code>

U-Boot 2020.10 (Aug 23 2022 - 13:09:23 +0000)

CPU: ADSP ADSP-SC589-0.1 (Detected Rev: 1.1) (spi flash boot) VCO: 450 MHz, Cclk0: 450 MHz, Sclk0: 112.500 MHz, Sclk1: 112.500 MHz, DCLK: 450 MHz OCLK: 150 MHz Model: ADI sc589-ezkit I2C: ready DRAM: 224 MiB MMC: SC5XX SDH: 0 Loading Environment from SPIFlash... SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB \**\* Warning - bad CRC, using default environment

In: serial@0x31003000 Out: serial@0x31003000 Err: serial@0x31003000 SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB other init Net: dwmac.3100c000 Hit any key to stop autoboot: 0 => </code>

::

   ;''**Terminal1: minicom (sc589-mini)**''
   :  <code>

U-Boot 2020.10 (Aug 23 2022 - 13:09:23 +0000)

CPU: ADSP ADSP-SC589-0.1 (Detected Rev: 1.1) (spi flash boot) VCO: 450 MHz, Cclk0: 450 MHz, Sclk0: 112.500 MHz, Sclk1: 112.500 MHz, DCLK: 450 MHz OCLK: 150 MHz Model: ADI sc589-mini I2C: ready DRAM: 224 MiB MMC: SC5XX SDH: 0 Loading Environment from SPIFlash... SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB \**\* Warning - bad CRC, using default environment

In: serial@0x31003000 Out: serial@0x31003000 Err: serial@0x31003000 other init Net: dwmac.3100c000 Hit any key to stop autoboot: 0 => </code>

| 
| == Flash U-Boot to SPI Flash ==
| In the U-Boot console, set the IP address of the Host Linux PC that hosts the U-Boot loader file (``u-boot-sc573-ezkit.ldr``) on TFTP.

::

   ;''**Terminal1: minicom**''
   :  

::

   => setenv serverip <SERVERIP>

.. note::

   To find the IP address of your host Linux PC you can issue the ``ip addr`` command from the shell or console.


If your network **supports** DHCP, run:

::

   => dhcp

If your network **does NOT support** DHCP, run:

::

   => set ipaddr <ADDR>

Where ``<ADDR>`` is the IP address you want to assign.

.. note::

   If flashing a board that had been previously programmed, it's good to erase the whole flash before as sometimes previous U-Boot installations might leave remnants. You can do that by typing ``=> sf probe 2:1; sf erase 0 ${sfsize}`` on the U-Boot prompt before proceeding to the following instructions


Next, run the U-Boot update command to copy the U-Boot loader file from the host PC to the target board, and write it into flash:

::

   => run update

You will see an output similar to the one below:

::

   => run update
   Speed: 1000, full duplex
   Using dwmac.3100c000 device
   TFTP from server 192.168.1.223; our IP address is 192.168.1.218
   Filename 'u-boot-sc589-ezkit.ldr'.
   Load address: 0xc2000000
   Loading: ################################
            3.8 MiB/s
   done
   Bytes transferred = 459144 (70188 hex)
   SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
   SF: 524288 bytes @ 0x0 Erased: OK
   device 0 offset 0x0, size 0x70188
   SF: 459144 bytes @ 0x0 Written: OK
   =>

   | At this point the U-Boot binary is stored in flash. You can now disconnect the ICE-1000 or ICE-2000 from the development board and make sure to switch the BMODE to position 1. You will only need to reconnect this if your board fails to boot and you need to re-follow these instructions.

Booting Linux
=============

Booting Linux Using SD Card
---------------------------

Formatting the SD Card
~~~~~~~~~~~~~~~~~~~~~~

In order to use an SD Card with Linux we need to prepare it by formatting it in the correct format. This section of instructions requires you to correctly identify the SD Card and format the card. If you select the wrong drive you may cause irreversible damage to you Host PC. To format the SD Card, follow the commands below. The example code in this section assumes that the SD Card device is reported to be /dev/sdb. Ensure that you change these commands to use your device.

::

   $ sudo fdisk /dev/sdb
   /* Create primary partition 1, 256M size*/
   Command (m for help): n
   Select (default p): p
   Partition number (1-4, default 1): 1
   First sector (2048-3887103, default 2048): PRESS ENTER
   Last sector, +sectors or +size{K,M,G} (2048-3887103, default 3887103): PRESS ENTER

   /* Save partition */
   Command (m for help): w

Format the SD card to EXT filesystem

::

   $ sudo mkfs.ext2 /dev/sdb1

|

| === Writing the kernel and file system to the SD Card === Next, we need to copy the Linux file system and kernel image to the SD Card. We install this on to the SD Card by mounting the file system on to the local Host PC and copying the contents on to the SD Card. To allow the choice of booting using ramboot and sdcard boot we copy the ramboot image to the SD card as well as extract the minimal image to the SD card.

::

   $ mkdir ~/mnt
   $ sudo mount -t ext2 /dev/sdb1 ~/mnt
   $ sudo mkdir ~/mnt/boot
   $ sudo cp tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-ramdisk-adsp-sc589-ezkit.cpio.xz.u-boot ~/mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp tmp/deploy/images/adsp-sc589-ezkit/sc589-ezkit.dtb ~/mnt/boot/
   $ sudo cp tmp/deploy/images/adsp-sc589-ezkit/fitImage ~/mnt/boot/
   $ sudo tar -xf tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-minimal-adsp-sc589-ezkit.tar.xz -C ~/mnt
   $ sudo umount ~/mnt

or

::

   $ mkdir ~/mnt
   $ sudo mount -t ext2 /dev/sdb1 ~/mnt
   $ sudo mkdir ~/mnt/boot
   $ sudo cp tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-ramdisk-adsp-sc589-mini.cpio.xz.u-boot ~/mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp tmp/deploy/images/adsp-sc589-mini/sc589-mini.dtb ~/mnt/boot/
   $ sudo cp tmp/deploy/images/adsp-sc589-mini/fitImage ~/mnt/boot/
   $ sudo tar -xf tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-minimal-adsp-sc589-mini.tar.xz -C ~/mnt
   $ sudo umount ~/mnt

The file system and kernel image are now installed on to the SD Card. The SD Card can now be safely removed from the Host PC.

| 
| === Booting Linux from the SD card === Insert the SD card to target board, and reset the board and enter into U-Boot

::

   => run sdcardboot
   or 
   => run ramboot_emmc

The linux kernel will then boot up using the file system stored in SD card.


| 

Booting Linux from the USB Mass Storage
---------------------------------------

Formating USB stick
~~~~~~~~~~~~~~~~~~~

Frist step is to format USB stick to U-Boot supported formats.

To format the USB stick, follow the commands below. The example code in this section assumes that the USB device is reported to be /dev/sdb. Ensure that you change these commands to use your device.

::

   $ sudo fdisk /dev/sdb
   /* Create primary partition 1, 256M size*/
   Command (m for help): n
   Select (default p): p
   Partition number (1-4, default 1): 1
   First sector (2048-3887103, default 2048): PRESS ENTER
   Last sector, +sectors or +size{K,M,G} (2048-3887103, default 3887103): PRESS ENTER

   /* Save partition */
   Command (m for help): w

Format the USB stick to EXT4 filesystem

::

   $ sudo mkfs.ext4 /dev/sdb1

Writing kernel and rootfs image to USB stick
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   $ mkdir ~/mnt
   $ sudo mount -t ext4 /dev/sdb1 ~/mnt
   $ sudo mkdir ~/mnt/boot
   $ sudo cp tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-ramdisk-adsp-sc589-ezkit.cpio.xz.u-boot ~/mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp tmp/deploy/images/adsp-sc589-ezkit/fitImage ~/mnt/boot/
   $ sudo umount ~/mnt

or for SC598-mini

::

   $ mkdir ~/mnt
   $ sudo mount -t ext4 /dev/sdb1 ~/mnt
   $ sudo mkdir ~/mnt/boot
   $ sudo cp tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-ramdisk-adsp-sc589-mini.cpio.xz.u-boot ~/mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp tmp/deploy/images/adsp-sc589-mini/fitImage ~/mnt/boot/
   $ sudo umount ~/mnt

Booting Linux from USB Mass Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To boot from ADSP-SC589-EZKIT run this commands in u-boot

::

   setenv usbload 'ext4load usb 0 ${initramaddr} /boot/${initramfile}; ext4load usb 0 ${loadaddr} /boot/${imagefile};'
   setenv usbboot 'usb start; run usbload; run ramargs; bootm ${loadaddr} ${initramaddr};'
   run usbboot

To boot from ADSP-SC589-MINI there is need to disable emac0 device in u-boot device tree, as USB and ethernet port share same pin and can't run simultaneously. Inside Yocto directory type

::

   devtool modify u-boot-adi

edit build/workspace/sources/u-boot-adi/arch/arm/dts/sc589-mini.dts by adding

::

   &emac0 {
       status="disable";
   };

To rebuild U-boot after modifications

::

   devtool build u-boot-adi

Booting rootfs from USB Mass Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the step how to setup USB stick in chapter above. Set environment variables in U-boot

::

   setenv usbargs 'setenv bootargs root=/dev/sda1 rw rootfstype=ext4 rootwait earlycon=adi_uart,0x31003000 console=ttySC0,115200'
   setenv usbload 'ext4load usb 0 ${loadaddr} /boot/${imagefile};'
   setenv usbboot 'usb start; run usbload; run usbargs; bootm ${loadaddr};'

And type to boot

::

   run usbboot

Now the rootfs is set to your USB stick and amount of space equals of size of partition on USB stick.

|

| ==== Booting Linux Using TFTP ==== In order to boot Linux, the TFTP server should be setup as :doc:`above </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc589>` and (for both NFS and RAM boot) a copy of the kernel image should be copied into the **/tftpboot** directory.

::

   $ cp tmp/deploy/images/adsp-sc589-ezkit/fitImage /tftpboot

or

::

   $ cp tmp/deploy/images/adsp-sc589-mini/fitImage /tftpboot

| 
| === RAM Boot === For RAM boot we need to copy the image containing filesystem to the /tftpboot directory.

::

   $ cp tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-ramdisk-adsp-sc589-ezkit.cpio.xz.u-boot /tftpboot/ramdisk.cpio.xz.u-boot

or

::

   $ cp tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-ramdisk-adsp-sc589-mini.cpio.xz.u-boot /tftpboot/ramdisk.cpio.xz.u-boot

| 
| === NFS Boot === For NFS boot we use the Network File System which is stored in local Ubuntu Host. This is suggested when you do application development. To setup the NFS server:

::

   $ sudo apt-get install nfs-kernel-server
   $ sudo vi /etc/exports

   #Add following commands
   /romfs *(rw,sync,no_root_squash,no_subtree_check)

   $ sudo mkdir /romfs/
   $ sudo chmod 777 /romfs/
   $ sudo service nfs-kernel-server start

We can verify that the NFS service is running by executing

::

   $ sudo service nfs-kernel-server status

The output will indicate that the server is active, i.e.

::

   ● nfs-server.service - NFS server and services
        Loaded: loaded (/lib/systemd/system/nfs-server.service; enabled; vendor preset: enabled)
       Drop-In: /run/systemd/generator/nfs-server.service.d
                └─order-with-mounts.conf
        Active: active (exited) since Tue 2022-09-06 14:38:31 BST; 3 months 14 days ago
      Main PID: 953 (code=exited, status=0/SUCCESS)
         Tasks: 0 (limit: 18797)
        Memory: 0B
        CGroup: /system.slice/nfs-server.service

   Sep 06 14:38:29 $YOUR_HOSTNAME systemd[1]: Starting NFS server and services...
   Sep 06 14:38:31 $YOUR_HOSTNAME systemd[1]: Finished NFS server and services.

If it's reported as inactive, wait a few moments and check the status again.

| The root filesystem should then be copied to /romfs.
| If you are using the ADSP-SC589-EZKIT with the full image (you ran 'bitbake adsp-sc5xx-full'):

::

   $ sudo tar -xf tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-full-adsp-sc589-ezkit.tar.xz -C /romfs

Or if you are using the ADSP-SC589-EZKIT with the minimal image (you ran 'bitbake adsp-sc5xx-minimal'):

::

   $ sudo tar -xf tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-minimal-adsp-sc589-ezkit.tar.xz -C /romfs

Or if you are using the ADSP-SC589-MINI with the full image (you ran 'bitbake adsp-sc5xx-full'):

::

   $ sudo tar -xf tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-full-adsp-sc589-mini.tar.xz -C /romfs

Or if you are using the ADSP-SC589-MINI with the minimal image (you ran 'bitbake adsp-sc5xx-minimal'):

::

   $ sudo tar -xf tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-minimal-adsp-sc589-mini.tar.xz -C /romfs

| 
| === Booting into Linux from TFTP === Next, on the target, from u-boot, run one of the following command:

::

   => run ramboot
    or
   => run nfsboot
   ......
   ......
            Starting Update UTMP about System Runlevel Changes...
   [  OK  ] Started Update UTMP about System Runlevel Changes.


        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@            @@@@@@@@@@@@@@@@@@@
        @@@@@@@@               @@@@@@@@@@@@@@@@
        @@@@@@@@                   @@@@@@@@@@@@
        @@@@@@@@                     @@@@@@@@@@
        @@@@@@@@                        @@@@@@@
        @@@@@@@@                     @@@@@@@@@@
        @@@@@@@@                   @@@@@@@@@@@@
        @@@@@@@@               @@@@@@@@@@@@@@@@
        @@@@@@@@            @@@@@@@@@@@@@@@@@@@
        @@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

           Analog Devices Yocto Distribution
                    www.analog.com
                 www.yoctoproject.org

   adsp-sc589-ezkit login: root
   Password: adi
   root@adsp-sc589-ezkit:~#

The default username is **root** and the password is **adi**.

| 
| ==== Building the SDK ==== To build the SDK follow the instructions here :doc:`Building the SDK </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/building-the-sdk>`.

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc589-ezkit_overview.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc589-mini_overview.jpg
   :width: 400px
