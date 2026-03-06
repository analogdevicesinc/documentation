Building for Raspberry PI
=========================

The Analog Devices kernel can be built to run on the Raspberry PI boards. Unfortunately, these changes are not in master, because they diverge too much (at this point in time) from the changes in both Xilinx & ADI kernel.

Because of this, there are special branches in the repository that should be built to run on the Raspberry PI. They contain several drivers that are not upstreamed yet. These are mostly used for internal testing, and they also contain device-tree overlays for some of these drivers.

.. note::

   The Raspberry PI branches do not contain all of the changes in master. They contain only a set of them, typically for simple ADCs & DACs. The more complex drivers are in master and are typically tested/running on Xilinx & Intel boards using FPGA parts. These FPGA parts are needed for some reference designs/boards supported by Analog Devices.


The Raspberry PI branches are:

-  :git-linux:`tree/rpi-4.9.y` - this is an older branch, when Raspberry PI's default kernel version was at 4.9 ; it's kept around for some older boards/setups
-  :git-linux:`tree/rpi-5.10.y` - the current default Raspberry PI branch, also the official version of Raspbian at this point in time
-  There maybe be a few other branches that start with **rpi-xxx** ; these should not be used, they will be removed in the future, and were used to test things sometime in the past.

Initial setup
-------------

The initial setup is to get an SD-card image from here: https://www.raspberrypi.org/downloads/raspbian/ It does not matter which distribution is used/preferred.

Instructions on writing to SD-card are here: https://www.raspberrypi.org/documentation/installation/installing-images/README.md

At the time of this writing Raspbian's kernel version is 4.14.

Getting the ADI kernel
----------------------

::

   git clone https://github.com/analogdevicesinc/linux
   git checkout rpi-4.14.y

Building the ADI kernel - manual cross-compiling
------------------------------------------------

Get a toolchain for cross-compiling.

::

   git clone https://github.com/raspberrypi/tools

Get an ARM compiler for cross-compiling for Pi 3.

::

   ARCH=arm make adi_bcm2709_defconfig
   ARCH=arm CROSS_COMPILE=<path-to-arm-toolchain> make

For Pi 4.

::

   ARCH=arm make adi_bcm2711_defconfig
   ARCH=arm CROSS_COMPILE=<path-to-arm-toolchain> make

For Pi Zero, Pi Zero 2.

::

   ARCH=arm make adi_bcmrpi_defconfig
   ARCH=arm CROSS_COMPILE=<path-to-arm-toolchain> make

Building the ADI kernel - script method
---------------------------------------

Download this script (and make it executable): :git-wiki-scripts:`linux/build_rpi_kernel_image`.sh

Run it:

::

   ./build_rpi_kernel_image.sh linux

.. note::

   The linux directory in the above example is optional. If unspecified, a **linux-adi** directory will be cloned


Adding the generated file on the SD-card
----------------------------------------

First backup the **kernel7.img** file on the SD-card.

The generated **arch/arm/boot/zImage** file should be copied to the /boot to overwrite the **kernel7.img** (or kernel7l.img for Pi4+, kernel.img for Pi Zero/Pi Zero 2).

Any drivers built as modules must be installed onto the rootfs:

::

   make ARM=arm CROSS_COMPILE=<toolchain> INSTALL_MOD_PATH=< path to SD card rootfs> modules_install

.. important::

   Always remember to run **sudo sync** or un-mount the SD-card safely so that whatever is copied on it, actually gets flushed to it.


Customizing the kernel/adding-drivers
-------------------------------------

For Raspberry-PI, a way to add a driver (and usually in IIO), is to build it into the **kernel7.img** and add a device-tree overlay.

Adding drivers is done via **make menuconfig**, and selecting the **[y]** option.

Device-tree overlays are covered in these docs:

-  https://www.raspberrypi.org/documentation/configuration/device-tree.md
-  https://learn.adafruit.com/introduction-to-the-beaglebone-black-device-tree/device-tree-overlays

Some examples of DT overlays for drivers written for ADI parts can be found at this link: :git-linux:`commits/rpi-4`.14.y/arch/arm/boot/dts/overlays

Copy built overlays (usually name <def config name>.dtbo) to the overlays folder onto the boot partition and reference the overlay in config.txt. For example:

::

   [all]
   dtoverlay=rpi-adar1000
