.. warning:: Conversion failed for ``resources/eval/user-guides/eval-ltc2862a-ardz``

   Reason: pandoc error: Error at "/tmp/tmp99q04do7.txt" (line 53, column 1):
expecting inline
not found
|**LK1**|If jumper is inserted, the 120 ohm termination resistor is connected between A and B. If not inserted, the termination resistor is disconnected.|
^

.. code-block:: text

   ====== EVAL-LTC2862A-ARDZ Arduino Shield ======
   
   Use the <fc #ff0000>**EVAL-LTC2862A-ARDZ**</fc> Arduino Shield with the widely available Arduino UNO and other Arduino compatible devices to easily evaluate the <fc #ff0000>[[adi>en/products/ltc2862a.html|LTC2862A]]</fc>. \\
   <fc #ff0000>[[adi>en/products/ltc2862a.html|LTC2862A]]</fc> is a robust RS485/RS422 transceiver with the following features:
     * //A protection from Overvoltage Line Faults to ±60V,// 
     * //±40kV HBM ESD Interface Pins, ±15kV Other Pins//, 
     * //IEC Level 4 ESD and EFT on Interface Pins//, 
     * //Extended Common Mode Range: ±25V//, 
     * //Guaranteed Failsafe Receiver Operation// \\
   The <fc #ff0000>[[adi>en/products/ltc2862a.html|LTC2862A-2]]</fc> features slew rate limited transmitters for low electromagnetic interference (EMI) in sensitive applications. The slew rate limit circuit maintains consistent control of transmitter slew rates across voltage and temperature to ensure low EMI. \\ 
   It also provides additional noise immunity by adding low-pass filtering to the differential signal in its receiver.\\ \\
   The <fc #ff0000>**EVAL-LTC2862A-ARDZ**</fc>  also includes [[adi>en/products/adu6421a.html|ADuM6421A]], quad-channel digital isolators with an isoPower®, integrated, isolated dc-to-dc converter. Based on the Analog Devices, Inc., iCoupler® technology, the dc-to-dc converter provides regulated, isolated power that meets CISPR 32/EN 55032 Class B limits.
   {{ :resources:eval:user-guides:eval_ltc2862a_ardz:47454_evalltc2862aardzangle_sourcecopy_5.jpg?600 |}}
   ----
   ====== EVAL-LTC2862A-ARDZ features ======
     * //Full <fc #6495ed>Data</fc> + <fc #ffa500>Power</fc> Isolation//
     * //Arduino style header for easy evaluation//
     * //Terminal blocks for easy wire connections//
     * //Test points and jumpers for easy config and monitoring of signals//
   
   -----
   ====== Key Features ======
   ===== High Receiver Input Resistance =====
   The bus receiver input load from A or B to GND is less than one-seventh unit load, permitting a total of 224 receivers per system without exceeding the RS485 receiver loading specification. The input load of the receiver is unaffected by enabling/disabling the receiver or by powering/unpowering the part.
   ===== Supply Current =====
   The unloaded static supply currents in these devices are low — typically 1.1mA for non slew limited devices 
   and 3.5mA for slew limited devices. 
   ===== Shutdown Mode Delay =====
   The [[adi>en/products/ltc2862a.html|LTC2862A]] features a low power shutdown mode that is entered when both the driver and the receiver 
   are simultaneously disabled (pin DE low and RE high). 
   ===== Full Failsafe Operation =====
   When the absolute value of the differential voltage between the A and B pins is greater than 200mV with the receiver 
   enabled, the state of RO will reflect the polarity of (A–B).[[adi>en/products/ltc2862a.html|LTC2862A]] has a failsafe feature that guarantees the receiver output will be in a logic 1 state (the idle state) when the inputs are shorted, left open, or terminated but not driven. The delay allows normal data signals to transition through the threshold region without being interpreted as a failsafe condition. This failsafe feature is guaranteed to work for inputs spanning the entire common mode range of –25V to 25V
   ===== Low EMI 250kbps Data Rate =====
   The [[adi>en/products/ltc2862a.html|LTC2862A-2]] features slew rate limited transmitters for low electromagnetic interference (EMI) in sensitive applications. The slew rate limit circuit maintains consistent control of transmitter slew rates across voltage and temperature to ensure low EMI under all operating conditions. 
   ===== Enhanced Receiver Noise immunity =====
   The [[adi>en/products/ltc2862a.html|LTC2862A-2]] provides additional noise immunity by adding low-pass filtering to the differential signal in its receiver. Commensurate with its maximum data rate of 250kbps, the LTC2862A-2 receiver attenuates high frequency signals above approximately 660kHz. This lowpass filter removes high frequency noise transients that might otherwise be interpreted as data.
   ===== Driver Overvoltage and Overcurrent Protection =====
   The [[adi>en/products/ltc2862a.html|LTC2862A]] is an improved overvoltage fault-tolerant RS485/RS422 transceiver that operates from 3V to 5.5V power supplies. Industrial installations may encounter common mode voltages between nodes far greater than the –7V to 12V range specified by the RS485 standards. Standard RS485 transceivers can be damaged by voltages above their typical absolute maximum ratings of –8V to 12.5V. The limited overvoltage tolerance of standard RS485 transceivers makes implementation of effective external protection networks difficult without interfering with proper data network performance within the –7V to 12V region of RS485 operation. Replacing standard RS485 transceivers with the rugged [[adi>en/products/ltc2862a.html|LTC2862A]]  devices may eliminate field failures due to overvoltage faults without using costly external protection devices. The [[adi>en/products/ltc2862a.html|LTC2862A]] is protected from ±60V faults even with the loss of GND or VCC (GND open faults not tested in
   production).
   
   
   
   -----
   ====== Connectors ======
   
   
   ^**Port** ^ Function ^
   |**EXT01**|Screw Terminal Block; Connect an external power supply (5V or 3.3V) to pin 1 of the EXT01 for VDD1. This powers side 1 of the eval board. Connect pin 2 of EXT01 to 0V to provide isolated ground for side 1 of the board.|
   |**P1-4**|Arduino headers on the <fc #ff0000>**EVAL-LTC2862A-ARDZ**</fc> board. The P4 header provides connectivity for RS485 signals to and from an external Arduino/Arduino Compatible device. P4.1 (pin 1 of the P4 header) is connected to the RX_RS485 pin of the [[adi>en/products/ltc2862a.html|LTC2862A]]transceiver and should be connected externally to the (set) RX pin of an Arduino/Arduino Compatible device if the source of this signal is provided by an Arduino. P4.2 is connected to the TX_RS485 pin of the [[adi>en/products/ltc2862a.html|LTC2862A]] transceiver and should be connected to the TX pin (set) on the Arduino. DE (Driver Enable) and RE (Receiver enable) pins from the transceiver are connected to P4.3 (pin 3) and P4.4 (pin 4) of the P4 header and should be connected to the DE (Driver Enable) and RE (Receiver enable) as set on the Arduino. Select_Mode is connected to the pin 7 of P4 header (P4.7). It gives an external Arduino/Arduino compatible device the choice to select the source for the transmitter signal for the [[adi>en/products/ltc2862a.html|LTC2862A]] transceiver. (Can select USB or UART as a source for the signal) |
   |**P9**|Screw terminal for external connections to pin A (P9.2), B (P9.3) and isolated GND2 (P9.1 or P9.4) for the eval board.|
   
   -----
   ====== Jumper Configuration ======
   ^**Jumper ** ^ Configuration
   |**LK1**|If jumper is inserted, the 120 ohm termination resistor is connected between A and B. If not inserted, the termination resistor is disconnected.|
   |**LK2**|If jumper is inserted, the 120 ohm termination resistor is connected between A and B. If not inserted, the termination resistor is disconnected.|
   |**J1**|The jumper configuration on J1 selects the power supply source for VDD1. If J1.1 and J1.2 are connected, one of the 5V supply is selected. The choice of the 5V supply depends on the jumper configurations on the J3 header. If J1.2 (pin 2 of J1) and J1.3 (pin 3 of J1) are connected, 3.3V rail from an Arduino via the Arduino header should be used as a supply. This should be connected to the P1.5 (pin 5 of the P1 Arduino header) on the Evaluation board.|
   |**J3**|The jumper configuration on J3 determines the 5V power supply source for VDDP pin of ADUM6421 and VCCIO pin of FT232R. If J3.1 and J3.2 are connected, USB 5V is chosen as the power supply source. If J3.3 (pin 3 of J3) and J3.4 (pin 4 of J3) are connected, EXT_VIN is chosen as the 5V supply. Lastly, if J3.5 (pin 5 of J3) and J3.6 (pin 6 of J3) are connected, an Arduino/Arduino-compatible device should provide 5V to the pins via the Arduino header. The 5V rail on the Arduino should be connected to P1.4 (Pin 4 of the P1 Arduino header on the Evaluation board).|
   |**JMP2-1/JMP2-2**|The connection of these resistors determines the output voltage. Only connect one of the two resistors. Connecting JMP2-1 pulls down VSEL to GNDISO, therefore the output voltage is set to 3.3V. Whereas, connecting JMP2-2 pulls up VSEL to VISO. Therefore, the output voltage is set to 5V.|
   |**J4**|Jumper configuration on J4 determines the source for the DE pin on the [[adi>en/products/ltc2862a.html|LTC2862A]]. If J4.1 and J4.2 are connected, FT232R (USB to RS485 converter) provides the source for the DE signal which comes D+ and D- signals from the USB. If J4.3 and J4.4 are connected, DE signal comes from P4.3 (pin 3 of the P4 Arduino header) which should be connected externally to an Arduino or an Arduino Compatible device. If J4.5 and J4.6 are connected, DE is connected to GND, disabling the drivers. |
   |**J5**|Jumper configuration on J5 determines the source for the RE_N (Receiver-Enable) pin on the [[adi>en/products/ltc2862a.html|LTC2862A]]. If J5.1 and J5.2 are connected, DE (Driver-Enable) signal is used as a source for the RE_N. This configuration makes sure that when the driver is enabled, the receiver is disabled and vice versa. If J5.3 and J5.4 are connected, RE_N signal comes from P4.4 (pin 4 of the P4 Arduino header) which should be connected to an external Arduino or an Arduino Compatible device. If J5.5 and J5.6 are connected, RE_N is connected to VDD1 and is disabled (it is active low). Lastly, if J5.7 and J5.8 are connected, RE_N is connected to GND1 and is enabled (Receiver Enable pin is is active low).|
   |**J6**|Jumper configuration on J6 determines the voltage applied to the Input_Sel which selects the source for the TX_RS485 signal. If J6.1 (pin 1 of the J6) and J6.2 (pin 2 of the J6) are connected, an external Arduino/ Arduino Compatible device controls Input_Sel pin. Connect the respective pin of the Arduino which codes for Input_Sel to P4.7 (Pin 7 of P4 Arduino header). If J6.3 (pin 3 of J6) and J6.4 (pin 4 of J6) are connected, Input_Sel is connected to GND, therefore, UART is selected to be the source for the TX_RS385 signal. Lastly, if J6.5 (pin 5 of J6) and J6.6 (pin 6 of J6) are connected, Input_Sel is connected to VDD1 +5V. Therefore, the source of the TX_RS485 signal comes from the USB data lines (D+/D-) that are converted to RS485 signals by FT232R IC.|
   |**J7**|Jumper configuration on J7 selects either 5V (if J7.1 and J7.2 are connected) or 3.3V (if J7.3 and J7.4 are connected) for the FT232R IC. However, this should match the VDD1 supply voltage on the board.|
   
   -----
   ====== TestPoints ======
   ^**TestPoint ** ^ Signal^
   |**TP1**|VDD1|
   |**TP2-4**|GND|
   |**TP5**|+5V|
   |**TP6-7**|isolated gnd|
   |**TP8**|VDD2|
   |**TP9**|TX_RS485|
   |**TP10**|RE_N|
   |**TP11**|DE|
   |**TP12**|RX_RS485|
   |**TP13**|DI_ISO|
   |**TP14**|RE_N_ISO|
   |**TP15**|DE_ISO|
   |**TP16**|RO_ISO|
   |**TP17**|A|
   |**TP18**|B|
   
   
   -----
   ====== Schematic, Bill of Materials and Layout Files======
   <WRAP round 80% download>
   
       *{{ :resources:eval:user-guides:eval_ltc2862a_ardz:ltc2862a_ardz_bom.xlsx |BOM}}
       *{{ :resources:eval:user-guides:eval_ltc2862a_ardz:ltc2862a_ardz_layout.pdf|Layout}}
       *{{ :resources:eval:user-guides:eval_ltc2862a_ardz:ltc2862a_ardz_schematic.pdf |Schematic}}
   
   </WRAP>
   ------
   ====== Change Log======
   
       *Initial Revision 
   
   ---------
   ====== Resources and Documents ======
       * LTC2862A Data Sheet: https://www.analog.com/media/en/technical-documentation/data-sheets/2862af.pdf
       * ADuM6420A Data Sheet: https://www.analog.com/media/en/technical-documentation/data-sheets/ADuM6420A-6421A-6422A.pdf  
       * SDP-K1: https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html
       * RS-485/RS-422 implementation guide AN-960: https://www.analog.com/media/en/technical-documentation/application-notes/AN-960.pdf
       * Enhanced RS-485 Performance: Receiver Fail-Safe, Hysteresis, Common-Mode Range and Gain Bandwidth Optimized for Long Fieldbus Cables AN-1399: https://www.analog.com/media/en/technical-documentation/application-notes/an-1399.pdf
   
   -----------
   ====== Software ======
     * [[https://ttssh2.osdn.jp/index.html.en|Tera Term]]
     * [[https://os.mbed.com/studio/|Mbed Studio for SDP-K1]]
     * [[https://ide.mbed.com/compiler/|Mbed online Compiler]]
     * [[https://os.mbed.com/platforms/SDP_K1/|SDP-K1 programming / set up guide]]
     * [[https://www.arduino.cc/en/software|Arduino IDE]]
     * {{ :resources:eval:user-guides:eval_ltc2862a_ardz:arduino_code.zip |Arduino Code}}
     * {{ :resources:eval:user-guides:eval_ltc2862a_ardz:sdp-k1_ltc2862a.zip |SDP-K1 C++ code for evaluating the EVAL-LTC2862A, use Mbed Studio or online compiler, see above for SDP-K1 programming guide}}
   
   -----------
   ====== Procedure for using USB to provide signals to the transceiver by using a USB>UART converter ======
   
   {{:resources:eval:user-guides:eval_ltc2862a_ardz:img_20201203_092525.jpg?400|}} \\ 
   Photo of board showing the jumper configuration using USB for providing signals for the [[adi>en/products/ltc2862a.html|LTC2862A]] transceiver.\\ 
   This requires two **<fc #ff0000>EVAL-LTC2862A-ARDZ</fc>** board.\\ 
   **For both boards**
     - Insert jumpers on both LK1 and LK2 (connects 120 ohm termination resistor between A and B)
     - Set jumper configuration on J3 to use USB_5V as the 5V source:  (If J3.1 (pin 1 of J3) and J3.2 (pin 2 of J3) are connected, USB 5V is chosen as the supply.
     - Set jumper configuration on J1 to select 5V as the power source (Connect (J1.1 (pin 1 of J1) and J1.2 (pin 2 of J1))
     - Set jumper configuration on J4 to get the Driver Enable signal from FT232R IC. (Connect J4.1 and J4.2).
     - Set jumper configuration on J5 so that DE (Driver-Enable) is used as a source for the RE_N (Receiver-Enable) (Connect J5.1 and J5.2) 
     - Set jumper configuration on J6 so that Input_Sel is connected to VDD1 +5V. Therefore, the source of the TX_RS485 signal comes from the USB data lines that are converted to RS485 signals by FT232R, i.e. Connect J6.4 (pin 4 of J6) and J6.5 (pin 5 of J6). 
     - Set jumper configuration on J7 so that 5V is selected as the power supply option for the FT232R (Connect J7.1 and J7.2) 
     - Connect pin A of Screw Terminal (P9.2) on one board to pin A Screw Terminal (P9.2) on the other eval board.
     - Connect pin B of Screw Terminal (P9.3) on one board to pin B Screw Terminal (P9.3) on the other eval board.
     - Connect the two USB cables, one for each eval board, from a PC to the eval board. (You should see the LEDs on the board flash briefly and hear the sound of the device connected on your PC)
     - Open up two instances of Tera Term or Putty or similar software.
     - Connect one instance to the COM port of one eval board, and the other instance of COM port to the other eval board. (In Tera Term it will give you a drop down menu of choices, you should see two choices(one for each board)). **Both serial ports in Tera Term / Putty should be set to the same Baud Rate, Parity, stop bits etc. **
     - You should now be able to type in one of the terminals and the characters will be transmitted through the USB to the FT232R IC on the board, then over UART to the [[adi>en/products/ltc2862a.html|LTC2862A]], and then over RS-485 to the other board and so on before being transmitted back to the other terminal window.
     - The Yellow/Orange LED will flash on the board when it is receiving data over USB (from PC to board), the RED led flashes when it is transmitting data over USB (from board to PC)\\ 
   {{:resources:eval:user-guides:eval_ltc2862a_ardz:img_20201203_094335.jpg?400|}}\\ 
   Photo of full setup\\ 
   {{:resources:eval:user-guides:eval_ltc2862a_ardz:teraterm.png?400|}}
   {{:resources:eval:user-guides:eval_ltc2862a_ardz:teraterm1.png?400|}}\\ 
   Photo showing text being sent from one board to the other in Tera Term (the black cursor shows the terminal being typed in (transmitting), while the hollow cursor shows the receiving terminal. The device does not echo back what is being sent in USB->UART mode)
   
   
   
   -----------
   ====== Procedure for Evaluating the board with an Arduino and the USB to UART converter ======
   
   
   This requires two <fc #ff0000>**EVAL-LTC2862A-ARDZ**</fc> boards and an Arduino UNO Kit/similar device.\\ 
   {{:resources:eval:user-guides:eval_ltc2862a_ardz:img_20201203_092525.jpg?400|}} \\ 
   Photo of board with correct Jumper Configuration for USB -> UART.\\ 
   **For USB->UART board**
     - Insert a jumper on both LK1 and LK2 (Insert the jumper so that it connects 120 ohm termination resistor between A and B).
     - Set jumper configuration on J3 to use USB 5V as the 5V source: (If J3.1 (pin 1 of J3) and J3.2 (pin 2 of J3) are connected, USB 5V is chosen as the supply.
     - Set jumper configuration on J1 to select 5V as the power source: Connect (J1.1 (pin 1 of J1) and J1.2 (pin 2 of J1).
     - Set jumper configuration on J4 to get the Driver Enable signal from FT232RQ IC. (Connect J4.1 and J4.2).
     - Set jumper configuration on J5 so that DE (Driver Enable) is used as a source for the RE_N (Receiver Enable) (Connect J5.1 and J5.2).
     - Set jumper configuration on J6 so that Input_Sel is connected to VDD1 +5V. Therefore, the source of the TX_RS485 signal comes from the USB data lines that are converted to RS485 signals by FT232R, i.e. Connect J6.4 (pin 4 of J6) and J6.5 (pin 5 of J6).
     - Set jumper configuration on J7 so that 5V are selected as the power supply option for the FT232R (Connect J7.1 and J7.2).
     - Connect pin A of Screw Terminal (P9.2) on one board to pin A Screw Terminal (P9.2) on the other board.
     - Connect pin B of Screw Terminal (P9.3) on one board to pin B Screw Terminal (P9.3) on the other board.\\ 
   {{:resources:eval:user-guides:eval_ltc2862a_ardz:img_20201203_132007.jpg?400|}}\\ 
   Photo of board with correct Jumper Configuration for Arduino.\\ 
   **For board attached to Arduino**
     - Power up Arduino and program it using the sketch provided. (see software section above).
     - Unpower the Arduino.
     - Insert jumpers on both LK1 and LK2 (connects 120 ohm termination resistor between A and B).
     - Set jumper configuration on J3 so that Arduino is chosen to provide 5V to the pins (Connect J3.5 (pin 5 of J3) and J3.6 (pin 6 of J3)).
     - Set jumper configuration on J1 to get 3.3V from the Arduino. (Connect J1.2 (pin 2 of J1) and J1.3 (pin 3 of J1)).
     - Set jumper configuration on J5 to get the RE/RE_N(Receiver-Enable) signal from the Arduino. (Connect J5.3 and J5.4) RE_N signal comes from P4.4 (pin 4 of the P4 Arduino header on the eval board) which should be connected to an external Arduino or an Arduino Compatible device.
     - Set jumper configuration on J6 so that Input_Sel is connected to GND, therefore, UART is selected to be the source for the TX_RS385 signal. (Connect J6.2 (pin 2 of J6) and J6.3 (pin 3 of J6)).
     - Set jumper configuration on J7 so 3.3V is selected as a supply for the  FT232R IC IC. (Connect J7.3 and J7.4).
     - Connect the Eval board to the Arduino using the Arduino headers on the eval board. The P4 header provides connectivity for RS485 signals to and from an external Arduino/Arduino Compatible device. P4.1 is connected to the RX_RS485 pin of the [[adi>en/products/ltc2862a.html|LTC2862A]] transceiver. P4.2 should be connected to the TX pin set on the Arduino. DE (Driver Enable) and RE (Receiver enable) pins from the transceiver are connected to P4.3 (pin 3) and P4.4 (pin 4) of the P4 header and should be connected to the DE (Driver-Enable) and RE (Receiver-Enable) as set on the Arduino and so on.
   
   **Continued Procedure for both boards**
     - Connect power to the Arduino, either through USB or through the barrel jack.
     - Connect a USB cable to the other eval board, from the PC to the board. (You should see the LEDs on the board flash briefly and hear the Windows Device Connected sound on your PC)
     - Open up an instance of Tera Term or Putty or similar software.
     - Connect the instance to the COM port of the USB->UART board. (In Tera Term it will give you a drop down menu of choices, you should see two, one for each board). **The serial port in Tera Term / Putty should be set to the same Baud Rate, Parity, stop bits etc as the Arduino code (The included code is 9600, 8 bit, no parity, 1 stop bit). **
     - You should now be able to type a character into the terminal and the character will be transmitted through the USB to the FT232R IC on the board, then over UART to the [[adi>en/products/ltc2862a.html|LTC2862A]], then over RS-485 to the other board then to the Arduino before being transmitted back over the same connection by the Arduino and back to the terminal window. (Please note the included code will receive until it receives a full stop or the enter key is pressed. On pressing one of the two, it will stop receiving and will transmit what it received back).
     - The Yellow/Orange LED will flash on the evaluation board (in USB->UART mode) when it is receiving data over USB (from PC to board), the RED led flashes when it is sending data over USB (from board to PC).\\ 
   {{:resources:eval:user-guides:eval_ltc2862a_ardz:img_20201203_132347.jpg?400|}}\\ 
   Photo of full setup\\ 
   {{:resources:eval:user-guides:eval_ltc2862a_ardz:teraterm2.png?400|}}\\ 
   Photo showing characters received back in terminal after being sent.
   
   -----------
   ====== Procedure for Evaluating the board with SDP-K1 ======
   
   **Make sure the SDP-K1 VIO_ADJUST is set at 3.3V**\\ 
   This requires two <fc #ff0000>**EVAL-LTC2862A-ARDZ**</fc> board and two SDP-K1s (you can use only one SDP-K1 if you replace one side with the USB->UART config or the Arduino Config).\\ 
   {{:resources:eval:user-guides:eval_ltc2862a_ardz:img_20201215_151704.jpg?400|}}\\ 
   Photo of board with correct Jumper Configuration for SDP-K1 / Arduino.\\ 
   **For both boards attached to SDP-K1 with USB power, //Or replace one of the sides with the USB->UART or Arduino set up.//**
     - Power up and program the SDP-K1 and/or Arduino (see software above)
     - Disconnect power on the SDP-K1 and or Arduino.
     - Insert jumpers on both LK1 and LK2 (connects 120 ohm termination resistor between A and B).
     - Set jumper configuration on J3 so that Arduino is chosen to provide 5V to the pins (Connect J3.5 (pin 5 of J3) and J3.6 (pin 6 of J3)).
     - Set jumper configuration on J1 to get 3.3V from the Arduino. (Connect J1.2 (pin 2 of J1) and J1.3 (pin 3 of J1)).
     - Set jumper configuration on J4 to get the DE signal from the Arduino (Connect J4.2 and J4.3). The DE signal comes from P4.3 (pin 3 of the P4 Arduino header) which should be connected to an external Arduino or an Arduino Compatible device. 
     - Set jumper configuration on J5 to get receiver enable signal from the Arduino. (Connect J5.3 and J5.4) RE_N signal comes from P4.4 (pin 4 of the P4 Arduino header on the eval board) which should be connected to an external Arduino or an Arduino Compatible device.
     - Set jumper configuration on J6 so that Input_Sel is connected to GND, therefore, UART is selected to be the source for the TX_RS385 signal. (Connect J6.2 (pin 2 of J6) and J6.3 (pin 3 of J6)).
     - Set jumper configuration on J7 so 3.3V is selected as a supply for the FT232R IC IC. (Connect J7.3 and J7.4).
     - Connect the Eval board onto SDP-K1 or the Arduino using the Arduino headers on the eval board. The P4 header provides connectivity for RS485 signals to and from an external Arduino/Arduino Compatible device. P4.1 is connected to the RX_RS485 pin of the [[adi>en/products/ltc2862a.html|LTC2862A]] transceiver. P4.2 should be connected to the TX pin (as set) on the Arduino. DE (Driver-Enable) and RE (Receiver-Enable) pins from the transceiver are connected to P4.3 (pin 3) and P4.4 (pin 4) of the P4 header and should be connected to the DE (Driver Enable) and RE (Receiver enable) (as set) on the Arduino and so on.
     - Connect power to the SDP-K1, either through USB or through the barrel jack. 
     - Connect the second board to an SDP-K1 or other set ups explained above.
     - Open up two instances of Tera Term or Putty or similar software.
     - Connect the instance to the COM port of the SDP-K1 board. (In Tera Term it will give you a drop down menu of choices, you should see two, one for each board (you may see three/four if you supplied USB power to the eval boards from USB ports on the PC, in such a case typically, the SDP-K1 shows up as //USB Serial Device// rather than USB Serial Port)). **The serial port in Tera Term / Putty should be set to the same Baud Rate, Parity, stop bits etc as the SDP-K1 code (The included code is 9600, 8 bit, no parity, 1 stop bit). **
     - You should now be able to type a character into the terminal and the character will be transmitted through the USB to the SDP-K1 the board, then over UART to the [[adi>en/products/ltc2862a.html|LTC2862A]], then over RS-485 to the other board then to the other SDP-K1/Arduino before being transmitted to the other terminal window.
     - The Yellow/Orange LED will flash on the Evaluation board (in USB->UART mode) when it is receiving data over USB (from PC to board), the RED led flashes when it is transmitting data over USB (from board to PC)\\ 
   
   -----------
   
   // End of Document // 
