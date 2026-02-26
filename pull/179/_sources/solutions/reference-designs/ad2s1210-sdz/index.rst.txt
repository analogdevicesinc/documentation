.. _ad2s1210-sdz:

EVAL-AD2S1210SDZ User Guide
============================

Introduction
------------

The :adi:`AD2S1210` is a complete monolithic resolver-to-digital converter
(RDC), offering 10-bit to 16-bit resolution in a single package. It provides
a high-resolution tracking solution for applications that require accurate
position information from resolvers, converting analog resolver signals
(sine/cosine) into a digital angle and velocity output.

The :adi:`AD2S1210` interfaces to the host processor via SPI and includes
features such as:

- Programmable resolution (10, 12, 14, or 16 bits)
- Loss of signal (LOS) and degradation of signal (DOS) fault detection
- Loss of tracking (LOT) fault detection
- Phase lock fault detection
- Integrated reference oscillator output
- Excitation frequency range from 2 kHz to 20 kHz

Applications include industrial motor control, robotics, factory automation,
and any system requiring angular position and velocity from a resolver.

Supported Devices
-----------------

- :adi:`AD2S1210`

Supported Carriers
------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
  (via SDP-FMC interposer)

Hardware
--------

Hardware Required
~~~~~~~~~~~~~~~~~

- :adi:`EVAL-AD2S1210SDZ` evaluation board
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
  Rev D or later
- SDP to FMC interposer (:adi:`EVAL-SDP-CS1Z`)
- 16 GB (or larger) Class 10 (or faster) micro-SD card
- 12 V DC, 3 A power supply
- Micro-USB cable
- Ethernet cable

Hardware Connection
~~~~~~~~~~~~~~~~~~~

The EVAL-AD2S1210SDZ connects to the ZedBoard through an SDP-FMC interposer
board. The following table describes the signal routing from the ZedBoard FMC
connector through the SDP adapter to the evaluation board.

.. list-table::
   :header-rows: 1

   * - FPGA
     - FMC Name
     - FMC Pin
     - SCH Signal Name
     - SDP (J2) Pin
     - Eval Board Signal
   * - PS SPI 0 SDI
     - FMC_LPC_LA01_CC_P
     - D08
     - CON_PAR_DATA[15]
     - 110
     - SDO
   * - PS SPI 0 SDO
     - FMC_LPC_CLK0_M2C_P
     - H04
     - CON_PAR_DATA[14]
     - 12
     - SDI
   * - PS SPI 0 CLK
     - FMC_LPC_CLK0_M2C_N
     - H05
     - CON_PAR_DATA[13]
     - 13
     - SCLK
   * - Logic low
     - FMC_LPC_LA04_N
     - H11
     - CON_PAR_CS
     - 22
     - PAR_CS_n
   * - PS SPI 0 CSn 0
     - FMC_LPC_LA09_N
     - D15
     - CON_PAR_WR
     - 100
     - PAR_WR_n
   * - PS EMIO 32 (Linux 86)
     - FMC_LPC_LA13_N
     - D18
     - CON_PAR_ADDR[0]
     - 96
     - PAR_A0
   * - PS EMIO 33 (Linux 87)
     - FMC_LPC_LA07_P
     - H13
     - CON_PAR_ADDR[1]
     - 25
     - PAR_A1
   * - PS EMIO 34 (Linux 88)
     - FMC_LPC_LA21_P
     - H25
     - CON_GPIO[0]
     - 43
     - SDP_RES_0
   * - PS EMIO 35 (Linux 89)
     - FMC_LPC_LA26_P
     - D26
     - CON_GPIO[1]
     - 78
     - SDP_RES_1
   * - PS EMIO 36 (Linux 90)
     - FMC_LPC_LA27_P
     - C26
     - CON_GPIO[3]
     - 77
     - TMR_A (SAMPLE)

SPI connections:

.. list-table::
   :header-rows: 1

   * - SPI Manager Instance
     - Alias
     - SPI Address
     - SPI Subordinate
     - CSn
   * - psu_spi_0
     - spi_fpga
     - 0xFF040000
     - AD2S1210
     - 0

GPIO signals (PS8 EMIO offset = 54):

.. list-table::
   :header-rows: 1

   * - GPIO Signal
     - GPIO
     - HDL GPIO EMIOn
   * - TMR_A (SAMPLE)
     - 90
     - 36
   * - SDP_RES_1
     - 89
     - 35
   * - SDP_RES_0
     - 88
     - 34
   * - A1
     - 87
     - 33
   * - A0
     - 86
     - 32

Quick Start
-----------

Loading the SD Card Image
~~~~~~~~~~~~~~~~~~~~~~~~~

To boot the ZedBoard and control the EVAL-AD2S1210SDZ, install ADI Kuiper Linux
on an SD card. Complete instructions, including where to download the SD card
image, how to write it to the SD card, and how to configure the system are
provided on the :doc:`Kuiper Linux page </linux/kuiper/index>`.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

Follow the configuration procedure under **Configuring the SD Card for FPGA
Projects** on the Kuiper Linux page. Copy the following files onto the boot
partition to configure the SD card:

- ``uImage`` for Zynq
- ``BOOT.BIN`` specific to the EVAL-AD2S1210SDZ + ZedBoard
- ``devicetree.dtb`` for Zynq specific to the EVAL-AD2S1210SDZ + ZedBoard

Setting Up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: zedboard.png
   :align: center

   ZedBoard top view with key connectors labeled

1. Insert the SD card into the SD card interface connector (J12) on the ZedBoard.
2. Connect the EVAL-AD2S1210SDZ board to the SDP adapter and plug it into the
   ZedBoard FMC connector.
3. Connect the USB UART (J14, Micro-USB) to your host PC.
4. Plug the Ethernet cable into the RJ45 connector (J11).
5. Plug the 12 V power supply into the power input connector (J20) — do not
   power on yet.
6. Set the ZedBoard boot mode jumpers to boot from SD card, and ensure the
   VADJ jumper is set to 3.3 V.

   .. figure:: jumpers_boot_sd_zedboard.jpg
      :align: center

      ZedBoard boot mode jumper configuration for SD card boot

7. Connect oscilloscope probes to the SMB connectors on the evaluation board.
8. Power on the ZedBoard and wait approximately 30 seconds for the DONE LED
   to turn blue.

.. warning::

   Observe proper ESD precautions when handling the evaluation board.

Software Support
----------------

Linux Driver
~~~~~~~~~~~~

The AD2S1210 is supported by a mainline Linux IIO resolver driver. The driver
was mainlined in kernel v6.7 and is backported to the v6.1 ADI tree.

- :git-linux:`drivers/iio/resolver/ad2s1210.c`
- :git-linux:`Documentation/devicetree/bindings/iio/resolver/adi,ad2s1210.yaml`

Device Tree
~~~~~~~~~~~

The ZedBoard device tree for the EVAL-AD2S1210SDZ is available at:

- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad2s1210.dts`

Example device tree snippet for the AD2S1210 SPI node:

.. code-block:: none

   &spi0 {
       status = "okay";

       ad2s1210@0 {
           compatible = "adi,ad2s1210";
           reg = <0>;
           spi-cpha;
           spi-max-frequency = <20000000>;
           clocks = <&ad2s1210_clkin>;
           sample-gpios = <&gpio0 90 GPIO_ACTIVE_LOW>;
           mode-gpios = <&gpio0 87 0>, <&gpio0 86 0>;
           resolution-gpios = <&gpio0 89 0>, <&gpio0 88 0>;
           assigned-resolution-bits = <16>;
           avdd-supply = <&ad2s1210_avdd>;
           dvdd-supply = <&ad2s1210_dvdd>;
           vdrive-supply = <&ad2s1210_dvdd>;
       };
   };

Kernel Configuration
~~~~~~~~~~~~~~~~~~~~

Enable the driver via ``make menuconfig``:

.. code-block:: none

   Device Drivers --->
       <*> Industrial I/O support --->
           Resolver to digital converters --->
               <*> Analog Devices AD2S1210 driver

The driver depends on ``CONFIG_SPI``.

IIO ABI (Register Mapping)
~~~~~~~~~~~~~~~~~~~~~~~~~~

The driver exposes the following IIO attributes:

.. list-table::
   :header-rows: 1

   * - Register
     - Addr
     - IIO ABI (sysfs)
     - Units
   * - DOS Overrange Threshold
     - 0x89
     - events/in_altvoltage0_thresh_rising_value
     - mV
   * - DOS Mismatch Threshold
     - 0x8A
     - events/in_altvoltage0_mag_rising_value
     - mV
   * - DOS Reset Maximum Threshold
     - 0x8B
     - events/in_altvoltage0_mag_rising_reset_max
     - mV
   * - DOS Reset Minimum Threshold
     - 0x8C
     - events/in_altvoltage0_mag_rising_reset_min
     - mV
   * - LOT High Threshold
     - 0x8D
     - events/in_angl1_thresh_rising_value
     - Radians
   * - LOT Low Threshold
     - 0x8E
     - events/in_angl1_thresh_rising_hysteresis
     - Radians
   * - Excitation Frequency
     - 0x91
     - out_altvoltage0_frequency
     - Hz
   * - Phase lock range
     - D5
     - events/in_phase0_mag_rising_value
     - Radians
   * - Hysteresis
     - D4
     - in_angl0_hysteresis
     -
   * - Resolution
     - D1:0
     - (device tree: assigned-resolution-bits)
     - Bits

IIO Oscilloscope
~~~~~~~~~~~~~~~~

The IIO Oscilloscope application can be used to visualize and interact with
the AD2S1210 channels. Download the latest version from the
`IIO Oscilloscope releases page <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`__.

After installation, open the application, supply the target URI, press
**Refresh** to display available IIO devices, and press **Connect**.

.. figure:: iio_connect.png
   :align: center

   IIO Oscilloscope connection dialog

More Information
----------------

- :adi:`AD2S1210 Product Page <AD2S1210>`
- :adi:`EVAL-AD2S1210SDZ Evaluation Board <EVAL-AD2S1210SDZ>`
- :dokuwiki:`AD2S1210 Linux IIO Driver <resources/tools-software/linux-drivers/iio-resolver/ad2s1210>`
- `IIO subsystem documentation <https://www.kernel.org/doc/html/latest/driver-api/iio/index.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`Linux Software Drivers <linux-software-drivers>` sub-community.
