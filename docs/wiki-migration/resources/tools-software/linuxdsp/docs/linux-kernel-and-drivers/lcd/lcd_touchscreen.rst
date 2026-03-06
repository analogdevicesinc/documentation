Linux LCD Touchscreen
=====================

Introduction
------------

This section describes the steps required to build and use SPI Touchscreen device on Linux using an ADSP-SC58x board and a WVGA/LCD EI3 extender board.

Hardware Setup
--------------

-  ADSP-SC58x EZ-KIT: ADSP-SC589/SC584 EZ-Board
-  A WVGA/LCD EI3 Extender Board

Connect the J1 connector on the LCD EI3 Extender Board to the P1A connector on the SC58x-EZKIT

Software Configuration
----------------------

The following configuration should be done on top of the sc589-ezkit/sc584-ezkit default configuration.

Configure Linux Kernel
~~~~~~~~~~~~~~~~~~~~~~

Run **bitbake linux-adi -c menuconfig** and configure the kernel as follows:

There are two things to enable in the Linux kernel.  First, you need the common code for the event interface.  Then you need the specific driver for the touchscreen device you're using.

::

   Device Drivers  --->
       Input device support  --->
           [*] Generic input layer (needed for keyboard, mouse, ...)
           <*>   Event interface

The touchscreen drivers will be in the same place.  Enable the driver for the device you're using.

::

   Device Drivers  --->
       Input device support  --->
           [*] Touchscreens  --->
               <*>   Analog Devices AD7879-1/AD7889-1 touchscreen interface
               <*>     support SPI bus connection

Don't forget to enable LCD and disable CAN driver for touch screen calibraion.

::

   Device Drivers  --->
        Graphics support  --->
            Frame buffer Devices  --->
                <*> Support for frame buffer devices  --->
                <*> NEC NL8048HL WVGA LCD for ADI SC5XX boards
   [*] Networking support  --->
       < > CAN bus subsystem support  ---->

Enable Packages
~~~~~~~~~~~~~~~

Add the touchscreen test program in the filesystem images, it's enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "tslib tslib-calibrate evtest"

Example
-------

Enable LCD Back-light
~~~~~~~~~~~~~~~~~~~~~

Look for the right gpio number of target boards:

::

   # cat /sys/kernel/debug/gpio
   gpiochip0: GPIOs 0-15, adi-gpio:
   gpiochip1: GPIOs 16-31, adi-gpio:
   gpio-30 ( |mdio-reset ) out hi
   gpiochip2: GPIOs 32-47, adi-gpio:
   gpio-32 ( |spi0.32 ) out hi 
   gpio-38 ( |spi2.38 ) out hi 
   gpio-39 ( |spi0.39 ) out hi 
   gpio-44 ( |spi0.44 ) out hi
   gpiochip3: GPIOs 48-63, adi-gpio:
   gpiochip4: GPIOs 64-79, adi-gpio:
   gpiochip5: GPIOs 80-95, adi-gpio:
   gpiochip6: GPIOs 96-101, adi-gpio:
   gpiochip9: GPIOs 479-479, parent: spi/spi0.32, AD7879-GPIO, can sleep:
   gpiochip8: GPIOs 480-495, parent: i2c/0-0022, mcp23017, can sleep:
   gpiochip7: GPIOs 496-511, parent: i2c/0-0021, mcp23017, can sleep:
   gpio-498 P0.2 (adi-uart4.0 ) out lo 
   gpio-499 P0.3 (3100c000.ethernet) out lo 
   gpio-500 P0.4 (3100e000.ethernet) out lo 
   gpio-507 P0.11 (31010000.mmc) out lo 
   gpio-508 P0.12 (spi2.38 ) out lo 
   gpio-509 P0.13 (spi2.38 ) out lo

As above showed, GPIO 479 is what we are looking for.

::

   # echo 479 > /sys/class/gpio/export 
   # echo high > /sys/class/gpio/gpio479/direction

Make sure your LCD screen becomes white at this point.

Soft Switch Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

The settings in this section is only apply to ADSP-SC584 EZ-Board.

::

   # echo 484 > /sys/class/gpio/export
   # echo high > /sys/class/gpio/gpio484/direction
   # echo 491 > /sys/class/gpio/export
   # echo high > /sys/class/gpio/gpio491/direction

Runtime Config
~~~~~~~~~~~~~~

Before you can use the touchscreen, you need to export a few environment variables.  You may want to put these into a file so you can easily source it at runtime.

::

   # vi /etc/tslib.env
   export TSLIB_FBDEVICE=/dev/fb0
   export TSLIB_CONSOLEDEVICE=none
   export TSLIB_CONFFILE=/etc/ts.conf
   export TSLIB_CALIBFILE=/etc/pointercal
   export TSLIB_TSDEVICE=/dev/input/event0
   # . /etc/tslib.env

Calibration
~~~~~~~~~~~

Before you start using the touchscreen, you should calibrate it.  This can be easily accomplished with the ts_calibrate application on the EI3 LCD extender.  Just follow the on-screen directions.

Then run following commands and touch the appropriate location according to screen`s prompts .

::

   # ts_calibrate
   xres = 800, yres = 480
   Took 3 samples...
   Top left : X = 261 Y = 648
   Took 5 samples...
   Top right : X = 3631 Y = 657
   Took 6 samples...
   Bot right : X = 3633 Y = 3407
   Took 5 samples...
   Bot left : X = 236 Y = 3467
   Took 2 samples...
   Center : X = 1970 Y = 2001
   -4.445068 0.206877 0.000894
   -39.800293 0.001046 0.136427
   Calibration constants: -291312 13557 58 -2608352 68 8940 65536

Event Test
~~~~~~~~~~

After run following the command, start using the touchscreen.  The application should decode the input immediately.

::

   # evtest /dev/input/event0
   Input driver version is 1.0.1
   Input device ID: bus 0x1c vendor 0x0 product 0x7a version 0x3
   Input device name: "AD7879 Touchscreen"
   Supported events:
     Event type 0 (EV_SYN)
     Event type 1 (EV_KEY)
       Event code 330 (BTN_TOUCH)
     Event type 3 (EV_ABS)
       Event code 0 (ABS_X)
         Value      0
         Min        0
         Max     4095
       Event code 1 (ABS_Y)
         Value      0
         Min        0
         Max     4095
       Event code 24 (ABS_PRESSURE)
         Value      0
         Min        0
         Max    10000
   Properties:
   Testing ... (interrupt to exit)
   Event: time 1572578217.819961, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 1
   Event: time 1572578217.819961, type 3 (EV_ABS), code 0 (ABS_X), value 1552
   Event: time 1572578217.819961, type 3 (EV_ABS), code 1 (ABS_Y), value 2577
   Event: time 1572578217.819961, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 446
   Event: time 1572578217.819961, -------------- SYN_REPORT ------------
   Event: time 1572578217.832117, type 3 (EV_ABS), code 0 (ABS_X), value 1565
   Event: time 1572578217.832117, type 3 (EV_ABS), code 1 (ABS_Y), value 2564
   Event: time 1572578217.832117, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 644
   Event: time 1572578217.832117, -------------- SYN_REPORT ------------
   Event: time 1572578217.844232, type 3 (EV_ABS), code 0 (ABS_X), value 1571
   Event: time 1572578217.844232, type 3 (EV_ABS), code 1 (ABS_Y), value 2563
   Event: time 1572578217.844232, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 383
   Event: time 1572578217.844232, -------------- SYN_REPORT ------------
   Event: time 1572578217.856371, type 3 (EV_ABS), code 0 (ABS_X), value 1557
   Event: time 1572578217.856371, type 3 (EV_ABS), code 1 (ABS_Y), value 2572
   Event: time 1572578217.856371, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 326
   Event: time 1572578217.856371, -------------- SYN_REPORT ------------
   Event: time 1572578217.868511, type 3 (EV_ABS), code 0 (ABS_X), value 1551
   Event: time 1572578217.868511, type 3 (EV_ABS), code 1 (ABS_Y), value 2588
   Event: time 1572578217.868511, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 298
   Event: time 1572578217.868511, -------------- SYN_REPORT ------------
   Event: time 1572578217.880664, type 3 (EV_ABS), code 0 (ABS_X), value 1554
   Event: time 1572578217.880664, type 3 (EV_ABS), code 1 (ABS_Y), value 2613
   Event: time 1572578217.880664, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 286
   Event: time 1572578217.880664, -------------- SYN_REPORT ------------
   Event: time 1572578217.892814, type 3 (EV_ABS), code 0 (ABS_X), value 1559
   Event: time 1572578217.892814, type 3 (EV_ABS), code 1 (ABS_Y), value 2624
   Event: time 1572578217.892814, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 288
   Event: time 1572578217.892814, -------------- SYN_REPORT ------------
   Event: time 1572578217.904947, type 3 (EV_ABS), code 0 (ABS_X), value 1562
   Event: time 1572578217.904947, type 3 (EV_ABS), code 1 (ABS_Y), value 2626
   Event: time 1572578217.904947, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 300
   Event: time 1572578217.904947, -------------- SYN_REPORT ------------
   Event: time 1572578217.917082, type 3 (EV_ABS), code 1 (ABS_Y), value 2611
   Event: time 1572578217.917082, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 334
   Event: time 1572578217.917082, -------------- SYN_REPORT ------------
   Event: time 1572578217.969468, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 0
   Event: time 1572578217.969468, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 0
   Event: time 1572578217.969468, -------------- SYN_REPORT ------------

--------------

**Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
