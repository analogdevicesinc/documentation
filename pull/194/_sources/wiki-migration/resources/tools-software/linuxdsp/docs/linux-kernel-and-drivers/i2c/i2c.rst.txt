I2C
===

Introduction
------------

The Inter-Integrated Circuit (I2C) bus is a two wire multi-master/slave low speed serial bus. Multiple slave devices may be accessed over the same bus, using a unique 7-bit addresses for each slave. Communication on the bus is half-duplex, and slaves do not transmit any data unless a master has addressed it first.

From the Linux point of view the driver for I2C hardware controller is the adapter driver, while drivers for the peripheral I2C devices are the client drivers. The adapter driver is provided by ADI, and most of the work that a product developer needs to do is in implementing the client driver to connect a specific I2C slave device to applications running under Linux on the SC5xx processor.

This document focuses on explaining the programming interface for the I2C client driver, it talks about how to create the client driver from both kernel and user space, to guide the audience to develop the client driver of their own.

I2C in the Linux Kernel
-----------------------

This section talks about the I2C kernel driver framework and how to implement the client I2C driver from kernel space.

I2C Kernel Driver
~~~~~~~~~~~~~~~~~

The main source code for the SC5xx I2C adapter driver is in drivers/i2c/busses/i2c-bfin-twi.c. The "Blackfin" name is used here because the ADSP-SC5xx processors use the same hardware IP for the I2C interface as the ADSP-BFxxx series. The device tree description for the 3 controllers, i2c0, i2c1 and i2c2 is in file arch/arm/boot/dts/sc58x.dtsi or arch/arm/boot/dts/sc57x.dtsi. Select from the following options to enable the I2C adapter driver, and you can set the clock speed from there:

::

   Linux Kernel Configuration
       Device Drivers  --->
           I2C support  --->
               I2C Hardware Bus support  --->
                   <*> ADI TWI I2C support
                   (50)  ADI TWI I2C clock (kHz) 
                   

I2C Client Driver Example
~~~~~~~~~~~~~~~~~~~~~~~~~

In this section we take audio codec driver for ADAU1977 as an example to show the typical code structure for the I2C client driver, demonstrating how users normally initialize a client's driver, register it to the system, then use the registered method to do data read/write via the I2C bus. The main source code file for this example includes sound/soc/codecs/adau1977-i2c.c, sound/soc/codecs/adau1977.c, drivers/base/regmap/regmap-i2c.c and device tree file arch/arm/boot/dts/sc589-ezkit.dts.

Client driver instance
~~~~~~~~~~~~~~~~~~~~~~

The following C code defines a client driver instance, which is later registered to the Linux I2C sub-system. See the source code for details on the implementation of each method.

::

   static struct i2c_driver adau1977_i2c_driver = {
           .driver = {
                   .name = "adau1977",
                   .owner = THIS_MODULE,
                   .of_match_table = of_match_ptr(adau1977_dt_ids),
           },
           .probe = adau1977_i2c_probe,
           .remove = adau1977_i2c_remove,
           .id_table = adau1977_i2c_ids,
   };
    

Register
~~~~~~~~

The following C code registers the above client driver to the Linux I2C sub-system

::

   module_i2c_driver(adau1977_i2c_driver);

Data read/write method
~~~~~~~~~~~~~~~~~~~~~~

This audio codec driver uses the regmap programming interface, which is built upon the lower level of the I2C data read/write interface, to do the data read/write immediately with code of the following style in the file sound/soc/codecs/adau1977.c

::

   ret = regmap_read(adau1977->regmap, ADAU1977_REG_PLL, &val);
     
   ret = regmap_write(adau1977->regmap, ADAU1977_REG_POWER,
                           ADAU1977_POWER_RESET);

This regmap interface for the I2C bus is implemented in file drivers/base/regmap/regmap-i2c.c. In this file, we can see the I2C bus data read/write is carried out via either the raw I2C transfer interface or the SMBus interface. Take the SMBus for example:

Read data:

::

   static int regmap_smbus_byte_reg_read(void *context, unsigned int reg,
                                         unsigned int *val)
   {
           struct device *dev = context;
           struct i2c_client *i2c = to_i2c_client(dev);
           int ret;
           if (reg > 0xff)
                   return -EINVAL;
           ret = i2c_smbus_read_byte_data(i2c, reg);
           if (ret < 0)
                   return ret;
           *val = ret;
           return 0;
   }

Write data:

::

   static int regmap_smbus_byte_reg_write(void *context, unsigned int reg,
                                          unsigned int val)
   {
           struct device *dev = context;
           struct i2c_client *i2c = to_i2c_client(dev);
           if (val > 0xff || reg > 0xff)
                   return -EINVAL;
           return i2c_smbus_write_byte_data(i2c, reg, val);
   }

SMBus protocol and its APIs is a subset of the I2C protocol and is widely used for the I2C device driver in Linux, get more details on the SMBus protocol from the kernel source: Documentation/i2c/smbus-protocol.

I2C in User Space Usually I2C devices are controlled by the device driver in kernel space, but we can also implement this from user space.

Kernel configuration
--------------------

Linux kernel introduced an i2c-dev layer. It exports the adapter driver for the I2C controller as device nodes to user space, so we can implement the driver for a specific I2C client in user space. To take advantage of this feature, we need to enable the i2c-dev interface from the kernel menu configuration

::

   Linux Kernel Configuration
       Device Drivers  --->
           I2C support  --->
                <*>   I2C device interface

Get more details about i2c-dev interface from Documentation/i2c/dev-interface.

Example
~~~~~~~

The TWI LCD I2C driver code is a good example for an I2C user space driver. Add the following package to IMAGE_INSTALL_append in local.conf file:

::

   $ vim build/conf/local.conf
   IMAGE_INSTALL_append = " twi-lcd-test"

Once rebuilt, the file twilcd_userspace_test.c is the main source code for this example. We can see the general steps for implementing a user space I2C client driver in function main, code skeleton as follows:

::

   int main (int argc, char *argv[])
   {
       int file;
       int adapter_nr = 2; /* probably dynamically determined */
       char filename[20];
       snprintf(filename, 19, "/dev/i2c-%d", adapter_nr);
        
       /** Open the I2C controller device node **/
       file = open(filename, O_RDWR);
        
       if (file < 0) {
          /* ERROR HANDLING; you can check errno to see what went wrong */
          exit(1);
       }
     
       int addr = 0x40; /* The I2C address */
      
       /** Set the address for the I2C peripheral device **/
       if (ioctl(file, I2C_SLAVE, addr) < 0) {
             /* ERROR HANDLING; you can check errno to see what went wrong */
             exit(1);
        }
        /* Using SMBus commands for data transaction*/
        res = i2c_smbus_read_word_data(file, reg);
        if (res < 0) {
           /* ERROR HANDLING: i2c transaction failed */
        } else {
           /* res contains the read word */
        }        
    
   }

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
