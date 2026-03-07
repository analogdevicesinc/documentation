GPIO operation
==============

Introduction
------------

A General Purpose Input/Output (GPIO) is a flexible software-controlled digital signal. They are provided from many kinds of chip, and are familiar to Linux developers working with embedded and custom hardware. Each GPIO represents a bit connected to a particular pin, or “ball” on Ball Grid Array (BGA) packages. Board schematics show which external hardware connects to which GPIOs. Drivers can be written generically, so that board setup code passes such pin configuration data to drivers.

Often different aspects of the GPIO need to be controlled, such as:

-  direction: input or output
-  value: set or unset
-  polarity: high or low
-  edge: rising or falling

Hardware
--------

-  ADSP-SC5xx EZKIT Board:

   -  ADSP-SC589 Ezkit v1.1 and above, or,

      -  ADSP-SC584 Ezkit v1.0 and above, or,
      -  ADSP-SC589 MINI board, or,
      -  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above

In the ADSP-SC58x processors there are 7 gpio blocks, called PORTA..PORTG. Each PORTx interface has 16 GPIO pins. PORT(A-G) pins are brought out on the 110 pins of SC589-EZKIT(PA0-PG13) and 80 pins of SC584-EZKIT(PA0-PD16). While in the ADSP-SC573 processors there are only 6 gpio blocks, called PORTA..PORTF.

Application space GPIO support
------------------------------

Standard Linux kernel have inside a special interface allow to access to GPIO pins. You can use kernel menuconfig (linux-menuconfig) to verify that these interfaces are active in your kernel and, if necessary, enable them.

The kernel tree path is the following:

::

   Symbol: GPIO_SYSFS [=y]
     Prompt: /sys/class/gpio/... (sysfs interface)
       Defined at drivers/gpio/Kconfig:51
       Depends on: GPIOLIB && SYSFS && EXPERIMENTAL
        Location:
         -> Kernel configuration
           -> Device Drivers
            -> GPIO Support (GPIOLIB [=y])

 

Paths in Sysfs
--------------

There are three kinds of entry in /sys/class/gpio:

-  Control interfaces used to get userspace control over GPIOs
-  GPIOs themselves
-  GPIO controllers ("gpio_chip" instances)

This is in addition to standard files including the "device" symlink.

The control interfaces are write-only:

::

       /sys/class/gpio/

           "export" ... Userspace may ask the kernel to export control of
           a GPIO to userspace by writing its number to this file.

           Example:  "echo 19 > export" will create a "gpio19" node
           for GPIO #19, if that's not requested by kernel code.

           "unexport" ... Reverses the effect of exporting to userspace.

           Example:  "echo 19 > unexport" will remove a "gpio19"
           node exported using the "export" file.

   GPIO signals have paths like /sys/class/gpio/gpio42/ (for GPIO #42)
   and have the following read/write attributes:

       /sys/class/gpio/gpioN/

       "direction" ... reads as either "in" or "out". This value may
           normally be written. Writing as "out" defaults to
           initializing the value as low. To ensure glitch free
           operation, values "low" and "high" may be written to
           configure the GPIO as an output with that initial value.

           Note that this attribute *will not exist* if the kernel
           doesn't support changing the direction of a GPIO, or
           it was exported by kernel code that didn't explicitly
           allow userspace to reconfigure this GPIO's direction.

       "value" ... reads as either 0 (low) or 1 (high). If the GPIO
           is configured as an output, this value may be written;
           any nonzero value is treated as high.

           If the pin can be configured as interrupt-generating interrupt
           and if it has been configured to generate interrupts (see the
           description of "edge"), you can poll(2) on that file and
           poll(2) will return whenever the interrupt was triggered. If
           you use poll(2), set the events POLLPRI and POLLERR. If you
           use select(2), set the file descriptor in exceptfds. After
           poll(2) returns, either lseek(2) to the beginning of the sysfs
           file and read the new value or close the file and re-open it
           to read the value.

       "edge" ... reads as either "none", "rising", "falling", or
           "both". Write these strings to select the signal edge(s)
           that will make poll(2) on the "value" file return.

           This file exists only if the pin can be configured as an
           interrupt generating input pin.

       "active_low" ... reads as either 0 (false) or 1 (true). Write
           any nonzero value to invert the value attribute both
           for reading and writing. Existing and subsequent
           poll(2) support configuration via the edge attribute
           for "rising" and "falling" edges will follow this
           setting.

   GPIO controllers have paths like /sys/class/gpio/gpiochip42/ (for the
   controller implementing GPIOs starting at #42) and have the following
   read-only attributes:

       /sys/class/gpio/gpiochipN/

           "base" ... same as N, the first GPIO managed by this chip

           "label" ... provided for diagnostics (not always unique)

           "ngpio" ... how many GPIOs this manges (N to N + ngpio - 1)

 

Dump the GPIO configuration
---------------------------

::

   # cat /sys/kernel/debug/gpio 
   GPIOs 0-15, platform/31004000.gport, adi-gpio:
   GPIOs 16-31, platform/31004080.gport, adi-gpio:
    gpio-30  (mdio-reset          ) out hi    
   GPIOs 32-47, platform/31004100.gport, adi-gpio:
   GPIOs 48-63, platform/31004180.gport, adi-gpio:
   GPIOs 64-79, platform/31004200.gport, adi-gpio:
   GPIOs 80-95, platform/31004280.gport, adi-gpio:
   GPIOs 96-101, platform/31004300.gport, adi-gpio:
   GPIOs 480-495, i2c/0-0022, mcp23017, can sleep:
   GPIOs 496-511, i2c/0-0021, mcp23017, can sleep:

--------------

**Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
