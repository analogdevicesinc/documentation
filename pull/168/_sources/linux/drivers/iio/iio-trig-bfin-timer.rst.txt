.. _iio iio-trig-bfin-timer:

iio-trig-bfin-timer driver
""""""""""""""""""""""""""

This driver allows any Blackfin system timer to be used as IIO trigger. It
supports trigger rates from 0 to 100kHz in Hz resolution.

.. tip::

   This driver depends on ``BLACKFIN``

Adding Linux driver support
===========================

Configure kernel with ``make menuconfig`` (alternatively use ``make xconfig`` or
``make qconfig``)

::

   Linux Kernel Configuration
       Device Drivers  --->
           [*] Staging drivers  --->
               <*>     Industrial I/O support  --->
                   --- Industrial I/O support
                   -*-   Enable ring buffer support within IIO
                   -*-     Industrial I/O lock free software ring
                   -*-   Enable triggered sampling support

                   [--snip--]

                         *** Triggers - standalone ***
                   < >   Periodic RTC triggers
                   < >   GPIO trigger
                   < >   SYSFS trigger
                   <*>   Blackfin TIMER trigger

Example platform device initialization
======================================

One or multiple instances of this driver can be declared by adding appropriate
platform device data. An example is shown below:

.. code:: c

   static struct resource iio_bfin_trigger_resources[] = {
       {
           .start = IRQ_TIMER3,
           .end = IRQ_TIMER3,
           .flags = IORESOURCE_IRQ,
       },
   };

   static struct platform_device iio_bfin_trigger = {
       .name       = "iio_bfin_tmr_trigger",
       .id     = 0,
       .num_resources  = ARRAY_SIZE(iio_bfin_trigger_resources),
       .resource   = iio_bfin_trigger_resources,
   };

.. code:: c

   static struct platform_device *board_devices[] __initdata = {
       &iio_bfin_trigger
   };

.. code:: c

   static int __init board_init(void)
   {
       [--snip--]

       platform_add_devices(board_devices, ARRAY_SIZE(board_devices));

       [--snip--]

       return 0;
   }
   arch_initcall(board_init);

Driver testing
==============

.. shell::

   $cd /sys/bus/iio/devices
   $ls
    device0                  device0:buffer0:event0   device1:buffer0:access0
    device0:buffer0          device1                  device1:buffer0:event0
    device0:buffer0:access0  device1:buffer0          trigger0

.. shell::

   /sys/bus/iio/devices
   $cd trigger0
   $ls
    name         subsystem    frequency  uevent

.. shell::

   /sys/devices/trigger0
   $cat name
    bfintmr3

.. shell::

   /sys/devices/trigger0
   $echo 1000 > frequency
   $echo 0 > frequency
