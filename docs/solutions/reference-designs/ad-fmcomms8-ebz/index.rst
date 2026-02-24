.. _ad-fmcomms8-ebz:

AD-FMCOMMS8-EBZ User Guide
============================

Introduction
------------

The :adi:`AD-FMCOMMS8-EBZ
<en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad-fmcomms8-ebz.html>`
is an integrated RF design containing two :adi:`ADRV9009` wideband
transceivers. By connecting to a compatible FPGA development board that
supports FMC HPC mechanical connector and JESD204B bus interface, it can be
used for evaluation and prototyping with up to 4 transmit and receive channels
that can be synchronized in phase and frequency.

Additionally it can be used with the :ref:`ADRV9009-ZU11EG <adrv9009zu11eg>`
RF-SOM system. This gives a path to evaluating and prototyping with up to 8
phase and frequency synchronized transmit and receive channels for complex
multi-stream applications ensuring end-to-end deterministic latency.

The ADRV9009 transceivers include integrated LO and phase synchronization.
Overall system frequency and phase synchronization is maintained with a clock
tree structure using the ADI high performance low jitter :adi:`HMC7044` device,
making it ideal for applications requiring RF phase alignment with a large
number of channels.

.. image:: fmcomms8_top.png
   :align: center
   :width: 400

.. image:: fmcomms8-bot.png
   :align: center
   :width: 400

Features
~~~~~~~~

- Two ADRV9009 devices, providing (in total):

  - Quad transmitters / Quad receivers
  - Quad input observation receiver for DPD
  - Max Rx BW: 200 MHz
  - Max tunable Tx synthesis BW: 450 MHz
  - Max observation Rx BW: 450 MHz
  - Tuning range: 75 MHz to 6000 MHz
  - Fully integrated fractional-N RF synthesizers
  - Multi-chip phase synchronization for all RF LO and baseband clocks

- FMC HPC compatible interface (complies with VITA 57.1, 84 mm x 69 mm)
- Multi-chip phase synchronization using :adi:`HMC7044`
- Platform development environment support includes Linux Industrial I/O (IIO),
  MATLAB, Simulink, GNU Radio, and streaming interfaces for custom C, C++,
  Python, and C# applications
- HDL reference designs and drivers for zero-day development

.. toctree::
   :hidden:

   quickstart_a10soc
   testing

Supported Devices
-----------------

- :adi:`ADRV9009`

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - Yes
     - Yes
   * - :ref:`ADRV9009-ZU11EG <adrv9009zu11eg>` (via ADRV2CRR-FMC)
     - Yes
     - Yes
   * - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10/sx.html>`
     - Yes
     - Yes

Schematic, PCB Layout, Bill of Materials
-----------------------------------------

`AD-FMCOMMS8-EBZ Design & Integration Files <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/ad-fmcomms8-ebz-designsupport.zip>`__

- Schematic
- PCB Layout
- Bill of Materials
- Allegro Project

Quick Start
-----------

Required Software
~~~~~~~~~~~~~~~~~

- SD card (16 GB or larger) imaged with the latest
  :doc:`Kuiper Linux </linux/kuiper/index>` release
- A UART terminal (PuTTY / Tera Term / Minicom), baud rate 115200 (8N1)

SD Card Boot Files
++++++++++++++++++

After writing the Kuiper Linux image, copy the carrier-specific boot files
into the **BOOT** partition of the SD card:

**ADRV9009-ZU11EG carrier:**

- **BOOT.BIN** from ``zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-sync-fmcomms8``
- **Image** from ``zynqmp-common``
- **system.dtb** from ``zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-sync-fmcomms8``

**ZCU102 carrier:**

- **BOOT.BIN** from ``zynqmp-zcu102-rev10-adrv9009-fmcomms8``
- **Image** from ``zynqmp-common``
- **system.dtb** from ``zynqmp-zcu102-rev10-adrv9009-fmcomms8``

Required Hardware
~~~~~~~~~~~~~~~~~

**ADRV9009-ZU11EG setup:**

- ADRV9009-ZU11EG SoM board
- ADRV2CRR-FMC carrier board
- AD-FMCOMMS8-EBZ evaluation board
- Micro-USB cable
- Ethernet cable
- 12 V power supply (145 W, included with carrier kit)

**ZCU102 setup:**

- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` evaluation board
- AD-FMCOMMS8-EBZ evaluation board
- Micro-USB cable
- Ethernet cable
- Power supply

**Optional:**

- Reference clock source
- USB Type-C multiport HUB
- USB keyboard and mouse
- DisplayPort compatible monitor

Hardware Setup (ADRV9009-ZU11EG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: testing/adrv2crr_sw_jmp_settings.jpg
   :align: center

   ADRV2CRR-FMC switch and jumper settings

#. Connect the ADRV9009-ZU11EG SoM to the ADRV2CRR-FMC carrier board.
#. Connect the AD-FMCOMMS8-EBZ to the FMC HPC connector on the ADRV2CRR-FMC.
#. Connect the 12 V power supply to **P11**.
#. Connect USB UART **P8** (Micro USB) to your host PC.
#. Connect fan to **P9**.
#. Insert SD card into socket **P15**.
#. Configure the ADRV2CRR-FMC for SD boot using **S13**, **S14**, **S15**,
   **S16** (see figure above).

   .. figure:: testing/adrv9009-zu11g-sd-card-select.png
      :align: center
      :width: 400

      SD card boot select (S9) — set to boot from carrier

#. Configure boot source using **S9** to boot from the carrier SD card.
#. Turn on the power switch using **S12**.
#. Optionally connect test and measurement equipment to U.FL RF ports.
#. Observe kernel and serial console messages on your terminal (use the first
   ttyUSB or COM port registered, baud rate 115200 8N1).

Hardware Setup (ZCU102)
~~~~~~~~~~~~~~~~~~~~~~~

For the ZCU102, the FMCOMMS8 board connects to the **HPC0** connector. The
carrier setup requires:

#. Connect the AD-FMCOMMS8-EBZ to the HPC0 FMC connector on the ZCU102.
#. Connect the power supply to the ZCU102.
#. Connect USB UART (Micro USB) to your host PC.
#. Connect an Ethernet cable for network access.
#. Insert the SD card.
#. Optionally connect a DisplayPort monitor, USB keyboard, and mouse.
#. Turn on the power switch on the ZCU102.
#. Observe kernel and serial console messages on your terminal (baud rate
   115200, 8N1).

Hardware Setup (Arria 10 SoC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When used with the Arria 10 SoC Development Kit, an FMC pin rework is
required. See :doc:`quickstart_a10soc` for detailed instructions.

Expected Boot Messages
~~~~~~~~~~~~~~~~~~~~~~

After power-on, the UART terminal will display U-Boot and Linux kernel boot
messages. Key messages to look for:

- ``adrv9009 spiX.0: adrv9009_info: adrv9009-x2 Rev 192, ... successfully initialized via jesd204-fsm``
  confirms both ADRV9009 devices initialized successfully.
- ``cf_axi_adc ... probed ADC ADRV9009-X2 as MASTER`` confirms the AXI ADC
  core is operational.
- ``cf_axi_dds ... probed DDS ADRV9009-X2`` confirms the AXI DAC DDS core is
  operational.

After boot completes, log in with:

- Username: ``analog``
- Password: ``analog``

Verifying Operation
~~~~~~~~~~~~~~~~~~~

Verify all IIO devices are present:

.. code-block:: bash

   iio_info | grep iio:device

**ZCU102 expected output:**

.. code-block::

   iio:device7: axi-adrv9009-tx-hpc (buffer capable)
   iio:device5: axi-adrv9009-rx-hpc (buffer capable)
   iio:device3: adrv9009-phy-c
   iio:device1: hmc7044-fmc
   iio:device6: axi-adrv9009-rx-obs-hpc (buffer capable)
   iio:device4: adrv9009-phy-d
   iio:device2: ad7291
   iio:device0: ams

**ADRV9009-ZU11EG expected output:**

.. code-block::

   iio:device0: ams
   iio:device1: hmc7044-car
   iio:device2: hmc7044-ext
   iio:device3: hmc7044-fmc
   iio:device4: hmc7044
   iio:device5: adrv9009-phy-c
   iio:device6: adrv9009-phy-d
   iio:device7: adrv9009-phy
   iio:device8: adrv9009-phy-b
   iio:device9: axi-adrv9009-rx-hpc (buffer capable)
   iio:device10: axi-adrv9009-rx-obs-hpc (buffer capable)
   iio:device11: axi-adrv9009-tx-hpc (buffer capable)

.. note::

   When using the ADRV9009-ZU11EG with FMCOMMS8, there are four ADRV9009
   devices (adrv9009-phy, adrv9009-phy-b on the SoM, and adrv9009-phy-c,
   adrv9009-phy-d on FMCOMMS8) and four HMC7044 clock chips (hmc7044 on the
   SoM, hmc7044-fmc on FMCOMMS8, hmc7044-car on the carrier, and hmc7044-ext).

Verify Clock Chip Lock Status
++++++++++++++++++++++++++++++

**ZCU102 (single HMC7044):**

.. code-block:: bash

   iio_attr -q -D hmc7044 status

Expected output shows both PLLs locked and SYSREF valid:

.. code-block::

   --- PLL1 ---
   Status: Locked
   Using:  CLKIN3 @ 19200000 Hz
   PFD:    3840 kHz
   --- PLL2 ---
   Status: Locked (Unsynchronized)
   Frequency:      2949120000 Hz (Autocal cap bank value: 14)
   SYSREF Status:  Valid & Locked
   SYNC Status:    Unsynchronized
   Lock Status:    PLL1 & PLL2 Locked

**ADRV9009-ZU11EG (three HMC7044 chips):**

When using the ADRV9009-ZU11EG setup, verify lock status on the SoM, FMCOMMS8,
and carrier clock chips:

.. code-block:: bash

   iio_attr -q -D hmc7044 status
   iio_attr -q -D hmc7044-fmc status
   iio_attr -q -D hmc7044-car status

All three should report ``PLL1 & PLL2 Locked`` and ``SYSREF Status: Valid &
Locked``.

JESD204B Link Synchronization
++++++++++++++++++++++++++++++

The :adi:`ADRV9009` transceivers are synchronized using the
JESD204 (FSM) Interface Linux Kernel Framework. The transceivers should always
be in a synchronized state after boot.

Verify JESD204B link status:

.. code-block:: bash

   TERM=vt100 jesd_status -s

Expected output shows all links enabled with DATA status:

.. code-block::

   (DEVICES) Found 3 JESD204 Link Layer peripherals

   (0): 85a30000.axi-jesd204-tx
   (1): 85a70000.axi-jesd204-rx
   (2): 85a50000.axi-jesd204-rx

   (STATUS)               (0)          (1)        (2)
   Link is                 enabled      enabled    enabled
   Link Status             DATA         DATA       DATA
   Measured Link Clock     122.891      122.893    245.782
   Reported Link Clock     122.880      122.880    245.760
   Lane rate               4915.200     4915.200   9830.400
   Lane rate / 40          122.880      122.880    245.760
   LMFC rate               7.680        3.840      7.680
   SYSREF captured         Yes          Yes        Yes
   SYSREF alignment error  No           No         No
   SYNC~                   deasserted

   (LANE STATUS)                   (1)                          (2)
   Lane#                             0      1      2      3       0      1      2      3
   Errors                            0      0      0      0       0      0      0      0
   CGS State                         DATA   DATA   DATA   DATA    DATA   DATA   DATA   DATA
   Initial Frame Sync                Yes    Yes    Yes    Yes     Yes    Yes    Yes    Yes
   Initial Lane Alignment Sequence   Yes    Yes    Yes    Yes     Yes    Yes    Yes    Yes

.. note::

   The base addresses shown above are for the ZCU102. On the ADRV9009-ZU11EG,
   the addresses are ``84aX0000`` instead of ``85aX0000``, and the
   ADRV9009-ZU11EG setup has 8 lanes per receiver peripheral (serving 4
   ADRV9009 devices).

Video Configuration
++++++++++++++++++++

.. note::

   The default display output for this project uses DisplayPort (not HDMI).
   If using a local display, ensure a DisplayPort monitor is connected.

IIO Oscilloscope Remote
~~~~~~~~~~~~~~~~~~~~~~~~

The :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application
can be used to connect remotely to the platform from a network-enabled Linux
host.

#. Build and start the IIO Oscilloscope on your host PC.
#. Go to **Settings > Connect** and enter the IP address of the target.

.. warning::

   This is a persistent file system. Always shut down properly from the
   terminal (``sudo shutdown -h now``) before disconnecting power, otherwise
   the SD card may be corrupted.

HDL Reference Design
--------------------

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/fmcomms8`

Software Support
----------------

Linux Drivers
~~~~~~~~~~~~~

- :git-linux:`ADRV9009 Device Driver <drivers/iio/adc/adrv9009.c>`
- :git-linux:`HMC7044 Clock Driver <drivers/iio/frequency/hmc7044.c>`
- :git-linux:`AXI ADC HDL Driver <drivers/iio/adc/cf_axi_adc_core.c>`
- :git-linux:`AXI DAC HDL Driver <drivers/iio/frequency/cf_axi_dds.c>`
- :git-linux:`AXI JESD204 TX Driver <drivers/iio/jesd204/axi_jesd204_tx.c>`
- :git-linux:`AXI JESD204 RX Driver <drivers/iio/jesd204/axi_jesd204_rx.c>`
- :git-linux:`AXI ADXCVR Driver <drivers/iio/jesd204/axi_adxcvr.c>`
- :git-linux:`AXI DMAC Driver <drivers/dma/dma-axi-dmac.c>`

Linux Applications
~~~~~~~~~~~~~~~~~~

- **IIO Oscilloscope**: Full graphical interface for device control, data
  capture, and spectral analysis. Supports the ADRV9009/ADRV9008 plugin views
  for transceiver configuration.
- **JESD204B Status Utility**: Command-line tool for verifying link status
  (``jesd_status``).
- **JESD204 Eye Scan**: Utility for viewing transceiver eye diagrams.

Working with Data
~~~~~~~~~~~~~~~~~

- Data can be streamed into or out of the ADRV9009 using MATLAB/Simulink via
  the :doc:`libiio </software/libiio/index>` client bindings.
- Custom applications can use the IIO streaming interface with C, C++, Python,
  or C# for real-time data acquisition and playback.

Functional Testing
------------------

Details on how the AD-FMCOMMS8-EBZ is functionally tested can be found in the
:doc:`testing` page.

More Information
----------------

- :ref:`ADRV9009-ZU11EG User Guide <adrv9009zu11eg>`
- :adi:`ADRV9009 Product Page <ADRV9009>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__
- `ADRV9009 MATLAB Filter Wizard / Profile Generator <https://www.analog.com/en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
