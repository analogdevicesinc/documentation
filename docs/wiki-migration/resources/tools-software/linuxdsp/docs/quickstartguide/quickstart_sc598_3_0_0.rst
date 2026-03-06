Yocto Linux 3.0.0 Quickstart Guide for ADSP-SC598
=================================================

.. important::

   The following instructions are for the ADSP-SC598-EZKIT development board (the EV-SC598-SOM System-on-Module (SOM) board attached to the EV-SOMCRR-EZKIT carrier board). For instructions for other processors and development boards please refer to :doc:`Linux for ADSP-SC5xx Processors 3.0.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>`\


Setting Up Your Host PC
-----------------------

The build system is currently supported on host PCs running Ubuntu 20.04 LTS 64-bit.

| 
| ==== Installing Required Packages ==== In order to build and deploy Linux to your ADSP-SC598-EZKIT development board you will need to install the following packages on your host PC.

.. code:: bash

   $ sudo apt-get update
   $ sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm u-boot-tools openssl curl tftpd-hpa python zstd liblz4-tool

| 
| ==== Configuring TFTP Service==== A TFTP server on the host is used to transfer images to the development board. Install and configure.

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

   $ mkdir ~/gxp2
   $ cd ~/gxp2
   $ mkdir bin
   $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ./bin/repo
   $ chmod a+x ./bin/repo
   $ ./bin/repo init \
      -u https://github.com/analogdevicesinc/lnxdsp-repo-manifest.git \
      -b release/yocto-3.0.0 \
      -m release-yocto-3.0.0.xml
   $ ./bin/repo sync

| 
| ====== Building the Image ======

Preparing the buildtool
~~~~~~~~~~~~~~~~~~~~~~~

Yocto requires the environment to be configured before building is possible.  A setup-environment script in the gxp2 folder contains all the required environment settings for your build target. Source the setup script for your board:

.. code:: bash

   $ source setup-environment -m adsp-sc598-som-ezkit

Sourcing the script will configure your build environment and create a build folder along with a local build configuration file.  See the Yocto Manual for further details.

.. important::

   Note that the build environment needs to be sourced once only before building.  If later working in a different terminal the setup-environment script should be sourced again.  If sourcing the setup-environment script is done without specifying the machine Yocto will reuse the previous configuration settings and retain any changes made to the files in the conf folder.


| 
| ==== Building the example ==== You can build two different versions of the root file system; minimal and full. To build the example images invoke bitbake from within the build directory created previously.

.. code:: bash

   $ bitbake adsp-sc5xx-minimal
   $ bitbake adsp-sc5xx-full

When the build completes you will see a warning that the ELF binary has relocations in .text. It is OK to ignore this warning

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

When the build has completed you will find a set of files in the <BUILD_DIR>/tmp/deploy/sdk directory. For example, the minimal image on SC598:

.. code:: bash

   $ ls tmp/deploy/sdk
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa55-adsp-sc598-som-ezkit-toolchain-3.0.0.host.manifest
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa55-adsp-sc598-som-ezkit-toolchain-3.0.0.sh
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa55-adsp-sc598-som-ezkit-toolchain-3.0.0.target.manifest
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa55-adsp-sc598-som-ezkit-toolchain-3.0.0.testdata.json

The ``adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa55-adsp-sc598-som-ezkit-toolchain-3.0.0.sh`` is a self-extracting archive containing the SDK.

Installing the SDK
^^^^^^^^^^^^^^^^^^

Invoke the self-extracting archive. It will default to installing to ``/opt/adi-distro-glibc/3.0.0`` but gives you the option to select your own install folder during the installation. For the minimal image on SC598

.. code:: bash

   $ ./adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa55-adsp-sc598-som-ezkit-toolchain-3.0.0.sh
   Analog Devices Inc Reference Distro (glibc) SDK installer version 3.0.0
   =======================================================================
   Enter target directory for SDK (default: /opt/adi-distro-glibc/3.0.0):
   You are about to install the SDK to "/opt/adi-distro-glibc/3.0.0". Proceed [Y/n]?
   Extracting SDK....................................................................................................................done
   Setting it up...done
   SDK has been successfully set up and is ready to be used.
   Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
    $ . /opt/adi-distro-glibc/3.0.0/environment-setup-cortexa55-adi_glibc-linux

Your SDK is now installed.

Running U-Boot on the Board for the first time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   It's always good practice to erase the contents of ``/tftpboot/`` before running and/or flashing a new build of U-Boot or Linux. You can do so by executing ``rm /tftpboot/*`` before proceeding


Copy the U-Boot binary & loader files to the tftp directory:

.. code:: bash

   $ cp tmp/deploy/images/adsp-sc598-som-ezkit/u-boot-proper-sc598-som-ezkit.elf /tftpboot/
   $ cp tmp/deploy/images/adsp-sc598-som-ezkit/u-boot-spl-sc598-som-ezkit.elf /tftpboot/
   $ cp tmp/deploy/images/adsp-sc598-som-ezkit/stage1-boot.ldr /tftpboot/
   $ cp tmp/deploy/images/adsp-sc598-som-ezkit/stage2-boot.ldr /tftpboot/

Before installing the software on to the development board, ensure that the following cables are connected:

-  Board connected to network via ethernet cable using J13 connector.
-  Board connected to host PC using USB micro cable, connected to USB/UART port on the development board
-  Board connected to the ICE 1000 or ICE 2000 via the DEBUG port on the board
-  ICE is also connected to host PC via USB mini cable

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc598-som-ezkit_overview-4.png
   :width: 400px

-  On the carrier board is a set of micro switches labelled SW1. These should all be set to the OFF position before continuing.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc594-som-ezkit-switches.jpg
   :width: 400px

-  The Power jumper JP1 on the EV-SC598-SOM board should be fitted so that it shorts the two pins closest to the edge. This will enable the routing of power from the SOMCRR-EZKIT.

-  The BOOT MODE selector on the EV-SC598-SOM board should be turned to "0".

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/sc598-closeup-1.jpg
   :width: 400px

The console output from U-Boot and later on Linux will appear on the USB serial port configured in minicom earlier so open up minicom.

::

   ;''**Terminal1: minicom**''
   :<code bash>$ sudo minicom </code>

In a separate console launch OpenOCD and connect to the development board.

::

   ;''**Terminal2: OpenOCD**''
   :<code bash>

$ sdk_usr=/opt/adi-distro-glibc/3.0.0/sysroots/x86_64-adi_glibc_sdk-linux/usr/ $ $sdk_usr/bin/openocd -f $sdk_usr/share/openocd/scripts/interface/<ICE>.cfg -f $sdk_usr/share/openocd/scripts/target/adspsc59x_a55.cfg </code> Where ``<ICE>`` should be replaced with ``ice1000`` or ``ice2000`` depending on your hardware. When successful you should see a message similar to the console output below

.. code:: bash

   Open On-Chip Debugger (PKGVERSION)  OpenOCD 0.10.0-g40378454d (2023-04-05-10:35)
   Licensed under GNU GPL v2
   Report bugs to <processor.tools.support@analog.com>
   Info : only one transport option; autoselect 'jtag'
   adapter speed: 5000 kHz

   Info : halt and restart using CTI
   Info : Listening on port 6666 for tcl connections
   Info : Listening on port 4444 for telnet connections
   Info : ICE-1000 firmware version is 1.0.2
   Info : clock speed 5000 kHz
   Info : JTAG tap: adspsc59x.adjc tap/device found: 0x028240cb (mfg: 0x065 (Analog Devices), part: 0x2824, ver: 0x0)
   Info : JTAG tap: adspsc59x.cpu enabled
   Info : DAP adspsc59x.cpu DPIDR indicates ADIv5 protocol is being used
   Info : starting gdb server for adspsc59x.cpu on 3333
   Info : Listening on port 3333 for gdb connections

In a third console window launch GDB and type ``target extended-remote :3333``. This will make GDB to connect to the gdbserver on the local host using port 3333. Then, load the U-Boot SPL into RAM by typing ``load``. Hit Ctrl+C to interrupt thereafter.

::

   ;''**Terminal3: GDB**''
   : <code bash>

$ cd /tftpboot $ /opt/adi-distro-glibc/3.0.0/sysroots/x86_64-adi_glibc_sdk-linux/usr/bin/aarch64-adi_glibc-linux/aarch64-adi_glibc-linux-gdb u-boot-spl-sc598-som-ezkit.elf ... (gdb) target extended-remote :3333 Remote debugging using :3333 0x000000000000352c in ?? () (gdb) load Loading section .text, size 0x153b0 lma 0x20080000 Loading section .rodata, size 0x312b lma 0x200953b0 Loading section .dtb.init.rodata, size 0x19e0 lma 0x200984e0 Loading section .data, size 0xaed lma 0x20099ec0 Loading section .u_boot_list, size 0x1720 lma 0x2009a9b0 Start address 0x20080000, load size 114888 Transfer rate: 29 KB/sec, 11488 bytes/write. (gdb) c Continuing. ^C Program received signal SIGINT, Interrupt. </code>

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

   (gdb) load u-boot-proper-sc598-som-ezkit.elf
   Loading section .text, size 0x150 lma 0x96000000
   Loading section .efi_runtime, size 0x1068 lma 0x96000150
   Loading section .text_rest, size 0x60ec0 lma 0x96001800
   Loading section .rodata, size 0x13b5d lma 0x960626c0
   Loading section .hash, size 0x18 lma 0x96076220
   Loading section .dtb.init.rodata, size 0x2260 lma 0x96076240
   Loading section .data, size 0x41b0 lma 0x960784a0
   Loading section .got, size 0x8 lma 0x9607c650
   Loading section .got.plt, size 0x18 lma 0x9607c658
   Loading section .u_boot_list, size 0x3318 lma 0x9607c670
   Loading section .efi_runtime_rel, size 0x1b0 lma 0x9607f988
   Loading section .rela.dyn, size 0xbfd0 lma 0x9607fb38
   Start address 0x96000000, load size 570549
   Transfer rate: 28 KB/sec, 12967 bytes/write.
   (gdb) c
   Continuing.

At this point U-Boot will now be running in RAM on your target board. You should see U-Boot booting in the minicom console (Terminal 1). Press a key to interrupt the boot process before the countdown terminates:

::

   ;''**Terminal1: minicom**''
   :  <code bash>

U-Boot 2020.10 (Mar 16 2023 - 13:07:24 +0000)

CPU: ADSP ADSP-SC598-0.0 (spi slave boot) Model: ADI sc598-som-ezkit DRAM: 224 MiB WDT: Started with servicing (30s timeout) MMC: mmc@310C7000: 0 Loading Environment from SPIFlash... SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB OK In: serial@0x31003000 Out: serial@0x31003000 Err: serial@0x31003000 Net: eth0: eth0 Hit any key to stop autoboot: 0 => </code>

Flash U-Boot to SPI Flash
"""""""""""""""""""""""""

| 
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

   If flashing a board that had been previously programmed, it's good to erase the whole flash before as sometimes previous U-Boot installations might leave remnants. You can do that by typing ``=> sf probe ${sfdev}; sf erase 0 0x4000000`` on the U-Boot prompt before proceeding to the following instructions


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
   Load address: 0x96000000
   Loading: ########
            4.8 MiB/s
   done
   Bytes transferred = 115008 (1c140 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x0, size 0x1c140
   SF: 115008 bytes @ 0x0 Written: OK
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'stage2-boot.ldr'.
   Load address: 0x96000000
   Loading: ###########################################
            5.3 MiB/s
   done
   Bytes transferred = 629616 (99b70 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x20000, size 0x99b70
   SF: 629616 bytes @ 0x20000 Written: OK

In order to store the ``serverip`` and the DHCP or otherwise assigned IP address of the board and have them available on next boot, you can run the following command:

.. code:: bash

   => saveenv
   Saving Environment to SPIFlash... Erasing SPI flash...Writing to SPI flash...done
   OK

At this point the U-Boot binary is stored in flash. You can now disconnect the ICE-1000 or ICE-2000 from the development board and make sure to switch the BMODE to position 1. You will only need to reconnect this if your board fails to boot and you need to re-follow these instructions.

Booting Linux
-------------

Booting the minimal image from QSPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The U-Boot console is used to copy U-Boot (SPL and Proper), the minimal root filesystem image and the fitImage (which contains the kernel image and dtb file) into RAM and then write them to Flash. Copy the required files from <BUILD DIR>/tmp/deploy/images to your /tftpboot directory.

.. code:: bash

   $ cp tmp/deploy/images/adsp-sc598-som-ezkit/stage1-boot.ldr /tftpboot/
   $ cp tmp/deploy/images/adsp-sc598-som-ezkit/stage2-boot.ldr /tftpboot/
   $ cp tmp/deploy/images/adsp-sc598-som-ezkit/fitImage /tftpboot/
   $ cp tmp/deploy/images/adsp-sc598-som-ezkit/adsp-sc5xx-minimal-adsp-sc598-som-ezkit.jffs2 /tftpboot

If your network **supports** DHCP, run:

.. code:: bash

   => run update_spi

If your network **does NOT support** DHCP, in the U-Boot console configure the board IP address and remove the "run init_ethernet;" from the "start_update_spi" command.

.. code:: bash

   => setenv ipaddr <IPADDR>
   => edit start_update_spi
   => edit: <remove "run init_ethernet;" from here> sf probe ${sfdev}; sf erase 0 ${sfsize}; run update_spi_uboot; run update_spi_fit; run update_spi_rfs; sleep 3; saveenv
   => run update_spi 

After removing "run init_ethernet;" from update_spi, issue the "run update_spi" command as above.

You should see output similar to the following.

.. code:: bash

   => run update_spi
   PHY 0x00: OUI = 0x80028, Model = 0x23, Rev = 0x01, 100baseT, FDX
   Speed: 1000, full duplex
   BOOTP broadcast 1
   DHCP client bound to address 10.37.33.113 (97 ms)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   SF: 67108864 bytes @ 0x0 Erased: OK
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'stage1-boot.ldr'.
   Load address: 0x96000000
   Loading: ########
            393.6 KiB/s
   done
   Bytes transferred = 115008 (1c140 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x0, size 0x1c140
   SF: 115008 bytes @ 0x0 Written: OK
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'stage2-boot.ldr'.
   Load address: 0x96000000
   Loading: ###########################################
            2.4 MiB/s
   done
   Bytes transferred = 629616 (99b70 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x20000, size 0x99b70
   SF: 629616 bytes @ 0x20000 Written: OK
   Speed: 1000, full duplex
   Using eth0 device
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
            #####################################################
            2.5 MiB/s
   done
   Bytes transferred = 7456974 (71c8ce hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x100000, size 0x71c8ce
   SF: 7456974 bytes @ 0x100000 Written: OK
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'adsp-sc5xx-minimal-adsp-sc598-som-ezkit.jffs2'.
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
            #########
            3.2 MiB/s
   done
   Bytes transferred = 23986176 (16e0000 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x1000000, size 0x16e0000
   SF: 23986176 bytes @ 0x1000000 Written: OK
   Saving Environment to SPIFlash... Erasing SPI flash...Writing to SPI flash...done
   OK
   =>

The U-Boot image, root filesystem and Linux kernel are now stored in QSPI. Adjust the BOOT MODE selector to **position 1** and press the RESET button, the board should boot into Linux.

.. code:: bash

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

   adsp-sc598-som-ezkit login: root
   Password: adi
   root@adsp-sc598-som-ezkit:~# 

The username is **root** and the password is **adi**.

Booting Linux Using SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setting up U-boot to boot from SD Card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setup Yocto for changes in U-boot

.. code:: bash

   $ devtool modify u-boot-adi

There is an issue with devtool in this version of bitbake - apply the following fix to ../sources/poky/meta/classes/externalsrc.bbclass

.. code:: diff

   --- a/meta/classes/externalsrc.bbclass
   +++ b/meta/classes/externalsrc.bbclass
   @@ -36,6 +36,8 @@ python () {
        if externalsrcbuild and not externalsrcbuild.startswith("/"):
            bb.error("EXTERNALSRC_BUILD must be an absolute path")
    
   +    srcpv = d.getVar('SRCPV')
   +
        # If this is the base recipe and EXTERNALSRC is set for it or any of its
        # derivatives, then enable BB_DONT_CACHE to force the recipe to always be
        # re-parsed so that the file-checksums function for do_compile is run every

Edit workspace/source/u-boot-adi/arch/arm/dts/sc598-som.dtsi

.. code:: bash

   --- a/arch/arm/dts/sc598-som.dtsi
   +++ b/arch/arm/dts/sc598-som.dtsi
   @@ -60,8 +60,11 @@
               pinctrl-0 = <&mmc_defaults>;
               clocks = <&emmcclk>;
               clock-names = "core";
   -           max-frequency = <50000000>;
   -           bus-width = <8>;
   +           //max-frequency = <50000000>;
   +           max-frequency = <44000000>;
   +           no-1-8-v;
   +           //bus-width = <8>;
   +           bus-width = <4>;
               u-boot,dm-pre-reloc;
           };
       };
   @@ -203,7 +206,7 @@
           emmc {
               gpio-hog;
               gpios = <8 GPIO_ACTIVE_HIGH>;
   -           output-low;
   +           output-high;
               line-name = "emmc-en";
               u-boot,dm-pre-reloc;
           };
   @@ -211,7 +214,7 @@
           emmc-som-en {
               gpio-hog;
               gpios = <9 GPIO_ACTIVE_HIGH>;
   -           output-high;
   +           output-low;
               line-name = "emmc-som-en";
               u-boot,dm-pre-reloc;
           };

Rebuild U-boot in Yocto

.. code:: bash

   $ devtool build u-boot-adi

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

   $ sudo mkfs.ext4 /dev/sdb1

| 
| === Writing the kernel and file system to the SD Card === Next, we need to copy the Linux file system and kernel image to the SD Card. We install this on to the SD Card by mounting the file system on to the local Host PC and copying the contents on to the SD Card. To allow the choice of booting using ramboot and sdcard boot we copy the ramboot image to the SD card as well as extract the minimal image to the SD card.

.. code:: bash

   $ mkdir ~/mnt
   $ sudo mount -t ext4 /dev/sdb1 ~/mnt
   $ sudo mkdir ~/mnt/boot
   $ sudo cp tmp/deploy/images/adsp-sc598-som-ezkit/adsp-sc5xx-ramdisk-adsp-sc598-som-ezkit.cpio.xz ~/mnt/boot/adsp-sc5xx-ramdisk-adsp-sc598-som-ezkit.cpio.xz.u-boot
   $ sudo cp tmp/deploy/images/adsp-sc598-som-ezkit/sc598-som-ezkit.dtb ~/mnt/boot/
   $ sudo cp tmp/deploy/images/adsp-sc598-som-ezkit/fitImage ~/mnt/boot/
   $ sudo tar -xf tmp/deploy/images/adsp-sc598-som-ezkit/adsp-sc5xx-minimal-adsp-sc598-som-ezkit.tar.xz -C ~/mnt
   $ sudo umount ~/mnt

The file system and kernel image are now installed on to the SD Card. The SD Card can now be safely removed from the Host PC.

| 
| === Booting Linux from the SD card === Set U-boot environment variables

.. code:: bash

   => setenv mmcargs 'setenv bootargs root=/dev/mmcblk0p1 rw rootfstype=ext4 rootwait earlycon=adi_uart,0x31003000 console=ttySC0,115200'
   => setenv mmcboot 'mmc rescan; run mmcload; run mmcargs; bootm ${loadaddr};'
   => setenv mmcload 'ext4load mmc 0:1 ${loadaddr} /boot/${imagefile};'
   => saveenv

Run Linux from SD card

.. code:: bash

   $ run mmcboot

The linux kernel will then boot up using the file system stored in SD card.

Booting rootfs from SD card
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the steps to enable SD card boot. This step include enabling emmc peripheral in Linux Kernel.

.. code:: bash

   $ devtool modify linux-adi

Modify build/workspace/source/linux-adi/arch/arm64/boot/dts/adi/sc598-som.dtsi

.. code:: bash

   @@ -297,14 +297,14 @@ uart0-flow-en {
                   emmc {
                           gpio-hog;
                           gpios = <8 0x0>;
   -                       output-low;
   +                       output-high;
                           line-name = "emmc-en";
                   };
    
                   emmc-som-en {
                           gpio-hog;
                           gpios = <9 0x0>;
   -                       output-high;
   +                       output-low;
                           line-name = "emmc-som-en";
                   };
           };
   @@ -313,8 +313,9 @@ emmc-som-en {
    &mmc0{
           pinctrl-names = "default";
           pinctrl-0 = <&mmc0_8bgrp>;
   -       bus-width = <8>;
   -       max-frequency = <50000000>;
   +       bus-width = <4>;
   +       no-1-8-v;
   +       max-frequency = <44000000>;
           non-removable;
           status = "okay";
    };

Rebuild the Linux kernel

.. code:: bash

   $ devtool build linux-adi

Copy the new generated fitImage to boot folder on SD card.


| 

Booting Linux from USB Mass Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Formatting USB stick
^^^^^^^^^^^^^^^^^^^^

First step is to format USB stick to U-Boot supported formats.

To format the USB stick, follow the commands below. The example code in this section assumes that the USB device is reported to be /dev/sdb. Ensure that you change these commands to use your device.

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

Format the USB stick to EXT4 filesystem

.. code:: bash

   $ sudo mkfs.ext4 /dev/sdb1

Writing kernel and rootfs image to USB Mass Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

   $ mkdir ~/mnt
   $ sudo mount -t ext4 /dev/sdb1 ~/mnt
   $ sudo mkdir ~/mnt/boot
   $ sudo tar -xf tmp/deploy/images/adsp-sc598-som-ezkit/adsp-sc5xx-minimal-adsp-sc598-som-ezkit.tar.xz -C ~/mnt
   $ sudo cp tmp/deploy/images/adsp-sc598-som-ezkit/fitImage ~/mnt/boot/
   $ sudo umount ~/mnt

Booting Linux from the USB Mass Storage device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To boot from ADSP-SC598-EZKIT run in u-boot

.. code:: bash

   => setenv usbload 'ext4load usb 0 ${initramaddr} /boot/${initramfile}; ext4load usb 0 ${loadaddr} /boot/${imagefile};'
   => setenv usbboot 'usb start; run usbload; run ramargs; bootm ${loadaddr} ${initramaddr};'
   => run usbboot

Booting rootfs from USB Mass Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the step how to setup USB stick in chapter above :doc:`Yocto Linux 3.0.0 Quickstart Guide for ADSP-SC598 </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc598_3_0_0>`. Set environment variables in U-boot

.. code:: bash

   => setenv usbargs 'setenv bootargs root=/dev/sda1 rw rootfstype=ext4 rootwait earlycon=adi_uart,0x31003000 console=ttySC0,115200'
   => setenv usbload 'ext4load usb 0 ${loadaddr} /boot/${imagefile};'
   => setenv usbboot 'usb start; run usbload; run usbargs; bootm ${loadaddr};'

And type to boot

.. code:: bash

   => run usbboot

Now the rootfs is set to your USB stick and amount of space equals of size of partition on USB stick.

|

| ==== Booting Linux Using TFTP ==== In order to boot Linux, the TFTP server should be setup as :doc:`above </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc598>` and a copy of the fitImage should be copied into the **/tftpboot** directory.

.. code:: bash

   $ cp tmp/deploy/images/adsp-sc598-som-ezkit/fitImage /tftpboot/

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
         Tasks: 0 (limit: 18797)
        Memory: 0B
        CGroup: /system.slice/nfs-server.service

   Sep 06 14:38:29 $YOUR_HOSTNAME systemd[1]: Starting NFS server and services...
   Sep 06 14:38:31 $YOUR_HOSTNAME systemd[1]: Finished NFS server and services.

If it's reported as inactive, wait a few moments and check the status again.

The root filesystem should then be copied to /romfs.

.. code:: bash

   $ sudo tar -xf tmp/deploy/images/adsp-sc598-som-ezkit/adsp-sc5xx-full-adsp-sc598-som-ezkit.tar.xz -C /romfs

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

   adsp-sc598-som-ezkit login: root
   Password: adi
   root@adsp-sc598-som-ezkit:~# 

--------------

Further Examples
----------------

-  :doc:`USB Gadget Audio </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/device_mode/gadget_audio_3_0_0>`
-  :doc:`U-Boot Falcon Mode </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/u-boot-falcon-mode>`
-  :doc:`SHARC-ALSA Example </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/sharc-alsa-example>`
-  :doc:`Store kernel image and RootFS on the eMMC </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/emmc-kernel-rfs-storage>`
