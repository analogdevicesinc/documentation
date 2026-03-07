ADALM-PLUTO Performance Metrics
===============================

Receiver
--------

Transmitter
-----------

Data Throughput
---------------

Via IIOD USB backend

::

   iio_readdev -u usb:1.100.5 -b 100000 cf-ad9361-lpc | pv > /dev/null
   210GiB 1:19:51 [**26,1MiB/s**] [     <=>     

Via IIOD Network backend with RNDIS

::

   iio_readdev -n 192.168.2.1 -b 100000 cf-ad9361-lpc | pv > /dev/null
   203MiB 0:00:10 [**20,4MiB/s**] [              <=>  

Via local IIO device (running on Linux inside PLUTO, with self-compiled pv(1))

::

   iio_readdev -u local: -b 100000 cf-ad9361-lpc | pv > /dev/null
   13.5GiB 0:02:09 [** 107MiB/s**] [                           <=>                    ]
