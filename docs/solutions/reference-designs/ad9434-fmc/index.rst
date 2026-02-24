.. _ad9434-fmc:

AD9434-FMC User Guide
=====================

Introduction
------------

The :adi:`AD9434` is a 12-bit monolithic sampling analog-to-digital converter
(ADC) optimized for high performance, low power, and ease of use. The part
operates at up to 500 MSPS conversion rate and is optimized for outstanding
dynamic performance in wideband carrier and broadband systems. All necessary
functions, including a sample-and-hold and voltage reference, are included on
the chip to provide a complete signal conversion solution.

This reference design includes a data capture interface and the external
DDR-DRAM interface for sample storage. It allows programming the device and
monitoring its internal status registers. The board also provides options to
drive the clock and analog inputs of the ADC.

The LVDS interface captures and buffers data from the ADC using ISERDES
primitives, capturing 4 samples wide at 1/4th of the ADC clock (125 MHz at
500 MHz ADC clock). The DMA interface then transfers the samples to the
external DDR-DRAM.

Features
~~~~~~~~

- Full featured evaluation board for the :adi:`AD9434`
- SPI interface for setup and control
- External, on-board oscillator, and :adi:`AD9517-4` clocking options
- Balun/transformer or amplifier input drive option
- LDO regulator or switching power supply options
- VisualAnalog and SPI Controller software interfaces

Supported Devices
-----------------

- :adi:`AD9434`

Supported Carriers
------------------

- :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>` LPC Slot
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
  LPC Slot

HDL Reference Design
--------------------

Block Diagram
~~~~~~~~~~~~~

.. figure:: ad9434_fmc_bd.svg
   :align: center

   AD9434-FMC block diagram

CPU/Memory Interconnects
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Instance
     - Zynq Address
   * - axi_ad9434
     - 0x44A0_0000
   * - axi_ad9434_dma
     - 0x44A3_0000

SPI Connections
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - SPI Type
     - SPI Manager Instance
     - SPI Subordinate
     - CSB
   * - PS
     - SPI 0
     - AD9517
     - 1
   * - PS
     - SPI 0
     - AD9434BCPZ
     - 0

Interrupts
~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Instance Name
     - HDL
     - Linux Zynq
     - Actual Zynq
   * - axi_ad9434_dma
     - 13
     - 57
     - 89

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad9434_fmc`

Software Support
----------------

Linux Driver
~~~~~~~~~~~~

The AD9434 is supported by the AD9467 family Linux IIO driver.

Driver and device tree source files:

- :git-linux:`drivers/iio/adc/ad9467.c`
- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zc706-adv7511-ad9434-fmc-500ebz.dts`
- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad9434-fmc-500ebz.dts`

Evaluating the AD9434 (SDP-H1)
-------------------------------

Equipment Needed
~~~~~~~~~~~~~~~~

- :adi:`AD9434` (AD9434-FMC-500EBZ) evaluation board
- :adi:`EVAL-SDP-CH1Z <SDP-H1>` (SDP-H1) data capture board
- Analog signal source (preferably Rohde & Schwarz SMA 100A signal generator)
- Antialiasing filter (narrow-band band-pass filter with 50 Ohm terminations)
- Sample clock source (if not using the on-board oscillator)
- 12 V power supply
- 1 m SMA cable
- USB Mini-B cable
- PC running Windows

Software Needed
~~~~~~~~~~~~~~~

- `VisualAnalog <https://www.analog.com/en/design-center/interactive-design-tools/visualanalog.html>`__
- `SPI Controller <https://www.analog.com/en/design-center/interactive-design-tools/spicontroller.html>`__

Typical Measurement Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ad9434_fmc_500ebz_typical_setup.jpg
   :align: center

   Evaluation board connection -- AD9434-FMC-500EBZ (left) and
   EVAL-SDP-CH1Z SDP-H1 (right)

Configuring the Board
~~~~~~~~~~~~~~~~~~~~~

Before using the software for testing, configure the evaluation board
as follows:

1. Connect the AD9434-FMC-500EBZ evaluation board to the SDP-H1 data capture
   board as shown in the figure above.
2. Connect one 12 V switching power supply to the SDP-H1 board.
3. Connect the SDP-H1 board to the PC with a USB cable (connector J1).
4. To use the on-board clock, short pins 1 and 2 on header P1.
5. On the ADC evaluation board, use a clean signal generator with low phase
   noise to provide an input signal to the input channel (J100). Use a 1 m,
   shielded, RG-58, 50 Ohm coaxial cable to connect the signal generator.
   For best results, use a narrow-band band-pass filter with 50 Ohm
   terminations and an appropriate center frequency.
6. If using an external clock signal, remove the jumper on P1 and connect
   a clean signal generator to J201.

Setting Up the ADC Data Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After configuring the board, set up the ADC data capture using VisualAnalog:

1. Start **VisualAnalog**.
2. Select **AD9434** and double-click **FFT** to create a new canvas.
3. Click **Settings** under the **ADC Data Capture** block.
4. Set the device to **Default** in the General tab.
5. Navigate to the **Capture Board** tab and browse for the FPGA image file
   (``ad9434_sdph1.bin``).
6. Click **Program** and verify that LED0 on the SDP-H1 lights up, then
   click **OK**.

Setting Up the SPI Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Start **SPIController**.
2. If a **Read Test Failure** message appears, select **Ignore**.
3. Click **File > Cfg Open** and load the file
   ``ad9434_12bit_500MSspiR03.cfg``.
4. If another **Read Test Failure** message appears, select **Ignore** again.
5. Click **Config > Controller Dialog**.
6. Uncheck **SDO Active** and click **OK**.
7. Click **Read Chip ID** and **Read Chip Grade** to verify the SPI
   communication.

Obtaining an FFT
~~~~~~~~~~~~~~~~

1. Go back to **VisualAnalog** and click the **Play** button.
2. Adjust the amplitude of the input signal so that the fundamental is at
   approximately **-1.0 dBFS**. Verify by examining the **Fund Power** reading
   in the left panel of the **VisualAnalog Graph -- AD9434 Average FFT**
   window.
3. Click the disk icon within the **Graph** window to save the performance
   data as a ``.csv`` file.

.. figure:: ad9434_typical_fft.png
   :align: center

   AD9434-FMC-500EBZ typical FFT capture

Clock Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD9434-FMC-500EBZ board supports several clock configurations: external
signal generator, on-board oscillator (CCS575S Crystek SAW clock oscillator),
LVPECL, and LVDS. The LVPECL and LVDS options use the :adi:`AD9517-4` as
a clock buffer with its internal VCO in clock distribution mode.

.. figure:: ad9434_clock_setup.png
   :align: center

   AD9434 clocking setup

.. figure:: ad9434_snr_performance.png
   :align: center

   AD9434 SNR performance using different clock configurations

The external signal generator provides the best SNR performance due to having
the lowest clock jitter. The CCS575S oscillator ranks second, followed by
LVPECL (960 mVpp swing) and LVDS (3.5 mA current setting). As a trade-off,
the external signal generator has higher material cost and resource
requirements, while the :adi:`AD9517-4` configurations offer the lowest
cost with slightly reduced performance.

.. list-table:: Component changes for different clock configurations
   :header-rows: 1

   * - Clock Configuration
     - Install
     - Uninstall
   * - External Signal Generator
     - As shipped
     - As shipped
   * - Oscillator
     - R209, P1 (shunt)
     - None
   * - LVPECL
     - R208, R307, R308, C300, C311, C304, C305
     - C209, C210
   * - LVDS
     - R208, C306, C307
     - C209, C210, R311

For LVPECL and LVDS configurations, appropriate charge pump filter circuit
values are necessary for optimized clock buffer performance from the
:adi:`AD9517-4`. Simulate the :adi:`AD9517-4` using
`ADIsimCLK <https://www.analog.com/en/design-center/adisimclk.html>`__
to determine the appropriate values.

Using SPIController for AD9517-4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After configuring SPIController for AD9434 using FIFO Select 1, a second
instance of SPIController is needed for the :adi:`AD9517-4`:

1. Start another **SPIController** instance.
2. If a **Read Test Failure** message appears, select **Ignore**.
3. Click **File > Cfg Open** and load the file ``AD9517spiR03.cfg``.
4. If another **Read Test Failure** message appears, select **Ignore** again.
5. Click **Config > Controller Dialog**.
6. Set **FIFO Chip Sel#** to **2**, uncheck **SDO Active**, then click **OK**.
7. Go to the **Global** tab and click **Reset**.
8. Configure the **PLL** tab to the desired settings.
9. In the **Output** tab, configure either LVPECL or LVDS:

   - **LVPECL**: configure **Output3 LVPECL (0x0F5)**, set the differential
     voltage swing and power mode to **Normal Operation**. Set the remaining
     LVPECL outputs to **Safe LVPECL power-down** and power down all LVDS
     outputs.
   - **LVDS**: configure **Output5 (0x141)**, uncheck **Power-down Output**,
     set output polarity to **CMOS = A, CMOS B = N, LVDS = N** and LVDS
     output current level to **3.5 mA at 100 Ohms**. Set all LVPECL outputs
     to **Safe LVPECL power-down**.

10. Configure the desired divider settings (LVPECL or LVDS divider).
11. For internal VCO mode, set the **VCO divider** to the desired value and
    set **Input to VCO divider** to **VCO**.
12. Go back to the **PLL** tab (**PLL CTRL 3 (0x18)**) and click
    **VCO Cal Now**.
13. Click **Update DUT from Controller** and wait for LED CR300 to illuminate.
    Insert a REFCLK at J201 for the PLL in the :adi:`AD9517-4` to lock.
14. Go back to **VisualAnalog** and verify that an FFT can be produced using
    the configured clock source.

Troubleshooting
~~~~~~~~~~~~~~~

**FFT plot appears abnormal:**

- If a normal noise floor is visible when the signal generator is disconnected,
  the ADC may be overdriven. Reduce the input level.
- In **VisualAnalog**, click **Settings** in the **Input Formatter** block and
  verify that **Number Format** is set to the correct encoding (offset binary
  by default).

**FFT appears normal but performance is poor:**

- Verify that an appropriate band-pass filter is used on the analog input.
- Verify that the signal generators for clock and analog input are clean
  (low phase noise).
- Change the analog input frequency slightly if non-coherent sampling is used,
  or use coherent frequencies.
- Verify that the SPI configuration file matches the product being evaluated.
- Ensure there is no extra stress or torque on the clock and analog input
  connectors.

**FFT window remains blank after clicking Run:**

- Verify that the evaluation board is securely connected to the SDP-H1 board.
- Verify that the FPGA has been programmed by checking that the **FPGA_DONE**
  LED is illuminated on the SDP-H1 board. If not, reprogram the FPGA through
  VisualAnalog. If the LED still does not illuminate, disconnect the USB and
  power cord for 15 seconds, reconnect, and repeat the setup process.
- Verify the correct FPGA bin file was used.
- Verify that the correct sample rate is configured. Click **Settings** in the
  **ADC Data Capture** block and check the **Clock Frequency** setting.
- Ensure that the ADC has a valid clock input.

**Analog input frequency does not match in VisualAnalog:**

- Check the clock frequency at the ADC and ensure it matches the **Clock
  Frequency** setting in the ADC Data Capture block.
- For LVPECL and LVDS configurations using the :adi:`AD9517-4`, reset the
  board and redo the SPIController settings.

Evaluating the AD9434 (FPGA)
----------------------------

The AD9434-FMC-500EBZ can also be evaluated using an FPGA carrier board
running Linux with IIO Oscilloscope.

Equipment Needed
~~~~~~~~~~~~~~~~

- :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>` or
  `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
- AD9434-FMC-500EBZ board (the default setup uses the on-board clock)
- SD card (at least 16 GB) with
  `ADI Kuiper Linux <https://analogdevicesinc.github.io/wiki/software/linux/kuiper_linux/>`__
- Signal generator (for data)
- 1 x SMA cable
- 1 x Ethernet cable
- A UART terminal (Tera Term or similar), baud rate 115200

Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~

**ZC706:** Set the SW11 boot switch to **0110** (left to right) to boot from
the SD card. Set VADJ to **2.5 V**.

**ZedBoard:** Place the VADJ jumper on **2.5 V**.

Configure the AD9434-FMC-500EBZ board jumpers:

- **P100**: Pins 1 and 2 (selects the internal oscillator clock source)
- **J300**: Pins 3 and 4 (PD and AGND)
- **P400**: Pins 5 and 6
- **P300**: No configuration required

Quick Start
~~~~~~~~~~~

1. Connect the AD9434-FMC board to the FMC-LPC connector of the carrier
   board.
2. Connect the power source, Ethernet cable, and USB cable for UART
   communication.
3. Program the SD card with the latest
   `ADI Kuiper Linux <https://analogdevicesinc.github.io/wiki/software/linux/kuiper_linux/>`__
   image. Copy the appropriate **BOOT.BIN** and **devicetree.dtb** files to the
   boot partition.
4. Insert the SD card and power on the carrier board.
5. After the system boots, find the IP address from the UART console.
6. Open **IIO Oscilloscope** and choose manual connection. Enter
   ``ip:<your_ip_address>`` and click **Refresh**.
7. Click **File > New Plot** to create a new plot. Connect a signal generator
   to the analog input and verify the captured signal.

.. figure:: ad9434_zc706_setup.png
   :align: center

   AD9434-FMC with ZC706 setup

.. figure:: ad9434_zc706_10mhz_1000samples.png
   :align: center

   IIO Oscilloscope capture: 10 MHz input, 1000 samples

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- :adi:`AD9434 Product Page <AD9434>`
- :adi:`AD9517-4 Product Page <AD9517-4>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
