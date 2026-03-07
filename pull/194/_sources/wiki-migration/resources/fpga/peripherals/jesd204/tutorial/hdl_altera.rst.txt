DAQ2 HDL Project for Altera
===========================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/daq2_altera.svg
   :alt: Altera HDL Block Diagram
   :width: 800px

The reference design is a processor based embedded system. The sources are split into three different folders:

-  base design for the carrier board, :git-hdl:`/projects/common <projects/common>` where all generic peripherals are instantiated. Here we do most of the PS8 configuration, add SPI, I2C and GPIOs. In some cases, we have scripts to instantiate also the PL DDR as ADC offload memory or DAC offload memory
-  base design for the evaluation board, :git-hdl:`/projects/daq2/common <projects/daq2/common>`, where all the IPs to control the DAQ2 evaluation board are instantiated, in a way in which it can be integrated with most of the carriers that we support
-  specific design for the project, in our case the A10SOC :git-hdl:`/projects/daq2/a10soc <projects/daq2/a10soc>`. Here, we source the carrier board configuration, then the evaluation board configuration and then we do some specific parameter modification, if required. In this folder, the constraints and ``system_top.v`` are also defined.

The reference design is a processor based (ARM or Nios2) embedded system. A functional block diagram of the system is given above. The shared transceivers are followed by the individual JESD204B and ADC/DAC IP cores. The cores are programmable through an AXI-lite interface.

The digital interface consists of 4 transmit and 4 receive lanes running at 10Gbps, by default. The transceivers interface the ADC/DAC cores at 128bits@250MHz. The data is sent or received based on the configuration of separate transmit and receive chains.

When using Qsys, implementing JESD204B protocol requires several IPs. AVL_XCVR is a wrapper which instantiates all the required IPs and configures them according to the desired data rate. One AVL_XCVR must be instantiated for the transmit path and one for the receive path. It adds clock bridges, PLL and reconfiguration IP, proper reset, lane PLL for the transmit path, a JESD204B IP instantiating the JESD204B base and a JESD204B IP for each lane instantiating the PHY.

One important aspect for AD-FMCDAQ2-EBZ is that the reference clock needed for the FPGA transceiver calibration is generated only after the AD9523-1 clock generator is configured The programming is done only after the FPGA is configured and software is running. Because of this, the software needs to perform a transceiver re-calibration after the transceiver reference clock is stable and before taking AXI_XCVR cores out of reset.

Project Flow
------------

The entry point for project creation is ``system_project.tcl``. Some support scripts are first loaded then the project is created. Based on the suffix of the project, the carrier board is automatically detected. The constraint files and custom modules instantiated directly in the system_top module must be added to the project files list.

.. code:: tcl

   source ../../scripts/adi_env.tcl
   source ../../scripts/adi_project_alt.tcl

   adi_project_altera daq2_a10soc

   source $ad_hdl_dir/projects/common/a10soc/a10soc_system_assign.tcl
   source $ad_hdl_dir/projects/common/a10soc/a10soc_plddr4_assign.tcl

   set_global_assignment -name VERILOG_FILE ../common/daq2_spi.v

   .
   .
   .

   execute_flow -compile

Because transceiver sharing is used in this design, explicit assignments are needed.

.. code:: tcl

   # Merge RX and TX into single transceiver
   for {set i 0} {$i < 4} {incr i} {
     set_instance_assignment -name XCVR_RECONFIG_GROUP xcvr_${i} -to rx_serial_data[${i}]
     set_instance_assignment -name XCVR_RECONFIG_GROUP xcvr_${i} -to tx_serial_data[${i}]
   }

Some parameters will be defined in the first part, which will configure the ADC/DAC FIFOs. These are part of the systems in which the DDR throughput is not enough to keep up with the ADC/DAC data rates. When the project is created, ``system_qsys.tcl`` is sourced. ``System_qsys.tcl`` will generate the Qsys system. The resulting system will be instantiated in the system_top module.

.. code:: tcl

   set dac_fifo_name avl_ad9144_fifo
   set dac_fifo_address_width 10
   set dac_data_width 128
   set dac_dma_data_width 128

The next step is to instantiate the A10SOC base design:

.. code:: tcl

   source $ad_hdl_dir/projects/common/a10soc/a10soc_system_qsys.tcl

If ADC/DAC FIFOs implemented in the PL DDR will be used in the system, the corresponding tcl file must be sourced.

.. code:: tcl

   source $ad_hdl_dir/projects/common/a10soc/a10soc_plddr4_dacfifo_qsys.tcl

The next step is to source the DAQ2 specific design.

.. code:: tcl

   source ../common/daq2_qsys.tcl

DAQ2 Design
-----------

Physical/Data Link Layer
~~~~~~~~~~~~~~~~~~~~~~~~

The ADI_JESD204 IP is a wrapper which instantiates all the submodules implementing the physical and data Link layers. It covers all internal clock and reset generation for the transceivers. For some FPGAs, the HARD PCS componend doesn't run at maximum speeds, so a SOFT_PCS implementation is available. If lane swapping is required, it can be selected as a parameter.

.. code:: tcl

   add_instance ad9144_jesd204 adi_jesd204
   set_instance_parameter_value ad9144_jesd204 {ID} {0}
   set_instance_parameter_value ad9144_jesd204 {TX_OR_RX_N} {1}
   set_instance_parameter_value ad9144_jesd204 {LANE_RATE} {10000}
   set_instance_parameter_value ad9144_jesd204 {REFCLK_FREQUENCY} {333.333333}
   set_instance_parameter_value ad9144_jesd204 {LANE_MAP} {0 3 1 2}
   set_instance_parameter_value ad9144_jesd204 {SOFT_PCS} {true}

   --clock used for reconfiguring the IP
   add_connection sys_clk.clk ad9144_jesd204.sys_clk
   add_connection sys_clk.clk_reset ad9144_jesd204.sys_resetn
   add_interface tx_ref_clk clock sink
   set_interface_property tx_ref_clk EXPORT_OF ad9144_jesd204.ref_clk
   add_interface tx_serial_data conduit end
   set_interface_property tx_serial_data EXPORT_OF ad9144_jesd204.serial_data
   add_interface tx_sysref conduit end
   set_interface_property tx_sysref EXPORT_OF ad9144_jesd204.sysref
   add_interface tx_sync conduit end
   set_interface_property tx_sync EXPORT_OF ad9144_jesd204.sync

   # ad9680-xcvr
   Instantiation of the RX JESD204 IP
   add_instance ad9680_jesd204 adi_jesd204
   set_instance_parameter_value ad9680_jesd204 {ID} {1}
   set_instance_parameter_value ad9680_jesd204 {TX_OR_RX_N} {0}
   set_instance_parameter_value ad9680_jesd204 {LANE_RATE} {10000.0}
   set_instance_parameter_value ad9680_jesd204 {REFCLK_FREQUENCY} {333.333333}
   set_instance_parameter_value ad9680_jesd204 {NUM_OF_LANES} {4}
   set_instance_parameter_value ad9680_jesd204 {SOFT_PCS} {true}

   add_connection sys_clk.clk ad9680_jesd204.sys_clk
   add_connection sys_clk.clk_reset ad9680_jesd204.sys_resetn
   add_interface rx_ref_clk clock sink
   set_interface_property rx_ref_clk EXPORT_OF ad9680_jesd204.ref_clk
   add_interface rx_serial_data conduit end
   set_interface_property rx_serial_data EXPORT_OF ad9680_jesd204.serial_data
   add_interface rx_sysref conduit end
   set_interface_property rx_sysref EXPORT_OF ad9680_jesd204.sysref
   add_interface rx_sync conduit end
   set_interface_property rx_sync EXPORT_OF ad9680_jesd204.sync

Transport Layer
~~~~~~~~~~~~~~~

The transport layer peripherals are responsible for converter specific data framing and de-framing and provide a generic FIFO interface to the rest of the system.

.. code:: tcl

   add_instance axi_ad9144_core axi_ad9144
   set_instance_parameter_value axi_ad9144_core {QUAD_OR_DUAL_N} {0}

   add_connection ad9144_jesd204.link_clk axi_ad9144_core.if_tx_clk
   add_connection axi_ad9144_core.if_tx_data ad9144_jesd204.link_data
   add_connection sys_clk.clk_reset axi_ad9144_core.s_axi_reset
   add_connection sys_clk.clk axi_ad9144_core.s_axi_clock

   add_instance axi_ad9680_core axi_ad9680

   add_connection ad9680_jesd204.link_clk axi_ad9680_core.if_rx_clk
   add_connection ad9680_jesd204.link_sof axi_ad9680_core.if_rx_sof
   add_connection ad9680_jesd204.link_data axi_ad9680_core.if_rx_data
   add_connection sys_clk.clk_reset axi_ad9680_core.s_axi_reset
   add_connection sys_clk.clk axi_ad9680_core.s_axi_clock

Additional IPs
~~~~~~~~~~~~~~

For a complete system, we use additional modules to transfer data. The transport layer transfers data continuously from/to the ADC/DAC. CPACK/Upack will only send the enabled channels to the DMA which in turn will transfer it to the system memory. Depending on system specifics, data offload FIFOs may be inserted between upack/cpack and the DMA. When a FIFO is used, the DMA connection to the DDR can run at a lower speed, as data capture cannot be done continuously.

.. code:: tcl

   add_instance util_ad9144_upack util_upack
   set_instance_parameter_value util_ad9144_upack {CHANNEL_DATA_WIDTH} {64}
   set_instance_parameter_value util_ad9144_upack {NUM_OF_CHANNELS} {2}

   add_connection ad9144_jesd204.link_clk util_ad9144_upack.if_dac_clk
   add_connection axi_ad9144_core.dac_ch_0 util_ad9144_upack.dac_ch_0
   add_connection axi_ad9144_core.dac_ch_1 util_ad9144_upack.dac_ch_1

   add_interface tx_fifo_bypass conduit end
   set_interface_property tx_fifo_bypass EXPORT_OF avl_ad9144_fifo.if_bypass

   add_connection ad9144_jesd204.link_clk avl_ad9144_fifo.if_dac_clk
   add_connection ad9144_jesd204.link_reset avl_ad9144_fifo.if_dac_rst
   add_connection util_ad9144_upack.if_dac_valid avl_ad9144_fifo.if_dac_valid
   add_connection avl_ad9144_fifo.if_dac_data util_ad9144_upack.if_dac_data
   add_connection avl_ad9144_fifo.if_dac_dunf axi_ad9144_core.if_dac_dunf

   add_instance axi_ad9144_dma axi_dmac
   set_instance_parameter_value axi_ad9144_dma {DMA_DATA_WIDTH_SRC} {128}
   set_instance_parameter_value axi_ad9144_dma {DMA_DATA_WIDTH_DEST} {128}
   set_instance_parameter_value axi_ad9144_dma {DMA_2D_TRANSFER} {0}
   set_instance_parameter_value axi_ad9144_dma {DMA_LENGTH_WIDTH} {24}
   set_instance_parameter_value axi_ad9144_dma {AXI_SLICE_DEST} {0}
   set_instance_parameter_value axi_ad9144_dma {AXI_SLICE_SRC} {0}
   set_instance_parameter_value axi_ad9144_dma {SYNC_TRANSFER_START} {0}
   set_instance_parameter_value axi_ad9144_dma {CYCLIC} {1}
   set_instance_parameter_value axi_ad9144_dma {DMA_TYPE_DEST} {1}
   set_instance_parameter_value axi_ad9144_dma {DMA_TYPE_SRC} {0}
   set_instance_parameter_value axi_ad9144_dma {FIFO_SIZE} {16}

   add_connection sys_dma_clk.clk avl_ad9144_fifo.if_dma_clk
   add_connection sys_dma_clk.clk_reset avl_ad9144_fifo.if_dma_rst
   add_connection sys_dma_clk.clk axi_ad9144_dma.if_m_axis_aclk
   add_connection axi_ad9144_dma.if_m_axis_valid avl_ad9144_fifo.if_dma_valid
   add_connection axi_ad9144_dma.if_m_axis_data avl_ad9144_fifo.if_dma_data
   add_connection axi_ad9144_dma.if_m_axis_last avl_ad9144_fifo.if_dma_xfer_last
   add_connection axi_ad9144_dma.if_m_axis_xfer_req avl_ad9144_fifo.if_dma_xfer_req
   add_connection avl_ad9144_fifo.if_dma_ready axi_ad9144_dma.if_m_axis_ready
   add_connection sys_clk.clk_reset axi_ad9144_dma.s_axi_reset
   add_connection sys_clk.clk axi_ad9144_dma.s_axi_clock
   add_connection sys_dma_clk.clk_reset axi_ad9144_dma.m_src_axi_reset
   add_connection sys_dma_clk.clk axi_ad9144_dma.m_src_axi_clock

   add_instance util_ad9680_cpack util_cpack
   set_instance_parameter_value util_ad9680_cpack {CHANNEL_DATA_WIDTH} {64}
   set_instance_parameter_value util_ad9680_cpack {NUM_OF_CHANNELS} {2}

   add_connection sys_clk.clk_reset util_ad9680_cpack.if_adc_rst
   add_connection ad9680_jesd204.link_clk util_ad9680_cpack.if_adc_clk
   add_connection axi_ad9680_core.adc_ch_0 util_ad9680_cpack.adc_ch_0
   add_connection axi_ad9680_core.adc_ch_1 util_ad9680_cpack.adc_ch_1

   add_instance ad9680_adcfifo util_adcfifo
   set_instance_parameter_value ad9680_adcfifo {ADC_DATA_WIDTH} {128}
   set_instance_parameter_value ad9680_adcfifo {DMA_DATA_WIDTH} {128}
   set_instance_parameter_value ad9680_adcfifo {DMA_ADDRESS_WIDTH} {16}

   add_connection sys_clk.clk_reset ad9680_adcfifo.if_adc_rst
   add_connection ad9680_jesd204.link_clk ad9680_adcfifo.if_adc_clk
   add_connection util_ad9680_cpack.if_adc_valid ad9680_adcfifo.if_adc_wr
   add_connection util_ad9680_cpack.if_adc_data ad9680_adcfifo.if_adc_wdata
   add_connection sys_dma_clk.clk ad9680_adcfifo.if_dma_clk
   add_connection sys_dma_clk.clk_reset ad9680_adcfifo.if_adc_rst

   add_instance axi_ad9680_dma axi_dmac
   set_instance_parameter_value axi_ad9680_dma {DMA_DATA_WIDTH_SRC} {128}
   set_instance_parameter_value axi_ad9680_dma {DMA_DATA_WIDTH_DEST} {128}
   set_instance_parameter_value axi_ad9680_dma {DMA_LENGTH_WIDTH} {24}
   set_instance_parameter_value axi_ad9680_dma {DMA_2D_TRANSFER} {0}
   set_instance_parameter_value axi_ad9680_dma {SYNC_TRANSFER_START} {0}
   set_instance_parameter_value axi_ad9680_dma {CYCLIC} {0}
   set_instance_parameter_value axi_ad9680_dma {DMA_TYPE_DEST} {0}
   set_instance_parameter_value axi_ad9680_dma {DMA_TYPE_SRC} {1}

   add_connection sys_dma_clk.clk axi_ad9680_dma.if_s_axis_aclk
   add_connection ad9680_adcfifo.if_dma_wr axi_ad9680_dma.if_s_axis_valid
   add_connection ad9680_adcfifo.if_dma_wdata axi_ad9680_dma.if_s_axis_data
   add_connection ad9680_adcfifo.if_dma_wready axi_ad9680_dma.if_s_axis_ready
   add_connection ad9680_adcfifo.if_dma_xfer_req axi_ad9680_dma.if_s_axis_xfer_req
   add_connection ad9680_adcfifo.if_adc_wovf axi_ad9680_core.if_adc_dovf
   add_connection sys_clk.clk_reset axi_ad9680_dma.s_axi_reset
   add_connection sys_clk.clk axi_ad9680_dma.s_axi_clock
   add_connection sys_dma_clk.clk_reset axi_ad9680_dma.m_dest_axi_reset
   add_connection sys_dma_clk.clk axi_ad9680_dma.m_dest_axi_clock

Transceiver Reconfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reconfiguration IP for all the transceiver channels. Channels have a TX port and an RX port, which may affect each other when reconfiguration is performed.

.. code:: tcl

   for {set i 0} {$i < 4} {incr i} {
     add_instance avl_adxcfg_${i} avl_adxcfg
     add_connection sys_clk.clk avl_adxcfg_${i}.rcfg_clk
     add_connection sys_clk.clk_reset avl_adxcfg_${i}.rcfg_reset_n
     add_connection avl_adxcfg_${i}.rcfg_m0 ad9144_jesd204.phy_reconfig_${i}
     add_connection avl_adxcfg_${i}.rcfg_m1 ad9680_jesd204.phy_reconfig_${i}
   }

CPU Address Allocation
~~~~~~~~~~~~~~~~~~~~~~

.. code:: tcl

   ad_cpu_interconnect 0x00020000 ad9144_jesd204.link_reconfig
   ad_cpu_interconnect 0x00024000 ad9144_jesd204.link_management
   ad_cpu_interconnect 0x00025000 ad9144_jesd204.link_pll_reconfig
   ad_cpu_interconnect 0x00026000 ad9144_jesd204.lane_pll_reconfig
   ad_cpu_interconnect 0x00028000 avl_adxcfg_0.rcfg_s0
   ad_cpu_interconnect 0x00029000 avl_adxcfg_1.rcfg_s0
   ad_cpu_interconnect 0x0002a000 avl_adxcfg_2.rcfg_s0
   ad_cpu_interconnect 0x0002b000 avl_adxcfg_3.rcfg_s0
   ad_cpu_interconnect 0x0002c000 axi_ad9144_dma.s_axi
   ad_cpu_interconnect 0x00030000 axi_ad9144_core.s_axi

   ad_cpu_interconnect 0x00040000 ad9680_jesd204.link_reconfig
   ad_cpu_interconnect 0x00044000 ad9680_jesd204.link_management
   ad_cpu_interconnect 0x00045000 ad9680_jesd204.link_pll_reconfig
   ad_cpu_interconnect 0x00048000 avl_adxcfg_0.rcfg_s1
   ad_cpu_interconnect 0x00049000 avl_adxcfg_1.rcfg_s1
   ad_cpu_interconnect 0x0004a000 avl_adxcfg_2.rcfg_s1
   ad_cpu_interconnect 0x0004b000 avl_adxcfg_3.rcfg_s1
   ad_cpu_interconnect 0x0004c000 axi_ad9680_dma.s_axi
   ad_cpu_interconnect 0x00050000 axi_ad9680_core.s_axi

High Perfomance Port Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: tcl

   ad_dma_interconnect axi_ad9144_dma.m_src_axi
   ad_dma_interconnect axi_ad9680_dma.m_dest_axi

Interrupts
~~~~~~~~~~

.. code:: tcl

   ad_cpu_interrupt 8 ad9680_jesd204.interrupt
   ad_cpu_interrupt 9 ad9144_jesd204.interrupt
   ad_cpu_interrupt 10 axi_ad9680_dma.interrupt_sender
   ad_cpu_interrupt 11 axi_ad9144_dma.interrupt_sender

Constraints
-----------

The reference clocks frequency must be defined in the constraints:

.. code:: tcl

   create_clock -period  "3.000 ns"  -name rx_ref_clk          [get_ports {rx_ref_clk}]
   create_clock -period  "3.000 ns"  -name tx_ref_clk          [get_ports {tx_ref_clk}]

Building the HDL Project
------------------------

When building the project, you should always use the recommended version of the tools for the specific :doc:`release </wiki-migration/resources/fpga/docs/releases>`. In this example, we'll use release 2018_r1, which has Quartus 17.1.1 as the recommended version. If you're using different Quartus versions, it's possible that there are slight modifications on how the synthesis works, or different Intel IP changes, which affect the system functionality.

::

   git clone https://github.com/analogdevicesinc/hdl.git
   cd hdl/
   git status ## check for everything, including branch name
   git checkout hdl_2018_r1 ## change to the hdl_2018_r1 branch
   make -C projects/daq2/a10soc

References
----------

| :doc:`/wiki-migration/resources/fpga/docs/build`
