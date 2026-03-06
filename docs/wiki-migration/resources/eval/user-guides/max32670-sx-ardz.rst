.. warning:: Conversion failed for ``resources/eval/user-guides/max32670-sx-ardz``

   Reason: pandoc error: Error at "/tmp/tmpemt54etd.txt" (line 343, column 1):
expecting inline
not found

^

.. code-block:: text

   ====== MAX32670-SX-ARDZ: Long Range Wireless Radio Development Platform  ======
   
   <WRAP round important 65%>
   **Notice:**
   This page has been fully migrated to GitHub.io and is no longer maintained on the Wiki. Please refer to the GitHub link below for the most current and accurate information.
   \\
   \\
   https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-max32sxwise-sl/max32670-sx-ardz/index.html
   \\
   \\
   If you would like to contribute updates to this document, please submit your suggestions via a Pull Request on the GitHub page.
   \\
   \\
   Thank you for your understanding, and we apologize for any inconvenience this transition may cause.
   
   </WRAP>
   
   ===== Overview =====
   The [[adi>MAX32670-SX-ARDZ]] base board features the MAX32670 high-reliability, ultralow power microcontroller based on Arm Cortex-M4 processor, and the SX1261 long range RF transceiver module.  
   \\
   \\
   The integrated RF transceiver supports a frequency range from 800 MHz up to 960 MHz, making it suitable for high-performance flexible platforms that wirelessly transmit encrypted data at long-range; enabling a wide range of IoT applications using ADI sensing solutions.  
   \\
   \\
   Due to its low power consumption, this module is ideal for devices running on small-sized batteries.  The integrated Arm Cortex®-M4 32-bit microcontroller can run entire RF stacks and has sufficient resources available to run user applications.
   
   {{:resources:eval:user-guides:lora-reference-design:max32670-sx-ardz_base_board.png?600|}}
   
   
   
   \\
   ==== Features ====
   
   <WRAP center box 65%>
   ^ MCU ^
   | Arm Cortex-M4 core with FPU up to 100 MHz |
   | 384 kB flash memory with error correction |
   | 160 kB SRAM (128 kB with ECC enabled), optionally preserved in lowest power modes |
   | Compatible RTC resolution for long range wireless radio application for protocol timeout management |
   ^ Security ^
   | Available secure boot |
   | Support cryptographic algorithms, including AES-128/192/256 |
   ^ Power ^
   | Ultralow power real time clock with integrated power switch |
   | With 300 nA power consumption during sleep mode |
   ^ Long Range Radio ^
   | Supports FSK, GFSK, MSK, GMSK, and long range FHSS modulations |
   | Power output: +15 dBm transmit peak power |
   | Programmable bit rate up to 62.5 kbps and 300 kbps |
   | Supports sub-GHz ISM bands from 800 MHz to 960 MHz |
   | High sensitivity: down to -148 dBm |
   
   </WRAP>
   
   
   \\
   ==== Applications ====
     * Smart meters
     * Supply chain and logistics
     * Building automation
     * Agricultural sensors
     * Smart cities
     * Retail store sensors
     * Asset tracking
     * Streetlights
     * Parking sensors
     * Environmental sensors
   
   \\
   ===== System Architecture =====
   \\
   {{ :resources:eval:user-guides:lora-reference-design:max32670-sx-ardz_block_diagram.png?800 |}}
   \\
   \\
   
   ----
   ====== Hardware Design ======
   In order to use this base board, all hardware settings such as the hardware peripheral connections, jumpers and UART switch configurations, power configurations, connectivity options, and the USB and programming connections are provided in this page. Links to the schematics and the layout files are also available below.
   
   
   \\
   ===== Components and Connections =====
   ==== Peripheral Connectors ====
   
   <WRAP indent>
   The following standard connectors are provided on the base board for customer to use with external add-on modules:
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670-sx-ardz_hardware_peripherals_top_view.png?800 |}}
   
   ^ Connector Name ^ Function^
   | DC Power Connector Header | Input range from +4 V to +6 V DC supply voltage |
   | Battery Holder | Battery holder for CR123A    |
   | Cortex SWD Header | Used for flash programming and debug interface; also, provides a virtual serial port connection to MAX32670 microcontroller |
   | PMOD_SPI | 12-pin SPI PMOD connector |
   | PMOD_I2C | 8-pin I2C PMOD connector |
   | ESP32 Connector | ESP32 Devkit V1 connector |
   | Arduino Connectors | Arduino Uno Rev3 compatible connectors |
   </WRAP>
   
   
   
   \\
   \\
   ==== MAX32670 MCU Pin Map ====
   \\
   <WRAP indent>
   The pin map for the [[adi>MAX32670]] is described in the table and its schematic diagram below.
   </WRAP>
   
   
   <WRAP center round box 76%>
   |	**Net Name**	|	**Pin**	|	**Name**	|		|
   | 	|	**UART**	|		|		|
   |	UART0A_RX_32670	|	20	|	 P0.8	|	P0.8/UART0A_RX/I2S0_SDO/TMR0B_I 	|
   |	UART0A_TX_32670	|	21	|	 P0.9	|	P0.9/UART0A_TX/I2S0_WS/TMR0B_O 	|
   |	UART0A_CTS_32670	|	22	|	 P0.10	|	P0.10/UART0A_CTS/I2S0_SCK/TMR1B_I/DIV_CLK_OUTB 	|
   |	UART0A_RTS_32670	|	23	|	 P0.11	|	P0.11/UART0A_RTS/I2S0_SDI/TMR1B_O 	|
   |	UART1A_RX_32670	|	17	|	 P0.28	|	P0.28/UART1A_RX/TMR2D_I 	|
   |	UART1A_TX_32670	|	18	|	 P0.29	|	P0.29/UART1A_TX/TMR2D_O	|
   |	UART1A_CTS_32670	|	19	|	 P0.30	|	P0.30/UART1A_CTS/TMR3D_I	|
   |		|		|		|		|
   |		|	**SPI**	|		|		|
   |	SPI0_MISO_32670	|	6	|	 P0.2	|	P0.2/SPI0_MISO/UART1B_RX/TMR1A_I 	|
   |	SPI0_MOSI_32670	|	7	|	 P0.3	|	P0.3/SPI0_MOSI/UART1B_TX/TMR1A_O 	|
   |	SPI0_SCK_32670	|	8	|	 P0.4	|	P0.4/SPI0_SCK/UART1B_CTS/TMR2A_I 	|
   |	SPI0_SS0_32670	|	9	|	 P0.5	|	P0.5/SPI0_SS0/UART1B_RTS/TMR2A_O/DIV_CLK_OUTA 	|
   |	SPI1_MISO_32670	|	26	|	 P0.14	|	P0.14/SPI1_MISO/UART2B_RX/TMR3B_I 	|
   |	SPI1_MOSI_32670	|	27	|	 P0.15	|	P0.15/SPI1_MOSI/UART2B_TX/TMR3B_O 	|
   |	SPI1_SCK_32670	|	28	|	 P0.16	|	P0.16/SPI1_SCK/UART2B_CTS/TMR0C_I 	|
   |	SPI1_SS0_32670	|	29	|	 P0.17	|	P0.17/SPI1_SS0/UART2B_RTS/TMR0C_O 	|
   |		|		|		|		|
   |		|	**I2C**	|		|		|
   |	I2C0_SCL_32670	|	10	|	 P0.6	|	P0.6/I2C0_SCL/LPTMR0_I/TMR3A_I 	|
   |	I2C0_SDA_32670	|	11	|	 P0.7	|	P0.7/I2C0_SDA/LPTMR0_O/TMR3A_O	|
   |	I2C1_SCL_32670	|	24	|	 P0.12	|	P0.12/I2C1_SCL/EXT_CLK2/TMR2B_I/EXT_CLK1 	|
   |	I2C1_SDA_32670	|	25	|	 P0.13	|	P0.13/I2C1_SDA/32KCAL/TMR2B_O/SPI1_SS0 	|
   |	I2C2_SCL_32670	|	30	|	 P0.18	|	P0.18/I2C2_SCL/TMR1C_I 	|
   |	I2C2_SDA_32670	|	31	|	 P0.19	|	P0.19/I2C2_SDA/TMR1C_O	|
   |		|		|		|		|
   |		|	**JTAG**	|		|		|
   |	SWDIO_32670	|	4	|	 P0.0	|	P0.0/SWDIO/TMR0A_I 	|
   |	SWDCLK_32670	|	5	|	 P0.1	|	P0.1/SWDCLK/TMR0A_O 	|
   |	SWDCLKB_32670	|	1	|	 P0.20	|	P0.20/CM4_RX/TMR2C_I/SWDCLKB 	|
   |	SWDIOB_32670	|	3	|	 P0.22	|	P0.22/LPTMR1_I/TMR3C_I/SWDIOB	|
   |		|		|		|		|
   |		|	**GPIO**	|		|		|
   |	P0_21_32670	|	2	|	 P0.21	|	P0.21/CM4_TX/TMR2C_O 	|
   |	P0_23_32670	|	12	|	 P0.23	|	P0.23/LPTMR1_O/TMR3C_O 	|
   |	P0_24_32670	|	13	|	 P0.24	|	P0.24/LPUART0_CTS/UART0B_RX/TMR0D_I 	|
   |	P0_25_32670	|	14	|	 P0.25	|	P0.25/LPUART0_RTS/UART0B_TX/TMR0D_O 	|
   |	P0_26_32670	|	15	|	 P0.26	|	P0.26/LPUART0_RX/UART0B_CTS/TMR1D_I 	|
   |	P0_27_32670	|	16	|	 P0.27	|	P0.27/LPUART0_TX/UART0B_RTS/TMR1D_O 	|
   |	RSTN_32670	|	35	|	RSTN	|	RSTN	|
   </WRAP>
   
   
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670_mcu_pin_map.png?500 |}}
   
   \\
   \\
   ==== ESP32 Connector Pin Map ====
   \\
   <WRAP indent>
   All connector pinouts for the ESP32 Development Board are described in the table and its schematic diagram below.
   </WRAP>
   
   
   <WRAP center left box 45%>
   
   |	**Pin Name**	|	**Pin Number**	|	**Pin Description**	|
   |	EN	|	1	|	P0_27_32670	|
   |	GPIO	|	2	|	P0_21_32670	|
   |	GPIO	|	3	|	P0_23_32670	|
   |	GPIO	|	4	|	P0_24_32670	|
   |	GPIO	|	5	|	P0_25_32670	|
   |	GPIO	|	6	|	P0_26_32670	|
   |	GPIO	|	7	|	I2C2_SDA_32670	|
   |	GPIO	|	8	|	I2C1_SCL_32670	|
   |	GPIO	|	9	|	I2C1_SDA_32670	|
   |	GPIO	|	10	|	I2C2_SCL_32670	|
   |	HSPI CLK	|	11	|	SPI0_SCK_32670	|
   |	HSPI MISO	|	12	|	SPI0_MISO_32670	|
   |	HSPI MOSI	|	13	|	SPI0_MOSI_32670	|
   |	GPIO	|	14	|		|
   |	GPIO	|	15	|		|
   |	GPIO	|	16	|		|
   |	GND	|	17	|	GND	|
   |	VIN	|	18	|	VOUT_3130(def)/VCC_31334	|
   
   </WRAP>
   
   <WRAP center right box 45%>
   
   |	**Pin Name**	|	**Pin Number**	|	**Pin Description**	|
   |	VSPI MOSI	|	1	|	SPI1_MOSI_32670	|
   |	I2C SCL	|	2	|	I2C0_SCL_32670	|
   |	UART 0 TX	|	3	|	UART0A_TX_32670	|
   |	UART 0 RX	|	4	|	UART0A_RX_32670	|
   |	I2C SDA	|	5	|	I2C0_SDA_32670	|
   |	VSPI MISO	|	6	|	SPI1_MISO_32670	|
   |	VSPI CLK	|	7	|	SPI1_SCK_32670	|
   |	VSPI CS0	|	8	|	SPI1_SS0_32670	|
   |	UART 2 TX	|	9	|	UART1A_TX_32670	|
   |	UART 2 RX	|	10	|	UART1A_RX_32670	|
   |	RTC	|	11	|	UART0A_CTS_32670	|
   |	RTC	|	12	|	UART0A_RTS_32670	|
   |	RTC	|	13	|	SPI0_SS0_32670	|
   |	RTC	|	14	|	UART1A_CTS_32670	|
   |	SDI	|	15	|		|
   |	SDO	|	16	|		|
   |	SCK	|	17	|		|
   |	3V3	|	18	|	VOUT_3130	|
   
   </WRAP>
   						
   {{ :resources:eval:user-guides:lora-reference-design:max32670_esp32_connectors_pin_map.png?600 |}}
   
   \\
   \\
   ==== Arduino Connector Pin Map ====
   
   <WRAP center round box 78%>
   |	**Net Name**	|	**Pin Number**	|	**Pin Name**	|	**Description**	|
   |	**P4**	|		|		|		|
   |	 --	|	1	|	NC	|		|
   |	1V8_SSB0/3V3_SSB3(def)	|	2	|	IOREF	|	POW	|
   |	RSTN_32670	|	3	|	RESET	|	AVR/POW	|
   |	VOUT_3130	|	4	|	3.3V	|	POW	|
   |	 --	|	5	|	5V	|	POW	|
   |	 --	|	6	|	GND	|	POW	|
   |	 --	|	7	|	GND	|	POW	|
   |	1V8_SSB0/0V7_SSB2/3V3_SSB3(def)/VCC_31334	|	8	|	VIN	|	POW	|
   |	**P3**	|		|		|		|
   |	P0_21_32670	|	1	|	A0/PC0	|	AVR/DIG/ANA	|
   |	P0_23_32670	|	2	|	A1/PC1	|	AVR/DIG/ANA	|
   |	P0_24_32670	|	3	|	A2/PC2	|	AVR/DIG/ANA	|
   |	P0_25_32670	|	4	|	A3/PC3	|	AVR/DIG/ANA	|
   |	I2C1_SDA_32670(def)/I2C2_SDA_32670	|	5	|	A4/PC4/SDA	|	AVR/DIG/ANA/I2C	|
   |	I2C1_SCL_32670(def)/I2C2_SCL_32670	|	6	|	A5/PC5/SCL	|	AVR/DIG/ANA/I2C	|
   |	**P6**	|		|		|		|
   |	I2C0_SCL_32670	|	1	|	PC5/SCL	|	AVR/DIG/ANA/I2C	|
   |	I2C0_SDA_32670	|	2	|	PC4/SDA	|	AVR/DIG/ANA/I2C	|
   |	 --	|	3	|	AREF	|	POW	|
   |	 --	|	4	|	GND	|	POW	|
   |	SPI0_SCK_32670	|	5	|	PB5/SCK	|	AVR/DIG/SPI	|
   |	SPI0_MISO_32670	|	6	|	PB4/MISO	|	AVR/DIG/SPI	|
   |	SPI0_MOSI_32670	|	7	|	PB3/MOSI	|	AVR/DIG/SPI/PWM	|
   |	SPI0_SS0_32670	|	8	|	PB2/SS	|	AVR/DIG/SPI/PWM	|
   |	SWDCLKB_32670	|	9	|	PB1	|	AVR/DIG/PWM	|
   |	SWDIOB_32670	|	10	|	PB0	|	AVR/DIG	|
   |	**P7**	|		|		|		|
   |	SPI1_SS0_32670	|	1	|	PD7	|	AVR/DIG	|
   |	UART0A_CTS_32670	|	2	|	PD6	|	AVR/DIG/PWM	|
   |	UART1A_CTS_32670	|	3	|	PD5	|	AVR/DIG/PWM	|
   |	UART0A_RTS_32670	|	4	|	PD4	|	AVR/DIG	|
   |	UART1A_TX_32670	|	5	|	PD3	|	AVR/DIG/PWM/INT	|
   |	UART1A_RX_32670	|	6	|	PD2	|	AVR/DIG/INT	|
   |	UART0A_TX_32670(def)/P0_27_32670	|	7	|	PD1	|	AVR/DIG/SER	|
   |	UART0A_RX_32670(def)/P0_26_32670	|	8	|	PD0	|	AVR/DIG/SER	|
   |	**P5**	|		|		|		|
   |	SPI1_MISO_32670	|	1	|	MISO	|		|
   |	3V3_SSB3(def)/VCC_31334	|	2	|	VCC	|		|
   |	SPI1_SCK_32670	|	3	|	SCK	|		|
   |	SPI1_MOSI_32670	|	4	|	MOSI	|		|
   |	RSTN_32670	|	5	|	RESET	|		|
   |	 --	|	6	|	GND	|		|
   </WRAP>
   
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670_arduino_connectors_pin_map.png?600 |}}
   \\
   \\
   ==== PMOD Connector Pin Map ====
   
   <WRAP left box 48%>
   |	**Net Name**	|	**Pin Number**	|	**Pin Name**	|
   |	**SPI PMOD**	|		|		|
   |	SPI0_SS0_32670(def)/SPI1_SS0_32670	|	1	|	SS	|
   |	SPI0_MOSI_32670	|	2	|	MOSI	|
   |	SPI0_MISO_32670	|	3	|	MISO	|
   |	SPI0_SCK_32670	|	4	|	SCK	|
   |	GND	|	5	|	GND	|
   |	1V8_SSB3/3V3_SSB3(def)/VOUT_3130	|	6	|	VCC	|
   |	P0_21_32670	|	7	|	INT	|
   |	P0_26_32670	|	8	|	RST	|
   |	SWDIOB_32670	|	9	|	IO7	|
   |	P0_23_32670	|	10	|	IO8	|
   |	GND	|	11	|	GND	|
   |	1V8_SSB3/3V3_SSB3(def)/VOUT_3130	|	12	|	VCC	|
   </WRAP>
   
   <WRAP right box 47%>
   |	**Net Name**	|	**Pin Number**	|	**Pin Name**	|
   |	**I2C PMOD**	|		|		|
   |	I2C1_SCL_32670/I2C2_SCL_32670	|	1	|	SCL	|
   |	I2C1_SCL_32670/I2C2_SCL_32670	|	2	|	SCL	|
   |	I2C1_SDA_32670/I2C2_SDA_32670	|	3	|	SDA	|
   |	I2C1_SDA_32670/I2C2_SDA_32670	|	4	|	SDA	|
   |	GND	|	5	|	GND	|
   |	GND	|	6	|	GND	|
   |	1V8_SSB3/3V3_SSB3(def)/VOUT_3130	|	7	|	VCC	|
   |	1V8_SSB3/3V3_SSB3(def)/VOUT_3130	|	8	|	VCC	|
   </WRAP>
   
   
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670_pmod_connectors_pin_map.png?500 |}}
   
   \\
   \\
   ==== Wireless Connectivity Options ====
   \\
   <WRAP indent>
   This board has two wireless connectivity options available to use for Internet of Things (IoT) applications:
     - On-board Chip Antenna
     - External Antenna connected through SMA connector
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670-sx-ardz_base_board_peripherals_connector.png?700 |}}
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670-sx-ardz_wireless_antenna.png?600 |}}
   
   These options can be configured by populating C63 with 39 pF for the external antenna or R156 with 0 Ω for on-board RF chip antenna with the center frequency tuned at 915 MHz.
   
   </WRAP>
   
   ==== Long Range Radio Connectivity Chipset ====
   \\
   <WRAP indent>
   The MAX32670-SX-ARDZ utilizes the SX1261 long range radio connectivity chipset from Semtech.  This chipset comes complete with the full low-power, wide area networking protocol built on top of the long range radio modulation technique.
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670-sx-ardz_lora_chipset.png?600 |}}
   
   The [[adi>MAX32670]] communicates to the SX1261 using the SPI bus, so the users will need to send long range commands and data over SPI bus.  Library functions calls have been specifically designed to be used with the MAX32670 and SX1261 using SPI bus.  
   
   The pins that connect the MAX32670 and the SX1261 are as follows:
   
   |	**Connected to**	|	**Net Name**	|	**Pin Number**	|	**Pin Name**	|	**Type (I=Input, O=Output)**	|	**Description**	|
   |	P0_21_32670	|	 - - 	|	6	|	 DIO3	|	 I/O	|	 Multi-purpose digital I/O - external TCXO supply voltage	|
   |	P0_23_32670	|	 - - 	|	12	|	 DIO2	|	 I/O	|	 Multi-purpose digital I/O / RF Switch control	|
   |	P0_24_32670	|	DIO2_SX	|	13	|	 DIO1	|	 I/O	|	 Multi-purpose digital IO	|
   |	P0_25_32670	|	 - - 	|	14	|	 BUSY	|	 O	|	 Busy indicator	|
   |	P0_26_32670	|	 - - 	|	15	|	 NRESET	|	 I	|	 Reset signal active low	|
   |	SPI0_MISO_32670	|	 - - 	|	16	|	 MISO	|	 O	|	 SPI subordinate output	|
   |	SPI0_MOSI_32670	|	 - - 	|	17	|	 MOSI	|	 I	|	 SPI subordinate input	|
   |	SPI0_SCK_32670	|	 - - 	|	18	|	 SCK	|	 I	|	 SPI clock	|
   |	SPI0_SS0_32670	|	 - - 	|	19	|	 NSS	|	 I	|	 SPI subordinate select	 
   
   {{ :resources:eval:user-guides:lora-reference-design:sx1261_pins.png?500 |}}
   </WRAP>
   
   \\
   ==== Input Power Source Options ====
   \\
   <WRAP indent>
   There are two (2) ways of powering the eval board, and user may use any combination of power sources.
     - Terminal Block - can be used when an external supply is connected to the Terminal block connector P11.
     - Battery Powered - can be used when batteries are connected to BT1 connector on the back of the board.
   
   {{ :resources:eval:user-guides:lora-reference-design:hardware:max32670_sx1261:power_source_options.png?600 |}}
   
   Each of the different power modes, provides a different level of control and flexibility.  You can find a matrix table of the different power modes and their general function here:
   
   ^  Power Source  ^  Voltage Rails Provided  ^  Peripherals Powered  ^  Function  ^
   | Terminal Block (P11) |  3 V to 6 V  | - MAX32670\\ - SPI and I2C PMODs\\ - ESP32 connectors\\ - Arduino connectors\\ - SX1261 chip | able to supply ALL voltages any peripheral might need|
   | Battery Power (BT1) |  3 V and 6 V  | - MAX32670\\ - SPI and I2C PMODs\\ - ESP32 connectors\\ - Arduino connectors\\ - SX1261 chip | able to supply ALL voltages any peripheral might need|
   </WRAP>
   
   
   \\
   \\
   ==== Reset Button ====
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670-sx-ardz_reset.png?600 |}}
   
   <WRAP center round box 55%>
   ^ Button	^   Function	^
   |  S1  | provides a hardware RESET to MAX32670 microcontroller. |
   
   </WRAP>
   
   ==== LED Indicators ====
   \\
   <WRAP indent>
   The base board has five LEDs: **DS1**, **DS2**, **DS3**, **DS4**, and **DS5**.
   </WRAP>
   
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670-sx-ardz_led_indicator.png?700 |}}
   
   <WRAP center round box 60%>
   ^ Button	^  Function	^
   |  DS1	| used as a LED indicator to one of the GPIO of the MAX32670, P0.28.  |
   |  DS2	| used as a LED indicator to one of the GPIO of the MAX32670, P0.29.  |
   |  DS3	| used as a LED indicator for the voltage output from the power supply. |
   |  DS4	| used as a LED indicator for the voltage output from the MAX31334. |
   |  DS5	| used as a LED indicator for the 3.3 V voltage output from the MAX3130. |
   
   </WRAP>
   
   ==== Programming Connectors ====
   \\
   <WRAP indent>
   This board uses SWD Interface and uses the [[adi>MAX32625PICO]] board for programming the on-board MCUs.  See the [[adi>/media/en/technical-documentation/data-sheets/MAX32625PICO.pdf|MAX32625PICO]] page for more details.  
     * P1 - SWD Interface used to program the MAX32670
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670-sx-ardz_swd_connector.png?700 |}}
   
   {{:resources:eval:user-guides:lora-reference-design:max32670_swd_connectors_pin_map.png?500 |}}
   
   <WRAP center round box 35%>
   |	**Connected to**	|	**Pin Number**	|
   |	1V8_SSB0/3V3_SSB3(def)	|	1	|
   |	SWDIO_32670	|	2	|
   |	GND	|	3	|
   |	SWDCLK_32670	|	4	|
   |	GND	|	5	|
   |	UART0A_TX_32670	|	6	|
   |	 - 	|	7	|
   |	UART0A_RX_32670	|	8	|
   |	 - 	|	9	|
   |	RSTN_32670	|	10	|
   </WRAP>
   
   
   
   The connector used are based off the 10-pin ARM Cortex standard pinout (0.05" pin spacing).  That pinout is common to both JTAG and SWD debug modes and is depicted in the following image.{{ :resources:eval:user-guides:eval-adicup3029:hardware:jtag_swd_10_connector.png?350 |}}
   
   <WRAP center round important 80%>
   The debugger board will need to be **plugged in via the USB port** in order to program any board.
   \\ 
   \\
   In order to program the MAX32670 node board, that board must be powered by one (1) CR123A battery or by an external power supply through P11.  Otherwise, there will be no connection between the two boards.
   </WRAP>
   </WRAP>
   
   \\
   \\
   
   
   ----
   ====== Applications =======
   
   <WRAP center box tip 100%>
   The [[adi>MAX32670-SX-ARDZ]] Base Board can be used with the compatible ADI-developed sensor nodes such as the:
        * [[adi>EV-STRUCTURAL-ARDZ]] for Structural Monitoring
        * [[adi>EV-FLOWMETER-ARDZ]] for Flow Rate Metering
        * [[adi>EV-ADE9000SHIELDZ]] for Electric Metering
   
   \\
   Using these platforms together enables users to design solutions based on low-power, long range proprietary radio communication technique.
   \\
   \\
   To learn more about the Long Range Wireless Radio solution developed by Analog Devices, visit the [[:resources:eval:user-guides:ad-max32sxwise-sl | AD-MAX32SXWISE-SL Long Range Wireless Radio Development Kit User Guide]]
   
   </WRAP>
   
   ----
   ====== System Setup ======
   
   
   ===== PHASE 1: Hardware Setup =====
   
   Note that this setup only applies for MAX32670-SX-ARDZ Base Board. Users may use a different base board or microcontroller, however the firmware built for this demo application cannot be used as this is specifically designed for the MAX32670-SX-ARDZ.
   
   \\
   ==== Equipment Needed ====
   
     * One (1) [[adi>MAX32670-SX-ARDZ]] Base Board
     * One (1) Sensor Node (any of these: [[adi>EV-STRUCTURAL-ARDZ]], [[adi>EV-FLOWMETER-ARDZ]], [[adi>EV-ADE9000SHIELDZ]])
     * One (1) MAX32625PICO Rapid Development Platform with 10-pin ribbon cable
         * with firmware image: [[repo>max32625pico-firmware-images/raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin| MAX32625PICO Firmware Image for MAX32670]]
     * One (1) CR123A Battery or any equivalent external DC power supply (+3 V to +4.7 V)
        *** Note that this is not included in the kit**
     * One (1) Micro USB to USB cable
     * Host PC (Windows 10 or later)
   \\
   {{ :resources:eval:user-guides:lora-reference-design:hardware_setup.png?800 |}}
   
   
   \\
   \\
     - Insert one CR123A battery (3 V to 4.7 V) into the battery holder (BT1 connector) of the [[adi>MAX32670-SX-ARDZ]] Base Board. <WRAP center round box 100%>
   **Make sure to check for the battery polarity in the BT1 connector, refer to the figure below. The DS3 LED will light up indicating that you have inserted the battery correctly and that power is provided in the base board.**</WRAP> {{ :resources:eval:user-guides:lora-reference-design:base_board_with_battery.png?600 |}}
     - Connect one <fc #6495ed> **Sensor Node** </fc> to the [[adi>MAX32670-SX-ARDZ]] Base Board by aligning the corresponding Arduino headers on each board. <WRAP center tip 100%>
   You do not have to set up the three sensor nodes altogether, just choose **one** from the available sensors in the kit:
        * [[adi>EV-STRUCTURAL-ARDZ]] for Structural Monitoring
        * [[adi>EV-FLOWMETER-ARDZ]] for Flow Rate Metering
        * [[adi>EV-ADE9000SHIELDZ]] for Electric Metering
   </WRAP>
     - Connect the [[adi>MAX32625PICO]] programming adapter to the [[adi>MAX32670-SX-ARDZ]] Base Board through the 10-pin ribbon cable. <WRAP center round box 100%>
   **Make sure that the MAX32625PICO programming adapter has been flashed with the correct image before connecting it to the MAX32670-SX-ARDZ Base Board. If you do not know how to load the image, click on the instructions below:
   **
   <hidden **How to flash the firmware image in the MAX32625PICO** >
     -   Download the firmware image: [[repo>max32625pico-firmware-images/raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin| MAX32625PICO Firmware Image for MAX32670]]
     -   Do not connect the MAX32625PICO to the [[adi>MAX32670-SX-ARDZ]] Base Board yet.
     -   Connect the MAX32625PICO to the Host PC using the micro USB to USB cable.
     -   Press the button on the MAX32625PICO. **(Do not release the button until the MAINTENANCE drive is mounted)**.{{ :resources:eval:user-guides:ad-paarray3552r-sl:max32625pico_maxdap.png?400 |}}
     -   Release the button once the MAINTENANCE drive is mounted.
     -   Drag and drop (to the MAINTENANCE drive) the firmware image.
     -   After a few seconds, the MAINTENANCE drive will disappear and be replaced by a drive named DAPLINK. This indicates that the process is complete, and the MAX32625PICO can now be used to flash the firmware of the [[adi>MAX32670-SX-ARDZ]] Base Board.
   </hidden>
   </WRAP>
     - Connect the [[adi>MAX32625PICO]] programming adapter to the Host PC using the micro USB to USB cable. {{ :resources:eval:user-guides:lora-reference-design:max32670-sx-ardz_to_maxpico.png?1500 |}}
   
   \\
   <WRAP center todo 100%> 
   
   **Once you have completed this setup, proceed to PHASE 2 found in
   [[:resources:eval:user-guides:longrangewirelessradio:software| ADI Long Range Wireless Radio Software User Guide]]**.
   
   </WRAP>
   
   
   
   \\
   
   ----
   ====== Resources ======
     * [[adi>MAX32670 | MAX32670 Product Page]]
     * [[adi>MAX77675 | MAX77675 Product Page]]
     * [[adi>MAX31334 | MAX31334 Product Page]]
     * [[adi>LTC3130 | LTC3130 Product Page]]
     * [[:resources:eval:user-guides:ad-max32sxwise-sl | AD-MAX32SXWISE-SL: Long Range Wireless Radio Development Kit based on MAX32670 MCU and SX1261 RF Transceiver ]]
     * [[:resources:eval:user-guides:ev-structural-ardz | EV-STRUCTURAL-ARDZ Sensor for Structural Monitoring ]]
     * [[:resources:eval:user-guides:ev-flowmeter-ardz | EV-FLOWMETER-ARDZ Sensor for Flow Rate Metering ]]
     * [[:resources:eval:user-guides/eval-ade9000shieldz:sensor_node:demo | EV-ADE9000-SHIELDZ Sensor for Electric Metering ]]
   
   
   \\
   ==== Design and Integration Files ====
   <WRAP round center 100% download>
   
   {{ :resources:eval:user-guides:lora-reference-design:max32670-sx-ardz-designsupport.zip | MAX32670-SX-ARDZ Design Support Package }}
   \\
   \\
   **REV C**
     * Schematic
     * Bill of Materials
     * Layout
     * Fabrication Files
   </WRAP>
   
   
   \\
   ===== Help and Support =====
   
   For questions and more information about this product, connect with us through the Analog Devices Engineer Zone.
   
   <WRAP center round help 100%>
   [[ez>reference-designs | EngineerZone Support Community]]
   </WRAP>
   
   
   \\
   \\
   
   // End of Document
