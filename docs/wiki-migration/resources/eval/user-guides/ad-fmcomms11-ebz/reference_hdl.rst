FMCOMMS11 HDL Reference Design
==============================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/fmcomms11/index.html\


Functional Overview
-------------------

The HDL reference design is an embedded system built around a processor core either ARM, NIOS-II or Microblaze. A functional block diagram of the system is shown below. The high speed digital interface of the converters is handled by the :doc:`JESD204B framework </wiki-migration/resources/fpga/peripherals/jesd204>`. Due to the system's memory interface bandwidth limitation, there are intermediary buffers in the both TX and RX data paths, in order to save and push data using high data rates. In case of the ZC706 carrier board, the RX buffer depth is 1Gbyte, and TX buffer depth is 1Mbyte. This depths can be swapped if required.

By default the AD9162 is configured in complex mode with 8 lanes (see Table 16. in data sheet), and the AD9625 is configured in generic operation mode with 8 lanes (see Table 16. in data sheet). Both JESD204 interfaces run in Subclass 0.

Other configurations can be used too, but the user needs to make sure that all the parties (clock chip, converters and FPGA JESD204 IPs) of the interface are reconfigured accordingly.

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/fmcomms11_bd.svg
   :alt: fmcomms11_bd.svg
   :align: center

Reference design for Xilinx carriers
------------------------------------

The reference design is a processor based embedded system. The sources are split into three different folders:

-  Base design for the carrier board (e.g. :git-hdl:`/projects/common/zc706 <projects/common/zc706>`) where all generic peripherals are instantiated. Here we do most of the PS configuration, add SPI, I2C and GPIOs. In some cases, we have scripts to instantiate also the PL DDR as ADC offload memory or DAC offload memory.
-  Base design for the evaluation board (:git-hdl:`/projects/fmcomms11/common <projects/fmcomms11/common>`), where all the IPs to control the FMCOMMS11 evaluation board and to capture or send data are instantiated. The data paths defined in this block design are common across multiple carrier platforms.
-   Specific design for the project, in our case for ZC706 (:git-hdl:`/projects/fmcomms11/zc706 <projects/fmcomms11/common>`). Here, we source the carrier board configuration, then the evaluation board configuration and then we do some specific parameter modification, if required. In this folder, the constraints and system_top.v are also defined.

The reference design is a processor based (ARM or Microblaze) embedded system. A functional block diagram of the system is given above. The data path consist of the shared transceivers, then are followed by the individual JESD204B link and transport layer IP cores. The cores are programmable through an AXI-lite interface.

The digital interface consists of 8 transmit and 8 receive lanes running at 9.8304Gbps and 4.9152 respectively, by default. The transceivers interface the DAC/ADC cores at 256bits@245.76MHz and 256bit@122.88MHz respectively. The data is sent or received based on the configuration of separate transmit and receive chains.

Project Flow
------------

The entry point for project creation is ``system_project.tcl``. Some support scripts are first loaded then the project is created. Based on the suffix of the project, the carrier board is automatically detected. The constraint files and custom modules instantiated directly in the system_top module must be added to the project files list.

:git-hdl:`projects/daq2/zc706/system_project.tcl` file:

.. code:: tcl

   source ../../scripts/adi_env.tcl
   source $ad_hdl_dir/projects/scripts/adi_project.tcl
   source $ad_hdl_dir/projects/scripts/adi_board.tcl

   adi_project_xilinx fmcomms11_zc706
   adi_project_files fmcomms11_zc706 [list \
     "../common/fmcomms11_spi.v" \
     "system_top.v" \
     "system_constr.xdc"\
     "$ad_hdl_dir/library/xilinx/common/ad_iobuf.v" \
     "$ad_hdl_dir/projects/common/zc706/zc706_plddr3_constr.xdc" \
     "$ad_hdl_dir/projects/common/zc706/zc706_system_constr.xdc" ]

   adi_project_run fmcomms11_zc706

When the project is created, ``system_bd.tcl`` is sourced. ``system_bd.tcl`` will generate the IP Integrator system. The resulting system will be instantiated in the system_top module.

The first step is to instantiate the ZC706 base design:

.. code:: tcl

   source $ad_hdl_dir/projects/common/zc706/zc706_system_bd.tcl

In order to use the ADC/DAC FIFOs, the corresponding tcl files must be sourced.

.. code:: tcl

   source $ad_hdl_dir/projects/common/zc706/zc706_plddr3_adcfifo_bd.tcl
   source $ad_hdl_dir/projects/common/xilinx/dacfifo_bd.tcl

If the user wants to swap the resources allocated to the FIFO, the following scripts should be sourced instead:

.. code:: tcl

   source $ad_hdl_dir/projects/common/zc706/zc706_plddr3_dacfifo_bd.tcl
   source $ad_hdl_dir/projects/common/xilinx/adcfifo_bd.tcl

The following parameters will define the FIFO's depth. Note, if the FIFO is using the PL side DDR interface, the address width parameter can be ignored, and the FIFO will have an equal depth with the DDR memory. (e.g. in case of the ZC706 board is 1Gbyte)

.. code:: tcl

   # the DAC FIFO has a 500KSMP depth - 1 Mbyte
   set dac_fifo_address_width 15

   # by default PLDDR is used (1 Gbyte), this varible should be ignored
   set adc_fifo_address_width 15

The next step is to source the FMCOMMS11 specific design.

.. code:: tcl

   source ../common/fmcomms11_bd.tcl

FMCOMMS11 Design
----------------

When using the JESD204 Framework we need to source the JESD204 support script. In this script several procedures which simplify the design are defined:

.. code:: tcl

   source $ad_hdl_dir/library/jesd204/scripts/jesd204.tcl

The main JESD204 configuration parameters are defined. These parameters are essential and need to respect the device side configuration in order to have a successful link bring up.

.. code:: tcl

   # JESD204 TX parameters
   set TX_NUM_OF_LANES 8      ; # L
   set TX_NUM_OF_CONVERTERS 2 ; # M
   set TX_SAMPLES_PER_FRAME 2 ; # S
   set TX_SAMPLE_WIDTH 16     ; # N/NP

   set TX_SAMPLES_PER_CHANNEL [expr [expr $TX_NUM_OF_LANES * 32 ] / \
                                    [expr $TX_NUM_OF_CONVERTERS * $TX_SAMPLE_WIDTH]] ; # L * 32 / (M * N)

   # JESD204 RX parameters
   set RX_NUM_OF_LANES 8      ; # L
   set RX_NUM_OF_CONVERTERS 1 ; # M
   set RX_SAMPLES_PER_FRAME 4 ; # S
   set RX_SAMPLE_WIDTH 16     ; # N/NP

Physical Layer
~~~~~~~~~~~~~~

The physical layer is responsible for instantiating and configuring the high speed serial transceivers in the FPGA. The physical layer is implemented with the use of two modules: AXI_ADXCVR and UTIL_ADXCVR. AXI_ADXCVR provides an AXI interface for performing DRP reads and writes to the transceivers, allowing for dynamic reconfiguration. Given that the hardware implements 8 data lines, that's how we'll configure the NUM_OF_LANES parameter. QPLL_ENABLE parameter gives control to this IP of the QPLL reconfiguration for the Transceiver QUAD. If the QUAD is shared with other RX IPs (as it is in this design), the second ADXCVR IP will need to have QPLL_ENABLE set to 0.

.. code:: tcl

   ad_ip_instance axi_adxcvr axi_ad9162_xcvr [list \ 
     NUM_OF_LANES 8 \
     QPLL_ENABLE 1 \
     TX_OR_RX_N 1 \
   ]

Instantiation of the ADC transceiver controller. For this IP, QPLL_ENABLE is set to 0.

.. code:: tcl

   ad_ip_instance axi_adxcvr axi_ad9625_xcvr [list \
     NUM_OF_LANES 8 \
     QPLL_ENABLE 0 \
     TX_OR_RX_N 0 \
   ]

Given that the IP uses the same QUAD as the DAC, performing channel reconfiguration may affect the DAC and vice versa. When using the JESD204B framework, this is taken into consideration by software.

The actual transceiver blocks are instantiated in UTIL_ADXCVR.

.. code:: tcl

   ad_ip_instance util_adxcvr util_fmcomms11_xcvr [list \
     QPLL_FBDIV 0x120 \
     CPLL_FBDIV 4 \
     TX_NUM_OF_LANES 8 \
     TX_CLK25_DIV 7 \
     RX_NUM_OF_LANES 8 \
     RX_CLK25_DIV 7 \
     RX_DFE_LPM_CFG 0x0904 \
     RX_CDR_CFG 0x03000023ff10400020 \
   ]

Xilinx JESD204-PHY IP can be used as an alternative to implementing the physical layer, as it's part of Vivado without additional licensing. We don't currently provide software support for the Xilinx IP. The drawback when using the Xilinx IP is that it doesn't provide Eyescan functionality.

Clocking
^^^^^^^^

Reference clocks are needed to be feed to the QPLL/CPLL. In this design, we are using a shared reference clock for both receive and transmit channels. What is important to note is that the reference clocks for the transceiver QUAD must be connected to the MGTREFCLK pins either for the QUAD or an adjacent QUAD.

.. code:: tcl

   create_bd_port -dir I tx_ref_clk_0
   create_bd_port -dir I rx_ref_clk_0
   ad_xcvrpll  tx_ref_clk_0 util_fmcomms11_xcvr/qpll_ref_clk_*
   ad_xcvrpll  rx_ref_clk_0 util_fmcomms11_xcvr/cpll_ref_clk_*
   ad_xcvrpll  axi_ad9162_xcvr/up_pll_rst util_fmcomms11_xcvr/up_qpll_rst_*
   ad_xcvrpll  axi_ad9625_xcvr/up_pll_rst util_fmcomms11_xcvr/up_cpll_rst_*

Data Link Layer
~~~~~~~~~~~~~~~

The JESD204 data link layer is instantiated in the next lines, for both TX and RX type of peripheral paths. The ADI AD-IP-JESD204 implements the data link layer, supporting subclass 0 and run time reconfiguration through an AXI memory mapped interface.

.. code:: tcl

   adi_axi_jesd204_tx_create axi_ad9162_jesd 8

   adi_axi_jesd204_rx_create axi_ad9625_jesd 8

The IP is equivalent with the Xilinx licensed JESD204 IP.

To relax the constraints for PCB design, the n-th physical lane it's not connected to the n-th logical lane, therefor there is a remapping scheme between the physical and link layer to reorder the data streams. In case of the FMCOMMS11 board, both ADC and DAC side using the same remapping scheme. With the following remapping scheme: {0 1 2 3 7 4 6 5}, where the n-th logical lane is mapped to the "list[n]" physical lane.

.. code:: tcl

   ad_xcvrcon  util_fmcomms11_xcvr axi_ad9162_xcvr axi_ad9162_jesd {0 1 2 3 7 4 6 5}
   ad_xcvrcon  util_fmcomms11_xcvr axi_ad9625_xcvr axi_ad9625_jesd {0 1 2 3 7 4 6 5}

Transport Layer
~~~~~~~~~~~~~~~

The transport layer peripherals are responsible for converter specific data framing and de-framing and provide a generic FIFO interface to the rest of the system.

.. code:: tcl

   adi_tpl_jesd204_tx_create axi_ad9162_core $TX_NUM_OF_LANES \
                                             $TX_NUM_OF_CONVERTERS \
                                             $TX_SAMPLES_PER_FRAME \
                                             $TX_SAMPLE_WIDTH

   adi_tpl_jesd204_rx_create axi_ad9625_core $RX_NUM_OF_LANES \
                                             $RX_NUM_OF_CONVERTERS \
                                             $RX_SAMPLES_PER_FRAME \
                                             $RX_SAMPLE_WIDTH

JESD204 Connections
~~~~~~~~~~~~~~~~~~~

When UTIL_ADXCVR is instantiated, the channel inside of the IP may be different than the hardware pin connection to lessen the layout burden. Because of this, the UTIL_ADXCVR IP will rearrange the inside channels so that they correspond to the outside pin connection for the RX path, keeping a common transport layer.

.. code:: tcl

   ad_xcvrcon  util_fmcomms11_xcvr axi_ad9162_xcvr axi_ad9162_jesd
   ad_xcvrcon  util_fmcomms11_xcvr axi_ad9625_xcvr axi_ad9625_jesd

Additional IPs
~~~~~~~~~~~~~~

For a complete system, we use additional modules to transfer data. The transport layer transfers data continuously from/to the ADC/DAC. In the TX data path UPACK will only send the enabled channels to the DMA which in turn will transfer it to the system memory. Depending on system specifics, data offload FIFOs may be inserted between upack/cpack and the DMA. When a FIFO is used, the DMA connection to the DDR can run at a lower speed, as data capture cannot be done continuously.

.. code:: tcl

   ad_ip_instance util_upack2 util_ad9162_upack [list \
     NUM_OF_CHANNELS $TX_NUM_OF_CONVERTERS \
     SAMPLES_PER_CHANNEL $TX_SAMPLES_PER_CHANNEL \
     SAMPLE_DATA_WIDTH $TX_SAMPLE_WIDTH \
   ]

   ad_ip_instance axi_dmac axi_ad9162_dma [list \
     DMA_TYPE_SRC 0 \
     DMA_TYPE_DEST 1 \
     ID 1 \
     AXI_SLICE_SRC 0 \
     AXI_SLICE_DEST 0 \
     DMA_LENGTH_WIDTH 24 \
     DMA_2D_TRANSFER 0 \
     CYCLIC 0 \
     DMA_DATA_WIDTH_SRC 256 \
     DMA_DATA_WIDTH_DEST 256 \
   ]

.. code:: tcl

   ad_ip_instance axi_dmac axi_ad9625_dma [list \
     DMA_TYPE_SRC 1 \
     DMA_TYPE_DEST 0 \
     ID 0 \
     AXI_SLICE_SRC 0 \
     AXI_SLICE_DEST 0 \
     SYNC_TRANSFER_START 0 \
     DMA_LENGTH_WIDTH 24 \
     DMA_2D_TRANSFER 0 \
     CYCLIC 0 \
     DMA_DATA_WIDTH_SRC 64 \
     DMA_DATA_WIDTH_DEST 64 \
   ]

Misc Connections
~~~~~~~~~~~~~~~~

.. code:: tcl

   # connections (dac)

   ad_connect  axi_ad9162_core/dac_valid_0 util_ad9162_upack/fifo_rd_en
   for {set i 0} {$i < $TX_NUM_OF_CONVERTERS} {incr i} {
     ad_connect  util_ad9162_upack/fifo_rd_data_$i axi_ad9162_core/dac_data_$i
     ad_connect  axi_ad9162_core/dac_enable_$i  util_ad9162_upack/enable_$i
   }

   ad_connect  util_fmcomms11_xcvr/tx_out_clk_0 axi_ad9162_fifo/dac_clk
   ad_connect  axi_ad9162_jesd_rstgen/peripheral_reset axi_ad9162_fifo/dac_rst
   ad_connect  sys_cpu_clk axi_ad9162_fifo/dma_clk
   ad_connect  sys_cpu_reset axi_ad9162_fifo/dma_rst
   ad_connect  sys_cpu_clk axi_ad9162_dma/m_axis_aclk
   ad_connect  sys_cpu_resetn axi_ad9162_dma/m_src_axi_aresetn
   ad_connect  util_ad9162_upack/s_axis_valid VCC
   ad_connect  util_ad9162_upack/s_axis_ready axi_ad9162_fifo/dac_valid
   ad_connect  util_ad9162_upack/s_axis_data axi_ad9162_fifo/dac_data
   ad_connect  axi_ad9162_core/dac_dunf axi_ad9162_fifo/dac_dunf
   ad_connect  axi_ad9162_fifo/dma_xfer_req axi_ad9162_dma/m_axis_xfer_req
   ad_connect  axi_ad9162_fifo/dma_ready axi_ad9162_dma/m_axis_ready
   ad_connect  axi_ad9162_fifo/dma_data axi_ad9162_dma/m_axis_data
   ad_connect  axi_ad9162_fifo/dma_valid axi_ad9162_dma/m_axis_valid
   ad_connect  axi_ad9162_fifo/dma_xfer_last axi_ad9162_dma/m_axis_last
   ad_connect  dac_fifo_bypass axi_ad9162_fifo/bypass

   # connections (adc)

   ad_connect  axi_ad9625_jesd/rx_sof axi_ad9625_core/link_sof
   ad_connect  axi_ad9625_jesd/rx_data_tdata axi_ad9625_core/link_data
   ad_connect  axi_ad9625_jesd/rx_data_tvalid axi_ad9625_core/link_valid

   ad_connect  util_fmcomms11_xcvr/rx_out_clk_0 axi_ad9625_fifo/adc_clk
   ad_connect  axi_ad9625_jesd_rstgen/peripheral_reset axi_ad9625_fifo/adc_rst
   ad_connect  axi_ad9625_core/adc_valid_0 axi_ad9625_fifo/adc_wr
   ad_connect  axi_ad9625_core/adc_data_0 axi_ad9625_fifo/adc_wdata
   ad_connect  sys_cpu_clk axi_ad9625_fifo/dma_clk
   ad_connect  sys_cpu_clk axi_ad9625_dma/s_axis_aclk
   ad_connect  sys_cpu_resetn axi_ad9625_dma/m_dest_axi_aresetn
   ad_connect  axi_ad9625_fifo/dma_wr axi_ad9625_dma/s_axis_valid
   ad_connect  axi_ad9625_fifo/dma_wdata axi_ad9625_dma/s_axis_data
   ad_connect  axi_ad9625_fifo/dma_wready axi_ad9625_dma/s_axis_ready
   ad_connect  axi_ad9625_fifo/dma_xfer_req axi_ad9625_dma/s_axis_xfer_req
   ad_connect  axi_ad9625_core/adc_dovf axi_ad9625_fifo/adc_wovf

CPU Address Allocation
~~~~~~~~~~~~~~~~~~~~~~

The below instructions assign addresses to all AXI modules in the design. These will be used when generating the device tree in linux.

.. code:: tcl

   ad_cpu_interconnect 0x44A60000 axi_ad9162_xcvr
   ad_cpu_interconnect 0x44A00000 axi_ad9162_core
   ad_cpu_interconnect 0x44A90000 axi_ad9162_jesd
   ad_cpu_interconnect 0x7c420000 axi_ad9162_dma
   ad_cpu_interconnect 0x44A50000 axi_ad9625_xcvr
   ad_cpu_interconnect 0x44A10000 axi_ad9625_core
   ad_cpu_interconnect 0x44AA0000 axi_ad9625_jesd
   ad_cpu_interconnect 0x7c400000 axi_ad9625_dma

High Performance Port Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The below instructions assign an HP port to all AXI masters, through an interconnect. If there is a single master per interconnect, it will be bypassed in the interconnect. The HP3 connections allow the physical layer to transmit eyescan data to memory, without software interference.

.. code:: tcl

   # gt uses hp3, and 100MHz clock for both DRP and AXI4

   ad_mem_hp3_interconnect sys_cpu_clk sys_ps7/S_AXI_HP3
   ad_mem_hp3_interconnect sys_cpu_clk axi_ad9625_xcvr/m_axi

   # interconnect (mem/dac)

   ad_mem_hp1_interconnect sys_cpu_clk sys_ps7/S_AXI_HP1
   ad_mem_hp1_interconnect sys_cpu_clk axi_ad9162_dma/m_src_axi
   ad_mem_hp2_interconnect sys_cpu_clk sys_ps7/S_AXI_HP2
   ad_mem_hp2_interconnect sys_cpu_clk axi_ad9625_dma/m_dest_axi

Interrupts
~~~~~~~~~~

.. code:: tcl

   ad_cpu_interrupt ps-10 mb-15 axi_ad9162_jesd/irq
   ad_cpu_interrupt ps-11 mb-14 axi_ad9625_jesd/irq
   ad_cpu_interrupt ps-12 mb-12 axi_ad9162_dma/irq
   ad_cpu_interrupt ps-13 mb-13 axi_ad9625_dma/irq

System Top
~~~~~~~~~~

The reference clock that is used for the transceivers, must be captured by an IBUFDS_GTE2 block. Because UTIL_ADXCVR doesn't have the buffer instantiated, the best place to instantiate it is in ``system_top.v``.

.. code:: tcl

     IBUFDS_GTE2 i_ibufds_tx_ref_clk (
       .CEB (1'd0),
       .I (trx_ref_clk_p),
       .IB (trx_ref_clk_n),
       .O (trx_ref_clk),
       .ODIV2 ());

We prefer using single ended signals as much as possible in the IPI system.

Constraints
~~~~~~~~~~~

As shown below, the transceiver channels are connected to the appropriate high speed FMC lane. The lane remapping is done after the JESD204 link layer, see the **Data Link Layer** section for more details.

.. code:: xdc


   set_property  -dict {PACKAGE_PIN  AH10} [get_ports rx_data_p[0]]  ; ## C06  FMC_HPC_DP0_M2C_P
   set_property  -dict {PACKAGE_PIN  AH9 } [get_ports rx_data_n[0]]  ; ## C07  FMC_HPC_DP0_M2C_N
   set_property  -dict {PACKAGE_PIN  AJ8 } [get_ports rx_data_p[1]]  ; ## A02  FMC_HPC_DP1_M2C_P
   set_property  -dict {PACKAGE_PIN  AJ7 } [get_ports rx_data_n[1]]  ; ## A03  FMC_HPC_DP1_M2C_N
   set_property  -dict {PACKAGE_PIN  AG8 } [get_ports rx_data_p[2]]  ; ## A06  FMC_HPC_DP2_M2C_P
   set_property  -dict {PACKAGE_PIN  AG7 } [get_ports rx_data_n[2]]  ; ## A07  FMC_HPC_DP2_M2C_N
   set_property  -dict {PACKAGE_PIN  AE8 } [get_ports rx_data_p[3]]  ; ## A10  FMC_HPC_DP3_M2C_P
   set_property  -dict {PACKAGE_PIN  AE7 } [get_ports rx_data_n[3]]  ; ## A11  FMC_HPC_DP3_M2C_N
   set_property  -dict {PACKAGE_PIN  AH6 } [get_ports rx_data_p[4]]  ; ## A14  FMC_HPC_DP4_M2C_P
   set_property  -dict {PACKAGE_PIN  AH5 } [get_ports rx_data_n[4]]  ; ## A15  FMC_HPC_DP4_M2C_N
   set_property  -dict {PACKAGE_PIN  AG4 } [get_ports rx_data_p[5]]  ; ## A18  FMC_HPC_DP5_M2C_P
   set_property  -dict {PACKAGE_PIN  AG3 } [get_ports rx_data_n[5]]  ; ## A19  FMC_HPC_DP5_M2C_N
   set_property  -dict {PACKAGE_PIN  AF6 } [get_ports rx_data_p[6]]  ; ## B16  FMC_HPC_DP6_M2C_P
   set_property  -dict {PACKAGE_PIN  AF5 } [get_ports rx_data_n[6]]  ; ## B17  FMC_HPC_DP6_M2C_N
   set_property  -dict {PACKAGE_PIN  AD6 } [get_ports rx_data_p[7]]  ; ## B12  FMC_HPC_DP7_M2C_P
   set_property  -dict {PACKAGE_PIN  AD5 } [get_ports rx_data_n[7]]  ; ## B13  FMC_HPC_DP7_M2C_N

   set_property  -dict {PACKAGE_PIN  AK10} [get_ports tx_data_p[0]]  ; ## C02  FMC_HPC_DP0_C2M_P
   set_property  -dict {PACKAGE_PIN  AK9 } [get_ports tx_data_n[0]]  ; ## C03  FMC_HPC_DP0_C2M_N
   set_property  -dict {PACKAGE_PIN  AK6 } [get_ports tx_data_p[1]]  ; ## A22  FMC_HPC_DP1_C2M_P
   set_property  -dict {PACKAGE_PIN  AK5 } [get_ports tx_data_n[1]]  ; ## A23  FMC_HPC_DP1_C2M_N
   set_property  -dict {PACKAGE_PIN  AJ4 } [get_ports tx_data_p[2]]  ; ## A26  FMC_HPC_DP2_C2M_P
   set_property  -dict {PACKAGE_PIN  AJ3 } [get_ports tx_data_n[2]]  ; ## A27  FMC_HPC_DP2_C2M_N
   set_property  -dict {PACKAGE_PIN  AK2 } [get_ports tx_data_p[3]]  ; ## A30  FMC_HPC_DP3_C2M_P
   set_property  -dict {PACKAGE_PIN  AK1 } [get_ports tx_data_n[3]]  ; ## A31  FMC_HPC_DP3_C2M_N
   set_property  -dict {PACKAGE_PIN  AH2 } [get_ports tx_data_p[4]]  ; ## A34  FMC_HPC_DP4_C2M_P
   set_property  -dict {PACKAGE_PIN  AH1 } [get_ports tx_data_n[4]]  ; ## A35  FMC_HPC_DP4_C2M_N
   set_property  -dict {PACKAGE_PIN  AF2 } [get_ports tx_data_p[5]]  ; ## A38  FMC_HPC_DP5_C2M_P
   set_property  -dict {PACKAGE_PIN  AF1 } [get_ports tx_data_n[5]]  ; ## A39  FMC_HPC_DP5_C2M_N
   set_property  -dict {PACKAGE_PIN  AE4 } [get_ports tx_data_p[6]]  ; ## B36  FMC_HPC_DP6_C2M_P
   set_property  -dict {PACKAGE_PIN  AE3 } [get_ports tx_data_n[6]]  ; ## B37  FMC_HPC_DP6_C2M_N
   set_property  -dict {PACKAGE_PIN  AD2 } [get_ports tx_data_p[7]]  ; ## B32  FMC_HPC_DP7_C2M_P
   set_property  -dict {PACKAGE_PIN  AD1 } [get_ports tx_data_n[7]]  ; ## B33  FMC_HPC_DP7_C2M_N

In default configuration the reference clocks run at 122.88 MHz, the RX core clock at 122.88MHz and TX core clock at 245.76MHz. See the block diagram above for detailed clock tree. The clock are slightly over constraint to 125 MHz and 250 MHz.

.. code:: xdc

   create_clock -name rx_ref_clk   -period  8 [get_ports trx_ref_clk_p]
   create_clock -name tx_div_clk   -period  4 [get_pins i_system_wrapper/system_i/util_fmcomms11_xcvr/inst/i_xch_0/i_gtxe2_channel/TXOUTCLK]
   create_clock -name rx_div_clk   -period  8 [get_pins i_system_wrapper/system_i/util_fmcomms11_xcvr/inst/i_xch_0/i_gtxe2_channel/RXOUTCLK]

Building the HDL Project
------------------------

When building the project, you should always use the recommended version of the tools for the specific :doc:`release </wiki-migration/resources/fpga/docs/releases>`. In this example, we'll use release 2019_r1, which has Vivado 2018.3 as the recommended version. If you're using different Vivado versions, it's possible that there are slight modifications on how the synthesis works, or different Xilinx IP changes, which affect the system functionality.

::

   mkdir adi
   cd adi
   git clone https://github.com/analogdevicesinc/hdl.git
   cd hdl/
   git status ## check for everything, including branch name
   git checkout hdl_2019_r1 ## change to the hdl_2019_r1 branch
   make -C projects/fmcomms11/zc706

HDL Downloads
-------------

.. admonition:: Download
   :class: download

   
   -


   
   |FMCOMMS11 HDL project|

Support
-------

.. hint::

   **Questions?** Feel free to ask your questions in EngineerZone support forums.

   
   -  :ez:`FPGA Reference Design <community/fpga>`
   


References
----------

.. note::

   
   -  :doc:`HDL Build Instructions </wiki-migration/resources/fpga/docs/build>`
      \* :doc:`JESD204 Framework </wiki-migration/resources/fpga/peripherals/jesd204>`
   -  :doc:`Using and modifying the HDL designs </wiki-migration/resources/fpga/docs/tips>`
      \* :doc:`Generic JESD204 block design </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`


.. |FMCOMMS11 HDL project| image:: https://wiki.analog.com/_media/:git-hdl:`projects/fmcomms11`
