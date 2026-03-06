Running the Examples on the ADuCM302x EZ-Kit
============================================

The FreeRTOS product for Analog Devices processors contains the following examples:

+-----------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Processor | Toolchain                 | Example(s)                                                                                                                       |
+===========+===========================+==================================================================================================================================+
| ADuCM3029 | IAR Embedded Workbench    | :doc:`Basic Demo </wiki-migration/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm302x-ez-kit/iar>`      |
+-----------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ADuCM3029 | Keil MDK                  | :doc:`Basic Demo </wiki-migration/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm302x-ez-kit/keil-mdk>` |
+-----------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ADuCM3029 | CrossCore Embedded Studio | :doc:`Basic Demo </wiki-migration/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm302x-ez-kit/cces>`     |
+-----------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------+

The basic demo example is based on the **Standard Demo Tasks** that FreeRTOS recommend are provided for each port of the FreeRTOS Operating System.

For more information on the Standard Demo Tasks please refer to http://www.freertos.org/a00013.html.

The tasks performed in the Analog Devices Basic Demo include:

-  LED flash
-  Polled queue tasks
-  Recursive Mutex tasks
-  Blocking Queue tasks
-  Statically allocated tasks
-  Suicidal tasks
