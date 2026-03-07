ADMFM2000 0.5 GHz to 32 GHz Microwave Downconverter Linux Driver
================================================================

The ADMFM2000 is a dual-channel microwave downconverter, system-in-package (SiP) module, with input RF and local oscillator (LO) frequency ranges covering 5 GHz to 32 GHz, with an output intermediate frequency (IF) frequency range from 0.5 GHz to 8 GHz. A common LO input signal is split to feed two separate buffer amplifiers to drive the mixer in each channel. Each down conversion path consists of an LNA, a mixer, an IF filter, a digital step attenuator (DSA), and an IF amplifier.

Supported Devices
-----------------

This driver supports the

-  :adi:`ADMFM2000`

Description
-----------

This is a Linux industrial I/O (:doc:`IIO </wiki-migration/software/linux/docs/iio/iio>`) subsystem driver, targeting serial interface Microwave converters. The industrial I/O subsystem provides a unified framework for drivers for many different types of converters and sensors using a number of different physical interfaces (i2c, spi, etc). See :doc:`IIO </wiki-migration/software/linux/docs/iio/iio>` for more information.

Source Code
===========

Status
------

+-------------------------------------------------------------------------------------------------+---------------+
| Source                                                                                          | Mainlined?    |
+=================================================================================================+===============+
| :git-linux:`git <drivers/iio/frequency/admfm2000.c>`                                            | [In-progress] |
+-------------------------------------------------------------------------------------------------+---------------+

Files
-----

======== ====
Function File
======== ====
======== ====

+----------------------+----------------------------------------------------------------------------------------+
| driver               | :git-linux:`drivers/iio/frequency/admfm2000.c`                                         |
+----------------------+----------------------------------------------------------------------------------------+
| device tree bindings | :git-linux:`Documentation/devicetree/bindings/iio/frequency/adi,admfm2000.yaml`        |
+----------------------+----------------------------------------------------------------------------------------+

Example Linux Device-Tree Initialization
========================================

The ADMFM2000 driver is a platform driver and can currently only be instantiated via device tree.

**Required properties:**

-  **compatible**: Must be of "adi,admfm2000".
-  \*\* switch-gpios:\*\*: GPIOs to select the RF path for the channel. The same state of CTRL-A and CTRL-B GPIOs is not permitted.
-  \*\* attenuation-gpios:\*\*: GPIOs to select the choice of attenuation for the channel.
-  **#address-cells**: Must be set to 1
-  **#size-cells**: Must be set to 0

**Optional properties:**

-  **adi,mixer-mode:**: Enable mixer mode for the channel. It downconverts RF between 5 GHz and 32 GHz to IF between 0.5 GHz and 8 GHz. If not present, the channel is in direct IF mode which bypasses the mixer and downconverts RF between 2 GHz and 8 GHz to IF between 0.5 GHz and 8 GHz.

**Example:**

::

   #include <dt-bindings/gpio/gpio.h>
   &{/} {
       admfm2000 {
                   compatible = "adi,admfm2000";
                   #address-cells = <1>;
                   #size-cells = <0>;

                   channel@0 {
                           reg = <0>;
               switch-gpios = <&gpio 1 GPIO_ACTIVE_LOW>,
                          <&gpio 2 GPIO_ACTIVE_HIGH>;

               attenuation-gpios = <&gpio 17 GPIO_ACTIVE_LOW>,
                               <&gpio 22 GPIO_ACTIVE_LOW>,
                           <&gpio 23 GPIO_ACTIVE_LOW>,
                           <&gpio 24 GPIO_ACTIVE_LOW>,
                           <&gpio 25 GPIO_ACTIVE_LOW>;
           };

                   channel@1 {
                           reg = <1>;
                           adi,mixer-mode;
               switch-gpios = <&gpio 3 GPIO_ACTIVE_LOW>,
                          <&gpio 4 GPIO_ACTIVE_HIGH>;

               attenuation-gpios = <&gpio 0 GPIO_ACTIVE_LOW>,
                           <&gpio 5 GPIO_ACTIVE_LOW>,
                           <&gpio 6 GPIO_ACTIVE_LOW>,
                           <&gpio 16 GPIO_ACTIVE_LOW>,
                           <&gpio 26 GPIO_ACTIVE_LOW>;
                   };
           };
   };

Enabling Linux driver support
=============================

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or "make qconfig")

.. hint::

   The ADMFM2000 driver depends on **GPIOLIB**


::

   Linux Kernel Configuration
       Device Drivers  --->
           <*>     Industrial I/O support --->
               --- Industrial I/O support
                   Frequency  --->
                       <*> Analog Devices ADMFM2000 Dual Microwave Down Converter

Driver testing / API
====================

Each and every IIO device, typically a hardware chip, has a device folder under /sys/bus/iio/devices/iio:deviceX. Where X is the IIO index of the device. Under every of these directory folders reside a set of files, depending on the characteristics and features of the hardware device in question. These files are consistently generalized and documented in the IIO ABI documentation. In order to determine which IIO deviceX corresponds to which hardware device, the user can read the name file /sys/bus/iio/devices/iio:deviceX/name. In case the sequence in which the iio device drivers are loaded/registered is constant, the numbering is constant and may be known in advance.
 This device can be found under **/sys/bus/iio/devices/**

::

   root:/> **cd /sys/bus/iio/devices/**
   root:/sys/bus/iio/devices> ls
   iio:device0

   root:/sys/bus/iio/devices> **cd iio:device0**

   root@analog:/sys/bus/iio/devices/iio:device0# **ls -l**
   total 0
   -r--r--r-- 1 root root 4096 Oct 26 22:20 name
   lrwxrwxrwx 1 root root    0 Oct 26 22:20 of_node -> ../../../../firmware/devicetree/base/admfm2000
   -rw-r--r-- 1 root root 4096 Oct 26 22:20 out_voltage0_hardwaregain
   -rw-r--r-- 1 root root 4096 Oct 26 22:20 out_voltage1_hardwaregain
   drwxr-xr-x 2 root root    0 Oct 26 22:20 power
   lrwxrwxrwx 1 root root    0 Oct 26 22:20 subsystem -> ../../../../bus/iio
   -rw-r--r-- 1 root root 4096 Oct 26 22:20 uevent
   -r--r--r-- 1 root root 4096 Oct 26 22:20 waiting_for_supplier
   root@analog:/sys/bus/iio/devices/iio:device0# 

Show device name
----------------

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device0# cat name
      **admfm2000**
   


Set ChannelY Gain
-----------------

| /sys/bus/iio/devices/iio:deviceX/out_voltageY_hardwaregain
| Hardware applied gain factor. If shared across all channels, <type>_hardwaregain is used.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device0#**cat out_voltage0_hardwaregain**
      -31.000000 dB
   
      root@analog:/sys/bus/iio/devices/iio:device0#**echo -10 > out_voltage0_hardwaregain**
      root@analog:/sys/bus/iio/devices/iio:device0#**cat out_voltage0_hardwaregain**
      -10.000000 dB
   


More Information
================

-  IIO mailing list: linux-iio@vger.kernel.org
-  `IIO Linux Kernel Documentation sysfs-bus-iio-\* <https://www.kernel.org/doc/Documentation/ABI/testing>`_
-  `IIO Documentation <https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-bus-iio>`_
-  :doc:`IIO test and visualization application </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`libiio - IIO system library </wiki-migration/resources/tools-software/linux-software/libiio>`
-  :doc:`libiio - Internals </wiki-migration/resources/tools-software/linux-software/libiio_internals>`
-  :doc:`Pointers and good books </wiki-migration/resources/tools-software/pointers>`
-  `IIO High Speed <https://events.static.linuxfound.org/sites/events/files/slides/iio_high_speed.pdf>`_
-  `Software Defined Radio using the IIO framework <http://video.fosdem.org/2015/devroom-software_defined_radio/iiosdr.mp4>`_
-

|libiio introduction|

.. image:: https://wiki.analog.com/_media/page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn
   :alt: page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn

.. |libiio introduction| image:: https://wiki.analog.com/_media/youtube>p_VntEwUe24

