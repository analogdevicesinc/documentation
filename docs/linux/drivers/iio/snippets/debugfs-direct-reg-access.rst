..
  Low level register access via debugfs (direct_reg_access)

Some IIO drivers feature an optional debug facility, allowing users to read or
write registers directly. Special care needs to be taken when using this
feature, since you can modify registers on the back of the driver.

.. tip::

   To simplify direct register access you may want to use the libiio
   :ref:`libiio cli`.

Accessing debugfs requires root privileges.

In order to identify if the IIO device in question feature this option you first
need to identify the IIO device number.

Therefore read the name attribute of each IIO device

.. shell::

   $grep "" /sys/bus/iio/devices/iio\:device*/name
    /sys/bus/iio/devices/iio:device0/name:ad7291
    /sys/bus/iio/devices/iio:device1/name:ad9361-phy
    /sys/bus/iio/devices/iio:device2/name:xadc
    /sys/bus/iio/devices/iio:device3/name:adf4351-udc-rx-pmod
    /sys/bus/iio/devices/iio:device4/name:adf4351-udc-tx-pmod
    /sys/bus/iio/devices/iio:device5/name:cf-ad9361-dds-core-lpc
    /sys/bus/iio/devices/iio:device6/name:cf-ad9361-lpc

Change directory to **/sys/kernel/debug**/iio/ iio:deviceX and check if the
direct_reg_access file exists.

.. shell::

   $cd /sys/kernel/debug/iio/iio\:device1
   /sys/kernel/debug/iio/iio:device1
   $ls direct_reg_access
    direct_reg_access

**Reading**

.. shell::

   /sys/kernel/debug/iio/iio:device1
   $echo 0x7 > direct_reg_access
   $cat direct_reg_access
    0x40

**Writing**

.. shell::

   /sys/kernel/debug/iio/iio:device1
   $echo 0x7 0x50  > direct_reg_access
   $cat direct_reg_access
    0x50

**Accessing HDL CORE registers**

Special ADI device driver convention for devices that have both:

* a SPI/I2C control interface
* and some sort of HDL Core with registers (AXI)

In this case when accessing the HDL Core Registers always set BIT31.

The register map for ADI HDL cores can be found at section "Register Map"
of each :external+hdl:ref:`library` documentation
(:external+hdl:ref:`example <i3c_controller regmap>`).

.. shell::

   /sys/kernel/debug/iio/iio:device6
   $echo 0x80000000 > direct_reg_access
   $cat direct_reg_access
    0x80062

