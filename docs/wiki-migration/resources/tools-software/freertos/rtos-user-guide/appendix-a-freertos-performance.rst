Appendix A: FreeRTOS Performance
================================

The following appendix contains code size and performance data for Analog Devices specific ports of FreeRTOS.

Timer Cycles
------------

The following benchmarks report time and cycle count measurements for post and pending operations using varying methods of communication.

Benchmark data is available for the following EZ-Kits:

-  :doc:`ADSP-SC589 EZ-Kit (Cortex A5 Core) </wiki-migration/resources/tools-software/freertos/rtos-user-guide/appendix-a-freertos-performance/adsp-sc589-cortex-a-core-benchmark-data>`
-  :doc:`ADSP-SC589 EZ-Kit (SHARC+ Core) </wiki-migration/resources/tools-software/freertos/rtos-user-guide/appendix-a-freertos-performance/adsp-sc589-sharc-core-benchmark-data>`
-  ADSP-SC573 EZ-Kit (Cortex A5 Core)
-  :doc:`ADSP-21569 EZ-Kit (SHARC Core) </wiki-migration/resources/tools-software/freertos/rtos-user-guide/appendix-a-freertos-performance/adsp-21569-sharc-core-benchmark-data>`
-  :doc:`ADSP-BF707 EZ-Kit </wiki-migration/resources/tools-software/freertos/rtos-user-guide/appendix-a-freertos-performance/adzs-bf707-benchmark-data>`

The following projects are executed to gather the benchmark data:

-  **ISR**: calculate Interrupt service time and Time to return from an ISR when in FreeRTOS system.
-  **FLAG ISR**: calculate FLAG Post/Pend available time,context switch time when unavailable, Interrupt service time and Time to return from an ISR when in FreeRTOS system
-  **MSG ISR**: calculate Message queue Post/Pend available time,context switch time when unavailable, Interrupt service time and Time to return from an ISR when in FreeRTOS system
-  **SEM ISR**: calculate Semaphore Post/Pend available time,context switch time when unavailable, Interrupt service time and Time to return from an ISR when in FreeRTOS system
-  **MUT ISR**: calculate Mutex Post/Pend available time,context switch time when unavailable, Interrupt service time and Time to return from an ISR when in FreeRTOS system

Spaces
------

The following benchmarks report code size for several common RTOS operations within FreeRTOS:

-  **NONE**: Basic project
-  **Message** Queues: Basic project using 1 static object / Basic project using 2 static objects
-  **Flags**: Basic project using 1 static object / Basic project using 2 static objects
-  **Mutexes**: Basic project using 1 static object / Basic project using 2 static objects
-  **Semaphores**: Basic project using 1 static object / Basic project using 2 static objects
-  **ALL**: Basic project using 1 static object / Basic project using 2 static objects
