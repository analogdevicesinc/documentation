FreeRTOS Addin vs uCOSIII: ADSP-21569
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

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
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
   


.. container:: column

   **uCOS III**

   
   ============================================================ ==========
   **Flags**                                                    **Cycles**
   OSFlagPend (flag available)                                  111
   OSFlagPend (flag unavailable, context switchto new task)     1105
   OSFlagPost (no task pending, no contextswitch)               111
   OSFlagPost (task waiting, context switch topending task)     1205
   OSFlagPost (from an ISR, switching to apending task)         561
   \**Message Queues \*\*                                       
   OSQPend (message available)                                  179
   OSQPend (message unavailable, context switchto new task)     1114
   OSQPost (no task pending, no context switch)                 196
   OSQPost (task waiting, context switch topending task)        1135
   OSQPost (from an ISR, switching to a pendingtask)            561
   **Mutexes**                                                  
   OSMutexPend (mutex available)                                110
   OSMutexPend (mutex unavailable, contextswitch to new task)   1306
   OSMutexPost (no task pending, no contextswitch)              118
   OSMutexPost (task waiting, context switch topending task)    1373
   **Semaphores**                                               
   OSSemPend (semaphore available)                              77
   OSSemPend (semaphore unavailable, contextswitch to new task) 1062
   OSSemPost (no task pending, no contextswitch)                116
   OSSemPost (task waiting, context switch topending task)      1118
   OSSemPost (from an ISR, switching to apending task)          541
   **Interrupt Service Time**                                   
   Interrupt service time (uC/OS-III)                           365
   Time to return from an ISR (uC/OS-III, notask switch)        428
   ============================================================ ==========
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 1** Compare Cycles for ADSP-21569</fc>


--------------

Compare Space
=============

All values in bytes.

.. container:: column

   **\__FreeRTOS Addin \_\_**

   
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
   


.. container:: column

   **uCOS III**

   
   =========================================== ======== ======== =========
   **Test**                                    **Data** **Code** **Total**
   Basic project                               12756    25286    38042
   **Message Queues**                                            
   Basic project using 1 static object         12836    27974    40810
   Basic project using 2 static objects        12884    27982    40866
   **Flags**                                                     
   Basic project using 1 static object         13092    28830    41922
   Basic project using 2 static objects        13132    28834    41966
   **Mutexes**                                                   
   Basic project using 1 static object         12836    27386    40222
   Basic project using 2 static objects        12884    27390    40274
   **Semaphores**                                                
   Basic project using 1 static object         12828    27070    39898
   Basic project using 2 static objects        12868    27070    39938
   **Semaphore + Mutex + MessageQueue + Flag**                   
   Basic project using 1 static object         13308    35270    48578
   Basic project using 2 static objects        13484    35286    48770
   =========================================== ======== ======== =========
   


.. container:: Centeralign

   <fc #4682b4>\ **Table 2** Compare Space for ADSP-21569</fc>


