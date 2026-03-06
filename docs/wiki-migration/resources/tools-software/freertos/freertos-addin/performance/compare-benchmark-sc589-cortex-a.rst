FreeRTOS Addin vs uCOSIII: ADSP-SC589(Cortex-A Core)
====================================================

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
   


.. container:: column

   **uCOS III**

   
   ============================================================= ==========
   **Flags**                                                     **Cycles**
   OSFlagPend(flag available)                                    127
   OSFlagPend (flag unavailable, context switch to new task)     613
   OSFlagPost (no task pending, no context switch)               66
   OSFlagPost (task waiting, context switch to pending task)     657
   OSFlagPost (from an ISR, switching to a pending task)         357
   \**Message Queues \*\*                                        
   OSQPend (message available)                                   126
   OSQPend (message unavailable, context switch to new task)     536
   OSQPost (no task pending, no context switch)                  158
   OSQPost (task waiting, context switch to pending task)        597
   OSQPost (from an ISR, switching to a pending task)            370
   **Mutexes**                                                   
   OSMutexPend (mutex available)                                 88
   OSMutexPend (mutex unavailable, context switch to new task)   734
   OSMutexPost (no task pending, no context switch)              104
   OSMutexPost (task waiting, context switch to pending task)    766
   **Semaphores**                                                
   OSSemPend (semaphore available)                               76
   OSSemPend (semaphore unavailable, context switch to new task) 521
   OSSemPost (no task pending, no context switch)                57
   OSSemPost (task waiting, context switch to pending task)      677
   OSSemPost (from an ISR, switching to a pending task)          376
   **Interrupt Service Time**                                    
   Interrupt service time (uC/OS-III)                            239
   Time to return from an ISR (uC/OS-III, notask switch)         226
   ============================================================= ==========
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 1** Compare Cycles for SC589 Cortex-A</fc>


--------------

Compare Space
=============

All values in bytes.

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
   =========================================== ======== ======== =========
   **Test**                                    **Data** **Code** **Total**
   Basic project                               146820   19664    166484
   **Message Queues**                                            
   Basic project using 1 static object         146820   19728    166548
   Basic project using 2 static objects        146820   19728    166548
   **Flags**                                                     
   Basic project using 1 static object         146864   20512    167376
   Basic project using 2 static objects        146864   20512    167376
   **Mutexes**                                                   
   Basic project using 1 static object         146820   19744    166564
   Basic project using 2 static objects        146820   19744    166564
   **Semaphores**                                                
   Basic project using 1 static object         146820   19712    166532
   Basic project using 2 static objects        146820   19712    166532
   **Semaphore + Mutex + MessageQueue + Flag**                   
   Basic project using 1 static object         146864   20700    167564
   Basic project using 2 static objects        146864   20700    167564
   =========================================== ======== ======== =========
   


.. container:: column

   **uCOS III**

   
   =========================================== ======== ======== =========
   **Test**                                    **Data** **Code** **Total**
   Basic project                               46756    21840    68596
   **Message Queues**                                            
   Basic project using 1 static object         46772    22584    69356
   Basic project using 2 static objects        46772    22584    69356
   **Flags**                                                     
   Basic project using 1 static object         46768    22552    69320
   Basic project using 2 static objects        46768    22552    69320
   **Mutexes**                                                   
   Basic project using 1 static object         46764    21888    68652
   Basic project using 2 static objects        46764    21896    68660
   **Semaphores**                                                
   Basic project using 1 static object         46764    22304    69068
   Basic project using 2 static objects        46764    22312    69076
   **Semaphore + Mutex + MessageQueue + Flag**                   
   Basic project using 1 static object         46796    24192    70988
   Basic project using 2 static objects        46796    24208    71004
   =========================================== ======== ======== =========
   


.. container:: Centeralign

   <fc #4682b4>\ **Table 2** Compare Space for SC589 Cortex-A</fc>


