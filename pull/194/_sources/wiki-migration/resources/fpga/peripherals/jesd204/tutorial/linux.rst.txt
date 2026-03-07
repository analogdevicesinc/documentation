Linux
=====

The JESD204 Interface Framework provides out of the box linux support for many of the ADI JESD204 based converters, clock chips and both Xilinx and Altera FPGA transceivers.

.. include:: ../../jesd204.rst

Kernel Configuration
--------------------

The first requirement for the JESD204 drivers to be supported by Linux is that they are compiled either as part of the kernel or as a kernel module. We recommend using them integrated in the kernel.

The physical layer support, implementing the reconfiguration of the FPGA transceiver for both Xilinx and Intel/Altera:

::

       Device Drivers  --->
       <*>     Industrial I/O support --->
           --- Industrial I/O support
           -*-   Enable ring buffer support within IIO
           -*-     Industrial I/O lock free software ring
           -*-   Enable triggered sampling support
               <*>   JESD204 High-Speed Serial Interface Support  --->
               [--snip--]
               <*>   Altera Arria10 JESD204 PHY Support
               <*>   Analog Devices AXI ADXCVR PHY Support
               <*>   Generic AXI JESD204B configuration driver
           [--snip--]

The data link layer support, implementing reconfiguration of JESD204 specific parameters. This applies for both Xilinx and Intel/Altera designs:

::

       Device Drivers  --->
       <*>     Industrial I/O support --->
           --- Industrial I/O support
           -*-   Enable ring buffer support within IIO
           -*-     Industrial I/O lock free software ring
           -*-   Enable triggered sampling support
           <*>   JESD204 High-Speed Serial Interface Support  --->
           [--snip--]
               <*>   Analog Devices AXI JESD204B RX Support
               <*>   Analog Devices AXI JESD204B TX Support
           [--snip--]

Transport layer support, implementing ADC/DAC chip configuration and HDL IP configuration:

.. code:: tcl

       Device Drivers  --->
       <*>     Industrial I/O support --->
           --- Industrial I/O support
           -*-   Enable ring buffer support within IIO
           -*-     Industrial I/O lock free software ring
           -*-   Enable triggered sampling support
           [--snip--]
           <*>   Analog Devices AD9467 AD9643 High-Speed AXI ADC driver
           [--snip--]

           *** Direct Digital Synthesis ***
           <*>   Analog Devices CoreFPGA AXI DDS driver
           <*>   Analog Devices AD9122 DAC
           [--snip--]

Clock device support:

.. code:: tcl

       Device Drivers  --->
       <*>  Industrial I/O support --->
                Frequency Synthesizers DDS/PLL  ---> 
                    Clock Generator/Distribution  --->
                    <*>  Analog Devices AD9528 Low Jitter Clock Generator

Devicetree Configuration
------------------------

After enabling the drivers in the kernel, the devicetree needs to be created and configured.

The devicetree is a description of the system hardware components that can be found both inside the FPGA, like the the JESD204 PHY, link and transport layer cores, as well as outside on the PCB like the JESD204 ADC or DAC and the clockchips.

The description in the devicetree is loaded by the operating system and is used to configure the device drivers at system boot time.

For more information about devicetree visit `devicetree.org <http://devicetree.org>`_.

Physical Layer
~~~~~~~~~~~~~~

Initially, the physical layer needs to be configured. The parameters depend on the HDL implementation and what clock is used as device clock.

| Required properties:
| **compatible**: Must always be “adi,axi-adxcvr-1.00”
| **reg**: Base address and register area size. This parameter expects a register range
| **clock-names**: List of input clock names - “s_axi_aclk”, “device_clk”
| **clocks**: Clock phandles and specifiers (See clock bindings for details on clock-names and clocks)
| **clock-output-names**: Generated clocks
| **adi,sys-clk-select**: 2 bit variable. For ultrascale, it selects the PLL reference clock source to be forwarded to the OUTCLK MUX: 0-CPLL, 3-QPLL0. Check RX/TXSYSCLKSEL parameter in the transceiver documentation for the FPGA you're using
| **adi,out-clk-select**: 3 bit variable. Controls the OUTCLKSEL multiplexer, controlling what will be forwarded to OUTCLK pin. Check RX/TXOUTCLKSEL parameter in the transceiver documentation for the FPGA you're using
| Optional properties:
| **adi,use-lpm-enable**: If set, the transceiver will be used in LPM mode. Otherwise, will be used in DFE mode. See transceiver documentation for details
| **adi,use-cpll-enable**: If set, the CPLL will be used for these transceivers

.. code:: tcl

   axi_ad9680_adxcvr: axi-ad9680-adxcvr@44a50000 {
       compatible = "adi,axi-adxcvr-1.0";
       reg = <0x44a50000 0x1000>;

       clocks = <&clk0_ad9523 4>;
       clock-names = "conv";

       #clock-cells = <1>;
       clock-output-names = "adc_gt_clk", "rx_out_clk";

       adi,sys-clk-select = <0>;
       adi,out-clk-select = <4>;
       adi,use-lpm-enable;
       adi,use-cpll-enable;
   };

   axi_ad9144_adxcvr: axi-ad9144-adxcvr@44a60000 {
       compatible = "adi,axi-adxcvr-1.0";
       reg = <0x44a60000 0x1000>;

       clocks = <&clk0_ad9523 9>;
       clock-names = "conv";

       #clock-cells = <1>;
       clock-output-names = "dac_gt_clk", "tx_out_clk";

       adi,sys-clk-select = <3>;
       adi,out-clk-select = <4>;
       adi,use-lpm-enable;
   };

Data Link Layer
~~~~~~~~~~~~~~~

| Required properties:
| **compatible**: Must always be “adi,axi-jesd204b-tx-1.00.a” or “adi,axi-jesd204b-tx-1.00.a”
| **reg**: Base address and register area size. This parameter expects a register range
| **interrupts**: Property with a value describing the interrupt number
| **clock-names**: List of input clock names - “s_axi_aclk”, “device_clk”
| **clocks**: Clock phandles and specifiers (See clock bindings for details on clock-names and clocks)
| **adi,frames-per-multiframe**: Number of frames per multi-frame (K)
| **adi,octets-per-frame**: Number of octets per frame (F)
| Optional properties:
| **adi,converter-resolution**: Converter resolution (N)
| **adi,bits-per-sample**: Number of bits per sample (N')
| **adi,high-density**: If specified the JESD204B link is configured for high density (HD) operation

.. code:: tcl

   axi_ad9144_jesd: axi-jesd204-tx@44a90000 {
       compatible = "adi,axi-jesd204-tx-1.0";
       reg = <0x44a90000 0x1000>;
       interrupts = <0 54 0>;
       clocks = <&clkc 16>, <&axi_ad9144_adxcvr 1>, <&axi_ad9144_adxcvr 0>;
       clock-names = "s_axi_aclk", "device_clk", "lane_clk";
       adi,octets-per-frame = <1>;
       adi,frames-per-multiframe = <32>;
       adi,converter-resolution = <16>;
       adi,bits-per-sample = <16>;
       adi,converters-per-device = <2>;
       #clock-cells = <0>;
       clock-output-names = "jesd_dac_lane_clk";
   };

   axi_ad9680_jesd: axi-jesd204-rx@00040000 {
       compatible = "adi,axi-jesd204-rx-1.0";
       reg = <0x00040000 0x4000>;
       interrupt-parent = <&intc>;
       interrupts = <0 27 0>;
       clocks = <&sys_clk>, <&rx_device_clk_pll>, <&axi_ad9680_xcvr>;
       clock-names = "s_axi_aclk", "device_clk", "lane_clk";
       adi,octets-per-frame = <1>;
       adi,frames-per-multiframe = <32>;
       clock-output-names = "jesd_adc_lane_clk";
   };

Transport Layer
~~~~~~~~~~~~~~~

when instantiating the transport layer, a DMA IP should also be instantiated for both the RX and TX path.

.. code:: tcl

   axi_ad9680_core: axi-ad9680-hpc@44a10000 {
       compatible = "adi,axi-ad9680-1.0";
       reg = <0x44a10000 0x10000>;
       dmas = <&rx_dma 0>;
       dma-names = "rx";
       spibus-connected = <&adc0_ad9680>;
   };

   axi_ad9144_core: axi-ad9144-hpc@44a04000 {
       compatible = "adi,axi-ad9144-1.0";
       reg = <0x44a04000 0x4000>;
       dmas = <&tx_dma 0>;
       dma-names = "tx";
       spibus-connected = <&dac0_ad9144>;
       adi,axi-pl-fifo-enable;
   };

   rx_dma: rx-dmac@7c400000 {
       compatible = "adi,axi-dmac-1.00.a";
       reg = <0x7c400000 0x10000>;
       #dma-cells = <1>;
       interrupts = <0 57 0>;
       clocks = <&clkc 16>;
       
       dma-channel {
           adi,source-bus-width = <64>;
           adi,destination-bus-width = <64>;
           adi,type = <0>;
       };
   };

   tx_dma: tx-dmac@7c420000 {
       compatible = "adi,axi-dmac-1.00.a";
       reg = <0x7c420000 0x10000>;
       #dma-cells = <1>;
       interrupts = <0 56 0>;
       clocks = <&clkc 16>;
       
       dma-channel {
           adi,source-bus-width = <128>;
           adi,destination-bus-width = <128>;
           adi,type = <1>;
           adi,cyclic;
       };
   };

Device Drivers
~~~~~~~~~~~~~~

Here we instantiate the device drivers, which will configure the actual ADC, DAC and clock generating chips.

Clock chip
^^^^^^^^^^

Depending on the schematic and available reference clock, the boot configuration should be done in the device-tree. Depending on the schematic, each output may have different functions. This configuration can be modified at runtime.

.. code:: tcl

       clk0_ad9523: ad9523-1@0 {
           #address-cells = <1>;
           #size-cells = <0>;
           #clock-cells = <1>;
           compatible = "adi,ad9523-1";
           reg = <0>;

           spi-max-frequency = <10000000>;
           clock-output-names = "ad9523-1_out0", "ad9523-1_out1", "ad9523-1_out2", "ad9523-1_out3", "ad9523-1_out4", "ad9523-1_out5", "ad9523-1_out6", "ad9523-1_out7", "ad9523-1_out8", "ad9523-1_out9", "ad9523-1_out10", "ad9523-1_out11", "ad9523-1_out12", "ad9523-1_out13";
           adi,vcxo-freq = <125000000>;
           adi,spi-3wire-enable;
           adi,pll1-bypass-enable;
           adi,osc-in-diff-enable;

           adi,pll2-charge-pump-current-nA = <413000>;

           /*
     * Valid ranges based on VCO locking range:
     *    980.00 MHz - 1033.33 MHz
     *    735.00 MHz -  775.00 MHz
     *    588.00 MHz -  620.00 MHz
            */
           adi,pll2-m1-freq = <1000000000>;

           /* Manual PLL2 divider configuration */
   //      adi,pll2-r2-div = <1>;
   //      adi,pll2-vco-div-m1 = <3>;
   //      adi,pll2-ndiv-a-cnt = <0>; /* a = N % 4 */
   //      adi,pll2-ndiv-b-cnt = <6>; /* b = N / 4 */

           adi,rpole2 = <0>;
           adi,rzero = <7>;
           adi,cpole1 = <2>;

           ad9523_0_c1:channel@1 {
               reg = <1>;
               adi,extended-name = "DAC_CLK";
               adi,driver-mode = <3>;
               adi,divider-phase = <1>;
               adi,channel-divider = <1>;
   //          adi,output-dis;
           };
           ad9523_0_c4:channel@4 {
               reg = <4>;
               adi,extended-name = "ADC_CLK_FMC";
               adi,driver-mode = <3>;
               adi,divider-phase = <1>;
               adi,channel-divider = <2>;
   //          adi,output-dis;
           };

           ad9523_0_c5:channel@5 {
               reg = <5>;
               adi,extended-name = "ADC_SYSREF";
               adi,driver-mode = <3>;
               adi,divider-phase = <1>;
               adi,channel-divider = <128>;
   //          adi,output-dis;
           };

           ad9523_0_c6:channel@6 {
               reg = <6>;
               adi,extended-name = "CLKD_ADC_SYSREF";
               adi,driver-mode = <3>;
               adi,divider-phase = <1>;
               adi,channel-divider = <128>;
   //          adi,output-dis;
           };

           ad9523_0_c7:channel@7 {
               reg = <7>;
               adi,extended-name = "CLKD_DAC_SYSREF";
               adi,driver-mode = <3>;
               adi,divider-phase = <1>;
               adi,channel-divider = <128>;
   //          adi,output-dis;
           };

           ad9523_0_c8:channel@8 {
               reg = <8>;
               adi,extended-name = "DAC_SYSREF";
               adi,driver-mode = <3>;
               adi,divider-phase = <1>;
               adi,channel-divider = <128>;
   //          adi,output-dis;
           };

           ad9523_0_c9:channel@9 {
               reg = <9>;
               adi,extended-name = "FMC_DAC_REF_CLK";
               adi,driver-mode = <3>;
               adi,divider-phase = <1>;
               adi,channel-divider = <2>;
   //          adi,output-dis;
           };

           ad9523_0_c13:channel@13 {
               reg = <13>;
               adi,extended-name = "ADC_CLK";
               adi,driver-mode = <3>;
               adi,divider-phase = <1>;
               adi,channel-divider = <1>;
   //          adi,output-dis;
           };
       };

DAC AD9144 chip
^^^^^^^^^^^^^^^

Instantiation the AD9144 chip, noting which clocks are connected to the chip.

.. code:: tcl

   dac0_ad9144: ad9144@1 {
       compatible = "adi,ad9144";
       reg = <1>;
       
       spi-max-frequency = <1000000>;
       
       clocks = <&axi_ad9144_jesd>, <&clk0_ad9523 1>, <&clk0_ad9523 8>;
       clock-names = "jesd_dac_clk", "dac_clk", "dac_sysref";
   };

ADC AD9680 chip
^^^^^^^^^^^^^^^

Instantiating the AD9680 chip, noting which clocks are connected to the chip.

.. code:: tcl

   adc0_ad9680: ad9680@2 {
       compatible = "adi,ad9680";
       reg = <2>;
       
       spi-max-frequency = <1000000>;
       
       clocks = <&axi_ad9680_jesd>, <&clk0_ad9523 13>, <&clk0_ad9523 5>;
       clock-names = "jesd_adc_clk", "adc_clk", "adc_sysref";
   };

Building the Linux Kernel and Device-tree
-----------------------------------------

For this tutorial we will use an ADI provided script.

We provide a script `for Zynq <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/linux/build_zynq_kernel_image.sh>`_ and one `for Zynqmp <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/linux/build_zynqmp_kernel_image.sh>`_ that do automate the build using the Linaro toolchain.

The script takes 3 parameters:

-  **<local_kernel_dir>** - default is **linux-adi** if left blank ; use this, if you want to use an already cloned kernel repo
-  **<devicetree_file>** - which device-tree should be exported/copied from the build
-  **<path_to_other_toolchain>** - in case you have your own preferred ARM64 toolchain [other than Linaro's or Xilinx's] you can use override it with this 3rd param

The script will:

-  clone the ADI kernel tree
-  download the Linaro GCC toolchain [if no other is specified]
-  build the ADI kernel tree
-  export/copy the Image file and device-tree file out of the kernel build folder

::

   wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/linux/build_zynq_kernel_image.sh && chmod +x build_zynq_kernel_image.sh && ./build_zynq_kernel_image.sh

Build the device-tree:

.. code:: tcl

   ~/github-linux-build/linux$  make xilinx/zynqmp-zcu102-rev10-fmcdaq2.dtb

Booting Linux on ZCU102
-----------------------

In order for linux to boot, you need to start from a clean ADI :doc:`Linux image </wiki-migration/resources/tools-software/linux-software/zynq_images>`. After that, you need to copy the newly generated files. Assuming the SD card BOOT partition was mounted in /media/BOOT:

::

   ~/github-linux-build/linux$ cp arch/arm64/boot/Image /media/BOOT/
   ~/github-linux-build/linux$ cp arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-fmcdaq2.dtb /media/BOOT/system.dtb

If a new ``BOOT.BIN`` file has been generated, it should also be copied in the root directory of the SD card.

Booting Linux on A10SOC
-----------------------

Status Registers
----------------

The JESD204B Interface framework provides several status functions for both TX and RX.

axi-jesd204-tx
~~~~~~~~~~~~~~

.. code:: tcl

   Status:
       Link is enabled
       Measured Link Clock: 250.002 MHz
       Reported Link Clock: 250.000 MHz
       Lane rate: 10000.000 MHz
       Lane rate / 40: 250.000 MHz
       SYNC~: deasserted
       Link status: DATA
       SYSREF captured: Yes
       SYSREF alignment error: No

axi-jesd204-rx
~~~~~~~~~~~~~~

.. code:: tcl

   Status:
       Link is enabled
       Measured Link Clock: 250.000 MHz Reported Link Clock: 250.000 MHz
       Lane rate: 10000.000 MHz
       Lane rate / 40: 250.000 MHz
       Link status: DATA
       SYSREF captured: Yes
       SYSREF alignment error: No

.. code:: tcl

   Lane Info:
       CGS state: DATA
       Initial Frame Synchronization: Yes
       Lane Latency: 3 Multi-frames and 15 Octets
       Initial Lane Alignment Sequence: Yes
       DID: 0, BID: 1, LID: 0, L: 3, SCR: 1, F: 0
       K: 31, M: 1, N: 13, CS: 0, N': 15, S: 0, HD: 1
       FCHK: 0x80, CF: 0
       ADJCNT: 0, PHADJ: 0, ADJDIR: 0, JESDV: 1, SUBCLASS: 1
       FC: 10000000
       CGS state: DATA
       Initial Frame Synchronization: Yes
       Lane Latency: 3 Multi-frames and 16 Octets
       Initial Lane Alignment Sequence: Yes
       DID: 0, BID: 1, LID: 1, L: 3, SCR: 1, F: 0
       K: 31, M: 1, N: 13, CS: 0, N': 15, S: 0, HD: 1
       FCHK: 0x81, CF: 0
       ADJCNT: 0, PHADJ: 0, ADJDIR: 0, JESDV: 1, SUBCLASS: 1
       FC: 10000000
       CGS state: DATA Initial Frame Synchronization: Yes
       Lane Latency: 3 Multi-frames and 14 Octets
       Initial Lane Alignment Sequence: Yes
       DID: 0, BID: 1, LID: 2, L: 3, SCR: 1, F: 0
       K: 31, M: 1, N: 13, CS: 0, N': 15, S: 0, HD: 1
       FCHK: 0x82, CF: 0
       ADJCNT: 0, PHADJ: 0, ADJDIR: 0, JESDV: 1, SUBCLASS: 1
       FC: 10000000
       CGS state: DATA
       Initial Frame Synchronization: Yes
       Lane Latency: 3 Multi-frames and 15 Octets
       Initial Lane Alignment Sequence: Yes
       DID: 0, BID: 1, LID: 3, L: 3, SCR: 1, F: 0
       K: 31, M: 1, N: 13, CS: 0, N': 15, S: 0, HD: 1
       FCHK: 0x83, CF: 0
       ADJCNT: 0, PHADJ: 0, ADJDIR: 0, JESDV: 1, SUBCLASS: 1
       FC: 10000000

Applications
------------

The easiest way to reconfigure application parameters like sampling rate and capturing data is by using :doc:`IIO Oscilloscope </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/iio_scope>`

The second option is to use :doc:`libiio </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/libiio>` library.

References
----------

| https:*wiki.analog.com/resources/tools-software/linux-build/generic/zynq
  https:*\ wiki.analog.com/resources/tools-software/linux-build/generic/zynqmp
| https:*wiki.analog.com/resources/tools-software/linux-software/altera_soc_images
  https:*\ wiki.analog.com/resources/tools-software/linux-drivers/platforms/nios2
| https:*wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/microblaze_kc705
  https:*\ github.com/analogdevicesinc/linux/blob/master/arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-fmcdaq2.dts
| https:*github.com/analogdevicesinc/linux/blob/altera_4.9/arch/arm/boot/dts/socfpga_arria10_socdk_daq2.dts
  https:*\ github.com/analogdevicesinc/linux/blob/master/arch/arm64/boot/dts/xilinx/adi-daq2.dtsi
