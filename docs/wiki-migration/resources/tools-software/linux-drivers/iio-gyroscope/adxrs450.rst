ADXRS450 IIO Gyroscope Linux Driver
===================================

Supported Devices
-----------------

-  :adi:`ADXRS450`
-  :adi:`ADXRS453`

Evaluation Boards
-----------------

-  :adi:`EVAL-ADXL313-Z-M`
-  :adi:`EVAL-ADXRS450Z`
-  :adi:`EVAL-ADXRS453Z`
-  `PmodGYRO2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-GYRO2>`__

ADXRS450: ±300°/sec High Vibration Immunity Digital Gyro
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/scrape>adi>ADXRS450#additional-details__paragraph
   :alt: scrape>adi>ADXRS450#additional-details\__paragraph

-  :adi:`Product Page <ADXRS450>`

ADXRS453: ±300°/sec High Vibration Immunity Digital Gyro
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/scrape>adi>ADXRS453#additional-details__paragraph
   :alt: scrape>adi>ADXRS453#additional-details\__paragraph

-  :adi:`Product Page <ADXRS453>`

Adding ADXRS450 to the Kernel
=============================

To add support for the ADXRS450 to the kernel build system, a few things must be enabled properly for things to work.The configuration is as following:

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or "make qconfig")

.. hint::

   The ADXRS450 Driver depends on **CONFIG_SPI**


::

   Linux Kernel Configuration
     Device Drivers  --->
           <*>     Industrial I/O support  --->
             <M>   Analog Devices ADXRS450/3 Digital Output Gyroscope SPI driver

Source Code
===========

Status
------

+------------------------------------------------------+------------------------------------------------------+
| Source                                               | Mainlined?                                           |
+======================================================+======================================================+
| `git </git.linux.org>drivers/iio/gyro/adxrs450.c>`__ | `Yes </git.linux.org>drivers/iio/gyro/adxrs450.c>`__ |
+------------------------------------------------------+------------------------------------------------------+

Files
-----

+----------+----------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                 |
+==========+======================================================================================================================+
| driver   | `adxrs450.c <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/gyro/adxrs450.c>`__ |
+----------+----------------------------------------------------------------------------------------------------------------------+

Example platform device initialization
======================================

Below is an example which is used on Blackfin board file.

Unlike PCI or USB devices, SPI devices are not enumerated at the hardware level. Instead, the software must know which devices are connected on each SPI bus segment, and what slave selects these devices are using. For this reason, the kernel code must instantiate SPI devices explicitly. The most common method is to declare the SPI devices by bus number.

This method is appropriate when the SPI bus is a system bus, as in many embedded systems, wherein each SPI bus has a number which is known in advance. It is thus possible to pre-declare the SPI devices that inhabit this bus. This is done with an array of struct spi_board_info, which is registered by calling spi_register_board_info().

For more information see: `spi-summary.rst <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/spi/spi-summary.rst>`__


.. code:: c

   static struct spi_board_info board_spi_board_info[] __initdata = {
   #if defined(CONFIG_ADXRS450) \
       || defined(CONFIG_ADXRS450_MODULE)
       {
           .modalias = "adxrs450",
           .bus_num = 0,
           .chip_select = GPIO_PF10 + MAX_CTRL_CS, /* GPIO controlled SSEL */
           .max_speed_hz = 2000000,
           .mode = SPI_MODE_0,
       },
   #endif
   };

.. code:: c

   static int __init board_init(void)
   {
       [--snip--]

       spi_register_board_info(board_spi_board_info, ARRAY_SIZE(board_spi_board_info));

       [--snip--]

       return 0;
   }
   arch_initcall(board_init);

Hardware configuration
======================

.. image:: https://wiki.analog.com/_media/software/driver/linux/adxrs450_eval_lr.jpg
   :alt: EVAL-ADXRS450
   :align: left
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/iio-gyroscope/pmodgyro2_lr.jpg
   :alt: PmodGYRO2
   :align: left
   :width: 600px

Driver testing
==============

Module loading
^^^^^^^^^^^^^^

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/> **modprobe adxrs450**
      adxrs450 spi0.18: The Part ID is 0x5201
      adxrs450 spi0.18: The Serial Number is 0xbaf2
   


Each and every IIO device, typically a hardware chip, has a device folder under /sys/bus/iio/devices/iio:deviceX. Where X is the IIO index of the device. Under every of these directory folders reside a set of files, depending on the characteristics and features of the hardware device in question. These files are consistently generalized and documented in the IIO ABI documentation. In order to determine which IIO deviceX corresponds to which hardware device, the user can read the name file /sys/bus/iio/devices/iio:deviceX/name. In case the sequence in which the iio device drivers are loaded/registered is constant, the numbering is constant and may be known in advance.


.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/> **cd /sys/bus/iio/devices/**
      root:/sys/bus/iio/devices> ls
      iio:device0 
      root:/sys/bus/iio/devices> **cd iio:device0 **
   
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0 > **ls -l**
      -r--r--r--    1 root     root          4096 Jan  3 16:24 dev
      -rw-r--r--    1 root     root          4096 Jan  3 16:24 in_anglvel_z_calibbias
      -rw-r--r--    1 root     root          4096 Jan  3 16:24 in_anglvel_z_quadrature_correction_raw
      -r--r--r--    1 root     root          4096 Jan  3 16:24 in_anglvel_z_raw
      -rw-r--r--    1 root     root          4096 Jan  3 16:24 in_anglvel_z_scale
      -r--r--r--    1 root     root          4096 Jan  3 16:24 in_temp0_raw
      -rw-r--r--    1 root     root          4096 Jan  3 16:24 in_temp0_scale
      -r--r--r--    1 root     root          4096 Jan  3 16:24 name
      drwxr-xr-x    2 root     root             0 Jan  3 16:24 power
      lrwxrwxrwx    1 root     root             0 Jan  3 16:24 subsystem -> ../../../../../bus/iio
      -rw-r--r--    1 root     root          4096 Jan  3 16:24 uevent
   


Show device name
^^^^^^^^^^^^^^^^

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0> **cat name**
      adxrs450
   


Show angular rate scale
^^^^^^^^^^^^^^^^^^^^^^^

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0> **cat in_anglvel_z_scale**
      0.000218166
   


Show angular rate
^^^^^^^^^^^^^^^^^

Rotate the device and read angular rate sampling values from sysfs nodes like this:

Rotate in positive direction
""""""""""""""""""""""""""""

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0 > **cat in_anglvel_z_raw**
      42
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0 > **cat in_anglvel_z_raw**
      1456
   


Rotate in negative direction
""""""""""""""""""""""""""""

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0 > **cat in_anglvel_z_raw**
      -1657
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0 > **cat in_anglvel_z_raw**
      -17215
   


Show quadrature correction
^^^^^^^^^^^^^^^^^^^^^^^^^^

This attribute is used to read the amount of quadrature error present in the device at a given time.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0 > **cat in_anglvel_z_quadrature_correction_raw**
      9
   


Set dynamic null correction
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This attribute is used to make small adjustments to the rateout of the device. This 10-bit value allows the user to adjust the static rateout of the device by up to ±6.4°/sec.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0 > **cat in_gyro_z_raw**
      40
   
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0 > **echo 40 > in_anglvel_z_calibbias**
   
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0 > **cat in_anglvel_z_raw**
      1
   


Show temperature
^^^^^^^^^^^^^^^^

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0> **cat in_temp0_scale**
      200
      root:/sys/devices/platform/bfin-spi.0/spi0.18/iio:device0> **cat in_temp0_raw**
      105
   


**T** = *in_temp0_raw* \* *in_temp0_scale* = 105 \* 200 = 21000 milli degree Celsius

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

