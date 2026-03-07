FreeRTOS Addin Performance
==========================

The following appendix contains:

-  Performance data and code size for Analog Devices specific ports of FreeRTOS.
-  Comparison benchmark data between FreeRTOS Addin and uCOS III

--------------

Benchmark Data
--------------

The benchmark data is available for the following EZ-Kits:

-  `ADSP-SC589 EZ-Kit (Cortex A5 Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/adsp-sc589-cortex-a-benchmark-data>`_
-  `ADSP-SC589 EZ-Kit (SHARC+ Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/adsp-sc589-sharcplus-benchmark-data>`_
-  `ADSP-SC584 EZ-Kit (Cortex A5 Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/adsp-sc584-cortex-a-benchmark-data>`_
-  `ADSP-SC584 EZ-Kit (SHARC+ Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/adsp-sc584-sharcplus-benchmark-data>`_
-  `ADSP-SC573 EZ-Kit (Cortex A5 Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/adsp-sc573-cortex-a-benchmark-data>`_
-  `ADSP-SC573 EZ-Kit (SHARC+ Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/adsp-sc573-sharcplus-benchmark-data>`_
-  `ADSP-21569 EZ-Kit (SHARC Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/adsp-21569-benchmark-data>`_
-  `ADSP-BF707 EZ-Kit <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/adsp-bf707-benchmark-data>`_

--------------

Timer Cycles
~~~~~~~~~~~~

The following benchmarks report time and cycle count measurements for post and pending operations using varying methods of communication.

Projects below are executed to gather the benchmark data:

-  **ISR**: calculate Interrupt service time and Time to return from an ISR when in FreeRTOS system.
-  **FLAG ISR**: calculate FLAG Post/Pend available time,context switch time when unavailable, Interrupt service time and Time to return from an ISR when in FreeRTOS system
-  **MSG ISR**: calculate Message queue Post/Pend available time,context switch time when unavailable, Interrupt service time and Time to return from an ISR when in FreeRTOS system
-  **SEM ISR**: calculate Semaphore Post/Pend available time,context switch time when unavailable, Interrupt service time and Time to return from an ISR when in FreeRTOS system
-  **MUT ISR**: calculate Mutex Post/Pend available time,context switch time when unavailable, Interrupt service time and Time to return from an ISR when in FreeRTOS system

Space
~~~~~

The following benchmarks report code size for several common RTOS operations within FreeRTOS.

Projects below are executed to gather the benchmark data:

-  **NONE**: Basic project
-  **Message** Queues: Basic project using 1 static object / Basic project using 2 static objects
-  **Flags**: Basic project using 1 static object / Basic project using 2 static objects
-  **Mutexes**: Basic project using 1 static object / Basic project using 2 static objects
-  **Semaphores**: Basic project using 1 static object / Basic project using 2 static objects
-  **ALL**: Basic project using 1 static object / Basic project using 2 static objects

--------------

Compare Benchmark Data with uCOS III
------------------------------------

Compare Benchmark Data with uCOS III for the following EZ-Kits:

-  `ADSP-SC589 EZ-Kit (Cortex A5 Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/compare-benchmark-sc589-cortex-a>`_
-  `ADSP-SC589 EZ-Kit (SHARC+ Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/compare-benchmark-sc589-sharcplus>`_
-  `ADSP-SC573 EZ-Kit (Cortex A5 Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/compare-benchmark-sc573-cortex-a>`_
-  `ADSP-SC573 EZ-Kit (SHARC+ Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/compare-benchmark-sc573-sharcplus>`_
-  `ADSP-21569 EZ-Kit(SHARC Core) <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/compare-benchmark-21569>`_
-  `ADSP-BF707 EZ-Kit <https://wiki.analog.com/resources/tools-software/freertos/freertos-addin/performance/compare-benchmark-bf707>`_
