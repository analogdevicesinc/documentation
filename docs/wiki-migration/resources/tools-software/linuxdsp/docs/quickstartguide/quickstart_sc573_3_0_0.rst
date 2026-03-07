Yocto Linux 3.0.0 Quickstart Guide for ADSP-SC573-EZKIT)
========================================================

.. important::

   The following instructions are for the ADSP-SC573-EZKIT development board. For instructions for other processors and development boards please refer to :doc:`Linux for ADSP-SC5xx Processors 3.0.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>`\


Setting Up Your Host PC
-----------------------

The build system is currently supported on host PCs running Ubuntu 20.04 LTS 64-bit.

| 
| ==== Installing Required Packages ==== In order to build and deploy Linux to your ADSP-SC573-EZKIT development board you will need to install the following packages on your host PC.

.. code:: bash

   $ sudo apt-get update
   $ sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm u-boot-tools openssl curl tftpd-hpa python3 zstd liblz4-tool

Configuring TFTP Service
~~~~~~~~~~~~~~~~~~~~~~~~

A TFTP server on the host is used to transfer images to the development board. Install and configure.

.. code:: bash

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

.. code:: bash

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

.. code:: bash

   $ mkdir ~/griffin
   $ cd ~/griffin
   $ mkdir bin
   $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ./bin/repo
   $ chmod a+x ./bin/repo
   $ ./bin/repo init \
      -u https://github.com/analogdevicesinc/lnxdsp-repo-manifest.git \
      -b release/yocto-3.0.0 \
      -m release-yocto-3.0.0.xml
   $ ./bin/repo sync

| 
| ===== Building the Image =====

Preparing the buildtool
~~~~~~~~~~~~~~~~~~~~~~~

Yocto requires the environment to be configured before building is possible.  A setup-environment script in the griffin folder contains all the required environment settings for your build target. Source the setup script for your board:

.. code:: bash

   $ source setup-environment -m adsp-sc573-ezkit

Sourcing the script will configure your build environment and create a build folder along with a local build configuration file.  See the Yocto Manual for further details.

.. important::

   Note that the build environment needs to be sourced once only before building.  If later working in a different terminal the setup-environment script should be sourced again.  If sourcing the setup-environment script is done without specifying the machine Yocto will reuse the previous configuration settings and retain any changes made to the files in the conf folder.


| 
| ==== Building the example ==== You can build three different versions of the root filesystem; tiny, minimal and full. To build the example images invoke bitbake from within the build directory created previously.

.. code:: bash

   $ bitbake adsp-sc5xx-tiny
   $ bitbake adsp-sc5xx-minimal
   $ bitbake adsp-sc5xx-full

When the build completes you will see a warning that the ELF binary has relocations in .text. It is OK to ignore this warning

.. note::

   Building a Linux distribution with Yocto is a significantly demanding process, both in CPU and network usage. A full build from scratch is estimated to take around 170 minutes for an 11th Gen Intel Core i5-11500T with 16 GB of RAM and a stable, fast Internet connection. This estimate can go up significantly for a poorer Internet connection or CPU resources, so set aside plenty of time for a clean build.


Building the SDK
~~~~~~~~~~~~~~~~

The SDK will provide you with the cross toolchain needed to develop application for the target board, alongside various miscellaneous tools. Notably, it will provide you with OpenOCD and GDB, which you can use to run and flash U-Boot on the board.

The SDK can be built for the ``adsp-sc5xx-minimal`` image or the ``adsp-sc5xx-full image``. To build the SDK for the adsp-sc5xx-minimal image invoke bitbake from within the build directory created previously.

.. code:: bash

   $ bitbake adsp-sc5xx-minimal -c populate_sdk

or for the adsp-sc5xx-full image

.. code:: bash

   $ bitbake adsp-sc5xx-full -c populate_sdk

When the build has completed you will find a set of files in the <BUILD_DIR>/tmp/deploy/sdk directory. For example, the minimal image on SC573:

.. code:: bash

   $ ls tmp/deploy/sdk
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc573-ezkit-toolchain-3.0.0.host.manifest
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc573-ezkit-toolchain-3.0.0.sh
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc573-ezkit-toolchain-3.0.0.target.manifest
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc573-ezkit-toolchain-3.0.0.testdata.json

The ``adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc573-ezkit-toolchain-3.0.0.sh`` is a self-extracting archive containing the SDK.

Installing the SDK
^^^^^^^^^^^^^^^^^^

Invoke the self-extracting archive. It will default to installing to ``/opt/adi-distro/3.0.0`` but gives you the option to select your own install folder during the installation. For the minimal image on SC573

.. code:: bash

   $ ./adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc573-ezkit-toolchain-3.0.0.sh
   Analog Devices Inc Reference Distro (glibc) SDK installer version 3.0.0
   =======================================================================
   Enter target directory for SDK (default: /opt/adi-distro-glibc/3.0.0):
   You are about to install the SDK to "/opt/adi-distro-glibc/3.0.0". Proceed [Y/n]? y
   Extracting SDK................................................................................................................done
   Setting it up...done
   SDK has been successfully set up and is ready to be used.
   Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
    $ . /opt/adi-distro-glibc/3.0.0/environment-setup-cortexa5t2hf-neon-adi_glibc-linux-gnueabi

Your SDK is now installed.

Running U-Boot on the Board for the first time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   It's always good practice to erase the contents of ``/tftpboot/`` before running and/or flashing a new build of U-Boot or Linux. You can do so by executing ``rm /tftpboot/*`` before proceeding


Copy the U-Boot binary & loader files to the tftp directory:

.. code:: bash

   $ cp tmp/deploy/images/adsp-sc573-ezkit/u-boot-spl-sc573-ezkit.elf /tftpboot/ 
   $ cp tmp/deploy/images/adsp-sc573-ezkit/u-boot-proper-sc573-ezkit.elf /tftpboot/ 
   $ cp tmp/deploy/images/adsp-sc573-ezkit/stage1-boot.ldr /tftpboot/ 
   $ cp tmp/deploy/images/adsp-sc573-ezkit/stage2-boot.ldr /tftpboot/ 

Before installing the software on to the development board, ensure that the following cables are connected:

-  Board connected to network via ethernet cable using J13 connector.
-  Board connected to host PC using USB micro cable, connected to USB/UART port on the development board
-  Board connected to the ICE 1000 or ICE 2000 via the DEBUG port on the board
-  ICE is also connected to host PC via USB mini cable

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc573-ezkit_overview.jpg
   :width: 400px

-  The BOOT MODE selector on the EV-SC573-SOM board should be turned to "0".

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc573-ezkit_boot_selector.jpg
   :width: 400px

The console output from U-Boot and later on Linux will appear on the USB serial port configured in minicom earlier so open up minicom.

::

   ;''**Terminal1: minicom**''
   :<code bash>$ sudo minicom </code>

In a separate console launch OpenOCD and connect to the development board.

::

   ;''**Terminal2: OpenOCD**''
   :<code bash>

$ sdk_usr=/opt/adi-distro-glibc/3.0.0/sysroots/x86_64-adi_glibc_sdk-linux/usr/ $ $sdk_usr/bin/openocd -f $sdk_usr/share/openocd/scripts/interface/<ICE>.cfg -f $sdk_usr/share/openocd/scripts/target/adspsc57x.cfg </code> Where ``<ICE>`` should be replaced with ``ice1000`` or ``ice2000`` depending on your hardware. When successful you should see a message similar to the console output below

.. code:: bash

   Open On-Chip Debugger (PKGVERSION)  OpenOCD 0.10.0-g40378454d (2023-04-05-10:35)
   Licensed under GNU GPL v2
   Report bugs to <processor.tools.support@analog.com>
   adapter speed: 1000 kHz
   Info : transports supported by the debug adapter: "jtag", "swd"
   Info : auto-select transport "jtag"
   halt and restart using CTI
   trst_only separate trst_push_pull
   adspsc58x_init
   Info : ICE-1000 firmware version is 1.0.2
   Info : clock speed 1000 kHz
   Info : JTAG tap: adspsc573.adjc tap/device found: 0x428080cb (mfg: 0x065, part: 0x2808, ver: 0x4)
   Info : JTAG tap: adspsc573.dap enabled
   Info : adspsc573.dap: hardware has 3 breakpoints, 2 watchpoints
   Info : adspsc573.dap: but you can only set 1 watchpoint
   Info : accepting 'gdb' connection on tcp/3333
   Info : JTAG tap: adspsc573.adjc tap/device found: 0x428080cb (mfg: 0x065, part: 0x2808, ver: 0x4)
   Info : JTAG tap: adspsc573.dap enabled
   Info : adspsc573.dap: hardware has 3 breakpoints, 2 watchpoints
   Info : adspsc573.dap: but you can only set 1 watchpoint

In a third console window launch GDB and type ``target extended-remote :3333``. This will make GDB to connect to the gdbserver on the local host using port 3333. Then, load the U-Boot SPL into RAM by typing ``load``. Hit Ctrl+C to interrupt thereafter.

::

   ;''**Terminal3: GDB**''
   : <code bash>

$ cd /tftpboot $ /opt/adi-distro-glibc/3.0.0/sysroots/x86_64-adi_glibc_sdk-linux/usr/bin/arm-adi_glibc-linux-gnueabi/arm-adi_glibc-linux-gnueabi-gdb u-boot-spl-sc573-ezkit.elf ... (gdb) target extended-remote :3333 Remote debugging using :3333 0x00004884 in ?? () (gdb) load Loading section .text, size 0x9c0c lma 0x20080000 Loading section .rodata, size 0x1198 lma 0x20089c0c Loading section .dtb.init.rodata, size 0x1460 lma 0x2008adb0 Loading section .data, size 0x514 lma 0x2008c210 Loading section .u_boot_list, size 0xa50 lma 0x2008c724 Start address 0x20080000, load size 53608 Transfer rate: 29 KB/sec, 7658 bytes/write. (gdb) c Continuing. ^C Program received signal SIGINT, Interrupt. </code>

You will see a message on Terminal 1 running minicom, informing you that you can now load U-Boot Proper

::

   ;''**Terminal1: minicom**''
   :<code bash>U-Boot SPL 2020.10 (Mar 16 2023 - 13:07:24 +0000)

ADI Boot Mode: 0x0 (JTAG/BOOTROM) SPL execution has completed. Please load U-Boot Proper via JTAG </code>

Now, load U-Boot Proper into RAM.

::

   ;''**Terminal3: GDB**''
   :

.. code:: bash

   (gdb) load u-boot-proper-sc573-ezkit.elf
   Loading section .text, size 0x3a8 lma 0x89200000
   Loading section .text_rest, size 0x46084 lma 0x892003c0
   Loading section .rodata, size 0xf56c lma 0x89246444
   Loading section .hash, size 0x18 lma 0x892559b0
   Loading section .dtb.init.rodata, size 0x19d0 lma 0x892559d0
   Loading section .data, size 0x22d8 lma 0x892573a0
   Loading section .got.plt, size 0xc lma 0x89259678
   Loading section .u_boot_list, size 0x1644 lma 0x89259684
   Loading section .rel.dyn, size 0x9c98 lma 0x8925acc8
   Loading section .dynsym, size 0x30 lma 0x89264960
   Loading section .dynstr, size 0x1 lma 0x89264990
   Loading section .dynamic, size 0x90 lma 0x89264994
   Loading section .gnu.hash, size 0x18 lma 0x89264a24
   Start address 0x89200000, load size 412185
   Transfer rate: 30 KB/sec, 11776 bytes/write.
   (gdb) c
   Continuing.

At this point U-Boot will now be running in RAM on your target board. You should see U-Boot booting in the minicom console (Terminal 1). Press a key to interrupt the boot process before the countdown terminates:

::

   ;''**Terminal1: minicom**''
   :  <code bash>

U-Boot 2020.10 (Mar 16 2023 - 13:07:24 +0000)

CPU: ADSP ADSP-SC573-0.1 (spi flash boot) Detected Revision: 1.1 Model: ADI sc573-ezkit DRAM: 112 MiB WDT: Not found! MMC: Loading Environment from SPIFlash... SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB \**\* Warning - bad CRC, using default environment

In: serial@0x31003000 Out: serial@0x31003000 Err: serial@0x31003000 Net: eth0: eth0 Hit any key to stop autoboot: 0 => </code>

| 
| == Flash U-Boot to SPI Flash ==
| In the U-Boot console, set the IP address of the Linux PC that hosts the U-Boot loader files (``stage1-boot.ldr`` & ``stage2-boot.ldr``) on TFTP.

::

   ;''**Terminal1: minicom**''
   :  

.. code:: bash

   => setenv serverip <SERVERIP>
   => setenv tftpserverip <SERVERIP>

.. note::

   To find the IP address of your host Linux PC you can issue the ``ip addr`` command from the shell or console.


If your network **supports** DHCP, run:

.. code:: bash

   => dhcp

If your network **does NOT support** DHCP, run:

.. code:: bash

   => set ipaddr <ADDR>

Where ``<ADDR>`` is the IP address you want to assign.

.. note::

   If flashing a board that had been previously programmed, it's good to erase the whole flash before as sometimes previous U-Boot installations might leave remnants. You can do that by typing ``=> sf probe ${sfdev}; sf erase 0 0x1000000`` on the U-Boot prompt before proceeding to the following instructions


Next, run the U-Boot update command to copy the U-Boot loader files from the host PC to the target board, and write it into flash:

.. code:: bash

   => run update_spi_uboot_only

You will see an output similar to the one below:

.. code:: bash

   => run update_spi_uboot_only
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'stage1-boot.ldr'.
   Load address: 0x89000000
   Loading: ####
            2.2 MiB/s
   done
   Bytes transferred = 53684 (d1b4 hex)
   SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
   device 0 offset 0x0, size 0xd1b4
   SF: 53684 bytes @ 0x0 Written: OK
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'stage2-boot.ldr'.
   Load address: 0x89000000
   Loading: #############################
            2 MiB/s
   done
   Bytes transferred = 412460 (64b2c hex)
   SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
   device 0 offset 0x20000, size 0x64b2c
   SF: 412460 bytes @ 0x20000 Written: OK

In order to store the ``serverip`` and the DHCP or otherwise assigned IP address of the board and have them available on next boot, you can run the following command:

.. code:: bash

   => saveenv
   Saving Environment to SPIFlash... Erasing SPI flash...Writing to SPI flash...done
   OK

At this point the U-Boot binary is stored in flash. You can now disconnect the ICE-1000 or ICE-2000 from the development board and make sure to switch the BMODE to position 1. You will only need to reconnect this if your board fails to boot and you need to re-follow these instructions.

| 
| ====== Booting Linux ======

Booting Linux from SPI Flash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADSP-SC573-EZKIT comes equipped with 16 MiB of SPI Flash. There's the option of building the ``adsp-sc5xx-tiny`` image, after changing the Libc implementation from the default GNU to musl, to further reduce the image's size. Follow the guide in :doc:`Boot from SPI Flash on the SC58x & SC573 </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/boot-flash-sc58x-573>`

</code>

| 
| ==== Booting Linux Using TFTP ==== In order to boot Linux, the TFTP server should be setup as :doc:`above </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc589>` and a copy of the kernel image should be copied into the **/tftpboot** directory.

.. code:: bash

   $ cp tmp/deploy/images/adsp-sc573-ezkit/fitImage /tftpboot

| 
| === NFS Boot === For NFS boot we use the Network File System which is stored in local Ubuntu Host. This is suggested when you do application development. To setup the NFS server:

.. code:: bash

   $ sudo apt-get install nfs-kernel-server
   $ sudo vi /etc/exports

   #Add following commands
   /romfs *(rw,sync,no_root_squash,no_subtree_check)

   $ sudo mkdir /romfs/
   $ sudo chmod 777 /romfs/
   $ sudo service nfs-kernel-server start

We can verify that the NFS service is running by executing

.. code:: bash

   $ sudo service nfs-kernel-server status

The output will indicate that the server is active, i.e.

.. code:: bash

   ● nfs-server.service - NFS server and services
        Loaded: loaded (/lib/systemd/system/nfs-server.service; enabled; vendor preset: enabled)
       Drop-In: /run/systemd/generator/nfs-server.service.d
                └─order-with-mounts.conf
        Active: active (exited) since Tue 2022-09-06 14:38:31 BST; 3 months 14 days ago
      Main PID: 953 (code=exited, status=0/SUCCESS)
         Tasks: 0 (limit: 18797)gxp2
        Memory: 0B
        CGroup: /system.slice/nfs-server.service

   Sep 06 14:38:29 $YOUR_HOSTNAME systemd[1]: Starting NFS server and services...
   Sep 06 14:38:31 $YOUR_HOSTNAME systemd[1]: Finished NFS server and services.

If it's reported as inactive, wait a few moments and check the status again.

| The root filesystem should then be copied to /romfs.
| If you are using the ADSP-SC573-EZKIT with the full image (you ran 'bitbake adsp-sc5xx-full'):

.. code:: bash

   $ sudo tar -xf tmp/deploy/images/adsp-sc573-ezkit/adsp-sc5xx-full-adsp-sc573-ezkit.tar.xz -C /romfs

Or if you are using the ADSP-SC573-EZKIT with the minimal image (you ran 'bitbake adsp-sc5xx-minimal'):

.. code:: bash

   $ sudo tar -xf tmp/deploy/images/adsp-sc573-ezkit/adsp-sc5xx-minimal-adsp-sc573-ezkit.tar.xz -C /romfs

| 
| === Booting into Linux from TFTP === Next, on the target, from u-boot, run the following command:

.. code:: bash

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

   adsp-sc573-ezkit login: root
   Password: adi
   root@adsp-sc573-ezkit:~#

The default username is **root** and the password is **adi**.

Booting Linux Using SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Formatting the SD Card
^^^^^^^^^^^^^^^^^^^^^^

In order to use an SD Card with Linux we need to prepare it by formatting it in the correct format. This section of instructions requires you to correctly identify the SD Card and format the card. If you select the wrong drive you may cause irreversible damage to you Host PC. To format the SD Card, follow the commands below. The example code in this section assumes that the SD Card device is reported to be /dev/sdb. Ensure that you change these commands to use your device.

.. code:: bash

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

.. code:: bash

   $ sudo mkfs.ext2 /dev/sdb1

| 
| === Writing the kernel and file system to the SD Card === Next, we need to copy the Linux file system and kernel image to the SD Card. We install this on to the SD Card by mounting the file system on to the local Host PC and copying the contents on to the SD Card. To allow the choice of booting using ramboot and sdcard boot we copy the ramboot image to the SD card as well as extract the minimal image to the SD card.

.. code:: bash

   $ mkdir ~/mnt
   $ sudo mount -t ext2 /dev/sdb1 ~/mnt
   $ sudo mkdir ~/mnt/boot
   $ sudo cp tmp/deploy/images/adsp-sc573-ezkit/adsp-sc5xx-ramdisk-adsp-sc573-ezkit.cpio.xz ~/mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp tmp/deploy/images/adsp-sc573-ezkit/sc573-ezkit.dtb ~/mnt/boot/
   $ sudo cp tmp/deploy/images/adsp-sc573-ezkit/fitImage ~/mnt/boot/
   $ sudo tar -xf tmp/deploy/images/adsp-sc573-ezkit/adsp-sc5xx-minimal-adsp-sc573-ezkit.tar.xz -C ~/mnt
   $ sudo umount ~/mnt

The file system and kernel image are now installed on to the SD Card. The SD Card can now be safely removed from the Host PC.

| 
| === Booting Linux from the SD card === Insert the SD card to target board, and reset the board and enter into U-Boot

.. code:: bash

   => run sdcardboot
   or 
   => run ramboot_emmc

The linux kernel will then boot up using the file system stored in SD card.

| 
