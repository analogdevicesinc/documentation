AD3552R Dual Channel, 16-Bit, 33 MUPS, Multispan, Multi-IO SPI DAC Linux device driver
======================================================================================

The AD3552R is a low drift, dual channel, ultra-fast, 16-bit accuracy, current output digital-to-analog converter (DAC) that can be configured in multiple voltage span ranges. The AD3552R operates with a fixed 2.5 V reference. Each DAC incorporates three drift-compensating feedback resistors for the required external trans-impedance amplifier (TIA) that scales the output voltage. Offset and gain scaling registers allow for the generation of multiple output span ranges, such as 0 V to 2.5 V, 0 V to 5 V, 0 V to 10 V, −5 V to +5 V, and −10 V to +10 V, and custom intermediate ranges with full 16-bit resolution. The DAC can operate in fast mode for maximum speed or precision mode for maximum accuracy.

Supported Devices
-----------------

-  :adi:`AD3552R`

Evaluation Boards
-----------------

-  :adi:`EVAL-AD3552RFMC1Z <EVAL-AD3552R>`
-  :adi:`EVAL-AD3552RFMC2Z <EVAL-AD3552R>`

Description
-----------

This is a Linux industrial I/O (:doc:`IIO </wiki-migration/software/linux/docs/iio/iio>`) subsystem driver, targeting RF Transceivers. The industrial I/O subsystem provides a unified framework for drivers for many different types of converters and sensors using a number of different physical interfaces (i2c, spi, etc). See :doc:`IIO </wiki-migration/software/linux/docs/iio/iio>` for more information.

Source Code
===========

Status
------

+--------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Source                                                                                           | Mainlined?                                                                                      |
+==================================================================================================+=================================================================================================+
| :git-linux:`git <drivers/iio/dac/axi-ad3552r.c>`                                                 | :git-linux:`No <drivers/iio/dac/axi-ad3552r.c>`                                                 |
+--------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+

Files
-----

+----------+----------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                       |
+==========+============================================================================================================================+
| driver   | :git-linux:`drivers/iio/dac/axi-ad3552r.c`                                                                                 |
+----------+----------------------------------------------------------------------------------------------------------------------------+

Example Linux Device-Tree Initialization
========================================

Required devicetree properties:

-  compatible: Should always be "adi,axi-ad3552r"
-  clocks: define reference clock See Documentation/devicetree/bindings/clock/clock-bindings.txt

Optional properties:

-  reset-gpios : a GPIO spec for the Reset pin.

Example:

::

   &fpga_axi {
       axi_ad3552r: axi-ad3552r@44a74000 {
           compatible = "adi,axi-ad3552r";
           reg = <0x44a74000 0x1000>;

           reset-gpios = <&gpio0 92 GPIO_ACTIVE_LOW>;      
           clocks = <&ref_clk>;

           dmas = <&dac_tx_dma 0>;
           dma-names = "tx";
       };
   };

+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function                                                           | File                                                                                                                                                           |
+====================================================================+================================================================================================================================================================+
| :adi:`EVAL-AD3552R` Device Tree                                    | :git-linux:`/arch/arm/boot/dts/zynq-zed-adv7511-axi-ad3552r_evb.dts`                                                                                           |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enabling Linux driver support
=============================

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or "make qconfig")

Adding Linux driver support
===========================

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or "make qconfig")

::

   Linux Kernel Configuration
       Device Drivers  --->
       <*>     Industrial I/O support --->
           --- Industrial I/O support
           -*-   Enable ring buffer support within IIO
           -*-     Industrial I/O lock free software ring
           -*-   Enable triggered sampling support

                 *** Digital to analog converters ***
           [--snip--]

           <*>   Analog Devices AXI_AD3552R DAC driver 

           [--snip--]

Hardware configuration
======================

Driver testing / API
====================

Each and every IIO device, typically a hardware chip, has a device folder under /sys/bus/iio/devices/iio:deviceX. Where X is the IIO index of the device. Under every of these directory folders reside a set of files, depending on the characteristics and features of the hardware device in question. These files are consistently generalized and documented in the IIO ABI documentation. In order to determine which IIO deviceX corresponds to which hardware device, the user can read the name file /sys/bus/iio/devices/iio:deviceX/name. In case the sequence in which the iio device drivers are loaded/registered is constant, the numbering is constant and may be known in advance.


.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/> **cd /sys/bus/iio/devices/**
      root@analog:/sys/bus/iio/device> ls -l
   
      iio:device0 -> ../../../devices/soc0/axi/f8007100.adc/iio:device0
      iio:device1 -> ../../../devices/soc0/fpga-axi@0/44a74000.axi-ad3552r/iio:device1
      iio_sysfs_trigger -> ../../../devices/iio_sysfs_trigger
   
      root:/sys/bus/iio/devices> **cd iio:device1**
   
      root@analog:/sys/bus/iio/devices/iio:device1# ls -l
      drwxr-xr-x 2 root root    0 May 16 07:42 buffer
      drwxr-xr-x 2 root root    0 May 15 15:04 buffer0
      -r--r--r-- 1 root root 4096 May 16 07:42 dev
      -rw-r--r-- 1 root root 4096 May 16 07:42 input_source
      -r--r--r-- 1 root root 4096 May 16 07:42 input_source_available
      -r--r--r-- 1 root root 4096 May 15 15:04 name
      lrwxrwxrwx 1 root root    0 May 16 07:42 of_node -> ../../../../../firmware/devicetree/base/fpga-axi@0/axi-ad3552r@44a74000
      -rw-r--r-- 1 root root 4096 May 16 07:42 output_range
      -r--r--r-- 1 root root 4096 May 16 07:42 output_range_available
      -rw-r--r-- 1 root root 4096 May 16 07:42 out_voltage0_raw
      -rw-r--r-- 1 root root 4096 May 16 07:42 out_voltage1_raw
      drwxr-xr-x 2 root root    0 May 15 15:04 power
      -rw-r--r-- 1 root root 4096 May 16 07:42 sampling_frequency
      drwxr-xr-x 2 root root    0 May 15 15:04 scan_elements
      -rw-r--r-- 1 root root 4096 May 16 07:42 stream_status
      -r--r--r-- 1 root root 4096 May 16 07:42 stream_status_available
      lrwxrwxrwx 1 root root    0 May 16 07:42 subsystem -> ../../../../../bus/iio
      -rw-r--r-- 1 root root 4096 May 16 07:42 uevent
      root:/sys/bus/iio/devices/iio:device1#
   


Show device name
----------------

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/bus/iio/devices/iio:device1> **cat name**
      **axi-ad3552r**
   


DAC sampling rate (sampling_frequency)
--------------------------------------

Read only attribute which returns the DAC sampling rate in Hz.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device1# **cat sampling_frequency**
      **16666667**
      root@analog:/sys/bus/iio/devices/iio:device1# echo 15000000 > sampling_frequency
      -bash: echo: write error: Invalid argument
      root@analog:/sys/bus/iio/devices/iio:device1#
   


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

