.. _ad7091r5:

EVAL-AD7091R-5SDZ User Guide
=============================

Introduction
------------

The :adi:`AD7091R-5` is a 12-bit, 4-channel, ultralow power, successive
approximation analog-to-digital converter (ADC). It operates from a single
2.7 V to 5.25 V power supply and features an I2C-compatible interface. The
low power consumption makes it ideal for portable and battery-powered
applications, while the 4 input channels provide multichannel data acquisition
capability.

Supported Devices
-----------------

- :adi:`AD7091R-5`

Evaluation Board
----------------

- :adi:`EVAL-AD7091R-5SDZ`

Block Diagram
~~~~~~~~~~~~~

.. figure:: ad7091r5_bd.png
   :align: center

   AD7091R-5 block diagram

Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ad7091r5.jpg
   :align: center

   EVAL-AD7091R-5SDZ hardware configuration

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The AD7091R-5 is supported by the Linux IIO ADC subsystem. The driver depends
on ``CONFIG_I2C``.

- :git-linux:`drivers/iio/adc/ad7091r5.c`
- :git-linux:`drivers/iio/adc/ad7091r-base.c`

Kernel Configuration
~~~~~~~~~~~~~~~~~~~~

Enable the driver via ``make menuconfig``:

.. code-block:: none

   Device Drivers --->
       <*> Industrial I/O support --->
           Analog to digital converters --->
               <*> Analog Devices AD7091R5 ADC driver

Device Tree
~~~~~~~~~~~

Required properties:

- **compatible**: Must be ``"adi,ad7091r5"``.
- **reg**: I2C address for the device.

Optional properties:

- **vref-supply**: phandle to a regulator for the external VREF supply. If no
  external VREF is supplied, this property should be omitted.

Example device tree entry:

.. code-block:: dts

   adc@2f {
       compatible = "adi,ad7091r5";
       reg = <0x2F>;
   };

IIO Attributes
~~~~~~~~~~~~~~

Once the driver is loaded, the IIO device is accessible at
``/sys/bus/iio/devices/iio:deviceX/``. The AD7091R-5 provides 4 voltage input
channels (voltage0 through voltage3). The following attributes are available:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Attribute
     - Description
   * - ``name``
     - Device name (``ad7091r5``)
   * - ``in_voltageY_raw``
     - Raw ADC conversion result for channel Y (0--3). Reading this attribute
       triggers a single conversion on the selected channel.
   * - ``in_voltage_scale``
     - Scale factor to convert raw values to millivolts

The actual input voltage in millivolts is calculated as:

.. code-block:: text

   U = in_voltageY_raw * in_voltage_scale

Example usage:

.. code-block:: console

   root:/sys/bus/iio/devices/iio:device0> cat name
   ad7091r5
   root:/sys/bus/iio/devices/iio:device0> cat in_voltage0_raw
   2048
   root:/sys/bus/iio/devices/iio:device0> cat in_voltage_scale
   0.610351562

The driver also supports threshold events for each channel, with configurable
high and low limits and hysteresis. When enabled, the ALERT/BUSY/GPO0 pin
signals an out-of-range condition.

.. figure:: ad7091r5_iio_terminal.jpg
   :align: center

   Reading AD7091R-5 IIO data via the Linux terminal

.. figure:: ad7091r5_iio_plot.jpg
   :align: center

   AD7091R-5 data capture using the ADI IIO Oscilloscope

No-OS Driver
~~~~~~~~~~~~~

- :git-no-OS:`drivers/adc/ad7091r5`

More Information
----------------

- :adi:`AD7091R-5 Product Page <AD7091R-5>`
- :adi:`EVAL-AD7091R-5SDZ Evaluation Board <EVAL-AD7091R-5SDZ>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`Linux Software Drivers <linux-software-drivers>` sub-community.
