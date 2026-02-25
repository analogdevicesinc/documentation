.. _adrv2crr-fmc:

ADRV2CRR-FMC Carrier Board
===========================

Overview
--------

.. image:: adrv2crr-fmc_desc.png
   :align: center
   :width: 600

The :adi:`ADRV2CRR-FMC` is the carrier board for evaluating the
:adi:`ADRV9009-ZU11EG` RF System-on-Module (RF-SOM). It provides common
high-speed I/O ports to give flexibility in connectivity options. The
carrier board package includes a power supply, a heatsink for the RF-SOM
heat spreader plate, and the necessary cables and adapters to get up and
running.

For information on getting started, system software, and quick start guides,
see the
:doc:`ADRV9009-ZU11EG user guide </solutions/reference-designs/adrv9009zu11eg/index>`.

The :adi:`ADRV2CRR-FMC` includes the following key features:

- Single 12 V input powering the complete prototyping platform
- ANSI/VITA 57.1 FMC HPC connector with 10 JESD204B transceiver lanes
- USB 3.0, USB 2.0, Gigabit Ethernet, DisplayPort, and PCIe interfaces
- QSFP+ and SFP+ cages for high-speed optical connectivity
- SD card slot, JTAG connector, and UART for debug
- PMOD and IO expansion connectors for prototyping

Power Input
-----------

The :adi:`ADRV2CRR-FMC` has a single 12 V supply input, distributed to
internal power supplies and interface connectors. Included in the package is a
12 V, 145 W power supply, which powers the complete prototyping platform built
out of the :adi:`ADRV9009-ZU11EG`, :adi:`ADRV2CRR-FMC`, and
:adi:`AD-FMCOMMS8-EBZ`.

There are four LEDs that show the status of the power supplies:

- **PG_ALL** --- Power good for all supplies
- **PG_SOM** --- Power good for the SOM
- **PWR_FAULT1** --- Power fault indicator 1
- **PWR_FAULT2** --- Power fault indicator 2

A detailed description of these signals is available in the
:doc:`ADRV9009-ZU11EG hardware overview </solutions/reference-designs/adrv9009zu11eg/index>`.

ZU11EG UltraScale+ Configuration
---------------------------------

Boot Mode Pins
~~~~~~~~~~~~~~

Slide switches S13--S16 select the boot source of the Xilinx ZU11EG
UltraScale+ MPSoC.

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

.. image:: btn_boot.png
   :align: center
   :width: 400

SD Card
~~~~~~~

SD card selection switch **S9** selects between the carrier board and the SOM
SD card connector.

.. image:: sd_card_select.png
   :align: center
   :width: 400

JTAG
~~~~

The JTAG connector **P7** is a 2x14 pin header intended to fit the Xilinx
Platform Cable.

RF-SOM Interface Connectors
----------------------------

The interface to the :adi:`ADRV9009-ZU11EG` consists of two SAMTEC SEARAY
400-pin connectors (**P12** and **P14**). For a detailed description of the
signal interface, visit the
:doc:`ADRV9009-ZU11EG user guide </solutions/reference-designs/adrv9009zu11eg/index>`.

FMC Connector
-------------

The :adi:`ADRV2CRR-FMC` includes a standard ANSI/VITA 57.1 FMC high-pin count
(HPC) connector **P1**, which is partially populated. The following signals are
present:

- 10 serial transceiver lanes (FMC_HPC_DPx), 2x serial transceiver reference
  clocks (FMC_HPC_GBTCLKx)
- 34 differential I/O pairs (FMC_HPC_LAx), 2 differential clocks
  (FMC_HPC_CLK0/1_M2C)
- JTAG, I2C interfaces

FMC HA and HB differential signals are not populated with user-defined digital
I/Os as specified in the FMC HPC standard. Instead, RF reference clock signals,
synchronization signals, and :adi:`ADRV9009` I/Os are connected to these
positions. This enhances the capability of the P1 connector by providing:

- The ability to add extra ADRV9009 transceivers to the system and synchronize
  them with the RF-SOM. This is accomplished with the
  :ref:`AD-FMCOMMS8-EBZ <ad-fmcomms8-ebz>`.
- The ability to design custom RF boards that make use of the analog and digital
  ADRV9009 I/Os.

All previously mentioned ADRV9009 I/Os and reference clocks are connected to
P1 through 0 Ohm jumpers (JP8--JP91). If an FMC mezzanine card is connected
that conflicts with these signals, remove the 0 Ohm jumpers. For the
synchronization signal SYNC_OUT2, remove R21.

IO Expansion Connector
-----------------------

IO expansion connector **P25** is a 2.54 mm pitch 2x10 female connector that
gives access to 12 single-ended (6 differential pairs) general-purpose I/Os.
These are connected to high-performance ZU11EG PL bank 65 and are referenced to
1.8 V. If other voltage levels are needed, external voltage level translators
must be used.

PMOD Connector
--------------

PMOD connector **P10** is a 2x6 pin, low-speed host interface, referenced to
3.3 V. A Fairchild FXLA108 bidirectional voltage level translator is used on
the PMOD signals to connect these to the 1.8 V referenced ZU11EG PL banks. The
FXLA108 has auto direction sensing and may not work properly with some signals,
such as bidirectional SPI data lines or open-drain signals.

Additional I/O
--------------

The carrier board also provides the following high-speed and general-purpose
interfaces:

- **USB 3.0** --- USB Type-C connector for SuperSpeed data transfer
- **USB 2.0** --- Micro-USB connector for UART console access
- **Gigabit Ethernet** --- Two RJ-45 connectors (M1: SGMII, M2: RGMII)
- **DisplayPort** --- Full-size DisplayPort output (P2)
- **PCIe** --- x4 PCIe Gen2 edge connector (P17)
- **QSFP+** --- Cage for 4-lane transceiver module (P3)
- **SFP+** --- Cage for single-lane transceiver module (P4)
- **Audio** --- 3.5 mm line-in (P5) and line-out (P6) jacks

Interfaces
----------

The following table outlines levels of functionality provided in software for
the I/O interfaces on the carrier board.

.. image:: carrier_io.png
   :align: center
   :width: 700

Switches and Jumpers
--------------------

USB PHY configuration (the only supported configuration):

.. image:: jmp_usb.png
   :align: center
   :width: 400

Power good jumpers (P18, P20) --- the only working configuration:

.. image:: jmp_pgood.png
   :align: center
   :width: 400

HDL Reference Design
--------------------

The HDL reference design for the ADRV9009-ZU11EG system is available at:

- :git-hdl:`projects/adrv9009zu11eg`

Software Support
----------------

Software support for the ADRV9009-ZU11EG system is described in the
:doc:`ADRV9009-ZU11EG user guide </solutions/reference-designs/adrv9009zu11eg/index>`.
The following software resources are available:

- :git-linux:`ADRV9009 Linux Driver <drivers/iio/adc/adrv9009.c>`
- `ADRV9009-ZU11EG HDL Project Documentation <https://analogdevicesinc.github.io/hdl/projects/adrv9009zu11eg/index.html>`__
- `IIO Oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope>`__

More Information
----------------

- :doc:`ADRV9009-ZU11EG User Guide </solutions/reference-designs/adrv9009zu11eg/index>`
- :ref:`AD-FMCOMMS8-EBZ User Guide <ad-fmcomms8-ebz>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- :adi:`ADRV2CRR-FMC Product Page <ADRV2CRR-FMC>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.

.. esd-warning::
