Managing Gain
=============

The ADALM-PLUTO has a sophisticated gain control.

Conclusion
==========

::

   # cat fo
   #!/bin/sh
   iio_attr -D ad9361-phy adi,agc-outer-thresh-low $(expr $1 + 7)
   iio_attr -D ad9361-phy adi,agc-inner-thresh-low $(expr $1 + 1)
   iio_attr -D ad9361-phy adi,agc-inner-thresh-high $(expr $1 - 1)
   iio_attr -D ad9361-phy adi,agc-outer-thresh-high $(expr $1 - 6)
   iio_attr -D ad9361-phy initialize 1 
