.. warning:: Conversion failed for ``resources/fpga/docs/axi_gpreg``

   Reason: pandoc error: Error at "/tmp/tmppnd9zwl6.txt" (line 34, column 1):
expecting inline
not found
|              | '' gp_ioenb_* '' | ''output [31:0]'' | IO enable port(generic output) |
^

.. code-block:: text

   ====== AXI GPREG IP core ======
   
   The [[https://github.com/analogdevicesinc/hdl/tree/master/library/axi_gpreg|axi_gpreg]] IP core can be used as a GPIO interface or as a generic register map for custom IPs/subsystems.
   
   ===== Features =====
   
     * AXI based configuration
     * 8 IO channels (enb, output and input) of 32 bit each
     * 8 clock monitors
     * User reset
     * Destination clock domain (internal CDC)
   
   ==== Configuration Parameters ====
   
   ^ Name ^ Description ^ Default Value^
   | ''ID'' | Core ID should be unique for each IP in the system | 0 |
   | ''DESTINATION_CLK'' | Enables CDC from PS clk to destination clk | 1 |
   | ''STAND_ALONE'' | If zero, the IP can be integrated in another IP controlled by axi  | 1 |
   | ''NUM_OF_IO'' | Number of input and output interfaces | 8 |
   | ''NUM_OF_CLK_MONS'' | Number of clocks to be monitor | 8 |
   | ''BUF_ENABLE_0'' | Enables BUFG for clock monitor 0  | 1 |
   | ''BUF_ENABLE_1'' | Enables BUFG for clock monitor 1  | 1 |
   | ''BUF_ENABLE_2'' | Enables BUFG for clock monitor 2  | 1 |
   | ''BUF_ENABLE_3'' | Enables BUFG for clock monitor 3  | 1 |
   | ''BUF_ENABLE_4'' | Enables BUFG for clock monitor 4  | 1 |
   | ''BUF_ENABLE_5'' | Enables BUFG for clock monitor 5  | 1 |
   | ''BUF_ENABLE_6'' | Enables BUFG for clock monitor 6  | 1 |
   | ''BUF_ENABLE_7'' | Enables BUFG for clock monitor 7  | 1 |
   
   ==== Signal and Interface Pins ====
   
   ^ Interface ^ Pin ^ Type ^ Description ^
   | ''Destination clock'' | ** Clock signal ** |||
   |              | ''clk'' | ''input'' | Reference clock |
   | ''Destination reset'' | ** Reset signal ** |||
   |              | ''reset_out'' | ''output'' | User reset synchronous to destination clock domain |
   | ''GP IO interfaces'' | ** interface signals ** |||0
   |              | '' gp_ioenb_* '' | ''output [31:0]'' | IO enable port(generic output) |
   |              | '' gp_out_*   '' | ''output [31:0]'' | Generic output port |
   |              | '' gp_in_*    '' | ''input [31:0]'' | Generic input port  |
   | ''Clock monitors'' | **  ** |||
   |              | '' d_clk_*    '' | ''input'' | Input to clock monitor * |
   | ''Pcore interface'' | ** Pcore interface ** |||
   |              | '' up_clk_ext   '' | '' input        '' | uP clk signal. |
   |              | '' up_rstn_ext  '' | '' input        '' | uP resetn signal. |
   |              | '' up_wreq_ext  '' | '' input        '' | uP write request signal. |
   |              | '' up_waddr_ext '' | '' input[16:0]  '' | uP write address signal. |
   |              | '' up_wdata_ext '' | '' input[31:0]  '' | uP write data signal. |
   |              | '' up_wack_ext  '' | '' output       '' | uP write acknoladge signal. |
   |              | '' up_rreq_ext  '' | '' input        '' | uP read request signal. |
   |              | '' up_raddr_ext '' | '' input[16:0]  '' | uP read address signal. |
   |              | '' up_rdata_ext '' | '' output[31:0] '' | uP read data signal. |
   |              | '' up_rack_ext  '' | '' output       '' | uP read acknoldge signal. |
   | ''s_axi'' | ** AXI Memory Map interface ** |||
   
   ==== Register Map ====
   
   |< 100% 5% 5% 5% 25% 5% 5% 50% >|
   |Address ||Bits |Name |Type |Default |Description |
   |DWORD |BYTE |::: |::: |::: |::: |::: |
   ^0x0000 ^0x0000 ^REG_VERSION ^^^^Version Register. ^
   | | |[31:0] |VERSION[31:0] |RO |0x00000100 |Version number. Unique to all cores. |
   ^0x0001 ^0x0004 ^REG_ID ^^^^ID Register ^
   | | |[31:0] |ID[31:0] |RO |0x00000000 |Instance identifier number. |
   ^0x0002 ^0x0008 ^REG_SCRACH ^^^^Scratch Register. ^
   | | |[31:0] |ID[31:0] |RW |0x00000000 |Scratch Register. |
   ^0x0003 ^0x000c ^REG_RESET ^^^^Core out reset. ^
   | | |[0] |RESET[0] |RW |0x0 |Reset Register. |
   ^0x0100 ^0x0400 ^REG_GP_IOENB ^^^^General purpose IO enable register. ^
   | | |[31:0] |GP_IO_ENB[31:0] |RW |0x00000000 |General purpose enable register.  |
   ^0x0101 ^0x0404 ^REG_GP_OUT_0 ^^^^General purpose output register. ^
   | | |[31:0] |GP_OUT_0[31:0] |RW |0x00000000 |General purpose output/control register.  |
   ^0x0102 ^0x0408 ^REG_GP_IN_0 ^^^^General purpose input register. ^
   | | |[31:0] |GP_IN_0[31:0] |RW |0x00000000 |General purpose input/status register.  |
   ^0x0110 ^0x0440 ^REG_GP_IOENB_1 ^^^^General purpose IO enable register. ^
   ^0x0111 ^0x0444 ^REG_GP_OUT_1 ^^^^General purpose out register. ^
   ^0x0112 ^0x0448 ^REG_GP_IN_1 ^^^^General purpose in register. ^
   ^0x0170 ^0x05c0 ^REG_GP_IOENB_7 ^^^^General purpose IO enable register. ^
   ^0x0171 ^0x05c4 ^REG_GP_OUT_7 ^^^^General purpose out register. ^
   ^0x0172 ^0x05c8 ^REG_GP_IN_7 ^^^^General purpose in register. ^
   ^0x0200 ^0x0800 ^REG_CM_RESET ^^^^Reset register ^
   | | |[0] |CM_RESET_N |RW |0x0 |Reset register (write a 0x01 to bring core out of reset). |
   ^0x0201 ^0x0804 ^REG_CM_COUNT ^^^^Clock count register ^
   | | |[31:0] |CM_CLK_COUNT |RO |0x00000000 |If active, the register contains the clock 0 frequency. This is relative to the processor clock and in many cases is 100MHz. The number is represented as unsigned 16.16 format. Assuming a 100MHz processor clock the minimum is 1.523kHz and maximum is 6.554THz. The actual interface clock is CLK_FREQ * CLK_RATIO (see below). Note that the actual sampling clock may not be the same as the interface clock- software must consider device specific implementation parameters to calculate the final sampling clock. |
   ^0x0210 ^0x0840 ^REG_RESER_CLK_FREQ_1 ^^^^Reset clock 0 frequency ^
   ^0x0211 ^0x0844 ^REG_CLK_FREQ_1 ^^^^Clock 0 frequency ^
   ^0x0220 ^0x0880 ^REG_RESER_CLK_FREQ_2 ^^^^Reset clock 0 frequency ^
   ^0x0221 ^0x0884 ^REG_CLK_FREQ_2 ^^^^Clock 2 frequency, similar to register 0x0200 (Clock 0 frequency) ^
   ^0x0270 ^0x09c0 ^REG_RESER_CLK_FREQ_7 ^^^^Reset clock 0 frequency ^
   ^0x0221 ^0x0884 ^REG_CLK_FREQ_7 ^^^^Clock 7 frequency, similar to register 0x0200 (Clock 0 frequency) ^
   ^Mon Nov  9 09:24:50 2020 ^^^^^^
   
   
   {{navigation HDL User Guide#ip_cores|IP cores#hdl|Main page#tips|Using and modifying the HDL design}}
