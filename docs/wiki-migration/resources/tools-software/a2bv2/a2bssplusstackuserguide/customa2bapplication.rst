Building an A2B Application on a custom platform
================================================

| :doc:`Click here to return to the A2B SSPLUS STACK USER GUIDE </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>`
| Building an A2B application on a custom platform involves two major steps

-  **Step-1 (Concept)**: Designing A2B schematic on SigmaStudioPlus.
-  **Step-2 (System Implementation)**: Building Target software for the custom platform.

Designing A2B Schematic on SigmaStudioPlus
------------------------------------------

This step is required to create a bus configuration file that stores the complete A2B network information required by the Target software running on the custom platform. An A2B schematic, corresponding to the Targeted application shall be designed and validated on SigmaStudioPlus before exporting the bus configuration file. The steps involved in this process are as follows

1. Build an A2B Schematic on SigmaStudioPlus matching your final A2B system

-  Refer :doc:`Drawing A2B Schematics </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/drawinga2bschematics>` for drawing an A2B schematic on SigmaStudioPlus. Ensure

   -  Audio streams are defined and assigned for the network.
   -  Configuration is provided for all A2B nodes and connected peripheral devices.

2. Validate the A2B Schematic using the PC as the host processor

-  Refer to the example in :doc:`Running the Sample Demo </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` to discover an A2B network using a PC as a Host
-  Link-compile-download and confirm successful network discovery, configuration, and audio routing.
-  Debug discovery issues (if any) using ‘Tracing’, ‘Sequence Chart’, and other features.

3. Perform Network analysis to ensure the drawn schematic matches the requirements of the end system

-  Check for Bandwidth usage per Node/Network.
-  Run Bit error Test for the network.
-  Check Power usage for the network.

4. Define application response to line faults (if required)

-  Auto-rediscovery upon faults, no. of attempts, etc.
-  Verify line fault handling/rediscovery upon line faults.

5. After successful validation, export **Bus Configuration.C** file for the validated A2B schematic.

6. Bus configuration file can also be exported as a binary file using the “\ **Dump as .dat**\ ” option.

NOTE
~~~~

MACROS to enable/disable based on the type of file used for configuration of the A2B Network.


|image1|

.. container:: centeralign

   \ **Table:** MACRO Information


Building Target software for a custom platform
----------------------------------------------

The next step is to build Target software for a custom platform that hosts the A2B stack and the application. The A2B stack is responsible for discovering and configuring the A2B network as per the configuration provided and handling any run-time events/faults. The subsequent sections describe the steps involved in porting the Stack. It may be necessary to implement additional responsibilities in the Target software depending on the end-system requirements which is beyond the scope of this document.

The best way of building Target software for a custom platform is to port a matching demo project (available in the A2B Software package under.\\Target). The below :doc:`figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>` shows Target software examples on different ADI platforms available within the software package.

A2B Target Software Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image2|

.. container:: centeralign

   \ **Figure: A2B Target Software Examples**\


The below table (Target Example Projects) provides A2B controller, and audio host details for each example. Refer to :doc:`Running the Sample Demo </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` to run the example

Target Example Projects
^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------+-------------------------------------------------+-----------------+----------------+
| Example Project Name  | Platform                                        | A2B Controller  | Audio Host     |
+=======================+=================================================+=================+================+
| a2bapp-bf             | SDP-B + EVAL-AD242xWDZ,SDP-B + EVAL-AD2433WA1BZ | BF527           | ADAU1452       |
+-----------------------+-------------------------------------------------+-----------------+----------------+
| a2bapp-adsp-sc58x     | ADSP-SC584 Ez Kit                               | ARM A5 (Core 0) | SHARC (Core 1) |
+-----------------------+-------------------------------------------------+-----------------+----------------+
| a2bstack-frmwrk-sc59x | EV-SOMCRR-EZKIT, EV-SC594-SOM                   | ARM A5(Core0)   | SHARC (Core 1) |
+-----------------------+-------------------------------------------------+-----------------+----------------+
| a2bapp-linux          | ADSP-SC584 Ez Kit                               | ARM A5 (Core 0) | SHARC (Core 1) |
+-----------------------+-------------------------------------------------+-----------------+----------------+

All Target example projects provided in the A2B Software package have a similar directory structure as shown in the below :doc:`figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>`. The figure also shows the folders that constitute the core A2B “Stack” and “Application” files. When porting Stack onto a custom platform, modifications are required only for the files under the ‘a2bstack-pal’ and ‘Application’ folders while the rest shall be moved as-is.

A2B Target Project Directory Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/a2btargetprojectdira2bplus.jpg
   :align: center

-  a2bstack

   -  The generic or target agnostic portions of the A2B Stack. Holds a scheduler designed to efficiently coordinate network activities, especially during the discovery and configuration phase, and execute units of work encapsulated in messages and jobs.

-  a2bplugin-master

   -  The sources for the A2B Stack master node plugin. The A2B network discovery algorithms and line fault diagnostics are encapsulated within these sources.

-  a2bplugin-slave

   -  The sources for simple A2B stack slave node plugin. These sources are a simple example of a slave plug-in for use as a launching pad for developing custom plugins.

-  a2bstack-pal

   -  The platform adaptation layer (PAL) for the A2B Software Stack.

-  a2bstack-protobuf

   -  The source code for parsing the A2B Bus Configuration File (BCF) from the ADI SigmaStudioPlus tool.
   -  Source code for parsing and decoding Google Protobuf (Nanopb) encoded A2B configuration file generated by Host Tool.

The steps involved in porting the A2B stack and defining application response to A2B events/faults are as follows

-  :doc:`Porting A2B Software Stack to a custom platform </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>`
-  :doc:`Apply A2B System Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>`
-  :doc:`Modify the application callback code </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>` (if necessary)

\_

Porting A2B Software Stack to a custom platform
-----------------------------------------------

The step-by-step approach in porting the A2B stack onto a custom platform is as follows

-  Copy all files from folders **a2bplugin-master**, **a2bplugin-slave**, **a2bstack**, **a2bstack-protobuf**, **a2bstack-pal**, **app**, **inc** of demo software to corresponding folders of your target platform project “as-is”.
-  2. Re-Implement **adi_a2b_SystemInit()** in **main()** to perform Target platform-specific initializations as required.

   -  Replace ADI platform-specific Board Support Package (BSP) with Target platform BSP.
   -  Ensure to generate and provide Bit Clock and SYNC signals for the master A2B Transceiver chip.
   -  Define the stack and heap memory for the Target platform project using the options provided by your development environment (IDE).

      -  4K stack and 5K heap are the typical requirements. If the number of nodes in the system is fixed, then memory can be statically allocated instead of using the Heap.

         -  Enabling the macro A2B_APP_STATIC_MEMORY_FOR_STACK, makes use of static memory allocation instead of dynamic memory allocation as preferred by many automotive customers (set to typical values with margin in .\\Target\\examples\\demo\\app-plugin\\src\\a2bapp.c)
         -  Stack memory - A2BAPP_STACK_NW_MEMORY (TBD bytes)
         -  Plugin memory - A2BAPP_PLUGIN_NW_MEMORY (TBD bytes)
         -  BCF File/EEPROM buffer (optional) - A2BAPP_E2PROM_BLOCK_MEMORY (TBD bytes)

3. Optionally, configure A2B Stack for the Target platform by modifying necessary macros in

-  “features.h” in **Target/examples/demo/<a2b-xx>>/a2bstack-pal/platform/a2b/**
-  “conf.h” in **Target/examples/demo/<a2b-xx>>/a2bstack-pal/platform/a2b/**

4. Re-implement PAL functions in the file **a2bstack-pal\\adi_a2b_pal.c**

-  This would require implementing drivers (I2C, SPI, Timers, SPORT etc) specific to the Target platform under the **a2bstack-pal** folder. The list of PAL functions to be re-implemented is listed in Table (PAL Functions to be Re-implemented).
-  Refer to the implementation in the Example projects provided within the software package.
-  Each re-implemented function shall be unit tested to confirm that it is working as per the function description before going to the next step.

In the table below, those functions marked as “Mandatory” must be implemented to have a minimally functional Stack. The remaining functions provide developers with convenient points in the Stack operation to ensure portability to a wide array of platforms.

PAL Functions to be Re-implemented
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I2C Functions
~~~~~~~~~~~~~

+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PAL Function                              | Mandatory            | Description                                                                                                                                                                                       |
+===========================================+======================+===================================================================================================================================================================================================+
| <fc #6495ed>a2b_pal_I2cInit</fc>          | No                   | This routine is called to do the initialization required by the I2C subsystem.                                                                                                                    |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_I2cOpenFunc</fc>      | <fc #008000>Yes</fc> | This routine is called to do post-initialization of the I2C subsystem during the Stack allocation process. This routine is called immediately following a successful call to the pal_i2cInitFunc. |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_I2cCloseFunc</fc>     | No                   | This routine is called to de-initialize the I2C subsystem.                                                                                                                                        |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_I2cReadFunc</fc>      | No                   | This routine reads bytes from an I2C device.                                                                                                                                                      |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_I2cWriteFunc</fc>     | <fc #008000>Yes</fc> | This routine writes bytes to an I2C device.                                                                                                                                                       |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_I2cWriteReadFunc</fc> | <fc #008000>Yes</fc> | This routine performs an atomic repeated start I2C write/read transaction to an I2C device.                                                                                                       |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_I2cShutdownFunc</fc>  | No                   | This routine is called to shut down the I2C subsystem.                                                                                                                                            |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

SPI Functions
~~~~~~~~~~~~~

+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PAL Function                              | Mandatory            | Description                                                                                                                                                                                       |
+===========================================+======================+===================================================================================================================================================================================================+
| <fc #6495ed>a2b_pal_SpiInit</fc>          | No                   | This routine is called to do the initialization required by the SPI subsystem.                                                                                                                    |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_SPiOpenFunc</fc>      | <fc #008000>Yes</fc> | This routine is called to do post initialization of the SPI subsystem during the Stack allocation process. This routine is called immediately following a successful call to the pal_i2cInitFunc. |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_SpiCloseFunc</fc>     | No                   | This routine is called to de-initialize the SPI subsystem.                                                                                                                                        |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_SpiWriteFunc</fc>     | <fc #008000>Yes</fc> | This routine writes bytes to an SPI device on MOSI                                                                                                                                                |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_SpiWriteReadFunc</fc> | <fc #008000>Yes</fc> | This routine performs write on MOSI and reads data on MISO. Note that this function considers only the read data followed by the write completion.                                                |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_SpiShutdownFunc</fc>  | No                   | This routine is called to shut down the SPI subsystem.                                                                                                                                            |
+-------------------------------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Timer Functions
~~~~~~~~~~~~~~~

+----------------------------------------------+----------------------+------------------------------------------------------------------------------------------------------------------+
| PAL Function                                 | Mandatory            | Description                                                                                                      |
+==============================================+======================+==================================================================================================================+
| <fc #6495ed>a2b_pal_TimerInitFunc</fc>       | No                   | This routine is called to do initialization the timer                                                            |
+----------------------------------------------+----------------------+------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_TimerGetSysTimeFunc</fc> | <fc #008000>Yes</fc> | This routine returns the current "system" time in milliseconds. The underlying system time is platform-specific. |
+----------------------------------------------+----------------------+------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_TimerShutdownFunc</fc>   | No                   | This routine is called to shut down the timer subsystem during the Stack destroy process.                        |
+----------------------------------------------+----------------------+------------------------------------------------------------------------------------------------------------------+

Audio Functions
~~~~~~~~~~~~~~~

+--------------------------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PAL Function                               | Mandatory | Description                                                                                                                                                                                                                                                                                                                    |
+============================================+===========+================================================================================================================================================================================================================================================================================================================================+
| <fc #6495ed>a2b_pal_AudioInitFunc</fc>     | No        | This routine is called to do initialization the audio subsystem during the Stack allocation process.                                                                                                                                                                                                                           |
+--------------------------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_AudioOpenFunc</fc>     | No        | This routine is called to do post-initialization of the audio subsystem during the Stack allocation process. This routine is called immediately after a successful call to the pal_audioInitFunc                                                                                                                               |
+--------------------------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_AudioCloseFunc</fc>    | No        | This routine is called to de-initialization the audio subsystem during the Stack destroy process.                                                                                                                                                                                                                              |
+--------------------------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_AudioConfigFunc</fc>   | No        | This routine is called to configure the audio subsystem master node during the discovery process. This routine is called during the "NetComplete" process after all nodes are discovered and before the master node "NodeComplete" process which fully initializes the master A2B registers and starts the up/downstream flow. |
+--------------------------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #6495ed>a2b_pal_AudioShutdownFunc</fc> | No        | This routine is called to shut down the audio subsystem during the Stack destroy process. This routine is called immediately after a successful call to the pal_audioCloseFunc.                                                                                                                                                |
+--------------------------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Memory Functions
~~~~~~~~~~~~~~~~

.. note::

   Only when A2B_FEATURE_MEMORY_MANAGER is disabled in features.h


+--------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PAL Function             | Mandatory | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+==========================+===========+=========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| a2b_pal_MemMgrInitFunc   | No        | This routine is called to do the initialization required by the memory manager service during the Stack allocation process. A PAL implementation has the option of implementing their own (or custom) memory allocation strategy. Another option is to leverage the built-in memory manager feature of the generic Stack if A2B_FEATURE_MEMORY_MANAGER is defined. This manager allocates memory blocks from a fixed-size heap whose size is derived in part from settings in ‘conf.h’. |
+--------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_MemMgrOpenFunc   | No        | This routine opens a memory-managed heap located at the specified address and of the specified size.If the Stack's heap cannot be opened and managed at the specified location (perhaps because the size is insufficient) then the returned handle will be A2B_NULL.                                                                                                                                                                                                                    |
+--------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_MemMgrMallocFunc | Yes       | This routine is called to allocate a fixed amount of memory. Only needed if A2B_FEATURE_MEMORY_MANAGER is disabled.                                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_MemMgrFreeFunc   | Yes       | This routine is called to free previously allocated memory. Only needed if A2B_FEATURE_MEMORY_MANAGER is disabled.                                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_MemMgrCloseFunc  | No        | This routine is called to de-initialization the memory management subsystem during the Stack destroy process. All resources associated with the heap are freed.                                                                                                                                                                                                                                                                                                                         |
+--------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_MemMgrShutdown   | No        | This routine is called to shut down the memory manager subsystem during the Stack destroy process. This routine is called immediately after a successful call to the pal_memMgrCloseFunc.                                                                                                                                                                                                                                                                                               |
+--------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Logging Functions
~~~~~~~~~~~~~~~~~

.. note::

   Only when A2B_FEATURE_SEQ_CHART or A2B_FEATURE_TRACE is enabled in features.h


+-------------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PAL Function            | Mandatory | Description                                                                                                                                                                |
+=========================+===========+============================================================================================================================================================================+
| a2b_pal_LogInitFunc     | No        | This routine is called to do the initialization of the log subsystem during the Stack allocation process.                                                                  |
+-------------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_LogOpenFunc     | No        | This routine opens a log channel.                                                                                                                                          |
+-------------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_LogCloseFunc    | No        | This routine closes a log channel.                                                                                                                                         |
+-------------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_LogWriteFunc    | No        | This routine writes to a log channel.                                                                                                                                      |
+-------------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_LogShutdownFunc | No        | This routine is called to shut down the log subsystem during the Stack destroy process. This routine is called immediately after a successful call to the pal_logCloseFunc |
+-------------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Plugin Functions
~~~~~~~~~~~~~~~~

.. note::

   Generally not required to be modified. Default implementation should suffice


+---------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------+
| PAL Function              | Mandatory | Description                                                                                                                       |
+===========================+===========+===================================================================================================================================+
| a2b_pal_PluginsLoadFunc   | No        | This routine returns a list of all available plugins. The plugins returned are queried during discovery as slave nodes are found. |
+---------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_PluginsUnloadFunc | No        | This routine is called to unload previously loaded plugins from pal_pluginsLoad.                                                  |
+---------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_PalGetVersionFunc | No        | This routine returns version information related to the PAL.                                                                      |
+---------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------+
| a2b_pal_PalGetBuildFunc   | No        | This routine returns build information related to the PAL.                                                                        |
+---------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------+

File Read Functions
~~~~~~~~~~~~~~~~~~~

.. note::

   Only when A2B_BCF_FROM_FILE_IO is enabled in features.h


+-------------------+-----------+----------------------------------------------------------------------------------------------------+
| PAL Function      | Mandatory | Description                                                                                        |
+===================+===========+====================================================================================================+
| a2b_pal_FileOpen  | No        | This routine opens the binary file in read mode and shall be modified as per the file system used. |
+-------------------+-----------+----------------------------------------------------------------------------------------------------+
| a2b_pal_FileRead  | No        | This routine reads the binary file and shall be modified as per the file system used.              |
+-------------------+-----------+----------------------------------------------------------------------------------------------------+
| a2b_pal_FileClose | No        | This routine closes the binary file.                                                               |
+-------------------+-----------+----------------------------------------------------------------------------------------------------+

Apply A2B Network configuration
===============================

After completing all steps as mentioned in Section "**Porting A2B Software Stack to a custom platform**", the next step is to apply bus configuration to the Target software.

1. In the Target platform project, include the validated bus configuration file (**adi_a2b_busconfig.c**), exported by following Section ":doc:`Designing A2B Schematic on SigmaStudioPlus </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>`".

-  Replace the existing in **.\\Target\\a2bstack\\demo\\<a2b-xx>\\app.**

2. Optionally, if the bus configuration is read from a binary file, replace the exported .dat format of the bus configuration file into the file system path (A2B_CONF_BINARY_BCF_FILE_URL).

3. Optionally, the audio routing table (.\\app\\adi_a2b_audioroutingtable.c) may need to be modified if the audio streams are to be routed by the audio host.

-  In case where the A2B controller is also the audio host for the network then modify the audio routing table as explained in :doc:`System Requirements </wiki-migration/resources/tools-software/a2bv2/quickstartguide/systemrequirements>`. Otherwise, the routing has to be modified in the audio host. :doc:`Running the Sample Demo </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` explains this process when using ADAU1452 as an audio host on ADI A2B evaluation boards such as EVAL-AD2425WDZ and EVAL-AD2428WD1BZ.

.. note::

   This step is not required if stream definition and the routing is defined in SigmaStudioPlus where streams are sourced and consumed within A2B nodes and not routed by the Audio Host.


4. Build and Run the Target project.

-  Use the build/flash tools provided by your development environment (IDE) to build and run the executable image.
-  A2B Network should get discovered and configured as per the added bus configuration file. Refer to Section ":doc:`Post-Discovery APIs </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/applicationintegration>`" for Debugging help.

Modify Application Call-back Functions
======================================

By this time, we should have completed the porting of A2B Stack as explained in Section ":doc:`Porting A2B Software Stack to a custom platform </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>`". At this stage, the A2B Stack ported on the custom platform should be capable of discovering and configuring a connected A2B network as per the added bus configuration file.

The A2B Stack offers provision for the application running on the Target software to register callback functions for important network activities. Three important application callback functions are registered with the Stack. These functions can be modified by the user to perform an action specific to the application.

.. note::

   All examples provided in the A2B Software package come with default implementations for these callback functions. Modifications to these functions are required only if the default implementation doesn’t match your targeted system requirement. When requiring additional functionality, it is recommended to add on top of the existing implementation unless rewriting completely.


The three application callback functions are explained in the following sub-sections.

Discovery completion Callback function
--------------------------------------

The discovery completion callback function is invoked by the stack upon completing the discovery and configuration of the whole A2B network. :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>` shows the application registration of a discovery completion callback function with the stack. The status of the discovery is notified by this function allowing the application to perform any additional tasks based on the notified status.


|image3|

.. container:: centeralign

   \ **Figure: A2BAPP OnDiscoveryComplete Callback Function**\


.. note::

   a2bapp_onDiscoveryComplete() comes with a default implementation for post-discovery bus drop monitoring and rediscovery upon faults (if it was set in SigmaStudioPlus while exporting the bus configuration file). Modify this function only to override default functionality (if required).


The code snippet shows a sample implementation of this callback function.

::

   a2bapp_onDiscoveryComplete
       (
       struct a2b_Msg* msg;
       a2b_Bool isCancelled;
       )
   {
       a2b_NetDiscovery* results;
       a2b_Bool* discDone;

       if ( A2B_NULL == msg )
       {
   #ifdef A2B_PRINT_CONSOLE
           /* This should "never" happen */
           fprintf(stderr, "Error: no response message for network discovery\n");
   #endif
       }
       else
       {
           discDone = a2b_msgGetUserData(msg);

           if ( isCancelled )
           {
   #ifdef A2B_PRINT_CONSOLE
               fprintf(stderr, "Discovery request was cancelled.\n");
   #endif
           }
           else
           {
               results = (a2b_NetDiscovery*)a2b_msgGetPayload(msg);
               if ( A2B_SUCCEEDED(results->resp.status) )
               {
                   printf("Discovery succeeded with %d nodes discovered\n", 
                          results->resp.numNodes);
                   gNumSlaveNodes = results->resp.numNodes;
               }
               else
               {
   #ifdef A2B_PRINT_CONSOLE
                   fprintf(stderr, "Discovery failed!\n");
   #endif
               }
           }
           /* Force the main loop to exit */
           *discDone = A2B_TRUE;
       }
   }

Power/Line Fault Callback function
----------------------------------

The power fault callback function is invoked by the stack upon detecting a power-related fault in any node of the network. An application callback function can be registered with the Stack for power fault notifications as shown in the below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>`.


|image4|

.. container:: centeralign

   \ **Figure: A2BAPP OnPowerFault Callback Function**\


The Stack provides a callback function to the application layer upon the occurrence of a fault in the A2B System. The stack performs necessary diagnostics and fault localization (in case of concealed faults) and reports the fault type and location to the application for further handling.

.. note::

   The Stack performs all necessary actions to handle the fault as recommended by the A2B Transceiver Programmer’s reference manual and finally invokes the application callback.


The function is invoked under the following fault conditions during and post discovery.

-  Critical faults

   -  Cable terminal shorted to GND
   -  Cable terminal shorted to VBat

-  Non-Critical faults

   -  Cable terminals shorted together
   -  Cable disconnected or open circuit
   -  Cable is reversely connected

-  Indeterminate faults
-  Bus/Node drop condition

Code Snippet shows a sample implementation of the a2bapp_onPowerFault callback function.

::

   a2bapp_onPowerFault (struct a2b_Msg *msg, a2b_Handle userData)
   {
       A2B_UNUSED(userData);
       a2b_PowerFault *fault;
       const char *faultString;

       if ( msg )
       {
           fault = (a2b_PowerFault *)a2b_msgGetPayload(msg);
           if ( fault )
           {
               if ( A2B_SUCCEEDED(fault->status) )
               {
                   switch (fault->intrType)
                   {
                       case A2B_ENUM_INTTYPE_PWRERR_CS_GND:
                           faultString = "Cable Shorted to GND";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_CS_VBAT:
                           faultString = "Cable Shorted to VBat";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_CS:
                           faultString = "Cable Shorted Together";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_CDISC:
                           faultString = "Cable Disconnected or Open Circuit";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_CREV:
                           faultString = "Cable Reverse Connected or Wrong Port";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_FAULT:
                           faultString = "Indeterminate Fault";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_NLS_GND:
                           faultString = "Non-Localized Short to GND";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_NLS_VBAT:
                           faultString = "Non-Localized Short to VBat";
                           /* Add your code to handle fault */
                           break;
                       default:
                           faultString = "Unknown";
                           /* Add your code to handle fault */
                           break;
                   }
                   gAPP_Info.faultNode = fault->faultNode;
               }
           }
       }
   }

The information about the presence of a locally powered slave is made known to the stack through the BDD. In case of critical faults (Cable terminal shorted to GND, Cable terminal shorted to VBat), the stack switches of the bus from the immediate upstream local powered slave onwards.

Partial bus operation is possible between master and this upstream local powered slave.

Interrupt Callback function
---------------------------

The Interrupt callback function is invoked by the Stack upon seeing any interrupts at the master node. The below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>` shows the application registration of an interrupt callback function with the Stack.


|image5|

.. container:: centeralign

   \ **Figure: Interrupt Callback Function**\


The code snippet shows a simple implementation of this callback function.

::

   static void a2bapp_onInterrupt(struct a2b_Msg* msg, a2b_Handle userData)
   {
       a2b_Interrupt* interrupt;

       A2B_UNUSED(userData);

       if (msg)
       {
           interrupt = a2b_msgGetPayload(msg);
           if (gDebug)
           {
               if (interrupt)
               {
   #ifdef A2B_PRINT_CONSOLE
                   printf("INTERRUPT: intrType=%u nodeAddr=%d\n",
                          interrupt->intrType, interrupt->nodeAddr);
   #endif
                   /* Add your code to handle interrupt */
               }
               else
               {
   #ifdef A2B_PRINT_CONSOLE
                   fprintf(stderr, "INTERRUPT: failed to retrieve payload\n");
   #endif
               }
           }
       }
   }

.. note::

   Any interrupt on the slave node can be handled within a2bplugin_slave\\ a2bslave_plugin.c file in the function a2b_pluginInterrupt as explained in "Handling Interrupts in a Plugin" in :doc:`applicationintegration </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/applicationintegration>`


Node Discovery Callback function
--------------------------------

The node discovery callback function is an optional callback, which is invoked by the stack upon each node discovery or when node authentication fails. The below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>` shows the application registration of this callback function with the Stack.


|image6|

.. container:: centeralign

   \ **Figure: Node Discovery Callback Function**\


The below Code Snippet shows a sample implementation of this callback function. The application can decide whether to continue with discovery or not and has more control with this callback function.

::

   static void a2bapp_onNodeDiscovery(struct a2b_Msg* msg, a2b_Handle userData)
   {
   #ifdef A2BAPP_ENABLE_RTMBOOT
       a2b_HResult                 nRes;
       a2b_App_t *pApp_Info        =   userData;
   #endif
       a2b_Nodedscvry* dscvrdNodeMsg;

   #ifdef A2B_PRINT_CONSOLE
       a2b_Int16 nodeAddr;
       bdd_Node *bddnode;
       bdd_Network *bddNetwork;
   #endif

   #ifndef A2BAPP_ENABLE_RTMBOOT
       A2B_UNUSED(userData);
   #endif

       if (msg)
       {
           /* details of the currently discovered node */
           dscvrdNodeMsg = a2b_msgGetPayload(msg);

   #ifdef A2B_PRINT_CONSOLE
           nodeAddr = dscvrdNodeMsg->nodeAddr; //this will number of slave node discovered
           bddNetwork = (bdd_Network *)dscvrdNodeMsg->bddNetObj;
           bddnode = (bdd_Node *)(&bddNetwork->nodes[nodeAddr]);
   #endif
           if (dscvrdNodeMsg)
           {
   #ifdef A2BAPP_ENABLE_RTMBOOT
               if(dscvrdNodeMsg->nodeAddr == (A2BAPP_RTM_NODEADDR + 1U))
               {
                   /* Call to boot the RTM Module */
                   nRes = a2bapp_RTMBoot(pApp_Info->ctx, A2BAPP_RTM_NODEADDR);
                   if (A2B_FAILED(nRes))
                   {
                       A2B_APP_LOG("NODE DISCOVERY: failed to boot RTM\n\r");
                   }
               }
   #endif
               A2B_APP_LOG("NODE DISCOVERY: nodeType=%u nodeAddr=%d discoveryCompleteCode=%u\n\r", bddnode->nodeType, nodeAddr, dscvrdNodeMsg->discoveryCompleteCode);

   #ifndef ENABLE_SUPERBCF
               /* CRITICAL: Populate the further action which is required to be taken by stack
                * Set,
                *      bContinueDisc to true if required to proceed with discovery process
                *      bContinueDisc to false if required to end the discovery process
                */
               dscvrdNodeMsg->bContinueDisc = A2B_TRUE;
   #endif  /* ENABLE_SUPERBCF */
           }
           else
           {
               A2B_APP_LOG("NODE DISCOVERY: failed to retrieve payload\n\r");
           }
       }
   }

I2C Error Callback Function
---------------------------

The I2C error callback function is invoked by the Stack upon seeing any I2C errors at the master node or at sub-node peripherals.


|image7|

.. container:: centeralign

   \ **Figure: I2C Error Callback Function**\


The code snippet shows a simple implementation of this callback function.

::

   static void a2bapp_onI2CError(struct a2b_Msg *msg, a2b_Handle userData)
   {
       a2b_I2CError *I2CError;
       A2B_UNUSED(userData);
       a2b_App_t *gApp_Info;

       I2CError = (a2b_I2CError *)a2b_msgGetPayload(msg);

       gApp_Info->bfaultDone = A2B_TRUE;
       gApp_Info->bRetry = A2B_TRUE;
       if(I2CError->nodeAddr == A2B_NODEADDR_MASTER)
       {
           A2B_APP_LOG("\n\Incorrect I2C address at main node\n\r");
       }
       else
       {
           A2B_APP_LOG("\n\rPeripheral configuration failed with I2C address 0x%x on node %d\n\r", I2CError->I2CAddr, I2CError->nodeAddr);
       }
   }

| 
| ==== Summary of Building A2B Application on Custom Platform ==== Figure: Building A2B Application on a Custom Platform |image8|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/macros_stack.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/a2btargetsoftwareexamplesa2bplus.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/a2bapp_ondiscoverycomplete_callback_function.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/a2bapp_onpowerfault_callback_registration.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/interrupt_callback_function.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/node_discovery_callback_function.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/i2c_error_callback_function.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/buildinga2bapplicationsoncustomplatform.jpg
