ADAQ8092
========

| Select output format decode mode.
| - bit [0] - enables digital output randomizer decode
| - bit [1] - enables alternate bit polarity decode

AD4858
======

| Select data format/oversampling
| - bit [2] - enable oversampling
| - bits [1:0] packet format selection:

-  0 = 20 bit
-  1 = 24 bit
-  2 = 32 bit
-  3 = 32 bit

AD7606X_PI
==========

| Select the parallel interface's operation mode
| - bit [2] - change mode with the selected one
| - bits [1:0] - requested operation mode:

-  0 = SIMPLE
-  1 = CRC_ENABLED
-  2 = STATUS_HEADER
-  3 = CRC_STATUS
