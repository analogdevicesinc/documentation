.. _eval-ad469x-linux-driver:

AD469x Linux IIO driver
===============================================================================

Overview
-------------------------------------------------------------------------------

The :adi:`AD4695 <en/products/ad4695.html>`,
:adi:`AD4696 <en/products/ad4696.html>`,
:adi:`AD4697 <en/products/ad4697.html>`, and
:adi:`AD4698 <en/products/ad4698.html>` are compact, 16-channel,
16-bit, multiplexed SAR ADCs with Easy Drive features and a
high-Z input mode.

The driver is mainlined in the Linux kernel.

.. note::

   A SPI offload capable host controller (such as the AXI SPI
   Engine) is required to achieve maximum sample rate.

Source code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 70

   * - Driver
     - ``drivers/iio/adc/ad4695.c``
   * - Bindings
     - ``Documentation/devicetree/bindings/iio/adc/adi,ad4695.yaml``
   * - Example devicetree
     - ``arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad4696.dts``

Adding Linux driver support
-------------------------------------------------------------------------------

Kernel configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable the driver through the kernel configuration menu:

.. code-block::

   Device Drivers
     -> Industrial I/O support
       -> Analog to digital converters
         -> Analog Devices AD4695 and similar ADCs driver

This corresponds to the ``CONFIG_AD4695`` kernel option.

Device tree configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SPI bus setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The chip appears as a child node of the SPI controller:

.. code-block:: dts

   spi@44a00000 {
       adc@0 {
           compatible = "adi,ad4696";
           reg = <0>;
           spi-max-frequency = <80000000>;
           spi-cpha;
           spi-cpol;
       };
   };

Power supplies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: dts

   avdd-supply = <&eval_u5>;
   ldo-in-supply = <&eval_u5>;
   vio-supply = <&eval_u6>;

Reference configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For an external reference supply:

.. code-block:: dts

   ref-supply = <&eval_u3>;

Reset pin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: dts

   reset-gpios = <&gpio0 86 GPIO_ACTIVE_LOW>;

CNV wiring modes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Two wiring configurations are possible:

- **Standard SPI**: CS connects to both CS and CNV pins. Omit
  ``cnv-gpios``.
- **SPI offload**: CS to CS only; CNV uses GPIO and PWM:

  .. code-block:: dts

     cnv-gpios = <&gpio0 88 GPIO_ACTIVE_HIGH>;
     pwms = <&adc_trigger 0 100000>;

Channel configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: dts

   #address-cells = <1>;
   #size-cells = <0>;

   channel@0 {
       reg = <0>;
   };

   channel@1 {
       reg = <1>;
       common-mode-channel = <AD4695_COMMON_MODE_COM>;
       bipolar;
   };

Using the driver
-------------------------------------------------------------------------------

Sysfs attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IIO devices appear at
``/sys/bus/iio/devices/iio:deviceY/``.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Attribute
     - Description
   * - ``name``
     - Returns chip identifier
   * - ``in_voltageX_raw``
     - Triggers conversion and returns raw ADC value
   * - ``in_voltageX_scale``
     - Conversion factor to millivolts
   * - ``in_voltageX_offset``
     - Common-mode voltage in raw units
   * - ``in_voltageX_calibbias``
     - Per-channel offset calibration
   * - ``in_voltageX_calibscale``
     - Per-channel gain calibration
   * - ``in_voltageX_calibbias_available``
     - Valid range for calibbias
   * - ``in_voltageX_calibscale_available``
     - Valid range for calibscale
   * - ``in_temp_scale``
     - Temperature measurement scale factor
   * - ``in_temp_offset``
     - Temperature measurement offset

Buffer operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With SPI offload
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When using a SPI offload capable controller, sample data is
32-bit. A minimum of 2 voltage channels must be enabled. To
include the temperature channel, at least 2 voltage channels
must also be enabled.

Set the sample rate:

.. code-block:: bash

   echo 10000 > /sys/bus/iio/devices/iio:device1/in_voltage0_sampling_frequency

Configure and enable the buffer:

.. code-block:: bash

   echo 8 > /sys/bus/iio/devices/iio:device1/buffer0/length
   echo 1 > /sys/bus/iio/devices/iio:device1/buffer0/in_voltage0_en
   echo 1 > /sys/bus/iio/devices/iio:device1/buffer0/in_voltage1_en
   echo 1 > /sys/bus/iio/devices/iio:device1/buffer0/enable

Read data from the buffer:

.. code-block:: bash

   hexdump -n $((8 * 2 * 2)) -e'2/4 "%04X " "\n"' /dev/iio:device1

Disable the buffer:

.. code-block:: bash

   echo 0 > /sys/bus/iio/devices/iio:device1/buffer0/enable

Without SPI offload
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Without SPI offload, sample data is 16-bit (no oversampling) or
32-bit (with oversampling). Manual trigger configuration is
required. There are no restrictions on which channels can be
enabled.

Testing
-------------------------------------------------------------------------------

The :adi:`EVAL-AD4696FMCZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad4696.html>`
evaluation board on a
`ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
can be used to test the driver.

Recommended tools:

- :dokuwiki:`IIO Oscilloscope <resources/tools-software/linux-software/iio_oscilloscope>`
- :dokuwiki:`Scopy <university/tools/m2k/scopy>`
- :external+kuiper:doc:`Kuiper Linux <index>` distribution
