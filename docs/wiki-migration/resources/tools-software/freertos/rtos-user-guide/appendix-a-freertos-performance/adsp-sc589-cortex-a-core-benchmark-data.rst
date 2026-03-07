ADSP-SC589 (Cortex-A Core) Benchmark Data
=========================================

ADSP-SC589 Cortex-A Core Performance Metrics
--------------------------------------------

================================================================== =====
FreeRTOS_FLGISR                                                    cyles
================================================================== =====
xEventGroupWaitBits (flag available)                               321
xEventGroupWaitBits (flag unavailable, context switch to new task) 1129
xEventGroupSetBits (no task pending, no context switch)            324
xEventGroupSetBits (task waiting, context switch to pending task)  1095
xEventGroupSetBits (from an ISR, switching to a pending task)      3158
================================================================== =====

===================================================== =====
FreeRTOS_ISR                                          cyles
===================================================== =====
Interrupt service time (FreeRTOS)                     109
Time to return from an ISR (FreeRTOS, no task switch) 24
===================================================== =====

============================================================== =====
FreeRTOS_MSGISR                                                cyles
============================================================== =====
xQueueReceive(message available)                               287
xQueueReceive(message unavailable, context switch to new task) 2290
xQueueSend(no task pending, no context switch)                 309
xQueueSend(task waiting, context switch to pending task)       1309
xQueueSend(from an ISR, switching to a pending task)           648
============================================================== =====

============================================================== =====
FreeRTOS_MUTISR                                                cyles
============================================================== =====
xSemaphoreTake(mutex available)                                239
xSemaphoreTake(mutex unavailable, context switch to new task） 2630
xSemaphoreGive(no task pending, no context switch)             274
xSemaphoreGive(task waiting, context switch to pending task)   1438
============================================================== =====

================================================================= =====
FreeRTOS_SEMISR                                                   cyles
================================================================= =====
xSemaphoreTake(semaphore available)                               212
xSemaphoreTake(semaphore unavailable, context switch to new task) 2442
xSemaphoreGive(no task pending, no context switch)                317
xSemaphoreGive(task waiting, context switch to pending task)      1344
xSemaphoreGive (from an ISR, switching to a pending task)         638
================================================================= =====

--------------

ADSP-SC589 Cortex-A Core Sizing Metrics
---------------------------------------

==== ============= ===== ===== ======
\                  Data  Code  Total
==== ============= ===== ===== ======
None Basic Project 97812 18624 116436
==== ============= ===== ===== ======

**Basic project using 1 static object**

============== ===== ===== ======
\              Data  Code  Total
============== ===== ===== ======
Message Queues 97812 18680 116492
Flags          97812 19096 116908
Mutexes        97812 18704 116516
Semaphores     97812 18664 116476
ALL            97812 19264 117076
============== ===== ===== ======

**Basic project using 2 static objects**

============== ===== ===== ======
\              Data  Code  Total
============== ===== ===== ======
Message Queues 97812 18680 116492
Flags          97812 19096 116908
Mutexes        97812 18704 116516
Semaphores     97812 18664 116476
ALL            97812 19256 117068
============== ===== ===== ======
