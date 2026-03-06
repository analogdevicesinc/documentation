ADSP-SC589 (Cortex-A Core) Benchmark Data
=========================================

ADSP-SC589 Cortex-A Core Performance Metrics
--------------------------------------------

**Processor and FreeRTOS Configuration:**

============== =============== ======================
Processor      Board Name      ``ADSP-SC589-EzKit``
============== =============== ======================
:::            Processor Type  ``Cortex-A5``
CUP Clock      Clock Frequency ''450,000,000 Hz ''
:::            Accuracy        ``2.2 nSec (1 cycle)``
RTOS Tick Rate Frequency       ``1000 Hz``
:::            Period          ``1 mSec``
:::            Cycles          ``450,000 Cycles``
\                              
============== =============== ======================

**Performance Data:**

+--------------------------------------------------------------------+------------+
| **Flags**                                                          | **Cycles** |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag available)                               | 348        |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag unavailable, context switch to new task) | 837        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (no task pending, no context switch)            | 322        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (task waiting, context switch to pending task)  | 791        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (from an ISR, switching to a pending task)      | 3072       |
+--------------------------------------------------------------------+------------+
| \**Message Queues \*\*                                             |            |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message available)                                  | 268        |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message unavailable, context switch to new task)    | 2031       |
+--------------------------------------------------------------------+------------+
| xQueueSend (no task pending, no context switch)                    | 312        |
+--------------------------------------------------------------------+------------+
| xQueueSend (task waiting, context switch to pending task)          | 998        |
+--------------------------------------------------------------------+------------+
| xQueueSend (from an ISR, switching to a pending task)              | 662        |
+--------------------------------------------------------------------+------------+
| **Mutexes**                                                        |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex available)                                   | 293        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex unavailable, context switch to new task)     | 2503       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 325        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 1050       |
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
| xSemaphoreGive (from an ISR, switching to a pending task)          | 655        |
+--------------------------------------------------------------------+------------+
| **Interrupt Service Time**                                         |            |
+--------------------------------------------------------------------+------------+
| Interrupt service time (FreeRTOS)                                  | 107        |
+--------------------------------------------------------------------+------------+
| Time to return from an ISR (FreeRTOS, no task switch)              | 30         |
+--------------------------------------------------------------------+------------+

--------------

ADSP-SC589 Cortex-A Core Sizing Metrics
---------------------------------------

All values in bytes.

=========================================== ======== ======== =========
**Test**                                    **Data** **Code** **Total**
Basic project                               146832   19664    166496
**Message Queues**                                            
Basic project using 1 static object         146832   19728    166560
Basic project using 2 static objects        146832   19728    166560
**Flags**                                                     
Basic project using 1 static object         146876   20512    167388
Basic project using 2 static objects        146876   20512    167388
**Mutexes**                                                   
Basic project using 1 static object         146832   19744    166576
Basic project using 2 static objects        146832   19744    166576
**Semaphores**                                                
Basic project using 1 static object         146832   19712    166544
Basic project using 2 static objects        146832   19712    166544
**Semaphore + Mutex + MessageQueue + Flag**                   
Basic project using 1 static object         146876   20700    167576
Basic project using 2 static objects        146876   20700    167576
=========================================== ======== ======== =========
