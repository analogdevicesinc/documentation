Quick Start
===========

.. image:: adrv9009_zu11eg_setup.png
   :align: center
   :width: 600

This guide provides instructions on how to set up the ADRV9009-ZU11EG on the
ADRV2CRR-FMC carrier board.

To use with the AD-FMCOMMS8-EBZ, refer to the
:ref:`AD-FMCOMMS8-EBZ Quick Start Guide <ad-fmcomms8-ebz>`.

Required Software
-----------------

- SD card (16 GB or larger) imaged with the latest
  :doc:`Kuiper Linux </linux/kuiper/index>` release
- A UART terminal (PuTTY / Tera Term / Minicom), baud rate 115200 (8N1)

Required Hardware
-----------------

- ADRV9009-ZU11EG SoM board
- ADRV2CRR-FMC carrier board
- Micro-USB cable
- Ethernet cable
- 12 V power supply (145 W, included with carrier kit)

Optional Hardware
-----------------

- Reference clock source
- USB Type-C multiport hub
- USB keyboard and mouse
- DisplayPort compatible monitor

Hardware Setup
--------------

#. Connect the ADRV9009-ZU11EG SoM to the ADRV2CRR-FMC carrier board.
#. Connect the 12 V power supply to **P11**.
#. Connect USB UART **P8** (Micro USB) to your host PC.
#. Connect fan to **P9**.
#. Insert SD card into socket **P15**.
#. Configure the ADRV2CRR-FMC for SD boot using **S13**, **S14**, **S15**,
   **S16**.
#. Configure boot source using **S9** to boot from the carrier SD card.
#. Turn on the power switch using **S12**.
#. Optionally connect test and measurement equipment to U.FL RF ports.
#. Observe kernel and serial console messages on your terminal (use the first
   ttyUSB or COM port registered).

Expected Boot Messages
----------------------

After power-on, the UART terminal will display U-Boot and Linux kernel boot
messages. The key messages to look for:

- ``adrv9009 spiX.0: adrv9009 Rev 192, ... successfully initialized via jesd204-fsm``
  confirms both ADRV9009 devices initialized successfully.

After boot completes, log in with:

- Username: ``analog``
- Password: ``analog``

Verifying Operation
-------------------

Verify all IIO devices are present:

.. code-block:: bash

   iio_info | grep iio:device

Expected output:

.. code-block::

   iio:device0: ams
   iio:device1: hmc7044-car
   iio:device2: adm1177
   iio:device3: hmc7044
   iio:device4: adrv9009-phy
   iio:device5: adrv9009-phy-b
   iio:device6: axi-adrv9009-rx-obs-hpc (buffer capable)
   iio:device7: axi-adrv9009-tx-hpc (buffer capable)
   iio:device8: axi-adrv9009-rx-hpc (buffer capable)

Verify clock chip lock status on the SoM:

.. code-block:: bash

   iio_attr -q -D hmc7044 status

Expected output shows both PLLs locked:

.. code-block::

   --- PLL1 ---
   Status: Locked
   Using:  CLKIN1 @ 122880000 Hz
   PFD:    7680 kHz
   --- PLL2 ---
   Status: Locked (Unsynchronized)
   Frequency:      2949120000 Hz
   SYSREF Status:  Valid & Locked
   SYNC Status:    Unsynchronized
   Lock Status:    PLL1 & PLL2 Locked

Verify JESD204B link status:

.. code-block:: bash

   TERM=vt100 jesd_status -s

Expected output shows all links enabled with DATA status:

.. code-block::

   (DEVICES) Found 3 JESD204 Link Layer peripherals

   (0): 84a30000.axi-jesd204-tx
   (1): 84a50000.axi-jesd204-rx
   (2): 84a70000.axi-jesd204-rx

   (STATUS)               (0)          (1)        (2)
   Link is                 enabled      enabled    enabled
   Link Status             DATA         DATA       DATA
   Measured Link Clock     122.881      245.761    122.881
   Reported Link Clock     122.880      245.760    122.880
   Lane rate               4915.200     9830.400   4915.200
   Lane rate / 40          122.880      245.760    122.880
   LMFC rate               7.680        7.680      3.840
   SYSREF captured         Yes          Yes        Yes
   SYSREF alignment error  No           No         No
   SYNC~                   deasserted

.. note::

   The default display output for this project uses DisplayPort (not HDMI).
   If using a local display, ensure a DisplayPort monitor is connected.

IIO Oscilloscope Remote
------------------------

The :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application
can be used to connect remotely to the platform from a network-enabled Linux
host.

#. Build and start the IIO Oscilloscope on your host PC.
#. Go to **Settings > Connect** and enter the IP address of the target.

.. note::

   This is a persistent filesystem. Always shut down properly from the
   terminal (``sudo shutdown -h now``) before disconnecting power, otherwise
   the SD card may be corrupted.

Multi-SOM Synchronization
--------------------------

Multiple ADRV9009-ZU11EG RF-SOMs can be synchronized together for complex
multi-stream applications with deterministic latency. Synchronization is
accomplished by phase-aligning the SYSREF and REFCLK signals using
:adi:`HMC7044` high-performance jitter attenuators. Phase alignment is
achieved by pulsed SYNC or RFSYNC inputs, which can be extended to multiple
clock tree stages.

With a single HMC7044 synchronization board, up to three carriers (twelve
ADRV9009 transceivers) can be synchronized.

Clock Tree Synchronization Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The HMC7044 used throughout the clock tree supports two alternative
synchronization modes. Both modes have their own tradeoffs regarding jitter,
correlated close-in phase noise, timing requirements, phase synchronization
reliability over PVT, unwanted signal coupling, thermal drift, and power
consumption. Device trees are provided for both methods.

Reference Distribution
^^^^^^^^^^^^^^^^^^^^^^

A lower-frequency reference is used between different levels in the clock
tree. All clock chips in the hierarchy require their own local VCXO, and the
reference is used to lock the VCXO using PLL1. A SYNC signal is used to
generate the synchronization event. If the SYNC pin transitions from 0 to 1
with sufficient setup/hold margin with respect to the VCXO, this
synchronization event is deterministically carried through PLL2, up the
timing chain through the N2 divider, and then to the master SYSREF timer.
This mechanism allows synchronization of SYSREF timer and output phases of
multiple HMC7044 devices.

.. list-table:: Reference Distribution Device Trees
   :header-rows: 1

   * - Configuration
     - Device Tree
   * - Primary (SOM only)
     - :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-sync-jesd204-fsm-multisom-primary.dts`
   * - Secondary (SOM only)
     - :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-sync-jesd204-fsm-multisom-secondary.dts`
   * - Primary (SOM + FMCOMMS8)
     - :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-sync-fmcomms8-jesd204-fsm-multisom-primary.dts`
   * - Secondary (SOM + FMCOMMS8)
     - :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-sync-fmcomms8-jesd204-fsm-multisom-secondary.dts`

Clock Distribution
^^^^^^^^^^^^^^^^^^

The maximum frequency used in the system is generated by the topmost HMC7044
and then distributed throughout the entire clock tree. This method bypasses
PLL1 and PLL2 of all clock chips below the top chip. All lower-level clock
chips act as clock fanout buffers, where only the output dividers can be
used. Lower-level clock chips receive their input clock via FIN/CLKIN1 and
are synced via RFSYNC/CLKIN0.

This mode also allows for TRX baseband rates that would otherwise not be
possible with the default installed VCXO of 122.88 MHz. For example, a
250.000 MSPS rate becomes possible by providing a 500.000 MHz or
1000.000 MHz external clock.

.. list-table:: Clock Distribution Device Trees
   :header-rows: 1

   * - Configuration
     - Device Tree
   * - Primary (SOM + FMCOMMS8)
     - :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-sync-fmcomms8-jesd204-fsm-multisom-primary-clockdist.dts`
   * - Secondary (SOM + FMCOMMS8)
     - :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-sync-fmcomms8-jesd204-fsm-multisom-secondary-clockdist.dts`

.. note::

   For clock distribution synchronization, passive component changes are
   required on the ADRV2CRR-FMC carrier board:

   **Rev C:**

   - Replace C18, C19, C236, C240 with 0 ohm resistors
   - Replace C289, C290 with 0 ohm resistors
   - Unload 0 ohm resistors from R77, R112 and insert to R110, R111

   **Rev C.1:**

   - Replace C289, C290 with 0 ohm resistors
   - Unload 0 ohm resistors from R77, R112 and insert to R110, R111

Hardware Setup for Multi-SOM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Required Equipment:**

- HMC7044 evaluation board (or AD-SYNCHRONA14-EBZ, depending on device tree
  version)
- 2x ADRV9009-ZU11EG RF-SOM with ADRV2CRR-FMC carriers

**HMC7044 Evaluation Board Modifications:**

.. warning::

   There is no over-voltage or reverse polarity protection. Connect a 5 V,
   1 A power supply to TP17 (GND) and TP14 (VCC).

The following changes must be made on the evaluation board:

#. Populate J4 and J20 SMA connectors (if not already present).
#. Replace C28 and C59 with 0 ohm resistors.
#. Replace R159, R160, R276, R180, R181, R365 with 50 ohm resistors.

**SPI Connection to Carrier Board:**

Connect the HMC7044 evaluation board J1 to the carrier P25 expansion
connector:

.. list-table::
   :header-rows: 1

   * - P25 (Carrier)
     - J1 (Clock Board)
     - Function
   * - 2
     - 12
     - GND
   * - 3
     - 20
     - CS
   * - 4
     - 16
     - MOSI
   * - 5
     - 18
     - MISO
   * - 6
     - 14
     - CLK

**RefCLK and SYNC Connections:**

- CLKOUT5_P and CLKOUT6_P connect to the SYNC SMAs on the carriers
- CLKOUT0 and CLKOUT2 connect to the REFCLK SMAs on the carriers

.. note::

   Only the following outputs work as SYNC in CMOS mode: CLKOUT0, 3, 5, 6,
   9, 10, and 13. Other outputs are 180 deg out of phase in CMOS mode and
   should be used as differential REFCLOCK.

Theory of Operation
~~~~~~~~~~~~~~~~~~~

There are two domains of synchronization: the ADRV9009 transceivers and the
FPGAs. Synchronization for the transceivers is provided by the clocking tree
of HMC7044s and the JESD protocol. The parent (external) HMC7044 is
responsible for general system reference (SYSREF) control, with reference
signals feeding the clock chips on the individual SOMs and FPGAs.

During multi-chip synchronization (MCS), all baseband data from the
converters is synchronized across transceiver chips. This requires specific
SYSREFs to be captured at each transceiver simultaneously, creating
deterministic phase differences between transceivers when RFPLL sync is
enabled.

Application-Layer Synchronization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Synchronization at the application layer across multiple FPGAs is achieved
using the external synchronization feature of the transport layer cores with
the SYSREF signal. Once the JESD links are up, later SYSREF pulses (matching
the initial timing) can be used as references for simultaneous data
capture/drive on multiple FPGAs.

The synchronization mechanism must be orchestrated by software:

#. Disable SYSREF generation to FPGAs.
#. Arm the external synchronization mechanisms in all transport layer cores.
#. Program all DMA cores to prepare data transfers.
#. Program the clock chips for a single SYSREF pulse that will reach all
   transport layer cores simultaneously.

Running Multi-SOM Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `pyadi-iio <https://github.com/analogdevicesinc/pyadi-iio>`__ library
provides a Python class for multi-SOM synchronization. The
``adrv9009_zu11eg_multi.py`` class and ``adrv9009_som_multi.py`` example
script handle the complete synchronization flow.

.. important::

   While the devices are not yet fully initialized during the multi-SOM
   synchronization process, they must not be accessed via their regular API.
   Ensure that:

   - IIO Oscilloscope does not start automatically (remove from
     ``/home/analog/.config/autostart/``)
   - No other script automatically accesses the ``adrv9009-phy`` IIO devices
   - Both boards have unique hardware MAC addresses to avoid network issues

Troubleshooting Multi-SOM
~~~~~~~~~~~~~~~~~~~~~~~~~~

On the primary setup, check the external clock chip status:

.. code-block:: bash

   iio_attr -D hmc7044-ext status

The external chip reporting ``Unsynchronized`` status is expected, since it
is only frequency-locked against a 30.72 MHz reference clock.

On both primary and secondary setups, verify that all clock chips (hmc7044,
hmc7044-car, and optionally hmc7044-fmc) report ``Locked`` and
``Synchronized`` status.

Production Testing
-------------------

Production tests for the ADRV9009-ZU11EG consist of a series of bash scripts
running on a Raspberry Pi 4 (host) connected via Ethernet to the DUT (Device
Under Test). The Raspberry Pi requires an HDMI monitor and USB keyboard. All
test sequences are started from the GUI interface displayed on the monitor.

**Required test equipment includes:**

- Raspberry Pi 4 (or newer) with prepared SD card
- HDMI monitor and USB keyboard for the Raspberry Pi
- DUT SD card with test image
- CAT5 Ethernet cable between Raspberry Pi and DUT
- I2C programming cable for ADM1266 sequencer
- USB cables (USB-A to USB-C, USB-A to Micro-USB)
- Loopback adapters: QSFP, SFP, FMC, PCIe, Ethernet, Audio
- 4x U.FL loopback cables for RF testing
- DisplayPort to HDMI cable
- USB 3.0 memory stick (FAT formatted)

**Test Sequence:**

When testing the ADRV9009-ZU11EG, run tests in this order: Test 1, Test 2,
Test 4, Test 5, Test 6. After installing the heatsink, run Test 6 again.

.. note::

   Always power off both the ADRV and Raspberry Pi properly before
   disconnecting power. Select menu item 9 to power off the ADRV first, then
   power off the Raspberry Pi.
