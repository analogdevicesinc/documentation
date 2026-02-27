.. imported from: https://wiki.analog.com/resources/demo/reference-designs/ad5758_adp1031

.. _ad5758-sdz:

AD5758-SDZ User Guide
=====================

Introduction
------------

The :adi:`AD5758` is a single-channel, voltage and current output digital-to-
analog converter (DAC) that operates with a power supply range from -33 V
minimum on AVSS to +33 V maximum on AVDD1 with a maximum operating voltage
between the two rails of 60 V.

On-chip dynamic power control (DPC) minimizes package power dissipation by
regulating the supply voltage (VDPC+) to the VIOUT output driver circuitry
from 5 V to 27 V using a buck dc-to-dc converter optimized for minimum on-chip
power dissipation. The CHART pin enables a HART signal to be coupled onto the
current output.

The device uses a versatile 4-wire SPI that operates at clock rates of up to
50 MHz and is compatible with standard SPI, QSPI, MICROWIRE, DSP, and
micro-controller interface standards. The interface also features an optional
SPI CRC and a watchdog timer. The AD5758 offers diagnostic features such as
output current monitoring and an integrated 12-bit diagnostic ADC. Additional
robustness is provided by a fault protection switch on VIOUT, +VSENSE, and
-VSENSE pins.

Applications:

- Process control
- Actuator control
- PLC and DCS applications
- HART network connectivity

The AD5758 supports the following output ranges:

**Voltage Output Ranges:**

- 0 V to 5 V
- 0 V to 10 V
- -5 V to +5 V
- -10 V to +10 V

**Current Output Ranges:**

- 0 mA to 20 mA
- 0 mA to 24 mA
- 4 mA to 24 mA
- -20 mA to +20 mA
- -24 mA to +24 mA
- -1 mA to +22 mA

The device includes an integrated 12-bit diagnostic ADC that can monitor
multiple internal nodes including die temperature, supply voltages, output
voltage/current sense, and reference voltages.

Supported Devices
-----------------

- :adi:`AD5758`

Evaluation Board
~~~~~~~~~~~~~~~~

- :adi:`EVAL-AD5758`

Supported Carriers
------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

HDL Reference Design
--------------------

The HDL project uses a ZedBoard and its hardware interfaces. There is no custom
logic in the programmable side of the Zynq 7000 SoC; the design uses the
standard base reference design framework.

To build the HDL design:

#. Confirm that you have the required tools (Vivado).
#. Clone the
   `HDL repository <https://github.com/analogdevicesinc/hdl>`__.
#. Build the project following the
   `HDL build guide <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`__.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad5758_sdz`

Software Support
----------------

No-OS Project
~~~~~~~~~~~~~

- :git-no-OS:`projects/ad5758-sdz`
- :git-no-OS:`drivers/dac/ad5758`

To set up the No-OS software:

#. Clone the
   `No-OS repository <https://github.com/analogdevicesinc/no-OS>`__.
#. Navigate to the ``projects/ad5758-sdz`` directory.
#. Follow the Xilinx software setup instructions in the
   `ADI FPGA documentation <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`__.

Linux Driver
~~~~~~~~~~~~

The :adi:`AD5758` is supported by a mainlined Linux IIO DAC driver.

- :git-linux:`AD5758 Linux Driver <drivers/iio/dac/ad5758.c>`

Device Tree
^^^^^^^^^^^

Required properties:

- ``compatible``: Must be ``"adi,ad5758"``
- ``reg``: SPI chip select number for the device
- ``spi-max-frequency``: Maximum SPI frequency to use (< 50000000)
- ``spi-cpha``: Required SPI mode

Optional properties:

- ``reset-gpios``: GPIO spec for the RESET pin (asserted during driver probe
  if specified)
- ``adi,dc-dc-mode``: Mode of operation of the dc-to-dc converter
- ``adi,dc-dc-ilim``: The dc-to-dc converter current limit
- ``adi,slew``: Array of slew rate settings (3 fields: enable, clock, step)
- ``adi,range``: The output range

Example device tree node:

.. code-block:: dts

   &spi0 {
       #address-cells = <1>;
       #size-cells = <0>;
       status = "okay";

       ad5758@0 {
           compatible = "adi,ad5758";
           reg = <0>;
           spi-max-frequency = <1000000>;
           spi-cpha;

           reset-gpios = <&gpio 22 0>;

           adi,dc-dc-mode = <2>;
           adi,dc-dc-ilim = <200>;
           adi,slew = <1 200000 12>;
           adi,range = <1>;
       };
   };

IIO Attributes
^^^^^^^^^^^^^^

Once the driver is loaded, the IIO device is accessible at
``/sys/bus/iio/devices/iio:deviceX/``. The following attributes are available:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Attribute
     - Description
   * - ``name``
     - Device name (``ad5758``)
   * - ``out_voltage0_raw``
     - Raw DAC output value for channel 0
   * - ``out_voltage_scale``
     - Scale factor to convert raw value to millivolts
   * - ``out_voltage0_powerdown``
     - Power-down control for channel 0 (write ``1`` to power down, ``0`` to
       resume normal operation)

To set the output voltage, write a raw value to ``out_voltage0_raw``. The
actual output voltage in millivolts is calculated as:

.. code-block:: text

   U = out_voltage0_raw * out_voltage_scale

For example, with the 0 V to 10 V range:

.. code-block:: console

   # echo 32767 > out_voltage0_raw

This produces approximately 32767 * 0.152587890 = 4999.84 mV.

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
