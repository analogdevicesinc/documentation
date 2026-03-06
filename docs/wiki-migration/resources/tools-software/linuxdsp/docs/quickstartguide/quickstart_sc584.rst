.. warning::

   These pages are not updated anymore. Documentation has been moved to :git-lnxdsp-adi-meta:`wiki\`


Yocto Linux 2.1.0 Quickstart Guide for ADSP-SC584
=================================================

.. important::

   The following instructions are for the ADSP-SC584-EZKIT development board. For instructions for other processors and development boards please refer to :doc:`Linux for ADSP-SC5xx Processors 2.1.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/2.1.0>`\


Setting Up Your Host PC
=======================

The build system is currently supported on host PCs running Ubuntu 20.04 LTS 64-bit.

| 
| ==== Installing Required Packages ==== In order to build and deploy Linux to your ADSP-SC584-EZKIT development board you will need to install the following packages on your host PC.

::

   $ sudo apt-get update
   $ sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm u-boot-tools openssl curl tftpd-hpa python

| 
| ==== Installing CrossCore Embedded Studio ==== CrossCore Embedded Studio contains OpenOCD which is used to transfer U-Boot into RAM for the first initial boot of the device. The tools are created for 32-bit architecture and therefore requires a 32-bit libz package to run. Download and install it.

::

   $ wget https://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.10.0/adi-CrossCoreEmbeddedStudio-linux-x86-2.10.0.deb
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

| 
| ==== Installing the Sources ==== The example is fully contained in the Analog Devices Yocto Linux github repositories.

To install the sources:

.. container:: hide

   TODO: Make sure its the correct repo, branch, manifest file etc


::

   $ mkdir ~/lnxdsp
   $ cd ~/lnxdsp
   $ mkdir bin
   $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ./bin/repo
   $ chmod a+x ./bin/repo
   $ ./bin/repo init \
      -u https://github.com/analogdevicesinc/lnxdsp-repo-manifest.git \
      -b release/yocto-2.1.0 \
      -m release-yocto-2.1.0.xml
   $ ./bin/repo sync

| 
| ===== Building the Image =====

Preparing the buildtool
-----------------------

Yocto requires the environment to be configured before building is possible. A setup-environment script in the ``lnxdsp`` folder contains all the required environment settings for your build target. Source the setup script for your board:

::

   $ source setup-environment -m adsp-sc584-ezkit

Sourcing the script will configure your build environment and create a build folder along with a local build configuration file. See the Yocto Manual for further details.

.. important::

   Note that the build environment needs to be sourced once only before building. If later working in a different terminal the setup-environment script should be sourced again. If sourcing the setup-environment script is done without specifying the machine Yocto will reuse the previous configuration settings and retain any changes made to the files in the conf folder.


| 
| ==== Building the example ==== You can build three different versions of the root filesystem; minimal, ramdisk and full. To build the example images invoke bitbake from within the build directory created previously.

::

   $ bitbake adsp-sc5xx-minimal
   $ bitbake adsp-sc5xx-ramdisk
   $ bitbake adsp-sc5xx-full

When the build completes you will see a warning that the ELF binary has relocations in .text. It is OK to ignore this warning

Running U-Boot on the Board for the first time
----------------------------------------------

Copy the U-Boot & the init binary files to the /tftpboot directory, so that U-Boot can be ran from the board's RAM, along with the U-Boot loader file so that it can be uploaded to the target board:

::

   $ cp tmp/deploy/images/adsp-sc584-ezkit/u-boot-sc584-ezkit /tftpboot/ 
   $ cp tmp/deploy/images/adsp-sc584-ezkit/init-sc584-ezkit.elf /tftpboot/ 
   $ cp tmp/deploy/images/adsp-sc584-ezkit/u-boot-sc584-ezkit.ldr /tftpboot/ 

Before installing the software on to the development board, ensure that the following cables are connected:

-  Board connected to network via ethernet cable using J13 connector.
-  Board connected to host PC using USB micro cable, connected to USB/UART port on the development board
-  Board connected to the ICE 1000 or ICE 2000 via the DEBUG port on the board
-  ICE is also connected to host PC via USB mini cable

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc584-ezkit_overview.jpg
   :width: 400px

-  The BOOT MODE selector on the EV-SC584-SOM board should be turned to "0".

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc584-ezkit_boot_selector.jpg
   :width: 400px

The console output from U-Boot and later on Linux will appear on the USB serial port configured in minicom earlier so open up minicom.

::

   ;''**Terminal1: minicom**''
   :<code>$ sudo minicom </code>

In a separate console launch OpenOCD and connect to the development board.

::

   ;''**Terminal2: OpenOCD**''
   :<code>

$ cd /opt/analog/cces/2.10.0/ARM/openocd/share/openocd/scripts $ sudo /opt/analog/cces/2.10.0/ARM/openocd/bin/openocd -f interface/<ICE>.cfg -f board/adspsc584_ezbrd.cfg</code> Where ``<ICE>`` should be replaced with ``ice1000`` or ``ice2000`` depending on your hardware. When successful you should see a message similar to the console output below

::

   Open On-Chip Debugger (Analog Devices CCES 2.10.0 OpenOCD 0.9.0-ge8d0a22) 0.9.0
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
   Info : JTAG tap: adspsc584.adjc tap/device found: 0x428080cb (mfg: 0x065, part: 0x2808, ver: 0x4)
   Info : JTAG tap: adspsc584.dap enabled
   Info : adspsc584.dap: hardware has 3 breakpoints, 2 watchpoints
   Info : adspsc584.dap: but you can only set 1 watchpoint

In a third console window launch GDB and type ``target extended-remote :3333``. This will make GDB to connect to the gdbserver on the local host using port 3333. Then, load the init file into RAM by typing ``load init-sc584-ezkit.elf`` and run it by typing ``c``. Hit Ctrl+C to interrupt thereafter.

::

   ;''**Terminal3: GDB**''
   : <code>

$ cd /tftpboot $ /opt/analog/cces/2.10.0/ARM/arm-none-eabi/bin/arm-none-eabi-gdb u-boot-sc584-ezkit ... (gdb) target extended-remote :3333 Remote debugging using :3333 0x00004884 in ?? () (gdb) load init-sc584-ezkit.elf Loading section .text, size 0x744 lma 0x20080000 Start address 0x20080028, load size 1860 Transfer rate: 22 KB/sec, 1860 bytes/write. (gdb) c Continuing. ^C Program received signal SIGINT, Interrupt. 0x20080024 in ?? () </code>

Now, load U-Boot into RAM.

::

   ;''**Terminal3: GDB**''
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

At this point U-Boot will now be running in RAM on your target board. You should see U-Boot booting in the minicom console (Terminal 1). Press a key to interrupt the boot process before the countdown terminates:

::

   ;''**Terminal1: minicom**''
   :  <code>

U-Boot 2020.10 (Aug 23 2022 - 13:09:23 +0000)

CPU: ADSP ADSP-SC584-0.1 (Detected Rev: 1.1) (spi flash boot) VCO: 450 MHz, Cclk0: 450 MHz, Sclk0: 112.500 MHz, Sclk1: 112.500 MHz, DCLK: 225 MHz OCLK: 150 MHz Model: ADI sc584-ezkit I2C: ready DRAM: 112 MiB MMC: Loading Environment from SPIFlash... SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB OK In: serial@0x31003000 Out: serial@0x31003000 Err: serial@0x31003000 other init Net: dwmac.3100c000 Hit any key to stop autoboot: 0 => </code>

| 
| == Flash U-Boot to SPI Flash ==
| In the U-Boot console, set the IP address of the Host Linux PC that hosts the U-Boot loader file (``u-boot-sc584-ezkit.ldr``) on TFTP.

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

Next, run the U-Boot update command to copy the U-Boot loader file from the host PC to the target board, and write it into flash:

::

   => run update

You will see an output similar to the one below:

::

   => run update
   Speed: 100, full duplex
   Using dwmac.3100c000 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'u-boot-sc584-ezkit.ldr'.
   Load address: 0x89000000
   Loading: ###############################
            2.2 MiB/s
   done
   Bytes transferred = 453828 (6ecc4 hex)
   SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
   SF: 524288 bytes @ 0x0 Erased: OK
   device 0 offset 0x0, size 0x6ecc4
   SF: 453828 bytes @ 0x0 Written: OK
   =>

| At this point the U-Boot binary is stored in flash. You can now disconnect the ICE-1000 or ICE-2000 from the development board and make sure to switch the BMODE to position 1. You will only need to reconnect this if your board fails to boot and you need to re-follow these instructions.
| ==== Booting Linux Using TFTP ==== In order to boot Linux, the TFTP server should be setup as :doc:`above </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc584>` and (for both NFS and RAM boot) a copy of the kernel image should be copied into the **/tftpboot** directory.

::

   $ cp tmp/deploy/images/adsp-sc584-ezkit/fitImage /tftpboot

| 
| === RAM Boot === For RAM boot a copy of the image containing the filesystem needs copied to the /tftpboot directory.

::

   $ cp tmp/deploy/images/adsp-sc584-ezkit/adsp-sc5xx-ramdisk-adsp-sc584-ezkit.cpio.xz.u-boot /tftpboot/ramdisk.cpio.xz.u-boot

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

The root filesystem should then be copied to /romfs.

::

   $ sudo tar -xf tmp/deploy/images/adsp-sc598-som-ezkit/adsp-sc5xx-full-adsp-sc598-som-ezkit.tar.xz -C /romfs

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

   adsp-sc584-ezkit login: root
   Password: adi
   root@adsp-sc584-ezkit:~# 

The username is **root** and the password is **adi**.

| 
| ==== Building the SDK ==== To build the SDK follow the instructions here :doc:`Building the SDK </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/building-the-sdk>`.
