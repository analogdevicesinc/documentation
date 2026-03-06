iio-trig-sysfs driver
=====================

Description
-----------

This driver adds a trigger that can be invoked by writing the sysfs file: trigger_now. This approach can be valuable during automated testing or in situations, where other trigger methods are not applicable. For example no RTC or spare GPIOs. Last but not least it allows user space applications to produce triggers.

Documentation
-------------

-  `sysfs-bus-iio-trigger-sysfs <https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-bus-iio-trigger-sysfs>`__

Adding Linux driver support
===========================

Configure kernel with “make menuconfig” (alternatively use “make xconfig” or “make qconfig”)

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
                   <*>   SYSFS trigger
                   < >   Blackfin TIMER trigger

sysfs trigger creation and removal
----------------------------------

When sysfs trigger support is enabled in the kernel configuration there will be a /sys/bus/iio/devices/iio_sysfs_trigger/ folder which can be used for sysfs trigger management. The folder contains two files "add_trigger" and "remove_trigger". New sysfs triggers can be created by writing a ID to the "add_trigger" file. E.g. \`echo 0 > add_trigger\`. This will create a new sysfs trigger, which you can access at "/sys/bus/iio/devices/iio:triggerX", where X is a the trigger number. Typically it will be 0 for the first trigger, 1 for the second, etc. The name of the trigger will be "sysfstrigID" where ID is the value writting to the "add_trigger" file.

To remove a sysfs trigger write the same ID used when registering it to the "remove_trigger" file. E.g \`echo 0 > remove_trigger\`.

Driver testing
==============

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/> **cd sys/bus/iio/devices/**
      root:/sys/bus/iio/devices> **ls**
      iio:device0
      iio:device1
      iio:trigger0
      root:/sys/bus/iio/devices> **cd iio:trigger0**
      root:/sys/devices/iio:trigger0> **ls**
      name         subsystem    trigger_now  uevent
      root:/sys/devices/iio:trigger0> **cat name**
      sysfstrig0
      root:/sys/devices/iio:trigger0> **echo 1 > trigger_now**
      root:/sys/devices/iio:trigger0> **echo 1 > trigger_now**
   


More Information
================

-  IIO mailing list: linux-iio@vger.kernel.org
-  `IIO Linux Kernel Documentation sysfs-bus-iio-\* <https://www.kernel.org/doc/Documentation/ABI/testing>`__
-  `IIO Documentation <https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-bus-iio>`__
-  :doc:`IIO test and visualization application </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`libiio - IIO system library </wiki-migration/resources/tools-software/linux-software/libiio>`
-  :doc:`libiio - Internals </wiki-migration/resources/tools-software/linux-software/libiio_internals>`
-  :doc:`Pointers and good books </wiki-migration/resources/tools-software/pointers>`
-  `IIO High Speed <https://events.static.linuxfound.org/sites/events/files/slides/iio_high_speed.pdf>`__
-  `Software Defined Radio using the IIO framework <http://video.fosdem.org/2015/devroom-software_defined_radio/iiosdr.mp4>`__
-

|libiio introduction|

.. image:: https://wiki.analog.com/_media/page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn
   :alt: page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn

.. |libiio introduction| image:: https://wiki.analog.com/_media/youtube>p_VntEwUe24

