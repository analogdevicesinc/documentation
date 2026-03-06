A2B CommChannel Integartion Guide
=================================

Introduction
============

This document describes the usage of A2B communication channel module for inter-processor communication over A2B. The module enables exchange of control and command messages between the Host and a Sub node processor using the Mailbox feature of A2B Transceivers.

Scope
-----

This document is intended to assist the application developers integrating the communication channel module to their system.

Specifications
==============

Target Platform
---------------

A2B communication channel is developed as a generic C module and hence can be ported to any platform. It is by default intended to be run on a smart Sub consisting of a controller connected to A2B Sub transceiver.

Features
--------

A2B Communication channel has the following features

-  Support for communication over mailbox between Main and Sub nodes
-  Configurable communication message size
-  Segmentation and Re-assembly of messages greater than Mailbox transmission size of 4 bytes
-  Non-Blocking Transmission APIs
-  Generic C implementation and hence portable across platform

Dependencies
------------

The A2B communication channel does not have any dependencies on the smart Sub node controller it runs on. However, at the system level, to communicate to the Main node the communication channel must also be running on the controller connected to the A2B Main transceiver and a suitable A2B stack capable of configuring and discovering the network. ADI A2B Stack Software provided by ADI has communication channel feature integrated. It enables quick and easy integration with a smart Sub running communication channel for exchanging messages via mailbox. For more details on utilizing the ADI A2B Stack Software for communicating over mailbox refer to the :doc:`A2B Stack user guide </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>`. Alternatively, if the host controller on Main node runs a non-ADI stack the communication channel needs to be ported onto the Main node controller. The steps for the same are provided in :doc:`Porting instructions </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` section.

Communication Channel Architecture
==================================

The Communication Channel (CommCh) architecture is as shown in :doc:`Figure 1 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/communication_channel_architecture.png
   :align: center

.. container:: centeralign

   \ **Figure 1:** Communication Channel Architecture


The communication channel component interfaces to the application using the API functions. The communication channel executes the platform dependant I2C communication using the PAL layer. The framework must also implement the PAL for the communication channel. It creates a communication channel instance and passes the PAL context associated for the instance. Application also requests for new transmission of messages via API. All the APIs are handled by the API interface of communication channel. The engine block of communication channel is responsible for framing/de-framing of messages from application. During transmission it segments the message received from application into segments of size 4 bytes to be transmitted over mailbox using the PAL layer. Additional protocol header information is appended for assembly and error checking at the receiver. During reception the engine processes every 4-byte chunk received from mailbox and assembles the chunks into a complete message after checking the validity of each chunk based on the protocol headers. All status information is given to the application via call-backs. It is used to inform applicable of new message received, the status of a transmission request and other error information. The communication channel works in a non-blocking mode which means that application must periodically tick the communication channel. On this tick the periodic polling of mailbox interrupts from A2B transceiver is done over the I2C bus using the PAL layer. During transmission after a 4-byte chunk is written to the local mailbox, polling is used to detect the mailbox empty interrupt which indicates that the Main has read the data. On receiving this interrupt, the next 4-byte chunk from the message is transmitted. Polling is also used to check for mailbox full interrupt which indicates that new data has been written from Main. On receiving this interrupt data from mailbox is read and passed to communication engine for further processing.

Programmers Reference
=====================

Files
-----

Communication channel consists of source and header files. The header files are available in the folder *‘ADI_A2B-SSPlus_Software-RelX.Y.Z/Target/a2bcommchannel/inc/ ’* in the release package and the source folders in *‘ADI_A2B-SSPlus_Software-RelX.Y.Z /Target/a2bcommchannel/src/’*.

Header Files
~~~~~~~~~~~~

The header files that need to be included by the Sub application are as explained below

-  *adi_a2b_commch_interface.h* - Contains the message identifiers that are reserved to be exchanged by A2B Main plugin of A2B stack on the Main node with communication channel on Sub nodes. User should not modify these macros. Macros if any required for custom messages to be exchanged between Sub and Main should be declared as part of application header files.
-  *adi_a2b_commch.h* - Contains the structures, data types and API definitions related to the APIs.
-  *regdefs.h* – This file contains all the A2B register definitions macros and masks for all the A2B chip registers. This file is available in the example communication channel Sub project in the path *‘ADI_A2B-SSPlus_Software-RelX.Y.Z/Target/examples/advancedapp/mboxcommch/a2b-sc59x-commch-smartslv/app/inc’*.
-  *ctypes.h* – This file contains the basic C data type definitions used by the communication channel. This file is available in the example communication channel Sub project in the path *‘ADI_A2B-SSPlus_Software-RelX.Y.Z/Target/examples/advancedapp/mboxcommch/a2b-sc59x-commch-smartslv/pal/inc/platform/a2b’*.

Source Files
~~~~~~~~~~~~

The source files required by to be included in the Sub are as below

-  *adi_a2b_commch_engine.c* - Contains the functions related to the communication engine. The communication engine runs the framing/de-framing protocol.
-  *adi_a2b_commch.c* - Contains the APIs related to the communication channel. It also contains the functions related to the polling and mailbox transmission & reception interface calls to PAL layer.

API Functions
-------------

This various API functions to be used on the Sub node and their purpose are summarized in below Table.

+--------------------------+---------------------------------------------------------+
| **API Function**         | **Purpose**                                             |
+==========================+=========================================================+
| adi_a2b_CommChPalInit    | Create a communication channel PAL context              |
+--------------------------+---------------------------------------------------------+
| adi_a2b_CommChCreate     | Create an instance of communication channel             |
+--------------------------+---------------------------------------------------------+
| adi_a2b_CommChDestroy    | Destroy an instance of communication channel            |
+--------------------------+---------------------------------------------------------+
| adi_a2b_CommChTxMsg      | Send a message over communication channel               |
+--------------------------+---------------------------------------------------------+
| adi_a2b_CommChTick       | Tick the communication channel instance                 |
+--------------------------+---------------------------------------------------------+
| adi_a2b_CommChSetFraming | Set the framing of an instance of communication channel |
+--------------------------+---------------------------------------------------------+
| adi_a2b_CommChGetFraming | Get the framing of an instance of communication channel |
+--------------------------+---------------------------------------------------------+

.. container:: centeralign

   \ **Table:** API functions summary


The detailed description of the API functions is provided in the API reference document. Refer to “Communication Channel Sub” sub-section under “Communication Channel” section in API reference document as shown in :doc:`Figure 2 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`.



|image1|

.. container:: centeralign

   \ **Figure 2:** API reference document


API Data Types
--------------

The detailed description of the Data Structures, Enumerations are provided in the API reference document. Refer to “Communication Channel Sub” sub-section under “Communication Channel” section in API reference document as shown in :doc:`Figure 2 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`.

Configurable macros
-------------------

The detailed description of the configurable macros in CommCh Engine and CommCh are provided in the API reference document. Refer to “Communication Channel Engine” & “Communication Channel Sub” sub-section under “Communication Channel” section in API reference document as shown in :doc:`Figure 2 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`.

Application Integration
=======================

This section explains the flow of initializing and communicating using the communication channel in the application on Sub. Ensure that the communication channel source and include files as explained in :doc:`Files </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` section is included in the Sub project.

Initialization
--------------

The application information structure used in code snippets below is as shown in :doc:`Code Snippet 1 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`. It contains the communication channel related structures to be maintained by the application.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/application_information_structure_for_communication_channel.png
   :align: center

.. container:: centeralign

   \ **Code Snippet 1:** Application Information Structure for communication Channel


The steps to initialize a communication channel on Sub node is as follows. The :doc:`Code Snippet 2 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` shows the same.

::

     * Application should define the PAL function for regwrite, regRead and timer functions specific to the platform. 
   *       Next a communication channel context must be created with the I2C PAL function pointers for the platform using the //adi_a2b_CommChPalInit// API. 
   *       Next the communication channel instance should be created specifying the required configuration using the //adi_a2b_CommChCreate// API. The configuration should specify the memory for the instance and application callback for handling the events. The A2B Sub node transceiver local I2C address is specified using the **ADI_A2B_COMMCH_SLVNODE_I2C_ADDR** macro. The context for the Communication channel and default Rx and Tx mailbox are also to be specified.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/initialization_of_communication_channel_at_Slave.png
   :align: center

.. container:: centeralign

   \ **Code Snippet 2:** Initialization of Communication Channel at Sub


Handling Events
---------------

The *a2b_app_CommChCallBk* callback registered during initialization should handle the various events as shown in below code snippet 3.


|image2|

.. container:: centeralign

   \ **Code Snippet 3:** Communication Channel Event handling at Sub


Periodic Ticking
----------------

The communication channel instance should be periodically ticked by calling the *adi_a2b_CommChTick* API as shown in :doc:`Code Snippet 4 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`. This performs the following activities

-  Schedules the 4-byte chunk I2C mailbox writes of any messages pending for transmission.
-  Check for the timeout of last transmitted 4-byte chunk over mailbox.
-  Polling for mailbox interrupts and initiate mailbox read once data is received.

This should be called at a period lesser than or equal to the interrupt polling period **ADI_A2B_COMMCH_INTR_POLLING_PERIOD** which is set to 1ms by default.


|image3|

.. container:: centeralign

   \ **Code Snippet 4:** Periodic Ticking at Sub


Transmission of messages
------------------------

Application can initiate the transmission over the communication channel using the *adi_a2b_CommChTxMsg* API as shown in :doc:`Code Snippet 5 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`. The result of the transmission is indicated via a communication channel event through a callback to the application which is registered during initialization. An event type of **A2B_COMMCH_EVENT_TX_DONE** indicates confirmation of transmission and an event type of **A2B_COMMCH_EVENT_TX_TIMEOUT** indicates a timeout. The code snippet is shown in :doc:`Handling Events </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` section as part of handling events.


|image4|

.. container:: centeralign

   \ **Code Snippet 5:** Transmission over Communication Channel at Sub


Reception of messages
---------------------

Any new message received is indicated to application by the communication channel via the application callback with the event type A2B_COMMCH_EVENT_RX_MSG. It is as explained as part of :doc:`Handling Events </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` section.

Enable/Disable Framing
----------------------

Application can enable or disable framing for a communication channel instance using the *adi_a2b_app_CommChSetFraming* API as shown in :doc:`Code Snippet 6 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`.


|image5|

.. container:: centeralign

   \ **Code Snippet 6:** CommCh Set Framing


Application can get the current framing information for a communication channel instance using the *adi_a2b_app_CommChGetFraming* API as shown in :doc:`Code Snippet 7 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`.



|image6|

.. container:: centeralign

   \ **Code Snippet 7:** CommCh Get Framing


Sequence Diagram
----------------

The communication channel is intended to be run a Sub node however it can be ported to a Main node as well. See :doc:`Porting Instructions </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` section for more details. The :doc:`Figure 3 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` shows the sequence diagram of a communication handshake between Main and Sub nodes using communication channel.


|image7|

.. container:: centeralign

   \ **Figure 3:** Main Sub Message Handshake Sequence


The sequence of events is as described below.

::

     * The Main node software on start-up performs the A2B network discovery and configures all the Sub nodes on start up. It configures the required mailbox register settings in all Sub nodes for communication channel. The mailbox registers    MBOX0_CTL and MBOX1_CTL should be configured to the values 0x3D and 0x3F to ensure the following configurations of mailbox:  \\  * Mailbox data length should be 4 bytes \\  * Mailbox full and empty interrupts should be enabled \\  * Mailbox 0 should be configured as receive mailbox (where Main transmits to Sub) and mailbox 1 should be configured as transmit (where Sub transmits to Main). \\ The Main node also initializes a PAL context and creates the communication instances using the APIs //adi_a2b_CommChPalInit// & //adi_a2b_CommChCreate// respectively. Similarly, the Sub node also initializes the PAL context and creates the communication instances using the APIs //adi_a2b_CommChPalInit// & //adi_a2b_CommChCreate// respectively.
   *  Post initialization the Main and Sub node call the //adi_a2b_CommChTick// API periodically to poll the A2B node for mailbox interrupts (if configured for polling) and for transmitting message chunks once a transmission is initiated. 
   * The Main node initiates the transmission of the message with the request message ID specifying the information required from Sub using the //adi_a2b_CommChTxMsg// API. Once all the message data has been written to the remote Sub receive mailbox and Sub has read the same, the application is notified that the transmission is complete via callback with transmission complete event and the message ID by the communication channel.
   * In the Sub node all the mailbox data received from Main is processed by the communication channel engine and once a valid message is decoded the same is notified to the application via callback. The callback contains the request message data and the ID with event type indicating that a new message has arrived.
   * Now the Sub node responds with the response message with the unique ID by initiating a new transmission using the //adi_a2b_CommChTxMsg// API. Once all the message data has been written to the local transmit Sub mailbox and Main has read the same, the application is notified that the transmission is complete via callback with transmission complete event and the message ID by the communication channel.
   * In the Main node all the mailbox data received from Sub is processed by the communication channel engine and once a valid message is decoded the same is notified to the application via callback. The callback contains the response message data and the ID with event type indicating that a new message has arrived. With this the handshake between Main and Sub is complete.

Interrupt/Polling Mode
----------------------

This section explains how to configure CommCh to operate in either interrupt or polling mode

A2B Main
~~~~~~~~

If CommCh is used along with ADI’s A2B stack, define “ENABLE_INTERRUPT_PROCESS” macro in a2bapp_defs.h to operate the stack along with CommCh in interrupt mode. Refer to :doc:`A2B Stack user guide </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>` for more details on how to configure the stack to operate in interrupt mode. Follow the steps as explained in :doc:`A2B Smart Sub </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` section if CommCh is integrated with Non-ADI A2B stack at the Main.

A2B Smart Sub
~~~~~~~~~~~~~

If CommCh is used along with Smart Sub,

-  Register for a GPIO pin interrupt after *adi_a2b_CommChPalInit* function. Refer to code under else condition of **“#if A2B_POLL_MB”** macro in :doc:`Code Snippet 8 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` for the same.
-   In the callback function of the GPIO pin interrupt, set a flag to indicate the interrupt.Now after the adi_a2b_CommChTick periodic function, call the *a2b_CommChIntrQuery* function after to query the mailbox interrupts if the interrupt flag is set. Refer to code under **“#if A2B_POLL_MB == 0”** macro in Code :doc:`Code Snippet 4 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` for the same.

Porting Instructions
--------------------

The communication channel by default is expected to run on a Sub node controller. On the Main node controller, it is advised to run the ADI A2B Software Stack and use the communication channel feature integrated to communicate with the Subs. An example Main demo application using communication channel with ADI A2B Software stack is available in *.\\ADI_A2B-SSPlus_Software-RelX.Y.Z \\Target\\examples\\advancedapp\\mboxcommch\\a2b-sc58x-commch-mstr* folder and the corresponding Sub demo application using the communication channel is available in the *.\\ADI_A2B-SSPlus_Software-RelX.Y.Z \\Target\\examples\\advancedapp\\mboxcommch\\a2b-sc59x-commch-smartslv’* folder. Refer to :doc:`Running the Sample Demo </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` section on detailed steps to set up and run the demo. For detailed steps to integrate the communication channel using ADI A2B software stack on Main application refer to the :doc:`A2B Stack user guide </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>`.

If, however a non-ADI stack is used on the Main node controller for network discovery and configuration then the communication channel should be initialized correctly with eNodeType and nTargetNodeNum. Refer to :doc:`Code Snippet 8 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` on how to initialize the CommCh if it’s being integrated with non-ADI stack on the Main node.


|image8|

.. container:: centeralign

   \ **Code Snippet 8:**\ CommCh Integration with A2B Stack on Main Node


Running the Sample Demo
=======================

ADSP-SC594
----------

This section describes the procedure to run the sample Communication Channel demo available at *.\\Target\\examples\\advancedapp\\mboxcommch*. This example demonstrates usage of Communication channel APIs for exchanging messages between Main and a smart Sub for the following two use cases.

-  :doc:`Sub node authentication </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`
-  :doc:`Switching between Audio sources </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`

The sample demo configuration is as shown in :doc:`Figure 4 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`. The demo uses ADSP-SC594 as host processor and smart Sub, both running an instance of Communication Channel, for exchange of messages over A2B Mailbox.


|image9|

.. container:: centeralign

   \ **Figure 4:**\ ADSP-SC594 as Main and Smart Sub


The A2B schematic for the demo configuration is available in *‘ADI_A2B-SSPlus_Software-RelX.Y.Z/ Schematics/SC59x/A2BSchematics/ adi_a2b_3NodeSampleDemoConfig - SmartSub.dspproj’*. The bus configuration .c file used in the Main is generated from this schematic. Refer :doc:`A2B SigmaStudio+ user guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>` for customizing A2B schematics and generating new bus/ node configuration files.

System Requirements
~~~~~~~~~~~~~~~~~~~

Software Requirements
^^^^^^^^^^^^^^^^^^^^^

-  Install Cross Core Embedded Studio 2.10.0 or later from the link www.analog.com/cces
-  Install the ADSP-SC59X Board Support Package 1.0.0 or later from the link https://download.analog.com/tools/EZBoards/EV-SC59x/Releases/Release_1.0.0/ADI_EV-SC59x_EZ-KIT-Rel1.0.0.exe
-  SigmaStudio+ setup as explained in :doc:`A2B SigmaStudio+ user guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>` is required only if modifying the demo A2B schematic.

Hardware Requirements
^^^^^^^^^^^^^^^^^^^^^

-  EV-SOMCRR-EZKIT Rev A or above
-  EV-SC594-SOM Rev A or above
-  ADZS-AD2435MINI Board
-  EVAL-AD2435WJ3LZ Boards
-  Three 12V Power Supply 1.5A
-  ICE-1000 programmer with USB cable
-  ICE-2000 programmer with USB cable
-  Two audio source devices (e.g. iPods)
-  One audio sink device (e.g. Speakers)

Hardware Setup
~~~~~~~~~~~~~~

Connections
^^^^^^^^^^^

After completing all connections, the A2B system should look as shown in :doc:`Figure 5 </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>`.

-  Mount ADZS-AD2435MINI Board with I2C address 0x6A on Connector J10 of EV-SOMCRR-EZKIT.
-  Connect a JTAG emulator from PC to EV-SC594-SOM board

|image10|

.. container:: centeralign

   \ **Figure 5:**\ Demo Setup


Running sample Demo
^^^^^^^^^^^^^^^^^^^

-  Connect ICE-1000 programmer to JTAG port of EV-SC594-SOM Main board and to PC through USB cable and connect ICE-2000 to ADSP-SC594-SOM Sub board. Power on both the boards.
-  Open two instances of CCES and import Target project into the workspace.
-  Open one instance of CCES and import Target project available in *.\\ADI_A2B-SSPlus_Software-RelX.Y.Z \\Target\\examples\\advancedapp\\mboxcommch\\* into the workspace using ‘File->Import->Existing Projects into Workspace’ browse and select ‘a2b-sc59x-commch-smartslv’. Build the project using ‘Project->Build Project’ option.
-  Open other instance of CCES and import Target project available in *.\\ADI_A2B-SSPlus_Software-RelX.Y.Z \\Target\\examples\\advancedapp\\mboxcommch\\* into the workspace using ‘File->Import->Existing Projects into Workspace’ browse and select ‘a2b-sc59x-commch-mstr_Core0. Build the project using ‘Project->Build Project’ option.
-  Run the ADSP-SC594 smartSub project first and then the ADSP-SC594 Main project by selecting a debug configuration.
-  The audio input to the Main should start playing out from smart Sub board indicating successful authentication of the Sub as explained in :doc:`Sub Node authentication </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` section.
-  Press push button 1 on the SOMCRR-EZ Main board. This should cause the audio output on ADSP-SC594 Sub to start playing audio from AD2435WJ3LZ input source.
-  Press push button 2 to switch back audio from ADSP-SC594 Main board to be played at ADSP-SC594 Sub again. The messages exchange in switching audio is explained in :doc:`Switching between Audio Sources </wiki-migration/resources/tools-software/a2bv2/a2bsspluscommchinterationguide>` section.

.. note::

   If Emulator is used the first time: Create a new debug configuration using Run->Debug Configurations, create new session, select the processor (ADSP-SC594) and click NEXT, select Emulator and click NEXT, choose In-Circuit Emulator platform (example: ADSP-SC594 via ICE1000) and click NEXT, then click FINISH.


Demo Use-cases
~~~~~~~~~~~~~~

The following two use cases were demonstrated in this example.

Sub Node authentication
^^^^^^^^^^^^^^^^^^^^^^^

Custom Node authentication via Mailbox option was enabled for ADSP-SC594 smart Sub in the demo A2B schematic. The A2B software stack running on the ADSP-SC594 Main node sends an authentication request message with ID **A2B_COMMCH_MSG_REQ_SLV_NODE_SIGNATURE** to the smart Sub. The Sub node then responds with its node ID using message ID **A2B_COMMCH_MSG_RSP_SLV_NODE_SIGNATURE**. The Main then verifies the received Node ID against the ID specified in the schematic.

The successful discovery and playback of audio from smart Sub node indicates the successful Sub node authentication using Communication channel messages.

Switching between Audio Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upon running the demo, audio from the Main node plays out at Sub ADSP-SC594 post successful discovery. The audio from the AD2435WJ3LZ Sub board is also routed to the ADSP-SC594 Sub. Based on a push button command, the Main initiates a communication channel message of ID **A2B_COMMCH_MSG_REQ_XFADE_AUDIO_SRC** wherein it specifies the audio source to be played at the output. Upon receiving the message, the Sub switches the audio source as specified in the message and responds with the message ID **A2B_COMMCH_MSG_RSP_SLV_NODE_SIGNATURE**.

The successful switching of audio source upon push button press indicates the successful exchanges Communication channel messages for audio source switch.

Terminology
===========

.. container:: centeralign

   \ **Table:** Terminology


+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Term**  | **Description**                                                                                                                                                                                                                                                                                               |
+===========+===============================================================================================================================================================================================================================================================================================================+
| A2B       | Automotive Audio Bus                                                                                                                                                                                                                                                                                          |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| A2B node  | Refers to AD242x/AD243x.                                                                                                                                                                                                                                                                                      |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Main Node | A2B transceiver that is connected to the host processor is considered as the Main A2B node.                                                                                                                                                                                                                   |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sub Node  | A2B Sub Transceiver with local peripherals such as speakers and microphones.                                                                                                                                                                                                                                  |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| I2C       | Is a multi-Main single-ended serial bus used for attaching low-speed peripherals to a processor. In TWI / I2C protocol the serial data transmission is done in asynchronous mode. This protocol uses only two wires named SDA (serial data) and SCL (serial clock) for communicating between two or more ICs. |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/api_reference_document.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/communication_channel_event_handling_at_Slave.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/periodic_ticking_at_Slave.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/transmission_over_communication_channel_at_Slave.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/commch_set_framing.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/commch_get_framing.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/Master_Slave_message_handshake_sequence.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/commch_integration_with_a2b_stack_on_Master_node.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/adsp-sc594_as_Master_and_smart_Slave.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/demo_setup_commch.png
