.. _software fru-dump-tool:

FMC FRU EEPROM Utility
===============================================================================

The FMC specification requires FMC mezzanine modules to provide hardware
definition information through FRU (Field Replaceable Unit) Information storage,
as defined in the "Intel Platform Management FRU Information Storage Definition
V1.1."

The FRU Information is used primarily to provide inventory information about the
boards, including part numbers, version numbers, and serial numbers.
FMC-specific MultiRecords define connector requirements, power requirements, and
I2C devices to ensure carrier platform compatibility before power application.

Analog Devices developed the ``fru-dump`` utility to dump and modify FRU files,
particularly for production testing of ADI FMC cards. Source code is available
at :git-fru_tools:`GitHub <>`.

Synopsis
-------------------------------------------------------------------------------

.. code-block::

   fru-dump [-b] [-c] [-p] [-o OUTPUT_FILE] [-s SERIAL_NUMBER] [-d DATE] [-i] INPUT_FILE

Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File options:**

- ``-i`` — input file
- ``-o`` — output file (only applicable when modifying data)

**Dump information:**

- ``-b`` — dump board info
- ``-c`` — dump connector info
- ``-p`` — dump power supply info
- ``-2`` — dump I2C info
- ``-v`` — verbose (display warnings)

**Modify information:**

- ``-d <num>`` — set date (minutes from 0:00 hrs 01Jan1996)
- ``-d <date>`` — set date (RFC3339 format: ``2012-12-21T15:12:30-05:00``)
- ``-d now`` — set date to current time
- ``-s <str>`` — set serial number
- ``-t <str>`` — set tuning parameters
- ``-6`` — force 6-bit ASCII output

Finding the EEPROM
-------------------------------------------------------------------------------

The FRU EEPROM responds to I2C Slave address 0x51.

.. code-block:: bash

   # find /sys -name eeprom
   /sys/bus/i2c/devices/0-0051/eeprom

Dump board information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # fru-dump -i /sys/bus/i2c/devices/0-0051/eeprom -b

.. code-block::

   read 256 bytes from /sys/bus/i2c/devices/0-0051/eeprom
   Date of Man  : Tue Sep 18 16:30:00 2012
   Manufacture  : Analog Devices
   Product Name : FMC Comms 1
   Serial Number: D836081
   Part Number  : AD-FMCOMMS1-EBZ
   Board Rev    : B

Dump power information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # fru-dump -i /sys/bus/i2c/devices/0-0051/eeprom -p

Example DC Load entry:

.. code-block::

   DC Load
     Output number: 1 (P1 3P3V)
     Nominal Volts:         3300 (mV)
     minimum voltage:       2970 (mV)
     maximum voltage:       3630 (mV)
     Ripple and Noise pk-pk 0000 (mV)
     Minimum current load   0000 (mA)
     Maximum current load   3000 (mA)

Dump connector information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # fru-dump -i /sys/bus/i2c/devices/0-0051/eeprom -c

.. code-block::

   read 256 bytes from /sys/bus/i2c/devices/0-0051/eeprom
   Single Width Card
   P1 is LPC
   P1 Bank A Signals needed 68
   P1 Bank B Signals needed 0
   P1 GBT Transceivers needed 0
   Max JTAG Clock 0

Set tuning parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tuning parameters (calibration values) can be written as raw hex strings:

.. code-block:: bash

   # fru-dump -i /sys/bus/i2c/devices/0-0051/eeprom -o /sys/bus/i2c/devices/0-0051/eeprom -t 0b10db

.. code-block::

   read 256 bytes from /sys/bus/i2c/devices/0-0051/eeprom changing tuning
   parameter to 0b10db
