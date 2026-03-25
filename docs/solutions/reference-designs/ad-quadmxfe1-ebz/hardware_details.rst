.. _ad-quadmxfe1-ebz-hardware:

Quad-MxFE Board Hardware Details
=================================

.. _quadmxfe-transmit-path:

Transmit Path
-------------

The 16x transmit front-ends are all on the bottom of the board and contain
identical components. The Tx front-end is comprised of a balun for differential
to single-ended transitioning, a filter, and an :adi:`HMC8411` RF amplifier to
serve as a modest gain stage for any downstream peripherals. The transmit signals
are launched off the board via an MMCX connector.

Within the digital domain, the transmit path receives a data stream from the
JESD204b/c interface and then has the option to traverse through 8x fine or 4x
coarse digital up-converters (DUCs) prior to reaching the DAC for waveform
synthesis. Use of these DUCs is described in
`UG-1578 <https://www.analog.com/media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`__.

.. figure:: quadmxfe_txsignalchainblockdiagram.png
   :align: center

   Transmit signal chain block diagram

.. _quadmxfe-receive-path:

Receive Path
------------

The ADC front-end paths are all on the top of the platform and contain identical
devices for all 16x RF input channels. These channels are comprised of
filtering, two :adi:`HMC8411` gain stages, gain control via a digital step
attenuator (either the :adi:`HMC425A` for Rev. A/B or :adi:`HMC540S` for Rev.
C), and a balun for single-ended to differential transitioning. Filtering can be
swapped with footprint-compatible filters to access different Nyquist zones. The
received signal is launched onto the board via an MMCX connector.

Once digitized via the ADC, the input signal can then be routed through the
digital down converters (DDCs) of the :adi:`AD9081` or :adi:`AD9082` to reduce
the data rate sampled by the ADCs and/or to frequency translate the data using
either the fine or coarse numerically-controlled oscillators (NCOs). Use of these
DDCs is described in
`UG-1578 <https://www.analog.com/media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`__.
Additionally, on-silicon programmable finite-impulse response filters (FIRs) can
be used to achieve broadband equalization across the channels. The data then is
sent over the JESD204b/c digital interface to the baseband processor (BBP).

.. figure:: quadmxfe_rxsignalchainblockdiagram.png
   :align: center

   Receive signal chain block diagram

DSA Gain Control
~~~~~~~~~~~~~~~~

Rev. A/B of the Quad-MxFE Platform uses the :adi:`HMC425A` as the receiver DSA
for gain control. Rev. C uses the :adi:`HMC540S` instead to provide a wider
frequency coverage at the sacrifice of attenuation resolution. The DSA control
is provided from both within ADI :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`
and via MATLAB control. The same DSA attenuation value is set for all ADC
front-ends. Within ADI IIO Oscilloscope, the DSA value can be modified on the
left side of the 'AD9081-3' tab as shown below. If using MATLAB to control the
DSA value, then use the ``rx.ExternalAttenuation`` property.

.. image:: quadmxfe_dsasettinglocation.png
   :align: center

.. _quadmxfe-clocking-architecture:

Clocking Architecture
---------------------

Clock Circuitry Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A 500 MHz reference clock between 0-3 dBm is required by the Quad-MxFE
Evaluation Platform. The reference clock is provided via a vertical SMA female
connector (reference designator J41) in the center of the board. From this
reference clock, the on-board clock distribution network generates the sampling
clocks and SYSREFs for the data converters, as well the FPGA clocks. The full
clock generation tree for Rev. C of the Quad-MxFE Platform is shown below.

.. figure:: quadmxfe_clockingblockdiagram.png
   :align: center

   Clocking block diagram

The quality of the clock directly impacts AC performance of the on-board data
converters. Ensure that the external clock path remains clean of any power supply
noise and select the phase noise and spur characteristics of the clock source to
meet the target application requirements. To verify PLL lock, there is a blue
LED connected to a lock detection output from each :adi:`ADF4371` PLL
synthesizer. A lit LED indicates that the PLL synthesizer associated with that
channel has locked.

.. _quadmxfe-clock-leds:

Clock LEDs
~~~~~~~~~~

.. list-table:: PLL/Synthesizer Lock Detect LEDs
   :header-rows: 1

   * - MxFE#
     - PLL/Synthesizer Ref Des
     - LED Ref Des
   * - 0
     - U77
     - DS2
   * - 1
     - U80
     - DS3
   * - 2
     - U83
     - DS4
   * - 3
     - U86
     - DS5

Direct MxFE Clocking
~~~~~~~~~~~~~~~~~~~~~

The Quad-MxFE Evaluation Platform also has provisions for directly driving the
sampling clock of each MxFE data converter. An SMPM plug is available on each
channel for this purpose, which connects to an AC-coupling capacitor that is not
populated by default. Reference the schematic for more information.

.. list-table:: Direct Clocking Modifications
   :header-rows: 1

   * - MxFE#
     - SMPM Ref Des
     - Modifications
   * - 0
     - J37
     - Depopulate C905, Populate C902
   * - 1
     - J38
     - Depopulate C955, Populate C952
   * - 2
     - J39
     - Depopulate C1005, Populate C1002
   * - 3
     - J40
     - Depopulate C1055, Populate C1052

Using MxFE On-Chip PLL
~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD9081` and :adi:`AD9082` have on-chip PLLs to allow the user to
inject a lower-frequency clock into the IC and then have this on-chip PLL
generate the higher-frequency sample clock needed for the DACs/ADCs. Beginning
with Rev. C of the Quad-MxFE Platform, this capability is exposed with the use
of differential :adi:`HMC7043` outputs serving as this low-frequency clock
source.

.. list-table:: On-Chip MxFE PLL Clocking Modifications (Rev. C Only)
   :header-rows: 1

   * - MxFE#
     - Modifications
   * - 0
     - Depopulate C886/C887, Populate C1118/C1119
   * - 1
     - Depopulate C936/937, Populate C1120/C1267
   * - 2
     - Depopulate C986/C987, Populate C1293/C1312
   * - 3
     - Depopulate C1036/C1037, Populate C1325/C1326

SYSREF Distribution
~~~~~~~~~~~~~~~~~~~

Rev. A/B of the board does not implement length-matched SYSREFs. A goal of the
platform's multi-chip synchronization (MCS) effort was to prove successful MCS
functionality with non length-matched SYSREFs. MCS has been demonstrated on
Rev. A/B boards.

However, Rev. C implements length-matched SYSREFs in an attempt to simplify
software support going forward.

LVPECL to LVDS (One-Shot/N-Shot SYSREF vs. Continuous SYSREF)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Quad-MxFE Platform operates by default in continuous SYSREF mode for
Rev. A/B of the system.

If desired, the :adi:`HMC7043` can be operated in one-shot or N-shot SYSREF mode
if using the :adi:`HMC7043` in LVPECL output. However, the :adi:`AD9081` devices
require a LVDS input for its SYSREF. As such, an on-board LVPECL to LVDS
transition is provided beginning with Rev. C of the platform.

.. figure:: quadmxfe_lvpecltolvds.png
   :align: center

   LVPECL to LVDS transition circuit

FPGA Clocks (Rev B)
~~~~~~~~~~~~~~~~~~~~

For the Quad MxFE Rev B boards, there are a number of reference clocks that are
routed back to the FPGA. In the Rev B design, there are a total of 5 clocks from
the :adi:`HMC7043` that are routed back to FPGA via the FMC+ adapter.

.. figure:: rev_b_hmc7043_overview.png
   :align: center

   Rev B HMC7043 clock overview

Each of the reference clocks out of the :adi:`HMC7043` shares the same
architecture:

.. figure:: rev_b_ref_clk_circuits.png
   :align: center

   Rev B reference clock circuits

This architecture is such that each clock is normally terminated with 100 Ohm
differential. Additional U.FL connectors can be included in the signal path by
placing two DNI'd resistors on the board. An alternative star termination scheme
can be used if the 49.9 Ohm to ground is populated. Each line is also AC coupled.

.. figure:: rev_b_ref_clk_structure.png
   :align: center

   Rev B reference clock to FPGA structure

.. list-table:: Reference Clocks Rev B Board
   :header-rows: 1

   * - Quad #
     - Quad Bank
     - MGTREFCLK0
     - MGTREFCLK1
   * - 121
     - X0Y2
     - HMC7043 CLKOUT2
     - HMC7043 CLKOUT0
   * - 122
     - X0Y3
     - HMC7043 CLKOUT4
     - HMC7043 CLKOUT0
   * - 125
     - X0Y6
     - HMC7043 CLKOUT6
     - HMC7043 CLKOUT0
   * - 126
     - X0Y7
     - HMC7043 CLKOUT2
     - HMC7043 CLKOUT0

FPGA Clocks (Rev C)
~~~~~~~~~~~~~~~~~~~~

On the Rev C boards, the total number of reference clocks was cut down to 3.
These are the FPGA REFCLK, FPGA JTX JESD and FPGA JRX JESD clocks from
CLKOUT0/2/4 respectively. The :adi:`HMC7043` also routes a number of SYSREF
signals and other lower frequency clocks back to the FPGA.

.. figure:: rev_c_hmc7043_overview.png
   :align: center

   Rev C HMC7043 clock overview

Unlike in Rev B of the board, the three reference clocks to the FPGA have
different circuits outside the :adi:`HMC7043`. The difference is the U.FL
connectors which are not present on the FPGA JTX and JRX reference clocks:

.. figure:: rev_c_ref_clk_circuits.png
   :align: center

   Rev C reference clock circuits

.. figure:: rev_c_ref_clk_structure.png
   :align: center

   Rev C reference clock to FPGA structure

Note that the reference clocks for the JRX and JTX are not fed to a Quad PLL,
but rather other clock inputs on the FPGA.

.. list-table:: Reference Clocks Rev C Board
   :header-rows: 1

   * - Quad #
     - Quad Bank
     - MGTREFCLK0
     - MGTREFCLK1
   * - 121
     - X0Y2
     - N/C
     - HMC7043 CLKOUT0
   * - 122
     - X0Y3
     - N/C
     - HMC7043 CLKOUT0
   * - 125
     - X0Y6
     - N/C
     - HMC7043 CLKOUT0
   * - 126
     - X0Y7
     - N/C
     - HMC7043 CLKOUT0

.. _quadmxfe-digital-interface:

Digital Interface
-----------------

The Quad-MxFE Platform supports both JESD204b and JESD204c links. However, only
four of the eight :adi:`AD9081` SERDES lanes are routed on the board to the FMC+
connector, for a total of 16 SERDES lanes used in the system.

JESD204 Link Establishment References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :doc:`HDL Reference Design <reference_hdl>`
- `JESD204B/C High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__

FMC+ Pinout
~~~~~~~~~~~~

The following pinout applies to Rev B Boards:

.. image:: rev_b_pinout.png
   :align: center

The following pinout applies to Rev C Boards:

.. image:: quadmxfe/revc_pinout.png
   :align: center

MxFE Software/Hardware Pinouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: quadmxfe/mmcx_decode_table.png
   :align: center

.. _quadmxfe-control-interfaces:

Control Interfaces
------------------

SPI (MxFE, ADF4371, HMC7043)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD9081` SPI interface is a 4-wire SPI by default, however the part can
be run in a 3-wire interface if desired. There is a separate SPI bus for each of
the :adi:`AD9081` to allow for parallel operation if desired, but the FPGA
currently supports sequential operation. The :adi:`HMC7043` and :adi:`ADF4371`
are both wired for 3-wire SPI only. The :adi:`ADF4371` share a common SPI bus
with 4 CS lines. The :adi:`HMC7043` has a separate dedicated SPI bus.

I2C (EEPROM, Voltage/Current Monitoring)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EEPROM on the Quad MxFE board is a M24C02-RDW6TP which is a 2Kbit (256 byte)
EEPROM with an I2C interface speed up to 400 kHz. In this design, the I2C SCL is
run at 400 kHz and the supply voltage is 3.3V from the VCU118 via the FMC+
connector. The address for this part is 101000b or 80 in decimal. This EEPROM is
also queried by the VCU118 upon startup to determine the required VADJ level for
the FMC+ VADJ. In the case the EEPROM is not programmed, the VADJ is
automatically set to 1.8V.

On Rev. C boards, the :adi:`ADM1177` is used as a power monitor to measure the
total current draw and voltage of the board.

.. _quadmxfe-power-supplies:

Power Supplies
--------------

The Quad-MxFE Evaluation Board develops all RF and digital rails from +12V
through the 6-terminal Power Connector. The kit also includes a compatible AC
adaptor. The Power Connector is a Molex 39301060 dual-row, right-angle header. A 5A
reverse polarity protection Schottky diode is connected between ground and +12V.

.. image:: labeled_conn.png
   :align: center

.. list-table:: Power Connector Pinout
   :header-rows: 1

   * - Pin Number
     - Function
   * - 1
     - +12V In
   * - 2
     - Ground
   * - 3
     - Ground
   * - 4
     - +12V In
   * - 5
     - +12V In
   * - 6
     - Ground

The on-board DC regulation scheme uses separate LDOs to keep analog and
mixed-signal voltage domains noise-isolated. They are broadly separated into:

- PLL voltages
- RF front-end voltage
- MxFE voltages
- Clock buffer voltage

Since some of this circuitry is repeated, many of the voltage domains are further
separated based on their corresponding MxFE channel.

Power Distribution
~~~~~~~~~~~~~~~~~~

A single 12V input is applied to the P1 connector, with a current rating greater
than 8.8A. All voltages needed for the board are then derived from this source.
Two :adi:`LTM4633` with downstream LDOs help to provide the 1V rails for each
MxFE. An :adi:`LTM8053` helps to derive the 2V rails needed for each MxFE. The
remaining 5V and 3.3V rails are ultimately derived from either an :adi:`LTM8053`
or an :adi:`LTM8063`, again with the aid of downstream LDOs.

A ``1.8V_VADJ`` signal is also received by the Quad-MxFE Platform from the FPGA
evaluation board and is used to power level translators and the ``DVDD1P8`` net
on each MxFE to enable SPI communication.

Additionally, a 3.3V Power Good ``PG_C2M`` signal is also received from the FPGA
evaluation board and is used to light the DS1 green LED and power the Quad-MxFE
Platform EEPROM.

.. figure:: quadmxfe_powerblockdiagram.png
   :align: center

   Power block diagram

Beginning with Rev. B of the Quad-MxFE Platform, a dedicated LTM8063 (U121) was
added to provide the 3.3V necessary to independently power the HMC7043 clock
buffer IC.

.. _quadmxfe-power-leds:

Power LEDs
~~~~~~~~~~

.. list-table:: Power LED Status Indicators
   :header-rows: 1

   * - LED Ref Des
     - Function
   * - DS1
     - ``1.8V_VADJ`` Good From FPGA Board
   * - DS6
     - LTM8053 ``6V_OUT`` 6V Output Good (RF Amps/PLL Synthesizers)
   * - DS7
     - LTM8053 ``6V_OUT`` 6V Output Good (RF Amps/PLL Synthesizers)
   * - DS8
     - LTM4633 ``PGOOD3`` 1.3V Output Good (MxFE0/1)
   * - DS9
     - LTM4633 ``PGOOD12`` 1V AND 1.3V Output Good (MxFE0/1)
   * - DS10
     - LTM4633 ``PGOOD3`` 1.3V Output Good (MxFE2/3)
   * - DS11
     - LTM4633 ``PGOOD12`` 1V AND 1.3V Output Good (MxFE2/3)

Current/Voltage Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~

Beginning with Rev. C of the Quad-MxFE Platform, current and voltage monitoring
is available via an :adi:`ADM1177` I2C interface. Additionally, a 10A current
limit threshold is set for the board and a voltage input threshold of greater
than 10.4V is enabled.

LDO Bypass
~~~~~~~~~~

Beginning with Rev. B of the Quad-MxFE Platform, the user is able to rotate
ferrites prior to the LDOs on the board to investigate system performance in
which only the silent switcher uModules are powering the downstream devices.

.. figure:: quadmxfe_ferriterotateschematic.png
   :align: center

   Ferrite rotate schematic for LDO bypass

As an example for one LDO, notice that E14 and E15 share a common pad. E14 is
normally populated, whereas E15 is set as 'Do Not Install' (DNI) by default.
The user can rotate the normally populated E14 to a position instead using E15,
then modify the upstream uModule voltage to output 1V instead of 1.3V.

Power Switch
~~~~~~~~~~~~

Beginning with Rev. C of the Quad-MxFE Platform, a 12V power switch was
installed to allow the platform to be plugged in to a wall or bench supply, but
still switch power to the system.

.. _quadmxfe-thermal-considerations:

Thermal Considerations
----------------------

Use of the Rev. A and B Quad-MxFE Platform requires an external fan blowing
across the long direction of the platform during operation. This allows the board
to maintain a thermal equilibrium and improves the JESD204b/c link signal
integrity.

5V On-MxFE Fans
~~~~~~~~~~~~~~~~

Beginning with Rev. C of the Quad-MxFE Platform, 5V 2-pin headers are placed
near each AD9081 to power a heat sink and fan assembly which is mounted directly
to each MxFE. This helps to prevent thermal runaway and provides higher system
stability.

To install these fan/heat sink assemblies, follow these instructions **prior to
the board's first-time use**:

#. Remove the two screws (#5) from the shipped assembly
#. Place the blue clip (#3) around the bottom of the MxFE
#. Peel the self stick/thermal compound adhesive/sticker (#2) off the bottom of
   the heat sink (#1)
#. Place the heat sink (#1) on the MxFE
#. Slide the clip (#4) over the heat sink (#1) until the heat sink (#1) latches
   onto the blue clips
#. Attach the fan (#5) with the two screws (#5)
#. Plug in the 2-pin power wires from the fan (#5) into the nearest 2-pin
   header on the Quad-MxFE Platform

.. image:: quadmxfe/qmxfe_fan_heat_sink_installation.jpg
   :align: center

.. image:: adquadmxfe1ebztop-web.gif
   :align: center

.. _quadmxfe-schematic:

Schematic
---------

Schematic/BOM Variants
~~~~~~~~~~~~~~~~~~~~~~

There are presently three Quad-MxFE Platform variants which are populated with
either different filters to access alternative Nyquist zones and/or different
MxFE devices to extend the IBW of the system.

The schematics are hierarchical schematics. After downloading the schematic, you
can go to page 2 and left click on any high-level block and then click 'Descend'
to more easily navigate the system's schematic.

**ADQUADMXFE1EBZ**

- Populated with :adi:`AD9081`
- 16x Rx Channels
- 16x Tx Channels
- Rx Analog Input Frequency Range: 2.7-3.7 GHz
- Tx Analog Output Frequency Range: Up to 4 GHz

**ADQUADMXFE2EBZ**

- Populated with :adi:`AD9081`
- 16x Rx Channels
- 16x Tx Channels
- Rx Analog Input Frequency Range: Up to ~1.8 GHz
- Tx Analog Output Frequency Range: Up to 5.8 GHz

Below is the ADQUADMXFE2EBZ variant:

.. image:: quadmxfe/20210426_152612_new1.jpg
   :align: center

.. image:: quadmxfe/20210426_152623_new1.jpg
   :align: center

**ADQUADMXFE3EBZ**

- Populated with :adi:`AD9082`
- 8x Rx Channels
- 16x Tx Channels
- Rx Analog Input Frequency Range: ~3.1 to 5.8 GHz
- Tx Analog Output Frequency Range: Up to 5.8 GHz

Below is the ADQUADMXFE3EBZ variant:

.. image:: quadmxfe/20210426_151511_new1.jpg
   :align: center

.. image:: quadmxfe/20210426_151613_new1.jpg
   :align: center

Earlier Systems
~~~~~~~~~~~~~~~

Only limited quantities of Rev. A and Rev. B systems were delivered. Rev. C
systems are the broad-market released systems.

Layout
------

Layout board files are provided to the customer after purchase of the Quad-MxFE
Platform. These files have been developed using Cadence Allegro tools and are in
the format of a .brd file. Detailed electromagnetic simulations were performed on
the layout to ensure optimum RF performance in such a dense channel footprint.

A few highlights of the board layout include:

- 600 mils Channel-to-Channel Spacing
- 300 mils RF Connector Spacing
- Board Footprint: 10.2" x 4.5"
- >2,500 Components

Description of FPGA Builds
~~~~~~~~~~~~~~~~~~~~~~~~~~

A full listing of the supported modes, device trees, and build configurations is
available on the :doc:`HDL Reference Design <reference_hdl>` page. The build
files should be downloaded from the :ref:`Downloads <quadmxfe-downloads>` section
and can be programmed using the Xilinx Software Command Line Tool (XSCT) or
MATLAB ``LoadVcu118Code`` function.
