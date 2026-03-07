System Resources Used By FreeRTOS
=================================

Memory
------

The memory used by FreeRTOS will vary depending on configuration, as many features can be removed and buffers resized. See the :doc:`Space Benchmark Figures </wiki-migration/resources/tools-software/freertos/rtos-user-guide/appendix-a-freertos-performance/adsp-21569-sharc-core-benchmark-data>` for an indication of space used in various configurations.

Interrupts
----------

FreeRTOS makes use of a software interrupt for context switching, and a timer interrupt for the tick mechanism

======== ============================== ==================
Platform Context Switch Interrupt       Timer
======== ============================== ==================
ARM      SWI                            System Timer 0
Blackfin IVG14 (Interrupt #14)          TMR (Interrupt #6)
SHARC    Core User Software Interrupt 3 TMZLI
======== ============================== ==================

Note: An alternative timer can be used by defining configTIMER_INTERRUPT.

Note: On ADSP-2158x/ADSP-SC58x and ADSP-2157x/ADSP-SC57x where anomaly 20-00-0081 applies, then system interrupts SOFT6 (Core1) and SOFT7 (Core2) are used instead of the core interrupt.
