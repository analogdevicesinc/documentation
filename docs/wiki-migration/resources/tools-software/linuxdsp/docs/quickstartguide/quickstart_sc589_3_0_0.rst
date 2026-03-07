Yocto Linux 3.0.0 Quickstart Guide for ADSP-SC589 (EZKIT & MINI)
================================================================

.. important::

   The following instructions are for the ADSP-SC589-EZKIT and ADSP-SC589-MINI development boards. For instructions for other processors and development boards please refer to :doc:`Linux for ADSP-SC5xx Processors 3.0.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>`\


Setting Up Your Host PC
-----------------------

The build system is currently supported on host PCs running Ubuntu 20.04 LTS 64-bit.

| 
| ==== Installing Required Packages ==== In order to build and deploy Linux to your ADSP-SC589-EZKIT or ADSP-SC589-MINI development board you will need to install the following packages on your host PC.

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

   $ source setup-environment -m adsp-sc589-ezkit

or

.. code:: bash

   $ source setup-environment -m adsp-sc589-mini

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

When the build has completed you will find a set of files in the <BUILD_DIR>/tmp/deploy/sdk directory. For example, the minimal image on SC589-EZKIT:

.. code:: bash

   $ ls tmp/deploy/sdk
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc589-ezkit-toolchain-3.0.0.host.manifest
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc589-ezkit-toolchain-3.0.0.sh
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc589-ezkit-toolchain-3.0.0.target.manifest
   adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc589-ezkit-toolchain-3.0.0.testdata.json

The ``adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc589-ezkit-toolchain-3.0.0.sh`` or ``adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc589-mini-toolchain-3.0.0.sh`` is a self-extracting archive containing the SDK.

Installing the SDK
^^^^^^^^^^^^^^^^^^

Invoke the self-extracting archive. It will default to installing to ``/opt/adi-distro/3.0.0`` but gives you the option to select your own install folder during the installation. For the minimal image on SC589-EZKIT

.. code:: bash

   $ ./adi-distro-glibc-glibc-x86_64-adsp-sc5xx-minimal-cortexa5t2hf-neon-adsp-sc589-ezkit-toolchain-3.0.0.sh
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

   $ cp tmp/deploy/images/adsp-sc589-ezkit/u-boot-proper-sc589-ezkit.elf /tftpboot
   $ cp tmp/deploy/images/adsp-sc589-ezkit/u-boot-spl-sc589-ezkit.elf /tftpboot
   $ cp tmp/deploy/images/adsp-sc589-ezkit/stage1-boot.ldr /tftpboot
   $ cp tmp/deploy/images/adsp-sc589-ezkit/stage2-boot.ldr /tftpboot

or

.. code:: bash

   $ cp tmp/deploy/images/adsp-sc589-mini/u-boot-proper-sc589-mini.elf /tftpboot
   $ cp tmp/deploy/images/adsp-sc589-mini/u-boot-spl-sc589-mini.elf /tftpboot
   $ cp tmp/deploy/images/adsp-sc589-mini/stage1-boot.ldr /tftpboot
   $ cp tmp/deploy/images/adsp-sc589-mini/stage2-boot.ldr /tftpboot

Before installing the software on to the development board, ensure that the following cables are connected:

-  Board connected to network via ethernet cable using J14 connector.
-  Board connected to host PC using USB micro cable, connected to USB/UART port on the development board
-  Board connected to the ICE 1000 or ICE 2000 via the DEBUG port on the board
-  ICE is also connected to host PC via USB mini cable

|image1| |image2|

-  **ADSP-SC589-EZKIT only:** The BOOT MODE selector on the board should be turned to "0".

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc589-ezkit_boot_selector.jpg
   :width: 400px

-  **ADSP-SC589-MINI only:** The BOOT MODE jumper on the board should be removed.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc589-mini_boot_selector_0.jpg
   :width: 400px

The console output from U-Boot and later on Linux will appear on the USB serial port configured in minicom earlier so open up minicom.

::

   ;''**Terminal1: minicom**''
   :<code bash>$ sudo minicom </code>

In a separate console launch OpenOCD and connect to the development board

::

   ;''**Terminal2: OpenOCD**''
   :<code bash>

$ sdk_usr=/opt/adi-distro-glibc/3.0.0/sysroots/x86_64-adi_glibc_sdk-linux/usr/ $ $sdk_usr/bin/openocd -f $sdk_usr/share/openocd/scripts/interface/<ICE>.cfg -f $sdk_usr/share/openocd/scripts/board/adspsc589_ezbrd.cfg</code> Where <ICE> should be replaced with ice1000 or ice2000 depending on your hardware. When successful you should see a message similar to the console output below

.. code:: bash

       Open On-Chip Debugger (PKGVERSION)  OpenOCD 0.10.0-g40378454d (2023-04-05-10:35)
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

In a third console window launch GDB and type ``target extended-remote :3333``. This will make GDB to connect to the gdbserver on the local host using port 3333. Then, load the spl file into RAM by typing ``load`` and run it by typing ``c``. Hit Ctrl+C to interrupt thereafter.

::

   ;''**Terminal3: GDB (sc589-ezkit)**''
   : <code bash>

$ cd /tftpboot $ /opt/adi-distro-glibc/3.0.0/sysroots/x86_64-adi_glibc_sdk-linux/usr/bin/arm-adi_glibc-linux-gnueabi/arm-adi_glibc-linux-gnueabi-gdb u-boot-spl-sc589-ezkit.elf ... Reading symbols from u-boot-spl-sc589-ezkit.elf...done. (gdb) target extended-remote :3333 Remote debugging using :3333 0x00004884 in ?? () (gdb) load Loading section .text, size 0x9f2c lma 0x20080000 Loading section .rodata, size 0x1198 lma 0x20089f2c Loading section .dtb.init.rodata, size 0x12c0 lma 0x2008b0d0 Loading section .data, size 0x514 lma 0x2008c390 Loading section .u_boot_list, size 0xa50 lma 0x2008c8a4 Start address 0x20080000, load size 53992 Transfer rate: 30 KB/sec, 7713 bytes/write. (gdb) c Continuing. ^C Program received signal SIGINT, Interrupt. </code>

::

   ;''**Terminal3: GDB (sc589-mini)**''
   : <code bash>

$ cd /tftpboot $ /opt/adi-distro-glibc/3.0.0/sysroots/x86_64-adi_glibc_sdk-linux/usr/bin/arm-adi_glibc-linux-gnueabi/arm-adi_glibc-linux-gnueabi-gdb u-boot-spl-sc589-mini.elf ... Reading symbols from u-boot-spl-sc589-mini.elf...done. (gdb) target extended-remote :3333 Remote debugging using :3333 0x00004884 in ?? () (gdb) load Loading section .text, size 0x9f2c lma 0x20080000 Loading section .rodata, size 0x1198 lma 0x20089f2c Loading section .dtb.init.rodata, size 0x12c0 lma 0x2008b0d0 Loading section .data, size 0x514 lma 0x2008c390 Loading section .u_boot_list, size 0xa50 lma 0x2008c8a4 Start address 0x20080000, load size 53992 Transfer rate: 30 KB/sec, 7713 bytes/write. (gdb) c Continuing. ^C Program received signal SIGINT, Interrupt. </code>

You will see a message on Terminal 1 running minicom, informing you that you can now load U-Boot Proper

::

   ;''**Terminal1: minicom**''
   :<code bash>U-Boot SPL 2020.10 (Mar 16 2023 - 13:07:24 +0000)

ADI Boot Mode: 0x0 (JTAG/BOOTROM) SPL execution has completed. Please load U-Boot Proper via JTAG </code>

Now, load U-Boot Proper into RAM.

::

   ;''**Terminal3: GDB (sc589-ezkit)**''
   :

.. code:: bash

   (gdb) load u-boot-proper-sc589-ezkit.elf
   Loading section .text, size 0x3a8 lma 0xc2200000
   Loading section .text_rest, size 0x48bd8 lma 0xc22003c0
   Loading section .rodata, size 0x1037d lma 0xc2248f98
   Loading section .hash, size 0x18 lma 0xc2259318
   Loading section .dtb.init.rodata, size 0x17f0 lma 0xc2259330
   Loading section .data, size 0x2410 lma 0xc225ab20
   Loading section .got.plt, size 0xc lma 0xc225cf30
   Loading section .u_boot_list, size 0x170c lma 0xc225cf3c
   Loading section .rel.dyn, size 0xa3b0 lma 0xc225e648
   Loading section .dynsym, size 0x30 lma 0xc22689f8
   Loading section .dynstr, size 0x1 lma 0xc2268a28
   Loading section .dynamic, size 0x90 lma 0xc2268a2c
   Loading section .gnu.hash, size 0x18 lma 0xc2268abc
   Start address 0xc2200000, load size 428726
   Transfer rate: 31 KB/sec, 11587 bytes/write.
   (gdb) c
   Continuing.

::

   ;''**Terminal3: GDB (sc589-mini)**''
   :

.. code:: bash

   (gdb) load u-boot-proper-sc589-mini.elf
   Loading section .text, size 0x3a8 lma 0xc2200000
   Loading section .text_rest, size 0x48bd8 lma 0xc22003c0
   Loading section .rodata, size 0x1037d lma 0xc2248f98
   Loading section .hash, size 0x18 lma 0xc2259318
   Loading section .dtb.init.rodata, size 0x17f0 lma 0xc2259330
   Loading section .data, size 0x2410 lma 0xc225ab20
   Loading section .got.plt, size 0xc lma 0xc225cf30
   Loading section .u_boot_list, size 0x170c lma 0xc225cf3c
   Loading section .rel.dyn, size 0xa3b0 lma 0xc225e648
   Loading section .dynsym, size 0x30 lma 0xc22689f8
   Loading section .dynstr, size 0x1 lma 0xc2268a28
   Loading section .dynamic, size 0x90 lma 0xc2268a2c
   Loading section .gnu.hash, size 0x18 lma 0xc2268abc
   Start address 0xc2200000, load size 428726
   Transfer rate: 31 KB/sec, 11587 bytes/write.
   (gdb) c
   Continuing.

At this point U-Boot will now be running in RAM on your target board. You should see U-Boot booting in the minicom console (Terminal 1). Press a key to interrupt the boot process before the countdown terminates:

::

   ;''**Terminal1: minicom (sc589-ezkit)**''
   :  <code bash>

U-Boot 2020.10 (Mar 16 2023 - 13:07:24 +0000)

CPU: ADSP ADSP-SC589-0.1 (spi flash boot) Detected Revision: 1.1 Model: ADI sc589-ezkit DRAM: 224 MiB WDT: Not found! MMC: mmc0@31010000: 0 Loading Environment from SPIFlash... SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB OK In: serial@0x31003000 Out: serial@0x31003000 Err: serial@0x31003000 Net: eth0: eth0 Hit any key to stop autoboot: 0 => </code>

::

   ;''**Terminal1: minicom (sc589-mini)**''
   :  <code bash>

U-Boot 2020.10 (Mar 16 2023 - 13:07:24 +0000)

CPU: ADSP ADSP-SC589-0.1 (spi flash boot) Detected Revision: 1.1 Model: ADI sc589-mini DRAM: 224 MiB WDT: Not found! MMC: mmc0@31010000: 0 Loading Environment from SPIFlash... SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB OK In: serial@0x31003000 Out: serial@0x31003000 Err: serial@0x31003000 Net: eth0: eth0 Hit any key to stop autoboot: 0 => </code>

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

   => setenv ipaddr <ADDR>

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
   TFTP from server 192.168.1.223; our IP address is 192.168.1.217
   Filename 'stage1-boot.ldr'.
   Load address: 0xc2000000
   Loading: ####
            2.5 MiB/s
   done
   Bytes transferred = 54068 (d334 hex)
   SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
   device 0 offset 0x0, size 0xd334
   SF: 54068 bytes @ 0x0 Written: OK
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 192.168.1.223; our IP address is 192.168.1.217
   Filename 'stage2-boot.ldr'.
   Load address: 0xc2000000
   Loading: ##############################
            3.4 MiB/s
   done
   Bytes transferred = 429012 (68bd4 hex)
   SF: Detected w25q128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
   device 0 offset 0x20000, size 0x68bd4
   SF: 429012 bytes @ 0x20000 Written: OK

In order to store the ``serverip`` and the DHCP or otherwise assigned IP address of the board and have them available on next boot, you can run the following command:

.. code:: bash

   => saveenv
   Saving Environment to SPIFlash... Erasing SPI flash...Writing to SPI flash...done
   OK

   | At this point the U-Boot binary is stored in flash. You can now disconnect the ICE-1000 or ICE-2000 from the development board and make sure to switch the BMODE to position 1. You will only need to reconnect this if your board fails to boot and you need to re-follow these instructions.

Booting Linux
-------------

Booting Linux from SPI Flash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADSP-SC589-EZKIT comes equipped with 16 MiB of SPI Flash. There's the option of building the ``adsp-sc5xx-tiny`` image, after changing the Libc implementation from the default GNU to musl, to further reduce the image's size. Follow the guide in :doc:`Boot from SPI Flash on the SC58x & SC573 </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/boot-flash-sc58x-573>`.

The ADSP-SC589-MINI (Board Revision: 1.5 or later) comes with 64 MiB of SPI Flash. This means that it can store not only the ``adsp-sc5xx-tiny`` image, but the ``adsp-sc5xx-minimal`` one, too. This image does not need the Libc implementation to be changed, and is more feature-rich compared to ``adsp-sc5xx-tiny``. The next section will cover this, among the rest of the boot modes.

Booting the minimal image from SPI Flash (MINI only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The U-Boot console is used to copy U-Boot (SPL and Proper), the minimal root filesystem image and the fitImage (which contains the kernel image and dtb file) into RAM and then write them to Flash. Copy the required files from <BUILD DIR>/tmp/deploy/images to your /tftpboot directory.

.. code:: bash

   $ cp tmp/deploy/images/adsp-sc589-mini/stage1-boot.ldr /tftpboot/
   $ cp tmp/deploy/images/adsp-sc589-mini/stage2-boot.ldr /tftpboot/
   $ cp tmp/deploy/images/adsp-sc589-mini/fitImage /tftpboot/
   $ cp tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-minimal-adsp-sc589-mini.jffs2 /tftpboot

Next, you have to change a U-Boot environment variable in order to flash the minimal image's root filesystem:

.. code:: bash

   => setenv jffs2file adsp-sc5xx-minimal-adsp-sc589-mini.jffs2

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

Now, by running ``update_spi``, the minimal image kernel and root filesystem will be copied to flash. You should see output similar to the following.

.. code:: bash

   => run update_spi
   PHY 0x00: OUI = 0x80028, Model = 0x23, Rev = 0x01, 100baseT, FDX
   Speed: 1000, full duplex
   BOOTP broadcast 1
   DHCP client bound to address 10.37.33.113 (90 ms)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   SF: 67108864 bytes @ 0x0 Erased: OK
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'stage1-boot.ldr'.
   Load address: 0x82000000
   Loading: ######
            2.9 MiB/s
   done
   Bytes transferred = 80032 (138a0 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x0, size 0x138a0
   SF: 80032 bytes @ 0x0 Written: OK
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'stage2-boot.ldr'.
   Load address: 0x82000000
   Loading: #################################
            4.7 MiB/s
   done
   Bytes transferred = 475344 (740d0 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x20000, size 0x740d0
   SF: 475344 bytes @ 0x20000 Written: OK
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'fitImage'.
   Load address: 0x82000000
   Loading: #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################

            5 MiB/s
   done
   Bytes transferred = 6678526 (65e7fe hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x100000, size 0x65e7fe
   SF: 6678526 bytes @ 0x100000 Written: OK
   Speed: 1000, full duplex
   Using eth0 device
   TFTP from server 10.37.33.116; our IP address is 10.37.33.113
   Filename 'adsp-sc5xx-minimal-adsp-sc589-mini.jffs2'.
   Load address: 0x82000000
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
            #####################################################
            5 MiB/s
   done
   Bytes transferred = 21757952 (14c0000 hex)
   SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   device 0 offset 0x900000, size 0x14c0000
   SF: 21757952 bytes @ 0x900000 Written: OK
   Saving Environment to SPIFlash... SF: Detected is25lx256 with page size 256 Bytes, erase size 128 KiB, total 32 MiB
   Erasing SPI flash...Writing to SPI flash...done
   OK
   =>

The U-Boot image, root filesystem and Linux kernel are now stored in SPI Flash. Place the BOOT MODE jumper to **position 1** and press the RESET button, the board should boot into Linux.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc589-mini_boot_selector_1.jpg
   :width: 400px

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

   adsp-sc589-mini login: root
   Password: adi
   root@adsp-sc589-mini:~# 

The username is **root** and the password is **adi**.

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
   $ sudo cp tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-ramdisk-adsp-sc589-ezkit.cpio.xz ~/mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp tmp/deploy/images/adsp-sc589-ezkit/sc589-ezkit.dtb ~/mnt/boot/
   $ sudo cp tmp/deploy/images/adsp-sc589-ezkit/fitImage ~/mnt/boot/
   $ sudo tar -xf tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-minimal-adsp-sc589-ezkit.tar.xz -C ~/mnt
   $ sudo umount ~/mnt

or

.. code:: bash

   $ mkdir ~/mnt
   $ sudo mount -t ext2 /dev/sdb1 ~/mnt
   $ sudo mkdir ~/mnt/boot
   $ sudo cp tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-ramdisk-adsp-sc589-mini.cpio.xz ~/mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp tmp/deploy/images/adsp-sc589-mini/sc589-mini.dtb ~/mnt/boot/
   $ sudo cp tmp/deploy/images/adsp-sc589-mini/fitImage ~/mnt/boot/
   $ sudo tar -xf tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-minimal-adsp-sc589-mini.tar.xz -C ~/mnt
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

Booting Linux from USB Mass Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Formating USB stick
^^^^^^^^^^^^^^^^^^^

Frist step is to format USB stick to U-Boot supported formats.

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

Writing kernel and rootfs image to USB stick
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

   $ mkdir ~/mnt
   $ sudo mount -t ext4 /dev/sdb1 ~/mnt
   $ sudo mkdir ~/mnt/boot
   $ sudo cp tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-ramdisk-adsp-sc589-ezkit.cpio.xz ~/mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp tmp/deploy/images/adsp-sc589-ezkit/fitImage ~/mnt/boot/
   $ sudo umount ~/mnt

or for SC598-mini

.. code:: bash

   $ mkdir ~/mnt
   $ sudo mount -t ext4 /dev/sdb1 ~/mnt
   $ sudo mkdir ~/mnt/boot
   $ sudo cp tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-ramdisk-adsp-sc589-mini.cpio.xz ~/mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp tmp/deploy/images/adsp-sc589-mini/fitImage ~/mnt/boot/
   $ sudo umount ~/mnt

.. _booting-linux-from-usb-mass-storage-1:

Booting Linux from USB Mass Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To boot from ADSP-SC589-EZKIT run this commands in u-boot

.. code:: bash

   setenv usbload 'ext4load usb 0 ${initramaddr} /boot/${initramfile}; ext4load usb 0 ${loadaddr} /boot/${imagefile};'
   setenv usbboot 'usb start; run usbload; run ramargs; bootm ${loadaddr} ${initramaddr};'
   run usbboot

To boot from ADSP-SC589-MINI there is need to disable emac0 device in u-boot device tree, as USB and ethernet port share same pin and can't run simultaneously. Inside Yocto directory type

.. code:: bash

   devtool modify u-boot-adi

edit build/workspace/sources/u-boot-adi/arch/arm/dts/sc589-mini.dts by adding

.. code:: bash

   &emac0 {
       status="disable";
   };

To rebuild U-boot after modifications

.. code:: bash

   devtool build u-boot-adi

Booting rootfs from USB Mass Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the step how to setup USB stick in chapter above. Set environment variables in U-boot

.. code:: bash

   setenv usbargs 'setenv bootargs root=/dev/sda1 rw rootfstype=ext4 rootwait earlycon=adi_uart,0x31003000 console=ttySC0,115200'
   setenv usbload 'ext4load usb 0 ${loadaddr} /boot/${imagefile};'
   setenv usbboot 'usb start; run usbload; run usbargs; bootm ${loadaddr};'

And type to boot

.. code:: bash

   run usbboot

Now the rootfs is set to your USB stick and amount of space equals of size of partition on USB stick.

|

| ==== Booting Linux Using TFTP ==== In order to boot Linux, the TFTP server should be setup as :doc:`above </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc589>` and a copy of the kernel image should be copied into the **/tftpboot** directory.

.. code:: bash

   $ cp tmp/deploy/images/adsp-sc589-ezkit/fitImage /tftpboot

or

.. code:: bash

   $ cp tmp/deploy/images/adsp-sc589-mini/fitImage /tftpboot

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
| If you are using the ADSP-SC589-EZKIT with the full image (you ran 'bitbake adsp-sc5xx-full'):

.. code:: bash

   $ sudo tar -xf tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-full-adsp-sc589-ezkit.tar.xz -C /romfs

Or if you are using the ADSP-SC589-EZKIT with the minimal image (you ran 'bitbake adsp-sc5xx-minimal'):

.. code:: bash

   $ sudo tar -xf tmp/deploy/images/adsp-sc589-ezkit/adsp-sc5xx-minimal-adsp-sc589-ezkit.tar.xz -C /romfs

Or if you are using the ADSP-SC589-MINI with the full image (you ran 'bitbake adsp-sc5xx-full'):

.. code:: bash

   $ sudo tar -xf tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-full-adsp-sc589-mini.tar.xz -C /romfs

Or if you are using the ADSP-SC589-MINI with the minimal image (you ran 'bitbake adsp-sc5xx-minimal'):

.. code:: bash

   $ sudo tar -xf tmp/deploy/images/adsp-sc589-mini/adsp-sc5xx-minimal-adsp-sc589-mini.tar.xz -C /romfs

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

   adsp-sc589-ezkit login: root
   Password: adi
   root@adsp-sc589-ezkit:~#

The default username is **root** and the password is **adi**.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc589-ezkit_overview.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc589-mini_overview.jpg
   :width: 400px
