FMC FRU EEPROM Utility
======================

The `FMC specification <http://www.vita.com/fmc>`__ includes a methodology where FMC mezzanine modules must provide hardware definition information that can be read by an external controller on the FMC Carrier platform (most of the time the FPGA on the carrier). This hardware definition is defined by FRU (Field Replaceable Unit) Information storage recorders, as defined in the `Intel Platform Management FRU Information Storage Definition V1.1 <https://www.intel.com/content/www/us/en/servers/ipmi/information-storage-definition.html>`__

The FRU Information is used to primarily to provide ‘inventory’ information about the boards that the FRU information device is located on. All FMC mezzanine modules include an EEPROM where this FRU Information, including the part number, version number, serial number can be read through software.

There are some extensions, or FMC-specific MultiRecords, that the FMC specification includes to help define connector requirements, power requirements, and other I2C devices which may be on the FMC mezzanine module to help the carrier platform ensure it is compatible with the mezzanine modules before it applies power. This means that if this EEPROM is blank, or has corrupt data in it, it could be that the carrier platform will not power the FMC slot at all.

In order to better use this data, Analog Devices has written a small utility which dumps the FRU file which can be found on many systems. It also can change the serial number and date (since we use this for production test of ADI's FMC cards).

::

   **NAME**
          fru-dump - print and manipulate FRU file information

   **SYNOPSIS**
          fru-dump [-b] [-c] [-p] [-o OUTPUT_FILE] [-s SERIAL_NUMBER] [-d DATE] [-i ] INPUT_FILE

   **DESCRIPTION**

   dump information about FRU files for FMC Cards
     file options
       -i  input file
       -o  output file, only makes sense when changing something
     dump info
       -b  dump board info
       -c  dump connector info
       -p  dump power supply info
       -2  dump I2C info
       -v  verbose (show warnings)
     set info (modifies output file)
       -d <num>    set date (Number of minutes from 0:00 hrs 01Jan1996)
       -d <date>   set date (Date in RFC3339 format: 2012-12-21T15:12:30-05:00)
       -d now      set the date to the current time
       -s <str>    set serial number (string)
       -t <str>    set tuning parameters
       -6          force output to be in 6-bit ASCII

Installing the FRUDump utility
------------------------------

The source code for the FRUDump utility is found at `Github <https://github.com/analogdevicesinc/fru_tools>`__.

Finding the eeprom
------------------

.. container:: box bggreen fgblack

   This specifies a root shell prompt running on the target, where the FMC module is attached

   
   ::
   
      # **find /sys -name eeprom**
      /sys/bus/i2c/devices/0-0051/eeprom
      #
   


The FRU EEPROM responds to I2C Slave address 0x51.

Dump FRU Board Information
--------------------------

.. container:: box bggreen fgblack

   This specifies any shell prompt running on the target

   
   ::
   
      # **fru-dump -i /sys/bus/i2c/devices/0-0051/eeprom -b**
      read 256 bytes from /sys/bus/i2c/devices/0-0051/eeprom
      Date of Man  : Tue Sep 18 16:30:00 2012
      Manufacture  : Analog Devices
      Product Name : FMC Comms 1
      Serial Number: D836081
      Part Number  : AD-FMCOMMS1-EBZ
      Board Rev    : B
   


Dump FRU Power Information
--------------------------

.. container:: box bggreen fgblack

   This specifies any shell prompt running on the target

   
   ::
   
      # **fru-dump -i /sys/bus/i2c/devices/0-0051/eeprom -p**
      read 256 bytes from /sys/bus/i2c/devices/0-0051/eeprom
      DC Load
        Output number: 0 (P1 VADJ)
        Nominal Volts:         2500 (mV)
        minimum voltage:       1800 (mV)
        maximum voltage:       2500 (mV)
        Ripple and Noise pk-pk 0000 (mV)
        Minimum current load   0000 (mA)
        Maximum current load   0000 (mA)
      DC Load
        Output number: 1 (P1 3P3V)
        Nominal Volts:         3300 (mV)
        minimum voltage:       2970 (mV)
        maximum voltage:       3630 (mV)
        Ripple and Noise pk-pk 0000 (mV)
        Minimum current load   0000 (mA)
        Maximum current load   3000 (mA)
      DC Load
        Output number: 2 (P1 12P0V)
        Nominal Volts:         12000 (mV)
        minimum voltage:       10800 (mV)
        maximum voltage:       13200 (mV)
        Ripple and Noise pk-pk 0000 (mV)
        Minimum current load   0000 (mA)
        Maximum current load   1000 (mA)
      DC Output
        Output Number: 3 (P1 VIO_B_M2C)
        Nominal volts:              0 (mV)
        Maximum negative deviation: 0 (mV)
        Maximum positive deviation: 0 (mV)
        Ripple and Noise pk-pk:     0 (mV)
        Minimum current draw:       0 (mA)
        Maximum current draw:       0 (mA)
      DC Output
        Output Number: 4 (P1 VREF_A_M2C)
        Nominal volts:              0 (mV)
        Maximum negative deviation: 0 (mV)
        Maximum positive deviation: 0 (mV)
        Ripple and Noise pk-pk:     0 (mV)
        Minimum current draw:       0 (mA)
        Maximum current draw:       0 (mA)
      DC Output
        Output Number: 5 (P1 VREF_B_M2C)
        Nominal volts:              0 (mV)
        Maximum negative deviation: 0 (mV)
        Maximum positive deviation: 0 (mV)
        Ripple and Noise pk-pk:     0 (mV)
        Minimum current draw:       0 (mA)
        Maximum current draw:       0 (mA)
   


Dump FRU Connector Information
------------------------------

.. container:: box bggreen fgblack

   This specifies any shell prompt running on the target

   
   ::
   
      # **fru-dump -i /sys/bus/i2c/devices/0-0051/eeprom -c**
      read 256 bytes from /sys/bus/i2c/devices/0-0051/eeprom
      Single Width Card
      P1 is LPC
      P1 Bank A Signals needed 68
      P1 Bank B Signals needed 0
      P1 GBT Transceivers needed 0
      Max JTAG Clock 0
   


Set tuning parameters
---------------------

A tuning (or calibration) parameter for the related board can be written to the EEPROM as seen below. Usually this is integer or floating point values encoded as a raw hex string that is then decoded where it's used such as in IIO Oscilloscope or wherever the parameter needs to be set.

.. container:: box bggreen fgblack

   This specifies any shell prompt running on the target

   
   ::
   
      # **fru-dump -i /sys/bus/i2c/devices/0-0051/eeprom -o /sys/bus/i2c/devices/0-0051/eeprom -t 0b10db**
      read 256 bytes from /sys/bus/i2c/devices/0-0051/eeprom
      changing tuning parameter to 0b10db
   


For Help
--------

For help and assistance with the tool, check out :ez:`the EngineerZone <community/linux-device-drivers/linux-software-drivers>`.
