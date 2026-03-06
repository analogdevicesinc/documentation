.. warning:: Conversion failed for ``resources/eval/ltc4296-1-sccp-evaluation-guide``

   Reason: pandoc error: Error at "/tmp/tmp95z47rx7.txt" (line 786, column 1):
expecting inline
not found
| b[15:8] | Reserved | Value Always 0 | Read Only |
^

.. code-block:: text

   ====== Serial Communication Classification Protocol (SCCP) with the LTC4296-1 ======
   
   
   ===== Introduction =====
   Serial Communication Classification Protocol (SCCP) allows for an IEEE 802.3cg, Single-pair Power over Ethernet (SPoE) compliant Power Sourcing Equipment (PSE) to classify a compliant Powered Device (PD) before power is applied to a cable. Through SCCP, information on device class, type, pd_faulted, and Cable resistance measurements enabled/disabled can be obtained.
   
   This Wiki provides an application circuitry overview, SCCP transactions overview, sample C code SCCP implementation, evaluation guidance and reference material for class and type. The sample C code may be used as a starting point for integrating SPoE power management into a system host microcontroller. 
   ==== Useful References ==== 
     - [[adi>media/en/technical-documentation/data-sheets/ltc4296-1.pdf | LTC4296-1 Datasheet]]
     - [[adi>media/en/technical-documentation/data-sheets/ltc9111.pdf | LTC9111 Datasheet]]
     - IEEE 802.3cg Standard (Clause 104)
   
   ===== SCCP APPLICATION CIRCUITRY =====
   The SCCP was derived from the 1-Wire® protocol and utilizes a half-duplex, bi-directional open-drain bus where the PSE or PD can pull-down. Figure 1 illustrates an SPoE system featuring the LTC4296-1 PSE, the LTC9111 PD, an application host microcontroller, and ADIN1100 10BASE-T1L PHYs. Only one of five LTC4296-1 ports is shown, and the "x" suffix denotes pin names as a function of port number. 
   
   The LTC4296-1 SCCP related components include pulldown MOSFET M3, line sense NPN BJT transistor Q1, snubber disconnect MOSFET M2, the LTC4296-1 SWx pin, and the host microcontroller GPOx and GPIx pins. The microcontroller's GPOx pin drives M3 to pulldown the line voltage while Q1 limits the maximum voltage sensed at the GPIx pin. Snubber R3/C4 is provided for loop stability during inrush and current limit of high-side MOSFET M1 and is disconnected during PD detection and SCCP. Secondary snubber R5/C5 prevents excess ringing at the OUTPx pin when snubber R3/C4 is disconnected. 
   
   Microcontroller requirements for implementing SCCP are:
     * Per port GPO pin (SCCPOx)
     * Per Port GPI pin with ADC functionality (SCCPIx)
     * A timer with resolution of at least 1us
   
   At the PSE, the LTC4296-1 is set up for the classification state by the microcontroller. Classification is configured by setting the software PSE ready bit (PxCFG0, Bit6, SW_PSE_READY) and the classification mode bit (PXCFG0, Bit 13, SET_CLASSIFICATION_MODE) before entering the detection state. If the microcontroller determines a valid PD with a compatible class is present, the port can proceed to the power-up state by setting the port software power available bit (Register PxCFG0, Bit 5, SW_POWER_AVAILABLE) and the end classification bit (Register PxCFG0, Bit 14, END_CLASSIFICATION). Further description of port states can be found in the [[adi>media/en/technical-documentation/data-sheets/ltc4296-1.pdf | LTC4296-1 Datasheet]]. 
   
   On the PD side, the LTC9111 detects the SCCP logic states on the lines through SNS1 and SNS2 and uses external MOSFETs (M13/M14) to pull-down the port voltage during classification in order to transmit a logic low. The use of two external MOSFETs allows successful classification regardless of input connector polarity configuration. 
   
   {{ :resources:eval:spoe_system.png?nolink |}}
   
   <WRAP centeralign>//<fc #4682b4>Figure 1. SPoE System </fc>//</WRAP>
   
   
   ===== SCCP Transactions Overview =====
   SCCP transactions are comprised of initialization, write slot, and read slot protocols. The PSE initiates all protocols by pulling down the bus. The PSE also provides a voltage limited pull-up current to restore the bus voltage to a logic high. The PD uses the rectified voltage from the PSE pull-up to retain state during pull-down events. Table 1 summarizes the basic SCCP protocols, and Figure 2-4 illustrates the corresponding waveforms. 
   
   
   
   
   ^ Operation ^ Description ^ Implementation ^
   | Initialization | Reset and detect the PD | PSE pulls bus low, delays t<sub>RSTL</sub>, releases bus, waits t<sub>MSP</sub> to sample PD pulse (Figure 2)|
   | Write Slot (1) |Send a '1' bit to the PD | PSE pulls bus low, delays t<sub>W1L</sub>, releases bus (Figure 3)|
   | Write Slot (0) | Send a '0' bit to the PD | PSE pulls bus low, delays t<sub>W0L</sub>, releases bus (Figure 3) |
   | Read Slot | Read a '0' or '1' bit from the PD | PSE pulls bus low, delays t<sub>W1L</sub>, releases bus, samples bus at t<sub>MSR</sub> (Figure 4)|
   <WRAP centeralign>//<fc #4682b4>Table 1. SCCP Protocols</fc>//</WRAP>
   
   ====Initialization ==== 
   The PSE initiates the SCCP transaction by pulling down on the bus during the reset pulse. After which the PD responds with a pull-down presence pulse. During the reset pulse, the PSE pulls down on the bus voltage below the input logic low voltage, V<sub>TL</sub> (2V PSE, 1V PD), for reset time low time, t<sub>RSTL</sub> (8ms-10.5ms).
    
   Once the PSE releases the bus, the PD detects the rising edge cross the input logic high voltage V<sub>TH</sub> (3V) and waits the presence-detect high time, t<sub>PDH</sub> (0.7ms-1.3ms), before transmitting a presence pulse. The PSE samples for the PD presence pulse by t<sub>MSP</sub> (1.8ms-2.2ms). The PD holds the presence pulse for the presence-detect low time, t<sub>PDL</sub> (2.8ms-5.2ms).    
   
   {{ :resources:eval:spoe_sccp_ideal_initialization5.png?nolink |}}
   <WRAP centeralign>//<fc #4682b4>Figure 2. SCCP Initialization </fc>//</WRAP>
   
   ====Write Time Slot ====
   The duration of the write time slot for either a '0' or '1' should last for a maximum of t<sub>WRITESLOT</sub> (2.78ms). When the PSE writes a '0' to the PD, first the PSE pulls down the bus voltage below the V<sub>TL</sub>, then the PSE releases within the write 0 low time, t<sub>W0L</sub> (1.8ms-2.2ms), as seen in Figure 3. In the case where the PSE aims to write a '1', the PSE pulls down on the bus voltage, and then it releases the line within the write 1 low time, t<sub>W1L</sub> (0.09ms-0.61ms), as illustrated in Figure 3. See Figures 26-29 for example waveforms.
   
   
   
   {{ :resources:eval:spoe_sccp_ideal_write_slot4.png?nolink |}}
   <WRAP centeralign>//<fc #4682b4>Figure 3. SCCP Write Time Slot </fc>//</WRAP>
   
   ====Read Time Slot ====
   The PSE initiates the read time slot by pulling low on the bus. Subsequently, the PSE releases the bus within t<sub>W1L</sub>, at which point the PD responds by pulling the bus low for the read 0 low time, t<sub>R0L</sub> (1.75ms-3.25ms), in order to transmit a '0' (Figure 4). Alternatively, if the intention is to transmit a '1', the PD refrains from pulling the bus low after the read 1 low time, t<sub>W1L</sub>. This read time slot is repeated for each PD bit, see Figure 30-34 for example waveforms. The PD sends data LSB first. Each of these read time slots has a maximum duration of t<sub>READSLOT</sub> (3.83ms).
   
   
   {{ :resources:eval:spoe_sccp_read_time_slot4.png?nolink |}}
   <WRAP centeralign>//<fc #4682b4>Figure 4. SCCP Read Time Slot </fc>//</WRAP>
   
   ==== Additional Requirements ====
   Following an Initialization Sequence or a Write/Read Time Slot, there is a recovery time of t<sub>REC</sub> (0.27ms-0.33ms). This recovery time begins from the moment the PSE OUTPx voltage exceeds the V<sub>TH</sub> threshold and extends until the bus voltage begins to get pulled down. Additionally, the bus voltage during any transaction must have a rise time from GND to V<sub>TH</sub> within t<sub>R</sub> (0.025ms-0.5ms). It must have a fall time from V<sub>PUP</sub> (4.7V-5.5V) to V<sub>TL</sub> within t<sub>F</sub> (0.025ms-0.25ms). The PD Reservoir Capacitor Recharge Time, denoted as t<sub>CHRG</sub>, extending from when the voltage on the bus crosses the V<sub>CHRG</sub> threshold (4.23V) to the commencement of the bus voltage being pulled down, must exceed 0.2ms. 
   
   ==== SCCP Transaction Waveform ====
   
   
   
   Figure 5 illustrates a basic example SCCP transaction. The two waveforms are:
     * Ch1: Differential voltage at PSE MDI/PI connector
     * Ch2: Voltage at LTC9111's SCCP pin relative to GND_PD
   
   Note SCCP data is read/written LSB first, low byte first.
   
   The basic SCCP transaction is comprised of:\\
   i. Initialization\\
   ii. Write Broadcast Address (0xCC)\\
     * Following the Initialization Sequence, the PSE proceeds with a Broadcast Address write operation. During this operation, the PSE transmits 0xCC to the PD. This is used to address a PD on the bus without sending out a unique address code information. 
   
   iii. Write Read_Scratchpad Command (0xAA)\\
     * Subsequent to the Broadcast Address write operation, the PSE sends a Read-Scratchpad Command (0xAA). This command configures the PD for subsequent two-byte CLASS_TYPE_INFO read plus CRC byte read operation.
   
   iv. Read PD CLASS_TYPE_INFO Low Byte\\
     * Following the Read_Scratchpad Command, the PD sends the Low Byte of its CLASS_TYPE_INFO to the PSE.
   
   v. Read PD CLASS_TYPE_INFO High Byte\\
     * After the Low Byte of the CLASS_TYPE_INFO is transmitted the PD sends the High Byte of the ClASS_TYPE_INFO to the PSE.  Interpretation of CLASS_TYPE_INFO is located in Table 7 & 9 located in the Appendix section of this Wiki. 
   
   vi. Read PD CRC Byte\\
     * In the final step, the PSE reads the cyclic redundancy check (CRC) value of the PD. This value is derived from the received scratchpad class info word. 
   
   
   {{ :resources:eval:spoe_basic_sccp_transaction.png?nolink |}}
   <WRAP centeralign>//<fc #4682b4>Figure 5. SCCP Transaction </fc>//</WRAP>
   
   ==== CLASS_TYPE_INFO Registers ====
   Table 2 shows the bit information from the CLASS_TYPE_INFO register bytes. Refer to the Appendix for Class and Type listing tables. 
   {{ :resources:eval:spoe_sccp_class_type_info_table.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Table 2. CLASS_TYPE_INFO Register Bytes Table </fc>//</WRAP>
   
   ===== Example C Code Implementation of SCCP =====
   
   ==== Initialization ====
   
   Example C code for send_reset_pulse() is shown in Figure 6. The send_reset_pulse() function returns an unsigned 8-bit integer which corresponds to the logic level of the voltage sampled by the PSE after delay t<sub>MSP</sub>.
   \\
   \\
   
     /******************************************************************************************************************
     Copyright © 2023 by Analog Devices, Inc. All rights reserved. This software is proprietary to Analog Devices, Inc.
     and its licensors. This software is provided on an "as is" basis without any representations, warranties,
     guarantees or liability of any kind. Use of the software is subject to the terms and conditions of the Clear BSD
     License (https://spdx.org/licenses/BSD-3-Clause-Clear.html).
     
     *Function: uint8_t send_reset_pulse() 
     *This function sends a reset pulse and searches for PD presence pulse. Reset pulse
     *utilizes the sccp timer to incorporate the timings as defined in IEEE 802.3cg
     *standard
     *
     *uint8_t value of PD presence pulse voltage is returned
     *
     ******************************************************************************************************************/
     uint8_t send_reset_pulse()
     {
       /* assert pulse  */
       PULL_DOWN_LINE();
       TimerDelay_ms(3); /* wait 3ms to see if GPIx went low */
       /* check GPIx voltage is low to protect pull-down fet from stuck high faults */
       if(READ_LINE())
       {
         RELEASE_LINE(); /* deassert GPOx if mosfet was unable to pull down */
         LED1_ON(); /* and turn on red LED to indicate fault */
       }
       else
       {
         LED1_OFF(): /* make sure the red LED is off */
       }
       TimerDelay_msf(T_RSTL_NOM-3); /* continue pulling-down if no fault */
       RELEASE_LINE(); /* stop puling-down */
       TimerDelay_msf(T_MSP); /* wait for pull-up to restore line voltage and then PD to pull-down with presence pulse */
       uint8_t level = READ_LINE(); /* look for PD presence pulse */
       TimerDelay_msf(3.22); /* wait for PD to stop pulling-down and pull-up to restore line voltage */
       return !level;
     }  
   
   <WRAP centeralign>//<fc #4682b4>Figure 6. Initialization Example C Code</fc>//</WRAP>
   
    
   
   
   
   ==== Write Bit ====
   
   
   
   Example C code for write_bit() is shown in Figure 7. Unlike the initialization sequence, no special precatuion is needed to protect the pulldown MOSFET against stuck-high faults since the write time for a 0 bit (t<sub>W0L</sub>) is less than 3ms. 
   \\
   \\
   
     /******************************************************************************************************************
     Copyright © 2023 by Analog Devices, Inc. All rights reserved. This software is proprietary to Analog Devices, Inc.
     and its licensors. This software is provided on an "as is" basis without any representations, warranties,
     guarantees or liability of any kind. Use of the software is subject to the terms and conditions of the Clear BSD
     License (https://spdx.org/licenses/BSD-3-Clause-Clear.html).
     
     * Function: void write_bit(uint8_t bit) 
     *
     * This function controls the pulldown FET to send a bit of a SCCP
     * transaction to the PD
     *
     ******************************************************************************************************************/
     void write_bit(uint8_t bit)
     {    
       TimerDelay_resetCount(); /* timer->CNT = 0 */   
       PULL_DOWN_LINE();
       
       if (bit)
       {
         TimerDelay_msf(T_W1L);
       }
       else
       {
         TimerDelay_msf(T_W0L);
       }
       RELEASE_LINE();
       while(TIMERDELAY_ellapsedUsec() < T_WRITESLOT*1000); /*elapsed time in us since timer count reset */
       
       return;
     }  
   
   <WRAP centeralign>//<fc #4682b4>Figure 7. Write Bit Example C Code</fc>//</WRAP>
   
   
   
   ==== Read Bit ====
   
   Example C code for the read_bit() function is shown in Figure 8. The read_bit() function returns the logical value of the bus voltage read from the PD at t<sub>MSR</sub>.
   \\
   \\
   
   
     /******************************************************************************************************************
     Copyright © 2023 by Analog Devices, Inc. All rights reserved. This software is proprietary to Analog Devices, Inc.
     and its licensors. This software is provided on an "as is" basis without any representations, warranties,
     guarantees or liability of any kind. Use of the software is subject to the terms and conditions of the Clear BSD
     License (https://spdx.org/licenses/BSD-3-Clause-Clear.html).
     
     * Function: uint8_t read_bit() 
     * This function implements the GPO pulse sequence required to receive and read a bit
     * on GPI and return the result. 
     *
     ******************************************************************************************************************/
     uint8_t read_bit()
     {
       TimerDelay_resetCount(); /* timer->CNT = 0
       PULL_DOWN_LINE();
       
       TimerDelay_msf(T_W1L);
       RELEASE_LINE();
       
       /*wait to get withing read window */
       while(TimerDelay_ellapsedUsec() < T_MSR*1000); /*elapsed time in us since timer 
             /*count reset
       volatile uint8_t bit = READ_LINE();
       if(!bit) /* if bit was a 0, need to wait for release of line then allow for */
             /* enough recovery time (T_REC)
       {
         while(!READ_LINE() && ( TimerDelay_ellapsedUsec() <
         T_READSLOT_MAX_TYPE_E*1000) ); /* wait until PD releases or t-readslot_max
         uint32_t t_release; /* declare time it takes PD to release as t_release
         
         if(READ_LINE()) // pd released in time
         {
           t_release = TimerDelay_ellapsedUsec();
         }
         else // pd failed to release before t_readslot_max so just return bit
         {
           return bit;
         }
         // wait for t_rec
         uint32_t ellapsed_trec = 0; /* define vars for trec
         uint32_t ellapsed_slot = 0;
         do
         {
           ellapsed_slot = TimerDelay_ellapsedUsec();
           ellapsed_trec = ellapsed_slot - t_release;
           
         } while( (ellapsed_trec < T_REC*1000) &&
         (ellapsed_slot < T_READSLOT_MAX_TYPE_E*1000) );
         /* we've now either waited for t_rec, or reached t-readslot_max
       }
       while(TimerDelay_ellapsedUsec() < T_READSLOT_MAX_TYPE_E*1000);
       return bit;
     }
   
   <WRAP centeralign>//<fc #4682b4>Figure 8. Read Bit Example C Code</fc>//</WRAP>
   
   
   
   ==== Interpreting CLASS_TYPE_INFO ====
   The example code in Figure 9 defines Class and Type codes as well as the PSE/PD class compatibility matrix for interpreting the CLASS_TYPE_INFO word.
   \\
   \\
   
   
     /******************************************************************************************************************
     Copyright © 2023 by Analog Devices, Inc. All rights reserved. This software is proprietary to Analog Devices, Inc.
     and its licensors. This software is provided on an "as is" basis without any representations, warranties,
     guarantees or liability of any kind. Use of the software is subject to the terms and conditions of the Clear BSD
     License (https://spdx.org/licenses/BSD-3-Clause-Clear.html).
     
     * global variable: const uint8_t class_compatibility[16][16]
     * This is 2 dimensional array returns the compatibility of PSE with PD class
     * Following an SCCP transaction class_compatibility[x][y] variable contains
     * compatibility of PSE class x with PD class y
     * 
     *
     * uint16_t sccp_classes[16] should return the sccp class code associated with each
     * class. sccp_classes[x] contains the class code associated with class x. 
     *
     * Similarly sccp_types[x] should return the type code associated with type x. 
     *
     * CLASS_TYPE_INFO returned from PD should have bits[9:0] consisting of class code
     * and bits[15:12] consisting of type code.
     * 
     ******************************************************************************************************************/
     
     /* PSE to PD class compatibility matrix as defined by IEEE 802.3bu/cg */
     const uint8_t class_compatibility[16][16] = {
     /*                    PSE class
     /*PD    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
     /*0*/   1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
     /*1*/   0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
     /*2*/   0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  
     /*3*/   0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
     /*4*/   0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0
     /*5*/   0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0
     /*6*/   0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0
     /*7*/   0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0
     /*8*/   0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0
     /*9*/   0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
     /*10*/  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0
     /*11*/  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0
     /*12*/  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0
     /*13*/  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1
     /*14*/  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1
     /*15*/  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
     }; 
     /* bottom 12 bits of CLASS_TYPE_INFO codes for PD power classes o through 15 */
     uint16_t sccp_classes[16] = {
         0x3FE, //class 0
         0X3FD, //class 1
         0X3FB, //class 2
         0X3F7, //class 3
         0X3EF, //class 4
         0X3DF, //class 5
         0x3BF, // class 6
         0x37F, // class 7
         0x2FF, // class 8
         0x1FF, // class 9
         0x001, // class 10
         0x002, // class 11
         0x003, // class 12
         0x004, // class 13
         0x005, // class 14
         0x006, // class 15
     };
     /* top 4 bits of CLASS_TYPE_INFO register for PD types A through E */
                                  /* A, B, C, D, E */
     const uint8_t sccp_types[5] = { 0xE, 0xD, 0xB, 0x7, 0xC };
     
     /***********************************************************************************
     *
     * Function: int index_of(uint16_t val, uint16_t* buf, uint16_t buf_len)
     * 
     * data bits parsed from SCCP_CLASS_INFO are interpreted for respective class and 
     * type through this function. 
     *
     ***********************************************************************************/
     int index_of(uint16_t val, uint16_t* buf, uint16_t buf_len)
     {
       uint16_t i;
       for(i=0; i<buf_len; i++)
       {
         if(buf[i] == val) return (int)i;
       }
       return -1;
     }
   
   <WRAP centeralign>//<fc #4682b4>Figure 9. Example Code for Class, Type, and PSE/PD Compatibility Matrix Definition</fc>//</WRAP>
   
    
   
   ==== SCCP Byte Level Functions ====
   \\
   === Transmit Byte ===
   
   Figure 10 shows example code for transmit_byte(). The transmit_byte() function accepts a byte and uses the write_bit() protocol function to transmit the passed tx_byte to the PD.
   \\
   \\
   
   
     /******************************************************************************************************************
     Copyright © 2023 by Analog Devices, Inc. All rights reserved. This software is proprietary to Analog Devices, Inc.
     and its licensors. This software is provided on an "as is" basis without any representations, warranties,
     guarantees or liability of any kind. Use of the software is subject to the terms and conditions of the Clear BSD
     License (https://spdx.org/licenses/BSD-3-Clause-Clear.html).  
     
     *Function: void transmit_byte(uint8_t tx_byte)
     *Byte to be transmitted is passed on to this function
     *
     *******************************************************************************************************************/
     void transmit_byte(uint8_t tx_byte)
     {
       uint8_t bit_pos = 0;
       while (bit_pos < 8)
       {
         uint8_t bit = (tx_byte>>bit_pos) & 0x01;
         write_bit(bit);
         bit_pos++;
       }
       return;
     }
   
   <WRAP centeralign>//<fc #4682b4>Figure 10. Example Code for transmit_byte()</fc>//</WRAP>
   
   === Receive Response ===
   
   Figure 11 shows example code for receive_response(). The receive_response() function utilizes the read_bit() protocol function to receive 2 bytes of CLASS_TYPE_INFO data plus a CRC byte from the PD. The resulting bytes are stored at the address of the passed *buf pointer. 
   \\
   \\
   
     /******************************************************************************************************************
     Copyright © 2023 by Analog Devices, Inc. All rights reserved. This software is proprietary to Analog Devices, Inc.
     and its licensors. This software is provided on an "as is" basis without any representations, warranties,
     guarantees or liability of any kind. Use of the software is subject to the terms and conditions of the Clear BSD
     License (https://spdx.org/licenses/BSD-3-Clause-Clear.html).
     
     * Function: void receive_response(uint8_t* buf)
     * Utilizes 'uint8_t read_bit()' to receive 2 bytes of data plus CRC byte from the PD
     *
     *******************************************************************************************************************/
     void receive_response(uint8_t* buf)
     {
       uint8_t rx_byte = 0, bytes_rxd=0, bit_pos = 0;
       
       while (bytes_rxd < 3)
       {
         rx_byte = 0;
         bit_pos = 0;
         while(bit_pos < 8)
         {
           uint8_t bit = read_bit();
           rx_byte |= (bit<<bit_pos);
           bit_pos++;
         }
         buf[bytes_rxd] = rx_byte;
         bytes_rxd++;
         //TimerDelay_ms(5); /* wait 5ms before reading the next byte, used for internal debugging */
       }
       return;
     }
   
   <WRAP centeralign>//<fc #4682b4>Figure 11. Example Code for receive_response()</fc>//</WRAP>
   
   === SCCP Read Registers ===
   
   Figure 12 shows example code for sccp_read_register(). The sccp_read_register() intializes the bus, checks for a PD presence pulse, writes the broadcast address command byte (0xCC) followed by the passed read command byte (cmd), and then reads two bytes of PD data plus the CRC byte. The PD data bytes plus CRC byte are stored at the address of the passed *buf pointer.
   \\
   \\
   
   
     /******************************************************************************************************************
     Copyright © 2023 by Analog Devices, Inc. All rights reserved. This software is proprietary to Analog Devices, Inc.
     and its licensors. This software is provided on an "as is" basis without any representations, warranties,
     guarantees or liability of any kind. Use of the software is subject to the terms and conditions of the Clear BSD
     License (https://spdx.org/licenses/BSD-3-Clause-Clear.html).
     
     * Function: uint8_t sccp_read_register(uint8_t cmd, uint8_t* buf)
     * This function sends the required bytes of SCCP to the PD and receives the response
     *
     *******************************************************************************************************************/
     uint8_t sccp_read_register(uint8_t cmd, uint8_t* buf)
     {
       uint8_t present = send_reset_pulse();
       if (!present) return 0; /* PD must respond to reset pulse with presence pulse */
       
       //TimerDelay_ms(5); /* line stays high for 5ms, used for internal debugging */
       transmit_byte(CMD_BROADCAST_ADDR); /* PSE sends broadcast address 0xCC */
       //TimerDelay_ms(5); /* line stays high for 5ms, used for internal debugging */
       transmit_byte(cmd); /* PSE sends read command (0xAA, 0xBB, 0x77, or 0x81) */
       //TimerDelay_ms(5); /* line stays high for 5ms, used for internal debugging */
       receive_response(buf); /* read 2 bytes of register data plus CRC byte */
       return 1;
     }
   
   <WRAP centeralign>//<fc #4682b4>Figure 12. Example Code for sccp_read_register()</fc>//</WRAP>
   
   === Get CRC ===
   
   Figure 13 shows example code for get_crc(). The get_crc() function returns the expected CRC byte based on two bytes of data stored at the address of the passed *buf pointer. The CRC calculation is based on the generator polynomial G(x) = x<sup>8</sup> + x<sup>5</sup> + x<sup>4</sup> + 1.
   \\
   \\
   
   
   
     /******************************************************************************************************************
     Copyright © 2023 by Analog Devices, Inc. All rights reserved. This software is proprietary to Analog Devices, Inc.
     and its licensors. This software is provided on an "as is" basis without any representations, warranties,
     guarantees or liability of any kind. Use of the software is subject to the terms and conditions of the Clear BSD
     License (https://spdx.org/licenses/BSD-3-Clause-Clear.html).
     
     * Function: uint8_t get_crc(uint8_t* buf)
     * SCCP bytes 
     *
     *******************************************************************************************************************/
     uint8_t get_crc(uint8_t* buf)
     {
       uint8_t byte, bit;
       uint8_t x3,x4,x7, in;
       
       uint8_t crc = 0;
       for(byte=0; byte<2; byte++)
       {
         for(bit=0; bit<8; bit++)
         {
           /* save some bits before shifting register */
           x3 = (crc>>3) & 0x01;
           x4 = (crc>>4) & 0x01;
           x7 = (crc>>7) & 0x01;
           in = (buf[byte] >> bit) & 0x01;
           in ^= x7;
           /* shift the register */
           crc = (crc<<1) | in;
           /* clear bits 4 & 5 */
           crc &= ~(0x30);
           /* replace bits with xor of 'in' and prev bit */
           uint8_t temp = x3 ^ in;
           crc |= (temp<<4);
           temp = x4 ^ in;
           crc |= (temp<<5);
         }
       }
       return crc;
     }
   
   <WRAP centeralign>//<fc #4682b4>Figure 13. Example Code for Calculating CRC Byte from 16 Bit PD Data</fc>//</WRAP>
   
   
   
   
   
   
   ==== Example Detection, Classification, and Power-up Implementation ====
   
   Figure 14 provides example code sccp_do_class() for implementing detection, SCCP, and then power-up one or more ports when the PSE and PD and PSE classes are compatible. The code assumes intialization of the following peripherals:
     - Timer Initialization
     - SPI peripheral for communicating with LTC4296-1
     - Per port GPI and GPO for supporting SCCP
   \\
   Outline of sccp_do_class():
     * 1.	For each port 'x': 
           * Check if port_supports_class[x] is True
           * Confirm LTC4296-1 port has not already powered-up with read of port status {pxst.pse_status != (PSE_STATUS_DELIVERING or PSE_STATUS_SLEEPING or PSE_STATUS_UNKNOWN)}
           * Go to next port if either a or b are false, otherwise go to 2. 
     * 2.   Read LTC4296-1 port configuration register 0 (pxcfg0) and save into 'pxcfg0_old' variable
     * 3.   Disable LTC4296-1 write protection, and write the following bits to the pxcfg0 register:
           * pxcfg0.sw_en = 1
           * pxcfg0.sw_pse_ready = 1
           * pxcfg0.set_classification_mode = 1
           * pxcfg0.tdet_disable = 1
     * 4. If pxst.pse_status fails to go to searching (011b) after 4ms, restore pxcfg0 register contents and go to next port, else proceed to 5. 
     * 5. Check PD detection signature (required by IEEE 802.3bu/cg before going to SCCP):
           * initialize t_det_start from timer
           * While time elapsed since t_det_start is less than 3.1ms:
             * If pxst.det_vlow = 0 & pxst.det_vhi = 0 (valid PD signature voltage), increment t_hold timer, else reset t_hold
             * If elapsed time since t_det_start > 3.1ms and t_hold < 1ms set valid_signature = 0, elseif t_hold > 1ms set valid_signature = 1
     * 6. Do SCCP (note IEEE 802.3bu/cg allows a PSE to power up w/out SCCP if valid_signature == 1):
           * Call sccp_read_register() function and pass Read_Scratchpad command byte
           * If no PD presence pulse was detected, restore pxcfg0 register contents with pxcfg0.sw_power_available=0 and go to next port. 
           * If PSE class and PD class are compatible (class_compatibility matrix), power up port by restoring old pxcfg0 register with pxcfg0.sw_power_available = 1, pxcfg0.sw_pse_ready = 1, and pxcfg0.sw_en = 1.
             * If PSE class and PD class are incompatible, set pxcfg0.sw_en = 0
     * 7. Go to next port or return if last port 
   \\
   \\
   
   
     /******************************************************************************************************************
     Copyright © 2023 by Analog Devices, Inc. All rights reserved. This software is proprietary to Analog Devices, Inc.
     and its licensors. This software is provided on an "as is" basis without any representations, warranties,
     guarantees or liability of any kind. Use of the software is subject to the terms and conditions of the Clear BSD
     License (https://spdx.org/licenses/BSD-3-Clause-Clear.html).
     
     *Function: sccp_do_class()
     *This function incorporates the SCCP using the functions described in previous sections. 
     *
     *Other functions used in this routine:
     *uint8_t LTC4296_pseStatus(uint8_t port): This function takes port number as the 
     *argument and returns the pse status of that port. SPI read command to read port status 
     *register is executed. 
     *uint16_t LTC4296_readRegister(uint8_t address): This function returns value at the 
     *specified register from LTC4296-1 SPI registry. A SPI read command is incorporated.
     * 
     *void LTC4296_writeRegister(uint8_t address, uint16_t value): The value specified is 
     *written and the specified register address. This function incorporates a SPI write 
     *command. 
     *
     *Further this function assumes that the pse sccp information per port is already known. 
     *Port_class[n] contains sccp class and type of port n
     *   
     ********************************************************************************************************************/
     void sccp_do_class()
     {
       uint8_t atLeastOneClassPort = 0;
       uint8_t port;
       for(port=0; port<5; port++)
       {
         if(port_supports_class[port])
         {
           atLeastOneClassPort = 1;
           break;
         }
       }
       if(!atLeastOneClassPort)
       {
         return;
       }
       /* disable write protection */
       LTC4296_writeRegister(REG_GCMD, 5);
     
       for(port=0; port<5; port++)
       {
         if(port_supports_class[port])
         {
           set_active_port(port);
           /* if pse_status == 2 or 1 (delivering or sleeping), skip this port, it's 
           already powered up */
           volatile PseStatus pse_status = LTC4296_pseStatus(port);
           if(pse_status == PSE_STATUS_DELIVERING || pse_status == PSE_STATUS_SLEEPING 
           || pse_status == PSE_STATUS_UNKNOWN)
           {
             continue; // next port
           }
         /* if port is not enabled or in idle, enable it and set tdet_disable and 
         set_classification_mode */
         uint16_t pncfg0_old = LTC4296_readRegister(REG_P0CFG0+0x10*port);
       
         LTC4296_writeRegister(0x13+0x10*port, 0x41 | (1<<11) | (1<<13));
       
         /* wait for pse_status == 3 (searching/detection) */
         pse_status = LTC4296_pseStatus(port);
         uint32_t t0 = HAL_GetTick();
         while(pse_status != PSE_STATUS_SEARCHING && pse_status != 
       PSE_STATUS_DELIVERING)
         {
           if(HAL_GetTick() - t0 > 4000)
           {
             pncfg0_old &= ~(1<<5); // clear pwr_avail
             LTC4296_writeRegister(REG_P0CFG0 + 0x10*port, pncfg0_old);
             LTC4296_writeRegister(REG_P0CFG0 + 0x10*port, pncfg0_old | (1<<14)); 
             //set end_classification bit
           
             return;
           }
           pse_status = LTC4296_pseStatus(port);
         }
         // Tdet additions
         uint32_t t_det_start = TimerDelay_getCount();
         uint32_t t_hold_start = TimerDelay_getCount();
         uint32_t t_hold = 0;
         uint16_t port_status_reg = LTC4296_readRegister(REG_P0ST + 0x10 * port);
         uint8_t port_det_sign = (port_status_reg & 0x3000) >> 12;
         uint8_t valid_sign = 0;
         while (TimerDelay_getCount() - t_det_start < 3100)
         {
           port_status_reg = LTC4296_readRegister(REG_P0ST + 0x10 * port);
           port_det_sign = (port_status_reg & 0x3000) >> 12;
           if (port_det_sign == 0)
           {
             t_hold = t_hold + (TimerDelay_getCount() - t_hold_start);
           }
           else
           {
             t_hold = 0;
             t_hold_start = TimerDelay_getCount();
           }
           if (t_hold > 1000)
           {
             valid_sign = 1;
           }
         }
       
       uint8_t sccp_buf[3];
       TimerDelay_ms(30);
       // read scratchpad and parse type and class
       uint8_t pd_present = sccp_read_register(CMD_READ_SCRATCHPAD, sccp_buf);
       if(!pd_present)
       {
         pncfg0_old &= ~(1<<5); // clear pwr_avail
         LTC4296_writeRegister(REG_P0CFG0 + 0x10*port, pncfg0_old);
         LTC4296_writeRegister(REG_P0CFG0 + 0x10*port, pncfg0_old | (1<<14)); 
         /* set end_classification bit */
         continue; /* next port */
       }
       uint16_t scratchpad = (uint16_t)(sccp_buf[1]) << 8;
       scratchpad |= (uint16_t)(sccp_buf[0]);
       uint16_t pd_class_code = scratchpad & 0x3FF;
       int pd_class_num = index_of(pd_class_code, sccp_classes, 16);
       int pse_class_num = index_of(port_class[port], sccp_classes,16);
       
       if(pse_class_num < 0 || pd_class_num < 0 || pse_class_num > 15 || 
       pd_class_num > 15 || (get_crc(sccp_buf) != sccp_buf[2]))
       {
         /* port hasn't been configured properly */
         pncfg0_old &= ~(1<<5); /* clear pwr_avail */
         LTC4296_writeRegister(REG_P0CFG0 + 0x10*port, pncfg0_old);
         LTC4296_writeRegister(REG_P0CFG0 + 0x10*port, pncfg0_old | (1<<14)); 
         /* set end_classification bit */
         continue;
       }
       uint8_t is_compatible = class_compatibility[pd_class_num][pse_class_num];
       /* if compatible class, read requested power info */
       if(!is_compatible)
       {
         /* sw disable port (unless auto pin is high) */
         LTC4296_writeRegister(0x13+0x10*port, 2 | (1<<14));
         continue; // next port
       }
       pncfg0_old |= (3<<5) | 1 | (1<<13); /* make sure sw_pwr_avail and pse_ready 
       is set */
       LTC4296_writeRegister(REG_P0CFG0 + 0x10*port, pncfg0_old);
       LTC4296_writeRegister(REG_P0CFG0 + 0x10*port, pncfg0_old | (1<<14)); 
       /* end_classification */
       
       /* wait for pse_status == 2 or 1 */
       pse_status = LTC4296_pseStatus(port);
       t0 = HAL_GetTick();
       while(pse_status != PSE_STATUS_DELIVERING && pse_status != 
       PSE_STATUS_SLEEPING)
       {
         if(HAL_GetTick() - t0 > 4000) break;
         pse_status = LTC4296_pseStatus(port);
           }
         }
       }
     }
   
   <WRAP centeralign>//<fc #4682b4>Figure 14. Example Implementation of Detection, SCCP, and Port Power-up</fc>//</WRAP>
   
   
   
   ===== SCCP Evaluation with EVAL-SPoE-KIT-AZ =====
   ==== Equipment for Evaluation====
     - EVAL-LTC4296-1-AZ: 5-port PSE controller LTC4296-1 motherboard
     - EVAL-LTC4296-1-RC-AZ: microcontroller card for driving LTC4296-1 motherboard
     - EVAL-10BT1L-SMC-AZ: Media Converters for PSE and PD motherboards
     - EVAL-LTC9111-AZ: PD controller LTC9111 motherboard
   \\
   SCCP transaction can be evaluated with the EVAL-SPoE-KIT-AZ and the LTC4296-1 GUI. In the drop down menu, boxed in Figure 15, select the maximum PSE class and select Type E. Select classify if classification without power is desired or select power up for classification and subsequent powering up of the PD if it is equal to or less than the maximum PSE class. Once successful power up of the PD has occurred Power Good indicator should light up green as shown in Figure 16.  
   
   Refer to [[:resources:eval:user-guides:eval-spoe-kit-az-wiki-user-guide|EVAL-SPoE-KIT-AZ Evaluation Kit User Guide]] for EVAL-kit setup. \\
   
   {{ :resources:eval:spoe_sccp_gui_part_1.png?nolink&200 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 15. SCCP Enable Configurations through evaluation GUI </fc>//</WRAP>
   {{ :resources:eval:spoe_sccp_gui_part_2.png?nolink&200 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 16. Successful Port Turn On GUI Port Status </fc>//</WRAP>
   
   ===== SCCP Example Waveforms =====
   
   Below are detailed descriptions of the SCCP transactions, parts i-vi. With waveforms captured using the setup in Figure 17. 
   
   
   {{ :resources:eval:spoe_sccp_waveform_key4.png?nolink |}}
   <WRAP centeralign>//<fc #4682b4>Figure 17. Proceeding Waveform Probe Location </fc>//</WRAP>
   ==== (i) Initialization ====
   
   {{ :resources:eval:spoe_sccp_initialization_sequence3.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 18. Initialization Sequence </fc>//</WRAP>
   
   
   === Reset Pulse ===
   
   
   {{ :resources:eval:spoe_sccp_reset_pulse3.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 19. Initialization Sequence Reset Pulse </fc>//</WRAP>
   
   === Presence-Detect High Time ===
   
   
   {{ :resources:eval:spoe_sccp_presence_detect_high3.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 20. Initialization Sequence Presence-Detect High Time </fc>//</WRAP>
   
   === Presence-Detect Low Time ===
   
   
   {{ :resources:eval:spoe_sccp_presence_detect_low3.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 21. Initialization Sequence Presence Detect Low Time </fc>//</WRAP>
   
   === Recovery Time ===
   
   {{ :resources:eval:spoe_sccp_recovery_time_initializtion3.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 22. Initialization Sequence Recovery Time </fc>//</WRAP>
   
   
   === PD Reservoir Capacitor Recharge Time ===
   
   {{ :resources:eval:spoe_sccp_chrg_initialization.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 23. Initialization Sequence PD Reservoir Capacitor Recharge Time </fc>//</WRAP>
   
   === Rise/Fall Time ===
   
   {{ :resources:eval:spoe_sccp_rise_time2.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 24. Initialization Sequence Rise Time </fc>//</WRAP>
   
   
   
   {{ :resources:eval:spoe_sccp_fall_time2.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 25. Initialization Sequence Fall Time </fc>//</WRAP>
   
   
   
   
   ==== Write Time Slot  ==== 
   
   {{ :resources:eval:spoe_sccp_write_time_slot_03.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 26. PSE Writes 0 Time Slot </fc>//</WRAP>
   
   
   
   {{ :resources:eval:spoe_sccp_writeslot_1_2.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 27. PSE Writes 1 Time Slot </fc>//</WRAP>
   
   
   ==== (ii) Broadcast Address  ====
    
   {{ :resources:eval:spoe_sccp_broadcast_address3.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 28. PSE Broadcast (0xCC)  </fc>//</WRAP>
   
   
   
   ==== (iii) Read_Scratchpad Command ====
   
   {{ :resources:eval:spoe_sccp_read_scratchpad3.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 29. PSE Read-Scratchpad Command (0xAA)  </fc>//</WRAP>
   
   
   
   === Alternative Commands ===
   
   ^ Bit(s) ^ Name ^ Description ^ R/W<sup>a</sup>
   | b[15:8] | Reserved | Value Always 0 | Read Only |
   | b[7:0] | Voltage at PD PI during presence pulse | ±20mV tolerance, 10mV per LSB | Read Only |
   <WRAP centeralign>//<fc #4682b4>Table 3. Read_VOLT_INFO Command (0xBB) </fc>//</WRAP>
   
   ^ Bit(s) ^ Name ^ Description ^ R/W<sup>a</sup>
   | b[15:12] | Reserved | Value Always 0 | Read Only |
   | b[11:0] | P<sub>PD_req</sub> PD requested Power | Power requested by PD, 0.025W per LSB | Read Only |
   <WRAP centeralign>//<fc #4682b4>Table 4. Read_POWER_INFO Command (0x77) </fc>//</WRAP>
   
   ^ Bit(s) ^ Name ^ Description ^ R/W<sup>a</sup>
   | b[15:12] | Reserved | Value Always 0 | Read Only |
   | b[11:0] | P<sub>PD_assign</sub> PD Assigned Power | PD assigned power, 0.025W per LSB | Read/Write |
   <WRAP centeralign>//<fc #4682b4>Table 5. Write_POWER_ASSIGN Command (0x99) </fc>//</WRAP>
   
   ^ Bit(s) ^ Name ^ Description ^ R/W<sup>a</sup>
   | b[15:12] | Reserved | Value Always 0 | Read Only |
   | b[11:0] | P<sub>PD_assign</sub> PD Assigned Power | PD assigned power, 0.025W per LSB | Read/Write |
   <WRAP centeralign>//<fc #4682b4>Table 6. Read_POWER_ASSIGN Command (0x81) </fc>//</WRAP>
   
   
   
   ==== Read Time Slot ====
   
   
   {{ :resources:eval:spoe_sccp_read_time_slot_03.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 30. PSE Read 0 Time Slot </fc>//</WRAP>
   {{ :resources:eval:spoe_sccp_read_time_slot_13.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 31. PSE Read 1 Time Slot </fc>//</WRAP>
   
   
     
   
   
   ==== (iv) Read CLASS_TYPE_INFO low byte ====
   
   {{ :resources:eval:spoe_sccp_class_type_info_low_byte_updated.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 32. Read CLASS_TYPE_INFO low byte </fc>//</WRAP>
   
   ==== (v) Read CLASS_TYPE_INFO high byte====
   
   
   {{ :resources:eval:spoe_sccp_class_type_info_high_byte_updated.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 33. Read CLASS_TYPE_INFO high byte </fc>//</WRAP>
   
   
   ==== (vi) Read CRC byte====
   
   {{ :resources:eval:spoe_sccp_pd_crc_updated.png?nolink&600 |}}
   <WRAP centeralign>//<fc #4682b4>Figure 34. PD CRC </fc>//</WRAP>
   
   
   
   
   
   
   
   
   
   ====== Appendix ======
   
   ===== Device Class =====
   IEEE 802.3bu defines Class 0-9 and 802.3cg extends these power classes to Class 10-15. The LTC4296-1 is intended to be used in Class 10-15 systems. Table 7 lists the corresponding Class data for CLASS_TYPE_INFO b[9:0].
   ^ b[9:0] ^ Description ^ 
   | 0x3FE | Class 0 |
   | 0x3FD | Class 1 |
   | 0x3FB | Class 2 |
   | 0x3F7 | Class 3 |
   | 0x3EF | Class 4 |
   | 0x3DF | Class 5 |
   | 0x3BF | Class 6 |
   | 0x37F | Class 7 |
   | 0x2FF | Class 8 |
   | 0x1FF | Class 9 |
   | 0x001 | Class 10 |
   | 0x002 | Class 11 |
   | 0x003 | Class 12 |
   | 0x004 | Class 13 |
   | 0x005 | Class 14 |
   | 0x006 | Class 15 |
   <WRAP centeralign>//<fc #4682b4>Table 7. CLASS_TYPE_INFO b[9:0] to Corresponding PD Class</fc>//</WRAP>
   
   ===== Class Power Requirements =====
   Table 8 shows the PSE, PD and cable requirements for Class 10-15.
   ^ Class Symbol and Unit^ Class Description ^ Class 10 ^ Class 11 ^ Class 12 ^ Class 13 ^ Class 14 ^ Class 15 ^
   |V<sub>PSE</sub> (V) | PSE Output Voltage | 20-30 | 20-30 | 20-30 | 50-58 | 50-58 | 50-58 |
   |I<sub>PI(max)</sub> (mA) | Cable Current | 92 | 240 | 632 | 231 | 600 | 1579 |
   |P<sub>Class(min)</sub> (W) | PSE Output Power | 1.85 | 4.8 | 12.63 | 11.54 | 30 | 79 |
   |V<sub>PD(min)</sub> (V) | PD Input Voltage | 14 | 14 | 14 | 35 | 35 | 35 |
   |P<sub>PD(max)</sub> (W) | PD Power | 1.23 | 3.2 | 8.4 | 7.7 | 20 | 52 |
   |R<sub>LINK_SEG_LOOP</sub> (Ω) | Cable Resistance | 65 | 25 | 9.5 | 65 | 25 | 9.5 | 
   
   <WRAP centeralign>//<fc #4682b4>Table 8. IEEE 802.3cg Class Power Requirements Matrix for PSE and PDs</fc>//</WRAP>
   
   ===== Device Type =====
   IEEE 802.3cg describes Types A-E device types. For 10Base-T1L both PSE and PD must be Type E. Table 9 lists the corresponding Type data for CLASS_TYPE_INFO b[15:12].
   ^ b[15:12] ^ Description ^ 
   | 0xE | Type A|
   | 0xD | Type B|
   | 0xB | Type C|
   | 0x7 | Type D|
   | 0xC | Type E|
   
   <WRAP centeralign>//<fc #4682b4>Table 9. CLASS_TYPE_INFO b[15:12] to Corresponding PD Type </fc>//</WRAP> 
   
   
   
   
   
   
