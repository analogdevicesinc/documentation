.. imported from: https://wiki.analog.com/resources/eval/ad9694-500ebz

.. _ad9694-fmc:

AD9694-FMC User Guide
=====================

Introduction
------------

The :adi:`AD9694` is a quad-channel, 14-bit, 500 MSPS analog-to-digital
converter (ADC) featuring an on-chip buffer and a sample-and-hold circuit
designed for low power, small size, and ease of use. The quad ADC cores feature
a multistage, differential pipelined architecture with integrated output error
correction logic. Each ADC features wide bandwidth inputs supporting a variety
of user-selectable input ranges.

The AD9694-FMC reference design is a processor-based embedded system. The
design consists of a receive chain that transports the captured samples from
the ADC to system memory (DDR). All cores in the receive chain are
programmable through an AXI-Lite interface.

Features
~~~~~~~~

- Full-featured evaluation board for the :adi:`AD9694`
- JESD204B coded serial digital outputs with support for lane rates up to
  15 Gbps/lane
- Wide full-power bandwidth supports IF sampling of signals up to 1.4 GHz
- Four integrated wideband decimation filter and NCO blocks supporting
  multi-band receivers
- Flexible SPI interface controls various product features and functions
- Programmable fast over-range detection and signal monitoring

Supported Devices
-----------------

- :adi:`AD9694`

Supported Carriers
------------------

- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` -- HPC1 Slot

Hardware
--------

Required Hardware
~~~~~~~~~~~~~~~~~

- AD9694-500EBZ evaluation board
- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` carrier
- 12 V, 6.5 A switching power supply
- Low phase noise 500 MHz sample clock source
- Low phase noise analog input source with antialiasing filter
- Reference clock source for FPGA transceivers
- SMA to SMA cables

Clock Configuration
~~~~~~~~~~~~~~~~~~~~

The AD9694-FMC reference design requires external clock sources for proper
operation.

.. list-table::
   :header-rows: 1

   * - Clock Signal
     - Frequency
     - Source
   * - ADC CLK
     - 500 MHz
     - External
   * - REFCLK
     - 500 MHz
     - External (Lane Rate / 20)
   * - DEVICE CLK
     - 250 MHz
     - External (Lane Rate / 40)
   * - SYSREF
     - 7.8125 MHz
     - External

REFCLK Calculation
^^^^^^^^^^^^^^^^^^^

For custom JESD204B configurations, the reference clock frequency depends on
the lane rate and decimation settings:

- Lane Line Rate = M x N' x (10/8) x Fout / L (bps/lane)
- Fout = ADC Sample Clock / Decimation Ratio
- REFCLK = Lane Line Rate / 20

With the default full bandwidth mode settings (L=4, M=4, N'=16, DCM=1), the
lane rate is 10 Gbps and the REFCLK is 500 MHz.

Standalone Evaluation with ADS7-V2
-----------------------------------

The AD9694-500EBZ can also be evaluated as a standalone board using the
ADS7-V2EBZ FPGA-based data capture kit, without requiring the ZCU102 carrier
or HDL reference design.

Equipment Needed
~~~~~~~~~~~~~~~~

- PC running Windows
- USB 2.0 port and USB 2.0 high-speed A-to-B cable
- AD9694-500EBZ evaluation board
- ADS7-V2EBZ FPGA-based data capture kit
- 12 V, 6.5 A switching power supply
- Low phase noise analog input source and antialiasing filter
- Low phase noise sample clock source
- Reference clock source
- `Analysis | Control | Evaluation (ACE) <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`__
  software

Board Configuration
~~~~~~~~~~~~~~~~~~~~

Before using the software for testing, configure the evaluation boards as
follows:

1. Before connecting the AD9694 to the ADS7-V2, jump the following pins:
   **P307**, **P308**, **P309**, **P311**, **P304**, **P305**, **P312**, and
   **P602** (SPI Enable). Do not jump **P100** (Power Down/Standby) and
   **P1**. Jump **P401** towards the inside of the board to power the board
   via FMC.
2. Ensure that the data capture board is switched to **OFF** (**S1** on the
   data capture board). Connect the evaluation board to the data capture board
   via the FMC connector found on the underside of the board. Connect the
   power supply and USB cable to the data capture board.
3. Turn on the ADS7-V2EBZ.
4. Provide a clean, low-jitter 500 MHz clock source to connector **P202** and
   set the amplitude to 10 dBm. This is the ADC sample clock.
5. On the ADS7-V2, provide a clean, low-jitter reference clock to connector
   **J3** and set the amplitude to 10 dBm. The REFCLK frequency should match
   the JESD204B lane configuration.
6. Connect a clean signal generator with low phase noise to **J101** or
   **J104** via coaxial cable for the desired input channel. It is recommended
   to use a narrow-band bandpass filter with 50 Ohm terminations.

.. warning::

   The AD9694-500EBZ is electrostatic discharge (ESD) sensitive. Handle the
   device with care, and employ conducting wrist straps or antistatic bags when
   handling the board.

Troubleshooting
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Domain
     - Jumper
     - Test Point
     - Approx. Voltage
   * - AVDD_0P9
     - P307
     - TP303
     - 0.95 V
   * - AVDD_1P8
     - P308
     - TP304
     - 1.80 V
   * - AVDD_BUF
     - P309
     - TP305
     - 2.50 V
   * - DRVDD_0P9
     - P304
     - TP301
     - 0.95 V
   * - AVDD_1P8_PLL
     - P311
     - TP306
     - 1.80 V
   * - DVDD_0P9
     - P305
     - TP302
     - 0.95 V
   * - AVDD_1P8_SPI
     - P312
     - TP307
     - 1.80 V

If a short is detected between any of the supply domains and ground, or an
open is detected across fuse chip F401 (next to P401), a component may have
been damaged from jumper or board removal while being actively powered.

HDL Reference Design
--------------------

The design has two JESD204B receive links with a total of 4 lanes at a rate
of 10 Gbps. Each JESD receive chain consists of a physical layer represented
by an XCVR module, a link layer represented by an RX JESD LINK module, and a
transport layer represented by an RX JESD TPL module. The link operates in
Subclass 1.

The default configuration uses full bandwidth mode. The transport layer
component presents the captured samples on its output every clock cycle. The
four receive channels are merged together and transferred to the DDR with a
single DMA.

JESD204B Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Parameter
     - Value
   * - L (Lanes per link)
     - 2 (4 total)
   * - M (Converters per link)
     - 2 (4 total)
   * - S (Samples per frame)
     - 1
   * - F (Octets per frame)
     - 2
   * - N' (Bits per sample)
     - 16
   * - Encoder
     - 8B10B
   * - JESD204B Lane Rate
     - 10 Gbps
   * - Subclass
     - 1

Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Parameter
     - Options
     - Default
   * - RX_JESD_L
     - 2, 4
     - 4
   * - RX_JESD_M
     - 2, 4, 8
     - 4
   * - RX_JESD_S
     - 1, 2
     - 1

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad9694_fmc`

HDL Documentation
~~~~~~~~~~~~~~~~~

- `AD9694-FMC HDL project <https://analogdevicesinc.github.io/hdl/projects/ad9694_fmc/index.html>`__

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The bitstream must be built from source. Clone the HDL repository and build
the ZCU102 project:

.. code-block:: bash

   cd hdl/projects/ad9694_fmc/zcu102
   make

Custom JESD204B configurations can be specified:

.. code-block:: bash

   cd hdl/projects/ad9694_fmc/zcu102
   make RX_JESD_L=2 RX_JESD_M=4 RX_JESD_S=1

A comprehensive build guide is available in the
`HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__.

Quick Start
-----------

Hardware Setup
~~~~~~~~~~~~~~

1. Connect the AD9694-500EBZ to the ZCU102 FMC HPC1 connector.
2. Connect the external clock sources (ADC CLK, REFCLK, SYSREF) per the
   clock configuration table above.
3. Connect SMA terminations to unused SMA connectors.
4. Power the ZCU102 with the 12 V supply.
5. Boot :doc:`Kuiper Linux </linux/kuiper/index>` from the SD card.

Verifying the Design
~~~~~~~~~~~~~~~~~~~~

After booting Linux on the ZCU102, verify that the IIO device is present:

.. code-block:: bash

   root@analog:~# iio_info | grep iio:device
           iio:device0: ams
           iio:device1: axi-ad9694-hpc (buffer capable)

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The AD9694 uses the AD9208 Linux IIO driver. Driver and device tree source
files:

- :git-linux:`drivers/iio/adc/ad9208.c`
- :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9694.dts`

ACE Software
~~~~~~~~~~~~

For standalone evaluation with the ADS7-V2EBZ, the
`Analysis | Control | Evaluation (ACE) <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`__
software provides device configuration, register-level control, FFT analysis,
and data capture capabilities.

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__
- :adi:`AD9694 Product Page <AD9694>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
