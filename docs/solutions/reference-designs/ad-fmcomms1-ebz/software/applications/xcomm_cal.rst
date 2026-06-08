.. _ad_fmcomms1_ebz software xcomm-cal:

Xcomm Cal
=========

.. warning::

   Analog Devices uses six designations to inform our customers where a
   semiconductor product is in its
   :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`.
   From emerging innovations to products which have been in production for
   twenty years, we understand that insight into life cycle status is important.
   Device life cycles are tracked on their individual product pages on
   `analog.com <https://www.analog.com/>`_, and should always be consulted
   before making any design decisions.

   This particular article/document/design has been retired or deprecated,
   which means it is no longer maintained or actively updated, even though the
   devices themselves may be Recommended for New Designs or in
   Production. This page is here for historical/reference purposes only.

Synopsis
--------

.. code-block:: text

   xcomm_cal [-s] [-f FREQUENCY] INPUT_FILE

Print and set EEPROM calibration data. When executed without options, it
displays all available calibration sets.

Options
-------

-f FREQUENCY
   Specifies the target frequency in MHz for calibration lookup.

-s
   Initializes device drivers using the best-matching calibration set.
   Used in conjunction with the ``-f`` option.

Installation
------------

.. code-block:: bash

   git clone https://github.com/analogdevicesinc/fmcomms1-eeprom-cal.git
   cd fmcomms1-eeprom-cal
   make
   make install

Finding the EEPROM
------------------

The calibration EEPROM typically responds to I2C slave address ``0x55``,
though this varies by hardware carrier and slot configuration. To identify it:

.. code-block:: bash

   find /sys/ -name eeprom

The largest listed path is typically the calibration EEPROM; smaller values
correspond to FRU EEPROMs.

Querying Calibration Data
-------------------------

.. code-block:: bash

   xcomm_cal -f 2400 -s /sys/bus/i2c/devices/0-0055/eeprom

This command queries calibration data for 2400 MHz and initializes device
drivers with the best-matching calibration set. The output includes adjustable
parameters such as DAC phase, offset and gain values, as well as ADC offset
and gain adjustments.
