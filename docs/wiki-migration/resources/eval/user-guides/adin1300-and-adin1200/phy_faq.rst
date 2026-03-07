ADIN1200/ADIN1300 Frequently Asked Questions
============================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/phy.jpg
   :align: center
   :width: 400px

Key Considerations when selecting an Industrial PHY
---------------------------------------------------

In automation applications there are a few critical features required to ensure high reliability and network resilience.

-  **Latency Performance** The network cycle time is the communication time required by the controller to both collect and update the data memories of all devices. A low latency PHY reduces network cycle time, improving network refresh time and allows more devices to the connected to the network. Many Industrial Ethernet Network topologies are typically LINE or RING, device connections requiring two ports for data in and out. This means PHY latency is doubled and therefore the impact of this specification can be very significant in determining the overall network cycle time. The ADIN1300 PHY has significantly lower latency compared to the competition 290ns Tx & Rx (RGMII)
-  **Robustness** to external radiated and conducted noise sources given the harsh operating environment. Select products who have been tested and adhere to EMI/EMC standards like CISPR 32, IEC 61000-4-2/4/5/6. This will prevent lengthy redesign cycles to secure certification later in the development flow. The customer evaluation board has been used for the various EMC tests to prove its robustness.
-  **Low Power** Devices in Industrial Applications are typically IP65/66 sealed from dust and moisture and therefore have restricted airflow and limited power dissipation capability. Similarly, devices are often exposed to high ambient temperature in industrial environments. Like the case for latency, 2 ports are needed for Line and Ring topologies and therefore 2 PHY’s so the effective is a doubling in the power dissipated for data In and Out. The ADIN1300 PHY offers on the order of 30% saving in power versus the competition with 330mW of power at 100% data throughput.

--------------

Differences between ADIN1200 & ADIN1300
---------------------------------------

The key differences are package size, speed, supply rails and feature set.


|image1|

--------------

Hardware Strapping Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PHYs hardware configuration pins allow user predefine the personality of the PHY for unmanaged applications. The features that can be configured by bootstrapping are as follows:

-  PHY Address
-  Forced/Advertised mode
-  PHY Speed
-  Software Powerdown Mode after Reset
-  Downspeed Enable
-  Energy Detect Powerdown Mode
-  EEE Enable
-  Auto-MDIX
-  MAC Interface Selection (RGMII/RMII/MII)
-  Review the datasheet section on Hardware configuration pins for full details.

Note that some pins use 4-level strapping (Mode 1-4), whereas other pins only use two level strapping (high & low). The PHY address pins use two level strapping.

--------------

MII 100M Latency
~~~~~~~~~~~~~~~~

The Latency in MII mode is a fixed number, dependent on clock cycles. There is no FIFO in MII and therefore no variation on this figure. For 1000M mode, there is a FIFO and there will be an 8ns uncertainty, this is captured in the datasheet latency specs.

--------------

Timing / Latency Maximum Receive Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Receive latency numbers quoted in Table 1 from the Datasheet are measured from start of data at MDI to the positive edge from RGMII.RXCLK. These are following the MDI to MII/GMII delay constraint definitions in Table 24-2/3 in IEEE Std 802.3 for 100BASE-TX and Table 40-14 for 1000BASE-T, extended to 10BASE-T and RMII/RGMII using the same reference points, i.e.

-  TX_EN/TX_CTL sampled with the rising edge of TX_CLK/TXC/REF_CLK to 1st bit/symbol on MDI

-  1st bit/symbol on MDI to RX_DV sampled with the rising edge of RX_CLK/RXC/REF_CLK

--------------

Resistor Values for Hardware pin config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The datasheet contains information on the recommended resistors to use on the various strapping pins. For the four level strapping resistor values of 10k/56k are recommended and chosen to minimize the power consumption from the resistor ladder. User could adjust the values of resistor if needed, but should retain similar ratio. User should also review if there is extra loading on each pin from external circuitry and adjust as needed. Note that some pins use 4-level strapping (Mode 1-4), whereas other pins only use two level strapping (high & low). The PHY address pins use two level strapping.

--------------

IO Voltage for MAC interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADIN1200 and ADIN1300 support VDDIO voltage range of 1.8V, 2.5V or 3.3V. Power consumption will increase with increased VDDIO voltage, see datasheet specifications for more details which includes plots showing typical data.

--------------

Typical Link time vs Speed
~~~~~~~~~~~~~~~~~~~~~~~~~~

Example Gigabit PHY Speed Configurations (assume local & remote node are configured the same):

-  Advertise All Speeds, Auto-Neg enabled, Auto-MDIX enabled .~4-5 sec
-  Advertise All Speeds, Auto-Neg enabled, Manual MDI/MDI-X.~3-4 sec
-  Force 1 Speed, Auto-Neg disabled, Manual MDI/MDI-X < 200ms

.. important::

   Forced Mode


Forced mode is always going to be the fastest mode to bring up a link. The auto-negotiation process is always going to take longer for the link to resolve. If user is sensitive to the link time, then forced mode is recommended.

--------------

Does the PHYs support JTAG?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, the ADIN1300 or ADIN1200 do not support JTAG

--------------

Any power sequencing requirements?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are no power up or down sequencing requirements.

--------------

Software tools for evaluation of the PHYs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using the ADI evaluation board with the ADuCM3029 MDIO interface dongle, there is an accompanying Software GUI which provides the user with easy access to all registers in the PHY and allows user do an initial evaluation of the part prior to developing own hardware and software. There is also a Linux driver for the ADIN1200 and ADIN1300, available in Linux mainline.

--------------

Exposed Paddle Keepout areas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The package has a standard exposed paddle, which should be soldered to the board for thermal reasons, ideally the solder pattern will have a full via array for best thermal performance. The extra exposed strips seen above and below the exposed padded are exposed bus bars, they are connected to internal voltages, so should not be grounded, there should be no vias directly underneath these areas, they should be treated as keepout areas. They do not need to be soldered down.

--------------

WoL (Wake on LAN)?
~~~~~~~~~~~~~~~~~~

WoL is primarily a MAC function. In a PC / LOM application a MAC-PHY is commonly used and WoL is implemented in the MAC-PHY and a processor / PC system can be put in a sleep mode and is woken by the receipt of a WoL packet.

Some PHYs include the detection of the magic packet so that the MAC can also be put in a sleep mode. The ADIN1300 does not include the magic packet detection function. In fact, WoL is not a low power mode from the PHY point of view as it still has to be up and is consuming power all the time, even in idle with no data transmission. An alternative approach and one that enables more efficient power consumption would be to use the PHY Energy Efficient Ethernet mode (EEE). If EEE is used, the link can be left in Gigabit EEE mode, the PHY power consumption is ~50 mW. So a significant saving vs Gb idle (330mW). Now when a packet is received, the PHY wakes up in 20 us (micro seconds) and wakes up the MAC. The MAC can process the packets to decide if a WoL packet and can wake up the system or ignore. A switch will usually only send packets destined for the device on that link. There will be occasional broadcast packets, so you will have some spurious wakes of the MAC, but overall the power should be lower using EEE than WoL.

--------------

SGMII interface?
~~~~~~~~~~~~~~~~

No, the ADIN1300 or ADIN1200 do not support SGMII interface. They supports MII, RMII & RGMII MAC interface modes.

--------------

C driver code for the PHYs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, currently we have a Linux driver which is available upstream in the kernel. Further detail around the driver is available on our :doc:`Wiki page </wiki-migration/resources/tools-software/linux-drivers/net-phy/adin>`

--------------

Conformance testing
~~~~~~~~~~~~~~~~~~~

Yes, UNH have performed conformance testing on our PHY test chip. In addition, we also performed internal testing using Tektronix TDSET compliance software. A summary report is available on request.

--------------

Back to back or repeater mode of operation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, when using the RGMII interface the PHY RX/TX are fully compatible, so they can be connected back to back. The only caution is to ensure to implement the internal delay on one side (typically the RX side for each side of link), this can be done either with hardware strapping or with a register write over the MDIO interface.

Note that the RMII PHY TX/RX interfaces are not functionally compatible, so cannot be connected back to back by default, instead a register write is required to support this mode of operation. Refer to the detail in the datasheet for specific details of the register involved.

--------------

IEEE1588 PTP support
~~~~~~~~~~~~~~~~~~~~

IEEE1588 enables high accuracy synchronization of clocks over Ethernet. To eliminate variability in the delay of timing packets between devices, PTP compliant Ethernet hardware records the time that PTP packets enter and exit the device and makes these time stamps available to PTP software, enabling the PTP application to use timing packets to accurately synchronize two clocks.

The ADIN1200 and ADIN1300 help to support IEEE1588 timestamping by providing start of packet indication to the MAC using hardware pins (programmable which pins). The PHYs do not timestamp the data directly. The MAC would timestamp based on the hardware pin indication from the PHY. Refer to the Start of Packet section in the PHY datasheets.

--------------

Synchronous Ethernet (SyncE)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, the ADIN1200 & ADIN1300 support Synchronous Ethernet. Synchronous Ethernet is the ability to output a clock synchronous to the recovered receive clock. A Master clock would exist at a local PHY in Gigabit Master mode. The remote PHY in Slave mode recovers the clock and outputs it on the GP_CLK pin. This clock source is then used to generate a local clock for any PHYs or switches beside this remote PHY. While SyncE is used in some applications, it has primarily been superseded by 1588.

--------------

Longer cable length?
~~~~~~~~~~~~~~~~~~~~

The ADIN1300 can support cable lengths up to 150 meters at Gigabit speeds and 180 meters when operating at 100 Mbps or 10 Mbps. The ADIN1200 supports cable lengths as long as 180m. Limited additional experimental data with the ADIN1200 suggests it can operate out to 210 meters (at 100 Mbps) over CAT5 cable with the default configuration settings.

--------------

1588 Start of Packet Programmable Delays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADIN1200 & ADIN1300 provide hardware pins for Start of Packet indication based on the SFD in the ethernet frame. This function is programmable in terms of which pins are used to provide the indication for Tx and Rx side. See datasheet for full detail on register programmability. One element of programmability is the delay

SopTxDelay Delay Register
^^^^^^^^^^^^^^^^^^^^^^^^^

The SopTxDel delay register is provided to align the TX_SOP signal on the chip pins to the TX SOP on the MDI pins. Jitter should be within ± 4ns by design for all speeds. Using TX_SOP makes more sense for the TX path since it would remove any variable PHY delays, which would happen depending on the speed/MAC interface mode, e.g., in the ADIN1300/1200:

-  In 1000BASE-T for any MAC interface (GMII/RGMII).
-  In 100BASE-TX and 10BASE-T for RGMII interface.

The recommended SopTxDel values (called out in the datasheet register documentation) would align the TX_SOP signal to the SOP signal on the MDI pins.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/soptx.png
   :align: center
   :width: 600px

SopRxDelay Delay Register
^^^^^^^^^^^^^^^^^^^^^^^^^

RX_SOP is less useful in general, since there is only a variable PHY delay in the RX path in ADIN1300/1200 when the RMII interface is used (100BASE-TX or 10BASE-T). In all other cases, there is no variable delay in the RX path, and therefore the SOP signal can be extracted at the MAC side. The timing between RX_SOP and the MAC side RX SOP (RX_DV=1, RXD = 0xD5) sampled on the rising edge of RX_CLK) would be fixed (See figure below). But since the RX MAC interface signals are synchronous to RX_CLK, while RX_SOP is not, the later would have to be re-synchronized to the MAC clock, so it might have in fact less precision (depending on the MAC implementation). The t1 value would be independent of the MAC interface (MII/GMII/RGMII/RMII). The values (from simulation) are:

- In 100BASE-TX: t1 = 260 ns - In 1000BASE-T: t1 = 212 ns The RX_SOP signal at the chip pin will have some additional delay, due to the internal routing and the I/O cell delay, which will be heavily dependent on the loading and PVT, estimate for that delay to be somewhere between 2 ns and 6 ns. The SopRxDel delay does not make so much sense in general for ADIN1200/1300. Given that the RX SOP on the MDI pins will happen before the RX_SOP signal on the chip pin, to align both signals (as done in the TX side), it would be required to advance the RX_SOP signal rather than delay it, but that is obviously not possible. Therefore, the SopRxDel delay was intended for a different purpose, it is provided for cases where there may be a very long latency in the MAC interface (for example if the PHY had an SGMII interface) to ensure that the RX_SOP signal is received at the MAC side during the corresponding frame, as if that was not the case it might cause problems.


|image2|

--------------

Voltage Mode Line Drive
~~~~~~~~~~~~~~~~~~~~~~~

The ADIN1200 & ADIN1300 are voltage mode with on chip terminations. Therefore, there is no need for external termination resistors from the center tap of the transformer to the supply as required in current mode line drivers. In addition to reducing components, Voltage mode driver also manifests a significant reduction in power consumption versus current mode.

When comparing PHY devices, ensure to check whether the output stage is voltage mode or current mode and also review whether the power consumption figures for current mode include the current dissipated in the transformer as a result of termination resistors.

--------------

Connecting a Cable to an Unpowered Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADIN1300 and ADIN1200 have internal protection circuitry on the MDI pins that will protect them from damage when standard ethernet traffic is sent into an unpowered device from a remote active device.

--------------

Do the Exposed Pad and Bus Bars have to be soldered down?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The LFCSP has an exposed pad underneath the package that must be soldered to the PCB ground for electrical, mechanical and thermal reasons. For thermal impedance performance and to maximize heat removal, use of a 4 × 4 array of thermal vias beneath the exposed ground pad is recommended.

There are also two bus bars on either side of the exposed pad, these bus bars are connected to internal voltage rails and are **not** intended to, and should **not** be soldered to the board. The PCB land pattern must incorporate the exposed ground paddle with vias and two keep out areas around the bus bars in the footprint. No PCB traces or vias can be used in either of the keep out areas. The EVAL-ADIN1300FMCZ uses an array of 4 × 4 vias on a 0.75 mm grid arrangement, as shown in the figure below. The via pad diameter dimension is 0.02 in. (0.5015 mm) and the finished drill hole diameter is 0.01 in. (0.2489 mm). This also applies to the exposed pad and bus bars for the ADIN1200. See the ADIN1200 Datasheet for the equivalent figure relating to the different package size.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/adin1300_paddle_and_keep_out_areas.png
   :align: center

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/phy_compare.jpg
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/soprx.png
   :width: 600px
