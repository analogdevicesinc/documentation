ADSP-SC589 (SHARC+ Core) Benchmark Data
=======================================

ADSP-SC589 SHARC+ Core Performance Metrics
------------------------------------------

================================================================== =====
FreeRTOS_FLGISR                                                    cyles
================================================================== =====
xEventGroupWaitBits (flag available)                               440
xEventGroupWaitBits (flag unavailable, context switch to new task) 1708
xEventGroupSetBits (no task pending, no context switch)            340
xEventGroupSetBits (task waiting, context switch to pending task)  1586
xEventGroupSetBits (from an ISR, switching to a pending task)      4643
================================================================== =====

===================================================== =====
FreeRTOS_ISR                                          cyles
===================================================== =====
Interrupt service time (FreeRTOS)                     236
Time to return from an ISR (FreeRTOS, no task switch) 182
===================================================== =====

============================================================== =====
FreeRTOS_MSGISR                                                cyles
============================================================== =====
xQueueReceive(message available)                               409
xQueueReceive(message unavailable, context switch to new task) 2710
xQueueSend(no task pending, no context switch)                 476
xQueueSend(task waiting, context switch to pending task)       1877
xQueueSend(from an ISR, switching to a pending task)           1160
============================================================== =====

============================================================== =====
FreeRTOS_MUTISR                                                cyles
============================================================== =====
xSemaphoreTake(mutex available)                                321
xSemaphoreTake(mutex unavailable, context switch to new task） 3199
xSemaphoreGive(no task pending, no context switch)             484
xSemaphoreGive(task waiting, context switch to pending task)   2117
============================================================== =====

================================================================= =====
FreeRTOS_SEMISR                                                   cyles
================================================================= =====
xSemaphoreTake(semaphore available)                               275
xSemaphoreTake(semaphore unavailable, context switch to new task) 2711
xSemaphoreGive(no task pending, no context switch)                404
xSemaphoreGive(task waiting, context switch to pending task)      1718
xSemaphoreGive (from an ISR, switching to a pending task)         1019
================================================================= =====

--------------

ADSP-SC589 SHARC+ Core Sizing Metrics
-------------------------------------

==== ============= ===== ===== =====
\                  Data  Code  Total
==== ============= ===== ===== =====
None Basic Project 59838 29764 89602
==== ============= ===== ===== =====

**Basic project using 1 static object**

============== ===== ===== =====
\              Data  Code  Total
============== ===== ===== =====
Message Queues 59934 29896 89830
Flags          59966 31692 91658
Mutexes        59926 32184 92110
Semaphores     59926 32048 91974
ALL            60054 34340 94394
============== ===== ===== =====

**Basic project using 2 static objects**

============== ===== ===== =====
\              Data  Code  Total
============== ===== ===== =====
Message Queues 59934 29896 89830
Flags          59966 31692 91658
Mutexes        59926 32184 92110
Semaphores     59926 32048 91974
ALL            60054 34340 94394
============== ===== ===== =====
