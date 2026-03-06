ADSP-SC589 (SHARC+ Core) Benchmark Data
=======================================

ADSP-SC589 SHARC+ Core Performance Metrics
------------------------------------------

**Processor and FreeRTOS Configuration:**

============== =============== ======================
Processor      Board Name      ``ADSP-SC589-EzKit``
============== =============== ======================
:::            Processor Type  ``SHARC+``
CUP Clock      Clock Frequency ''500,000,000 Hz ''
:::            Accuracy        ``2.0 nSec (1 cycle)``
RTOS Tick Rate Frequency       ``1000 Hz``
:::            Period          ``1 mSec``
:::            Cycles          ``500,000 Cycles``
\                              
============== =============== ======================

+--------------------------------------------------------------------+------------+
| **Flags**                                                          | **Cycles** |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag available)                               | 325        |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag unavailable, context switch to new task) | 1381       |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (no task pending, no context switch)            | 263        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (task waiting, context switch to pending task)  | 1299       |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (from an ISR, switching to a pending task)      | 3774       |
+--------------------------------------------------------------------+------------+
| \**Message Queues \*\*                                             |            |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message available)                                  | 313        |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message unavailable, context switch to new task)    | 2222       |
+--------------------------------------------------------------------+------------+
| xQueueSend (no task pending, no context switch)                    | 387        |
+--------------------------------------------------------------------+------------+
| xQueueSend (task waiting, context switch to pending task)          | 1530       |
+--------------------------------------------------------------------+------------+
| xQueueSend (from an ISR, switching to a pending task)              | 1042       |
+--------------------------------------------------------------------+------------+
| **Mutexes**                                                        |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex available)                                   | 265        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex unavailable, context switch to new task)     | 2526       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 339        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 1631       |
+--------------------------------------------------------------------+------------+
| **Semaphores**                                                     |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore available)                               | 222        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore unavailable, context switch to new task) | 2210       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 323        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 1400       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (from an ISR, switching to a pending task)          | 969        |
+--------------------------------------------------------------------+------------+
| **Interrupt Service Time**                                         |            |
+--------------------------------------------------------------------+------------+
| Interrupt service time (FreeRTOS)                                  | 227        |
+--------------------------------------------------------------------+------------+
| Time to return from an ISR (FreeRTOS, no task switch)              | 176        |
+--------------------------------------------------------------------+------------+

--------------

ADSP-SC589 SHARC+ Core Sizing Metrics
-------------------------------------

All values in bytes.

=========================================== ======== ======== =========
**Test**                                    **Data** **Code** **Total**
Basic project                               59581    30402    89983
**Message Queues**                                            
Basic project using 1 static object         59669    30534    90203
Basic project using 2 static objects        59741    30534    90275
**Flags**                                                     
Basic project using 1 static object         59653    32330    91983
Basic project using 2 static objects        59685    32330    92015
**Mutexes**                                                   
Basic project using 1 static object         59661    32822    92483
Basic project using 2 static objects        59741    32822    92563
**Semaphores**                                                
Basic project using 1 static object         59661    32690    92351
Basic project using 2 static objects        59741    32690    92431
**Semaphore + Mutex + MessageQueue + Flag**                   
Basic project using 1 static object         59813    34986    94799
Basic project using 2 static objects        59997    34986    94983
=========================================== ======== ======== =========
