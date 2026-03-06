.. warning:: Conversion failed for ``resources/eval/user-guides/eval-ad777x-ardz``

   Reason: pandoc error: Error at "/tmp/tmpz16k2icc.txt" (line 389, column 1):
expecting inline
not found
  * Connect USB UART J14 (Micro USB) to your host PC. \\
^

.. code-block:: text

   
   
   ====== AD777x Customer Evaluation Board User Guide ======
   
   The EVAL-AD7770-ARDZ / EVAL-AD7771-ARDZ / EVAL-AD7779-ARDZ evaluation kit features the AD7770, AD7771, and AD7779 24-bit, analog-to-digital converters (ADCs). The board interfaces with the system demonstration platform SDP-K1 controller board (EVAL-SDP-CK1Z), with the DE10-Nano development kit and with any microcontroller supported by Mbed platform via Arduino interface. The controller board can supply power to the EVAL-AD7770-ARDZ/EVAL-AD7771-ARDZ/EVAL-AD7779-ARDZ evaluation board and also connects to a PC running a Windows® operating system via a USB cable. 
   
   The AD777x evaluation software fully configures the AD7770, AD7771, and AD7779 device register functionality and provides dc and ac time domain analysis in the form of waveform graphs, histograms, and associated noise analysis for ADC performance evaluation. 
   
   This kit allows the user to evaluate the features of the ADC. The user PC software executable controls the AD7770, AD7771, and AD7779 over the USB cable through the controller board. 
   
   Full specifications for the AD7770, AD7771, or AD7779 are available in the AD7770, AD7771, or AD7779 data sheets and should be consulted in conjunction with this user guide when working with the evaluation board
   
   ==== The AD777x Family ====
   The AD777x is an 8-channel, simultaneous sampling analog-to-digital converter (ADC). Eight full Σ-Δ ADCs are on-chip. The AD777x provides an ultralow input current to allow direct sensor connection. Each input channel has a programmable gain stage allowing gains of 1, 2, 4, and 8 to map lower amplitude sensor outputs into the full-scale ADC input range, maximizing the dynamic range of the signal chain.
   
   Each channel contains an ADC modulator and a sinc3/sinc5 (AD7770 and AD7779 just sinc3), low latency digital filter. A sample rate converter (SRC) is provided to allow fine resolution control over the AD777x output data rate (ODR). This control can be used in applications where the ODR resolution is required to maintain coherency with 0.01 Hz changes in the line frequency. 
   
   The SRC is programmable through the serial port interface (SPI). The AD777x implements two different interfaces: a data output interface and SPI control interface. The ADC data output interface is dedicated to transmitting the ADC conversion results from the AD777x to the processor. The SPI writes to and reads from the AD777x configuration registers and for the control and reading of data from the successive approximation register (SAR) ADC. The SPI can also be configured to output the Σ-Δ conversion data. 
   
   The AD777x includes a 12-bit SAR ADC. This ADC can be used for AD777x diagnostics without having to decommission one of the Σ-Δ ADC channels dedicated to system measurement functions. With the use of an external multiplexer, which can be controlled through the three general-purpose input/output pins (GPIOs), and signal conditioning, the SAR ADC can validate the Σ-Δ ADC measurements in applications where functional safety is required. In addition, the AD777x SAR ADC includes an internal multiplexer to sense internal nodes. 
   
   {{:resources:eval:user-guides:ad777x.png|}}
   
   ==== Evaluation board Features ====
     * Full featured evaluation board for the AD777x
     * PC control in conjunction with the system demonstration platform (EVAL-SDP-CK1Z/DE10-Nano)
     * PC software for control and data analysis (time and frequency domain)
     * Standalone capability 
   ==== Evaluation Kit ====
     * EVAL-AD777x-ARDZ-Rev A Evaluation Board
   ==== Associated Software ====
     * [[adi>media/en/evaluation-boards-kits/evaluation-software/AD777x|AD777x Ace Plugin Evaluation Software]]
   ==== Related Documents ====
     * [[adi>media/en/technical-documentation/data-sheets/ad7770.pdf|AD7770 Data Sheet]]]
     * [[adi>media/en/technical-documentation/data-sheets/ad7771.pdf|AD7771 Data Sheet]]]
     * [[adi>media/en/technical-documentation/data-sheets/ad7779.pdf|AD7779 Data Sheet]]]
   
   ====== Quick Start Guide ======
   The following steps highlight the process to begin using the evaluation board.
   ==== Equipment Required ====
     - [[adi>en/products/ad777x.html|EV-AD777x-ADRZ-Rev A evaluation board]]
     - PC running Windows with a USB2.0 port and software installed.
     - Controller Board
         - Option A: [[adi>en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html
   |EVAL-SDP-CK1Z]] and a USB-C cable
         - Option B: [[https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&CategoryNo=167&No=1046|DE10-Nano kit]] and a Micro-USB cable
   
   
   ==== Getting started ====
   <note warning>  Ensure the SDP board is not connected to the USB port of the PC 
   </note>
     - Install the [[adi>en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html?doc=EVAL-AD7383FMCZ-ug-1770.pdf|Ace Plugin]]
         * [[resources:eval:user-guides:ad4170:softwareprocedures#ace_plugin_install_guide|Ace Plugin Install guide available here]] 
     - Connect the  EV-AD4170-ASD1Z-U1 to the controller board 
        - **Option A:** Connect the EV-AD4170-ASD1Z-U1 to the EVAL-SDP-CK1Z
           - Using the 120 pin connector
               *  Screw the two boards together using the plastic screw-washer set included in the evaluation board kit to ensure that the boards are connected firmly together. 
           - Using the Arduino Connectors 
        - **Option B:** Connect the EV-AD4170-ASD1Z-U1 to the EVAL-SDP-CB1Z
           * Using the 120 pin connector
               *  Screw the two boards together using the plastic screw-washer set included in the evaluation board kit to ensure that the boards are connected firmly together. 
     - If using Windows® XP, it may be needed to search for the controller board drivers. Choose to automatically search for the drivers for the controller board if prompted by the operating system.
     - Launch the ACE plugin from the **Analog Devices** subfolder in the **Programs** Menu.
   
   
   {{:resources:eval:user-guides:ad777x_description1.png|}}
   
   
   
   ====== Hardware Guide ======
   
   The EVAL-AD777x-ARDZ has been designed in such a way that the user can configure the ADC as close as possible as in their final application. For that purpose the board has multiple jumpers and solder link that allows the user to change the configuration easily.  
   
   The possible configuration are:
     - Bipolar / Unipolar supplies.
     - External / Internal power supplies.
     - Internal / External reference with/out buffer pin.
     - Pin Control / SPI mode.
     - Multiplexer for SAR debugging.
     - Multiple clock sources.
     - Multiple zio extension options
     - Possibility to connect external Signal chain via surfing connector
   
   More detail explained in the following sections
   
   ===== Block Diagram =====
   {{:resources:eval:user-guides:ad777x_eval_block_eval_20220331.drawio.png|}}
   ===== Connectors =====
   **Table 1. SMB connectors**
   |  Connector  |  Pin  |  Signal  |
   |  J1  |  1  |  AIN0+ (Analog input signal 0+)  |
   |  J2  |  1  |  AIN0- (Analog input signal 0-)  |
   |  J3  |  1  |  AIN1+ (Analog input signal 1+)  |
   |  J4  |  1  |  AIN1- (Analog input signal 1-)  |
   |  J5  |  1  |  AIN2+ (Analog input signal 2+)  |
   |  J6  |  1  |  AIN2- (Analog input signal 2-)  |
   |  J7  |  1  |  AIN3+ (Analog input signal 3+)  |
   |  J8  |  1  |  AIN3- (Analog input signal 3-)  |
   |  J10  |  1  |  External reference source  |
   |  J13  |  1  |  External clock source  |
   
   **Table 2. External AVDDx/AVSSx**
   |  Connector  |  Pin  |  Signal  |
   |  P7  |  1  |  External AVDD1  |
   |  P7  |  2  |  External AVDD2  |
   |  P7  |  3  |  External AVDD4  |
   |  P7  |  4  |  External AVSSX  |
   |  P7  |  5  |  GND  |
   
   **Table 3. External AVDDx/AVSSx**
   |  Connector  |  Pin  |  Signal  |
   |  P8  |  1  |  External IOVDD  |
   |  P8  |  2  |  GND  |
   
   **Table 4. External VIN**
   |  Connector  |  Pin  |  Signal  |
   |  P8  |  1  |  External VIN   |
   |  P8  |  2  |  GND  |
   
   **Table 5. Analog input signals**
   |  Connector  |  Pin  |  Signal  |
   |  P11  |  1  |  AIN0- (Analog input signal 0-)  |
   |  P11  |  2  |  AIN0+ (Analog input signal 0+)  |
   |  P11  |  3  |  AIN1- (Analog input signal 1-)  |
   |  P11  |  4  |  AIN1+ (Analog input signal 1+)  |
   |  P11  |  5  |  AIN2- (Analog input signal 2-)  |
   |  P11  |  6  |  AIN2+ (Analog input signal 2+)  |
   |  P11  |  7  |  AIN3- (Analog input signal 3-)  |
   |  P11  |  8  |  AIN3+ (Analog input signal 3+)  |
   |  P12  |  1  |  AIN7+ (Analog input signal 7+)  |
   |  P12  |  2  |  AIN7- (Analog input signal 7-)  |
   |  P12  |  3  |  AIN6+ (Analog input signal 6+)  |
   |  P12  |  4  |  AIN6- (Analog input signal 6-)  |
   |  P12  |  5  |  AIN5+ (Analog input signal 5+)  |
   |  P12  |  6  |  AIN5- (Analog input signal 5-)  |
   |  P12  |  7  |  AIN4+ (Analog input signal 4+)  |
   |  P12  |  8  |  AIN4- (Analog input signal 4-)  |
   
   **Table 6. Surfing connector**
   |  Connector  |  Pin  |  Signal  |
   |  P14  |  1  |  AIN7+ unfiltered  |
   |  P14  |  2  |  GND  |
   |  P14  |  3  |  VNEG for external board supply  |
   |  P14  |  4  |  VCM_OUT  |
   |  P14  |  5  |  VPOS for external board supply  |
   |  P14  |  6  |  GND  |
   |  P14  |  7  |  AIN7- unfiltered  |
   |  P18  |  1  |  AIN7+ unfiltered  |
   |  P18  |  2  |  GND  |
   |  P18  |  3  |  N.C.  |
   |  P18  |  4  |  N.C.  |
   |  P18  |  5  |  N.C.  |
   |  P18  |  6  |  GND  |
   |  P18  |  7  |  AIN7- unfiltered  |
   
   **Table 7. External reference voltage**
   |  Connector  |  Pin  |  Signal  |
   |  P20  |  1  |  Vref   |
   |  P20  |  2  |  AVSSx  |
   
   **Table 8. Interface connectors**
   |  Connector  |  Pin  |  Signal  |
   |  P1  |  1  |  NC  |
   |  P1  |  2  |  IOREF  |
   |  P1  |  3  |  RESET  |
   |  P1  |  4  |  +3.3V  |
   |  P1  |  5  |  +5V  |
   |  P1  |  6  |  GND  |
   |  P1  |  7  |  GND  |
   |  P1  |  8  |  VIN  |
   |  P2  |  1  |  NC  |
   |  P2  |  2  |  NC  |
   |  P2  |  3  |  NC  |
   |  P2  |  4  |  NC  |
   |  P2  |  5  |  NC  |
   |  P2  |  6  |  NC  |
   |  P3  |  1  |  ALT_SPI_MISO  |
   |  P3  |  2  |  +5V  |
   |  P3  |  3  |  ALT_SPI_SCL  |
   |  P3  |  4  |  ALT_SPI_MOSI  |
   |  P3  |  5  |  RESET  |
   |  P3  |  6  |  GND  |
   |  P4  |  1  |  DRDY_N  |
   |  P4  |  2  |  DCLK  |
   |  P4  |  3  |  CS_N  |
   |  P4  |  4  |  ARD_SPI_MOSI  |
   |  P4  |  5  |  ARD_SPI_MISO  |
   |  P4  |  6  |  ARD_SPI_SCK  |
   |  P4  |  7  |  GND  |
   |  P4  |  8  |  N.C.  |
   |  P4  |  9  |  SCL  |
   |  P4  |  10  |  SDA  |
   |  P5  |  1  |  DOUT3  |
   |  P5  |  2  |  CONVST  |
   |  P5  |  3  |  RESET_N  |
   |  P5  |  4  |  EXT_MCLK  |
   |  P5  |  5  |  DOUT2  |
   |  P5  |  6  |  DOUT1  |
   |  P5  |  7  |  DOUT0  |
   |  P5  |  8  |  START_N  |
   
   **Table 9. PMOD connectors**
   |  Connector  |  Pin  |  Signal  |
   |  P16  |  1  |  ALERT  |
   |  P16  |  2  |  SYNC_OUT_N  |
   |  P16  |  3  |  SYNC_IN_N  |
   |  P16  |  4  |  VIO  |
   |  P16  |  5  |  GND  |
   |  P16  |  6  |  IOVDD  |
   |  P16  |  7  |  GPIO0  |
   |  P16  |  8  |  GPIO1  |
   |  P16  |  9  |  GPIO2  |
   |  P16  |  10  |  ARD_EXT_VIN  |
   |  P16  |  11  |  GND  |
   |  P16  |  12  |  IOVDD  |
   |  P24  |  1  |  CS_N  |
   |  P24  |  2  |  SDI  |
   |  P24  |  3  |  SDO  |
   |  P24  |  4  |  SCLK  |
   |  P24  |  5  |  GND  |
   |  P24  |  6  |  IOVDD  |
   |  P24  |  7  |  EXT_MCLK  |
   |  P24  |  8  |  DRDY_N  |
   |  P24  |  9  |  DCLK  |
   |  P24  |  10  |  DOUT  |
   |  P24  |  11  |  GND  |
   |  P24  |  12  |  IOVDD  |
   |  P30  |  1  |  START_N  |
   |  P30  |  2  |  DOUT1  |
   |  P30  |  3  |  DOUT2  |
   |  P30  |  4  |  DOUT3  |
   |  P30  |  5  |  GND  |
   |  P30  |  6  |  IOVDD  |
   |  P30  |  7  |  RESET_N  |
   |  P30  |  8  |  CONVST  |
   |  P30  |  9  |  GND  |
   |  P30  |  10  |  GND  |
   |  P30  |  11  |  GND  |
   |  P30  |  12  |  IOVDD  |
   
   ===== Jumper configuration =====
   **Table 10. EVAL jumpers and switches**
   ^ Power Supply ^  Connector ^ Voltage Range ^ 
   |  S1   | Pos. 1-2; 4-5 | AVDD configuration: **(1)** Pos.1-2 and 4-5 => BIPOLAR: AVDD = 1.65V, AVSSX = -1.65V  **(2)** Pos.3-2 and 6-5 => UNIPOLAR: AVDD = 3.3V, AVSSX=0V |
   |  JP1  | Pos. B | AVSSX configuration: **(1)** Pos.A => EXT_AVSSX **(2)** Pos.B => ADP7182 |
   |  JP2  | Pos. B | AVDD1 configuration: **(1)** Pos.A => AVDD1 = EXT_AVDD1 **(2)** Pos.B => AVDD1 = ADP7118 |
   |  JP3  | Pos. B | AVDD2 configuration: **(1)** Pos.A => AVDD2 = EXT_AVDD2 **(2)** Pos.B => AVDD2 = ADP7118 |
   |  JP4  | Pos. B | AVDD4 configuration: **(1)** Pos.A => AVDD4 = EXT_AVDD4 **(2)** Pos.B => AVDD4 = ADP7118 |
   |  JP5  | Pos. A | Power supply for the Reference: (1) Pos.A => AVDD1  **(2)** Pos.B => VPOS |
   |  JP6  | Pos. A | ALERT configuration: **(1)** Pos.A => ALERT_SPI  **(2)** Pos.B => ALERT_PIN |
   |  JP7  | Pos. A | FORMAT1 configuration: **(1)** Pos.A => FORMAT1 = 1 **(2)** Pos.B => FORMAT1 = 0  **(3)** [FORMAT0, FORMAT1] = [1,1] => SPI CONTROL MODE **(4)** [FORMAT0, FORMAT1] = [0,X] => PIN CONTROL MODE **(5)** [FORMAT0, FORMAT1] = [X,0] => PIN CONTROL MODE |
   |  JP8  | Pos. A | FORMAT0 configuration: **(1)** Pos.A => FORMAT1 = 1 **(2)** Pos.B => FORMAT1 = 0  **(3)** [FORMAT0, FORMAT1] = [1,1] => SPI CONTROL MODE **(4)** [FORMAT0, FORMAT1] = [0,X] => PIN CONTROL MODE **(5)** [FORMAT0, FORMAT1] = [X,0] => PIN CONTROL MODE |
   |  JP9  | Pos. B | CLK selection: **(1)** Pos.A => CLK_SEL = 1 = Crystal  **(2)** Pos.B => CLK_SEL = 0 = CMOS |
   |  P10  | Inserted | Power from  Arduino |
   |  P13  | Pos. 5-6 | IOVDD configuration: **(1)** Pos.1-2 => EXT_IOVDD  **(2)** Pos.3-4 => VIO **(3)** Pos.5-6 => ADP7118 reference|
   |  P19  | Pos. 3-4 | VCM_OUT configuration: **(1)** Pos.1-2 => VCM_OUT = VCM **(2)** Pos.3-4 => VCM_OUT = ADA4896 **(3)** Pos.5-6 => VCM_OUT = GND|
   |  P22  | Pos. 1-2 | MODE3/ALERT configuration:**__(A)__** PIN control MODE: **(1)** Pos.3-4 => MODE3 = 1 = decimation configuration **(2)** Pos.5-6 => MODE3 = 0 = decimation configuration **__(B)__** SPI control MODE: **(1)** Pos.1-2 => ALERT_SPI|
   |  P23  | Pos. 1-2 | MODE1/ALERT configuration: **__(A)__** PIN control MODE: **(1)** Pos.3-4 => MODE1 = 1 = decimation configuration **(2)** Pos.5-6 => MODE1 = 0 = decimation configuration **__(B)__** SPI control MODE: **(1)** Pos.1-2 => ALERT_SPI|
   |  P25  | Pos. 1-2 | MODE2/ALERT configuration: **__(A)__** PIN control MODE: **(1)** Pos.3-4 => MODE2 = 1 = decimation configuration **(2)** Pos.5-6 => MODE2 = 0 = decimation configuration **__(B)__** SPI control MODE: **(1)** Pos.1-2 => ALERT_SPI|
   |  P26  | Pos. 1-2 | MODE0/ALERT configuration: **__(A)__** PIN control MODE: **(1)** Pos.3-4 => MODE0 = 1 = decimation configuration **(2)** Pos.5-6 => MODE0 = 0 = decimation configuration **__(B)__** SPI control MODE: **(1)** Pos.1-2 => ALERT_SPI|
   |  P27  | Pos. 1-2 | CONVST configuration: **__(A)__** PIN control MODE: **(1)** Pos.1-2 => CONVST_SAR = 1 = output via SPI (2) Pos.3-4 => CONVST_SAR = Start for SAR conversion **(3)** Pos.5-6: CONVST_SAR = 0 => output via DOUTx **__(B)__** SPI control MODE: **(1)** CONVST_SAR works as start for SAR |
   |  P28  | Open | MUX connected to AUX+ |
   |  P29  | Open | MUX connected to AUX- |
   |  P33  | Removed | AVSSX connection to GND |
   |  P34  | Removed | AVSSX connection to GND |
   |  P35  | Removed | AVSSX connection to GND |
   |  P36  | Removed | AVSSX connection to GND |
   |  P37  | Removed | AVSSX connection to GND |
   
   {{:resources:eval:user-guides:jumper_config.drawio.png|}}
   
   ===== Schematic =====
   {{ :resources:eval:user-guides:02_068869a_top_20211220.pdf |}}
   ==== Top Level ====
   The top level is formed by the interconnection of all different blocks: Power supplies, Analog filter, reference, ADC and the interface.
   
   The input power for the EVAL is either externally supplied by P9 or by the host connected with the Arduino interface. This voltage is internally used in the "POWERSUPPLIES" block to generate AVDD and IOVDD.
   
   P7 and P8 are used to generate externally AVDD and IOVDD and supply the ADC. 
   
   Jumpers P33, P34, P35, P36 and P37 are used to **short AVSSx** to GND when **Unipolar** supply is used and thereby reduce the noise in the different ground layers. 
   
   {{:resources:eval:user-guides:topview_sch.png|}}
   ==== Power Supplies ====
   
   The AD777x family requires up to 5 different supply voltages which can be easily configured thanks to jumpers and the switch S1 available in the EVAL.
   
   When the default configuration is used, the ADC supply voltages are internally generated with 3 LDOS. The LDOS are connected to the outputs of a dual DC-to-DC Switching Regulator which generates two intermediate voltage -4V and 4V. The usage of LDOs help reducing the noise injected to the ADC.
   
   IOVDD can be selected with P13. The internal 3.3V LDO is used by default. Two other options can be configured: VIO coming from the Arduino host or an external IOVDD connected to the connector P8.
      
   The AD777x can be operated in bipolar or unipolar mode. When S1 is in position 1-2 and 4-5, AVSS and AVDD are configured in bipolar mode. In bipolar mode U4 will generate 1.65V and AVSSx is connected to the output of JP1, which will be either -1.65V (U5) or the voltage externally connected to P7.4.
   
   When S1 is in position 3-2 and 6-5 the ADC is configured in unipolar mode and therefore AVSSX is grounded and AVDDx is either the external voltage connected to P7.1, P7.2 and P.7.3 or the 3.3V generated by U4. 
   
   
   {{:resources:eval:user-guides:power_supplies_sch.png|}}
   ==== Analog Input filter ====
   To provide some flexibility to the user, several different analog filter configurations can be found in the evaluation board. The default resistor values are 0Ohm,and the capacitors are nor populated so no filter is implemented to the input signal.
   
   Analog input signals are connected to P11 and P12 but channels CH0, CH1, CH2 and CH3 also have a second SMB connector in case a more precise measurements are required.
   
   CH1 and CH2 are an example of a real protection circuit for noisy industrial environments where bidirectional TVS and protection diodes are necessary for ESD protection.
   
   If R175 and R176 are removed, CH7 can be used together AMC-ADAxxxx-2ARMZ (Amplifier Mezzanine Card for ADC Drivers) to test the performance of the ADC with different input filter. The AMC can support any of Analog Devices operational amplifiers and ADC drivers in different packages. The user can configure the ADC driver as a Sallen-Key low-pass, high-pass, or band-pass filter, as a multiple feedback low-pass, high-pass, or band-pass filter, or as an inverting and noninverting operational amplifier. The user can also configure the AMC to drive a single-ended, fully differential, or a single-ended signal to a differential ADC.
   
   {{:resources:eval:user-guides:ain_sch.png|}}
   ==== VCM and Reference ====
   This block is the responsible for the generation of the ADC reference and the common mode voltage.
   
   Depending on the resistor mounted (R102, R101 or R103) the ADC reference voltage can be supplied by an discrete reference (R102), by the ADC itself (R101) or by a buffer connected to the output of the reference mentioned before (R103). Furthermore, two connector are provided (J10 and P20) just in case an external reference is desired. 
    
   The default Reference IC used in the EVAL is the LTC665LNBHMS8-2.5 but it is also possible to replace this reference with LTC6658BHMS8-2.5 or with ADR441ARMZ in which case the proper components must be mounted.
   
   P19 is used to select the ADC common mode voltage. There are two option: connect the common mode voltage directly to the ADC's output VCM or use a intermediate buffer.
   
   {{:resources:eval:user-guides:reference_sch.png|}}
   ==== Interface ====
   
   
   
   The AD777x communicates with the host via SPI. There are four primary signals: CS, SCLK, SDI, and SDO/RDY (all are inputs, except for SDO/RDY, which is an output).
   ===Serial communication options===
   
     - Arduino connection 
     - PMOD connector
   
   For an introduction to the Serial Peripheral Interface (SPI), click [[adi>en/analog-dialogue/articles/introduction-to-spi-interface.html|here]]
   
   {{ :resources:eval:user-guides:eval-ad7124:eval-ad7124:hardware_guide:spi_pic.png?direct&600 |}}
   
   The readout values are sent to the host either via SPI commands of via DOUTx channels. Due to the limited number of readout values that a uC can process, the Zio extension has been added which allows some uC to use the audio SAI input interface to enhance the number of readout samples.
   
   Since there exist two types of Board using the Zio extension, some resistors has been added to configure the SAI interface depending on the board selected. The resistors need to be mounted accordingly.
   
   The EEPROM is only used for the Host to identify which EVAL has been plugged.
   
   {{:resources:eval:user-guides:interface_sch.png|}}
   
   ==== AD777x ====
   The AD777x has multiple possible configurations and the following list will try to summarize how to configure it correctly with the existing hardware:
     * Clock:4 different clock sources can be used depending on the resistors mounted: Crystal, CMOS, EXT_MCLK from Arduino interface or connector J13.
     * SPI/ PIN control mode can be configured via JP7 (FORMAT1) and JP8 (FORMAT0). If both jumpers are set high, the device is configured in SPI control mode, otherwise pin control mode.
     *  P22, P23, P25 and P26, are used to configured the decimation rate and the number of channels in pin control mode. In SPI mode control P23, P25 and P25 can cause a conflict with the configuration of the pins if they are configured as an output, so care must be taken with the jumper position. P22 in SPI control must be in position 1-2 since this pin will behave as an error flag.
     * JP6 is used for the host as an error flag either in SPI or pin control mode
     * R129 must be mounted if the SRC update is done via GPIO0 instead being done via SPI commands.
     * R135 and R136 must be mounted depending on the selected mode to set properly the ALER/CS pin: R136 mounted to used the pin as SPI chip selec; R135 to use the pin as error flag in pin control mode.
     * With resistors R137, R138 and R139 can be selected the MCLK divider in pin control mode. In SPI control mode only R137 must be assembled to function as SDI pin. 
     * With resistors R140, R141 and R142 can be selected the MCLK divider in pin control mode. In SPI control mode only R140 must be assembled to function as SCLK pin.
     * With resistors R172, R173 and R174 can be selected the MCLK divider in pin control mode. In SPI control mode only R172 must be assembled to function as SDO pin.
     * JP9 is used for the clock source type selection: high for CMOS and low for Csytal.
     * P27 together with JP7 and JP8 is used in pin control mode for the output data format selection. In SPI control mode P27 should be connected to position 1-2. In this case CONVST_SAR works as start for SAR conversion.
    
   {{:resources:eval:user-guides:adc_sch.png|}}
   
   ====== Quick Start Guides ======
   ++++ Linux on ZedBoard |
   
   <WRAP>
   
   ==== Prerequisites ====
   === Required Hardware ===
     *	[[https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/ | ZedBoard]] Rev D or later board
     * AD777x-ARDZ board 
     * An 8GB SD card  
     * Ethernet cable
     * 1 x Micro-USB cable
   
   
   === Required Software ===
     * You need a Host PC (Windows or Linux) 
     * A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)
     * IIO Scope [[ https://github.com/analogdevicesinc/iio-oscilloscope/releases|Download]]
   
   
   ==== Creating / Configuring the SD Card ====
   
   <note tip>[[:resources:tools-software:linux-software:kuiper-linux | Create SD Image for Zynq Boards. (it is a single image for all boards).]]</note>
     
   == In this case the root of 'BOOT' should contain: ==
     *''uImage file for Zynq''
     *''BOOT.BIN specific to your AD777x-ARDZ + ZedBoard''
     *''devicetree.dtb for Zynq specific to your AD777x-ARDZ + ZedBoard''
   
   ==== Setting up the hardware (ZedBoard) ====
   
   You will need to:
   
     * Get the [[https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/ | ZedBoard]].\\ {{ resources:fpga:xilinx:fmc:AD777x-ARDZ:zedboard.png?600 }}
     * Insert the SD-CARD into the SD Card Interface Connector (J12). \\
     * Connect the AD777x-ARDZ as described here: \\
   \\
   ^  AD777x-ARDZ PMOD  ^  ZedBoard PMOD ^
   |  P24  |  JA  |
   |  P16  |  JB  |
   |  P30  |  JC  | \\
   
     * Connect USB UART J14 (Micro USB) to your host PC. \\
     * Plug your ethernet cable into the RJ45 ethernet connector(J11). \\
     * Plug the Power Supply into 12V Power input connector (J20) (DO NOT turn the device on). \\
     * Set the jumpers as seen in the below picture: {{ resources:fpga:xilinx:fmc:adaq8092:zed_jumpers.jpg?400 }} \\
     * Turn it on. \\
     * Wait ~30 seconds for the “DONE” LED to turn blue. This is near the DISP1. \\
     
   {{page>wiki/common#esd_warning&nofooter&noheader}}
   
   
   ==== Booting the SD Card ====
   === Remote IIO Oscilloscope ===
   
     * Observe kernel and serial console messages on your UART terminal (use the first ttyUSB or COM port resisted): \\
   <hidden Complete kernel boot log (Click to expand)>
   <WRAP box bggreen>
   <code>
   U-Boot 2018.01-21439-gd244ce5 (Jul 29 2021 - 16:33:01 +0100), Build: jenkins-development-build_uboot-1
   
   Model: Zynq Zed Development Board
   Board: Xilinx Zynq
   Silicon: v3.1
   DRAM:  ECC disabled 512 MiB
   MMC:   sdhci@e0100000: 0 (SD)
   SF: Detected s25fl256s_64k with page size 256 Bytes, erase size 64 KiB, total 32 MiB
   In:    serial@e0001000
   Out:   serial@e0001000
   Err:   serial@e0001000
   Net:   ZYNQ GEM: e000b000, phyaddr 0, interface rgmii-id
   eth0: ethernet@e000b000
   Hit any key to stop autoboot:  0
   Device: sdhci@e0100000
   Manufacturer ID: 3
   OEM: 5344
   Name: SC32G
   Tran Speed: 50000000
   Rd Block Len: 512
   SD version 3.0
   High Capacity: Yes
   Capacity: 29.7 GiB
   Bus Width: 4-bit
   Erase Group Size: 512 Bytes
   reading uEnv.txt
   407 bytes read in 16 ms (24.4 KiB/s)
   Loaded environment from uEnv.txt
   Importing environment from SD ...
   Running uenvcmd ...
   Copying Linux from SD to RAM...
   reading uImage
   7006656 bytes read in 416 ms (16.1 MiB/s)
   reading devicetree.dtb
   16291 bytes read in 24 ms (662.1 KiB/s)
   ** Unable to read file uramdisk.image.gz **
   ## Booting kernel from Legacy Image at 03000000 ...
      Image Name:   Linux-5.10.0-98063-g1d94258e8ab2
      Image Type:   ARM Linux Kernel Image (uncompressed)
      Data Size:    7006592 Bytes = 6.7 MiB
      Load Address: 00008000
      Entry Point:  00008000
      Verifying Checksum ... OK
   ## Flattened Device Tree blob at 02a00000
      Booting using the fdt blob at 0x2a00000
      Loading Kernel Image ... OK
      Loading Device Tree to 1eb12000, end 1eb18fa2 ... OK
   
   Starting kernel ...
   
   Booting Linux on physical CPU 0x0
   Linux version 5.10.0-98063-g1d94258e8ab2-dirty (ppop@romlx4.adlk.analog.com) (arm-none-linux-gnueabihf-gcc (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16)) 10.2.1 20201103, GNU ld (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16)) 2.35.1.20201028) #47 SMP PREEMPT Wed May 11 16:42:49 IST 2022
   CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=18c5387d
   CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   OF: fdt: Machine model: Xilinx Zynq ZED
   OF: fdt: earlycon: stdout-path /amba@0/uart@E0001000 not found
   Memory policy: Data cache writealloc
   cma: Reserved 128 MiB at 0x16800000
   Zone ranges:
     Normal   [mem 0x0000000000000000-0x000000001fffffff]
     HighMem  empty
   Movable zone start for each node
   Early memory node ranges
     node   0: [mem 0x0000000000000000-0x000000001fffffff]
   Initmem setup node 0 [mem 0x0000000000000000-0x000000001fffffff]
   percpu: Embedded 15 pages/cpu s29900 r8192 d23348 u61440
   Built 1 zonelists, mobility grouping on.  Total pages: 130048
   Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1
   Dentry cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
   Inode-cache hash table entries: 32768 (order: 5, 131072 bytes, linear)
   mem auto-init: stack:off, heap alloc:off, heap free:off
   Memory: 367344K/524288K available (10240K kernel code, 775K rwdata, 7300K rodata, 1024K init, 169K bss, 25872K reserved, 131072K cma-reserved, 0K highmem)
   rcu: Preemptible hierarchical RCU implementation.
   rcu:    RCU event tracing is enabled.
   rcu:    RCU restricting CPUs from NR_CPUS=4 to nr_cpu_ids=2.
           Trampoline variant of Tasks RCU enabled.
   rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
   rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=2
   NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
   efuse mapped to (ptrval)
   slcr mapped to (ptrval)
   L2C: platform modifies aux control register: 0x72360000 -> 0x72760000
   L2C: DT/platform modifies aux control register: 0x72360000 -> 0x72760000
   L2C-310 erratum 769419 enabled
   L2C-310 enabling early BRESP for Cortex-A9
   L2C-310 full line of zeros enabled for Cortex-A9
   L2C-310 ID prefetch enabled, offset 1 lines
   L2C-310 dynamic clock gating enabled, standby mode enabled
   L2C-310 cache controller enabled, 8 ways, 512 kB
   L2C-310: CACHE_ID 0x410000c8, AUX_CTRL 0x76760001
   random: get_random_bytes called from start_kernel+0x338/0x4d8 with crng_init=0
   zynq_clock_init: clkc starts at (ptrval)
   Zynq clock init
   sched_clock: 64 bits at 333MHz, resolution 3ns, wraps every 4398046511103ns
   clocksource: arm_global_timer: mask: 0xffffffffffffffff max_cycles: 0x4ce07af025, max_idle_ns: 440795209040 ns
   Switching to timer-based delay loop, resolution 3ns
   clocksource: ttc_clocksource: mask: 0xffff max_cycles: 0xffff, max_idle_ns: 537538477 ns
   timer #0 at (ptrval), irq=25
   Console: colour dummy device 80x30
   Calibrating delay loop (skipped), value calculated using timer frequency.. 666.66 BogoMIPS (lpj=3333333)
   pid_max: default: 32768 minimum: 301
   Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
   Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
   CPU: Testing write buffer coherency: ok
   CPU0: Spectre v2: using BPIALL workaround
   CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
   Setting up static identity map for 0x100000 - 0x100060
   rcu: Hierarchical SRCU implementation.
   smp: Bringing up secondary CPUs ...
   CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
   CPU1: Spectre v2: using BPIALL workaround
   smp: Brought up 1 node, 2 CPUs
   SMP: Total of 2 processors activated (1333.33 BogoMIPS).
   CPU: All CPU(s) started in SVC mode.
   devtmpfs: initialized
   VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
   clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
   futex hash table entries: 512 (order: 3, 32768 bytes, linear)
   pinctrl core: initialized pinctrl subsystem
   NET: Registered protocol family 16
   DMA: preallocated 256 KiB pool for atomic coherent allocations
   thermal_sys: Registered thermal governor 'step_wise'
   hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
   hw-breakpoint: maximum watchpoint size is 4 bytes.
   zynq-ocm f800c000.ocmc: ZYNQ OCM pool: 256 KiB @ 0x(ptrval)
   e0001000.serial: ttyPS0 at MMIO 0xe0001000 (irq = 33, base_baud = 3125000) is a xuartps
   printk: console [ttyPS0] enabled
   SCSI subsystem initialized
   usbcore: registered new interface driver usbfs
   usbcore: registered new interface driver hub
   usbcore: registered new device driver usb
   mc: Linux media interface: v0.10
   videodev: Linux video capture interface: v2.00
   jesd204: found 0 devices and 0 topologies
   FPGA manager framework
   Advanced Linux Sound Architecture Driver Initialized.
   clocksource: Switched to clocksource arm_global_timer
   NET: Registered protocol family 2
   tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
   TCP established hash table entries: 4096 (order: 2, 16384 bytes, linear)
   TCP bind hash table entries: 4096 (order: 3, 32768 bytes, linear)
   TCP: Hash tables configured (established 4096 bind 4096)
   UDP hash table entries: 256 (order: 1, 8192 bytes, linear)
   UDP-Lite hash table entries: 256 (order: 1, 8192 bytes, linear)
   NET: Registered protocol family 1
   hw perfevents: no interrupt-affinity property for /pmu@f8891000, guessing.
   hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
   workingset: timestamp_bits=30 max_order=17 bucket_order=0
   io scheduler mq-deadline registered
   io scheduler kyber registered
   zynq-pinctrl 700.pinctrl: zynq pinctrl initialized
   dma-pl330 f8003000.dmac: Loaded driver for PL330 DMAC-241330
   dma-pl330 f8003000.dmac:        DBUFF-128x8bytes Num_Chans-8 Num_Peri-4 Num_Events-16
   brd: module loaded
   loop: module loaded
   Registered mathworks_ip class
   spi-nor spi1.0: found s25fl256s1, expected n25q128a11
   spi-nor spi1.0: s25fl256s1 (32768 Kbytes)
   5 fixed-partitions partitions found on MTD device spi1.0
   Creating 5 MTD partitions on "spi1.0":
   0x000000000000-0x000000500000 : "boot"
   0x000000500000-0x000000520000 : "bootenv"
   0x000000520000-0x000000540000 : "config"
   0x000000540000-0x000000fc0000 : "image"
   0x000000fc0000-0x000002000000 : "spare"
   MACsec IEEE 802.1AE
   libphy: Fixed MDIO Bus: probed
   tun: Universal TUN/TAP device driver, 1.6
   libphy: MACB_mii_bus: probed
   macb e000b000.ethernet eth0: Cadence GEM rev 0x00020118 at 0xe000b000 irq 36 (aa:bb:cc:dd:ee:ff)
   usbcore: registered new interface driver asix
   usbcore: registered new interface driver ax88179_178a
   usbcore: registered new interface driver cdc_ether
   usbcore: registered new interface driver net1080
   usbcore: registered new interface driver cdc_subset
   usbcore: registered new interface driver zaurus
   usbcore: registered new interface driver cdc_ncm
   ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
   usbcore: registered new interface driver uas
   usbcore: registered new interface driver usb-storage
   usbcore: registered new interface driver usbserial_generic
   usbserial: USB Serial support registered for generic
   usbcore: registered new interface driver ftdi_sio
   usbserial: USB Serial support registered for FTDI USB Serial Device
   usbcore: registered new interface driver upd78f0730
   usbserial: USB Serial support registered for upd78f0730
   ULPI transceiver vendor/product ID 0x0451/0x1507
   Found TI TUSB1210 ULPI transceiver.
   ULPI integrity check: passed.
   ci_hdrc ci_hdrc.0: EHCI Host Controller
   ci_hdrc ci_hdrc.0: new USB bus registered, assigned bus number 1
   ci_hdrc ci_hdrc.0: USB 2.0 started, EHCI 1.00
   usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
   usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
   usb usb1: Product: EHCI Host Controller
   usb usb1: Manufacturer: Linux 5.10.0-98063-g1d94258e8ab2-dirty ehci_hcd
   usb usb1: SerialNumber: ci_hdrc.0
   hub 1-0:1.0: USB hub found
   hub 1-0:1.0: 1 port detected
   i2c /dev entries driver
   adv7511 0-0039: supply avdd not found, using dummy regulator
   adv7511 0-0039: supply dvdd not found, using dummy regulator
   adv7511 0-0039: supply pvdd not found, using dummy regulator
   adv7511 0-0039: supply bgvdd not found, using dummy regulator
   adv7511 0-0039: supply dvdd-3v not found, using dummy regulator
   at24 1-0050: supply vcc not found, using dummy regulator
   xiic-i2c 41620000.i2c: Timeout waiting at Tx empty
   xiic-i2c 41620000.i2c: Timeout waiting at Tx empty
   regulator-dummy: Underflow of regulator enable count
   usbcore: registered new interface driver uvcvideo
   USB Video Class driver (1.1.1)
   gspca_main: v2.14.0 registered
   cdns-wdt f8005000.watchdog: Xilinx Watchdog Timer with timeout 10s
   Xilinx Zynq CpuIdle Driver started
   failed to register cpuidle driver
   sdhci: Secure Digital Host Controller Interface driver
   sdhci: Copyright(c) Pierre Ossman
   sdhci-pltfm: SDHCI platform and OF driver helper
   ledtrig-cpu: registered to indicate activity on CPUs
   hid: raw HID events driver (C) Jiri Kosina
   usbcore: registered new interface driver usbhid
   usbhid: USB HID core driver
   mmc0: SDHCI controller on e0100000.mmc [e0100000.mmc] using ADMA
   mmc0: new high speed SDHC card at address aaaa
   mmcblk0: mmc0:aaaa SC32G 29.7 GiB
    mmcblk0: p1 p2 p3
   cf_axi_adc 43c00000.cf_axi_adc: ADI AIM (10.01.b) at 0x43C00000 mapped to 0x(ptrval), probed ADC ad7768_axi_adc as MASTER
   axi_sysid 45000000.axi-sysid-0: AXI System ID core version (1.01.a) found
   axi_sysid 45000000.axi-sysid-0: [ad777x_ardz] on [zed] git branch <ad777x_dev> git <f29163e21f9463dc8fd5605e48e406ea25ffabe7> clean [2022-05-12 12:54:58] UTC
   fpga_manager fpga0: Xilinx Zynq FPGA Manager registered
   usbcore: registered new interface driver snd-usb-audio
   axi-i2s 77600000.axi-i2s: probed, capture enabled, playback enabled
   NET: Registered protocol family 10
   Segment Routing with IPv6
   sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
   NET: Registered protocol family 17
   NET: Registered protocol family 36
   Registering SWP/SWPB emulation handler
   [drm] Initialized axi_hdmi_drm 1.0.0 20120930 for 70e00000.axi_hdmi on minor 0
   axi-hdmi 70e00000.axi_hdmi: [drm] Cannot find any crtc or sizes
   clk: Not disabling unused clocks
   ALSA device list:
     #0: HDMI monitor
     #1: ZED ADAU1761
   EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
   VFS: Mounted root (ext4 filesystem) on device 179:2.
   devtmpfs: mounted
   Freeing unused kernel memory: 1024K
   Run /sbin/init as init process
   random: fast init done
   systemd[1]: System time before build time, advancing clock.
   systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
   systemd[1]: Detected architecture arm.
   
   Welcome to Kuiper GNU/Linux 10 (buster)!
   
   systemd[1]: Set hostname to <analog>.
   systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
   systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
   systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of section. Ignoring.
   systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of section. Ignoring.
   random: systemd: uninitialized urandom read (16 bytes read)
   random: systemd: uninitialized urandom read (16 bytes read)
   systemd[1]: Listening on udev Kernel Socket.
   [  OK  ] Listening on udev Kernel Socket.
   random: systemd: uninitialized urandom read (16 bytes read)
   systemd[1]: Reached target Swap.
   [  OK  ] Reached target Swap.
   systemd[1]: Created slice system-systemd\x2dfsck.slice.
   [  OK  ] Created slice system-systemd\x2dfsck.slice.
   [  OK  ] Created slice system-serial\x2dgetty.slice.
   [  OK  ] Listening on udev Control Socket.
   [  OK  ] Created slice system-getty.slice.
   [  OK  ] Listening on Journal Socket (/dev/log).
   [  OK  ] Listening on Syslog Socket.
   [  OK  ] Listening on fsck to fsckd communication Socket.
   [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
   [  OK  ] Created slice User and Session Slice.
   [  OK  ] Reached target Slices.
   [  OK  ] Listening on Journal Socket.
            Starting Set the console keyboard layout...
            Starting Load Kernel Modules...
            Starting udev Coldplug all Devices...
            Mounting Kernel Debug File System...
            Starting Restore / save the current clock...
            Starting Journal Service...
            Mounting RPC Pipe File System...
   [  OK  ] Listening on initctl Compatibility Named Pipe.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Mounted Kernel Debug File System.
   [  OK  ] Started Restore / save the current clock.
   [FAILED] Failed to mount RPC Pipe File System.
   See 'systemctl status run-rpc_pipefs.mount' for details.
   [DEPEND] Dependency failed for RPC …curity service for NFS server.
   [DEPEND] Dependency failed for RPC …ice for NFS client and server.
   [  OK  ] Started Journal Service.
   [  OK  ] Reached target NFS client services.
   [  OK  ] Reached target Remote File Systems (Pre).
   [  OK  ] Reached target Remote File Systems.
            Starting Remount Root and Kernel File Systems...
            Starting Apply Kernel Variables...
            Mounting Kernel Configuration File System...
   [  OK  ] Started Set the console keyboard layout.
   [  OK  ] Mounted Kernel Configuration File System.
   [  OK  ] Started Apply Kernel Variables.
   [  OK  ] Started udev Coldplug all Devices.
            Starting Helper to synchronize boot up for ifupdown...
   [  OK  ] Started Helper to synchronize boot up for ifupdown.
   [  OK  ] Started Remount Root and Kernel File Systems.
            Starting Load/Save Random Seed...
            Starting Flush Journal to Persistent Storage...
            Starting Create System Users...
   [  OK  ] Started Load/Save Random Seed.
   [  OK  ] Started Create System Users.
   [  OK  ] Started Flush Journal to Persistent Storage.
            Starting Create Static Device Nodes in /dev...
   [  OK  ] Started Create Static Device Nodes in /dev.
   [  OK  ] Reached target Local File Systems (Pre).
            Starting udev Kernel Device Manager...
   [  OK  ] Started udev Kernel Device Manager.
            Starting Show Plymouth Boot Screen...
   [  OK  ] Started Show Plymouth Boot Screen.
   [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
   [  OK  ] Reached target Local Encrypted Volumes.
            Starting Load Kernel Modules...
   [  OK  ] Found device /dev/ttyPS0.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Found device /dev/disk/by-partuuid/18f1f9d5-01.
            Starting File System Check…isk/by-partuuid/18f1f9d5-01...
   [  OK  ] Started File System Check Daemon to report status.
            Starting Load Kernel Modules...
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Started File System Check …/disk/by-partuuid/18f1f9d5-01.
            Mounting /boot...
   [  OK  ] Mounted /boot.
   [  OK  ] Reached target Local File Systems.
            Starting Preprocess NFS configuration...
            Starting Tell Plymouth To Write Out Runtime Data...
            Starting Raise network interfaces...
            Starting Set console font and keymap...
            Starting Create Volatile Files and Directories...
   [  OK  ] Started Preprocess NFS configuration.
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [  OK  ] Started Set console font and keymap.
   [  OK  ] Started Create Volatile Files and Directories.
   [  OK  ] Started Raise network interfaces.
            Starting Tell Plymouth To Write Out Runtime Data...
            Starting Load Kernel Modules...
            Starting Update UTMP about System Boot/Shutdown...
            Starting Network Time Synchronization...
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Started Update UTMP about System Boot/Shutdown.
   [  OK  ] Started Network Time Synchronization.
   [  OK  ] Reached target System Initialization.
   [  OK  ] Listening on triggerhappy.socket.
   [  OK  ] Listening on CUPS Scheduler.
   [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
   [  OK  ] Started CUPS Scheduler.
   [  OK  ] Reached target Paths.
   [  OK  ] Started Daily Cleanup of Temporary Directories.
   [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
   [  OK  ] Listening on D-Bus System Message Bus Socket.
   [  OK  ] Reached target Sockets.
   [  OK  ] Reached target Basic System.
   [  OK  ] Started Regular background program processing daemon.
            Starting Modem Manager...
            Starting dphys-swapfile - …unt, and delete a swap file...
   [  OK  ] Started tof-server.service.
   [  OK  ] Started Manage Sound Card State (restore and store).
            Starting LSB: Switch to on…nless shift key is pressed)...
            Starting Disk Manager...
            Starting Check for Raspberry Pi EEPROM updates...
            Starting Avahi mDNS/DNS-SD Stack...
            Starting rng-tools.service...
            Starting triggerhappy global hotkey daemon...
            Starting dhcpcd on all interfaces...
   [  OK  ] Started CUPS Scheduler.
            Starting Save/Restore Sound Card State...
            Starting Login Service...
   [  OK  ] Started D-Bus System Message Bus.
            Starting WPA supplicant...
            Starting System Logging Service...
   [  OK  ] Reached target System Time Synchronized.
   [  OK  ] Started Daily man-db regeneration.
   [  OK  ] Started Daily rotation of log files.
   [  OK  ] Started Daily apt download activities.
   [  OK  ] Started Daily apt upgrade and clean activities.
   [  OK  ] Reached target Timers.
   [  OK  ] Started triggerhappy global hotkey daemon.
   [  OK  ] Started Check for Raspberry Pi EEPROM updates.
   [FAILED] Failed to start rng-tools.service.
   See 'systemctl status rng-tools.service' for details.
   [  OK  ] Started System Logging Service.
   [  OK  ] Started dhcpcd on all interfaces.
   [  OK  ] Started Save/Restore Sound Card State.
   [  OK  ] Started dphys-swapfile - s…mount, and delete a swap file.
   [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
            Starting Authorization Manager...
   [  OK  ] Reached target Sound Card.
   [  OK  ] Started WPA supplicant.
   [  OK  ] Started Login Service.
   [  OK  ] Started Avahi mDNS/DNS-SD Stack.
   [  OK  ] Started Make remote CUPS printers available locally.
   [  OK  ] Reached target Network.
            Starting OpenBSD Secure Shell server...
            Starting Permit User Sessions...
   [  OK  ] Started IIO Daemon.
            Starting /etc/rc.local Compatibility...
            Starting HTTP based time synchronization tool...
   [  OK  ] Started Permit User Sessions.
   [  OK  ] Started /etc/rc.local Compatibility.
   [  OK  ] Started Authorization Manager.
            Starting Hold until boot process finishes up...
            Starting Light Display Manager...
   [  OK  ] Started HTTP based time synchronization tool.
   [  OK  ] Started Modem Manager.
   [  OK  ] Started OpenBSD Secure Shell server.
   
   Raspbian GNU/Linux 10 analog ttyPS0
   
   analog login: root (automatic login)
   
   Last login: Sat Feb 27 10:00:52 GMT 2021 on ttyPS0
   Linux analog 5.10.0-98063-g1d94258e8ab2-dirty #47 SMP PREEMPT Wed May 11 16:42:49 IST 2022 armv7l
   
   The programs included with the Debian GNU/Linux system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.
   
   Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
   permitted by applicable law.
   root@analog:~#
   </code></WRAP>
   </hidden>
   \\
   ^  user  ^  password  ^
   |  root  |  analog  |
   \\
     * Run the ifconfig command on your UART terminal and get your board IP. \\ 
   <code>
   root@analog:~# ifconfig
   eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet your_board_ip  netmask 255.255.255.0  
           inet6 fe80::8e1e:23ed:a7c3:9897  prefixlen 64  scopeid 0x20<link>
           ether aa:bb:cc:dd:ee:ff  txqueuelen 1000  (Ethernet)
           RX packets 1757  bytes 1013110 (989.3 KiB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 575  bytes 52441 (51.2 KiB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
           device interrupt 36  base 0xb000
   root@analog:~#
   </code>
   \\
     * Open IIO Scope application and type ip:board_ip in the URI tab. \\ {{ resources:fpga:xilinx:fmc:ad777x-ardz:iioosc_remote_ad777x_ardz_zed_login.jpg?400 }} \\
   
   You should see two screens: \\
   
   {{ resources:fpga:xilinx:fmc:ad777x-ardz:iioosc_capture_ad777x_zed.jpg?850 }}
   //
   //
   <WRAP important round>Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ''sudo shutdown -h now''
   {{:resources:fpga:xilinx:fmc:ad-fmcomms1-ebz:shutdown.png?300|}}
   
   </WRAP>
   
   </WRAP>
   ++++
   
   ++++ Linux on DE10Nano |
   
   <WRAP>
   
   ==== Prerequisites ====
   === Required Hardware ===
     *	[[https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046 | DE10-Nano FPGA Board]]
     * 5V/2A Wall Power supply with barrel jack (comes with DE10-Nano)
     * AD777x-ARDZ board 
     * An 8GB Micro-SD Card 
     * Ethernet cable
     * 1 x Mini-USB cable
   
   
   === Required Software ===
     * You need a Host PC (Linux) 
     * A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)
     * IIO Scope [[ https://github.com/analogdevicesinc/iio-oscilloscope/releases|Download]]
   
   ===== Creating the Micro-SD Card =====
   
   <note tip>[[:resources:tools-software:linux-software:kuiper-linux | Create SD Image for DE10Nano SoCkit board. (it is a single image for all boards).]]</note>
   ====  Configuring the Micro-SD Card ====
   <code>
   analog@analog:~ $ lsblk
   
   NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
   sdb           8:16   1 29.7G  0 disk
   ├─sdb1        8:17   1    1G  0 part /media/analog/BOOT
   ├─sdb2        8:18   1  9.8G  0 part /media/analog/rootfs
   └─sdb3        8:19   1    4M  0 part
   
   analog@analog:~ $ cd /media/analog/BOOT/socfpga_de10nano_sockit_ad777x_ardz
   analog@analog:/media/analog/BOOT/socfpga_de10nano_sockit_ad777x_ardz $ ls -l
   
   total 10248
   -rwxr-xr-x 1 root root  500432 Jul 27 15:06 u-boot-with-spl.sfp
   -rwxr-xr-x 1 root root   25291 Jul 27 15:06 socfpga.dtb
   -rwxr-xr-x 1 root root 2685848 Jul 27 15:06 soc_system.rbf
   -rwxr-xr-x 1 root root     200 Jul 27 15:06 u-boot.scr
   -rwxr-xr-x 1 root root 7269944 Jul 27 15:06 zImage
   -rwxr-xr-x 1 root root     142 Jul 27 15:06 extlinux.conf
   
   analog@analog:/media/analog/BOOT/socfpga_de10nano_sockit_ad777x_ardz $ sudo cp socfpga.dtb /media/analog/BOOT/socfpga.dtb
   analog@analog:/media/analog/BOOT/socfpga_de10nano_sockit_ad777x_ardz $ sudo cp zImage /media/analog/BOOT/zImage
   analog@analog:/media/analog/BOOT/socfpga_de10nano_sockit_ad777x_ardz $ sudo cp extlinux.conf /media/analog/BOOT/extlinux/extlinux.conf
   analog@analog:/media/analog/BOOT/socfpga_de10nano_sockit_ad777x_ardz $ sudo cp u-boot.scr /media/analog/BOOT/u-boot.scr
   analog@analog:/media/analog/BOOT/socfpga_de10nano_sockit_ad777x_ardz $ sudo cp soc_system.rbf /media/analog/BOOT/soc_system.rbf
   analog@analog:/media/analog/BOOT/socfpga_de10nano_sockit_ad777x_ardz $ sudo dd if=u-boot-with-spl.sfp of=/dev/sdb3
   
   977+1 records in
   977+1 records out
   500432 bytes (500 kB, 489 KiB) copied, 0.138791 s, 3.6 MB/s
   
   analog@analog:/media/analog/BOOT/socfpga_de10nano_sockit_ad777x_ardz $ sync
   analog@analog:/media/analog/BOOT/socfpga_de10nano_sockit_ad777x_ardz $ cd ../../
   analog@analog:/media/analog $ sudo umount /dev/sdb1
   analog@analog:/media/analog $ sudo umount /dev/sdb2
   analog@analog:/media/analog $ lsblk
   
   NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
   sdb           8:16   1 29.7G  0 disk
   ├─sdb1        8:17   1    1G  0 part
   ├─sdb2        8:18   1  9.8G  0 part
   └─sdb3        8:19   1    4M  0 part
   
   </code>
   
   === The root of 'BOOT' should contain: ===
     *''socfpga.dtb file''
     *''zImage file''
     *''extlinux.conf''
     *''u-boot.scr file''
     *''soc_system.rbf file''
   === The root of preloader partition should contain: ===
     *''u-boot-with-spl.sfp file''
   
   
   
   ==== Setting up the hardware (DE10-Nan) ====
   
   You will need to:
   
     * Get the [[https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046 | DE10-Nano FPGA Board]].\\ {{ resources:fpga:xilinx:fmc:AD777x-ARDZ:zedboard.png?600 }}
     * Insert the Micro-SD into the Micro-SD Interface Connector (J11). \\
     * Connect the AD777x-ARDZ to the DE10Nano FPGA using the Arduino shield connection. \\
     * Connect USB UART J4 (Micro USB) to your host PC. \\
     * Plug your ethernet cable into the RJ45 ethernet connector(J10). \\
     * Plug the Power Supply into 5V Power input connector (J14) (DO NOT turn the device on). \\
     * Set the jumpers as seen in the below picture: {{ :resources:eval:user-guides:circuits-from-the-lab:cn0540:de10-nano_fpga_switch_matrix.png?800 |}} \\
     * Turn it on. \\
     * Wait ~30 seconds for the “DONE” LED to turn blue. \\
     
   {{page>wiki/common#esd_warning&nofooter&noheader}}
   
   
   ==== Booting the SD Card ====
   === Remote IIO Oscilloscope ===
   
     * Observe kernel and serial console messages on your UART terminal (use the first ttyUSB or COM port resisted): \\
   <hidden Complete kernel boot log (Click to expand)>
   <WRAP box bggreen>
   <code>
   U-Boot SPL 2021.07-16360-gee63370-dirty (May 12 2022 - 14:01:41 +0100)
   Trying to boot from MMC1
   
   
   U-Boot 2021.07-16360-gee63370-dirty (May 12 2022 - 14:01:41 +0100)
   
   CPU:   Altera SoCFPGA Platform
   FPGA:  Altera Cyclone V, SE/A6 or SX/C6 or ST/D6, version 0x0
   BOOT:  SD/MMC Internal Transceiver (3.0V)
          Watchdog enabled
   DRAM:  1 GiB
   MMC:   dwmmc0@ff704000: 0
   Loading Environment from MMC... *** Warning - bad CRC, using default environment
   
   In:    serial
   Out:   serial
   Err:   serial
   Model: Altera SOCFPGA Cyclone V SoC Development Kit
   Net:
   Warning: ethernet@ff702000 (eth0) using random MAC address - 2a:a4:7b:1c:05:3b
   eth0: ethernet@ff702000
   Hit any key to stop autoboot:  0
   150 bytes read in 5 ms (29.3 KiB/s)
   ## Executing script at 02100000
   2510000 bytes read in 131 ms (18.3 MiB/s)
   switch to partitions #0, OK
   mmc0 is current device
   Scanning mmc 0:1...
   Found /extlinux/extlinux.conf
   Retrieving file: /extlinux/extlinux.conf
   142 bytes read in 6 ms (22.5 KiB/s)
   1:      Linux Default
   Retrieving file: /extlinux/../zImage
   8215800 bytes read in 413 ms (19 MiB/s)
   append: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
   Retrieving file: /extlinux/../socfpga.dtb
   23143 bytes read in 9 ms (2.5 MiB/s)
   Kernel image @ 0x1000000 [ 0x000000 - 0x7d5cf8 ]
   ## Flattened Device Tree blob at 02000000
      Booting using the fdt blob at 0x2000000
      Loading Device Tree to 09ff7000, end 09fffa66 ... OK
   
   Starting kernel ...
   
   Deasserting all peripheral resets
   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Linux version 5.10.0-98063-g1d94258e8ab2-dirty (ppop@romlx4.adlk.analog.com) (arm-none-linux-gnueabihf-gcc (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16)) 10.2.1 20201103, GNU ld (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16)) 2.35.1.20201028) #50 SMP Thu May 12 16:49:39 IST 2022
   [    0.000000] CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=10c5387d
   [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   [    0.000000] OF: fdt: Machine model: Terasic DE10-Nano
   [    0.000000] printk: bootconsole [earlycon0] enabled
   [    0.000000] Memory policy: Data cache writealloc
   [    0.000000] cma: Reserved 128 MiB at 0x38000000
   [    0.000000] Zone ranges:
   [    0.000000]   Normal   [mem 0x0000000000000000-0x000000002fffffff]
   [    0.000000]   HighMem  [mem 0x0000000030000000-0x000000003fffffff]
   [    0.000000] Movable zone start for each node
   [    0.000000] Early memory node ranges
   [    0.000000]   node   0: [mem 0x0000000000000000-0x000000003fffffff]
   [    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000003fffffff]
   [    0.000000] percpu: Embedded 19 pages/cpu s45324 r8192 d24308 u77824
   [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 260608
   [    0.000000] Kernel command line: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
   [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
   [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
   [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
   [    0.000000] Memory: 884244K/1048576K available (13312K kernel code, 1266K rwdata, 7472K rodata, 1024K init, 205K bss, 33260K reserved, 131072K cma-reserved, 131072K highmem)
   [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
   [    0.000000] ftrace: allocating 41696 entries in 82 pages
   [    0.000000] ftrace: allocated 82 pages with 3 groups
   [    0.000000] rcu: Hierarchical RCU implementation.
   [    0.000000] rcu:     RCU event tracing is enabled.
   [    0.000000]  Rude variant of Tasks RCU enabled.
   [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
   [    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
   [    0.000000] L2C-310 erratum 769419 enabled
   [    0.000000] L2C-310 enabling early BRESP for Cortex-A9
   [    0.000000] L2C-310 full line of zeros enabled for Cortex-A9
   [    0.000000] L2C-310 ID prefetch enabled, offset 8 lines
   [    0.000000] L2C-310 dynamic clock gating enabled, standby mode enabled
   [    0.000000] L2C-310 cache controller enabled, 8 ways, 512 kB
   [    0.000000] L2C-310: CACHE_ID 0x410030c9, AUX_CTRL 0x76460001
   [    0.000000] random: get_random_bytes called from start_kernel+0x39c/0x558 with crng_init=0
   [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
   [    0.000006] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
   [    0.007890] Switching to timer-based delay loop, resolution 10ns
   [    0.014236] Console: colour dummy device 80x30
   [    0.018690] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
   [    0.029182] pid_max: default: 32768 minimum: 301
   [    0.033913] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
   [    0.041197] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
   [    0.049587] CPU: Testing write buffer coherency: ok
   [    0.054499] CPU0: Spectre v2: using BPIALL workaround
   [    0.059707] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
   [    0.065977] Setting up static identity map for 0x100000 - 0x100060
   [    0.072263] rcu: Hierarchical SRCU implementation.
   [    0.077380] smp: Bringing up secondary CPUs ...
   [    0.082596] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
   [    0.082606] CPU1: Spectre v2: using BPIALL workaround
   [    0.093404] smp: Brought up 1 node, 2 CPUs
   [    0.097488] SMP: Total of 2 processors activated (400.00 BogoMIPS).
   [    0.103747] CPU: All CPU(s) started in SVC mode.
   [    0.108873] devtmpfs: initialized
   [    0.117243] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
   [    0.125248] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
   [    0.135066] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
   [    0.147499] NET: Registered protocol family 16
   [    0.153919] DMA: preallocated 256 KiB pool for atomic coherent allocations
   [    0.161901] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
   [    0.169894] hw-breakpoint: maximum watchpoint size is 4 bytes.
   [    0.184843] OF: /soc/gpio@ff708000/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/sdmmc_clk
   [    0.195866] OF: /soc/gpio@ff709000/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/sdmmc_clk
   [    0.206866] OF: /soc/gpio@ff70a000/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/main_pll@40/main_nand_sdmmc_clk@58
   [    0.222492] OF: /soc/gpio@ff708000/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/sdmmc_clk
   [    0.233490] OF: /soc/gpio@ff709000/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/sdmmc_clk
   [    0.244488] OF: /soc/gpio@ff70a000/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/main_pll@40/main_nand_sdmmc_clk@58
   [    0.271243] vgaarb: loaded
   [    0.274271] SCSI subsystem initialized
   [    0.278223] usbcore: registered new interface driver usbfs
   [    0.283747] usbcore: registered new interface driver hub
   [    0.289094] usbcore: registered new device driver usb
   [    0.294314] usb_phy_generic soc:usbphy: supply vcc not found, using dummy regulator
   [    0.303327] mc: Linux media interface: v0.10
   [    0.307615] videodev: Linux video capture interface: v2.00
   [    0.313205] pps_core: LinuxPPS API ver. 1 registered
   [    0.318150] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
   [    0.327268] PTP clock support registered
   [    0.331445] jesd204: found 0 devices and 0 topologies
   [    0.336538] FPGA manager framework
   [    0.340006] Advanced Linux Sound Architecture Driver Initialized.
   [    0.347167] clocksource: Switched to clocksource timer1
   [    1.024384] NET: Registered protocol family 2
   [    1.029371] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
   [    1.037742] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
   [    1.045521] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
   [    1.052765] TCP: Hash tables configured (established 8192 bind 8192)
   [    1.059225] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
   [    1.065845] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
   [    1.073085] NET: Registered protocol family 1
   [    1.077938] RPC: Registered named UNIX socket transport module.
   [    1.083836] RPC: Registered udp transport module.
   [    1.088556] RPC: Registered tcp transport module.
   [    1.093240] RPC: Registered tcp NFSv4.1 backchannel transport module.
   [    1.099677] PCI: CLS 0 bytes, default 64
   [    1.104173] hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
   [    1.113571] workingset: timestamp_bits=30 max_order=18 bucket_order=0
   [    1.126272] NFS: Registering the id_resolver key type
   [    1.131386] Key type id_resolver registered
   [    1.135554] Key type id_legacy registered
   [    1.139580] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
   [    1.146583] ntfs: driver 2.1.32 [Flags: R/W].
   [    1.151133] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
   [    1.157896] bounce: pool size: 64 pages
   [    1.161726] io scheduler mq-deadline registered
   [    1.166237] io scheduler kyber registered
   [    1.178747] dma-pl330 ffe01000.pdma: Loaded driver for PL330 DMAC-341330
   [    1.185429] dma-pl330 ffe01000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
   [    1.197241] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
   [    1.204646] printk: console [ttyS0] disabled
   [    1.208998] ffc02000.serial0: ttyS0 at MMIO 0xffc02000 (irq = 45, base_baud = 6250000) is a 16550A
   [    1.217987] printk: console [ttyS0] enabled
   [    1.217987] printk: console [ttyS0] enabled
   [    1.226313] printk: bootconsole [earlycon0] disabled
   [    1.226313] printk: bootconsole [earlycon0] disabled
   [    1.237054] ffc03000.serial1: ttyS1 at MMIO 0xffc03000 (irq = 46, base_baud = 6250000) is a 16550A
   [    1.246904] adv7511 0-0039: supply avdd not found, using dummy regulator
   [    1.253788] adv7511 0-0039: supply dvdd not found, using dummy regulator
   [    1.260551] adv7511 0-0039: supply pvdd not found, using dummy regulator
   [    1.267297] adv7511 0-0039: supply bgvdd not found, using dummy regulator
   [    1.274105] adv7511 0-0039: supply dvdd-3v not found, using dummy regulator
   [    1.289106] brd: module loaded
   [    1.293506] spi_altera ff30a000.spi: regoff 0, irq 49
   [    1.299395] spi_altera ff308000.spi: regoff 0, irq 52
   [    1.305556] libphy: Fixed MDIO Bus: probed
   [    1.310320] CAN device driver interface
   [    1.314434] socfpga-dwmac ff702000.ethernet: IRQ eth_wake_irq not found
   [    1.321066] socfpga-dwmac ff702000.ethernet: IRQ eth_lpi not found
   [    1.327360] socfpga-dwmac ff702000.ethernet: PTP uses main clock
   [    1.333359] socfpga-dwmac ff702000.ethernet: No sysmgr-syscon node found
   [    1.340050] socfpga-dwmac ff702000.ethernet: Unable to parse OF data
   [    1.346437] socfpga-dwmac: probe of ff702000.ethernet failed with error -524
   [    1.353694] stmmaceth ff702000.ethernet: IRQ eth_wake_irq not found
   [    1.359967] stmmaceth ff702000.ethernet: IRQ eth_lpi not found
   [    1.365875] stmmaceth ff702000.ethernet: PTP uses main clock
   [    1.371705] stmmaceth ff702000.ethernet: Version ID not available
   [    1.377800] stmmaceth ff702000.ethernet:     DWMAC1000
   [    1.382662] stmmaceth ff702000.ethernet: DMA HW capability register supported
   [    1.389779] stmmaceth ff702000.ethernet: RX Checksum Offload Engine supported
   [    1.396887] stmmaceth ff702000.ethernet: COE Type 2
   [    1.401755] stmmaceth ff702000.ethernet: TX Checksum insertion supported
   [    1.408448] stmmaceth ff702000.ethernet: Enhanced/Alternate descriptors
   [    1.415036] stmmaceth ff702000.ethernet: Extended descriptors not supported
   [    1.421980] stmmaceth ff702000.ethernet: Ring mode enabled
   [    1.427461] stmmaceth ff702000.ethernet: device MAC address 5e:1a:56:ca:f1:ed
   [    1.443091] libphy: stmmac: probed
   [    1.446500] Micrel KSZ9031 Gigabit PHY stmmac-0:01: attached PHY driver [Micrel KSZ9031 Gigabit PHY] (mii_bus:phy_addr=stmmac-0:01, irq=POLL)
   [    1.460440] usbcore: registered new interface driver asix
   [    1.465863] usbcore: registered new interface driver ax88179_178a
   [    1.472010] usbcore: registered new interface driver cdc_ether
   [    1.477871] usbcore: registered new interface driver net1080
   [    1.483538] usbcore: registered new interface driver cdc_subset
   [    1.489476] usbcore: registered new interface driver zaurus
   [    1.495072] usbcore: registered new interface driver cdc_ncm
   [    1.501392] dwc2 ffb40000.usb: supply vusb_d not found, using dummy regulator
   [    1.508665] dwc2 ffb40000.usb: supply vusb_a not found, using dummy regulator
   [    1.516041] dwc2 ffb40000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
   [    1.523726] dwc2 ffb40000.usb: DWC OTG Controller
   [    1.528474] dwc2 ffb40000.usb: new USB bus registered, assigned bus number 1
   [    1.535524] dwc2 ffb40000.usb: irq 47, io mem 0xffb40000
   [    1.541024] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
   [    1.549277] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
   [    1.556471] usb usb1: Product: DWC OTG Controller
   [    1.561171] usb usb1: Manufacturer: Linux 5.10.0-98063-g1d94258e8ab2-dirty dwc2_hsotg
   [    1.568980] usb usb1: SerialNumber: ffb40000.usb
   [    1.574132] hub 1-0:1.0: USB hub found
   [    1.577938] hub 1-0:1.0: 1 port detected
   [    1.582772] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
   [    1.589307] ehci-pci: EHCI PCI platform driver
   [    1.594354] usbcore: registered new interface driver uas
   [    1.599776] usbcore: registered new interface driver usb-storage
   [    1.605842] usbcore: registered new interface driver usbserial_generic
   [    1.612393] usbserial: USB Serial support registered for generic
   [    1.618435] usbcore: registered new interface driver ftdi_sio
   [    1.624178] usbserial: USB Serial support registered for FTDI USB Serial Device
   [    1.631559] usbcore: registered new interface driver upd78f0730
   [    1.637493] usbserial: USB Serial support registered for upd78f0730
   [    1.645288] i2c /dev entries driver
   [    1.649615] usbcore: registered new interface driver uvcvideo
   [    1.655342] USB Video Class driver (1.1.1)
   [    1.661594] Synopsys Designware Multimedia Card Interface Driver
   [    1.668126] dw_mmc ff704000.dwmmc0: IDMAC supports 32-bit address mode.
   [    1.674777] ledtrig-cpu: registered to indicate activity on CPUs
   [    1.674831] dw_mmc ff704000.dwmmc0: Using internal DMA controller.
   [    1.680939] usbcore: registered new interface driver usbhid
   [    1.686946] dw_mmc ff704000.dwmmc0: Version ID is 240a
   [    1.692513] usbhid: USB HID core driver
   [    1.697682] dw_mmc ff704000.dwmmc0: DW MMC controller at irq 42,32 bit host data width,1024 deep fifo
   [    1.710830] mmc_host mmc0: card is polling.
   [    1.727178] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
   [    1.813536] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
   [    1.823310] mmc0: new high speed SDHC card at address aaaa
   [    1.829371] mmcblk0: mmc0:aaaa SC32G 29.7 GiB
   [    1.838632]  mmcblk0: p1 p2 p3
   [    1.928415] cf_axi_adc ff220000.cf_axi_adc: ADI AIM (10.01.b) at 0xFF220000 mapped to 0x(ptrval), probed ADC ad7768_axi_adc as MASTER
   [    1.946547] fpga_manager fpga0: Altera SOCFPGA FPGA Manager registered
   [    1.953958] usbcore: registered new interface driver snd-usb-audio
   [    1.962632] NET: Registered protocol family 10
   [    1.967994] Segment Routing with IPv6
   [    1.971718] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
   [    1.978223] NET: Registered protocol family 17
   [    1.982673] NET: Registered protocol family 15
   [    1.987325] can: controller area network core
   [    1.991725] NET: Registered protocol family 29
   [    1.996156] can: raw protocol
   [    1.999153] can: broadcast manager protocol
   [    2.003329] can: netlink gateway - max_hops=1
   [    2.007854] 8021q: 802.1Q VLAN Support v1.8
   [    2.012067] NET: Registered protocol family 36
   [    2.016523] Key type dns_resolver registered
   [    2.021107] oprofile: using arm/armv7-ca9
   [    2.025194] ThumbEE CPU extension supported.
   [    2.029483] Registering SWP/SWPB emulation handler
   [    2.039134] [drm] Initialized axi_hdmi_drm 1.0.0 20120930 for ff290000.axi_hdmi on minor 0
   [    2.048254] axi-hdmi ff290000.axi_hdmi: [drm] Cannot find any crtc or sizes
   [    2.055621] of_cfs_init
   [    2.058137] of_cfs_init: OK
   [    2.061148] ALSA device list:
   [    2.064109]   No soundcards found.
   [    2.067766] dw-apb-uart ffc02000.serial0: forbid DMA for kernel console
   [    2.089073] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
   [    2.097225] VFS: Mounted root (ext4 filesystem) on device 179:2.
   [    2.114079] devtmpfs: mounted
   [    2.120567] Freeing unused kernel memory: 1024K
   [    2.127769] Run /sbin/init as init process
   [    2.212817] random: fast init done
   [    2.752994] systemd[1]: System time before build time, advancing clock.
   [    2.804067] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
   [    2.825843] systemd[1]: Detected architecture arm.
   
   Welcome to Kuiper GNU/Linux 10 (buster)!
   
   [    2.930157] systemd[1]: Set hostname to <analog>.
   [    3.374719] systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
   [    3.391765] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
   [    3.602086] systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of section. Ignoring.
   [    3.611803] systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of section. Ignoring.
   [    3.866367] random: systemd: uninitialized urandom read (16 bytes read)
   [    3.887495] random: systemd: uninitialized urandom read (16 bytes read)
   [    3.894871] systemd[1]: Listening on udev Kernel Socket.
   [  OK  ] Listening on udev Kernel Socket.
   [    3.927361] random: systemd: uninitialized urandom read (16 bytes read)
   [    3.943603] systemd[1]: Listening on Syslog Socket.
   [  OK  ] Listening on Syslog Socket.
   [    3.977957] systemd[1]: Listening on Journal Socket (/dev/log).
   [  OK  ] Listening on Journal Socket (/dev/log).
   [  OK  ] Created slice system-getty.slice.
   [  OK  ] Created slice User and Session Slice.
   [  OK  ] Reached target Slices.
   [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
   [  OK  ] Reached target Swap.
   [  OK  ] Listening on fsck to fsckd communication Socket.
   [  OK  ] Listening on Journal Socket.
            Starting Restore / save the current clock...
   [  OK  ] Created slice system-systemd\x2dfsck.slice.
   [  OK  ] Listening on initctl Compatibility Named Pipe.
            Mounting Kernel Debug File System...
   [  OK  ] Created slice system-serial\x2dgetty.slice.
            Starting Journal Service...
            Starting Set the console keyboard layout...
            Starting Load Kernel Modules...
   [  OK  ] Listening on udev Control Socket.
            Starting udev Coldplug all Devices...
            Mounting RPC Pipe File System...
   [  OK  ] Started Restore / save the current clock.
   [  OK  ] Mounted Kernel Debug File System.
   [  OK  ] Started Journal Service.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Mounted RPC Pipe File System.
            Starting Apply Kernel Variables...
            Mounting Kernel Configuration File System...
            Starting Remount Root and Kernel File Systems...
   [  OK  ] Mounted Kernel Configuration File System.
   [  OK  ] Started Apply Kernel Variables.
   [  OK  ] Started Set the console keyboard layout.
   [  OK  ] Started Remount Root and Kernel File Systems.
   [  OK  ] Started udev Coldplug all Devices.
            Starting Helper to synchronize boot up for ifupdown...
            Starting Flush Journal to Persistent Storage...
            Starting Load/Save Random Seed...
            Starting Create System Users...
   [  OK  ] Started Helper to synchronize boot up for ifupdown.
   [  OK  ] Started Load/Save Random Seed.
   [  OK  ] Started Create System Users.
            Starting Create Static Device Nodes in /dev...
   [  OK  ] Started Flush Journal to Persistent Storage.
   [  OK  ] Started Create Static Device Nodes in /dev.
   [  OK  ] Reached target Local File Systems (Pre).
            Starting udev Kernel Device Manager...
   [  OK  ] Started udev Kernel Device Manager.
            Starting Show Plymouth Boot Screen...
   [  OK  ] Started Show Plymouth Boot Screen.
   [  OK  ] Reached target Local Encrypted Volumes.
   [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
   [  OK  ] Found device /dev/ttyS0.
   [  OK  ] Found device /dev/disk/by-partuuid/18f1f9d5-01.
            Starting File System Check…isk/by-partuuid/18f1f9d5-01...
   [  OK  ] Started File System Check Daemon to report status.
   [  OK  ] Started File System Check …/disk/by-partuuid/18f1f9d5-01.
            Mounting /boot...
   [  OK  ] Mounted /boot.
   [  OK  ] Reached target Local File Systems.
            Starting Create Volatile Files and Directories...
            Starting Raise network interfaces...
            Starting Tell Plymouth To Write Out Runtime Data...
            Starting Set console font and keymap...
            Starting Preprocess NFS configuration...
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [  OK  ] Started Preprocess NFS configuration.
   [  OK  ] Reached target NFS client services.
   [  OK  ] Reached target Remote File Systems (Pre).
   [  OK  ] Reached target Remote File Systems.
   [  OK  ] Started Set console font and keymap.
   [  OK  ] Started Create Volatile Files and Directories.
            Starting Network Time Synchronization...
            Starting Update UTMP about System Boot/Shutdown...
   [  OK  ] Started Update UTMP about System Boot/Shutdown.
   [  OK  ] Started Network Time Synchronization.
            Starting Load Kernel Modules...
   [  OK  ] Reached target System Time Synchronized.
            Starting Tell Plymouth To Write Out Runtime Data...
   [  OK  ] Started Raise network interfaces.
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Reached target System Initialization.
   [  OK  ] Started CUPS Scheduler.
   [  OK  ] Reached target Paths.
   [  OK  ] Started Daily Cleanup of Temporary Directories.
   [  OK  ] Listening on D-Bus System Message Bus Socket.
   [  OK  ] Listening on CUPS Scheduler.
   [  OK  ] Started Daily apt download activities.
   [  OK  ] Started Daily apt upgrade and clean activities.
   [  OK  ] Started Daily rotation of log files.
   [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
   [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
   [  OK  ] Listening on triggerhappy.socket.
   [  OK  ] Reached target Sockets.
   [  OK  ] Reached target Basic System.
   [  OK  ] Started D-Bus System Message Bus.
            Starting WPA supplicant...
   [  OK  ] Started tof-server.service.
            Starting rng-tools.service...
            Starting Login Service...
   [  OK  ] Started CUPS Scheduler.
            Starting System Logging Service...
            Starting Disk Manager...
            Starting Modem Manager...
            Starting Check for Raspberry Pi EEPROM updates...
            Starting dhcpcd on all interfaces...
            Starting LSB: Switch to on…nless shift key is pressed)...
   [  OK  ] Started Regular background program processing daemon.
            Starting dphys-swapfile - …unt, and delete a swap file...
            Starting Avahi mDNS/DNS-SD Stack...
            Starting triggerhappy global hotkey daemon...
   [  OK  ] Started Daily man-db regeneration.
   [  OK  ] Reached target Timers.
   [  OK  ] Started System Logging Service.
   [FAILED] Failed to start rng-tools.service.
   See 'systemctl status rng-tools.service' for details.
   [  OK  ] Started triggerhappy global hotkey daemon.
   [  OK  ] Started WPA supplicant.
   [  OK  ] Started Check for Raspberry Pi EEPROM updates.
   [  OK  ] Started Avahi mDNS/DNS-SD Stack.
   [  OK  ] Started Make remote CUPS printers available locally.
   [  OK  ] Started dhcpcd on all interfaces.
   [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
   [  OK  ] Started Login Service.
            Starting Authorization Manager...
   [  OK  ] Reached target Network.
            Starting /etc/rc.local Compatibility...
            Starting Permit User Sessions...
            Starting HTTP based time synchronization tool...
            Starting OpenBSD Secure Shell server...
   [  OK  ] Started IIO Daemon.
   [  OK  ] Started dphys-swapfile - s…mount, and delete a swap file.
   [  OK  ] Started /etc/rc.local Compatibility.
   [  OK  ] Started Permit User Sessions.
            Starting Light Display Manager...
            Starting Hold until boot process finishes up...
   [  OK  ] Started HTTP based time synchronization tool.
   [  OK  ] Started Authorization Manager.
   [  OK  ] Started Modem Manager.
   [  OK  ] Started Hold until boot process finishes up.
   
   Raspbian GNU/Linux 10 analog ttyS0
   
   analog login: root (automatic login)
   
   Last login: Thu Feb 25 03:29:37 GMT 2021 on ttyS0
   Linux analog 5.10.0-98063-g1d94258e8ab2-dirty #50 SMP Thu May 12 16:49:39 IST 2022 armv7l
   
   The programs included with the Debian GNU/Linux system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.
   
   Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
   permitted by applicable law.
   root@analog:~#
   </code></WRAP>
   </hidden>
   \\
   ^  user  ^  password  ^
   |  root  |  analog  |
   \\
     * Run the ifconfig command on your UART terminal and get your board IP. \\ 
   <code>
   root@analog:~# ifconfig
   eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet your_board_ip  netmask 255.255.255.0  
           inet6 fe80::8e1e:23ed:a7c3:9897  prefixlen 64  scopeid 0x20<link>
           ether aa:bb:cc:dd:ee:ff  txqueuelen 1000  (Ethernet)
           RX packets 1757  bytes 1013110 (989.3 KiB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 575  bytes 52441 (51.2 KiB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
           device interrupt 36  base 0xb000
   root@analog:~#
   </code>
   \\
      * Open IIO Scope application and type ip:board_ip in the URI tab. \\ {{ resources:fpga:xilinx:fmc:ad777x-ardz:iioosc_remote_ad777x_ardz_zed_login.jpg?400 }} \\
   
   You should see two screens: \\
   
   {{ resources:fpga:xilinx:fmc:ad777x-ardz:iioosc_capture_ad777x_zed.jpg?850 }}
   //
   //
   <WRAP important round>Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ''sudo shutdown -h now''
   {{:resources:fpga:xilinx:fmc:ad-fmcomms1-ebz:shutdown.png?300|}}
   </WRAP>
   
   </WRAP>
   ++++
   
   ====== Reference HDL Design ======
   ==== Functional Overview ====
   
   
   The reference design is a processor based (ARM) embedded system. A functional block diagram of the system is given below. 
   The device interface is a self-contained peripheral similar to other such pcores in the system. The core is programmable through an AXI-lite interface. \\
   
   ===Xilinx block diagram===
   {{resources:fpga:xilinx:fmc:ad777x-ardz:ad777x_ardz_xilinx.png?800|}} \\
   ===Intel block diagram===
   {{resources:fpga:xilinx:fmc:ad777x-ardz:ad777x_ardz_intel.png?800|}} \\
   <WRAP round download 100%>
   |< 100% 20% 18% 12% 25% 25%>|
   ^Hardware ^Project ^Carriers ^Resource Utilization ^Library Cores ^
   |[[adi>AD777x-ARDZ|AD777x-ARDZ]] |[[https://github.com/analogdevicesinc/hdl/tree/master/projects/ad777x_ardz|ad777x-ardz]] |[[https://github.com/analogdevicesinc/hdl/tree/master/projects/ad777x_ardz/zed|zed]] |NA |[[https://github.com/analogdevicesinc/hdl/tree/master/library/axi_ad777x|axi_ad777x_ardz]]  |
   | | |[[https://github.com/analogdevicesinc/hdl/tree/master/projects/ad777x_ardz/de10nano|de10nano]]  | |[[http://github.com/analogdevicesinc/hdl/tree/master/library/axi_dmac|axi_dmac]] |
   | | | | |[[http://github.com/analogdevicesinc/hdl/tree/master/library/axi_hdmi_tx|axi_hdmi_tx]] |  
   | | | | |[[https://github.com/analogdevicesinc/hdl/tree/hdl_2019_r2/library/util_pack/util_cpack2|util_cpack2]] |
   | | | | |[[http://github.com/analogdevicesinc/hdl/tree/hdl_2019_r2/library/axi_clkgen|axi_clkgen]] |
   | | | | |[[http://github.com/analogdevicesinc/hdl/tree/hdl_2019_r2/library/axi_i2s_adi|axi_i2s_adi]] |
   | | | | |[[http://github.com/analogdevicesinc/hdl/tree/hdl_2019_r2/library/axi_spdif_tx|axi_spdif_tx]] |
   | | | | |[[http://github.com/analogdevicesinc/hdl/tree/hdl_2019_r2/library/axi_sysid|axi_sysid]] |
   | | | | |[[http://github.com/analogdevicesinc/hdl/tree/hdl_2019_r2/library/sysid_rom|sysid_rom]] |
   | | | | |[[http://github.com/analogdevicesinc/hdl/tree/hdl_2019_r2/library/util_i2c_mixer|util_i2c_mixer]] |  
   
   </WRAP>
   
