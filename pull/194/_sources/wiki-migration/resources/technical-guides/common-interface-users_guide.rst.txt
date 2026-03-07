.. warning:: Conversion failed for ``resources/technical-guides/common-interface-users_guide``

   Reason: pandoc error: Error at "/tmp/tmp4h66_53s.txt" (line 5048, column 1):
expecting inline
not found
|Slot Number    |Slot Number    |Slot Number    |Slot Number
^

.. code-block:: text

   ====== Common Interface User's Guide ======
   
   ===== 1. Overview =====
   
   The “Common Interface” is a solution that is customizable to fit the needs of an Industrial Ethernet Device.  The user may modify the Peripherals and the I/O Application to match the system requirements.  The User I/O Application communicates to the Network Application using the Common Interface.  This document describes what is contained in the Common Interface and the needed Application Programming Interface (API) calls for an Industrial Ethernet Device.
   
   The Common Interface provides a single Application Programming Interface (API) to adapt, and a precompiled executable that runs as the network application for a given Industrial Ethernet protocol.  Because the interface is common, a single user application can be created and operate on any of the supported protocols.  The user implements the Common Interface functions in their code as needed to get data to and from the network.  The Network Application is treated as a black box; users do not need to worry about the Ethernet aspect of communication.
   
   The developer produces two elements to make up a working device. Configuration Data (created using the Configuration Tool) and an I/O application using other peripherals of the processor or to perform other tasks as required. The Configuration Data is used by the Network Application to map the elements of the I/O application to Industrial Ethernet protocols.  The developer modifies the sample application to fit the needs of the device.  On the Common Interface, an example workspace which uses sample configuration implements an application that echoes Output Data from the PLC back to the device Input Data which is then sent back to the PLC.  
   
   The environment provided uses the freeRTOS in the ADSP-CM408 (CM408) or MAX32690 processor(or potentially other processors). The software in CM408(Or other processor) is open source and has been widely used in many industrial fields. A single thread is made available to the user’s own application, while the others are utilized for management of the lower-level protocols/etc. The development model is similar to writing an application for a standard operating system (e.g. Linux or Windows).
   
   The Network Application uses four GPIOs of CM408, MDIO, 16-bit parallel BUS (SMC) and the System Timer to implement the network interface. This leaves the other hardware sources, like GPIOs, Timers, ADC, several external interrupt lines, PWM, UART, SPI, GPIO, I2C and Other ADSP-CM408 peripherals at the disposal of the I/O application.
   
   ===== 2. Common Interface Software Development Kit Contents =====
   
   The Common Interface Software Development Kit (SDK) is distributed as an integrated project compatible with IAR IDE (IAR ARM 8.10 or later).  IAR is widely used for ARM core development.  This project is the starting point for application development.  The provided project is a simple example Common Interface application.  Regarding this project, it includes several different components.
   
   NOTE: It is imperative that a user not modify the .icf file that is included in the zip file as it defines the memory map for the Common Interface.
   
   
   ==== 2.1 Network Application(thread) ====
   
   This is a binary application that includes the network protocol implementation and associated protocol stack and interfaces. 
   
   ==== 2.2 I/O Application(thread) ====
   
   This is an application that includes simple data I/O implementation example and users are expected to add their own application layer in this thread. In this application example, there are also .rpc files and a .eds file for EtherNet/IP. The user is expected to modify these files as well to fit the needs of their application.
   
   ==== 2.3 IAR Projects ====
   
   This zip file also includes several IAR projects. These are not intended to be modified and should just be left as part of the build environment.
      • libdrv40z
      • libssl50z
      • libosal40z_freertos
      • adsp-cm40x-sms-srv
      • adsp-cm40x-startup-srv
      • io-example-srv
      • potentially others depending on the build environment
   
   ==== 2.4 Libraries ====
   
   This workspace also includes several binary files with include files only so that the user can use the API and be aware of what it is but not modify the source.
   
   ===== 3. Application Development and Integration =====
   
   The Common Interface is built around a few basic element types used to model an I/O device.
      • Device – The Common Interface device element is used to define the global parameters for a device with respect            
        to a particular protocol.  There can only be one device added per implementation of a user application.
      • Items – Common Interface items are used to map different pieces and types of I/O from the application to the 
        network interface in use. A user is not limited to just one item but the maximum IO size is limited by several 
        factors including the allowable packet size on a network. Therefore the overall IO data size has a maximum of    
        1440 bytes.
      • Baskets – Baskets are a higher-level mechanism used to organize items and devices into consistent groups.  A 
        basket will contain exactly one device and up to 32 items, so long as the maximum IO data size (1440 bytes) is 
        not exceeded.
   The sample configuration that is pre-distributed with the Common Interface is as follows:
   
   • Device 400
      o Has parameters specific to the protocol in use.
   
   • Item 500 (Digital Inputs and Outputs)
      o Input size: 2 bytes 
      o Subindex 1 (2 bytes)
      o Output size: 2 bytes 
      o Subindex 1 (2 bytes)
      o Other protocol specific information.
   • Item 501 (Analog Inputs and Outputs)
      o Input size: 4 bytes 
      o Subindex 1 (2 bytes)
      o Output size: 4 bytes 
      o Subindex 1 (2 bytes)
      o Other protocol specific information
   • Item 502 (Control Register)
      o Input size: 0 bytes 
      o Output size: 2 bytes 
      o Subindex 1 (2 bytes Control Data)
      o Other protocol specific information.
   
   • Basket 1000 – Contains the following Devices and Items
      o Device 400
      o Item 500
      o Item 501
      o Item 502
   
   ==== 3.1 Common Interface Devices ====
   
   A Device, in terms of the Common Interface, is a single element that defines a set of protocol- specific parameters used to identify the overall device to the industrial network. The developer assigns a number (16-bits) to each device-type that the application is intended to support (regardless of protocol). The configuration data then defines all information needed to adapt that device to a particular protocol. See Figure 2 below.
   
   The API includes routines to set the current device (set once at initialization), as well as read and write some of the “fields” of the device.
   
    INSERT FIGURE HERE
   Figure 2 - Common Interface Devices 
   
   
   ==== 3.2 Common Interface Items ====
   
   An item identifies something that can be read or written. This can be a block of cyclic I/O data, a parameterization value (e.g. scale factor), or any number of other purposes. I/O data items will be mapped similarly for the various network protocols, other items can behave differently depending on the protocol.
   The API includes functions to add items to the device, read and write the data of items, and set and read parameters related to the items.
   
      INSERT FIGURE HERE
   Figure 3 - Common Interface Items 
   
   ==== 3.3 Common Interface Baskets ====
   
   Baskets are the simplest element of the Common Interface. They are simply a collection of a
   Device and one or more Items. They are also not protocol-specific. The API includes a routine to retrieve the contents of a basket. See Figure 5 below.
   
      INSERT FIGURE HERE
   Figure 4 - Common Interface Baskets
   
   
   ==== 3.4 Simple I/O Example ====
   
   The user’s application is developed beginning from the thread of IO_IoApplicationThread(), which is created in main() at ..io-example-app\src\IO_main.c as follows: 
   
     xTaskCreate(IO_IoApplicationThread, "IO Thread",
       2*configMINIMAL_STACK_SIZE, NULL, IO_APP_BASE_PRIORITY, NULL)
   
   This thread will then call an example of the user’s application in  
   io-app\src\IO_main.c:
   
   
   <code>
   extern int io_example_app()
   {
   #ifdef USE_BASKET_CONFIGURATION
     int i;
     CI_basket_t *basket_p;
   #endif
   
     int protocolType;
     int result;
     unsigned short shortData;
     static unsigned char largeData[1502];
     unsigned int longData;
     CI_IoStatus_t outputStatus;
   
     /* Initialize the Common Interface */
     CI_DEBUG("Beginning initialization of the Common Interface...\n");
     protocolType = CI_Init();
     if (protocolType < 0) {
       CI_FATAL_ERROR("Error %d initializing Common Interface\n", result);
     }
     else {
       CI_DEBUG("Detected %s Network Protocol\n", GetProtocolString(protocolType));
       SetEndianFlag((CI_mode_t)protocolType);
     }
   
     /*********************************************************************/
     /************* Configuration using the "basket" method ***************/
     CI_DEBUG("Using \"basket\" configuration method\n");
   
     /* Get basket description from demo configuration data */
     basket_p = CI_GetBasket(BASE_DEMO_BASKET);
   
     /* Set device type from device ID in Basket configuration */
     result = CI_SetDeviceType(basket_p->deviceID);
     if (result != CI_OK) {
       CI_FATAL_ERROR("Error %d setting device type\n", result);
     }
     else {
       CI_DEBUG("Successfully configured device ID %d\n", basket_p->deviceID);
     }
   
     /* Add each I/O item found in the Basket to the Common Interface run
      * time configuration, save the "handle" returned by the Common Interface. */
     for (i = 0; i < basket_p->itemCount; i++) {
       itemHandle[i] = CI_AddItem(basket_p->ItemInfo[i].itemID,
                                  basket_p->ItemInfo[i].itemLocation, i);
       if (itemHandle[i] < 0) {
         CI_FATAL_ERROR("Error %d adding item\n", itemHandle[i]);
       }
       else {
         CI_DEBUG("Successfully configured item ID %d\n",
                  basket_p->ItemInfo[i].itemID);
       }
     }
     /*********************************************************************/
   
     /* Tell the Network Application the configuration is complete */
     result = CI_ConfigComplete(100000);
     if (result != CI_OK) {
       CI_FATAL_ERROR("Error %d on CI config complete\n", result);
     }
   
     /* Create an event handler thread */
    //CI_taskCreateLowPriority(handleEvents, "Event Handler", 4096);
     if (ospl_TaskCreate((void *)handleEvents, NULL, "IO Event Handler",
       2*configMINIMAL_STACK_SIZE, EVENT_HANDLER_BASE_PRIORITY, NULL)
       != ospl_Success) {
       CI_FATAL_ERROR("Unable to launch IO event handler\n");
     }
   
     /* Start the module */
     CI_SetSystemStatus(CI_System_OK);
   
     /* Print a message on the debug console */
     CI_DEBUG("Initialization complete\n\n");
   
     while (1) {
   #ifdef USING_STANDARD_CONFIG_DATA
       // test with standard configuration data
   
       /*************************************************************************/
       /* Read the digital data item */
       outputStatus = CI_ReadItem(itemHandle[0], CI_IO_valid, &largeData);
       if (outputStatus < 0) {
         CI_FATAL_ERROR("Error %d on call to CI_ReadItem\n", outputStatus);
       }
   
       /* Then, if the data is valid, echo, save, convert and display it */
       if (outputStatus == CI_IO_valid) {
         /* Write (echo) it back to the Controller (exactly as received) */
         result = CI_WriteItem(itemHandle[0], CI_IO_valid, &largeData);
         if (result != CI_OK) {
           CI_FATAL_ERROR("Error %d on call to CI_WriteItem\n", result);
         }
   
         /* Save the data */
         shortData = (unsigned short)(largeData[0] | (largeData[1] << 8));
         digitalData = shortData;
   
         /* If necessary convert the data */
         if (g_endianMode == LITTLE_ENDIAN) {
           /* fido is big endian so only need to do this for little endian data */
           EndianConvertWord(digitalData);
         }
   
         /* Display the data */
   //      CI_DEBUG("New Digital I/O Data received: 0x%04x\n", digitalData);
       }
   #endif
   ……
   
       /*************************************************************************/
       /* Read the analog data item */
       outputStatus = CI_ReadItem(itemHandle[1], CI_IO_valid, &largeData);
       if (outputStatus < 0) {
         CI_FATAL_ERROR("Error %d on call to CI_ReadItem\n", outputStatus);
       }
   
       /* Then, if the data is valid, echo, save, convert and display it */
       if (outputStatus == CI_IO_valid) {
         /* Write (echo) it back to the Controller (exactly as received) */
         result = CI_WriteItem(itemHandle[1], CI_IO_valid, &largeData);
         if (result != CI_OK) {
           CI_FATAL_ERROR("Error %d on call to CI_WriteItem\n", result);
         }
   
         /* Save the data */
         longData = (unsigned int)(largeData[0]        | (largeData[1] << 8) |
                                  (largeData[2] << 16) | (largeData[3] << 24));
         analogData = longData;
   
         /* If necessary convert the data */
         if (g_endianMode == LITTLE_ENDIAN) {
           /* fido is big endian so only need to do this for little endian data */
           EndianConvertLongWord(analogData);
         }
   
         /* Display the data */
   //      CI_DEBUG("New Analog I/O Data received: 0x%08x\n", analogData);
       }
   
       /*************************************************************************/
       /* Read the control register data item */
       outputStatus = CI_ReadItem(itemHandle[2], CI_IO_valid, &largeData);
       if (outputStatus < 0) {
         CI_FATAL_ERROR("Error %d on call to CI_ReadItem\n", outputStatus);
       }
   
       /* If the data is valid, save, convert and display it */
       if (outputStatus == CI_IO_valid) {
   
         /* Save the data */
         shortData = (unsigned short)(largeData[0] | (largeData[1] << 8));
         controlReg = shortData;
   
         /* If necessary convert the data */
         if (g_endianMode == LITTLE_ENDIAN) {
           /* fido is big endian so only need to do this for little endian data */
           EndianConvertWord(controlReg);
         }
   
         /* Display the data */
         CI_DEBUG("New Control Register Data received: 0x%04x\n", controlReg);
       }
   
       /* Tell the Network Application we have completed one I/O cycle */
       CI_IoComplete();
   
       /* Wait for the Network Application to begin a new I/O cycle */
       CI_WaitIO();
     }
   
     /* The application should never get here */
     return 0;
   } 
     
   </code>
   
   This is a complete Common Interface application. Real I/O processing will have to occur to make a useful device, but most applications will have this basic form:
   
   •  Initialization
      o Includes lowering of interrupt mask (necessary for proper operation of CI_Init()). 
      o Includes call to CI_Init().
      o Call CI_SetDeviceType(). This will result in loading of various protocol-specific information from the configuration loaded into the network application (e.g. EtherCAT vendor ID, device type, etc.). 
      o Call CI_AddItem(). This will be called for each distinct set of I/O in the device.For example, in a modular system each module plugged into the backplane would typically generate a separate call to CI_AddItem() as they are detected. The example above has a simple, fixed set of I/O. This call also results in the discovery of information in the configuration loaded into the network application including size, direction, etc. Additionally, protocol-specific information is used to properly configure the device on the network.
      o Call CI_ConfigComplete() to indicate that all items have been added. At this point the network application has all the information it needs to start up the network side and begin communications. The argument to this call is the maximum delay, in microseconds, that the application can wait during a call to CI_WaitIO().
   
   • Operating Loop
      o Includes a call to CI_IoComplete(). In some protocols this function operates to update data to and from the network, in others this update occurs immediately on each call to CI_ReadItem()/CI_WriteItem().
      o Includes a blocking call (e.g. to CI_WaitIO() or to a CI timer function). This is critical - the user application runs at a higher priority than much of the network application and it must block to allow the lower priority contexts to execute.
         
   For a basic Common Interface application, the only dependencies are on the library project. This project generates static libraries that are linked into the Project executable. 
   
   ====3.5 Debugging with a Network Application ====
   
   To debug a Common Interface application, the Network Application binary and a Common Interface Configuration must be present on the module being used for debug. 
   
   Once the Network Application and configuration data are installed on the module, you can begin developing your own application using the IAR ARM environment.
   
   It is simplest to start with one of the provided the sample project (IO-example-app.eww) and its associated configuration data. As you begin to modify the application you can also modify the configuration data to match and load the updated configuration using the Configuration Tool.
   
   When using the debug version of the network application, you will notice that a number of messages are printed to the debugger console between the time that the application is loaded and when it breaks at the beginning of main(). This is the early initialization and setup of the freeRTOS. From this point on, the operating system (as opposed to your application) will only display on the console when an error is detected.
   
   The display of these messages is a time-consuming process and the startup will take a few seconds (generally about 4-5). When executing with the release version (which prints nothing to the console), startup will only require a fraction of a second. A user application can be executed with either a debug or release version of the network binary, regardless whether debugging is enabled in the user applications.
   
   ===== 4.Common Interface Configuration Development =====
   
   
   This tool allows the device developer to define the device-specific parameters for each protocol (multiple devices can be defined in a single configuration). Also, items are defined to map data I/O from the application to the specific protocol.
   
   There are three basic elements available to use for a configuration:
   • Devices
   • Items
   • Baskets
   
   A device represents a product from the network perspective. It contains information like the device ID, manufacturer ID, ordering information, and some default behaviors (with the specifics varying depending on the protocol for which it is defined). While many devices can be defined in a single configuration, only a single device can be set during initialization of the Common Interface. This allows the user to use a common set of software across a range of products, by detecting what the hardware configuration is and selecting the appropriate device.
   
   With some protocols, there is a relationship between a Common Interface Device and the configuration file used by the protocol. For example, a PROFINET device would have all the information necessary to indicate to a PROFINET configuration utility or controller what GSDML file to associate with the device. Similarly, an EtherNet/IP CI Device would be associated with an EDS file. However, the developer is free to differentiate among the protocols: a PROFINET GSDML file may be associated with several different devices (or an entire product line).
   
   An item is used to define data-flow between the user’s application and the Common Interface. The most straight-forward items define cyclic I/O data. Other items may be used to define acyclic I/O, initialization parameters, alarms, diagnostic data, etc.
   
   The ways of accessing data over a network vary substantially for the various protocols. Therefore, with no difference in the user’s application code, a parameter for an I/O device (e.g. a scale factor for an analog input) can be mapped to an Acyclic read/write interface in PROFINET.
   
   Finally, baskets are collections of the other configuration elements. A basket typically contains a single CI Device and one or more CI items. This mechanism can be used to write a generic application that can support sets of items (e.g. I/O modules) that have not been developed at the time of application development. A configuration change will provide support.
   
   Further examples of the usage of these elements are provided later in this document as well as in the protocol-specific chapters of the design integration guide.
   
   ===== 5. API =====
   
   This document contains general descriptions of the Common Interface Application programming Interface (API). The more commonly used functions are discussed below. For more details on the data types, function parameters and function return values, see the header files referenced. 
   
   === 5.1.1 CI_basket_t * CI_GetBasket(CI_basketID_t id); ===
   
   This function returns a pointer to a basket. This includes a Device ID and some number of Item IDs. Typically, it would be used to define a device and associated I/O in the configuration data, while supporting several such devices in generic code. The code will request the basket and use the device and items that are returned.
   
   === 5.1.2 int CI_SetDeviceType(CI_deviceID_t deviceType); ===
   
   Called once during initialization, this function indicates to the Common Interface what device definition to look up. The configured definition includes protocol-specific information necessary to establish communications on the network. This allows a single configuration database to support multiple device types (and multiple I/O applications).
   
   === 5.1.3 CI_ItemHandle_t CI_AddItem(CI_itemID_t id, int location, int userID); === 
   
   Called one or more times during initialization, this function installs an item in the network application. An item represents data transferred between the user application and the network application. The item ID matches a protocol-specific description of the item in the network application’s configuration database. The location parameter can mean various things for different types of items, but is typically used to indicate where a module/etc. is plugged into a configurable device (it also allows the installation of multiple copies of a device type).
   
   The last parameter, userID is for the convenience of the programmer. When an event is received for an item (e.g. a read request for an acyclic I/O item), the userID provided in this call is provided to the user’s application to ease identification of the item in question.
   
   Note that for items representing cyclic or acyclic I/O, in protocols that use such information (e.g. PROFINET), the location will be directly translated to a slot/subslot number in the protocol.
   
   ===  5.1.4 int CI_ConfigComplete(int maxPeriod); === 
   
   Called once during initialization after the device has been set and all items have been added, this function indicates to the network application that it has a complete configuration and can begin network communications. The parameter (maxPeriod) is used to indicate the longest delay that the user’s application can tolerate during a subsequent call to CI_WaitIO().
   
   === 5.1.5 int CI_RemoveItem(CI_ItemHandle_t handle); ===
   
   Called during normal operation, this function indicates to the network application that an item has been removed from service (e.g. a module has been unplugged).
   
   === 5.1.6 int CI_ReturnItem(CI_ItemHandle_t handle); ===
   If CI_RemoveItem() has been called for a particular item, the application can return it to normal operation with a call to CI_ReturnItem().
   
   === 5.1.7 int CI_WriteItem(CI_ItemHandle_t handle, CI_IoStatus_t status, void *data_p); === 
   This function writes data for an item to the Network Application. The meaning of this depends on the nature of the item involved.
   
   For an item representing cyclic input data, this function will provide the data to be output to the network. The status parameter indicates the health of the input path (bad status indicates that a problem has been detected in the hardware). For this type of I/O, CI_WriteItem() will typically be called periodically for each set of inputs (e.g. for each input module in a modular system).
   
   Another example is acyclic I/O. This type of I/O is typically only written in response to a request from the protocol master (controller or scanner). In terms of the Common interface, this would be in response to an event received by the user application.
   
   Item writes can also be used to set or to clear alarms or diagnostic information, if supported by the underlying protocol.
   
   === 5.1.8 CI_IoStatus_t CI_ReadItem(CI_ItemHandle_t handle, CI_IoStatus_t status, void *data_p);  ===
   This function retrieves output data from the network application. In this case the status parameter indicates the health of the output circuitry. The return value indicates the quality/validity of the returned data.
   
   Similar to CI_WriteItem(), this routine would be called periodically for cyclic output data, and based on events received from the Common Interface for acyclic items, alarms, etc.
   
   === 5.1.9 int CI_SetDeviceParam(CI_Device_Param_ID_e paramID, void *paramData, int paramSize);===
   This interface supports the setting of several device-wide parameters. This can be used to override some settings in the configuration data or default behaviors (e.g. set MAC Address or IP address).
   
   ===  5.1.10 int CI_GetDeviceParam(CI_Device_Param_ID_e paramID, void *paramData, int paramSize); ===
   This interface provides access to device-wide parameters like MAC address or serial number, etc.
   
   === 5.1.11 int CI_SetItemParam(CI_itemHandle_t handle, CI_Item_Param_ID_e paramID, void *paramData, int paramSize); === 
   This interface supports the setting of several item-specific parameters. The specific elements that can be changed depend on the type of item involved. Some parameters are protocol-specific.
   
   === 5.1.12 int CI_GetItemParam(CI_itemHandle_t handle, CI_Item_Param_ID_e paramID, void
   *paramData, int paramSize); ===
   
   This interface provides access to item-specific parameters. The parameters available depend on the item type and protocol in use.
   
   === 5.1.13 int CI_IoComplete(); ===
   
   This interface indicates to the network application that the current I/O cycle is complete.
   
   === 5.1.14 int CI_GetEvent(CI_EventStruct_t *event, short block);===
   
   This function implements an event interface for the user application. It can be called in a polling fashion (if the ‘block’ parameter is zero), or, if used in a dedicated thread, it can be called with the ‘block’ parameter set to 1 and will pend until an event is available.
   
   If an event is returned, it includes the handle of the item that that event concerns, the userID associated with that item, and the type of action indicated by the event. This generic interface can then be used to indicate that an acyclic write has been requested by the controller, for example.
   
   === 5.1.15 int CI_SetSystemStatus(CI_SystemStatus_t status);  === 
   
   This interface sets the overall system status for the network application. This will be reflected in LEDs and/or network communications (depending on the protocol).
   
   === 5.1.16 CI_NetworkStatus_t CI_GetNetworkStatus(); === 
   
   This function retrieves the status of the network application and network connection.
   
   === 5.1.17 CI_task_t CI_taskCreateLowPriority(void (*TaskEntry)(void), char *name, int stackSize);===
   
   This interface allows the programmer to spawn additional threads. These threads will operate at a lower priority than the user’s main program. It is intended that cyclic I/O processing should operate at a high priority, so it should be done in the context of the main program. These threads are intended for such things as event handling, socket management, handling of other interfaces, etc.
   
   Note that these threads, while at a lower priority, still need to take some blocking action regularly so that other low priority processing can execute.
   
   === 5.1.18 int CI_TicksPerSecond();  ===
   
   This function returns the frequency of the system tick in the network application. It can be used in conjunction with the provided time and timer functions.
   
   === 5.1.19 long long CI_RunTimeInTicks();  === 
   
   This function returns the period that the system has been operating in system ticks (typically 1 ms per tick). Note that this is a 64-bit value.
   
   === 5.1.20 int CI_GetCyclicPeriod();=== 
   
   This function returns the period in system ticks of the current cyclic I/O connection. This function is not supported in all protocols, if not supported it returns an error indicating that the value is unknown.
   
   === 5.1.21 CI_periodicTimer_t CI_CreateTimer(unsigned int period);=== 
   
   This function creates a timer with the given period for use by the application.
   
   === 5.1.22 int CI_WaitOnTimer(CI_periodicTimer_t timer); === 
   
   This function blocks operation of the user application until a timer created by a call to CI_CreateTimer() triggers.
   
   === 5.1.23 int CI_WaitIO();  ===
   
   This function blocks operation of the user application until data has been exchanged with the network. A timeout on this delay is set in the call to CI_ConfigComplete() (for example; so the application will continue to execute on the loss of a connection).
   
   === 5.1.24 CI_RequestReset(); ===
   
   This function causes a hard reset of the microprocessor, which will in turn reset the entire device.
   
   ===== Common Interface Complete API =====
   
   ==== 6.1 CI-srv/inc/CI_Codes.h ====
   
   The CI_Codes.h are in place to support specific Common Interface codes. The codes can be defined as seen below. 
   
   
   <code>
   /*
     * Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    /* Exclusionary ifdef */
    #ifndef _CI_CODES_H_
    #define _CI_CODES_H_
     
    // Includes *******************************************************************
    // End Includes ***************************************************************
     
    // Macros, typedefs, enums ****************************************************
    /* Success/error codes */
    #define CI_OK              0
    #define CI_ERROR          -1
    #define CI_INVALID_PARAM  -2
    #define CI_MEMORY_ERROR   -3
    #define CI_VERSION_ERROR  -4
    #define CI_TIMEOUT        -5
    #define CI_UNKNOWN        -6
     
    #define CI_EMPTY             -100
    #define CI_NOT_SUPPORTED     -101
    #define CI_NO_ENTRY          -102
    #define CI_READ_ONLY         -103
    #define CI_TIME_NOT_SYNCED   -104
     
    /* CI_MAX_SOCKETS sets the number of sockets to be supported by the application.
     * This macro is further used in CI_socket_defines.h to calculate the size of
     * fd_set member variable (fd).
     */
    #define CI_MAX_SOCKETS       50 
     
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Macros, typedefs, enums ************************************************
     
    // Global Variables (externs, globals, static globals) ************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Global Variables *******************************************************
     
    // Functions ******************************************************************
    // End Functions **************************************************************
     
    #endif /* _CI_CODES_H_ */
   </code>
   
   ==== 6.2 CI-srv/inc/CI_config_api.h  ====
   <code>
    /*
     *  Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     *  This software is proprietary and confidential to Analog Devices, Inc. and
     *  its licensors.
     */
    #ifndef H_CI_CFG_CONFIG_API
    #define H_CI_CFG_CONFIG_API
     
    #include "CI_config_types.h"
     
    /*
     * Open a database connection. Selects the data domain, the store and if write
     * permission is required. Returns a context handle that is used to access the
     * database.
     *
     * This is the first function a user must call to be able to access any of the
     * other functionality
     * in this API.
     *
     * Database connections are bound to a thread/task and ensure consistent
     * manipulation of data.
     * A connection is bound to a specific domain and store. Write access is
     * required for writing, committing, revoking and discarding a candidate. Write
     * access is ignored for other stores than candidate.
     *
     *  [in]      domain_p, default is "net" is domain is NULL. Enables to use this
     *            database for more than network config only. Example would be
     *            "ci-io" for io configuration of common interface devices/items.
     *  [in]      store, selects the store to be accessed (candidate,running,
     *            status, ...)
     *  [in]      wraccess: requesting write permission. If true the caller has
     *            write permission
     *  [out]     dhch_p, the database handle, is the identifier returned by this call
     *            and is used to identify this db connection in subsequent calls to
     *            access the database
     *
     *  return    CI_OK
     *            CI_INVALID_PARAM
     *            CI_ERROR if maximum number of data base connections is exceeded
     *            CI_READ_ONLY if there is another process already connected to
     *            the same domain/store with write permission.
     *
     */
    CI_openCfg_t CI_OpenCfg;
     
     
    /*
     *  Close a connection. After closing the connection, the dbch can no
     *  longer be used to access the database
     *
     *  [in]      dbch, database connection handle
     *
     *  return    CI_OK
     *            CI_ERROR if there is no open connection
     *
     */
    CI_closeCfg_t CI_CloseCfg;
     
     
    /*
     * Register a notification callback (one for each connection)
     *
     * [in]       domain
     * [in]       cb_p    Notification callback function
     *
     * return     CI_OK
     *            CI_ERROR
     *            CI_INVALID_PARAM
     */
    CI_regConfigEvt CI_RegConfigEvt;
     
     
    /*
     * Read an object from the database. The return values are in text form.
     *
     * [in]       dbch, database connection handle
     * [in]       path_p to the object
     * [in]       value_p, a buffer to receive the \0 terminated string
     * [in]       size of the value buffer
     *
     * return     CI_OK
     *            CI_NO_ENTRY if object does not exist
     *            CI_ERROR if value is not properly formated or the receiving
     *            buffer (value_p) is too small to hold the value
     *
     */
    CI_readCfg_t CI_ReadCfg;
     
     
    /*
     * Write an object to the database. The values are in text form.
     *
     * [in]       dbch, database connection handle
     * [in]       path_p to the object
     * [in]       value_p, a buffer to receive the \0 terminated string
     *
     * return     CI_OK
     *            CI_READ_ONLY or
     *            CI_NO_ENTRY if object does not exist
     *            CI_ERROR if value is not properly formated
     *
     * Note       Only possible if data store is CI_storeCandidate and database
     *            connection got write permission
     */
    CI_writeCfg_t CI_WriteCfg;
     
     
    /*
     * Each node in the database tree can have attribute. This function is designed
     * to retrieve the attribute for the node designated by path_p. This may be an
     * object, but also a node item or anything else.
     *
     * Attributes can be everything from an uri, a node type ("ntype"), object size,
     * elements in an list ("len")
     *
     * [in]       dbch, database connection handle
     * [in]       path_p into database
     * [in]       attr_p string, name of the attribute to read
     * [out]      value_p, a buffer to receive the \0 terminated string
     * [in]       size of the value buffer
     *
     * return     CI_OK
     *            CI_NO_ENTRY if object does not exist
     *            CI_ERROR if value is not properly formated
     */
    CI_readAttr_t CI_ReadAttr;
     
     
    /*
     *  Initialize a enumeration. A start path defines the starting point for the
     *  enumeration within data tree.
     *
     * [in]       dbch, database connection handle
     * [in]       The start_p path. If NULL, "", or "/" the starting point is the
     *            root of the domain/data store given by dbch
     * [in]       nodes, if 0 only  data object nodes are iterated. If not 0, all
     *            nodes are iterated
     *
     * return     CI_OK
     */
    CI_newEnum_t CI_NewEnum;
     
     
    /*
     * Travers the database starting at the root set by CI_NewEnum
     *
     * [in]       dbch, database connection handle
     * [out]      name_p returns the name of current object. Can be zero is not
     *            needed
     * [out]      value_p returns the value of current object. Can be zero is not
     *            needed
     * [in/out]   psize holds the size available to store the path and receives the
     *                  actual size of the path (including trailing zero) on return
     * [in/out]   vsize holds the size available to store the value and receives the
     *                  actual size of the value (including trailing zero) on return
     * [out]      node  If true, the retrieved values refer to a non-value element
     *                  in the path
     *
     * return     CI_OK if path and/or value have been retrieved as requested
     *            CI_INVALID_PARAM
     *            CI_ERROR if maximum number of data base connections is exceeded
     *            CI_NO_ENTRY enumeration complete, no more data in tree
     */
    CI_enumerate_t CI_Enumerate;
     
    /* data store management
     *
     *  - we do not support editing of the running configuration store.
     *  - or better said, we support write to candidate store only
     *
     */
     
    /*
     * Commit a candidate to running.
     *
     * This call require that the database connection (dbch) got write permission.
     *
     * Running store becomes the backup store, Candidate store becomes running store
     * If a timeout is set, no further edits to candidate are allowed until the
     * timeout is expired.
     * If another commit is executed while a timeout is still pending, the new
     * timeout overrides the previous value. This can be used to prolong the commit
     * timeout or to make a commit permanent.
     *
     * [in]       dbch, database connection handle
     * [in]       tout_in_sec, 0 means NO TIMEOUT (commit for ever)
     *                        max value for tout_in_sec is 3600. If its higher, it
     *                        will be limited to 3600
     *
     * return     CI_OK
     *            CI_READ_ONLY or
     *            CI_NO_ENTRY
     *
     * Note       Requires write access
     */
    CI_commit_t CI_Commit;
     
    /*
     * Revoke a running candidate.
     *
     * This call require that the database connection (dbch) got write permission.
     *
     * Backup store becomes the running store, running store becomes candidate
     * store.
     * Edits made in candidate since last commit are lost if not saved to file
     * before revoke.
     * Revoke can only be executed after a previously executed Commit
     *
     * [in]       dbch, database connection handle
     *
     * return     CI_OK
     *            CI_READ_ONLY or
     *            CI_NO_ENTRY
     *
     * Note       Requires write access
     */
    CI_revoke_t CI_Revoke;
     
    /*
     * Discard a candidate.
     *
     * This call require that the database connection (dbch) got write permission.
     *
     * Override pending edits of the candidate with the current values from the
     * running store.
     * Used to get rid of bad edits.
     *
     * [in]       dbch, database connection handle
     +
     * return     CI_OK
     *            CI_READ_ONLY or
     *            CI_NO_ENTRY
     *
     * Note       Requires write access
     */
    CI_discard_t CI_Discard;
     
     
    /* save/load files */
     
    /*
     * Save (serialize) a Store to a file.
     *
     * If default startup file is addressed, this call require that the database
     * connection (dbch) got write permission.
     *
     * [in]       dbch, database connection handle
     * [in]       file_p  The file. If NULL or "", the default startup file is used
     *
     * return     CI_OK
     *            CI_READ_ONLY or
     *            CI_ERROR
     */
    CI_saveCfg_t CI_SaveCfg;
     
    /*
     * Load (de-serialize) a Store from file.
     *
     * [in]       dbch, database connection handle
     * [in]       file_p  The file. If NULL or "", the default startup file is used
     *
     * return     CI_OK
     *            CI_INVALID_PARAM
     *            CI_ERROR
     *
     * Note       Does require write access
     */
    CI_loadCfg_t CI_LoadCfg;
     
    #endif
   </code>
   
   ==== 6.3 CI-srv/inc/ CI_config_types.h ====
   <code>
     *  Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     *  This software is proprietary and confidential to Analog Devices, Inc. and
     *  its licensors.
     */
    #ifndef H_CI_CFG_CONFIG_TYPES
    #define H_CI_CFG_CONFIG_TYPES
     
    #include "CI_config.h"
     
    #define CI_CFG_VER_MAJ  0x01
    #define CI_CFG_VER_MIN  0x00
    #define CI_CFG_VER      ((CI_CFG_VER_MAJ << 16) | CI_CFG_VER_MIN)
    #define CI_CFG_NAME     ("CI_config")
     
    /* API Function Name List */
    #define CI_CFG_NAME_VERSION              ("Version")         /* 1st in list */
    #define CI_CFG_NAME_OPEN_DB              ("open")
    #define CI_CFG_NAME_CLOSE_DB             ("close")
    #define CI_CFG_NAME_REG_NOTIF            ("registerNoti")
    #define CI_CFG_NAME_READ_OBJ             ("readObj")
    #define CI_CFG_NAME_WRITE_OBJ            ("writeObj")
    #define CI_CFG_NAME_READ_ATTR            ("readAttr")
    #define CI_CFG_NAME_INIT_ENUM            ("initEnum")
    #define CI_CFG_NAME_ENUMERATE            ("enumerate")
    #define CI_CFG_NAME_COMMIT               ("commitConfig")
    #define CI_CFG_NAME_REVOKE               ("revokeCommit")
    #define CI_CFG_NAME_DISCARD              ("discardCand")
    #define CI_CFG_NAME_SAVE                 ("saveConf")
    #define CI_CFG_NAME_LOAD                 ("loadConf")
     
    /*
     * Open a database connection. Selects the data domain, the store and if write
     * permission is required. Returns a context handle that is used to access the
     * database.
     */
    typedef int32_t (CI_openCfg_t)(char *domain_p,
                                   CI_store_t store,
                                   int32_t wraccess,
                                   int32_t *dbch_p);
    typedef CI_openCfg_t (*CI_openCfg_tp);
     
     
    /*
     *  Close a connection. After closing the connection, the dbch can no
     *  longer be used to access the database
     *
     *  [in]      dbch, database connection handle
     *
     *  return    TSNA_OK
     */
    typedef int32_t (CI_closeCfg_t)(int32_t dbch);
    typedef CI_closeCfg_t (*CI_closeCfg_tp);
     
     
    /*
     * Notification Callback. A driver or stack can issue a notification, that is an
     * event that is codified in a modules definition (YANG), to the database using
     * TSNA_eventType_t (see TSNA_CTR api). The database will translate the
     * notification from the driver/stack  * into a ascii (ascii subset of uft8)
     * formated notification that in turn is pushed to any application
     * with an open connection to the status store of the affected module.
     */
    typedef int32_t (CI_CFG_notificationCB_t)(char *path_p,
                                              uint16_t nargs,
                                              CI_keyValuePair_t *argv_p);
    typedef CI_CFG_notificationCB_t (*CI_CFG_notificationCB_tp);
     
    /*
     * Register a notification callback (one for each connection)
     */
    typedef int32_t (CI_regConfigEvt)(int32_t dbch,
                                      CI_CFG_notificationCB_tp cb_p);
    typedef CI_regConfigEvt (*CI_regConfigEvtp);
     
     
    /*
     * Read an object from the database. The return values are in text form.
     */
    typedef int32_t (CI_readCfg_t)(int32_t dbch,
                                   char *path_p,
                                   char *value_p,
                                   uint16_t size);
    typedef CI_readCfg_t (*CI_readCfg_tp);
     
     
    /*
     * Write an object to the database. The values are in text form.
     */
    typedef int32_t (CI_writeCfg_t)(int32_t dbch,
                                    char *path_p,
                                    char *value_p);
    typedef CI_writeCfg_t (*CI_writeCfg_tp);
     
     
    /*
     * Each node in the database tree can have attribute. This function is designed
     * to retrieve the attribute for the node designated by path_p. This may be an
     * object, but also a node item or anything else.
     */
    typedef int32_t (CI_readAttr_t)(int32_t dbch,
                                    char *path_p,
                                    char *attr_p,
                                    char *value_p,
                                    uint16_t size);
    typedef CI_readAttr_t (*CI_readAttr_tp);
     
     
    /*
     *  Initialize a enumeration. A start path defines the starting point for the
     *  enumeration within data tree.
     *
     */
    typedef int32_t (CI_newEnum_t)(int32_t dbch,
                                   char *start_p,
                                   CI_nodeType_t select);
    typedef CI_newEnum_t (*CI_newEnum_tp);
     
     
    /*
     * Travers the database starting at the root set by CI_NewEnum
     *
     */
    typedef int32_t (CI_enumerate_t)(int32_t dbch,
                                     char *name_p,
                                     char *value_p,
                                     uint16_t *nsize_p,
                                     uint16_t *vsize_p,
                                     CI_nodeType_t *ntype_p);
    typedef CI_enumerate_t (*CI_enumerate_tp);
     
     
     
    /*
     * Commit a candidate to running.
     *
     */
    typedef int32_t (CI_commit_t)(int32_t dbch,
                                  char *path_p,
                                  uint16_t tout_in_sec);
    typedef CI_commit_t (*CI_commit_tp);
     
    /*
     * Revoke a running candidate.
     *
     */
    typedef int32_t (CI_revoke_t)(int32_t dbch,
                                  char *path_p);
    typedef CI_revoke_t (*CI_revoke_tp);
     
    /*
     * Discard a candidate.
     */
    typedef int32_t (CI_discard_t)(int32_t dbch,
                                   char *path_p);
    typedef CI_discard_t (*CI_discard_tp);
     
     
    /* save/load files */
     
    /*
     * Save (serialize) a Store to a file.
     */
    typedef int32_t (CI_saveCfg_t)(int32_t dbch,
                                   char *file_p);
    typedef CI_saveCfg_t (*CI_saveCfg_tp);
     
    /*
     * Load (de-serialize) a Store from file.
     */
    typedef int32_t (CI_loadCfg_t)(int32_t dbch,
                                   char *file_p);
    typedef CI_loadCfg_t (*CI_loadCfg_tp);
     
     
    #endif
   
   </code>
   
   ==== 6.4 CI-srv/inc/ CI_config.h  ====
   <code>
   /*
   /*
     *  Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     *  This software is proprietary and confidential to Analog Devices, Inc. and
     *  its licensors.
     */
    #ifndef H_CI_CONFIG_AND_CONTROL_API_INC
    #define H_CI_CONFIG_AND_CONTROL_API_INC
     
     
    #include <stdint.h>
    #include <limits.h>
    #include "CI_codes.h"
     
    typedef enum {
      CI_storeCandidate,
      CI_storeRunning,
      CI_storeBackup,
      CI_storeStartup,
      CI_storeStatus,                          // formally not a store, it easier to
                                          // handle it like one
      CI_illegal=INT16_MIN,
      CI_storeLast=INT16_MAX
    } CI_store_t;
     
    typedef enum {
      CI_isValue=0x01,
      CI_isNode=0x02,
      CI_isAttribute=0x03,
      CI_isNIL=0,
      CI_isLast=INT8_MAX
    } CI_nodeType_t;
     
    typedef struct {
      char *key_p;
      char *value_p;
    } CI_keyValuePair_t;
     
    /*
     * event types of the callback routine
     */
    typedef enum {
      CI_evtStop,
      CI_evtStart,
      CI_evtReqStatus,
      CI_evtNewConfig,
      CI_evtRPC,
      CI_evtReset,
      CI_evtSIZE=INT16_MAX
    } CI_eventType_t;
     
    #endif
   
   </code>
   
   ==== 6.5 CI-srv/inc/ CI_control_api.h ====
   <code>
   /*
     *  Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     *  This software is proprietary and confidential to Analog Devices, Inc. and
     *  its licensors.
     */
    #ifndef H_CI_CONTROL_API
    #define H_CI_CONTROL_API
     
    #include "CI_control_types.h"
     
    /*
     * Register a driver with the database
     *
     * [in]       name of this driver instance (debug)
     * [out]      thisDriverID_p, a handle to identify this driver instance
     * [in]       cb_p, the callback function for this driver
     *
     * return     error code
     */
    CI_regDriver_t CI_RegDriver;
     
    /*
     * Instantiate a YANG module for this driver or stack
     *
     * [in]       path_p, identifies the module (Example "net/ieee802-dot1q-sched")
     * [in]       name_p, name under which the module get registered. Examples "P0",
     *            "ETH0"
     *            note: different module types can be registered under same name!
     * [in]       instanceID to identify the instance with any callbacks
     *
     * return     CI_OK
     *            CI_INVALID_PARAM
     *            CI_ERROR
     */
    CI_addModule_t CI_AddModule;
    /*
     * Fire a notification. YANG allows to define notifications that
     * are pushed upstream. This function is designed to support this mechanism
     *
     * [in]       path identifying the notification
     * [in]       ndata_p points to a structure that holds the parameters that
     *                  are required for this notification
     * [in]       nsize the size of the argument structure. Needed for error
     *                  checking only
     *
     * return     CI_OK
     *            CI_INVALID_PARAM
     */
    CI_fireEvent_t CI_FireEvent;
     
    CI_enableGateway_t CI_EnableGateway;
     
     
    #endif
   </code>
   
   ==== 6.6 CI-srv/inc/ CI_control_types.h ====
   <code>
     */
    typedef int32_t (CI_eventCB_t)(CI_eventType_t event,
                                   uint16_t instanceID,
                                   void *arg_p);
    typedef CI_eventCB_t (*CI_eventCB_tp);
     
    /*
     * Register a driver with the database
     */
    typedef int32_t (CI_regDriver_t)(char *name_p,
                                     uint16_t *thisDriverID_p,
                                     CI_eventCB_tp cb_p);
    typedef CI_regDriver_t (*CI_regDriver_tp);
     
    /*
     * Instantiate a YANG module for this driver or stack
     */
    typedef int32_t (CI_addModule_t)(uint16_t drv,
                                     char *path_p,
                                     char *name_p,
                                     uint16_t instanceID);
    typedef CI_addModule_t (*CI_addModule_tp);
    /*
     * Fire a notification.
     */
    typedef int32_t (CI_fireEvent_t)(char *path_p,
                                     void *ndata_p,
                                     uint16_t nsize);
    typedef CI_fireEvent_t (*CI_fireEvent_tp);
     
    /*
     * Enable TSN gateway functionality
     */
    typedef int32_t (CI_enableGateway_t)(void);
    typedef CI_enableGateway_t (*CI_enableGateway_tp);
     
    #endif
   
   </code>
   ==== 6.7 CI-srv/inc/ CI_debug.h ====
   <code>
   
   
   /*
     * Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    #ifndef DEBUG_H
    #define DEBUG_H
     
    #include <stdio.h>
     
    #define DBG_SHOW_ERROR  0
    #define DBG_SHOW_INFO   0
     
    #ifdef NDEBUG
    #define DBG_PRINT(...)
    #else
    #include <stdio.h>
     
    #define DBG_STRINGIFY(x)  #x
    #define DBG_TO_STRING(x)  DBG_STRINGIFY(x)
    #define DBG_AT            "[" __FILE__ ":" DBG_TO_STRING(__LINE__) "]"
    #define DBG_PRINT(...)    printf(DBG_AT " " __VA_ARGS__)
    #endif
     
    #if DBG_SHOW_ERROR == 1
    #define DBG_ERROR(...)    DBG_PRINT("ERROR: " __VA_ARGS__)
    #else
    #define DBG_ERROR(...)
    #endif
     
    #if DBG_SHOW_INFO == 1
    #define DBG_INFO(...)     DBG_PRINT("INFO: " __VA_ARGS__)
    #else
    #define DBG_INFO(...)
    #endif
     
    /* Note do-while is to guard the if statement */
    #define DBG_ASSERT(x)               \
      do {                              \
        if (!x) {                       \
          DBG_PRINT(" ASSERT\n");       \
          while(1);                     \
        }                               \
      } while(0)
     
    #endif /* DEBUG_H_ */
   
   
   </code>
   ==== 6.8 CI-srv/inc/ CI_devices.h====
   <code>
   /*
     *  Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     *  This software is proprietary and confidential to Analog Devices, Inc. and
     *  its licensors.
     */
    #ifndef H_CI_CONTROL_TYPES
    #define H_CI_CONTROL_TYPES
     
    #include "CI_config.h"
     
    #define CI_VER_MAJ  0x01
    #define CI_VER_MIN  0x00
    #define CI_VER      ((CI_VER_MAJ << 16) | CI_VER_MIN)
    #define CI_NAME     ("CI_control")
     
    /* API Function Name List */
    #define CI_NAME_VERSION           ("Version")           /* 1st in list */
    #define CI_NAME_REG_DRIVER        ("regDriver")
    #define CI_NAME_ADD_MODULE        ("addModule")
    #define CI_NAME_FIRE_NOTI         ("fireNoti")
    #define CI_NAME_ENABLE_GATEWAY    ("enGateway")
     
     
    /*
     * the control api has to deal with two data stores only:
     * - STATUS: data from the driver/stack towards the database
     * - RUNNING: current config data towards the driver/stack
     */
     
     
    /*
     * Callback function receive updates from the configuration database
    /*
     * Copyright (c) 2018 - 2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    /* Exclusionary ifdef */
    #ifndef _CI_DEVICES_H_
    #define _CI_DEVICES_H_
     
    /*****************************************************************************
     *
     * This file contains device structures to be used with the
     * CI_SetDeviceCustom() function
     *
     ****************************************************************************/
     
    // Includes *******************************************************************
    #include <stdint.h>
     
    // End Includes ***************************************************************
     
    // Macros, typedefs, enums ****************************************************
    /* PROFINET macros */
    #define CI_PNET_DEVICE_TYPE_LENGTH        240
    #define CI_PNET_DEVICE_ORDER_ID_LENGTH    20
    #define CI_PNET_DEVICE_SNMP_BUFFER_LENGTH 256
    #define CI_PNET_MAX_STATION_NAME_LENGTH   240
     
    #define CI_PNET_DEVICE_VERSION            0
     
    // EtherNet/IP macros
    #define CI_EIP_NUM_ETH_PORTS              2
    #define CI_EIP_MAX_PRODUCT_NAME_SIZE      33
    #define CI_EIP_DOMAIN_NAME_LENGTH         49
    #define CI_EIP_HOST_NAME_LENGTH           65
     
    #define CI_EIP_DEVICE_VERSION             2
     
    // EtherCAT macros
    #define MAX_DEVICE_NAME_STR_LEN           32    // Including NULL terminator
    #define MAX_HW_VERSION_STR_LEN            8     // Including NULL terminator
    #define MAX_SW_VERSION_STR_LEN            8     // Including NULL terminator
     
    #define CI_ECAT_DEVICE_VERSION            0
     
    // ----------------------------------------------------------------------------
     
    /* PROFINET device structure */
    typedef struct {
      uint16_t  vendorID;
      uint16_t  deviceID;
      uint16_t  profileID;
      uint16_t  profileType;
      uint32_t  moduleID;
      uint32_t  subModuleID;
      uint8_t   majorRevision;    /* Functional enhancement */
      uint8_t   minorRevision;    /* Bug fix */
      uint8_t   internalRevision; /* internal change */
      uint8_t   revisionCounter;
      int8_t    deviceType[CI_PNET_DEVICE_TYPE_LENGTH];
      int8_t    orderID[CI_PNET_DEVICE_ORDER_ID_LENGTH];
     
      /* SNMP data */
      uint32_t  enterpriseID;    /* Private SNMP OID */
     
      /* SNMP sys desc Mib2 */
      int8_t    systemDescription[CI_PNET_DEVICE_SNMP_BUFFER_LENGTH];
     
      /* InternalIf desc Mib2*/
      int8_t    internalInterface[CI_PNET_DEVICE_SNMP_BUFFER_LENGTH];
     
      /* Port IF desc Mib2 */
      int8_t    port1Interface[CI_PNET_DEVICE_SNMP_BUFFER_LENGTH];
     
      /* Port IF desc Mib2 */
      int8_t    port2Interface[CI_PNET_DEVICE_SNMP_BUFFER_LENGTH];
    } __attribute__ ((packed)) CI_profinetDevice_t;
     
    /* EtherNet/IP device structure */
    typedef struct {
      uint8_t   type;             /* Always 3 */
      int8_t    pad1;             /* Always 0 */
      uint16_t  vendorID;         /* Valid range 0-65535 */
      uint16_t  productType;      /* Valid range 0-65535 */
      uint16_t  productCode;      /* Valid range 0-65535 */
      uint16_t  majorRevision;    /* Valid range 0-255 */
      uint16_t  minorRevision;    /* Valid range 0-255 */
     
      /* The following portion of this structure contains the data that is used
       * as the "out of the box" defaults */
      uint8_t   use_dhcp;         /* 0 = static IP, non-zero = use DHCP */
      int8_t    pad2;             /* Always 0 */
      uint32_t  ipaddr;           /* Local IP address (if DHCP disabled)
                                   *   e.g. 192.168.21.26 is 0xc0a8151a */
      uint32_t  subnetMask;       /* Local subnet mask (if DHCP disabled)
                                   *   e.g. 255.255.255.0 is 0xffffff00 */
      uint32_t  defaultGateway;   /* Local gateway IP address (if DHCP disabled),
                                   * formatted as above */
      uint32_t  dns[2];           /* DNS server IP addresses (if DHCP disabled)
                                   * [0] for primary, [1] for secondary, formatted
                                   * as above */
      uint8_t   ifc_speed[CI_EIP_NUM_ETH_PORTS];  /* 0 = 10 Mbps, 1 = 100 Mbps */
      uint8_t   ifc_duplex[CI_EIP_NUM_ETH_PORTS]; /* 0 = half, 1 = full */
      uint8_t   ifc_use_autonegotiation[CI_EIP_NUM_ETH_PORTS]; /* 0 = force
                                                                * 1 = auto */
      uint8_t   byTTLValue;     /* Used by EtherNet/IP stack, see EIP Spec */
      uint8_t   byAllocControl; /* Used by EtherNet/IP stack, see EIP Spec */
      uint16_t  iNumMulticast;  /* Used by EtherNet/IP stack, see EIP Spec */
      uint8_t   use_ACD;        /* 0=don't, 1=do use Address Conflict Detection */
      int8_t    pad3;           /* always 0 */
     
      /* EtherNet/IP Ethernet Link Object settings */
      uint8_t   byAdminState[CI_EIP_NUM_ETH_PORTS]; /* 1=enable port
                                                     * 2=disable port */
      uint32_t  lMCastStartAddr; /* Used by EtherNet/IP stack, see EIP Spec */
     
      int8_t    productName[CI_EIP_MAX_PRODUCT_NAME_SIZE]; /* Local product name */
      int8_t    domain_name[CI_EIP_DOMAIN_NAME_LENGTH];  /* Local domain name (if
                                                          * DHCP disabled) */
      int8_t    host_name[CI_EIP_HOST_NAME_LENGTH];      /* Local host name */
      int8_t    pad4;      /* always 0 */
     
      uint8_t   dlrEnable; /* 0 = disable DLR, */
                           /* 1 = enable DLR   */
      int8_t    pad5;      /* Always 0 */
      uint16_t CI_deviceExtID; // Object number containing Extension Object info
    } __attribute__ ((packed)) CI_etherNetIpDevice_t;
     
    /* EtherCAT device structure*/
    typedef struct {
      uint32_t vendorId;                  // Vendor ID (from MDP object 0x1018)
      uint32_t productCode;               // Product Code (from MDP object 0x1018)
      uint8_t deviceName[MAX_DEVICE_NAME_STR_LEN];  // Device name (MDP object 0x1008)
      uint8_t hwVersion[MAX_HW_VERSION_STR_LEN];    // Hardware version (MDP object 0x1009)
      uint8_t swVersion[MAX_SW_VERSION_STR_LEN];    // Software version (MDP object 0x100A)
      uint16_t majorRevNum;               // Major revision number (from MDP object 0x1018)
      uint16_t minorRevNum;               // Minor revision number (from MDP object 0x1018)
    } __attribute__ ((packed)) CI_ethercatDevice_t;
     
    // ----------------------------------------------------------------------------
    // End Macros, typedefs, enums ************************************************
     
    // Global Variables (externs, globals, static globals) ************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Global Variables *******************************************************
     
    // Functions ******************************************************************
    // End Functions **************************************************************
     
    #endif /* _CI_DEVICES_H_ */
   
   </code>
   ==== 6.9 CI-srv/inc/ CI_extensions.h ====
   <code>
   
   /*
     * Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    /* Exclusionary ifdef */
    #ifndef _CI_EXTENSIONS_H_
    #define _CI_EXTENSIONS_H_
     
    /*--------------------------------------------------------------------------*/
    /*------------ EtherNet/IP Stack Common Interface Extension Sectionn -------*/
     
    /* Note Update this version number in case of ANY change to the EIP LED interface
     * extension (enums and function calls) */
    /* EIP led interface extension version */
    #define CI_LED_IF_EXT_VER       1
     
    /* Enumerations for CI_ifExtLedApi CI interface extension */
    typedef enum {
      CI_ledMod,
      CI_ledNet,
    } CI_ledStatus_t;
     
    typedef enum {
      CI_ledOff,
      CI_ledRedOn,
      CI_ledRedFlashing,
      CI_ledGreenOn,
      CI_ledGreenFlashing,
    } CI_ledStatusState_t;
     
    /* Functions for CI_ifExtLedApi interface extension */
     
    typedef int32_t CI_LedGetStatusStateFunct_t(CI_ledStatus_t led,
                                                CI_ledStatusState_t *state_p);
    CI_LedGetStatusStateFunct_t CI_LedGetStatusState;
     
    typedef int32_t CI_LedSetStatusStateFunct_t(CI_ledStatus_t led,
                                                CI_ledStatusState_t state);
    CI_LedSetStatusStateFunct_t CI_LedSetStatusState;
     
    /* Structure holding function pointer to callbacks to be passed to interface
     * exension function */
    typedef struct {
      CI_LedGetStatusStateFunct_t *CI_LedGetStatusStateFunct_p;
      CI_LedSetStatusStateFunct_t *CI_LedSetStatusStateFunct_p;
    } CI_LedStatusIfExt_t;
     
    /*--------------------------------------------------------------------------*/
    /*------------ PROFINET Stack Common Interface Extension Section ------------*/
     
    #define CI_PNET_STACK_VERSION   4
     
    typedef enum {
      alarmPriorityUnknown,
      alarmPriorityLow = 5,
      alarmPriorityHigh = 6
    } alarmPriority_t;
     
    typedef enum {
      alarmDiagnosis        = 0x01,
      alarmProcess          = 0x02
    } alarmType_t;
     
    typedef enum {
      Unknown_error = 0,  /* Reserved */
      Short_circuit,
      Undervoltage,
      Overvoltage,
      Overload,
      Overtemperature,
      Line_break,
      Upper_limit_exceeded,
      Lower_limit_exceeded,
      Error,
      Simulation_active,
      Parameter_missing = 0x000f,
      Parameter_fault,
      Power_fault,
      Fuse_blown,
      Comm_fault,
      Ground_fault,
      Reference_lost,
      Process_lost,
      Threshold_warning,
      Output_disabled,
      External_fault = 0x001a,
      ManufactureSpecific,
      Temporary_fault = 0x001f,
    } diagChannelError_t;
     
    typedef enum {
      Input = 1,
      Output,
      In_out,
    } diagChannelDir_t;
     
    typedef int32_t CI_PnetSendAlarm_t(alarmPriority_t alarmPriority,
                                       alarmType_t alarmType,
                                       uint16_t slot,
                                       uint16_t subslot,
                                       uint16_t alarmSpecifier,
                                       uint8_t *alarmData_p,
                                       uint16_t alarmDataLength,
                                       uint16_t usrStructureIdentifier);
    CI_PnetSendAlarm_t CI_PNET_Ext_SendAlarm_Func;
     
    typedef int32_t CI_PnetSendDiag_t(uint16_t slot,
                                      uint16_t subslot,
                                      uint16_t diagType,
                                      uint16_t channelNumber,
                                      uint16_t channelType,
                                      diagChannelDir_t direction,
                                      uint8_t *manSpecificData_p,
                                      uint16_t dataLen);
    CI_PnetSendDiag_t CI_PNET_Ext_SendDiag_Func;
     
    typedef int32_t CI_PnetClearDiag_t(uint16_t slot,
                                       uint16_t subslot,
                                       uint16_t diagType,
                                       uint16_t channelNumber,
                                       uint16_t channelType,
                                       diagChannelDir_t direction);
    CI_PnetClearDiag_t CI_PNET_Ext_ClearDiag_Func;
     
    typedef int32_t (CI_PnetAddItem_t)(uint16_t id,
                                       void *data_p,
                                       uint32_t bufSize,
                                       uint16_t slot,
                                       uint16_t subslot);
    CI_PnetAddItem_t CI_PNET_Ext_AddItem_Func;
     
    typedef int32_t CI_PnetModuleDiffFunct_t (uint16_t ARindix,
                                              uint32_t API,
                                              uint16_t slot,
                                              uint16_t subslot,
                                              uint32_t realModuleID,
                                              uint32_t expectedModuleID,
                                              uint32_t realsubmoduleID,
                                              uint32_t expectedSubmoduleID);
    CI_PnetModuleDiffFunct_t CI_PNET_Ext_ModuleDiff_CB;
     
    typedef int32_t CI_PnetParameterEnd_t (uint16_t ARindix);
    CI_PnetParameterEnd_t CI_PNET_Ext_ParamEnd_CB;
     
    /* Structure holding function pointer to callbacks to be passed to interface
     * exension function */
    typedef struct {
      CI_PnetModuleDiffFunct_t* CI_PNET_Ext_ModuleDiff_p;
      CI_PnetParameterEnd_t* CI_PNET_Ext_ParamEnd_p;
    } CI_PnetCallbackFunctionTable_t;
     
    /* Structure holding function pointer to callbacks to be passed to interface
     * exension function */
    typedef struct {
      CI_PnetSendAlarm_t* CI_PNET_Ext_SendAlarm_Func_p;
      CI_PnetSendDiag_t* CI_PNET_Ext_SendDiag_Func_p;
      CI_PnetClearDiag_t* CI_PNET_Ext_ClearDiag_Func_p;
      CI_PnetAddItem_t* CI_PNET_Ext_AddItem_Func_p;
    } CI_PnetInterfaceFunctionTable_t;
     
     
    /*---------------------------------------------------------------------------*/
    /*--------------- Place Other Protocol Extension Sections Below Here --------*/
     
    #endif /* _CI_EXTENSIONS_H_ */
   
   </code>
   ==== 6.10 CI-srv/inc/ CI_hardware_api.h ====
   <code>
   /*
     * Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    /* Exclusionary ifdef */
    #ifndef _CI_HARDWARE_API_H_
    #define _CI_HARDWARE_API_H_
     
    // Includes *******************************************************************
    #include "CI_hardware_types.h"
     
    // End Includes ***************************************************************
     
    // Macros, typedefs, enums ****************************************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Macros, typedefs, enums ************************************************
     
    // Global Variables (externs, globals, static globals) ************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Global Variables *******************************************************
     
    // Functions ******************************************************************
    CI_getAvailableTimerCount_t CI_GetAvailableTimerCount;
     
    CI_timerSetSignal_t CI_ConfigureTimerSignal;
     
    // End Functions **************************************************************
     
    #endif /* _CI_HARDWARE_API_H_ */
   </code>
   
   
   ==== 6.11 CI-srv/inc/ CI_hardware_types.h ====
   <code>
   /*
     * Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    /* Exclusionary ifdef */
    #ifndef _CI_HARDWARE_TYPES_H_
    #define _CI_HARDWARE_TYPES_H_
     
    // Includes *******************************************************************
    #include <stdint.h>
     
    // End Includes ***************************************************************
     
    // Macros, typedefs, enums ****************************************************
     
    /***************************************************************************
     * IMPORTANT: The interface version below is used to detect CHANGES the to
     * functions in the interface and SHALL be updated any time there is a change
     * to ANY function in this header that is part of a registered (i.e. used with
     * the registrar) interface. "Change" in this case only means a change to the
     * SIGNATURE of a function. The interface version need not be updated if the
     * number of functions in the interface changes (i.e. a function is added or
     * removed).
     ***************************************************************************/
    #define  CI_HW_VER_MAJ  0x01
    #define  CI_HW_VER_MIN  0x02
    #define  CI_HW_VER      ((CI_HW_VER_MAJ << 16) | CI_HW_VER_MIN)
    #define  CI_HW_NAME     ("CI_hwIf")
     
    /* API Function Name List */
    #define  CI_HW_NAME_VERSION              ("Version")           /* 1st in list */
    #define  CI_HW_NAME_GET_AVAIL_COUNT      ("GetAvailCount")
    #define  CI_HW_NAME_CONFIG_TIMER_SIGNAL  ("ConfTimerSig")
     
    // ----------------------------------------------------------------------------
     
    /* ------------------------------------------------------------------------ */
    /* ------------------ Data/enum types for this interface ------------------ */
    /* ------------------------------------------------------------------------ */
     
    /* Hardware timer signal active state  */
    typedef enum {
      CI_signalActiveLow,
      CI_signalActiveHigh
    } CI_signalActiveState_t;
     
    /* ------------------------------------------------------------------------- */
    /* ------------------- Function types for this interface ------------------- */
    /* ------  See the corresponding API header for function declarations ------ */
    /* ------------------------------------------------------------------------- */
     
    typedef int32_t (CI_getAvailableTimerCount_t)(void);
    typedef CI_getAvailableTimerCount_t (*CI_getAvailableTimerCount_tp);
     
    typedef int32_t (CI_timerSetSignal_t)(uint32_t timer,
                                          uint32_t pulsePeriod,
                                          uint32_t pulseOffset,
                                          uint32_t pulseWidth,
                                          CI_signalActiveState_t activeLevel);
    typedef CI_timerSetSignal_t (*CI_timerSetSignal_tp);
     
    // ----------------------------------------------------------------------------
    // End Macros, typedefs, enums ************************************************
     
    // Global Variables (externs, globals, static globals) ************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Global Variables *******************************************************
     
    // Functions ******************************************************************
    // End Functions **************************************************************
     
    #endif /* _CI_HARDWARE_TYPES_H_ */
   
   </code>
   
   ==== 6.12 CI-srv/inc/ CI_io_api.h ====
   <code>
   /*
    * Copyright (c) 2019-2020 Analog Devices, Inc. All Rights Reserved.
    *
    * This software is proprietary and confidential to Analog Devices, Inc. and
    * its licensors.
    */
   
   /* Exclusionary ifdef */
   #ifndef _CI_IO_API_H_
   #define _CI_IO_API_H_
   
   // Includes *******************************************************************
   #include "CI_io_types.h"
   
   // End Includes ***************************************************************
   
   // Macros, typedefs, enums ****************************************************
   // ----------------------------------------------------------------------------
   // ----------------------------------------------------------------------------
   // End Macros, typedefs, enums ************************************************
   
   // Global Variables (externs, globals, static globals) ************************
   // ----------------------------------------------------------------------------
   // ----------------------------------------------------------------------------
   // End Global Variables *******************************************************
   
   // Functions ******************************************************************
   /**
    * Set the device for the system
    *
    * Use this function to set a "canned" device from the IO configuration file by
    * device ID number. Using this function will effectively override the network
    * application's working copy of the device structure with the data from the IO
    * configuration file. Once CI_ConfigComplete() is called, the working copy
    * will be latched and may not be modified from that point forward.
    *
    * Parameters
    * Dir    Type      Name        Description
    * [in]   uint16_t  deviceId    ID number (from IO config file) of the device
    *                              to set for the system
    * Return
    * Type: int32_t
    * Values: CI_OK       on success
    *         CI_ERROR    if device not found in IO config data
    *         CI_ERROR    if called after CI_ConfigComplete()
    */
   CI_setDevice_t CI_SetDevice;
   
   /**
    * Set a custom device, bypassing the config data
    *
    * Use this function to set a custom device programatically rather than using a
    * "canned" device from the IO configuration file (using CI_SetDevice()). Using
    * this function will effectively override the network application's working
    * copy of the device structure with the data in the indicated buffer. Once
    * CI_ConfigComplete() is called, the working copy will be latched and may not
    * be modified from that point forward.
    *
    * This function has the same functionality as CI_SetDevice() except that the
    * device data comes from the IO application rather than the IO configuration
    * data file.
    *
    * Parameters
    * Dir    Type      Name        Description
    * [in]   void *    device_p    Pointer to a filled-in CI device structure in
    *                              the format expected by the protocol in use
    * [in]   uint32_t  bufSize     Size (in bytes) of the structure pointed to by
    *                              data_p
    *
    * Refer to the file CI_device_structs.h for the data structure this function
    * expects. Each protocol has a distinct device structure:
    *    (e.g. EtherNet/IP -----> CI_etherNetIpDevice_t)
    *
    * It is up to the IO application to know what the underlying protocol is and
    * supply a correctly-formated, corresponding device structure. (The underlying
    * protocol is returned by CI_GetProtocol().)
    *
    * Return
    * Type: int32_t
    * Values: CI_OK              on success
    *         CI_INVALID_PARAM   on error processing device information
    *         CI_INVALID_PARAM   if device data buffer size not equal to expected
    *                            structure size
    *         CI_ERROR           if called after CI_ConfigComplete()
    *         CI_ERROR           on error
    */
   CI_setDeviceCustom_t CI_SetDeviceCustom;
   
   /**
    * Get a copy of the device structure working copy
    *
    * Use this function to have the network application copy the working copy of
    * the device structure into the indicated buffer. This will enable the IO
    * application to read device parameters or optionally, read, modify and then
    * write them back to the network application using CI_SetDeviceCustom().
    *
    * Parameters
    * Dir    Type      Name        Description
    * [out]  void *    device_p    Pointer to buffer to be filled in with working
    *                              copy of device structure
    * [in]   uint16_t  maxSize     Maximum number of bytes that can be copied to
    *                              caller's buffer when filling in device structure
    *
    * The working copy of the device structure must be initialized (using
    * CI_SetDeviceCustom() or CI_SetDevice()) prior to calling this function.
    * Otherwise, an an error will be returned.
    *
    * Return
    * Type: int32_t
    * Values: number of bytes copied to caller's buffer
    *         CI_INVALID_PARAM if device_p == NULL
    *         CI_INVALID_PARAM if maxSize < size of device structure (i.e. buffer
    *                          too small for device structure)
    *         CI_ERROR if working copy of device structure not initialized
    *         CI_ERROR on error
    */
   CI_getDevice_t CI_GetDevice;
   
   /**
    * Add an item to the system
    *
    * Parameters
    * Dir    Type      Name        Description
    * [in]   uint16_t  id          Item ID number (from IO config file)
    * [in]   uint32_t  location    1-based location (i.e. slot) into which the
    *                              item should be installed
    * Return
    * Type: int32_t
    * Values: >= 0:  item handle (positive integer used in other calls)
    *           <0:  CI_INVALID_PARAM  if location out of range (must be >0)
    *                CI_ERROR          if item not found by ID
    *                CI_ERROR          if items not currently permitted to be added
    */
   CI_addItem_t CI_AddItem;
   
   /**
    * Create and add a custom item, bypassing the config data
    *
    * This is not the traditional way to set add an item. Normally, you would
    * simply add an item using CI_AddItem().
    *
    * This function has the same functionality as CI_AddItem() except that the
    * item data comes from the IO application rather than the IO configuration
    * data file.
    *
    * Parameters
    * Dir    Type      Name        Description
    * [in]   uint16_t  id          Item ID number (as if it from IO config file)
    * [in]   void *    data_p      Pointer to a filled-in CI item structure in the
    *                              format expected by the protocol in use
    * [in]   uint32_t  bufSize     Size (in bytes) of the structure pointed to by
    *                              data_p
    * [in]   uint32_t  location    1-based location (i.e. slot) into which the
    *                              item should be installed
    *
    * Refer to the file CI_item_structs.h for the data structure this function
    * expects. Each protocol has a distinct item structure:
    *    (e.g. EtherNet/IP ---- CI_etherNetIpItem_t)
    *
    * It is up to the IO application to know what the underlying protocol is and
    * supply the correctly-formatted, corresponding item structure. (The
    * underlying protocol is returned by CI_GetProtocol().)
    *
    * Return
    * Type: int32_t
    * Values: >= 0:  item handle (positive integer used with other CI calls)
    *           <0:  CI_INVALID_PARAM  if item data pointer == NULL
    *                CI_INVALID_PARAM  if item data buffer size not equal to
    *                                  expected structure size
    *                CI_INVALID_PARAM  if location out of range (must be >0)
    *                CI_INVALID_PARAM  if error processing item data
    */
   CI_addItemCustom_t CI_AddItemCustom;
   
   /**
    * Set the value of an item parameter
    *
    * Parameters
    * Dir    Type              Name          Description
    * [in]   int32_t           handle        Handle to item for which parameter
    *                                        should be set (returned
    *                                        from CI_AddItem())
    * [in]   CI_itemParamId_t  param         Item parameter to set (see
    *                                        CI_itemParamId_t for examples and
    *                                        descriptions of item parameters)
    * [in]   void *            paramData_p   Pointer to buffer in which the
    *                                        desired item parameter data currently
    *                                        resides
    * [in]   uint32_t          paramSize     The number of bytes in the buffer
    *                                        pointed to by paramData_p
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_INVALID_PARAM if invalid item handle
    *         CI_NOT_SUPPORTED if invalid item parameter
    *         CI_INVALID_PARAM if parameter data pointer == NULL
    *         CI_INVALID_PARAM if invalid item parameter size
    *         CI_ERROR on error
    */
   CI_setItemParam_t CI_SetItemParam;
   
   /**
    * Get the value of an item parameter
    *
    * Parameters
    * Dir    Type              Name          Description
    * [in]   int32_t           handle        Handle to item for which parameter
    *                                        should be retrieved (returned from
    *                                        CI_AddItem())
    * [in]   CI_itemParamId_t  param         Item parameter to get
    *                                        (see CI_itemParamId_t for examples
    *                                        and descriptions of item parameters)
    * [in]   void *            paramData_p   Pointer to buffer into which the
    *                                        desired item parameter data should be
    *                                        placed
    * [in]   uint32_t          paramSize     Size (in bytes) of the requested item
    *                                        parameter data
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_INVALID_PARAM if invalid item handle
    *         CI_INVALID_PARAM if invalid item parameter
    *         CI_INVALID_PARAM if parameter data pointer == NULL
    *         CI_INVALID_PARAM if invalid paramSize value
    *         CI_ERROR on error
    */
   CI_getItemParam_t CI_GetItemParam;
   
   /**
    * Install direct IO functions
    *
    * Use this function to install direct input/output functions. These functions
    * will be called directly by the network application to precisely synchronize
    * the IO application's input and/or output data processing with each network
    * cycle.
    *
    * NOTE: These functions may be called from an interrupt context. Only take
    * actions in these functions that are appropriate inside an interrupt service
    * routine.
    *
    * Parameters
    * Dir    Type              Name          Description
    * [in]   CI_dirIoFunc_t    dirInFunc_p   Pointer to direct input data handler
    *                                        function
    * [in]   CI_dirIoFunc_t    dirOutFunc_p  Pointer to direct output data handler
    *                                        function
    *
    * NOTE: NULL may be passed in for either parameter to disable installation of
    *       a handler for the corresponding data direction.
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR if called after CI_ConfigComplete()
    *         CI_NOT_SUPPORTED if direct IO not supported by network application
    */
   CI_installDirectIo_t CI_InstallDirectIo;
   
   /**
    * Remove a previously-added item
    *
    * Parameters
    * Dir    Type      Name    Description
    * [in]   int32_t   handle  Handle of the item to be removed (returned by
    *                          CI_itemAddItem() or CI_AddItemCustom())
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on successful removal
    *         CI_INVALID_PARAM if handle is invalid
    *         CI_NOT_SUPPORTED if function not supported
    */
   CI_removeItem_t CI_RemoveItem;
   
   /**
    * Return a previously-removed item
    *
    * Parameters
    * Dir    Type      Name    Description
    * [in]   int32_t   handle  Handle of the item to be returned (returned by
    *                          CI_itemAddItem() or CI_AddItemCustom())
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on successful replacement
    *         CI_INVALID_PARAM if handle is invalid
    *         CI_NOT_SUPPORTED if function not supported
    */
   CI_returnItem_t CI_ReturnItem;
   
   /**
    * Write item data
    *
    * Parameters
    * Dir    Type      Name    Description
    * [in]   int32_t   handle  Handle of item for which data should be written
    *                          (returned by CI_AddItem() or CI_AddItemCustom())
    * [in]   void *    data_p  Pointer to buffer containing the data to be written
    *                          to the item
    *
    * Return
    * Type: int32_t
    * Values: CI_OK             on success
    *         CI_INVALID_PARAM  if invalid handle or data pointer is NULL
    *         CI_ERROR          if item is written before CI_ConfigComplete()
    *         CI_ERROR          on error
    */
   CI_writeItem_t CI_WriteItem;
   
   /**
    * Read item data
    *
    * Parameters
    * Dir    Type      Name    Description
    * [in]   int32_t   handle  Handle of item for which data should be read
    *                          (returned by CI_AddItem() or CI_AddItemCustom())
    * [out]  void *    data_p  Pointer to buffer into which item data should be
    *
    * Return
    * Type: int32_t
    * Values: >=0: IO Status     status of data from network (see CI_ioStatus_t)
    *         CI_INVALID_PARAM   if invalid handle or data pointer is NULL
    *         CI_ERROR           if item is read before CI_ConfigComplete()
    *         CI_ERROR           on error
    */
   CI_readItem_t CI_ReadItem;
   
   /**
    * Set the input or output path status of an item
    *
    * Use this function to indicate the status of the input and/or output path to
    * the network application. Depending on the industrial protocol implemented by
    * the network application, this information may be to the PLC as "IO module
    * health" information.
    *
    * Parameters
    * Dir    Type                      Name        Description
    * [in]   int32_t                   handle      Handle of item for which the
    *                                              status should be set
    * [in]   CI_itemDataDir_t          direction   Data direction (input or output)
    *                                              for which the status should be
    *                                              set
    * [in]   CI_itemDataPathStatus_t   status      Status of the indicated input
    *                                              or output path for the indicated
    *                                              item
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_INVALID_PARAM on invalid item handle
    *         CI_INVALID_PARAM on invalid data direction
    *         CI_INVALID_PARAM on invalid status
    *         CI_ERROR on error
    */
   CI_setItemStatus_t CI_SetItemStatus;
   
   /**
    * Get the period of cyclic I/O connection
    *
    * Parameters
    * NONE
    *
    * Return
    * Type: int32_t
    * Values: cyclic I/O period in microseconds
    *         CI_UNKNOWN if protocol in use doesn't have a cyclic period
    */
   CI_getCyclicPeriod_t CI_GetCyclicPeriod;
   
   /**
    * Tell the network application that an I/O cycle is complete
    *
    * Parameters
    * NONE
    *
    * Return
    * Type: int32_t
    * Values: CI_OK     on success
    *         CI_ERROR  if called prior to CI_ConfigComplete()
    */
   CI_ioComplete_t CI_IoComplete;
   
   // End Functions **************************************************************
   
   #endif /* _CI_IO_API_H_ */
   </code>
   
   ==== 6.13 CI-srv/inc/ CI_io_types.h ====
   <code>
   /*
     * Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    /* Exclusionary ifdef */
    #ifndef _CI_IO_TYPES_H_
    #define _CI_IO_TYPES_H_
     
    // Includes *******************************************************************
    #include <stdint.h>
     
    // End Includes ***************************************************************
     
    // Macros, typedefs, enums ****************************************************
     
    /***************************************************************************
     * IMPORTANT: The interface version below is used to detect CHANGES the to
     * functions in the interface and SHALL be updated any time there is a change
     * to ANY function in this header that is part of a registered (i.e. used with
     * the registrar) interface. "Change" in this case only means a change to the
     * SIGNATURE of a function. The interface version need not be updated if the
     * number of functions in the interface changes (i.e. a function is added or
     * removed).
     ***************************************************************************/
    #define  CI_IO_VER_MAJ  0x01
    #define  CI_IO_VER_MIN  0x00
    #define  CI_IO_VER     ((CI_IO_VER_MAJ << 16) | CI_IO_VER_MIN)
    #define  CI_IO_NAME    ("CI_ioIf")
     
    /* API Function Name List */
    #define  CI_IO_NAME_VERSION             ("Version") /* 1st in list, required */
    #define  CI_IO_NAME_SET_DEVICE          ("SetDevice")
    #define  CI_IO_NAME_SET_DEVICE_CUST     ("SetDeviceCust")
    #define  CI_IO_NAME_GET_DEVICE          ("GetDevice")
    #define  CI_IO_NAME_ADD_ITEM            ("AddItem")
    #define  CI_IO_NAME_ADD_ITEM_CUST       ("AddItemCust")
    #define  CI_IO_NAME_SET_ITEM_PARAM      ("SetItemParam")
    #define  CI_IO_NAME_GET_ITEM_PARAM      ("GetItemParam")
    #define  CI_IO_NAME_INSTALL_DIR_IO      ("InstDirIo")
    #define  CI_IO_NAME_REMOVE_ITEM         ("RemoveItem")
    #define  CI_IO_NAME_RETURN_ITEM         ("ReturnItem")
    #define  CI_IO_NAME_WRITE_ITEM          ("WriteItem")
    #define  CI_IO_NAME_READ_ITEM           ("ReadItem")
    #define  CI_IO_NAME_SET_ITEM_STATUS     ("SetItemStatus")
    #define  CI_IO_NAME_GET_CYCLIC_PERIOD   ("GetCyclicPeriod")
    #define  CI_IO_NAME_IO_COMPLETE         ("IoComplete")
     
    // ----------------------------------------------------------------------------
     
    /* ------------------------------------------------------------------------ */
    /* ------------------ Data/enum types for this interface ------------------ */
    /* ------------------------------------------------------------------------ */
     
    /*
     * Item parameters (as used by CI_SetItemParam() and CI_GetItemParam())
     * and their data types/structures are documented below
     */
    typedef enum {
      CI_itemParamInputSize,
      /* Desc: Total size of input data for the indicated item
       * Type: uint16_t */
     
      CI_itemParamOutputSize,
      /* Desc: Total size of output data for the indicated item
       * Type: uint16_t */
     
      CI_itemParamCyclicness,
      /* Desc: Indicates whether the data for the indicated item is transferred on
       *       the network each cycle (cyclic) or not (acyclic).
       * Type: CI_itemCyclicness_t */
     
      /* place more item parameter ID codes here... */
     
      CI_itemParamLast = 0xFFFF           /* To force enumeration width */
    } CI_itemParamId_t;
     
    /* Item data direction */
    typedef enum {
      CI_itemDataDirInput,
      CI_itemDataDirOutput,
     
      CI_itemDataDirLast = 0xFFFF         /* To force enumeration width */
    } CI_itemDataDir_t;
     
    /* Item data path status */
    typedef enum {
      CI_itemDataPathBad,
      CI_itemDataPathOk,
     
      CI_itemDataPathLast = 0xFFFF        /* To force enumeration width */
    } CI_itemDataPathStatus_t;
     
    /* Item cyclicness (i.e. whether or not item data is transferred every
     * network cycle or not) */
    typedef enum {
      CI_itemCyclicnessAcyclic,
      CI_itemCyclicnessCyclic,
     
      CI_itemCyclicnessLast = 0xFFFF      /* To force enumeration width */
    } CI_itemCyclicness_t;
     
    /* IO status type (as returned by CI_ReadItem()) */
    typedef enum {
                              /* Data valid?  New?  Copied to caller's buffer? */
      CI_ioStatusInvalid,     /* No           N/A   No                         */
      CI_ioStatusValid,       /* Yes          Yes   Yes                        */
      CI_ioStatusValidNotNew, /* Yes          No    Yes                        */
     
      CI_ioStatusLast = 0xFFFFFFFF        /* To force enumeration width */
    } CI_ioStatus_t;
     
    /* Direct input/output data handler function prototype */
    typedef void (CI_dirIoFunc_t)();
     
    /* ------------------------------------------------------------------------- */
    /* ------------------- Function types for this interface ------------------- */
    /* ------  See the corresponding API header for function declarations ------ */
    /* ------------------------------------------------------------------------- */
     
    typedef int32_t (CI_setDevice_t)(uint16_t deviceId);
    typedef CI_setDevice_t (*CI_setDevice_tp);
     
    typedef int32_t (CI_setDeviceCustom_t)(void* device_p, uint32_t bufSize);
    typedef CI_setDeviceCustom_t (*CI_setDeviceCustom_tp);
     
    typedef int32_t (CI_getDevice_t)(void *device_p, uint16_t maxSize);
    typedef CI_getDevice_t (*CI_getDevice_tp);
     
    typedef int32_t (CI_addItem_t)(uint16_t id, uint32_t location);
    typedef CI_addItem_t (*CI_addItem_tp);
     
    typedef int32_t (CI_addItemCustom_t)(uint16_t id,
                                         void *data_p,
                                         uint32_t bufSize,
                                         uint32_t location);
    typedef CI_addItemCustom_t (*CI_addItemCustom_tp);
     
    typedef int32_t (CI_setItemParam_t)(int32_t handle,
                                        CI_itemParamId_t param,
                                        void *paramData_p,
                                        uint32_t paramSize);
    typedef CI_setItemParam_t (*CI_setItemParam_tp);
     
    typedef int32_t (CI_getItemParam_t)(int32_t handle,
                                        CI_itemParamId_t param,
                                        void *paramData_p,
                                        uint32_t paramSize);
    typedef CI_getItemParam_t (*CI_getItemParam_tp);
     
    typedef int32_t (CI_installDirectIo_t)(CI_dirIoFunc_t *dirInFunc_p,
                                           CI_dirIoFunc_t *dirOutFunc_p);
    typedef CI_installDirectIo_t (*CI_installDirectIo_tp);
     
    typedef int32_t (CI_removeItem_t)(int32_t handle);
    typedef CI_removeItem_t (*CI_removeItem_tp);
     
    typedef int32_t (CI_returnItem_t)(int32_t handle);
    typedef CI_returnItem_t (*CI_returnItem_tp);
     
    typedef int32_t (CI_writeItem_t)(int32_t handle, void *data_p);
    typedef CI_writeItem_t (*CI_writeItem_tp);
     
    typedef int32_t (CI_readItem_t)(int32_t handle, void *data_p);
    typedef CI_readItem_t (*CI_readItem_tp);
     
    typedef int32_t (CI_setItemStatus_t)(int32_t handle,
                                         CI_itemDataDir_t direction,
                                         CI_itemDataPathStatus_t status);
    typedef CI_setItemStatus_t (*CI_setItemStatus_tp);
     
    typedef int32_t (CI_getCyclicPeriod_t)(void);
    typedef CI_getCyclicPeriod_t (*CI_getCyclicPeriod_tp);
     
    typedef int32_t (CI_ioComplete_t)(void);
    typedef CI_ioComplete_t (*CI_ioComplete_tp);
     
    // ----------------------------------------------------------------------------
    // End Macros, typedefs, enums ************************************************
     
    // Global Variables (externs, globals, static globals) ************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Global Variables *******************************************************
     
    // Functions ******************************************************************
    // End Functions **************************************************************
     
    #endif /* _CI_IO_TYPES_H_ */
   
   </code>
   ==== 6.14 CI-srv/inc/ CI_items.h ====
   <code>
   /*
     * Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    /* Exclusionary ifdef */
    #ifndef _CI_ITEMS_H_
    #define _CI_ITEMS_H_
     
    /*****************************************************************************
     *
     * This file contains structures to be used with the CI_AddItemCustom()
     * function
     *
     ****************************************************************************/
     
    // Includes *******************************************************************
    #include <stdint.h>
     
    // End Includes ***************************************************************
     
    // Macros, typedefs, enums ****************************************************
    // ----------------------------------------------------------------------------
     
    /* PROFINET item section =================================================== */
    typedef enum {
      CI_pnetItemTypeCyclic,
      CI_pnetItemTypeAcyclic
    } CI_profinetItemType_t;
     
    #define CI_PNET_ITEM_VERSION       0
    typedef struct {
      uint8_t type;             // See CI_profinetItemType_t
      uint8_t pad1;
      uint8_t pad2;
      uint8_t pad3;
      uint32_t moduleID;
      uint32_t subModuleID;
      uint16_t outputBytes;
      uint16_t inputBytes;
    } CI_profinetItemCyclic_t;
     
    typedef struct {
      uint8_t type;             // See CI_profinetItemType_t
      uint8_t pad;
      uint16_t index;
      uint16_t inputBytes;
      uint16_t outputBytes;
    } CI_profinetItemAcyclic_t;
     
    /* ========================================================================= */
     
    /* EtherNet/IP item section ================================================ */
    #define CI_EIP_ITEM_VERSION       0
    typedef struct {
      uint8_t type;                   /* accumulating    = 0
                                       * incrementing    = 1
                                       * unique          = 2
                                       * configuration   = 3
                                       * diagnostic      = 4 */
      uint8_t pad;                    /* Always 0 */
      uint16_t consumeInstanceID;     /* Always 0 for diagnostic type */
      uint16_t consumeSize;           /* Consume size in bytes, always 0 for
                                       * diagnostic type */
      uint16_t produceInstanceID;     /* Always 0 for config type */
      uint16_t produceSize;           /* Produce size in bytes, always 0 for
                                       * configuration type */
    } CI_etherNetIpItem_t;
     
    /* ========================================================================= */
     
    /* EtherCAT item section ================================================ */
    #define OBJECT_NAME_STR_LEN       16    // Arbitrary
    #define SUBINDEX_NAME_STR_LEN     16    // Arbitrary
     
    /* NOTE: The maximum number of data subindices dictates the length of the RxPDO
     * and TxPDO objects (and many others). This affects the corresponding data
     * type in the ESI file. If the maximum number of data subindices is changed,
     * the "Descriptions:Devices:Device:Profile:Dictionary:DataTypes:DataType"
     * for all application structs typed out (i.e. described) in the ESI file will
     * need to be updated. This definition could exist in multiple device
     * dictionaries. Every dictionary will need to be updated.
     */
    #define MAX_DATA_SUBINDICES       16
     
    /* EtherCAT item type (see type field in CI_ethercatItem_t) */
    typedef enum {
      itemType_Data = 0,
      itemType_Configuration,
      itemType_Diagnostic
    } CI_ethercatItemType_t;
     
    /* EtherCAT object subindex */
    typedef struct {
      uint16_t dataType;           // Data type of this subindex (see EcatDataType_t)
      uint16_t arrLen;             // Array length (only if array data type)
      char name[SUBINDEX_NAME_STR_LEN];  // Name of this subindex
    } CI_ethercatSubindexDesc_t;
     
    #define CI_ECAT_ITEM_VERSION       1
    typedef struct {
      uint8_t type;                   // Item type (see CI_ethercatItemType_t)
      uint8_t pad;                    // Pad 0
      char inputObjName[OBJECT_NAME_STR_LEN];         // Name of the input object
      char outputObjName[OBJECT_NAME_STR_LEN];        // Name of the output object
      CI_ethercatSubindexDesc_t inputSubindices[MAX_DATA_SUBINDICES];  // Data entries for each input subindex
      CI_ethercatSubindexDesc_t outputSubindices[MAX_DATA_SUBINDICES]; // Data entries for each output subindex
    } CI_ethercatItem_t;
     
    /* ========================================================================= */
     
    // ----------------------------------------------------------------------------
    // End Macros, typedefs, enums ************************************************
     
    // Global Variables (externs, globals, static globals) ************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Global Variables *******************************************************
     
    // Functions ******************************************************************
    // End Functions **************************************************************
     
    #endif /* _CI_ITEMS_H_ */
   
   </code>
   ==== 6.15 CI-srv/inc/ CI_socket_api.h ====
   <code>
   /*
    * Copyright (c) 2019-2020 Analog Devices, Inc. All Rights Reserved.
    *
    * This software is proprietary and confidential to Analog Devices, Inc. and
    * its licensors.
    */
   
   /* Exclusionary ifdef */
   #ifndef _CI_SOCKET_API_H_
   #define _CI_SOCKET_API_H_
   
   // Includes *******************************************************************
   #include "CI_socket_types.h"
   
   // End Includes ***************************************************************
   
   // Macros, typedefs, enums ****************************************************
   // ----------------------------------------------------------------------------
   // ----------------------------------------------------------------------------
   // End Macros, typedefs, enums ************************************************
   
   // Global Variables (externs, globals, static globals) ************************
   // ----------------------------------------------------------------------------
   // ----------------------------------------------------------------------------
   // End Global Variables *******************************************************
   
   // Functions ******************************************************************
   /**
    * Set a socket to non-blocking IO
    *
    * Use CI_FIONBIO command to set socket to non-blocking mode. Other commands
    * CI_FIONREAD and CI_FIONWRITE not supported return error.
    *
    * Parameters
    * Dir    Type        Name        Description
    * [in]   int32_t     socket      Socket handle returned from the socket call
    * [in]   int32_t     cmd         Command (CI_SOCK_FIONBIO, CI_SOCK_FIONREAD, or
    *                                CI_SOCK_FIONWRITE)
    * [in]   uint32_t *  arg_p       Pointer to socket option data
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_IoctlSocketProto_t CI_IoctlSocket;
   
   /**
    * For SOCK_STREAM type sockets, respond to incomming connection requests
    *
    * Use one of the connection slots established by "listen" to create a new
    * socket and begin communications.
    *
    * Parameters
    * Dir    Type                Name        Description
    * [in]   int32_t             socket      The socket handle returned from the
    *                                        socket call
    * [in]   struct sockaddr *   addr_p      Pointer to an address structure
    * [in]   socklen_t *         addrlen_p   Pointer to the size of the address
    *                                        structure
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_acceptProto_t CI_Accept;
   
   /**
    * Bind an address (i.e. an interface) to a socket
    *
    * Parameters
    * Dir    Type                      Name      Description
    * [in]   int32_t                   socket    The socket handle returned from
    *                                            the socket call
    * [in]   const struct sockaddr *   addr_p    Pointer to an address structure
    * [in]   socklen_t                 addrlen   Size of the address structure
    *
    *
    * This function assigns the address specified by addr_p to the socket. This
    * address references one of our interfaces.
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_bindProto_t CI_Bind;
   
   /**
    * Terminate communications and close a socket
    *
    * Parameters
    * Dir    Type        Name      Description
    * [in]   int32_t     socket    The socket handle returned from the socket call
    * [in]   int32_t *   err_p     Pointer to an integer used to return the
    *                              stack's error code
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_closeSocketProto_t CI_CloseSocket;
   
   /**
    * Connect the socket to the address
    *
    * Parameters
    * Dir    Type                Name        Description
    * [in]   int32_t             socket      The socket handle returned from the
    *                                        socket call
    * [in]   struct sockaddr *   addr_p      Pointer to an address structure
    * [in]   socklen_t           addrlen     The size of the address structure
    *
    * For SOCK_STREAM sockets this function will attempt to establish a connection
    * to the specified address
    *
    * Return
    * Type: int32_t
    * Values: CI_OK                On success
    *         CI_ERROR             On failure
    *         CI_SOCK_SOCKET_EISCONN    Socket connection already established
    *         CI_SOCK_SOCKET_EALREADY   Connect already called by socket not connected
    *                               yet (non-blocking mode only)
    */
   CI_connectProto_t CI_Connect;
   
   /**
    * Release the memory used by the addrinfo linked list
    *
    * Parameters
    * Dir    Type                Name        Description
    * [in]   struct addrinfo *   res_p       Pointer to a linked list of addrinfo
    *                                        structs
    * Return nothing
    */
   CI_freeAddrInfoProto_t CI_FreeAddrInfo;
   
   /**
    * Return the address of the specified host and/or service
    *
    * Parameters
    * Dir    Type                      Name        Description
    * [in]   const char *              node_p      Host name or dotted string
    *                                              address
    * [in]   const char *              service_p   Service or port name
    * [in]   const struct addrinfo *   hints_p     Pointer to addrinfo struct
    * [out]  struct addrinfo **        res_p       Pointer to a linked list of
    *                                              addrinfo structs
    *
    * This function directly returns a translated version of whatever the IP stack
    * returns. This is either zero for success or a non-zero error code.
    *
    * To avoid memory leaks, call CI_FreeAddrInfo to release the memory used by
    * res_p.
    *
    * Return
    * Type: int32_t
    * Values:  0 on success
    *         <0 on failure
    *            (see http://man7.org/linux/man-pages/man3/getaddrinfo.3.html)
    */
   CI_getAddrInfoProto_t CI_GetAddrInfo;
   
   /**
    * Return the last socket error code
    *
    * Parameters
    * Dir    Type        Name      Description
    * [in]   int32_t     socket    The socket handle returned from the socket call
    * [out]  int32_t *   err_p     Pointer to an integer to receive the last error
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_getLastSocketErrorProto_t CI_GetLastSocketError;
   
   /**
    * Convert a socket address to a corresponding host and service
    *
    * Parameters
    * Dir    Type                      Name        Description
    * [in]   const struct sockaddr *   addr_p      Pointer to a socket address to
    *                                              be translated
    * [in]   socklen_t                 addrlen     Size of the socket address
    * [out]  char *                    host_p      Pointer to a buffer the
    *                                              function will use to return the
    *                                              host name
    * [in]   int32_t                   hostlen     Length of the buffer
    * [out]  char *                    serv_p      Pointer to a buffer the
    *                                              function will use to return the
    *                                              service name
    * [in]   int32_t                   servlen     Length of the buffer
    * [in]   int32_t                   flags       Flags used to alter the
    *                                              behavior of GetNameInfo
    *
    * This function directly returns a translated version of whatever the IP stack
    * returns. This is either zero for success or a non-zero error code.
    *
    * Return
    * Type: int32_t
    * Values:  0 on success
    *         <0 on failure
    *            (see http://man7.org/linux/man-pages/man3/getnameinfo.3.html
    */
   CI_getNameInfoProto_t CI_GetNameInfo;
   
   /**
    * Returns the address of the peer connected to the socket
    *
    * Parameters
    * Dir    Type                Name        Description
    * [in]   int32_t             socket      The socket handle returned from the
    *                                        socket call
    * [in]   struct sockaddr *   addr_p      Pointer to an address structure
    * [in]   socklen_t *         addrlen_p   The size of the address structure
    *
    * See http://man7.org/linux/man-pages/man2/getpeername.2.html
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_getPeerNameProto_t CI_GetPeerName;
   
   /**
    * Return the address to which the socket is bound
    *
    * Parameters
    * Dir    Type                Name        Description
    * [in]   int32_t             socket      The socket handle returned from the
    *                                        socket call
    * [out]  struct sockaddr *   addr_p      Pointer to an address structure
    * [out]  socklen_t *         addrlen_p   Pointer to the size of the address
    *                                        structure
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_getSockNameProto_t CI_GetSockName;
   
   /**
    * Return the specified option state/data from a specified socket
    *
    * Parameters
    * Dir    Type          Name        Description
    * [in]   int32_t       socket      The socket handle returned from the socket
    *                                  call
    * [in]   int32_t       level       The protocol level at which the option
    *                                  resides
    * [in]   int32_t       optname     The single option to set/get
    * [out]  void *        optval_p    Pointer to buffer to receive the data
    *                                  specific to this option
    * [out]  socklen_t *   optlen      Pointer to the option data length
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_getSockOptProto_t CI_GetSockOpt;
   
   /**
    * Begin waiting for a connection
    *
    * Set the socket up to be used to allow incoming connection requests using
    * accept
    *
    * Parameters
    * Dir    Type      Name        Description
    * [in]   int32_t   socket      The socket handle returned from the socket call
    * [in]   int32_t   backlog     the max number of allowed connections
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_listenProto_t CI_Listen;
   
   /**
    * Receive a message from another socket
    *
    * Once the socket is in the connected state recv is used to communicate with
    * the remote connection.
    *
    * Parameters
    * Dir    Type          Name        Description
    * [in]   int32_t       socket      The socket handle returned from the socket
    *                                  call
    * [out]  const void *  buf_p       Pointer to a buffer to receive the data
    * [in]   int32_t       length      The length (in bytes) of the buffer
    * [in]   int32_t       flags       Not supported, use 0
    *
    * Return
    * Type: int32_t
    * Values: On success, the number of bytes received
    *         CI_ERROR on failure
    */
   CI_recvProto_t CI_Recv;
   
   /**
    * Receive a message from another socket
    *
    * When a message is recieved from a remote peer the data is placed into the
    * provided buffer and the peer's address is placed into the supplied address
    * structure.
    *
    * Parameters
    * Dir    Type                Name        Description
    * [in]   int32_t             socket      the socket handle returned from the
    *                                        socket call
    * [out]  const void *        buf_p       pointer to a buffer to receive the
    *                                        data
    * [in]   int32_t             length      The length (in bytes) of the buffer
    * [in]   int32_t             flags       Not supported, use 0
    * [in]   struct sockaddr *   addr_p      Pointer to an address structure
    * [in]   socklen_t *         addrlen_p   Pointer to the size of the address
    *                                        structure
    *
    * Return
    * Type: int32_t
    * Values: On success, the number of bytes received
    *         CI_ERROR on failure
    */
   CI_recvFromProto_t CI_RecvFrom;
   
   /**
    * Wait for a file descriptor
    *
    * When a socket operation is ready the file descriptor will indicate this
    *
    * Parameters
    * Dir    Type      Name              Description
    * [in]   int32_t   nfds              Number of file descriptors to wait on
    * [in]   fd_set *  readset_p         The set of read descriptors
    * [in]   fd_set *  writeset_p        The set of write descriptors
    * [in]   fd_set *  exceptset_p       The set of exception descriptors
    * [in]   int32_t   timeoutMicroSec   the max time (in uSec) to wait before
    *                                    returning, use -1 to wait forever
    *
    * Return
    * Type: int32_t
    * Values: On success, the number of set bits in the file descriptors
    *         CI_ERROR on failure
    */
   CI_selectProto_t CI_Select;
   
   /**
    * File descriptor "macro" functions to accompany select
    *
    * Since the file descriptors and FD set data structures are particular to each
    * TCP/IP stack implementation, we need to add porting layer functions to
    * provide access to these.
    *
    * CI_GetFdSet() --------------------------------------------------------------
    * Parameters
    * None
    *
    * Return
    * Nothing
    *
    * CI_ReturnFdSet() -----------------------------------------------------------
    * Parameters
    * Dir    Type      Name        Description
    *        void *    set_p       Pointer to a set of descriptors
    *
    * Return
    * Nothing
    *
    * CI_FdClr() -----------------------------------------------------------------
    * Parameters
    * Dir    Type      Name        Description
    *        int32_t   fd          A particular file descriptor (socket handle)
    *        void *    set_p       Pointer to a set of descriptors
    *
    * Return
    * Nothing
    *
    * CI_FdIsSet() ---------------------------------------------------------------
    * Parameters
    * Dir    Type      Name        Description
    *        int32_t   fd          A particular file descriptor (socket handle)
    *        void *    set_p       Pointer to a set of descriptors
    *
    * Return
    * Type: int32_t
    * Values: 0 if specified fd is not a part of the set
    *         1 if specified fd is a part of the set
    *
    * CI_FdSet() -----------------------------------------------------------------
    * Parameters
    * Dir    Type      Name        Description
    *        int32_t   fd          A particular file descriptor (socket handle)
    *        void *    set_p       Pointer to a set of descriptors
    *
    * Return
    * Nothing
    *
    * CI_FdZero() ----------------------------------------------------------------
    * Parameters
    * Dir    Type      Name        Description
    *        void *    set_p       Pointer to a set of descriptors
    *
    * Return
    * Nothing
    *
    * The IP stack definitions of things like file descriptors and the associated
    * macros are very specific to that IP stack. The following group of functions
    * provide that interface here.
    */
   CI_getFdSetProto_t CI_GetFdSet;
   CI_returnFdSetProto_t CI_ReturnFdSet;
   CI_fdClrProto_t CI_FdClr;
   CI_fdIsSetProto_t CI_FdIsSet;
   CI_fdSetProto_t CI_FdSet;
   CI_fdZeroProto_t CI_FdZero;
   
   /**
    * Transmit a message to another socket
    *
    * Once the socket is in the connected state send is used to communicate with
    * the remote connection
    *
    * Parameters
    * Dir    Type          Name        Description
    * [in]   int32_t       socket      The socket handle returned from the socket
    *                                  call
    * [out]  const void *  buf_p       Pointer to the payload data to send
    * [in]   int32_t       length      Length (in bytes) of the payload data
    * [in]   int32_t       flags       Not supported, use 0
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_sendProto_t CI_Send;
   
   /**
    * Transmit a message to another socket
    *
    * Send a message to the remote peer at the specified address
    *
    * Parameters
    * Dir    Type                Name        Description
    * [in]   int32_t             socket      The socket handle returned from the
    *                                        socket call
    * [in]   const void *        buf_p       Pointer to the payload data to send
    * [in]   int32_t             length      The length (in bytes) of the payload
    *                                        data
    * [in]   int32_t             flags       Not supported, use 0 here
    * [in]   struct sockaddr *   addr_p      Pointer to an address structure
    * [in]   socklen_t           addrlen     The size of the address structure
    *
    * Return
    * Type: int32_t
    * Values: On success, the number of bytes sent
    *         CI_ERROR on failure
    */
   CI_sendToProto_t CI_SendTo;
   
   /**
    * Invoke a specified option on a specified socket
    *
    * Parameters
    * Dir    Type          Name        Description
    * [in]   int32_t       socket      The socket handle returned from the socket
    *                                  call
    * [in]   int32_t       level       The protocol level at which the option
    *                                  resides
    * [in]   int32_t       optname     The single option to set/get
    * [in]   const void *  optval_p    The data specific to this option
    * [in]   socklen_t     optlen      The data length
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_setSockOptProto_t CI_SetSockOpt;
   
   /**
    * Create an endpoint for communication
    *
    * Create and initialize a socket within the TCP/IP stack
    *
    * Parameters
    * Dir    Type        Name        Description
    * [in]   int32_t     domain      Communications domain, use AF_INET or
    *                                AF_PACKET
    * [in]   int32_t     type        Socket type, use one of SOCK_STREAM,
                                                             SOCK_DGRAM or
                                                             SOCK_RAW
    * [in]   int32_t     protocol    Socket protocol, use one of IPPROTO_IP or
                                                                 IPPROTO_UDP or
                                                                 0
    * [out]  int32_t *   err_p       Pointer to an integer used to return the
    *                                stack's error code
    *
    * Return
    * Type: int32_t
    * Values: On success, a socket handle is returned (this could be zero)
    *         On error, CI_ERROR
    */
   CI_socketProto_t CI_Socket;
   
   /**
    * Shut down a socket in the direction(s) indicated
    *
    * Parameters
    * Dir    Type        Name        Description
    * [in]   int32_t     fd          Socket descriptor
    * [in]   int32_t     direction   Direction to shut down, use CI_SHUT_RD or
    *                                                            CI_SHUT_WR or
    *                                                            CI_SHUT_RDWR)
    * [out]  int32_t *   err_p       Pointer to location in which to place any
    *                                error codes
    *
    * Return
    * Type: int32_t
    * Values: IPM_OK on success
    *         IPM_ERROR on failure
    */
   CI_shutdown_t CI_Shutdown;
   
   /**
    * Convert from ASCII internet address to network ordered address
    *
    * Converts a ASCII internet address (e.g. "192.168.1.1") to a network ordered
    * address of an integer type
    *
    * Parameters
    * Dir    Type          Name        Description
    * [in]   const char *  c_p         Pointer to ASCII string to be converted
    *
    * Return
    * Type: uint32_t
    * Values: On success, a network ordered IP address (uint32_t)
    *         On error, 0
    */
   CI_inetAddr_t CI_InetAddr;
   
   /**
    * Network ordered address to ASCII internet address
    *
    * Converts a network ordered unsigned integer address to a ASCII internet
    * address (e.g. "192.168.1.1")
    *
    * Parameters
    * Dir    Type            Name        Description
    * [in]   struct in_addr  in          Network ordered address
    *
    * Return
    * Type: char *
    * Values: pointer to ASCII internet address string
    */
   CI_inetNtoA_t CI_InetNtoA;
   
   // End Functions **************************************************************
   
   #endif /* _CI_SOCKET_API_H_ */
   
   </code>
   ==== 6.16 CI-srv/inc/ CI_socket_defines.h ====
   <code>
   /*
     * Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    /* Exclusionary ifdef */
    #ifndef _CI_SOCKET_DEFINES_H_
    #define _CI_SOCKET_DEFINES_H_
     
    #pragma pack(push, 1)
     
    // Includes *******************************************************************
    #ifdef WIN32
      #include <winsock2.h>
    #endif
     
    #include "CI_codes.h"
    // End Includes ***************************************************************
     
    // Macros, typedefs, enums ****************************************************
     
    #define CI_FDSET_SIZE             (CI_MAX_SOCKETS + 1)
    #define CI_FDSET_FD_NBITS         32
     
    /*
     * Define the following macro if this library is to be executed on a
     * little-endian processor. Comment it out if it is to be run on a big-endian
     * processor.
     */
    #define CI_LITTLE_ENDIAN
     
     
    #ifdef CI_LITTLE_ENDIAN
      /* Little endian swapping macros */
      #define CI_NTOHS(x)    (uint16_t)( \
          (((uint16_t)x << 8)  & 0xFF00) | \
          (((uint16_t)x >> 8)  & 0x00FF))
      #define CI_NTOHL(x)    (uint32_t)( \
          (((uint32_t)x << 24) & 0xFF000000) | \
          (((uint32_t)x << 8)  & 0x00FF0000) | \
          (((uint32_t)x >> 8)  & 0x0000FF00) | \
          (((uint32_t)x >> 24) & 0x000000FF))
      #define CI_NTOHLL(x)   (uint64_t)( \
          (((uint64_t)x << 56) & 0xFF00000000000000ULL) | \
          (((uint64_t)x << 40) & 0x00FF000000000000ULL) | \
          (((uint64_t)x << 24) & 0x0000FF0000000000ULL) | \
          (((uint64_t)x << 8)  & 0x000000FF00000000ULL) | \
          (((uint64_t)x >> 8)  & 0x00000000FF000000ULL) | \
          (((uint64_t)x >> 24) & 0x0000000000FF0000ULL) | \
          (((uint64_t)x >> 40) & 0x000000000000FF00ULL) | \
          (((uint64_t)x >> 56) & 0x00000000000000FFULL))
      #define CI_HTONS       CI_NTOHS
      #define CI_HTONL       CI_NTOHL
      #define CI_HTONLL      CI_NTOHLL
    #else
      /* Big endian swapping macros */
      #define CI_NTOHS(x)    (uint16_t)(x)
      #define CI_NTOHL(x)    (uint32_t)(x)
      #define CI_NTOHLL(x)   (uint64_t)(x)
      #define CI_HTONS       CI_NTOHS
      #define CI_HTONL       CI_NTOHL
      #define CI_HTONLL      CI_NTOHLL
    #endif
     
    // Common socket success/error codes:
    #define CI_SOCK_UNKNOWN_OPTION               (int32_t) -100
    #define CI_SOCK_SOCKET_EISCONN               (int32_t) -101
    #define CI_SOCK_SOCKET_EALREADY              (int32_t) -102
    #define CI_SOCK_DIGEST_AUTH_NONCE_EXPIRE_ERR (int32_t) -103
    #define CI_SOCK_DIGEST_AUTH_NONCE_STALE_ERR  (int32_t) -104
     
    /* socket shutdown codes */
    #define CI_SHUT_RD                   0
    #define CI_SHUT_WR                   1
    #define CI_SHUT_RDWR                 2
     
    /* Translated network/socket error codes: */
    #define CI_EPERM                     1
    #define CI_ENOENT                    2
    #define CI_ESRCH                     3
    #define CI_EINTR                     4
    #define CI_EIO                       5
    #define CI_ENXIO                     6
    #define CI_E2BIG                     7
    #define CI_ENOEXEC                   8
    #define CI_EBADF                     9
    #define CI_ECHILD                    10
    #define CI_EAGAIN                    11
    #define CI_ENOMEM                    12
    #define CI_EACCES                    13
    #define CI_EFAULT                    14
    #define CI_ENOTBLK                   15
    #define CI_EBUSY                     16
    #define CI_EEXIST                    17
    #define CI_EXDEV                     18
    #define CI_ENODEV                    19
    #define CI_ENOTDIR                   20
    #define CI_EISDIR                    21
    #define CI_EINVAL                    22
    #define CI_ENFILE                    23
    #define CI_EMFILE                    24
    #define CI_ENOTTY                    25
    #define CI_ETXTBSY                   26
    #define CI_EFBIG                     27
    #define CI_ENOSPC                    28
    #define CI_ESPIPE                    29
    #define CI_EMLINK                    30
    #define CI_EPIPE                     31
    #define CI_EDOM                      32
    #define CI_ERANGE                    33
    #define CI_ENOMSG                    34
    #define CI_EIDRM                     35
    #define CI_EDEADLOCK                 36
    #define CI_EWOULDBLOCK               37
    #define CI_EINPROGRESS               38
    #define CI_EALREADY                  39
    #define CI_ENOTSOCK                  40
    #define CI_EDESTADDRREQ              41
    #define CI_EMSGSIZE                  42
    #define CI_EPROTOTYPE                43
    #define CI_ENOPROTOOPT               44
    #define CI_EPROTONOSUPPORT           45
    #define CI_ESOCKTNOSUPPORT           46
    #define CI_EOPNOTSUPP                47
    #define CI_EAFNOSUPPORT              48
    #define CI_EADDRINUSE                49
    #define CI_EADDRNOTAVAIL             50
    #define CI_ENETDOWN                  51
    #define CI_ENETUNREACH               52
    #define CI_ENETRESET                 53
    #define CI_ECONNABORTED              54
    #define CI_ECONNRESET                55
    #define CI_ENOBUFS                   56
    #define CI_EISCONN                   57
    #define CI_ENOTCONN                  58
    #define CI_ESHUTDOWN                 59
    #define CI_ETIMEDOUT                 60
    #define CI_ECONNREFUSED              61
    #define CI_EPFNOSUPPORT              62
    #define CI_EHOSTDOWN                 63
    #define CI_EHOSTUNREACH              64
    #define CI_ENOURGENTDATA             65
    #define CI_ENOOOBDATA                66
    #define CI_ETOOMANYREFS              67
    #define CI_EUNATCH                   68
    #define CI_ELNRNG                    69
    #define CI_ENETUNKNOWN               70
     
    /* Locally defined Socket option levels and Socket protocol codes: */
    #define CI_SOL_SOCKET                1
    #define CI_IPPROTO_IP                2
    #define CI_IPPROTO_IPV6              3
    #define CI_IPPROTO_TCP               4
    #define CI_IPPROTO_UDP               5
     
    /* Locally defined Socket option names: */
    #define CI_SO_DEBUG                  1
    #define CI_SO_ACCEPTCONN             2
    #define CI_SO_REUSEADDR              3
    #define CI_SO_KEEPALIVE              4
    #define CI_SO_DONTROUTE              5
    #define CI_SO_LINGER                 6
    #define CI_SO_THROUGHPUT             7
    #define CI_SO_EXPEDITE               8
    #define CI_SO_BROADCAST              9
    #define CI_SO_REUSEPORT              10
    #define CI_SO_NOCHKSUM               11
    #define CI_SO_NO_WAKEUP              12
    #define CI_SO_NO_WAKEUP_INHERIT      13
    #define CI_SO_ERROR                  14
    #define CI_SO_MAXMSG                 15
    #define CI_SO_MYADDR                 16
    #define CI_SO_NONBLOCK               17
    #define CI_SO_OOBINLINE              18
    #define CI_SO_RCVBUF                 19
    #define CI_SO_RXDATA                 20
    #define CI_SO_SNDBUF                 21
    #define CI_SO_TYPE                   22
    #define CI_SO_BIO                    23
    #define CI_SO_NBIO                   24
    #define CI_SO_MSG_PRIORITY           25
    #define CI_SO_VLAN_MSG_PRIORITY      26
    #define CI_SO_BINDTODEVICE           27
    #define CI_IP_O_TOS                  28
    #define CI_IP_O_FRAG                 29
    #define CI_IP_O_SECURE               30
    #define CI_IP_O_LSRR                 31
    #define CI_IP_O_SSRR                 32
    #define CI_IP_O_RR                   33
    #define CI_IP_O_STREAM               34
    #define CI_IP_O_TIME                 35
    #define CI_IP_ADD_MEMBERSHIP         36
    #define CI_IP_DROP_MEMBERSHIP        37
    #define CI_IP_MULTICAST_IF           38
    #define CI_IP_MULTICAST_LOOP         39
    #define CI_IP_MULTICAST_TTL          40
    #define CI_IP_TTL                    41
    #define CI_IP_BLOCK_SOURCE           42
    #define CI_IP_UNBLOCK_SOURCE         43
    #define CI_IP_ADD_SOURCE_MEMBERSHIP  44
    #define CI_IP_DROP_SOURCE_MEMBERSHIP 45
    #define CI_MCAST_JOIN_GROUP          46
    #define CI_MCAST_LEAVE_GROUP         47
    #define CI_MCAST_BLOCK_SOURCE        48
    #define CI_MCAST_UNBLOCK_SOURCE      49
    #define CI_MCAST_JOIN_SOURCE_GROUP   50
    #define CI_MCAST_LEAVE_SOURCE_GROUP  51
    #define CI_IPV6_MULTICAST_IF         52
    #define CI_IPV6_MULTICAST_HOPS       53
    #define CI_IPV6_MULTICAST_LOOP       54
    #define CI_IPV6_JOIN_GROUP           55
    #define CI_IPV6_LEAVE_GROUP          56
    #define CI_IPV6_V6ONLY               57
    #define CI_IPV6_PREFER_TEMP_ADDRS    58
    #define CI_IPV6_TCLASS               59
    #define CI_TCP_ACKDELAYTIME          60
    #define CI_TCP_ACKNSEG               61
    #define CI_TCP_ADAPT_ACKNSEG         62
    #define CI_TCP_PERMIT_SACKS          63
    #define CI_TCP_SEND_SACKS            64
    #define CI_TCP_FAST_RETR_RECOV       65
    #define CI_TCP_SLOW_START_CA         66
    #define CI_TCP_MAX_TTL               67
    #define CI_TCP_KEEPALIVE_CNT         68
    #define CI_TCP_KEEPALIVE_IDLE        69
    #define CI_TCP_KEEPALIVE_INTVL       70
    #define CI_TCP_ENABLE_PAWS           71
    #define CI_TCP_MAXSEG                72
    #define CI_TCP_NODELAY               73
    #define CI_TCP_O_SEQNO               74
    #define CI_TCP_PROVIDE_TIMESTAMPS    75
    #define CI_TCP_REX_MAX               76
    #define CI_TCP_REX_MIN               77
    #define CI_TCP_REX_INIT              78
    #define CI_TCP_RTT_ALGORITHM         79
    #define CI_TCP_SET_RCV_MSS           80
    #define CI_TCP_USE_PEER_MSS_OPTION   81
    #define CI_TCP_WINDOW_SCALE          82
     
    /* Socket "type" codes */
    #define CI_SOCK_STREAM               1
    #define CI_SOCK_DGRAM                2
    #define CI_SOCK_RAW                  3
     
    /* Defines for CI_IoctlSocket commands. Values are arbitrary. */
    #define CI_FIONBIO                   0
    #define CI_FIONREAD                  1
    #define CI_FIONWRITE                 2
     
     
    /* AF/PF Defines */
    #ifndef AF_INET
      #define AF_INET                    1
    #endif
     
    #ifndef AF_PACKET
      #define AF_PACKET                  1
    #endif
     
    #ifndef PF_INET
      #define PF_INET                    AF_INET
    #endif
     
    #ifndef PF_PACKET
      #define PF_PACKET                  AF_PACKET
    #endif
     
    #ifndef INADDR_ANY
      #define INADDR_ANY                 0x00000000L
    #endif
     
    // ----------------------------------------------------------------------------
    #ifndef sa_family_t
      typedef uint16_t sa_family_t;
    #endif
     
     
    #ifndef IP_SERVICE
      struct sockaddr {
        sa_family_t      sa_family;
        int8_t           sa_data[28];
      };
     
      struct in_addr {
        uint32_t         s_addr;
      };
     
      struct sockaddr_in {
        int16_t          sin_family;
        uint16_t         sin_port;
        struct in_addr   sin_addr;
        char             sin_zero[8];
      };
     
      struct ip_mreq {
        struct in_addr imr_multiaddr;
        struct in_addr imr_interface;
      };
     
      struct ip_mreq_source {
        struct in_addr imr_multiaddr;
        struct in_addr imr_sourceaddr;
        struct in_addr imr_interface;
      };
     
      struct linger {
        int32_t l_onoff;
        int32_t l_linger;
      };
     
      struct ipot_t {
        uint8_t pointer;
        uint8_t oflw_flg;
        uint32_t ipt_addr[9];
      };
     
      typedef struct {
        uint32_t fd[(CI_FDSET_SIZE/CI_FDSET_FD_NBITS)+1];
      } fd_set;
    #endif
     
     
    /* BSD Socket structs */
    #ifndef socklen_t
      typedef int32_t  socklen_t;
    #endif
     
    #ifndef WIN32
      struct addrinfo {
        int32_t          ai_flags;
        int32_t          ai_family;
        int32_t          ai_socktype;
        int32_t          ai_protocol;
        socklen_t        ai_addrlen;
        struct sockaddr *ai_addr;
        char            *ai_canonname;
        struct addrinfo *ai_next;
      };
    #endif
     
    // ----------------------------------------------------------------------------
    // End Macros, typedefs, enums ************************************************
     
    // Global Variables (externs, globals, static globals) ************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Global Variables *******************************************************
     
    // Functions ******************************************************************
    // End Functions **************************************************************
     
    // Unset the packing setting used for this file to the previous one
    #pragma pack(pop)
     
    #endif /* _CI_SOCKET_DEFINES_H_ */
   
   </code>
   
   ==== 6.17 CI-srv/inc/ CI_socket_types.h====
   <code>
   /*
     * Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    /* Exclusionary ifdef */
    #ifndef _CI_SOCKET_TYPES_H_
    #define _CI_SOCKET_TYPES_H_
     
    // Includes *******************************************************************
    #include <stdint.h>
     
    #include "CI_socket_defines.h"
     
    // End Includes ***************************************************************
     
    // Macros, typedefs, enums ****************************************************
     
    /***************************************************************************
     * IMPORTANT: The interface version below is used to detect CHANGES the to
     * functions in the interface and SHALL be updated any time there is a change
     * to ANY function in this header that is part of a registered (i.e. used with
     * the registrar) interface. "Change" in this case only means a change to the
     * SIGNATURE of a function. The interface version need not be updated if the
     * number of functions in the interface changes (i.e. a function is added or
     * removed).
     ***************************************************************************/
    #define  CI_SOCKET_VER_MAJ  0x01
    #define  CI_SOCKET_VER_MIN  0x02
    #define  CI_SOCKET_VER      ((CI_SOCKET_VER_MAJ << 16) | CI_SOCKET_VER_MIN)
    #define  CI_SOCKET_NAME     ("CI_socketIf")
     
    /* API Function Name List */
    #define  CI_SOCKET_NAME_VERSION            ("Version")     /* 1st in list */
    #define  CI_SOCKET_NAME_IOCTLSOCKET        ("IoctlSocket")
    #define  CI_SOCKET_NAME_ACCEPT             ("Accept")
    #define  CI_SOCKET_NAME_BIND               ("Bind")
    #define  CI_SOCKET_NAME_CLOSESOCKET        ("CloseSocket")
    #define  CI_SOCKET_NAME_CONNECT            ("Connect")
    #define  CI_SOCKET_NAME_FREEADDRINFO       ("FreeAddrInfo")
    #define  CI_SOCKET_NAME_GETADDRINFO        ("GetAddrInfo")
    #define  CI_SOCKET_NAME_GETLASTSOCKETERROR ("GetLastSockErr")
    #define  CI_SOCKET_NAME_GETNAMEINFO        ("GetNameInfo")
    #define  CI_SOCKET_NAME_GETPEERNAME        ("GetPeerName")
    #define  CI_SOCKET_NAME_GETSOCKNAME        ("GetSockName")
    #define  CI_SOCKET_NAME_GETSOCKOPT         ("GetSockOpt")
    #define  CI_SOCKET_NAME_LISTEN             ("Listen")
    #define  CI_SOCKET_NAME_RECV               ("Recv")
    #define  CI_SOCKET_NAME_RECVFROM           ("RecvFrom")
    #define  CI_SOCKET_NAME_SELECT             ("Select")
    #define  CI_SOCKET_NAME_GETFDSET           ("GetFdSet")
    #define  CI_SOCKET_NAME_RETURNFDSET        ("ReturnFdSet")
    #define  CI_SOCKET_NAME_FDCLR              ("FD_CLR")
    #define  CI_SOCKET_NAME_FDISSET            ("FD_ISSET")
    #define  CI_SOCKET_NAME_FDSET              ("FD_SET")
    #define  CI_SOCKET_NAME_FDZERO             ("FD_ZERO")
    #define  CI_SOCKET_NAME_SEND               ("Send")
    #define  CI_SOCKET_NAME_SENDTO             ("SendTo")
    #define  CI_SOCKET_NAME_SETSOCKOPT         ("SetSockOpt")
    #define  CI_SOCKET_NAME_SOCKET             ("Socket")
    #define  CI_SOCKET_NAME_SHUTDOWN           ("Shutdown")
    #define  CI_SOCKET_NAME_INET_ADDR          ("InetAddr")
    #define  CI_SOCKET_NAME_INET_NTOA          ("InetNtoA")
     
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Macros, typedefs, enums ************************************************
     
    /* indexes must match order of CI_socketIf_g array */
    typedef enum {
      CI_SOCKETS_UTILS_VERSION_INDEX,
      CI_SOCKETS_IOCTLSOCKET_INDEX,
      CI_SOCKETS_ACCEPT_INDEX,
      CI_SOCKETS_BIND_INDEX,
      CI_SOCKETS_CLOSESOCKET_INDEX,
      CI_SOCKETS_CONNECT_INDEX,
      CI_SOCKETS_FREEADDRINFO_INDEX,
      CI_SOCKETS_GETADDRINFO_INDEX,
      CI_SOCKETS_GETLASTSOCKERR_INDEX,
      CI_SOCKETS_GETNAMEINFO_INDEX,
      CI_SOCKETS_GETPEERNAME_INDEX,
      CI_SOCKETS_GETSOCKNAME_INDEX,
      CI_SOCKETS_GETSOCKOPT_INDEX,
      CI_SOCKETS_LISTEN_INDEX,
      CI_SOCKETS_RECV_INDEX,
      CI_SOCKETS_RECVFROM_INDEX,
      CI_SOCKETS_SELECT_INDEX,
      CI_SOCKETS_GETFDSET_INDEX,
      CI_SOCKETS_RETURNFDSET_INDEX,
      CI_SOCKETS_FD_CLR_INDEX,
      CI_SOCKETS_FD_ISSET_INDEX,
      CI_SOCKETS_FD_SET_INDEX,
      CI_SOCKETS_FD_ZERO_INDEX,
      CI_SOCKETS_SEND_INDEX,
      CI_SOCKETS_SENDTO_INDEX,
      CI_SOCKETS_SETSOCKOPT_INDEX,
      CI_SOCKETS_SOCKET_INDEX,
      CI_SOCKETS_SHUTDOWN_INDEX,
      CI_SOCKETS_INET_ADDR_INDEX,
      CI_SOCKETS_INET_NTOA_INDEX,
      CI_SOCKETS_NUM_FUNC_INDEXES        /* this value always last */
    } CI_socketsIndex_t;
     
     
    // Global Variables (externs, globals, static globals) ************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Global Variables *******************************************************
     
    // Functions ******************************************************************
     
    /* ------------------------------------------------------------------------- */
    /* ------------------- Function types for this interface ------------------- */
    /* ------  See the corresponding API header for function declarations ------ */
    /* ------------------------------------------------------------------------- */
     
    typedef int32_t (CI_IoctlSocketProto_t)(int32_t socket,
                                            int32_t cmd,
                                            uint32_t *argp);
    typedef CI_IoctlSocketProto_t (*CI_IoctlSocket_tp);
     
    typedef int32_t (CI_acceptProto_t)(int32_t socket,
                                       struct sockaddr *addr_p,
                                       socklen_t *addrlen_p);
    typedef CI_acceptProto_t (*CI_accept_tp);
     
    typedef int32_t (CI_bindProto_t)(int32_t socket,
                                     const struct sockaddr *addr_p,
                                     socklen_t addrlen);
    typedef CI_bindProto_t (*CI_bind_tp);
     
    typedef int32_t (CI_closeSocketProto_t)(int32_t socket, int32_t *err_p);
    typedef CI_closeSocketProto_t (*CI_closeSocket_tp);
     
    typedef int32_t (CI_connectProto_t)(int32_t socket,
                                        struct sockaddr *addr_p,
                                        socklen_t addrlen);
    typedef CI_connectProto_t (*CI_connect_tp);
     
    typedef void (CI_freeAddrInfoProto_t)(struct addrinfo *res_p);
    typedef CI_freeAddrInfoProto_t (*CI_freeAddrInfo_tp);
     
    typedef int32_t (CI_getAddrInfoProto_t)(const char *node_p,
                                            const char *service_p,
                                            const struct addrinfo *hints_p,
                                            struct addrinfo **res_p);
    typedef CI_getAddrInfoProto_t (*CI_getAddrInfo_tp);
     
    typedef int32_t (CI_getLastSocketErrorProto_t)(int32_t socket, int32_t *err_p);
    typedef CI_getLastSocketErrorProto_t (*CI_getLastSocketError_tp);
     
    typedef int32_t (CI_getNameInfoProto_t)(const struct sockaddr *addr_p,
                                            socklen_t addrlen,
                                            char *host_p,
                                            int32_t hostlen,
                                            char *serv_p,
                                            int32_t servlen,
                                            int32_t flags);
    typedef CI_getNameInfoProto_t (*CI_getNameInfo_tp);
     
    typedef int32_t (CI_getPeerNameProto_t)(int32_t socket,
                                            struct sockaddr *addr_p,
                                            socklen_t *addrlen_p);
    typedef CI_getPeerNameProto_t (*CI_getPeerName_tp);
     
    typedef int32_t (CI_getSockNameProto_t)(int32_t socket,
                                            struct sockaddr *addr_p,
                                            socklen_t *addrlen_p);
    typedef CI_getSockNameProto_t (*CI_getSockName_tp);
     
    typedef int32_t (CI_getSockOptProto_t)(int32_t socket,
                                           int32_t level,
                                           int32_t optname,
                                           void *optval_p,
                                           socklen_t *optlen);
    typedef CI_getSockOptProto_t (*CI_getSockOpt_tp);
     
    typedef int32_t (CI_listenProto_t)(int32_t socket, int32_t backlog);
    typedef CI_listenProto_t (*CI_listen_tp);
     
    typedef int32_t (CI_recvProto_t)(int32_t socket,
                                     void *buf_p,
                                     int32_t length,
                                     int32_t flags);
    typedef CI_recvProto_t (*CI_recv_tp);
     
    typedef int32_t (CI_recvFromProto_t)(int32_t socket,
                                         void *buf_p,
                                         int32_t length,
                                         int32_t flags,
                                         struct sockaddr *addr_p,
                                         socklen_t *addrlen_p);
    typedef CI_recvFromProto_t (*CI_recvFrom_tp);
     
    typedef int32_t (CI_selectProto_t)(int32_t nfds,
                                       fd_set *readset_p,
                                       fd_set *writeset_p,
                                       fd_set *exceptset_p,
                                       int32_t timeoutMicroSec);
    typedef CI_selectProto_t (*CI_select_tp);
     
    typedef void *(CI_getFdSetProto_t)();
    typedef CI_getFdSetProto_t (*CI_getFdSet_tp);
     
    typedef void (CI_returnFdSetProto_t)(void *set_p);
    typedef CI_returnFdSetProto_t (*CI_returnFdSet_tp);
     
    typedef void (CI_fdClrProto_t)(int32_t fd, void *set_p);
    typedef CI_fdClrProto_t (*CI_fdClr_tp);
     
    typedef int32_t (CI_fdIsSetProto_t)(int32_t fd, void *set_p);
    typedef CI_fdIsSetProto_t (*CI_fdIsSet_tp);
     
    typedef void (CI_fdSetProto_t)(int32_t fd, void *set_p);
    typedef CI_fdSetProto_t (*CI_fdSet_tp);
     
    typedef void (CI_fdZeroProto_t)(void *set_p);
    typedef CI_fdZeroProto_t (*CI_fdZero_tp);
     
    typedef int32_t (CI_sendProto_t)(int32_t socket,
                                     const void *buf_p,
                                     int32_t length,
                                     int32_t flags);
    typedef CI_sendProto_t (*CI_send_tp);
     
    typedef int32_t (CI_sendToProto_t)(int32_t socket,
                                       const void *buf_p,
                                       int32_t length,
                                       int32_t flags,
                                       struct sockaddr *addr_p,
                                       socklen_t addrlen);
    typedef CI_sendToProto_t (*CI_sendTo_tp);
     
    typedef int32_t (CI_setSockOptProto_t)(int32_t socket,
                                           int32_t level,
                                           int32_t optname,
                                           const void *optval_p,
                                           socklen_t optlen);
    typedef CI_setSockOptProto_t (*CI_setSockOpt_tp);
     
    typedef int32_t (CI_socketProto_t)(int32_t domain,
                                       int32_t type,
                                       int32_t protocol,
                                       int32_t *err_p);
    typedef CI_socketProto_t (*CI_socket_tp);
     
    typedef int32_t (CI_shutdown_t)(int32_t fd,
                                    int32_t direction,
                                    int32_t *err_p);
    typedef CI_shutdown_t (*CI_shutdown_tp);
     
    typedef uint32_t (CI_inetAddr_t)(const char *c_p);
    typedef CI_inetAddr_t (*CI_inetAddr_tp);
     
    typedef char * (CI_inetNtoA_t)(struct in_addr in);
    typedef CI_inetNtoA_t (*CI_inetNtoA_tp);
     
    // End Functions **************************************************************
     
    #endif /* _CI_SOCKET_TYPES_H_ */
   
   </code>
   ==== 6.18 CI-srv/inc/ CI_system_api.h ====
   <code>
   /*
    * Copyright (c) 2019-2020 Analog Devices, Inc. All Rights Reserved.
    *
    * This software is proprietary and confidential to Analog Devices, Inc. and
    * its licensors.
    */
   
   /* Exclusionary ifdef */
   #ifndef _CI_SYSTEM_API_H_
   #define _CI_SYSTEM_API_H_
   
   // Includes *******************************************************************
   #include "CI_system_types.h"
   
   // End Includes ***************************************************************
   
   // Macros, typedefs, enums ****************************************************
   // ----------------------------------------------------------------------------
   // ----------------------------------------------------------------------------
   // End Macros, typedefs, enums ************************************************
   
   // Global Variables (externs, globals, static globals) ************************
   // ----------------------------------------------------------------------------
   // ----------------------------------------------------------------------------
   // End Global Variables *******************************************************
   
   // Functions ******************************************************************
   /**
    * Get a basket from the IO configuration file
    *
    * Parameters
    * Dir    Type      Name        Description
    * [in]   uint16_t  basketID    Basket ID number (from IO config file)
    *
    * Return
    * Type: CI_basket_t *
    * Values: pointer to CI_basket_t structure containing the contents of the
    *         specified basket or NULL if the basket doesn't exist
    */
   CI_getBasket_t CI_GetBasket;
   
   
   /**
    * Get the protocol implemented by the underlying network application
    *
    * Parameters
    * NONE
    *
    * Return
    * Type: CI_protocol_t
    * Values: protocol implemented by the network application (see CI_protocol_t)
    *         CI_protocolError if retrieval failed
    */
   CI_getProtocol_t CI_GetProtocol;
   
   /**
    * Set a system parameter
    *
    * Parameters
    * Dir    Type              Name          Description
    * [in]   CI_systemParam_t  param         The system parameter to set
    * [in]   void *            paramData_p   Pointer to buffer in which the
    *                                        desired system parameter data
    *                                        currently resides
    * [in]   uint16_t          paramSize     The number of bytes in the buffer
    *                                        pointed to by paramData_p
    *
    * The number of bytes in a given system parameter varies from parameter to
    * parameter. See the definition of CI_systemParam_t for the sizes and
    * structures of each parameter.
    *
    * For string parameters the value of paramSize must be less than or equal to
    * the value shown in CI_systemParam_t.  Otherwise, an error will be returned if
    * the caller provides fewer bytes than the size of the indicated parameter as
    * indicated by the paramSize argument.
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_INVALID_PARAM if parameter not a writeable parameter
    *         CI_INVALID_PARAM on unrecognized system parameter
    *         CI_INVALID_PARAM on NULL parameter data pointer
    *         CI_INVALID_PARAM if paramSize argument < size of indicated parameter
    *         CI_ERROR if called after CI_ConfigComplete()
    */
   CI_setSystemParam_t CI_SetSystemParam;
   
   /**
    * Get a system parameter
    *
    * Parameters
    * Dir    Type              Name        Description
    * [in]   CI_systemParam_t  param       The system parameter of interest (see
    *                                      CI_systemParam_t for examples and
    *                                      descriptions of system parameters)
    * [out]  void *            paramData_p Pointer to buffer into which the system
    *                                      parameter data should be copied
    * [in]   int32_t           paramLen_p  The number of bytes available in the
    *                                      buffer pointed to by paramData_p
    *
    * The number of bytes in a given system parameter varies from parameter to
    * parameter. See the definition of CI_systemParam_t for the sizes and
    * structures of each parameter.
    *
    * Return
    * Type: int32_t
    * Values: number of bytes copied to caller's buffer (i.e. the parameter size)
    *         CI_INVALID_PARAM if parameter not a readable parameter
    *         CI_INVALID_PARAM on unrecognized system parameter
    *         CI_INVALID_PARAM on NULL parameter data pointer
    */
   CI_getSystemParam_t CI_GetSystemParam;
   
   /**
    * Apply and/or store the system IP settings.
    *
    * Parameters
    * Dir    Type           Name        Description
    * [in]   bool           store       set to true to override stored settings
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_INVALID_PARAM if IP settings conflict
    *         CI_ERROR if error in applying IP settings.
    */
   CI_applySystemIpParam_t  CI_ApplySystemIpParam;
   
   /**
    * Store the ethernet settings in non-volatile memory.
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR if error storing settings in NVM
    */
   CI_storeSystemEthParam_t CI_StoreSystemEthParam;
   
   /**
    * Set the value of an industrial Ethernet protocol parameter
    *
    * Parameters
    * Dir    Type                Name        Description
    * [in]   CI_protocolParam_t  param       The protocol parameter to set (see
    *                                        CI_protocolParam_t)
    * [in]   void *              paramData_p Pointer to buffer in which the
    *                                        desired parameter data currently
    *                                        resides
    * [in]   uint32_t            paramSize   The number of bytes in the buffer
    *                                        pointed to by paramData_p
    *
    * The number of bytes in a given protocol parameter varies from parameter to
    * parameter. See the definition of CI_protocolParam_t for the sizes and
    * structures of each parameter.
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_INVALID_PARAM if protocol parameter unsupported
    *         CI_INVALID_PARAM if protocol parameter data pointer == NULL
    *         CI_INVALID_PARAM if protocol parameter size incorrect
    *         CI_ERROR on error
    */
   CI_setProtocolParam_t CI_SetProtocolParam;
   
   /**
    * Get the value of an industrial Ethernet protocol parameter
    *
    * Parameters
    * Dir    Type                Name        Description
    * [in]   CI_protocolParam_t  param       The protocol parameter of interest
    *                                        (see CI_protocolParam_t)
    * [out]  void *              paramData_p Pointer to buffer into which the
    *                                        protocol parameter data should be
    *                                        copied
    * [in]   uint32_t            paramSize   Size (in bytes) of the requested
    *                                        parameter data
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_INVALID_PARAM if protocol parameter unsupported
    *         CI_INVALID_PARAM if protocol parameter data pointer == NULL
    *         CI_INVALID_PARAM if protocol parameter size incorrect
    *         CI_ERROR on error
    */
   CI_getProtocolParam_t CI_GetProtocolParam;
   
   /**
    * Indicate that configuration is complete (device set, all items added, system
    * parameters set, etc.).
    *
    * This is the last function called during configuration time. No further calls
    * should be made to CI_AddItem(), etc. No calls to standard operation
    * functions (e.g. CI_WriteItem(), CI_ReadItem()) should be made before this
    * function is called.
    *
    * Parameters
    * NONE
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR if there is a problem with the system
    */
   CI_configComplete_t CI_ConfigComplete;
   
   /**
    * Set the status for the IO app side of the system
    *
    * Parameters
    * Dir    Type                Name        Description
    * [in]   CI_systemStatus_t   status      New IO app status to report to
    *                                        network app
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR if system not configured
    */
   CI_setSysStatus_t CI_SetSystemStatus;
   
   /**
    * Get the status of the network application side of the system
    *
    * Return
    * Type: int32_t
    * Values: CI_systemStatus_t on success
    *         CI_ERROR if system not configured
    */
   CI_getSysStatus_t CI_GetSystemStatus;
   
   /**
    * Block until the next network I/O cycle
    *
    * Use this routine to synchronize the IO application's I/O processing with
    * network IO cycle
    *
    * Parameters
    * [in]   uint32_t  maxWait   Maximum number of microseconds the call to this
    *                            function will take (subject to rounding to the
    *                            system clock tick). Use CI_WAIT_FOREVER to wait
    *                            indefinitely.
    *
    * Return
    * Type: int32_t
    * Values: CI_OK after wait on complete
    *         CI_ERROR if blocking feature not available yet
    */
   CI_waitIo_t CI_WaitIO;
   
   /**
    * Get a Common Interface event
    *
    * Parameters
    * Dir    Type              Name      Description
    * [out]  CI_eventInfo_t *  event_p   Pointer to event information structure to
    *                                    be filled in
    * [in]   int16_t           block     ==0: return immediately whether or not an
    *                                         event has been retrieved
    *                                    !=0: return only after (i.e. block until)
    *                                         an event has been retrieved
    *
    * Return
    * Type: int32_t
    * Values: CI_OK            event structure successfully retrieved
    *         CI_EMPTY         if the event queue is empty
    *         CI_ERROR         if there is an error within the queue
    *         CI_INVALID_PARAM if event invalid or system not in proper state
    */
   CI_getEvent_t CI_GetEvent;
   
   /**
    * Add an extension to the Common Interface
    *
    * Parameters
    *
    * Dir: [in]
    * Type: CI_interfaceExtension_t
    * Name: extension
    * Description: Requested interface extension
    *
    * Dir: [in]
    * Type: int32_t
    * Name: version
    * Description: Version for the requested interface extension
    *
    * Dir: [in]
    * Type: void*
    * Name: callbackTable_p
    * Description: Pointer to IO application-side callback function pointer
    * table structure e.g. CI_EipStatusLedIfExt_t (provided by IO app to network
    * app). Callback functions are defined and pointers to them are placed into
    * the callback table structure. The pointer to the table is passed to the
    * interface extension function to allow the network app to invoke the
    * callbacks using the function pointers stored in the table structure.
    *
    * Dir: [out]
    * Type: void**
    * Name: ifExtensionTable_p
    * Reference to a pointer to a function pointer table structure defined on the
    * network application side. This table structure contains pointers to
    * functions that extend the interface referred to by the extension variable.
    * The IO application, prior to attempting to use any these functions needs to
    * test that the table pointer is non-null, and that any given function pointer in
    * the table is non-null. Once these checks are completed, the application may
    * use the function pointer to invoke the desired network-app-side function.
    *
    * Return
    * Type: int32_t
    * Values: CI_OK for success
    *         CI_INVALID_PARAM if callback table pointer is null, unsupported
    *                          extension, or protocol implementation of
    *                          interface extension function is not registered
    *         CI_ERROR if extension cannot be added or other error
    */
   CI_addInterfaceExtension_t CI_AddInterfaceExtension;
   
   /**
    * Get system time
    *
    * Parameters
    * Dir    Type              Name      Description
    * [out]  CI_time_t *       time_p   Pointer to time information structure to
    *                                    be filled in
    *
    * Return
    * Type: int32_t
    * Values: CI_OK               system time successfully retrieved
    *         CI_ERROR            never got response from SNTP server
    *         CI_TIME_NOT_SYNCED  last sync was more than one minute ago
    *         CI_PARAM_ERROR      argument is invalid
    */
   CI_getSystemTime_t CI_GetSystemTime;
   
   /**
    * Configure time zone
    *
    * Parameters
    * Dir    Type              Name            Description
    * [in]   int32_t           timeCorrection  time correction in minutes with 
    *                                          respect to UTC
    *
    * Type: int32_t
    * Values: CI_OK            timezone configuration successful
    *         CI_ERROR         if there is an error while configuring timezone
    */
   CI_configureTimezone_t CI_ConfigureTimezone;
   
   /**
    * Open network ports
    *
    * Parameters
    * Dir    Type                 Name      Description
    * [in]   CI_portsSubsystem_t  subSystem Open all ports associated with 
    *                                         requested subsystem
    *
    * Return
    * Type: int32_t
    * Values: CI_OK            Open ports was successful
    *         CI_ERROR         Error while opening ports
    */
   CI_openPorts_t CI_OpenPorts;
   
   /**
    * Close network ports
    *
    * Parameters
    * Dir    Type                 Name      Description
    * [in]   CI_portsSubsystem_t  subSystem Close all ports associated with 
    *                                         requested subsystem
    *
    * Return
    * Type: int32_t
    * Values: CI_OK            Close ports was successful
    *         CI_ERROR         Error while closing ports
    */
   CI_closePorts_t CI_ClosePorts;
   
   // End Functions **************************************************************
   
   #endif /* _CI_SYSTEM_API_H_ */
   
   </code>
   ==== 6.19 CI-srv/inc/CI_system_types.h ====
   <code>
   /*
     * Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     * This software is proprietary and confidential to Analog Devices, Inc. and
     * its licensors.
     */
     
    /* Exclusionary ifdef */
    #ifndef _CI_SYSTEM_TYPES_H_
    #define _CI_SYSTEM_TYPES_H_
     
    // Includes *******************************************************************
    #include <stdint.h>
    #include <stdbool.h>
    // End Includes ***************************************************************
     
    // Macros, typedefs, enums ****************************************************
     
    /***************************************************************************
     * IMPORTANT: The interface versions below is used to detect CHANGES the to
     * functions in the interfaces and SHALL be updated any time there is a change
     * to ANY function in this header that is part of a registered (i.e. used with
     * the registrar) interface. "Change" in this case only means a change to the
     * SIGNATURE of a function. The interface version need not be updated if the
     * number of functions in the interface changes (i.e. a function is added or
     * removed).
     ***************************************************************************/
    #define  CI_SYS_VER_MAJ  0x01
    #define  CI_SYS_VER_MIN  0x02
    #define  CI_SYS_VER     ((CI_SYS_VER_MAJ << 16) | CI_SYS_VER_MIN)
    #define  CI_SYS_NAME    ("CI_systemIf\0")
     
    #define  CI_SYS_PROTO_VER_MAJ  0x01
    #define  CI_SYS_PROTO_VER_MIN  0x00
    #define  CI_SYS_PROTO_VER     ((CI_SYS_PROTO_VER_MAJ << 16) | \
                                    CI_SYS_PROTO_VER_MIN)
    #define  CI_SYS_PROTO_NAME    ("CIsystemProtoIf")
     
    /* System API Function Name List */
    #define  CI_SYS_NAME_VERSION                 ("Version") /* must be first */
    #define  CI_SYS_NAME_GET_PROTOCOL            ("GetProtocol")
    #define  CI_SYS_NAME_GET_BASKET              ("GetBasket")
    #define  CI_SYS_NAME_SET_SYSTEM_PARAM        ("SetSystemParam")
    #define  CI_SYS_NAME_GET_SYSTEM_PARAM        ("GetSystemParam")
    #define  CI_SYS_NAME_STORE_SYSTEM_PARAM      ("StoreSysIpParam")
    #define  CI_SYS_NAME_APPLY_SYSTEM_IP_PARAM   ("ApplySysIpParam")
    #define  CI_SYS_NAME_STORE_SYSTEM_ETH_PARAM  ("StoreEthParam")
    #define  CI_SYS_NAME_CONFIG_COMPLETE         ("ConfigComplete")
    #define  CI_SYS_NAME_WAIT_IO                 ("WaitIo")
    #define  CI_SYS_NAME_GET_EVENT               ("GetEvent")
    #define  CI_SYS_NAME_GET_SYSTEM_STATUS       ("GetSysStatus")
    #define  CI_SYS_NAME_GET_SYSTEM_TIME         ("GetSystemTime")
    #define  CI_SYS_NAME_CONFIG_TIME_ZONE        ("ConfigTimeZone")
    #define  CI_SYS_NAME_OPEN_PORTS              ("OpenPorts")
    #define  CI_SYS_NAME_CLOSE_PORTS             ("ClosePorts")
     
    /* System Protocol API Function Name List */
    #define  CI_SYS_PROTO_NAME_VERSION            ("Version") /* must be first */
    #define  CI_SYS_PROTO_NAME_SET_PROTO_PARAM    ("SetProtoParam")
    #define  CI_SYS_PROTO_NAME_GET_PROTO_PARAM    ("GetProtoParam")
    #define  CI_SYS_PROTO_NAME_SET_SYS_STATUS     ("SetSysStatus")
    #define  CI_SYS_PROTO_NAME_ADD_IF_EXTENSION   ("AddIfExtension")
     
    // Wait forever for a network output data cycle to complete
    #define CI_WAIT_FOREVER                 0xFFFFFFFF
     
    // ----------------------------------------------------------------------------
     
    /* ------------------------------------------------------------------------ */
    /* ------------------ Data/enum types for this interface ------------------ */
    /* ------------------------------------------------------------------------ */
     
    /* Supported Common Interface protocols */
    typedef enum {
      CI_protocolError           = -1,
      CI_protocolProfinet        = 2,
      CI_protocolEtherNetIP      = 3,
      CI_protocolModbusTCP       = 4,
      CI_protocolEtherCAT        = 7,
      CI_protocolPowerlink       = 8,
      CI_protocolIP              = 9,
     
      CI_protocolLast            = 0xFFFFFFFF /* To force enumeration width */
    } CI_protocol_t;
     
    typedef enum {
      CI_phyDuplexModeHalf,
      CI_phyDuplexModeFull,
      CI_phyDuplexUnknown,
    } CI_phyDuplexMode_t;
     
    /* The item description data contained in a basket */
    typedef struct {
      uint16_t itemID;
      uint16_t itemLocation;
      uint32_t infoA;  /* developer-specified data A */
      uint32_t infoB;  /* developer-specified data B */
    } CI_basketCase_t;
     
    /* The basket structure, used to contain groups of items */
    #define CI_BASKET_VERSION  1  /* Increment for any change to basket structure */
    typedef struct {
      uint16_t deviceID;
      uint16_t itemCount;
      CI_basketCase_t *itemInfo_p; /* pointer to array of CI_basketCase_t structs */
    } CI_basket_t;
     
    /* Supported interface extensions of the Common Interface */
    typedef enum {
      CI_ifExtProfinetStackApi,
      CI_ifExtLedApi,
     
      /* Future extensions go here */
     
      CI_ifExtLast = 0xFFFF            /* To force enumeration width */
    } CI_interfaceExtension_t;
     
    /* Define the IP stats structure */
    /* Note the following counters are defined in the RFC 1213 MIB-II with the
     * exception of openSockets and maxSockets which were added for use by the
     * user application */
    typedef struct {
      /*TCP and UDP */
      uint32_t maxSockets;
      /* Total number of sockets of any type currently open */
      uint32_t openSockets;
     
      /* IP */
      uint32_t ipInDelivers;
      uint32_t ipReasmTimeout;
      uint32_t ipReasmReqds;
      uint32_t ipReasmOKs;
      uint32_t ipReasmFails;
      uint32_t ipInUnknownProtos;
      uint32_t ipInDiscards;
      uint32_t ipInReceives;
      uint32_t ipInHdrErrors;
      uint32_t ipForwDatagrams;
      uint32_t ipInAddrErrors;
      uint32_t ipInTruncPkts;
      uint32_t ipInMcastPkts;
      uint32_t ipInBcastPkts;
      uint32_t ipOutRequests;
      uint32_t ipFragOKs;
      uint32_t ipFragFails;
      uint32_t ipFragCreates;
      uint32_t ipOutDiscards;
      uint32_t ipOutNoRoutes;
      uint32_t ipRoutingDiscards;
      uint32_t ipOutMcastPkts;
      uint32_t ipOutBcastPkts;
      uint32_t ipOutTransmPkts;
      uint32_t ipOutMcastOctets;
      uint32_t ipOutOctets;
      uint32_t ipInOctets;
      uint32_t ipInMcastOctets;
      uint32_t ipForwarding;
      uint32_t ipDefTTL;
      uint64_t ipInHCReceives;
      uint64_t ipInHCOctets;
      uint64_t ipHCForwDatagrams;
      uint64_t ipInHCDelivers;
      uint64_t ipOutHCRequests;
      uint64_t ipOutHCTransmPkts;
      uint64_t ipOutHCOctets;
      uint64_t ipInHCMcastPkts;
      uint64_t ipInHCMcastOctets;
      uint64_t ipOutHCMcastPkts;
      uint64_t ipOutHCMcastOctets;
      uint64_t ipInHCBcastPkts;
      uint64_t ipOutHCBcastPkts;
     
      /* ICMP */
      uint32_t icmpInMsgs;
      uint32_t icmpInErrors;
      uint32_t icmpOutMsgs;
      uint32_t icmpOutErrors;
      uint32_t icmpInDestUnreachs;
      uint32_t icmpInPktTooBig;
      uint32_t icmpInTimeExcds;
      uint32_t icmpInParmProbs;
      uint32_t icmpInEchos;
      uint32_t icmpInEchoReps;
      uint32_t icmpInMcastLstQ;
      uint32_t icmpInMcastLstR;
      uint32_t icmpInMcastLstD;
      uint32_t icmpInRedirects;
      uint32_t icmpInSrcQuenchs;
      uint32_t icmpInAddrMaskReps;
      uint32_t icmpInAddrMasks;
      uint32_t icmpInTimestampReps;
      uint32_t icmpInTimestamps;
      uint32_t icmpOutDestUnreachs;
      uint32_t icmpOutPktTooBig;
      uint32_t icmpOutTimeExcds;
      uint32_t icmpOutParmProbs;
      uint32_t icmpOutEchos;
      uint32_t icmpOutEchoReps;
      uint32_t icmpOutMcastLstQ;
      uint32_t icmpOutMcastLstR;
      uint32_t icmpOutMcastLstD;
      uint32_t icmpOutRedirects;
      uint32_t icmpOutSrcQuenchs;
      uint32_t icmpOutAddrMaskReps;
      uint32_t icmpOutAddrMasks;
      uint32_t icmpOutTimestampReps;
      uint32_t icmpOutTimestamps;
     
      /* TCP */
      uint32_t tcpActiveOpens;
      uint32_t tcpPassiveOpens;
      uint32_t tcpAttemptFails;
      uint32_t tcpEstabResets;
      uint32_t tcpInSegs;
      uint32_t tcpOutSegs;
      uint32_t tcpRetransSegs;
      uint32_t tcpInErrs;
      uint32_t tcpOutRsts;
      uint64_t tcpHCOutSegs;
      uint64_t tcpHCInSegs;
     
      /* TCP Connections */
      uint32_t tcpEstablished;
     
      /* UDP */
      uint32_t udpInErrors;
      uint32_t udpInDatagrams;
      uint32_t udpNoPorts;
      uint32_t udpOutDatagrams;
      uint64_t udpHCInDatagrams;
      uint64_t udpHCOutDatagrams;
     
    } CI_statistic_t;
     
    /*
     * System parameters (as used by CI_SetSystemParam() and CI_GetSystemParam())
     * and their data types/structures are documented below
     */
    typedef enum {
      CI_sysParamIoAppVersion,
      /* Desc: Pointer to IO application version information structure
       * Type: IO_appInfo_t* */
     
      CI_sysParamNetworkAppVersion,
      /* Desc: Pointer to network application version information structure
       * Type: IO_appInfo_t* */
     
      CI_sysParamNumPorts,
      /* Desc: Number of attached ports
       * Type: uint16_t */
     
      CI_sysParamPortLinkState,
      /* Desc: Link state (up/down) for all attached ports
       * Type: uint32_t[]   Each element of the array is the link state for the
       *                    corresponding port - use CI_sysParamNumPorts to
       *                    get the number of attached ports
       *         ==0: no link on corresponding port
       *         !=0: link on corresponding port */
     
      CI_sysParamPortPhyState,
      /* Desc: PHY configuration for all attached ports from current settings
       * Type: uint32_t[][3]   (2-D array of uint32_t)
       *       Number of attached ports by uint32_t[3] per port - use
       *       CI_sysParamNumPorts to get the number of attached ports)
       *
       *       Per-port configuration array format
       *         Index 0: Auto-negotiation enabled
       *         Index 1: Link speed (in Mbps - 0: indicates speed is unknown)
       *         Index 2: Duplex mode see CI_phyDuplexMode_t */
     
      CI_sysParamPortPhyStateNvm,
      /* Desc: PHY configuration for all attached ports from NV memory
       *       Can be used by CI_GetSystemParam()
       * Type: uint32_t[][3]   (2-D array of uint32_t)
       *       Number of attached ports by uint32_t[3] per port - use
       *       CI_sysParamNumPorts to get the number of attached ports)
       *
       *       Per-port configuration array format
       *         Index 0: Auto-negotiation enabled
       *         Index 1: Link speed (in Mbps - 0: indicates speed is unknown)
       *         Index 2: Duplex mode see CI_phyDuplexMode_t */
     
      CI_sysParamPortEthStats,
      /* Desc: Simplified Ethernet statistics for all attached ports
       * Type: uint32_t[][18]   (2-D array of uint32_t)
       *       Number of attached ports by uint32_t[18] per port - use
       *       CI_sysParamNumPorts to get the number of attached ports)
       *
       *       Per-port statistics array format
       *         Index 0: Bytes received
       *         Index 1: Unicast packets received
       *         Index 2: Broadcast packets received
       *         Index 3: Multicast packets received
       *         Index 4: Frames received with alignment error
       *         Index 5: Frames received with CRC/FCS error
       *         Index 6: Frames received with large frame error
       *         Index 7: Frames with RX MAC errors
       *         --------------------
       *         Index 8: Bytes transmitted
       *         Index 9: Unicast packets transmitted
       *         Index 10: Broadcast packets transmitted
       *         Index 11: Multicast packets transmitted
       *         Index 12: Frames transmitted after single collision
       *         Index 13: Frames transmitted after multiple collisions
       *         Index 14: Frames dropped after excessive collisions
       *         Index 15: Frames with a collision after 512 bits
       *         Index 16: Frames delayed by traffic
       *         Index 17: Frames with TX MAC errors  */
     
      CI_sysParamMacAddresses,
      /* Desc: Local MAC addresses
       * Type: uint8_t[][6]   2-D array of uint8_t
       *       (Number of attached ports PLUS ONE for the system MAC by uint8_t[6]
       *       per MAC address - use CI_sysParamNumPorts to get the number of
       *       attached ports) */
     
      CI_sysParamDhcpEnable,
      /* Desc: DHCP enable flag
       * Type: uint8_t
       *       ==0: disable DHCP (use static IP address)
       *       !=0: enable DHCP */
     
      CI_sysParamIpAddress,
      /* Desc: System IP address
       * Type: uint32_t */
     
      CI_sysParamSubnetMask,
      /* Desc: Subnet mask
       * Type: uint32_t */
     
      CI_sysParamDefaultGateway,
      /* Desc: Default gateway IP address
       * Type: uint32_t */
     
      CI_sysParamPrimaryDns,
      /* Desc: Primary DNS server's IP address
       * Type: uint32_t */
     
      CI_sysParamSecondaryDns,
      /* Desc: Secondary DNS server's IP address
       * Type: uint32_t */
     
      CI_sysParamDomainName,
      /* Desc: Domain name
       * Type char[64] */
     
      CI_sysParamHostname,
      /* Desc: Local hostname
       * Type char[64] */
     
      CI_sysParamSerialNumber,
      /* Desc: Serial Number
       * Type: uint32_t */
     
      CI_sysParamIpStats,
      /* Desc: Simplified IP statistics for TCP/IP stack
       * Type: CI_statistic_t */
     
      CI_sysParamWebServerEnable,
      /* Desc: Web server enable flag
       * Type: uint8_t
       *       ==0: disable web server (use static IP address)
       *       !=0: enable web server */
     
      CI_sysParamSntpEnable,
      /* Desc: Sntp enable flag
       * Type: uint8_t
       *       ==0: disable sntp
       *       !=0: enable sntp */
     
      CI_sysParamPrimarySntp,
      /* Desc: Sntp primary server IP address
       * Type: uint32_t */
     
      CI_sysParamSecondarySntp,
      /* Desc: Sntp secondary server IP address
       * Type: uint32_t */
     
      /* Future system parameters go here... */
     
      CI_sysParamLast = 0xFFFFFFFF       /* To force enumeration width */
     
    } CI_systemParam_t;
     
    /*
     * Protocol parameters (as used by CI_SetProtocolParam() and
     * CI_GetProtocolParam()) and their data types/structures are documented below
     */
    typedef enum {
      /* PROFINET-specific parameters */
      CI_protoParamProfinetStationName = (CI_protocolProfinet * 1000),
      /* Desc: PROFINET station name (as assigned by the PLC)
       * Type: char[] (max length: 240 characters) */
     
     
      /* EtherNet/IP-specific parameters */
     
     
      /* Modbus/TCP-specific parameters */
     
     
      /* EtherCAT-specific parameters */
     
     
      /* POWERLINK-specific parameters */
     
      CI_protoParamLast = 0xFFFFFFFF      /* To force enumeration width */
    } CI_protocolParam_t;
     
    /* Status for IO application in general */
    typedef enum {
      CI_systemStatusFail,
      CI_systemStatusOk,
     
      CI_systemStatusLast = 0xFFFF        /* To force enumeration width */
    } CI_systemStatus_t;
     
    /* Overall link state */
    typedef enum {
      CI_ethLinkStateUnknown,      /* Link state not known or knowable */
      CI_ethLinkStateDown,         /* No ports have link */
      CI_ethLinkStateUp,           /* At least one port has link */
     
      CI_ethLinkStateLast = 0xFFFF        /* To force enumeration width */
    } CI_ethLinkState_t;
     
    /* PLC connection status */
    typedef enum {
      CI_plcConnectionStatusUnknown,    /* PLC connection status not known or
                                         * knowable */
      CI_plcConnectionStatusDown,       /* No PLC currently connected */
      CI_plcConnectionStatusUp,         /* At least one PLC connected */
      CI_plcConnectionStatusTimedOut,   /* IO transfer with PLC timed out */
     
      CI_plConnectionStatusLast = 0xFFFF  /* To force enumeration width */
    } CI_plcConnectionStatus_t;
     
    /* Common Interface events */
    typedef enum {
      CI_eventLinkChange,
      /* Description: The link state of the indicated port has changed.
       * info:        The new port link state (see CI_ethLinkState_t)
       * detail:      Upper 16 bits: interface number on which the port is located,
       *              Lower 16 bits: port number on the indicated interface on
       *                             which the link state changed
       */
     
      CI_eventIpConfigChange,
      /* Description: The system's IP configuration (e.g. IP address, subnet mask,
       *              default gateway address, etc.) has been changed via the
       *              underlying industrial protocol or configuration mechanism
       *              (e.g. DHCP). This event signals a IP configuration change
       *              caused by either the PLC or DHCP.
       * info:        == 0 if IP configuration just went invalid (IP address
       *                   received via DHCP or from PLC, etc. and deemed
       *                   invalid/unusable)
       *              != 0 if IP configuration just went valid (IP address received
       *                   via DHCP or from PLC, etc. and deemed valid)
       * detail:      Not used
       */
     
      CI_eventIpConflict,
      /* Description: EtherNet/IP only: The local system detected an IP address
       *              conflict with another device on the network.
       * info:        Not used
       * detail:      Not used
       */
     
      CI_eventPlcConnectionChange,
      /* Description: The state of the PLC connection has changed. A PLC has
       *              connected or disconnected from the local device or the
       *              connection has timed out.
       * info:        The new state of the PLC connection
       *              (see CI_plcConnectionStatus_t)
       * detail:      Not used
       */
     
      CI_eventReadItem,
      /* Description: New item data has arrived from the network, the IO
       *              application can read the indicated item to get the new data
       *              before the next network cycle takes place.
       * info:        Handle of the item for which data has arrived
       * detail:      ID of the item (used when the item was added to the system)
       */
     
      CI_eventWriteItem,
      /* Description: Item data was just retrieved by the network, the IO
       *              application can write the indicated item to set new data for
       *              the next network cycle.
       * info:        Handle of the item for which data has arrived
       * detail:      ID of the item (used when the item was added to the system)
       */
     
      CI_eventRiFlagChange,
      /* Description: EtherNet/IP only: The Run/Idle flag just changed.
       * info:        The new state of the Run/Idle flag
       * detail:      Not used
       */
     
      CI_eventDeviceBlinkInd,
      /* Description: PROFINET only: the PLC has requested that the local device
       *              blink (via its LEDs, display, etc.)
       * info:        Number of times to blink
       * detail:      Upper 16 bits: time for LED on, Lower 16 bits: time for LED off
       */
     
      CI_eventNetworkResetRequest,
      /* Description: The PLC (or other networked control device) has requested a
       *              local reset.
       * info:        For EtherNet/IP: the type of reset that was requested
       *              For all others: always 0
       * detail:      Not used
       */
     
      CI_eventWebServerStatus,
      /* Description: Status of the web server.
       * info:        Web Server specific sub-event
       * detail:      Status code of the sub-event
       */
     
      CI_eventLast = 0xFFFFFFFF           /* To force enumeration width */
    } CI_event_t;
     
    /* Event information */
    typedef struct {
      CI_event_t  event;    // What happened and/or what the IO app should do
      int32_t     info;     // Information about the event (see event descriptions)
      int32_t     detail;   // Detail about the event (see event descriptions)
    } CI_eventInfo_t;
     
    /* SNTP time */
    typedef struct {
      int32_t hour;
      int32_t minute;
      int32_t second;
      int32_t month;
      int32_t day;
      int32_t year;
    } CI_time_t;
     
    /* Subsystem ports */
    typedef enum {
      CI_portsIeProtocol,
      CI_portsWebServer,
      CI_portsSntp,
    }CI_portsSubsystem_t;
     
    /* ------------------------------------------------------------------------- */
    /* ------------------- Function types for this interface ------------------- */
    /* ------  See the corresponding API header for function declarations ------ */
    /* ------------------------------------------------------------------------- */
     
    // ===========================================================================
    // ===================== System Interface function types =====================
    // ===========================================================================
     
    typedef CI_protocol_t (CI_getProtocol_t)(void);
    typedef CI_getProtocol_t (*CI_getProtocol_tp);
     
    typedef CI_basket_t *(CI_getBasket_t)(uint16_t id);
    typedef CI_getBasket_t (*CI_getBasket_tp);
     
    typedef int32_t (CI_setSystemParam_t)(CI_systemParam_t param,
                                          void *paramData_p,
                                          uint16_t paramSize);
    typedef CI_setSystemParam_t (*CI_setSystemParam_tp);
     
    typedef int32_t (CI_getSystemParam_t)(CI_systemParam_t param,
                                          void *paramData_p,
                                          int32_t *paramLen);
    typedef CI_getSystemParam_t (*CI_getSystemParam_tp);
     
    typedef int32_t (CI_waitIo_t)(uint32_t maxWait);
    typedef CI_waitIo_t (*CI_waitIo_tp);
     
    typedef int32_t (CI_getEvent_t)(CI_eventInfo_t *event_p, int16_t block);
    typedef CI_getEvent_t (*CI_getEvent_tp);
     
    typedef int32_t (CI_addInterfaceExtension_t)(CI_interfaceExtension_t extension,
                                                 int32_t version,
                                                 void* callbackTable_p,
                                                 void** ifExtensionTable_p);
    typedef CI_addInterfaceExtension_t (*CI_addInterfaceExtension_tp);
     
    typedef int32_t (CI_applySystemIpParam_t)(bool store);
    typedef CI_applySystemIpParam_t (*CI_applySysemIpParam_tp);
     
    typedef int32_t (CI_storeSystemEthParam_t)(void);
    typedef CI_storeSystemEthParam_t (*CI_storeSystemEthParam_tp);
     
    typedef int32_t (CI_getSystemTime_t)(CI_time_t *time_p);
    typedef CI_getSystemTime_t (*CI_getSystemTime_tp);
     
    typedef int32_t (CI_configureTimezone_t)(int32_t timeCorrection);
    typedef CI_configureTimezone_t (*CI_configureTimezone_tp);
    // ===========================================================================
    // ================= System Protocol Interface function types ================
    // ===========================================================================
     
    typedef int32_t (CI_setProtocolParam_t)(CI_protocolParam_t param,
                                            void *paramData_p,
                                            uint32_t paramSize);
    typedef CI_setProtocolParam_t (*CI_setProtocolParam_tp);
     
    typedef int32_t (CI_getProtocolParam_t)(CI_protocolParam_t param,
                                            void *paramData_p,
                                            uint32_t paramSize);
    typedef CI_getProtocolParam_t (*CI_getProtocolParam_tp);
     
    typedef int32_t (CI_configComplete_t)(void);
    typedef CI_configComplete_t (*CI_configComplete_tp);
     
    typedef int32_t (CI_setSysStatus_t)(CI_systemStatus_t status);
    typedef CI_setSysStatus_t (*CI_setSysStatus_tp);
     
    typedef CI_systemStatus_t (CI_getSysStatus_t)(void);
    typedef CI_getSysStatus_t (*CI_getSysStatus_tp);
     
    typedef int32_t (CI_openPorts_t)(CI_portsSubsystem_t subSystem);
    typedef CI_openPorts_t(*CI_openPorts_tp);
     
    typedef int32_t (CI_closePorts_t)(CI_portsSubsystem_t subSystem);
    typedef CI_closePorts_t(*CI_closePorts_tp);
     
    // ----------------------------------------------------------------------------
    // End Macros, typedefs, enums ************************************************
     
    // Global Variables (externs, globals, static globals) ************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Global Variables *******************************************************
     
    // Functions ******************************************************************
    // End Functions **************************************************************
     
    #endif /* _CI_SYSTEM_TYPES_H_ */
   
   </code>
   ==== 6.20 CI-srv/inc/CI_webserver_api.h ====
   <code>
   /*
    *  Copyright (c) 2019-2020 Analog Devices, Inc. All Rights Reserved.
    *
    *  This software is proprietary and confidential to Analog Devices, Inc. and
    *  its licensors.
    */
   
   /****************************************************************************
   ** This header defines the CI webserver API.
   */
   
   #ifndef _CI_WEBSERVER_API_H_
   #define _CI_WEBSERVER_API_H_
   
   // Includes *******************************************************************
   #include "CI_webserver_types.h"
   
   // End Includes ***************************************************************
   
   // Macros, typedefs, enums ****************************************************
   // ----------------------------------------------------------------------------
   // ----------------------------------------------------------------------------
   // End Macros, typedefs, enums ************************************************
   
   // Global Variables (externs, globals, static globals) ************************
   // ----------------------------------------------------------------------------
   // ----------------------------------------------------------------------------
   // End Global Variables *******************************************************
   
   // Functions ******************************************************************
   
   /**
    * Set http tunnel handler.
    *
    * Parameters
    * Dir    Type                       Name            Description
    * [in]   CI_httpTunnelHandler_tp   handler_p      http tunnel handler to set
    *
    * The handler set using this function is called when tunnel request is
    * received from the web browser.
    *
    * An error will be returned if the caller provides invalid function pointer
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on NULL handler_p
    */
   CI_setHttpTunnelHandler_t CI_SetHttpTunnelHandler;
   
   /**
    * Set http response not found handler.
    *
    * Parameters
    * Dir    Type                          Name         Description
    * [in]   CI_httpResNotFoundHandler_tp handler_p   http res not found
    *                                                  handler to set
    *
    * The handler set using this function is called when webserver could not find
    * response for the given http request.
    *
    * An error will be returned if the caller provides invalid function pointer
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on NULL handler_p
    */
   CI_setHttpResNotFoundHandler_t CI_SetHttpResNotFoundHandler;
   
   
   /**
    * Write http response.
    *
    * Parameters
    * Dir    Type               Name         Description
    * [in]   const char *    format_p    pointer to the data to be formatted
    * [in]     -                -        variable number of arguments.
    *
    * Formats and writes the http response directly to the transmit buffer.
    * Format of the arguments is similar to standard library printf function.
    *
    * An error will be returned if format_p is null or when there is webserver
    * session exists.
    *
    * Return
    * Type: int32_t
    * Values: > 0 Number of bytes written.
    *         CI_ERROR on NULL format_p or there is no webserver connection.
    */
   
   CI_writeHttpResponse_t  CI_WriteHttpResponse;
   
   /**
    * Reloads certificate(/private/pki/server.crt) and key(/private/pki/server.key) 
    * used by the web-server from the file system
    *
    * Parameters
    * None
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success
    *         CI_ERROR on failure
    */
   CI_webserverCertificateReload_t  CI_WebserverCertificateReload;
   
   /**
    * Register url --> CGI handler mappings.
    *
    * Parameters
    * Dir    Type               Name         Description
    * [in]   CI_cgiEntry_t*   entry_p      Pointer to the cgi entries.
    * [in]   uint32_t*        numEntries   Number of entries to register.
    *
    * Register url --> CGI handler with web server.
    * Registered CGI handler (entry_p->handler_p) will be called when
    * url (entry_p->url) is received by the web server
    *
    * Return
    * Type: int32_t
    * Values: CI_OK on success.
    *         CI_ERROR on failure.
    */
   
   CI_registerCgiEntry_t  CI_RegisterCgiEntry;
   
   // End Functions **************************************************************
   
   #endif /* _CI_WEBSERVER_API_H_ */
   
   </code>
   ==== 6.21 CI-srv/inc/CI_webserver_types.h ====
   <code>
   
   /*
     *  Copyright (c) 2019-2021 Analog Devices, Inc. All Rights Reserved.
     *
     *  This software is proprietary and confidential to Analog Devices, Inc. and
     *  its licensors.
     */
     
    /****************************************************************************
    ** This header defines the CI web server API.
    */
     
    #ifndef _CI_WEBSERVER_TYPES_H_
    #define _CI_WEBSERVER_TYPES_H_
     
    // Includes *******************************************************************
    #include <stdint.h>
    #include <stdarg.h>
     
    // End Includes ***************************************************************
     
    // Macros, typedefs, enums ****************************************************
     
    /***************************************************************************
     * IMPORTANT: The interface version below is used to detect CHANGES the to
     * functions in the interface and SHALL be updated any time there is a change
     * to ANY function in this header that is part of a registered (i.e. used with
     * the registrar) interface. "Change" in this case only means a change to the
     * SIGNATURE of a function. The interface version need not be updated if the
     * number of functions in the interface changes (i.e. a function is added or
     * removed).
     ***************************************************************************/
     
    #define  CI_WEBS_VER_MAJ  0x01
    #define  CI_WEBS_VER_MIN  0x01
    #define  CI_WEBS_VER      ((CI_WEBS_VER_MAJ << 16) | CI_WEBS_VER_MIN)
    #define  CI_WEBS_NAME     ("CI_websIf")
     
    /* API Function List */
    #define  CI_WEBS_NAME_VERSION                    ("Version")
    #define  CI_NAME_SET_HTTP_TUNNEL_HANDLER         ("HttpTunlHandler")
    #define  CI_NAME_SET_HTTP_RES_NOT_FOUND_HANDLER  ("HttpResNotFound")
    #define  CI_NAME_WRITE_HTTP_RESPONSE             ("WriteHttpRes")
    #define  CI_NAME_WEBS_CERTIFICATE_RELOAD         ("WebsCertReload")
    #define  CI_NAME_WEBS_PASSWORD_RESET             ("WebsPassReset")
    #define  CI_NAME_REGISTER_CGI                    ("RegisterCgi")
     
    #define  CI_MAX_CGI_ENTRIES   256
    // ----------------------------------------------------------------------------
     
    /* ------------------------------------------------------------------------ */
    /* ------------------ Data/enum types for this interface ------------------ */
    /* ------------------------------------------------------------------------ */
     
    /* Tunnel request structure */
    typedef struct {
      char *requestData_p;
      int requestDataLen;
      char *requestUrl_p;
      int requestUrlLen;
    } CI_httpTunnelRequest_t;
     
    /* Tunnel response structure */
    typedef struct {
      char *responseData_p;
      int responseDataLen;
    } CI_httpTunnelResponse_t;
     
    /* Http error codes */
    typedef enum {
      CI_httpContinue = 0,             /* 100 */
      CI_httpSwitching,                /* 101 */
      CI_httpOk,                       /* 200 */
      CI_httpCreated,                  /* 201 */
      CI_httpAccepted,                 /* 202 */
      CI_httpNonAuthoritative,         /* 203 */
      CI_httpNoContent,                /* 204 */
      CI_httpReset,                    /* 205 */
      CI_httpPartial,                  /* 206 */
      CI_httpPartialOk,                /* 207 */
      CI_httpMultiple,                 /* 300 */
      CI_httpMoved,                    /* 301 */
      CI_httpFound,                    /* 302 */
      CI_httpMethod,                   /* 303 */
      CI_httpNotModified,              /* 304 */
      CI_httpUseProxy,                 /* 305 */
      CI_httpProxyRedirect,            /* 306 */
      CI_httpTempRedirect,             /* 307 */
      CI_httpBadRequest,               /* 400 */
      CI_httpUnAuthorized,             /* 401 */
      CI_httpPaymentRequired,          /* 402 */
      CI_httpForbidden,                /* 403 */
      CI_httpNotFound,                 /* 404 */
      CI_httpNotAllowed,               /* 405 */
      CI_httpNoneAcceptable,           /* 406 */
      CI_httpProxyUnauthorized,        /* 407 */
      CI_httpTimeout,                  /* 408 */
      CI_httpConflict,                 /* 409 */
      CI_httpGone,                     /* 410 */
      CI_httpLengthRequired,           /* 411 */
      CI_httpPreconFailed,             /* 412 */
      CI_httpTooBig,                   /* 413 */
      CI_httpUriTooBig,                /* 414 */
      CI_httpUnsupported,              /* 415 */
      CI_httpBadRange,                 /* 416 */
      CI_httpExpectationFailed,        /* 417 */
      CI_httpReauth,                   /* 418 */
      CI_httpProxyReauth,              /* 419 */
      CI_httpInternal,                 /* 500 */
      CI_httpNotImplemented,           /* 501 */
      CI_httpBadGate,                  /* 502 */
      CI_httpDown,                     /* 503 */
      CI_httpGateTimeout,              /* 504 */
      CI_httpBadVersion,               /* 505 */
      CI_httpNoPartialUpdate           /* 506 */
    } CI_httpStatus_t;
     
     
    /*CGI meta variables structure*/
    typedef struct {
      int contentLength;
      int serverPort;
      int remotePort;
      const char *authType_p;
      const char *contentType_p;
      const char *documentArgs_p;
      const char *queryString_p;
      const char *remoteUser_p;
      const char *requestMethod_p;
      const char *scriptName_p;
      const char *remoteAddress_p;
    } CI_cgiMetaVariable_t;
     
    /* CGI request structure*/
    typedef struct {
      CI_cgiMetaVariable_t metaVar;
      const char *msgBody_p;
    } CI_cgiRequest_t;
     
    /* CGI response structure.*/
    typedef struct {
      char *msgBody_p;
      int msgBodyMaxLen;
     
      const char *contentType_p;
      int msgBodyLen;
    } CI_cgiResponse_t;
     
    /* Web Server Events */
    typedef enum {
      CI_websStatusEventInit
      /* Description: Web Server Initialization Event status.
       *              It is used to report the return value of
       *              web server initialization.
       *              detailStatusCode will have the return value as
       *              CI_OK if Initialization is successful and
       *              CI_ERROR if Initialization is failed.
       */
    } CI_websStatusEvent_t;
     
    /* Web server event data */
    typedef struct {
      CI_websStatusEvent_t  statusEvent;
      int32_t               detailStatusCode;
    } CI_websEventData_t;
     
    /* Forward declaration of CGI handler */
    typedef void (*CI_cgiHandler_tp)(CI_cgiRequest_t, CI_cgiResponse_t *);
     
    /* CGI entry structure.*/
    typedef struct {
      const char *url_p;
      CI_cgiHandler_tp handler_p;
    } CI_cgiEntry_t;
     
    /* ------------------------------------------------------------------------- */
    /* ------------------- Function types for this interface ------------------- */
    /* ------  See the corresponding API header for function declarations ------ */
    /* ------------------------------------------------------------------------- */
    typedef int32_t (*CI_httpTunnelHandler_tp)(CI_httpTunnelRequest_t *req_p,
                                               CI_httpTunnelResponse_t *resp_p);
    typedef int32_t (CI_setHttpTunnelHandler_t)(CI_httpTunnelHandler_tp handler_p);
    typedef CI_setHttpTunnelHandler_t (*CI_setHttpTunnelHandler_tp);
     
    typedef int32_t (*CI_httpResNotFoundHandler_tp)(int32_t socket,
                                                    uint8_t* request_p,
                                                    uint32_t reqLen);
     
    typedef int32_t (CI_setHttpResNotFoundHandler_t)(
        CI_httpResNotFoundHandler_tp handler_p);
     
    typedef CI_setHttpResNotFoundHandler_t (*CI_setHttpResNotFoundHandler_tp);
     
    typedef int32_t (CI_writeHttpResponse_t)(const char* format_p, ...);
    typedef CI_writeHttpResponse_t (*CI_writeHttpResponse_tp);
     
    typedef int32_t (CI_webserverCertificateReload_t)(void);
    typedef CI_webserverCertificateReload_t (*CI_webserverCertificateReload_tp);
     
    typedef int32_t (CI_WebserverPasswordReset_t)(void);
    typedef CI_WebserverPasswordReset_t (*CI_WebserverPasswordReset_tp);
     
    typedef void (CI_cgiHandler_t)(CI_cgiRequest_t req, CI_cgiResponse_t *resp_p);
     
    typedef int32_t (CI_registerCgiEntry_t)(CI_cgiEntry_t *entry_p,
                                            uint32_t numEntries);
    typedef CI_registerCgiEntry_t (*CI_registerCgiEntry_tp);
     
    // ----------------------------------------------------------------------------
    // End Macros, typedefs, enums ************************************************
     
    // Global Variables (externs, globals, static globals) ************************
    // ----------------------------------------------------------------------------
    // ----------------------------------------------------------------------------
    // End Global Variables *******************************************************
     
    // Functions ******************************************************************
    // End Functions **************************************************************
    #endif /* _CI_WEBSERVER_TYPES_H_ */
   	
   </code>
   
   ===== 7. Profinet Extension API =====
   
   The RapID _Common Interface API (CI)_ is designed to provide a uniform interface on top of very different Industrial Ethernet Protocols, including EtherNet/IP, EtherCAT and Profinet. This allows an application on top of the Common Interface to work across protocols.
   While this works fine for many, maybe even most applications, there are sometimes needs that require deeper integration with a specific protocol. To enable this type of protocol specific work, the protocol Extensions API was introduced. It extents the Common Interface with functionality specific to a certain Industrial Ethernet protocol.
   This document focuses on the Profinet Extension available thru CI_extensions.h.
   
   ==== 7.1 Extensions and Callbacks ====
   
   === 7.1.1 Functions ===
   
   A class of functions provided by the respective protocol stacks within the NetworkApp. Functions defined in this table can be called by the application.
   Typical example for these kind of functions is CI_PnetAddItem_t function. It is Profinet specific and called by the application to plug a specific sub-module into a slot/subslot with a given API type.
   
   === 7.1.2 Extension Callbacks ===
   
   A class of function provided by the application and called by the NetworkApp. 
   Typical example for these kind of functions is the CI_LedSetStatusStateFunct_p() function that provides the current system LED status to the application.
   It is important to understand that those calls are executed by the calling context (CPU stack and priority). Therefore the calls shall be short and crisp. 
   •	Furthermore Interrupts shall not be disabled, at least not permanently
   •	IPC functions that send the calling thread into a wait state (e.g. wait on timer, wait on message, take semaphore) shall not be called from within a callback
   •	Sharing non-atomic variables (e.g. structs, 64-Bit variables) with the application code must be implemented with care
   
   
   === 7.1.3 When to install a function or callbacks ===
   
   Extensions can be installed any time before Config Complete is reached. After that point in time, calls to CI_AddInterfaceExtension() will be refused.
         int32_t CI_AddInterfaceExtension(CI_interfaceExtension_t extension,
                                          int32_t version,
                                          void* callbackTable_p,
                                          void** ifExtensionTable_p);
   
   This function provides a pointer to a structure that holds pointers to the extension functions - _ifExtensionTable_p_. before using one of the functions, the user shall check _ifExtensionTable_p_ as well as the specific function pointer in these structures being not _NULL_.
   
   === 7.1.4 Extend Set Device ===
   
   In Ci, one of the first things that need to be set up after system start is the device type. The device type defines many data important to a industrial ethernet device, such as vendorID and deviceID values. The device type information is protocol specific.
   The CI_SetDevice and CI_SetDeviceCustom functions are provided to set up the device. While CI_SetDevice will take the device information from the io-config database, CI_SetDevice allows the user to pass the device type information via a protocol specif data structure.
   However, the default data structure to set up a Profinet device lacks specific IDs for DAP and port submodules. This can lead to a conflict with some profiles, such as the PA profile. 
   Using the function 'CI_PNET_Ext_SetDevice_Func' from the extension interface allows to pass a DAPSubID and an individual portSubID per port:
         typedef int32_t (CI_PnetSetDevice_t)(CI_ProfinetDevice_t* device_p,
                                              uint32_t DAPSubID,
                                              uint16_t ports,
                                              uint32_t  *portSubId_p);
         CI_PnetSetDevice_t CI_PNET_Ext_SetDevice_Func;                                           
   Please note that DAPSubID and the portSubIds need to match the related values in the GSDML file.
   
   === 7.1.5 Managing Modules ===
   
   == 7.1.5.1 CI_PNET Ext ModuleDiff CB ==
   
   The CI_PNET_Ext_ModuleDiff_CB allows a customer to fix any deviations between the list of expected modules/submodules by the PLC and the modules/submodules actual plugged in the device. It grants the user an opportunity to fix miss mismatches before startup is completed.
   *Background:* 
   For each entry in the diff block, the function is called to compare expected slot/sub-slot configuration ("what the PLC believe is installed") with the installed ("what the device got actually installed"). This grants the application an opportunity to adjust the actual configuration to that expected by the PLC.
   This function does not directly influence how the stack handles any remaining differences between the PLC and device configuration.
   The return value just indicates whether the app was able to fix any mismatches or not. 
   The function will get called for the expected submodules only (the configuration defined in the PLC program).
   <code>
         typedef int32_t CI_PnetModuleDiffFunct_t (uint16_t ARindix,
                                                   uint32_t API,
                                                   uint16_t slot,
                                                   uint16_t subslot,
                                                   uint32_t realModuleID,
                                                   uint32_t expectedModuleID,
                                                   uint32_t realsubmoduleID,
                                                   uint32_t expectedSubmoduleID);
         CI_PnetModuleDiffFunct_t CI_PNET_Ext_ModuleDiff_CB;
         </code>
   The functions CI_addItem() and CI_removeItem() can be used to modify the configuration from within this callback. All memory associated with a CI_addItem() call is carefully removed in CI_removeItem() as needed.
   Once called for each expected module, a final call to this callback, called _finalization_ is executed with arNum and api both being 0xffff. This convenience call allows an application to clean up its configuration. It is still allowed to remove/add items at this point.
   If the call is used to change an existing configuration, the first call to that function or a "PLC down event" can be used to remove all slots/subslots of the current configuration. As an alternative, a list of modules no longer needed can be recorded and all module sin that list can be removed in the _finalization_ callback.  
   Note on Adding Record Indices (Acyclics)
   It is recommended to add acyclic items only after the related submodule has been plugged.
   
   == 7.1.5.2 ParamEnd  ==
   
   This callback is designed to inform an application that an Application Relationship (AR) has been established and configured. No further startup parameters will be sent by the PLC. Can be used to lock certain functionality. The ARindex passed as a parameter can help to understand which AR has completed the configuration in case than more than one AR is established. 
   Please note that adding and deleting items out of that callback will not work and will cause a deadlock of the Profinet stack.
   
   <code>
         typedef int32_t CI_PnetParameterEnd_t (uint16_t ARindix);
         CI_PnetParameterEnd_t CI_PNET_Ext_ParamEnd_CB;
   </code>
   
   == 7.1.5.3 Adding Items ==
   
   The Profinet device model uses a module/sub-module concept. A module in the Profinet model is like an envelop or box for a set of one or more submodules. Data is provided and consumed by submodules only.
   While standard CI_AddItem() and CI_AddItemCustom() function allows to plug one module with one sub-module into a certain slot only. To allow more flexibility, the extension api adds the following function:
   
   <code>
   typedef int32_t (CI_PnetAddItem_t)(uint16_t id,
                                            void *data_p,
                                            uint32_t bufSize,
                                            uint16_t slot,
                                            uint16_t subslot,
                                            uint16_t api);
         CI_PnetAddItem_t CI_PNET_Ext_AddItem_Func;                                         
   
   </code>
   Using CI_PNET_Ext_AddItem_Func allows an item to be plugged into a certain slot/subslot. In addition, a api number for the submodule can be set.
   • Modules with a predefined set of sub-modules 
   • Modules with free sub-slots and the ability plug sub-modules into a module at runtime
   • Allows to add submodules with a distinct api number
   The ability to set an api value other than the default api=0 allows implementation of Profinet profiles.
   The first four parameters of this call are identical to CI_AddItemCustom(), just subslot and api are added to the parameter list.
   
   == 7.1.5.4 Diagnosis and Alarms ==
   
   In Profinet there are ALRAMS and DIAGNOSIS available. Whats the difference? 
   Diagnosis provides status messages to the PLC. They are logged in the Engineering system and give the operator some inside on what's going on in the device. A diagnosis message can be activated and removed when no longer valid. Diagnosis messages are bound to a submodule and can be generated by the application and by the stack. The stack actually generates quite a few diagnosis messages. The user of the RapID platform has not to worry about maintaining those alarms and diagnosis messages. They are covered in the stack inside the NetworkApp.
   Alarms are disruptive events that are handled by the PLC and that may affect the plant operation. An alarm is sent upstream to the PLC and acknowledged by the PLC. Like with Diagnosis, source of an alarm may be the stack or the application. The user application shall not handle alarms that are dedicated to the stack.  
   The details of the how alarms and diagnosis messages are formatted are documented in IEC CD 61158-5-10 "Diagnosis ASE".
   
   ==== 7.2 Supported Diagnosis Types ====
   
   Please note that while QualifiedChannelDiagnosis is not supported yet, the function parameter _severity_ used in the diagnosis api in CI_extensions.h follows the required coding for QualifiedChannelQualifier for future compatibility.
   
   ^ Channel Diagnosis	^ Ext Channel Diagnosis	^ Qualified Channel Diagnosis	^ Manufacturer Specific Diagnosis
   |Slot Number	|Slot Number	|Slot Number	|Slot Number
   |SubSlot Number	|SubSlot Number	|SubSlot Number	|SubSlot Number
   |USI = 0x8000	|USI = 0x8002	|USI = 0x8003 	|USI = 0x0000-0x7FFF, Manfacturer Data
   |Channel Number	|Channel Number	|Channel Number	|Channel Number
   |Channel Type	|Channel Type	|Channel Type	|-
   |Channel Error Type	|Channel Error Type	|Channel Error Type	|-
   |-	|ExtChannelErrorType	|ExtChannelErrorType	|-
   |-	|ExtChannelAddValue	|ExtChannelAddValue	|-
   |-	|QualifiedChannelQualifer	|-	|-
   
   ==== 7.2.1 Addressing Model ==== 
   
   A diagnosis message is bound to an address based on api, slot, subslot and channel. While _api_, _slot_ and _subslot_ are common entities in Profinet, the _ChannelNumber_ is less prominent. The idea is that a submodule has one or more channels of a certain _ChannelType_. Examples: a digital input submodule with four inputs got four channels, one bit wide each. A analog output submodule with 8 channels uses a array of 8 16-bit words to represent its data. 
   
   Please note that ChannelType is a data width information only, not a datatype designation. A CI_pnetDiagChannelTypeDWord can be an 32-bit integer as well as an 32-bit float value. 
   
   The width of the channel is passed via the parameter ChannelType and defined as follows:
   
   ^ CI_pnetDiagChannelType_t	^ Channel Data Width in Bits	^ Example Use
   |CI_pnetDiagChannelTypeOthers	|Undefined	|-
   |CI_pnetDiagChannelType1Bit   	|Channel is a single bit wide	|Digital io          
   |CI_pnetDiagChannelType2Bit   	|Channel is two bits wide     	|-
   |CI_pnetDiagChannelType4Bit   	|Channel is 4 bits wide       	|-
   |CI_pnetDiagChannelTypeByte   	|Channel is 8 bits wide       	|-
   |CI_pnetDiagChannelTypeWord   	|Channel is 16-bits wide      	|Raw analog integer  
   |CI_pnetDiagChannelTypeDWord  	|Channel is 32-bits wide      	|Scaled analog float
   |CI_pnetDiagChannelTypeLWord  	|Channel is 64-bits wide      	|-
   
   Finally, a channel has a _direction_, its either input, output or both.
   
   ^Direction	^Comment |
   |CI_pnetInput	|input, data towards controller |  
   |CI_pnetOutput  |output, data from the controller|
   |CI_pnetIn_out  |input and output                 |
   
   ==== 7.2.2 Channel Error Code ==== 
   
   The error code defined in _CI_pnetDiagChannelError_t_ can be used to signal standard error codes as defined in IEC CD 61158-5-10 "Diagnosis ASE".
   The definition includes frequently used, self explanatory error codes, such as (list not complete): 
   
   <code>
         CI_pnetShortCircuit
         CI_pnetUndervoltage
         CI_pnetOvervoltage
         CI_pnetOverload
         CI_pnetOvertemperature
         CI_pnetLineBreak
         CI_pnetUpperLimitExceeded
         CI_pnetLowerLimitExceeded
         CI_pnetPowerFault
         CI_pnetFuseBlown
   </code>
   
   ==== 7.2.3 Severity ==== 
   
   All diagnosis calls in the extension api for Profinet support a parameter severity. The coding of this value follows the specification of QualifiedChannelQualifier.
   However, only 3 values can currently be used for severity:
   
   ^Severity Code	^Comment	^Severity
   |CI_PNET_S_LOW	|Lowest Severity	|Low|
   |CI_PNET_S_MAINTENANCEREQUIRED	|Error signals that maintenance is required	|Medium|
   |CI_PNET_S_MAINTENANCEDEMANDED	|Error signals that maintenance is demanded	|High|
   
   
   ==== 7.2.4 Stack Internal Reference(diagTag) ==== 
   
   The parameter lists of the diagnosis calls also refer to a parameter called _diagTag_. This tag is user supplied and shall be unique for each diagnosis sent. That said, the same value shall be used to send and to clear a diagnosis message, making diagTag an internal reference to a unique diagnosis transaction.  It helps the stack to track diagnosis messages for the same api, slot, subslot and channel.
   ==== 7.2.5 Channel Diagnostics ==== 
   
   Channel specific process diagnosis message. Channel diagnosis is used to signal process/application errors related to individual IO channels. 
   The channel is addressed by _api_, _slot_, _subslot_, _channelNumber_ and _channelType_. The _errorNumber_ is one of the predefined values in _CI_pnetDiagChannelType_t_. Please refer to the Profinet Diagnosis Guideline for the latest definitions.
   Channel type defines the width of the channel as per CI_pnetDiagChannelType_t. Typical examples are CI_pnetDiagChannelType1Bit for digital IO channels and CI_pnetDiagChannelTypeWord for analog input (16-Bit).
   The diagTag shall be unique to the message sent.
   
   <code>
         typedef int32_t CI_PnetSendChanDiag_t(uint16_t api,
                                               uint16_t slot,
                                               uint16_t subslot,
                                               uint16_t channelNumber,
                                               uint16_t channelType,
                                               uint16_t direction,
                                               uint16_t errorNum,
                                               uint16_t diagTag,
                                               uint32_t severity);
         CI_PnetSendChanDiag_t CI_PNET_Ext_SendChanDiag_Func;
   </code>
   
   ==== 7.2.6 Extended Channel Diagnostics ==== 
   
   Send an extended channel diagnosis message to the controller. Like channel diagnosis, extend channel diagnosis is used to signal process/application errors related to individual IO channels.
   The channel is addressed by _api_, _slot_, _subslot_, _channelNumber_ and _channelType_. The _errorNumber_ is one of the predefined values in _CI_pnetDiagChannelType_t_. Please refer to the Profinet Diagnosis Guideline for the latest definitions.
   Channel type defines the width of the channel as per CI_pnetDiagChannelType_t. Typical examples are CI_pnetDiagChannelType1Bit for digital IO channels and CI_pnetDiagChannelTypeWord for analog input (16-Bit).
   The extended information passed is used for specific use cases, where more error details are required. This includes nested errors, where an error is caused within  an existing error.
   
   <code>
   
         typedef int32_t CI_PnetSendExtChanDiag_t(uint16_t api,
                                                  uint16_t slot,
                                                  uint16_t subslot,
                                                  uint16_t channelNumber,
                                                  uint16_t channelType,
                                                  uint16_t direction,
                                                  uint16_t errorNum,
                                                  uint16_t diagTag,
                                                  uint32_t severity,
                                                  uint16_t extChannelErrType,
                                                  uint32_t extChannelAddValue);
         CI_PnetSendExtChanDiag_t CI_PNET_Ext_SendExtChanDiag_Func;
   
   </code>
   
   Pls refer to Profinet Diagnosis Guideline for details.
   ==== 7.2.7 Clear Channel Diagnosis ==== 
   Once the root cause for a channel diagnosis message or extended channel diagnosis message has vanished, use 
   
   <code>
                                                uint16_t slot,
                                                uint16_t subslot,
                                                uint16_t channelNumber,
                                                uint16_t channelType,
                                                uint16_t direction,
                                                uint16_t errorNum,
                                                uint16_t diagTag);
         CI_PnetClearChanDiag_t CI_PNET_Ext_ClearChanDiag_Func;
   </code>
   
   to inactivate the diagnosis message. The same _CI_PNET_Ext_ClearChanDiag_Func()_ function is used to deactivate both, Channel Diagnosis and Extended Channel Diagnosis messages.
   Parameter diagTag must be identical to the related CI_PNET_Ext_SendChanDiag_Func or CI_PNET_Ext_SendExtChanDiag_Func call.
   
   ==== 7.2.8 Qualified Channel Diagnosis ==== 
   
   This type is currently not supported_.
   ==== 7.2.9 Manufacturer Specific Diagnostics ==== 
   
   Issue manufacturer specific diagnosis message. Like with channel diagnosis, the error is addressed by api, slot, subslot, channelNumber and channelType.
   The diagTag shall be unique to the message sent.
   As the name suggest, this diagnosis can be use to raise non standard, customized diagnosis messages. Please note that no error code is given, the message uses a single, predefined error code (CI_pnetManufactureSpecific).
   The parameter usrStructureIdentifier allows to create a set of manufacturer specific messages, it's valid range is 0-0x7fff. 
   Please refer to Profinet Diagnosis Guideline for details.
   
   <code>
   typedef int32_t CI_PnetSendManDiag_t(uint16_t api,
                                              uint16_t slot,
                                              uint16_t subslot,
                                              uint16_t channelNumber,
                                              uint16_t channelType,
                                              uint16_t direction,
                                              uint16_t diagTag,
                                              uint16_t usrStructureIdentifier,
                                              uint32_t severity,
                                              uint8_t *manSpecificData_p,
                                              uint16_t dataLen);
         CI_PnetSendManDiag_t CI_PNET_Ext_SendManDiag_Func;
   
   </code>
   
   ==== 7.2.10 Alarms ==== 
   
   An alarm is a message that can trigger an interrupt on the controller. The behavior on the controller may be implementation depended. The classical way to handle interrupts is using OB40..48 blocks. Please refer op your PLC vendor documentation for implementing alarm driven interrupts.
   If an alarm is sent while a pending alarm has not been processed yet, the function returns CI_ERROR.
   
   
   === Appendix A Alarm Specifier===
   This value is for future compatibility and shall be set to zero for now.
   
   === Appendix B User Structure Identifier ===
   Like with manufacturer specific diagnosis, usrStructureIdentifier shall be in range of 0..0x7FFF. This value identifies reasons for the alarm and identifies what type of data is passed via alarmData_p. 
   
   === Appendix C Alarm Data ===
   Data can be passed along with an alarm. AlarmData_p points to the data and alamaDataLength gives the length of the data in bytes.
   
   <code>
         typedef int32_t CI_PnetSendAlarm_t(uint16_t api,
                                            uint16_t slot,
                                            uint16_t subslot,
                                            uint16_t alarmSpecifier,
                                            uint16_t diagTag,
                                            uint16_t usrStructureIdentifier,
                                            uint8_t *alarmData_p,
                                            uint16_t alarmDataLength);
         CI_PnetSendAlarm_t CI_PNET_Ext_SendAlarm_Func;
   </code>
   
   ==== 7.3 Validate Records====
   In CI, a event is sent to the application in case a record-item has has been read or updated. However, that is seen as too late to validate the record data and to possibly answer with a Profinet specific error code.
   Both validate callbacks shall not cause a context switch by calling inter process communication functions nor other CommonInterface functions. Stack usage shall be conservative.
   
   === 7.3.1 Read Record Validation ===
   The CI_PnetReadItemValidate_t callback allows a application to inspect whether data in the addressed item is valid or not before it is actually read by the stack. It may use the callback to update an out-of-date item using CI_WriteItem(). 
   If CI_ERROR is returned the read will be canceled and no data is read from the item. In this case, the application has to provide valid error information using the CI_PnetStatus_t structure.
   If the callback returns CI_OK, the data will be read from the respective item.
   _Note - it is allowed to pass NULL for this callback in CI_PnetCallbackFunctionTable_t if the use of this callback is not required_.
   
   <code>
         typedef int32_t (CI_PnetReadItemValidate_t)(int32_t handle,
                                                     uint32_t *rdLen_p,
                                                     CI_pnetStatus_t *pnioStatus_p);
   
   </code>
   
   === 7.3.2 Write Record Validation ===
   
   The writeItemValidate_p callback allows a application to inspect the data provided by buffer_p/wrLen for validity. If CI_ERROR is returned the write will be canceled and no data is written to the associated item. The application may capture a copy of the data using memcpy.
   In case of a error, the application has to provide valid error information using the CI_PnetStatus_t structure. 
   If the callback returns CI_OK, the data will be stored in the respective item.
   _Note - it is allowed to pass NULL for this callback in CI_PnetCallbackFunctionTable_t if the use of this callback is not required
   
   <code>
         typedef int32_t (CI_PnetWriteItemValidate_t)(int32_t handle,
                                                uint8_t *buffer_p,
                                                uint32_t *wrLen_p,
                                                CI_pnetStatus_t *pnioStatus_p);
   </code>
   
   === 7.3.3 finet Status – CI_PnetStatus_t ===
   
   The first four parameters represent the PNIO Status according to IEC61158-6
   The "addValue" values shall contain additional user information within negative responses. The value zero indicates no further information. For positive read responses, the a 1 in addValue1 shall indicate that the Record Data Object contains more data than have been read.
   
   <code>
         typedef struct {
           uint8_t   errorCode;
           uint8_t   errorDecode;
           uint8_t   errorCode1;
           uint8_t   errorCode2;
           uint16_t  addValue1;
           uint16_t  addValue2;
         } CI_pnetStatus_t;
   </code>
   
   ==== 7.4 Reading and Writing I&M Data====
   Profinet knows 5 I&M (Information and Maintenance) records. This implementation supports I&M 0 thru 4:
   ^I&M Record	^Content	^Use
   |IM0       	|Submodule manufacturer data, software and hardware version  	|Physical module properties|                                   
   |I&M1       	|Installation location and function tags                     	|Plant information where and what a modules does|        
   |I&M2       	|Installation data                                           	|Date of installation |                                        
   |I&M3       	|User defined descriptor                                     	|A 54 byte visible string for holding additional information  |
   |I&M4       	|Reserved for use by PROFIsafe                               	|PROFIsafe not supported currently |                           
   
   I&M0 is special for the device module and DAP/Port modules. These carry the device I&M0 data and can not be overwritten.
   For more information see [Profinet University][https://profinetuniversity.com/profinet-features/profinet-im-how-to-use-im-records]
   
   === 7.4.1 How to write I&M Data via Network ===
   
   Using TIA Portal [Siemens Support][https://support.industry.siemens.com/cs/mdm/49948856?c=86913163787&lc=en-WW] or use [Proneta][https://new.siemens.com/global/en/products/automation/industrial-communication/profinet/proneta.html] instead of TIA Portal.
   
   === 7.4.2 Read I&M Data Via Extension API ===
   
   Read one of the 5 I&M data records from the Profinet stack.
   The function works pretty straight forward, using just the address information as an input (api, slot, subslot). The selectIM value can be in range 0..4 to select the desired I&M record.
   _Please note that the user is not informed whether the PLC updates IM 1..4_
   
   <code>
         typedef int32_t (CI_PnetReadIMData_t)(uint16_t selectIM,
                                               uint16_t api,
                                               uint16_t slot,
                                               uint16_t subslot,
                                               uint8_t  *buffer_p,
                                               uint16_t bufLen);
         CI_PnetReadIMData_t CI_PNET_Ext_ReadIMData_Func;
   
   </code>
   
   === 7.4.3 Write I&M Data via Extension API === 
   
   Write one of the writeable I&M data records to the Profinet stack.
   The function works pretty straight forward, using just the address information as an input (api, slot, subslot). The selectIM value can be in range 0..4 to select the desired I&M record.
   Also note that IM0 is read only, with two exceptions:
   1. Exception: The value revCount
   For some profiles, it is required to update revCount. RefCount is updated for the given module at api/slot/subslot if a IM0 record is supported by the module. To write revCount via this api function, use a CI_PnetIM0Record_t struct and set revCount to the desired value. All other values in that struct are ignored.
   _Note: To update the device I&M0 revCount, use api=0, slot=0 and subslot=1;_ 
   2. Exception: If a sub-module does not have a I&M set already
   If a I&M0 record per submodule is desired, it can be attached using this function. However, once it is set future updates will not be successful - except for updating the revCount. Or more generally said, a IM0 record can not be overwritten once set.
   _Note: Reset to factory or unplugging will clear the I&M0 records of any but device/DAP/PORT submodule in Slot 0!_
   _Note: Reset to factory clears I&M records_
   
   <code>
         typedef int32_t (CI_PnetWriteIMData_t)(uint16_t selectIM,
                                                uint16_t api,
                                                uint16_t slot,
                                                uint16_t subslot,
                                                uint8_t *data_p,
                                                uint16_t dataLen);
         CI_PnetWriteIMData_t CI_PNET_Ext_WriteIMData_Func;
   
   </code>
   
   ===== 8. Revision History =====
   Below is a history of the revisions to the common interface users guide.
   
   ^ Revision Number   ^ Description of Changes   ^ Changes to Page Numbers ^Date of Changes
   |0	|Initial Release	|All        | 1/17/2023 |
   |1 	|Update of Initial Paragraph and CI PNET extensions	|XX-YY |10/23/2025   |
   
