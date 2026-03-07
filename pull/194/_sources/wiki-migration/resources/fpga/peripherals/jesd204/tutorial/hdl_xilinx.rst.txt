DAQ2 HDL Project for Xilinx
===========================

The reference design is a processor based embedded system. The sources are split into three different folders:

-  base design for the carrier board, :git-hdl:`/projects/common <projects/common>` where all generic peripherals are instantiated. Here we do most of the PS8 configuration, add SPI, I2C and GPIOs. In some cases, we have scripts to instantiate also the PL DDR as ADC offload memory or DAC offload memory
-  base design for the evaluation board, :git-hdl:`/projects/daq2/common <projects/daq2/common>`, where all the IPs to control the DAQ2 evaluation board are instantiated, in a way in which it can be integrated with most of the carriers that we support
-  specific design for the project, in our case the ZCU102 :git-hdl:`/projects/daq2/zcu102 <projects/daq2/zcu102>`. Here, we source the carrier board configuration, then the evaluation board configuration and then we do some specific parameter modification, if required. In this folder, the constraints and ``system_top.v`` are also defined.

AD-FMCDAQ2-EBZ block diagram
----------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/AD-FMCDAQ2-EBZ_1.svg
   :alt: Xilinx HDL Block Diagram
   :width: 600px

Xilinx block diagram
--------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/daq2_xilinx_2.svg
   :alt: Xilinx HDL Block Diagram
   :width: 800px

The reference design is a processor based (ARM or Microblaze) embedded system. A functional block diagram of the system is given above. The shared transceivers are followed by the individual JESD204B and ADC/DAC IP cores. The cores are programmable through an AXI-lite interface.

The digital interface consists of 4 transmit and 4 receive lanes running at 10Gbps, by default. The transceivers interface the ADC/DAC cores at 128bits@250MHz. The data is sent or received based on the configuration of separate transmit and receive chains.

Project Flow
~~~~~~~~~~~~

The entry point for project creation is ``system_project.tcl``. Some support scripts are first loaded then the project is created. Based on the suffix of the project, the carrier board is automatically detected. The constraint files and custom modules instantiated directly in the system_top module must be added to the project files list.

:git-hdl:`projects/daq2/zc706/system_project.tcl` file:

.. code:: tcl

   source ../../scripts/adi_env.tcl
   source $ad_hdl_dir/projects/scripts/adi_project.tcl
   source $ad_hdl_dir/projects/scripts/adi_board.tcl

   adi_project_xilinx daq2_zcu102
   adi_project_files daq2_zcu102 [list \
     "../common/daq2_spi.v" \
     "system_top.v" \
     "system_constr.xdc"\
     "$ad_hdl_dir/library/xilinx/common/ad_iobuf.v" \
     "$ad_hdl_dir/projects/common/zcu102/zcu102_system_constr.xdc" ]

   adi_project_run daq2_zcu102

When the project is created, ``system_bd.tcl`` is sourced. ``system_bd.tcl`` will generate the IP Integrator system. The resulting system will be instantiated in the system_top module.

Some parameters will be defined in the first part, which will configure the ADC/DAC FIFOs. These are part of the systems in which the DDR throughput is not enough to keep up with the ADC/DAC data rates.

.. code:: tcl

   set adc_fifo_name axi_ad9680_fifo
   set adc_fifo_address_width 16
   set adc_data_width 128
   set adc_dma_data_width 64

   set dac_fifo_name axi_ad9144_fifo
   set dac_fifo_address_width 10
   set dac_data_width 128
   set dac_dma_data_width 128

The next step is to instantiate the ZCU102 base design:

.. code:: tcl

   source $ad_hdl_dir/projects/common/zcu102/zcu102_system_bd.tcl

If ADC/DAC FIFOs will be used in the system, the corresponding tcl files must be sourced.

.. code:: tcl

   source $ad_hdl_dir/projects/common/xilinx/adcfifo_bd.tcl
   source $ad_hdl_dir/projects/common/xilinx/dacfifo_bd.tcl

The next step is to source the DAQ2 specific design.

.. code:: tcl

   source ../common/daq2_bd.tcl

The generic design is optimized to supports the maximum number of carriers with minimal changes. If the specific carrier has different parameters than the default, some minor IP parameter changes need to be done. In the case below, the generic design uses parameters for 7 Series FPGAs, so parameters must be adjusted for Ultrascale+.

.. code:: tcl

   ad_ip_parameter axi_ad9144_xcvr CONFIG.XCVR_TYPE 2
   ad_ip_parameter axi_ad9680_xcvr CONFIG.XCVR_TYPE 2

   ad_ip_parameter util_daq2_xcvr CONFIG.XCVR_TYPE 2
   ad_ip_parameter util_daq2_xcvr CONFIG.QPLL_FBDIV 20
   ad_ip_parameter util_daq2_xcvr CONFIG.QPLL_REFCLK_DIV 1

DAQ2 Design
~~~~~~~~~~~

When using the JESD204 Framework we need to source the JESD204 support script. In this script several procedures which simplify the design are defined:

.. code:: tcl

   source $ad_hdl_dir/library/jesd204/scripts/jesd204.tcl

Physical Layer
--------------

The physical layer is responsible for instantiating and configuring the high speed serial transceivers in the FPGA. The physical layer is implemented with the use of two modules: AXI_ADXCVR and UTIL_ADXCVR. AXI_ADXCVR Provides an AXI interface for performing DRP reads and writes to the transceivers, allowing for dynamic reconfiguration. Given that the hardware implements 4 data lines, that's how we'll configure the NUM_OF_LANES parameter. QPLL_ENABLE parameter gives control to this IP of the QPLL reconfiguration for the Transceiver QUAD. If the QUAD is shared with other RX IPs (as it is in this design), the second ADXCVR IP will need to have QPLL_ENABLE set to 0.

.. code:: tcl

   ad_ip_instance axi_adxcvr axi_ad9144_xcvr
   ad_ip_parameter axi_ad9144_xcvr CONFIG.NUM_OF_LANES 4
   ad_ip_parameter axi_ad9144_xcvr CONFIG.QPLL_ENABLE 1
   ad_ip_parameter axi_ad9144_xcvr CONFIG.TX_OR_RX_N 1

Instantiation of the ADC transceiver controller. For this IP, QPLL_ENABLE is set to 0.

.. code:: tcl

   ad_ip_instance axi_adxcvr axi_ad9680_xcvr
   ad_ip_parameter axi_ad9680_xcvr CONFIG.NUM_OF_LANES 4
   ad_ip_parameter axi_ad9680_xcvr CONFIG.QPLL_ENABLE 0
   ad_ip_parameter axi_ad9680_xcvr CONFIG.TX_OR_RX_N 0

Given that the IP uses the same QUAD as the DAC, performing channel reconfiguration may affect the DAC and vice versa. When using the JESD204B framework, this is taken into consideration by software.

The actual transceiver blocks are instantiated in UTIL_ADXCVR.

.. code:: tcl

   ad_ip_instance util_adxcvr util_daq2_xcvr
   ad_ip_parameter util_daq2_xcvr CONFIG.RX_NUM_OF_LANES 4
   ad_ip_parameter util_daq2_xcvr CONFIG.TX_NUM_OF_LANES 4

.. code:: tcl

   ad_connect  sys_cpu_resetn util_daq2_xcvr/up_rstn
   ad_connect  sys_cpu_clk util_daq2_xcvr/up_clk

Xilinx JESD204-PHY IP can be used as an alternative to implementing the physical layer, as it's part of Vivado without additional licensing. We don't currently provide software support for the Xilinx IP. The drawback when using the Xilinx IP is that it doesn't provide Eyescan functionality.

Clocking
~~~~~~~~

Reference clocks are needed to be feed to the QPLL/CPLL. In this design, we are using tx reference clock for QPLL and rx reference clock for QPLL. If the system works at 10Gbps, the QPLL clock will be used for both the RX and TX channels. What is important to note is that the reference clocks for the transceiver QUAD must be connected to the MGTREFCLK pins either for the QUAD or an adjacent QUAD.

.. code:: tcl

   create_bd_port -dir I tx_ref_clk_0
   create_bd_port -dir I rx_ref_clk_0
   ad_xcvrpll  tx_ref_clk_0 util_daq2_xcvr/qpll_ref_clk_*
   ad_xcvrpll  rx_ref_clk_0 util_daq2_xcvr/cpll_ref_clk_*
   ad_xcvrpll  axi_ad9144_xcvr/up_pll_rst util_daq2_xcvr/up_qpll_rst_*
   ad_xcvrpll  axi_ad9680_xcvr/up_pll_rst util_daq2_xcvr/up_cpll_rst_*

Data Link Layer
---------------

The JESD204 data link layer is instantiated in the next lines, for both TX and RX type of peripheral paths. The ADI AD-IP-JESD204 implements the data link layer, supporting subclass 0 or subclass 1 and runtime reconfigurability through an AXI memory mapped interface.

.. code:: tcl

   adi_axi_jesd204_tx_create axi_ad9144_jesd 4

   adi_axi_jesd204_rx_create axi_ad9680_jesd 4

The IP is equivalent with the Xilinx licensed JESD204 IP.

Transport Layer
---------------

The transport layer peripherals are responsible for converter specific data framing and de-framing and provide a generic FIFO interface to the rest of the system.

.. code:: tcl

   ad_ip_instance axi_ad9144 axi_ad9144_core
   ad_ip_parameter axi_ad9144_core CONFIG.QUAD_OR_DUAL_N 0
   ad_ip_instance axi_ad9680 axi_ad9680_core

JESD204 Connections
-------------------

When UTIL_ADXCVR is instantiated, the channel inside of the IP may be different than the hardware pin connection to lessen the layout burden. Because of this, the UTIL_ADXCVR IP will rearrange the inside channels so that they correspond to the outside pin connection for the RX path, keeping a common transport layer. Each channel from the QUAD has assigned a specific pin for TX and RX. After rearranging the channels so they correspond to the RX pins, the TX pins may not be in the order they are connected to the DAC. The below {0 2 3 1} parameter will connect the physical layer to the data link layer as if the channels and pin connections are in order.

.. code:: tcl

   ad_xcvrcon  util_daq2_xcvr axi_ad9680_xcvr axi_ad9680_jesd
   ad_xcvrcon  util_daq2_xcvr axi_ad9144_xcvr axi_ad9144_jesd {0 2 3 1}

Additional IPs
--------------

For a complete system, we use additional modules to transfer data. The transport layer transfers data continuously from/to the ADC/DAC. CPACK/Upack will only send the enabled channels to the DMA which in turn will transfer it to the system memory. Depending on system specifics, data offload FIFOs may be inserted between upack/cpack and the DMA. When a FIFO is used, the DMA connection to the DDR can run at a lower speed, as data capture cannot be done continuously.

.. code:: tcl

   ad_ip_instance util_upack axi_ad9144_upack
   ad_ip_parameter axi_ad9144_upack CONFIG.CHANNEL_DATA_WIDTH 64
   ad_ip_parameter axi_ad9144_upack CONFIG.NUM_OF_CHANNELS 2

   ad_ip_instance axi_dmac axi_ad9144_dma
   ad_ip_parameter axi_ad9144_dma CONFIG.DMA_TYPE_SRC 0
   ad_ip_parameter axi_ad9144_dma CONFIG.DMA_TYPE_DEST 1
   ad_ip_parameter axi_ad9144_dma CONFIG.ID 1
   ad_ip_parameter axi_ad9144_dma CONFIG.AXI_SLICE_SRC 0
   ad_ip_parameter axi_ad9144_dma CONFIG.AXI_SLICE_DEST 0
   ad_ip_parameter axi_ad9144_dma CONFIG.DMA_LENGTH_WIDTH 24
   ad_ip_parameter axi_ad9144_dma CONFIG.DMA_2D_TRANSFER 0
   ad_ip_parameter axi_ad9144_dma CONFIG.CYCLIC 0
   ad_ip_parameter axi_ad9144_dma CONFIG.DMA_DATA_WIDTH_SRC 128
   ad_ip_parameter axi_ad9144_dma CONFIG.DMA_DATA_WIDTH_DEST 128

.. code:: tcl

   ad_ip_instance util_cpack axi_ad9680_cpack
   ad_ip_parameter axi_ad9680_cpack CONFIG.CHANNEL_DATA_WIDTH 64
   ad_ip_parameter axi_ad9680_cpack CONFIG.NUM_OF_CHANNELS 2

   ad_ip_instance axi_dmac axi_ad9680_dma
   ad_ip_parameter axi_ad9680_dma CONFIG.DMA_TYPE_SRC 1
   ad_ip_parameter axi_ad9680_dma CONFIG.DMA_TYPE_DEST 0
   ad_ip_parameter axi_ad9680_dma CONFIG.ID 0
   ad_ip_parameter axi_ad9680_dma CONFIG.AXI_SLICE_SRC 0
   ad_ip_parameter axi_ad9680_dma CONFIG.AXI_SLICE_DEST 0
   ad_ip_parameter axi_ad9680_dma CONFIG.SYNC_TRANSFER_START 0
   ad_ip_parameter axi_ad9680_dma CONFIG.DMA_LENGTH_WIDTH 24
   ad_ip_parameter axi_ad9680_dma CONFIG.DMA_2D_TRANSFER 0
   ad_ip_parameter axi_ad9680_dma CONFIG.CYCLIC 0
   ad_ip_parameter axi_ad9680_dma CONFIG.DMA_DATA_WIDTH_SRC 64
   ad_ip_parameter axi_ad9680_dma CONFIG.DMA_DATA_WIDTH_DEST 64

Misc Connections
----------------

.. code:: tcl

   ad_connect  util_daq2_xcvr/tx_out_clk_0 axi_ad9144_core/tx_clk
   ad_connect  axi_ad9144_jesd/tx_data_tdata axi_ad9144_core/tx_data
   ad_connect  util_daq2_xcvr/tx_out_clk_0 axi_ad9144_upack/dac_clk
   ad_connect  axi_ad9144_core/dac_enable_0 axi_ad9144_upack/dac_enable_0
   ad_connect  axi_ad9144_core/dac_ddata_0 axi_ad9144_upack/dac_data_0
   ad_connect  axi_ad9144_core/dac_valid_0 axi_ad9144_upack/dac_valid_0
   ad_connect  axi_ad9144_core/dac_enable_1 axi_ad9144_upack/dac_enable_1
   ad_connect  axi_ad9144_core/dac_ddata_1 axi_ad9144_upack/dac_data_1
   ad_connect  axi_ad9144_core/dac_valid_1 axi_ad9144_upack/dac_valid_1
   ad_connect  util_daq2_xcvr/tx_out_clk_0 axi_ad9144_fifo/dac_clk
   ad_connect  axi_ad9144_jesd_rstgen/peripheral_reset axi_ad9144_fifo/dac_rst
   ad_connect  axi_ad9144_upack/dac_valid axi_ad9144_fifo/dac_valid
   ad_connect  axi_ad9144_upack/dac_data axi_ad9144_fifo/dac_data
   ad_connect  axi_ad9144_core/dac_dunf axi_ad9144_fifo/dac_dunf
   ad_connect  sys_cpu_clk axi_ad9144_fifo/dma_clk
   ad_connect  sys_cpu_reset axi_ad9144_fifo/dma_rst
   ad_connect  sys_cpu_clk axi_ad9144_dma/m_axis_aclk
   ad_connect  sys_cpu_resetn axi_ad9144_dma/m_src_axi_aresetn
   ad_connect  axi_ad9144_fifo/dma_xfer_req axi_ad9144_dma/m_axis_xfer_req
   ad_connect  axi_ad9144_fifo/dma_ready axi_ad9144_dma/m_axis_ready
   ad_connect  axi_ad9144_fifo/dma_data axi_ad9144_dma/m_axis_data
   ad_connect  axi_ad9144_fifo/dma_valid axi_ad9144_dma/m_axis_valid
   ad_connect  axi_ad9144_fifo/dma_xfer_last axi_ad9144_dma/m_axis_last

   # connections (adc)

   ad_connect  util_daq2_xcvr/rx_out_clk_0 axi_ad9680_core/rx_clk
   ad_connect  axi_ad9680_jesd/rx_sof axi_ad9680_core/rx_sof
   ad_connect  axi_ad9680_jesd/rx_data_tdata axi_ad9680_core/rx_data
   ad_connect  util_daq2_xcvr/rx_out_clk_0 axi_ad9680_cpack/adc_clk
   ad_connect  axi_ad9680_jesd_rstgen/peripheral_reset axi_ad9680_cpack/adc_rst
   ad_connect  axi_ad9680_core/adc_enable_0 axi_ad9680_cpack/adc_enable_0
   ad_connect  axi_ad9680_core/adc_valid_0 axi_ad9680_cpack/adc_valid_0
   ad_connect  axi_ad9680_core/adc_data_0 axi_ad9680_cpack/adc_data_0
   ad_connect  axi_ad9680_core/adc_enable_1 axi_ad9680_cpack/adc_enable_1
   ad_connect  axi_ad9680_core/adc_valid_1 axi_ad9680_cpack/adc_valid_1
   ad_connect  axi_ad9680_core/adc_data_1 axi_ad9680_cpack/adc_data_1
   ad_connect  util_daq2_xcvr/rx_out_clk_0 axi_ad9680_fifo/adc_clk
   ad_connect  axi_ad9680_jesd_rstgen/peripheral_reset axi_ad9680_fifo/adc_rst
   ad_connect  axi_ad9680_cpack/adc_valid axi_ad9680_fifo/adc_wr
   ad_connect  axi_ad9680_cpack/adc_data axi_ad9680_fifo/adc_wdata
   ad_connect  sys_cpu_clk axi_ad9680_fifo/dma_clk
   ad_connect  sys_cpu_clk axi_ad9680_dma/s_axis_aclk
   ad_connect  sys_cpu_resetn axi_ad9680_dma/m_dest_axi_aresetn
   ad_connect  axi_ad9680_fifo/dma_wr axi_ad9680_dma/s_axis_valid
   ad_connect  axi_ad9680_fifo/dma_wdata axi_ad9680_dma/s_axis_data
   ad_connect  axi_ad9680_fifo/dma_wready axi_ad9680_dma/s_axis_ready
   ad_connect  axi_ad9680_fifo/dma_xfer_req axi_ad9680_dma/s_axis_xfer_req
   ad_connect  axi_ad9680_core/adc_dovf axi_ad9680_fifo/adc_wovf

CPU Address Allocation
----------------------

The below instructions assign addresses to all AXI modules in the design. These will be used when generating the device tree in linux.

.. code:: tcl

   # interconnect (cpu)
   ad_cpu_interconnect 0x44A60000 axi_ad9144_xcvr
   ad_cpu_interconnect 0x44A00000 axi_ad9144_core
   ad_cpu_interconnect 0x44A90000 axi_ad9144_jesd
   ad_cpu_interconnect 0x7c420000 axi_ad9144_dma
   ad_cpu_interconnect 0x44A50000 axi_ad9680_xcvr
   ad_cpu_interconnect 0x44A10000 axi_ad9680_core
   ad_cpu_interconnect 0x44AA0000 axi_ad9680_jesd
   ad_cpu_interconnect 0x7c400000 axi_ad9680_dma

High Perfomance Port Connections
--------------------------------

The below instructions assign an HP port to all AXI masters, through an interconnect. If there is a single master per interconnect, it will be bypassed in the interconnect. The HP3 connections allow the physical layer to transmit eyescan data to memory, without software interference.

.. code:: tcl

   # gt uses hp3, and 100MHz clock for both DRP and AXI4
   ad_mem_hp3_interconnect sys_cpu_clk sys_ps7/S_AXI_HP3
   ad_mem_hp3_interconnect sys_cpu_clk axi_ad9680_xcvr/m_axi
   # interconnect (mem/dac)

   ad_mem_hp1_interconnect sys_cpu_clk sys_ps7/S_AXI_HP1
   ad_mem_hp1_interconnect sys_cpu_clk axi_ad9144_dma/m_src_axi
   ad_mem_hp2_interconnect sys_cpu_clk sys_ps7/S_AXI_HP2
   ad_mem_hp2_interconnect sys_cpu_clk axi_ad9680_dma/m_dest_axi

Interrupts
----------

.. code:: tcl

   ad_cpu_interrupt ps-10 mb-15 axi_ad9144_jesd/irq
   ad_cpu_interrupt ps-11 mb-14 axi_ad9680_jesd/irq
   ad_cpu_interrupt ps-12 mb-13 axi_ad9144_dma/irq
   ad_cpu_interrupt ps-13 mb-12 axi_ad9680_dma/irq

System Top
~~~~~~~~~~

The reference clock that is used for the transceivers, must be captured by an IBUFDS_GTE4 block. Because UTIL_ADXCVR doesn't have the buffer instantiated, the best place to instantiate it is in ``system_top.v``.

.. code:: tcl

     IBUFDS_GTE4 i_ibufds_rx_ref_clk (
       .CEB (1'd0),
       .I (rx_ref_clk_p),
       .IB (rx_ref_clk_n),
       .O (rx_ref_clk),
       .ODIV2 ());

We prefer using single ended signals as much as possible in the IPI system.

Constraints
~~~~~~~~~~~

As shown below, the transceiver channels and ADC channels are not connected one to one.

.. code:: xdc

   set_property  -dict {PACKAGE_PIN  K2} [get_ports rx_data_p[0]] ; ## A10  FMC_HPC0_DP3_M2C_P
   set_property  -dict {PACKAGE_PIN  K1} [get_ports rx_data_n[0]] ; ## A11  FMC_HPC0_DP3_M2C_N
   set_property  -dict {PACKAGE_PIN  H2} [get_ports rx_data_p[1]] ; ## C06  FMC_HPC0_DP0_M2C_P
   set_property  -dict {PACKAGE_PIN  H1} [get_ports rx_data_n[1]] ; ## C07  FMC_HPC0_DP0_M2C_N
   set_property  -dict {PACKAGE_PIN  F2} [get_ports rx_data_p[2]] ; ## A06  FMC_HPC0_DP2_M2C_P
   set_property  -dict {PACKAGE_PIN  F1} [get_ports rx_data_n[2]] ; ## A07  FMC_HPC0_DP2_M2C_N
   set_property  -dict {PACKAGE_PIN  J4} [get_ports rx_data_p[3]] ; ## A02  FMC_HPC0_DP1_M2C_P
   set_property  -dict {PACKAGE_PIN  J3} [get_ports rx_data_n[3]] ; ## A03  FMC_HPC0_DP1_M2C_N
   set_property  -dict {PACKAGE_PIN  K6} [get_ports tx_data_p[0]] ; ## A30  FMC_HPC0_DP3_C2M_P (tx_data_p[0])
   set_property  -dict {PACKAGE_PIN  K5} [get_ports tx_data_n[0]] ; ## A31  FMC_HPC0_DP3_C2M_N (tx_data_n[0])
   set_property  -dict {PACKAGE_PIN  G4} [get_ports tx_data_p[1]] ; ## C02  FMC_HPC0_DP0_C2M_P (tx_data_p[3])
   set_property  -dict {PACKAGE_PIN  G3} [get_ports tx_data_n[1]] ; ## C03  FMC_HPC0_DP0_C2M_N (tx_data_n[3])
   set_property  -dict {PACKAGE_PIN  F6} [get_ports tx_data_p[2]] ; ## A26  FMC_HPC0_DP2_C2M_P (tx_data_p[1])
   set_property  -dict {PACKAGE_PIN  F5} [get_ports tx_data_n[2]] ; ## A27  FMC_HPC0_DP2_C2M_N (tx_data_n[1])
   set_property  -dict {PACKAGE_PIN  H6} [get_ports tx_data_p[3]] ; ## A22  FMC_HPC0_DP1_C2M_P (tx_data_p[2])
   set_property  -dict {PACKAGE_PIN  H5} [get_ports tx_data_n[3]] ; ## A23  FMC_HPC0_DP1_C2M_N (tx_data_n[2])

The reference clocks run at 500 MHz, and the frame clock at 250, in the maximum throughput configuration(default).

.. code:: xdc

   create_clock -name tx_ref_clk   -period  2.00 [get_ports tx_ref_clk_p]
   create_clock -name rx_ref_clk   -period  2.00 [get_ports rx_ref_clk_p]

   create_clock -name tx_div_clk   -period  4.00 [get_pins i_system_wrapper/system_i/util_daq2_xcvr/inst/i_xch_0/i_gthe4_channel/TXOUTCLK]
   create_clock -name rx_div_clk   -period  4.00 [get_pins i_system_wrapper/system_i/util_daq2_xcvr/inst/i_xch_0/i_gthe4_channel/RXOUTCLK]

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

When building the project, you should always use the recommended version of the tools for the specific :doc:`release </wiki-migration/resources/fpga/docs/releases>`. In this example, we'll use release 2018_r1, which has Vivado 2017.4.1 as the recommended version. If you're using different Vivado versions, it's possible that there are slight modifications on how the synthesis works, or different Xilinx IP changes, which affect the system functionality.

::

   mkdir adi
   cd adi
   git clone https://github.com/analogdevicesinc/hdl.git
   cd hdl/
   git status ## check for everything, including branch name
   git checkout hdl_2018_r1 ## change to the hdl_2018_r2 branch
   make -C projects/daq2/zcu102

Building BOOT.BIN
~~~~~~~~~~~~~~~~~

The boot image ``BOOT.BIN`` is build using the bootgen tool which requires several input files. For ease of use we provide a bash shell script which allows building ``BOOT.BIN`` from ``system_top.hdf``, ``u-boot.elf`` and either ``bl31.elf`` or a path to the Arm Trusted Firmware repository.

The script can be downloaded from here:

-  `build_zynqmp_boot_bin.sh <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/zynqmp_boot_bin/build_zynqmp_boot_bin.sh>`_

| **NOTE: After downloading the script you need to make it executable**
| ``$ chmod +x build_zynqmp_boot_bin.sh``

::

   usage: build_zynqmp_boot_bin.sh system_top.hdf u-boot.elf (download | bl31.elf | <path-to-arm-trusted-firmware-source>) [output-archive]

-  Path to ``system_top.hdf`` and ``u-boot.elf`` are required parameters.
-  The 3rd argument must either be ``download`` (which will git clone the ATF repository), ``bl31.elf`` or the file system ``path`` to the Arm Trusted Firmware source code repository
-  An optionally 4th ``name`` parameter can be given to tar.gz the output directory. (``name``.tar.gz)
-  Build output is located in a local directory named: output_boot_bin.
-  This script requires Xilinx XSDK and bootgen in the PATH.
   \* A simple way is to source vivado settings[32|64].sh:

::

   $ source /opt/Xilinx/Vivado/201x.x/settings64.sh

| **NOTE: u-boot.elf**
| For those who don't want to build u-boot themselves.
| The **u-boot.elf** can be extracted from the project folder on the :doc:`SD Card image </wiki-migration/resources/tools-software/linux-software/zynq_images>`, **bootgen_sysfiles.tgz**

References
~~~~~~~~~~

| :doc:`HDL Build Instructions </wiki-migration/resources/fpga/docs/build>`
| :doc:`How to build the ZynqMP boot image BOOT.BIN </wiki-migration/resources/tools-software/linux-software/build-the-zynqmp-boot-image>`
| :doc:`How to build the Zynq boot image BOOT.BIN </wiki-migration/resources/tools-software/linux-software/build-the-zynq-boot-image>`
