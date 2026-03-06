HMC425A Digital Step Attenuator Linux Driver
============================================

Supported Devices
-----------------

-  :adi:`HMC425A`
-  :adi:`HMC540S`

Evaluation Boards
-----------------

-  :adi:`EVAL-HMC425A`
-  :adi:`EVAL-HMC540S`

Description
-----------

This is a Linux industrial I/O (:doc:`IIO </wiki-migration/software/linux/docs/iio/iio>`) subsystem driver, targeting Digital Step Attenuator IIO devices with gpio interface. The industrial I/O subsystem provides a unified framework for drivers for many different types of converters and sensors using a number of different physical interfaces (i2c, spi, etc). See :doc:`IIO </wiki-migration/software/linux/docs/iio/iio>` for more information.

-  HMC425A 0.5 dB LSB GaAs MMIC 6-BIT DIGITAL POSITIVE CONTROL ATTENUATOR, 2.2 - 8.0 GHz

Source Code
===========

Status
------

+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Source                                                                                           | Mainlined?                                                                                                         |
+==================================================================================================+====================================================================================================================+
| :git-linux:`git <drivers/iio/amplifiers/hmc425a.c>`                                              | `WIP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/amplifiers/hmc425a.c>`__ |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

Files
-----

+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Function      | File                                                                                                                                |
+===============+=====================================================================================================================================+
| driver        | :git-linux:`drivers/iio/amplifiers/hmc425a.c`                                                                                       |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Documentation | `sysfs-bus-iio <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/ABI/testing/sysfs-bus-iio>`__ |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+

Devicetree
----------

properties
~~~~~~~~~~

**compatible:**

-  enum:

   -  adi,hmc425a

**vcc-supply:**

-  description: digital voltage regulator (see regulator/regulator.txt)
-  maxItems: 1

**ctrl-gpios:**

-  description: Must contain an array of 6 GPIO specifiers, referring to the GPIO pins connected to the control pins V1-V6.
-  maxItems: 6

**required:**

-  compatible
-  ctrl-gpios

Example
~~~~~~~

.. code:: c

       #include <dt-bindings/gpio/gpio.h>

       &gpio {
           #address-cells = <1>;
           #size-cells = <0>;
           gpio_hmc425a: hmc425a {
               compatible = "adi,hmc425a";
               ctrl-gpios = <&gpio 40 GPIO_ACTIVE_HIGH>,
               <&gpio 39 GPIO_ACTIVE_HIGH>,
               <&gpio 38 GPIO_ACTIVE_HIGH>,
               <&gpio 37 GPIO_ACTIVE_HIGH>,
               <&gpio 36 GPIO_ACTIVE_HIGH>,
               <&gpio 35 GPIO_ACTIVE_HIGH>;

               vcc-supply = <&foo>;
           };
       }

Adding Linux driver support
===========================

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or "make qconfig")

.. hint::

   The HMC425A Driver depends on **CONFIG_GPIOLIB**


::

   Linux Kernel Configuration
       Device Drivers  --->
           <*>     Industrial I/O support --->
               --- Industrial I/O support
                   Amplifiers  --->
                       <*> Analog Devices HMC425A DSA

Hardware configuration
======================

Driver testing
==============

Each and every IIO device, typically a hardware chip, has a device folder under /sys/bus/iio/devices/iio:deviceX. Where X is the IIO index of the device. Under every of these directory folders reside a set of files, depending on the characteristics and features of the hardware device in question. These files are consistently generalized and documented in the IIO ABI documentation. In order to determine which IIO deviceX corresponds to which hardware device, the user can read the name file /sys/bus/iio/devices/iio:deviceX/name. In case the sequence in which the iio device drivers are loaded/registered is constant, the numbering is constant and may be known in advance.


.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/> **cd /sys/bus/iio/devices/**
      root:/sys/bus/iio/devices> ls
      iio:device0
      root:/sys/bus/iio/devices> **iio:device0**
   
      root:/> **ls -l**
      drwxr-xr-x    2 root     root             0 Jan  1 00:00 .
      drwxr-xr-x    3 root     root             0 Jan  1 00:00 ..
      -r--r--r--    1 root     root          4096 Jan  1 00:00 dev
      -r--r--r--    1 root     root          4096 Jan  1 00:00 name
      -rw-r--r--    1 root     root          4096 Jan  1 00:00 out_voltage0_hardwaregain
      lrwxrwxrwx    1 root     root             0 Jan  1 00:00 subsystem -> ../../../../../../../../../bus/iio
      -rw-r--r--    1 root     root          4096 Jan  1 00:00 uevent
   


Show device name
^^^^^^^^^^^^^^^^

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/> **cd /sys/bus/iio/devices/iio\:device0/**
      root:/> **cat name**
      hmc425a
   


Set ChannelY Gain
^^^^^^^^^^^^^^^^^

| /sys/bus/iio/devices/iio:deviceX/out_voltageY_hardwaregain
| Hardware applied gain factor. If shared across all channels, <type>_hardwaregain is used.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/> **cat out_voltage0_hardwaregain**
      -31.500000 dB
   
      root:/> **echo -10 > out_voltage0_hardwaregain**
      root:/> **cat out_voltage0_hardwaregain**
      -10.000000 dB
   


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

