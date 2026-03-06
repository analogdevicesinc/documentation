iio_writedev
============

``iio_writedev`` is part of the `Libiio <https://wiki.analog.com/../libiio>`__ package, a library that has been developed to ease the development of software interfacing Linux Industrial I/O (IIO) devices. There are four main userspace helper/utilities:

-  :doc:`iio_attr </wiki-migration/resources/tools-software/linux-software/libiio/iio_attr>` : read and write IIO attributes
-  :doc:`iio_info </wiki-migration/resources/tools-software/linux-software/libiio/iio_info>` : dump the IIO attributes
-  :doc:`iio_readdev </wiki-migration/resources/tools-software/linux-software/libiio/iio_readdev>` : read an IIO buffer device
-  :doc:`iio_writedev </wiki-migration/resources/tools-software/linux-software/libiio/iio_writedev>` : write an IIO buffer device
-  :doc:`iio_reg </wiki-migration/resources/tools-software/linux-software/libiio/iio_reg>` : read or write SPI or I2C registers in an IIO device (useful to debug drivers)

::

   analog@imhotep:~$ **iio_writedev** -h
   Usage:
           iio_writedev [-n <hostname>] [-t <trigger>] [-T <timeout-ms>] [-b <buffer-size>] [-s <samples>] <iio_device> [<channel> ...]

   Options:
           -h, --help
                           Show this help and quit.
           -n, --network
                           Use the network backend with the provided hostname.
           -u, --uri
                           Use the context with the provided URI.
           -t, --trigger
                           Use the specified trigger.
           -b, --buffer-size
                           Size of the capture buffer. Default is 256.
           -s, --samples
                           Number of samples to write, 0 = infinite. Default is 0.
           -T, --timeout
                           Buffer timeout in milliseconds. 0 = no timeout
           -a, --auto
                           Scan for available contexts and if only one is available use it.
           -c, --cyclic
                           Use cyclic buffer mode.

Example
-------

::

   # iio_readdev -b 100000 cf-ad9361-lpc | iio_writedev -b 100000 cf-ad9361-dds-core-lpc
