Fastboot Example
================

The fastboot example is a proof of concept system that has been configured to boot a minimal Linux platform as quickly as possible. The system constraints are:

-  Must boot from flash device
-  Use a network application to establish a connection to the development board
-  Must indicate successful connection by toggling LED
-  SHARC core wakeup and audio playback triggered by Linux
-  Must play audio on A2B daughterboard controlled by SHARC core

.. note::

   Current Status: This project is in early development, work is still in progress on this project.


System Requirements
-------------------

The demo is currently supported using the **ADSP-SC589-MINI** development board and the **EVAL-AD2428WB1BZ** A2B board.

A logic probe can be used to measure performance points by attaching it to the LEDs on the board.

System Concept
--------------

U-Boot is configured to run in Falcon mode to provide a fast boot time. Once booted, Linux uses remoteproc to enable the SHARC cores. Activity on the SHARC core1 is controlled by a fastboot server application (fastboot_server.c) running under Linux on the development board. The server waits for a connection to be established over a TCP socket from a Node.js web-app running on the host PC (on the same network). Once the connection has been established the server application turns on an LED, reads an audio file from a mounted MMC into mapped memory which is accessible by the SHARC core1. Linux raises an interrupt to let the SHARC app know when audio data is available and SHARC raises an interrupt to let Linux know when it has finished reading the data. SHARC then begins playing the audio via the A2B device. The web-app provides a GUI which lists the available files and can be used to select a file to be played. Alternatively push button 2 can be used to cycle through the files.

Changes from the Release Yocto Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The concept changes the default Yocto Linux system to optimize boot time performance.

-  Boot U-Boot from flash
-  Modify Yocto to build **uImage** file which contains compressed Linux kernel and minimal filesystem
-  uImage stored in flash and extracted by U-Boot
-  Remove unnecessary drivers and applications from the minimal root filesystem
-  Change U-Boot to run in Falcon boot mode. A small minimal footprint U-Boot bootloader is invoked. If PB1 push button is depressed during reset, the full U-Boot application will be loader.
-  Remove console output during Linux boot
-  Remoteproc loads minimal SHARC application during boot
-  Board LEDs configured to indicate progress
-  UIO used by Linux to receive interrupts from SHARC

System Setup
~~~~~~~~~~~~

| |image1|
| Connect the A2B EVAL-AD2428WB1BZ from connector J7 to the slave port on the SC589-Mini as shown in the photo above. Connect headphones or a speaker to EVAL-AD2428WB1BZ (hp out). Connect the SC589-Mini from the USB/UART port to your host PC (USB). Connect the SC589-Mini to your network with an ethernet cable (directly to your router or to your host PC if configured correctly). When flashing U-Boot for the first time, the SC589-Mini will need connected from the debug port to an ICE1000 which will need to be connected to your host PC (USB). A micro sd card formatted as ext is required for hosting the audio files.

Setting Up Your Host PC
-----------------------

The demo is currently supported on host PCs running **Ubuntu 18.04 LTS 64-bit**.

Install Linux Add-In Toolchain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The demo currently requires the Linux add-in and CrossCore Embdded Studio to build U-Boot:

::

   wget https://download.analog.com/tools/LinuxAddInForCCES/Releases/Release_1.3.1/adi-LinuxAddinForCCES-linux-x86-1.3.1.deb
   wget http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.8.3/adi-CrossCoreEmbeddedStudio-linux-x86-2.8.3.deb
   sudo dpkg -i ./adi-CrossCoreEmbeddedStudio-linux-x86-2.8.3.deb
   sudo dpkg -i ./adi-LinuxAddinForCCES-linux-x86-1.3.1.deb

Next we install the 32-bit libz package to allow to the 32-bit toolchain to function on the 64-bit host:

::

   sudo apt-get install lib32z1

Installing Required System Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have not previously configured your host PC to build the Yocto Linux product you will need to install the following packages:

::

   sudo apt-get update
   sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm u-boot-tools openssl curl tftpd-hpa python

You will also require Node.js to run the web-app:

::

   sudo apt-get install nodejs npm

Configuring TFTP Service
~~~~~~~~~~~~~~~~~~~~~~~~

If you have not previously configured your host PC to build the Yocto Linux product you will need to configure the tftp service:

::

   sudo vi /etc/default/tftpd-hpa

   #Replace the existing file with the following
   TFTP_USERNAME="tftp"
   TFTP_DIRECTORY="/tftpboot"
   TFTP_ADDRESS="0.0.0.0:69"
   TFTP_OPTIONS="--secure"
   #End of File

   sudo mkdir /tftpboot
   sudo chmod 777 /tftpboot
   sudo service tftpd-hpa restart

Configure Minicom
~~~~~~~~~~~~~~~~~

If you have not previously configured your host PC to build the Yocto Linux product you will need to configure minicom:

::

   sudo apt-get install minicom
   sudo minicom -s

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
        Set Bps/Par/Bits to 57600 8N1
        Set Hardware Flow Control to No
        
        Close the Serial port setup option by press Esc
    Select Save setup as dfl
    Select Exit

Installing the Sources
----------------------

The example is fully contained in the Analog Devices Yocto Linux github repositories. All source code for the example is currently available via the **develop/yocto-1.0.0-fastboot** branch in each repository.

.. important::

   The current version of the demo relies on repositories that are configured to be private. As such you will need to log in to github to clone the repositories. It is recommended that you configure your local git to cache your credentials to avoid the build process failing to check out the code. To cache your credentials you can issue the command **git config --global credential.helper store**. Then clone one of the required repositories. This will prompt you for your username and password which will be cached locally.


To install the sources:

::

   mkdir ~/fastboot
   cd ~/fastboot
   mkdir bin
   curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ./bin/repo
   chmod a+x ./bin/repo
   ./bin/repo init -u https://github.com/sammyarschaviradi/lnxdsp-repo-manifest.git -b develop/fastboot-mvp
   ./bin/repo sync
   source setup-environment -m adsp-sc589-mini

Building the Example
--------------------

.. important::

   The current version of the demo uses the legacy toolchain from the Linux Add-In to build U-Boot. This will be changed at a later date to use the toolchain built by the Yocto framework. Be careful when building U-Boot and the uImage/initramfs that the correct toolchain is used. Instructions below will make this clear.


Building uImage
~~~~~~~~~~~~~~~

Configure the build to use the Yocto internal toolchain by modifying the **conf/local.conf** file:

-  Edit **~/fastboot/build/conf/local.conf**

   -  Ensure that the last line of the file is commented out so that it does **NOT** set **TCMODE**. The last line should be:

::

   # TCMODE = "external-adi"

Next we build the ramdisk and uImage files:

::

   bitbake adsp-sc5xx-ramdisk

Copy the binary files to the Tftp directory:

::

   cp tmp/deploy/images/adsp-sc589-mini/uImage /tftpboot/uImage
   cp tmp/deploy/images/adsp-sc589-mini/sc589-mini.dtb /tftpboot/sc589-mini.dtb

Building U-Boot
~~~~~~~~~~~~~~~

Configure the build to use the Linux add-in toolchain to build U-Boot by modifying the **conf/local.conf** file:

-  Edit **~/fastboot/build/conf/local.conf**

   -  Uncomment the last line of the file so that it sets **TCMODE**. The last line should be:

::

   TCMODE = "external-adi"

Clean out the u-boot components build by the previous commands:

::

   bitbake u-boot -c cleanall
   bitbake u-boot -c clean
   bitbake libtool -c cleanall
   bitbake libtool -c clean

Build U-Boot:

::

   bitbake u-boot

.. tip::

   When the build completes you will see a warning that the ELF binary has relocations in .text. It is OK to ignore this warning


.. warning::

   Copy the u-boot binaries to the TFTP directory **before** building the ramdisk and uImage files


::

   cp tmp/deploy/images/adsp-sc589-mini/u-boot-spl.ldr /tftpboot
   cp tmp/deploy/images/adsp-sc589-mini/init-sc589-mini.elf /tftpboot
   cp tmp/deploy/images/adsp-sc589-mini/u-boot-sc589-mini /tftpboot
   cp tmp/deploy/images/adsp-sc589-mini/u-boot-sc589-mini.bin /tftpboot

Installing to Software on the Board
-----------------------------------

.. tip::

   If you have an older version of U-Boot on your development board, you will need to erase the U-Boot environment on the board. To do this follow the **First Time** instructions below and execute the optional note commands.


Before installing the software on to the development board, ensure that the following cables are connected:

-  Board connected to network via ethernet cable
-  Board connected to host PC using USB mini cable, connected to **USB/UART** port on the development board
-  Board connected to the ICE 1000 or ICE 2000 via the **DEBUG** port on the board
-  ICE is also connected to host PC via USB mini cable

Installing U-Boot on the Board for the First Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install U-Boot on to the board for the first time we need to connect the board to the GDB debugger, load the main U-Boot application into RAM and run this application so that it writes a copy of itself into the board flash.

Open the minicom console, If you can see the output from Minicom after you reset the board, you could skip the section "**Flash U-Boot for the First Time**" below and turn to section "**Flash U-Boot to SPI Flash**" directly.

::

   ;''**Terminal1: minicom**''
   :<code>sudo minicom </code>

::

   ;''**Terminal2: Run OpenOCD**''
   :In a second terminal window launch the OpenOCD and connect to the development board. The  **config file** parameters should be changed if you are using a different interface or target.

::

   cd /opt/analog/cces/2.8.3/ARM/openocd/share/openocd/scripts 
   sudo /opt/analog/cces/2.8.3/ARM/openocd/bin/openocd -f interface/<ICE>.cfg -f target/<TARGET>.cfg

Where **<ICE>** and **<TARGET>** should be replaced.

======= =========
ICE     TARGET
======= =========
ice1000 adspsc58x
ice2000 adspsc57x
======= =========

When success you should see a message similar to the console output below:

::

   Open On-Chip Debugger (Analog Devices CCES 2.9.0 OpenOCD 0.9.0-ga44a178) 0.9.0
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

::

   ;''**Terminal3: Loading U-Boot With GDB**''
   :In a third console window launch GDB and load the U-Boot image to flash:

::

   cd  /tftpboot
   /opt/analog/cces/2.8.3/ARM/arm-none-eabi/bin/arm-none-eabi-gdb u-boot-sc589-mini
   (gdb) target remote :3333
   (gdb) load init-sc589-mini.elf
   (gdb) c 
   <Press Ctrl+C to interrupt the application after 2 seconds>
   (gdb) load
   (gdb) c

::

   :Switch back to the minicom console:

| 
| At this point U-Boot will now be running in RAM on your target board. You should see U-Boot booting in the minicom console. Press a key to interrupt the boot process before the countdown terminates:

::

   ;''**Terminal1: minicom**''
   :<code>

U-Boot 2015.01 ADI-YOCTO-1.0.0 (May 14 2020 - 19:26:23)

CPU: ADSP ADSP-SC589-0.1 (Detected Rev: 1.1) (spi flash boot) VCO: 450 MHz, Cclk0: 450 MHz, Sclk0: 112.500 MHz, Sclk1: 112.500 MHz, DCLK: 450 MHz OCLK: 150 MHz

::

        Watchdog enabled

| I2C: ready DRAM: 224 MiB MMC: SC5XX SDH: 0 SF: Detected IS25LP512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB In: serial Out: serial Err: serial other init Net: dwmac.3100c000 Hit any key to stop autoboot: 0 sc # </code>

Flash U-Boot to SPI Flash
~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   If you have a version of U-Boot installed on to the board from a previous project you will need to erase the U-Boot environment from flash. Execute the following command from the U-Boot prompt:

   
   sf probe 2:1 50000000;sf erase 0x10000 0x2000


Here we use the u-Boot console to TFTP a version of u-Boot into RAM, and then write this application into SPI flash.

In the U-Boot console, configure the board IP address. This can either be a static address or DHCP allocated. For DHCP:

::

    ;''**Terminal1: minicom**''
   :<code>

dhcp </code> The console should report the IP address allocated to the board (you will need to provide this as an argument to the web-app).

If you want to manually assign an IP address:

::

   set ipaddr <ADDR>

Where **<ADDR>** is the IP address you want to assign.

Next, set the serverip variable to the IP address of your host PC where the **TFTP** server is running:

.. tip::

   You can find the IP address of your host Ubuntu machine by executing the **ifconfig** command from the console.


::

   set serverip <SERVERIP>
   save

Where **<SERVERIP>** is the IP address of your host PC. The save command saves the U-Boot environment to flash.

Next, we run the **splupdate** command. This will install U-Boot to the development board flash memory:

::

   run splupdate

You will see output similar to the following:

::

   sc # run splupdate                                                                                                                                                             
   Speed: 1000, full duplex                                                                                                                                                       
   Using dwmac.3100c000 device                                                                                                                                                    
   TFTP from server 192.168.1.71; our IP address is 192.168.1.178                                                                                                                 
   Filename 'u-boot-spl.ldr'.                                                                                                                                                     
   Load address: 0xc2000000                                                                                                                                                       
   Loading: ##                                                                                                                                                                    
            104.5 KiB/s                                                                                                                                                           
   done                                                                                                                                                                           
   Bytes transferred = 23812 (5d04 hex)                                                                                                                                           
   SF: Detected IS25LP512 with page size 256 Bytes, erase size 4 KiB, total 64 MiB, mapped at 60000000                                                                            
   SF: 8192 bytes @ 0x10000 Erased: OK                                                                                                                                            
   SF: 65536 bytes @ 0x0 Erased: OK                                                                                                                                               
   SF: 23812 bytes @ 0x0 Written: OK                                                                                                                                              
   Speed: 1000, full duplex                                                                                                                                                       
   Using dwmac.3100c000 device                                                                                                                                                    
   TFTP from server 192.168.1.71; our IP address is 192.168.1.178                                                                                                                 
   Filename 'u-boot-sc589-mini.bin'.                                                                                                                                              
   Load address: 0xc2000000                                                                                                                                                       
   Loading: ###################                                                                                                                                                   
            560.5 KiB/s                                                                                                                                                           
   done                                                                                                                                                                           
   Bytes transferred = 278244 (43ee4 hex)                                                                                                                                         
   SF: 327680 bytes @ 0x12000 Erased: OK                                                                                                                                          
   SF: 278244 bytes @ 0x12000 Written: OK                                                                                                                                         
   sc #                                     

At this point the U-Boot binary is stored in flash. You can now disconnect the ICE-1000 or ICE-2000 from the development board. You will only need to reconnect this if your board fails to boot and you need to re-install U-Boot from scratch. Updates to U-Boot can be performed using the instructions below.

Controlling the System Boot
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once U-Boot is installed on the board the default behaviour upon power-on or reset is to fast-boot into Linux. To return to the U-Boot command prompt hold down the **PB1** button while pressing the **Reset** button.

Updating U-Boot
~~~~~~~~~~~~~~~

Once U-Boot has been installed on to the board, it can be updated by performing the following steps

-  Remember to copy the new version of the U-Boot files into the **/tftpboot** directory on the host PC
-  While holding down **PB1** press the **Reset** button on the board
-  Press any key to interrupt the U-Boot count down
-  Execute the **run splupdate** command to update U-Boot

Installing the Kernel
~~~~~~~~~~~~~~~~~~~~~

To install the kernel, we first install the uImage file to flash, which contains the kernel and minimal root filesystem. We then write boot arguments to flash. Start by rebooting the board to the U-Boot prompt using the instructions above.

.. tip::

   Sometimes updating U-Boot can erase the U-Boot environment from flash. This will reset the ipaddr and serverip environment variables. If this happens simply update the values and save the environment to flash.


The boot arguments will need altered to add support for receiving interupts from within the Linux user space. Edit the splargs environment variable by typing the command below and then add "uio_pdrv_genirq.of_id=generic-uio" to the end of the variable and press enter, then run "save" to save the environment to flash.

::

   sc # edit splargs
   edit: set bootargs root=/dev/mtdblock2 rw rootfstype=jffs2 clkin_hz=(25000000) console=ttySC0,57600 mem=224M ip=${ipaddr}:${serverip}:${gatewayip}:${netmask}:${hostname}:eth0:off quiet lpj=595968 uio_pdrv_genirq.of_id=generic-uio
   sc # save

Now run kupdate.

::

   run kupdate

You should see output similar to the following:

::

   sc # run kupdate
   Speed: 1000, full duplex
   Using dwmac.3100c000 device
   TFTP from server 192.168.1.71; our IP address is 192.168.1.178
   Filename 'uImage'.
   Load address: 0xc2000000
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
            #########################
            884.8 KiB/s
   done
   Bytes transferred = 13721440 (d15f60 hex)
   SF: Detected IS25LP512 with page size 256 Bytes, erase size 4 KiB, total 64 MiB, mapped at 60000000
   SF: 13762560 bytes @ 0x112000 Erased: OK
   SF: 13721440 bytes @ 0x112000 Written: OK
   Speed: 1000, full duplex
   Using dwmac.3100c000 device
   TFTP from server 192.168.1.71; our IP address is 192.168.1.178
   Filename 'sc589-mini.dtb'.
   Load address: 0xc4000000
   Loading: ##
            592.8 KiB/s
   done
   Bytes transferred = 18817 (4981 hex)
   SF: 65536 bytes @ 0x92000 Erased: OK
   SF: 18817 bytes @ 0x92000 Written: OK
   sc # 
   CTRL-A Z for help | 57600 8N1 | NOR | Minicom 2.7.1 | VT102 | Offline | ttyUSB0                                                                                               

This step may take a while.

Next:

-  **reset the board** while holding down **PB1** to return to the U-Boot prompt.

The next step stores the Linux arguments into flash:

::

   run splexport

This produces output similar to the following:

::

   sc # run splexport
   Speed: 1000, full duplex
   Using dwmac.3100c000 device
   TFTP from server 192.168.1.71; our IP address is 192.168.1.178
   Filename 'uImage'.
   Load address: 0xc2000000
   Loading: T #################################################################
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
            #########################
            649.4 KiB/s
   done
   Bytes transferred = 13721440 (d15f60 hex)
   Speed: 1000, full duplex
   Using dwmac.3100c000 device
   TFTP from server 192.168.1.71; our IP address is 192.168.1.178
   Filename 'sc589-mini.dtb'.
   Load address: 0xc4000000
   Loading: ##
            4.9 KiB/s
   done
   Bytes transferred = 18817 (4981 hex)
   SF: Detected IS25LP512 with page size 256 Bytes, erase size 4 KiB, total 64 MiB, mapped at 60000000
   SF: 262144 bytes @ 0xd2000 Erased: OK
   ## Booting kernel from Legacy Image at c2000000 ...
      Image Name:   Linux-4.19.0-yocto-standard
      Image Type:   ARM Linux Kernel Image (uncompressed)
      Data Size:    13721376 Bytes = 13.1 MiB
      Load Address: c2008000
      Entry Point:  c2008000
      Verifying Checksum ... OK
   ## Flattened Device Tree blob at c4000000
      Booting using the fdt blob at 0xc4000000
      Loading Kernel Image ... OK
      Loading Device Tree to cfe59000, end cfe60980 ... OK
   subcommand not supported
   subcommand not supported
      Loading Device Tree to cfe4e000, end cfe58980 ... OK
   Argument image is now in RAM: 0xcfe4e000

.. important::

   Make note of the address reported on the last line of output above


.. tip::

   Ignore the warnings in the output above reporting subcommand not supported


Finally we update the arguments from RAM to flash. We do this by editting the splargs_update command so that the first hexadecimal value is replaced by the argument address that you made a note of during the previous step. Press enter to save the new string and the run splargs update command:

::

   sc # edit splargs_update
   edit: sf write 0xcfe4e000 0xD2000 0x40000
   sc # run splargs_update
   SF: 262144 bytes @ 0xd2000 Written: OK

Setting Up Your Micro SD card
-----------------------------

The micro sd card needs formatted as ext. First insert the sd card into your host PC and identify the device listed in /dev which is reported to be your micro sd card. The example commands below assume your device is reported to be /dev/mmcblk0. If your host PC has automatically mounted the device then un-mount it with the command below, where <DIRECTORY> is the location the card has been mounted to (this can be identified with the "mount" command).

::

   sudo umount <DIRECTORY>

First format the sd card with fdisk:

::

   $ sudo fdisk /dev/mmcblk0
   /* Create primary partition 1, 256M size*/
   Command (m for help): n

If "All space for primary partitions is in use." then:

::

   Command (m for help): d
   Selected partition 1
   Partition 1 has been deleted.

   Command (m for help): n

Then follow the default options for 1 partition:

::

   Select (default p): p
   Partition number (1-4, default 1): 1
   First sector (2048-3887103, default 2048): PRESS ENTER
   Last sector, +sectors or +size{K,M,G} (2048-3887103, default 3887103): PRESS ENTER

   /* Save partition */
   Command (m for help): w

Once fdisk is closed, your Host PC may mount the SD Card again. If it does, un-mount it following the instructions above. Now format the card as ext (this may take a moment):

::

   $ sudo mkfs /dev/mmcblk0p1
   $ sudo mount /dev/mmcblk0p1 /mnt

Now copy the media files from the examples repo you cloned earlier:

::

   cp -r ~/fastboot/lnxdsp-exaples/fastboot/audio/* /mnt
   sudo umount /mnt

Now place the micro sd card in the slot on the SC589-Mini.

Running the Demo
----------------

To run the demo, boot the board into Linux by pressing pushbutton 1. The output should be as below:

::

   U-Boot SPL 2015.01 ADI-YOCTO-1.0.0-g7f38d49 (Mar 31 2021 - 13:20:49)
   IP-Config: Gateway not on directly connected network
   Warning: unable to open an initial console.
   starting pid 373, tty '/dev/ttySC0': '/bin/sh'
   / # 

The fastboot-listener app should now be running and waiting on a TCP socket connection from the web-app. To run the web app, on your host pc change to the web-app's directory and start the node app:

::

   cd ~/fastboot/lnxdsp-examples/fastboot/web-app
   npm install --global http-server
   ./start-host.sh <ADDR>

Where **<ADDR>** is the IP address you assigned earlier to the board. You should then hear the first file being played through the headphones and see something similar in the console as below:

::

    ./start-host.sh 10.100.4.50
   Server listening on 8000
   connected!
   received message from fastboot server: {"files": ["Intro4.wav", "Intro1.wav", "Intro2.wav", "Intro3.wav", "Intro5.wav", "Intro6.wav", "Intro6.mp3"]}
   Starting up http-server, serving ./client/
   Available on:
     http://127.0.0.1:8080
     http://10.100.4.51:8080
     http://192.168.0.39:8080
   Unhandled requests will be served from: http://0.0.0.0:8000
   Hit CTRL-C to stop the server

You should then be able to navigate to one of the addresses listed serving "./client" (that is, one of the addresses on port 8080, not port 8000) from your browser where you should see a list of the available files.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/examples/fastboot-system-setup-1.jpg
   :width: 800px
