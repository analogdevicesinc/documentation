ADSP-21569 Benchmark Data
=========================

ADSP-21569 SHARC Core Performance Metrics
-----------------------------------------

**Processor and FreeRTOS Configuration:**

============== =============== ======================
Processor      Board Name      ``ADSP-21569-EzKit``
============== =============== ======================
:::            Processor Type  ``SHARC``
CUP Clock      Clock Frequency ''1000,000,000 Hz ''
:::            Accuracy        ``1.0 nSec (1 cycle)``
RTOS Tick Rate Frequency       ``1000 Hz``
:::            Period          ``1 mSec``
:::            Cycles          ``1000,000 Cycles``
\                              
============== =============== ======================

+--------------------------------------------------------------------+------------+
| **Flags**                                                          | **Cycles** |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag available)                               | 325        |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag unavailable, context switch to new task) | 1381       |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (no task pending, no context switch)            | 260        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (task waiting, context switch to pending task)  | 1258       |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (from an ISR, switching to a pending task)      | 3802       |
+--------------------------------------------------------------------+------------+
| \**Message Queues \*\*                                             |            |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message available)                                  | 303        |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message unavailable, context switch to new task)    | 2195       |
+--------------------------------------------------------------------+------------+
| xQueueSend (no task pending, no context switch)                    | 353        |
+--------------------------------------------------------------------+------------+
| xQueueSend (task waiting, context switch to pending task)          | 1503       |
+--------------------------------------------------------------------+------------+
| xQueueSend (from an ISR, switching to a pending task)              | 1073       |
+--------------------------------------------------------------------+------------+
| **Mutexes**                                                        |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex available)                                   | 253        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex unavailable, context switch to new task)     | 2516       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 315        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 1629       |
+--------------------------------------------------------------------+------------+
| **Semaphores**                                                     |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore available)                               | 234        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore unavailable, context switch to new task) | 2208       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 347        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 1409       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (from an ISR, switching to a pending task)          | 984        |
+--------------------------------------------------------------------+------------+
| **Interrupt Service Time**                                         |            |
+--------------------------------------------------------------------+------------+
| Interrupt service time (FreeRTOS)                                  | 227        |
+--------------------------------------------------------------------+------------+
| Time to return from an ISR (FreeRTOS, no task switch)              | 174        |
+--------------------------------------------------------------------+------------+

--------------

ADSP-21569 SHARC Core Sizing Metrics
------------------------------------

All values in bytes.

=========================================== ======== ======== =========
**Test**                                    **Data** **Code** **Total**
Basic project                               58973    31190    90163
**Message Queues**                                            
Basic project using 1 static object         59061    31322    90383
Basic project using 2 static objects        59133    31322    90455
**Flags**                                                     
Basic project using 1 static object         59045    33086    92131
Basic project using 2 static objects        59077    33086    92163
**Mutexes**                                                   
Basic project using 1 static object         59053    33582    92635
Basic project using 2 static objects        59133    33582    92715
**Semaphores**                                                
Basic project using 1 static object         59053    33454    92507
Basic project using 2 static objects        59133    33454    92587
**Semaphore + Mutex + MessageQueue + Flag**                   
Basic project using 1 static object         59205    35706    94911
Basic project using 2 static objects        59389    35706    95095
=========================================== ======== ======== =========
