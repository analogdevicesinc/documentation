Hardware
========

Functional Overview
-------------------

Transmit Path
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Component
     - Function
   * - :adi:`AD9122`
     - Dual 16-bit, 1200 MSPS TxDAC with offset, phase, and gain compensation
   * - :adi:`ADL5375`
     - 400 MHz to 6 GHz broadband quadrature modulator
   * - :adi:`ADL5602`
     - 50 MHz to 4.0 GHz RF/IF gain block (20 dB)
   * - :adi:`ADF4351`
     - Wideband synthesizer with integrated VCO (35 MHz to 4400 MHz)

Output power is up to 7.5 dBm. Transmit bandwidth is up to 250 MHz depending
on ADL5602/ADL5375 response flatness. Optional amplifiers (:adi:`ADL5605` or
:adi:`ADL5606`) can be added for antenna driving.

Receive Path
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Component
     - Function
   * - :adi:`ADL5380`
     - 400 to 6000 MHz quadrature demodulator (500 MHz bandwidth)
   * - :adi:`AD8366`
     - DC to 600 MHz dual variable gain amplifier (4.5 dB to 20.25 dB gain)
   * - :adi:`AD9643`
     - 14-bit, 250 MSPS dual analog-to-digital converter

Baseband response extends to DC to 400 MHz (-3 dB point). An optional
external LNA (:adi:`ADL5523`, 400 MHz to 4000 MHz) can be used.

Clocking
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Component
     - Function
   * - :adi:`AD9548`
     - Quad/octal input network clock generator (1 Hz to 750 MHz)
   * - :adi:`AD9523-1`
     - Low jitter clock generator with 14 outputs (1 MHz to 1 GHz)

Default clock configuration: 30 MHz FPGA clock is cleaned up via the AD9548,
then the AD9523-1 generates 491.52 MHz for DAC sample rate, 245.76 MHz for
ADC sample rate, and 122.88 MHz for LO PLL reference clocks. External
synchronization is supported for multiple board configurations.

Power Supply
~~~~~~~~~~~~

The board is powered entirely from the FPGA carrier board through the FMC
connector:

- :adi:`ADP2323`: 3 A switching regulator
- :adi:`ADP7104`: 500 mA low dropout regulator
- :adi:`ADP151`: 150/200 mA ultra-low-noise LDO
- :adi:`ADP1740`: 2 A LDO

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

The board ships in the default RF-enabled configuration. The ADC RF section
uses three-pad solder jumpers (JP1-JP3, JP7) and the DAC RF section uses
solder jumpers (JP4-JP6, JP17).

A bypass mode (RF disabled) is available for direct analog interface to the
ADC inputs/DAC outputs, but performance suffers and the RF section still
consumes power.

.. warning::

   Frequent jumper changes will damage the solder pads and they may lift off
   the board. Solder jumpers provide better RF performance than traditional
   pin jumpers.

Three Pi attenuators (0 dB default) are included in the design: one in the
receive chain (before the balun) and two in the transmit chain.

I2C-to-SPI Bridge
~~~~~~~~~~~~~~~~~~

To stay within the LPC FMC pin count, the board uses a PIC microcontroller
as an I2C-to-SPI bridge for device register access (SPI chip selects would
exceed the LPC pin count).

.. list-table:: I2C Slave Addresses
   :header-rows: 1

   * - FMC Connector
     - I2C Address
   * - HPC
     - 0x58
   * - LPC
     - 0x59

.. list-table:: SPI Device Map
   :header-rows: 1

   * - Device
     - Chip Select
     - SPI Mode
     - Function
   * - :adi:`AD8366`
     - 6
     - MODE_0, 3-Wire
     - VGA
   * - :adi:`AD9122`
     - 0
     - MODE_0
     - DAC
   * - :adi:`AD9523-1`
     - 3
     - MODE_0, 3-Wire
     - Clock Distribution
   * - :adi:`AD9548`
     - 2
     - MODE_0, 3-Wire
     - Clock Sync
   * - :adi:`AD9643`
     - 1
     - MODE_0, 3-Wire
     - ADC
   * - :adi:`ADF4351`
     - 4
     - MODE_0
     - RX PLL
   * - :adi:`ADF4351`
     - 5
     - MODE_0
     - TX PLL

Supported Devices
-----------------

- :adi:`AD9122` (DAC)
- :adi:`AD9643` (ADC)
- :adi:`AD9523-1` (Clock Generator)
- :adi:`AD9548` (Clock Sync)
- :adi:`ADF4351` (Synthesizer)
- :adi:`AD8366` (VGA)
- :adi:`ADL5375` (Quadrature Modulator)
- :adi:`ADL5380` (Quadrature Demodulator)

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Board
     - Platform
     - HDL
   * - :xilinx:`ZC702 <products/boards-and-kits/ek-z7-zc702-g.html>`
     - Zynq
     - Yes
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - Zynq
     - Yes
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Zynq
     - Yes
   * - :xilinx:`KC705 <products/boards-and-kits/ek-k7-kc705-g.html>`
     - MicroBlaze
     - Yes
   * - :xilinx:`VC707 <products/boards-and-kits/ek-v7-vc707-g.html>`
     - MicroBlaze
     - Yes
