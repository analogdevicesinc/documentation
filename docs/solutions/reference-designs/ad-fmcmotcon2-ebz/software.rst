Software Support
================

HDL Reference Design
--------------------

The reference design is based on the ZedBoard. It contains HDL blocks for
interfacing with the various components of the motor control hardware:

- **Current Monitor** - Implements the communication with the :adi:`AD7401`
  sigma delta modulators and SINC3 filters for demodulating the 1-bit
  digital stream. Exposes AXI Lite registers and a FIFO/DMA interface for
  streaming real-time data. An ADC PACK IP allows 1, 2, or all channels to
  stream data at a time.
- **Controller** - Implements the interface to the IP control blocks in the
  system, basic six point drive of the motor. A FIFO/DMA interface allows
  streaming real-time data. An ADC PACK block allows 1, 2, 4, or all
  channels to stream simultaneously.
- **Speed Detector** - Implements the algorithm for converting Hall, BEMF and
  Encoder signals into speed and position data
- **GMII to RGMII** - Converts the GMII interface from the two Ethernet cores
  of the PS7 block to RGMII interface available on the FMC controller board.
  The IP allows RX pins to reside on different I/O banks.
- **I2C** - Two I2C interfaces connected to the FMC board

.. image:: motorcontrolrev2.jpg
   :align: center

Vivado Design Generation
~~~~~~~~~~~~~~~~~~~~~~~~~

Build the project following the
`ADI HDL Reference Designs <https://analogdevicesinc.github.io/hdl/>`__.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`hdl_2018_r2:projects/motcon2_fmc`

Linux IIO Drivers
-----------------

The Linux Industrial I/O (IIO) drivers for the motor control solution require
the HDL cores to have a specified register map. A DMA interface is set up for
high-speed data transfer using multiple multiplexed data channels. The
FMCMOTCON2 design supports two motors simultaneously through paired drivers.

.. list-table::
   :header-rows: 1

   * - IIO Driver
     - Channel
     - Description
   * - **ad-mc-adc**
     - voltage1
     - Motor 1 Ia ADC raw data
   * -
     - voltage2
     - Motor 1 Ib ADC raw data
   * -
     - voltage3
     - Motor 1 VBus ADC raw data
   * - **ad-mc-adc-m2**
     - voltage1
     - Motor 2 Ia ADC raw data
   * -
     - voltage2
     - Motor 2 Ib ADC raw data
   * -
     - voltage3
     - Motor 2 VBus ADC raw data
   * - **ad-mc-speed**
     - voltage0
     - Motor 1 speed (counts in 10 ns units between commutations)
   * - **ad-mc-speed-m2**
     - voltage0
     - Motor 2 speed (counts in 10 ns units between commutations)
   * - **ad-mc-ctrl**
     - ---
     - Motor 1 controller (not used as capture channel)
   * - **ad-mc-ctrl-m2**
     - ---
     - Motor 2 controller (not used as capture channel)

To display speed in RPM, enable the 1/x option and multiply by 25,000,000.

Example device tree entries for the motor control IIO drivers:

.. code-block:: none

   &fpga_axi {
       ad-mc-speed@40410000 {
           compatible = "xlnx,axi-ad-mc-speed-1.00.a";
           reg = <0x40410000 0x10000>;
           dmas = <&ad_mc_speed_dma 0>;
           dma-names = "ad-mc-speed-dma";
       };
       ad_mc_speed_dma: dma@40510000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40510000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 57 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <32>;
               adi,type = <0>;
           };
       };

       ad-mc-adc@40420000 {
           compatible = "xlnx,axi-ad-mc-adc-1.00.a";
           reg = <0x40420000 0x10000>;
           dmas = <&ad_mc_adc_dma 0>;
           dma-names = "ad-mc-adc-dma";
       };
       ad_mc_adc_dma: dma@40520000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40520000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 54 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <64>;
               adi,type = <0>;
           };
       };

       ad-mc-ctrl@40430000 {
           compatible = "xlnx,axi-ad-mc-ctrl-1.00.a";
           reg = <0x40430000 0x10000>;
           dmas = <&ad_mc_ctrl_dma 0>;
           dma-names = "ad-mc-ctrl-dma";
       };
       ad_mc_ctrl_dma: dma@40530000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40530000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 53 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <256>;
               adi,type = <0>;
           };
       };

       ad-mc-speed-m2@40440000 {
           compatible = "xlnx,axi-ad-mc-speed-1.00.a";
           reg = <0x40440000 0x10000>;
           dmas = <&ad_mc_speed_dma_m2 0>;
           dma-names = "ad-mc-speed-dma";
       };
       ad_mc_speed_dma_m2: dma@40540000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40540000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 52 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <32>;
               adi,type = <0>;
           };
       };

       ad-mc-adc-m2@40450000 {
           compatible = "xlnx,axi-ad-mc-adc-1.00.a";
           reg = <0x40450000 0x10000>;
           dmas = <&ad_mc_adc_dma_m2 0>;
           dma-names = "ad-mc-adc-dma";
       };
       ad_mc_adc_dma_m2: dma@40550000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40550000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 36 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <64>;
               adi,type = <0>;
           };
       };

       ad-mc-ctrl-m2@40460000 {
           compatible = "xlnx,axi-ad-mc-ctrl-1.00.a";
           reg = <0x40460000 0x10000>;
           dmas = <&ad_mc_ctrl_dma_m2 0>;
           dma-names = "ad-mc-ctrl-dma";
       };
       ad_mc_ctrl_dma_m2: dma@40560000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40560000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 35 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <256>;
               adi,type = <0>;
           };
       };
   };

   &spi0 {
       status = "okay";
       ad2s1210@0 {
           compatible = "ad2s1210";
           reg = <0>;
           spi-cpha;
           spi-max-frequency = <1000000>;
           sample-gpios = <&gpio 86 0>;
           adi,entirely-configuration-mode-enable;
       };
   };

IIO Oscilloscope
----------------

The ADI IIO Oscilloscope application is used for monitoring and controlling the
AD-FMCMOTCON2-EBZ board when using the Linux operating system.

**Signals Monitoring**

The IIO Oscilloscope allows monitoring of current, voltage, speed, and control
signals from the system.

.. image:: mc_iio_signals.png
   :align: center

**Motor Control -- Manual Control**

This dialog allows control of both motors in manual mode by directly specifying
the PWM fill factor used to control the 3-phase inverters. Motors are driven
using a 6-step commutation algorithm.

.. image:: mc_manual_ctrl.png
   :align: center

.. list-table::
   :header-rows: 1

   * - Control
     - Description
   * - Run
     - Starts the motor
   * - Delta
     - Selects between Star and Delta commutation sequence
   * - Direction
     - Selects clockwise or counterclockwise rotation
   * - PWM
     - In manual mode, sets PWM between 50%--100%

QDESYS Motor Control IP
------------------------

`QDESYS <http://www.qdesys.com/>`__ provides the following reference designs
for the AD-FMCMOTCON2-EBZ:

- EtherCAT design showing how to do real-time motor control over the network
- A high performance Field Oriented Controller (FOC) implemented as a highly
  optimized IP core that can be integrated in the FPGA project

Support
-------

If you have any questions regarding the AD-FMCMOTCON2-EBZ feel free to ask on
the :ez:`FPGA Reference Designs Forum <fpga>`.
