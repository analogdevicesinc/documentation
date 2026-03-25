.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9025

.. _adrv9026:

ADRV9026/ADRV9029 Prototyping Platform User Guide
===================================================

.. image:: eval_adrv9026_board.png
   :align: center
   :width: 500

The :adi:`EVAL-ADRV9026 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV9026.html>`,
is an FMC radio card for the :adi:`ADRV9026` and :adi:`ADRV9029`, highly
integrated, radio frequency (RF) agile transceivers offering four independently
controlled transmitters, dedicated observation receiver inputs for monitoring
each transmitter channel, four independently controlled receivers, integrated
synthesizers, and digital signal processing functions providing complete
transceiver solutions. The devices provide the performance demanded by cellular
infrastructure applications, such as small cell base station radios, macro
3G/4G/5G systems, and massive multiple in/multiple out (MIMO) base stations.

The EVAL-ADRV9026/ADRV9029 radio cards are designed to showcase the
:adi:`ADRV9026` (quad-channel wideband RF transceiver) and :adi:`ADRV9029`
(quad-channel wideband RF transceiver with integrated DPD and CFR). The radio
cards provide a 4x4 transceiver platform for device evaluation. All peripherals
necessary for the radio card to operate include a separate high efficiency power
circuit board and a high-performance clocking solution included on the radio
board. Connecting one of the radio cards with an FPGA motherboard through the
FMC connector forms a complete evaluation platform for :adi:`ADRV9026` and
:adi:`ADRV9029`.

.. figure:: eval_adrv9029_angle.png
   :align: center
   :width: 500

   EVAL-ADRV9026/ADRV9029 Evaluation Board

While the complete chip level design package can be found on the
:adi:`ADI web site <en/products/adrv9026.html#product-documentation>`,
information on the card and how to use it, the design package that surrounds it,
and the software which can make it work can be found here.

Supported Devices
-----------------

- :adi:`ADRV9026`
- :adi:`ADRV9029`
- :adi:`ADRV9025`

Supported Carriers
------------------

The EVAL-ADRV9026/ADRV9029 is, by definition, an "FPGA mezzanine card" (FMC),
which means it needs a carrier to plug into.

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
     - No-OS
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` (FMC1 Slot)
     - Yes
     - Yes
     - Yes

Table of Contents
-----------------

#. Use the board to better understand the ADRV9026/ADRV9029

   #. :ref:`What you need to get started <adrv9026-prerequisites>`
   #. :ref:`Quick Start Guide: Linux on ZCU102 <adrv9026-quickstart-zcu102>`
   #. :doc:`Kuiper Linux </linux/kuiper/index>` (SD card images)

#. Software Solutions

   #. :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`
   #. `Transceiver Toolbox for MATLAB and Simulink <https://github.com/analogdevicesinc/TransceiverToolbox>`__
   #. `pyadi-iio <https://analogdevicesinc.github.io/pyadi-iio/>`__
   #. `IIO Command Line Tools <https://github.com/analogdevicesinc/libiio>`__
   #. `GNU Radio <https://github.com/analogdevicesinc/gr-iio>`__

#. Embedded Resources

   #. :ref:`ADRV9025 Linux Device Driver <adrv9026-linux-driver>`
   #. :ref:`No-OS System Level Design Setup <adrv9026-no-os>`

#. FPGA Resources

   #. :ref:`HDL Reference Design <adrv9026-hdl>`
   #. `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

#. Hardware Resources

   #. :adi:`ADRV9026 Product Page <ADRV9026>`
   #. :adi:`ADRV9029 Product Page <ADRV9029>`
   #. :adi:`Full Datasheet and Chip Design Package <en/products/adrv9026.html#product-documentation>`

#. Help and Support

   #. :ez:`FPGA Reference Designs <fpga>` -- HDL reference design questions
   #. :ez:`Linux Software Drivers <linux-software-drivers>` -- Linux distribution, drivers, and device tree questions
   #. :ez:`Microcontroller No-OS Drivers <microcontroller-no-os-drivers>` -- no-OS driver questions

.. _adrv9026-prerequisites:

Prerequisites
~~~~~~~~~~~~~

To evaluate the EVAL-ADRV9026/ADRV9029 board, you will need:

#. A compatible FPGA carrier board (see table above).
#. A way to interact with the platform:

   - DisplayPort monitor, USB keyboard and mouse (for ARM/FPGA SoC platforms)
   - LAN cable and host PC (for FPGA-only solutions)

#. Internet connection to update scripts/binaries on the SD card.
#. RF test equipment for transmit/receive verification.

.. _adrv9026-quickstart-zcu102:

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
- EVAL-ADRV9026 or EVAL-ADRV9029 evaluation board
- Reference clock source
- Micro-USB cable
- Ethernet cable
- Optionally: USB keyboard, mouse, and a DisplayPort compatible monitor

Hardware Setup
~~~~~~~~~~~~~~

.. image:: ../images/adrv9026_zcu102_setup.jpg
   :align: center
   :width: 600

#. Connect the EVAL-ADRV9026/ADRV9029 board to the FPGA carrier **HPC1**
   (FMC1) socket.
#. Connect USB UART J83 (Micro USB) to your host PC.
#. Insert the SD card into the slot.
#. Configure ZCU102 for SD BOOT (mode SW6[4:1] switch in the position
   **OFF, OFF, OFF, ON** as shown below).
#. Turn on the power switch on the FPGA board.
#. Observe kernel and serial console messages on your terminal (use the first
   ttyUSB or COM port registered).

.. image:: ../images/zcu102_1p0_bootmode.jpg
   :align: center
   :width: 400

Expected Boot Messages
~~~~~~~~~~~~~~~~~~~~~~

After power-on, the UART terminal will display U-Boot and Linux kernel boot
messages. The key message to look for:

- ``adrv9025 spi1.0: adrv9025 Rev 176, Firmware 6.4.0.6 API version: 6.4.0.14 Stream version: 9.4.0.1 successfully initialized via jesd204-fsm``
  confirms successful ADRV9025 initialization.

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
   iio:device2: adrv9025-phy
   iio:device3: axi-adrv9025-rx-hpc (buffer capable)
   iio:device4: axi-adrv9025-tx-hpc (buffer capable)

Read the board FRU EEPROM for identification:

.. code-block:: bash

   fru-dump -b /sys/bus/i2c/devices/15-0050/eeprom

Verify JESD204B link status:

.. code-block:: bash

   TERM=vt100 jesd_status -s

Expected output shows both Rx and Tx links enabled with DATA status.

IIO Oscilloscope Remote
~~~~~~~~~~~~~~~~~~~~~~~~

The :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application
can be used to connect remotely to the platform from a network-enabled Linux
host.

#. Build and start the IIO Oscilloscope on your host PC.
#. Go to **Settings > Connect** and enter the IP address of the target.

IIO Oscilloscope Channels
^^^^^^^^^^^^^^^^^^^^^^^^^^

Main receivers RX1, RX2, RX3, and RX4 are handled by the
``axi-adrv9025-rx-hpc`` IIO device.

.. list-table:: Receiver Input Channels
   :header-rows: 1

   * - IIO Device Channels
     - RX1
     - RX2
     - RX3
     - RX4
   * - axi-adrv9025-rx-hpc
     - voltage0_i / voltage0_q
     - voltage1_i / voltage1_q
     - voltage2_i / voltage2_q
     - voltage3_i / voltage3_q

.. note::

   This is a persistent filesystem. Always shut down properly from the
   terminal (``sudo shutdown -h now``) before disconnecting power, otherwise
   the SD card may be corrupted.

.. _adrv9026-hdl:

HDL Reference Design
--------------------

The HDL reference design is an embedded system built around a processor core.
The device digital interface is handled by the transceiver IP followed by the
JESD204B and device-specific cores. The cores are programmable through an
AXI-Lite interface. The delineated data is then passed on to independent DMA
cores for the transmit and receive paths.

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~~

General build instructions can be found in the
`ADI HDL Build Guide <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`__.

Block Diagram
~~~~~~~~~~~~~

.. figure:: adrv9026_jesd_bd.png
   :align: center

   ADRV9026 JESD block diagram

JESD204B Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Rx Links (ADC Path)
   :header-rows: 1

   * - Parameter
     - Value
   * - Rx Deframer (L, M, F, S, N, N')
     - L=4, M=4, F=4, S=1, N=16, N'=16
   * - Sample Rate
     - 250 MSPS
   * - RX_DEVICE_CLK
     - 250 MHz (Lane Rate / 40)
   * - REF_CLK
     - 250 MHz (Lane Rate / 40)
   * - JESD204B Lane Rate
     - 10 Gbps
   * - PLL
     - CPLL

.. list-table:: Tx Links (DAC Path)
   :header-rows: 1

   * - Parameter
     - Value
   * - Tx Framer (L, M, F, S, N, N')
     - L=4, M=4, F=4, S=1, N=16, N'=16
   * - Sample Rate
     - 250 MSPS
   * - TX_DEVICE_CLK
     - 250 MHz (Lane Rate / 40)
   * - REF_CLK
     - 250 MHz (Lane Rate / 40)
   * - JESD204B Lane Rate
     - 10 Gbps
   * - PLL
     - QPLL0

Clock Sources
~~~~~~~~~~~~~

.. figure:: adrv9026_clocking.png
   :align: center

   Clock sources diagram

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/adrv9026`

.. _adrv9026-linux-driver:

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The :adi:`ADRV9026` is a highly integrated, radio frequency (RF) agile
transceiver. ADI's 4th generation wideband RF transceiver delivers
quad-channel integration with the lowest power, smallest size, common platform
solution available to simplify design and reduce system power, size, weight,
and costs for 3G/4G/5G applications, including multi-standard base stations,
massive MIMO, and small cells.

This is a Linux industrial I/O (IIO) subsystem driver, targeting RF
transceivers. The industrial I/O subsystem provides a unified framework for
drivers for many different types of converters and sensors using a number of
different physical interfaces (I2C, SPI, etc).

Driver Source Code
^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Function
     - File
   * - Main driver
     - :git-linux:`drivers/iio/adc/adrv902x/adrv9025.c`
   * - Converter interface
     - :git-linux:`drivers/iio/adc/adrv902x/adrv9025_conv.c`
   * - Driver header
     - :git-linux:`drivers/iio/adc/adrv902x/adrv9025.h`
   * - API driver directory
     - :git-linux:`drivers/iio/adc/adrv902x`

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
   * - AXI JESD204B RX Driver
     - :git-linux:`drivers/iio/jesd204/axi_jesd204_rx.c`
   * - AXI JESD204B TX Driver
     - :git-linux:`drivers/iio/jesd204/axi_jesd204_tx.c`
   * - AXI ADXCVR Transceiver Driver
     - :git-linux:`drivers/iio/jesd204/axi_adxcvr.c`

Processors and Firmware
^^^^^^^^^^^^^^^^^^^^^^^^

The ADRV9025/9026/9029 contains several internal processors that require
firmware loading during initialization.

**ARM Processor**

The transceiver is equipped with a built-in ARM M4 processor. The firmware
for this ARM processor is loaded during the initialization process. The
firmware memory size is 224 kB, and the ARM has access to another 160 kB of
data memory. The ARM is tasked with configuring the transceiver for the
selected use case, performing initial calibrations of the signal paths, and
maintaining device performance over time through tracking calibrations.

**DFE Processor**

There is a dual core embedded ARM processor in which the DPD and CLGC
algorithms reside. One of the dual core ARM processors is a control processor
(ARM-C), which is the master, and the second core is a dedicated ARM core for
DPD processing (ARM-D).

The firmware files for these processors must be stored in the ``/lib/firmware``
folder, or compiled into the kernel using the ``CONFIG_FIRMWARE_IN_KERNEL`` and
``CONFIG_EXTRA_FIRMWARE`` config options. The firmware loaded during driver
probe is specified using the following device tree property:

.. code-block:: dts

   arm-firmware-name = "ADRV9025_FW.bin;ADRV9025_DPDCORE_FW.bin";

.. list-table::
   :header-rows: 1

   * - Function
     - File
   * - ARM processor firmware
     - :git-linux:`firmware/ADRV9025_FW.bin`
   * - DFE processor firmware
     - :git-linux:`firmware/ADRV9025_DPDCORE_FW.bin`

**Stream Processor**

A stream processor within the transceiver performs a series of configuration
tasks based on events. After a request from the user, the stream processor
performs predefined actions loaded during device initialization. It executes
streams for:

- Tx1/Tx2/Tx3/Tx4 enable/disable
- Rx1/Rx2/Rx3/Rx4 enable/disable
- ORx1/ORx2/ORx3/ORx4 enable/disable

The stream binary must be stored in ``/lib/firmware`` and is specified using:

.. code-block:: dts

   stream-firmware-name = "stream_image_6E3E00EFB74FE7D465FA88A171B81B8F.bin";

**Gain Tables**

The gain tables for the RX and TX paths are also loaded during boot using the
firmware framework.

.. list-table::
   :header-rows: 1

   * - Function
     - File
   * - RX Gain Correction table
     - :git-linux:`firmware/ADRV9025_RxGainTable.csv`
   * - TX Attenuation table
     - :git-linux:`firmware/ADRV9025_TxAttenTable.csv`

Enabling Linux Driver Support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configure the kernel with ``make menuconfig`` (alternatively use
``make xconfig`` or ``make qconfig``):

.. code-block::

   Linux Kernel Configuration
       Device Drivers  --->
       <*>     Industrial I/O support --->
           --- Industrial I/O support
               *** Analog to digital converters ***
           [--snip--]
               <*> Analog Devices ADRV9025/ADRV9026/ADRV9029 RF Transceiver driver
           [--snip--]

       Frequency Synthesizers DDS/PLL  --->
               Direct Digital Synthesis  --->
                   <*> Analog Devices CoreFPGA AXI DDS driver
               Clock Generator/Distribution  --->
                   <*> Analog Devices AD9528 Low Jitter Clock Generator

       <*>   JESD204 High-Speed Serial Interface Support  --->
               <*>   Analog Devices AXI ADXCVR PHY Support
               <*>   Analog Devices AXI JESD204B TX Support
               <*>   Analog Devices AXI JESD204B RX Support

IIO Devices
~~~~~~~~~~~

The following IIO devices are enumerated on a ZCU102 system:

- **ad9528-1** -- Clock generator providing device and reference clocks
- **adrv9025-phy** -- Transceiver control (LO frequency, gain, calibrations)
- **axi-adrv9025-rx-hpc** -- Receive data path (buffer capable)
- **axi-adrv9025-tx-hpc** -- Transmit data path (buffer capable)

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
     - Observation RX1
   * - ``in_voltage5_[...]``
     - Observation RX2
   * - ``out_altvoltage0_[...]``
     - TRX LO1
   * - ``out_altvoltage1_[...]``
     - TRX LO2
   * - ``out_altvoltage2_[...]``
     - TRX AUX LO
   * - ``out_voltage0_[...]``
     - TX1
   * - ``out_voltage1_[...]``
     - TX2
   * - ``out_voltage2_[...]``
     - TX3
   * - ``out_voltage3_[...]``
     - TX4

Channel Enable/Disable Controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For use cases where pin control mode is not used, these attributes can
enable/disable the Rx/Tx signal paths while in the ENSM radio_on state:

.. code-block:: bash

   # Read channel enable state
   cat /sys/bus/iio/devices/iio:device2/in_voltage0_en
   # Disable RX1
   echo 0 > /sys/bus/iio/devices/iio:device2/in_voltage0_en

Local Oscillator Control (LO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The device contains two RF PLLs, each using a 4-core VCO block providing a
6 dB phase noise improvement over a single core VCO. The tunable range of the
RF LO is 30--6000 MHz.

.. list-table::
   :header-rows: 1

   * - Attribute
     - Port
   * - ``out_altvoltage0_LO1_frequency``
     - LO1
   * - ``out_altvoltage1_LO2_frequency``
     - LO2
   * - ``out_altvoltage2_AUX_LO_frequency``
     - AUX LO

.. code-block:: bash

   # Read LO frequency
   cat /sys/bus/iio/devices/iio:device2/out_altvoltage0_LO1_frequency
   # Set LO frequency to 3.6 GHz
   echo 3600000000 > /sys/bus/iio/devices/iio:device2/out_altvoltage0_LO1_frequency

TX Signal Path
^^^^^^^^^^^^^^^

The ADRV9026 transmitter section consists of four identical and independently
controlled channels that provide all the digital processing, mixed-signal, and
RF blocks necessary to implement a direct conversion system while sharing a
common frequency synthesizer. The digital data from the SERDES lanes pass
through a programmable digital processing block that includes half-band filters,
interpolation stages, and a programmable FIR filter with up to 80 taps.

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

The ADRV9026 provides four independent receiver channels. Each channel can be
configured as a direct conversion system supporting up to 200 MHz bandwidth.
Each channel contains a programmable attenuator stage, followed by matched I
and Q mixers that downconvert received signals to baseband for digitization.

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

The ADRV9025 driver supports advanced debug controls via the kernel debugfs.
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

.. _adrv9026-device-tree:

Device Tree Customization
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV9025 driver is configured through the device tree. Key device tree
properties for the transceiver node:

.. list-table::
   :header-rows: 1

   * - Devicetree property
     - Description
   * - ``adi,device-profile-name``
     - Device profile file
   * - ``adi,init-profile-name``
     - Initialization profile file
   * - ``adi,arm-firmware-name``
     - Firmware file for the ARM processor
   * - ``adi,stream-firmware-name``
     - Firmware file for the stream processor
   * - ``adi,rx-gaintable-names``
     - RX gain table
   * - ``adi,rx-gaintable-channel-masks``
     - Channel mask for RX gain values
   * - ``adi,tx-attntable-names``
     - TX attenuation table
   * - ``adi,tx-attntable-channel-masks``
     - Channel mask for TX attenuation values

Example ADRV9025 PHY device tree node:

.. code-block:: dts

   trx0_adrv9025: adrv9025-phy@0 {
       compatible = "adrv9025";
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
       jesd204-link-ids = <DEFRAMER0_LINK_TX FRAMER0_LINK_RX>;

       jesd204-inputs =
           <&axi_adrv9025_rx_jesd 0 FRAMER0_LINK_RX>,
           <&axi_adrv9025_core_tx 0 DEFRAMER0_LINK_TX>;

       adi,device-profile-name = "ActiveUseCase.profile";
       adi,init-profile-name = "ActiveUtilInit.profile";
       adi,arm-firmware-name = "ADRV9025_FW.bin;ADRV9025_DPDCORE_FW.bin";
       adi,stream-firmware-name = "stream_image_6E3E00EFB74FE7D465FA88A171B81B8F.bin";
       adi,rx-gaintable-names = "ADRV9025_RxGainTable.csv";
       adi,rx-gaintable-channel-masks = <0xFF>;
       adi,tx-attntable-names = "ADRV9025_TxAttenTable.csv";
       adi,tx-attntable-channel-masks = <0x0F>;
   };

GPIO configuration example:

.. code-block:: dts

   &trx0_adrv9025 {
       reset-gpios = <&gpio 135 0>;
       test-gpios = <&gpio 136 0>;
   };

.. _adrv9026-no-os:

No-OS System Level Design
--------------------------

The No-OS system level design for ADRV9026/ADRV9029 provides a bare-metal
software reference for platforms without an operating system.

- :git-no-OS:`projects/adrv902x`

Downloads
---------

The latest boot files for ADRV9026/ADRV9029 (for all supported carriers) can be
found in the latest :doc:`Kuiper Linux </linux/kuiper/index>` release.

Source code:

- :git-linux:`Linux driver <drivers/iio/adc/adrv902x>`
- :git-hdl:`HDL project <projects/adrv9026>`
- :git-no-OS:`No-OS project <projects/adrv902x>`

ADI Articles
~~~~~~~~~~~~

Four Quick Steps to Production: Using Model-Based Design for Software-Defined
Radio:

- :adi:`Part 1 -- The ADI/Xilinx SDR Rapid Prototyping Platform <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
- :adi:`Part 2 -- Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
- :adi:`Part 3 -- Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
- :adi:`Part 4 -- Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~

- `Modelling and Simulating Analog Devices' RF Transceivers with MATLAB and SimRF <https://www.mathworks.com/videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`__
- `Getting Started with Software-Defined Radio using MATLAB and Simulink <https://www.mathworks.com/videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`__

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
