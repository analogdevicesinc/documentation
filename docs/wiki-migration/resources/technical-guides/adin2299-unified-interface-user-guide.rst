RPG2 Unified Interface User Guide
=================================

INTRODUCTION The Unified Interface is an interface by which an application processor communicates through an industrial Ethernet network with another system to configure and interact with it. The Unified Interface provides a common messaging protocol across a variety of different link types. This common messaging protocol allows the application processor to be industrial Ethernet protocol agnostic as the core set of messages have nothing to do with any particular industrial protocol. Extensions may exist to take advantage of protocol specific features but are not a required part of the core messaging protocol.

BLOCK DIAGRAM FOR EMBEDDED DESIGN AND MODULE USERS INSERT FIGURRE HERE Figure 1.

Background
----------

A Unified Interface includes the following: • A communication controller, which is the embedded processor responsible for managing transmission and/or reception of Unified Interface messages on the communication side and running the industrial Ethernet protocol software. • A communication side, consisting of the ADSP-CM409F hardware with the Unified Interface application software and an industrial networking application software running on it. • An application processor, which is the processor responsible for configuring the communication side via the Unified Interface protocol as well as the application specific input and output (I/O), for example, the motor control, ADC, and more. • An application side, which is the system portion that includes the processor in use by the user containing the API described in the Unified Interface API section. • A link, which is the low level hardware interface used between the application processor and the communication controller to transfer Unified Interface messages. For example, serial peripheral interface (SPI), UART, and Ethernet. See the Application Processor Link Type section for more information. • A Unified Interface protocol, which is a set of messages that makes up the Unified Interface. • An I/O application, which is the main function that provides the entry point for the embedded firmware. • A Unified Interface application, which is the I/O application that implements the Unified Interface protocol. • A system, which is the combination of the application side components and the communication side components that make up the industrial Ethernet device. • A transaction, which is the transfer of tye Unified Interface message bytes over the configured link.

Design Flow Using the Unified Interface
---------------------------------------

See Figure 2 and the following sections for an outline of the steps to make an industrial Ethernet device using a Unified Interface. Prior to a user performing the porting exercise, the user must run through the quickstart guide example for the chosen protocol of the user. Refer to the Analog Devices, Inc., Chronous Developer Portal to download the protocol specific quickstart guide and run the application processor example for that given protocol. The Unified Interface is the same no matter what protocol is chosen.

Run the Quickstart Guide Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Regardless of the protocol, the quickstart guide for each protocol directs users on how to use the ni-example-app executable. Refer to the Analog Devices, Inc., Chronous Developer Portal for any of the protocol specific quickstart guides.

DESIGN HARDWARE FOR THE INDUSTRIAL ETHERNET DEVICE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While this step can occur during several portions of the design phase, doing so before creating the needed link porting layer may be the most efficient. However, this need can vary from device to device. Refer to the RPG2 Hardware Design Integration Guide for more information.

CREATE A LINK PORTING LAYER FOR THE APPLICATIONS PROCESSOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The link porting layer is the responsibility of the customer to create. It is the software layer that hooks up the Unified Interface stack to the hardware drivers for any given platform. Refer to the Porting and Customization section for more details on how to implement this task.

PORT THE EXAMPLE TO THE APPLICATIONS PROCESSOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are examples distributed for both a Windows®-based application and one that is based on an Arm® Cortex®-M4-based platform. The intention is to port specific portions of the code as needed and develop the others. Refer to the Porting and Customization section for more details on what a user must include in the user environment. Table 1 also outlines what the responsibilities of the customer are vs. what is provided by Analog Devices. See the NI Example Application for Windows section for a complete breakdown of the Windows application and some of the modification steps.

MAKE MODIFICATIONS TO THE EXAMPLE USING THE UNIFIED INTERFACE APPLICATION PROGRAMMING INTERFACE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Unified Interface application processor interface (API) is a driver that enables the user to interact with the RapID Platform Generation 2 (RPG2) solution. The user makes additions, modifications, or subtractions as applicable to the device and system needs of the user. The needs of every system varies, and the user must determine what to implement or not based on the system needs of the user. See the Unified Interface API section for a detailed description of the API.

Application Processor Link Porting Layer
----------------------------------------

The link porting layer is the layer between the Unified Interface stack and the drivers of a customer that is used to control the hardware on the application processor. The user is expected to provide a driver and modify the link porting layer to interact with that driver. Figure 3 shows the architecture of the application processor software, and Table 1 details which party is responsible for implementing this architecture. While there may be some specific processor examples for the link porting layer, the user is ultimately responsible for this porting.

Application IO drivers
~~~~~~~~~~~~~~~~~~~~~~

The application I/O drivers are the portion of the code where the application processor does all of its tasks that are not part of the networking part of the device. Examples are toggling physical I/O, physically starting or stopping the motor, and passing data to a liquid crystal display (LCD). The application I/O drivers layer is not part of the RPG2 product and is therefore not supported.

Application
~~~~~~~~~~~

The application is where the user makes calls to the API provided by the Unified Interface. The user can set or retrieved the I/O data or communicate with the communications processor to do other Ethernet related tasks.

NI-API_Srv
~~~~~~~~~~

Ni-api-srv is the actual Unified Interface driver that a user incorporates into the software environment of the user.

UI-Stk
~~~~~~

Ui-stk is the software stack where the Unified Interface messages are handled and processed to and from the network. Ui-stk must be included in the software environment of the user.

UI-xxx-lpl-srv
~~~~~~~~~~~~~~

Ui-xxx-lpl-srv is a project/file where the user links the physical hardware (drivers) of the user with the Unified Interface stack. There are sample link porting layers distributed for Windows and the ADSP-CM409F.

Link Hardware Drivers
~~~~~~~~~~~~~~~~~~~~~

The link hardware drivers are the drivers that the user has for the application processor interface type (UART, SPI or Ethernet) of the user.

INSERT IMAGE HERE.

Porting and Customization
-------------------------

This section describes how to implement a link type into the Unified Interface. The available software zip file contains examples for Ethernet, SPI, and UART link types for an embedded platform, and the zip file also contains Ethernet and UART link type examples for a Windows-based platform.

Link Porting Layer Customization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To customize the link porting layer for link type hardware and/or a driver for the processor, add a new header and C source file that contains functionality for the following items: • Link initialization • Link configuration • Message transmission • Message receive handling • Link deinitialization Note that the link porting layer library can be renamed during the customization process.

Link Initialization
~~~~~~~~~~~~~~~~~~~

Use the link initialization function to set up the link hardware. A pseudo code example follows:

::

   LinkInitialization(Link-specific parameters)
   {

    Initialize the link

    if link initialization error 

    then return LPL_ERROR;

    return LPL_OK;
   }

Link Configuration
~~~~~~~~~~~~~~~~~~

Use the link configuration function to configure link specific parameters. A pseudo code example follows:

::

   LinkConfiguration(Link-specific parameters)
   {
    
    Configure the link

    if link configuration error 

    then return LPL_ERROR;

    return LPL_OK;
   }

If required, the link configuration can be performed inside the link initialization function. A pseudo code example follows:

::

   LinkInitialization(Link-specific parameters)
   {
    
    Initialize the link
    

    if Link initialization error 

    then return LPL_ERROR;


    Configure the link

    if link configuration error 

    then return LPL_ERROR;

    return LPL_OK;

   }

Message Transmission
~~~~~~~~~~~~~~~~~~~~

Use the message transmission function to send a message from the Unified Interface stack via the link. This function is called by the ui-stk via a function pointer. The signature (return type, argument types, and argument order) of this function must match UI_TxFunc_t. A pseudo code example follows:

::

   MessageTransmission(data location, message size)
   {
    
    Transmit the Unified Interface message on the link
    

    if data transmission error

    then return LPL_ERROR;

    return LPL_OK;
   }

Message Receive Handling
~~~~~~~~~~~~~~~~~~~~~~~~

Message receive handling receives incoming data from the link and forwards this data to the Unified Interface stack. This handling can be accomplished in a tread or an interrupt handler. To minimize the amount of data movement, the Unified Interface stack allows incoming data to be directly copied into its input buffer space. To obtain the location where the incoming data must be placed, call UI_GetRxLocation(). The incoming data then is sequentially copied starting at that location. From there, UI_ProcessMsgData() is called to begin processing of the newly received data. A pseudo code example follows:

::

   MessageReception()
   {

    Request the current receive location → UI_GetRxLocation()
    
    Read the incoming data and place the data into the buffer

    Call UI_ProcessMsgData();
    

To keep the internal data pointers in sync, for every call to UI_ProcessMsgData(), there has to be a preceding call to UI_GetRxLocation().

Link Deinitialization
~~~~~~~~~~~~~~~~~~~~~

Use the link deinitialization function to deinitialize the link hardware. This function may not be required for all platforms. The designer must decide if this functionality is required for the platform in use. A pseudo code example follows:

::

   Link Deinitialization()
   {
    
    Deinitialize the link

    if link deinitialization error 

    then return LPL_ERROR;

    return LPL_OK;
   }

Porting the Platform Support Service
------------------------------------

This section describes the functions available in the platform support service of the example application and how to port these functions to the destination platform. These functions are examples that must not be modified and adapted by the user.

PLAT_StartupSystem()
~~~~~~~~~~~~~~~~~~~~

The PLAT_StartupSystem() function initializes the platform the example application runs on. This function turns on clocks and sets up any peripherals that are required for the operation of the platform. If the platform successfully initializes, this function returns PLAT_OK, and if an error occurs during initialization, this function returns PLAT_ERROR.

PLAT_ProcessArgs()
~~~~~~~~~~~~~~~~~~

The PLAT_ProcessArgs() function processes the passed in command line arguments. If the command line arguments successfully processed, this function returns PLAT_OK. If no command line arguments were supplied, and no error occurred, this function returns PLAT_NO_ARGS. If any of the command line arguments did not process, this function returns PLAT\_ ERROR. If no command line arguments have to be processed, this function simply returns a success code. If the embedded application does not have a command line capability, do not call on this function from ni-example-app.

PLAT_InitLink()
~~~~~~~~~~~~~~~

The PLAT_InitLink() function initializes the local link where Unified Interface messages are transmitted and received. If the link initialization was successful, this function returns a pointer to the function that must be used to transmit the Unified Interface messages. If the link initialization failed, it returns a NULL pointer. The included example application allows for link type selection at run time. If only one link type is required, use the function as follows:

::

   UI_TxFunc_t *PLAT_InitLink()
   {
    int32_t result;
    UI_TxFunc_t *msgTx_p;

    result = LPL_CustomInit(Link specific parameters);

    if (result != LPL_OK)
    msgTx_p = NULL;
    else
    msgTx_p = LPL_CustomTxMsg;


    return msgTx_p;
   }

PLAT_StartTimeUpdate()
~~~~~~~~~~~~~~~~~~~~~~

The PLAT_StartTimeUpdate() function starts the process that notifies the network interface API service that a given time interval has elapsed (that is, calls NI_TimeUpdate()) by using platform specific tasking and/or timing resources. On a platform with an operating system (for example, Windows), this this functionality can be a thread that calls NI_TimeUpdate() periodically. On a platform without an operating system, implement this functionality as a periodic interrupt handler. There are no predefined requirements on the actual implementation of this function other than that this function must reliably supply ticks to the network interface API service. The time update process, whether it is a thread or a timer interrupt, must run at a higher priority than the application. Otherwise, the time does not advance from the perspective of ni-api-srv and the timeouts do not work.

PLAT_StartApplication()
~~~~~~~~~~~~~~~~~~~~~~~

The PLAT_StartApplication() function starts the example application layer. The startup of the application is dependent on the platform. On an embedded platform, this function can call NI_application(). On a platform with an operating system (for example, Windows), this function can spawn a thread that calls NI_application().

PLAT_TerminateExecution()
~~~~~~~~~~~~~~~~~~~~~~~~~

The PLAT_TerminateExecution() function is called by the example application to terminate execution. This function gives the platform support library the opportunity to trap errors and then clean up and/or release resources. This function is an expected exit point for the executable, and this function is not expected to return. If applicable, a success or failure code returns to the operating system.

PLAT_ProtectUiStack()
~~~~~~~~~~~~~~~~~~~~~

The PLAT_ProtectUiStack() function can take the mutex on a system with an operating system so that each thread or process must wait for ownership of the mutex before the function can access the Unified Interface stack. On a system without an operating system, this function may disable interrupts.

PLAT_UnprotectUIStack()
~~~~~~~~~~~~~~~~~~~~~~~

The PLAT_UnprotectUiStack() function reverses the actions of the PLAT_ProtectUiStack() function. On a system with an operating system, this function can release the ownership of the mutex so that other threads or processes can access the Unified Interface stack. On a system without an operating system, this function can enable interrupts.

NI EXAMPLE APPLICATION FOR WINDOWS
----------------------------------

The example application for Windows is called ni-example-app. This application is an application processor simulator that contains the needed API calls to interact with the Communications Controller. The ni-example-app application can be downloaded from the Analog Devices, Inc., Chronous Developer Portal. Extract the zipped file to a local directory and navigate to ..\\ni-example-app\\project\\vs\\ni-example-app. Open ni-example-app.sln with Visual Studio 2015 or later. The Solution Explorer will show the following five projects: • ni-api-srv • ni-example-app • ni-windows-support-srv • ui-stk • ui-windows-lpl-srv If not already selected, select ×86 as the Solution Platform.

Specify the Endianness
~~~~~~~~~~~~~~~~~~~~~~

To specify the endianness, take the following steps: 1. In the Solution Explorer, right-click ui-stk. 2. Under Configuration Properties, expand C/C++. 3. Select Preprocessor. 4. Select Preprocessor Definitions (see Figure 4). 5. Click the dropdown arrow and select <Edit…>. The default definition is UI_LITTLE_ENDIAN. A preprocessor definition is required either UI_LITTLE_ENDIAN or UI_BIG_ENDIAN. For a Windows platform, little endian is expected. For an embedded processor, endianness is something that varies depending on the application processor chosen.

INSERT IMAGE HERE

Setting the Command Arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To set the Command Arguments, take the following steps: 1. In the Solution Explorer, right-click ni-example-app. 1. Under Configuration Properties, select Debugging. 2. Select Command Arguments. Click the dropdown arrow and select <Edit…>.

Ethernet as Application Processor Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To set the Ethernet as an application processor interface, take the following steps: 1. To see all available network devices, enter -l ETH under Command Arguments (see Figure 5). 2. Click Apply 3. Click OK 4. Press Ctrl + Shift + B to build the solution. 5. Press Ctrl + F5 to start without debugging. The following output appears in the Console window:

   ni-example-app.exe -l ETH

::

   [..\..\..\src\NI_main.c:75] INFO: Welcome to ni-example-app!

   [..\..\..\src\NI_main.c:78] INFO: Processing arguments...
   A network device must be specified if the ETH link type is chosen.
   Use the -n option to set the desired network device.

   List of available network devices:
    1: \Device\NPF_{080146B3-7B09-488E-8C10-BC05B800F39B}, (Microsoft)
    2: \Device\NPF_{9AC18211-0815-4F54-8060-C5904AD9C4F2}, (NdisWan Adapter)
    3: \Device\NPF_{8767E47B-BAF3-4821-8A1D-F8EDE935F8C5}, (Microsoft)
    4: \Device\NPF_{E26E29A0-5899-4925-B0EF-2499B98570C8}, (Realtek USB NIC)
    5: \Device\NPF_{CAB0CB19-2CCA-4018-9FB5-B816CD055359}, (NdisWan Adapter)
    6: \Device\NPF_{F1F73818-E911-448D-9C9A-40511FB69628}, (Microsoft)
    7: \Device\NPF_{A550E718-E38D-49ED-8873-71E7B6A74923}, (NdisWan Adapter)

   [..\..\..\src\NI_main.c:81] INFO: FAILED

INSERT IMAGE HERE

Take the following steps to set the Ethernet Command Arguments: 1. Select the appropriate network device and change the Command Arguments to -l ETH -n \\Device\\NPF\_ {E26E29A0-5899-4925-B0EF-2499B98570C8}. 2. Click Apply. 3. Click OK.

INSERT IMAGE HERE

UART as an Application Processor Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To set the UART as an application processor interface, take the following steps:

-  Open the Device Manager and expand the Ports (COM & LPT) section. A list of two Silicon Labs dual CP2105 USB to UART bridge: enhanced COM ports appears as follows:
-  Silicon Labs Dual CP2105 USB to UART Bridge: Enhanced COM Port (COM6)
-  Silicon Labs Dual CP2105 USB to UART Bridge: Standard COM Port (COM7)
-  Note the name of the enhanced COM port and enter -l UART -c COM6 under Command Arguments.
-  Click Apply.
-  Click OK.

INSERT IMAGE HERE

Running ni-example-app in Debug Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Take the following steps to run ni-example-app in debug mode: 1. Before running the ni-example-app, users must set up the EV-RPG2 board chosen as detailed in the UG-1780. 2. Press Ctrl + Shift + B to build the solution. 3. Press Ctrl + F5 to start without debugging. The following output appears in the Console window:

::

   [..\..\..\src\NI_main.c:75] INFO: Welcome to ni-example-app!

   [..\..\..\src\NI_main.c:78] INFO: Processing arguments...
   [..\..\..\src\NI_main.c:86] INFO: DONE
   [..\..\..\src\NI_main.c:90] INFO: Performing system startup...
   [..\..\..\src\NI_main.c:96] INFO: DONE
   [..\..\..\src\NI_main.c:100] INFO: Start time update process...
   [..\..\..\src\NI_main.c:106] INFO: DONE
   [..\..\..\src\NI_main.c:110] INFO: Starting up example application...
   [..\..\..\src\NI_main.c:137] INFO: DONE
   [..\..\..\src\NI_main.c:140] INFO: Link init...
   [..\..\..\src\NI_main.c:146] INFO: DONE
   [..\..\..\src\NI_main.c:150] INFO: Unified Interface stack init...
   [..\..\..\src\NI_main.c:159] INFO: DONE
   [..\..\..\src\NI_main.c:164] INFO: Set response timeout...
   [..\..\..\src\NI_main.c:170] INFO: DONE
   [..\..\..\src\NI_main.c:175] INFO: Find Network Interface...
   [..\..\..\src\NI_main.c:186] INFO: DONE
   [..\..\..\src\NI_main.c:190] INFO: Set transmit modes...
   [..\..\..\src\NI_main.c:204] INFO: DONE
   [..\..\..\src\NI_main.c:208] INFO: Get installed protocol...
   [..\..\..\src\NI_main.c:220] INFO: DONE (EtherNet/IP)
   [..\..\..\src\NI_main.c:281] INFO: Set device 400...
   [..\..\..\src\NI_main.c:292] INFO: DONE
   [..\..\..\src\NI_main.c:296] INFO: Add item 500 to location 1...
   [..\..\..\src\NI_main.c:307] INFO: DONE
   [..\..\..\src\NI_main.c:311] INFO: Add item 501 to location 2...
   [..\..\..\src\NI_main.c:322] INFO: DONE
   [..\..\..\src\NI_main.c:326] INFO: Add item 502 to location 3...
   [..\..\..\src\NI_main.c:337] INFO: DONE
   [..\..\..\src\NI_main.c:342] INFO: Finalize configuration...
   [..\..\..\src\NI_main.c:353] INFO: DONE

The item and device constructs are the default values for the predistributed sample industrial Ethernet configuration database. For more information, see the RPG2 I/O Configuration Tool User Guide. While not in the Console display, once the user has called the configuration complete in the application processor code, the user then must make calls specific to the inputs and outputs as shown in Table 3 (NI_SetInputData and NI_GetOutputData). The program then continuously calls the NI_ProcessEvents() function to process events. Inside of NI_ProcessEvents() there is an input data subroutine and an output data subroutine.

INSERT Tables Here

::

   void NI_ProcessEvents(void) {
    int32_t result;
    UI_msgType_t msgType;

    // Call any time-dependent handlers
    if (NI_inDataTransmitMode_g == NI_transmitMode_onTime) {
    if (NI_time_us_g >= NI_nextInDataTxTime_g) {
    NI_InputDataLatchHandler();
    NI_nextInDataTxTime_g += NI_inDataTxPeriod_us_g;
    }
    }

    /* Checks for additional calls to time-dependent handlers go here */

    // Call any message-dependent handlers
    result = UI_GetNextMsgType(UI_msgSetEvent, &msgType);
    if (result == UI_OK) {
    switch (msgType) {
    case UI_itemOutData:
    NI_OutputDataHandler();
    break;

    case UI_itemInDataLatch:
    UI_ParseItemInDataLatch();
    NI_InputDataLatchHandler();
    break;

    default:
    // TODO: Flush unrecognized messages
    break;
    }
    }
   }

Unified Interface API
---------------------

The Unified Interface API is protocol agnostic. The user makes calls into the given functions as applicable for the application of the user. The RapID Platform Generation 2 (RPG2) block diagram is shown in Figure 8. As shown in Figure 9, the RPG2 is a black box that users must only worry about when using the Unified Interface API. Figure 10 shows a diagram of some of the main Unified Interface messages and details of when these messages are seen in the time of the system. Message validity is determined pre and post ConfigComplete, which is shown in Figure 10 for the system. To do industrial Ethernet communication, call ConfigComplete first.

INSERT IMAGES HERE

Some functions are valid only before the NI_ConfigComplete() function. Some functions are valid only after the NI_Config Complete() function. Some are valid in either case, which is dependent on the industrial Ethernet protocol currently used. Table 4 lists the valid time for NI functions.

NI_Init()
~~~~~~~~~

The NI_Init() function initializes the Unified Interface and gets the Unified Interface to where the Unified Interface is stable and able to receive additional messages that are required. This function cannot be called after the NI_ConfigComplete() function.

NI_Init Function Prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^

The prototype of this function follows:

::

   /* Initialize the local API software in preparation for communication via the
     * Unified Interface and attempt to detect an attached Network Interface module
    *
     * maxAttempts The maximum number of attempts this function will make to
     * detect an attached Network Interface module
    *
     * Returns NI_OK on successful initialization
     * NI_ERROR on failure during initialization
     * NI_ERROR if Network Interface module found but response incorrect
     * NI_NOT_FOUND if couldn't detect a Network Interface module
    */
   int32_t NI_Init(uint16_t maxAttempts);

The main purpose of NI_Init() is to determine if the application processor interface is correctly connected and ready for further Unified Interface communication. The user can specify the maximum number of times the application processor of the user attempts to find the module.

NI_GetProtocol
~~~~~~~~~~~~~~

The NI_GetProtocol() function returns the current protocol that the module is running.

NI_GetProtocol() function prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   The function of NI_GetProtocol is as follows:
   /* Get the Industrial Ethernet protocol installed on the attached Network
     * Interface module
    *
     * No parameters
    *
     * Returns >=0: the installed Industrial Ethernet protocol (typecast returned
     * value to NI_protocol_t to get enumerated value)
     * <0: NI_TIMEOUT if operation timed out
     * NI_ERROR if a Unified Interface stack error was detected
    */
   int32_t NI_GetProtocol(void);

This function either times out or gives an enumeration as dictated by the protocol used. Table 5 lists the possible returns and their corresponding protocol code.

INSERT TABLE HERE

NI_SetDevice()
~~~~~~~~~~~~~~

The NI_SetDevice() function sets the device that exists from the module configuration data. This function is not valid after NI_ConfigComplete() is called.

NI_SetDevice() prototype
^^^^^^^^^^^^^^^^^^^^^^^^

The prototype of this function follows:

::

   /* Set the system device according to the indicated ID
    *
     * deviceId ID of the device to be set for the system
    *
     * Returns NI_OK on success
     * NI_ERROR if device not found in IO config data
     * NI_ERROR if called after configuration completed
     * NI_TIMEOUT if operation timed out
    */
   int32_t NI_SetDevice(uint16_t deviceId);

NI_AddItem()
~~~~~~~~~~~~

The NI_AddItem() function adds an item from the configuration database of the user. This function can be valid after NI_Config Complete depending on the protocol that is in use (see Table 6). This function also has no use in the IP use case.

NI_AddItem() Prototype
^^^^^^^^^^^^^^^^^^^^^^

::

   /* Add an item to the system
    *
     * itemId ID of the item to be added to the system
     * location into which the item should be installed
    *
     * Returns >= 0: item handle
     * <0: NI_INVALID_PARAM if location out of range (must be >0)
     * NI_ERROR if item not found by ID
     * NI_ERROR if items not currently permitted to be added
     * NI_TIMEOUT if operation timed out
    */
   int32_t NI_AddItem(uint16_t itemId, uint32_t location);

NI_ConfigComplete()
~~~~~~~~~~~~~~~~~~~

The NI_ConfigComplete() function is called to indicate that the application processor has no more options to configure the communication controller and is ready for Ethernet communication. After this function is called, some functions become available to the application processor and some cease being available.

NI_ConfigComplete Function Prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prototype of this function follows:

::

   /* Indicate that configuration should be completed
    *
     * No parameters
    *
     * Returns NI_OK on success
     * NI_ERROR if there is a problem with the system
     * NI_TIMEOUT if operation timed out
    */
   int32_t NI_CompleteConfig(void);

NI_GetOutputData()
~~~~~~~~~~~~~~~~~~

The NI_GetOutputData() function obtains the newly received output data from the Unified Interface stack. Call this function in response to the NI_OutputDataHandler() function.

NI_GetOutputData() function prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The function prototype is as follows:

::

   /* Get the newly-received output data
   *
   * Use this function to retrieve the newly-received output data from the
   * Unified Interface stack.
   *
   * This function should be called as a response to the notification of new
   * output data. It should either be called from or immediately after
   * NI_OutputDataHandler() is called. It should never be called otherwise.
   *
   * dataStatus_p Pointer to location into which the status of the item
   * output data should be copied (see NI_ioStatus_t)
   * itemHandle_p Pointer to location into which the item handle to
   * which the output data corresponds should be copied
   * outDataSize_p Location into which the size (in bytes) of the received
   * output data should be copied
   * outData_p Pointer to location into which the received output data
   * should be copied
   *
   * Returns NI_OK on success retrieving output data
   * NI_ERROR if there was a problem parsing the received output data
   * message
   * NI_TIMEOUT if operation timed out
   */
   int32_t NI_GetOutputData(int32_t *dataStatus_p,
    int32_t *itemHandle_p,
    uint16_t *outDataSize_p,
    uint8_t *outData_p);

NI_SetInputData
~~~~~~~~~~~~~~~

The NI_SetInputData() function sets the input data that is sent to the industrial Ethernet network.

NI_SetInputData Prototype
^^^^^^^^^^^^^^^^^^^^^^^^^

The function prototype is as follows:

::

   /* Set the most-recent input data
    *
     * Use this function to push the latest input data into the NI API for
     * transmission to the Network Interface module. This function should be called
     * in either of the following scenarios:
    *
     * A) At the application side's discretion in order to update the input data
     * supplied on the network
     * B) From NI_InputDataLatchHandler() in order to complete an isochronous
     * network cycle
    *
     * itemHandle Handle to the item for which the input data is being supplied
     * inDataSize Size (in bytes) of the supplied input data
     * inData_p Pointer to the input data to be supplied for the indicated
     * item
     * complete Flag indicating whether or not the write of the input data to
     * the Network Interface module is complete
    *
     * NOTE: Use NI_ALL_ITEMS as the item handle parameter value if the supplied
     * input data is for all installed items and is already packed.
    *
     * NOTE: Setting the 'complete' flag will cause the NI API to notify the
     * Network Interface module that this input cycle is complete. Clearing
     * this flag will simply tell provide the input data to the Network
     * Interface module. If NI_ALL_ITEMS is supplied as the item handle,
     * the NI API will automatically tell the Network Interface module that
     * this input cycle is complete (the 'complete' flag is ignored).
    *
     * Returns NI_OK on success setting input data
     * NI_ERROR if there was a problem creating the input data message
     * NI_TIMEOUT if operation timed out
    */
   int32_t NI_SetInputData(int32_t itemHandle,
    uint16_t inDataSize,
    uint8_t *inData_p,
    uint8_t complete);

NI_TimeUpdate()
~~~~~~~~~~~~~~~

Use this NI_TimeUpdate() function to get the time the function was last called. Users can call this several times in their code to monitor the timing between different parts of their application

NI_TimeUpdate() function prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prototype of this function follows:

::

   /* Notify this library that time has passed
    *
     * Use this function to tick this library and let it know how much time has
     * passed since the last call. This allows it to monitor things like response
     * message arrivals and the associated timeouts.
    *
     * NOTE: The precision of response timeouts is subject to how often this
     * function is called. The more often this function is called, the more
     * precise timeouts will be - at the cost of increased overhead. The
     * less often this function is called, the less precise timeouts will
     * be but at the benefit of decreased overhead.
    *
     * elapsedUs The number of microseconds that have passed since the last
     * call to this function
    *
     * Returns nothing
    */
   void NI_TimeUpdate(uint32_t elapsedUs);

NI_SetResponseTimeout()
~~~~~~~~~~~~~~~~~~~~~~~

The NI_SetResponseTimeout() function sets the time duration that is acceptable between an API call and its corresponding response. This function gives users the ability to set parameters for acceptable delays in communication between the application processor and the communication processor.

NI_SetResponseTimeout() function prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prototype of this function follows:

::

   /* Set the timeout time for expected response messages
    *
     * Use this function to override how long the application will wait before
     * timing a response out and considering it lost. This setting applies to all
     * responses.
    *
     * timeout_us Timeout duration (in us)
    *
     * Returns NI_OK on success setting timeout value
     * NI_INVALID_PARAM if timeout duration invalid
    */
   int32_t NI_SetRespTimeout(uint32_t timeout_us);

NI_OutputDataHandler()
~~~~~~~~~~~~~~~~~~~~~~

The NI_OutputDataHandler() function serves as a notification to the application processor that output data has arrived from the network. The user must call NI_GetOutputData as a response to this function. This call can be done right away or when the users must decouple their inputs and outputs.

NI_OutputDataHandler() function prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prototype of this function follows:

::

   /* Application output data handler
    *
     * This function is implemented by the application and called the Network
     * Interface API service. It is called immediately after new output data from
     * the module has arrived. It serves as a notification that NI_GetOutputData()
     * should be called. NI_GetOutputData() MUST be called once for every call to
     * this function. If the output data and associated metadata is not of interest
     * to the output data handler, all parameters to NI_GetOutputData() can be set
     * to NULL.
    *
     * It is permissible to call NI_GetOutputData() from this function or after
     * execution of this function completes.
    *
     * The application can handle this data however it would like. Some typical
     * actions might be:
     * - Scenario 1: A) Store the output data to be applied later (along with
     * supplying input data)
     * - Scenario 2: A) Apply the output data to the physical outputs
     * B) Read the physical inputs to latch the input data
     * C) Push the latched input data into the NI API to be
     * transmitted to the Network Interface module
    *
     * NOTE: Unless the NI API was configured to use a polling approach, this
     * function will be called from the same context (i.e. ISR or non-ISR)
     * as the LPL function that called the Unified Interface stack.
    *
     * NOTE: If no items were added to the system that contain output data, this
     * function will never be called by the NI API.
    *
     * No parameters
    *
     * Returns nothing

NI_InputDataLatchHandler
~~~~~~~~~~~~~~~~~~~~~~~~

The NI_InputDataLatchHandler() function is called directly after the network interface module has indicated that the current input data must be latched. The NI_SetInputData() function must be called to write new input data to the network interface module and to complete the I/O cycle.

NI_InputDataLatchHandler function prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prototype of this function follows:

::

   /* Application input data latch handler
    *
     * This function is implemented by the application and called by the Network
     * Interface API service. It is called immediately after the NI module has
     * indicated that the input data should be latched. It serves as a notification
     * that NI_SetInputData() should be called in order to write fresh input data
     * to the NI module and complete the current network IO cycle.
    *
     * No parameters
    *
     * Returns nothing
    */
   void NI_InputDataLatchHandler(void);

NI_SetTransmitModes()
~~~~~~~~~~~~~~~~~~~~~

The NI_SetTransmitModes() function sets the input data and output data transmit modes. Supported output data transmit modes are on request, on time (that is, periodically), on change, or on network (that is, every network cycle). Supported input data transmit modes are on time (that is, periodically) or on network (that is,. every network cycle).

NI_SetTransmitModes() function prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prototype of this function follows:

::

   /* Set the input and output data transmit modes
    *
     * Use this function to set what triggers transmission of output data from the
     * NI module and what triggers transmission of input data to the NI module.
    *
     * Output data may be transmitted 'on request', 'on time' (i.e. periodically),
     * 'on change' or 'on network' (i.e. every network cycle). This setting affects
     * the trigger that causes the NI module to transmit messages that contain
     * output data. If 'on request' is selected, the application must send a
     * message requesting that the NI module send output data. The timing of this
     * request is the responsibility of the application. If 'on time' is selected,
     * the NI module will send output data periodically with no respect to network
     * cycle. If 'on change' is selected, the NI module will send output data in
     * synchronization with the network cycle but only when the data has changed.
     * If 'on network' is selected, the NI module will send output data every
     * network cycle in synchronization with the network cycle.
    *
     * Input data may be transmitted 'on time' (i.e. periodically) 'on network'
     * (every network cycle). This setting affects the trigger that causes
     * NI_InputDataLatchHandler() to be called. If 'on time' is selected,
     * NI_InputDataLatchHandler() will be called periodically based on the local
     * time and the supplied input data transmit period parameter. If 'on network'
     * is selected, NI_InputDataLatchHandler() will be called as a follow on action
     * to a received 'latch inputs' event message.
    *
     * NOTE: If an isochronous application is desired, the selected output data
     * transmit mode must be either 'on change' or 'on network'. The other
     * modes are not compatible with isochronous operation.
    *
     * NOTE: If an isochronous application is desired, the selected input data
     * transmit mode must be 'on network'.
    *
     * NOTE: The supported transmit modes for output data are
     * - 'on request'
     * - 'on time'
     * - 'on change'
     * - 'on network'
    *
     * NOTE: The supported transmit modes for input data are
     * - 'on time'
     * - 'on network'
    *
     * outTxMode The output data transmit mode for which the NI module should
     * be configured
     * outTxPeriod_us The period (in us, subject to NI system tick rounding) at
     * which output data should be transmitted (only valid if
     * 'on time' transmit mode is selected, ignored for all others)
     * inTxMode The input data transmit mode for which the local system
     * should be configured
     * inTxPeriod_us The period (in us, subject to local system time update
     * rounding) at which input data should be transmitted from the
     * local system (only valid if 'on time' transmit mode is
     * selected, ignored for all others)
    *
    *
     * Return NI_OK on success setting transmit modes
     * NI_INVALID_PARAM on unrecognized transmit mode
     * NI_INVALID_PARAM if selected transmit mode is invalid for a given
     * data direction (e.g. if selected input data transmit
     * mode is 'on change')
     * NI_INVALID_PARAM if invalid input or output data transmit period
     * (only returned if selected transmit mode is
     * 'on time')
     * NI_TIMEOUT if operation timed out
     * NI_ERROR if NI module reported an error while setting transmit mode
    */
   int32_t NI_SetTransmitModes(NI_transmitMode_t outTxMode,
    uint32_t outTxPeriod_us,
    NI_transmitMode_t inTxMode,
    uint32_t inTxPeriod_us);

NI_GetBasket()
~~~~~~~~~~~~~~

The NI_GetBasket() function gets a basket from the configuration database of the user. This function can be valid after NI_Config Complete depending on the protocol that is in use.

INSERT IMAGE HERE

NI_GetBasket() function prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prototype of this function follows:

::

   /* Get a basket from the system
    *
     * basketId ID of the basket to be retrieved
     * basket_pp Pointer to location into which the pointer to the retrieved
     * basket data should be copied (out parameter)
    *
     * Returns NI_OK on success (basket_pp updated)
     * NI_ERROR if basket not found (basket_pp not updated)
    */
   int32_t NI_GetBasket(uint16_t basketId, NI_basket_t **basket_pp);

   ==== NI_ProcessEvents() ====
   Use the NI_ProcessEvents() function to check if an event occurred and then call the proper event handler function to notify the application.

   === NI_ProcessEvents() Function Prototype ===
   The prototype of this function follows:
   <code>
   /* Process events
    *
     * Process any events that have come in since the last call to this function
     * (or since the beginning of time).
    *
     * This function will check if any events have been occurred and then call the
     * appropriate event handler to notify the application of the event and its
     * information.
    *
     * In order to expedite event handling, this function should be called
     * repeatedly and as often as possible.
    *
     * No parameters
    *
     * Returns nothing
    */
   void NI_ProcessEvents(void);

NI_MsgReadyCallback()
~~~~~~~~~~~~~~~~~~~~~

The NI_MsgReadyCallback() function is a pointer to the function the stack must call when a new message arrives and is ready for parsing. When a new message is received and queued for parsing by the application, the application implements this function and calls the function by the stack.

NI_MsgReadyCallback() function prototype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prototype of this function follows:

::

   /* Unified Interface message ready handler
    *
     * During Unified Interface stack initialization, the application should point
     * the stack at this function to handle received messages
    *
     * This library will manage waiting for the required response on behalf of the
     * application
    *
     * NOTE: Conforms to the requirements set by the Unified Interface stack in
     * UI_common.h. Parameters and return values are not discussed here.
    */
   UI_MsgReady_t NI_MsgReadyCallback;

Network Interface Application Design Decisions
----------------------------------------------

This section exists to talk through what a user/customer will do with the Unified Interface Code in their application.

It gives some recommendations about what a user can expect in using the Unified Interface Source Code.

Transmit Modes
~~~~~~~~~~~~~~

Unified Interface Network Configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unified Interface Stack Codes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
