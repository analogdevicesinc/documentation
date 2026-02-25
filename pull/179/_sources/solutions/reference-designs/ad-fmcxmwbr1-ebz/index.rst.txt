.. _ad-fmcxmwbr1-ebz:

AD-FMCXMWBR1-EBZ User Guide
============================

Introduction
------------

The :adi:`AD-FMCXMWBR1-EBZ` is an FMC-compatible level translator and power
supply board that bridges FPGA/controller devices with
`X-Microwave <https://www.xmicrowave.com/>`__ blocks. It provides SPI, I2C,
and GPIO interfaces with bidirectional voltage level translation, along with
multiple power supply outputs for the X-Microwave ecosystem.

The board draws power from the FMC connector but has the option to add an
external supply for applications that require higher load currents.

Features
~~~~~~~~

- FMC HPC form factor with level translation
- Multiple supply voltage outputs with high current capability
- 2x SPI buses, 2x I2C buses, 8 GPIO channels
- Compatible with X-Microwave controller and Raspberry Pi
- Powered from FMC connector with optional external 12 V supply

Applications
~~~~~~~~~~~~

- RF and microwave prototyping with X-Microwave blocks
- Software-defined radio (SDR)
- Radar systems
- Point-to-point communications
- MIMO radio systems
- Automated test equipment (ATE)

.. image:: ad-fmcxmwbr1-ebz_kit_set.jpg
   :align: center
   :width: 600

Kit Contents
------------

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Item
     - Part Number
     - Description
   * - FMC Bridge Board
     - AD-FMCBRIDGE1A (BR-066232 Rev B)
     - FMC card with level translators and power supplies
   * - Protoplate Board
     - AD-FMCBRIDGE1B (BR-066233)
     - Prototyping board with signal access for X-Microwave blocks
   * - Ribbon Cable
     -
     - For signal rails between bridge and protoplate
   * - Custom Cable
     -
     - For power rails between bridge and protoplate

Hardware Overview
-----------------

Power Supply
~~~~~~~~~~~~

The board uses an :adi:`LTC4418` dual-channel prioritized powerpath controller
to select between two input sources, with priority given to the external
supply.

.. figure:: input_power_priority.png
   :align: center

   Input power path selection

**Input Sources:**

- **External 12 V supply** (P2): Molex 0039301060, 12 V at 5 A minimum
- **FMC 12P0V pin**: Maximum 1 A from FMC connector

.. list-table:: Input Supply Validity Thresholds
   :header-rows: 1
   :widths: 30 35 35

   * - Parameter
     - External Supply
     - FMC 12V0
   * - UV Threshold
     - 10 V
     - 10 V
   * - OV Threshold
     - 13 V
     - 13 V
   * - Hysteresis
     - 250 mV
     - 250 mV
   * - Inrush Current Limit
     - 4 A
     - 4 A
   * - Validation Delay
     - 16 ms
     - 16 ms

**Output Power Rails (directly from FMC):**

- +12 V at 1 A
- +3.3 V at 3 A
- +VADJ (0 to 3.3 V) at 4 A

**Output Power Rails (generated from external supply):**

.. figure:: power_map.png
   :align: center

   Power supply map (Rev B)

- +6 V at 1 A (LTM8078 step-down)
- +4 V at 1 A (LTM8078 step-down)
- +18 V at 50 mA (LTC3265 charge pump + ADP7142 LDO)
- +3.3 V at 1 A (LTC3261 step-down)
- +1.8 V at 30 mA (ADP7118 adjustable LDO)
- 2x potentiometer adjustable 1.5 to 12 V at 700 mA each (LTM8049 SEPIC)
- 1x potentiometer adjustable 0 to -6 V at 600 mA (LTM8045 inverting)

Level Translation
~~~~~~~~~~~~~~~~~

The board provides bidirectional voltage level translation between the
FPGA-side I/O voltages and the X-Microwave block voltages.

.. list-table::
   :header-rows: 1
   :widths: 20 30 30 20

   * - Protocol
     - IC
     - Configuration
     - Supply Range
   * - SPI CLK, COPI
     - 74AVC4T774GUX
     - 4 inputs, per-pin direction control
     - 0.8 to 3.6 V
   * - SPI CIPO
     - 74LVC1T45GS
     - 1 input, 1 direction pin
     - 1.2 to 3.6 V
   * - SPI CS
     - 74AVCH8T245PW
     - 8 inputs, common direction
     - 0.8 to 3.6 V
   * - I2C
     - NTS0302JKZ
     - 2 inputs
     - 0.95 to 3.6 V
   * - GPIO
     - 74AVC4T774GUX
     - 4 inputs, per-pin direction control
     - 0.8 to 3.6 V

Digital Communication Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **SPI:** 2 channels with CLK, COPI, CIPO, and CS0-CS7 signals
- **I2C:** 2 channels with SDA and SCL signals
- **GPIO:** 8 pins (GPIO0-GPIO7), configurable direction (default: 6 output,
  2 input)

Connectors
~~~~~~~~~~

**P1 -- FMC Connector**

Standard ANSI/VITA 57.1 FMC HPC connector carrying SPI buses, I2C buses,
GPIO signals, and power.

.. figure:: fmc_pinout.png
   :align: center

   FMC connector (P1) pinout

**P10 -- Raspberry Pi / X-Microwave Controller Connector**

40-pin connector compatible with Raspberry Pi standard pinout. Connects to
an X-Microwave controller or Raspberry Pi via ribbon cable.

.. figure:: rpi_conn_pinout.png
   :align: center

   Raspberry Pi connector (P10) pinout

.. note::

   The FMC (P1) and Raspberry Pi (P10) interfaces cannot be used
   simultaneously.

**P2 -- External Power Input**

Molex 0039301060 rectangular 6-position connector for 12 V external supply.

.. figure:: p2_pinout.png
   :align: center

   External power input connector (P2) pinout

**P9 -- Signal Output Header**

Carries all digital communication signals to the protoplate interface board.

.. figure:: p9_pinout.png
   :align: center

   Signal output header (P9) pinout

**P11 -- Output Power Connector**

Provides access to all power rails generated on the bridge board.

.. figure:: p11_pinout.png
   :align: center

   Output power connector (P11) pinout

Quick Start
-----------

The AD-FMCXMWBR1-EBZ is a dual-board kit. The FMC Bridge Board (AD-FMCBRIDGE1A)
plugs into the FMC connector on the carrier, while the Protoplate Interface Board
(AD-FMCBRIDGE1B) mounts on a 32x32 X-Microwave prototype plate and connects to
the bridge board via the included ribbon and power cables.

The board supports three setup modes:

FMC Carrier Setup (ADRV9009-ZU11EG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Set up the :ref:`ADRV9009-ZU11EG <adrv9009zu11eg>` base system on the
   ADRV2CRR-FMC carrier following its quick start guide.
#. Connect Ethernet from the ADRV2CRR-FMC carrier to your network.
#. Attach a DisplayPort monitor to the carrier board.
#. Connect a USB OTG adapter with a USB hub for keyboard and peripherals.
#. Insert the AD-FMCXMWBR1-EBZ into the FMC HPC connector.
#. Use the provided ribbon and power cables to connect the bridge board to the
   protoplate and your X-Microwave setup.
#. Power on the carrier board.

X-Microwave Controller Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The P10 connector provides a 40-pin header compatible with both the X-Microwave
controller and a Raspberry Pi. Connect the X-Microwave controller or Raspberry
Pi to P10 using a 40-pin ribbon cable. The provided cables then link the
protoplate to your X-Microwave prototype plate.

.. note::

   The FMC (P1) and Raspberry Pi/X-MW Controller (P10) interfaces cannot be
   used simultaneously.

.. note::

   The adjustable power supplies (potentiometer-controlled) default to their
   maximum output values at power-up.

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
   * - ADRV2CRR-FMC (with :ref:`ADRV9009-ZU11EG <adrv9009zu11eg>` RF-SOM)
     - Yes

HDL Reference Design
--------------------

The AD-FMCXMWBR1-EBZ HDL design is a variant of the
:ref:`ADRV9009-ZU11EG <adrv9009zu11eg>` reference design. It extends the base
design with AXI-based SPI and I2C cores along with GPIO control for the
X-Microwave bridge module. The FMC HPC connector on the ADRV2CRR-FMC carrier
is used to interface with the bridge board.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/adrv9009zu11eg/adrv2crr_fmcxmwbr1`

Software Support
----------------

The Linux reference design exposes the following interfaces on the
ADRV9009-ZU11EG + ADRV2CRR-FMC platform:

- **2x AXI SPI** cores (accessible as ``/dev/spidevX.Y``), supporting devices
  such as the :adi:`AD5721R` DAC
- **2x AXI I2C** cores, supporting devices such as the :adi:`AD7291` ADC
- **AXI GPIO** controller, providing access to 8 GPIO lines via
  ``/sys/class/gpio``

IIO devices enumerated on a typical boot include SPI-connected DACs and
I2C-connected ADCs, accessible through the standard Linux IIO subsystem.

More Information
----------------

- :ref:`ADRV9009-ZU11EG User Guide <adrv9009zu11eg>`
- :ref:`ADRV2CRR-FMC Carrier User Guide <adrv2crr-fmc>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.

.. esd-warning::
