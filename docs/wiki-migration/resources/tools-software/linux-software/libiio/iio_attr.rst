iio_attr
========

``iio_attr`` is part of the `Libiio <https://wiki.analog.com/../libiio>`__ package, a library that has been developed to ease the development of software interfacing Linux Industrial I/O (IIO) devices. There are four main userspace helper/utilities:

-  :doc:`iio_attr </wiki-migration/resources/tools-software/linux-software/libiio/iio_attr>` : read and write IIO attributes
-  :doc:`iio_info </wiki-migration/resources/tools-software/linux-software/libiio/iio_info>` : dump the IIO attributes
-  :doc:`iio_readdev </wiki-migration/resources/tools-software/linux-software/libiio/iio_readdev>` : read an IIO buffer device
-  :doc:`iio_writedev </wiki-migration/resources/tools-software/linux-software/libiio/iio_writedev>` : write an IIO buffer device
-  :doc:`iio_reg </wiki-migration/resources/tools-software/linux-software/libiio/iio_reg>` : read or write SPI or I2C registers in an IIO device (useful to debug drivers)

::

   analog@imhotep:~$ **iio_attr -h**
   Usage:
           iio_attr [OPTION]...    -d [device] [attr] [value]
                                   -c [device] [channel] [attr] [value]
                                   -B [device] [attr] [value]
                                   -D [device] [attr] [value]
                                   -C [attr]
   Options:
           -h, --help           : Show this help and quit.
           -I, --ignore-case    : Ignore case distinctions.
           -q, --quiet          : Return result only.
           -a, --auto           : Use the first context found.
   Optional qualifiers:
           -u, --uri            : Use the context at the provided URI.
           -i, --input-channel  : Filter Input Channels only.
           -o, --output-channel : Filter Output Channels only.
   Attribute types:
           -s, --scan-channel   : Filter Scan Channels only.
           -d, --device-attr    : Read/Write device attributes
           -c, --channel-attr   : Read/Write channel attributes.
           -C, --context-attr   : Read IIO context attributes.
           -B, --buffer-attr    : Read/Write buffer attributes.
           -D, --debug-attr     : Read/Write debug attributes.

Examples
--------

Look at Context Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   rgetz@brain:~/github/libiio$ **iio_attr -a -C**
   Using auto-detected IIO context at URI "usb:3.8.5"
   IIO context with 14 attributes:
   hw_model: Analog Devices PlutoSDR Rev.B (Z7010-AD9364)
   hw_model_variant: 0
   hw_serial: 104473222a87000618000600473ed57ae0
   fw_version: v0.31
   ad9361-phy,xo_correction: 40000000
   ad9361-phy,model: ad9364
   local,kernel: 4.14.0-42540-g387d584
   usb,idVendor: 0456
   usb,idProduct: b673
   usb,release: 2.0
   usb,vendor: Analog Devices Inc.
   usb,product: PlutoSDR (ADALM-PLUTO)
   usb,serial: 104473222a87000618000600473ed57ae0
   usb,libusb: 1.0.22.11312

List Devices in a Context
~~~~~~~~~~~~~~~~~~~~~~~~~

::

   rgetz@brain:~/github/libiio$ **iio_attr -u usb:3.8.5 -d**
   IIO context has 5 devices:
       iio:device0: adm1177, found 0 device attributes
       iio:device1: ad9361-phy, found 18 device attributes
       iio:device2: xadc, found 1 device attributes
       iio:device3: cf-ad9361-dds-core-lpc, found 0 device attributes
       iio:device4: cf-ad9361-lpc, found 0 device attributes

::

   rgetz@brain:~/github/libiio$ **iio_attr -u usb:3.8.5 -c**
   IIO context has 5 devices:
       iio:device0: adm1177, found 2 channels
       iio:device1: ad9361-phy, found 9 channels
       iio:device2: xadc, found 10 channels
       iio:device3: cf-ad9361-dds-core-lpc, found 6 channels
       iio:device4: cf-ad9361-lpc, found 2 channels

List Channel attributes
~~~~~~~~~~~~~~~~~~~~~~~

the ``.`` can be used as a wildcard if you don't know the name.

::

   rgetz@brain:~/github/libiio$ **iio_attr -u ip:192.168.2.1 -c adm1177 .**
   dev 'adm1177', channel 'voltage0' (input), attr 'raw', value '771'
   dev 'adm1177', channel 'voltage0' (input), attr 'scale', value '6.433105468'
   dev 'adm1177', channel 'current0' (input), attr 'raw', value '776'
   dev 'adm1177', channel 'current0' (input), attr 'scale', value '0.516601562'

Read a channel attributes
~~~~~~~~~~~~~~~~~~~~~~~~~

::

   rgetz@brain:~/github/libiio$ **iio_attr -u ip:192.168.2.1 -c ad9361-phy RX_LO**
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'external', value '0'
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'fastlock_load', value '0'
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'fastlock_recall', ERROR: Invalid argument (-22)
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'fastlock_save', value '0 242,198,163,125,228,163,171,195,167,187,179,163,241,167,187,167'
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'fastlock_store', value '0'
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'frequency', value '2400000000'
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'frequency_available', value '[70000000 1 6000000000]'
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'powerdown', value '0'

::

   rgetz@brain:~/github/libiio$ **iio_attr -u ip:192.168.2.1 -c ad9361-phy RX_LO frequency**
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'frequency', value '2400000000'

Write to a channel attribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   rgetz@brain:~/github/libiio$ **iio_attr -u ip:192.168.2.1 -c ad9361-phy RX_LO frequency 2400000100**
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'frequency', value '2400000000'
   wrote 11 bytes to frequency
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'frequency', value '2400000100'
