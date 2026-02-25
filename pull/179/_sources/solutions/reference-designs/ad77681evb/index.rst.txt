.. _ad77681evb:

AD7768-1-EVB User Guide
========================

Introduction
------------

The :adi:`AD7768-1` is a low power, high performance, sigma-delta
analog-to-digital converter (ADC) with a sigma-delta modulator and digital
filter for precision conversion of both AC and DC signals. It is a single
channel version of the :adi:`AD7768`, an 8-channel, simultaneously sampling,
sigma-delta ADC.

The AD7768-1 achieves a 108.5 dB dynamic range when using the low ripple FIR
digital filter at 256 kSPS, giving 110.8 kHz input bandwidth, combined with
+/-1.1 ppm INL, +/-30 uV offset error, and +/-30 ppm gain error.

The AD7768-1 offers flexibility to configure and optimize for input bandwidth
vs. output data rate and vs. power dissipation through three operating modes:

- **Fast mode** - sinc filter with up to 256 kSPS and 52.2 kHz bandwidth at
  26.4 mW, or FIR filter with up to 256 kSPS, 110.8 kHz bandwidth at 36.8 mW
- **Median mode** - FIR filter with up to 128 kSPS, 55.4 kHz bandwidth at
  19.7 mW
- **Low power mode** - FIR filter with up to 32 kSPS, 13.85 kHz bandwidth at
  6.75 mW

Filter options include:

- A low ripple FIR filter with +/-0.005 dB pass-band ripple to 102.4 kHz
- A low latency sinc5 filter with up to 1.024 MHz data rate for maximum
  control loop responsiveness
- A programmable sinc3 filter with 50 Hz/60 Hz rejection capabilities

Wider bandwidth up to 500 kHz Nyquist (204 kHz, -3 dB) is available using the
sinc5 filter, providing visibility of signals over an extended range. The
1.024 MHz sinc5 path is quantization noise limited and best suited for
applications requiring minimum latency for control loops or implementing custom
digital filtering on an external FPGA or DSP.

The embedded analog functionality greatly reduces the design burden. The
precharge buffer on each analog input decreases analog input current, while a
full buffer input on the reference provides a high impedance input for the
external reference device.

The device operates with a 5.0 V AVDD1 - AVSS supply, a 2.0 V to 5.0 V
AVDD2 - AVSS supply, and a 1.8 V to 3.3 V IOVDD - DGND supply. In low power
mode, the AVDD1, AVDD2, and IOVDD supplies can run from a single 3.3 V rail.

Supported Devices
-----------------

- :adi:`AD7768-1`

Evaluation Boards
-----------------

- :adi:`EVAL-AD7768-1`

Supported Carriers
------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

HDL Reference Design
--------------------

The reference design uses the standard
`SPI Engine Framework <https://analogdevicesinc.github.io/hdl/library/spi_engine/index.html>`__.
The offload module is triggered by the DRDY (data ready) signal of the device.
Because the board has two :adi:`AD7768-1` devices, the data path consists of
two separate SPI interfaces and GPIOs, and two DMAs for data stream capture.

.. figure:: ad7768evb_fmc_hdl.svg
   :align: center

   AD7768-1-EVB HDL block diagram

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ensure you have the correct tools version (see the
   `HDL releases <https://github.com/analogdevicesinc/hdl/releases>`__ page).
2. Clone the HDL repository and build the project:

.. code-block:: bash

   cd hdl/projects/ad77681evb/zed
   make

For general build prerequisites and instructions, refer to the
`Building HDL projects <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`__
guide.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad77681evb`

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The AD7768-1 Linux IIO driver is a serial interface ADC driver in the
Linux Industrial I/O (IIO) subsystem. The driver exposes channel data,
sampling frequency control, filter bandwidth selection, and direct register
access via debugfs.

- :git-linux:`drivers/iio/adc/ad7768-1.c`

Key IIO attributes:

- ``in_voltage0_raw`` -- raw unscaled voltage measurement on channel 0
- ``in_voltage_scale`` -- scale factor to convert raw values to millivolts
- ``sampling_frequency`` -- get/set the ADC output data rate (e.g. 32000,
  128000, 256000)
- ``in_voltage_filter_low_pass_3db_frequency`` -- get/set the filter
  bandwidth for the current sampling frequency
- ``in_voltage_filter_low_pass_3db_frequency_available`` -- list of
  available bandwidths

Device Trees
~~~~~~~~~~~~

- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad7768-1-evb.dts`

Device tree required properties:

- ``compatible``: Must be ``"ad7768-1"``
- ``reg``: SPI chip select number
- ``spi-max-frequency``: Maximum SPI clock frequency
- ``spi-cpol``, ``spi-cpha``: SPI mode configuration
- ``vref-supply``: Phandle to the fixed voltage reference regulator
- ``clocks``: Phandle to the MCLK clock source
- ``interrupts``: Interrupt specifier for the DRDY signal

Example device tree node:

.. code-block:: none

   adc_vref: fixedregulator@0 {
       compatible = "regulator-fixed";
       regulator-name = "fixed-supply";
       regulator-min-microvolt = <4096000>;
       regulator-max-microvolt = <4096000>;
       regulator-boot-on;
   };

   clocks {
       ad7768_mclk: clock@0 {
           #clock-cells = <0>;
           compatible = "fixed-clock";
           clock-frequency = <16384000>;
       };
   };

   &spi0 {
       #address-cells = <1>;
       #size-cells = <0>;
       status = "okay";

       ad7768@0 {
           compatible = "ad7768-1";
           reg = <0>;
           spi-max-frequency = <16000000>;
           spi-cpol;
           spi-cpha;
           #interrupt-cells = <2>;
           interrupts = <25 0x2>;
           interrupt-parent = <&gpio>;
           vref-supply = <&adc_vref>;
           clocks = <&ad7768_mclk>;
           clock-names = "mclk";
       };
   };

Driver Testing
~~~~~~~~~~~~~~

The measured voltage in millivolts is calculated as:

.. code-block:: text

   U = in_voltage0_raw * in_voltage_scale

For example:

.. code-block:: console

   # cat in_voltage_scale
   0.000488281
   # cat in_voltage0_raw
   2040915

This gives: 2040915 * 0.000488281 = 996.54 mV.

To change the sampling frequency:

.. code-block:: console

   # cat sampling_frequency
   32000
   # echo 256000 > sampling_frequency
   # cat sampling_frequency
   256000

To view and change the filter bandwidth:

.. code-block:: console

   # cat in_voltage_filter_low_pass_3db_frequency_available
   6528.000000, 8320.000000, 13760.000000
   # echo 13760 > in_voltage_filter_low_pass_3db_frequency
   # cat in_voltage_filter_low_pass_3db_frequency
   13760.000000

The driver supports its own default trigger source ``ad7768-1-dev0``. Buffer
management uses the standard IIO buffer interface with ``enable``, ``length``,
and ``watermark`` controls, and scan elements for channel selection.

Direct register access is available via debugfs at
``/sys/kernel/debug/iio/iio:deviceX/direct_reg_access``.

No-OS Project
~~~~~~~~~~~~~

- :git-no-OS:`drivers/adc/ad7768-1`

More Information
----------------

- :ref:`AD7768-EVB User Guide <ad7768-ebz>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `SPI Engine Framework <https://analogdevicesinc.github.io/hdl/library/spi_engine/index.html>`__
- :adi:`AD7768-1 Product Page <AD7768-1>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
