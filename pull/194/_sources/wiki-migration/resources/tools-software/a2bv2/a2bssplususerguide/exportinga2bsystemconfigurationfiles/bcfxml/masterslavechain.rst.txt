Go back to :doc:`Home Page </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml>`

Master_Slave_Chain
==================

Master_Slave_Chain has below attributes.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image6.png
   :align: center

Each Attribute is of “Byte” Data type.

Sub Elements of Master_Slave_Chain
==================================

-   Chain_Num – Main-Sub Nodes daisy chain number in the A2B Network.
-   Num_of_Slave_Nodes – Number of Slave nodes for the current daisy chain.

Node elements depends on Number of A2B Sub nodes present in the current daisy chain.

Main Node Configuration in A2B Network
======================================

This xml element contains set of attributes and sub elements as below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image7.png
   :align: center

-   Version – Silicon version of the A2B Transceiver.
-   Type – Node Type (Master/Slave)
-   ID – Main/Slave Node ID. For main node it is always "0x00", for first Slave node it is "0x00", second slave node it is "0x01" and so on.
-   Source_ID – Main Node ID, it is always "0xFF", for slave node, it is always 0x00
-   Part_number – Part number of A2B Transceiver [AD2428,AD2433 etc.]
-   NodeName – Transceiver label in the schematic
-   Local_power – Node power configuration [local or bus powered]
-   HighPwrSw_config – High power switch configuration

Each attribute is of “String” Data type.

Sub Elements of Main Node
=========================

Authentication_Settings
=======================

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image8.png
   :align: center

Each attribute is of “String” Data type.

-   Vendor – Transceiver Vendor ID
-   Version – Transceiver Silicon Version
-   Product – Transceiver Product ID
-   Capability – Interface Capability (3 – I2C)
-   Transceiver Authentication – Enable/Disable

This xml element contains 1 sub element with attribute as below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image9.png
   :align: center

This attribute Is of “String” Data type.

Custom_Node_Id_Settings
=======================

-  Custom_Node_Id_Authentication – Enable/Disable Custom Node Id Settings using I2C Device.
-  Read_Frm ="A2B_READ_FROM_MEM"
-  Device_Addr="0x50" - Device Address
-  Node_Id="AD243xSubNode_0" - Node name
-  Node_Id_Length="0xF" - Length of node name
-  Read_Mem_Addr_Width="0x2" - Address Width
-  Read_Mem_Addr="0x100" - Address
-  Custom_Node_Id_Authentication - Enable/Disable Custom Node Id Settings using GPIO strapping.
-  Read_Gpio="A2B_READ_FROM_GPIO"
-  GPIOx_Value="A2B_IGNORE" - Enable/Disable/Ignore
-  Custom_Node_Id_Authentication="A2B_ENABLED" Enable/Disable Custom Node Id Settings using Mail Box Authentication.
-  Read_Comm="A2B_READ_FROM_COMM_FW"
-  Time_Out="0x64" -
-  Node_Id="AD243xSubNode_0" - Node name
-  Node_Id_Length="0xF" - Length of node name
-  CustAuth_RetryCnt="0x0" - Retry Count for all modes

Pin_Assignment_Settings:
========================

This xml element contains below sub elements with two attributes each called Func and its corresponding IOMapping (except the last one which has GPIO_Mode) as below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image10.png
   :align: center

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image11.png
   :align: center

I2S_Settings:
=============

This xml element contains below sub elements with combination of Register field and Rate Settings with attributes as below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image12.png
   :align: center

-   TDM_mode – 2/4/8/12/16/20/24/32.
-   TDM_channel_size – 16/32 bit.
-   Sync_Mode – Pulse/Duty cycle.
-   Sync_polarity – Raising/falling Edge.
-   Early_frame_sync_status – Enable/Disable
-   Transmit_Bit_clock_polarity(DTX) - change BCLK edge (Raising/falling)
-   Receive_Bit_clock_polarity(DRX) - sampling BCLK edge (Raising/falling)
-   TX_interleave_slots – Interleave slots between Tx pins. (Enable/Disable)
-   RX_interleave_slots – Interleave slots between Rx pins. (Enable/Disable)
-   Transmit_data_offset_in_TDM – Transmit channel offset in TDM (0 to 3).
-   Receive_data_offset_in_TDM – Receive channel offset in TDM (0 to 63).
-   Txpin_TriState_before_driving_TDM_slots – Enable/Disable.
-   Txpin_TriState_after_driving_TDM_slots – Enable/Disable.
-   Sync – Enable/Disable.

Each attribute is of “String” Data type.

Rate Settings
=============

This xml element contains below sub elements and is part of I2S_Settings

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image13.png
   :align: center

-   LSB – Enable/Disable Valid RR bit in LSB.
-   Extra_Bit – Enable/Disable Valid RR bit in Extra Bit.
-   Extra_Channel - Enable/Disable
-   Strobe_in_IO1 – Enable Reduced Rate Strobe in ADR1/IO1.
-   Strobe_Direction – High/Low.

Each attribute is of “String” Data type.

Basic_Configuration_and_Control
===============================

This xml elements contains below sub elements with attributes as below.


|image1|

-   Response_cycles
-   Slot_Fmt
-   Pass_Up_Slots
-   Pass_Down_Slots
-   Early_acknowledge_for_I2C
-  Data_control
-   Dis_I2C_Interface

Each attribute is of “String” Data type.

GPIO_Settings
=============

This xml element contains below sub elements with attributes as below:


|image2|

-  GPIO_1_Pin_multiplexing
-   GPIO_2_Pin_multiplexing
-   GPIO_3_Pin_multiplexing
-   GPIO_4_Pin_multiplexing
-   GPIO_5_Pin_multiplexing
-   GPIO_6_Pin_multiplexing
-   GPIO_7_Pin_multiplexing
-   Digital_Pin_Drive_Strength – High/Low
-   IRQ_Edge – Rising/falling.
-   IRQ_Tristate – Enable/Disable.

Each attribute is of “String” Data type.

Interrupt_Configuration:
========================

This xml element contains below sub elements with attributes as below and these attributes can be enabled/disabled by selecting Report/Do not Report.

Each attribute is of “String” Data type.

|image3| |image4|

GPIO_Over_Distance_Settings:
============================

This xml element contains one sub element for each GPIO, and each contains attributes as below:

|image5| |image6|

-   GPIOD_X - Enable/Disable GPIO Over Distance, where X = 0 - 7
-   GPIOD_X_Signal_Invert - Enable/Disable Signal Invert, where X = 0 - 7
-   GPIOX_FlagY – Bus port masks, where X, Y = 0 - 7

Each attribute is of “String” Data type.

Clock_Output_Settings
=====================

This xml element contains below sub elements with attributes as below: |image7|


|image8|

-  Pre_Div_Factor1 – Clock1 pre-division
-   Post_Div_Factor1 – Clock1 post-division
-   Clk1_Invert – Enable/Disable Clock1 inversion.
-   Pre_Div_Factor2 – Clock2 pre-division
-   Post_Div_Factor2 – Clock2 post-division
-   Clk2_Invert – Enable/Disable Clock2 inversion.

Attributes are of “Byte” Data type except Clk1_Invert; Clk2_Invert attributes which are of “String” Data type.

Register Settings
=================

This xml element contains below sub elements with attributes as below:


|image9|

-   SWCTL_Register – Switch Control Register
-   PDMCTL_Register – PDM Control Register
-   PDMCTL2_Register – PDM Control 2 Register
-   PLLCTL_Register – PLL Control Register
-   CONTROL_Register – Control Register
-   TESTMODE_Register – Test Mode Register
-   BECCTL \_Register – Error Control Register
-   ERRMGMT_Register – Error Management Register
-   I2STEST_Register – I2S Test Register
-   GENERR_Register – Generate Error Register
-   RAISE_Register – Raise Interrupt Register
-   BMMCFG_Register – Bus Monitor Configuration Register.
-   SWCTL2 – Switch Control 2 Register
-   SWCTL5 – Switch Control 5 Register
-   TXCTL_Register – TX Control Register

Each attribute is of “String” Data type.

SPI_Settings
============

This xml element contains below sub elements with attributes as below. Each attribute is of “String” Data type.

-   SPI_Mode - Master / Slave
-   SPI_CPOL – Lead Clock Edge
-   SPI_CPHA – Sample Clock Edge
-   SPI_ClkDivFactor – Clock Division Factor

|image10| |image11|

::

     * SPI_FD_Slave_Select – Full Duplex Slave Select
   *  SPI_FD_Size – Full Duplex Size
   *  SPI_FD_TargetNode – Full Duplex Target Node
   *  SPI_Target_SlaveSelect – Full Duplex Target Slave Select
   *  SPI_FD_ClkStretch_Enable – Enable/Disable Full Duplex Clock Stretch
   *  SPI_INTMASK_FIFO_Underflow – Enable/Disable FIFO Underflow Error
   *  SPI_INTMASK_FIFO_Overflow – Enable/Disable FIFO Overflow Error
   *  SPI_INTMASK_Bad_Command – Enable/Disable Bad command.
   *  SPI_INTMASK_Data_Tunnel – Enable/Disable Data Tunnel Error
   *  SPI_INTMASK_Remote_I2C – Enable/Disable SPI Remote I2C Access Error
   *  SPI_INTMASK_Remote_Reg - Enable/Disable SPI Remote Reg Access Error
   *  SPI_INTMASK_Spi_Done – Enable/Disable SPI Done
   *  SPI_DT_Enable – Data Tunnel Enable
   *  SPI_DT_Ownership – Tunnel Ownership (Owner/Responder)
   *  SPI_DT_Position – Tunnel Position
   *  SPI_DT_Downstream_Slots – Data Tunnel Downstream Slots
   *  SPI_DT_Upstream_Slots – Data Tunnel Upstream Slots
   *  SPI_DT_Downstream_Offset – Data Tunnel Downstream Offset
   *  SPI_DT_Upstream_Offset – Data Tunnel Downstream Offset

TXXBAR Settings
===============

This xml element contains below sub elements with attributes as below and each attribute is of “String” Data type.

-  TXXBARy - Byte (y = 0 - 31)

RXXBAR Settings
===============

This xml element contains below sub elements with attributes as below and each attribute is of “String” Data type.

-  RXMASKy - Byte (y = 0 - 7)

VMTR Settings
=============

This xml element contains below sub elements with attributes as below and each attribute is of “String” Data type.

-  VMTR_VEN
-  VMTR_IntEN = Byte
-  VMTR_MaxStat = Byte
-  VMTR_MinStat = Byte
-  VMTR_Vtgx_Max = Byte (x = 0 - 6)
-  VMTR_Vtgx_Min = Byte (x = 0 - 6)

PWM_Settings
============

This xml element contains below sub elements with attributes as below and each attribute is of “String” Data type.


|image12|

-  PWM_PwmCfg – PWM Configuration
-   PWM_PwmFreq – PWM Pin Frequency
-   PWM_PwmBlink1 – PWM Blink rate

   -  PWM_PwmBlink2 – PWM Blink rate

-   PWM_PwmxValH – PWM x = 1,2,3 High value
-   PWM_PwmxValL – PWM x = 1,2,3 Low value
-   PWM_PwmOEValH – PWM OE High value
-   PWM_PwmOEValL – PWM OE Low value

PDM_Settings
============

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image27.png
   :align: center

-  Number_of_PDM0_slots
-   Number_of_PDM1_slots
-   Use_High_Pass_Filter
-   PDM_AltClk_Inv_OnBCLK
-   PDM_Alt_Clk
-   PDM0_Falling_Edge_First
-   PDM1_Falling_Edge_First
-   PDM_Destination
-   PDM_HPF_Corner_Freq

Each Attribute is of “String” Data type.

Sub Node x Configuration in A2B Network:
========================================

This xml element contains similar elements as Main node configuration except for additional sub elements as below:

Peripheral_Config
=================

Peripheral_x_Config sub element depends on the number of peripherals connected to each A2B sub-Node in the schematic. Each Peripheral_x_Config element contains sub elements with attributes as below.


|image13|

-  Number_of_Peripherals
-   I2C_interface_status – Enable/Disable
-   I2C_Address – 7-bit I2C Address
-   SPI_interface_status – Enable/Disable
-   SPI_SlaveSelect
-   Device_Type – audio source/sink/host
-   Rx0_Pin_Use – Rx0 pin in use (Enable/Disable)
-   Tx0_Pin_Use – Tx0 pin in use (Enable/Disable)
-   Rx1_Pin_Use – Rx1 pin in use (Enable/Disable)
-   Tx1_Pin_Use – Tx1 pin in use (Enable/Disable)
-   No_of_Tx0_Channels
-   No_of_Rx0_Channels
-   No_of_Tx1_Channels
-   No_of_Rx1_Channels
-   Enable_Program_During_Discovery – True/False
-   Config_XML_File – File path for config XML

Each attribute is of “String” Data type.

Common_Config
=============

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image29.png
   :align: center

-   Downstream_slot_size – 8/12/16/20/24/28/32-bit
-   Upstream_slot_size - 8/12/16/20/24/28/32-bit
-   Upstream_compression – floating point compression
-   Downstream_compression – floating point compression
-   Enable_upstream – Enable/Disable Upstream
-   Enable_Downstream – Enable/Disable Downstream
-   Master_I2C_address – 7-bit I2C master address
-   Bus_I2C_address – 7-bit I2C Bus address

Each attribute is of “String” Data type.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image14.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image15.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image17.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image18.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image19.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image20.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image21.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image22.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image23.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image24.png
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image25.png
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image26.png
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image28.png
