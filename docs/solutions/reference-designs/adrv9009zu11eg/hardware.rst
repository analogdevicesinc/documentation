Hardware
========

RF-SOM Overview
---------------

The ADRV9009-ZU11EG RF-SOM package includes the board with a heat spreader
plate mounted on top. The heat spreader plate is designed to accommodate an
active cooler with an AMD-type SP3/TR4/sTRX4 socket.

Connector Interface
-------------------

The interface to the ADRV9009-ZU11EG consists of two SAMTEC SEARAY 400-pin
female connectors (P1 and P2).

**P1 Connector:**

- 24x GTH transceiver lanes with reference clock inputs
- Reference clock and synchronization inputs for on-board :adi:`HMC7044`
  clock generator
- Analog and digital I/O signals from two on-board ADRV9009 transceivers
- Dedicated SPI bus for ADRV9009 and HMC7044
- ZU11EG programmable logic GPIOs
- Power fault signals (PWR_FAULT1, PWR_FAULT2)
- 1.8 V digital supply output (for powering I/O buffers only)

**P2 Connector:**

- ZU11EG PL GPIOs and PS MIO pins
- ZU11EG GTR lanes
- SD 3.01 memory card interface
- MDI interface to Marvell 88E1512 Ethernet PHY
- USB 2.0 interface to Microchip USB3320C PHY
- ZU11EG JTAG interface and configuration pins
- I2C interface for :adi:`ADM1266` power sequencer
- Power good signals and 12 V power input
- PL bank I/O supply inputs and reference inputs
- 1.8 V, 3.3 V digital supply outputs (for powering I/O buffers only)

Power
-----

The ADRV9009-ZU11EG is powered from a single 12 V supply (12 V +/- 8%,
120 W). The board features:

- :adi:`ADM1177` hot-swap controller for safe board insertion, with digital
  current and voltage monitoring via 12-bit ADC over I2C
- :adi:`ADM1266` voltage sequencer/supervisor that monitors input voltage,
  controls power-up sequence, supervises internal supplies, and monitors
  on-board temperature (PWR_FAULT1 at 65 C, shutdown at 90 C)

Power Monitoring
~~~~~~~~~~~~~~~~

The :adi:`ADM1266` handles the following tasks:

- Monitors 12 V input voltage. If it exits the +/- 4% window (11.5 V to
  12.5 V), PWR_FAULT2 is asserted. If it exceeds +/- 8% (11 V to 13 V),
  power to the RF-SOM is switched off.
- Controls power-up voltage sequence. Asserts PG_SOM and monitors PG_ALL.
- Supervises internal voltage supplies during operation. If any supply
  exceeds under/over voltage limits, power is turned off.
- Monitors on-board temperature. PWR_FAULT1 is asserted at 65 C, and power
  is switched off at 90 C.
- Records shutdown events in a non-volatile Blackbox.

Power Fault Signals
~~~~~~~~~~~~~~~~~~~

The two fault signals PWR_FAULT1 and PWR_FAULT2 are open-drain active high
signals with internal 4.7 kohm pull-ups to 1.8 V. These are controlled by
the :adi:`ADM1266` as described above. The purpose of the fault signals is to
indicate that either temperature or input voltage are close to the limit and
a power-down is imminent. Once power is turned off, the state of the fault
signals resets, and the cause of the shutdown can be found only by reading
the ADM1266 Blackbox.

Power Good Signals
~~~~~~~~~~~~~~~~~~

The RF-SOM uses two power good signals (PG_SOM and PG_ALL) to ensure
correct power-up timing. PG_SOM is an output controlled by the ADM1266.
PG_ALL is an input that must be asserted by the carrier. Both are active
high, open-drain signals with on-board pull-ups to 1.8 V.

Reading the ADM1266 Blackbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following tools are needed to read the Blackbox records:

- `ADI Power Studio <https://www.analog.com/en/design-center/adi-power-studio.html>`__
  GUI software
- :adi:`EVAL-ADP-I2C-USB` I2C USB dongle

The I2C dongle connects to the :adi:`ADM1266` dedicated I2C interface
signals (SCL_ADM1266_3V3, SDA_ADM1266_3V3) accessible in connector P2. On
the ADRV2CRR-FMC carrier board, this is available at connector P19.

After connecting the I2C cable, open the ADI Power Studio software, connect
to the dongle, and open the ADRV9009-ZU11EG RF-SOM project. The Blackbox
Records can be accessed from the Monitor menu.

Interfaces
----------

RGMII Ethernet
~~~~~~~~~~~~~~

The RF-SOM has an on-board Marvell 88E1512 10/100/1000 Mbps Ethernet PHY
connected to the GEM3 controller in the PS on the ZU11EG.

USB
~~~

The ADRV9009-ZU11EG features both USB 2.0 and USB 3.0, configurable in
host, device, or OTG mode:

- **USB 2.0:** On-board USB3320 ULPI transceiver connected to USB0
  controller on the ZU11EG.
- **USB 3.0:** I/O path through the PS-GTR transceivers.

Gigabit Serial Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **PS-GTR transceivers:** Support data rates up to 6 Gb/s, providing I/O
  paths for USB 3.0, SGMII Ethernet, and DisplayPort.
- **GTH transceivers:** Run up to 12.5 Gb/s, supporting additional JESD
  lanes, 100 Gb Ethernet, and PCIe.

SD Card
~~~~~~~

The ZU11EG on-chip SD controller is compatible with SD memory card
specification version 3.01, supporting UHS-I speeds and SDXC capacity
format. The RF-SOM includes an on-board uSD card connector, with an option
for a carrier SD card connector via an on-board multiplexer.

- Leave SDIO_SEL floating to use the uSD on the RF-SOM.
- Pull SDIO_SEL to ground to use the SD on the carrier.

Low-Speed Interfaces
~~~~~~~~~~~~~~~~~~~~

The PS Multiplexed I/Os (MIO) provide access to low-speed interfaces inside
the Zynq UltraScale+. The I/O voltage level on all MIO pins is 1.8 V.

- 2x I2C buses (I2C0 also connected to the internal I2C bus with 2.2 kohm
  pull-ups to 1.8 V)
- 1x SPI bus
- 2x UART buses (UART1 is used for debug messages and should always be
  connected)

Programmable Logic GPIOs
~~~~~~~~~~~~~~~~~~~~~~~~

**High-Performance GPIOs:**

PL banks 65, 67, and 68 are fully accessible in connector P2. Bank supply
VCCO must be provided (0.95 V to 1.9 V). A reference voltage must be
applied if the I/O standard requires one. To use the internal VREF voltage,
connect a 500 ohm or 1 kohm resistor from the VREF pin to ground.

**High-Density GPIOs:**

PL bank 89 is partially available in connector P2. Connect a voltage
between 1.14 V and 3.4 V to the bank supply VCCO_89.

**ADC Inputs:**

Some I/Os in bank 89 (AD12P/N to AD15P/N) can be used as ADC inputs for the
ZU11EG on-chip System Monitor. The internal 1.25 V reference is used. The
analog input range is 0 to 1 V for unipolar operation, or +/- 0.5 V
differential at 0.5 V common mode for bipolar operation.

Thermal Considerations
----------------------

The RF-SOM requires active cooling with an AMD-type SP3/TR4/sTRX4 socket
cooler. Without a fan, the RF-SOM will shut down within minutes under normal
operating conditions due to overtemperature protection at 90 C.

The RF-SOM comes with a custom heat spreader plate using a Panasonic
EYG-T7070A10A thermal pad. The heat spreader has two sets of threaded holes.
When a thermal sheet is added between the heat plate and fan, use the set of
holes with the smaller thread depth for mounting.

The ADRV2CRR-FMC kit includes a heatsink with fan and Wurth Elektronik 39410
EMI gasket sheet, which acts as both thermal transfer material between plate
and heatsink, and RF shield/absorber.

Minimal Carrier Setup
----------------------

The following connections to the ADRV9009-ZU11EG RF-SOM are mandatory for a
minimum functional carrier system:

- **Power:** Connect 12 V, 120 W supply. Connect PG_ALL to PG_SOM.
- **Configuration:** Include reset buttons, status LEDs, slide switches for
  boot mode selection, and JTAG connector.
- **SD card:** If needed, place an SD card connector on the carrier and pull
  SDIO_SEL to ground.
- **UART:** Connect UART1 (MIO pins 16 and 17). The I/O voltage is 1.8 V;
  if using a USB-to-UART chip (e.g., FTDI FT232R), a voltage level
  translator from 3.3 V to 1.8 V is required.
- **Ethernet:** For a minimal setup, use RGMII Ethernet (requires only an
  RJ45 connector with magnetics on the carrier).
- **Clock inputs:** Provide BNC connectors for CLKIN0/CLKIN1 and SYNC
  signals for multi-SOM synchronization.
- **ADM1266 I2C:** Place a 1x4 pin, 2.54 mm pitch male header for the
  :adi:`EVAL-ADP-I2C-USB` dongle to access the Blackbox memory.
- **Active cooler:** Required; the heat spreader accommodates AMD-type
  SP3/TR4/sTRX4 socket coolers.

ADRV2CRR-FMC Carrier Board
----------------------------

.. figure:: adrv2crr-fmc_overview.png
   :align: center

   ADRV2CRR-FMC carrier board overview

The ADRV2CRR-FMC carrier board provides common high-speed I/O ports for
evaluating the ADRV9009-ZU11EG RF-SOM. It includes a 12 V, 145 W power
supply that powers the complete prototyping platform.

Carrier Power
~~~~~~~~~~~~~

The ADRV2CRR-FMC has a single 12 V supply input, distributed to the internal
power supplies and interface connectors. The included 145 W power supply
powers the complete prototyping platform (ADRV9009-ZU11EG, ADRV2CRR-FMC, and
optionally AD-FMCOMMS8-EBZ).

Four LEDs show the status of the power supplies: PG_ALL, PG_SOM,
PWR_FAULT1, and PWR_FAULT2.

Boot Mode Configuration
~~~~~~~~~~~~~~~~~~~~~~~

Slide switches S13-S16 select the boot source:

.. list-table::
   :header-rows: 1

   * - Mode Pins [3:0]
     - Boot Source
   * - 0000
     - JTAG
   * - 0010
     - Quad-SPI (32b)
   * - 1110
     - SD1 (3.0)

SD card selection switch **S9** switches between the carrier and SOM SD card
connector.

The JTAG connector **P7** is a 2x14 pin header intended to fit the Xilinx
Platform Cable.

FMC Connector
~~~~~~~~~~~~~

The carrier includes a standard ANSI/VITA 57.1 FMC HPC connector (P1) with:

- 10 serial transceiver lanes, 2x reference clocks
- 34 differential I/O pairs, 2 differential clocks
- JTAG, I2C interfaces

FMC HA and HB positions carry RF reference clock, synchronization, and
ADRV9009 I/O signals for adding extra transceivers via the
:ref:`AD-FMCOMMS8-EBZ <ad-fmcomms8-ebz>`.

All ADRV9009 I/Os and reference clocks are connected to P1 through 0 ohm
jumpers (JP8-JP91). If an FMC mezzanine card conflicts with these signals,
remove the 0 ohm jumpers. For SYNC_OUT2, remove R21.

Additional Connectors
~~~~~~~~~~~~~~~~~~~~~

- **I/O expansion connector (P25):** 2.54 mm pitch 2x10 female connector
  providing 12 single-ended GPIOs (PL bank 65, 1.8 V). If other voltage
  levels are needed, external level translators are required.
- **PMOD connector (P10):** 2x6 pin, 3.3 V, with Fairchild FXLA108
  bidirectional voltage level translator to connect to 1.8 V PL banks. The
  FXLA108 has auto direction sensing and may not work properly with
  bidirectional SPI data lines or open-drain signals.

Carrier I/O Interfaces
~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: adrv2crr-fmc_carrier_io.png
   :align: center

   ADRV2CRR-FMC carrier board I/O interface functionality
