ADZS-BF707 Benchmark Data
=========================

ADZS-BF707 Performance Metrics
------------------------------

================================================================== =====
FreeRTOS_FLGISR                                                    cyles
================================================================== =====
xEventGroupWaitBits (flag available)                               420
xEventGroupWaitBits (flag unavailable, context switch to new task) 1856
xEventGroupSetBits (no task pending, no context switch)            356
xEventGroupSetBits (task waiting, context switch to pending task)  1866
xEventGroupSetBits (from an ISR, switching to a pending task)      3158
================================================================== =====

===================================================== =====
FreeRTOS_ISR                                          cyles
===================================================== =====
Interrupt service time (FreeRTOS)                     98
Time to return from an ISR (FreeRTOS, no task switch) 126
===================================================== =====

============================================================== =====
FreeRTOS_MSGISR                                                cyles
============================================================== =====
xQueueReceive(message available)                               447
xQueueReceive(message unavailable, context switch to new task) 2937
xQueueSend(no task pending, no context switch)                 630
xQueueSend(task waiting, context switch to pending task)       2412
xQueueSend(from an ISR, switching to a pending task)           1417
============================================================== =====

============================================================== =====
FreeRTOS_MUTISR                                                cyles
============================================================== =====
xSemaphoreTake(mutex available)                                337
xSemaphoreTake(mutex unavailable, context switch to new task） 3553
xSemaphoreGive(no task pending, no context switch)             663
xSemaphoreGive(task waiting, context switch to pending task)   2624
============================================================== =====

================================================================= =====
FreeRTOS_SEMISR                                                   cyles
================================================================= =====
xSemaphoreTake(semaphore available)                               271
xSemaphoreTake(semaphore unavailable, context switch to new task) 2943
xSemaphoreGive(no task pending, no context switch)                504
xSemaphoreGive(task waiting, context switch to pending task)      2093
xSemaphoreGive (from an ISR, switching to a pending task)         1235
================================================================= =====

--------------

ADZS-BF707 Sizing Metrics
-------------------------

==== ============= ==== ===== =====
\                  Data Code  Total
==== ============= ==== ===== =====
None Basic Project 6535 13698 20233
==== ============= ==== ===== =====

**Basic project using 1 static object**

============== ==== ===== =====
\              Data Code  Total
============== ==== ===== =====
Message Queues 6623 13762 20385
Flags          6567 14402 20969
Mutexes        6619 14682 21301
Semaphores     6619 14618 21237
ALL            6655 15506 22161
============== ==== ===== =====

**Basic project using 2 static objects**

============== ==== ===== =====
\              Data Code  Total
============== ==== ===== =====
Message Queues 6707 13762 20469
Flags          6599 14402 21001
Mutexes        6703 14682 21385
Semaphores     6703 14618 21321
ALL            6771 15506 22277
============== ==== ===== =====
