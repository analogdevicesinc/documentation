.. _pulsar-adc-pmdz:

PulSAR ADC PMOD User Guide
============================

Introduction
------------

The PulSAR ADC PMOD evaluation boards provide a low-cost way to evaluate the
ADI PulSAR family of precision SAR ADCs. These low power ADCs offer very high
performance from 14-bits up to 18-bits with throughputs ranging from 100 kSPS
to 1.3 MSPS. The boards are designed to demonstrate the ADC's performance and
to provide an easy digital interface for a variety of system applications.

.. figure:: pulsar_pmod.jpg
   :align: center

   PulSAR ADC PMOD evaluation board

Applications
~~~~~~~~~~~~

- Battery-powered equipment
- Data acquisition
- Instrumentation
- Medical instruments
- Process controls

.. list-table:: Supported PulSAR ADC PMOD Boards
   :header-rows: 1

   * - Product
     - Resolution
     - ADC Throughput
     - Input Stage
   * - :adi:`AD7942`
     - 14-bit
     - 250 kSPS
     - Unipolar, Single-Ended
   * - :adi:`AD7946`
     - 14-bit
     - 500 kSPS
     - Unipolar, Single-Ended
   * - :adi:`AD7988-1`
     - 16-bit
     - 100 kSPS
     - Unipolar, Single-Ended
   * - :adi:`AD7685`
     - 16-bit
     - 250 kSPS
     - Unipolar, Single-Ended
   * - :adi:`AD7687`
     - 16-bit
     - 250 kSPS
     - Unipolar, Differential
   * - :adi:`AD7686`
     - 16-bit
     - 500 kSPS
     - Unipolar, Single-Ended
   * - :adi:`AD7688`
     - 16-bit
     - 500 kSPS
     - Unipolar, Differential
   * - :adi:`AD7693`
     - 16-bit
     - 500 kSPS
     - Unipolar, Differential
   * - :adi:`AD7988-5`
     - 16-bit
     - 500 kSPS
     - Unipolar, Single-Ended
   * - :adi:`AD7980`
     - 16-bit
     - 1000 kSPS
     - Unipolar, Single-Ended
   * - :adi:`AD7983`
     - 16-bit
     - 1333 kSPS
     - Unipolar, Single-Ended
   * - :adi:`AD7690`
     - 18-bit
     - 400 kSPS
     - Unipolar, Differential
   * - :adi:`AD7691`
     - 18-bit
     - 250 kSPS
     - Unipolar, Differential
   * - :adi:`AD7982`
     - 18-bit
     - 1000 kSPS
     - Unipolar, Differential
   * - :adi:`AD7984`
     - 18-bit
     - 1333 kSPS
     - Unipolar, Differential

All PulSAR ADC PMOD boards use the :adi:`ADA4841` precision amplifier as the
input driver. The actual throughput of the ADC is limited by the SPI bus speed
of the host platform.

Hardware Setup
--------------

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

The ADC's are driven by precision amplifiers optimized for noise and power. In
order to enable the amplifiers to provide zero and full scale inputs to the ADC,
external power supplies of -2.5 V, GND, and 7.5 V are needed. These supplies
provide the power for the entire PMOD board.

.. figure:: pmod_power_supplies.png
   :align: center

   PulSAR ADC PMOD power supply connections

Input Connectors
~~~~~~~~~~~~~~~~

SMB connectors are used for the input signals to minimize noise. Each board
has two SMB connectors for positive (+) and negative (-) inputs to the
converter. Each converter has a combination of single-ended, differential, or
pseudo-differential inputs; consult the device datasheet for details.

.. figure:: vin.png
   :align: center

   PulSAR ADC PMOD analog input connectors

Digital Interface (PMOD)
~~~~~~~~~~~~~~~~~~~~~~~~

The PMOD interface uses the extended SPI configuration. Each of the PulSAR
PMOD boards is hardware configured in a 3-wire mode with no busy indicator.
The signals between the converter and the processor are CNV (chip select),
SCLK (serial clock), and MISO (serial data out).

.. figure:: pmod_pinout.png
   :align: center

   PulSAR ADC PMOD digital interface pinout

Supported Carriers
------------------

- `Cora Z7S <https://digilent.com/reference/programmable-logic/cora-z7/start>`__

HDL Reference Design
--------------------

Block Diagram
~~~~~~~~~~~~~

.. figure:: pulsar_adc_pmod_hdl.svg
   :align: center

   PulSAR ADC PMOD block diagram

The reference design uses the standard SPI Engine Framework with an integrated
PWM generator, which provides the required conversion rate for the ADC.

Design Configuration
~~~~~~~~~~~~~~~~~~~~

The reference design uses a clock generator for the division of the SPI clock
and a PWM generator for the conversion signal. The ``PULSE_0_PERIOD`` parameter
is computed as ``Tcyc_min / Tspi_clk``:

.. list-table::
   :header-rows: 1

   * - Part
     - PULSE_0_PERIOD
   * - AD7942
     - 640
   * - AD7946
     - 320
   * - AD7988-1
     - 1600
   * - AD7685
     - 640
   * - AD7687
     - 640
   * - AD7691
     - 640
   * - AD7686
     - 320
   * - AD7688
     - 320
   * - AD7693
     - 320
   * - AD7988-5
     - 320
   * - AD7980
     - 160
   * - AD7983
     - 120
   * - AD7690
     - 250
   * - AD7982
     - 160
   * - AD7984
     - 120

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/pulsar_adc`
- `PulSAR ADC HDL Project Documentation <https://analogdevicesinc.github.io/hdl/projects/pulsar_adc/index.html>`__

Software Support
----------------

Linux
~~~~~

The PulSAR ADC PMOD boards are supported by the AD7944 Linux driver which
covers the entire PulSAR family. Individual device trees are provided for each
supported ADC on the Cora Z7S carrier.

- :git-linux:`AD7944 Linux driver <drivers/iio/adc/ad7944.c>`

Example device trees for the Cora Z7S:

- :git-linux:`AD7942 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7942-pmdz.dts>`
- :git-linux:`AD7946 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7946-pmdz.dts>`
- :git-linux:`AD7685 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7685-pmdz.dts>`
- :git-linux:`AD7686 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7686-pmdz.dts>`
- :git-linux:`AD7687 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7687-pmdz.dts>`
- :git-linux:`AD7688 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7688-pmdz.dts>`
- :git-linux:`AD7690 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7690-pmdz.dts>`
- :git-linux:`AD7691 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7691-pmdz.dts>`
- :git-linux:`AD7693 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7693-pmdz.dts>`
- :git-linux:`AD7980 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7980-pmdz.dts>`
- :git-linux:`AD7982 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7982-pmdz.dts>`
- :git-linux:`AD7983 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7983-pmdz.dts>`
- :git-linux:`AD7984 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7984-pmdz.dts>`
- :git-linux:`AD7988-1 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7988-1-pmdz.dts>`
- :git-linux:`AD7988-5 <arch/arm/boot/dts/xilinx/zynq-coraz7s-ad7988-5-pmdz.dts>`

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `SPI Engine Framework Documentation <https://analogdevicesinc.github.io/hdl/library/spi_engine/index.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.

.. esd-warning::
