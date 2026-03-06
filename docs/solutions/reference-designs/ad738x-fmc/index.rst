.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad738x

.. _ad738x-fmc:

AD738x-FMC User Guide
=====================

Introduction
------------

The AD7380 family are dual and quad 16-bit, 14-bit, and 12-bit pin-compatible
simultaneous sampling, high speed, low power, successive approximation
analog-to-digital converters (ADC) that operate from a 3.3 V power supply with
throughput rates up to 4 MSPS.

The analog input type is differential for the :adi:`AD7380` and :adi:`AD7381`,
pseudo-differential for the :adi:`AD7383` and :adi:`AD7384`, and single-ended
for the :adi:`AD7386`, :adi:`AD7387`, and :adi:`AD7388`. The AD7380 family has
optional integrated on-chip oversampling blocks to improve dynamic range and
reduce noise at lower bandwidths. An internal 2.5 V reference is included.

Alternatively, an external reference up to 3.3 V can be used. The conversion
process and data acquisition use standard control inputs allowing for easy
interfacing to microprocessors or DSPs. It is compatible with 1.8 V, 2.5 V, and
3.3 V interfaces, using a separate logic supply.

Applications:

- Motor control position feedback
- Motor control current sense
- Data acquisition systems
- EDFA applications
- I and Q demodulation
- SONAR
- Power quality

Supported Devices
-----------------

- :adi:`AD7380`
- :adi:`AD7381`
- :adi:`AD7383`
- :adi:`AD7384`
- :adi:`AD7386`
- :adi:`AD7387`
- :adi:`AD7388`
- :adi:`AD4680`
- :adi:`AD4681`
- :adi:`AD4682`
- :adi:`AD4683`
- :adi:`AD4684`
- :adi:`AD4685`

Evaluation Boards
-----------------

- :adi:`EVAL-AD7380FMCZ`
- :adi:`EVAL-AD7381FMCZ`
- :adi:`EVAL-AD7386FMCZ`
- :adi:`EVAL-AD7383FMCZ`
- :adi:`EVAL-AD7380-4FMCZ`

Supported Carriers
------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

HDL Reference Design
--------------------

The reference design uses the standard SPI Engine Framework with an integrated
pulse generator, which provides the required conversion rate for the ADC.

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The design is built upon ADI's generic HDL reference design framework. ADI
does not distribute pre-built bitstream files, so the project must be built
from source. Clone the HDL repository and, with the correct tools installed,
navigate to the project directory and run ``make``:

.. code-block:: bash

   cd hdl/projects/ad738x_fmc/zed
   make

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad738x_fmc`

Software Support
----------------

No-OS Project
~~~~~~~~~~~~~

- :git-no-OS:`projects/ad738x_fmcz`
- :git-no-OS:`drivers/adc/ad738x`

The No-OS project provides bare metal support for the AD738x-FMC evaluation
boards. The No-OS driver provides the following key capabilities:

- Device initialization and removal
- Internal or external reference selection
- Power down mode control (normal or full power-down)
- Oversampling configuration (normal or rolling average mode, ratios from x2
  to x32, with 16-bit or 18-bit resolution)
- Conversion mode selection (one-wire or two-wire SPI output)
- Software and hardware device reset
- Single conversion readback

To set up the software:

#. Clone the No-OS GitHub repository
#. Build the project located at ``projects/ad738x_fmcz``
#. Follow the instructions in the
   `ADI No-OS build guide <https://analogdevicesinc.github.io/no-OS/doxygen/build_guides.html>`__

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The AD738x Linux driver is an IIO (Industrial I/O) subsystem driver targeting
dual and quad channel serial interface ADCs from the AD7380 family.

- :git-linux:`drivers/iio/adc/ad7380.c`

Linux Device Tree
^^^^^^^^^^^^^^^^^

A complete example device tree for the EVAL-AD7380FMCZ evaluation board can be
found in the ADI Linux source code. This can be adapted for other evaluation
boards by changing the ``compatible`` property:

- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad7380.dts`

Required device tree properties:

- ``compatible``: Must be set to the specific chip, e.g. ``"adi,ad7380"``
- ``reg``: SPI chip select number
- ``spi-max-frequency``: Maximum SPI clock rate (use datasheet max if wiring
  permits)
- ``spi-cpol``: Must be set for correct clock polarity
- ``vcc-supply``: VCC power supply
- ``vlogic-supply``: Logic power supply

Reference supply configuration:

- ``refio-supply``: External reference on the REFIO pin (omit to use
  internal reference)
- ``refin-supply``: Used for AD7380-4 and ADAQ chips which require an extra
  supply on the REFIN pin

For SPI offloading support (required for maximum throughput), add:

- ``adi,num-sdi``: Number of SDI lines, must match the ``NUM_OF_SDI`` compile
  option used when building the FPGA bitstream

IIO Attributes
^^^^^^^^^^^^^^

Once the driver is loaded, the following IIO attributes are available at
``/sys/bus/iio/devices/iio:deviceX/``:

.. list-table::
   :header-rows: 1

   * - Attribute
     - Description
   * - ``in_voltageX_raw``
     - Raw unscaled voltage measurement on channel X
   * - ``in_voltage_scale``
     - Scale to apply to raw values to obtain millivolts
   * - ``in_voltage_sampling_frequency``
     - Sampling frequency (when using SPI offload)
   * - ``in_voltage_sampling_frequency_available``
     - Maximum available sample rate
   * - ``in_voltage_oversampling_ratio``
     - Current oversampling ratio (1 = disabled)
   * - ``in_voltage_oversampling_ratio_available``
     - Available oversampling ratios (1, 2, 4, 8, 16, 32)

The measured voltage in millivolts is calculated as:

   ``voltage_mV = in_voltageX_raw * in_voltage_scale``

For pseudo-differential chips, an ``in_voltageX_offset`` attribute is also
available.

Oversampling
^^^^^^^^^^^^

Normal averaging oversampling is supported via the
``in_voltage_oversampling_ratio`` attribute. Writing a value greater than 1
enables oversampling, and writing 1 disables it. When oversampling is enabled,
the resolution boost feature of the chip is also turned on.

.. note::

   The resolution boost changes the ``scan_type`` for buffered reads. Older
   versions of libiio do not expect this to change, so you may need to
   restart ``iiod`` after enabling oversampling for correct data interpretation.

Trigger Management
^^^^^^^^^^^^^^^^^^

**SPI Offload Trigger:** When using the chip with a SPI controller that has
offload capabilities (such as the SPI Engine in the HDL reference design),
``in_voltage_sampling_frequency`` and
``in_voltage_sampling_frequency_available`` attributes control the hardware
trigger frequency. No manual trigger setup is needed beyond setting the
desired sample rate.

.. note::

   For single-ended chips, the effective sample rate is half of the
   ``in_voltage_sampling_frequency`` value when all channels are enabled,
   due to the input MUX switching between banks.

**Conventional IIO Trigger:** When using a standard SPI controller, the
driver supports hrtimer-based triggers for data capture:

.. code-block:: console

   # mkdir /sys/kernel/config/iio/triggers/hrtimer/trigger0
   # echo 500 > /sys/bus/iio/devices/trigger0/sampling_frequency
   # echo trigger0 > /sys/bus/iio/devices/iio:device0/trigger/current_trigger

Buffer Management
^^^^^^^^^^^^^^^^^

The IIO buffer interface provides ``enable``, ``length``, and ``watermark``
controls in the ``buffer`` subdirectory:

- **length**: Get/set the number of sample sets held by the buffer.
- **enable**: Enables/disables the buffer. Write last, after configuring length
  and scan elements.

Scan elements in the ``scan_elements`` directory control which channels are
captured:

- ``in_voltageX_en``: Enable/disable scan element (write 1/0)
- ``in_voltageX_type``: Data storage format (e.g. ``s16/16>>0``)
- ``in_voltageX_index``: Position of this element in the buffer

.. note::

   When using SPI offloading, **all** channels must be enabled for buffered
   reads (except for single-ended chips, where half the channels from the
   same MUX position may be enabled). Software timestamp attributes are not
   present when using hardware triggers.

Alert Output
^^^^^^^^^^^^

The ALERT output thresholds are accessed via event attributes:

- ``events/in_thresh_falling_value``: Low threshold (raw units)
- ``events/in_thresh_rising_value``: High threshold (raw units)
- ``events/thresh_either_en``: Enable/disable the ALERT output pin

Threshold values are in raw units. To set a specific voltage, account for
``scale`` (and ``offset`` if present). For example, with a 3.3 V reference,
the scale is 0.050354003 and the default rising threshold of 32768 corresponds
to approximately 1650 mV.

ADAQ Chip Gain Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ADAQ chips have a resistor network for each input that determines the
amplifier gain. These are specified using channel properties in the device
tree. The ``adi,gain-milli`` property is the gain multiplied by 1000 (e.g.,
a gain of 0.3 is written as 300):

.. code-block:: none

   #address-cells = <1>;
   #size-cells = <0>;

   channel@0 {
       reg = <0>;
       adi,gain-milli = /bits/ 16 <300>;
   };

If any channel is omitted, the gain for that channel is assumed to be 1.0.

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
