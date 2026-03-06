Step 3. Customizing the Projec (Optional)
=========================================

With the CCES headless builder tool, we can modify the code and customize the project, such as link some codes/files into the projects, change project settings, modify the searching paths of the headerfiles, libraries or some other additional settings.

--------------

Creating links to Files
-----------------------

We can create some link files that are linked to any files or folders (usually source files, header files or configuration files) that reside in local file system.

+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name                              | Description                                                                                                                                                                                                                                                                                                                                      |
+==========================================+==================================================================================================================================================================================================================================================================================================================================================+
| -link [ ``Source'' ] [ ''Destination`` ] | ''**:math:`Source**'' specifies the file in the local file system that is going to be created link from.| | ::: |**''`\ Destination''** specifies where the link file should be created. It should be a relative path to the project base path. Destination is optional and if it's omitted, the link file will be created at project base path. |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example and Command Syntax:**

.. code:: batch

   ccesc.exe
       -nosplash
       -application com.analog.crosscore.headlesstools
       -data c:/workspace
       -project ./test
       -link c:/sources/test.c system/test_l.c 

--------------

Changing Tool Options for Projects
----------------------------------

The headless builder provides a couple of options used to append/remove/change tool switches of a project. Here are these options:

+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option Name                                   | Description                                                                                                                                               |
+===============================================+===========================================================================================================================================================+
| -cfg [ configName ][Optional]                 | If set, selects the configuration whose tool options to modify. Note: If not set, all configurations are affected.                                        |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| -append-switch [ toolname ] [ switch=value ]  | [Optional] Append value to a tool option. Whitespace is not allowed to be in the middle of the switch name. ( e.g. -D=MACRO1, additionaloption=OPTION1 ). |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| -remove-switch [ toolname ] [ switch=value ]  | [Optional] Remove a tool option. Whitespace is not allowed to be in the middle of the switch name. ( e.g. -D=MACRO1, additionaloption=OPTION1 ).          |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| -replace-switch [ toolname ] [ switch=value ] | [Optional] Replace a tool option value. Whitespace is not allowed to be in the middle of the switch name. ( e.g. -D=MACRO1, additionaloption=OPTION1 )    |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| -processor [ processorModel ]                 | [Optional] This option can be specified to change processor for a project                                                                                 |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| -revision [ siliconRevision ]                 | [Optional] This option can be specified to change silicon revision for a project                                                                          |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. code:: batch

   @SET project_path1="C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core1"
   @CALL ccesc.exe^
           -nosplash^
           -consoleLog^
           -application com.analog.crosscore.headlesstools^
           -data "c:/workspace"^
           -project %project_path1%^
           -append-switch compiler -I="\"${workspace_loc:/${ProjName}/src/%2%_Semaphore}\""

.. note::

   TO DO: add the examples


--------------

FreeRTOS Example
----------------

Now here is a simple example to modify the target SHARC Core 1 project created early, in which we create a task and set task to output the log every 5 seconds with vTaskDelayUntil().



.. raw:: html

   <details><summary>Click to expand</summary>

.. code:: c++

   /*****************************************************************************
     * 
     * FRTOS_Demo_SC589_Core1.c
    *
     * Copyright (C) 2019 Analog Devices Inc., All Rights Reserved.
    *
    *****************************************************************************/

   /* Standard includes. */
   #include <stdlib.h>
   #include <stdio.h>
   #include <sys/platform.h>
   #include <sys/adi_core.h>

   /* Kernel includes. */
   #include "FreeRTOSConfig.h"
   #include "FreeRTOS.h"
   #include "task.h"

   /* User application includes. */
   #include "adi_initialize.h"
   /*-----------------------------------------------------------*/

   #define userSTARTUP_STACK_SIZE              ( configMINIMAL_STACK_SIZE )
   #define userSTARTUP_TASK_PRIORITY           ( tskIDLE_PRIORITY + 2 )

   static void vUserStartupTask( void *pvParameters );
   static TaskHandle_t xStartupTaskHandle = NULL;
   /*-----------------------------------------------------------*/

   /* Perform an action every 5 seconds . */
   void vUserStartupTask( void *pvParameters )
   {
   TickType_t xLastWakeTime;
   const TickType_t xFrequency = ( ( TickType_t ) 5*1000 / portTICK_PERIOD_MS );
   BaseType_t xRound = 0;

       /* Initialize the xLastWakeTime variable with the current time.*/
       xLastWakeTime = xTaskGetTickCount();

       /*
        * Add user defined code for your first task here.
        * This function should never return.
        * When complete it should call vTaskDelete().
        */
       for ( ; ; )
       {
           /* Wait for the next cycle. */
           vTaskDelayUntil( &xLastWakeTime, xFrequency );

           /* Perform action here.*/
           printf("Task running round: %lu \r\n" , ++xRound );
       }
   }
   /*-----------------------------------------------------------*/

   int main()
   {
       /**
        * Initialize managed drivers and/or services that have been added to 
        * the project.
        * @return zero on success 
        */
       adi_initComponents();

       /* Begin adding your custom code here */

       /* When using FreeRTOS calls to SSL/DD cannot be made until the scheduler is active.
       To ensure that devices are initialized before tasks are started place your code
       in vApplicationDaemonTaskStartupHook() located in FreeRTOSHooks.c */

       /* Create a FreeRTOS task to run when the scheduler starts */
       BaseType_t xReturned;

       xReturned = xTaskCreate(
                   vUserStartupTask,           /* Task function implements */
                   "Startup Task",             /* Text name of the task */
                   userSTARTUP_STACK_SIZE,     /* Stack size in words, not bytes */
                   ( void * ) NULL,            /* Parameter passed into the task */
                   userSTARTUP_TASK_PRIORITY,  /* Task priority */
                   &xStartupTaskHandle );      /* Task's handle */

       if( xReturned != pdPASS )
       {
           printf("Creating Task Error: %s, %d \r\n", __func__, __LINE__);
           abort();
       }

       /* Start the scheduler. */
       vTaskStartScheduler();

       return 0;
   }
   /*-----------------------------------------------------------*/

.. raw:: html

   </details>


You can copy this code and replace the override the previous code of *C:\\freertos_command_line_examples\\cces_tools\\FRTOS_Demo_SC589_Core1\\src\\FRTOS_Demo_SC589_Core1.c* directly, or download this modified-attached file **FRTOS_Demo_SC589_Core1.c** into your local path and cover the original one.

**Example with batch command**

.. code:: batch

   @TITLE modify the code to the Project
   :: delet the FreeRTOSUserApplication.c and FreeRTOSUserApplication.h
   @SET original_file="C:\freertos_command_line_examples\cces_tools\FRTOS_Demo_SC589_Core1\src\FRTOS_Demo_SC589_Core1.c"
   @SET modified_file="C:\Users\sliu7\Downloads\FRTOS_Demo_SC589_Core1.c"
   :: Delete the original file of SHARC Core 1 Project
   del /f/s %original_file%
   ::  Copy the modified file to the target projcet
   echo F| XCOPY /k/i/y %modified_file% %original_file%
   @PAUSE

--------------

**HOME:** `Getting Started <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/tools/cces-tools/freertos-add-in-usage-with-cces-tools-from-command-line>`__ **PREV:** :doc:`Step 2. Adding the FreeRTOS Add-In </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/cces-tools/adding-the-freertos-add-in>` **NEXT:** :doc:`Step 4. Building the Projects </wiki-migration/resources/tools-software/freertos/freertos-addin/tools/cces-tools/building-the-projects>`

--------------
