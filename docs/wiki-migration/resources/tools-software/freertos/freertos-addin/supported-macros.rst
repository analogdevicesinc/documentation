Supported Configuration Macros
==============================

The UI generates macros in FreeRTOSConfig.h, usually based on a field in the FreeRTOS pane of the system.svc editor. These fields will have some validation where invalid values will not be accepted and will need to be replaced by valid values in order to save or regenerate the configuration.

The following tables detail the value range for all of the free-form entry fields within the UI.

--------------

Macro Tables
============

Priorities
----------

+---------------------------------------+----------------+--------------------------------+
| Macro Name                            | Validator Type | Range                          |
+=======================================+================+================================+
| configMAX_PRIORITIES                  | int            | 0 - 100                        |
+---------------------------------------+----------------+--------------------------------+
| configTIMER_TASK_PRIORITY             | int            | 0 - (configMAX_PRIORITIES - 1) |
+---------------------------------------+----------------+--------------------------------+
| configMAX_CO_ROUTINE_PRIORITIES       | int            | 0 - 100                        |
+---------------------------------------+----------------+--------------------------------+
| configMAX_API_CALL_INTERRUPT_PRIORITY | int            | 0 - 100                        |
+---------------------------------------+----------------+--------------------------------+

--------------

Memory Allocation
-----------------

===================== ============== =======
Macro Name            Validator Type Range
===================== ============== =======
configTOTAL_HEAP_SIZE int            0 - 1GB
===================== ============== =======

--------------

Tasks & Synchronization
-----------------------

======================================= ============== ========
Macro Name                              Validator Type Range
======================================= ============== ========
configMAX_TASK_NAME_LEN                 int            0 - 32
configNUM_THREAD_LOCAL_STORAGE_POINTERS int            0 - 1024
configMINIMAL_STACK_SIZE                int            64KB
configUSE_TASK_NOTIFICATIONS            int            1024
configQUEUE_REGISTRY_SIZE               int            1024
======================================= ============== ========

--------------

Timers & Co-Routines
--------------------

============================ ============== =========
Macro Name                   Validator Type Range
============================ ============== =========
configTIMER_QUEUE_LENGTH     int            0 - 1000
configTIMER_TASK_STACK_DEPTH int            0 - 100KB
============================ ============== =========

--------------

RTOS Behaviour
--------------

================== ============== ============================
Macro Name         Validator Type Range
================== ============== ============================
configTICK_RATE_HZ int            0-100MHz
configCPU_CLOCK_HZ int            0-<max processor clock rate>
================== ============== ============================
