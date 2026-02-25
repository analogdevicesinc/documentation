.. _adaq23875:

ADAQ23875 User Guide
====================

Introduction
------------

The :adi:`ADAQ23875` is a high-speed, 16-bit, 15 MSPS data acquisition
uModule system that integrates a precision SAR ADC (based on the
:adi:`LTC2387-18` core), a precision reference, a reference buffer, and a
high-bandwidth ADC driver into a single system-in-package (SiP). The ADAQ23875
is part of the Low Harmonic Interleaving (LHI) family of high-speed SAR ADCs,
which enables multi-channel interleaving while maintaining low harmonic
distortion.

By integrating critical signal chain components into a compact package, the
ADAQ23875 simplifies board-level design, reduces overall solution size, and
provides optimized performance that would otherwise require extensive design
effort with discrete components.

Supported Devices
-----------------

- :adi:`ADAQ23875`

Supported Carriers
------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

Hardware
--------

Required Hardware
~~~~~~~~~~~~~~~~~

- EVAL-ADAQ23875 evaluation board
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
- 12 V power supply
- SD card (at least 16 GB) with :doc:`Kuiper Linux </linux/kuiper/index>`
- LAN cable for network connection to the ZedBoard
- SMA cables and XLR-to-SMA adapter for analog input

Power Supply Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board features multiple on-board regulators that generate the
required supply rails:

.. list-table::
   :header-rows: 1

   * - Rail
     - Voltage
     - Regulator
   * - VS
     - +7 V
     - LTM8049
   * - VDD
     - +5 V
     - ADP7118
   * - VIO
     - +2.5 V
     - LT3023
   * - -VS
     - -2.0 V
     - ADP7183

A single ground plane is used on the board to minimize the effect of high
frequency noise interference.

Analog Input
~~~~~~~~~~~~

The SMA connectors (VIN+, VIN-) support three configuration paths:

- Direct input to the ADAQ23875
- Through optional :adi:`ADA4899-1` amplifiers in unity-gain mode
- Via :adi:`ADG774` switch matrix for signal routing

HDL Reference Design
--------------------

The HDL reference design implements the ``axi_ltc2387`` IP core, which provides
a parallel LVDS data interface to the ADAQ23875 ADC. The captured data is
moved from the IP core output to system memory via a DMA engine.

HDL IP Core Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

- `AXI LTC2387 IP core documentation <https://analogdevicesinc.github.io/hdl/library/axi_ltc2387/index.html>`__

HDL Project Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

- `ADAQ23875 HDL project documentation <https://analogdevicesinc.github.io/hdl/projects/adaq23875/index.html>`__

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/adaq23875`
- :git-hdl:`library/axi_ltc2387`

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The design is built upon ADI's generic HDL reference design framework. ADI
does not distribute pre-built bitstream files, so the project must be built
from source. Clone the HDL repository and, with the correct tools installed,
navigate to the project directory and run ``make``:

.. code-block:: bash

   cd hdl/projects/adaq23875/zed
   make

A comprehensive build guide is available in the
`HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__.

Quick Start
-----------

1. Flash the :doc:`Kuiper Linux </linux/kuiper/index>` image onto the SD card.
2. Configure the boot files (BOOT.BIN, devicetree.dtb, uImage) for the
   ADAQ23875 design.
3. Insert the SD card into the ZedBoard.
4. Attach the EVAL-ADAQ23875 evaluation board to the ZedBoard FMC connector.
5. Connect the analog signal source via the XLR-to-SMA adapter.
6. Power the board with the 12 V supply.
7. Connect to the board via LAN and use
   :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` for data
   capture and visualization.

Software Support
----------------

Linux Driver
~~~~~~~~~~~~

The ADAQ23875 uses the LTC2387 Linux IIO driver, which provides buffered data
capture and sampling frequency control through the IIO subsystem.

Driver and device tree source files:

- :git-linux:`drivers/iio/adc/ltc2387.c`
- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ltc2387.dts`

IIO Oscilloscope
~~~~~~~~~~~~~~~~

The :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application
provides a graphical interface for data capture and analysis. It supports:

- Time domain and frequency domain (FFT) plotting
- DMM tab for continuous voltage readings
- Data export in CSV, MAT, and PNG formats

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- :adi:`ADAQ23875 Product Page <ADAQ23875>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
