ADSP-SC584 (Cortex-A Core) Benchmark Data
=========================================

ADSP-SC584 Cortex-A Core Performance Metrics
--------------------------------------------

**Processor and FreeRTOS Configuration:**

============== =============== ======================
Processor      Board Name      ``ADSP-SC584-EzKit``
============== =============== ======================
:::            Processor Type  ``Cortex-A5``
CUP Clock      Clock Frequency ''450,000,000 Hz ''
:::            Accuracy        ``2.2 nSec (1 cycle)``
RTOS Tick Rate Frequency       ``1000 Hz``
:::            Period          ``1 mSec``
:::            Cycles          ``450,000 Cycles``
\                              
============== =============== ======================

+--------------------------------------------------------------------+------------+
| **Flags**                                                          | **Cycles** |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag available)                               | 355        |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag unavailable, context switch to new task) | 838        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (no task pending, no context switch)            | 322        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (task waiting, context switch to pending task)  | 791        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (from an ISR, switching to a pending task)      | 3078       |
+--------------------------------------------------------------------+------------+
| \**Message Queues \*\*                                             |            |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message available)                                  | 192        |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message unavailable, context switch to new task)    | 1955       |
+--------------------------------------------------------------------+------------+
| xQueueSend (no task pending, no context switch)                    | 296        |
+--------------------------------------------------------------------+------------+
| xQueueSend (task waiting, context switch to pending task)          | 922        |
+--------------------------------------------------------------------+------------+
| xQueueSend (from an ISR, switching to a pending task)              | 645        |
+--------------------------------------------------------------------+------------+
| **Mutexes**                                                        |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex available)                                   | 293        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex unavailable, context switch to new task)     | 2519       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 325        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 1066       |
+--------------------------------------------------------------------+------------+
| **Semaphores**                                                     |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore available)                               | 250        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore unavailable, context switch to new task) | 2004       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 390        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 953        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (from an ISR, switching to a pending task)          | 663        |
+--------------------------------------------------------------------+------------+
| **Interrupt Service Time**                                         |            |
+--------------------------------------------------------------------+------------+
| Interrupt service time (FreeRTOS)                                  | 107        |
+--------------------------------------------------------------------+------------+
| Time to return from an ISR (FreeRTOS, no task switch)              | 30         |
+--------------------------------------------------------------------+------------+

--------------

ADSP-SC584 Cortex-A Core Sizing Metrics
---------------------------------------

All values in bytes.

=========================================== ======== ======== =========
**Test**                                    **Data** **Code** **Total**
Basic project                               146820   19664    166484
**Message Queues**                                            
Basic project using 1 static object         146820   19728    166548
Basic project using 2 static objects        146820   19728    166548
**Flags**                                                     
Basic project using 1 static object         146864   20512    167376
Basic project using 2 static objects        146864   20512    167376
**Mutexes**                                                   
Basic project using 1 static object         146820   19744    166564
Basic project using 2 static objects        146820   19744    166564
**Semaphores**                                                
Basic project using 1 static object         146820   19712    166532
Basic project using 2 static objects        146820   19712    166532
**Semaphore + Mutex + MessageQueue + Flag**                   
Basic project using 1 static object         146864   20700    167564
Basic project using 2 static objects        146864   20700    167564
=========================================== ======== ======== =========
