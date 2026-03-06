Modbus/TCP Quickstart Guide, ERD or ADIN2299
============================================

Overview
--------

FEATURES
~~~~~~~~

Modbus TCP

EVALUATION KIT CONTENTS
~~~~~~~~~~~~~~~~~~~~~~~

-  1 baseboard with the RPG2 module installed with the protocol specific software preloaded 12V,
-  1 A power supply with outlet adapters
-  Ethernet cable
-  USB cable

EQUIPMENT NEEDED
~~~~~~~~~~~~~~~~

-  EV-RPG2 Evaluation Board
-  1 PC, using 2 PCs may be easier

SOFTWARE NEEDED
~~~~~~~~~~~~~~~

-  Network Interface Example Application Suite
-  Modbus server tester utility within the Modbus TCP toolkit
-  Windows WinPcap
-  DHCP server (optional)

General Description
-------------------

The RapID Platform Generation 2 (RPG2) module is a pretested, industrial network interface designed to manage industrial protocols and network traffic. The RPG2 module supports PROFINET®, PROFINET isochronous real-time (IRT), Ethernet/IP®, Ethernet/IP with device level ring (DLR), EtherCAT®, and Modbus/TCP. The RPG2 module uses the Unified Interface to communicate with different protocols. The Unified Interface is a custom protocol by Analog Devices, Inc., that allows interaction between an application processor and the RPG2 module. The Unified Interface is agnostic of the industrial protocol. The Unified Interface ensures that the application processor hardware and software interface is not required to change when switching or updating protocols. The RPG2 module connects to an application processor via a universal asynchronous receiver transmitter (UART), Ethernet, or serial peripheral interface (SPI). The EV-RPG2 evaluation kit provides end to end evaluation of the communication path from the application processor to the programmable logic controller (PLC) over the industrial Ethernet interface by using the Network Interface Example Application Suite. This user guide describes how to use the EV-RPG2 evaluation kit to set up and run a PLC example application. For the example described in this user guide, the application processor is a PC and communicates to the RPG2 module via an Ethernet port.

TABLE OF CONTENTS
~~~~~~~~~~~~~~~~~

::

   *Features 1
   *Evaluation Kit Contents  1
   *Equipment Needed 1
   *Software Needed  1
   *Revision History 2
   *EVALUATION KIT SETUP FOR MODBUS/TCP  3
   *NETWORK INTERFACE APPLICATION SUITE WITH MODBUS Master   5
   *SETTING UP THE APPLICATION PROCESSOR SIMULATOR SOFTWARE  5
   *SETTING UP THE MODBUS/TCP NETWORK WITH MODBUS SERVER TESTER UTILITY  7
   *NEXT STEP: Design Phase  12

REVISION HISTORY
----------------

::

   *8/2022—Revision 0: Initial Version

EVALUATION KIT SETUP FOR MODBUS/TCP
-----------------------------------

Refer to the EV-RPG2 User Guide to set up the hardware. Note that the default link type is determined by the pins. When a change of link type to UART is required, refer to the RPG2 Hardware Design Integration Guide. See Figure 1 and Figure 2 for the setup for running the MODBUS/TCP application example with the default link type for one PC or two PCs, respectively. Use one PC if having both the Modbus server tester utility and the network interface example application suite (ni-example-app.exe) on one PC is acceptable. Use two PC(s) if there is a requirement to clearly distinguish between the two applications. For the rest of this user guide, the two PC setup is used for setting up the Modbus server tester utility and for running the network interface example application suite (ni-example-app.exe). When LED3 and LED4 are solid green, it indicates that the startup process is complete.

Figure 1. MODBUS Example Application Setup, Ethernet (Default) Link with One PC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_1.png
   :align: center
   :width: 400px

Figure 2. MODBUS Example Application Setup, Ethernet (Default) Link with Two PCs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NETWORK INTERFACE APPLICATION SUITE WITH MODBUS MASTER

.. image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_2.png
   :align: center
   :width: 400px

Enable Communication between the application processor and the RPG2 module by using USB virtual COM port or Ethernet port. In addition to the RPG2 module evaluation kit, users must have the following items (at a minimum):

::

   • A PC running the network interface example application suite (ni-example-app.exe).
   • Modbus server tester utility. This utility comes with the Modbus® TCP toolkit. 
   • DHCP server (if DHCP mode is selected for IP configuration)

SETTING UP THE APPLICATION PROCESSOR SIMULATOR SOFTWARE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Obtain the network interface example application suite from the Analog Devices Chronous Developer Portal.

-  Log in to your myAnalog account under the MYANALOG tab found on the main Analog Devices webpage (www.analog.com) and then go to the Analog Devices Chronous Developer Portal. Note that you must have a myAnalog account to access this portal.

-  Select the RapID Platform Generation 2 (RPG2) tab.

-  Click the RPG2 Network Interface Example Application Suite (ZIP) link.

-  Review the Terms and Conditions and accept.

-  Extract the contents of the .zip file. The extracted folder includes the ni-example-app.exe file that users must run from their command line. (Figure 3)
-  To see the syntax to start up the example application using any link type, type ni-example-app.exe –h in the command line.
-  To see the available Ethernet devices from the command line prompt, enter ni-example-app.exe -l ETH -n and a list of available Ethernet NICs will display. Running this command gives the network device numbers in the following format: XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXXXXXX. Use this list along with the Network and Sharing Center name in Windows® to determine which of the listed numbers to use.
-  For IP address configuration, user can select between DHCP by using command line option “--enable-dhcp” or static IP address by using command line option “--static-ip ipaddress subnet gateway dns1 dns2 domain”
-  Once all the information is known, enter the command:

**ni-example-app.exe -l ETH -n XXXXXXXX-XXXXXXXX-XXXX-XXXXXXXXXXXX --static-ip 192.168.23.105 255.255.255.0 and it will run the proper initialization and application processor functionality. Note that if you see FATAL Bad Memory Block while running the network interface example application suite, ensure that you have the most updated version of Windows® WinPcap on your PC. The NIC identifier begins with \\Device\\NPF\_.**

\**NOTE: If a UART is going to be used for the initalization, then the proper command will be as follows. ni-example-app.exe -l UART -c COMx --static-ip 192.168.23.105 255.255.255.0. The IP Address is arbitrary in this example \*\*

Figure 3. Network Interface Example Application Suite

.. image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_3.png
   :align: center
   :width: 400px

SETTING UP THE MODBUS/TCP NETWORK WITH MODBUS SERVER TESTER UTILITY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example uses the Modbus server tester utility on the PC. This application example uses the configuration described in Table 1. This configuration defines three items with different types of inputs and outputs. Item 500 defines 2 bytes of digital inputs and 2 bytes of digital outputs that are mapped to 16-bit coils and 16-bit input registers. Item 501 defines 4 bytes of analog inputs and 4 bytes of analog outputs that are mapped as two 2 byte values placed back to back in the respective register space. Item 502 defines a register output of 2 bytes that is mapped to one holding register.

For more information on items, refer to the RPG2 I/O Configuration Tool User Guide. This section provides instructions for setting up and using the RPG2 module with the link type set to Ethernet. The test network is set up as shown in the Figure 4 diagram. Note that the equipment may differ with respect to the master used for Modbus/TCP. Modbus/TCP has built in flexibility to allow utilization of the Modbus/TCP protocol using PLCs or using tools written for a PC. This example uses a Modbus server test.

.. image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_4.png
   :align: center
   :width: 800px

When the RPG2 module is initialized, use the following steps to connect to the RPG2 module using the Modbus server tester utility. 1. Open the Modbus server tester utility (see Figure 5).

Figure 5. Slave Configuration 2. In the IP Address field, enter the IP address of RPG2 module. Set the slave address to 00 default address used to connect to a RPG2 module. |image1| 3. Click OK. The Modbus/TCP tester utility connects to the RPG2 module (see Figure 6).

Figure 6. Modbus Server Connected 4. Write data to the LSB of Item 500. Access Item 500 through Modbus/TCP coil reads and writes (Function Code 01 and Function Code 05), as well as discrete input reads (Function Code 02). Use Function Code 05 to write to the LSB. |image2| 5. Click Tests, and then click Send New Frame to bring up the window shown in Figure 7.

Figure 7. Modbus Function Codes 6. Highlight 05 Write Single Output and click Data Wizard to bring up the window shown in Figure 8.

|image3|\ |image4|

Figure 8. Writing to Coil |image5| 7. Use this function code to change the value of a single coil. Changing the coil output bit affects the LSB of the digital output data. Note that when looking at the output of the ni-example-app.exe application, Coil 0 to Coil 7 are mapped to the most significant byte of Item 500, and Coil 8 to Coil 15 are mapped to the least significant byte of Item 500. 8. Change the output address to 0x0008 and click Finish. |image6| 9. Ensure that 05 Write Single Output is still highlighted and click Send to change the LSB of Item 500 to 1. Observe this change in value in the ni-example-app.exe console output. This item change reflects the new value of the coil at 0x0008. Note that the item A value (which is item 500) changes to 0x0001 as shown in Figure 10

10. ni-example-app echoes data from all 16 coils back on the discrete inputs. Use Function Code 02, highlight the 02 Read Discrete Inputs box, and click Data Wizard to read back the value written on the coils on the corresponding discrete inputs. The window shown in Figure 9 appears.

|image7| Figure 9. Function Code 2

11. Enter 0008 in the Starting Address text field and click Finish. The log from the Modbus server tester utility reflects the change in value. Figure 11 shows a log for Function Code 05 and Function Code 02.

.. image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_11.png
   :align: center

Figure 11. Result of Function Code 2 12. Keep the 05 Write Single Output highlighted and change the Output Value to OFF (see Figure 12) to change the value of the coil again.

.. image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_12.png
   :align: center

Figure 12. Function Code 5 13. Click Finish. 14. Ensure that 05 Write Single Output is still highlighted and click Send. The value in the ni-example-app console window changes. Note that the item A value changes back to 0x0000 (see Figure 13).

.. image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_13.png
   :align: center

15. Use Function Code 02 discrete inputs to read back the value that was written to the bit at Address 0x0008. See the function code in the log of the Modbus server tester utility. The user has now manually toggled the LSB of Item 500 data using the Modbus Server Tester utility

.. image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_14.png
   :align: center

Figure 14. Resulting Toggle in Master Screen

NEXT STEP: DESIGN PHASE

When the module is initialized and configured to use Modbus/TCP inputs and outputs, move on to the next phase of the design. For more information of how to progress, consult the following documents:

::

   • The RPG2 Hardware Design Integration Guide explains how to embed and integrate the module for use into the system. The RPG2 Hardware Design Integration Guide also includes: 
   • Detailed descriptions of the signals on the module. 
   • Information about the ac, dc, thermal, and power requirements.
   • Further details about the host interface. 
   • The pin configuration of the RPG2 module. 
   • The RPG2 I/O Configuration Tool User Guide explains how to create a customized input and output footprint for the system. 

• The RPG2 Unified Interface User Guide explains how to interact with the Analog Devices RPG2 module (embedded or otherwise) via the Unified Interface. The Unified Interface is how an application processor communicates with a network interface module by means of a UART, a serial-parallel interface (SPI), or Ethernet. The Unified Interface is the custom protocol that allows interaction between an application processor and the RPG2 module. When the Unified Interface commands are integrated into the application software, the solution takes care of the Industrial Ethernet protocol communication.

All this documentation is provided on the Analog Devices Chronous Developer Portal under the RapID Platform Generation 2 (RPG2) tab > Tools and Documentation area. The standard Analog Devices configuration for Modbus/TCP uses the three items detailed in Table 1.

Note that the needs of a system are not typically encompassed in the default configuration data that is provided in the network interface module. The configuration tool allows the user to create a configuration that fits the needs of a particular system

::

     ESD Caution 

ESD (electrostatic discharge) sensitive device. Charged devices and circuit boards can discharge without detection. Although this product features patented or proprietary protection circuitry, damage may occur on devices subjected to high energy ESD. Therefore, proper ESD precautions should be taken to avoid performance degradation or loss of functionality. Legal Terms and Conditions By using the evaluation board discussed herein (together with any tools, components documentation or support materials, the “Evaluation Board”), you are agreeing to be bound by the terms and conditions set forth below (“Agreement”) unless you have purchased the Evaluation Board, in which case the Analog Devices Standard Terms and Conditions of Sale shall govern. Do not use the Evaluation Board until you have read and agreed to the Agreement. Your use of the Evaluation Board shall signify your acceptance of the Agreement. This Agreement is made by and between you (“Customer”) and Analog Devices, Inc. (“ADI”), with its principal place of business at One Technology Way, Norwood, MA 02062, USA. Subject to the terms and conditions of the Agreement, ADI hereby grants to Customer a free, limited, personal, temporary, non-exclusive, non-sublicensable, non-transferable license to use the Evaluation Board FOR EVALUATION PURPOSES ONLY. Customer understands and agrees that the Evaluation Board is provided for the sole and exclusive purpose referenced above, and agrees not to use the Evaluation Board for any other purpose. Furthermore, the license granted is expressly made subject to the following additional limitations: Customer shall not (i) rent, lease, display, sell, transfer, assign, sublicense, or distribute the Evaluation Board; and (ii) permit any Third Party to access the Evaluation Board. As used herein, the term “Third Party” includes any entity other than ADI, Customer, their employees, affiliates and in-house consultants. The Evaluation Board is NOT sold to Customer; all rights not expressly granted herein, including ownership of the Evaluation Board, are reserved by ADI. CONFIDENTIALITY. This Agreement and the Evaluation Board shall all be considered the confidential and proprietary information of ADI. Customer may not disclose or transfer any portion of the Evaluation Board to any other party for any reason. Upon discontinuation of use of the Evaluation Board or termination of this Agreement, Customer agrees to promptly return the Evaluation Board to ADI. ADDITIONAL RESTRICTIONS. Customer may not disassemble, decompile or reverse engineer chips on the Evaluation Board. Customer shall inform ADI of any occurred damages or any modifications or alterations it makes to the Evaluation Board, including but not limited to soldering or any other activity that affects the material content of the Evaluation Board. Modifications to the Evaluation Board must comply with applicable law, including but not limited to the RoHS Directive. TERMINATION. ADI may terminate this Agreement at any time upon giving written notice to Customer. Customer agrees to return to ADI the Evaluation Board at that time. LIMITATION OF LIABILITY. THE EVALUATION BOARD PROVIDED HEREUNDER IS PROVIDED “AS IS” AND ADI MAKES NO WARRANTIES OR REPRESENTATIONS OF ANY KIND WITH RESPECT TO IT. ADI SPECIFICALLY DISCLAIMS ANY REPRESENTATIONS, ENDORSEMENTS, GUARANTEES, OR WARRANTIES, EXPRESS OR IMPLIED, RELATED TO THE EVALUATION BOARD INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT WILL ADI AND ITS LICENSORS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT, OR CONSEQUENTIAL DAMAGES RESULTING FROM CUSTOMER’S POSSESSION OR USE OF THE EVALUATION BOARD, INCLUDING BUT NOT LIMITED TO LOST PROFITS, DELAY COSTS, LABOR COSTS OR LOSS OF GOODWILL. ADI’S TOTAL LIABILITY FROM ANY AND ALL CAUSES SHALL BE LIMITED TO THE AMOUNT OF ONE HUNDRED US DOLLARS ($100.00). EXPORT. Customer agrees that it will not directly or indirectly export the Evaluation Board to another country, and that it will comply with all applicable United States federal laws and regulations relating to exports. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts (excluding conflict of law rules). Any legal action regarding this Agreement will be heard in the state or federal courts having jurisdiction in Suffolk County, Massachusetts, and Customer hereby submits to the personal jurisdiction and venue of such courts. The United Nations Convention on Contracts for the International Sale of Goods shall not apply to this Agreement and is expressly disclaimed. ©2022 Analog Devices, Inc. All rights reserved. Trademarks and registered trademarks are the property of their respective owners.

::

     UG16482-0-2/19(0) 

.. |image1| image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_5.png
.. |image2| image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_6.png
.. |image3| image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_7.png
.. |image4| image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_8.png
.. |image5| image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_8.png
.. |image6| image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_9.png
.. |image7| image:: https://wiki.analog.com/_media/resources/quick-start/modbus_image_10.png
