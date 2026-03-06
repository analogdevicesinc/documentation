FreeRTOS Addin vs uCOSIII: ADSP-SC573 (Cortex A5 Core)
======================================================

**Applicable Version**

+-----------+------------+-------------------------------------------------------------+
| Name      | Version    | Description                                                 |
+===========+============+=============================================================+
| µC/OS-III | ``v2.9.0`` | ADI-uCOS-III-Rel2.9.0                                       |
+-----------+------------+-------------------------------------------------------------+
| FreeRTOS  | ``v1.0.0`` | ADI-FreeRTOS-Addin-1.0.0 ( Based Official FreeRTOSv10.0.0 ) |
+-----------+------------+-------------------------------------------------------------+
|           |            |                                                             |
+-----------+------------+-------------------------------------------------------------+

Compare Timer Cycles
====================

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

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
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
   


.. container:: column

   **uCOS III**

   
   ============================================================= ==========
   **Flags**                                                     **Cycles**
   OSFlagPend(flag available)                                    117
   OSFlagPend (flag unavailable, context switch to new task)     551
   OSFlagPost (no task pending, no context switch)               68
   OSFlagPost (task waiting, context switch to pending task)     681
   OSFlagPost (from an ISR, switching to a pending task)         372
   \**Message Queues \*\*                                        
   OSQPend (message available)                                   126
   OSQPend (message unavailable, context switch to new task)     547
   OSQPost (no task pending, no context switch)                  158
   OSQPost (task waiting, context switch to pending task)        612
   OSQPost (from an ISR, switching to a pending task)            372
   **Mutexes**                                                   
   OSMutexPend (mutex available)                                 98
   OSMutexPend (mutex unavailable, context switch to new task)   750
   OSMutexPost (no task pending, no context switch)              97
   OSMutexPost (task waiting, context switch to pending task)    848
   **Semaphores**                                                
   OSSemPend (semaphore available)                               76
   OSSemPend (semaphore unavailable, context switch to new task) 517
   OSSemPost (no task pending, no context switch)                68
   OSSemPost (task waiting, context switch to pending task)      678
   OSSemPost (from an ISR, switching to a pending task)          374
   **Interrupt Service Time**                                    
   Interrupt service time (uC/OS-III)                            229
   Time to return from an ISR (uC/OS-III, notask switch)         216
   ============================================================= ==========
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 1** Compare Cycles for ADSP-SC573 (Cortex A5 Core)</fc>


--------------

Compare Space
=============

All values in bytes.

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
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
   


.. container:: column

   **uCOS III**

   
   =========================================== ======== ======== =========
   **Test**                                    **Data** **Code** **Total**
   Basic project                               48452    19920    68372
   **Message Queues**                                            
   Basic project using 1 static object         48468    20640    69108
   Basic project using 2 static objects        48468    20640    69108
   **Flags**                                                     
   Basic project using 1 static object         48464    20624    69088
   Basic project using 2 static objects        48464    20624    69088
   **Mutexes**                                                   
   Basic project using 1 static object         48460    19968    68428
   Basic project using 2 static objects        48460    19968    68428
   **Semaphores**                                                
   Basic project using 1 static object         48460    20384    68844
   Basic project using 2 static objects        48460    20384    68844
   **Semaphore + Mutex + MessageQueue + Flag**                   
   Basic project using 1 static object         48492    22248    70740
   Basic project using 2 static objects        48492    22264    70756
   =========================================== ======== ======== =========
   


.. container:: Centeralign

   <fc #4682b4>\ **Table 2** Compare Space for ADSP-SC573 (Cortex A5 Core) </fc>


