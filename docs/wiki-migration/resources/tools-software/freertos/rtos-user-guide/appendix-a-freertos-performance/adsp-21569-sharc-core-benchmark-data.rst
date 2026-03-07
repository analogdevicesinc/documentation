ADSP-21569 (SHARC Core) Benchmark Data
======================================

ADSP-21569 SHARC Core Performance Metrics
-----------------------------------------

================================================================== =====
FreeRTOS_FLGISR                                                    cyles
================================================================== =====
xEventGroupWaitBits (flag available)                               314
xEventGroupWaitBits (flag unavailable, context switch to new task) 1244
xEventGroupSetBits (no task pending, no context switch)            255
xEventGroupSetBits (task waiting, context switch to pending task)  1156
xEventGroupSetBits (from an ISR, switching to a pending task)      3742
================================================================== =====

===================================================== =====
FreeRTOS_ISR                                          cyles
===================================================== =====
Interrupt service time (FreeRTOS)                     227
Time to return from an ISR (FreeRTOS, no task switch) 174
===================================================== =====

============================================================== =====
FreeRTOS_MSGISR                                                cyles
============================================================== =====
xQueueReceive(message available)                               298
xQueueReceive(message unavailable, context switch to new task) 2108
xQueueSend(no task pending, no context switch)                 363
xQueueSend(task waiting, context switch to pending task)       1434
xQueueSend(from an ISR, switching to a pending task)           1097
============================================================== =====

============================================================== =====
FreeRTOS_MUTISR                                                cyles
============================================================== =====
xSemaphoreTake(mutex available)                                238
xSemaphoreTake(mutex unavailable, context switch to new task） 2411
xSemaphoreGive(no task pending, no context switch)             329
xSemaphoreGive(task waiting, context switch to pending task)   1540
============================================================== =====

================================================================= =====
FreeRTOS_SEMISR                                                   cyles
================================================================= =====
xSemaphoreTake(semaphore available)                               213
xSemaphoreTake(semaphore unavailable, context switch to new task) 2097
xSemaphoreGive(no task pending, no context switch)                313
xSemaphoreGive(task waiting, context switch to pending task)      1293
xSemaphoreGive (from an ISR, switching to a pending task)         1029
================================================================= =====

--------------

ADSP-21569 SHARC Core Sizing Metrics
------------------------------------

==== ============= ===== ===== =====
\                  Data  Code  Total
==== ============= ===== ===== =====
None Basic Project 59307 29842 89149
==== ============= ===== ===== =====

**Basic project using 1 static object**

============== ===== ===== =====
\              Data  Code  Total
============== ===== ===== =====
Message Queues 59403 29970 89373
Flags          59459 31702 91161
Mutexes        59395 32114 91509
Semaphores     59395 31982 91377
ALL            59547 34198 93745
============== ===== ===== =====

**Basic project using 2 static objects**

============== ===== ===== =====
\              Data  Code  Total
============== ===== ===== =====
Message Queues 59483 29970 89453
Flags          59491 31702 91193
Mutexes        59483 32114 91597
Semaphores     59483 31982 91465
ALL            59667 34198 93865
============== ===== ===== =====
