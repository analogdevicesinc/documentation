AD57xx-ARDZ
===========

Evaluating the AD5760/AD5780/AD5781/AD5790/AD5791 Precision Voltage Output DACs.

Overview
--------

The :adi:`AD5791` is a single, 20-bit, unbuffered voltage-output digital-to-analog
converter (DAC) that operates from a bipolar supply of up to 33 V. It accepts a
positive reference input in the range 5 V to VDD - 2.5 V and a negative reference
input in the range VSS + 2.5 V to 0 V. The AD5791 offers a relative accuracy
specification of +/-1 LSB max, and operation is guaranteed monotonic with a
+/-1 LSB differential nonlinearity (DNL) maximum specification.

The device uses a versatile 3-wire serial interface that operates at clock rates
up to 35 MHz and is compatible with standard SPI, QSPI, MICROWIRE, and DSP
interface standards. The device incorporates a power-on reset circuit that
ensures the DAC output powers up to 0 V and remains in this state until a valid
write takes place.

Applications
~~~~~~~~~~~~

- Medical instrumentation
- Test and measurement
- Industrial control
- High-end scientific and aerospace instrumentation

Supported Devices
-----------------

- :adi:`AD5760`
- :adi:`AD5780`
- :adi:`AD5781`
- :adi:`AD5790`
- :adi:`AD5791`

Evaluation Boards
-----------------

- :adi:`EVAL-AD5780ARDZ`
- :adi:`EVAL-AD5781ARDZ`
- :adi:`EVAL-AD5791ARDZ`

Reference Circuits
~~~~~~~~~~~~~~~~~~

- :adi:`CN0177`
- :adi:`CN0191`
- :adi:`CN0200`
- :adi:`CN0257`
- :adi:`CN0278`
- :adi:`CN0318`

Supported Carriers
------------------

.. list-table::

   * - Carrier
     - no-OS
     - Linux
   * - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development/>`__
     - ✓
     - ✓
   * - `DE10-Nano <https://www.terasic.com.tw/cgi-bin/page/archive.pl?No=1046>`__
     - ✓
     - ✓

HDL Reference Design
--------------------

The HDL reference design uses the SPI Engine Framework with an integrated
pulse generator, providing the required update rate for the DAC. The design
supports streaming data from DMA to the DAC with high speed and precise
timing through SPI offload.

The source code is available at
:git-hdl:`projects/ad57xx_ardz`
and documented at
:external+hdl:ref:`ad57xx_ardz`.

The following carriers are supported:

.. list-table::

   * - Carrier
     - HDL project
   * - Cora Z7S
     - :git-hdl:`projects/ad57xx_ardz/coraz7s`
   * - DE10-Nano
     - :git-hdl:`projects/ad57xx_ardz/de10nano`

Linux Driver
------------

The AD5791 Linux driver is part of the Industrial I/O (IIO) subsystem.
The driver is mainlined in the Linux kernel.

SPI offload support was added in kernel v6.15, enabling continuous
streaming of waveforms from DMA to the DAC.

Source Code
~~~~~~~~~~~

.. list-table::

   * - Function
     - File
   * - Driver
     - :git-linux:`drivers/iio/dac/ad5791.c`
   * - Devicetree bindings
     - :git-linux:`Documentation/devicetree/bindings/iio/dac/adi,ad5791.yaml`

Kernel Configuration
~~~~~~~~~~~~~~~~~~~~

The AD5791 driver depends on ``CONFIG_SPI``. Enable it through kernel
menuconfig:

.. code-block::

   Linux Kernel Configuration
       Device Drivers  --->
           <*>     Industrial I/O support --->
               --- Industrial I/O support
               Digital to analog converters  --->
                   <*>   Analog Devices AD5760/AD5780/AD5781/AD5790/AD5791 DAC SPI driver

Linux Devicetrees
~~~~~~~~~~~~~~~~~

.. list-table::

   * - Carrier
     - Devicetree
   * - DE10-Nano
     - :git-linux:`socfpga_cyclone5_de10_nano_ad5791.dts <arch/arm/boot/dts/intel/socfpga/socfpga_cyclone5_de10_nano_ad5791.dts>`

IIO Sysfs Attributes
~~~~~~~~~~~~~~~~~~~~

The driver exposes the following control interfaces under
``/sys/bus/iio/devices/iio:deviceX/``:

.. list-table::
   :header-rows: 1

   * - Attribute
     - Description
   * - ``out_voltage0_raw``
     - Raw output voltage value.
   * - ``out_voltage_scale``
     - Conversion factor to millivolts.
   * - ``out_voltage0_powerdown``
     - Enable/disable power-down mode.
   * - ``out_voltage_powerdown_mode``
     - Select power-down behavior (``6kohm_to_gnd`` or ``three_state``).
   * - ``out_voltage_powerdown_mode_available``
     - Lists available power-down modes.

When used with a SPI controller that supports offloading, additional attributes
are available: a ``sampling_frequency`` attribute to set the DAC update rate and
a ``buffer`` folder for buffered writes.

No-OS Driver
-------------

The no-OS driver provides bare-metal control of the AD5791 and related devices
via SPI.

The driver source code is available at
:git-no-OS:`drivers/dac/ad5791`.

No-OS projects for the supported evaluation boards can use the driver
directly with the no-OS framework.

Functions
~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Function
     - Description
   * - ``ad5791_init()``
     - Initialize the device.
   * - ``ad5791_remove()``
     - Free resources allocated by ``ad5791_init()``.
   * - ``ad5791_set_register_value()``
     - Write data into a register.
   * - ``ad5791_get_register_value()``
     - Read register value.
   * - ``ad5791_dac_ouput_state()``
     - Set the DAC output state (normal, clamped, or tristate).
   * - ``ad5791_set_dac_value()``
     - Write to the DAC register.
   * - ``ad5791_soft_instruction()``
     - Assert RESET, CLR, or LDAC in software.
   * - ``ad5791_setup()``
     - Configure the output amplifier, coding, SDO state, and linearity
       error compensation.

Hardware Setup
--------------

.. figure:: test-with-de10-nano.png
   :width: 500 px

   EVAL-AD5791ARDZ test setup with DE10-Nano

The ARDZ evaluation boards connect to the carrier board via the Arduino Uno
compatible headers.

To power the evaluation board, provide external differential supply voltage
and reference voltage as described in the evaluation board user guide.

Help and Support
----------------

For questions and more information, please visit the
:ez:`EngineerZone Support Community <reference-designs>`.

.. esd-warning::
