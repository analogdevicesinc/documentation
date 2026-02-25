Hardware
========

Hardware Specifications
-----------------------

.. list-table::
   :header-rows: 1

   * - Parameter
     - Value
   * - FPGA
     - Xilinx Zynq XC7Z035-L2 FBG676I (dual-core ARM Cortex-A9 + PL),
       -2 speed grade, low power (-L) bin
   * - RF Transceiver
     - :adi:`AD9361` (70 MHz to 6 GHz, 200 kHz to 56 MHz channel bandwidth)
   * - Memory
     - 1 GB DDR3L (2x MT41K256M16HA-125), 256 Mbit quad-SPI NOR flash
       (Micron N25Q256A)
   * - DDR3L Speed
     - 1,066 MT/s
   * - Data Interface
     - Dual parallel ports (P0, P1) in LVDS mode (DDR)
   * - Max Data Rate
     - 122.88 MSPS (AD9361 maximum)
   * - Channels
     - 2 Rx x 2 Tx
   * - PCB
     - 20-layer, 62 mm x 100 mm
   * - Connectors
     - 4x FCI 0.8 mm BergStak 100-position micro headers (JX1--JX4)
   * - Temperature Range
     - Industrial (-40 to +85 deg C)

AD9361/Zynq SoC Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV9361-Z7035 connects the Zynq Z-7035 SoC directly to the :adi:`AD9361`
with dedicated high-bandwidth data ports, clocks, an SPI control interface, and
framing signals.

The AD9361 digital interface comprises two parallel data ports (P0 and P1) and
several clock/synchronization signals to transfer samples between the AD9361
and the Zynq SoC. In LVDS mode the interface operates in double-data rate
(DDR), sending 12-bit samples across two 6-bit lanes on differential pairs.
The maximum rate across the data interface is limited by the AD9361 maximum
data rate of 122.88 MSPS.

While the AD9361 supports both LVDS and CMOS modes, all reference designs for
this SOM use LVDS. CMOS mode is known to work on platforms without connectors
between the AD9361 and the digital baseband device, but is not tested or
supported through the FMC connector interface.

Memory Subsystem
~~~~~~~~~~~~~~~~

**DDR3L** -- Two Micron MT41K256M16HA-125 DDR3L components create a
256M x 32-bit interface (1 GB). The DDR3L memory connects to the hard memory
controller in the Zynq PS with fly-by routing topology per Xilinx UG-933.
Speeds of up to 1,066 MT/s are supported.

**Quad-SPI Flash** -- A Micron N25Q256A 256 Mbit quad-SPI NOR flash provides
non-volatile boot, application code, and data storage. It can initialize the
Zynq PS subsystem and configure the PL (bitstream). In quad-SPI mode it
supports data rates up to 400 Mb/s (108 MHz clock, x4).

**Micro SD Card** -- A micro SD card interface connects through the Zynq PS
SD/SDIO peripheral via a TI TXS02612 SDIO Port Expander with voltage-level
translation and ESD protection. Switch S1 on the SOM selects between the SOM
micro SD card and a carrier card SD interface.

Peripheral Interfaces
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Interface
     - Description
   * - USB 2.0 OTG
     - Microchip USB3320 ULPI PHY, host or device mode via carrier card
   * - Gigabit Ethernet
     - Marvell 88E1512 PHY, RGMII to Zynq PS, RJ-45 on carrier card
   * - JTAG
     - Routed to JX1 connector, 3.3 V Bank 0
   * - GTX Transceivers
     - 4x full-duplex lanes, up to 6.6 Gb/s each, 2 reference clock inputs
   * - User I/O
     - 193 Zynq PL SelectIO pins, 12 Zynq PS MIO pins, 4 AD9361 GPO pins

User I/O Summary
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Bank
     - Type
     - Voltage
     - Available Pins
     - LVDS Pairs
     - Max DDR LVDS Rate
   * - 12
     - HR
     - 1.2--3.3 V (set by carrier)
     - 50
     - 24
     - 1,250 Mb/s
   * - 13
     - HR
     - 1.2--3.3 V (set by carrier)
     - 48
     - 23
     - 1,250 Mb/s
   * - 33
     - HP
     - 1.2--1.8 V (set by carrier)
     - 50
     - 24
     - 1,400 Mb/s
   * - 34
     - HP
     - 1.2--1.8 V (set by carrier)
     - 45
     - 22
     - 1,400 Mb/s

Auxiliary ADC and DAC
~~~~~~~~~~~~~~~~~~~~~

In addition to the primary RF signal chain, the SOM provides access to:

- **AD9361 Auxiliary ADC** -- 12-bit, 0.05 V to 1.25 V input range, routed to
  JX4-7. Multiplexed with a built-in temperature sensor.
- **AD9361 Auxiliary DACs** -- Two 10-bit DACs (0.5 V to VDD_GPO - 0.3 V,
  10 mA drive), routed to JX4-8 and JX4-10. Can provide PA bias or other
  system functionality.
- **Zynq XADC** -- Dual 12-bit 1 MSPS ADCs with on-chip thermal and supply
  sensors. Primary differential input (VP_0/VN_0) on JX3-1/JX3-3.

Clock Architecture
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Clock
     - Frequency
     - Source
     - Notes
   * - Zynq PS
     - 33.333 MHz
     - ABRACON ASDMB oscillator
     - Dedicated PS clock, generates PL clocks via PLLs
   * - AD9361
     - 40 MHz
     - Rakon 513371 crystal (default)
     - External clock input (10--80 MHz) via ADG772 MUX, selected by
       Zynq PL Bank 34 pin K11
   * - Ethernet PHY
     - 25 MHz
     - FOX ABM8G crystal
     - Cannot be disabled
   * - USB PHY
     - 24 MHz
     - ABRACON ASDMB oscillator
     - Can be powered down via PS_MIO9

The external clock input enables multi-SOM synchronization when used with the
SYNC_IN signal connected to the Zynq SoC.

RF Connections
~~~~~~~~~~~~~~

The SOM connects four RX and four TX analog RF channels to the AD9361, plus
two TX Monitor inputs. All TX/RX analog RF signals pass through Mini Circuits
TCM1-63AX+ wideband differential-to-single-ended transformers (50 ohm,
10 MHz to 6 GHz) and terminate at U.FL miniature coaxial connectors.

.. warning::

   Take care when plugging and unplugging cables from the U.FL connectors to
   avoid damaging the surface-mount connectors. U.FL connectors are designed
   to connect to cables, not PCBs. Plug insertion and extraction tools are
   recommended.

Boot Configuration
~~~~~~~~~~~~~~~~~~

The SOM supports three boot modes selected by switches S1, S3, and S4:

.. list-table::
   :header-rows: 1

   * - Boot Mode
     - S4 (MIO4)
     - S3 (MIO3)
     - S1
   * - Cascade JTAG
     - 0
     - 0
     - x
   * - Quad-SPI
     - 1
     - 0
     - x
   * - SD Card (SOM)
     - 1
     - 1
     - 0
   * - SD Card (Carrier)
     - 1
     - 1
     - 1

.. note::

   White dot on switch is logic 0.

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Carrier
     - Description
   * - ADRV1CRR-FMC (PZSDRCC-FMC)
     - FMC Carrier
   * - ADRV1CRR-BOB (PZSDRCC-BRK)
     - Breakout/BOB Carrier
   * - PZSDRCC-PCIE
     - PCIe Carrier
   * - PZSDRCC-PackRF
     - PackRF Carrier

.. note::

   The ADRV9361-Z7035 supports all features on the
   :adi:`ADRV1CRR-FMC <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-FMC.html>`
   carrier board. For breakout/BOB use, the
   :adi:`ADRV1CRR-BOB <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-BOB.html>`
   is recommended.

Performance
-----------

EVM Results
~~~~~~~~~~~

Error Vector Magnitude (EVM) testing was performed on the ADRV9361-Z7035 using
an LTE10 (64-QAM) waveform generated from the MathWorks LTE System Toolbox.
The waveform was transmitted through the AD9361 TX signal chain and received
through the RX chain using U.FL-to-U.FL loopback cables, swept from 70 MHz to
6 GHz in 100 MHz steps.

All EVM measurements were under approximately 2.5% (-32 dB combined TX+RX).
The AD9361 datasheet specifications are approximately -37.8 dB TX and -37.5 dB
RX (about 1.4% each), yielding an expected combined value of approximately
1.86% (-34.6 dB). The difference of 0.6% is attributed to the wideband
transformers on the SOM versus the narrowband baluns used for datasheet
measurements.

Environmental and Mechanical
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV9361-Z7035 is rated for operation in the industrial temperature range
(-40 to +85 deg C). Environmental testing was performed against MIL-STD-202G
and MIL-STD-810G standards:

- **Emissions and Immunity** -- EN 55022:2010 unwanted emissions and
  EN 55024:2010 immunity (CE Mark)
- **Sinusoidal Vibration** -- MIL-STD-202G Method 201A (10--55 Hz sweep,
  0.03 in amplitude, 2 hours per axis)
- **Random Vibration** -- MIL-STD-202G Method 214A (50--2000 Hz, 5.35 g rms,
  1.5 hours per axis)
- **Shock** -- MIL-STD-202G Method 213B (20 g half-sine, 11 ms, 18 total
  shocks)

Both the Zynq SoC and the AD9361 can measure and report their internal die
temperature using built-in data converters. These can be used to monitor
real-time temperature and trigger cooling. A heat sink may be attached directly
to the Zynq SoC package for additional heat dissipation.

Mechanical
----------

The SOM uses a 20-layer PCB measuring 62 mm x 100 mm, compatible with the
DP10062 form factor specification.

The micro headers are FCI 0.8 mm BergStak 100-position dual-row BTB vertical
receptacles (61082-101400LF) that mate with FCI 0.8 mm BergStak plugs
(61083-10x400LF) for variable stack heights of 5 mm to 8 mm. Both receptacle
and plug include PCB locator pegs for precise alignment.

Revision History
----------------

**Revision F** (current shipping version):

- RF traces modified to improve insertion loss, return loss, and EVM.
  Schematic unchanged from Rev E.

**Revision E**:

- No public change notes.

**Revision D**:

- Moved all GTX ports from Bank 111 to Bank 112 for PCIe compliance.
- Improved power structure and increased 0.95 V current from 2 A to 6 A.
- Added 1000BASE-KX Ethernet PHY option.
- Added revision and part number to silkscreen/copper.
- LED D3 anode connected to 3V3_I2C for power-up state indication.

**Revision C** (first publicly available revision).
