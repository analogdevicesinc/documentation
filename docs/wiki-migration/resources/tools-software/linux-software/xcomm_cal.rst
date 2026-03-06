AD-FMCOMMS1-EBZ Calibration EEPROM Utility
==========================================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



::

   **NAME**
          xcomm_cal - print and set EEPROM calibration data

   **SYNOPSIS**
          xcomm_cal [-s] [-f FREQUENCY] INPUT_FILE

   **DESCRIPTION**
       Print and set EEPROM calibration data. 
       Without option - print all calibration sets available.

       -f Target frequency in MHz

       -s Initialize device drivers with best match calibration set.
          This option is used together with the -f option.

Download/Install
----------------

Git: https://github.com/analogdevicesinc/fmcomms1-eeprom-cal

::

   root@linaro-ubuntu-desktop:~# **git clone https://github.com/analogdevicesinc/fmcomms1-eeprom-cal.git**
   root@linaro-ubuntu-desktop:~# **cd fmcomms1-eeprom-cal**
   root@linaro-ubuntu-desktop:~# **make**
   root@linaro-ubuntu-desktop:~# **make install**

Find the EEPROM
---------------

Normally, the calibration EEPROM responds to I2C Slave address 0x55, but it depends on the hardware carrier, and the slot that the card is plugged into.

To find the eeprom - use the ``find`` command.

::

   root@linaro-ubuntu-desktop:~# **find /sys/ -name eeprom**
   /sys/devices/amba.1/41600000.i2c/i2c-1/1-0050/eeprom
   /sys/devices/amba.1/41600000.i2c/i2c-1/1-0054/eeprom

It's normally the largest value. (the smaller value is the :doc:`FRU eeprom </wiki-migration/resources/tools-software/linux-software/fru_dump>`).

Query best match calibration set for a given Frequency
------------------------------------------------------

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      # **xcomm_cal -f 2400 -s /sys/bus/i2c/devices/0-0055/eeprom**
   
      --- Best match ENTRY 1 ---
      Calibration Frequency:  2400 MHz
      DAC I Phase Adjust:             357
      DAC Q Phase Adjust:             0
      DAC I Offset:           214
      DAC Q Offset:           25
      DAC I Full Scale Adj:   401
      DAC Q Full Scale Adj:   401
      ADC I Offset:           -2
      ADC Q Offset:           -34
      ADC I Gain Adj: 32853
      ADC Q Gain Adj: 32768
   

