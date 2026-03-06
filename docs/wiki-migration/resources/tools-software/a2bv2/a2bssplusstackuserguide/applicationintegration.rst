.. warning:: Conversion failed for ``resources/tools-software/a2bv2/a2bssplusstackuserguide/applicationintegration``

   Reason: pandoc error: Error at "/tmp/tmpx5aml72p.txt" (line 249, column 1):
expecting inline
not found
 while PWM channel is running (AD243x only)|
^

.. code-block:: text

   ====== Application Integration ====== 
   
   [[resources/tools-software/a2bv2/a2bssplusstackuserguide|Click here to return to the A2B SSPLUS STACK USER GUIDE]]\\
   \\
   
   Integrator can take 3 approaches to integrate A2B stack:
     - Using Wrapper Services Layer 1
     - Using Wrapper Services Layer 2
     - A2B Network Stack Public APIs
   \\
   1. **Using Wrapper Services Layer 1**
     * This is the topmost layer below the Application, refer [[:resources:tools-software:a2bv2:a2bssplusstackuserguide:introduction#a2b software stack architecture|Figure]]. This provides ease of integration with minimal service APIs. The example implementation of this layer is available in .\Target\examples\demo\app-plugin\src\a2bapp.c.
     * The main services provided in this layer are:
         * A2B network setup - a2b_setup()
           * Implements the higher level service of network setup including stack memory allocation, initialization, and discovery.
         * A2B fault monitor - a2b_fault_monitor()
           * If line diagnostics is enabled this function checks if a line fault occurred post-discovery and initiates re-discovery.
         * A2B stack time tick - a2b_stackTick()
           * Stack tick function ensures that the stack is periodically called to keep all the processes/states rolling within the stack.
         * A2B stop - a2b_stop()
           * This function stops stack, un-registering call-backs, turning off interrupt polling, disabling sequence charts, and freeing resources associated with the application context.
       
       * The code snippet below shows a sample usage of Wrapper services layer 1 APIs as in .\Target\examples\demo\a2b-bf\appc\a2bapp_bf.c.
   
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:wrapper_services_layer_1_usage.jpg?1000 |}}
   <WRAP centeralign>**Figure:** Code Snippet: Wrapper Services Layer 1 Usage </WRAP>
   \\
   \\
   2. **Using Wrapper Services Layer 2**
     * .\Target\examples\demo\app-plugin\src\a2bapp.c provides wrapper services for achieving stack functionality. The services of this layer is invoked by Wrapper Services Layer 1. This layer invokes the A2B Network Stack Public APIs, which are core A2B stack services.
     * The below [[:resources:tools-software:a2bv2:a2bssplusstackuserguide:applicationintegration#application_level_state_transition_diagram|figure]] shows the state transition diagram for different Stack states at Wrapper Services Layer 2.  The stack starts network discovery after it has been allocated and loaded with the configuration file. After discovery, the stack continues to poll indefinitely for interrupts/events until it is stopped or encounters a critical error in any of the earlier states.
   
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:flow_chart.png |}}
   <WRAP centeralign>**Figure:** Application Level State Transition Diagram </WRAP>
   \\
   Each Stack state is explained in the following sub-section
   \\
   \\
   3. **A2B Network Stack Public APIs**
     * Once an integrator is familiar with the wrapper services like Initialize, Load, Discover, etc. as described above, he/she can implement his/her own services using the A2B Network Stack Public APIs directly (refer [[:resources:tools-software:a2bv2:a2bssplusstackuserguide:introduction#a2b software stack architecture|Figure]].)
   ===== Stack States =====
   \\
   ==== Initialize/Allocate ====
     * The Stack requires the application to allocate and initialize one or more instances to run. Each individual instance maintains the complete Stack state for an A2B network. Multiple instances allow the Stack to manage multiple A2B networks simultaneously.
     * This state corresponds to the function a2b_allocate() in the application file a2bapp.c.
   \\
   ==== Load ====
     * This application state loads A2B bus configuration data into the Stack context. A bus configuration file exported from SigmaStudioPlus (or Bus Description Data from Mentor A2B Analyzer Application) contains all the information needed to perform a successful discovery and configuration of an A2B network.
     * SigmaStudioPlus generated BCF file can be optionally encoded in a Google Protocol Buffer (Protobuf) format. Mentor-generated BDD file is always encoded in Protobuf format. More information on Google Protocol Buffers can be found here: https://developers.google.com/protocol-buffers/. This function decodes and loads bus configuration when the included file is protobuf encoded
     * This state corresponds to the function a2b_load() in the application file a2bapp.c.
   \\
   ==== Start ====
     * Starting the Stack involves instructing the Stack to begin polling for interrupts, enabling sequence charts and debugging output, and hooking in application-level call-backs.
     * This corresponds to the function a2b_start() in the application file a2bapp.c.
   \\
   ==== Discover ====
     * Discovery starts when the application sends an A2B_MSGREQ_NET_DISCOVERY message to the Stack. Once this message has been sent, the application should transition to the Polling state in order to complete the discovery process.
     * This state corresponds to the function a2b_discover() in the application file a2bapp.c.
   \\
   === **Partial discovery of dropped nodes** ===
       * During node drops, partial discovery attempts of dropped nodes can be enabled by defining A2B_FEATURE_PARTIAL_DISC. When the application detects a node drop, instead of re-discovery of the whole bus, the discovery of dropped nodes is attempted without disturbing the nodes that are up and running.
       * This is achieved by bypassing “Initialize/Allocate”, “Load” and “Start” routines and directly calling the “Discover” state. In “Discover” state, A2B_MSGREQ_NET_POST_DISCOVERY message is sent to the stack. This message allows the stack to start discovery attempts from dropped nodes.
   \\
   ==== Interrupt Poll ====
     * Polling for system events is simply calling the tick function of the Stack on a regular basis. The Stack will enforce the interrupt poll time established in the Start state if called too often.
     * The calls to a2b_stackTick() drive the internal scheduler which ultimately drives all aspects of the Stack. The internal scheduler runs every A2B_CONF_SCHEDULER_TICK_MULTIPLE ticks as defined in conf.h 
     * By default, A2B_CONF_SCHEDULER_TICK_MULTIPLE is set to two (2). Therefore, if a2b_stackTick() is called every 5ms a job will be scheduled every 10ms. Change this value to one (1) to have the scheduler run on each tick. While the Stack itself is neither thread nor interrupt safe, it can be called as a result of an interrupt to minimize system latency to A2B events. Following an interrupt, one should call a2b_intrQueryIRQ() . This call into the Stack must be from the same thread of execution as all of the other Stack calls.
     * This call will service up to A2B_CONF_CONSECUTIVE_INTERRUPTS as defined in conf.h.
     * We can also have interrupt-based event handling instead of polling system events by enabling the macro ENABLE_INTERRUPT_PROCESS. The a2b_processIntrpt()function will periodically check if a pin interrupt is latched and will process them. An example is provided in. \Target\examples\demo\app-plugin\src\a2bapp.c. Platform specific interrupt callback shall be implemented by the integrator to latch the pin interrupt.
   \\
   ==== Stop ====
     * Stopping the Stack involves un-registering call-backs, turning off interrupt polling, disabling sequence charts, and freeing resources associated with a particular network configuration.
     * This state corresponds to the function a2b_stop() in the application file a2bapp.c.
   \\
   ==== Free ====
     * Freeing the Stack is simply a matter of freeing the application context container.
     * This state corresponds to the function a2b_free() in the application file a2bapp.c.
   \\
   ===== Application Extensions to Environment control block =====
   The environmental control block (or ECB) is the container for all platform and environment data passed throughout the Stack. Most PAL functions receive a pointer to the ECB making this a central data structure for the PAL.
   
   The core Stack ECB is defined by the a2b_Ecb structure which is comprised of two other sub-structure definitions as shown in Table (ECB Components).
   == Table: ECB Components ==
   ^Data Type^Description^
   |a2b_BaseEcb|This contains the basic platform-independent environment parameters. This structure must be defined first in the ECB structure.|
   |a2b_PalEcb|These are the platform-specific environment properties defined by the PAL. This structure must be defined second in the ECB structure.|
   \\
   Application-specific extensions can be added to the standard Stack ECB by adding custom application fields in the appropriate structures of a2b_Ecb.
   
   ===== Plugin Architecture =====
   One of the most powerful elements of the Stack is the plug-in architecture for initializing and managing slave nodes throughout an A2B network lifecycle. Plugins can initialize peripheral hardware on slave nodes, manipulate GPIO, communicate directly with I2C/SPI devices, create timers for periodic events, service interrupts, and monitor A2B diagnostic registers. Plugins can also send/receive notifications to/from the application to enable rich interactive system features. Custom plugins can be developed to support new A2B hardware. 
   \\
   ==== Plugin Examples ====
   Unordered List ItemThe Stack in all example Target projects comes with a Master and a generic Slave plugin designed using the plugin architecture.
   === Master Plugin ===
     * Slave node discovery and diagnostics are coordinated and enabled by the Master plugin. The Master plugin supports a variety of discovery modes, line diagnostics, as well as slave EEPROM configuration processing, and custom node authentication.
     * If necessary, the Master plugin can be customized. It is always recommended to add customizations on top of the existing implementation rather than replacing it with a newer version as the Master plugin is responsible for some important functions like discovery, diagnostics etc.
   === Generic Slave Plugin ===
     * The default slave plugin provided with the Stack example projects is generic in nature and has minimal command handling with support for initializing and de-initializing peripherals connected on slave nodes. The plugin always responds affirmately to query requests during discovery making it “default” plugin when included within a system.
     * A Custom Slave plugin may be necessary only in cases where the slave node needs to run a complex functionality specific to the slave board capabilities. Otherwise, a common generic slave plugin may be sufficient for all cases as used in Stack example projects in the software package.
   \\
   ==== Handling Interrupts in a Plugin ====
   In some cases, it may be necessary for the plugins to handle interrupts generated by A2B nodes. The function a2b_pluginInterrupt() in the plugin shall be implemented to handle such interrupts. The Stack takes care of passing the interrupt to the appropriate plugin depending on the interrupt type and location.
   
   The Master plugin in the Stack comes with a default implementation to handle master interrupts and to invoke appropriate application callback functions if registered.
   
   The generic Slave plugin in the Stack doesn’t come with a default implementation for interrupts generated by a slave node (GPIO pin). If a specific functionality is required on a slave node upon an interrupt, it can be implemented in the a2b_pluginInterrupt()  function of the slave plugin after checking the Interrupt Type and Source node as shown in Code Snippet.
   \\
   \\
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:a2b_plugininterrupt.png |}}
   
   \\
   <WRAP centeralign>**Figure:** Code snippet: a2b_pluginInterrupt dummy implementation </WRAP>
   \\
   ==== Writing a Custom Plugin ====
   A custom plugin can be developed to support a new A2B hardware based on an example plugin. A Stack plugin must export a set of functions as indicated in the below table (Plugin Functions).
   
   == Table: Plugin Functions == 
   ^Function Name^Use^
   |a2b_pluginInit()|Called by the Stack once to initialize the a2b_PluginApi structure allowing the plugin to register the remaining entry-point functions. This is the only function that should be exported by a plugin.|
   |a2b_pluginOpen()|Called during network discovery to see if the plugin handles a specific node. Any plugin related resources should be allocated here.|
   |a2b_pluginExecute()|Called when a job needs to be processed by this plugin.|
   |a2b_pluginInterrupt()|Called to process an interrupt for the slave associated with this plugin. Slave plugins only receive GPIO related interrupts.|
   |a2b_pluginClose()|Called to close the plugin. Any plugin related resources should be freed here.|
   
   A typical a2b_pluginInit() function for a plugin looks like this:
   \\
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:a2b_plugin_init.png |}}
    
   <WRAP centeralign>**Figure:** Code Snippet: Custom PluginInit Implementation </WRAP>
   
   Implementation details for other plugin functions can be referred in file .\a2bplugin-slave\src\a2bslave_plugin.c.
   \\
   === Custom Slave Plugin – Remote Tuner Module as an example ===
   An example implementation of the custom slave plugin is provided in file .\Target\examples\advancedapp\remoteTuner\a2b-bf\a2bplugin-rtm\src\a2brtm_plugin.c.
   
   This example plugin follows the plugin architecture as explained in "[[:resources:tools-software:a2bv2:a2bssplusstackuserguide:applicationintegration#plugin_architecture|Plugin Architecture]]" of this document in general and "[[:resources:tools-software:a2bv2:a2bssplusstackuserguide:applicationintegration#writing_a_custom_plugin|Writing a Custom Plugin]]" in particular.
   
   The custom plugin name and initialization function prototype are defined in file .\Target\examples\advancedapp\remoteTuner\a2b-bf\a2bplugin-rtm\inc \rtm_plugin.h as follows.
   
   == RTM PluginInit Implementation ==
   \\
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:rtm_plugininit_implementation.png?900 |}}
   \\
   The PAL layer registers a custom plugin load function as below in file .\Target\examples\advancedapp\remoteTuner\a2b-bf\a2bstack-pal\adi_a2b_pal.c in function a2b_palInit.
   
   == Plugin registration in PAL ==
   
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:plugin_registration_in_pal.png? |}}
   \\
   The plugins load function will load the RTM plugin as shown below. In this demo, RTM is connected to slave node 1 and slave node 0 has generic slave plugin. Refer to function a2brtm_pluginsLoad in file .\Target\examples\advancedapp\remoteTuner\a2b-bf\a2bplugin-rtm\src\a2b-rtm_plugin.c
   
   == RTM plugin load in plugins load function ==
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:rtm_plugin_load_in_plugins_load_function-transformed.png |}}
   \\
   The RTM plugin implementation has the following functions:
   == Table: RTM custom plugin functions ==
   ^Function Name^Use^
   |A2B_RTM_PLUGIN_INIT|Called by the plugin's load function. This is the only function that should be exported by a plugin.|
   |a2b_pluginOpen()|Called during network discovery to see if the plugin handles a specific node. Any plugin-related resources should be allocated here.|
   |a2b_pluginExecute()|The RTM booting, tuning, and mute functionalities are implemented in this custom function.|
   |a2b_pluginInterrupt()|Called to process an interrupt for the slave associated with this plugin. Slave plugins only receive GPIO-related interrupts.|
   |a2b_pluginClose()|Called to close the plugin. Any plugin-related resources should be freed here.|
   
   The custom Plugin execute function supports RTM specific messages which can be called externally.
   == Table: RTM custom Messages ==
   ^Message Name^Use^
   |A2B_MSGREQ_RTM_BOOT|RTM boot message|
   |A2B_MSGREQ_RTM_TUNE|RTM tune to a particular frequency|
   |A2B_MSGREQ_RTM_MUTE|Mute/Unmute the RTM|
   
   Post discovery, RTM custom messages are triggered by the application to perform specific functions. In the example application, UART-based commands are used to trigger these custom messages on a specific UART command as shown below.
   Refer .\Target\examples\demo\a2b-uart-utility\cmd_parse.c.
   
   == RTM message trigger from application ==
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:rtm_message_trigger_from_application.jpg? |}}
   \\
   === Loading Plugins into the Stack ===
   Plugins are loaded into the Stack through the a2b_PluginsLoadFunc PAL function. This function returns a structured list of pointers pointing to the a2b_pluginInit() function of each plugin. 
   
   During the discovery process, each registered plugin is queried, in order, when a new slave node is discovered to 
   determine whether or not that plugin can service the node. The first plugin to respond affirmatively by returning a non-NULL value will be assigned by the Stack to that node.
   
   Since each discovered slave node carries its own context, **a single plugin can service more than one slave node concurrently**. It’s important to note, however, that each slave plugin instance is responsible for maintaining its context.
   \\
   ==== Using A2B Stack for Multi-Master Network ====
   In cases where the Host processor is controlling multiple A2B Masters, it is necessary to maintain multiple stack instances. At the application level, one stack context is mapped per network master.  Each individual instance maintains the complete Stack state for an A2B network. Multiple instances allow the Stack to manage multiple A2B networks simultaneously. 
   
   Each application context can either register separate callback functions (for Discovery completion, Power Fault or Interrupt events) or have a single function with a unique callback parameter for each network chain.
   
   An example project to demonstrate multi-master bus setup is provided in ‘ADI_A2B-SSPlus_Software-RelX.Y.Z\Target\examples\advancedapp\multimaster’ of the A2B Software package. This example uses an ADSP-SC584 processor to discover and route the audio between two A2B networks.  In the example project, the structure a2b_App_t represents the application-level instance. Separate objects of this structure are created for each network instance. Each instance is identified with an index – ‘nChainIndex’, starting with 0. This parameter is used inside notification callback and PAL functions to differentiate the handling between two A2B networks.
   
   Note that when requiring to support multiple A2B Masters on a different platform, it is not just sufficient to change the macro ‘A2B_CONF_MAX_NUM_MASTER_NODE’ in Target/examples/demo/<a2b-xx>>/a2bstack-pal/platform/a2b/conf.h but also would require modifications to the functions in adi_a2b_pal.c.
   
   ==== Inter-Processor Communication over A2B Mailbox ====
   The Stack running on the master node target processor can communicate with an intelligent slave node having a connected processor. This can be achieved by using the Mailbox Communication Channel module. The module enables the exchange of control and command messages between the two processors.
   
   An example project for demonstrating the inter-processor communication using mailbox communication channel is provided in ‘ADI_A2B-SSPlus_Software-RelX.Y.Z\ Target\examples\ advancedapp\mboxcommch of the A2B Software package. Refer [[:resources:tools-software:a2bv2:a2bsspluscommchinterationguide]] for more details on running the demo. The document also provides details of the module APIs and the integration approach
   
   One example use case of this module is when Custom node authentication using Mailbox option is set in SigmaStudioPlus. In this case, the Stack running on the Target/Host processor queries a slave node processor for Node Identifier using A2B_COMMCH_MSG_REQ_SLV_NODE_SIGNATURE and the slave node responds with A2B_COMMCH_MSG_RSP_SLV_NODE_SIGNATURE using the module API as shown in [[:resources:tools-software:a2bv2:a2bssplusstackuserguide:applicationintegration#figure_:_message_exchange_between_master_and_slave_node_process|Figure]]. The figure also shows an example sequence of exchange when the slave initiates a request message transmission with message ID say A2B_COMMCH_MSG_REQ_MSTR_VERSION and the master responds back with the response message ID A2B_COMMCH_MSG_RES_MSTR_VERSION.
   \\
   
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:message_exchange_between_master_and_slave_node_proces_1_.jpg |}}
   <WRAP centeralign>**Figure:** Message exchange between Master and Slave node process </WRAP>
   \\
   Every message communicated has a unique ID assigned that is common across master and slave nodes. Message ID is 6 bits in length. Message IDs up to 0xA are reserved to be used for communication with the Master Plugin and should not be used by the application. All these message IDs are defined in ‘ADI_A2B-SSPlus_Software-RelX.Y.Z/Target/a2bcommchannel/ inc/adi_a2b_commch_interface.h’ file. 
   
   The Target example projects in ‘ADI_A2B-SSPlus_Software-RelX.Y.Z\Target\examples\demo’ does not come with the mailbox communication channel module integrated. To use the module for inter-processor communication the following pre-requisites shall be met.
   
   ==== Pre-Requisites for Inter-Processor Communication ====
     * The mailbox registers in the slave node need to be configured appropriately during discovery. This is controlled by the bus configuration file (adi_a2b_busconfig.c) exported from the Sigma Studio schematic. While designing the A2B schematic in Sigma Studio the mailbox registers    MBOX0_CTL and MBOX1_CTL should be set to the values 0x3D and 0x3F from the register tab view for the slave node to which communication channel messages via mailbox is to be exchanged.  The above register settings ensure the following configurations of mailbox:
       * Mailbox data length should be 4 bytes
       * Mailbox full and empty interrupts should be enabled
       * Mailbox 0 should be configured as receive mailbox (where master transmits to slave) and mailbox 1 should be configured as transmit (where slave transmits to master). 
     * The communication channel feature must be enabled in the Target project by defining the macro A2B_FEATURE_COMM_CH in the stack configuration file features.h.
     * The following header files need to be included in the Target project. The header files are available in the folder ‘ADI_A2B-SSPlus_Software-RelX.Y.Z/Target/a2bcommchannel/inc/ ’ in the release package.
       * adi_a2b_commch_interface.h - Contains the message identifiers that are reserved to be exchanged by the A2B master plugin of A2B stack on the master node with communication channel on slave nodes. Users should not modify these macros.
       * adi_a2b_commch_mstr.h - Contains the structures, data types, and function declarations for a master communication channel. User-configurable macros are also present in this file.
       * adi_a2b_commch_engine.h - Contains the structures, data types, and function declarations of the communication channel engine. The communication engine runs the framing/de-framing protocol.
       * The directory structure of the Target example project with the above-included files is shown in [[:resources:tools-software:a2bv2:a2bssplusstackuserguide:applicationintegration#figure_:_a2b_target_project _directory_structure_with_communication_channel_include|Figure]] (A2B Target project directory structure with communication channel include)
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:untitled.png |}}
   <WRAP centeralign>**Figure:** A2B Target project directory structure with communication channel include </WRAP>
   \\
   
     * The following source files need to be included in the application. The source files are available in the folder ‘ADI_A2B-SSPlus_Software-RelX.Y.Z/Target/a2bcommchannel/src/’ in the release package
       * adi_a2b_commch_mstr.c - Contains the function definitions for master communication channel which are used by the Master Plugin to create and use the communication channel for transmitting & receiving messages.
       * adi_a2b_commch_engine.c - Contains the function definitions of the communication channel engine. The communication engine runs the framing/de-framing protocol.
       * The directory structure of the Target example project with the above source files included as a part of the virtual folder ‘a2bcommchnl’ is shown in [[:resources:tools-software:a2bv2:a2bssplusstackuserguide:applicationintegration#figure_:_a2b_target_project_directory_structure_with _communication_channel_sources|Figure]].
   \\
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:a2b_comchannel.png |}}
   <WRAP centeralign>**Figure:** A2B Target project directory structure with communication channel sources </WRAP>
   \\
   For details on integration of A2B mailbox into application, please refer [[:resources:tools-software:a2bv2:a2bsspluscommchinterationguide]].
   \\
   ===== Post discovery APIs =====
   A2B network’s biggest advantage is “setup once and forget”. After network discovery and setup of all the nodes, minimal host intervention is required. Audio streams get transmitted across nodes seamlessly. So host intervention is only limited to fault monitoring. Host action is required only when bus faults are detected.
   
   With AD243x supporting SPI tunnelling, there is a need to have post discovery action as well. So the A2B stack has been adapted to provide post discovery APIs to application software in order to  transfer asynchronous data across A2B nodes through SPI tunnels.
   
   To ease applications in performing some basic post discovery operations, the following APIs are provided to the application. Post discovery APIs are provided in .\Target\examples\demo\app-plugin\src\a2bapp.c.
   
   == Table: Supported Post Discovery APIs ==
   ^API Name^Use^
   |a2b_reset()|This function does A2B network soft reset.|
   |a2b_AppWriteReg()|This function writes a register value to a particular A2B node.|
   |a2b_AppReadReg()|This function reads a register value from a particular A2B node.|
   |a2b_app_handle_becovf()|This routine periodically resets BECNT and BECOVF registers and checks for bus drop.|
   |a2b_AppDetectBusDrop()|This function reads the Vendor Id register of all A2B nodes discovered and declares a bus drop at a particular node where the read value is not the expected.|
   |a2b_AppPWMSetup()|This function configures the PWM registers for the PWM functionality in AD243x. It is called one time to setup the PWM channel (AD243x only)|
   |a2b_AppPWMControl()|This function controls the PWM blink and duty cycle registers and can be called
    while PWM channel is running (AD243x only)|
   |a2bapp_VMTRMonitor()|API for VMTR monitor to check if the monitored voltages are beyond the min and max thresholds. This API can be periodically called to determine voltage-related errors. This API assumes that all the VMTR threshold registers are already statically configured (AD243x only)|
   \\
   ==== SPI post-discovery APIs ====
   Post-discovery SPI APIs are available in .\Target\a2bstack\a2bstack\src\perieng.c. These APIs can be used to read/write from a remote SPI peripheral device like EEPROM via an A2B bus. Please refer to the .\Docs\ AE_09_A2B_Stack_API_Reference.chm(19.10.0) for detailed API reference.
   
   == Table: Supported SPI transaction modes ==
   ^SPI Mode^Use^
   |A2B_SPI_ATOMIC|Use Atomic SPI transactions to allow a write or read initiated on any node in an A2B system to occur at a peripheral on a different node|
   |A2B_SPI_BULK|Use Bulk SPI transactions|
   |A2B_SPI_FD_CMD_BASED|Use Full duplex SPI transaction - slave select 0 (ADR1) selects the SPI slave from the host|
   |A2B_SPI_FD_REG_BASED|Use Full duplex register-based SPI transaction – the A2B node is selected by either the ADR2 or SIO2 pin|
   |A2B_SPI_BULK_EXTENDED|Use Bulk extended transactions (more than 256 bytes in a single transaction at remote node)|
   |A2B_SPI_FD_CMD_BASED_EXTENDED|Use Full duplex extended SPI transaction (more than 256 bytes in a single transaction at remote node)|
   
   == Table: Supported API Modes ==
   ^API Mode^Use^
   |A2B_API_BLOCKING|API returns only after entire payload is Transmitted/Received|
   |A2B_API_NON_BLOCKING|API returns immediately and does not wait for entire payload to be Transmitted/Received|
   <note>For non-blocking implementation, the SPI_BUSY signal can be routed to a dedicated GPIO of the processor and can be processed on pin interrupts.</note>
   
   == SPI Post Discovery API structures ==
   ^Structure Name^Use^
   |a2b_SpiConfig|Structure holding the various configurable parameters of SPI|
   |a2b_SpiWrRdParams|Structure holding the various write/read parameters of SPI|
   
   Please refer the .\Docs\ AE_09_A2B_Stack_API_Reference.chm(19.10.0 Rel) for details on structure members.
   
   ==  SPI Post Discovery APIs ==
   ^API Name^Use^
   |adi_a2b_spiPeriCreate()|This function is used to allocate the SPI to SPI peripheral configuration time-out timer. This function shall be called only once.|
   |adi_a2b_spiPeriSetMode()|This function is used to register the call back function, SPI mode of operation etc, for SPI peripheral post-discovery event handling.|
   |adi_a2b_spiPeriGetMode()|This function is used get the current SPI & API mode of operation.|
   |adi_a2b_spiPeriWrRd()|This function is used to write/write-read payload to/from peripherals connected to A2B nodes using the SPI interface. The write and read buffers have to be configured in “a2b_SpiWrRdParams” structure before accessing this API. The application can submit the buffer to this API. The API will handle the segmentation and convert it into one or many A2B SPI bus transactions internally.|
   
   Please refer the .\Docs\ AE_09_A2B_Stack_API_Reference.chm(19.10.0 Rel) for details on API reference and its call and return parameters.
   
     * SPI Post Discovery API usage example
       * SPI post discovery APIs are used in example RTM plugin. Please refer .\Target\examples\advancedapp\remoteTuner\a2b-bf\a2bplugin-rtm\src\a2brtm_plugin.c for example usage. It is also explained in the below code snippet.
   
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:spi_post_discovery_api_usage_example.jpg? |}}
   
   {{ :resources:tools-software:a2bv2:a2bssplusstackuserguide:spi_post_discovery_api_usage_example1.jpg? |}}
   \\
   ==== A2B direct register write/read APIs ====
   These APIs provide access to A2B registers (master or slave nodes) via I2C or SPI depending on the stack’s access interface and node.
   ^API Name^Use^
   |a2b_regWrite()|Writes bytes to the SPI/I2C device. This is a synchronous call and will block until the operation is complete.|
   |a2b_regWriteRead()|Writes and then reads bytes from the SPI/I2C device. This is a synchronous call and will block until the operation is complete.|
   
   
   
   
