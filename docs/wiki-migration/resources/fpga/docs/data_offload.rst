.. warning:: Conversion failed for ``resources/fpga/docs/data_offload``

   Reason: pandoc error: Error at "/tmp/tmpfjbjcwm3.txt" (line 110, column 1):
expecting inline
not found
^ 0x0080 ^ 0x0200 ^ FSM_DBG          |||||
^

.. code-block:: text

   ====== Data Offload Engine HDL IP Core ======
   
   <note important>We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/data_offload/index.html</note>
   
   The data offload engine is, in essence, a clock-domain crossing store-and-forward buffer (or FIFO) with some extra features useful in bursty RF applications. More specifically, it was designed to sit between a DMA and DAC for the TX and ADC and DAC for the RX path of a digital RF chain. This is reflected in the synthesis settings of the device, that also enable or disable certain other settings of features where appropriate. For example in the receive path cyclic operation isn't supported.
   
   ===== Features =====
   
     * Configurable storage unit with support for Block-RAM and External DRAM (Up to 16 GiB) or external High Bandwidth Memory (HBM)
     * Configurable interface width and rates
     * External timing synchronization for precisely timed buffers (For example in combination with the [[resources:fpga:docs:axi_tdd|Timing-Division Duplexing Controller]])
     * Cyclic and oneshot store and forward operation
     * Bypass mode to completely bypass all features and act as a pure CDC fifo
     * Many settings configurable at runtime via MM AXI4-Lite bus
   
   <note>The data offload does NOT support, in its current state, continuous streaming except when in bypass mode (Thus disabling all other functionality).</note>
   
   ===== Utilization =====
   
   Utilization is estimated without a storage unit. The size and complexity of your storage unit depends completely on the kind of storage in use. For Block-RAM the complexity will be dependent on the amount of storage, while with external DRAM a fixed cost can be assumed.
   
   ^ Device Family ^ LUTs ^ FFs ^
   | Xilinx Zynq UltraScale+ | 750 | 2000 |
   
   ===== Files =====
   
   ^ Name ^ Description ^
   | [[https://github.com/analogdevicesinc/hdl/blob/master/library/data_offload/|data_offload HDL]] | Verilog source for the peripheral. |
   | [[https://github.com/analogdevicesinc/linux/blob/master/drivers/misc/adi-axi-data-offload.c|adi-axi-data-offload.c]] | Linux Driver |
   | [[https://github.com/analogdevicesinc/linux/blob/master/arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9081-m8-l4-do.dts|xilinx/zynqmp-zcu102-rev10-ad9081-m8-l4-do.dts]] | Example device tree using the data offload |
   
   ===== Architecture and Theory of Operation =====
   
   The main role of our data paths, is to stream data from point A to point B in a particular system. There are always a SOURCE and a DESTINATION point, which can be a device (ADC or DAC), a DMA (for system memory) or any other data processing IP.
   
   In the context of Data Offload IP, we don't need to know who is the source and who is the destination. Both interface is a AXI4 Stream interface, which can be supported in both Xilinx's an Intel's architecture, and can be connected to any device core or DMA.
   
   The storage unit is connected to the Data Offload controller via two FIFO interface. This way the same controller can be used for various storage solutions. (BRAM, URAM, external memory etc.)
   
   ===== Block Diagram =====
   
   ==== Local Storage ====
   
   {{:resources:fpga:docs:data_offload_bd.png|}}
   
   ==== External Storage ====
   
   {{:resources:fpga:docs:data_offload_ddr_bd.png|}}
   
   ===== Synthesis Configuration Parameters =====
   
   ^ Name ^ Description ^ Default ^
   | ''ID'' | Instance identification number. | 0 |
   | ''MEM_TYPE'' | Define the used storage type: 0: BlockRAM; 1: external DDR | 0 |
   | ''MEM_SIZE_LOG2'' | Define the log2 size of the storage element in bytes | 10 |
   | ''TX_OR_RXN_PATH'' | If set TX path enabled, otherwise RX | 1 |
   | ''SRC_DATA_WIDTH'' | The data width of the source interface | 64 |
   | ''DST_DATA_WIDTH'' | The data width of the destination interface | 64 |
   | ''DST_CYCLIC_EN'' | Enables CYCLIC mode for destinations like DAC | 0 |
   | ''AUTO_BRINUP'' | If enabled the IP runs automatically after bootup | 0 |
   | ''SYNC_EXT_ADD_INTERNAL_CDC '' | If enabled the CDC circuitry for the external sync signal is added | 0 |
   | ''HAS_BYPASS '' | If enabled the bypass circuitry is added | 0 |
   
   ===== Signal and Interface Pins =====
   
   ^ Interface ^ Pin ^ Type ^ Description ^
   | **Control Signals** ||||
   |              | ''s_axi_aclk''   | ''input''  | AXI4-Lite clock signal |
   |              | ''s_axi_aresetn'' | ''input'' | Control-Domain Reset Input |
   |              | ''s_axi''        |            | MM AXI4-Lite control interface |
   |              | ''init_req''     | ''input''  | Indicator that the signal source (e.g. DMA) intends to provide new data soon |
   |              | ''init_ack''     | ''output'' | Init acknowledgement |
   |              | ''sync_ext''     | ''input''  | External synchronization signal, with or without internal clock-domain crossing logic. Can be used to couple certain state machine transitions to external processes |
   |              | ''ddr_calib_done'' | ''input'' | Allows the user to read back status information about the DDR calibration status from software |
   | ** Source Domain ** ||||
   |              | ''s_axis_aclk''  | ''input''  | Source Domain Clock Signal Input |
   |              | ''s_axis''       | ''input''  | AXI4-Stream slave data input |
   | ** Destination Domain ** ||||
   |              | ''m_axis_aclk''  | ''input''  | Destination Domain Clock Signal Input |
   |              | ''m_axis''       | ''output'' | AXI4-Stream master output stream |
   
   
   ===== Register Map =====
   
   <hidden>
   
   |< 100% 5% 5% 5% 25% 5% 5% 50% >|
   |Address ||         Bits    | Name             | Type | Default    | Description |
   | DWORD  | BYTE   | :::     | :::              | :::  | :::        | :::         |
   ^ 0x0000 ^ 0x0000 ^ VERSION          |||||
   |        |        | [31:16] | MAJOR            |      |            |             |
   | :::    | :::    | [15:8]  | MINOR            |      |            |             |
   | :::    | :::    | [7:0]   | PATCH            |      |            |             |
   ^ 0x0001 ^ 0x0004 ^ PERIPHERAL_ID    |||||
   |        |        | [31:0]  | PERIPHERAL_ID    | RO   | 0x00000000 | Optional value provided at synthesis time to distinguish multiple instances |
   ^ 0x0002 ^ 0x0008 ^ SCRATCH          |||||
   |        |        | [31:0]  | SCRATCH          | RW   | 0x00000000 | Scratchpad, can be written to and read at will |
   ^ 0x0003 ^ 0x000c ^ IDENTIFICATION   |||||
   |        |        | [31:0]  | IDENTIFICATION   | RW   | 0x44414F46 | MAGIC peripheral identifier, can be used to verify that you're actually talking to a data offload |
   ^ 0x0004 ^ 0x0010 ^ SYNTHESIS_CONFIG |||||
   |        |        | [13: 8]   | MEM_SIZE_LOG2| RO   |            | Log2 of memory size in bytes|
   |        |        | [2:2]   | HAS_BYPASS | RO   |            | If not set the bypass logic is not implemented. |
   |        |        | [1:1]   | TX_OR_RXN_PATH   | RO   |            | If this device was configured for the TX path, this bit will be set to 1. Conversely, the bit will be 0 for the RX path. |
   | :::    | :::    | [0:0]   | MEMORY_TYPE      | RO   |            | This bit identifies the type of memory that was chosen during synthesis. A value of 1 identifies external memory, while a value of zero indicates that block ram was used |
   ^ 0x0007 ^ 0x001c ^ TRANSFER_LENGTH  |||||
   |        |        | [31:0]  | TRANSFER_LENGTH  | RW   |            | The transfer length register can be used to override the transfer length in RX mode in increments of 64 bytes |
   ^ 0x0020 ^ 0x0080 ^ MEM_PHY_STATE    |||||
   |        |        | [5:5]   | UNDERFLOW | RO   |            | Indicates that storage could not handle data rate during play. Available when core is in TX mode. |
   |        |        | [4:4]   | OVERFLOW | RO   |            | Indicates that storage could not handle data rate during capture. Available when core is in RX mode. |
   |        |        | [0:0]   | CALIB_COMPLETE   | RO   |            | Information about the memory phy for setups with external (DDR) storage. Indicates that the memory initialization and calibration have completed |
   ^ 0x0021 ^ 0x0084 ^ RESETN_OFFLOAD   |||||
   |        |        | [0:0]   | RESETN           | RW   |            | "Software Reset": Resets all the internal address registers and state machines |
   ^ 0x0022 ^ 0x0088 ^ CONTROL          |||||
   |        |        | [1:1]   | ONESHOT_EN       | RW   |            | Enables oneshot mode. This means that the data offload will only play a received buffer once, and then stop. This mode is useful when you want to use the data offload for its synchronization features, but don't need the repeating output. |
   | :::    | :::    | [0:0]   | OFFLOAD_BYPASS   | RW   |            | Enables bypass mode. In this mode pretty much *all* functionality of the data offload is bypassed, and the data offload will simply act as an async dual-port FIFO and forward your data stream. |
   ^ 0x0040 ^ 0x0100 ^ SYNC_TRIGGER     |||||
   |        |        | [0:0]   | SYNC_TRIGGER     | RW1C |            | Software trigger for software sync mode |
   ^ 0x0041 ^ 0x0104 ^ SYNC_CONFIG      |||||
   |        |        | [1:0]   | SYNC_CONFIG      | RW   |            | Synchronization mode: 0: auto, 1: external hardware trigger, 2: software trigger (See SYNC_TRIGGER), 3: RESERVED/FORBIDDEN VALUE.
   ^ 0x0080 ^ 0x0200 ^ FSM_DBG          |||||
   |        |        | [11:8]   | FSM_STATE_READ   | RO   |            | The current read / output FSM state. |
   | :::    | :::    | [4:0]   | FSM_STATE_WRITE  | RO   |            | The current write / input FSM state. |
   ^ 0x0081 ^ 0x0204 ^ SAMPLE_COUNT_LSB |||||
   
   </hidden>
   
   |< 100% 10em 10em >|
   ^ Access Type ^ Name ^ Description ^
   | RO | Read-only | Reads will return the current register value. Writes have no effect. |
   | RW | Read-write | Reads will return the current register value. Writes will change the current register value. |
   | RW1C | Write-1-to-clear | Reads will return the current register value. Writing the register will clear those bits of the register which were set to 1 in the value written. Bits are set by hardware. |
   | RW1S | Write-1-to-set | Reads will return the current register value. Writing the register will set those bits of the register which were set to 1 in the value written. Bits are cleared by hardware. |
   | V | Volatile | The V suffix indicates that the register is volatile and its content might change without software interaction. The value of registers without the volatile designation will not change without an explicit write done by software. |
   
   ===== Linux Driver =====
   
   The linux driver has two responsibilities:
   
     * Initialize the data offload on startup.
     * Integrate with cf_axi_dds to allow IIO to utilize the data offload for cyclic operation.
   
   The former of those two is covered by the device tree, which implements five options:
   
   <code>
   	axi_data_offload_tx: axi-data-offload-0@9c440000 {
   		compatible = "adi,axi-data-offload-1.0.a";
   		reg = <0x9c440000 0x10000>;
   		// adi,bringup;
   		// adi,oneshot;
   		// adi,bypass;
   		// adi,sync-config = <2>;
   		// adi,transfer-length = /bits/ 64 <0x10000>; // 2**16 bytes
   	};
   </code>
   
     * ''adi,bringup'' will automatically enable the data offload on startup. Note that this option isn't always necessary, because the HDL itself may have been synthesized with auto-bringup.
     * ''adi,oneshot'' configures the default mode of operation for TX data offloads. This will usually be overridden by the IIO buffer integration and thus doesn't have an effect in most situations.
     * ''adi,bypass'' enables bypass mode, i.e. disables all functionality and makes the data offload act like a small async fifo.
     * ''adi,sync-config'': The sync config determines how the synchronization mechanism should operate. More information about this value can be found in the register map.
     * ''adi,transfer-length'': This option is useful for RX instances, where the size of the receive buffer  can be reduced from the default (All available storage).
   
   The latter is addressed by the integration into [[linux.github>master/drivers/iio/frequency/cf_axi_dds.c|cf_axi_dds.c]] and [[linux.github>master/drivers/iio/frequency/cf_axi_dds_buffer_stream.c|cf_axi_dds_buffer_stream.c]], which allow the drivers to control the oneshot functionality of the data offload based on what was requested with the current IIO buffer, assuming bypass was disabled.
   
   {{navigation HDL User Guide#ip_cores|IP cores#hdl|Main page#tips|Using and modifying the HDL design}}
