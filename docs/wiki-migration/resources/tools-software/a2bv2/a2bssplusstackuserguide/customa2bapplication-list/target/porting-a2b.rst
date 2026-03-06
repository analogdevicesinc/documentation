:doc:`Click here to return to Building target software for a custom platform </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication-list/target>`

Porting A2B Software Stack to a custom platform
===============================================

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
----------------------------------

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
