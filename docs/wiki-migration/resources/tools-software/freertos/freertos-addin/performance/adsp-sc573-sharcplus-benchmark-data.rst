ADSP-SC573 (SHARC+ Core) Benchmark Data
=======================================

ADSP-SC573 SHARC+ Core Performance Metrics
------------------------------------------

**Processor and FreeRTOS Configuration:**

============== =============== ======================
Processor      Board Name      ``ADSP-SC573-EzKit``
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
| xEventGroupWaitBits (flag available)                               | 344        |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag unavailable, context switch to new task) | 1397       |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (no task pending, no context switch)            | 258        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (task waiting, context switch to pending task)  | 1293       |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (from an ISR, switching to a pending task)      | 3840       |
+--------------------------------------------------------------------+------------+
| \**Message Queues \*\*                                             |            |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message available)                                  | 312        |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message unavailable, context switch to new task)    | 2241       |
+--------------------------------------------------------------------+------------+
| xQueueSend (no task pending, no context switch)                    | 379        |
+--------------------------------------------------------------------+------------+
| xQueueSend (task waiting, context switch to pending task)          | 1558       |
+--------------------------------------------------------------------+------------+
| xQueueSend (from an ISR, switching to a pending task)              | 1069       |
+--------------------------------------------------------------------+------------+
| **Mutexes**                                                        |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex available)                                   | 256        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex unavailable, context switch to new task)     | 2533       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 339        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 1659       |
+--------------------------------------------------------------------+------------+
| **Semaphores**                                                     |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore available)                               | 220        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore unavailable, context switch to new task) | 2197       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 310        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 1401       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (from an ISR, switching to a pending task)          | 983        |
+--------------------------------------------------------------------+------------+
| **Interrupt Service Time**                                         |            |
+--------------------------------------------------------------------+------------+
| Interrupt service time (FreeRTOS)                                  | 227        |
+--------------------------------------------------------------------+------------+
| Time to return from an ISR (FreeRTOS, no task switch)              | 174        |
+--------------------------------------------------------------------+------------+

--------------

ADSP-SC573 SHARC+ Core Sizing Metrics
-------------------------------------

All values in bytes.

=========================================== ======== ======== =========
**Test**                                    **Data** **Code** **Total**
Basic project                               59141    31576    90717
**Message Queues**                                            
Basic project using 1 static object         59229    31708    90937
Basic project using 2 static objects        59301    31708    91009
**Flags**                                                     
Basic project using 1 static object         59213    33504    92717
Basic project using 2 static objects        59245    33504    92749
**Mutexes**                                                   
Basic project using 1 static object         59221    33996    93217
Basic project using 2 static objects        59301    33996    93297
**Semaphores**                                                
Basic project using 1 static object         59221    33864    93085
Basic project using 2 static objects        59301    33864    93165
**Semaphore + Mutex + MessageQueue + Flag**                   
Basic project using 1 static object         59373    36160    95533
Basic project using 2 static objects        59557    36160    95717
=========================================== ======== ======== =========
