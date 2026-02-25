.. _adrv904x:

ADRV904x Prototyping Platform User Guide
=========================================

.. image:: adrv904x_block_diagram.png
   :align: center
   :width: 600

The :adi:`ADRV904x-MB/PCBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV904x.html>`
is an FMC radio card for the :adi:`ADRV9040`, a highly integrated, system on
chip (SoC) radio frequency (RF) agile transceiver featuring eight independently
controlled transmitters, dedicated observation receiver inputs for monitoring
transmitter channels, eight independently controlled receivers, integrated
synthesizers, and digital signal processing functions. The :adi:`ADRV9040`
provides the performance demanded by cellular infrastructure applications,
including small cell base station radios, macro 3G/4G/5G systems, and massive
multiple in/multiple out (MIMO) base stations.

The ADRV904x radio card is designed to showcase the :adi:`ADRV9040`
(8-channel wideband RF transceiver with integrated DPD and CFR). The radio card
provides an 8x8 transceiver platform supporting 400 MHz instantaneous bandwidth
for device evaluation. All peripherals necessary for the radio card to operate
include a separate high efficiency power circuit board and a high-performance
clocking solution on the radio board. Connecting the radio card to an FPGA
motherboard through the FMC connector forms a complete evaluation platform for
the :adi:`ADRV9040`.

While the complete chip level design package can be found on the
:adi:`ADI web site <en/products/adrv9040.html#product-documentation>`,
information on the card and how to use it, the design package that surrounds it,
and the software which can make it work can be found here.

Supported Devices
-----------------

- :adi:`ADRV9040`

Supported Carriers
------------------

The ADRV904x-MB/PCBZ is, by definition, an "FPGA mezzanine card" (FMC),
which means it needs a carrier to plug into.

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
     - No-OS
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` (FMC HPC0 Slot)
     - Yes
     - Yes
     - Yes

Table of Contents
-----------------

#. Use the board to better understand the ADRV904x

   #. :ref:`What you need to get started <adrv904x-prerequisites>`
   #. :ref:`Quick Start Guide: Linux on ZCU102 <adrv904x-quickstart-zcu102>`
   #. :doc:`Kuiper Linux </linux/kuiper/index>` (SD card images)

#. Software Solutions

   #. :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`
   #. `Transceiver Toolbox for MATLAB and Simulink <https://github.com/analogdevicesinc/TransceiverToolbox>`__
   #. `pyadi-iio <https://analogdevicesinc.github.io/pyadi-iio/>`__
   #. `IIO Command Line Tools <https://github.com/analogdevicesinc/libiio>`__
   #. `GNU Radio <https://github.com/analogdevicesinc/gr-iio>`__

#. Embedded Resources

   #. :ref:`ADRV904x Linux Device Driver <adrv904x-linux-driver>`
   #. :ref:`No-OS System Level Design Setup <adrv904x-no-os>`

#. FPGA Resources

   #. :ref:`HDL Reference Design <adrv904x-hdl>`
   #. `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

#. Hardware Resources

   #. :adi:`ADRV9040 Product Page <ADRV9040>`
   #. :adi:`Full Datasheet and Chip Design Package <en/products/adrv9040.html#product-documentation>`

#. Help and Support

   #. :ez:`FPGA Reference Designs <fpga>` -- HDL reference design questions
   #. :ez:`Linux Software Drivers <linux-software-drivers>` -- Linux distribution, drivers, and device tree questions
   #. :ez:`Microcontroller No-OS Drivers <microcontroller-no-os-drivers>` -- no-OS driver questions

.. _adrv904x-prerequisites:

Prerequisites
~~~~~~~~~~~~~

To evaluate the ADRV904x-MB/PCBZ board, you will need:

#. A compatible FPGA carrier board (see table above).
#. A way to interact with the platform:

   - DisplayPort monitor, USB keyboard and mouse (for ARM/FPGA SoC platforms)
   - LAN cable and host PC (for FPGA-only solutions)

#. Internet connection to update scripts/binaries on the SD card.
#. RF test equipment for transmit/receive verification.

.. _adrv904x-quickstart-zcu102:

Quick Start Guide: ZCU102
--------------------------

Required Software
~~~~~~~~~~~~~~~~~

- SD card (8 GB or larger) imaged with the latest
  :doc:`Kuiper Linux </linux/kuiper/index>` release
- A UART terminal (PuTTY / Tera Term / Minicom), baud rate 115200 (8N1)

Required Hardware
~~~~~~~~~~~~~~~~~

- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` Rev 1.0 or later
- ADRV904x-MB/PCBZ evaluation board
- 12 VDC 3 A MAX power supply for the ADRV904x board
- Micro-USB cable
- Ethernet cable
- Optionally: USB keyboard, mouse, and a DisplayPort compatible monitor

Hardware Setup
~~~~~~~~~~~~~~

#. Ensure the following jumpers are mounted on the ADRV904x board:

   - P209 -- GPIO4_FMC
   - P216 -- GPIO11_FMC
   - P2021 -- TEST connected to GND

#. Connect the ADRV904x board to the FPGA carrier **HPC0** (FMC0) socket.
#. Connect USB UART J83 (Micro USB) to your host PC.
#. Connect the 12 VDC power supply to the ADRV904x board.
#. Insert the SD card into the ZCU102 slot.
#. Configure ZCU102 for SD BOOT (mode SW6[4:1] switch in the position
   **OFF, OFF, OFF, ON**).
#. Turn on the power switch on the FPGA board.
#. Observe kernel and serial console messages on your terminal (use the first
   ttyUSB or COM port registered).

Expected Boot Messages
~~~~~~~~~~~~~~~~~~~~~~

After power-on, the UART terminal will display U-Boot and Linux kernel boot
messages. The key message to look for:

- ``adrv904x spi1.0: adrv904x Rev XX, Firmware X.X.X.X API version: X.X.X.X successfully initialized via jesd204-fsm``
  confirms successful ADRV9040 initialization.

After boot completes, log in with:

- Username: ``analog``
- Password: ``analog``

Verifying Operation
~~~~~~~~~~~~~~~~~~~

Verify all IIO devices are present:

.. code-block:: bash

   iio_info | grep iio:device

Expected output:

.. code-block::

   iio:device0: xilinx-ams
   iio:device1: ad9528-1
   iio:device2: adrv904x-phy
   iio:device3: axi-adrv904x-rx-hpc (buffer capable)
   iio:device4: axi-adrv904x-tx-hpc (buffer capable)

Verify JESD204C link status:

.. code-block:: bash

   TERM=vt100 jesd_status -s

Expected output shows Rx, Tx, and (optionally) Rx Observation links enabled
with DATA status.

IIO Oscilloscope Remote
~~~~~~~~~~~~~~~~~~~~~~~~

The :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application
can be used to connect remotely to the platform from a network-enabled Linux
host.

#. Build and start the IIO Oscilloscope on your host PC.
#. Go to **Settings > Connect** and enter the IP address of the target.

IIO Oscilloscope Channels
^^^^^^^^^^^^^^^^^^^^^^^^^^

Main receivers RX1 through RX8 are handled by the ``axi-adrv904x-rx-hpc``
IIO device.

.. list-table:: Receiver Input Channels
   :header-rows: 1

   * - IIO Device Channels
     - RX1
     - RX2
     - RX3
     - RX4
     - RX5
     - RX6
     - RX7
     - RX8
   * - axi-adrv904x-rx-hpc
     - voltage0_i / voltage0_q
     - voltage1_i / voltage1_q
     - voltage2_i / voltage2_q
     - voltage3_i / voltage3_q
     - voltage4_i / voltage4_q
     - voltage5_i / voltage5_q
     - voltage6_i / voltage6_q
     - voltage7_i / voltage7_q

.. note::

   This is a persistent filesystem. Always shut down properly from the
   terminal (``sudo shutdown -h now``) before disconnecting power, otherwise
   the SD card may be corrupted.

.. _adrv904x-hdl:

HDL Reference Design
--------------------

The HDL reference design is an embedded system built around a processor core.
The device digital interface is handled by the transceiver IP followed by the
JESD204C and device-specific cores. The cores are programmable through an
AXI-Lite interface. The delineated data is then passed on to independent DMA
cores for the transmit and receive paths.

The full HDL documentation is available in the
`ADRV904x HDL project documentation <https://analogdevicesinc.github.io/hdl/projects/adrv904x/index.html>`__.

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd hdl/projects/adrv904x/zcu102
   make

Configurable build parameters can be passed as make arguments:

.. code-block:: bash

   make JESD_MODE=8B10B ORX_ENABLE=1

General build instructions can be found in the
`ADI HDL Build Guide <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`__.

Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Parameter
     - Default (ZCU102)
     - Description
   * - JESD_MODE
     - 64B66B
     - Link layer encoder mode (64B66B or 8B10B)
   * - ORX_ENABLE
     - 0
     - Observation receiver path enable
   * - RX_LANE_RATE
     - 16.22
     - ADC link lane rate (Gbps)
   * - TX_LANE_RATE
     - 16.22
     - DAC link lane rate (Gbps)
   * - RX_JESD_M
     - 16
     - Number of converters per Rx link
   * - RX_JESD_L
     - 8
     - Number of lanes per Rx link
   * - TX_JESD_M
     - 16
     - Number of converters per Tx link
   * - TX_JESD_L
     - 8
     - Number of lanes per Tx link

JESD204C Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Rx Links (ADC Path)
   :header-rows: 1

   * - Parameter
     - Value
   * - Rx Deframer (L, M, F, S, NP, N)
     - L=8, M=16, F=4, S=1, NP=16, N=16
   * - Sample Rate
     - 491.52 MSPS
   * - RX_DEVICE_CLK
     - 245.76 MHz
   * - REF_CLK
     - 491.52 MHz
   * - JESD204C Lane Rate
     - 16.22 Gbps
   * - Encoding
     - 64B66B
   * - PLL
     - QPLL0

.. list-table:: Tx Links (DAC Path)
   :header-rows: 1

   * - Parameter
     - Value
   * - Tx Framer (L, M, F, S, NP, N)
     - L=8, M=16, F=4, S=1, NP=16, N=16
   * - Sample Rate
     - 491.52 MSPS
   * - TX_DEVICE_CLK
     - 245.76 MHz
   * - REF_CLK
     - 491.52 MHz
   * - JESD204C Lane Rate
     - 16.22 Gbps
   * - Encoding
     - 64B66B
   * - PLL
     - QPLL0

.. list-table:: Rx Observation Links (ORx Path, when enabled)
   :header-rows: 1

   * - Parameter
     - Value
   * - Rx Observation Deframer (L, M, F, S, NP, N)
     - L=4, M=8, F=4, S=1, NP=16, N=16
   * - Sample Rate
     - 491.52 MSPS
   * - JESD204C Lane Rate
     - 16.22 Gbps
   * - Encoding
     - 64B66B

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/adrv904x`

.. _adrv904x-linux-driver:

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The :adi:`ADRV9040` is a highly integrated, system on chip (SoC) radio
frequency (RF) agile transceiver. ADI's wideband RF transceiver delivers
8-channel integration with integrated DPD/CFR to simplify design and reduce
system power, size, weight, and costs for 5G applications, including macro
base stations, massive MIMO, and small cells.

This is a Linux industrial I/O (IIO) subsystem driver, targeting RF
transceivers. The industrial I/O subsystem provides a unified framework for
drivers for many different types of converters and sensors using a number of
different physical interfaces (I2C, SPI, etc).

.. note::

   The Linux driver for the ADRV904x is currently available on the
   ``koror_dev`` development branch and has not yet been mainlined.

Driver Source Code
^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Function
     - File
   * - Main driver
     - `adrv904x.c <https://github.com/analogdevicesinc/linux/blob/koror_dev/drivers/iio/adc/adrv904x/adrv904x.c>`__
   * - Converter interface
     - `adrv904x_conv.c <https://github.com/analogdevicesinc/linux/blob/koror_dev/drivers/iio/adc/adrv904x/adrv904x_conv.c>`__
   * - Driver header
     - `adrv904x.h <https://github.com/analogdevicesinc/linux/blob/koror_dev/drivers/iio/adc/adrv904x/adrv904x.h>`__
   * - API driver directory
     - `drivers/iio/adc/adrv904x <https://github.com/analogdevicesinc/linux/tree/koror_dev/drivers/iio/adc/adrv904x>`__

Interrelated Device Drivers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Component
     - Reference
   * - JESD204 (FSM) Framework
     - :git-linux:`drivers/jesd204`
   * - AD9528 Clock Driver
     - :git-linux:`drivers/iio/frequency/ad9528.c`
   * - AXI-DMAC DMA Controller
     - :git-linux:`drivers/dma/dma-axi-dmac.c`
   * - AXI ADC HDL Driver
     - :git-linux:`drivers/iio/adc/cf_axi_adc_core.c`
   * - AXI DAC / DDS HDL Driver
     - :git-linux:`drivers/iio/frequency/cf_axi_dds.c`
   * - AXI JESD204C RX Driver
     - :git-linux:`drivers/iio/jesd204/axi_jesd204_rx.c`
   * - AXI JESD204C TX Driver
     - :git-linux:`drivers/iio/jesd204/axi_jesd204_tx.c`
   * - AXI ADXCVR Transceiver Driver
     - :git-linux:`drivers/iio/jesd204/axi_adxcvr.c`

Processors and Firmware
^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`ADRV9040` contains several internal processor subsystems that require
firmware loading during initialization.

**ARM Processors**

The transceiver is equipped with dual built-in ARM M4 processors. The firmware
for these ARM processors is loaded during the initialization process. The ARM
processors handle radio functionality, configuring the transceiver for the
selected use case, performing initial calibrations of the signal paths, and
maintaining device performance over time through tracking calibrations.

**DFE Processor**

An ARM A55 quad-core processor is dedicated to digital front-end (DFE) features
including DPD (Digital Pre-Distortion), CLGC (Closed Loop Gain Control), and
VSWR monitoring. The DFE processor runs proprietary ADI algorithms for
real-time pre-distortion and gain correction.

**Stream Processor**

A stream processor within the transceiver performs a series of configuration
tasks based on events. After a request from the user, the stream processor
performs predefined actions loaded during device initialization. Nineteen
instances exist (18 slice processors plus 1 core processor). It executes
streams for:

- Tx1--Tx8 enable/disable
- Rx1--Rx8 enable/disable
- ORx1/ORx2 enable/disable

The firmware files for these processors must be stored in the ``/lib/firmware``
folder, or compiled into the kernel using the ``CONFIG_FIRMWARE_IN_KERNEL`` and
``CONFIG_EXTRA_FIRMWARE`` config options.

.. list-table::
   :header-rows: 1

   * - Function
     - File
   * - ARM processor firmware
     - ADRV9040_FW.bin
   * - DFE processor firmware
     - ADRV9040_DFE_CALS_FW.bin
   * - Stream processor binary
     - stream_image.bin
   * - Device profile
     - DeviceProfileTest.bin

**Gain Tables**

The gain tables for the RX paths are also loaded during boot using the firmware
framework.

.. list-table::
   :header-rows: 1

   * - Function
     - File
   * - RX Gain Correction table
     - ADRV9040_RxGainTable.csv

IIO Devices
~~~~~~~~~~~

The following IIO devices are enumerated on a ZCU102 system:

- **ad9528-1** -- Clock generator providing device and reference clocks
- **adrv904x-phy** -- Transceiver control (LO frequency, gain, calibrations)
- **axi-adrv904x-rx-hpc** -- Receive data path (buffer capable)
- **axi-adrv904x-tx-hpc** -- Transmit data path (buffer capable)

IIO Attribute Naming Convention
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - IIO sysfs attribute prefix
     - Target
   * - ``in_voltage0_[...]``
     - RX1
   * - ``in_voltage1_[...]``
     - RX2
   * - ``in_voltage2_[...]``
     - RX3
   * - ``in_voltage3_[...]``
     - RX4
   * - ``in_voltage4_[...]``
     - RX5
   * - ``in_voltage5_[...]``
     - RX6
   * - ``in_voltage6_[...]``
     - RX7
   * - ``in_voltage7_[...]``
     - RX8
   * - ``in_voltage8_[...]``
     - Observation RX1
   * - ``in_voltage9_[...]``
     - Observation RX2
   * - ``out_altvoltage0_[...]``
     - TRX LO1
   * - ``out_altvoltage1_[...]``
     - TRX LO2
   * - ``out_voltage0_[...]``
     - TX1
   * - ``out_voltage1_[...]``
     - TX2
   * - ``out_voltage2_[...]``
     - TX3
   * - ``out_voltage3_[...]``
     - TX4
   * - ``out_voltage4_[...]``
     - TX5
   * - ``out_voltage5_[...]``
     - TX6
   * - ``out_voltage6_[...]``
     - TX7
   * - ``out_voltage7_[...]``
     - TX8

Local Oscillator Control (LO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The device contains two fractional-N RF PLLs supporting a tunable range of
450--7100 MHz with 1 kHz frequency raster resolution.

.. list-table::
   :header-rows: 1

   * - Attribute
     - Port
   * - ``out_altvoltage0_LO1_frequency``
     - LO1
   * - ``out_altvoltage1_LO2_frequency``
     - LO2

.. code-block:: bash

   # Read LO frequency
   cat /sys/bus/iio/devices/iio:device2/out_altvoltage0_LO1_frequency
   # Set LO frequency to 3.6 GHz
   echo 3600000000 > /sys/bus/iio/devices/iio:device2/out_altvoltage0_LO1_frequency

TX Signal Path
^^^^^^^^^^^^^^^

The ADRV9040 transmitter section consists of eight identical and independently
controlled channels that provide all the digital processing, mixed-signal, and
RF blocks necessary to implement a direct conversion system while sharing
common frequency synthesizers. The digital data from the SERDES lanes pass
through a programmable digital processing block that includes half-band filters,
interpolation stages, and a tunable baseband filter (300--840 MHz bandwidth).
Each TX channel features an RF variable gain amplifier with 32 dB attenuation
range.

Each TX channel exposes the following IIO attributes:

.. code-block:: bash

   # Query TX primary signal bandwidth
   cat /sys/bus/iio/devices/iio:device2/out_voltage0_rf_bandwidth
   # Query TX hardware gain (attenuation)
   cat /sys/bus/iio/devices/iio:device2/out_voltage0_hardwaregain
   # Set TX attenuation to -12 dB
   echo -12 > /sys/bus/iio/devices/iio:device2/out_voltage0_hardwaregain

RX Signal Path
^^^^^^^^^^^^^^^

The ADRV9040 provides eight independent receiver channels. Each channel
contains an RF attenuator, passive mixer, transimpedance amplifier, and
continuous-time pipeline ADC with selectable hardware gain and bandwidth.

Two gain control options are available:

- **Manual gain control** -- users implement their own gain control algorithms
- **Automatic gain control (AGC)** -- using the on-chip AGC system

Each RX channel exposes the following IIO attributes:

.. code-block:: bash

   # Query RX hardware gain
   cat /sys/bus/iio/devices/iio:device2/in_voltage0_hardwaregain
   # Query RX gain control mode
   cat /sys/bus/iio/devices/iio:device2/in_voltage0_gain_control_mode
   # Query available gain control modes
   cat /sys/bus/iio/devices/iio:device2/in_voltage0_gain_control_mode_available
   # Query RSSI
   cat /sys/bus/iio/devices/iio:device2/in_voltage0_rssi
   # Query device temperature
   cat /sys/bus/iio/devices/iio:device2/in_temp0_input

Advanced Debug Facilities
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV904x driver supports advanced debug controls via the kernel debugfs.
These controls are used to debug device settings and run built-in self-tests.

To access debugfs controls, first identify the IIO device number:

.. code-block:: bash

   grep "" /sys/bus/iio/devices/iio:device*/name

Then navigate to the debugfs directory:

.. code-block:: bash

   cd /sys/kernel/debug/iio/iio:device2

BIST PRBS
^^^^^^^^^

Pseudorandom Binary Sequence (PRBS) injection to Framer 0:

.. list-table::
   :header-rows: 1

   * - Value
     - Function
   * - 0
     - ADC data source
   * - 1
     - Checkerboard data source
   * - 2
     - Toggle 0 to 1 data source
   * - 3
     - PRBS31 data source
   * - 4
     - PRBS23 data source
   * - 5
     - PRBS15 data source
   * - 6
     - PRBS9 data source
   * - 7
     - PRBS7 data source
   * - 8
     - Ramp data

.. code-block:: bash

   # Inject ramp PRBS
   echo 8 > /sys/kernel/debug/iio/iio:device2/bist_framer_0_prbs

BIST Loopback
^^^^^^^^^^^^^

Allows digitally looping back framer data into the deframer:

.. code-block:: bash

   # Enable digital TX -> RX loopback
   echo 1 > /sys/kernel/debug/iio/iio:device2/bist_framer_loopback
   # Disable loopback
   echo 0 > /sys/kernel/debug/iio/iio:device2/bist_framer_loopback

BIST Tone
^^^^^^^^^

User selectable tone injection into the TX path (all TX channels):

Syntax: ``echo <Enable> <Tone_Frequency_Hz> [Tone_Gain] > bist_tone``

.. list-table:: Tone Gain Values
   :header-rows: 1

   * - Value
     - Function
   * - 0
     - NCO gain -18 dB
   * - 1
     - NCO gain -12 dB
   * - 2
     - NCO gain -6 dB
   * - 3
     - NCO gain 0 dB

.. code-block:: bash

   # Inject 0 dB tone at 3 MHz into TX
   echo 1 3000 > /sys/kernel/debug/iio/iio:device2/bist_tone

.. _adrv904x-device-tree:

Device Tree Customization
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV904x driver is configured through the device tree. Key device tree
properties for the transceiver node:

.. list-table::
   :header-rows: 1

   * - Devicetree property
     - Description
   * - ``adi,device-config-name``
     - Device profile/configuration file
   * - ``adi,arm-firmware-name``
     - Firmware file for the ARM processors
   * - ``adi,dfe-firmware-name``
     - Firmware file for the DFE processor
   * - ``adi,stream-firmware-name``
     - Firmware file for the stream processor
   * - ``adi,rx-gaintable-names``
     - RX gain table
   * - ``adi,rx-gaintable-channel-masks``
     - Channel mask for RX gain values

Example ADRV904x PHY device tree node:

.. code-block:: dts

   trx0_adrv904x: adrv904x-phy@0 {
       compatible = "adrv904x";
       reg = <0>;

       spi-max-frequency = <25000000>;

       interrupt-parent = <&gpio>;
       interrupts = <134 IRQ_TYPE_EDGE_RISING>;

       clocks = <&clk0_ad9528 1>;
       clock-names = "dev_clk";

       clock-output-names = "rx_sampl_clk", "tx_sampl_clk";
       #clock-cells = <1>;

       jesd204-device;
       #jesd204-cells = <2>;
       jesd204-top-device = <0>;

       adi,device-config-name = "DeviceProfileTest.bin";
       adi,arm-firmware-name = "ADRV9040_FW.bin";
       adi,dfe-firmware-name = "ADRV9040_DFE_CALS_FW.bin";
       adi,stream-firmware-name = "stream_image.bin";
       adi,rx-gaintable-names = "ADRV9040_RxGainTable.csv";
       adi,rx-gaintable-channel-masks = <0xFF>;
   };

GPIO configuration example:

.. code-block:: dts

   &trx0_adrv904x {
       reset-gpios = <&gpio 134 0>;
   };

.. _adrv904x-dpd:

Digital Pre-Distortion (DPD) and CFR
--------------------------------------

The :adi:`ADRV9040` includes integrated Digital Pre-Distortion (DPD) and Crest
Factor Reduction (CFR) capabilities, making it well suited for 5G macro and
massive MIMO applications.

DPD Overview
~~~~~~~~~~~~

DPD works on the principle of pre-distorting the transmit data in the digital
domain to cancel the distortion caused by power amplifier (PA) compression in
the analog domain. A baseband model of the PA is trained on input and output
digital samples. The pre-distorter then applies an inverse function to input
samples before transmission, making the cascade of the pre-distorter response
and the PA response become a nearly-linear system.

Key benefits of DPD:

- Improves PA power-added efficiency by double or more
- Allows amplifiers to operate closer to saturation while maintaining linearity
- Reduces adjacent channel leakage ratio (ACLR) by 15--20 dB
- Addresses wideband transmission challenges in LTE/NR protocols

DFE Processor
~~~~~~~~~~~~~

The on-chip ARM A55 quad-core DFE processor executes the DPD, CLGC (Closed
Loop Gain Control), and VSWR monitoring algorithms in real-time. The DFE
firmware (``ADRV9040_DFE_CALS_FW.bin``) is loaded during device initialization
and runs autonomously to maintain PA linearity.

For detailed DPD evaluation and development workflows, including GUI-based
evaluation using the Transceiver Evaluation Software, refer to the
:adi:`ADRV9040 product documentation <en/products/adrv9040.html#product-documentation>`.

.. _adrv904x-no-os:

No-OS System Level Design
--------------------------

The No-OS system level design for ADRV904x provides a bare-metal software
reference for platforms without an operating system.

- :git-no-OS:`projects/adrv904x`

Downloads
---------

The latest boot files for ADRV904x (for all supported carriers) can be found
in the latest :doc:`Kuiper Linux </linux/kuiper/index>` release.

Source code:

- `Linux driver <https://github.com/analogdevicesinc/linux/tree/koror_dev/drivers/iio/adc/adrv904x>`__ (koror_dev branch)
- :git-hdl:`HDL project <projects/adrv904x>`
- :git-no-OS:`No-OS project <projects/adrv904x>`

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `ADRV904x HDL Project Documentation <https://analogdevicesinc.github.io/hdl/projects/adrv904x/index.html>`__
- `JESD204 High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
