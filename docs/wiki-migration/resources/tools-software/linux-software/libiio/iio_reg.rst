iio_reg
=======

``iio_reg`` is part of the `Libiio <https://wiki.analog.com/../libiio>`__ package, a library that has been developed to ease the development of software interfacing Linux Industrial I/O (IIO) devices. There are four main userspace helper/utilities:

-  :doc:`iio_attr </wiki-migration/resources/tools-software/linux-software/libiio/iio_attr>` : read and write IIO attributes
-  :doc:`iio_info </wiki-migration/resources/tools-software/linux-software/libiio/iio_info>` : dump the IIO attributes
-  :doc:`iio_readdev </wiki-migration/resources/tools-software/linux-software/libiio/iio_readdev>` : read an IIO buffer device
-  :doc:`iio_writedev </wiki-migration/resources/tools-software/linux-software/libiio/iio_writedev>` : write an IIO buffer device
-  :doc:`iio_reg </wiki-migration/resources/tools-software/linux-software/libiio/iio_reg>` : read or write SPI or I2C registers in an IIO device (useful to debug drivers)

::

   analog@imhotep:~$ **iio_reg** -h
   Usage:

   iio_reg <device> <register> [<value>]

Running Remote
--------------

The ``iio_reg`` application can also connect to a libiio remote device via IP. Prior in running ``iio_reg`` set the ``IIOD_REMOTE`` environmental variable.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the host or target

   
   ::
   
      > **export IIOD_REMOTE=IP address of the remote platform**
   


Finding
-------

An IIO context can have multiple logical devices, and sometimes not all devices will have a specific register interface. To find out which IIO device support register access, try (remember that ``iio_attr`` supports a ``-D`` option to look for debug attributes).

::

   # **iio_attr  -u ip:192.168.2.1 -D**
   IIO context has 4 devices:
       iio:device0, ad9361-phy: found 179 debug attributes
       iio:device1, xadc: found 0 debug attributes
       iio:device2, cf-ad9361-dds-core-lpc: found 1 debug attributes
       iio:device3, cf-ad9361-lpc: found 2 debug attributes

   # **iio_attr  -u ip:192.168.2.1 -D . direct_reg_access**
   dev 'ad9361-phy', debug attr 'direct_reg_access', value :'0x0'
   dev 'cf-ad9361-dds-core-lpc', debug attr 'direct_reg_access', value :'0x90162'
   dev 'cf-ad9361-lpc', debug attr 'direct_reg_access', value :'0x0'

From here you can see the three different devices that support the ``iio_reg`` tool.

Example
-------

::

   # iio_reg ad9361-phy 0x3
   0x5c
