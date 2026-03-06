1. INTRODUCTION
===============

This user guide is an overview of the real-time Ethernet multiprotocol (REM) switch software driver usage. For details regarding available functions and their parameters, see the header files referenced in this user guide. The REM switch driver is designed to provide a standard, protocol independent interface (/Common/inc/REMS_Standard.h) used for initialization, interrupt management, timer management, and protocol independent packet transmission and receiving. Additional functionality is accessed through protocol specific interfaces, which are designed to support the software application-level stack of a particular industrial Ethernet protocol, such as REMS_PROFINET.h. The timer functionality provided by the REM switch is synchronized via an internal precision timer and can be used to capture external events or generate signals that are synchronized to a protocol specific timing function, such as parallel transmission control protocol (PTCP), IEEE 1588, and EtherCAT distributed clock, among others. Timer functions include the following: • Input capture, which time stamps a rising or falling edge on an external signal. • Output compare, which generates an edge on a chip output at a programmable time. The REM switch has many features dedicated to the protocol specific operation, including multiple transmit and receive queues, internal timer resources, and various interrupt events. The driver software manages these resources internally. It is assumed that the user is familiar with the REM switch hardware and has reviewed the fido5100/fido5200 data sheet.

TABLE OF CONTENTS
-----------------

Introduction 1 Revision History 2 Configuration 3 Driver Contents 3 Build Environment 4 Porting 4 Using the Driver 6 Standard Interface 6 Addressing Tables 11 Protocols 12 PROFINET 13 Synchronization (PTCP) 13 PROFINET Connection Establishment 13 RT Class 1 Connection Establishment 14 RT Class 3 Connection Establishment 14 IO Data Handling 15 Netload Filtering 18 Profinet Interrrupt Handling 19 EDDF Implementation 26 EtherNet/IP 33 EtherNet/IP Initialization 33 Handling PHY Link States 33 Handling CPU Interrupts 34 Low Priority TCP/IP Frame Receive and Transmit Processing 34 High Priority EtherNet/IP Class 1 Frame Receive and Transmit Processing 35 EtherNet/IP DLR Frame Receive and Transmit Processing 35 Other Considerations for DLR 36 Broadcast and Multicast Filtering 37 Modbus/TCP 38 Modbus/TCP Initialization 38 Modbus/TCP Interrupt Handling 38 Modbus/TCP PHY Link State Interrupt Handling 38 Modbus/TCP Received Packet Interrupt Handling 39 Modbus/TCP Packet Transmission 39 EtherCAT 40 EtherCAT Initialization 40 EtherCAT Interrupt Handling 40 EtherCAT Slave Stack to Driver Interface 42 MII Management Interface 42 EtherCAT SSC 43 POWERLINK 49 POWERLINK Initialization 49 POWERLINK Interrupt Handling 49 POWERLINK PHY Link State Interrupt Handling 51 POWERLINK Received Packet Interrupt Handling 51 POWERLINK Packet Transmission 51 Register Maps and Definitions 52 Direct Address Registers 59 Indirect Address Host Registers 62 Function Reentrancy 80 EtherCAT fido5200 Functional Differences from the Beckhoff ET1100 82 Prebuild Steps for the IAR Tool Chain 84 Considerations when Using Six or Seven FMMUs for the EtherCAT Driver 86

REVISION HISTORY

08/2022- Rev. L to Rev. M Changes to some of the overall format Changes to the Profinet Section. 3/2020—Rev. K to Rev. L Changes to Initialization Section 11 Changes to Interrupt Handling Section 18 Changes to EtherCAT Slave Stack to Driver Interface Section 20 Changes to SSC Changes Section 25

This Innovasic product user guide has been reformatted to the styles and standards of Analog Devices, Inc. 8/2018—Revision K: Initial Version

INTRODUCTION This user guide is an overview of the real-time Ethernet multiprotocol (REM) switch software driver usage. For details regarding available functions and their parameters, see the header files referenced in this user guide. The REM switch driver is designed to provide a standard, protocol independent interface (/Common/inc/REMS_Standard.h) used for initialization, interrupt management, timer management, and protocol independent packet transmission and receiving. Additional functionality is accessed through protocol specific interfaces, which are designed to support the software application-level stack of a particular industrial Ethernet protocol, such as REMS_PROFINET.h. The timer functionality provided by the REM switch is synchronized via an internal precision timer and can be used to capture external events or generate signals that are synchronized to a protocol specific timing function, such as parallel transmission control protocol (PTCP), IEEE 1588, and EtherCAT distributed clock, among others. Timer functions include the following: • Input capture, which time stamps a rising or falling edge on an external signal. • Output compare, which generates an edge on a chip output at a programmable time. The REM switch has many features dedicated to the protocol specific operation, including multiple transmit and receive queues, internal timer resources, and various interrupt events. The driver software manages these resources internally. It is assumed that the user is familiar with the REM switch hardware and has reviewed the fido5100/fido5200 data sheet.

TABLE OF CONTENTS

Introduction 1 Revision History 2 Configuration 3 Driver Contents 3 Build Environment 4 Porting 4 Using the Driver 6 Standard Interface 6 Addressing Tables 11 Protocols 12 PROFINET 13 Synchronization (PTCP) 13 PROFINET Connection Establishment 13 RT Class 1 Connection Establishment 14 RT Class 3 Connection Establishment 14 IO Data Handling 15 Netload Filtering 18 Profinet Interrrupt Handling 19 EDDF Implementation 26 EtherNet/IP 33 EtherNet/IP Initialization 33 Handling PHY Link States 33 Handling CPU Interrupts 34 Low Priority TCP/IP Frame Receive and Transmit Processing 34 High Priority EtherNet/IP Class 1 Frame Receive and Transmit Processing 35 EtherNet/IP DLR Frame Receive and Transmit Processing 35 Other Considerations for DLR 36 Broadcast and Multicast Filtering 37 Modbus/TCP 38 Modbus/TCP Initialization 38 Modbus/TCP Interrupt Handling 38 Modbus/TCP PHY Link State Interrupt Handling 38 Modbus/TCP Received Packet Interrupt Handling 39 Modbus/TCP Packet Transmission 39 EtherCAT 40 EtherCAT Initialization 40 EtherCAT Interrupt Handling 40 EtherCAT Slave Stack to Driver Interface 42 MII Management Interface 42 EtherCAT SSC 43 POWERLINK 49 POWERLINK Initialization 49 POWERLINK Interrupt Handling 49 POWERLINK PHY Link State Interrupt Handling 51 POWERLINK Received Packet Interrupt Handling 51 POWERLINK Packet Transmission 51 Register Maps and Definitions 52 Direct Address Registers 59 Indirect Address Host Registers 62 Function Reentrancy 80 EtherCAT fido5200 Functional Differences from the Beckhoff ET1100 82 Prebuild Steps for the IAR Tool Chain 84 Considerations when Using Six or Seven FMMUs for the EtherCAT Driver 86

REVISION HISTORY

08/2022- Rev. L to Rev. M Changes to some of the overall format Changes to the Profinet Section. 3/2020—Rev. K to Rev. L Changes to Initialization Section 11 Changes to Interrupt Handling Section 18 Changes to EtherCAT Slave Stack to Driver Interface Section 20 Changes to SSC Changes Section 25

This Innovasic product user guide has been reformatted to the styles and standards of Analog Devices, Inc. 8/2018—Revision K: Initial Version

Prior to initialization or use, certain system requirements must be met for the REM switch driver to operate properly. A complete list of system requirements is detailed in Table 1.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-1.png
   :align: center

DRIVER CONTENTS The REM switch driver is divided into the three subdirectories described in the Common section, the Porting section, and the Protocol Specific section. Common The common directory includes low level portions of the driver, as well as common types of functions, such as static table support and dynamic table management. Files of interest to the user are as follows: • inc/REMS_Standard.h, which is an interface to standard switch functions. • inc/REMS_Error.h, which contains error codes returned by driver routines. • inc/REMS_DynamicTable.h, which provides management of the switch dynamic forwarding table. • inc/REMS_StaticTable.h, which provides management of the switch static forwarding table. Porting The porting directory contains the files that must be modified to support a particular hardware platform. Nothing in this directory needs to be available to the application layer. Protocol Specific In the protocol specific subdirectory, a separate directory is provided for each supported protocol. Any given application depends on a single protocol. Available protocols are as follows: • PROFINET. Only the main PROFINET header must be accessed by the software application levels of the application. inc/REMS_PROFINET.h provides setup and operation of PROFINET functionality. • EtherNET/IP. Only the main EtherNet/IP header must be accessed by the software application levels of the application. inc/REMS_EthernetIP.h provides setup and operation of Ethernet/IP functionality. • Modbus/transmission control protocol (TCP). Only the main Modbus/TCP header must be accessed by the software application levels of the application. inc/REMS_ModbusTCP.h provides setup and operation of Modbus/TCP functionality. • EtherCAT. Two EtherCAT header files must be accessed by the software application levels of the application, as follows: • inc/REMS_ECATHw.h provides setup and operation of REM switch as an EtherCAT slave controller. • inc/REMS_ECATinternals.h sets the EtherCAT distributed clock synchronization offset parameter. All other header and source files are specific to the driver operation and organization and do not need to be accessed by software application levels of the application.

BUILD ENVIRONMENT When building the REM switch driver, the following directories must be on the included path: • REMS_Driver/Common • REMS_Driver/Porting • REMS_Driver/<ProtocolSpecificDirectory> ProtocolSpecificDirectory is the name of one of the supported protocols, such as PROFINET. Build a single protocol for a given project. For example, it is not possible to build a driver that supports both PROFINET and EtherCAT. When building the rest of the application using the REM switch driver, only the common and protocol specific subdirectories must be available. Some parameters are provided to enable debugging features and additional checks in the driver code. These parameters are as follows: • REMS_ENABLE_DEBUG. If defined, this parameter enables the error level debug macros embedded in the code. If REMS_ENABLE_DEBUG is set to 1, this parameter also enables informational printouts. For example, if the symbol is set on the compiler command line, the command code may look as follows: • -D REMS_ENABLE_DEBUG (generates error printouts) • -D REMS_ENABLE_DEBUG = 1 (generates error and informational printouts) • REMS_PARAMETER_CHECKS. If defined, this parameter causes the code to perform detailed checks on function parameters. Defining this parameter on a command line may look like -D REMS_PARAMETER_CHECKS. PORTING Because the driver has no dependencies on any operating system resources (such as no threading and semaphores), porting is limited to defining how the host processor communicates with the REM switch and some debugging options. All porting related code is located in the porting directory and found in the /Porting/inc/REMS_Port.h and /Porting/src/REMS_Port.c files. The porting/examples directory contains versions of these files that are specific to various processors. REMS_Port.h The REMS_DEBUG(), REMS_INFO(), and REMS_EVENT() debug macros may require platform specific customization. When enabled, these macros are used by driver code to display error and warning events. Calling printf() implements these macros. If printf() is not available, other logging mechanisms can be used. The following parameters in REMS_Port.h define the hardware environment in which the driver operates: • REMS_32_BIT_BUS. Define this parameter if the interface from the host processor to the REM switch is 32 bits wide. Otherwise, the driver assumes the interface is 16 bits wide. • REMS_LITTLE_ENDIAN_HOST. Define this parameter if the host processor uses little endian byte ordering for memory accesses. Otherwise, the driver assumes the host processor uses big endian byte ordering. • REMS_BASE_ADDRESS. This parameter must be set to the base address at which the REM switch is accessed, or the location of the external chip select in the memory map. • REMS_ADDR_SHIFT. This parameter indicates how far the address values are shifted depending on the size of the host processor data bus. The default operation of the driver is to work with byte addressable memory (REMS_ADDR_SHIFT = 0). If the memory bus addresses 16-bit words, set REMS_ADDR_SHIFT to 1. If the memory bus addresses 32-bit words, set REMS_ADDR_SHIFT to 2. If using separate address and data buses to communicate to REM, coordinate the setting of this parameter with the alignment of the address bus to address the input of the REM. If using a multiplexed address or data bus, this parameter can be used to adjust for the operation of the user bus processor. • \_SWAPL\_() and \_SWAPS\_(). Use these macros to swap bytes in limited cases when reading or writing packets. These macros are only used for control words, packet sizes, and time stamps, but not all packet data. Because the REM switch uses big endian internal organization, these macros have no effect on a big-endian host. If user processor has hardware support for endian swapping, rewriting the macros is possible. REMS_Port.c Typically, only the REMS_ReadBlock() and REMS_WriteBlock() functions in this file must be modified. REMS_ReadBlock() is used by the driver to read packet data from a first in, first out (FIFO) queue and REMS_WriteBlock() is used to write packet data to a FIFO queue. The sample processor example code is a simple C-language implementation for a 16-bit data bus. The sample processor can be easily adapted to a 32 bit bus by changing the short pointers to long pointers. If direct memory access (DMA) resources are available on the user processor, they can be used within REMS_ReadBlock() and REMS_WriteBlock(). USING THE DRIVER STANDARD INTERFACE Basic, protocol independent functionality of the REM switch is accessible through REMS_Standard.h. Driver Initialization When initializing the REM switch, first call REMS_StdInit(). REMS_StdInit() checks basic communication between the host processor and the REM switch, loads the protocol specific configuration to the device, defines the communication interface for the physical Ethernet layers (PHYs) (media independent interface (MII) and reduced media independent interface (RMII)), and identifies which of the REM switch interrupt outputs are associated with events of different priorities. If REMS_StdInit() returns REMS_OK, proceed to the next step. If REMS_OK is not returned, there is a communication error to the REM switch. After the REM switch is initialized, the media access control (MAC) addresses for the REM switch must be set. Either one or three MAC addresses are required, depending on the protocol. PROFINET requires a host MAC address for each port, whereas other protocols require a single host address. Call REMS_StdSetMacAddress() to call the MAC addresses. Interrupts The REM switch supports up to three separate interrupt lines. While fewer lines may be used, use of all three interrupt lines yields the best performance on protocols with critical timing. The interrupt events supported by the device and driver are defined in REMS_Standard.h in the REMS_StdIntEvent_t enumerated type. Additional interrupt events from the device are handled directly by the driver. The REM switch hardware and driver are compatible with either edge triggered or level sensitive interrupts. Interrupts are configured using the following routines: • REMS_StdAssignInterrupt() determines the line and priority for an interrupt event. • REMS_StdEnableInterrupt() enables an interrupt event. • REMS_StdDisableInterrupt() disables an interrupt event. Hardware events in REMS_StdIntEvent_t are available for use. Protocol specific events are typically generated by the driver based upon the occurrence of events more complex than those in REMS_StdIntEvent. Protocol specific events are already enabled or disabled and are already assigned to a particular interrupt line by the driver when firmware is loaded. To define interrupt handlers for the various priorities, use a structure similar to the following. The specific handler syntax varies depending on user environment. /\**\* Handle REM Switch Interrupt Line 0. \***/

\__attribute [1]_) void LEASHstandardExternalInt0() {

::

   volatile unsigned long ack;
   /* acknowledge the interrupt */
   ack = *FIDO_INTCONTROLCH0;

::

   HandleIntREMS(REMS_Int_Line_0);

} Interrupt Line 1 and Interrupt Line 2 use similar handler syntaxes, with the difference being that Line 1 and Line 2 take the place of Line 0. The main handler routine functions regardless of how interrupt events are allocated across the interrupt lines and may appear as follows: static void HandleIntREMS(REMS_IntLine_t line) {

::

   REMS_stdIntEvent_t event;
   unsigned short status;

::

   /* Have driver read interrupt events from REM and queue them up locally */
   REMS_StdEvaluateInterrupt(line);
   do {
     /* read events from the local queue one at a time */
     event = REMS_StdGetNextEvent(line);

::

     switch (event) {
     case REMS_StdInt_Port_1_LinkChange:
       port = REMS_enetPort_1;
       AddToQueue(linkManagementQueue_g, &port, WAIT_FOREVER);
       break;

::

     case REMS_StdInt_Port_2_LinkChange:   port = REMS_enetPort_2;
       AddToQueue(linkManagementQueue_g, &port, WAIT_FOREVER);
       break;

::

     case REMS_StdInt_PktReady:
       /* handle a packet received on the low priority queue,
   * pass it to the TCP/IP stack */
       REM_ReceivePacket();
       break;

::

     case REMS_StdInt_Capture_0:
       /* handle timer capture events … */
       break;
     case REMS_StdInt_Capture_1:
       break;
     case REMS_StdInt_Capture_2:
       break;
     case REMS_StdInt_Capture_3:
       break;
       /* handle timer output compare events */
     case REMS_StdInt_Compare_0:
       break;
     case REMS_StdInt_Compare_1:
       break;
     case REMS_StdInt_Compare_2:
       break;
     case REMS_StdInt_Compare_3:
       break;
       /* Handle periodic timer events (TCU) */
     case REMS_StdInt_TimerControl_0:
       break;
     case REMS_StdInt_TimerControl_1:
       break;
     case REMS_StdInt_TimerControl_2:
       break;
     case REMS_StdInt_TimerControl_3:
       break;

::

     /* Protocol-specific interrupt events */    /*...*/
     default:
       break;
     }
   } while (event != REMS_Int_None); /* handle all outstanding events */

Handle Link Change Interrupt The below example provides an example of how to manage REMS_StdInt_Port_1_LinkChange and REMS_StdInt_Port_2_LinkChange interrupts. In the previous example, the link change event as well as port number were added to a queue. In this separate thread the queue is evaluated and the necessary actions for each event and port are taken: queue linkManagementQueue_g;

/\* Used to save link event data and provide to IP stack;

-  interface ID, link up/down, port of link event, interface speed, duplex mode

\*/ linkEventInfo_t linkEvent_g

/\* Enum; provides speed and duplex mode per port \*/ linkState_t portSpeedDuplex_g[NUM_DEVICE_PORTS];

/\* Used to save PHY config parameters for external use; auto-negotiation status, speed, duplex mode, mdi crossover settings \*/ phyConfig_t phyConfig_g[]

void HandleLinkChange(void \*param) {

::

   EthLinkStatus_t linkUp;
   REMS_SpeedDuplex_t REMSspeedDuplex;
   REMS_CommonEnetPort_t port;
   uint8_t partnerAutoNegState;

::

   do{
     RemoveFromQueue(linkManagementQueue_g, &port, WAIT_FOREVER);

::

     // set event notification interface index
     linkEvent_g.interfaceIdx = ifHandle_g;
     // determine the PHY address and type
     if(port == REMS_enetPort_1){
       linkEvent_g.port = macPort0;
     }else if(port == REMS_enetPort_2){
       linkEvent_g.port = macPort1;
     }

::

     // Get the link status from REMS
     linkUp = REMS_StdGetLinkState(port);

::

     // Perform an edge detect on link up/down
     if((linkUp == LINK_UP) &&
        (portStatus_g[port-1] == LINK_DOWN))
     {
       /* Link went up */
       linkEvent_g.link = true;

::

       // Get the speed and duplex from the PHY

::

       // Get the link partner auto-negotiation state

::

       if((partnerAutoNegState == LINK_PARTNER_FORCED) &&
          (phyConfig_g[port-1].autoNegEnable)) {
         /*Set Phy Duplex mode; For Profinet, fall back to full duplex mode if auto-
          negotiation fails*/

::

         // Save full duplex mode at port status variable
         // portSpeedDuplex_g[port-1] = duplexMode
       }

::

       // Tell REMS what the new link settings are
       switch(portSpeedDuplex_g[port-1]){

::

       /*...*/
       case LinkState100BaseTxFd:
         REMSspeedDuplex = REMS_100_Full_Duplex;
         linkEvent_g.duplex = phyDuplexModeFull;
         linkEvent_g.speed = phySpeed100;
       break;

::

       /*...*/
       }

::

       // Set REMS' speed and duplex
       REMS_StdSetSpeedAndDuplex(port, REMSspeedDuplex);
       // Set the port state to forwarding
       REMS_StdSetPortState(port, REMS_PORT_FORWARDING);

::

       // Update PHY configuration settings if auto-negotiation enabled 
       if (phyConfig_g[port-1].autoNegEnable) 
       {
         phyConfig_g[port-1].speed = linkEvent_g.speed;
         phyConfig_g[port-1].duplexMode = linkEvent_g.duplex;
       }

::

       // Store the port link status for the next go 'round and so others can see it
       portStatus_g[port-1] = linkUp;

::

       // Last thing publish the link up event to all other subsystems
       PublishEvent(LINK_UP);

::

     }else if((linkUp == LINK_DOWN) &&
        (portStatus_g[port-1] == LINK_UP))
     {
       /* link went down */

::

       /* check opposite port to determine there is a link on either port */
       if (portStatus_g[(((port-1) == 0)? 1:0)] == LINK_DOWN)
         linkEvent_g.link = false;
       else
         linkEvent_g.link = true;

::

       // Read the PHY status register to unlatch the link status bit

::

       // Shut the port down since there is no link
       REMS_StdSetPortState(port, REMS_PORT_OFF);
       
       // Flush the dynamic table on link down
       REMS_FlushDynamicTable();

::

       // Publish the link down event
       linkEvent_g.duplex = phyDuplexUnknown;
       linkEvent_g.speed = phySpeedUnknown;

::

       // Update PHY configuration settings if auto-negotiation enabled
       if (phyConfig_g[port-1].autoNegEnable) {
         phyConfig_g[port-1].speed = linkEvent_g.speed;
         phyConfig_g[port-1].duplexMode = linkEvent_g.duplex;
       }

::

       // Store the port link status for the next go 'round and so others can see it
       portStatus_g[port-1] = linkUp;

::

       // Last thing publish the link down event to all other subsystems
       PublishEvent(LINK_DOWN);
     }

::

   }while (1);

}

Note: A separate thread is provided to handle the link change event, to keep runtime during ISRs short. Also in the case for PROFINET a call to eddf_interrupt(), which follows the publishing of link down and up events, may not be called from an ISR context.

Packet Transmission and Receiving REMS_Standard.h provides an interface by which to transmit and receive packets over the lowest priority queue. This interface leaves the higher priority queues open for protocol specific traffic. The transmit interface allows the user to determine the port from which the packet transmits and the receive interface indicates on which port a packet was received. These interfaces, in conjunction with the static forwarding table, allow the use of protocols such as link layer discovery protocol (LLDP), rapid spanning tree protocol (RSTP), and media redundancy protocol (MRP). As noted in the Porting section, the routines that read and write packet data to and from the REM switch can be customized to take advantage of DMA resources on the host processor. Synchronized Timer Signals The timer control unit (TCU) controls the external timer signals on the REM switch. These signals come directly from the REM switch. They are also synchronized directly to the network. The TCU can be called using the functions REMS_StdGetTcuTimersAvailable() and REMS_StdSetTcuIoParams(). Both functions allow the TCU to generate a timer signal that fits the needs of the system. Both functions are defined in REMS_Standard.h. REMS_StdGetTcuTimersAvailable() is used to get the number of TCU timer signals that are available to the application. REMS_StdSetTcuIoParams() allows the user to specify parameters for the timer in use. Call this function to set pulse parameters on the indicated timer channel. ADDRESSING TABLES Static Forwarding Table The static forwarding table is used to manage the handling of packets with a multicast destination MAC address. The interface for managing the table is located in REMS_StaticTable.h. By default, the REM switch forwards any multicast packet from the receiving Ethernet port to the other Ethernet port but does not forward the packet to the host processor. The user can add a specific multicast MAC address to the static table to alter the forwarding of the multicast packet. REMS_AddStaticTableEntry() defines the rule to apply to packets with a given address, and also indicates whether the packets override port state settings. The static forwarding table also provides functions to remove an entry and to flush all entries from the table. The number of entries in the static forwarding table varies by protocol, as shown in Table 2. The static forwarding table only applies to packets received from an Ethernet port.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-2.png
   :align: center

Dynamic Forwarding Table
~~~~~~~~~~~~~~~~~~~~~~~~

The dynamic forwarding table is used to manage the handling of packets with a unicast destination MAC address. This table operates automatically and does not require input from the application. A common operation for the dynamic forwarding table is to change the aging time for entries in the table, which affects how long a forwarding rule for an address stays in the table without being refreshed by a packet received from that address. The dynamic forwarding table is also often used to flush the table on a network topology change. These functions, along with the ability to add or delete an address in the table, are available in REMS_DynamicTable.h. The current dynamic table implementation allows aging time between 12 sec to 12 minutes. The dynamic forwarding table is set to 512 items by default and is not used by EtherCAT. PROTOCOLS At the time of this release of the driver, the supported protocols are EtherCAT, PROFINET, Modbus/TCP, Ethernet/IP, and POWERLINK. These are described in the PROFINET section, the EtherNet/IP section, the Modbus/TCP section, the EtherCAT section, and the POWERLINK section.

PROFINET The current version of the driver supports a relative forwarder device of Version 2.3 of the PROFINET Specification, Conformance Class B. Manage the standard setup of the TCP/IP stack as usual. LLDP and discovery and configuration protocol (DCP) packets are relayed to the host via the low priority queue, which is interfaced through REMS_Standard.h. The integrator must differentiate traffic as necessary. The interface for input/output (I/O) data is described in the RT Class 1 Connection Establishment section and the RT Class 3 Connection Establishment section. The PROFINET REM Switch driver also provides the ability to support System Redundancy. This has an implication that there must be multiple connections to the PROFINET device. The PROFINET driver supports up to 4 Application Relations (ARs)/Connections.

SYNCHRONIZATION (PTCP ) Precision Time Control Protocol (PTCP) line delay and synchronization traffic is handled entirely by the driver. Most parameters are dependent on the specifics of the connection process. Ensure that the PROFINET transmit and receive delay values of the device are set at initialization time. Ensure that these are the same delay values advertised in the GSDML file of the device and in LLDP packets transmitted by the device. These delay values are constants for a particular hardware design, which are dependent on the PHYs chosen. The receive value represents the time between the arrival of a packet on the cable side of the receive PHY and the time stamp in the REM switch. The transmit value represents the time between the time stamp in the REM switch device and the packet being transmitted on the cable side of the PHY. PHYs targeting the PROFINET IRT market include estimates of this timing in the respective device datasheet. Some adjustments must be made to the PHY values to account for timing within the REM switch. The PHY transmit delay takes an additional 64 ns in the REM switch, and the receive delay in the REM switches 8 ns less than the PHY receive delay. Use the REMS_pnetSetDelayValues() function to provide these values to the driver. After the delay values are set, call REMS_syncStartBridge(). Calling this function initializes the basic message processing and data structures for line delay calculation and synchronization.

Line delay processing takes place without intervention from the software application levels. Either based on parameters from nonvolatile memory or data provided in the connection request, call REMS_syncStartSlave() when appropriate. This function provides the parameters necessary for the driver to validate synchronization packets and synchronize to the proper master. At this point, the driver begins the process of synchronization. The following functions are useful to the software application levels: • REMS_syncCableDelay() returns the calculated cable delay per port in LLDP packets. • REMS_getSyncMasterAddr() returns the MAC address of the synchronization master for presentation as master in LLDP packets. • REMS_getPeerDelays() returns the transmit and receive delays of the peer per port for presentation as master in LLDP packets. The following events are generated through the interrupt interface to inform the software application levels of changes to the synchronization state: • REMS_PnetInt_Sync indicates that the local machine is synchronized with the master. • REMS_PnetInt_Wrong_Sync_Master indicates that a synchronization packet has been received from the wrong master, which does not affect the synchronization state. • REMS_PnetInt_Master_Lost indicates that a preliminary timeout occurred, and the machine enters the tsync state, which is a state in the PROFINET specification. • REMS_PnetInt_No_Sync_Message_Received indicates that the machine timed out and is no longer synchronized. • REMS_PnetInt_Jitter_Out_Of_Boundary indicates that the difference between local time and the time in the received synchronization packet is too great, and that the machine is no longer synchronized. PROFINET CONNECTION ESTABLISHMENT REMS_pnetConnectionStart() must be called when a connect.req frame is received, indicated by a call to the callback function PNIO_cbf_ar_connect_ind() This function provides the driver with the MAC address, application relation (AR) type, and start up mode of the I/O controller necessary for a connection. The application then must initialize a provider protocol machine (PPM) and consumer protocol machine (CPM). The REMS_PnetPpmInsert() and REMS_PnetCpmInsert() functions are provided for PPM and CPM initialization. There is no order requirement, when initializing the PPM and CPM. To start the PPM, call REMS_PnetPpmStart(). If the connection is closed for any reason, such as a consumer watchdog timeout, the PPM and CPM must be removed using the REMS_PnetPpmRemove() and REMS_PnetCpmRemove() functions, respectivelyCPM and PPM initialization, startup and removal are currently handled by the PN-Stack via the EDDF in their respective files (eddf_crt_cons.c and eddf_crt_prov.c). In order to provide the PN-stack with new IP parameters, use \`PNIO_change_ip_suite()\`-function, when your IP-Stack provides new parameters. The PROFINET stack also needs to be notified of link change events (see chapter Handle Link Change Interrupt). To notify the PN Stack provide something similar to the following:

void HandleEvent(int eventIndex){

::

   switch (event) {
     /* ... */

::

     case (LINK_UP):
     case (LINK_DOWN):
       pDDB = &g_EDDF_coreDev;
       if (!pDDB->Core.Isr.Active) {
         // Save link indication, if PN Stack is not yet ready
         PNET_linkIntFired_g = 1;
       }
       else {
         eddf_interrupt(pDDB->hDDB, EDDF_INT_STATUSCHANGE);
       }
     break;

::

     /* ... */
   }

}

Note: Calls to eddf_interrupt(), which follow the publishing of link down and up events, or reception of NRT packets from Queue1 (see Acyclic Message Reception) may not be made from an ISR context. Therefore make sure to provide one or more separate threads, from which the call to eddf_interrupt() is issued. RT CLASS 1 CONNECTION ESTABLISHMENT For a PROFINET RT Class 1 connection, there are no additional parameters required. The application must only call REMS_PnetUserDataValid() when the device is ready to send the ApplicationReady.req frame, e.g. after the PN CPU is finished with parameterization of the PN Device, indicated by PNIO_cbf_param_end_ind(), if parameter MoreFollows is set to false. Additionally, a call is required after the PN CPU issues a READY FOR INPUT UPDATE event (PNIO_cbf_ready_for_input_update_ind()). When support for Legacy Startup Mode is required, check the startup mode via startMode_g in PNIO_cbf_ar_connect_ind() and issue a call to REMS_PnetUserDataValid().

RT CLASS 3 CONNECTION ESTABLISHMENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a PROFINET RT Class 3 connection, the application must call REMS_IrBeginEnddata_PortAssignment() for both ports when the PDIR data index Write.req frame is received. The application can then call REMS_pnetUserDataValid() when the device is ready to send the ApplicationReady.req frame. The application also manages the RT_Class_3 port state machine. Use the REMS_pnetSetPortRedState() function to set the switch port state to off, up, or run to match the LLDP frames. Finally, call REMS_pnetReadyForRTClass3 when the device is fully synchronized and ready for a Class 3 connection.

IO DATA HANDLING
~~~~~~~~~~~~~~~~

The IOM can be used to set up buffers for the Communication Relation and communicate them to the PN-Stack and the REMS driver. PNIOD_PLATFORM_SLATER or PNIOD_PLATFORM_ECOS_FIDO defines are used to set up the calls to the functions defined for use with FIDO. An example implementation of the IO-Management can be found in iom_swif.c, which can be adjusted for the necessary platform. IOM can handle setup, initialization and access to the buffers required. iom_swif_init() and iom_swif_allocate_iocr_memory() are used to initialize the buffers and provide the necessary sizes for each relevant AR. The REMS driver currently supports four different ARs, therefore four provider buffers can be set up. Consumer buffers are supposed to be doubled, to allow for swapping the active, to be written to, buffers. While the REMS driver writes received data to one buffer, the PN-Stack is able to work with the second provided buffer. In general, the REMS driver is provided with buffers for cyclic data exchange during REMS_PnetCpmInsert() and REMS_PnetPpmInsert() calls. Provide both CPM and PPM with the buffers initialized by IOM. The consumer buffer is expected to be swapped after each reception of new data, which is currently handled by the PN-Stack in EDDF_CRTScoreboardHandler()(iom_swif_swap_cpm_buffer() is called by EDDF_CRTScoreboardHandler()). iom_swif_consumer_lock() and iom_swif_provider_lock() are used throughout the PN-Stack to access the locations of CPM and PPM buffers. The locking feature of the critical sections of these functions can be ignored as of now. Important: Make sure to provide buffers with a minimum size of 40 bytes. Smaller buffer sizes lead to mangled messages as the REMS driver expects the minimum size of 40B for REMS_WritePacket(). To safely readout CPM data, retrieve e.g. the primary AR ID, retrieve the relevant buffer with a call to iom_consumer_lock(). The PNPB (PROFINET IO device user interface for the customer application) provides the offset of the cyclic data inside the IOM buffer, as well as data length. During readout also do provide the PNPB with the current APDU status: int32_t PNET_ReadItem(int32_t itemID, void \*data_p) {

::

   int32_t rv = (PNIO_NOT_OK); // IO data invalid
   LSA_UINT8* cpmDataBuf_p;
   iom_apdu_status_t* apduStatus_p;
   PNIO_EXP_SUB*  pExpSub;
   LSA_UINT16 arIdx;

::

   //get primary AR
   arIdx = iom_swif_get_session_prim_ar_idx();

   if (itemID >= PnpbExp[arIdx].NumOfPluggedSub)
     // Controller hasn't plugged in the submodule associated with this item
     // so report back there's no valid output data for it
     return (PNIO_NOT_OK);

   // get pointer to IOCR buffer and APDU status (including cycle counter and status bits)
   iom_consumer_lock((void*)&cpmDataBuf_p, &apduStatus_p, arIdx);

::

   if (cpmDataBuf_p == NULL)
   {
     OsExitX (OS_MUTEX_PNPB_IO);
     OS_INSTRUMENT_USER_STOP(0xAA, 5678);
     return (PNIO_NOT_OK);
   }

::

   // Provide PNPB with APDUStatus
   OsMemCpy(&PnpbExp[arIdx].LastApduStat, apduStatus_p, 4);

::

   pExpSub = &(PnpbExp[arIdx].Sub[itemID]);
   if (pExpSub->OwnSessionKey)
   { // AR is submodule owner
     if (pExpSub->IoProp & PNIO_SUB_PROP_OUT)
     {
       if (pExpSub->isPlugged)
       {
         // Readout data from IOM buffer to provided data pointer
         OsMemCpy(data_p, cpmDataBuf_p + pExpSub->Out.data_offset, pExpSub->Out.data_length);
         rv = (PNIO_OK); // IO data valid
       }
       else
       {
         pExpSub->Out.iocs_val = PNIO_S_BAD;
       }
       /* save remote producer state */
     }
     if (pExpSub->IoProp & PNIO_SUB_PROP_IN)
     {
       /* save remote consumer state */
       pExpSub->In.iocs_val = *(cpmDataBuf_p + pExpSub->In.iocs_offset);
     }
   }
   else
   { // AR is not submodule owner
     if (pExpSub->IoProp & PNIO_SUB_PROP_IN)
     { // save remote consumer state
       pExpSub->In.iocs_val = PNIO_S_BAD;
     }
   }

::

   // **** free pointer to IOCR buffer ***
   iom_consumer_unlock(arIdx);

::

   return rv;

}

Similarly proceed when writing data items and additionally provide items with their current IOPS value: int32_t PNET_WriteItem(int32_t handle, void \*data_p) {

::

   LSA_UINT8* ppmDataBuf_p;
   PNIO_EXP_SUB* pExpSub;
   LSA_UINT16 arIdx;

::

   arIdx = iom_swif_get_session_prim_ar_idx();

   if (handle >= PnpbExp[arIdx].NumOfPluggedSub)
     // Controller hasn't plugged in the submodule associated with this item
     // so just return OK since there's no buffer slot for it
     return (PNIO_NOT_OK);

   iom_provider_lock((void*)&ppmDataBuf_p, arIdx);
   pExpSub = &(PnpbExp[arIdx].Sub[handle]);

::

   //provide io data and iops from input submodule
   if (pExpSub->OwnSessionKey && pExpSub->isPlugged)
   {
     if (pExpSub->IoProp == PNIO_SUB_PROP_NO_DATA)
     { // ** submod has no IO data **
       // *** update (input-)provider state in input frame ***
       if ((!pExpSub->IsWrongSubmod) && pExpSub->ParamEndValid)
         *(ppmDataBuf_p + pExpSub->In.iops_offset) = pExpSub->In.iops_val;
       else
         *(ppmDataBuf_p + pExpSub->In.iops_offset) = PNIO_S_BAD;
     }
     else
     {
       if (pExpSub->IoProp & PNIO_SUB_PROP_IN)
       {  // ** submod has input data **
           // *** update (input-)provider state in input frame ***
         if ((!pExpSub->IsWrongSubmod) && pExpSub->ParamEndValid)
         {
           OsMemCpy(ppmDataBuf_p + pExpSub->In.data_offset, data_p,
                    pExpSub->In.data_length);
           *(ppmDataBuf_p + pExpSub->In.iops_offset) = pExpSub->In.iops_val;
         }
         else
         {
           *(ppmDataBuf_p + pExpSub->In.iops_offset) = PNIO_S_BAD;
         }
       }
       if (pExpSub->IoProp & PNIO_SUB_PROP_OUT)
       { // ** submod has out put data **
         if ((!pExpSub->IsWrongSubmod) && pExpSub->ParamEndValid)
           *(ppmDataBuf_p + pExpSub->Out.iocs_offset) = pExpSub->Out.iocs_val;
         else
           *(ppmDataBuf_p + pExpSub->Out.iocs_offset) = PNIO_S_BAD;
       }
     }
   }
   else // submod not owned or not plugged
   {
     if (pExpSub->IoProp == PNIO_SUB_PROP_NO_DATA)
     { // ** submod has no data **
       *(ppmDataBuf_p + pExpSub->In.iops_offset) = PNIO_S_BAD;
     }
     else
     {
       if (pExpSub->IoProp & PNIO_SUB_PROP_IN)
       { // ** submod has input data **
         OsMemSet((void*)(ppmDataBuf_p + pExpSub->In.data_offset), 0x00,
                  pExpSub->In.data_length);
         *(ppmDataBuf_p + pExpSub->In.iops_offset) = PNIO_S_BAD;
       }
       if (pExpSub->IoProp & PNIO_SUB_PROP_OUT)
       { // ** submod has out put data **
         *(ppmDataBuf_p + pExpSub->Out.iocs_offset) = PNIO_S_BAD;
       }
     }
   }

::

   iom_provider_unlock(arIdx);

::

   return (PNIO_OK);

}

IO DATA HANDLING The IOM can be used to set up buffers for the Communication Relation and communicate them to the PN-Stack and the REMS driver. PNIOD_PLATFORM_SLATER or PNIOD_PLATFORM_ECOS_FIDO defines are used to set up the calls to the functions defined for use with FIDO. An example implementation of the IO-Management can be found in iom_swif.c, which can be adjusted for the necessary platform. IOM can handle setup, initialization and access to the buffers required. iom_swif_init() and iom_swif_allocate_iocr_memory() are used to initialize the buffers and provide the necessary sizes for each relevant AR. The REMS driver currently supports four different ARs, therefore four provider buffers can be set up. Consumer buffers are supposed to be doubled, to allow for swapping the active, to be written to, buffers. While the REMS driver writes received data to one buffer, the PN-Stack is able to work with the second provided buffer. In general, the REMS driver is provided with buffers for cyclic data exchange during REMS_PnetCpmInsert() and REMS_PnetPpmInsert() calls. Provide both CPM and PPM with the buffers initialized by IOM. The consumer buffer is expected to be swapped after each reception of new data, which is currently handled by the PN-Stack in EDDF_CRTScoreboardHandler()(iom_swif_swap_cpm_buffer() is called by EDDF_CRTScoreboardHandler()). iom_swif_consumer_lock() and iom_swif_provider_lock() are used throughout the PN-Stack to access the locations of CPM and PPM buffers. The locking feature of the critical sections of these functions can be ignored as of now. Important: Make sure to provide buffers with a minimum size of 40 bytes. Smaller buffer sizes lead to mangled messages as the REMS driver expects the minimum size of 40B for REMS_WritePacket(). To safely readout CPM data, retrieve e.g. the primary AR ID, retrieve the relevant buffer with a call to iom_consumer_lock(). The PNPB (PROFINET IO device user interface for the customer application) provides the offset of the cyclic data inside the IOM buffer, as well as data length. During readout also do provide the PNPB with the current APDU status: int32_t PNET_ReadItem(int32_t itemID, void \*data_p) {

::

   int32_t rv = (PNIO_NOT_OK); // IO data invalid
   LSA_UINT8* cpmDataBuf_p;
   iom_apdu_status_t* apduStatus_p;
   PNIO_EXP_SUB*  pExpSub;
   LSA_UINT16 arIdx;

::

   //get primary AR
   arIdx = iom_swif_get_session_prim_ar_idx();

   if (itemID >= PnpbExp[arIdx].NumOfPluggedSub)
     // Controller hasn't plugged in the submodule associated with this item
     // so report back there's no valid output data for it
     return (PNIO_NOT_OK);

   // get pointer to IOCR buffer and APDU status (including cycle counter and status bits)
   iom_consumer_lock((void*)&cpmDataBuf_p, &apduStatus_p, arIdx);

::

   if (cpmDataBuf_p == NULL)
   {
     OsExitX (OS_MUTEX_PNPB_IO);
     OS_INSTRUMENT_USER_STOP(0xAA, 5678);
     return (PNIO_NOT_OK);
   }

::

   // Provide PNPB with APDUStatus
   OsMemCpy(&PnpbExp[arIdx].LastApduStat, apduStatus_p, 4);

::

   pExpSub = &(PnpbExp[arIdx].Sub[itemID]);
   if (pExpSub->OwnSessionKey)
   { // AR is submodule owner
     if (pExpSub->IoProp & PNIO_SUB_PROP_OUT)
     {
       if (pExpSub->isPlugged)
       {
         // Readout data from IOM buffer to provided data pointer
         OsMemCpy(data_p, cpmDataBuf_p + pExpSub->Out.data_offset, pExpSub->Out.data_length);
         rv = (PNIO_OK); // IO data valid
       }
       else
       {
         pExpSub->Out.iocs_val = PNIO_S_BAD;
       }
       /* save remote producer state */
     }
     if (pExpSub->IoProp & PNIO_SUB_PROP_IN)
     {
       /* save remote consumer state */
       pExpSub->In.iocs_val = *(cpmDataBuf_p + pExpSub->In.iocs_offset);
     }
   }
   else
   { // AR is not submodule owner
     if (pExpSub->IoProp & PNIO_SUB_PROP_IN)
     { // save remote consumer state
       pExpSub->In.iocs_val = PNIO_S_BAD;
     }
   }

::

   // **** free pointer to IOCR buffer ***
   iom_consumer_unlock(arIdx);

::

   return rv;

}

Similarly proceed when writing data items and additionally provide items with their current IOPS value: int32_t PNET_WriteItem(int32_t handle, void \*data_p) {

::

   LSA_UINT8* ppmDataBuf_p;
   PNIO_EXP_SUB* pExpSub;
   LSA_UINT16 arIdx;

::

   arIdx = iom_swif_get_session_prim_ar_idx();

   if (handle >= PnpbExp[arIdx].NumOfPluggedSub)
     // Controller hasn't plugged in the submodule associated with this item
     // so just return OK since there's no buffer slot for it
     return (PNIO_NOT_OK);

   iom_provider_lock((void*)&ppmDataBuf_p, arIdx);
   pExpSub = &(PnpbExp[arIdx].Sub[handle]);

::

   //provide io data and iops from input submodule
   if (pExpSub->OwnSessionKey && pExpSub->isPlugged)
   {
     if (pExpSub->IoProp == PNIO_SUB_PROP_NO_DATA)
     { // ** submod has no IO data **
       // *** update (input-)provider state in input frame ***
       if ((!pExpSub->IsWrongSubmod) && pExpSub->ParamEndValid)
         *(ppmDataBuf_p + pExpSub->In.iops_offset) = pExpSub->In.iops_val;
       else
         *(ppmDataBuf_p + pExpSub->In.iops_offset) = PNIO_S_BAD;
     }
     else
     {
       if (pExpSub->IoProp & PNIO_SUB_PROP_IN)
       {  // ** submod has input data **
           // *** update (input-)provider state in input frame ***
         if ((!pExpSub->IsWrongSubmod) && pExpSub->ParamEndValid)
         {
           OsMemCpy(ppmDataBuf_p + pExpSub->In.data_offset, data_p,
                    pExpSub->In.data_length);
           *(ppmDataBuf_p + pExpSub->In.iops_offset) = pExpSub->In.iops_val;
         }
         else
         {
           *(ppmDataBuf_p + pExpSub->In.iops_offset) = PNIO_S_BAD;
         }
       }
       if (pExpSub->IoProp & PNIO_SUB_PROP_OUT)
       { // ** submod has out put data **
         if ((!pExpSub->IsWrongSubmod) && pExpSub->ParamEndValid)
           *(ppmDataBuf_p + pExpSub->Out.iocs_offset) = pExpSub->Out.iocs_val;
         else
           *(ppmDataBuf_p + pExpSub->Out.iocs_offset) = PNIO_S_BAD;
       }
     }
   }
   else // submod not owned or not plugged
   {
     if (pExpSub->IoProp == PNIO_SUB_PROP_NO_DATA)
     { // ** submod has no data **
       *(ppmDataBuf_p + pExpSub->In.iops_offset) = PNIO_S_BAD;
     }
     else
     {
       if (pExpSub->IoProp & PNIO_SUB_PROP_IN)
       { // ** submod has input data **
         OsMemSet((void*)(ppmDataBuf_p + pExpSub->In.data_offset), 0x00,
                  pExpSub->In.data_length);
         *(ppmDataBuf_p + pExpSub->In.iops_offset) = PNIO_S_BAD;
       }
       if (pExpSub->IoProp & PNIO_SUB_PROP_OUT)
       { // ** submod has out put data **
         *(ppmDataBuf_p + pExpSub->Out.iocs_offset) = PNIO_S_BAD;
       }
     }
   }

::

   iom_provider_unlock(arIdx);

::

   return (PNIO_OK);

} NETLOAD FILTERING The PROFINET REM switch driver provides frame filtering capabilities for net load management. All filtering is disabled by default. Two types of filtering can be applied by the REM switch PROFINET firmware. In the first type, careful filtering is applied to eliminate certain classes of frames that are not directed to the local device, such as broadcast address resolution protocol (ARP) requests that do not match the local IP address. In the second type, frames directed to the local device are dropped if the host processor is asked to process high volume of packets. In such a case, priority is given to frames necessary to maintain the PROFINET connection. The following functions are provided for enabling and configuring these filters: • REMS_PnetResetQueue0filterCount() resets the Q0 (lowest priority) frame counter. The first time this function is called, the driver sets a counter that is decremented with every received frame on Q0. The frame count starts at 10 frames and if the counter reaches 0, the driver starts dropping frames that do not have a source MAC address matching the controller of an established connection. The REMS_pnetResetQueue0filterCount() function must then be called periodically to reset the Q0 filter count. Call this function in the lowest priority thread to ensure all threads are serviced under heavy net load. Under normal conditions, the counter never reaches 0 and no frames are dropped. • REMS_PnetSetLldpFilter() sets the MAC address of the neighbor port for a given device port. This function adjusts the low priority filtering to allow all frames from another MAC address. This function allows neighbor LLDP frames through, even if the frame counter reaches 0. • REMS_PnetSetDcpName() sets the device name for DCP device identify request frame filtering. This function enables the filtering of all name of station identify request frames that do not match the given name of station. • REMS_PnetSetDcpAlias() sets the alias name for DCP device identify request frame filtering. This function enables the filtering of all alias name identify request frames that do not match the given alias name. • REMS_PnetSetArpFilter() sets the IP address for ARP filtering. This function enables the filtering of all ARP requests that do not match the device IP address.

PROFINET INTERRRUPT HANDLING For PROFINET Interrupts, the events that are required are left to the application to implement. They must first be assigned using REMS_PL_AssignRemsInts() and then enabled using REMS_PL_EnableRemsInts(), as provided below.

An example of a how a user might go about assigning the interrupt lines is shown in the following code snippets:

int32_t REMS_PL_AssignRemsInts() {

::

   // Assign standard application layer interrupts to the desired lines
   REMS_StdAssignInterrupt(REMS_Int_Queue_3_Packet_Ready, REMS_Int_Line_2);
   REMS_StdAssignInterrupt(REMS_Int_Queue_2_Packet_Ready, REMS_Int_Line_2);
   REMS_StdAssignInterrupt(REMS_Int_Timer_Control_Int_0,  REMS_Int_Line_2);
   REMS_StdAssignInterrupt(REMS_Int_Timer_Control_Int_1,  REMS_Int_Line_2);
   REMS_StdAssignInterrupt(REMS_Int_Timer_Control_Int_2,  REMS_Int_Line_2);

::

   REMS_StdAssignInterrupt(REMS_Int_Periodic_Timer_0,     REMS_Int_Line_1);
   REMS_StdAssignInterrupt(REMS_Int_Queue_1_Packet_Ready, REMS_Int_Line_1);

::

   REMS_StdAssignInterrupt(REMS_StdInt_Port_1_LinkChange, REMS_Int_Line_0);
   REMS_StdAssignInterrupt(REMS_StdInt_Port_2_LinkChange, REMS_Int_Line_0);

::

   // Standard TCP/IP
   REMS_StdAssignInterrupt(REMS_StdInt_PktReady,          REMS_Int_Line_0);

::

   REMS_StdAssignInterrupt(REMS_Int_Periodic_Timer_1,     REMS_Int_Line_0);
   REMS_StdAssignInterrupt(REMS_Int_Host_Port_0,          REMS_Int_Line_0);

::

   return (REMS_PL_OK);

} ¬¬ int32_t REMS_PL_EnableInterrupts() {

::

   // Enable the desired standard REMS interrupts
   REMS_StdEnableInterrupt(REMS_StdInt_Port_1_LinkChange);
   REMS_StdEnableInterrupt(REMS_StdInt_Port_2_LinkChange);
   REMS_StdEnableInterrupt(REMS_StdInt_PktReady);

::

   REMS_StdEnableInterrupt(REMS_Int_Queue_3_Packet_Ready);
   REMS_StdEnableInterrupt(REMS_Int_Queue_2_Packet_Ready);
   REMS_StdEnableInterrupt(REMS_Int_Queue_1_Packet_Ready);
   REMS_StdEnableInterrupt(REMS_Int_Timer_Control_Int_0);
   REMS_StdEnableInterrupt(REMS_Int_Timer_Control_Int_1);
   REMS_StdEnableInterrupt(REMS_Int_Timer_Control_Int_2);
   REMS_StdEnableInterrupt(REMS_Int_Periodic_Timer_0);
   REMS_StdEnableInterrupt(REMS_Int_Host_Port_0);
   return (REMS_PL_OK);

} This block of code will assign and enable interrupts to all three lines with packets that are received on Queue1 for the fido5100/5200 being separate from the other Queues.

Table 3. PROFINET Specific Interrupt Signals PROFINET specific interrupts Indication Usage/Handling REMS_StdInt_TimerControl_0 = REMS_Int_Timer_Control_Event_0 Timer Control Unit (TCU) Signal, send Provider Frame of AR 0 handled by REMS driver REMS_StdInt_TimerControl_1 = REMS_Int_Timer_Control_Event_1 TCU Signal, send Provider Frame of AR 1 handled by REMS driver REMS_StdInt_TimerControl_2 = REMS_Int_Timer_Control_Event_2 TCU Signal, send Provider Frame of AR 2 handled by REMS driver REMS_Int_Periodic_Timer_0 Provider data management during IRT legacy startup handled by REMS driver, IRT specific REMS_Int_Periodic_Timer_1 Periodic processing of synchronization handled by REMS driver, IRT specific REMS_PnetInt_PktReady = REMS_Int_Queue_1_Packet_Ready Non Realtime Traffic (NRT) packet received forward to PN Stack (chapter REMS_Int_Queue_1_Packet_Ready)

REMS_PnetInt_CPM_Watchdog_Timeout0 = REMS_Int_Host_Port_0 AR 0 Data Hold Timer (DHT) expired CSBHandler (chapter REMS_PnetInt_CPM_Watchdog_TimeoutX)

REMS_PnetInt_CPM_Watchdog_Timeout1 = REMS_Int_Host_Port_1 AR 1 DHT expired CSBHandler (chapter REMS_PnetInt_CPM_Watchdog_TimeoutX)

REMS_PnetInt_CPM_Watchdog_Timeout2 = REMS_Int_Host_Port_2 AR 2 DHT expired CSBHandler (chapter REMS_PnetInt_CPM_Watchdog_TimeoutX)

REMS_PnetInt_CPM_Watchdog_Timeout3 = REMS_Int_Host_Port_3 AR 3 DHT expired CSBHandler (chapter REMS_PnetInt_CPM_Watchdog_TimeoutX)

REMS_PnetInt_ReceivedRtData0 = PROTOCOL_INT_ID AR 0 cyclic packet received CSBHandler (chapter REMS_PnetInt_ReceivedRtDataX)

REMS_PnetInt_ReceivedRtData1 AR 1 cyclic packet received CSBHandler (chapter REMS_PnetInt_ReceivedRtDataX)

REMS_PnetInt_ReceivedRtData2 AR 2 cyclic packet received CSBHandler (chapter REMS_PnetInt_ReceivedRtDataX)

REMS_PnetInt_ReceivedRtData3 AR 3 cyclic packet received CSBHandler (chapter REMS_PnetInt_ReceivedRtDataX)

.. image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-4.png
   :align: center

As the PROFINET REM Switch driver supports multiple connections, there are a couple of things to consider. For single and multi-connection use cases, something like the following would be needed to configure interrupts in general.

void REMS_PL_InterruptHandler(uint32_t line) {

::

   volatile REMS_stdIntEvent_t event;
   REMS_CommonEnetPort_t port;

::

   interruptCnt_g++;
   REMS_StdEvaluateInterrupt((REMS_IntLine_t)line);

::

   do {
     event = REMS_StdGetNextEvent((REMS_IntLine_t)line);

::

     switch (event) {
     case ((REMS_stdIntEvent_t)0):
       break;
     /*...*/
         

::

     case REMS_StdInt_PktReady:
       ipFrameCnt_g++;
       LTE_SemSignal(REMS_PL_stdPacketSem_g);
       break;

::

     default:
       prtSpecificCnt_g++;
       REMS_PL_HandleIeEvent(line, event);
       break;
     }
   } while (event != (REMS_stdIntEvent_t)REMS_Int_None);

::

   return;

} The above implementation has REMS_PL_HandleEvent handling the PROFINET specific interrupts. How this is done is dependent on the number of connections the user wishes to support. If there is no system redundancy, then one connection is acceptable and described in “Interrupts for one connection”. If there is a need for multiple connections, then this use case is described in “Interrupts for multiple connections”

Interrupts for One Or Multiple Connections When implementing one connection the user would map “REMS_PL_HandleEvent(line,event)()” to something like the following.

void REMS_PL_HandleIeEvent(uint32_t line, REMS_stdIntEvent_t event) {

::

   uint32_t arep;
   ETH_frameData_t *frameData_p;

   switch (event) {
   case ((REMS_stdIntEvent_t)0):
     break;

   case REMS_PnetInt_CPM_Watchdog_Timeout0:
     // for REMS_PnetInt_CPM_Watchdog_Timeout1 to -3 provide arep values 1 to 
     arep = 0;
     // call EDDF_CRT_ISR_CSB_changed_IFA event number 12 - arep    
     break;
   case REMS_PnetInt_ReceivedRtData0:
     // for REMS_PnetInt_ReceivedRtData1 to -3 provide arep values 1 to 3
     arep = 0;
     // call EDDF_CRT_ISR_CSB_changed_IFA event number 13 + arep    break;
   case REMS_Int_Queue_1_Packet_Ready:
     LTE_SemSignal(REMS_PL_iePacketSem_g);
     break;
   default:
     break;
   }

::

   return;

}

Acyclic Message ReceptionREMS Queue 1 is designated to receive PROFINET NRT frames, this includes ACP, LLDP, and MRP Frames. In the current revision, PTCP-Frames are ignored. After reading the packets from the driver, they must be provided to the PN-Stack. This is achieved by calling eddf_interrupt(pDDB->hDDB, EDDF_INT_ACYC_RCV_IFA). eddf_interrupt() leads to a call to EDDF_NRT_ISR_Acyc_Rcv_IFA(), which will retrieve the current frame with a call to REMS_ReadPacket(). Make sure to clear the frame out of the REMS queue by a call to REMS_ReadPacket() in any error case as well.

sem_t q1PacketSem_g

//Signal Semaphore when receiving Q1 interrupt void InterruptHandler(uint32_t line) {

::

   volatile REMS_stdIntEvent_t event;
   REMS_CommonEnetPort_t port;
   REMS_StdEvaluateInterrupt((REMS_IntLine_t)line);

::

   do {
     event = REMS_StdGetNextEvent((REMS_IntLine_t)line);

::

     switch (event) {
     /*...*/
     /* Protocol-specific interrupt events */
     case REMS_Int_Queue_1_Packet_Ready:
       SignalSemaphore(q1PacketSem_g);
       break;

::

     /*...*/
     }
   } while (event != (REMS_stdIntEvent_t)REMS_Int_None);
   return;

}

void HandleQ1Packet(void \*param) {

::

   EDDF_LOCAL_DDB_PTR_TYPE    pDDB;

   do{
     LTE_SemTake(q1PacketSem_g, LTE_WAIT_FOREVER);
     pDDB = &g_EDDF_coreDev;
     if (pDDB->Core.Isr.Active) {
         eddf_interrupt(pDDB->hDDB, EDDF_INT_ACYC_RCV_IFA);
     } else {
       //read and dump packet
       REMS_ReadPacket(/*...*/);
     }
   } while (1);

}

/\* called by PN-Stack*/ LSA_VOID EDDF_LOCAL_FCT_ATTR EDDF_NRT_ISR_Acyc_Rcv_IFA(

::

     EDDF_LOCAL_DDB_PTR_TYPE     pDDB,
     LSA_UINT32                  EventNr)

{

::

   /*...*/

::

   /* Allocate buffer for receive frame */

::

   /* Get NRT frame from Q1 */
   rv = REMS_ReadPacket(REMS_Queue_1,
                        &portNum,
                        &(ingressTime),
                 buf_p,
                        &size);

::

   frameHeader_p = (DCP_ETHDR*)buf_p;
   dataOffset = EDD_NRT_MIN_SND_LEN;
   //Get ethertype and skip VLAN if present
   /*...*/

::

   // Check ethertype and determine protocol
   // get User Channel RQB Queue 
   switch (ethertype) {
     case 0x8892: //ACP_ETHERTYPE_RT:
       /*...*/
       break;
     case 0x88E3: //MRP_ETHERTYPE:
       /*...*/
       break;
     case 0x88CC: //LLDP_ETHERTYPE:
       /*...*/
       break;
     default:
       /* alert ip manager to presence of frame */
       isFramePass     = LSA_FALSE;
       ReleaseBuffer(buf_p);
       break;
   }

::

   // if protocol is known and RQB Queue is available, send RQB to Stack
   if (isFramePass)
   {
     if (pUsrChRqbQueue->Count)
     {
       /*...*/
     }
     else
     {
       ReleaseBuffer(buf_p);
     }
   }

} Cyclic Data Exchange The PN Stack handles reception of cyclic data and their connected watchdog events separate from NRT traffic, via a so-called consumer scoreboard (CSB) handler. The CSB handler provides the PN Stack with information about the current status of cyclic traffic. This information is conveyed to the CSB handler via EDDF_CRT_ISR_CSB_changed_IFA(). EDDF_CRT_ISR_CSB_changed_IFA Provides the PN-Stack with information about the status of the cyclic communication. The event parameter of the function is currently used to discern between different communication events. Communication events are currently: 1. the reception of a cyclic frame. 2. the trigger of a watchdog, monitoring the cyclic communication. The REMS driver supports up to 3 ARs (the fourth AR is used for redundancy purposes) and therefore issues different events for each AR (e.g., REMS_PnetInt_CPM_Watchdog_Timeout0 - REMS_PnetInt_CPM_Watchdog_Timeout2). EDDF_CRT_ISR_CSB_changed_IFA() and in turn the EDDF_CRTScoreboardHandler() use these event numbers to discern between the reception and watchdog events. Currently event values 12-9 correspond to watchdog events for AR 0-4, whereas event values 13-17 correspond to reception events for AR 0-4. REMS_PnetInt_CPM_Watchdog_TimeoutX The REMS driver receives a timer interrupt (REMS_Int_Timer_Control_Int_X) by FIDO. After the valid input of PROFINET configuration data, the driver monitors the reception of frames each send cycle. If no reception took place between two cycles, a miss counter is increased. When the miss count exceeds the configured watchdog counter (also called Data Hold Timer DHT) the driver issues REMS_PnetInt_CPM_Watchdog_TimeoutX. This event needs to be handled by the PN Stack via a call to EDDF_CRT_ISR_CSB_changed_IFA() with the event parameter value 12 - ARReferenceNumber. REMS_PnetInt_ReceivedRtDataX REMS_PnetInt_ReceivedRtData event is published each time a new cyclic io-frame is received, similar to REMS_PnetInt_CPM_Watchdog_TimeoutX the event must handled by a call to EDDF_CRT_ISR_CSB_changed_IFA with the event parameter value 13 + ARReferenceNumber. Additionally this event leads to a call to iom_swif_swap_cpm_buffer() during the execution of EDDF_CRT_ISR_CSB_changed_IFA. The buffer pointer for the consumer buffer is then changed to provide a new/free buffer to the REMS driver to fill during the next reception. EDDF ADAPTION The provided EDDF requires additional hardware specific implementations. The following chapter provides information on the location and tasks of the required additions. Required changes are added as comments throughout the code snippets. EDDF Core General The following functions in eddf_core_gen.c require adaptions:EDD_RSP EDDF_LOCAL_FCT_ATTR EDDF_GENLEDBlink(/\*...*/) {

::

   /*...*/
   // Interface HW function to blink PROFINET LEDs using EDDF_LED_BLINK_ON_OFF_DURATION_IN_100ms as cycle time 

::

   EDDF_CORE_TRACE_01(pDDB->TraceIdx, LSA_TRACE_LEVEL_CHAT, "[H:%2X] OUT:
                      EDDF_GENLEDBlink()", pHDB->Handle)
   return (EDD_STS_OK);

}

LSA_VOID EDDF_LOCAL_FCT_ATTR EDDF_GENLEDBlink_Toggle(/\*...*/) {

::

   /*...*/
   if (pDDB->SWI.LEDBlink.TotalBlinkCountIn500ms < 

(pDDB->SWI.LEDBlink.TotalBlinkDurationInSeconds \* 2))

::

   {
     /* Toggle all LEDs of this interface to blink green*/
   }
   else
   {
     /*...*/
     /* Restore LEDs to initial state after blinking (continuously show green) */
   }
   /*...*/

}

LSA_VOID EDDF_LOCAL_FCT_ATTR \_EDDF_GEN_ReadPhyStatusRegs(/\*...*/) {

::

   phyConfig_t phyConfig;

   EDDF_ASSERT_FALSE((LSA_HOST_PTR_ARE_EQUAL(pLinkStatus, LSA_NULL)));

::

   // Check for current LinkState of Port e.g. through REMS_GetPortLinkStatus()
   if (LinkStateUp(HWPortID-1)) == 0) {
     pLinkStatus->Link = EDD_LINK_DOWN;
     pLinkStatus->Speed = EDD_LINK_SPEED_100;
     pLinkStatus->Duplexity = EDD_LINK_MODE_FULL;
   } else {
     pLinkStatus->Link = EDD_LINK_UP;
     // Read Speed and Duplex config of Port
     GetPhyConfig(PNET_PL_ifHandle_g, 
                   HWPortID-1),
                   &phyConfig, 
                   sizeof(phyConfig));
     // Set pLinkStatus->Speed and pLinkStatus->Duplexity accordingly
     
   }

}

/\*============= D E F I N E S =============*/ typedef struct mcItem {

::

   LSA_UINT8 macAddr[EDD_MAC_ADDR_SIZE];
   LSA_UINT32 refCnt;
   struct mcItem *next_p;

} mcItem_t;

/\*============= D A T A =============*/ static mcItem_t \*mcHead_gp = NULL;

EDD_RSP EDDF_LOCAL_FCT_ATTR EDDF_GEN_Remove_Multicast_Address(/\*...*/) {

::

   mcItem_t *item_p = mcHead_gp, *prev_p = NULL;
   ETH_generalParamData_t ethIfparam;

::

   /*...*/

   // Check if provided Address is MC Addres, issue Error if not
   if ((MAC_Address.MacAdr[0] & 0x01) == 0) {
     return EDD_STS_ERR_PARAM;
   }

::

   while (item_p != NULL && OsMemCmp(MAC_Address.MacAdr,
                                     item_p->macAddr,
                                     sizeof(item_p->macAddr)) != 0) {
     prev_p = item_p;
     item_p = item_p->next_p;
   }

::

   if (item_p == NULL) {
     // Entry not in static table but probably best to just clear the caller
     // reference counter and return OK instead of an error so we're not forcing
     // the caller to keep track of what's in the table
     *RefCnt = 0;
     return EDD_STS_OK;
   }

::

   if (--(item_p->refCnt) > 0) {
     // Can't remove entry yet since someone still needs it
     *RefCnt = item_p->refCnt;
     return EDD_STS_OK;
   }

::

   // Remove entry from static table
   ethIfparam.data_p = MAC_Address.MacAdr;
   ethIfparam.dataSize = 6;

::

   if (REMS_DeleteStaticTableEntry(MAC_Address.MacAdr) != 0) 
   {
     // Something went wrong removing this entry from the static table
     return EDD_STS_ERR_PARAM;
   }

::

   // Entry was removed so let's keep track of it in the list
   if (prev_p == NULL) {
     // Item is the list head
     mcHead_gp = item_p->next_p;
   } else
     prev_p->next_p = item_p->next_p;

::

   OsFree(item_p);

::

   *RefCnt = 0;
   return EDD_STS_OK;

}

EDDF NRT In eddf_nrt_rcv.c return/release previously allocated buffers, if necessary. EDD_RSP EDDF_LOCAL_FCT_ATTR EDDF_NRTRecv(/\*...*/) {

::

   /*...*/  
   /* Check if buffer has been allocated */
   if (pRQBRcv->UserDataLength > 0)
   {
     // Return/release pRQBRcv->pBuffer received to it's origin, e.g., IP Stack
     pRQBRcv->UserDataLength = 0;
   }
   /*...*/

}

EDDF PHY eddf_phy.c provides functions for the EDDF to get/set values of the underlying PHY. The following functions require adaptions to perform properly: EDD_RSP EDDF_SYSTEM_OUT_FCT_ATTR EDDF_PHY_LoadDelayValues(/\*...*/) {

::

   int16_t rxDelay;
   int16_t txDelay;

   LSA_UNUSED_ARG(hDDB);

::

   // Read HW Phy delays from PHY and provide them in txDelay/rxDelay

::

   pLinkStatus->RealPortTxDelay    = txDelay;
   pLinkStatus->RealPortRxDelay    = rxDelay;
   pLinkStatus->MaxPortTxDelay     = txDelay;
   pLinkStatus->MaxPortRxDelay     = rxDelay;

::

   return EDD_STS_OK;

}

EDD_RSP EDDF_SYSTEM_OUT_FCT_ATTR EDDF_PHY_GetLinkStatus(/\*...*/) {

::

   /*...*/

   // ***** Examine passed parameters to determine link, speed and duplexity.

::

   /* Depending on PHY speed provide values for:
   * pLinkStatus->Link
   * pLinkStatus->Speed
   * pLinkStatus->Duplexity
   * pLinkStatus->MAUType 
    */
     
   pLinkStatus->AutonegCapAdvertised = 0;

::

   pLinkStatus->AutonegCapAdvertised |= EDD_AUTONEG_CAP_10BASET;

::

   /*...*/

   return EDD_STS_OK;

}

EDD_RSP EDDF_SYSTEM_OUT_FCT_ATTR EDDF_PHY_SetPowerDown(/\*...*/) {

::

   LSA_UNUSED_ARG(hSysDev);

::

   if (EDDF_PHY_POWERDOWN == PowerDown)
   {
     // Power down phy
   }
   else
   {
     // Power up phy
   }

::

   return EDD_STS_OK;

}

EDD_RSP EDDF_SYSTEM_OUT_FCT_ATTR EDDF_PHY_CheckPowerDown(/\*...*/) {

::

   LSA_UNUSED_ARG(hSysDev);

::

   /* Get PHY link status and set pIsPowerdown accordingly
   * Values: EDDF_PHY_POWERDOWN or EDDF_PHY_POWERUP
    */

::

   return EDD_STS_OK;

}

EDD_RSP EDDF_SYSTEM_OUT_FCT_ATTR EDDF_PHY_SetSpeedDuplexityOrAutoneg(/\*...*/) {

::

   /*...*/

::

   /* read current PHY config */

::

   if (EDD_AUTONEG_ON == Autoneg)
   {
     /* set PHY config to auto negotiation
   * speed/duplexmode/crossover values to unknown
      */
   }
   else
   {
     /* Set PHY config according to function parameters */
   }

::

   /*...*/

}

EDDF SWI In eddf_swi.c add a missing call to REMS_FlushDynamicTable() as indicated below. Additionally, the boundary states of the REMS driver must be properly set in the functions listed here. LSA_VOID EDDF_LOCAL_FCT_ATTR EDDF_SWIRequest(/\*...*/) {

::

   /*...*/
   switch (Service)
   {
   /*...*/
   case EDD_SRV_SWITCH_FLUSH_FILTERING_DB:
     {   
       /*...*/
       if (bBreak)
       {
         break;  // exit case FLUSH_FILTERING_DB
       }
       /* -------------------------------- */
       /* execute the service              */
       /* -------------------------------- */
       // Flush Dynamic Table:
       REMS_FlushDynamicTable();
     }
     break;
     /*...*/
   }
   /*...*/

}

LSA_VOID EDDF_LOCAL_FCT_ATTR EDDF_SWI_MC_Entry_Set_To_Default(/\*...*/) {

::

   // PTCP not supported at this time, so skip mac 0x010ECF0004
   // Clear DCP Ident Boundary State if MAC_Address.MacAdr is 0x010ECF000000
   if( CheckDCPIdentMac(MAC_Address.MacAdr))
   {
     REMS_PnetSetPortBoundaryState(1, REMS_PORT_DCP_BOUNDARY_CLEAR);
     REMS_PnetSetPortBoundaryState(2, REMS_PORT_DCP_BOUNDARY_CLEAR);
   }
   // Clear DCP Hello Boundary State if MAC_Address.MacAdr is 0x010ECF000001
   else if (CheckDCPHelloMac(MAC_Address.MacAdr))
   {
     REMS_PnetSetPortBoundaryState(1, REMS_PORT_ANOUNCE_BOUNDARY_CLEAR);
     REMS_PnetSetPortBoundaryState(2, REMS_PORT_ANOUNCE_BOUNDARY_CLEAR);
   }

}

EDD_RSP EDDF_LOCAL_FCT_ATTR EDDF_SWI_MC_Entry_Set_DomainBoundary(/\*...*/) {

::

   EDD_RSP         Response = EDD_STS_OK;

   // PTCP not supported at this time, so skip mac 0x010ECF0004

   // Set DCP Ident Boundary State if MAC_Address.MacAdr is 0x010ECF000000
   if( CheckDCPIdentMac(MAC_Address.MacAdr))
   {
     REMS_PnetSetPortBoundaryState(PortID, REMS_PORT_DCP_BOUNDARY_SET);
   }
   // Set DCP Hello Boundary State if MAC_Address.MacAdr is 0x010ECF000001
   else if (CheckDCPHelloMac(MAC_Address.MacAdr))
   {
     REMS_PnetSetPortBoundaryState(PortID, REMS_PORT_ANOUNCE_BOUNDARY_SET);
   }
   else
   {
     Response = EDD_STS_ERR_PARAM;
     EDDF_DBG_SET_DETAIL_ERR(pDDB, Response);
     EDDF_SWI_TRACE_01(pDDB->TraceIdx, LSA_TRACE_LEVEL_ERROR, "[H:--]
                       EDDF_SWI_MC_Entry_Set_Ingress_and_Egress(): ERROR -> given PortID(%d)                       
                       is out of range!", PortID);
   }

   return (Response);

}

ETHERNET/IP The REM EtherNet/IP driver can be used to develop a device capable of supporting priority channel-based Ethernet/IP communications and, when combined with the DLR support library, beacon-based device level ring (DLR) redundancy. The REM switch is Open DeviceNet Vendors Association, Inc. (ODVA) conformant. Additional capabilities of the REM switch include the following: • Cut through operation • IEEE-1588 end to end transparent clock • Common industrial protocol (CIP) compliant quality of service (QOS) handling of EtherNet/IP Class 1 I/O frames (DSCP) The creation of a complete EtherNet/IP device using the REM switch and this driver also requires a TCP/IP protocol stack and an EtherNet/IP protocol stack, both provided by the user. In addition, to support the DLR protocol details, combine this driver with the DLR support library. See the DLR support library user guide for more information on how to use the library. The REM switch manages the Ethernet Layer 2 communications and switching, and also manages selected details of other protocol frames. Specifically, the REM switch detects EtherNet/IP Class 1 I/O frames that are directed to this device. Using one of the priority queues internal to the REM switch hardware, the REM switch redirects these frames to a higher priority queue. In addition, the REM switch detects DLR frames and redirects them to an independent queue. As such, there are three independent channels through which Ethernet frames can flow to the system software. This version of the REM driver provides a static MAC address lookup table that contains space for six entries. This version of the REM driver for EtherNet/IP supports DLR as a DLR ring node only. This version does not support CIP synchronization. The handling of DLR multicast frames does not require the use of the static table, regardless of whether the DLR is enabled. ETHERNET/IP INITIALIZATION To initialize the REM EtherNet/IP driver, complete the following steps: 1. Configure the external interrupt input pins on the host processor. 2. Call REMS_StdInit as follows: REMS_StdInit(REMS_MII, 0, REMS_Int_Line_0, REMS_Int_Line_1, REMS_Int_Line_2); 1. For the three priority levels, select the PHY mode (currently MII), 0 (the second argument is reserved, allowing for user specification), and the designation of the REM interrupt lines. 3. Optional. Call REMS_EipSetFilterCounters to provide the broadcast and multicast storm filter values. If this function is not called, the filters remain disabled. 4. Call REMS_StdSetMacAddress to communicate the system MAC address to the REM switch. This function takes three MAC addresses as parameters. When using EtherNet/IP, only one MAC address is necessary, and the second and third arguments can be zeros. 5. Call REMS_StdSetPortState once for each port to set the port state to REMS_PORT_FORWARDING. 6. Optional. Call REMS_EipSetDSCPValues to set the differential services code point (DSCP) QOS values. If this function is not called, the REM switch contains suitable default values for these settings and fully conforms to the ODVA requirements set forth in the CIP specification Volume 2 Section 5-7.4.2. After completing these steps, the REM switch is fully configured and is ready to begin communications. There are two other considerations: handling the PHY link states and handling central processing unit (CPU) interrupts, which are discussed in the following sections. HANDLING PHY LINK STATES To function correctly, the REM switch must be told the external speed and duplex settings for each port. Because EtherNet/IP devices can be used in either 100 Mbps or 10 Mbps networks, do not assume a 100 Mbps full duplex. The REM driver provides a function named REMS_StdSetSpeedAndDuplex to change the speed and duplex settings. The REM medium priority interrupt events for port link change (REMS_Int_Port_1_Link_Change or REMS_Int_Port_2_Link_Change) must be used to trigger the process of reading the PHYs to determine the link speed and duplex, typically using the management data input/output (MDIO) serial management interface. After the medium priority interrupt events take place, call REMS_StdSetSpeedAndDuplex to update the switch settings. The PHYs used with the REM switch are required to supply a link status output that can be routed to the REM switch input with the same name. This process triggers REMS_Int_Port_n_Link_Change. This PHY output must be the link status, not link activity or status. A typical PHY has a low active output (generally intended to drive a light emitting diode (LED)) that is often set by default to also act as an activity indicator. If unchanged, this output continually toggles as communications proceed, triggering erroneous link up and link down interrupts. The PHY configuration must be changed so that this toggling does not occur. The REM switch and driver do not provide any MDIO hardware or subroutines. The system designer must supply these subroutines. HANDLING CPU INTERRUPTS During the REM initialization process, calling REMS_StdInit designates the REM interrupt lines high, medium, or low priority. The REM switch and driver then assign these interrupt lines to the various interrupt events as described in Table 3.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-5.png
   :align: center

The user determines how to set up the host low level interrupt request line (IRQ) handler. After being set up, the IRQ handler can call a REM event handler function. The IRQ handler must have access to the REM interrupt line being used and may use various REM driver functions to perform the following sequence: 1. At the start of the handler, call REMS_StdEvaluateInterrupt one time only to obtain a complete list of all events currently pending for the interrupt line of interest. This function not only retrieves this event list but also acknowledges all the pending and enabled interrupt events detected within the REM hardware. All detected events must be handled in the same interrupt. 2. In a while loop, repeatedly call REMS_StdGetNextEvent to get the next pending event until the event returned is REMS_Int_None. For each event retrieved, call the appropriate code to handle that event. This process is described in detail in the Low Priority TCP/IP Frame Receive and Transmit Processing, High Priority EtherNet/IP Class 1 Frame Receive and Transmit Processing, and EtherNet/IP DLR Frame Receive and Transmit Processing sections. See the Interrupts section for general examples of this process. For EtherNet/IP, the user must handle interrupt events. LOW PRIORITY TCP/IP FRAME RECEIVE AND TRANSMIT PROCESSING The setup and utilization of the TCP/IP stack is up to the user. This user guide describes how to use the REM driver to connect the REM switch hardware to the stack using the following three mechanisms, which the user stack must contain: • A buffer pool for placing received frames. • A mechanism for notifying if frames have been received. • A way to register a callback function that the stack uses to transmit a frame when desired. Receive When a low priority frame arrives, the REM hardware triggers the low priority interrupt line and issues a REMS_Int_Queue_0_Packet_Ready event. The user handler must be ready to detect this event, as well as perform the following sequence: 1. Get a buffer from the buffer pool of the TCP/IP stack. 2. Use the REMS_StdReadPacket or REMS_StdReadPacketWithTimestamp REM driver functions to read the data from the switch queue into that buffer. Note that the difference between these two functions involves the return of the ingress timestamp, which is the time at which the packet was received. 3. Use the notification mechanism of the TCP/IP stack to tell the TCP/IP stack a received frame is ready.

Transmit To transmit a low priority TCP/IP frame, no REM interrupt or event handler is used. Assuming a transmit handler function can be registered with the TCP/IP stack, the user must only write this function and register the function with the stack. The function must perform the following sequence: 1. Get the frame from the TCP/IP stack. 2. Call either REMS_StdXmitTaggedPacket, REMS_StdXmitPacket, or REMS_StdXmitPacketWithControlFlag, as required to send data through the switch queue. The difference between the first two functions involves the use of an IEEE-802.1Q VLAN tag. Many TCP/IP stacks do not have the capability of tagging the frames themselves. If this is the case, use the tagged version and supply the tag data to the REM driver separately. The driver inserts the tag at the location designated. The third function allows the command of an egress timestamp insertion or capture. If an egress timestamp insertion is called, the hardware overwrites packet data at the location with the current timestamp as the packet is transmitted. Likewise, if a timestamp capture is called, the hardware captures the timestamp when the packet is transmitted. The commands and insertion sizes used to create the control flags are defined in REMS_Basic.h. HIGH PRIORITY ETHERNET/IP CLASS 1 FRAME RECEIVE AND TRANSMIT PROCESSING The REM hardware detects EtherNet/IP Class 1 I/O frames and directs them to a dedicated high priority receive queue. To ensure undisturbed handling of this data, this queue is used for no other purpose. Because the frames used to set up the EtherNet/IP Class 1 connection (such as register session and forward open) are not Class 1 I/O frames, those frames are not directed to the high priority queue. This communication takes place in a low priority queue. If the user EtherNet/IP stack can make use of the independent flow of this data, connecting EtherNet/IP stack to this queue to create a high priority I/O channel is simple. If the user stack does not have this capability, follow the steps described in the Low Priority TCP/IP Frame Receive and Transmit Processing section. Receive When a high priority Class 1 I/O frame arrives, the REM hardware triggers the high priority interrupt line and issues a REMS_Int_Queue_1_Packet_Ready event. The user handler must be able to detect this event, as well as perform the following sequence: 1. Get a buffer from the buffer pool of the EtherNet/IP stack. 2. Use the REMS_Class1ReadPacket REM driver function to read the data from the switch queue into that buffer. 3. Use the notification mechanism of the EtherNet/IP stack to inform the EtherNet/IP stack that a received frame is ready. Transmit To transmit a high priority Class 1 I/O frame, use of an REM interrupt or event handler is not necessary. Assuming a transmit handler function can be registered with the EtherNet/IP stack, the user must only write this function and register it. The function must perform the following sequence: 1. Retrieve the frame from the EtherNet/IP stack. 2. Call either REMS_Class1XmitTaggedPacket or REMS_Class1XmitPacket to send data through the switch queue. The difference between these two functions involves the use of an IEEE-802.1Q VLAN tag. Many TCP/IP stacks do not have the capability of tagging the frames themselves. If this is the case, use the tagged version and supply the tag data to the REM driver separately. The driver inserts the tag at the location designated. ETHERNET/IP DLR FRAME RECEIVE AND TRANSMIT PROCESSING The REM hardware detects EtherNet/IP DLR frames and directs these frames to a dedicated receive queue. To ensure the undisturbed handling of this data, this queue is used for no other purpose. Receive When an EtherNet/IP DLR frame arrives, the REM hardware triggers the low priority interrupt line and issues a REMS_Int_Queue_2\_ Packet_Ready event. The user handler must be able to detect this event, as well as perform the following tasks: 1. Get a buffer from the buffer pool of the EtherNet/IP DLR stack. 2. Use the REMS_DlrReadPacket REM driver function to read the data from the switch queue into that buffer. 3. Use the notification mechanism of the EtherNet/IP DLR stack to inform the EtherNet/IP DLR stack that a received frame is ready. The DLR support library uses a software queuing mechanism to receive these frames. This queue is created by the board support package files and is referred to by the g_DLR_PacketQueue variable name. The frames, when received, are added to this queue and are retrieved when the DLR library calls the BSP_Get_DLR_Packet board support package function. This process takes place when the RING_EVENT_RECEIVE_MSG event is processed within the EtherIpRingProtocol_ProcessEvents function. Transmit To transmit an EtherNet/IP DLR frame, no REM interrupt or event handler is used. Assuming a transmit handler function can be registered with the Ethernet/IP DLR stack, the user must only write this function and register it. The function must perform the following sequence: 1. Get the frame from the EtherNet/IP DLR stack 2. Call REMS_DlrXmitPacket to send data through the switch queue. The DLR support library has a function to transmit DLR frames when necessary. The function is integrated in the DLR library and, in this case, does not need to be registered. The function is called BSP_Put_DLR_Packet and can be found in the DLR library board support package file, BspEnetSwitch.c. OTHER CONSIDERATIONS FOR DLR By default, on power up, the REM switch disables all DLR features. It is necessary to specifically enable REM switch DLR features by using the REM driver function REMS_DlrEnable. It is also necessary to use the DLR support library to implement the software details of the DLR protocol itself. The initialization of the support library is described in the DLR support library user guide. After the REM switch or driver and the DLR library are initialized, route the received DLR frames to the DLR support library. DLR Frame Handling by Frame Type When the DLR is enabled, all DLR frames are routed by the REM switch. There is no need to use an entry in the static routing table. The specific routing of the DLR frames is described in Table 4.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-6.png
   :align: center

Handling DLR Beacon Frames The REM switch sends beacon frames to the host only if the DLR ring state changes or if the active DLR supervisor MAC changes. When one of these events occurs, expect one frame from each port. When the beacon frames are received and successfully processed by the user code or DLR stack, extract the beacon interval and timeout data and use them to program the TCU by using the REMS_EipStartTcu REM driver function. After the TCU is started, call REMS_EipEnableBTOIrq to enable the beacon timeout interrupt. This interrupt is routed to the medium priority interrupt and the REM events. REMS_Int_Port_1_1 and REMS_Int_Port_2_1 are used to indicate this interrupt. Each port independently monitors for beacon timeouts. Successful processing of the beacon frames means that a valid beacon frame has been received from both ports, and both frames indicate that the system has made the transition into ring normal state. Only start the TCU once. At this point, the REM switch begins to process received beacon frames to monitor for timeouts, active supervisor MAC changes, or ring state changes. Handling Unintended Loop Detect The external ports on the REM switch examine the source MAC of each received frame to detect frames with a source MAC that matches that of the system. If the external ports detect a matching frame, an Ethernet loop exists. These frames are not forwarded to the other port, but instead generate a medium priority interrupt to the host. The interrupt events generated are REMS_Int_Port_1_0 and REMS_Int_Port_2_0. These events allow the user DLR stack to report the detection of an unintentional loop. Handling Port Link Change When an Ethernet link up or link down event occurs, the DLR library must be informed. The event itself is an interrupt that the REM switch generates to the host CPU (see Table 3). The EtherIpRingProtocol_HandleLinkStateChange DLR library function is called in response. See the DLR library user guide for more information. BROADCAST AND MULTICAST FILTERING When using the EtherNet/IP protocol, the REM switch can be set to limit the rate of broadcast and multicast frames that are routed through the switch. This setup is referred to as broadcast or multicast storm protection. This protection is implemented with an adjustable threshold that allows the REM switch to only accept n number of frames in t milliseconds. To set up this protection, the REM switch counts the broadcast and multicast frames accepted until it reaches n and then begins to discard them. Each frame type (broadcast or multicast) is counted separately so there are two independent filters. The host CPU can enable this filtering by calling REMS_EipSetFilterCounters to set the packet limits. There is no specific mechanism to set the time period, and it is only necessary to periodically signal the switch to reset the limit counters. The REM switch driver function that resets the limit counters is named REMS_EipServiceBcastMcastFilter. Because this signal resets both counters, there is only one time interval shared between both filters. Although it is possible to use one of the periodic timers of the REM switch for this purpose, the creation and maintenance of such a function is user dependent. MODBUS/TCP This REM switch driver software provides a mechanism that allows the exchange of I/O data information and Modbus/TCP configuration with the REM switch. Use this software driver with the REM switch to implement a priority channel in a Modbus/TCP device. To complete a Modbus/TCP device, a TCP/IP protocol stack and a Modbus/TCP slave stack is required. These stacks are not provided as part of this software package. This driver package handles communication between the application and stacks and the REM switch. The REM switch ensures Layer 2 switch functionality (such as broadcast and multicast frame routing, static table, and dynamic table) and also prioritizes Modbus/TCP traffic above all other traffic. The REM switch expects packets from the driver to be written to different host write queues depending on their priority. Packets written to the high priority queue are transmitted before any packets that are written to the standard priority queue. In this way, the application can write standard, nonModbus/TCP packets to the standard priority queue and can write Modbus/TCP packets to the high priority queue to ensure that Modbus/TCP packets are transmitted with preference over standard packets. Similarly, the REM switch examines all received unicast frames intended for the device to determine if they are Modbus/TCP frames. If the packet is determined to be a Modbus/TCP packet, the packet is routed to the high priority host read queue. All other traffic is routed to the standard priority host read queue. As such, the attached host processor can give preference to Modbus/TCP packets over all other packets, ensuring that Modbus/TCP packets always arrive at the host processor, regardless of network loading. MODBUS/TCP INITIALIZATION The software initialization procedure of the REM switch and driver for Modbus/TCP is as follows: 1. Configure the external interrupt input pins on the host processor. 2. Assert the REM switch reset line and wait for the switch to become ready. 3. Call REMS_StdInit(). Provide the PHY mode (currently MII), the clock enable flag (set to 0), and the REM switch interrupt lines you want to use for the three priority levels. 4. Call REMS_StdSetMacAddress() to set the MAC address for the system. There are three MAC address parameters to this function. For Modbus/TCP, supply the same MAC address for each of the three MAC address parameters. MODBUS/TCP INTERRUPT HANDLING When REMS_StdInit() is called, the interrupt outputs are assigned high, medium, and low priority positions according to the passed in parameters. The REM switch driver assigns interrupt sources to interrupt lines, as shown in Table 5. The low level interrupt handler must be aware of which REM switch interrupt line caused the interrupt and then call the REM switch event handler function (as shown in the Interrupts section). After the event handler function is called, all pending interrupts are evaluated and handled individually in a loop.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-7.png
   :align: center

MODBUS/TCP PHY LINK STATE INTERRUPT HANDLING The REM switch determines link up or down from a signal supplied to it by the PHYs, but the link speed and duplex settings must be written to the REM switch by the host processor. The REM switch does not determine these settings on its own. When the EtherNet link becomes active (REMS_StdInt_Port_1_LinkChange or REMS_StdInt_Port_2_LinkChange interrupt event occurs), the application reads the link speed and duplex from the PHYs. The link speed and duplex are then written to the REM switch using REMS_StdSetSpeedAndDuplex() to keep the REM switch updated with the current link settings. The REM switch and driver do not provide MDIO hardware or driver subroutines. The system designer is responsible for providing a mechanism to deliver link and duplex information to the REM switch.

MODBUS/TCP RECEIVED PACKET INTERRUPT HANDLING When the REM switch triggers the REMS_Int_Queue_0_Packet_Ready or REMS_Int_Queue_1_Packet_Ready event, a high or standard priority packet for the device has arrived and is ready for the host processor to read from the REM switch memory. The interrupt handler then supplies the new packet to the TCP/IP stack. Depending on the architecture of the TCP/IP stack to which the packet is supplied, the process of supplying the stack may appear as follows: 1. Check for a free buffer from the TCP/IP stack. 2. If a free buffer is found, use REMS_StdReadPacket() for standard priority packets or REMS_Read_ModbusTCP_Packet() for Modbus/TCP packets to read the new packet from the REM switch memory into the buffer. 3. Supply the buffer to the TCP/IP stack to begin processing. All received TCP/IP packets with a source or destination port number of 502 generate a REMS_Int_Queue_0_Packet_Ready interrupt event. All other received packets generate a REMS_Int_Queue_1_Packet_Ready interrupt event. Because the REMS_Int_Queue_0 \_Packet_Ready interrupt event has a higher priority than the REMS_Int_Queue_1_Packet_Ready interrupt event, Modbus/TCP packets inherently arrive at the host processor at a higher priority than other packets. MODBUS/TCP PACKET TRANSMISSION Transmission of frames can be initiated at any time. The system designer registers a packet transmission routine with the TCP/IP stack to connect the TCP/IP stack to the Ethernet driver. This process is also true when using the REM switch. When it is time to transmit a packet, the TCP/IP stack calls the packet transmission routine to retrieve the packet from the TCP/IP stack and supply the packet to the REM switch for transmission using REMS_StdXmitPacket()or REMS_Xmit_ModbusTCP_Packet(). REMS_StdXmitPacket() writes the packet to the REM switch using the standard priority queue while REMS_Xmit_ModbusTCP_Packet() writes the packet to the REM switch using the high priority queue. In this way, Modbus/TCP packets transmit from the device at a higher priority than standard packets. EtherCAT The EtherCAT driver provides a software interface by which an application layer and EtherCAT slave stack can initialize and use the REM switch as an EtherCAT slave controller (ESC). When this driver is used, the Beckhoff EtherCAT slave stack code (SSC) can be integrated with minimal porting effort because the driver is designed to interact directly with the SSC. To create a finished EtherCAT device, an EtherCAT slave stack must be supplied by the user. The driver is designed to directly integrate with the Beckhoff EtherCAT SSC. The REM switch, in combination with this driver, acts as an ESC that supports distributed clocks, eight synchronization managers, hereafter referred to as SyncManager) and eight Fieldbus Memory Management Units (FMMUs) with 10 kB of RAM. ETHERCAT INITIALIZATION To initialize an EtherCAT slave stack, perform the following actions: 1. Disable PHYs and power down both PHYs via MDIO to prevent any network traffic from entering until the REM switch and the system are completely initialized and ready for EtherCAT communication. 2. Restore electrically erasable programmable read only memory (EEPROM) emulation data. Retrieve the emulated EEPROM data from nonvolatile memory. The REM switch does not have attached EEPROM so the EEPROM must be emulated by the application. This requirement means that the application must provide functions for the EtherCAT master to read and write EEPROM. See the EEPROM Emulation section for more details. 3. Reset the REM switch. This reset ensures proper system startup and that the host processor software and the REM switch firmware are synchronized. Initialize the REM switch. Perform the standard REM switch initialization by calling REMS_StdInit(). Use MII for the PHY mode and leave the clock enabled. A call to REMS_StdInit() may appear as follows: REMS_StdInit(REMS_MII, 0, REMS_Int_Line_2, REMS_Int_Line_1, REMS_Int_Line_0); Calling REM_StdInit() in this way is highly recommended for EtherCAT as it maps the priorities per what is expected for the EtherCAT version of the REMS Driver. 4. Set the synchronization offset value. Call REMS_ecatSetSyncOffsetValue() to inform the driver of the delay across the PHYs. This information is used to compensate for the propagation delay across the PHYs, because this information relates to maintaining synchronization using distributed clocks. No other functions declared in REMS_ECATinternals.h need to be called by the application. This driver assumes that both ports have identical PHYs and thus that the PHY delay values are the same. 5. Enable PHYs. Power up both PHYs via MII. Now that the REM switch is ready for network communication, the PHYs can be enabled, which allows packets to reach the REMS. 6. Initialize the EtherCAT slave stack. If the Beckhoff EtherCAT SSC is being used, call MainInit(). Otherwise, initialize the EtherCAT slave stack appropriate for the user system. 7. Start the EtherCAT slave stack main processing. If the Beckhoff EtherCAT SSC is being used, call MainLoop() according to the conditions provided in the associated documentation from Beckhoff Automation. Otherwise, start the EtherCAT slave stack that is in use. ETHERCAT INTERRUPT HANDLING The REM switch provides the ability to have three prioritized interrupt lines. The REM switch chip and this driver communicate frequently. The driver reads and writes to the REM switch and the REM switch requests interrupts to the driver for reads, writes, and other actions. Not all of these interrupts must be handled by the application. Most are handled internally by the driver. The remainder of the interrupts must be handled by the application, as shown in Table 6.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-8.png
   :align: center

A recommended function structure for handling interrupts from the REM switch follows. This example shows interrupts being internally handled by the driver and interrupts that are supplied to the application for handling. This function is intended to be called directly from the host processor interrupt service routine.

void HandleIntREMS(REMS_IntLine_t line) {

::

     REMS_stdIntEvent_t event;

::

     REMS_StdEvaluateInterrupt(line);
     do {
         // Interrupts for the driver are evaluated and handled here
         event = REMS_StdGetNextEvent(line);

::

         // Interrupts for the application are handled here
         switch (event) {
         case REMS_StdInt_Port_1_LinkChange:
         case REMS_StdInt_Port_2_LinkChange:
             // Call link change handler here
             break;

::

         case REMS_EcatInt_AL_Event_Change:
             PDI_Isr();      // Call stack handler
             break;

::

         case REMS_EcatInt_SYNC0_Event:
             Sync0_Isr();    // Call stack handler
             break;

::

         case REMS_EcatInt_SYNC1_Event:
             Sync1_Isr();    // Call stack handler
             break;

::

         case REMS_EcatInt_MII_MGT_Event:
             // Signal external process to handle MIIMI command here
             break;

::

         case REMS_EcatInt_Reset_Requested:
             // Reset host processor
             break;

::

         default:
             break;
         }
     } while (event != REMS_Int_None);

}

The driver requires the host processor to be configured for level sensitive interrupts on the interrupt lines. The application waits to acknowledge the actual interrupt until after HandleIntREMS() returns. If additional REM switch interrupts are generated while the current interrupts are being processed, the external CPU interrupt line remains high. When the CPU interrupt is acknowledged, a new CPU interrupt is requested, which ensures that all interrupt requests are processed. EtherCAT SLAVE STACK TO DRIVER INTERFACE Although this driver can be used with any stack, the driver is designed to work with Version 5.11 and Version 5.12 of the EtherCAT slave stack from Beckhoff Automation. All porting layer functions that the EtherCAT slave stack expects, such as HW_EscRead(), are defined in this driver. When using the EtherCAT SSC tool, the HW_ACCESS_FILE configuration parameter allows the user to specify the header file that contains the low level hardware access functions. Use this parameter in the SSC tool to specify the REMS_ECATHw.h file in this driver. The value for the HW_ACCESS_FILE parameter in the SSC tool may appear as follows: #include “inc/REMS_ECATHw.h” Included in the driver package is a sample SSC tool settings file called SSC_Tool_Settings.esp. Open this file with the SSC tool for an example of the settings that can generate the EtherCAT SSC. EEPROM Emulation The host processor is responsible for emulating the EEPROM that typically connects directly to the ESC. This emulation includes handling EEPROM read commands, write commands, and reload commands. A reload command is issued at system startup. The EtherCAT master commands the reload command at any time. While servicing the reload command, certain data from EEPROM must be placed in the EEPROM data register in packed form. MII MANAGEMENT INTERFACE Most ESCs can access registers on the connected PHYs via the MDIO and MDC lines. The REM switch does not have these signals, and thus does not have the ability to directly read or write registers on connected PHYs. ESC Register 0x0510 to Register 0x0515 allow the EtherCAT master to command the ESC to access the registers on the connected PHYs. Because the REM switch does not have the MDIO and MDC signals, the REM switch cannot fulfill the PHY register read or write requests. To accomplish the PHY register read or write, the REM switch requests that the host processor perform the PHY register read or write in its place. When an EtherCAT master generates a PHY register read or write, the REM switch generates a REMS_EcatInt_MII_MGT_Event event. This event signals the host processor to perform the PHY register read or write in the place of the ESC, and then provides the results of the operation. The application layer software must perform the action and indicate if the operation is successful or failed, as well as the result of the operation if successful. In this process, the MIIMI is emulated. Similarly, ESC Register 0x0301 and Register 0x0303 contain the number of receive errors that occurred. The REM switch does not have an RX_ERR pin to connect the RX_ERR signal from the PHYs. To report receive errors, the REM switch must periodically request the host processor to read the receive error register on the PHYs to keep Register 0x0301 and Register 0x0303 updated. The REM switch accomplishes this read through the MIIMI emulation mechanism. The REM switch generates a REMS_EcatInt_MII_MGT_Event event to begin the read of the receive error register on the indicated PHY. When the EtherCAT master issues an MIIMI request, or when the REM switch attempts to periodically read a receive error register from a connected PHY, a REMS_EcatInt_MII_MGT_Event event is generated. When this event is generated, the application calls REMS_ecatMiiEventParams(), declared in REMS_ECATHw.h, to obtain the parameters for the MIIMI command. After the command parameters are obtained, the command can be executed. When the application responds to a REMS_EcatInt_MII_MGT_Event event, the application may be responding to one of two functions. To determine whether the application is responding to a PHY register read or write from the EtherCAT master or to a periodic read of a PHY receive error register, examine the values in the variables populated by REMS_ecatMiiEventParams() after the application returns. The suggested process for responding to a REMS_EcatInt_MII_MGT_Event event is as follows: 1. Call REMS_ecatMiiEventParams() to retrieve the parameters for the REMS_EcatInt_MII_MGT_Event event. 2. Map the indicated PHY address to the actual PHY address. The EtherCAT master assumes that the PHY connected to Port 0 has Address 0 on the MDIO bus, and that the PHY connected to Port 1 has Address 1 on the MDIO bus. If this is not the case, remap the PHY addresses so that the intended PHY is accessed. The REM switch makes this same assumption when issuing periodic reads of the receive error registers. 3. Optional. Verify that the PHY register that is to be read or written is supported on the indicated PHY. Set a local error variable if not. a) If the REM switch is requesting the receive error register value from PHY 0, read the receive error register on the PHY attached to Port 0. Call REMS_ecatMiiReadComplete() and indicate if any errors occurred, the value of the receive error register if no errors occurred, and that the periodic receive error register read is complete (why parameter = 0). b) If the REM switch requests the receive error register value from PHY 1, read the receive error register on the PHY attached to Port 1. Call REMS_ecatMiiReadComplete() and indicate if any errors occurred, the value of the receive error register if no errors occurred, and that the periodic receive error register read is complete (why parameter = 0). c) If the EtherCAT master requests a PHY register read, read the indicated register address from the PHY at the remapped MDIO bus address. Call REMS_ecatMiiReadComplete() and indicate if any errors occurred, the value the value requested from the indicated register on the indicated PHY if no errors occurred, and that the standard PHY register read is complete (why parameter = 1). d) If the EtherCAT master requests a PHY register write, write the indicated PHY register value to the indicated PHY register at the remapped MDIO bus address. Call REMS_ecatMiiWriteComplete() and indicate if any errors occurred. Because the transaction on the MDIO/MDC lines can take a relatively large amount of time, avoid performing the PHY read or write inside the interrupt service routine that handles the REMS_EcatInt_MII_MGT_Event event. It is possible to receive a REMS_EcatInt_MII_MGT_Event event while REMS_EcatInt_AL_Event_Change, REMS_EcatInt_SYNC0_Event, and REMS_EcatInt_SYNC1_Event are disabled. Because of this ability, it is recommended to ensure that a REMS_EcatInt_MII\_ MGT_Event event is not serviced while the other events are disabled. The relatively large amount of time the MDIO transaction takes may prevent other events from being handled quickly enough during standard operation. EtherCAT SSC The EtherCAT SSC driver operates with the EtherCAT slave stack from Beckhoff Automation. There is no need to review this section if using a different slave stack. SSC Tool Settings The SSC tool settings file used to create the SSC for the RapID platform is included in this package. The user can modify this existing file or create a new settings file. Some settings in the SSC tool are restricted to maintain compatibility with this driver and ease integration. These settings are described in Table 7.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-9.png
   :align: center

::

   When selecting minimum or maximum addresses for process data reads and writes, maximum process data input/output sizes and minimum, default, and maximum addresses for mailboxes, bear in mind that the REM switch has 10 kB of RAM that can be used. This space is available to accommodate space for the input mailbox, output mailbox, triple buffered input process data, and triple buffered output process data. Pick all of the minimum, maximum, and default values so that there is enough RAM available for all operations. The SSC tool settings file sets the ALLOCMEM (size), FREEMEM (pointer), APPL_AllocMailboxBuffer (size), and APPL_FreeMailboxBuff (pointer) parameters to application specific functions. Unless the system requires something different, malloc() and free() can be used for these parameters.

   SSC Changes

To obtain correctly functioning code, minor changes are made to the SSC after the SSC tool produced the source code. The majority of these changes relate to the SSC not running correctly on a big endian host processor. These changes are detailed in this section. The user may or may not need to make the same changes when configuring the SSC tool, and the following changes are provided as a reference material. In ecatappl.c, lines 889 to 891, added: else |EEPROMReg &= ~ESC_EEPROM_ERROR_CRC;| In ecatslv.c, lines 2110 to 2114, added: DISABLE_ESC_INT(); In ecatslv.c, lines 2186 to 2190, added: ENABLE_ESC_INT(); In eoeappl.c, lines 145-150, replaced: switch ( ((ETHERNET_FRAME \*) pFrame)->FrameType ) with: switch ( SWAPWORD(((ETHERNET_FRAME \*) pFrame)->FrameType )) In eoeappl.c, lines 182 to 189, added: else {

::

   if(pSendFrame != NULL)
   {
     FREEMEM(pSendFrame);
     pSendFrame = NULL;
   }

} In eoeappl.c, lines 298 to 305, replaced: if ( SWAPWORD(pEoeInit->Flags1) & EOEINIT_CONTAINSMACADDR ) with: pEoeInit->Flags1 = SWAPWORD(pEoeInit->Flags1);

::

     if (pEoeInit->Flags1 & EOEINIT_CONTAINSMACADDR )

In esc.h, lines 91 to 95, replaced: #define ESC_EEPROM_ERROR_MASK 0x7800 with: #define ESC_EEPROM_ERROR_MASK 0x6000 In mailbox.h, lines 101 to 114, replaced: #define MBX_OFFS_TYPE 0 /**< \\brief Protocol type offset*/ #define MBX_MASK_TYPE 0x0F00 /**\ < \\brief Protocol type mask*/ #define MBX_SHIFT_TYPE 8 /**< \\brief Protocol type shift*/ #define MBX_OFFS_COUNTER 0 /**\ < \\brief Protocol counter offset*/ #define MBX_MASK_COUNTER 0xF000 /**< \\brief Protocol counter mask*/ #define MBX_SHIFT_COUNTER 12 /**\ < \\brief Protocol counter shift*/ with:

// ORIGINAL ^^^ #define MBX_OFFS_TYPE 0 /**< \\brief Protocol type offset*/ #define MBX_MASK_TYPE 0x000F /**\ < \\brief Protocol type mask*/ #define MBX_SHIFT_TYPE 0 /**< \\brief Protocol type shift*/ #define MBX_OFFS_COUNTER 0 /**\ < \\brief Protocol counter offset*/ #define MBX_MASK_COUNTER 0x00F0 /**< \\brief Protocol counter mask*/ #define MBX_SHIFT_COUNTER 4 /**\ < \\brief Protocol counter shift*/ In objdef.c, lines 890 to 895, replaced: if((((UINT16)pVarPtr) & 0x1) == 0x1) with: if((((UINT32)pVarPtr) & 0x1) == 0x1) In sdoserv.c, lines 508 to 513, replaced: pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] &= 0xFF00; with: pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] &= 0x00FF; In sdoserv.c, lines 527 to 540, replaced:

::

   pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET]  
   |=     SDOHEADER_SIZEINDICATOR     | SDOHEADER_TRANSFERTYPE   
   | completeAccess | ((MAX_EXPEDITED_DATA – 

 [2]_ << SDOHEADERSHIFT_DATASETSIZE) \| SDOSERVICE_INITIATEUPLOADRES; with:

::

   pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] |= SWAPWORD(SDOHEADER_SIZEINDICATOR | SDOHEADER_TRANSFERTYPE |completeAccess


   | ((MAX_EXPEDITED_DATA - ((UINT8)objLength)) << SDOHEADERSHIFT_DATASETSIZE) |

SDOSERVICE_INITIATEUPLOADRES); In sdoserv.c, lines 555 to 564, replaced: pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] \|= SDOHEADER_SIZEINDICATOR \| completeAccess \| SDOSERVICE_INITIATEUPLOADRES;

with: pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] \|= SWAPWORD(SDOHEADER_SIZEINDICATOR \| completeAccess \| SDOSERVICE_INITIATEUPLOADRES); In sdoserv.c, lines 572 to 577, replaced: pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] \|= SDOSERVICE_DOWNLOADSEGMENTRES; with: pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] \|= SWAPWORD(SDOSERVICE_DOWNLOADSEGMENTRES); In sdoserv.c, lines 583 to 588, replaced: pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] \|= SDOSERVICE_INITIATEDOWNLOADRES; with: pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] \|= SWAPWORD(SDOSERVICE_INITIATEDOWNLOADRES); In sdoserv.c, lines 597 to 602, replaced: pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] = SDOSERVICE_ABORTTRANSFER; with: pSdoRes->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] = SWAPWORD(SDOSERVICE_ABORTTRANSFER); In sdoserv.c, lines 629 to 634, replaced: UINT8 sdoHeader = pSdoInd->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] & SDOHEADER_COMMANDMASK; with: UINT8 sdoHeader = (pSdoInd->SdoHeader.Sdo[SDOHEADER_COMMANDOFFSET] & SDOHEADER_COMMANDMASK) >> SDOHEADER_COMMANDSHIFT; In sdoserv.c, lines 658 to 672, replaced: index = pSdoInd->SdoHeader.Sdo[SDOHEADER_INDEXHIOFFSET] & SDOHEADER_INDEXHIMASK;

::

       index <<= 8;
       index += pSdoInd->SdoHeader.Sdo[SDOHEADER_INDEXLOOFFSET]
      >> SDOHEADER_INDEXLOSHIFT;

/\*the variable subindex contains the requested subindex of the SDO service \*/ subindex = pSdoInd->SdoHeader.Sdo[SDOHEADER_SUBINDEXOFFSET]

::

      >> SDOHEADER_SUBINDEXSHIFT;

with: index = pSdoInd->SdoHeader.Sdo[SDOHEADER_INDEXHIOFFSET] & SDOHEADER_INDEXHIMASK;

index += (pSdoInd->SdoHeader.Sdo[SDOHEADER_INDEXLOOFFSET]

      SDOHEADER_INDEXLOSHIFT) & SDOHEADER_INDEXLOMASK;

/\*the variable subindex contains the requested subindex of the SDO service \*/

subindex = (UINT8)(pSdoInd->SdoHeader.Sdo[SDOHEADER_SUBINDEXOFFSET] >> SDOHEADER_SUBINDEXSHIFT) & SDOHEADER_SUBINDEXMASK;

In sdoserv.h, lines 94 to 116, replaced: #define SDOHEADER_COMMANDOFFSET 0 /**< \\brief Memory offset for the command*/ #define SDOHEADER_INDEXLOOFFSET 0 /**\ < \\brief Memory offset for the low Byte of the object index*/ #define SDOHEADER_INDEXHIOFFSET 1 /**< \\brief Memory offset for the high Byte of the object index*/ #define SDOHEADER_SUBINDEXOFFSET 1 /**\ < \\brief Memory offset for subindex*/ #define SDOHEADER_COMMANDMASK 0xFF /**< \\brief Mask to get the command Byte*/ #define SDOHEADER_INDEXLOSHIFT 8 /**\ < \\brief Shift to get the low Byte of the object index*/ #define SDOHEADER_INDEXHIMASK 0xFF /**< \\brief Mask to get the high byte of the object index*/ #define SDOHEADER_SUBINDEXSHIFT 8 /**\ < \\brief Shift to get the subindex*/ with: #define SDOHEADER_COMMANDOFFSET 0 /**< \\brief Memory offset for the command*/ #define SDOHEADER_INDEXLOOFFSET 0 /**\ < \\brief Memory offset for the low Byte of the object index*/ #define SDOHEADER_INDEXHIOFFSET 1 /**< \\brief Memory offset for the high Byte of the object index*/ #define SDOHEADER_SUBINDEXOFFSET 1 /**\ < \\brief Memory offset for subindex*/ #define SDOHEADER_COMMANDMASK 0xFF00 /**< \\brief Mask to get the command Byte*/ #define SDOHEADER_COMMANDSHIFT 8 /**\ < \\brief Shift to get the command Byte*/ #define SDOHEADER_INDEXLOSHIFT 0 /**< \\brief Shift to get the low Byte of the object index*/ #define SDOHEADER_INDEXLOMASK 0x00FF /**\ < \\brief Mask to get low Byte of the object index*/ #define SDOHEADER_INDEXHIMASK 0xFF00 /**< \\brief Mask to get the high byte of the object index*/ #define SDOHEADER_SUBINDEXSHIFT 0 /**\ < \\brief Shift to get the subindex*/ #define SDOHEADER_SUBINDEXMASK 0x00FF /\**< \\brief Mask to get the subindex*/ In coeappl.c, line 411, replaced TOBJ1C00 sSyncmanagertype = {0x04, {0x0102, 0x0304}}; with: TOBJ1C00 sSyncmanagertype = {0x04, {0x0201, 0x0403}}; Interrupt Enable and Disable Depending on the SSC tool settings used, the user application may be required to implement the ENABLE_ESC_INT() and DISABLE_ESC_INT() functions. It is important that implementation of these functions does not completely disable all interrupts coming from the REM switch. The REM switch occasionally requests interrupts that are internally handled by the driver. The purpose of ENABLE_ESC_INT() and DISABLE_ESC_INT() is to enable and disable the REMS_EcatInt_AL_Event_Change, REMS_EcatInt_SYNC0_Event, and REMS_EcatInt_SYNC1_Event events. As long as these events are disabled after a call to DISABLE_ESC_INT() and enabled after a call to ENABLE_ESC_INT(), the user system behaves properly. Application Programming Interface (API) Usage In the application, a maximum of two operational threads are allowed. One thread can act as the standard, background thread. This thread can use all API functions except those ending in Isr. The other thread is limited to API functions ending in Isr. The EtherCAT slave stack meets this requirement. If using the EtherCAT slave stack, it is recommended to call MainLoop() in the background of the application and call PDI_Isr(), Sync0_Isr(), and Sync1_Isr() from the interrupt handler. PDI_Isr(), Sync0_Isr(), and Sync1_Isr() only use API functions that end in Isr.

POWERLINK To set up a POWERLINK device, a TCP/IP protocol stack and a POWERLINK slave stack are necessary. It is recommended to use the open-source openPOWERLINK stack. This driver package is developed and tested using this POWERLINK slave stack. This REM switch driver and firmware software is developed with the REM switch hardware and the openPOWERLINK stack to handle all aspects of the POWERLINK protocol while operating as a controlled node (CN). The operating features include operation as a 100 Mbps, half-duplex, two-port hub and REM switch firmware and hardware assisted poll request (PREQ) and poll response (PRES) autoresponse. In addition, it is possible to add standard TCP/IP features, such as a web server. Because the POWERLINK protocol tightly controls when traffic is allowed to enter the network, the openPOWERLINK stack primarily manages this operation with the REM switch firmware providing autoresponse features during the asynchronous phase. POWERLINK INITIALIZATION To initialize a POWERLINK device, perform the following actions: 1. Configure the external interrupt input pins on the host processor. 2. Assert the REM switch reset line and wait for it to become ready. 3. Call REMS_StdInit() and provide the PHY mode (currently MII), the clock enable flag (set to 0), and the REM switch interrupt lines for use as the three priority levels. 4. Call REMS_StdAssignInterrupt and REMS_StdEnableInterrupt to establish the REM switch hardware interrupt configuration: REMS_StdAssignInterrupt(REMS_Int_Port_1_Link_Change, REMS_Int_Line_0); REMS_StdAssignInterrupt(REMS_Int_Port_2_Link_Change, REMS_Int_Line_0); REMS_StdAssignInterrupt(REMS_Int_Queue_0_Packet_Ready, REMS_Int_Line_1); REMS_StdEnableInterrupt(REMS_Int_Port_1_Link_Change); REMS_StdEnableInterrupt(REMS_Int_Port_2_Link_Change); REMS_StdEnableInterrupt(REMS_Int_Queue_0_Packet_Ready); 5. Call REMS_StdSetMacAddress() to set the MAC address for the system. There are three MAC address parameters for this function. For POWERLINK, supply the same MAC address for each of the MAC address parameters. 6. Call REMS_StdSetPortState() for each of the switch ports with REMS_PORT_FORWARDING and the port number as the arguments. POWERLINK INTERRUPT HANDLING When REMS_StdInit() is called, the interrupt outputs are assigned high, medium, and low priority positions according to the passed in parameters. The REM switch driver assigns interrupt sources to interrupt lines as shown in Table 8.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-10.png
   :align: center

The low level interrupt handler must be aware of which REM switch interrupt line caused the interrupt. The low level interrupt handler may then call the REM switch event handler function. After this function is called, all pending interrupts are evaluated and can be handled individually in a loop. The recommended REM switch interrupt handler for POWERLINK is as follows: /\* Low level hardware ISR's: \*/ void REMS_Interrupt_Line0(void) {

::

   HandleIntREMS(0);

}

void REMS_Interrupt_Line1(void) {

::

   HandleIntREMS(1);

}

void REMS_Interrupt_Line2(void) {

::

   HandleIntREMS(2);

}

/\* Common code to handle interrupts: \*/ void HandleIntREMS(REMS_IntLine_t line) {

::

   tOplkError rv;
   REMS_CommonEnetPort_t   rcvPort;
   static unsigned char dummyBuffer[1500];
   static int dummyCount;

::

   REMS_stdIntEvent_t event;

::

   REMS_StdEvaluateInterrupt(line);
   do {
     event = REMS_StdGetNextEvent(line);
     switch (event) {
       case REMS_StdInt_Port_1_LinkChange:
       case REMS_StdInt_Port_2_LinkChange:
         /* .... manage PHY link state as described below .... */
         break;

::

       case REMS_Int_Queue_0_Packet_Ready:
           rv = edrv_receiveBuffer();
           if (rv) {
             // ERROR CASE, read the frame and dump it...
             REMS_StdReadPacket(&rcvPort, &dummyBuffer, &dummyCount);
           }
           break;

::

       /* Add other interrupt event cases here as needed */

::

       default:
         break;
     }
   } while (event != REMS_Int_None);

} loop.

POWERLINK PHY LINK STATE INTERRUPT HANDLING When the REM switch detects a link up or down event from the PHY (because the link signal output from the PHY is required to be connected to REM switch link status input), the link speed and duplex settings must be written to the REM switch by the host processor. The REM switch does not determine these settings on its own. As a result, when the Ethernet link is functional (when either the REMS_StdInt_Port_1_LinkChange or the REMS_StdInt_Port_2_LinkChange interrupt event occurs), read the link speed, duplex from the PHYs, and write to the REM switch using REMS_StdSetSpeedAndDuplex(). In the case of POWERLINK, fix the speed and duplex at 100 Mbps half duplex operation. An error is likely to occur if the PHY reports something other than 100 Mbps half duplex. POWERLINK RECEIVED PACKET INTERRUPT HANDLING When a packet is received, the REM switch issues a REMS_Int_Queue_0_Packet_Ready interrupt to the processor. In response, call edrv_receiveBuffer(). This function asks the POWERLINK stack for a buffer and, using REMS_StdReadPacket(), reads the packet from the hardware. The remainder of the function is responsible for passing the packet into the stack logic, at which point stack logic takes over control of functionality. Functions such as edrv_receiveBuffer() are not typically present in the standard REMs driver package, because it is specific to openPOWERLINK and is one part of a porting layer the user must provide. An example version is provided in the porting_layer_helpers directory for edrv-fido1100.c. There are several functions contained in this file that the user may use. POWERLINK PACKET TRANSMISSION Because the REM switch POWERLINK implements an autoresponse, POWERLINK is always monitoring received packets. If POWERLINK detects a frame that requires an immediate response, it provides a response with no software intervention. This response allows for a very fast response, but requires that the response frame must already be on-board. The openPOWERLINK stack accounts for this factor and uses the edrv_sendTxBuffer() and edrv_updateTxBuffer() functions. Transmission of frames to the REM switch device is still accomplished with REMS_StdXmitPacket().

REGISTER MAPS AND DEFINITIONS
-----------------------------

Table 9 and Table 10 detail the register mapping and definitions for the fido5100 and fido5200. The user of the REM switch typically does not need to modify any values in these registers because the API described in this user guide interacts with the registers as required. Note that the register maps and definitions provided in this user guide are provided as reference. It is not intended for the user to read and write registers in the exact ways defined, but to use the API defined in |image1|\ the driver source code. For direct address registers, when accessing registers, the contents are swapped when read and unswapped when written. When accessing memory, the contents are swapped when read or written.

Table 11. Direct Address Register Definitions


|image2|

Table 12. Indirect Address Host Register Definitions


|image3|

DIRECT ADDRESS REGISTERS
------------------------

Table 13. Host Queue n Read Registers—Address 0x00, Address 0x04, Address 0x08, and Address 0x0C


|image4|

Reads from the direct address registers retrieve data from the queue that was read from the memory and pointed to by the current value of the read queue address register. These registers are read only. Writes have no effect.

Table 14. Host Queue n Write Registers—Address 0x00, Address 0x04, Address 0x08, and Address 0x0C


|image5|

Table 15. Host Read Queue n Data Head—Address 0x18 and Address 0x1C


|image6|

.. [1]
   interrupt, section (".rem"

.. [2]
   UINT8)objLength

.. |EEPROMReg &= ~ESC_EEPROM_ERROR_CRC;| image:: https://wiki.analog.com/_media/EEPROMReg &= ~ESC_EEPROM_ERROR_CRC;
.. |image1| image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-13.png
.. |image2| image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-11.png
.. |image3| image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-12.png
.. |image4| image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-13.png
.. |image5| image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-13.png
.. |image6| image:: https://wiki.analog.com/_media/resources/technical-guides/rssug-15.png
