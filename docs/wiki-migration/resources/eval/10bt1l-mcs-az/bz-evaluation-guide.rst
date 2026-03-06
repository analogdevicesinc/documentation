EVAL-10BT1L-MCS IEEE 802.3cg SPoE Shield
========================================

Description
-----------

The EVAL-10BT1L-MCS-AZ/BZ is a 10BASE-TX, traditional 4-pair Ethernet, to 10BASE-T1L Single-pair Power over Ethernet (SPoE) media converter shield (MCS) that is compatible with the EVAL-LTC4296-1-KIT-AZ SPoE Power Sourcing Equipment (PSE) and the EVAL-LTC9111-AZ SPoE Powered Device (PD) evaluation boards. The EVAL-10BT1L-MCS-AZ shield has a power coupling network suited for Class 10 through 14 powers while the EVAL-10BT1L-MCS-BZ shield’s power coupling network is suited for the higher power levels of Class 15 and compatible with Class 10 through 14. In the context of a PSE, the power coupling network allows for power to be coupled on the single pair Ethernet lines. Regarding the PD, the power coupling network extracts power from the combined power and data line. The shield comes with the ADIN1100, 10BASE-T1L PHY, and the ADIN1200, 10BASE-TX PHY, which provide the Ethernet data media conversion in the system. The shield comes with the LT8301, isolated flyback converter, used to provide an isolated 3.3V power source to the PHYs.

**Design files for this circuit board are available from Analog Devices Applications**

BOARD PHOTO
-----------

.. container:: group

   
   .. container:: half column


   
   |image1|

         .. container:: centeralign

            \ *<fc #4682b4>Figure 1. EVAL-10BT1L-MCS-AZ (Class 10-14) </fc>*\

         

   
   .. container:: half column


         

   
   |image2|

         .. container:: centeralign

            \ *<fc #4682b4>Figure 2. EVAL-10BT1L-MCS-BZ (Class 15) </fc>*\

         

   


QUICK START PROCEDURE
---------------------

This quick start procedure shows how to connect the EVAL-10BT1L-MCS-AZ/BZ shield with either the EVAL-LTC4296-1-KIT-AZ or the EVAL-LTC9111-AZ motherboards. Follow the procedure below and refer to Figures 1 through 6, and Table 1 for proper equipment setup.

.. container:: group

   
   .. container:: half column

         
         Board Installation on EVAL-LTC4296-1-KIT-AZ
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         
         -  Select the EVAL-10BT1L-MCS shield version, -AZ or -BZ, for the intended max class at each port as shown in Table 1 and Figure 1.
         -  Verify all power supplies are off prior to installing or removing shield.
         -  Align the respective port’s shield headers over the headers on the EVAL-LTC4296-1-KIT-AZ motherboard. Push down firmly on the shield until all headers are flush. Verify no pins are sticking out.
         
         | 
         | **NOTE: The last two female pins of P1 (the longer connector) will be left floating. Refer Figure 4 for alignment of SPoE Shield. Powering the EVAL-LTC4296-1-AZ motherboard with a misaligned shield can cause damage to the system.**
         

   
   .. container:: half column

         
         Board Installation on EVAL-LTC9111-AZ
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

         | 
         
         -  Select the EVAL-10BT1L-MCS shield version, -AZ or -BZ, for the intended max class as shown in Table 1 and Figure 5.
         -  Verify all power supplies are off prior to installing or removing shield.
         -  Align the shield over the headers on the EVAL-LTC9111-AZ motherboard. Push down firmly on the shield until all headers are flush. Verify no pins are sticking out.
         
         |

         | **NOTE: The last two female pins of P1 (the longer connector) will be left floating. Refer Figure 6 for alignment of SPoE Shield. Powering the EVAL-LTC9111-AZ motherboard with a misaligned shield can cause damage to the system.**
         
      |

   


|

.. container:: centeralign

   \ *<fc #4682b4>Table 1. EVAL-LTC4296-1-AZ Board Default Port Class Configuration (See Figure 3) </fc>*\


+----------+--------------------+----------------------+----------------------+-------------------------------------+
| **PORT** | \**PORT CONFIGURED | MAX CLASS            | MAX CLASS            | SHIELD                              |
|          | CURENT LIMIT \*\*  | (SPoE Voltage = 24V) | (SPoE Voltage = 52V) |                                     |
+==========+====================+======================+======================+=====================================+
| 0        | 0.116A             | 10                   | N/A                  | <fc #ff0000>EVAL-10BT1L-MCS-AZ</fc> |
+----------+--------------------+----------------------+----------------------+-------------------------------------+
| 1        | 0.300A             | 11                   | 13                   | <fc #ff0000>EVAL-10BT1L-MCS-AZ</fc> |
+----------+--------------------+----------------------+----------------------+-------------------------------------+
| 2        | 0.775A             | 12                   | 14                   | <fc #ff0000>EVAL-10BT1L-MCS-AZ</fc> |
+----------+--------------------+----------------------+----------------------+-------------------------------------+
| 3        | 1.860A             | N/A                  | 15                   | <fc #f0e68c>EVAL-10BT1L-MCS-BZ</fc> |
+----------+--------------------+----------------------+----------------------+-------------------------------------+
| 4        | 0.775A             | 12                   | 14                   | <fc #ff0000>EVAL-10BT1L-MCS-AZ</fc> |
+----------+--------------------+----------------------+----------------------+-------------------------------------+

| 
| |image3|

.. container:: centeralign

   \ *<fc #4682b4>Figure 3. EVAL-LTC4296-1-KIT-AZ Port Shield Placements </fc>*\


| |image4|

.. container:: centeralign

   \ *<fc #4682b4>Figure 4. Alignment of an EVAL-10BT1L-MCS shield with the EVAL-LTC4296-1-AZ </fc>*\


| |image5|

.. container:: centeralign

   \ *<fc #4682b4>Figure 5. EVAL-LTC9111-AZ Shield Placement </fc>*\


   |image6|

.. container:: centeralign

   \ *<fc #4682b4>Figure 6. Alignment of an EVAL-10BT1L-MCS shield with the EVAL-LTC9111-AZ </fc>*\


DEMONSTRATION CIRCUIT EVAL-10BT1L-MCS-AZ/BZ
-------------------------------------------

| 

Shield Interface
~~~~~~~~~~~~~~~~

The shield’s headers interface and pinouts are shown in Figure 7 and Table 2 through 4.

In the case of the PSE, the shield will receive power from the PSE motherboard through headers J1 and J2 and deliver SPoE power and data via the SPoE connector. In the case of the PD, the shield will receive SPoE power and data at the SPoE connector and deliver power to the PD motherboard via the headers.

Additional connections to the PSE or PD motherboard at J3 are used for various signals, supply, and ground.

| |image7|
|

.. container:: centeralign

   \ *<fc #4682b4>Figure 7. Shield Header </fc>*\


|

.. container:: centeralign

   \ *<fc #4682b4>Table 2. J1 Pinout </fc>*\


+-----------------+-------------------------------------+-------------------------------+------------------------------+
| Pins            | Signal                              | Funciton with PSE Motherboard | Function with PD Motherboard |
+=================+=====================================+===============================+==============================+
| 1,2,3,4,5,6,7,8 | OUTM (Input/Output, PSE/PD Power -) | Connected to PSE output OUTM  | Connected to PD input OUTM   |
+-----------------+-------------------------------------+-------------------------------+------------------------------+
| 9,10            | Unused (tied together)              | DNC                           | DNC                          |
+-----------------+-------------------------------------+-------------------------------+------------------------------+

.. container:: centeralign

   \ *<fc #4682b4>Table 3. J2 Pinout </fc>*\


+-----------------+-------------------------------------+-------------------------------+------------------------------+
| Pins            | Signal                              | Funciton with PSE Motherboard | Function with PD Motherboard |
+=================+=====================================+===============================+==============================+
| 1,2,3,4,5,6,7,8 | OUTP (Input/Output, PSE/PD Power +) | Connected to PSE output OUTP  | Connected to PD input OUTP   |
+-----------------+-------------------------------------+-------------------------------+------------------------------+
| 9,10            | Unused (tied together)              | Tied to local ground          | Tied to local ground         |
+-----------------+-------------------------------------+-------------------------------+------------------------------+

.. container:: centeralign

   \ *<fc #4682b4>Table 4. J3 Pinout </fc>*\


+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Pins            | Signal                                                                                       | Funciton with PSE Motherboard                                                                                                                | Function with PD Motherboard                                                                       |
+=================+==============================================================================================+==============================================================================================================================================+====================================================================================================+
| 1,2             | MDIO (Input/Output, PHY Management Data I/O                                                  | (Pins(2,1) Connected to the motherboard’s micro-controller for respective port which is pulled to the local 3.3V via 3.3kΩ. Open drain line. | (Pins 2,1) Pulled up to the local 3.3V via 4.7kΩ. Open drain line.                                 |
+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| 3,4             | MDC (Input, PHY Management Data Clock)                                                       | (Pins 4,3) Connected to the micro-controller for respective port which is pulled to the local 3.3V via 3.3kΩ. Open drain line.               | (Pins 4,3) Pulled up to the local 3.3V via 4.7kΩ and tied to the microcontroller. Open drain line. |
+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| 5,6,9,10,13,14  | 3.3V (Input, sourced from motherboard)                                                       | (Pins 6, 5, 10, 9, 14, 13) Connected to the 3.3V filtered output voltage of the on-board buck regulator                                      | (Pins 6, 5, 10, 9, 14, 13) Connected to local 3.3V output voltage of the on-board buck regulator   |
+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| 7,8,11,12,15,16 | GND (non-isolated shield ground, common to motherboard)                                      | (Pins 8, 7, 12, 11, 16, 15) Connected to ground                                                                                              | (Pins 8, 7, 12, 11, 16, 15) Connected to ground                                                    |
+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| 17              | VSTBY_GATE (Version -AZ, reserved test point, not connected) NC (Version -BZ, not connected) | (Pin 18) Connected to ground                                                                                                                 | (Pin 18) Connected to the LTC9111 STBY pin                                                         |
+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| 18              | VSTBY (Test point for PD STBY, not connected)                                                | (Pin 17) Connected to local 3.3V                                                                                                             | (Pin 17) Connected to the LTC9111 STBY pin                                                         |
+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| 19              | INH (Version -AZ, not connected) NC (Version -BZ, not connected)                             | (Pin 20) Not connected                                                                                                                       | (Pin 20) Not connected                                                                             |
+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| 20              | PSE_PD# (Test point for PSE or PD motherboard, not connected)                                | (Pin 19) Connected to local 3.3V                                                                                                             | (Pin 19) Connected to ground                                                                       |
+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| 21              | VSNS2 (PD Power Interface (PI) Kelvin sense, connected to PI- through 1.1kΩ)                 | (Pin 22) Not connected                                                                                                                       | (Pin 22) Optionally connected to the LTC9111 VSNS1 pin for closer sensing at the PI                |
+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| 22              | VSNS1 (PD Power Interface (PI) Kelvin sense, connected to PI+ through 1.1kΩ)                 | (Pin 21) Not connected                                                                                                                       | (Pin 21) Optionally connected to the LTC9111 VSNS2 pin for closer sensing at the PI                |
+-----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+

NOTE: Pin 23 and 24 are not on the shield but are reserved for future use on the PSE and PD motherboards.

| 

EVAL-10BT1L-MCS-AZ (Class 10-14) Power Coupling Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the EVAL-10BT1L-MCS-AZ shield, the ADIN1100 (10BASE-T1L PHY) is coupled with SPoE class 10-14 power with the power coupling network shown in Figure 8.

The isolated coupled inductor (T1) provides the isolation between the PHY and the power interface. Capacitors C25 and C26 function as DC blocking capacitors. Their role is to ensure that only the AC component of the signal is propagated through. To help discharge these capacitors once power has been removed, resistors R87 and R88, which have high resistance, are placed in parallel. L3 serve as the common mode choke (CMC), which is used to reduce the high frequency common mode noise entering and exiting the power interface.

Differential mode inductors (DMI) L2 are responsible for the injection or extraction of power. It ensures that only DC power is injected or extracted, and no data is passed onto the PD or the PSE. The shields have options for using different DMIs as specified on the schematic. These inductors are selected to meet the droop, return loss, and mode conversion specification as defined in the IEEE 802.3cg. By default, the shield uses the Coilcraft MSD1278T-224KLB. This inductor has an inductance of 220uH which produces a compliant transmitter droop. If better transmission droop is required the MSD1278H-474KED, with an inductance value of 470uH can be used. On the other hand, if transmission droop is not a priority, the MSD1048H-104 inductor can be used (100uH).

The DMI on the EVAL-10BT1L-MCS -AZ of the shield is placed on the PHY side of the CMC. Placing the DMI on the PHY side, requires that the CMC be able to sustain class 10-14 current. This coupling network is not rated for class 15.

| |image8|

.. container:: centeralign

   \ *<fc #4682b4> Figure 8. Class 10-14 Power Coupling Network </fc>*\


EVAL-10BT1L-MCS-BZ (Class 15) Power Coupling Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the EVAL-10BT1L-MCS-BZ shield, the ADIN1100 (10BASE-T1L PHY) is coupled with SPoE class 15 power with the power coupling network shown in Figure 9.

The isolated coupled inductor (L1) provides the isolation between the PHY and the power interface. In the context of the EVAL-10BT1L-MCS -BZ shield, capacitors C65 and C66 act as the DC blocking capacitors, which ensure that only the AC component of the signal is propagated through. The high resistance discharging resistors for these capacitors are R1 and R10. The CMC (L5) is used to reduce the high frequency common mode noise coming in and out of the power interface.

The DMI (L9) is responsible for the injection or extraction of power. For the EVAL-10BT1L-MCS-BZ shield, the DMI is placed on the line (cable) side of the CMC (L5). As power does not pass through L5, this CMC can be designed to be significantly smaller than high current CMC options. Although there are high current-rated CMC options available, their larger size leads to increased leakage inductance, which could compromise the integrity of the data lines.

When the power coupling network is placed on the line-side, the power coupling network must include an extra CMC (L6) to limit the common mode noise going into the PSE or PD. In this configuration two capacitors (C60 & C61) with two resistors (R87 & R88) to ground are added to act as an AC short. Additionally, C64 and R89 form an RC network which is used to prevent the power coupling inductor from resonating at a frequency within the data band, which would cause the coupling inductor to look like an AC short.

The shield has options for using different DMIs as specified on the schematic. These inductors are selected to meet the droop, return loss, and mode conversion specification as defined in IEEE 802.3cg.


|image9|

.. container:: centeralign

   \ *<fc #4682b4> Figure 9. Class 15 Power Coupling Network </fc>*\


   | 

10BASE-T1L to 10BASE-T1 Media Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A 10BASE-TX data source is connected to the RJ45 magjack at J4. The data is then transferred to the ADIN1200, a 10BASE-TX Ethernet transceiver PHY. The ADIN1200 PHY interfaces with the ADIN1100, IEEE802.3cg 10BASE-T1L transceiver PHY, through a Reduced Media-Independent Interface (RMII). An external 50MHz clock at the REF_CLK pin is used for both transmit and receive at the RMII. The ADIN1100 PHY then passes single pair Ethernet data to get coupled with power before dispatching it to the SPoE connector at J5.

The configuration of the ADIN1100 is hardware-based. A pull-up resistor on the SWPD_ENB pin configures the ADIN1100 to not go into software power-down after reset. Another pull-up resistor on the MEDIA_CNV pin enables it to operate as a media converter. This allows the ADIN1100 to connect to a 10BASE-T PHY via either the RMII or RGMII interfaces. The ADIN1100 by default, with the MACIF_SEL0 and MACIF_SEL1 pins left floating, are in RMII mode.

The ADIN1200 has some hardware configurations on the shield. It is configured to go into software power-down mode after reset through the mode selection on LINK_ST and LED_0 pins. Pull-up resistors on the MACIF_SEL0 and MACIF_SEL1 pins configure the ADIN1200 for RMII mode. A pull-up resistor sets the MDIX_MODE pin to MODE_4, “Auto MDIX, Prefer MDI”.

The software configuration of the ADIN1200 is facilitated through the Management Data Input/Output (MDIO) interface. On both the PD and the PSE motherboards, their respective microcontroller interfaces at this MDIO. The configuration commands are relayed from the motherboard to the shield headers, and subsequently electrically isolated through the ADUM1251 isolator.

Through the ADIN1200’s MDIO, the execution of software commands enables the use of autonegotiation. Autonegotiation facilitates the exchange of information between the ADIN1100 and ADIN1200, enabling link partners to agree on the highest supported mode of operation. During the autonegotiation process, each PHY advertises its capabilities and compares them with those of the link partner.

To advertise 10BASE-T full duplex to the ADIN1100 PHY, 0x41 must be written to the Autonegotiation Advertisement Register (0x0004). The PHY must then be configured for media converter application which involves using Clause 22 access. This is done by specifying the Subsystem 10BASE-T Preamble Generation Register (0xFF38) to be accessed in the Extended Register Pointer Register (0x0010). Once this is set, all subsequent write and read operations to this register are performed through the Extended Register Data Register (0x0011). To configure for the media converter application, 0x0001 must be written to register 0xFF38 via register 0x0011. Lastly 0x1300 is written to the MII Control Register (0x0000) to set the speed of operation to 10Mbps, enable full duplex mode, restart the autonegotiation process, and enable the autonegotiation process.

After software configurations the ADIN1200 is configured out of the software power-down mode. The ADIN1200 then attempts to bring up links according to its media converter and autonegotiation configurations.

The pushbutton SW1 is used to reset both the ADIN1100 and the ADIN1200.

|

Connectors
~~~~~~~~~~

A 10BASE-TX data source such as an Ethernet switch, or Ethernet end device such as a security camera, is connected with a traditional CAT5 Ethernet cable to the Wurth Elektronic 7498011211 RJ45 magjack at J4. This RJ45 connector is equipped with built in 10/100BASE-T Ethernet transformers and two LED indicators. The green LED signifies the establishment of a valid link, while the yellow is solid when a valid link is established and blinks to indicate link activity.

Connector J5 of the shield is a Phoenix Contact (1803280) 3-position, terminal block header for single pair Ethernet (SPE) cable connection. This compact connector, measuring 12.82mm x 10.65mm x 9.2mm, has a low contact resistance of 1.3mΩ and can carry a nominal current of up to 8A, which is suitable for the SPoE current levels. It is rated for 160V and can withstand surge voltage of 2.5kV. Connector J5 mates with the Phoenix Contact 1803581, 3-position, screw terminal, female which can be installed by screwdriver on a single-pair Ethernet cable with optional cable shielding.

Table 4 shows the signal pinout of J5. Note the polarity of the power interface is inverted between the two shields.


| 
|

.. container:: centeralign

   \ *<fc #4682b4>Table 5. J5 SPE Connector Signal Pinout </fc>*\


======================= ====== ==== ============
\                       J5 Pin      
======================= ====== ==== ============
EVAL-10BT1L-MCS Version 1      2    3
-AZ                     OUTP   OUTM Cable Shield
-BZ                     OUTM   OUTP Cable Shield
======================= ====== ==== ============

Isolated Grounds and Supplies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-10BT1L-MCS-AZ/BZ shield features three distinct grounds: GND, GND_PHY, and GND_EARTH. Each ground is galvanically isolated from the other grounds.

GND is the common ground for SPoE and originates from the motherboard it is installed on, either from the LTC4296-1 or the LTC9111. The non-isolated 3.3V to the input of the LT8301 (isolated flyback), comes from the motherboard and is referenced to GND.

GND_PHY is the isolated ground reference for the PHYs. The isolated 3.3V generated from the LT8301 is referenced to GND_PHY and powers both PHYs.

GND_EARTH is an Earth ground plane on the EVAL-10BT1L-MCS-AZ/BZ, which can optionally connect via resistor(R49) and/or capacitor(C35) to the SPE cable shield (if the cable has a shield).

The shields feature an optional footprint for a 2010 resistor, R86 on the EVAL-10BT1L-MCS-AZ and R82 on the EVAL-10BT1L-MCS-BZ, which is across the isolation barrier between GND_EARTH and GND_PHY. A shunt resistor can be installed in this location if GND_EARTH and GND_PHY need to be tied together.


| 

Isolation Components
~~~~~~~~~~~~~~~~~~~~

The Isolated Coupled Inductor from TDK, ICI70CGI-222N, is used to provide the isolation between the PHY and the PI on both shields.

The ADUM1251 is used to isolate the Management Data Input/Output (MDIO) and Management data clock (MDC) from the shield PHYs to the microcontroller on their respective motherboard.

Additional filter components are placed across the isolation between the GND plane and GND_EARTH for common mode noise filtering.

|

Surge Components
~~~~~~~~~~~~~~~~

For ADIN1100 and ADIN1200 PHY protection at the Ethernet lines, an optional SP3051-04HTG TVS diode array is available at D1 and D5. This part integrates eight diodes and one Zener to protect the PHYs from ESD and high surge events.

Surge protection at the power interface is handled with the D55V0M1B2WSQ-7 bidirectional TVS diode on D6. If more robust surge protection is desired, the SMAJ54CA bidirectional TVS on D7 can be installed. A Gas Discharge Tube (GDT) on T2 provides a breakdown voltage on the line-to-line as well as line-to-ground on the SPE lines and GND_EARTH.

| 
| ==== Termination Components ==== Depending on customer’s requirements with isolation, C35 and/or R49 on the EVAL-10BT1L-MCS-AZ shield and C36 and/or R35 on the EVAL-10BT1L-MCS-BZ shield give the option of connecting the shield on the SPE cable to the GND_EARTH of the shield (if the SPE cable has a shield).

LTC9111 PD Input Kelvin Sense Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The LTC9111 measures its port voltage by default at the input of the EVAL-LTC9111-AZ motherboard via its R11 and R12 resistors. This measurement is desirable since the voltage is measured after the power coupling network which can filter out excessive ringing that can be observed directly at the connector during classification.

If voltage at the SPE connector of the shield is desired, R11 and R12 can be removed and R21 and R22 installed on the EVAL-LTC9111-AZ motherboard. This disconnects the Kelvin sense lines from the PD input and connects the Kelvin sense line to the shield headers. The Kelvin sense lines are then connected to the shield SPE connector through the shield’s R77 and R78 resistors. Optional capacitors (C55 and C56) are there for filtering.

| 
| |image10|

.. container:: centeralign

   \ *<fc #4682b4> Figure 10. Optional Componentry for EVAL-10BT1L-MCS-AZ </fc>*\


   |image11|

.. container:: centeralign

   \ *<fc #4682b4> Figure 11. Optional Componentry for EVAL-10BT1L-MCS-BZ </fc>*\


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/10bt1l-mcs-az/eval-10bt1l-mcs-az_shield_2.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/10bt1l-mcs-az/eval-10bt1l-mcs-bz_shield_2.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc4296-1-kit-az_top_shield_placement.jpg
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/10bt1l-mcs-az/alignment_of_an_eval-10bt1l-mcs_shield_with_the_eval-ltc4296-1-az_2.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc9111-az_top_shield_placement.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/10bt1l-mcs-az/ltc9111_shield_instalation.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/10bt1l-mcs-az/shield_header_2.jpg
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/10bt1l-mcs-az/class10_14_powercouplingnetwork_3.jpg
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/10bt1l-mcs-az/class15_powercouplingnetwork_3.jpg
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/10bt1l-mcs-az/optional_componentry_for_eval-10bt1l-mcs-az_3.jpg
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/10bt1l-mcs-az/optional_componentry_for_eval-10bt1l-mcs-az_2.jpg
