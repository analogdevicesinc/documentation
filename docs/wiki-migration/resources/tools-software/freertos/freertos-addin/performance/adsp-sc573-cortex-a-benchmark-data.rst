ADSP-SC573 (Cortex-A Core) Benchmark Data
=========================================

ADSP-SC573 Cortex-A Core Performance Metrics
--------------------------------------------

**Processor and FreeRTOS Configuration:**

============== =============== ======================
Processor      Board Name      ``ADSP-SC573-EzKit``
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
| xEventGroupWaitBits (flag available)                               | 338        |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag unavailable, context switch to new task) | 837        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (no task pending, no context switch)            | 324        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (task waiting, context switch to pending task)  | 786        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (from an ISR, switching to a pending task)      | 3021       |
+--------------------------------------------------------------------+------------+
| \**Message Queues \*\*                                             |            |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message available)                                  | 265        |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message unavailable, context switch to new task)    | 2042       |
+--------------------------------------------------------------------+------------+
| xQueueSend (no task pending, no context switch)                    | 300        |
+--------------------------------------------------------------------+------------+
| xQueueSend (task waiting, context switch to pending task)          | 1012       |
+--------------------------------------------------------------------+------------+
| xQueueSend (from an ISR, switching to a pending task)              | 673        |
+--------------------------------------------------------------------+------------+
| **Mutexes**                                                        |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex available)                                   | 290        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex unavailable, context switch to new task)     | 2554       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 323        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 1067       |
+--------------------------------------------------------------------+------------+
| **Semaphores**                                                     |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore available)                               | 252        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore unavailable, context switch to new task) | 2026       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 332        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 969        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (from an ISR, switching to a pending task)          | 668        |
+--------------------------------------------------------------------+------------+
| **Interrupt Service Time**                                         |            |
+--------------------------------------------------------------------+------------+
| Interrupt service time (FreeRTOS)                                  | 107        |
+--------------------------------------------------------------------+------------+
| Time to return from an ISR (FreeRTOS, no task switch)              | 33         |
+--------------------------------------------------------------------+------------+

--------------

ADSP-SC573 Cortex-A Core Sizing Metrics
---------------------------------------

All values in bytes.

=========================================== ======== ======== =========
**Test**                                    **Data** **Code** **Total**
Basic project                               146556   19648    166204
**Message Queues**                                            
Basic project using 1 static object         146556   19712    166268
Basic project using 2 static objects        146556   19712    166268
**Flags**                                                     
Basic project using 1 static object         146600   20504    167104
Basic project using 2 static objects        146600   20504    167104
**Mutexes**                                                   
Basic project using 1 static object         146556   19728    166284
Basic project using 2 static objects        146556   19728    166284
**Semaphores**                                                
Basic project using 1 static object         146556   19696    166252
Basic project using 2 static objects        146556   19696    166252
**Semaphore + Mutex + MessageQueue + Flag**                   
Basic project using 1 static object         146600   20680    167280
Basic project using 2 static objects        146600   20680    167280
=========================================== ======== ======== =========
