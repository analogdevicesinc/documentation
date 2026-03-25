.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz

.. _ad-fmcomms2-ebz:

AD-FMCOMMS2-EBZ
================

The :adi:`AD-FMCOMMS2-EBZ` is an FMC board for the :adi:`AD9361`, a highly
integrated RF Agile Transceiver. The purpose of the AD-FMCOMMS2-EBZ is to
provide an RF platform which shows maximum performance of the AD9361 at
2.4 GHz, using the Johanson Technology 2450BL15B050E 2.45 GHz balun.

The AD-FMCOMMS2-EBZ board is very similar to the
:ref:`AD-FMCOMMS3-EBZ <ad-fmcomms3-ebz>` board with only one exception: the
RX/TX RF differential to single-ended balun/transformer. The AD-FMCOMMS3-EBZ
uses a wideband transformer for broader tuning range applications.

.. image:: fmcomms2_top.png
   :align: center
   :width: 400

.. toctree::
   :hidden:

   card_specification
   quickstart_microblaze
   quickstart_zynqmp
   no_os_software
   filter_wizard
   iq_datafiles
   interface_timing
   testing

Table of Contents
-----------------

#. :doc:`RF Card Specifications <card_specification>`
#. :doc:`MicroBlaze Quick Start Guide <quickstart_microblaze>`
#. :doc:`ZCU102 Quick Start Guide <quickstart_zynqmp>`
#. :doc:`No-OS Software <no_os_software>`
#. :doc:`AD9361 Filter Design Wizard <filter_wizard>`
#. :doc:`I/Q Data Files <iq_datafiles>`
#. :doc:`Digital Interface Timing Validation <interface_timing>`
#. :doc:`Production Testing <testing>`

AD936x Board Comparison
-----------------------

The AD-FMCOMMS2/3/4/5-EBZ and ARRADIO cards are high-speed analog modules
designed to showcase the :adi:`AD9361` or :adi:`AD9364`, a high performance,
highly integrated RF agile transceiver intended for use in RF applications such
as 3G and 4G base station applications and software defined radios.

The :adi:`AD9361` and :adi:`AD9364` operate in the 70 MHz to 6 GHz range,
covering most licensed and unlicensed bands. The boards, due to discrete
external components, may have less performance on some of the RF input/output
connectors (for example, the FMCOMMS2 and specific connectors on the FMCOMMS5
are specifically tuned to 2.4 GHz).

The difference between the :adi:`AD9361` (2 Rx, 2 Tx) and :adi:`AD9364`
(1 Rx, 1 Tx) is the number of channels. Software, HDL, pinout, etc. are all
exactly the same.

.. list-table:: Available Hardware
   :header-rows: 1

   * - Board
     - AD936x Device
     - Simultaneous Tx/Rx
     - Tx Ranges
     - Rx Ranges
     - Connector
   * - :ref:`ARRADIO <arradio>`
     - 1 x AD9361
     - 2 x 2
     - 2 (2400-2500 MHz)
     - 2 (2400-2500 MHz)
     - HSMC
   * - AD-FMCOMMS2-EBZ
     - 1 x AD9361
     - 2 x 2
     - 2 (2400-2500 MHz)
     - 2 (2400-2500 MHz)
     - FMC-LPC
   * - :ref:`AD-FMCOMMS3-EBZ <ad-fmcomms3-ebz>`
     - 1 x AD9361
     - 2 x 2
     - 2 (70-6000 MHz)
     - 2 (70-6000 MHz)
     - FMC-LPC
   * - :ref:`AD-FMCOMMS4-EBZ <ad-fmcomms4-ebz>`
     - 1 x AD9364
     - 1 x 1
     - 1 (2400-2500 MHz) / 1 (70-6000 MHz)
     - 1 (2400-2500 MHz) / 1 (70-6000 MHz)
     - FMC-LPC
   * - :ref:`AD-FMCOMMS5-EBZ <ad-fmcomms5-ebz>`
     - 2 x AD9361
     - 4 x 4
     - 4 (2400-2500 MHz) / 4 (70-6000 MHz)
     - 4 (2400-2500 MHz) / 4 (70-6000 MHz)
     - 2 x FMC-LPC

.. note::

   While the AD9361 digital interface supports both LVDS and CMOS mode, all the
   FMCOMMS boards have been verified in LVDS mode only. Configuring the digital
   interface in CMOS mode is not tested nor supported on these platforms. This is
   due to the purposefully weak CMOS drivers (to keep noise off the part as much
   as possible) and the large capacitance of the FMC connector.

   CMOS mode is known to work on platforms without connectors between the AD936x
   and the digital baseband device (like PicoZed SDR).

Introduction
------------

The AD-FMCOMMS2-EBZ is an analog front-end hardware platform that addresses a
broad range of research, academic, industrial, and defense applications. The
:adi:`AD9361` provides the following capabilities:

- Continuous frequency coverage from 70 MHz to 6.0 GHz
- Up to 56 MHz of instantaneous bandwidth
- 2 x 2 MIMO with shared synthesizer
- Integrated 12-bit DACs and ADCs
- Integrated frequency synthesizers
- Integrated digital filtering and calibration
- SPI access for all device registers

Specifications & Features
~~~~~~~~~~~~~~~~~~~~~~~~~

- General purpose design suitable for any application
- Software tunable across wide frequency range (70 MHz to 6 GHz)
- Less than 200 kHz to 56 MHz channel bandwidth
- Powered from a single FMC connector
- Supports MIMO radio, with less than 1 sample sync on both ADC and DAC
- Includes schematics, layout, BOM, HDL, Linux drivers, and application software
- SPI access for all device registers

Applications
~~~~~~~~~~~~

- Wireless communications demonstration and learning tool
- Remote radio head
- Software-defined radio
- Satellite modems
- Electronic test and measurement equipment
- Radar and advanced imaging
- General purpose data acquisition

Functional Overview
-------------------

.. figure:: cf_ad9361_zc706_bd.jpg
   :align: center

   AD-FMCOMMS2-EBZ functional block diagram

The system consists of four functional partitions: receive path, transmit path,
clocking, and power supply. The data path is fully integrated into the AD9361.

Receive Path
~~~~~~~~~~~~

The AD9361 receive section consists of up to 2 direct conversion RF receive
channels with fully integrated synthesizers (including loop filter). The receive
chain is: LNA, Demodulator, LPF, ADC, Digital Filters.

.. list-table::
   :header-rows: 1

   * - Parameter
     - Value
   * - Channels
     - 2 (direct conversion)
   * - Noise Figure
     - 2.5 dB @ 1 GHz
   * - ADC
     - Continuous-time sigma-delta, 640 MSPS
   * - Digital Filters
     - 128 complex taps, decimation 2-48x
   * - Gain Control
     - 1 dB step size, 80 dB analog + 30 dB digital range
   * - RSSI
     - On-chip temperature-corrected sensor

Transmit Path
~~~~~~~~~~~~~

The AD9361 transmit section provides up to 2 direct conversion RF transmit
channels with fully integrated synthesizers.

.. list-table::
   :header-rows: 1

   * - Parameter
     - Value
   * - Channels
     - 2 (direct conversion)
   * - DAC
     - 320 MSPS
   * - Digital Filters
     - 128 complex taps, interpolation 2-48x
   * - Gain Control
     - 0.25 dB step size, 86 dB range

Clocking
~~~~~~~~

A 40 MHz crystal oscillator is provided on the board. All clocks are fully
software programmable. The AD9361 contains three PLLs:

- **2 RF PLLs** (Rx/Tx, identical): F_RFPLL = F_REF x (N_Integer +
  N_Fractional / 8388593). Step size at 40 MHz REF: 4.77 Hz.
- **1 Baseband PLL**: F_BB = F_REF x (N_Integer + N_Fractional / 2088960).
  Step size at 40 MHz REF: 19.15 Hz.

.. note::

   Integer spur issues occur within +/-1.25% of integer boundary frequencies.

Clock Options
^^^^^^^^^^^^^

- **XTALN**: External oscillator (10-80 MHz) for master clock sync in BTS
  applications
- **XTALP/XTALN**: Dedicated crystal (19-50 MHz) with DCXO tuning for UE
  applications. DCXO tuning range: +/-60 ppm, resolution: 0.0125 ppm
  worst-case.

Crystal Specifications
^^^^^^^^^^^^^^^^^^^^^^

The board uses an Epson TSX-3225 crystal with the following tolerance budget:

.. list-table::
   :header-rows: 1

   * - Parameter
     - Value
   * - Initial Tolerance
     - +/-10 ppm
   * - Temperature Stability
     - +/-15 ppm max
   * - Aging
     - +/-2 ppm max
   * - RMS Average (all effects)
     - +/-18.1 ppm
   * - Frequency Offset at 2.4 GHz
     - +/-43.2 kHz

DCXO Tuning
^^^^^^^^^^^^

The DCXO tuning uses an adjustable capacitor inside the AD9361 crystal tank
circuit (XTALP pin), providing a tuning range of +/-60 ppm. Tuning can be
performed manually or automated using the IIO Oscilloscope with SCPI.

For automated tuning, a frequency counter (Hameg HM8123 or Agilent 53131A) is
required. The measurement can be performed on the REFCLK (CLK_OUT pin on
P202 header) or the RF output. Launch the oscilloscope with the
``OSC_FORCE_PLUGIN=scpi`` flag to enable the tuning interface.

Power Supply
~~~~~~~~~~~~

The board is powered entirely from the FPGA carrier board through the FMC
connector. The power supply components include:

- :adi:`ADP1755`: Low dropout linear regulator (1.2 A, 1.6-3.6 V)
- :adi:`ADP2164`: Step-down DC-DC regulator (6.5 V, 4 A)

Digital Interface
~~~~~~~~~~~~~~~~~

The AD9361 uses a 12-bit DDR parallel interface (LVDS mode) for data transfer
to the FPGA. Full duplex operation supports up to 2x2 MIMO with a shared clock
for TX and RX paths.

- SPI interface for control and configuration
- Control/Monitor signals for gain, sync, and state machine control
- Refer to the AD9361 Reference Manual (UG-570) for complete interface details

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
     - No-OS
   * - :xilinx:`ZC702 <products/boards-and-kits/ek-z7-zc702-g.html>`
     - Yes
     - Yes
     - Yes
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - Yes
     - Yes
     - Yes
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - Yes
     - Yes
     - Yes
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
   * - :xilinx:`AC701 <products/boards-and-kits/ek-a7-ac701-g.html>`
     - Yes
     -
     - Yes

Quick Start
-----------

Prerequisites
~~~~~~~~~~~~~

- Host PC (Windows or Linux)
- SD card with Kuiper Linux image (for Zynq platforms)
- USB keyboard and mouse
- HDMI display (Full HD)
- Antenna or SMA loopback cable
- Power supply as specified by the carrier board
- Ethernet cable (for remote IIO Oscilloscope access)

ZC706 Setup
~~~~~~~~~~~~

.. figure:: cf_ad9361_setup.jpg
   :align: center

   ZC706 + FMCOMMS2 setup

#. Insert the SD card with the Kuiper Linux image into the ZC706.
#. Connect the AD-FMCOMMS2-EBZ to the FMC LPC connector (J5).
#. Set boot jumpers (SW11): 1-Down, 2-Down, 3-Up, 4-Up, 5-Down.
#. Connect HDMI, USB keyboard/mouse, and Ethernet.
#. Power on the board.
#. The DONE LED indicates FPGA programming is complete (~30 seconds).
#. HDMI display appears approximately 60 seconds after power-on.
#. IIO Oscilloscope launches automatically for RF transceiver control.

ZedBoard Setup
~~~~~~~~~~~~~~

.. figure:: quickstart/zed_setup.jpg
   :align: center

   ZedBoard + FMCOMMS2 setup

#. Insert the SD card with the Kuiper Linux image.
#. Connect the AD-FMCOMMS2-EBZ to the FMC LPC connector (J1).
#. Set boot jumpers: JP7-JP11 for SD card boot, JP6 (MIO0) to GND.
#. Set J18 for 1.8 V FMC bank voltage.
#. Connect HDMI, USB keyboard/mouse, and Ethernet.
#. Power on the board.
#. Blue LED and green LED illuminate (~15 seconds), HDMI display follows
   (~30 seconds).

.. figure:: quickstart/zed_sw.png
   :align: center

   ZedBoard boot switch configuration

.. tip::

   To protect against ESD damage, consider using a plexiglass cover over the
   board with a 270 kOhm grounding resistor.

The board can also be accessed remotely over the network. By default, DHCP is
enabled. A static IP can be configured using the ``enable_static_ip.sh``
script.

Additional platform-specific quickstart guides:

- :doc:`MicroBlaze (KC705/VC707) Quick Start Guide <quickstart_microblaze>`
- :doc:`ZCU102 Quick Start Guide <quickstart_zynqmp>`

HDL Reference Design
--------------------

The reference design is a processor-based (ARM Zynq, MicroBlaze, or NIOS II)
embedded system with a self-contained AXI-Lite peripheral for the AD9361
interface.

Architecture
~~~~~~~~~~~~

- **Transmit Path**: Internal DDS with programmable phase/frequency, or
  external DDR source via VDMA
- **Receive Path**: PN monitoring for digital interface validation, optional
  DC filtering and I/Q offset correction, DDR write via DMA, optional
  offline FFT for spectrum analysis
- **Data Width**: 12-bit DDR data paths, full duplex 2x2 MIMO
- **Multi-Core Support**: AD-FMCOMMS5-EBZ uses 2 synchronized instances with
  common clock synchronization

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/fmcomms2`

Software Support
----------------

Linux Drivers
~~~~~~~~~~~~~

- :git-linux:`AD9361 Linux Driver <drivers/iio/adc/ad9361.c>`
- :git-linux:`AXI ADC HDL Linux Driver <drivers/iio/adc/cf_axi_adc_core.c>`
- :git-linux:`AXI DAC DDS Linux Driver <drivers/iio/frequency/cf_axi_dds.c>`

Device Trees
~~~~~~~~~~~~

- :git-linux:`ZC702 DTS <arch/arm/boot/dts/xilinx/zynq-zc702-adv7511-ad9361-fmcomms2-3.dts>`
- :git-linux:`ZC706 DTS <arch/arm/boot/dts/xilinx/zynq-zc706-adv7511-ad9361-fmcomms2-3.dts>`
- :git-linux:`ZED DTS <arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad9361-fmcomms2-3.dts>`
- :git-linux:`ZCU102 DTS <arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dts>`

Linux Applications
~~~~~~~~~~~~~~~~~~

- :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` -- graphical tool
  for device control, waveform capture, and spectrum analysis
- `libiio <https://github.com/analogdevicesinc/libiio>`__ -- C library for
  interfacing with IIO devices locally or over the network
- `pyadi-iio <https://github.com/analogdevicesinc/pyadi-iio>`__ -- Python
  interfaces for ADI hardware

Data Streaming Tools
~~~~~~~~~~~~~~~~~~~~

- `Analog Devices Transceiver Toolbox
  <https://www.mathworks.com/hardware-support/analog-devices-rf-transceivers.html>`__
  -- MATLAB/Simulink streaming support for AD9361 platforms
- `GNU Radio <https://github.com/analogdevicesinc/gr-iio>`__ -- GNU Radio
  IIO blocks for real-time signal processing

No-OS Software
~~~~~~~~~~~~~~

The No-OS bare-metal software provides direct hardware access without a Linux
operating system. Supported platforms include AC701, KC705, VC707, ZC702,
ZC706, and ZedBoard.

For detailed No-OS API reference and serial commands, see
:doc:`no_os_software`.

- :git-no-OS:`projects/ad9361`
- :git-no-OS:`drivers/rf-transceiver/ad9361`

AD9361 Filter Design Wizard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD9361 Filter Design Wizard (MATLAB-based) allows design of transmitter
and receiver FIR filters, accounting for magnitude and phase response from
analog and digital filter stages. For the full walkthrough, see
:doc:`filter_wizard`.

LTE preset profiles are available:

.. list-table::
   :header-rows: 1

   * - LTE Bandwidth
     - Occupied RF BW
     - Sample Rate
   * - 1.4 MHz
     - 1.08 MHz
     - 1.92 MSPS
   * - 3 MHz
     - 2.7 MHz
     - 3.84 MSPS
   * - 5 MHz
     - 4.5 MHz
     - 7.68 MSPS
   * - 10 MHz
     - 9 MHz
     - 15.36 MSPS
   * - 15 MHz
     - 13.5 MHz
     - 23.04 MSPS
   * - 20 MHz
     - 18 MHz
     - 30.72 MSPS

The filter wizard supports phase equalization (reducing passband group delay
variance from 16.6 ns to 1.52 ns typical), FVTool integration, and direct
target connection for uploading coefficients to Zynq boards.

RF Blockset Model
~~~~~~~~~~~~~~~~~

MathWorks provides two validated `RF Blockset
<https://www.mathworks.com/hardware-support/analog-devices-rf-transceivers.html>`__
models of the :adi:`AD9361` for Tx and Rx signal paths. These models can be
used to iterate and evaluate designs prior to hardware implementation.

Required MATLAB toolboxes: MATLAB, Simulink, Simscape, RF Toolbox, RF Blockset,
Stateflow, Signal Processing Toolbox, DSP System Toolbox, Communications System
Toolbox, and Fixed-Point Designer.

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- :adi:`AD9361 Product Page <AD9361>`
- :doc:`RF Card Specifications <card_specification>`
- :doc:`I/Q Data Files <iq_datafiles>`
- :doc:`Digital Interface Timing Validation <interface_timing>`
- :doc:`Production Testing <testing>`

Support
-------

If you have any questions regarding the AD-FMCOMMS2-EBZ feel free to ask on
the :ez:`FPGA Reference Designs Forum <fpga>`.
