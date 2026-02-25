.. _ad916x-fmc:

AD916x-FMC User Guide
=====================

Introduction
------------

The :adi:`AD9161`, :adi:`AD9162`, :adi:`AD9163`, and :adi:`AD9164` are
high-performance digital-to-analog converters (DACs) supporting data rates up
to 6 GSPS with programmable JESD204B serializer/deserializer interfaces
accommodating up to 8 lanes.

The EVAL-AD916X evaluation board provides a full-featured platform for
evaluating these DACs using a ZCU102 FPGA carrier. The AD916x-FMC reference
design implements a transmit data path that moves samples from system memory
(DDR) through the JESD204B link to the DAC. All cores in the transmit chain
are programmable through an AXI-Lite interface.

Features
~~~~~~~~

- Full-featured evaluation board for the AD916x DAC family
- JESD204B coded serial digital inputs with support for up to 8 lanes
- Data rates up to 6 GSPS
- Multiple operating modes with configurable JESD204B parameters
- On-board clock generator with optional external clock input
- SPI interface for device configuration

Supported Devices
-----------------

- :adi:`AD9161`
- :adi:`AD9162`
- :adi:`AD9163`
- :adi:`AD9164`

Supported Carriers
------------------

- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` -- HPC0 Slot

Hardware
--------

Required Hardware
~~~~~~~~~~~~~~~~~

- EVAL-AD916X evaluation board
- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` carrier
- 12 V power supply
- Spectrum analyzer for DAC output measurement
- SMA cables

Clock Configuration
~~~~~~~~~~~~~~~~~~~~

The EVAL-AD916X board includes an on-board clock generator controlled by
jumper J61:

- **J61 mounted**: Uses on-board clock generator
- **J61 unmounted**: Requires external clock source

HDL Reference Design
--------------------

The design implements a JESD204B transmit chain with configurable parameters.
The transmit chain consists of a physical layer represented by an XCVR module,
a link layer represented by a TX JESD LINK module, and a transport layer
represented by a TX JESD TPL module. A data offload block provides buffering
between the DMA engine and the JESD204B link.

JESD204B Configuration (Default: Mode 08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Parameter
     - Value
   * - L (Lanes)
     - 8
   * - M (Converters)
     - 2
   * - S (Samples per frame)
     - 2
   * - F (Octets per frame)
     - 1
   * - N (Converter resolution)
     - 16
   * - N' (Bits per sample)
     - 16
   * - JESD204B Lane Rate
     - 12.5 Gbps

Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~

The build supports multiple DAC devices and operating modes:

.. list-table::
   :header-rows: 1

   * - Parameter
     - Options
     - Default
   * - ADI_DAC_DEVICE
     - AD9161, AD9162, AD9163, AD9164
     - AD9161
   * - ADI_DAC_MODE
     - 01--08 (device dependent)
     - 08
   * - ADI_LANE_RATE
     - 4.16 GHz, 12.5 GHz
     - 12.5 GHz

Custom JESD204B parameters (M, L, S, F, NP) can also be overridden directly.
Refer to the individual device datasheets for supported mode configurations.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad916x_fmc`

HDL Documentation
~~~~~~~~~~~~~~~~~

- `AD916x-FMC HDL project <https://analogdevicesinc.github.io/hdl/projects/ad916x_fmc/index.html>`__

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The bitstream must be built from source. Clone the HDL repository and build
the ZCU102 project:

Default build (AD9161, Mode 08, 12.5 GHz lane rate):

.. code-block:: bash

   cd hdl/projects/ad916x_fmc/zcu102
   make

Custom device and mode example:

.. code-block:: bash

   cd hdl/projects/ad916x_fmc/zcu102
   make ADI_DAC_DEVICE=AD9163 ADI_DAC_MODE=02 ADI_LANE_RATE=12.5

Custom JESD204B parameters example:

.. code-block:: bash

   cd hdl/projects/ad916x_fmc/zcu102
   make ADI_DAC_DEVICE=AD9164 ADI_LANE_RATE=12.5 M=1 L=8 S=4 NP=16

A comprehensive build guide is available in the
`HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__.

Quick Start
-----------

1. Build the HDL bitstream for the desired DAC device and operating mode.
2. Flash the :doc:`Kuiper Linux </linux/kuiper/index>` image onto the SD card.
3. Configure the boot files (BOOT.BIN, devicetree.dtb, Image) for the
   AD916x design.
4. Insert the SD card into the ZCU102.
5. Attach the EVAL-AD916X evaluation board to the ZCU102 FMC HPC0 connector.
6. Connect the DAC output to a spectrum analyzer via SMA cable.
7. Power the ZCU102 with the 12 V supply.
8. Use :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` for signal
   generation and analysis.

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

Driver and device tree source files:

- :git-linux:`drivers/iio/frequency/ad9162.c`

Device trees are available for each supported device and mode:

- :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9161-fmc-ebz_m2_s2.dts`
- :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9162-fmc-ebz_m2_s2.dts`
- :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9163-fmc-ebz_m2_l8.dts`
- :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9164-fmc-ebz_m2_s2.dts`

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__
- `UG-1526: AD9161/AD9162/AD9163/AD9164 User Guide <https://www.analog.com/media/en/technical-documentation/user-guides/ad9161-ad9162-ad9163-ad9164-ug-1526.pdf>`__
- :adi:`AD9161 Product Page <AD9161>`
- :adi:`AD9162 Product Page <AD9162>`
- :adi:`AD9163 Product Page <AD9163>`
- :adi:`AD9164 Product Page <AD9164>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
