:doc:`Click here to return to the A2B Raspberry Pi User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi>`

Building the Kernel and Running Application
===========================================

To build the kernel locally on the Raspberry Pi 4, follow the appropriate steps to download, compile, and install it for optimal performance.

.. note::

   If using a system with an encryption mechanism, ensure a LAN connection between the system and the Raspberry Pi for file transfers, as the build may fail due to encryption issues. We recommend using *scp* commands for secure transfers over the LAN connection.


-  Flash the Raspberry Pi OS to the SD card using the following link: :doc:`Raspberry Pi4 </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi/raspberrypiboard>`
-  Boot the Raspberry Pi by inserting the flashed SD card, connecting the power supply, and ensuring the mouse, keyboard, and monitor are properly connected. Alternatively, you can use SSH to communicate with the Raspberry Pi. For SSH setup, refer to the following link: `SSH Configuration <https://www.raspberrypi.com/documentation/computers/remote-access.html#ssh>`__.
-  Ensure that the system time is synchronized, as discrepancies may cause errors during the build process. If the time is not in sync, manually set it using the command: ``sudo date -s 'yyyy-mm-dd hh:mm:ss'``
-  Ensure that the system time is synchronized and that there is an active internet connection to access the necessary sources. Install Git and the build dependencies with the following commands: ``sudo apt update
   sudo apt install git
   sudo apt install bc bison flex libssl-dev make``
-  Clone the ADI Linux kernel repository with the rpi-5.15.y branch using the following command: ``git clone -b rpi-5.15.y https://github.com/analogdevicesinc/linux.git``
-  For the Raspberry Pi 4 with the default 64-bit build configuration, navigate to the linux directory and configure the build with the following commands: ``cd linux
   KERNEL=kernel8
   make bcm2711_defconfig``
-  To distinguish the new kernel from the upstream kernel, adjust the LOCALVERSION setting by modifying the .config file to include a custom version string. Change the following line: ``CONFIG_LOCALVERSION="-v8-MY_CUSTOM_KERNEL"``
-  Build the ADI Linux kernel by running: ``make –j4 Image.gz modules dtbs``

.. note::

   The build process may take some time to complete.


-  Install the kernel and modules with the following commands:``sudo make modules_install
   sudo cp arch/arm64/boot/dts/broadcom/*.dtb /boot/firmware/
   sudo cp arch/arm64/boot/dts/overlays/*.dtb* /boot/firmware/overlays/
   sudo cp arch/arm64/boot/dts/overlays/README /boot/firmware/overlays/
   sudo cp arch/arm64/boot/Image.gz /boot/firmware/$KERNEL.img``
-  Ensure that the config.txt file located in /boot/firmware/ is updated with the following settings: ``dtparam=i2s=on
   dtoverlay=rpi-ad242x``

.. note::

   The Raspberry Pi uses a configuration file instead of the BIOS you would expect to find on a conventional PC. The system configuration parameters, which would traditionally be edited and stored using a BIOS, are stored instead in an optional text file named config.txt. This is read by the GPU before the ARM CPU and Linux are initialized. It must therefore be located on the first (boot) partition of your SD card, alongside bootcode.bin and start.elf. This file is normally accessible as /boot/config.txt from Linux, and must be edited as the root user.


-  Reboot the Raspberry Pi to apply the changes.\ ``sudo reboot``
-  After rebooting, check the connected I2C devices with the following command: ``i2cdetect –y 1``\ The AD2428 Mini should be detected as an I2C device. In this scenario, 0x6C and 0x6D are the I2C addresses of the connected devices with the Raspberry Pi 4.\

|image1|

-  In Terminal 1, run aplay on the corresponding AD242x card, which can be identified by running *aplay –l* and *arecord -l*. For example, as shown in image below, the AD2428 Mini should be detected as follows:

|image2|

   -  PLAYBACK device: Card 1, Device 0

      -  CAPTURE device: Card 1, Device 1

-  In Terminal 2, run the aplay command on the AD24xx card, specifically Card 0 and Device 0, as shown in below image. This step provides BCLK and FS to the AD2428 Mini node, which is necessary for the discovery process to succeed.\


|image3|

.. note::

   The hw:Card#,Device# values for the command are derived from the aplay -l listing, as shown in above steps image.


-  The libasound2-dev package, which provides the necessary development files for ALSA, must be installed.\ ``sudo apt update 
   sudo apt install libasound2-dev:armhf``
-  The customer needs to create their application, implement the appropriate PAL (Platform Abstraction Layer) functions, integrate the A2B stack into the repository, and create a Makefile to build the application. Refer to the following link to build the A2B application on the custom platform: :doc:`Building an A2B Application on a custom platform </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>`.
-  In the Makefile, the correct path for the ALSA library needs to be provided, whether using a 32-bit or 64-bit toolchain. Ensure that the appropriate library path is specified based on the architecture.
-  21. If building with a 32-bit toolchain, the following CC and AR can be added in the Makefile:``CC = arm-linux-gnueabihf-gcc
     AR = arm-linux-gnueabihf-ar``
-  If building with a 64-bit toolchain, the following CC and AR can be added in the Makefile:``CC = aarch64-linux-gnu-gcc
     AR = aarch64-linux-gnu-ar``
-  If building with a 32-bit toolchain, the following changes need to be made in conf.h located at cd /opt/analog/a2b-software/19.4.4/Target/examples/demo/a2b-linux/a2b-rpi4-linux/a2b-app-linux_Core0/a2bstack-pal/platform/a2b/:``#define A2B_CONF_MEMORY_ALIGNMENT           (4u)
     #define A2B_CONF_POINTER_SIZE               (32u)``
-  If building with a 64-bit toolchain, the following changes need to be made in conf.h located at cd /opt/analog/a2b-software/19.4.4/Target/examples/demo/a2b-linux/a2b-rpi4-linux/a2b-app-linux_Core0/a2bstack-pal/platform/a2b/:``#define A2B_CONF_MEMORY_ALIGNMENT           (8u)
     #define A2B_CONF_POINTER_SIZE               (64u)``
-  Clean the repository: ``sudo make -f <MakeFile> clean``
-  Build the repository: ``sudo make -f <MakeFile>``

.. note::

   Replace <MakeFile> with the appropriate Makefile created for the application.


-  Run the A2B application with sudo permissions using the following command:``Sudo ./<Builded Application>``

.. note::

   Make sure to run the aplay or arecord command mentioned in above steps to enable BCLK and FS to the AD2428 Mini.


-  Discovery should occur as shown in below image, and downstream audio will be available at Sub node 1's Headphone OUT.\



|image4|

.. note::

   This has been tested on a Raspberry Pi 4 with Raspberry Pi OS 64-bit.


.. note::

   The *-dv* option is used to specify debug and verbose logging during the execution of the application. This causes additional information pertaining to the a2b interrupts to be displayed on the console.


-  To verify Upstream Audio at RPi’s Headphones, provide Audio IN at Sub Node 1. Record on Card 1, Device 1 (ad242x) interface of RPi and play on Card 0, Device 0 (Headphones) as shown in below image.\



|image5|

.. note::

   hw:1,1 is derived from ‘arecord -l’ command and hw:0,0 derived from ‘aplay -l’


**PREV :** :doc:`Setup Details </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi/setupdetails>` **NEXT :** :doc:`DTS Overlay </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi/dtsoverlay>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2braspberrypi/i2c_detect.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2braspberrypi/arecord_aplay.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2braspberrypi/aplay-d.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2braspberrypi/ouput_disc.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2braspberrypi/audio_check.png
