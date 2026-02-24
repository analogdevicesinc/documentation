.. _ad9213-dual-ebz:

AD9213-DUAL-EBZ User Guide
===========================

Introduction
------------

The AD9213-DUAL-EBZ reference design is a processor-based (ARM) embedded
system featuring two :adi:`AD9213` ADCs. The device interfaces to the FPGA
transceivers followed by the individual JESD204B and ADC cores. The cores are
programmable through an AXI-Lite interface. The samples are initially captured
in a FIFO buffer and then passed to the system memory (DDR).

The user can capture up to 1048576 samples per channel if both channels are
selected, or 2097152 per channel if only one channel is selected.

The AD9213-DUAL-EBZ platform includes two :adi:`AD9213` single, 12-bit,
10 GSPS radio frequency (RF) ADCs with the JESD204B interface. The two
10 GSPS data converters can be interleaved to sample at 20 GSPS, enabled by
their built-in multi-chip synchronization capability. The :adi:`ADF4377`
ultra-low jitter dual output integer-N PLL with integrated VCO supports the
interleaving. The :adi:`LTC6955` low jitter fanout clock buffer and the
:adi:`LTC6952` JESD204B clock generation and distribution IC enable a clocking
architecture built for multi-channel scalability.

The platform allows users to direct-sample L, S, and C bands, all while
supporting up to 8 GHz of instantaneous bandwidth per channel. It is a
complete reference design from RF to bits: RF layouts, clocking architectures,
power distribution network designs, and a full software stack (HDL to MATLAB).
The design is intended to be plug-and-play out of the box, enabling a
reduction in design and prototype cycle time.

Operation Modes
~~~~~~~~~~~~~~~

The AD9213-DUAL-EBZ supports two primary operation modes:

- **Synchronized 10G Mode** -- Both AD9213 ADCs operate independently at
  10 GSPS with multi-chip synchronization (MCS). Data can be captured and
  plotted from each AD9213 separately or simultaneously.
- **Interleaved 20G Mode** -- The two AD9213 ADCs are interleaved to achieve
  an effective 20 GSPS sample rate. The sample clock to one AD9213 is inverted
  with respect to the other, and the two devices must be gain- and
  timing-aligned. In this mode, voltage 0 (channel 0) represents the combined
  interleaved data from both converters.

Features
~~~~~~~~

- 20 GSPS sample rate through interleaving supporting up to 8 GHz of
  instantaneous bandwidth
- Multi-chip synchronization (MCS) at 10 GSPS using a scalable reference
  distribution architecture
- Input network supporting a wide analog frequency range DC to 9 GHz
- Compact layout scheme that can be quickly adopted into a customer application

Applications
~~~~~~~~~~~~

- Electronic warfare (EW)
- Electronic countermeasures (ECM/ECCM)
- Radar
- Instrumentation
- Multi-channel wideband receivers

Supported Devices
-----------------

- :adi:`AD9213`

Supported Carriers
------------------

- :intel:`Stratix 10 SoC Dev Kit
  <content/www/us/en/products/details/fpga/development-kits/stratix/10-sx.html>`

HDL Reference Design
--------------------

The design has two JESD receive chains each having 16 lanes at a rate of
12.5 Gbps. The JESD receive chain consists of a physical layer represented by
an XCVR module, a link layer represented by an RX JESD LINK module. The
transport layer is common and is represented by a single RX JESD TPL module.

The links operate in Subclass 1 using the SYSREF signal to edge-align the
internal local multiframe clock and to release the received data from all
lanes simultaneously, ensuring that data from all channels is synchronized at
the application layer.

The transport layer component presents 1024 bits on its output on every clock
cycle, representing 16 samples per converter. A custom packing module is
implemented in the system top module because the typical AXI_PACK IP does not
meet timing for this design. An ADC buffer stores 1024k samples per converter
in the fabric before transferring with the DMA.

JESD204B Configuration
~~~~~~~~~~~~~~~~~~~~~~

Both links are set for full bandwidth mode and operate with the following
parameters:

.. list-table::
   :header-rows: 1

   * - Parameter
     - Value
   * - Deframer (L, M, F, S, N')
     - L=32, M=2, F=2, S=16, N'=16
   * - GLBLCLK
     - 312.5 MHz (Lane Rate / 40)
   * - REFCLK
     - 312.5 MHz (Lane Rate / 20)
   * - SYSREF
     - 1.46 MHz (DEVCLK / 2048)
   * - DEVCLK
     - 10000 MHz
   * - JESD204B Lane Rate
     - 12.5 Gbps

Block Diagram
~~~~~~~~~~~~~

.. figure:: s10soc_ad9213_dual_ebz.png
   :align: center

   AD9213-DUAL-EBZ block diagram

Clock Sources
~~~~~~~~~~~~~

.. figure:: ad9213_s10soc_clocking.png
   :align: center

   Clock sources diagram

Both physical layer transceiver modules receive two reference clocks from
the LTC6952 OUT4-7 outputs. The global clock (Lane Rate / 40) is received
from the OUT8 output and SYSREF is received from the OUT9 output of the
LTC6952.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad9213_dual_ebz`

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

- :git-linux:`drivers/iio/adc/ad9208.c`

Quick Start Guide
-----------------

Hardware Requirements
~~~~~~~~~~~~~~~~~~~~~

- Intel Stratix 10 SX SoC Development Kit (1SX280HU2F50E1VGAS)
- AD9213-DUAL-EBZ evaluation board
- RF signal generator (analog signal source and 500 MHz reference clock)
- RF power splitter for splitting the test tone to both ADC inputs
- Phase-matched coaxial cables
- RF balun for single-ended-to-differential conversion of the 500 MHz
  reference clock
- PC with Windows, one mini-USB, one micro-USB, and one Ethernet cable

Software Requirements
~~~~~~~~~~~~~~~~~~~~~

- `Intel Quartus Prime Programmer 19.3 or later
  <https://www.intel.com/content/www/us/en/software-kit/661657/intel-quartus-prime-pro-edition-design-software-version-19-3-for-windows.html>`__
- `PuTTY <https://www.putty.org>`__
- :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`
- `VisualAnalog <https://www.analog.com/en/design-center/interactive-design-tools/visualanalog.html>`__
  (optional, for frequency domain analysis with ADI-provided canvas files)

Board Setup
~~~~~~~~~~~

Configure the Stratix 10 SX SoC board switches as follows:

**SW1:**

.. list-table::
   :header-rows: 1

   * - S10
     - M10B
     - FMCA
     - FMCB
     - PCIE
     - MSTR0
     - MSTR1
     - MSTR2
   * - OFF
     - ON
     - ON
     - ON
     - ON
     - ON
     - ON
     - ON

**SW2 (MSEL):**

.. list-table::
   :header-rows: 1

   * - PIN1
     - PIN2
     - PIN3
     - PIN4
   * - ON
     - ON
     - ON
     - OFF

**SW3 (USR_DIPSW_FPGA):** All pins OFF.

**SW4:**

.. list-table::
   :header-rows: 1

   * - I2C FLAG
     - DC_POWER CTRL
     - FACTORY LOAD
     - SECURITY MODE
   * - ON
     - OFF
     - OFF
     - ON

SD Card Preparation
~~~~~~~~~~~~~~~~~~~

1. Program a blank SD card (16 GB minimum) with the
   :doc:`Kuiper Linux </linux/kuiper/index>` image.
2. Once the image is written, eject and re-insert the SD card.
3. Place the provided ``socfpga_stratix10_socdk.dtb`` and ``u-boot.itb`` files
   into the top-level directory (BOOT partition) of the SD card.
4. Additionally, place the appropriate ``Image`` file into the BOOT partition:

   - For **Synchronized 10G Mode**: use the image from the ``Dual 10G Image``
     folder.
   - For **Interleaved 20G Mode**: use the image from the
     ``Single 20G Image`` folder.

5. Insert the SD card into the Stratix 10 SX SoC board.

FPGA Programming
~~~~~~~~~~~~~~~~

1. Connect a mini-USB cable from the Stratix 10 board to the host PC for JTAG.
2. Open Intel Quartus Prime Programmer 19.3.
3. The software should detect the Stratix 10 SoC Evaluation Board automatically
   in the Hardware Setup section. If it does not appear, select it manually.
4. Click **Add File**, navigate to the ADI-provided FPGA binary (``.sof``
   file), and click **Open**.
5. Click **Start** and wait for the programmer to complete.

.. note::

   Programming the FPGA also triggers the Linux boot on the HPS. The PuTTY
   COM console provides updates on the progress of the boot.

Connecting to the Board
~~~~~~~~~~~~~~~~~~~~~~~

1. Set up a serial COM port connection using PuTTY at 115200 baud to monitor
   the boot process.
2. Once the boot and initialization scripts have completed, obtain the board's
   IP address by running ``ifconfig`` in the console.
3. Open IIO Oscilloscope, go to the **Connect** tab, select **manual**, enter
   ``ip:<board-ip>`` in the URL field, and click **Refresh**.
4. All IIO devices on the evaluation board (including both AD9213s and the
   clock chips) will appear. Click **Connect**.
5. Use the plotting window to capture data from one AD9213 at a time or from
   both simultaneously. Time domain and frequency domain captures are
   available.

The board runs at login ``root`` with password ``analog``.

For **Interleaved 20G Mode**, an SSH connection to the board is also required
to run SPI scripts for gain and timing alignment. Open PuTTY with SSH as the
connection type, use the board's IP address, and port 22.

Using VisualAnalog
~~~~~~~~~~~~~~~~~~

For more detailed frequency domain analysis, VisualAnalog can be used with
ADI-provided canvas files:

1. Install `libiio <https://github.com/analogdevicesinc/libiio/releases>`__
   (required for the IIO Client block in VisualAnalog).
2. Open the appropriate VisualAnalog canvas:

   - **Synchronized 10G Mode**: ``Dual9213_IIOScope_FFT.vac``
   - **Interleaved 20G Mode**: ``Dual9213_Interleaved20G_FFT.vac``

3. Open the IIO Client module settings and enter the IP address of the
   Stratix 10 board, set the sampling frequency and sample size, and enable
   the desired channels.
4. Click **Play** to capture FFTs.

For Interleaved 20G Mode, before capturing data, ensure the two AD9213s are
gain- and timing-aligned using the ADI-provided calibration scripts.

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the core
with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
