FreeRTOS Addin vs uCOSIII: ADSP-BF707
=====================================

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

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
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
   


.. container:: column

   **uCOS III**

   
   ============================================================ ==========
   **Flags**                                                    **Cycles**
   OSFlagPend (flag available)                                  84
   OSFlagPend (flag unavailable, context switchto new task)     670
   OSFlagPost (no task pending, no contextswitch)               83
   OSFlagPost (task waiting, context switch topending task)     766
   OSFlagPost (from an ISR, switching to apending task)         432
   \**Message Queues \*\*                                       
   OSQPend (message available)                                  112
   OSQPend (message unavailable, context switchto new task)     648
   OSQPost (no task pending, no context switch)                 130
   OSQPost (task waiting, context switch topending task)        711
   OSQPost (from an ISR, switching to a pendingtask)            414
   **Mutexes**                                                  
   OSMutexPend (mutex available)                                67
   OSMutexPend (mutex unavailable, contextswitch to new task)   832
   OSMutexPost (no task pending, no contextswitch)              75
   OSMutexPost (task waiting, context switch topending task)    848
   **Semaphores**                                               
   OSSemPend (semaphore available)                              58
   OSSemPend (semaphore unavailable, contextswitch to new task) 579
   OSSemPost (no task pending, no contextswitch)                76
   OSSemPost (task waiting, context switch topending task)      683
   OSSemPost (from an ISR, switching to apending task)          412
   **Interrupt Service Time**                                   
   Interrupt service time (uC/OS-III)                           196
   Time to return from an ISR (uC/OS-III, notask switch)        288
   ============================================================ ==========
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 1** Compare Cycles for ADSP-BF707</fc>


--------------

Compare Space
=============

All values in bytes.

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
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
   


.. container:: column

   **uCOS III**

   
   =========================================== ======== ======== =========
   **Test**                                    **Data** **Code** **Total**
   Basic project                               8091     10858    18949
   **Message Queues**                                            
   Basic project using 1 static object         8223     12066    20289
   Basic project using 2 static objects        8247     12066    20313
   **Flags**                                                     
   Basic project using 1 static object         8247     11906    20153
   Basic project using 2 static objects        8267     11906    20173
   **Mutexes**                                                   
   Basic project using 1 static object         8259     12466    20725
   Basic project using 2 static objects        8287     12466    20753
   **Semaphores**                                                
   Basic project using 1 static object         8167     11618    19785
   Basic project using 2 static objects        8187     11618    19805
   **Semaphore + Mutex + MessageQueue + Flag**                   
   Basic project using 1 static object         8563     14946    23509
   Basic project using 2 static objects        8655     14954    23609
   =========================================== ======== ======== =========
   


.. container:: Centeralign

   <fc #4682b4>\ **Table 2** Compare Space for ADSP-BF707</fc>


