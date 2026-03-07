PHY Exchange Guide, DP83822 to ADIN1200 10/100Mb
================================================

.. container:: group

   
   .. container:: half column

         
         **Overview**

         
         This PHY exchange guide captures pertinent information to support migration from the TI DP83822 to the Analog Devices ADIN1200 Ethernet PHY. Both devices support MII, RMII and RGMII MAC interfaces from the same package version. The PHYs have different pinouts, therefore the ADIN1200 is not a drop-in replacement for the TI product. This requires edits to the schematic and board layout to achieve this exchange. The following sections detail the modifications at the schematic level required to migrate from DP83822 to the ADIN1200 device.
         
         **Hardware Changes By Function**

         
         **Power Supplies Overview**

         
         The supply requirements are listed in Table 1. Both devices can operate from a minimum of one 3.3V power supply rail AVDD_3P3 (AVD), where the VDDIO rail is connected to 3.3V, alternatively the VDDIO rails can be run with a different supply voltage. The ADIN1200 has an on chip voltage regulator to generate the internal core supply rail and provided to a pin for decoupling purposes.
         
         .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/dp83822_table1.png
            :align: center
            :width: 600px
         
         The ADIN1200 is robust to power supply sequencing and the power can be applied in any order. The ADIN1200 provides two pins for each supply rail, whereas the TI device provides one power supply pin for each rail. The VDDIO supply rail powers the MAC interface and MDIO blocks, this can operate from 1.8V, 2.5V or 3.3V. Decoupling requirements for each device differs as described in Table 2 {{ :resources:eval:user-guides:adin1300-and-adin1200:dp83822_table2.png?direct&600 \|
         
         RESET Operation
         ~~~~~~~~~~~~~~~
         
         An active low hardware reset pin, RESET_N is provided on Pin 6 of the ADIN1200 and pin 18 of the DP83822. The hardware strapping pins are read and updated at the de-assertion of reset for both devices. For the ADIN1200, the RESET_N pin resides in the AVDD_3P3 voltage domain, whereas for the TI device, the RESET_N pin is referenced to VDDIO. In applications where the MAC interface is powered from VDDIO of 1.8V, level shifting of the RESET_N signal applied to the ADIN1200 may be required to ensure the voltage level on the RESET_N pin is in excess of the minimum input high threshold level.
         
         Clocking
         ~~~~~~~~
         
         A 25 MHz crystal or external clock source is used to provide the reference clock for both devices. In RMII mode, the ADIN1200 expects an external 50MHz REF_CLK provided to the XTAL_I/REF_CLK pin. In RMII master mode, the DP83822 (RMII mode) can provide a 50 MHz REF_CLK to the MAC device from the 25 MHz source. Alternatively, in RMII slave mode, provide an external 50 MHz both the PHY and MAC.
         
         Bias Resistor
         ~~~~~~~~~~~~~
         
         An external resistor, REXT (RBIAS) is required to bias internal reference circuitry for both DP83822 and ADIN1200. The ADIN1200 requires a 3.01 kΩ resistor (1% tolerance, 100 ppm/°C temperature coefficient) connected to pin 10. The DP83822 uses a 4.87 kΩ on pin 16 (RBIAS).
         
         .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/dp83822_table3.png
            :align: center
            :width: 600px
         
         Media Dependent Interface (MDI)
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         
         The ADIN1200 has voltage mode line drivers with on-chip terminations so no external termination resistors are required and the center tap of the transformer does not require biasing to supply voltage. The recommended external circuit for the interface to the magnetics and RJ-45 is shown in Figure 1 for the voltage mode ADIN1200. The DP83822 uses current mode drivers requiring external termination resistors on the differential pairs in addition to requiring the center tap pin on the device side of the transformer be pulled to the analog supply rail (AVD). The configuration shown in Figure 2 illustrates a simplified diagram showing the additional termination resistors and the biasing of the center tap required for current mode PHYs. Note there may be additional decoupling and inductance used in practice.
         
         |image1| **Figure 1 Isolation using Discrete Magnetics (Voltage Mode Driver) ADIN1200** |image2| **Figure 2 Simplified circuit for Current Mode Driver (DP83822)**
         
         MDIO/Management Interface
         ~~~~~~~~~~~~~~~~~~~~~~~~~
         
      Both devices can be hardware strapped to be used in an unmanaged configuration. Alternatively, they can provide SMI/MII access over the two wire MDIO interface. The MDIO pin (Management Data Open Drain Input/Output) for SMI/MII interface to MAC and requires an external pullup resistor. The recommended value for ADIN1200 is a 1.5kΩ resistor connected to pin 24. The DP83822 recommends 2.2kΩ connected to pin 19. The ADIN1200 supports an MDC clock up to 5.5MHz, while the DP83822 supports an MDC clock as fast as 25MHz. A hardware interrupt output pin INT_N (INTb) is provided in both devices and is open drain. The recommended value for ADIN1200 is a 1.5kΩ resistor connected to INT_N pin 27. The DP83822 has a weak internal pullup, and in application circuit shows a 2.2kΩ connected to INTb, pin 8.

   
   .. container:: half column

         
         **LED Function**

         
         Both devices support two LED pins. The ADIN1200 pins are LED_0 and LINK_ST. The LED_0 has programmability of LED functions, with different blinking operation possible through MDIO configuration, the default mode is ON when Link is Up, blink if activity. The LINK_ST provides static information about Link up or down status. The DP83822 pins are LED0, LED1, where LED0 can be configured for On/Off and Blink if activity while LED1 can be configured to indicate 10 or 100M link speed. Both devices use these pins for Speed and Auto-Neg strapping purposes.
         
         **LED Circuit**

         
         The ADIN1200 LED_0 operates from the AVDD_3P3 voltage domain, therefore can support driving LEDs even when the MAC interface is running at the lower voltage of VDDIO= 1.8V. The default LED operation is on if the Link is up and blinks when there is activity, this operation can be reprogrammed through MDIO write. For the LED_0 of the ADIN1200, it can be configured with 4-level strapping. The strapping configuration will have an impact on how the LED function operates, and needs to be considered if the LED pins are used to directly drive an LED. If the strap pin is pulled high by the strapping resistors, (MODE_3/MODE_4) the output will be configured as an active low driver and conversely if the strapping input is pulled low (MODE_0/MODE_1), the output will be configured as active high. This LED circuit should be configured accordingly.
         
         |image3| Figure 2. LED_0 Hardware Configuration Pin Interaction
         
         **Link Status, LINK_ST**

         
         The ADIN1200 has a dedicated LINK_ST pin to provide information to the MAC on the status of the Link. By default, the LINK_ST pin goes high indicating the link is up and low to indicate the link is down. The LINK_ST polarity is programmable by setting the bit high GE_LNK_STAT_INV_EN. The LINK_ST could be used to drive an LED, however it resides in the VDDIO voltage domain, therefore, when driving an LED in an integrated RJ45 jack where the PHY VDDIO is 1.8V, level shifting will be required.
         

   


--------------

.. container:: group

   
   .. container:: half column

         
         **MAC Interface**

         
         Both PHYs support MII, RMII and RGMII MAC interface modes. The following sections describe specifically the interfaces for both devices.
         
         **MII Interface**

         
         The MII interface is the communication path between the PHY and MAC devices. The MII interface has a high pin count, with a total of 15 pins for data transmission, reception and to signal errors or collision. It is sometimes used in 100M applications as it has a lower latency than RGMII and is much lower than RMII. Table 4 shows a pin overview of both devices for the MII MAC interface mode. When using the ADIN1200 in MII mode, the multifunction pin “LED_0/COL/TX_ER” automatically becomes COL. Similarly, the “INT_N/CRS” becomes CRS. The ADIN1200 sub-system registers provide user with ability to reconfigure which pin the COL and CRS functions are provided on (option of redirecting to GP_CLK, LINK_ST or INT_N). This requires a register write over MDIO interface to reconfigure.
         
         .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/dp38322_table_4_mii_mac_interface_mode_pin_comparison.png
         
         RMII Interface
         ^^^^^^^^^^^^^^
         
         RMII is a reduced MII interface using fewer pins as shown in Table 5. The pin count for this interface is 8 pins.

         
         |image4|

      RMII mode requires a 50MHz clock, REF_CLK. In RMII mode, the ADIN1200 requires an external 50MHz clock applied to XTAL_I. The DP83822 can generate a 50MHz clock internally and provide it to the MAC (master mode). Alternatively in slave mode, it can accept an external 50MHz clock from the MAC.

   
   .. container:: half column

         
         **RGMII Interface**

         
         Both support an RGMII interface mode. The RGMII interface has a low pin count interface support for 10M, 100M and Gigabit operation with a total of 12 pins for data transmission, reception and to signal errors or collisions. It is the most common interface used for Gigabit applications. These PHYs can support 10/100 M speeds over the RGMII interface.

         
         |image5|

         **100BASE-FX**

         
         The DP83822 “F” versions also support 100BASE-FX interface. The ADIN1200 does not support 100BASE-FX.
         
         **Output Clocks**

         
         The ADIN1200 can optionally provide a number of clock signals on the GP_CLK pin. This is configured via MDIO writes and the clocks available are a 125 MHz free running clock, 25 MHz clock and 25MHz/125 MHz recovered clock.
         

   


--------------

.. container:: group

   
   .. container:: half column

         
         **Hardware Configuration**

         
         Both devices have a number of strapping options to enable managed or unmanaged configurations of the PHY function such as PHY address, mode of operation, Auto-Negotiation and MAC Interface. After power on, the strapping pin voltages get sensed and latched upon existing from a reset and the sensed voltages are used to set the personality of the PHY. When configuring any strapping configurations, ensure to review the default state of the MAC side, whether the pins are being driven when coming out of reset or if there are internal pulls. Understanding the behavior on the MAC side is key to ensuring there are no conflicts with the hardware strapping implemented, or to adjust the strapping resistor values if required. The DP83822 uses 4-level strapping options throughout, while the ADIN1200 uses a mix of 2-level and 4-level. In general, strapping pins are multi-functional and have different operation after the device is brought out of reset. The ADIN1200 has internal pull downs on many of its strapping pins (not all), therefore it would be possible to minimize external strapping resistors.
         
         |image6| Figure 4. ADIN1200 Hardware Strapping, 2 and 4 level strapping resistors |image7|
         
         Strapping configurations are very specific to the device, consult the respective datasheets to determine the exact configuration for required use case. The DP83822 has internal pullup resistors of 50kΩ on COL, LED_0, CRS and RX_ER. All other pins used in strapping functios have internal 9 kΩ pulldown resistors, therefore external strapping values differ depending on pin as shown in Table 8 and Table 9.

         
         |image8|

   .. container:: half column

         
         **Hardware Configuration of Speed**

         
         For the ADIN1200, speed configuration is done using two pins, PHY_CFG0 and PHY_CFG1. These pins do not have any internal pull resistors, therefore external strapping is required. Both pins support 4-level strapping, providing much flexibility in terms of the possible combinations, such as Auto-neg speeds shown in Table 10 or Forced modes shown in Table 11. Review the datasheet hardware configuration pin section for full detail on the possible settings using these pins. The DP83822 uses pins RX_D0, RX_D3 and LED_0 to select speeds 10 or 100 M speeds, duplex and forced mode or auto-negotiation.

         
         |image9|

         .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/ksz_table9.png
            :width: 600px
         
         Hardware Configuration of Auto-MDIX
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         
         Selection of Auto-MDIX for the ADIN1200 is done using one pin, (MDIX_MODE) with 4-level strapping. In the DP83822 Auto-MDI/MDI-X is enabled by default and set by the RX_ER strapping pin.
         
         .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/ksz_table10.png
            :width: 600px
         
         MAC Interface Selection
         ~~~~~~~~~~~~~~~~~~~~~~~
         
         The ADIN1200 uses two hardware pins, MACIF_SEL0 and MACIF_SEL1 to provide user ability to select different MAC interfaces. These two pins have internal weak pull downs, therefore the default operation would be RGMII with delays as shown in Table 13. To configure any other MAC interface mode, use 10kΩ pull up or pull down resistors to select accordingly. The DP83822 MAC interface selection is chosen by selecting the appropriate configuration of RX_DV, RX_ER (for MII, RMII or RGMII mode) with combination of RX_ER, LED_1 and COL for 100BASE-FX mode.
         
         Hardware Configuration of PHY Address
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         
         Both devices use two-level strapping, either pull high or low to configure the PHY address. The ADIN1200 provides four PHY address pins, allowing up to 16 unique addresses possible. The PHY address pins are shared with the RXD output pins. The default PHY address strapping for ADIN1200 is 0x0000. The DP83822 provides five PHY address pins, capable of 32 unique addresses. The PHY Address pins are also on RX_Dx pins and COL. The default PHY address strapping for DP83822 is 0x0001.
         

   


.. important::

   Strapping configurations are very specific to the device, consult the respective datasheets to determine the exact configuration for required use case.


--------------

.. container:: group

   
   .. container:: half column

         
         **Package**

         
         Both the ADIN1200 and the DP83822 are available in a 32 lead QFN/LFCSP package of 5 mm x 5mm body size. The devices have different pinouts, therefore the ADIN1200 is not a drop-in replacement for the TI product. This requires edits to the schematic and board layout to achieve this exchange.
         
         .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/dp83822_table14.png
            :align: center
            :width: 600px
         
         The underside of the LFCSP package for the ADIN1200 includes an exposed paddle which should be soldered directly to the board with an array of vias for thermal purposes. There are also two exposed stripes adjacent to the exposed paddle. These do not need to be soldered to the board, they should be treated as a keepout area as they are connected to supply rails in the device, therefore should not be tied to ground and there should be no routing or traces on the PCB layer directly underneath them.
         
         Other Pinout Considerations
         ---------------------------
         
         Integrated MDI Termination
         ~~~~~~~~~~~~~~~~~~~~~~~~~~
         
         The ADIN1200 is a voltage mode PHY, therefore includes integrated termination resistors on the MDI paths. The DP83822 is a current mode PHY, so requires external resistors for biasing and center tap of the transformer must be pulled to supply.
         

   
   .. container:: half column

         
         **Software Considerations**

         
         Both devices can be hardware strapped to be used in an unmanaged configuration. Alternatively, they can provide SMI/MII access over the MDIO interface. The KSZ8081 supports Clause 22 register access, while the ADIN1200 supports both Clause 22 and Clause 45 access. Registers 0x0 to 0xF are common across all PHYs.
         
         **Linux Driver**

         
         The ADIN1200 has a Linux Driver available in the Linux mainline kernel. The ADIN1200 linux driver detail is captured here: :doc:`/wiki-migration/resources/tools-software/linux-drivers/net-phy/adin`
         
         **Non Operating System Driver**

         
         The ADIN1200 has a Non Operating System Driver available from the devices product page here: :adi:`adin1200.html#product-requirement <en/products/adin1200.html#product-requirement>`
         

   


.. tip::

   The ADIN1200 has a Linux Driver available in the Linux mainline kernel.


--------------

High Level Comparison
---------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/dp83822_table_comparison.png
   :align: center

--------------

Side by Side Package/Pinout Comparison
--------------------------------------

The following is a side-by-side comparison of the package and pinouts, showing the position of the corresponding functional pins on each device.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/dp83822_side_by_side.png
   :align: center

--------------

Example Configurations for RMII
-------------------------------

The following example captures how to configure the ADIN1200 for an unmanaged configuration with RGMII Interface, operating in Auto-negotiation mode advertising all speeds. The PHY will power up in this state, ready to establish a link with a link partner. The MAC interface configuration pins (MACIF_SEL0/1) are pulled to ground, setting the PHY to RGMII mode. GP_CLK is set to MODE_3 to configure an automatic MDIX operation. In addition, the PHY_CFG0 and PHY_CFG1 pins are configured for MODE_4 and MODE_1 respectively. The PHY_CFG0 pin is also shared with the LED_0 pin, it’s configuration with MODE_4 means an active low LED can be used on LED_0. The following list summarizes an RMII auto negotiate, 10 Mbps or 100 Mbps full duplex or half duplex:

-  MAC Interface = RMII

::

      *MACIF_SEL0 = MODE_1 = 10 kΩ pull-down resistor
      *MACIF_SEL1 = MODE_1 = 10 kΩ pull-down resistor

-  MDIX_MODE = automatic MDIX, preferred MDIX

   -  MDIX_MODE = MODE_3

-  PHY address = 0b0001
-  Speed selection = 10 Mbps, 100 Mbps with full duplex or half duplex, auto-negotiation enabled

   -  PHY_CFG0 = MODE_4 = 10 kΩ pull-up resistor

::

     *PHY_CFG1 = MODE_1 = 10 kΩ pull-down resistor 

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/rgmii_example.png
   :align: center

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/adin1200_magnetics_cmchoke.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/dp83822_magnetics_cmchoke.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/led.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/dp83822_table5.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/dp83822_table6.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/strapping.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/ksz_table7.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/dp83822_table8_9.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/ksz_table8.png
   :width: 600px
