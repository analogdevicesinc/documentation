.. _cn0506:

CN0506 User Guide
==================

Introduction
------------

The :adi:`CN0506` Dual PHY Ethernet evaluation board features two :adi:`ADIN1300`
robust, industrial, low power 10/100/1000Base-T Ethernet PHY devices. The
board is designed to interface the MAC and PHY through RGMII, MII, or RMII
interfaces.

The circuit consists of two individual, independent 10/100/1000 Mbps PHYs,
each with an energy efficient Ethernet (EEE) physical layer device (PHY) core
with all associated common analog circuitry, input and output clock buffering,
management interface, subsystem registers, MAC interface, and control logic.

On the RJ45 LAN socket, the status and speed LEDs are controlled from the FPGA.
Each LED is bi-color (green or yellow). The right LED indicates activity/status,
and the left LED indicates speed: off = 10 Mbit, yellow = 100 Mbit, green =
1 Gbit.

Supported Devices
-----------------

- :adi:`ADIN1300`

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Board
     - Interface(s)
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - MII, RMII, RGMII
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - MII, RMII, RGMII
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - MII, RMII, RGMII

Evaluation Board Hardware
-------------------------

Connectors
~~~~~~~~~~

.. figure:: cn0506_connectors.png
   :align: center

   EVAL-CN0506-FMCZ board connector layout

FMC Connector
^^^^^^^^^^^^^

The FMC connector connects to the LPC connector of the carrier board.

RJ45 Connectors
^^^^^^^^^^^^^^^^

The RJ45 connectors M1 (Channel A) and M2 (Channel B) have built-in magnetics
that help reduce the size of the board. Each connector is dedicated to a PHY
interface (:adi:`ADIN1300`), allowing each channel to operate independently.

Configuration Resistors
~~~~~~~~~~~~~~~~~~~~~~~

MAC Interface Selection
^^^^^^^^^^^^^^^^^^^^^^^

The MAC interface selection pins are shared with the RX_CTL/RX_DV/CRS_DV and
RXC/RX_CLK pins, which have weak internal pull-down resistors and are
configured in RGMII mode with 2 ns delay by default. The MAC interface can be
selected via software, or hardware-configured at power-up using the resistors
listed below.

.. list-table:: MAC Interface Selection
   :header-rows: 1

   * - MAC Interface
     - MACIF_SEL1 (Phy A / Phy B)
     - MACIF_SEL0 (Phy A / Phy B)
   * - RGMII (RXC/TXC 2 ns delay)
     - R12 / R78
     - R9 / R75
   * - RGMII (RXC/TXC 2 ns delay)
     - R11 / R77
     - R9 / R75
   * - MII
     - R17 / R78
     - R8 / R74
   * - RMII
     - R11 / R77
     - R8 / R74

Configuration Modes
^^^^^^^^^^^^^^^^^^^

The configuration modes set Auto MDIX and PHY speed configurations for both
PHY channels A and B.

.. list-table:: Configuration Mode Resistor Values
   :header-rows: 1

   * - Mode
     - R_LO
     - R_HI
   * - MODE_1
     - 10k
     - Open
   * - MODE_2
     - 10k
     - 56k
   * - MODE_3
     - 56k
     - 10k
   * - MODE_4
     - Open
     - 10k

The board has both channels configured for 10 Half Duplex/Full Duplex,
100 Half Duplex/Full Duplex, and 1000 Full Duplex slave mode upon power-up.

.. list-table:: Auto MDIX Configuration
   :header-rows: 1

   * - Configuration
     - MDIX_MODE
   * - Manual MDI
     - MODE_1
   * - Manual MDIX
     - MODE_2
   * - Auto MDIX - Prefer MDIX
     - MODE_3
   * - Auto MDIX - Prefer MDI
     - MODE_4

LED Indicators
~~~~~~~~~~~~~~

The LEDs indicate when a link is established and blink when there is activity.
The LED on PHY Channel A is labeled DS4 and the LED on PHY Channel B is labeled
DS2.

.. figure:: cn0506-silkscreen.jpg
   :align: center

   CN0506 board silkscreen showing LED locations

Quick Start Guide (ZC706)
--------------------------

Prerequisites
~~~~~~~~~~~~~

Required Hardware
^^^^^^^^^^^^^^^^^

- EVAL-CN0506-FMCZ board
- Xilinx :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
  evaluation board (Rev 1.0 or later)
- Power cord and adapter compatible with ZC706
- SD card (16 GB or larger)
- Mini USB cable
- Ethernet cable

Required Software
^^^^^^^^^^^^^^^^^

- Linux or Windows OS on a host PC
- UART terminal application (e.g., TeraTerm, PuTTY)

Hardware Setup
~~~~~~~~~~~~~~

.. figure:: cn0506_zc706_setup.jpg
   :align: center

   CN0506 evaluation setup with ZC706

1. Connect the EVAL-CN0506-FMCZ to the low pin count (LPC) FMC connector on
   the ZC706 evaluation board.

   .. figure:: cn0506_fmc_connection.jpg
      :align: center

      FMC connector attachment

2. Connect the ZC706 USB-to-UART bridge (U52, J21) to the host PC using a
   mini USB cable.

   .. figure:: cn0506_uart_connection.jpg
      :align: center

      UART connection via mini USB

3. Connect an Ethernet cable to the CN0506 M1 or M2 Ethernet port.

   .. figure:: cn0506_ethernet_connection.jpg
      :align: center

      Ethernet cable connection

4. Plug the power cord into the 12 V power jack (2x6 connector J22). Do not
   switch on the Power On/Off Switch (SW1) until the SD card is inserted.
   Ensure that switch and jumper settings are in default mode. Refer to the
   `ZC706 User Guide <https://docs.amd.com/v/u/en-US/ug954-zc706-eval-board-xc7z045-ap-soc>`__
   for default jumper settings.

   .. figure:: cn0506_power_connection.jpg
      :align: center

      Power supply connection

SD Card Setup
~~~~~~~~~~~~~

1. Download the latest `ADI Kuiper Linux <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`__
   image and flash it to the SD card.

2. In the BOOT partition of the flashed image, copy the appropriate kernel
   file (``uImage`` from the ``zynq-common`` folder) to the root of the BOOT
   partition.

3. Copy the boot files from the desired interface configuration folder
   (e.g., ``zynq-zed-adv7511-cn0506-mii`` or ``zynq-zed-adv7511-cn0506-rgmii``)
   to the root of the BOOT partition.

4. Safely eject the SD card and insert it into the ZC706 SD Card Interface
   Connector (J30).

   .. figure:: cn0506_sdcard_slot.jpg
      :align: center

      SD card slot on ZC706

5. Power on the ZC706 by toggling SW1. The board should boot from the SD card.

6. Open a UART terminal (115200 baud, 8N1) on the host PC to monitor the
   boot process and interact with the Linux console.

HDL Reference Design
--------------------

Build Parameters
~~~~~~~~~~~~~~~~

The default MAC-to-PHY interface is RGMII. To build a specific interface
configuration, set the ``INTF_CFG`` environment variable:

.. code-block:: bash

   make INTF_CFG=MII
   make INTF_CFG=RMII
   make INTF_CFG=RGMII

Management Interface
~~~~~~~~~~~~~~~~~~~~

A synchronous serial data interface similar to I2C is made from MDC and MDIO
(bidirectional) signals.

MII Interface
~~~~~~~~~~~~~

The MII interface supports data rates of 100 Mbps and 10 Mbps.

.. figure:: cn0506_mii.png
   :align: center

   CN0506 MII interface block diagram

The PHY sends a free-running clock as the receive clock (RX_CLK). The transmit
clock is also a free-running clock generated by the PHY. Based on the link
speed, the frequency of the Rx/Tx clock is 25 MHz for 100 Mbit/s and 2.5 MHz
for 10 Mbit/s.

Typically the PS/HPS MAC only exposes a GMII interface, but the required MII
signals can be obtained since MII is a subset of GMII. The GMII interface
contains extra signals: GTXCLK (125 MHz clock for gigabit TX) and an additional
4 MSBs for both RXD and TXD data buses.

The reset signal for both ADIN1300 devices comes from the PS/HPS. An optional
``link_st`` signal indicates if a valid link is established, connected to
GPIO[35] for PHY A and GPIO[34] for PHY B. The speed LEDs are hard-coded to
yellow (100 Mbit).

MII Supported Carriers
^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Board
     - FMC Slot
     - Connections
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - FMC HPC1
     - PS8: PHY_A-Ethernet0, PHY_B-Ethernet1
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - FMC LPC
     - PS7: PHY_A-Ethernet0, PHY_B-Ethernet1
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC
     - PS7: PHY_A-Ethernet0, PHY_B-Ethernet1

RMII Interface
~~~~~~~~~~~~~~

The RMII interface supports data rates of 100 Mbps and 10 Mbps with a reduced
number of signals compared to MII.

.. figure:: cn0506_rmii.png
   :align: center

   CN0506 RMII interface block diagram

The reference clock operates at 50 MHz in both 100 Mbit/s and 10 Mbit/s mode.
Software is used to configure the programmable clock oscillators on the board to
50 MHz via I2C. In this design both the MAC (MII to RMII converter) and PHY
work on the same 50 MHz clock.

Software should not be used to set the ADIN1300 in RMII mode; instead, this is
done by setting MAC_IF_SEL1 (CRS_DV) and MAC_IF_SEL0 both to high using
internal pull-up resistors in the FPGA.

Because the REF_CLOCK is configured by software independently for each PHY, an
independent reset signal is required for the initialization of each PHY. The
main reset signal comes from the PS/HPS reset generator. Software can
independently reset PHY A by setting GPIO[37] high and PHY B by setting
GPIO[36] high (controlled by the PS/HPS). The speed LEDs are hard-coded to
yellow (100 Mbit).

RMII Supported Carriers
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Board
     - FMC Slot
     - Connections
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - FMC HPC1
     - PS8: PHY_A-Ethernet0, PHY_B-Ethernet1
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - FMC LPC
     - PS7: PHY_A-Ethernet0, PHY_B-Ethernet1
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC
     - PS7: PHY_A-Ethernet0, PHY_B-Ethernet1

RGMII Interface
~~~~~~~~~~~~~~~

The RGMII interface supports data rates of 1 Gbps, 100 Mbps, and 10 Mbps.
It consists of only 12 pins, compared to GMII's 24.

.. figure:: cn0506_rgmii.png
   :align: center

   CN0506 RGMII interface block diagram

Source synchronous interfaces are used for both RX and TX. The ADIN1300
generates a 125 MHz, 25 MHz, or 2.5 MHz RXC signal to synchronize the RXD
pins. The transmit clock signal is provided by the MAC on the TXC line.

The reset signal for both ADIN1300 devices comes from the PS/HPS.
The INT_N signal is not used as an interrupt; it is only monitored by software
as input on GPIO[33] (PHY A) and GPIO[32] (PHY B).

The speed LEDs are fully functional for the RGMII interface. For Xilinx
carriers, the GMII to RGMII converters use shared clock resources, but this
does not affect the independence of the two interfaces.

RGMII Supported Carriers
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Board
     - FMC Slot
     - Connections
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - FMC HPC1
     - PS8: PHY_A-Ethernet0, PHY_B-Ethernet1
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - FMC LPC
     - PS7: PHY_A-Ethernet0, PHY_B-Ethernet1
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC
     - PS7: PHY_A-Ethernet0, PHY_B-Ethernet1

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/cn0506`

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The :adi:`ADIN1300` PHY is supported by the Linux kernel ADIN PHY driver:

- :git-linux:`drivers/net/phy/adin.c`

Device Tree
~~~~~~~~~~~

The following device tree sources are available for CN0506 configurations:

**ZC706:**

- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zc706-adv7511-cn0506-rgmii.dts`
- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zc706-adv7511-cn0506-mii.dts`
- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zc706-adv7511-cn0506-rmii.dts`

**ZedBoard:**

- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zed-adv7511-cn0506-rgmii.dts`
- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zed-adv7511-cn0506-mii.dts`
- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zed-adv7511-cn0506-rmii.dts`

**ZCU102:**

- :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-cn0506-rgmii.dts`
- :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-cn0506-mii.dts`
- :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-cn0506-rmii.dts`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

- `EVAL-CN0506-FMCZ Design & Integration Files <https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/cn0506.html#designtools>`__

  - Schematics
  - Gerber Files
  - Bill of Materials
  - Allegro Layout Files
  - Assembly Files

More Information
----------------

- :adi:`ADIN1300 Product Page <ADIN1300>`
- `CN0506 HDL Reference Design <https://analogdevicesinc.github.io/hdl/projects/cn0506/index.html>`__
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
