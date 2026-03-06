FreeRTOS Addin vs uCOSIII: ADSP-SC573(SHARC+ Core)
==================================================

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
:::            Processor Type  ``SHARC+``
CUP Clock      Clock Frequency ''500,000,000 Hz ''
:::            Accuracy        ``2.0 nSec (1 cycle)``
RTOS Tick Rate Frequency       ``1000 Hz``
:::            Period          ``1 mSec``
:::            Cycles          ``500,000 Cycles``
\                              
============== =============== ======================

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
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
   


.. container:: column

   **uCOS III**

   
   ============================================================ ==========
   **Flags**                                                    **Cycles**
   OSFlagPend (flag available)                                  167
   OSFlagPend (flag unavailable, context switchto new task)     1277
   OSFlagPost (no task pending, no contextswitch)               140
   OSFlagPost (task waiting, context switch topending task)     1358
   OSFlagPost (from an ISR, switching to apending task)         626
   \**Message Queues \*\*                                       
   OSQPend (message available)                                  198
   OSQPend (message unavailable, context switchto new task)     1281
   OSQPost (no task pending, no context switch)                 271
   OSQPost (task waiting, context switch topending task)        1320
   OSQPost (from an ISR, switching to a pendingtask)            603
   **Mutexes**                                                  
   OSMutexPend (mutex available)                                115
   OSMutexPend (mutex unavailable, contextswitch to new task)   1451
   OSMutexPost (no task pending, no contextswitch)              145
   OSMutexPost (task waiting, context switch topending task)    1547
   **Semaphores**                                               
   OSSemPend (semaphore available)                              93
   OSSemPend (semaphore unavailable, contextswitch to new task) 1232
   OSSemPost (no task pending, no contextswitch)                132
   OSSemPost (task waiting, context switch topending task)      1272
   OSSemPost (from an ISR, switching to apending task)          599
   **Interrupt Service Time**                                   
   Interrupt service time (uC/OS-III)                           363
   Time to return from an ISR (uC/OS-III, notask switch)        450
   ============================================================ ==========
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 1** Compare Cycles for SC573 SHARC+</fc>


--------------

Compare Space
=============

All values in bytes.

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
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
   


.. container:: column

   **uCOS III**

   
   =========================================== ======== ======== =========
   **Test**                                    **Data** **Code** **Total**
   Basic project                               11689    21234    32923
   **Message Queues**                                            
   Basic project using 1 static object         11793    23590    35383
   Basic project using 2 static objects        11817    23598    35415
   **Flags**                                                     
   Basic project using 1 static object         11769    23582    35351
   Basic project using 2 static objects        11793    23590    35383
   **Mutexes**                                                   
   Basic project using 1 static object         11737    22858    34595
   Basic project using 2 static objects        11769    22862    34631
   **Semaphores**                                                
   Basic project using 1 static object         11737    22618    34355
   Basic project using 2 static objects        11761    22622    34383
   **Semaphore + Mutex + MessageQueue + Flag**                   
   Basic project using 1 static object         11989    28818    40807
   Basic project using 2 static objects        12069    28834    40903
   =========================================== ======== ======== =========
   


.. container:: Centeralign

   <fc #4682b4>\ **Table 2** Compare Space for SC573 SHARC+</fc>


