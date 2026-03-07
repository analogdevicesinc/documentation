.. warning::

   These pages are not updated anymore. Documentation has been moved to :git-lnxdsp-adi-meta:`wiki\`


Yocto Linux 2.1.0 Quickstart Guide for ADSP-SC594
=================================================

.. important::

   The following instructions are for the ADSP-SC594-EZKIT development board (the EV-SC594-SOM System-on-Module (SOM) board attached to the EV-SOMCRR-EZKIT carrier board). For instructions for other processors and development boards please refer to :doc:`Linux for ADSP-SC5xx Processors 2.1.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/2.1.0>`\


Setting Up Your Host PC
=======================

The build system is currently supported on host PCs running Ubuntu 20.04 LTS 64-bit.

| 
| ==== Installing Required Packages ==== In order to build and deploy Linux to your ADSP-SC594-EZKIT development board you will need to install the following packages on your host PC.

::

   $ sudo apt-get update
   $ sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm u-boot-tools openssl curl tftpd-hpa python

| 
| ==== Installing CrossCore Embedded Studio ==== CrossCore Embedded Studio contains OpenOCD which is used to transfer U-Boot into RAM for the first initial boot of the device. The tools are created for 32-bit architecture and therefore requires a 32-bit libz package to run. Download and install it.

::

   $ wget https://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.11.0/adi-CrossCoreEmbeddedStudio-linux-x86-2.11.0.deb
   $ sudo dpkg -i ./adi-CrossCoreEmbeddedStudio-linux-x86-2.11.0.deb
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

   $ mkdir ~/gxp
   $ cd ~/gxp
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

Yocto requires the environment to be configured before building is possible. A setup-environment script in the gxp folder contains all the required environment settings for your build target. Source the setup script for your board:

::

   $ source setup-environment -m adsp-sc594-som-ezkit

Sourcing the script will configure your build environment and create a build folder along with a local build configuration file. See the Yocto Manual for further details.

.. important::

   Note that the build environment needs to be sourced once only before building. If later working in a different terminal the setup-environment script should be sourced again. If sourcing the setup-environment script is done without specifying the machine Yocto will reuse the previous configuration settings and retain any changes made to the files in the conf folder.


   | 

Building the example
--------------------

You can build three different versions of the root filesystem; minimal, ramdisk and full. To build the example images invoke bitbake from within the build directory created previously.

::

   $ bitbake adsp-sc5xx-minimal
   $ bitbake adsp-sc5xx-ramdisk
   $ bitbake adsp-sc5xx-full

When the build completes you will see a warning that the ELF binary has relocations in .text. It is OK to ignore this warning

Running U-Boot on the Board for the first time
----------------------------------------------

Copy the U-Boot SPL and Proper elf files to the tftp directory:

::

   $ cp tmp/deploy/images/adsp-sc594-som-ezkit/u-boot-spl-sc594-som-ezkit.elf /tftpboot/ 
   $ cp tmp/deploy/images/adsp-sc594-som-ezkit/u-boot-proper-sc594-som-ezkit.elf /tftpboot/

Before installing the software on to the development board, ensure that the following cables are connected:

-  Board connected to network via ethernet cable using J13 connector.
-  Board connected to host PC using USB micro cable, connected to USB/UART port on the development board
-  Board connected to the ICE 1000 or ICE 2000 via the DEBUG port on the board
-  ICE is also connected to host PC via USB mini cable

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc594-som-ezkit.jpg
   :width: 400px

-  On the SOMCRR-EZKIT is a set of micro switches labelled SW1. These should all be set to the OFF position before continuing.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc594-som-ezkit-switches.jpg
   :width: 400px

-  The Power jumper JP1 on the EV-SC594-SOM board should be fitted so that it shorts the two pins closest to the edge. This will enable the routing of power from the SOMCRR-EZKIT.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc594-som-ezkit-power-selector.jpg
   :width: 400px

-  The BOOT MODE selector on the EV-SC594-SOM board should be turned to "0".

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc594-som-ezkit-bootmode-fault.jpg
   :width: 400px

.. note::

   The FAULT LED on the board will come on the first time the device is powered on. This is due to the BootROM failing to find a valid image stored in QSPI. Once the QSPI has been correctly programmed this will no longer be the case.


The console output from U-Boot and later on Linux will appear on the USB serial port configured in minicom earlier so open up minicom.

::

   ;''**Terminal1: minicom**''
   :<code>$ sudo minicom </code>

In a separate console launch OpenOCD and connect to the development board.

::

   ;''**Terminal2: OpenOCD**''
   :<code>

$ cd /opt/analog/cces/2.11.0/ARM/openocd/share/openocd/scripts $ sudo /opt/analog/cces/2.11.0/ARM/openocd/bin/openocd -f interface/<ICE>.cfg -f board/ev-sc594-som.cfg</code> Where ``<ICE>`` should be replaced with ``ice1000`` or ``ice2000`` depending on your hardware. When successful you should see a message similar to the console output below

::

   Open On-Chip Debugger (Analog Devices CCES 2.11.0)  OpenOCD 0.10.0-gd1ba667 (2022-04-13-15:58)
   Licensed under GNU GPL v2
   Report bugs to <processor.tools.support@analog.com>
   Info : only one transport option; autoselect 'jtag'
   adapter speed: 5000 kHz

   Info : halt and restart using CTI
   adspsc59x_a55_init
   Info : Listening on port 6666 for tcl connections
   Info : Listening on port 4444 for telnet connections
   Info : ICE-1000 firmware version is 1.0.2
   Info : clock speed 5000 kHz
   Info : JTAG tap: adspsc594.adjc tap/device found: 0x0282e0cb (mfg: 0x065 (Analog Devices), part: 0x282e, ver: 0x0)
   Info : JTAG tap: adspsc594.cpu enabled
   Info : DAP adspsc594.cpu DPIDR indicates ADIv6 protocol is being used
   Info : adspsc594.cpu: hardware has 6 breakpoints, 4 watchpoints
   Info : starting gdb server for adspsc594.cpu on 3333
   Info : Listening on port 3333 for gdb connections

In a third console window launch GDB and type ``target extended-remote :3333``. This will make GDB to connect to the gdbserver on the local host using port 3333. Then, load the U-Boot SPL into RAM by typing ``load u-boot-spl-sc594-som-ezkit.elf`` and hit Ctrl+C to interrupt.

::

   ;''**Terminal3: GDB**''
   : <code>

$ cd /tftpboot $ /opt/analog/cces/2.11.0/ARM/arm-none-eabi/bin/arm-none-eabi-gdb u-boot-proper-sc594-som-ezkit.elf ... (gdb) target extended-remote :3333 Remote debugging using :3333 0x000000000000352c in ?? () (gdb) load Loading section .text, size 0x150 lma 0x96000000 Loading section .efi_runtime, size 0xfb0 lma 0x96000150 Loading section .text_rest, size 0x5ad94 lma 0x96001800 Loading section .rodata, size 0x12f1c lma 0x9605c594 Loading section .hash, size 0x18 lma 0x9606f4b8 Loading section .dtb.init.rodata, size 0xac0 lma 0x9606f4d0 Loading section .data, size 0x47e8 lma 0x9606ff90 Loading section .got, size 0x8 lma 0x96074778 Loading section .got.plt, size 0x18 lma 0x96074780 Loading section .u_boot_list, size 0x2800 lma 0x96074798 Loading section .efi_runtime_rel, size 0x1b0 lma 0x96076f98 Loading section .rela.dyn, size 0xb700 lma 0x96077148 Start address 0x96000000, load size 532800 Transfer rate: 29 KB/sec, 12685 bytes/write. (gdb) c Continuing. </code>

At this point U-Boot will now be running in RAM on your target board. You should see U-Boot booting in the minicom console (Terminal 1). Press a key to interrupt the boot process before the countdown terminates:

::

   ;''**Terminal1: minicom**''
   :  <code>

U-Boot SPL 2020.10 (Aug 23 2022 - 13:09:23 +0000) ADI Boot Mode: 0 (JTAG/BOOTROM) SPL execution has completed. Please load U-Boot Proper via JTAG

U-Boot 2020.10 (Aug 23 2022 - 13:09:23 +0000)

Model: ADI sc594-som-ezkit

::

        Watchdog enabled

I2C: ready DRAM: 224 MiB MMC: mmc@310C7000: 0 Loading Environment from SPIFlash... SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB OK In: serial@0x31003000 Out: serial@0x31003000 Err: serial@0x31003000 Net: eth0: eth@0x31040000 Hit any key to stop autoboot: 0 => </code>

|

| ==== Booting the minimal image from QSPI ==== The U-Boot console is used to copy U-Boot (SPL and Proper), the minimal root filesystem image and the fitImage (which contains the kernel image and dtb file) into RAM and then write them to Flash. Copy the required files from <BUILD DIR>/tmp/deploy/images to your /tftpboot directory.

::

   $ cp tmp/deploy/images/adsp-sc594-som-ezkit/stage1-boot.ldr /tftpboot/
   $ cp tmp/deploy/images/adsp-sc594-som-ezkit/stage2-boot.ldr /tftpboot/
   $ cp tmp/deploy/images/adsp-sc594-som-ezkit/fitImage /tftpboot/
   $ cp tmp/deploy/images/adsp-sc594-som-ezkit/adsp-sc5xx-minimal-adsp-sc594-som-ezkit.jffs2 /tftpboot

| 
| In the U-Boot console, set the IP address of the Host Linux PC that hosts the binary files on TFTP. Also, set the same address to the variable ``serverip``

::

   ;''**Terminal1: minicom**''
   :  

::

   => setenv tftpserverip <SERVERIP>
   => setenv serverip <SERVERIP>

.. note::

   To find the IP address of your host Linux PC you can issue the ``ip addr`` command from the shell or console.


If your network **supports** DHCP, run:

::

   => run update_qspi_sc594

If your network **does NOT support** DHCP, in the U-Boot console configure the board IP address and remove the "run init_ethernet;" from the "update_spi_sc594" command.

::

   => setenv ipaddr <IPADDR>
   => edit update_spi_sc594
   => edit: <remove "run init_ethernet;" from here> sf probe ${sfdev}; sf erase 0 ${sfsize}; run update_spi_uboot; run update_spi_fit; run update_spi_rfs; sleep 3; saveenv
   => run update_qspi_sc594 

After removing "run init_ethernet;" from update_spi_sc594, issue the "run update_qspi_sc594" command as above.

You should see output similar to the following.

::

   => run update_qspi_sc594
   PHY 0x00: OUI = 0x80028, Model = 0x23, Rev = 0x01, 100baseT, FDX
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   SF: 67108864 bytes @ 0x0 Erased: OK
   Speed: 1000, full duplex
   Using eth@0x31040000 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'stage1-boot.ldr'.
   Load address: 0x96000000
   Loading: ######
            3.6 MiB/s
   done
   Bytes transferred = 79480 (13678 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x0, size 0x13678
   SF: 79480 bytes @ 0x0 Written: OK
   Speed: 1000, full duplex
   Using eth@0x31040000 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'stage2-boot.ldr'.
   Load address: 0x96000000
   Loading: #########################################
            5.2 MiB/s
   done
   Bytes transferred = 592288 (909a0 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x20000, size 0x909a0
   SF: 592288 bytes @ 0x20000 Written: OK
   Speed: 1000, full duplex
   Using eth@0x31040000 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'fitImage'.
   Load address: 0x96000000
   Loading: #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            ######################################################
            5.6 MiB/s
   done
   Bytes transferred = 14149218 (d7e662 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x160000, size 0xd7e662
   SF: 14149218 bytes @ 0x160000 Written: OK
   Speed: 1000, full duplex
   Using eth@0x31040000 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'adsp-sc5xx-minimal-adsp-sc594-som-ezkit.jffs2'.
   Load address: 0x96000000
   Loading: #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            ##############################
            5.6 MiB/s
   done
   Bytes transferred = 30015488 (1ca0000 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x1000000, size 0x1ca0000
   SF: 30015488 bytes @ 0x1000000 Written: OK
   Saving Environment to SPIFlash... Erasing SPI flash...Writing to SPI flash...done
   OK
   =>

The U-Boot image, root filesystem and Linux kernel are now stored in QSPI. Adjust the BOOT MODE selector to **position 1** and press the RESET button, the board should boot into Linux.

::

   ...
   [  OK  ] Started Login Service.
   [  OK  ] Reached target Multi-User System.
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

   adsp-sc594-som-ezkit login: root
   Password: adi
   root@adsp-sc594-som-ezkit:~# 

The username is **root** and the password is **adi**.

| 
| ==== Booting Linux Using TFTP ==== In order to boot Linux, the TFTP server should be setup as :doc:`above </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc594>` and (for both NFS and RAM boot) a copy of the kernel image and dtb file should be copied into the **/tftpboot** directory.

::

   $ cp tmp/deploy/images/adsp-sc594-som-ezkit/Image /tftpboot
   $ cp tmp/deploy/images/adsp-sc594-som-ezkit/sc594-som-ezkit.dtb /tftpboot

| 
| === RAM Boot === For RAM boot a copy of the image containing the filesystem needs copied to the /tftpboot directory.

::

   $ cp tmp/deploy/images/adsp-sc594-som-ezkit/adsp-sc5xx-ramdisk-adsp-sc594-som-ezkit.cpio.xz.u-boot /tftpboot/ramdisk.cpio.xz.u-boot

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

   adsp-sc594-som-ezkit login: root
   Password: adi
   root@adsp-sc594-som-ezkit:~# 

| 
| ==== Building the SDK ==== To build the SDK follow the instructions here :doc:`Building the SDK </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/building-the-sdk>`.
