iio_readdev
===========

``iio_readdev`` is part of the `Libiio <https://wiki.analog.com/../libiio>`_ package, a library that has been developed to ease the development of software interfacing Linux Industrial I/O (IIO) devices. There are four main userspace helper/utilities:

-  :doc:`iio_attr </wiki-migration/resources/tools-software/linux-software/libiio/iio_attr>` : read and write IIO attributes
-  :doc:`iio_info </wiki-migration/resources/tools-software/linux-software/libiio/iio_info>` : dump the IIO attributes
-  :doc:`iio_readdev </wiki-migration/resources/tools-software/linux-software/libiio/iio_readdev>` : read an IIO buffer device
-  :doc:`iio_writedev </wiki-migration/resources/tools-software/linux-software/libiio/iio_writedev>` : write an IIO buffer device
-  :doc:`iio_reg </wiki-migration/resources/tools-software/linux-software/libiio/iio_reg>` : read or write SPI or I2C registers in an IIO device (useful to debug drivers)

::

   analog@imhotep:~$ **iio_readdev -h**
   Usage:
       iio_readdev [-n <hostname>] [-t <trigger>] [-T <timeout-ms>] [-b <buffer-size>] [-s <samples>] <iio_device> [<channel> ...]

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
               Number of samples to capture, 0 = infinite. Default is 0.
       -T, --timeout
               Buffer timeout in milliseconds. 0 = no timeout
       -a, --auto
               Scan for available contexts and if only one is available use it.

a quick example, captures 4 frames of 256 samples, (1024 samples in total), from the receive side of the ADALM-PLUTO.

-  find the device:``analog@imhotep:~/github/libiio/build$ **iio_info -s**
   Library version: 0.9 (git tag: 263bd08)
   Compiled with backends: local xml ip usb serial
   Available contexts:
       0: 0456:b673 (Analog Devices Inc. PlutoSDR (ADALM-PLUTO)), serial=104473222a87000c0a000e009b8ed5102e [usb:3.80.5]``
-  find the streaming device ``analog@imhotep:~$ **iio_attr -u usb:3.80.5 -s -c *ad* **
   dev 'cf-ad9361-dds-core-lpc', channel 'voltage0' (output, index: 0, format: le:S16/16>>0)
   dev 'cf-ad9361-dds-core-lpc', channel 'voltage1' (output, index: 1, format: le:S16/16>>0)
   dev 'cf-ad9361-lpc', channel 'voltage0' (input, index: 0, format: le:S12/16>>0)
   dev 'cf-ad9361-lpc', channel 'voltage1' (input, index: 1, format: le:S12/16>>0)``\ In this case (which happens to use the ADALM-PLUTO, it is ``cf-ad9361-lpc`` for the input (rx), and ``cf-ad9361-dds-core-lpc`` for the output.
-  put the device into Digital loopback mode, so we know what we should be seeing\ ``analog@imhotep:~$ **iio_attr -u usb:3.80.5  -D ad9361-phy loopback 1**
   dev 'ad9361-phy', debug attr 'loopback', value :'0'
   wrote 2 bytes to loopback
   dev 'ad9361-phy', debug attr 'loopback', value :'1'``
-  set the DDS to something slow, so it is easier to see, and we don't alias when looking at things in the time domain.\ ``analog@imhotep:~$ **iio_attr -a -c cf-ad9361-dds-core-lpc altvoltage0 frequency 50000**
   Using auto-detected IIO context at URI "usb:2.26.5"
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage0' (output), id 'TX1_I_F1', attr 'frequency', value '9279985'
   wrote 5 bytes to frequency
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage0' (output), id 'TX1_I_F1', attr 'frequency', value '50034'

   analog@imhotep:~$ **iio_attr -a -c cf-ad9361-dds-core-lpc altvoltage2 frequency 50000**
   Using auto-detected IIO context at URI "usb:2.26.5"
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage2' (output), id 'TX1_I_F2', attr 'frequency', value '9279985'
   wrote 5 bytes to frequency
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage2' (output), id 'TX1_I_F2', attr 'frequency', value '50034'``
-  set the amplitude of the DDS, so you know what it is:``analog@imhotep:~$ **iio_attr -a -c cf-ad9361-dds-core-lpc altvoltage0 scale 0.4**
   Using auto-detected IIO context at URI "usb:2.26.5"
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage0' (output), id 'TX1_I_F1', attr 'scale', value '0.000000'
   wrote 4 bytes to scale
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage0' (output), id 'TX1_I_F1', attr 'scale', value '0.400024'

   analog@imhotep:~$ **iio_attr -a -c cf-ad9361-dds-core-lpc altvoltage1 scale 0.0**
   Using auto-detected IIO context at URI "usb:2.26.5"
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage1' (output), id 'TX1_I_F2', attr 'scale', value '0.000000'
   wrote 4 bytes to scale
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage1' (output), id 'TX1_I_F2', attr 'scale', value '0.000000'

   analog@imhotep:~$ **iio_attr -a -c cf-ad9361-dds-core-lpc altvoltage2 scale 0.4**
   Using auto-detected IIO context at URI "usb:2.26.5"
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage2' (output), id 'TX1_I_F2', attr 'scale', value '0.000000'
   wrote 4 bytes to scale
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage2' (output), id 'TX1_I_F2', attr 'scale', value '0.400024'

   analog@imhotep:~$ **iio_attr -a -c cf-ad9361-dds-core-lpc altvoltage3 scale 0.0**
   Using auto-detected IIO context at URI "usb:2.26.5"
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage3' (output), id 'TX1_I_F2', attr 'scale', value '0.000000'
   wrote 4 bytes to scale
   dev 'cf-ad9361-dds-core-lpc', channel 'altvoltage3' (output), id 'TX1_I_F2', attr 'scale', value '0.000000'``
-  Set the sample rate to something reasonable for the DDS frequency\ ``analog@imhotep:~$ **iio_attr -a -i -c ad9361-phy voltage0 sampling_frequency 3000000**
   Using auto-detected IIO context at URI "usb:2.29.5"
   dev 'ad9361-phy', channel 'voltage0' (input), attr 'sampling_frequency', value '3000000'
   wrote 8 bytes to sampling_frequency
   dev 'ad9361-phy', channel 'voltage0' (input), attr 'sampling_frequency', value '3000000'``
-  capture 1024 samples in 256 sample buffers ``analog@imhotep:~$ **iio_readdev -u usb:3.80.5 -b 256 -s 1024 cf-ad9361-lpc > samples.dat**``
-  check the data via ``hexdump``:``analog@imhotep:~$ **hexdump -d ./samples.dat | less**
   0000000   64086   65499   64097   65352   64124   65206   64165   65064
   0000010   64220   64926   64289   64794   64371   64670   64466   64555
   0000020   64572   64451   64688   64358   64813   64278   64946   64211
   0000030   65085   64158   65228   64119   65374   64095   65520   64086
   0000040   00131   64092   00277   64113   00421   64148   00561   64199
   0000050   00695   64263   00822   64341   00940   64431   01048   64533
   0000060   01145   64646   01230   64768   01302   64898   01360   65035
   0000070   01404   65177   01433   65322   01448   65468   01447   00079
   0000080   01431   00225   01401   00370   01356   00512   01296   00648``
-  plot the results in gnuplot:``analog@imhotep:~$ **gnuplot**
   gnuplot> **plot 'samples.dat' binary format='%short%short' using 1 with lines, 'samples.dat' binary format='%short%short' using 2 with lines**``\

   |image1|

-  If you can see discontinuities then the sample rate is too high, so check that.\ ``analog@imhotep:~$ **iio_attr -a -i -c ad9361-phy voltage0 sampling_frequency**
   dev 'ad9361-phy', channel 'voltage0' (input), attr 'sampling_frequency', value '30720000'``\ You can expect that 30.72 MSPS is too fast to stream over USB with zero gaps between buffers. Increasing the buffer length is the best thing to do.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/sine_wave_pluto.png
   :width: 600px
