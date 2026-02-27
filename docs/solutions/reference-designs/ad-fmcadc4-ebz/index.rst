.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcadc4-ebz

.. _ad-fmcadc4-ebz:

AD-FMCADC4-EBZ
===============

.. warning::

   The :adi:`AD-FMCADC4-EBZ <EVAL-AD-FMCADC4-EBZ>` board has been retired
   and is no longer available for sale. Support has been discontinued, with the
   latest tested release being **2018_r2**. The HDL project has been removed
   from the main branch but is still available in the
   :git-hdl:`hdl_2018_r2 <hdl_2018_r2:projects/fmcadc4>` release branch.

The :adi:`AD-FMCADC4-EBZ <EVAL-AD-FMCADC4-EBZ>` is a high speed four channel
data acquisition board featuring two :adi:`AD9680` dual channel ADCs at
1000 MSPS (1240 MSPS) and four :adi:`ADA4961` low distortion, 3.2 GHz, RF
DGAs driving each converter. The FMC form factor supports the JESD204B high
speed serial interface. All clocking and channel synchronization is provisioned
on-board using the :adi:`AD9528` clock generator.

This board is targeted to use the ADI reference designs that work with Xilinx
development systems.

.. image:: ad-fmcadc4-ebz-top.jpg
   :align: center
   :width: 500

Hardware
--------

The AD-FMCADC4-EBZ board's primary purpose is to demonstrate the capabilities
of the devices on board quickly and easily by providing a seamless interface
to an FMC carrier platform and running the reference design on the carrier
FPGA. The board is designed to self power and self clock when connected to the
FMC carrier. The analog signals (up to four) are connected to J301A, J301B,
J301C and J301D. This rapid prototyping board can also be synchronized across
channels.

.. figure:: ad-fmcadc4-ebz-bottom.jpg
   :align: center
   :width: 500

   AD-FMCADC4-EBZ bottom view

Devices
~~~~~~~

The FMC board includes the following products by Analog Devices:

- :adi:`AD9680` 14-bit dual channel ADC with sampling speeds of up to
  1250 MSPS, with a JESD204B digital interface
- :adi:`ADA4961` Low Distortion, 3.2 GHz, RF Digital Gain Amplifier
- :adi:`AD9528` JESD204B Clock Generator with 14 LVDS Outputs
- :adi:`ADP2384` 20 V, 4 A, Synchronous, Step-Down DC-to-DC Regulator
- :adi:`ADP7104` 20 V, 500 mA, low noise, CMOS LDO
- :adi:`ADM7154` 600 mA, Ultra Low Noise, High PSRR, RF Linear Regulator
- :adi:`ADM7172` 6.5 V, 2 A, Ultralow Noise, High PSRR, Fast Transient
  Response CMOS LDO
- :adi:`ADP1741` 2 A, low Vin, low dropout, CMOS linear regulator

Clocking
~~~~~~~~

The AD-FMCADC4-EBZ includes an on-board 80 MHz reference oscillator from
Crystek. This feature can be disconnected and an external reference can be
applied through J901. When referencing the schematic make sure the proper
component changes are made in order to directly route the input into the
AD9528.

The :adi:`AD9528` clock generator is configured to produce the following
default clocks:

- **ADC sampling clock:** 1000 MHz for both :adi:`AD9680` devices
- **FPGA reference clock:** 500 MHz for the JESD204B transceiver cores

Analog Front End
~~~~~~~~~~~~~~~~

The AD-FMCADC4-EBZ uses a passive front end designed for very wide bandwidth.
A single ended input needs to be provided to the analog inputs. A 1:2
impedance ratio broadband balun then converts the input signal differentially
to the ADA4961 inputs and has a 1.6 GHz bandwidth at -3 dB. Each channel
amplifier can be adjusted independently in terms of gain.

Note for Revision A
~~~~~~~~~~~~~~~~~~~~

The revision A board supports amplifier gain control via SPI. After power-up,
the gain of the amplifier defaults to an attenuated state. Use a low jitter,
low noise signal source with a level at -20 dBm to the analog inputs
(J301-A/B/C/D). Apply a signal source no greater than -10 dBm to achieve
full-scale of the converter when maximum gain of the amplifier is applied.

Supported Carriers
------------------

- :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>` HPC Slot

HDL Reference Design
--------------------

The reference design includes the device data capture via the JESD204B serial
interface and the SPI interface. The samples are written to the external
DDR-DRAM. It allows programming the device and monitoring its internal
registers via SPI.

The design uses ADI's JESD204B IP core which must be programmed to match the
device settings (frame count, byte count, scrambling, etc.). The transceiver
cores are initialized with DRP access and the JESD204B link is brought up by
checking PLL lock status through to SYNC de-assertion.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`hdl_2018_r2:projects/fmcadc4/zc706`

No-OS Application
-----------------

The HDL reference design is built around a processor as in an embedded system.
A No-OS application is available that demonstrates the design without a full
operating system. The application performs the following initialization
sequence:

#. Configure GPIOs and bring the :adi:`AD9528` clock generator out of reset.
#. Program the :adi:`AD9528` to output the desired clocks and SYSREF signals
   (default: 1 GHz for the :adi:`AD9680`, 500 MHz for the FPGA).
#. Initialize the transceiver cores (DRP access only).
#. Initialize both :adi:`AD9680` devices and verify PLL lock status.
#. Program the JESD204B IP to match device settings (frame count, byte count,
   scrambling).
#. Bring up the transceivers and verify the link (PLL lock through SYNC
   de-assertion).
#. Bring the individual ADC cores out of reset.
#. Run PRBS verification to confirm link integrity at the sample level.
#. Capture data to DDR-DRAM.

The No-OS source code can be built using the following steps:

#. Clone the `No-OS repository <https://github.com/analogdevicesinc/no-OS>`__.
#. Checkout the release branch matching the HDL release (see
   `HDL release notes <https://github.com/analogdevicesinc/hdl/releases>`__).
#. Navigate to the ``fmcadc4/zc706`` directory.
#. Run ``make`` (optionally specify the HDF file path with
   ``make HDF-FILE=<path>/system_top.hdf``).
#. Run ``make run`` to download the HDL bitstream and software ELF via JTAG.
#. Run ``make capture`` to read captured samples from RAM (saved as CSV files).

Upon successful execution, the UART terminal should display::

   QPLL ENABLE
   Rx link is enabled
   Measured Link Clock: 250 MHz
   Link status: DATA
   SYSREF captured: Yes
   adc_setup adc core initialized (1000 MHz).
   adc_setup adc core initialized (1000 MHz).
   RX capture done.

Software Support
----------------

Linux Drivers
~~~~~~~~~~~~~

- :git-linux:`AD9680 Linux Driver <drivers/iio/adc/ad9680.c>`
- :git-linux:`ADA4961 Linux Driver <drivers/iio/amplifiers/ad8366.c>`
- :git-linux:`AXI ADC HDL Linux Driver <drivers/iio/adc/cf_axi_adc_core.c>`
- :git-linux:`JESD204B Receive Linux Driver <drivers/iio/jesd204/axi_jesd204_rx.c>`

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the core
with Analog Devices components (ADC, DAC, Video, Audio, etc) via the
:ez:`FPGA Reference Designs Forum <fpga>`.
