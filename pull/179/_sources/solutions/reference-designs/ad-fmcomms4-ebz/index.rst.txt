.. _ad-fmcomms4-ebz:

AD-FMCOMMS4-EBZ
================

AD9364 Wideband Software Defined Radio Board.

.. figure:: ad-fmcomms4-ebz.jpg
   :align: center
   :width: 400px

   AD-FMCOMMS4-EBZ evaluation board

The :adi:`AD-FMCOMMS4-EBZ` is an FMC board for the :adi:`AD9364`, a highly
integrated RF Agile Transceiver. While the complete chip level design package
can be found on the
:adi:`ADI website <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`,
information on the card, and how to use it, the design package that surrounds
it, and the software which can make it work, can be found here.

The purpose of the AD-FMCOMMS4-EBZ is to provide an RF platform to software
developers, system architects, etc, who want a single platform which operates
over a much wider tuning range (70 MHz -- 6 GHz).

The AD-FMCOMMS4-EBZ board is very similar to the
:ref:`AD-FMCOMMS2-EBZ <ad-fmcomms2-ebz>` and
:ref:`AD-FMCOMMS3-EBZ <ad-fmcomms3-ebz>` boards with only one exception,
rather than the :adi:`AD9361` (which is 2 Rx, 2 Tx), it uses the
:adi:`AD9364`, a lower cost 1 Rx, 1 Tx device. The AD-FMCOMMS4-EBZ includes
both types of external baluns, one targeted for wider tuning range applications
(Minicircuits TCM1-63AX+), and ones which provide optimized performance for
2.4 GHz.

Since much of the FMCOMMS2/3/4 share a common device and infrastructure, much
of the documentation is the same.

Functional Overview
-------------------

A functional block diagram of the system is given below. The system consists of
four functional partitions -- receive path, transmit path, clocking, and power
supply. The data path is fully integrated into the :adi:`AD9364`. The key
features of the receive and transmit paths are listed below. Please refer to the
device data sheet for more details.

.. figure:: ad9364_block_diagram.jpg
   :align: center
   :width: 600px

   AD-FMCOMMS4-EBZ system block diagram

AD9364
~~~~~~

Receive
^^^^^^^

- Supports 1 direct conversion RF receive channel
- Fully integrated synthesizers (including loop filter)
- Data path consists of LNA, Demodulator, LPF, ADC and digital filters
- AGC, Quadrature calibration and DC offset calibration
- Noise Figure: 2.5 dB at 1 GHz
- ADC: Continuous time sigma-delta, 640 MSPS
- Digital Filters: 128 complex taps, decimation between 2 and 48
- Gain: 1 dB step size, 80 dB analog range, 30 dB digital range
  (post ADC scaling)
- On-chip sensor for temperature-corrected RSSI

Transmit
^^^^^^^^

- Supports 1 direct conversion RF transmit channel
- Fully integrated synthesizers (including loop filter)
- Data path consists of digital filters, DAC and Modulators
- Digital Filters: 128 complex taps, interpolation between 2 and 48
- Gain: 0.25 dB step size, 86 dB range
- DAC: 320 MSPS

Clocking
^^^^^^^^

The clocks are managed by the device and are software programmable. Please refer
to the device data sheet for the various clocks within the device. The board
provides a 40 MHz crystal for the AD9364.

SPI
^^^

The SPI signals are directly passed to the FMC connector.

Control/Monitor
^^^^^^^^^^^^^^^

The device allows real-time control via dedicated pins. These signals are passed
to the FMC connector. The functionality of these pins are programmable and
includes gain, synchronization, state machine control, etc. Please refer to the
data sheet for more details.

The device also allows real-time monitoring of internal signals via another set
of dedicated pins. Again, these signals are passed to the FMC connector. The
internal signals are multiplexed into these pins, and details of which are best
described in the data sheet.

Hardware
--------

Board Photo and Main Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: fmcomms4_locations.png
   :align: center
   :width: 600px

   AD-FMCOMMS4-EBZ component locations

The AD-FMCOMMS4-EBZ uses the same PCB design as the
:ref:`AD-FMCOMMS2-EBZ <ad-fmcomms2-ebz>` but is populated with the
:adi:`AD9364` instead of the :adi:`AD9361`.

Balun Selection
~~~~~~~~~~~~~~~

The Rev C board includes two types of baluns:

.. list-table::
   :header-rows: 1

   * - Balun
     - Type
     - Frequency Range
     - Connected To
   * - Johanson Technology 2450BL15B050E
     - 2.45 GHz Balun
     - 2400 -- 2500 MHz
     - RXB Input, TXB Output
   * - Mini-Circuits TCM1-63AX+
     - Wideband Transformer
     - 70 MHz -- 6 GHz
     - RXA Input, TXA Output

I/O Voltage
~~~~~~~~~~~~

The :adi:`AD9364` requires a VDD_INTERFACE voltage between 1.71 V and 2.625 V
(1.8 to 2.5 V +/- 5%).

.. warning::

   Setting the I/O voltage to 3.3 V will damage the part.

Board Dimensions
~~~~~~~~~~~~~~~~

.. figure:: fmcomms4_dimensions.png
   :align: center
   :width: 500px

   AD-FMCOMMS4-EBZ board dimensions

The AD-FMCOMMS4-EBZ is a 10 layer board using the standard VITA 57.1 FMC LPC
form factor.

Power
~~~~~

The board receives all the power from the FPGA carrier board through the FMC
connector. Key power components:

.. list-table::
   :header-rows: 1

   * - Component
     - Description
   * - :adi:`ADP1755`
     - Low dropout linear regulator, 1.2 A, 1.6 to 3.6 V
   * - :adi:`ADP2164`
     - High efficiency step-down DC-to-DC regulator, 6.5 V, 4 A

Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

To get started with the AD-FMCOMMS4-EBZ, you will need:

- AD-FMCOMMS4-EBZ FMC board
- A supported FPGA carrier board (see :ref:`Supported Carriers <fmcomms4_carriers>`)
- Two SMA cables for RF loopback testing
- A micro-USB cable for UART console access
- A power supply for the carrier board

.. figure:: ad9364_setup.jpg
   :align: center
   :width: 500px

   AD-FMCOMMS4-EBZ connected to a carrier board

RF Loopback
~~~~~~~~~~~~

For initial testing and verification, a simple loopback configuration connects
the Tx output to the Rx input.

.. figure:: fmcomms4-loopback.jpg
   :align: center
   :width: 500px

   AD-FMCOMMS4-EBZ RF loopback configuration

.. _fmcomms4_carriers:

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
   * - :xilinx:`ZC702 <products/boards-and-kits/ek-z7-zc702-g.html>`
     - Yes
     - Yes
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - Yes
     - Yes
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - Yes
     - Yes

HDL Reference Design
--------------------

The AD-FMCOMMS4-EBZ shares the HDL reference design with the
:ref:`AD-FMCOMMS2-EBZ <ad-fmcomms2-ebz>`.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/fmcomms2`

Software Support
----------------

Linux Drivers
~~~~~~~~~~~~~

- :git-linux:`AD9361/AD9364 Linux Driver <drivers/iio/adc/ad9361.c>`
- :git-linux:`AXI ADC HDL Linux Driver <drivers/iio/adc/cf_axi_adc_core.c>`
- :git-linux:`AXI DAC DDS Linux Driver <drivers/iio/frequency/cf_axi_dds.c>`

Device Trees
~~~~~~~~~~~~

- :git-linux:`AD9364 FMCOMMS4 DTSI <arch/arm/boot/dts/xilinx/adi-fmcomms4.dtsi>`
- :git-linux:`ZC702 DTS <arch/arm/boot/dts/xilinx/zynq-zc702-adv7511-ad9364-fmcomms4.dts>`
- :git-linux:`ZC706 DTS <arch/arm/boot/dts/xilinx/zynq-zc706-adv7511-ad9364-fmcomms4.dts>`
- :git-linux:`ZedBoard DTS <arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad9364-fmcomms4.dts>`
- :git-linux:`ZCU102 DTS <arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9364-fmcomms4.dts>`

Software Applications
~~~~~~~~~~~~~~~~~~~~~

The following software applications and frameworks are supported with the
AD-FMCOMMS4-EBZ:

- **IIO Oscilloscope**: GUI application for data capture and visualization
- **AD936X Control Plugin**: IIO Oscilloscope plugin for AD9364 device
  configuration
- **AD936X Advanced Plugin**: Advanced IIO Oscilloscope plugin for detailed
  AD9364 control
- **libiio**: C/C++ library for interfacing with IIO devices
- **pyadi-iio**: Python interfaces for IIO devices
- **GNU Radio**: Software radio framework support
- **MATLAB/Simulink**: Transceiver Toolbox for streaming data into/out of
  MATLAB

Design Resources
~~~~~~~~~~~~~~~~

When designing with the AD9364, the following resources may be useful:

- :adi:`AD9364 Product Page <AD9364>` -- full datasheet and ordering information
- :adi:`AD9361/AD9364 Design Files <ad9361_design_files>` -- chip level design
  package
- No-OS Driver -- bare-metal driver for platforms without an operating system
- HDL Reference Design -- the FPGA-based baseband design

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- :adi:`AD9364 Product Page <AD9364>`
- :adi:`AD-FMCOMMS4-EBZ Product Page <ad-fmcomms4-ebz>`
- :adi:`SDR For Engineers <en/education/education-library/software-defined-radio-for-engineers.html>`

Warning
-------

.. esd-warning::

Support
-------

If you have any questions regarding the AD-FMCOMMS4-EBZ feel free to ask on
the :ez:`FPGA Reference Designs Forum <fpga>`.
