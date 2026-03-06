EVALUATION BOARD HARDWARE
=========================

The diagram below gives an overview of how the board components are connected.


|02-063798-01-b_blockdiagram.jpg|

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/02-063798-01-b_board.jpg
   :alt: 02-063798-01-b_board.jpg
   :align: center
   :width: 548px
   :height: 386px

POWER SUPPLIES
--------------

The EVAL-ADIN1100FMCZ comes with several board links to select how to power the board as well as the voltage level for the ADIN1100 and ADuCM4050. See the table below for the default link configuration and link description.

+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Link no. | Default Position | Link Function                                                                                                                               |
+==========+==================+=============================================================================================================================================+
| J101     | Earth            | Shield shorted either directly to Earth, or via 4nF cap.                                                                                    |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| P4       | EXT              | The EVAL-ADIN1100FMCZ is powered by a single, external, 5-30 V BOARD_PWR supply rail that can be supplied via the selectable sources below: |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|          |                  | \* FMC - Connects 12V FMC supply to the input of LT8619.                                                                                    |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|          |                  | \* USB – Connects 5V USB supply to the input of the LT8619.                                                                                 |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|          |                  | \* EXT - Connects externally supplied power from P1 or P2 to the input of LT8619.                                                           |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| P10      | Burst            | The LT8619 regulator generates a 3.3 V rail from which the LTC3547 regulator in turn generates a 1.8 V and 1.1 V rail.                      |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|          |                  | \* FORCED CURRENT – (H) Force Continuous mode of operation of LT8619.                                                                       |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|          |                  | \* PULSE SKIP (o/c) - Pulse-Skipping mode of operation of LT8619.                                                                           |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|          |                  | \* BURST (L) – Burst mode of operation of LT8619.                                                                                           |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| J2       | Inserted         | This link supplies 3.3V rail to circuitry on the board, beyond the LT8619.                                                                  |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| P11      | 3V3              | ADuCM4050 supply voltage – choice of 3.3V or 1.8V.                                                                                          |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| P13      | 3V3              | AVDD_H supply voltage – choice of 3.3V or 1.8V.                                                                                             |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| P14      | 3V3              | AVDD_L supply voltage – choice of 3.3V or 1.8V.                                                                                             |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| P15      | 3V3              | VDDIO supply voltage – choice of 3.3V or 1.8V.                                                                                              |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| P17      | DVDD_1P1         | DVDD_1P1 supply voltage – choice of EXT 1V1 rail or internally generated DLDO_1P1 (silkscreen label “DVDD_1P1”)                             |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| P19      | Not inserted     | Option to short AVDD_H to AVDD_L.                                                                                                           |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| P20      | Not inserted     | Option to short AVDD_L to VDDIO.                                                                                                            |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| P8       | PHY RESET        | Option to hold ADuCM4050 in reset (GND RESET) or short it to the PHY RESET_N (PHY RESET).                                                   |
+----------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

HARDWARE CONFIGURATION PINS SETUP
---------------------------------

The ADIN1100 hardware configuration pin settings can be changed by manipulating S1 and S2 switch settings found on the right-hand side of the EVAL-ADIN1100FMCZ board. The table below lists the default switch configuration settings on the board. When the switch is OFF, the hardware configuration pin is pulled low via an internal pulldown resistor, and when the switch is ON, the pin is pulled high via an external 4.7 kΩ pull-up resistor.

+----------------+------------------+---------------------------------------------------------+
| Switch/Pin no. | Default Position | Default Switch Position Function                        |
+================+==================+=========================================================+
| S1/Pin1        | OFF              | TX2P4_ENB – 1 Vpk-pk/2.4 Vpk-pk transmit amplitude mode |
+----------------+------------------+---------------------------------------------------------+
| S1/Pin2        | OFF              | MS_SEL – Prefer slave selection                         |
+----------------+------------------+---------------------------------------------------------+
| S1/Pin3        | ON               | SWPD_ENB – ADIN1100 not in SWPD                         |
+----------------+------------------+---------------------------------------------------------+
| S1/Pin4        | OFF              | MEDIA_CNV – Disable Media Converter mode                |
+----------------+------------------+---------------------------------------------------------+
| S2/Pin1        | OFF              | PHYAD_0 – PHY H/W Address 0x0                           |
+----------------+------------------+---------------------------------------------------------+
| S2/Pin2        | OFF              | PHYAD_1 – PHY H/W Address 0x0                           |
+----------------+------------------+---------------------------------------------------------+
| S2/Pin3        | OFF              | PHYAD_2 – PHY H/W Address 0x0                           |
+----------------+------------------+---------------------------------------------------------+
| S2/Pin4        | ON               | MACIF_SEL0 – MII interface selected                     |
+----------------+------------------+---------------------------------------------------------+
| S2/Pin5        | ON               | MACIF_SEL1 – MII interface selected                     |
+----------------+------------------+---------------------------------------------------------+

ON-BOARD ADUCM4050 MICROCONTROLLER
----------------------------------

The EVAL-ADIN1100FMCZ has an on-board ADuCM4050 which can be used to read/write to the ADIN1100 PHY over the MDIO interface using the USB connection. This allows interaction with the ADIN1100 device via the Ethernet PHY software GUI running on the PC.

ADuCM4050 Configuration Switches
--------------------------------

The ADuCM4050 has 4 associated configuration switches which are pulled low when the switch is in the ON position and pulled high when in the OFF position. By default, all four configuration pins are pulled low. The table below lists the ADuCM4050 operating modes base on the S4-Pin setting.

+----------+------------------------------------------------------------------------------------------------------+
| CFG[3:0] | Operating Mode                                                                                       |
+==========+======================================================================================================+
| 0111     | Enable LED & continuously report MSE value to UART if link is present.                               |
+----------+------------------------------------------------------------------------------------------------------+
| 1101     | Enable Frame Generator/Checker (10,000 frames)                                                       |
+----------+------------------------------------------------------------------------------------------------------+
| 1110     | Enable MAC Interface Remote Loopback4 (MAC_IF_REM_LB_EN)                                             |
+----------+------------------------------------------------------------------------------------------------------+
| 1111     | Search for the PHY, enable & configure LED to blink rate 0x3636, use GUI to interface with ADIN1100. |
+----------+------------------------------------------------------------------------------------------------------+

ADuCM4050 MSE Result
--------------------

The Mean Square Error (MSE) result returned when the ADuCM4050 switches are configured CFG[3:0] = [OFF, ON, ON, ON] indicates link quality. It is in fact the reciprocal of SNR. To meet the 1e-9 Bit Error Rate (BER) mandated by the IEEE802.3cg Standard (clause 146.5.5.1), an SNR of 20.05dB (i.e. MSE of -20.05dB) is required. So a result equal to, or below -20dB is considered compliant with the Standard.

When CFG[3:0] = [OFF, ON, ON, ON], the MSE value of the link is continuously written to the UART and can be read using Termite RS232 terminal (or equivalent) software (assuming there is a valid link in place between two link partners).

ADuCM4050 LEDs
--------------

There are two LEDs associated with the ADuCM4050 – labeled “uC1” and “uC2”. When the ADuCM4050 has been programmed and is ready for use, the orange uC2 led flashes and the red uC1 led blinks once. The red LED turns on if a fault occurs and blinks once upon programming the ADuCM4050, or power-on or hardware reset.

ADIN1100 LED PIN
----------------

There is one LED pin (labeled “LED”) on the ADIN1100. The LED pin can be configured in various operating modes via the MDIO interface (see the ADIN1100 datasheet).

On the first silicon, by default, the LED pin is disabled (this is subject to change on the next revision of silicon). However, the ADuCM4050 has been programmed to enable the LED and cause it to illuminate when a link is established, and flash when there is activity. These LED configuration commands are written to the ADIN1100 in one of four configurations from ADuCM4050 Configuration Switches Table, CFG[3:0]:

-  0111 - Enable LED & continuously report MSE value to UART if the link is present.
-  1101 - Enable Frame Generator/Checker (10,000 frames)
-  1110 - Enable MAC Interface Remote Loopback (MAC_IF_REM_LB_EN)
-  1111 - Search for the PHY, enable & configure LED to blink rate 0x3636, use GUI to interface with ADIN1100.

Note that, by default, the LED does not flash when there is activity in Enable MAC Interface Remote Loopback mode. This is because MAC_IF_LB_TX_SUP_EN = 1, and this suppresses the activity on the RX pins. For the LED to flash on activity, MAC_IF_LB_TX_SUP_EN would need to be set to 0.

Note that if an action performed by the GUI causes the PHY to reset without the ADuCM4050 re-enabling the LED, a pre-loaded script can be run using the GUI to re-issue the commands to re-enable the LED. See the Loading a Script File section. Performing a hardware reset using the S5 button on the board will also cause the LED to be re-enabled, assuming one of the two previously mentioned configurations of the “CONFIG 0-3” switches is in place.

MDIO INTERFACE
--------------

The MDIO interface of the ADIN1100 can be accessed in several ways as highlighted below:

-  UART/USB access via the ADuCM4050.
-  FMC connector access via an FPGA host.
-  Using the 8-pin P12 header.
-  The MDIO interface signals are also accessible on the P7 header.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/02-063798-01-b_mdio.jpg
   :alt: 02-063798-01-b_mdio.jpg
   :align: center
   :width: 380px

EVALUATION BOARD USAGE OPTIONS
------------------------------

The EVAL-ADIN1100FMCZ can be used in two general modes. In standalone mode (see image below), the EVAL-ADIN1100FMCZ can be used to evaluate the ADIN1100 in IEEE 802.3 test modes, establish links with a link partner, and evaluate the performance of the chip. In standalone mode, power the EVAL-ADIN1100FMCZ with a 5-30 V supply at the P1 or P2 connector or via USB.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/10base-t1l/02-063798-01-b_standalonemode.png
   :alt: 02-063798-01-b_standalonemode.png
   :align: center
   :width: 395px

Alternative to standalone mode, the EVAL-ADIN1100FMCZ has an FMC low pin count (LPC) connector, which can be plugged into an FPGA development board. When used with an FPGA board, the media independent interfaces (MII/RMII), clocks, and MDIO interface can be connected to the FPGA board where the MAC and upper layers can be implemented for evaluation of the ADIN1100 in a full system. In this case, the board can be powered from the 12 V FMC supply.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/10base-t1l/02-063798-01-b_fmcmode.png
   :alt: 02-063798-01-b_fmcmode.png
   :align: center
   :width: 395px

CLOCK OPTIONS
-------------

The crystal oscillators on the EVAL-ADIN1100FMCZ include the following:

-  Unordered List ItemY1 is a 32.768 kHz crystal used for the onboard ADuCM4050.
-  Y2 is a 26 MHz crystal used for the onboard ADuCM4050.
-  Y3 is a 25 MHz crystal connected across the XTAL_I pin and XTAL_O pin of the ADIN1100.

As shown in Figure below, the EVAL-ADIN1100FMCZ provides the option to supply the ADIN1100 clock requirements from either an on-board crystal oscillator (Y3), or an external clock (EXT_CLK) applied to the J1 connector. The FMC connector provides a third alternative (RMII_REF_CLK) to supply the ADIN1100 clock signal.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/10base-t1l/02-063798-01-b_clock.png
   :alt: 02-063798-01-b_clock.png
   :align: center
   :width: 472px

When a 25 MHz external clock is applied to the J1 connector, the R86 resistor must be populated and the R72 and R87 resistors must be removed to disconnect the Y1 crystal. The 25 MHz clock must be a sine or square wave signal with an input range of 0.8 Vpk-pk to 2.5 Vpk-pk. See the ADIN1100 datasheet for more information.

For RMII mode, a 50 MHz clock must be used. This could be provided from the host via the FMC connector – RMII_REF_CLK – in which case the R73 resistor must be populated and the R72, R86 and R87 resistors removed.

In either of the cases where an external clock, other than the on-board 25 MHz crystal, is being provided to the ADIN1100, this signal must be capacitively coupled and divided down such that the maximum amplitude does not exceed 2.5 Vp-p. If the clock signal is less than 2.5 Vpk-pk, then C18 (in the case of the J1-supplied clock) and C3 (in the case of the FMC-supplied clock) are not required and a 1 nF coupling capacitor (C55 or C4 respectively) is recommended. If the clock signal is greater than 2.5 Vpk-pk, then C3 or C18 should be 10pF and C55 or C4 chosen such that the signal does not exceed 2.5 Vpk-pk.

The ADIN1100 also provides a 25 MHz reference clock output from the crystal oscillator on the CLK25_REF pin, which is available on the P7 header.

RESET OPTIONS
-------------

The S5 push-button switch is used to reset both the ADIN1100 PHY and the ADuCM4050 microcontroller (P8 is by default in the “PHY RESET” position – see Figure below). Alternatively, the RESET_N signal can be driven from the FMC connector (not shown in Figure 12). A third way to reset the PHY is from the ADuCM4050 output (signal name = uC_to_PHY_RESET). In this case, P8 should be left unconnected, such that the ADuCM4050 uC_to_PHY_RESET signal does not also drive the RESET_uC_N signal to reset the ADuCM4050 itself. The P8 link also facilitates the option to hold the ADuCM4050 in reset using the “GND RESET” position.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/10base-t1l/02-063798-01-b_reset.png
   :alt: 02-063798-01-b_reset.png
   :align: center
   :width: 758px

ON-BOARD EEPROMS
----------------

The EVAL-ADIN1100FMCZ has one unprogrammed, I2C EEPROM, U7 – labeled “FMC EEPROM”. U7 can be programmed with voltage settings to allow the FPGA board to provide the correct voltages on the supply rails. The write address of the EEPROM is 0b[10100 [GA1] [GA0] 0] and the read address is 0b[10100 [GA1] [GA0] 1].

The EVAL-ADIN1100FMCZ also has an SPI EEPROM, U6, which could be used to store the board type, revision, and unique ID but as yet, is unprogrammed.

PROGRAMMING THE ADUCM4050
-------------------------

The ADuCM4050 is programmed out-of-the-box, so unless a new hex file is being downloaded to the ADuCM4050, it is not necessary to program it to use the EVAL-ADIN1100FMCZ evaluation board. The default behavior of the configuration switches based on the pre-loaded firmware is listed in Table 5. The current revision of the firmware can be viewed using a UART terminal window and pressing the RESET push-button-switch (S5).

To program the ADuCM4050, use the following steps:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/10base-t1l/02-063798-01-B_CrossCore.png
   :alt: 02-063798-01-B_CrossCore.png
   :align: center
   :width: 400px

-  Ensure the mini USB cable is connected between the EVAL-ADIN1100FMCZ board and the PC and open the CrossCore serial flash programmer software.
-  Set the CrossCore Serial Flash programmer according to Figure above(COM port may vary depending on the PC).
-  Browse to select the hex file to download.
-  On the EVAL-ADIN1100FMCZ board, simultaneously press buttons S3 (BOOT) and S5 (RESET). Hold and release the RESET button first, followed by the BOOT button. Now the ADuCM4050 microcontroller is in the programming state.
-  Click Start and the code should start to download with updates provided in the Status window and progress bar across the bottom of the window.
-  After programming, press & release the RESET button (S5).

INTERACTING WITH THE PHY USING UART TERMINAL WINDOW
---------------------------------------------------

To interact with the PHY using a UART terminal window such as Termite, the ADuCM4050 configuration switches (CFG[3:0]) can be in any configuration. Launch the UART terminal window and ensure the relevant COM port is selected. Type ‘?’<newline> to get a list of possible commands. Typing ‘info’<newline> displays the board informed of the evaluation board connected to the active COM port, while typing ‘reset’<newline> resets the ADuCM4050. The other two relevant commands to read/write from/to the ADIN1100 are:

::

   *‘mdiord_cl45 <PhyAddr>, <RegAddress in hex>’<newline>
   *‘mdiowr_cl45 <PhyAddr>, <RegAddress in hex>, <Data>’<newline>

where “RegAddress” is a concatenation of the ADIN1100 Device Address & Register Address per the ADIN1100 datasheet e.g. AN_STATUS register address would be inserted as “0x07006C”. > |02-063798-01-B_UARTex.png| >


|02-063798-01-B_STA.png|

For example:

-  The AN_STATUS register is initially read with a value of 0x006C, meaning that the AN_LINK_STATUS bit (device address 0x07, register address 0x0201, bit 2) is a 1 and a valid link is present.
-  Subsequently, the CRSM_SFT_PD bit (device address 0x1E, register address 0x8812, bit 0) is set to a 1 which puts the PHY on one side of the link into software power-down.
-  The next command written checks that the previous write took effect and that the CRSM_SFT_PD bit is indeed read back as a 1.
-  A subsequent check of the AN_STATUS register contents reveals that the AN_LINK_STATUS bit is now a 0 and there is no longer a valid link present.
-  Next, the CRSM_SFT_PD bit is cleared to 0.
-  And subsequently readback to ensure it is read as a 0.
-  Finally, the AN_STATUS register is read once more and it can be seen that the AN_LINK_STATUS bit is once more a 1 and there is a valid link present.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/10base-t1l/02-063798-01-B_UARTEX2.png
   :alt: 02-063798-01-B_UARTEX2.png
   :align: center
   :width: 400px

.. |02-063798-01-b_blockdiagram.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/02-063798-01-b_blockdiagram.jpg
   :width: 548px
   :height: 286px
.. |02-063798-01-B_UARTex.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/10base-t1l/02-063798-01-B_UARTex.png
   :width: 400px
.. |02-063798-01-B_STA.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/10base-t1l/02-063798-01-B_STA.png
   :width: 400px
