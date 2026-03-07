Linux LCD device driver
=======================

Introduction
------------

This section describes the steps required to build and use LCD device driver on Linux using an ADSP-SC58x board and a WVGA/LCD EI3 extender board.

WVGA/LCD EI3 Extender LCD board is not supported on the ADSP-SC573 EZ-KIT due to some board level hardawre confilict, the SC573 processor itself is capable of doing this. 

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

Run bitbake linux-adi -c menuconfig and configure the kernel as follows:

Enable touchscreen and backlight
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   Device Drivers  --->
        Input device support  --->
            [*]   Touchscreens  --->
                <*> Analog Devices AD7879-1/AD7889-1 touchscreen interface
                <*> support SPI bus connection

Enable NL8048HL WVGA LCD for ADSP-SC58x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   Device Drivers  --->
        Graphics support  --->
             Frame buffer Devices  --->
                 <*> Support for frame buffer devices  --->
                 <*> NEC NL8048HL WVGA LCD for ADI SC5XX boards

Avoid LCD driver probe failure by disabling CAN bus support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   [*] Networking support  --->
             < >   CAN bus subsystem support  ----

Enable Packages
~~~~~~~~~~~~~~~

Add the video test program in the filesystem images, it's default enabled in adsp-sc5xx-full image.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "video-test"

Example
-------

Enable LCD Back-light
~~~~~~~~~~~~~~~~~~~~~

::

   # cat /sys/kernel/debug/gpio 
   mcp230xx 0-0022: restoring reg 0x00 from 0x0000 to 0xffff (power-loss?)
   mcp230xx 0-0021: restoring reg 0x00 from 0x0000 to 0xffff (power-loss?)
   gpiochip0: GPIOs 0-15, adi-gpio:
   gpiochip1: GPIOs 16-31, adi-gpio:
    gpio-30  (                    |mdio-reset          ) out hi    
   gpiochip2: GPIOs 32-47, adi-gpio:
    gpio-32  (                    |spi0.32             ) out hi    
    gpio-39  (                    |spi0.39             ) out hi    
    gpio-44  (                    |spi0.44             ) out hi    
   gpiochip3: GPIOs 48-63, adi-gpio:
   gpiochip4: GPIOs 64-79, adi-gpio:
   gpiochip5: GPIOs 80-95, adi-gpio:
   gpiochip6: GPIOs 96-101, adi-gpio:
   gpiochip9: GPIOs 479-479, parent: spi/spi0.32, AD7879-GPIO, can sleep:
   gpiochip8: GPIOs 480-495, parent: i2c/0-0022, mcp23017, can sleep:
   gpiochip7: GPIOs 496-511, parent: i2c/0-0021, mcp23017, can sleep:
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

Run video_test Program
~~~~~~~~~~~~~~~~~~~~~~

You will see a  crossing curve like an "8" in the LCD window.

::

   # video_test

How to Install Modules
----------------------

Select these drivers as modules:

::

   <M>   Analog Devices AD7879-1/AD7889-1 touchscreen interface    
   <M>     support SPI bus connection
   <M> Support for frame buffer devices  --->
   <M> NEC NL8048HL WVGA LCD for ADI SC5XX boards

Then **bitbake adsp-sc5xx-full -C compile**

If AD7879 module has already been installed, removed it first:

::

   # lsmod
   Module                  Size  Used by 
   ad7879_spi              2222  0 
   ad7879                  3763  1 ad7879_spi 
   # modprobe -r ad7879_spi
   # lsmod
   Module                  Size  Used by

Then install the modules as follows:

::

   # modprobe adi_nl8048
   adi_nl8048 31040000.lcd: LCD fb0 registered@cf15f846,dma=28,irq=48,cs=39
   # modprobe ad7879_spi
   input: AD7879 Touchscreen as /devices/platform/scb/31042000.spi/spi_master/spi0/spi0.32/input/input0

Now you can run LCD test as above.

**Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
