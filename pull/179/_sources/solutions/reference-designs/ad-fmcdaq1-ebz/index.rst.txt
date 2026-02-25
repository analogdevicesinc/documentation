.. _ad-fmcdaq1-ebz:

AD-FMCDAQ1-EBZ
===============

The :adi:`AD-FMCDAQ1-EBZ
<en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad-fmcdaq1-ebz.html#eb-overview>`
is an FMC board for the high speed DAC :adi:`AD9122` and ADC :adi:`AD9684`.
It is a data acquisition platform that connects the analog world using FMC to
the FPGA.

.. image:: fmcdaq1_top.jpg
   :align: center
   :width: 500

Introduction
------------

The AD-FMCDAQ1-EBZ module is comprised of the :adi:`AD9684` dual, 14-bit,
0.5 GSPS, LVDS ADC, the :adi:`AD9122` dual, 16-bit, 1.2 GSPS, LVDS DAC,
the :adi:`AD9523-1` clock, and power management components. It is clocked by
an internally generated carrier platform via the FMC connector, comprising a
completely self contained data acquisition and signal synthesis prototyping
platform. In an FMC footprint (84 mm x 69 mm), the module's combination of
wideband data conversion, clocking, and power closely approximates real-world
hardware and software for system prototyping and design, with no compromise in
signal chain performance.

Features
~~~~~~~~

- FMC-compatible form factor
- Powered from single FMC connector
- Provides two channels of ADC and two channels of DAC with full
  synchronization capabilities

AD9684 ADC
~~~~~~~~~~

- 14-bit 500 MSPS LVDS
- SFDR: 85 dBc at 170 MHz AIN, 0.5 GSPS
- Noise density: -153 dBFS/Hz at 0.5 GSPS
- 2 GHz of usable analog input full power bandwidth
- Two integrated DDCs per channel

AD9122 DAC
~~~~~~~~~~

- 16-bit 1200 MSPS LVDS
- Supports complex signal bandwidths up to 800 MHz
- SFDR = 85 dBc (BW = 300 MHz) at DC IF
- Selectable 2x, 4x, 8x interpolation filters

Applications
~~~~~~~~~~~~

- Electronic test and measurement equipment
- General-purpose software radios
- Radar systems
- Ultra wideband satellite receivers
- Signals intelligence (SIGINT)
- Point to point communication systems
- Multiple input/multiple output (MIMO) radios
- Automated test equipment

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
     - No-OS
   * - :xilinx:`KC705 <products/boards-and-kits/ek-k7-kc705-g.html>`
     - Yes
     - Yes
     - Yes
   * - :xilinx:`KCU105 <products/boards-and-kits/kcu105.html>`
     - Yes
     - Yes
     - Yes
   * - :xilinx:`VC707 <products/boards-and-kits/ek-v7-vc707-g.html>`
     - Yes
     - Yes
     - Yes
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - Yes
     - Yes
     - Yes

Quick Start
-----------

The AD-FMCDAQ1-EBZ connects to the HPC connector of the carrier board.
The carrier setup requires power, UART (115200), Ethernet (Linux), HDMI
(if available) and/or JTAG (No-OS) connections.

.. image:: daq1_carrier.jpg
   :align: center
   :width: 500

Hardware
--------

Board Size
~~~~~~~~~~

The size of the board (not including the SMA connectors) is 3.102 inches by
2.712 inches (approximately 79 mm x 69 mm).

.. image:: daq1_dimensions.png
   :align: center
   :width: 400

Software Support
----------------

Linux Drivers
~~~~~~~~~~~~~

- :git-linux:`AD9122 Linux Driver <drivers/iio/frequency/ad9122.c>`
- :git-linux:`AD9523-1 Clock Linux Driver <drivers/iio/frequency/ad9523.c>`
- :git-linux:`AXI ADC HDL Linux Driver <drivers/iio/adc/cf_axi_adc_core.c>`
- :git-linux:`AXI DAC DDS Linux Driver <drivers/iio/frequency/cf_axi_dds.c>`

Device Trees
~~~~~~~~~~~~

- :git-linux:`ZC706 DTS <arch/arm/boot/dts/xilinx/zynq-zc706-adv7511-fmcdaq1.dts>`

Support
-------

If you have any questions regarding the AD-FMCDAQ1-EBZ feel free to ask on
the :ez:`FPGA Reference Designs Forum <fpga>`.
