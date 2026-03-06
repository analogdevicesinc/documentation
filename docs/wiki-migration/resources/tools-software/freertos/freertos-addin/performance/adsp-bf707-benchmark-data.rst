ADSP-BF707 Benchmark Data
=========================

ADSP-BF707 Performance Metrics
------------------------------

**Processor and FreeRTOS Configuration:**

============== =============== ======================
Processor      Board Name      ``ADSP-BF707-EzKit``
============== =============== ======================
:::            Processor Type  ``Blackfin``
CUP Clock      Clock Frequency ''400,000,000 Hz ''
:::            Accuracy        ``2.5 nSec (1 cycle)``
RTOS Tick Rate Frequency       ``1000 Hz``
:::            Period          ``1 mSec``
:::            Cycles          ``400,000 Cycles``
\                              
============== =============== ======================

+--------------------------------------------------------------------+------------+
| **Flags**                                                          | **Cycles** |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag available)                               | 476        |
+--------------------------------------------------------------------+------------+
| xEventGroupWaitBits (flag unavailable, context switch to new task) | 2132       |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (no task pending, no context switch)            | 416        |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (task waiting, context switch to pending task)  | 2020       |
+--------------------------------------------------------------------+------------+
| xEventGroupSetBits (from an ISR, switching to a pending task)      | 3666       |
+--------------------------------------------------------------------+------------+
| \**Message Queues \*\*                                             |            |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message available)                                  | 518        |
+--------------------------------------------------------------------+------------+
| xQueueReceive (message unavailable, context switch to new task)    | 3200       |
+--------------------------------------------------------------------+------------+
| xQueueSend (no task pending, no context switch)                    | 702        |
+--------------------------------------------------------------------+------------+
| xQueueSend (task waiting, context switch to pending task)          | 2620       |
+--------------------------------------------------------------------+------------+
| xQueueSend (from an ISR, switching to a pending task)              | 1591       |
+--------------------------------------------------------------------+------------+
| **Mutexes**                                                        |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex available)                                   | 406        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (mutex unavailable, context switch to new task)     | 3865       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 740        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 2890       |
+--------------------------------------------------------------------+------------+
| **Semaphores**                                                     |            |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore available)                               | 344        |
+--------------------------------------------------------------------+------------+
| xSemaphoreTake (semaphore unavailable, context switch to new task) | 3246       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (no task pending, no context switch)                | 592        |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (task waiting, context switch to pending task)      | 2331       |
+--------------------------------------------------------------------+------------+
| xSemaphoreGive (from an ISR, switching to a pending task)          | 1421       |
+--------------------------------------------------------------------+------------+
| **Interrupt Service Time**                                         |            |
+--------------------------------------------------------------------+------------+
| Interrupt service time (FreeRTOS)                                  | 141        |
+--------------------------------------------------------------------+------------+
| Time to return from an ISR (FreeRTOS, no task switch)              | 154        |
+--------------------------------------------------------------------+------------+

--------------

ADSP-BF707 Core Sizing Metrics
------------------------------

All values in bytes.

=========================================== ======== ======== =========
**Test**                                    **Data** **Code** **Total**
Basic project                               6303     16762    23065
**Message Queues**                                            
Basic project using 1 static object         6383     16826    23209
Basic project using 2 static objects        6459     16826    23285
**Flags**                                                     
Basic project using 1 static object         6375     17826    24201
Basic project using 2 static objects        6403     17826    24229
**Mutexes**                                                   
Basic project using 1 static object         6379     18026    24405
Basic project using 2 static objects        6455     18026    24481
**Semaphores**                                                
Basic project using 1 static object         6379     17962    24341
Basic project using 2 static objects        6455     17962    24417
**Semaphore + Mutex + MessageQueue + Flag**                   
Basic project using 1 static object         6531     19218    25749
Basic project using 2 static objects        6711     19218    25929
=========================================== ======== ======== =========
