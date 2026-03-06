FreeRTOS Addin vs uCOSIII: ADSP-SC589(SHARC+ Core)
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

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
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
   


.. container:: column

   **uCOS III**

   
   ============================================================ ==========
   **Flags**                                                    **Cycles**
   OSFlagPend (flag available)                                  167
   OSFlagPend (flag unavailable, context switchto new task)     1264
   OSFlagPost (no task pending, no contextswitch)               140
   OSFlagPost (task waiting, context switch topending task)     1340
   OSFlagPost (from an ISR, switching to apending task)         629
   \**Message Queues \*\*                                       
   OSQPend (message available)                                  198
   OSQPend (message unavailable, context switchto new task)     1264
   OSQPost (no task pending, no context switch)                 271
   OSQPost (task waiting, context switch topending task)        1299
   OSQPost (from an ISR, switching to a pendingtask)            603
   **Mutexes**                                                  
   OSMutexPend (mutex available)                                115
   OSMutexPend (mutex unavailable, contextswitch to new task)   1440
   OSMutexPost (no task pending, no contextswitch)              145
   OSMutexPost (task waiting, context switch topending task)    1531
   **Semaphores**                                               
   OSSemPend (semaphore available)                              107
   OSSemPend (semaphore unavailable, contextswitch to new task) 1195
   OSSemPost (no task pending, no contextswitch)                132
   OSSemPost (task waiting, context switch topending task)      1250
   OSSemPost (from an ISR, switching to apending task)          592
   **Interrupt Service Time**                                   
   Interrupt service time (uC/OS-III)                           366
   Time to return from an ISR (uC/OS-III, notask switch)        454
   ============================================================ ==========
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 1** Compare Cycles for SC589 SHARC+</fc>


--------------

Compare Space
=============

All values in bytes.

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
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
   


.. container:: column

   **uCOS III**

   
   =========================================== ======== ======== =========
   **Test**                                    **Data** **Code** **Total**
   Basic project                               12125    20858    32983
   **Message Queues**                                            
   Basic project using 1 static object         12229    23182    35411
   Basic project using 2 static objects        12253    23186    35439
   **Flags**                                                     
   Basic project using 1 static object         12209    23174    35383
   Basic project using 2 static objects        12229    23182    35411
   **Mutexes**                                                   
   Basic project using 1 static object         12177    22474    34651
   Basic project using 2 static objects        12205    22478    34683
   **Semaphores**                                                
   Basic project using 1 static object         12169    22218    34387
   Basic project using 2 static objects        12189    22226    34415
   **Semaphore + Mutex + MessageQueue + Flag**                   
   Basic project using 1 static object         12421    28338    40759
   Basic project using 2 static objects        12501    28354    40855
   =========================================== ======== ======== =========
   


.. container:: Centeralign

   <fc #4682b4>\ **Table 2** Compare Space for SC589 SHARC+</fc>


