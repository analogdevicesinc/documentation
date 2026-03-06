ADP5588 GPIO Linux Driver
=========================

Supported Devices
-----------------

-  :adi:`ADP5587`
-  :adi:`ADP5588`

Evaluation Boards
-----------------

-  :adi:`ADP5588-EVALZ`
-  :adi:`ADP5587CB-EVALZ`
-  :adi:`ADP5587CP-EVALZ`

Description
-----------

Configuration
-------------

.. image:: https://wiki.analog.com/_media/software/driver/linux/adp5588_typ_op.png
   :width: 600px

Software configurable features
------------------------------

Source Code
===========

Status
------

+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Source                                                                                                        | Mainlined?                                                                                                    |
+===============================================================================================================+===============================================================================================================+
| `git <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-adp5588.c>`__ | `Yes <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-adp5588.c>`__ |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+

Files
-----

+----------+--------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                     |
+==========+==========================================================================================================================+
| driver   | `gpio-adp5588.c <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-adp5588.c>`__ |
+----------+--------------------------------------------------------------------------------------------------------------------------+
| include  | `adp5588.h <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/include/linux/i2c/adp5588.h>`__      |
+----------+--------------------------------------------------------------------------------------------------------------------------+

Example platform device initialization
======================================

For compile time configuration, it’s common Linux practice to keep board- and application-specific configuration out of the main driver file, instead putting it into the board support file.

For devices on custom boards, as typical of embedded and SoC-(system-on-chip) based hardware, Linux uses platform_data to point to board-specific structures describing devices and how they are connected to the SoC. This can include available ports, chip variants, preferred modes, default initialization, additional pin roles, and so on. This shrinks the board-support packages (BSPs) and minimizes board and application specific #ifdefs in drivers.


<source trunk/include/linux/i2c/adp5588.h:/i2c_board_info/-EOF c linux-kernel>

<source trunk/arch/blackfin/mach-bf537/boards/stamp.c:adp5588_gpio_data{} c linux-kernel>

Unlike PCI or USB devices, I2C devices are not enumerated at the hardware level. Instead, the software must know which devices are connected on each I2C bus segment, and what address these devices are using. For this reason, the kernel code must instantiate I2C devices explicitly. There are different ways to achieve this, depending on the context and requirements. However the most common method is to declare the I2C devices by bus number.

This method is appropriate when the I2C bus is a system bus, as in many embedded systems, wherein each I2C bus has a number which is known in advance. It is thus possible to pre-declare the I2C devices that inhabit this bus. This is done with an array of struct i2c_board_info, which is registered by calling i2c_register_board_info().

So, to enable such a driver one need only edit the board support file by adding an appropriate entry to i2c_board_info.

For more information see: `instantiating-devices.rst <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/i2c/instantiating-devices.rst>`__


.. code:: C

   static struct i2c_board_info __initdata bfin_i2c_board_info[] = {
   #if defined(CONFIG_GPIO_ADP5588) || defined(CONFIG_GPIO_ADP5588_MODULE)
       {
           I2C_BOARD_INFO("adp5588-gpio", 0x34),
           .irq = IRQ_PG0,
           .platform_data = (void *)&adp5588_gpio_data,
       },
   #endif
   }

Adding Linux driver support
===========================

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or "make qconfig")

|

.. hint::

   The ADP5588 Driver depends on **CONFIG_I2C**

   | IRQ-Chip interrupt controller support is not available in case this driver is build as Module


::

   Device Drivers  --->
   [*] GPIO Support  --->

       --- GPIO Support
       [ ]   Debug GPIO calls
       [*]   /sys/class/gpio/... (sysfs interface)
             *** Memory mapped GPIO expanders: ***
       < >   IT8761E GPIO support
             *** I2C GPIO expanders: ***
       < >   Maxim MAX7300 GPIO expander
       < >   MAX7319, MAX7320-7327 I2C Port Expanders
       < >   PCA953x, PCA955x, TCA64xx, and MAX7310 I/O ports
       < >   PCF857x, PCA{85,96}7x, and MAX732[89] I2C GPIO expanders
       [ ]   Semtech SX150x I2C GPIO expander
       < >   GPIO Support for ADP5520 PMIC
       <*>   ADP5588 I2C GPIO expander
       [*]     Interrupt controller support for ADP5588
   <
   /code>

   ====== Hardware configuration ======
   {{:software:driver:linux:adp5588_demo_brd_and_stamp.jpg?600|}}

   There is no dedicated Blackfin STAMP evaluation board for the ADP5588.
   During test and driver development we used the ADP5588 Demo Mother/Daughter Board.

   It can be easily wired to the Blackfin STAMP TWI/I2C header.

   ^ BF537-STAMP (P10) TWI/I2C header  ^^ ADP5588 Daughter Board ^
   ^ PIN ^ Function ^ PIN/Function ^
   | 2 | (+3.3V) | VCC |
   | 5 | SCL | SCL |
   | 6 | SDA| SDA |
   | 10 | PORTG0 | INTB |
   | 20 | GND | GND |

.. tip::

      On the ADP5588 Demo Mother Board replace R30 (10kOhm PULL-UP resistor on /INTB strobe) with a 1-3kOhm resistor.
      The 10kOhm resistor is too weak - Blackfin might see an additional falling edge interrupt on the rising edge of /INTB.


====== Driver testing ======
   When the driver is loaded, you should see positive output that it found the ADP5588 GPIO device.

   <code>
   root:/> **modprobe adp5588-gpio**
   **adp5588-gpio 0-0034: gpios 50..67 on a adp5588-gpio Rev. 4**

For more information see also here: `linux-kernel:drivers:gpio-sysfs <https://analogdevicesinc.github.io/linux-kernel:drivers:gpio-sysfs>`__

::

   root:/> echo 67 > /sys/class/gpio/export

   root:/> echo low > /sys/class/gpio/gpio67/direction
   root:/> echo high > /sys/class/gpio/gpio67/direction

   root:/> echo in > /sys/class/gpio/gpio67/direction
   root:/> cat /sys/class/gpio/gpio67/value
   1
   root:/> cat /sys/class/gpio/gpio67/value
   0
   root:/

More Information
================
