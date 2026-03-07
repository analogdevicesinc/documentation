µC/OS-III® to FreeRTOS Migration Guide
======================================

Introduction
------------

This page describes how to migrate the µC/OS-III to FreeRTOS for those customers who want to migrate their µC/OS-III-based application to FreeRTOS. You will find that migrating µC/OS-III Applications into FreeRTOS is quite straightforward and in most cases will requires just a few hours.

**Supported Boards**

Analog Devices **ADPS-SC5xx** \| **ADSP-215xx** \| **ADSP-BF7xx** series boards.

**The guide covers the following topics**:

.. container:: col2

   
   -  Source Code Organisation
   -  Interrupt Vector Table
   -  Critical sections
   -  Kernel-Aware Interrupts
   -  Initializing and Starting the OS
   -  Task Priorities
   -  Task Creation
   -  Task Delay
   -  Scheduler Lock/Suspend
   -  Semaphores and Mutexes
   -  Task Semaphores/Notifications
   -  Message Queues
   -  Task Message Queues
   -  Event Flags/Group
   -  Software Timers
   -  Full API Map
   


--------------

Source Code Organisation
------------------------

The folder structure for both µC/OS-III and FreeRTOS are shown below in Table 1. Simple replace the µC/OS-III source code with the files shown on the right column.

.. container:: column

   **uCOS-III**

   
   .. code:: bash
   
      uCOS-III
      ├── common
      │   ├── Templates
      │   │   ├── app_cfg.h
      │   │   ├── app_ucos3_cfg.h
      │   │   ├── os_app_hooks.c
      │   │   ├── os_app_hooks.h
      │   │   ├── os_cfg_app.h
      │   │   ├── os_cfg.h
      │   │   └── rom
      │   └── uCOS-III
      │       ├── os.h
      │       ├── Source
      │       │   ├── os_cfg_app.c
      │       │   ├── os_core.c
      │       │   ├── os_dbg.c
      │       │   ├── os_flag.c
      │       │   ├── os.h
      │       │   ├── os_int.c
      │       │   ├── os_mem.c
      │       │   ├── os_msg.c
      │       │   ├── os_mutex.c
      │       │   ├── os_pend_multi.c
      │       │   ├── os_prio.c
      │       │   ├── os_q.c
      │       │   ├── os_sem.c
      │       │   ├── os_stat.c
      │       │   ├── os_task.c
      │       │   ├── os_tick.c
      │       │   ├── os_time.c
      │       │   ├── os_tmr.c
      │       │   ├── os_type.h
      │       │   └── os_var.c
      │       └── TLS
      │           └── CCES
      │               └── os_tls.c
      ├── ARM-Cortex-A5
      │   └── uCOS-III
      │       └── Ports
      │           ├── os_adi_xx.x
      │           └── os_cpu_xx.x
      ├── Blackfin
      │   └── uCOS-III
      │       └── Ports
      │           ├── os_adi_xx.x
      │           └── os_cpu_xx.x
      └── SHARC
          └── uCOS-III
              └── Ports
                  ├── os_adi_xx.x
                  └── os_cpu_xx.x
   


.. container:: column

   **FreeRTOS**

   
   .. code:: bash
   
      FreeRTOS
      └── Source
          ├── croutine.c
          ├── event_groups.c
          ├── list.c
          ├── queue.c
          ├── stream_buffer.c                        (1-1)
          ├── tasks.c
          ├── timers.c
          ├── include
          │   ├── deprecated_definitions.h
          │   ├── message_buffer.h
          │   ├── stack_macros.h
          │   ├── stdint.readme
          │   ├── stream_buffer.h
          │   ├── croutine.h
          │   ├── event_groups.h
          │   ├── FreeRTOS.h                        (1-2)
          │   ├── list.h
          │   ├── mpu_prototypes.h
          │   ├── mpu_wrappers.h
          │   ├── portable.h
          │   ├── projdefs.h
          │   ├── queue.h
          │   ├── semphr.h
          │   ├── StackMacros.h
          │   ├── task.h
          │   └── timers.h
          └── portable
              ├── GCC
              │   └── ARM_CA9
              │       ├── portASM.S                 (2-1)
              │       ├── port.c
              │       └── portmacro.h
          └── CCES
                  ├── ARM_CA5
                  │   ├── dispatcher.c
                  │   ├── freertos.specs
                  │   ├── io_startup.c              (2-2)
                  │   ├── timer.c
                  │   └── vectors.S
                  ├── Blackfin_BF70x
                  │   ├── portASM.asm
                  │   ├── portASM.h                 (2-3)
                  │   ├── port.c
                  │   └── portmacro.h
                  └── SHARC_215xx
                      ├── portASM.asm
                      ├── portASM.h                 (2-4)
                      ├── port.c
                      └── portmacro.h
   


.. container:: Centeralign

   <fc #4682b4>\ **Table 1** Source Code Directory Structures</fc>



Like the µC/OS-III, the directory structure of FreeRTOS includes some files that implement the kernel core, other files implement specific kernel objects and services.The table annotations below describe the different groups

+-----------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Section               | Name                                                           | note                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+=======================+================================================================+================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| **``Section (1-1)``** | **FreeRTOS Source Code** ``processor-independent``             | Common and official source code providing the FreeRTOS general functionalities and features implementation about the ``Tasks`` ``Co-routines`` ``Queues/Mutexes/Semaphores`` ``Task Notifications`` ``Event Groups(or "Flags")`` ``Stream & Message Buffers`` and ``Software Timers``. All files in this directory should be included in the build. And features that are not required will be compiled out based on the value of #define constants in the configuration file FreeRTOSConfig.h |
+-----------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **``Section (1-2)``** | **FreeRTOS Header File** ``processor-independent``             | Header Files of the FreeRTOS common & official functionalities and features                                                                                                                                                                                                                                                                                                                                                                                                                    |
+-----------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **``Section (2-1)``** | **FreeRTOS Portable Code** ``proccessor-dependent, ARM``       | Portable folder allows the vendors to add the implementation codes to the functions of ``interrupt vector tables`` ``interrupt handlers`` ``critical section handling`` and ``context switch``, etc. based on the processor information                                                                                                                                                                                                                                                        |
+-----------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **``Section (2-2)``** | **FreeRTOS Portable Code** ``proccessor-dependent, Cortex A5`` | Support for the ADSP-SC5xx ``Cortex-A5`` Core                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+-----------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **``Section (2-3)``** | **FreeRTOS Portable Code** ``proccessor-dependent, Blackfin``  | Support for the ADSP-BF7xx ``BLACKFIN`` Core                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **``Section (2-4)``** | **FreeRTOS Portable Code** ``proccessor-dependent, SHARC``     | Support for the ADSP-215XX / ADSP-SC5xx ``SHARC`` Core                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+-----------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

--------------

Interrupt Vector Table
----------------------

Both µC/OS-III and FreeRTOS require two interrupt handlers that need to be installed in the Interrupt Vector Table(IVT).

-  **``PendSV Handler``**: Suspend system interrupt Vector
-  **``SysTick Handler``**: System tick timer interrupt Vector.

The **``Interrupt Vector Table``** is typically located at some known memory address (e.g. 0x00000000) and its default interrupt handlers are registered directly in some startup code in assembly language by the compiler.

This startup code is compiler-dependent and varies widely depending on the architecture and semiconductor manufacturer.

ADI provides the respective ``Interrupt Handler Vector Table`` for Processor ``BLACKFIN``, ``CORTEX-A5`` and ``SHARC`` on µC/OS-III and FreeRTOS listed in the following Table 2.

+------------------+----------------+------------------------+--------------------------------------------------------------------------------------------+
| IRQ Handler Name | Processor Name | µC/OS-III              | FreeRTOS                                                                                   |
+==================+================+========================+============================================================================================+
| **``PendSV``**   | ``CORTEX-A5``  | OS_CPU_PendSVHandler() | <fc #4682b4>FreeRTOS_IRQ_Handler()</fc> **[ in portASM.s ]**                               |
+------------------+----------------+------------------------+--------------------------------------------------------------------------------------------+
|                  | ``BACKFIN``    |                        | <fc #dda0dd>_xPortIVG14Handler()</fc> **[ in portASM.asm ]**                               |
+------------------+----------------+------------------------+--------------------------------------------------------------------------------------------+
|                  | ``SHARC``      |                        | <fc #6495ed>xPortSFT31Handler()</fc> \*\* [ in portASM.asm ]\ **\| \|**\ ``SysTick``\ \*\* |
+------------------+----------------+------------------------+--------------------------------------------------------------------------------------------+
|                  |                |                        |                                                                                            |
+------------------+----------------+------------------------+--------------------------------------------------------------------------------------------+

.. container:: Centeralign

   <fc #4682b4>\ **Table 2** Cortex-A5/Blackfin/SHARC IRQ Handlers</fc>



--------------

Critical Sections
-----------------

Both in the µC/OS-III and FreeRTOS, kernel needs to disable interrupts during the critical section, and below will show the functions used in µC/OS-III and FreeRTOS.

.. container:: column

   **µC/OS-III**

   
   All of the critical sections function macros that are currently protected by µC/OS-III :
   
   .. code:: c
   
      CPU_SR_ALLOC()
      CPU_CRITICAL_ENTER()
      CPU_CRITICAL_EXIT()
   


.. container:: column

   **FreeRTOS**

   
   These macros can be replaced with the equivalent in FreeRTOS macros as below:
   
   .. code:: c
   
      taskENTER_CRITICAL()
      taskEXIT_CRITICAL()
      taskENTER_CRITICAL_FROM_ISR()
      taskEXIT_CRITICAL_FROM_ISR()
   



FreeRTOS provides two sets of kernel control APIs for critical sections:

+-----------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| name                              | type                 | note                                                                                                                                                      |
+===================================+======================+===========================================================================================================================================================+
| ``taskENTER_CRITICAL()``          | ``Calling None-IRQ`` | In a Critical Sections are entered by calling ``taskENTER_CRITICAL()``, and subsequently exited by ``calling taskEXIT_CRITICAL()``                        |
+-----------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``taskEXIT_CRITICAL()``           |                      |                                                                                                                                                           |
+-----------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``taskENTER_CRITICAL_FROM_ISR()`` | ``Calling with IRQ`` | In an ISR Critical Sections are entered by calling ``taskENTER_CRITICAL_FROM_ISR()``, and subsequently exited by calling ``taskEXIT_CRITICAL_FROM_ISR()`` |
+-----------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``taskEXIT_CRITICAL_FROM_ISR()``  |                      |                                                                                                                                                           |
+-----------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                      |                                                                                                                                                           |
+-----------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

Note That the ``configMAX_SYSCALL_INTERRUPT_PRIORITY`` in the FreeRTOS configuration file when you use the above APIs, more detail can be found at `RTOS Kernel Control <https://www.freertos.org/a00020.html>`_.

**Example Usage**

.. container:: column

   **µC/OS-III**

   
   .. code:: c
   
      void MyFunction (void)
      {
          // Storage for SR register
          CPU_SR_ALLOC();
        
          // Create a critical section
          CPU_CRITICAL_ENTER();
              :
              :
              : // Code protected by critical sections ...
              :
              :
              :  // ... from interrupts or concurrent access.
              :     
              :
          // Exit the critical section
          CPU_CRITICAL_EXIT();
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: java
   
      void MyFunction_1 (void)   /** Called without ISR **/
      {
          /** Create a critical section **/
          taskENTER_CRITICAL();
            : /** Code protected by critical sections ...**/
          /** Exit the critical section **/
          taskEXIT_CRITICAL();
      }
       
      void MyFunction_2_FromISR (void)   /** Called from ISR **/
      {
      UBaseType_t uxSavedIrqStatus;
          /** Create a critical section **/
          uxSavedIrqStatus = taskENTER_CRITICAL_FROM_ISR();
           :  /**... from interrupts or concurrent access.**/
          /** Exit the critical section **/
          taskEXIT_CRITICAL_FROM_ISR( uxSavedIrqStatus );
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 3** Critical Sections</fc>



For more information on Critical Sections, see the full documentation of `RTOS Kernel Control <https://www.freertos.org/taskENTER_CRITICAL_taskEXIT_CRITICAL.html>`_ in FreeRTOS API Reference.

--------------

Kernel-Aware Interrupts
-----------------------

Interrupt Service Routines (ISRs) that need to notify a task are called Kernel Aware Interrupts (or KAI) and trigger the task context switching. When writing an interrupt handler function in your project, keep in mind that during an interrupt, if a ``semaphore``, ``event flag``, ``message queue``, or other functions that ``could trigger a task context switch`` was previously used in µC/OS-III, now you can call the corresponding API called ``xxx_FromIS`` in FreeRTOS (and please note that the corresponding API without "FromISR" is not allowed on ISR.).

If the following APIs are called in the interrupt handler function in µC/OS-III, please replace it with the\ ``xxx_FromISR`` API in FreeRTOS.

**µC/OS-III**

.. code:: c

   OSSemPost()
   OSFlagPost()
   OSQPost()
   OSTaskSemPost()
   OSTaskResume()

**FreeRTOS**

.. code:: c

   xSemaphoreGiveFromISR()
   xEventGroupSetBitsFromISR()
   xQueueSendFromISR()
   vTaskNotifyGiveFromISR()
   xTaskResumeFromISR()

**Example Usage**

Here is an example in using the Queue Send from an interrupt in µC/OS-III\ ``(left)`` and FreeRTOS\ ``(right)``.

.. container:: column

   **µC/OS-III**

   
   .. code:: c
   
      void My_IRQ_Handler (void)
      {
          // Save the CPU registers
          CPU_SR_ALLOC();
          // Protect a critical section
          CPU_CRITICAL_ENTER();
          // Make the kernel aware that
          // the interrupt has started
          OSIntEnter();
          CPU_CRITICAL_EXIT();
          // Handle the interrupt
              .
              .
              .
           OS___Post();
          // Make the kernel aware that
           // the interrupt has ended
          OSIntExit();
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c
   
      void My_IRQ_Handler (void)
      {
      char cIn;
      BaseType_t xHigherPrioTaskWoken;
       
       
          xHigherPrioTaskWoken = pdFALSE;
           
          /* Handle the interrupt */
           xQueueSendFromISR(
                              xRxQueue,
                              &cIn,
                              &xHigherPrioTaskWoken);
           
          if (xHigherPrioTaskWoken)
          {
              taskYIELD_FROM_ISR();
          }
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 4** Kernel Aware ISRs</fc>



**Deferred Interrupt Handling**

Generally, both for µC/OS-III and FreeRTOS, it is considered best practice to keep ISRs as short as possible. If there is a long-term response/pending in the IRS, The same as we called The tick task (OS_TickTask(), os_tick.c) and The ISR handler task (OS_IntQTask(), os_int.c) in the µC/OS-III, FreeRTOS also provides the ISR Handler mechanism called Deferred Interrupt Handling. Typically, it's to deliver the processing necessitated by the interrupt to be performed at a high priority unblocked task( High priority deferred interrupter handler task ), rather than within the ISR.

.. container:: column

   
   .. container:: Centeralign

      <fc #4682b4>**Diagram \*\* </fc>

   
   .. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/migration-guide/completing_interrupt_processing_in_a_high_priority_task.jpg
      :align: center
      :width: 800px
   
   .. container:: Centeralign

      <fc #4682b4>\ **Figure 1** Deferred Interrupt Processing</fc>

   
   The above diagram showing how the deferred interrupt process, which to trigger a high-priority task and complete interrupt processing in this high-priority task.
   


.. container:: column

   
   +--------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Time   | Name                    | Note                                                                                                                                                                                                                 |
   +========+=========================+======================================================================================================================================================================================================================+
   | ``t1`` | **task 1 running**      | A low priority task ``Task 1`` is running                                                                                                                                                                            |
   +--------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | ``t2`` | **Interrupt occurring** | The low priority task ``Task 1`` is pre-empted by an interrupt, an the ISR executes, handles the interrupting peripheral, clears the interrupt, then unblocks ``Task 2``                                             |
   +--------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | ``t3`` | **task 2 running**      | The ISR returns directly to a deferred processing task ``task 2`` that was unblocked from within the ISR. The majority of interrupt processing is performed within this unblocked task                               |
   +--------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | ``t4`` | **task 1 continue**     | The deferred processing task ``task 2`` that was unblocked by the ISR returns to the Blocked state to wait for the next interrupt, allowing the lower priority application task ``task 1`` to continue its execution |
   +--------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   



Here provides two categories of methods for users in using the Deferred Interrupt Handling:

-  **Unordered List ItemCentralised Deferred Interrupt Handling**: Centralised deferred interrupt handling is so called because each interrupt that uses this method executes in the context of the same RTOS daemon task
-  **Unordered List ItemApplication Controlled Deferred Interrupt Handling**: Application controlled deferred interrupt handling is so called because each interrupt that uses this method executes in the context of a task created by the application writer

For example, the function pvPortMalloc() is forbidden to be called at any Standard ISR Processing in FreeRTOS, but we can call it at the Deferred Interrupt Handling. For more information on Critical Sections, see the full documentation of `Deferred Interrupt Handling <https://www.freertos.org/deferred_interrupt_processing.html>`_.

--------------

Initializing and Starting the OS
--------------------------------

For both of the µC/OS-III and FreeRTOS, we need to use the corresponding function to start the Operating System (OS). The difference is that before calling any µC/OS-III function we need to initialize µC/OS-III by calling OSInit() and start multi-tasking by calling OSStart(), but at FreeRTOS, just call vTaskStartScheduler() to start the real-time scheduler after creating tasks and kernel objects.

**µC/OS-III**

APIs for initializing and starting the OS at µC/OS-III

.. code:: c++

   OSInit()
   OSStart()

**FreeRTOS**

API to start the OS at FreeRTOS:

.. code:: c++

   vTaskStartScheduler()

Typically, before the scheduler has been started, main() (or a function called by main()) will be executing. After the scheduler has been started, only tasks and interrupts will ever execute. Starting the scheduler causes the highest priority task that was created while the scheduler was in the Initialization state to enter the Running state.

**Example Usage**

.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      void main (void)
      {
      OS_ERR err;
          // Initialize µC/OS-III
          OSInit(&err);
        
          // Create tasks and other
          // kernel objects
          CreateTasksFun();
              .
              .
              .
          // Start Multitasking
          OSStart(&err);
          // Will not get here unless there is an error (check err)
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
      void main (void)
      {
          /* Create tasks and other */
          /* kernel objects */
          CreateTasksFun();
              .
              .
              .
          /* Start the scheduler  */
          vTaskStartScheduler();
          /* This code will only be reached if the idle task
             could not be created inside vTaskStartScheduler().
             An infinite loop is used to assist debugging by
             ensuring this scenario does not result in main()
             exiting. */
          for( ;; );
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 5** Starting the Kernels </fc>



For more information, please see the full documentation of `RTOS Kernel Control to Start Scheduler <https://www.freertos.org/a00132.html>`_ in FreeRTOS API Reference.

--------------

Task Priorities
---------------

In µC/OS-III, low priority numbers denote high priority tasks. On the other hand, a low-priority number corresponds to a low-priority level in FreeRTOS. Priority level zero (0) is thus the lowest priority level and priority configMAX_PRIORITIES - 1 is the highest priority level as shown in the following table.

.. container:: column

   **Task Priority Leve**

   
   Both kernels have the Idle task at the lowest priority level. As same as the µC/OS-III changing the task's priority via the API ``OSTaskChangePrio()``, FreeRTOS also provides to queries or changes the priority of a task by calling the corresponding API Functions ``uxTaskPriorityGet()`` or ``vTaskPrioritySet()`` when the system is running.


.. container:: column

   
   ======== ======================= ============================
   Level    µC/OS-III               FreeRTOS
   ======== ======================= ============================
   ``LOW``  ``OS_CFG_PRIO_MAX - 1`` ``0``
   ``HIGH`` ``0``                   ``configMAX_PRIORITIES - 1``
   \                                
   ======== ======================= ============================
   
   .. container:: Centeralign

      <fc #4682b4>\ **Table 6** Task Priority Levels </fc>

   



**µC/OS-III**

.. code:: c++

   OSTaskChangePrio()

**FreeRTOS**

.. code:: c++

   uxTaskPriorityGet()
   vTaskPrioritySet()

Please find the examples in using these APIs at the full documentations `uxTaskPriorityGet() <https://www.freertos.org/a00128.html>`_ and `vTaskPrioritySet() <https://www.freertos.org/a00129.html>`_ of Task Control.

.. tip::

   Both of µC/OS-III and FreeRTOS support **multiple tasks at the same priority level**. For more information on task priorities in FreeRTOS see the full documentation on `Task Priorities <https://freertos.org/RTOS-task-priority.html>`_ of the FreeRTOS Feature/Tasks.


--------------

Task Creation
-------------

In both µC/OS-III and FreeRTOS , tasks are written as an infinite loop function or, as a function that deletes the task once completed.

.. container:: column

   **common**

   
   Both µC/OS-III and FreeRTOS tasks support passing an argument to the task when it’s created and this argument is declared as a void \*. In other words, you do not need to change the function prototype of your task functions.


.. container:: column

   **difference**

   
   ``In µC/OS-III``: Kernel Objects are created statically only. They can be allocated dynamically but the functionality is not built-in µC/OS-III. Instead, you would need to allocate them in the Micrium Heap by using the Memory Module in µC/LIB.
   
   ``In FreeRTOS``: Kernel Objects such as tasks, queues, semaphores and mutexes can be created either statically or by dynamically allocating them in FreeRTOS’s heap.



.. container:: col2

   
   =============================== ================== ==================
   Supported feature               µC/OS-III          FreeRTOS
   =============================== ================== ==================
   Passing an argument to the task <fc #4682b4>✔</fc> <fc #4682b4>✔</fc>
   Static RTOS memory Allocation   <fc #4682b4>✔</fc> <fc #4682b4>✔</fc>
   Dynamic RTOS memory Allocation  <fc #ff0000>✘</fc> <fc #4682b4>✔</fc>
   =============================== ================== ==================
   
   This means that any of the kernel objects in your µC/OS-III project were created statically, when migrating them to FreeRTOS with the similar API functions, **two methods** of allocating them from the Heap ``statically`` or ``dynamically`` can be used in FreeRTOS.
   
   And more detail about the FreeRTOS memory allocation can be found in `Memory Management <https://www.freertos.org/a00111.html>`_.
   



For example, to migrate your tasks, locate in your project all the places where a task gets created by µC/OS-III ``OSTaskCreate()``, The equivalent API functions in FreeRTOS are/is ``xTaskCreate()`` and/or ``xTaskCreateStatic()``.

**µC/OS-III**

.. code:: c++

   OSTaskCreate()
   OSTaskDel()

**FreeRTOS**

.. code:: c++


   xTaskCreate()
   xTaskCreateStatic()
   vTaskDelete()

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| name                     | note                                                                                                                                                                                                                                                                                                                                                                                                                         |
+==========================+==============================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``xTaskCreate()``        | Create a new task and add it to the list of tasks that are ready to run. **configSUPPORT_DYNAMIC_ALLOCATION** must be set to **``1``** in FreeRTOSConfig.h, or left **``undefined``** (in which case it will default to 1), for this RTOS API function to be available.                                                                                                                                                      |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ''xTaskCreateStatic() '' | Create a new task and add it to the list of tasks that are ready to run. **configSUPPORT_STATIC_ALLOCATION** must be set to **``1``** in FreeRTOSConfig.h for this RTOS API function to be available. If a task is created using ``xTaskCreateStatic()`` then the RAM is provided by the application writer, which results in a greater number of parameters, but allows the RAM to be statically allocated at compile time. |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vTaskDelete()``        | **INCLUDE_vTaskDelete** must be defined as **``1``** for this function to be available. calling this function will remove a task from the RTOS kernels management. The task being deleted will be removed from all ``ready``, ``blocked``, ``suspended`` and ``event`` lists.                                                                                                                                                |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example Usage**

.. container:: column

   **µC/OS-III**

   
   .. code:: java
   
      #define MY_TASK_PRIORITY 5
      #define MY_TASK_STK_SIZE 200
       
      OS_TCB MyTaskTCB;
      CPU_STK MyTaskStk[MY_TASK_STK_SIZE];
       
      void MyTaskCode (void *p_arg)
      {
          while (DEF_ON) {
          // Wait for an event (i.e. Pend)
          // Task code goes here
          }
      }
       
      void MyInitFunction (void)
      {
          OS_ERR err;
          
          // Create a user application task 
          OSTaskCreate (
              &MyTaskTCB,
              "Task Name Here",
              MyTaskCode,
              (void *)0,
              MY_TASK_PRIORITY,
              &MyTaskStk[0],
              MY_TASK_STK_SIZE / 10,
              MY_TASK_STK_SIZE,
              0,
              0,
              (void *)0,
              OS_OPT_TASK_STK_CHK +
              OS_OPT_TASK_STK_CLR,
              &err);
              
              // Check “err”
              :
              :
              :
              :
              :
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: java
   
      #define MY_TASK_PRIORITY 5
      #define MY_TASK_STK_SIZE 200
       
      StaticTask_t MyTaskTCB;
      StackType_t MyTaskStk[MY_TASK_STK_SIZE];
       
      void MyTaskCode (void *pvParameters)
      {
          for (;;) {
          /* Wait for an event */
          /* Task code goes here */
          }
      }
       
      void MyInitFunction(void)
      {
      BaseType_t xReturned;
      TaskHandle_t xHandle = NULL;
           
          /** Method 1 to Create the task static **/
          xHandle = xTaskCreateStatic(
                          MyTaskCode,        
                          "Task Name Here",
                          MY_TASK_STACK_SIZE,
                          ( void * ) 1,      
                          MY_TASK_PRIORITY,  
                          MyTaskStk,         
                          &MyTaskTCB);       
       
          /** Method 2 to Create the task **/
          xReturned = xTaskCreate(
                          MyTaskCode,        
                          "Task Name Here",  
                          MY_TASK_STACK_SIZE,
                          ( void * ) 1,      
                          MY_TASK_PRIORITY,  
                          &xHandle );  
          if( xReturned == pdPASS )
          {
              vTaskDelete( xHandle );
          }  
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 7** Task Creation </fc>



For more information on the task creation, see the full documentation of `Task Creation <https://www.freertos.org/a00019.html>`_ in FreeRTOS API Reference.

--------------

Task Delay
----------

Just like in µC/OS-III, you can delay a task with FreeRTOS for a certain number of ticks. In both of µC/OS-III and FreeRTOS the delay can either be ``relative`` (delay from current time), ``periodic`` (delay occurs at fixed intervals) or ``absolute`` (delay until we reach some time). The actual delay time depends on the tick rate. The API functions usage and introduction in the two OS are as follows.

**µC/OS-III**

.. code:: c++

   OSTimeDly()
   OSTimeDlyHMSM()             
   OSTimeDlyResume()

Typically, in µC/OS-III, the Task delay modes (Relative, periodic or absolute) can be selected by inputting the parameter opt of ``OSTimeDly()`` or ``OSTimeDlyHMSM()``.

**FreeRTOS**

.. code:: c++

   vTaskDelay()
   vTaskDelayUntil()
   xTaskAbortDelay()

+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| name                  | note                                                                                                                                                                                                                                                                                                               |
+=======================+====================================================================================================================================================================================================================================================================================================================+
| ``vTaskDelay()``      | define **INCLUDE_vTaskDelay** as **``1``** to enable this function. It delays a task for a given number of ticks and the task's actual blocked time depends on the tick rate. Also ``vTaskDelay()`` specifies a time at which the task wishes to unblock relative to the time at which ``vTaskDelay()`` is called. |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vTaskDelayUntil()`` | define **INCLUDE_vTaskDelayUntil** as **``1``** to enable this function. It delays a task until a specified time and can be used by periodic tasks to ensure a constant execution frequency. unlike the ``vTaskDelay``, ``vTaskDelayUntil()`` specifies an absolute time at which the task wishes to unblock.      |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xTaskAbortDelay``   | define **INCLUDE_xTaskAbortDelay** as **``1``** to enable this function. Forces a task to leave the ``Blocked`` state, and enter the ``Ready`` state, even if the event the task was in the ``Blocked`` state to wait for has not occurred, and any specified timeout has not expired.                             |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example Usage**

The following example shows a task that toggles a LED every 500ms. The 500ms delay starts from the moment the API is called (``relative``).

.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      void MyTaskFunction (void *p_arg)
      {
          OS_ERR err;
          const OS_TICK delay = 500;  // 500ms Delay.
       
          while (DEF_ON) {
              BSP_TOGGLE_LED(LED2);   // Toggle LED2.
       
              OSTimeDly(delay,        // Block task for 500ms.
                        OS_OPT_TIME_DLY,
                        &err);
       
              if (err != OS_ERR_NONE) {
                 // Handle the error
              }
          }
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
      void MyTaskFunction(void * pvParameters)
      {
      /* Block for 500ms. */
      const TickType_t xDelay = 500 / portTICK_PERIOD_MS;
       
          for (;;)
          {
              /* Simply toggle the LED every 500ms,
        * blocking between each toggle.
               */
              BSP_TOGGLE_LED(LED2);
               
              /* Block task for 500ms. */
              vTaskDelay( delay );
          
          }
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 8** Task Delay - Relative </fc>



If you want to delay a task for an absolute time, then you can use the API vTaskDelayUntil() to replace vTaskDelay(), The other option is a periodic delay as shown in the following example(``periodic``).

.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      void MyTaskFunction (void *p_arg)
      {
          OS_ERR err;
          const OS_TICK period = 100;
       
          while (DEF_ON) {
              // Toggle LED2.
              BSP_TOGGLE_LED(LED2);
       
              // Wait for the next cycle.
              OSTimeDly(period,
                        OS_OPT_TIME_PERIODIC,
                        &err);
       
              if (err != OS_ERR_NONE) {
                  // Handle the error
              
              }
          }
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
   
      void MyTaskFunction( void * pvParameters )
      {
      TickType_t xLastWakeTime;
      /* Perform an action every 100 ticks. */
      const TickType_t xFrequency = 100;
   
          /* Initialise "xLastWakeTime" with current time. */
          xLastWakeTime = xTaskGetTickCount();
       
          for( ;; )
          {
             /* Toggle LED2.*/
             BSP_TOGGLE_LED(LED2);
               
             /* Wait for the next cycle.*/
             vTaskDelayUntil( &xLastWakeTime, xFrequency );
             
             /* Perform action here.*/
          }
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 9** Task Delay - Periodic </fc>



More about the Task Delay in FreeRTOS can be found at the Section of `Task Control <https://www.freertos.org/a00127.html>`_ of API Reference.

--------------

Task Suspend
------------

Both of the µC/OS-III and FreeRTOS provide to Suspend and Resume the tasks by calling the relevant function interface. The suspended task is invisible for the scheduler, so it will never available until it is Resumed.

**µC/OS-III**

.. code:: c++

   OSTaskSuspend()
   OSTaskResume()

**FreeRTOS**

In FreeRTOS, the corresponding APIs called with/without ISR for controlling tasks suspend/resume are provided as below:

.. code:: c++

   vTaskSuspend()
   vTaskResume()
   xTaskResumeFromISR()

+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| name                     | note                                                                                                                                                                                              |
+==========================+===================================================================================================================================================================================================+
| ``vTaskSuspend()``       | define **INCLUDE_vTaskSuspend** as **``1``** to enable this function. Suspend any task and when suspended a task will never get any microcontroller processing time, no matter what its priority. |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vTaskResume()``        | define **INCLUDE_vTaskSuspend** as **``1``** to enable this function. Resumes a suspended task that has been suspended by one or more calls to ``vTaskSuspend()``.                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xTaskResumeFromISR()`` | define **INCLUDE_vTaskSuspend** and **INCLUDE_xTaskResumeFromISR** as **``1``** to enable this function. Function to resume a suspended task that can be called from within an ISR.               |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example Usage**

.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      OS_TCB   Task_1_TCB;
   
      void main( void )
      {
          // Create a user application task 
          OSTaskCreate (
              &Task_1_TCB,
              "Task_1",
              Task_1,
              ...
              &err);
      }
   
      void Task_1 (void *p_arg)
      {
        OS_ERR  err;
   
        (void)&p_arg;
        while (DEF_ON) {
            // ...
            
            /* Suspend current task Task_1*/
            OSTaskSuspend((OS_TCB *)0, &err);       
   
            /* Check “err” */
            // ...
        }
      }
   
      void Task_2 (void *p_arg)
      {
        OS_ERR err;
        
        (void)&p_arg;
        while (DEF_ON) {
            // ...
            
            /* Resume suspended task Task_1 */
            OSTaskResume(&Task_1_TCB, &err);
   
            /* Check “err” */
            // ...
   
            // ...
        }
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
      TaskHandle_t xHandleTask_1;
   
      void main( void )
      {
          // Create a task, storing the handle.
          xTaskCreate( vTask_1,
                   "Task_1",
               STACK_SIZE,
               NULL,
               tskIDLE_PRIORITY,
               &xHandleTask_1 );
      }
   
      void vTask_1( void * pvParameters  )
      {
          ( void ) pvParameters;
          for( ; ; )
          {
             // ...
             
             // Suspend current task vTask_1
             
             /* The created task will not run during
        * this period, unless another task calls
        * vTaskResume( xHandleTask_1 ). */ 
             vTaskSuspend( NULL );
          }
      }
   
      void vTask_2( void * pvParameters  )
      {
          ( void ) pvParameters;
          for( ; ; )
          {
             // ...
             
             // Resume the suspended task vTask_1.
             vTaskResume( xHandleTask_1 );
             
             /* The created task will once again get
        * microcontroller processing time in accordance
        * with its priority within the system. */
             
             // ...
          }
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 10** Task Suspend </fc>



For more information about the FreeRTOS task suspend and resume, please see the full documentation of `Task Control <https://www.freertos.org/a00130.html>`_ in FreeRTOS API Reference.

--------------

Scheduler Lock/Suspend
----------------------

Both µC/OS-III and FreeRTOS allow a task to retain control of the CPU and suspend the remaining tasks (or lock the scheduler so that context switches will not occur until the scheduler is unlocked) even though other higher-priority tasks are ready-to-run. However but interrupts are still recognized and serviced (assuming interrupts are enabled).

**µC/OS-III**

.. code:: c++

   OSSchedLock()
   OSSchedUnlock()

**FreeRTOS**

.. code:: c++

   vTaskSuspendAll()
   xTaskResumeAll()

+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| name                  | note                                                                                                                                                                                                            |
+=======================+=================================================================================================================================================================================================================+
| ``vTaskSuspendAll()`` | Suspends the scheduler without disabling interrupts. RTOS ticks that occur while the scheduler is suspended will be held pending until the scheduler has been unsuspended using a call to ``xTaskResumeAll()``. |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xTaskResumeAll()``  | Resumes the scheduler after it was suspended using a call to ``vTaskSuspendAll()``.                                                                                                                             |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. container:: col1

   
   .. tip::

      API functions that have the potential to cause a context switch (for example, Task delay, Queue/message blocking send, etc.) must not be called while the scheduler is locked/suspended.

   
   .. tip::

      **xTaskResumeAll()** only resumes the scheduler. It does not unsuspend tasks that were previously suspended by a call to **vTaskSuspend()**.

   


**Example Usage**

.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      void MyTaskFunction(void *p_arg)
      {
          OS_ERR  err;
          (void)&p_arg;
          while (DEF_ON) {
           /* Task code goes here. */
                 :
            /* Prevent other tasks to run */
            OSSchedLock(&err);
            /* Check “err” */
            
            /* Code protected from context switch */
                      :
                      :
                      :
            /* Enable other tasks to run */
            OSSchedUnlock(&err);
            /* Check “err” */
              :
              :
            }
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
      void vMyTaskFunction( void * pvParameters )
      {
          for( ;; )
          {
            // Task code goes here.
            
            // ...
            
            // Prevent the RTOS kernel swapping out the task.
            vTaskSuspendAll();
   
            /* Code protected from context switch 
        * During this time interrupts will still
        * operate and the RTOS kernel tick count
        * will be maintained. */
            
             // ...
             
             // Operation is complete. Restart the RTOS kernel.
             xTaskResumeAll();
           }
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 11** Scheduler Suspend </fc>



.. note::

   At some point the task wants to perform a long operation during which it does not want to get swapped out. It cannot use **taskENTER_CRITICAL()** or **taskEXIT_CRITICAL()** as the length of the operation may cause interrupts to be missed - including the ticks, so you can use the scheduler suspend/lock API **vTaskSuspendAll()** and **xTaskResumeAll()** in this moment.


For more information about the FreeRTOS ``vTaskSuspendAll()`` and ``xTaskResumeAll()``, please see the full documentation of `RTOS Kernel Control <https://www.freertos.org/a00134.html>`_ in FreeRTOS API Reference.

--------------

Semaphores and Mutexes
----------------------

Both of the µC/OS-III and FreeRTOS, the **Semaphores and Mutexes** APIs are shared and visible to all tasks, they can be divided into 3 types of semaphores including ``Binary Semaphore``, ``Counting Semaphore`` and ``Mutex``, FreeRTOS also provides the APIs of ``Recursive Mutex``.

+------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| type       | name                   | µC/OS-III                                                                                                                                                                                                                                              | FreeRTOS                                                                                              |
+============+========================+========================================================================================================================================================================================================================================================+=======================================================================================================+
| Semaphores | ``Binary Semaphore``   | Binary and Counting semaphores are implemented through a single set of API functions that start with the prefix ``OSSem_XXX()``, and via the argument ``<fc #4682b4>OS_SEM_CTR</fc> cnt`` to distinguish this is called a binary or counting semaphore | FreeRTOS uses the APIs with ``xSemaphoreCreateBinary_XXX()`` to create the Binary Semaphores.         |
+------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|            | ``Counting Semaphore`` |                                                                                                                                                                                                                                                        | FreeRTOS uses the APIs with the ``xSemaphoreCreateCounting_XXX()`` to create the Counting Semaphores. |
+------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Mutexes    | ``Mutex``              | mutexes are implemented through a separate set of API functions that start with the prefix ``OSMutex_xxx()``                                                                                                                                           | FreeRTOS uses the APIs with ``xSemaphoreCreateMutex_XXX()`` to create the Mutexes.                    |
+------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|            | ``Recursive Mutex``    | <fc #ff0000>✘</fc>                                                                                                                                                                                                                                     | FreeRTOS use the APIs with ``xSemaphoreCreateRecursiveMutex_XXX()`` to create the Recursive Mutexes   |
+------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
|            |                        |                                                                                                                                                                                                                                                        |                                                                                                       |
+------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

**µC/OS-III**

Kernel Semaphore/Mutex APIs in µC/OS-III

.. code:: c++

   /*Kernel Semaphore API*/
   OSSemCreate()       
   OSSemDel()         
   OSSemPend()         
   OSSemPendAbort()   
   OSSemPost()  
   OSSemSet()
   /*Kernel Mutex API*/
   OSMutexCreate()     
   OSMutexDel()       
   OSMutexPend()      
   OSMutexPendAbort()  
   OSMutexPost()

**FreeRTOS**

Kernel Semaphore/Mutex APIs in FreeRTOS

.. code:: c++

   /*Binary Semaphore Create.*/
   xSemaphoreCreateBinary();
   xSemaphoreCreateBinaryStatic();
   /*Counting Semaphore Create.*/
   xSemaphoreCreateCounting()
   xSemaphoreCreateCountingStatic()
   /*Mutex Create*/
   xSemaphoreCreateMutex()            
   xSemaphoreCreateMutexStatic()  
   /*Recursive Mutex Create.*/
   xSemaphoreCreateRecursiveMutex()     
   xSemaphoreCreateRecursiveMutexStatic()
   /*All Semaphores/Mutexes share the same delete function.*/
   vSemaphoreDelete()
   /*Semaphores/Mutexes Take/Give.*/
   xSemaphoreTake()
   xSemaphoreGive()
   /*Semaphores/Mutexes Take/Give from ISR.*/
   xSemaphoreTakeFromISR()
   xSemaphoreGiveFromISR()
   /*Mutexes Take/Give Recursive.*/
   xSemaphoreTakeRecursive()
   xSemaphoreGiveRecursive()
   /*Others.*/
   xSemaphoreGetMutexHolder() 
   uxSemaphoreGetCount()

In FreeRTOS, ``Binary Semaphore``, ``Counting Semaphore``, ``Mutex`` and ``Recursive Mutex`` all share the same API functions except for the ones to create the actual objects. More about the `Semaphore/Mutexes <https://www.freertos.org/a00113.html>`_ in FreeRTOS can be found at the Section of Semaphore/Mutexes of API Reference.

**Example Usage**

The following example shows how to protect a shared resource with a mutex.

.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      OS_MUTEX MyMutex;
       
      void MyInitFunction( void )
      {
          OS_ERR err;
          OSMutexCreate(&MyMutex,
                        "Mutex Name Here",
                        &err);
      }
       
       
      void MyTaskCode( void *p_arg )
      {
          OS_ERR err;
          CPU_TS ts;
          while (DEF_ON) {
              // Acquire the mutex
              OSMutexPend(&MyMutex,
                          0,
                          OS_OPT_PEND_BLOCKING,
                          &ts,
                          &err);
                       
              if (err == OS_ERR_NONE) {
                  // We now have the mutex and can
                  // access the shared resource.
                      .
                      .
                      .
                  // We have finished accessing
                  // the shared resource.
                  // Now we can free the mutex.
                  OSMutexPost(&MyMutex,
                              OS_OPT_POST_NONE,
                              &err);
              }
          }
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
      SemaphoreHandle_t MyMutex = NULL;
       
      void MyInitFunction( void )
      {
          MyMutex = xSemaphoreCreateMutex();
          if(MyMutex == NULL)
          {
              /* Create the Semaphore Error.*/
          }
      }
       
      void MyTaskCode( void *pvParameters )
      {
          for ( ;; )
          {
              /* Acquire the mutex */
              if (xSemaphoreTake( MyMutex,
                                  (TickType_t)0) )
              {
                  /* We now have the mutex and can */
                  /* access the shared resource.*/
                      .
                      .
                      .
                  /* We have finished accessing the*/
                  /* shared resource.*/
                  /* Now we can free the mutex.*/
                  if( xSemaphoreGive(MyMutex) != pdPASS )
                  {
                      /* Give semaphore Error. */
                  }
                  else
                  {
                      /* Give semaphore Correct.*/
                  }
              }
          }
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 12** Protecting a Shared Resource with a Mutex </fc>



More examples in using the FreeRTOS Kernel Semaphores and Mutexes can be found in the :doc:`FreeRTOS Add-In Example Projects </wiki-migration/resources/tools-software/freertos/freertos-addin/examples>` .

--------------

Task Semaphores/Notifications
-----------------------------

**µC/OS-III**

In µC/OS-III, for the Task Semaphore APIs, each task has its own built-in semaphore, that in those cases where your code knows which task to signal, makes for a simpler and more efficient code than using a separate semaphore object. The API functions for Task Semaphores start with the prefix OSTaskSemXXX().

.. code:: c++

   /*OS Task Semaphore API.*/
   OSTaskSemPend()
   OSTaskSemPendAbort()
   OSTaskSemPost()
   OSTaskSemSet()

**FreeRTOS**

Corresponding to the µC/OS-III Task Semaphore APIs is the Task Notifications Feature. Each FreeRTOS task has a 32-bit notification value which is initialized to zero when the RTOS task is created. An RTOS task notification is an event sent directly to a task that can unblock the receiving task, and optionally update the receiving task’s notification value.

.. code:: c++

   xTaskNotifyGive()
   vTaskNotifyGiveFromISR()
   ulTaskNotifyTake()
   xTaskNotify()
   xTaskNotifyStateClear()

More about the Task Notifications in FreeRTOS can be found at the Section of `Direct To Task Notifications <https://www.freertos.org/RTOS-task-notification-API.html>`_ of API Reference.

--------------

Message Queues
--------------

Both kernels support inter-task communication, which allows a task or ISR to communicate information to another task.

.. container:: column

   The difference between the µC/OS-III and FreeRTOS message queue functionality is that in µC/OS-III the data sent must remain in scope, because it is sent by reference instead of by value, but in FreeRTOS, the data sent no need to be remain in scope. In other words, unlike the µC/OS-III, FreeRTOS enables the data sent to be copied via the buffer or a pointer.


.. container:: column

   
   +--------------------------------------------+--------------------+--------------------+
   | type                                       | µC/OS-III          | FreeRTOS           |
   +============================================+====================+====================+
   | ``Send/Recv Data from a Task``             | <fc #4682b4>✔</fc> | <fc #4682b4>✔</fc> |
   +--------------------------------------------+--------------------+--------------------+
   | ``Send/Recv Data from an ISR``             | <fc #4682b4>✔</fc> | <fc #4682b4>✔</fc> |
   +--------------------------------------------+--------------------+--------------------+
   | ``No-need-remain (in scope) Data sending`` | <fc #ff0000>✘</fc> | <fc #4682b4>✔</fc> |
   +--------------------------------------------+--------------------+--------------------+
   



**µC/OS-III**

.. code:: c++

   OSQCreate()
   OSQDel()
   OSQFlush()
   OSQPend()
   OSQPendAbort()
   OSQPost()

**FreeRTOS**

Mainly queue APIs in FreeRTOS.

.. code:: c++

   xQueueCreate()
   xQueueCreateStatic()
   vQueueDelete()
   xQueueSend()
   xQueueSendToBack()
   xQueueSendToFront()
   xQueueReceive()
   uxQueueMessagesWaiting()
   uxQueueSpacesAvailable()
   xQueueReset()
   xQueueOverwrite()
   xQueuePeek()
   vQueueAddToRegistry()
   vQueueUnregisterQueue()
   pcQueueGetName()
   /*APIs with ISR*/
   xQueueSendFromISR()
   xQueueSendToBackFromISR()
   xQueueSendToFrontFromISR()
   xQueueReceiveFromISR()
   uxQueueMessagesWaitingFromISR()
   xQueueOverwriteFromISR()
   xQueuePeekFromISR()
   xQueueIsQueueFullFromISR()
   xQueueIsQueueEmptyFromISR()

.. container:: col2

   
   +------------------------------+---------------------------------------------------------------------------------------------+
   | name                         | note                                                                                        |
   +==============================+=============================================================================================+
   | ``xQueueCreate()``           | Creates a new queue and returns a handle by which the queue can be referenced.              |
   +------------------------------+---------------------------------------------------------------------------------------------+
   | ``vQueueDelete()``           | Delete a queue – freeing all the memory allocated for storing of items placed on the queue. |
   +------------------------------+---------------------------------------------------------------------------------------------+
   | ``xQueueSend()``             | Post an item on a queue.                                                                    |
   +------------------------------+---------------------------------------------------------------------------------------------+
   | ``xQueueSendToBack()``       | Post an item to the back of a queue                                                         |
   +------------------------------+---------------------------------------------------------------------------------------------+
   | ``xQueueSendToFront()``      | Post an item to the front of a queue.                                                       |
   +------------------------------+---------------------------------------------------------------------------------------------+
   | ``xQueueReceive()``          | Receive an item from a queue.                                                               |
   +------------------------------+---------------------------------------------------------------------------------------------+
   | ``uxQueueMessagesWaiting()`` | Return the number of messages stored in a queue.                                            |
   +------------------------------+---------------------------------------------------------------------------------------------+
   | ``uxQueueSpacesAvailable()`` | Return the number of free spaces in a queue.                                                |
   +------------------------------+---------------------------------------------------------------------------------------------+
   
   +-----------------------------+--------------------------------------------------------------------------------------------------------+
   | name                        | note                                                                                                   |
   +=============================+========================================================================================================+
   | ``xQueueReset()``           | Resets a queue to its original empty state.                                                            |
   +-----------------------------+--------------------------------------------------------------------------------------------------------+
   | ``xQueueOverwrite()``       | Will write to the queue even if the queue is full, overwriting data that is already held in the queue. |
   +-----------------------------+--------------------------------------------------------------------------------------------------------+
   | ``xQueuePeek()``            | Receive an item from a queue without removing the item from the queue.                                 |
   +-----------------------------+--------------------------------------------------------------------------------------------------------+
   | ``vQueueAddToRegistry()``   | Assigns a name to a queue and adds the queue to the registry.                                          |
   +-----------------------------+--------------------------------------------------------------------------------------------------------+
   | ``vQueueUnregisterQueue()`` | Removes a queue from the queue registry.                                                               |
   +-----------------------------+--------------------------------------------------------------------------------------------------------+
   | ``pcQueueGetName ()``       | Look up a queue name from the queue’s handle.                                                          |
   +-----------------------------+--------------------------------------------------------------------------------------------------------+
   



For a more detailed description of each of the arguments/usage for the above FreeRTOS Queue APIs, please see the full documentation on the `Queues <https://www.freertos.org/Embedded-RTOS-Queues.html>`_ and `Queue Management <https://www.freertos.org/a00018.html>`_ section of FreeRTOS API Reference.

**Example Usage**

.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      #define BUFFER_SIZE 128
      OS_Q My_UART_Q;
      OS_MEM My_UART_MemPartition;
      char My_UART_Buffer[BUFFER_SIZE];
       
      void My_UART_RxTaskCode (void *p_arg)
      {
          OS_ERR err;
          void *p_msg;
          OS_MSG_SIZE msg_size;
          CPU_TS ts;
        
          // Create a memory pool of 128 bytes
          OSMemCreate(&My_UART_MemPartition,
                      "UART Memory Pool",
                      (void *)&My_UART_Buffer[0],
                      BUFFER_SIZE,
                      1,
                      &err);
          if (err != OS_ERR_NONE) {
              // Handle the error
          }
        
          // Create a Q of 128 pointers
          OSQCreate(&My_UART_Q,
                    "Queue name here",
                    BUFFER_SIZE,
                    &err);
          if (err != OS_ERR_NONE) {
              // Handle the error
          } else {
              // Enable UART interrupts
          }
        
          while (1) {
              // Receive a message from the queue.
              // Block for 10-ticks if queue is empty.
              p_msg = (char *)OSQPend(&My_UART_Q,
                                      10,
                                      OS_OPT_PEND_BLOCKING,
                                      &msg_size,
                                      &ts,
                                      &err);
              if (err == OS_ERR_NONE) {
                  // Process the received byte p_msg
                  // Put p_msg back to the memory pool
                  OSMemPut(&My_UART_MemPartition,
                           p_msg,
                           &err);
              } else {
                  // Handle the error
              }
          }
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
      #define BUFFER_SIZE 128
       
      QueueHandle_t My_UART_Q;
       
       
      void My_UART_RxTaskCode (void *pvParameters)
      {
      char *pxRxedMessage;
           
          /* Create a Q capable of containing 128 bytes */
          My_UART_Q = xQueueCreate( BUFFER_SIZE,
                                    1 );
          if (My_UART_Q == pdFAIL)
          {
              /* Failed to create the queue. */
          }
          else
          {
              /* Enable UART interrupts */
                   .
                   .
                   .
          }
           
       
       
       
       
       
       
       
       
       
       
          for ( ;; )
          {
              /* Receive a message from the queue.*/
              /* Block for 10-ticks if queue is empty.*/
              if( xQueueReceive( My_UART_Q,
                                 &(pxRxedMessage),
                                 (TickType_t)10) )
              {
                  /* Process the received byte. */
                   .
                   .
                   .
                   .
              }
              else
              {
                  /* Handle the error */
              }
          }
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 13-1** Inter-task Communication - Tasks </fc>



.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      char *My_UART_RxDataPtr;
       
      void My_UART_IRQ_Handler(void)
      {
          OS_ERR err;
          char rx_data;
          // Storage for the SR register
          CPU_SR_ALLOC();
          // Protect a critical section
          CPU_CRITICAL_ENTER();
           
          // Make the kernel aware that
          // the interrupt has started
          OSIntEnter();
           
          CPU_CRITICAL_EXIT();
           
          // Loop until the buffer is empty
          do
          {
              // Obtain a byte from the UART
              rx_data = UART_RX_REGISTER;
              My_UART_RxDataPtr =
                  (char *)OSMemGet(&My_UART_MemPartition, &err);
               
              *My_UART_RxDataPtr++ = rx_data;
               
              // Post byte to task for processing
              OSQPost((OS_Q *)&My_UART_Q,
                      (void *)My_UART_RxDataPtr,
                      (OS_MSG_SIZE)1,
                      (OS_OPT )OS_OPT_POST_FIFO,
                      (OS_ERR *)&err);
               
              // Don't point to sent buffer
              My_UART_RxDataPtr = NULL;
          } while (UART_RX_BUFFER_COUNT);
           
          // Make the kernel aware that
          // the interrupt has ended
          OSIntExit();
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
      QueueHandle_t xQueue;
       
      void My_UART_IRQ_Handler(void)
      {
      char rx_data;
      BaseType_t xHigherPriorityTaskWoken;
      xHigherPriorityTaskWoken = pdFALSE;
   
          // Loop until the buffer is empty.
          do
          {
            // Obtain a byte from the UART.
            rx_data = UART_RX_REGISTER;
       
            // Post byte to task for processing.
            xQueueSendToBackFromISR(xQueue,
                                    &rx_data,
                                    &xHigherPriorityTaskWoken);
                                        
            //A character was received and output it now.
            vOutputCharacter( rx_data );
                 :
                 :
                 :
            /* If removing the character from the queue woke
            the task that was posting onto the queue xHigher-
            PriorityTaskWoken will have been set to pdTRUE.
            No matter how many times this loop iterates only
            one task will be woken.*/
          } while (UART_RX_BUFFER_COUNT);
        
          /* Now we can switch context if necessary */
          if ( xHigherPriorityTaskWoken != pdFALSE )
          {
            /* We should switch context so the ISR returns to a
            different task. NOTE:  How this is done depends on
            the port you are using.  Check the documentation and
            examples for your port. */
       
            taskYIELD_FROM_ISR();
          }
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 13-2** Inter-task Communication - ISRs </fc>



**Queue Sets**

FreeRTOS also provides a feature **Queue sets** that enables an RTOS task to block (pend) when receiving from multiple queues and/or semaphores at the same time. Queues and semaphores are grouped into sets, then, instead of blocking on an individual queue or semaphore, a task instead blocks on the set.

.. code:: c++

   xQueueCreateSet()
   xQueueAddToSet()
   xQueueRemoveFromSet()
   xQueueSelectFromSet()
   xQueueSelectFromSetFromISR()

Define **configUSE_QUEUE_SETS** to **``1``** to enable the above API functions of queue sets.

Example usage can be found at the section of `Queue Sets <https://www.freertos.org/xQueueCreateSet.html>`_ and see the `Blocking on Multiple Objects <https://www.freertos.org/Pend-on-multiple-rtos-objects.html>`_ page for more information.

--------------

Task Message Queue
------------------

Both kernels provide a single to single communication mechanisms that allows a task to send/receive messages directly to/from an ISR or another task, without going through an intermediate message queue. In µC/OS-III, you can use the Task Message Queue APIs ``OSTaskQPost()`` /``OSTaskQPend()``, and in FreeRTOS, Stream Buffers and Message Buffers can be used.

::

   ;   * //**µC/OS-III**// : ''Task Message Queue''
   ;   * //**FreeRTOS**// : ''Stream Buffer'' : ''Message Buffer''

**µC/OS-III**

Task Message Queue APIs

.. code:: c++

   OSTaskQPost()
   OSTaskQPend()
   OSTaskQPendAbort()
   OSTaskQFlush()

**FreeRTOS**

Stream/Message buffers are an RTOS task to RTOS task, and interrupt to task communication primitives. Unlike most other FreeRTOS communications primitives, they are optimised for single reader single writer scenarios, such as passing data from an interrupt service routine to a task, or from one microcontroller core to another on dual core CPUs. Data is passed by copy – the data is copied into the buffer by the sender and out of the buffer by the read.

+--------------------+------------------------------------------------------------+
| name               | note                                                       |
+====================+============================================================+
| ``Stream Buffer``  | Stream buffers pass a continuous stream of bytes.          |
+--------------------+------------------------------------------------------------+
| ``Message Buffer`` | Message buffers pass variable sized but discrete messages. |
+--------------------+------------------------------------------------------------+

.. container:: column

   **Stream Buffer**

   
   .. code:: c++
   
      xStreamBufferCreate()
      xStreamBufferCreateStatic()
      xStreamBufferSend()
      xStreamBufferSendFromISR()
      xStreamBufferReceive()
      xStreamBufferReceiveFromISR()
      vStreamBufferDelete()
      xStreamBufferBytesAvailable()
      xStreamBufferSpacesAvailable()
      xStreamBufferSetTriggerLevel()
      xStreamBufferReset()
      xStreamBufferIsEmpty()
      xStreamBufferIsFull() 
   


.. container:: column

   **Message Buffers**

   
   .. code:: c++
   
      xMessageBufferCreate()
      xMessageBufferCreateStatic()
      xMessageBufferSend()
      xMessageBufferSendFromISR()
      xMessageBufferReceive()
      xMessageBufferReceiveFromISR()
      vMessageBufferDelete()
      xMessageBufferSpacesAvailable()
      xMessageBufferReset()
      xMessageBufferIsEmpty()
      xMessageBufferIsFull()  
   



For a more detailed description of each of the arguments/usage for the above FreeRTOS Stream& Message Buffer APIs, please see the full documentation on the `Stream & Message Buffers <https://www.freertos.org/RTOS-stream-message-buffers.html>`_ and the API Reference sections of `Stream buffers <https://www.freertos.org/RTOS-stream-buffer-API.html>`_ and `Message Buffers <https://www.freertos.org/RTOS-message-buffer-API.html>`_.

--------------

Event Flags/Group
-----------------

Event flags are used when a task needs to synchronize with the occurrence of multiple events. Both µC/OS-III and FreeRTOS provide the Event Flags ( or 'Group') Feature for user to conveniently using it.

**µC/OS-III**

.. code:: c++

   OSFlagCreate()
   OSFlagDel()
   OSFlagPend()
   OSFlagPendAbort()
   OSFlagPendGetFlagsRdy()
   OSFlagPost()

**FreeRTOS**

.. code:: c++

   xEventGroupCreate()
   xEventGroupCreateStatic()
   vEventGroupDelete()
   xEventGroupWaitBits()
   xEventGroupSetBits()
   xEventGroupGetBits()
   xEventGroupClearBits()
   xEventGroupSetBitsFromISR()
   xEventGroupGetBitsFromISR()
   xEventGroupClearBitsFromISR()
   xEventGroupSync()

For this RTOS API function to be available:

-  **configSUPPORT_DYNAMIC_ALLOCATION** must be set to **``1``** in FreeRTOSConfig.h, or left undefined (in which case it will default to **``1``**).
-  The RTOS source file **<fc #4682b4>FreeRTOS/source/event_groups.c</fc>** must be included in the build.

+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| name                          | note                                                                                                                                                                                                                                          |
+===============================+===============================================================================================================================================================================================================================================+
| ``xEventGroupCreate()``       | Creates a new RTOS event group, and returns a handle by which the newly created event group can be referenced. **configSUPPORT_STATIC_ALLOCATION** must be set to **``1``** in FreeRTOSConfig.h to use the API ``xEventGroupCreateStatic()``. |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xEventGroupCreateStatic()`` |                                                                                                                                                                                                                                               |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vEventGroupDelete``         | Delete an event group that was previously created using a call to ``xEventGroupCreate()``.                                                                                                                                                    |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xEventGroupWaitBits()``     | Read bits within an RTOS event group, optionally entering the Blocked state (with a timeout) to wait for a bit or group of bits to become set.                                                                                                |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xEventGroupSetBits()``      | Set bits (flags) within an RTOS event group.                                                                                                                                                                                                  |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xEventGroupClearBits()``    | Clear bits (flags) within an RTOS event group.                                                                                                                                                                                                |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``xEventGroupSync()``         | This functionality is typically used to synchronize multiple tasks (often called a task rendezvous), where each task has to wait for the other tasks to reach a synchronization point before proceeding.                                      |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For a more detailed description of each of the arguments/usage for the above FreeRTOS Event Flags APIs, please see the full documentation on the `Event Groups (or 'flags') <https://www.freertos.org/event-groups-API.html>`_ Section of FreeRTOS API Reference.

**Example Usage**

The following example demonstrates how to use the Event Flags in the both µC/OS-III and FreeRTOS.

.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      #define      TEMP_LOW   (OS_FLAGS)0x0001                            
      #define      BATT_LOW   (OS_FLAGS)0x0002
         
      OS_FLAG_GRP  MyEventFlagGrp;
       
      void main (void)
      {
          OS_ERR  err;
          OSInit(&err);
          :
          OSFlagCreate(&MyEventFlagGrp,                                   
                       ”My Event Flag Group”,
                       (OS_FLAGS)0,
                       &err);
          /* Check ’err” */
          :
          OSStart(&err); 
      }
       
      void  MyTask (void *p_arg)
      {
          OS_ERR  err;
          CPU_TS  ts;
          const OS_TICK delay = 100;
         
          while (DEF_ON) {
              OSFlagPend(&MyEventFlagGrp,
                         TEMP_LOW + BATT_LOW,
                         (OS_TICK )delay,      
                         (OS_OPT)OS_OPT_PEND_FLAG_SET_ANY,
                         &ts,                             
                         &err);                           
              /* Check ’err” */
              :
              :
              
              /* Handle the event */
              :
              :
              :
              :
              :
              :
              :
              :
              :
          }
      }
       
      void  MyISR (void)
      {
          OS_ERR  err;
          :
          OSFlagPost(&MyEventFlagGrp,                                  
                     BATT_LOW,                     
                     (OS_OPT)OS_OPT_POST_FLAG_SET,
                     &err);                       
          /* Check ’err” */
          :
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
   
      #define BIT_0   ( 1 << 0 )
      #define BIT_4   ( 1 << 4 )
       
      EventGroupHandle_t xEventGroup = NULL;
       
      void main (void)
      {
          /* Create an event group. */
          xEventGroup = xEventGroupCreate();
          if( xEventGroup == NULL)
          {
              /* Event group create Error. */
          }
       
          /* Create task and start the scheduler */
          :
          :
          vTaskStartScheduler();
      }
         
      void  MyTask( void *pvParameters )
      {
      EventBits_t uxBits;
      const TickType_t xTicksToWait = 100 / portTICK_PERIOD_MS;
       
          /* Were the event flags have been set? */
          uxBits = xEventGroupWaitBits( xEventGroup,
                                        BIT_0 | BIT_4,
                                        pdFALSE,
                                        pdFALSE,        
                                        xTicksToWait );
          if( (uxBits & (BIT_0 | BIT_4)) == (BIT_0 | BIT_4) )
          {
            /*returned because both bits were set. */
          }
          else if( ( uxBits & BIT_0 ) != 0 )
          {
            /*returned because just BIT_0 was set. */
          }
          else if( ( uxBits & BIT_4 ) != 0 )
          {
              /*returned because just BIT_4 was set. */
          }
          else
          {
            /*returned because xTicksToWait ticks passed
        * without either BIT_0 or BIT_4 becoming set. */
          }
      }
       
      void  MyISR (void)
      {
          :
          if( (BIT_4 & xEventGroupSetBitsFromISR(xEventGroup, BIT_4)) != BIT_4 )
          {
              /* Set event Error.*/
               :
          }
          /* Set event Correctly.*/
          :
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 14** Event Flags/Group</fc>



--------------

Software Timers
---------------

Both kernels allows users to create a software timer that enable a function to be executed at a set time in the future, The timer can be configured to run continuously or only once (one-short).

**µC/OS-III**

.. code:: c++

   OSTmrCreate()
   OSTmrDel()
   OSTmrRemainGet()
   OSTmrSet()
   OSTmrStart()
   OSTmrStateGet()
   OSTmrStop()

**FreeRTOS**

Mainly Software Timer APIs in FreeRTOS.

.. code:: c++

   xTimerCreate()
   xTimerDelete()
   xTimerStart()
   xTimerStop()
   xTimerReset()
   pvTimerGetTimerID()
   pcTimerGetName()
   xTimerGetPeriod()
   xTimerGetExpiryTime()

+--------------------+--------------------------------------------------------------------------------------------------+
| name               | note                                                                                             |
+====================+==================================================================================================+
| ``xTimerCreate()`` | Creates a new software timer instance and returns a handle by which the timer can be referenced. |
+--------------------+--------------------------------------------------------------------------------------------------+
| ``xTimerDelete()`` | Deletes a timer that was previously created using the xTimerCreate() API function.               |
+--------------------+--------------------------------------------------------------------------------------------------+
| ``xTimerStart()``  | Starts a timer that was previously created using the xTimerCreate() API function.                |
+--------------------+--------------------------------------------------------------------------------------------------+
| ``xTimerStop()``   | Stopping a timer ensures the timer is not in the active state.                                   |
+--------------------+--------------------------------------------------------------------------------------------------+
| ``xTimerReset()``  | Re-starts a timer that was previously created using the xTimerCreate() API function.             |
+--------------------+--------------------------------------------------------------------------------------------------+

For a more detailed description of each of the arguments/usage for the above FreeRTOS Software Timers APIs, please see the full documentation on the `Software Timers <https://www.freertos.org/RTOS-software-timer.html>`_ Section and `FreeRTOS Software Timer API Functions <https://www.freertos.org/FreeRTOS-Software-Timer-API-Functions.html>`_.

**Example Usage**

.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      OS_TMR  CloseDoorTmr;
         
      void Task (void *p_arg)
      {
          OS_ERR   err;
          CPU_BOOLEAN  status;
         
          (void)&p_arg;
          while (DEF_ON) {
             OSTmrCreate(&CloseDoorTmr,        // p_tmr
                         "Door close"          // p_name
                          10,                  // dly
                          100,                 // period
                          OS_OPT_TMR_PERIODIC, // opt
                          DoorCloseFnct,       // p_callback
                          0,                   // p_callback_arg
                         &err);                // p_err
              /* Check “err” */
              :
              :
       
              status = OSTmrStart(&CloseDoorTmr,
                                  &err);
              /* Check “err” */
              :
              :
          }
      }
   
      void  DoorCloseFnct (OS_TMR  *p_tmr,
                           void    *p_arg)
      {
          /* Close the door! */
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
   
      TimerHandle_t  xTimers;
         
      void Task (void *pvParameters)
      {
          ( void ) pvParameters;
       
       
          while (DEF_ON) {
              xTimers = 
                xTimerCreate( "Door close",    // pcTimerName
                               100,            // period
                               pdTRUE,         // uxAutoReload
                               ( void * ) 0,   // pvTimerID
                               DoorCloseFnct );// Callback Func          
              if( xTimers == NULL )
               {
                   /* The timer was not created. */
               }
               else
               {   // delay 10 (in ticks)
                   if( xTimerStart( xTimers, 10 ) != pdPASS )
                   {
                       /* The timer could not be set
                       into the Active state. */
                   }
               }
          }
      }
         
      void  DoorCloseFnct( TimerHandle_t xTimer )
      {
          /* Close the door! */
       
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 15** Software Timers </fc>



--------------

Full API Map
------------

Locate in your project all the rest of µC/OS-III API function calls, and replace them with their equivalent FreeRTOS API function.

+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Features                                         | µC/OS-III               | FreeRTOS                               | Description                                                                                                                                                                                                                |
+==================================================+=========================+========================================+============================================================================================================================================================================================================================+
| Task Management                                  | OSTaskCreate()          | xTaskCreate()                          | `xTaskCreate() <https://www.freertos.org/a00125.html>`_                                                                                                                                                                    |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTaskCreateStatic()                    | `xTaskCreateStatic() <https://www.freertos.org/xTaskCreateStatic.html>`_                                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskDel()             | OSTaskDel()                            | `vTaskDelete <https://www.freertos.org/a00126.html>`_                                                                                                                                                                      |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskChangePrio()      | vTaskPrioritySet()                     | `vTaskPrioritySet() <https://www.freertos.org/a00129.html>`_                                                                                                                                                               |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | uxTaskPriorityGet()                    | `uxTaskPriorityGet() <https://www.freertos.org/a00128.html>`_                                                                                                                                                              |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskSuspend()         | vTaskSuspend()                         | `vTaskSuspend() <https://www.freertos.org/a00130.html>`_                                                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskResume()          | vTaskResume()                          | `vTaskResume() <https://www.freertos.org/a00131.html>`_                                                                                                                                                                    |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTaskResumeFromISR()                   | `xTaskResumeFromISR() <https://www.freertos.org/taskresumefromisr.html>`_                                                                                                                                                  |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskRegGet()          | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskRegSet()          | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskStkChk()          | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskTimeQuantaSet()   | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Time Management                                  | OSTimeDly()             | vTaskDelay()                           | `vTaskDelay() <https://www.freertos.org/a00127.html>`_                                                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | vTaskDelayUntil()                      | `vTaskDelayUntil() <https://www.freertos.org/vtaskdelayuntil.html>`_                                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xTaskAbortDelay()                      | `xTaskAbortDelay() <https://www.freertos.org/xTaskAbortDelay.html>`_                                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTimeDlyHMSM()         | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTimeDlyResume()       | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTimeDynTick()         | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTimeGet()             | xTaskGetTickCount()                    | `xTaskGetTickCount() <https://www.freertos.org/a00021.html#xTaskGetTickCount>`_                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTaskGetTickCountFromISR()             | `xTaskGetTickCountFromISR() <https://www.freertos.org/a00021.html#xTaskGetTickCountFromISR>`_                                                                                                                              |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTimeSet()             | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTimeTick()            | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Mutual Exclusion Semaphores                      | OSMutexCreate()         | xSemaphoreCreateMutex()                | `xSemaphoreCreateMutex() <https://www.freertos.org/CreateMutex.html>`_                                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreCreateMutexStatic()          | `xSemaphoreCreateMutexStatic() <https://www.freertos.org/xSemaphoreCreateMutexStatic.html>`_                                                                                                                               |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreCreateRecursiveMutex()       | `xSemaphoreCreateRecursiveMutex() <https://www.freertos.org/xSemaphoreCreateRecursiveMutex.html>`_                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreCreateRecursiveMutexStatic() | `xSemaphoreCreateRecursiveMutexStatic() <https://www.freertos.org/xSemaphoreCreateRecursiveMutexStatic.html>`_                                                                                                             |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSMutexDel()            | vSemaphoreDelete()                     | `vSemaphoreDelete() <https://www.freertos.org/a00113.html#vSemaphoreDelete>`_                                                                                                                                              |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSMutexPend()           | xSemaphoreTake()                       | `xSemaphoreTake() <https://www.freertos.org/a00122.html>`_                                                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreTakeFromISR()                | `xSemaphoreTakeFromISR() <https://www.freertos.org/xSemaphoreTakeFromISR.html>`_                                                                                                                                           |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreTakeRecursive()              | `xSemaphoreTakeRecursive() <https://www.freertos.org/xSemaphoreTakeRecursive.html>`_                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSMutexPendAbort()      | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSMutexPost()           | xSemaphoreGive()                       | `xSemaphoreGive() <https://www.freertos.org/a00123.html>`_                                                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreGiveFromISR()                | `xSemaphoreGiveFromISR() <https://www.freertos.org/a00124.html>`_                                                                                                                                                          |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreGiveRecursive()              | `xSemaphoreGiveRecursive() <https://www.freertos.org/xSemaphoreGiveRecursive.html>`_                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xSemaphoreGetMutexHolder()             | `xSemaphoreGetMutexHolder() <https://www.freertos.org/xSemaphoreGetMutexHolder.html>`_                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Semaphores                                       | OSSemCreate()           | xSemaphoreCreateBinary()               | `xSemaphoreCreateBinary() <https://www.freertos.org/xSemaphoreCreateBinary.html>`_                                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreCreateBinaryStatic()         | `xSemaphoreCreateBinaryStatic() <https://www.freertos.org/xSemaphoreCreateBinaryStatic.html>`_                                                                                                                             |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreCreateCounting()             | `xSemaphoreCreateCounting() <https://www.freertos.org/CreateCounting.html>`_                                                                                                                                               |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreCreateCountingStatic()       | `xSemaphoreCreateCountingStatic() <https://www.freertos.org/xSemaphoreCreateCountingStatic.html>`_                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSSemDel()              | vSemaphoreDelete()                     | `vSemaphoreDelete() <https://www.freertos.org/a00113.html#vSemaphoreDelete>`_                                                                                                                                              |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSSemPend()             |                                        | `xSemaphoreTake() <https://www.freertos.org/a00122.html>`_                                                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreTakeFromISR()                | `xSemaphoreTakeFromISR() <https://www.freertos.org/xSemaphoreTakeFromISR.html>`_                                                                                                                                           |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSSemPendAbort()        | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSSemPost()             | xSemaphoreGive()                       | `xSemaphoreGive() <https://www.freertos.org/a00123.html>`_                                                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xSemaphoreGiveFromISR()                | `xSemaphoreGiveFromISR() <https://www.freertos.org/a00124.html>`_                                                                                                                                                          |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSSemSet()              | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | uxSemaphoreGetCount()                  | `uxSemaphoreGetCount() <https://www.freertos.org/uxSemaphoreGetCount.html>`_                                                                                                                                               |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Task Semaphores (Task Notifications)             | OSTaskSemPend()         | ulTaskNotifyTake()                     | `ulTaskNotifyTake() <https://www.freertos.org/ulTaskNotifyTake.html>`_                                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskSemPendAbort()    | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskSemPost()         | xTaskNotifyGive()                      | `xTaskNotifyGive() <https://www.freertos.org/xTaskNotifyGive.html>`_                                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | vTaskNotifyGiveFromISR()               | `vTaskNotifyGiveFromISR() <https://www.freertos.org/vTaskNotifyGiveFromISR.html>`_                                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskSemSet()          | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xTaskNotify()                          | Notify a task form a Task or an ISR `xTaskNotify() <https://www.freertos.org/xTaskNotify.html>`_ `xTaskNotifyFromISR() <https://www.freertos.org/xTaskNotifyFromISR.html>`_                                                |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTaskNotifyFromISR()                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xTaskNotifyWait()                      | Waiting for the Notifies from a Task `xTaskNotifyWait() <https://www.freertos.org/xTaskNotifyWait.html>`_                                                                                                                  |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xTaskNotifyAndQuery()                  | Quarry and Notify from a Task or an ISR `xTaskNotifyAndQuery() <https://www.freertos.org/xTaskNotifyAndQuery.html>`_ `xTaskNotifyAndQueryFromISR() <https://www.freertos.org/xTaskNotifyAndQueryFromISR.html>`_            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTaskNotifyAndQueryFromISR()           |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xTaskNotifyStateClear()                | Clear (Pending to Not Pending) a pending notification.\ `xTaskNotifyStateClear() <https://www.freertos.org/xTaskNotifyStateClear.html>`_                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Message Queues                                   | OSQCreate()             | xQueueCreate()                         | `xQueueCreate() <https://www.freertos.org/a00116.html>`_                                                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xQueueCreateStatic()                   | `xQueueCreateStatic() <https://www.freertos.org/xQueueCreateStatic.html>`_                                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSQDel()                | vQueueDelete()                         | `vQueueDelete <https://wiki.analog.com/ttps/www.freertos.org/a00018.html>`_                                                                                                                                                |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSQFlush()              | xQueueReset()                          | `xQueueReset() <https://www.freertos.org/a00018.html#xQueueReset>`_                                                                                                                                                        |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSQPend()               | xQueueReceive()                        | `xQueueReceive() <https://freertos.org/a00118.html>`_                                                                                                                                                                      |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xQueueReceiveFromISR()                 | `xQueueReceiveFromISR() <https://freertos.org/a00120.html>`_                                                                                                                                                               |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSQPendAbort()          | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSQPost()               | xQueueSend()                           | `xQueueSend() <https://freertos.org/a00117.html>`_                                                                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xQueueSendFromISR()                    | `xQueueSendFromISR() <https://freertos.org/a00119.html>`_                                                                                                                                                                  |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xQueueSendToBack()                     | `xQueueSendToBack() <https://freertos.org/xQueueSendToBack.html>`_                                                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xQueueSendToBackFromISR()              | `xQueueSendToBackFromISR() <https://freertos.org/xQueueSendToBackFromISR.html>`_                                                                                                                                           |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xQueueSendToFront()                    | `xQueueSendToFront() <https://freertos.org/xQueueSendToFront.html>`_                                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xQueueSendToFrontFromISR()             | `xQueueSendToFrontFromISR() <https://freertos.org/xQueueSendToFrontFromISR.html>`_                                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | uxQueueMessagesWaiting()               | `uxQueueMessagesWaiting() <https://freertos.org/a00018.html#ucQueueMessagesWaiting>`_                                                                                                                                      |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | uxQueueMessagesWaitingFromISR()        | `uxQueueMessagesWaitingFromISR() <https://freertos.org/a00018.html#ucQueueMessagesWaitingFromISR>`_                                                                                                                        |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | uxQueueSpacesAvailable()               | `uxQueueSpacesAvailable() <https://freertos.org/a00018.html#uxQueueSpacesAvailable>`_                                                                                                                                      |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xQueueOverwrite()                      | `xQueueOverwrite() <https://freertos.org/xQueueOverwrite.html>`_                                                                                                                                                           |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xQueueOverwriteFromISR()               | `xQueueOverwriteFromISR() <https://freertos.org/xQueueOverwriteFromISR.html>`_                                                                                                                                             |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xQueuePeek()                           | `xQueuePeek() <https://freertos.org/xQueuePeek.html>`_                                                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xQueuePeekFromISR()                    | `xQueuePeekFromISR() <https://freertos.org/xQueuePeekFromISR.html>`_                                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | pcQueueGetName()                       | `pcQueueGetName() <https://freertos.org/pcQueueGetName.html>`_                                                                                                                                                             |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xQueueIsQueueFullFromISR()             | `xQueueIsQueueFullFromISR() <https://freertos.org/a00018.html#xQueueIsQueueFullFromISR>`_                                                                                                                                  |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xQueueIsQueueEmptyFromISR()            | `xQueueIsQueueEmptyFromISR() <https://freertos.org/a00018.html#xQueueIsQueueEmptyFromISR>`_                                                                                                                                |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | vQueueAddToRegistry()                  | `vQueueAddToRegistry() <https://freertos.org/vQueueAddToRegistry.html>`_                                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Task Message Queues (Stream&Message Buffer)      | N.A.                    | xStreamBufferCreate()                  | `xStreamBufferCreateStatic() <https://www.freertos.org/xStreamBufferCreate.html>`_                                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xStreamBufferCreateStatic()            | `xStreamBufferCreateStatic() <https://www.freertos.org/xStreamBufferCreateStatic.html>`_                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xMessageBufferCreate()                 | `xMessageBufferCreate() <https://www.freertos.org/xMessageBufferCreate.html>`_                                                                                                                                             |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xMessageBufferCreateStatic()           | `xMessageBufferCreateStatic() <https://www.freertos.org/xMessageBufferCreateStatic.html>`_                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | vStreamBufferDelete()                  | `vStreamBufferDelete() <https://www.freertos.org/vStreamBufferDelete.html>`_                                                                                                                                               |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | vMessageBufferDelete()                 | `vMessageBufferDelete() <https://www.freertos.org/vMessageBufferDelete.html>`_                                                                                                                                             |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskQFlush()          | xStreamBufferReset()                   | `xStreamBufferReset() <https://www.freertos.org/xStreamBufferReset.html>`_                                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xMessageBufferReset()                  | `xMessageBufferReset() <https://www.freertos.org/xMessageBufferReset.html>`_                                                                                                                                               |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskQPend()           | xStreamBufferReceive()                 | `xStreamBufferReceive() <https://www.freertos.org/xStreamBufferReceive.html>`_                                                                                                                                             |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xStreamBufferReceiveFromISR()          | `xStreamBufferReceiveFromISR() <https://www.freertos.org/xStreamBufferReceiveFromISR.html>`_                                                                                                                               |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xMessageBufferReceive()                | `xMessageBufferReceive() <https://freertos.org/xMessageBufferReceive.html>`_                                                                                                                                               |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xMessageBufferReceiveFromISR()         | `xMessageBufferReceiveFromISR() <https://freertos.org/xMessageBufferReceiveFromISR.html>`_                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskQPendAbort()      | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTaskQPost()           | xStreamBufferSend()                    | `xStreamBufferSend() <https://freertos.org/xStreamBufferSend.html>`_                                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xStreamBufferSendFromISR()             | `xStreamBufferSendFromISR() <https://freertos.org/xStreamBufferSendFromISR.html>`_                                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xMessageBufferSend()                   | `xMessageBufferSend() <https://freertos.org/xMessageBufferSend.html>`_                                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xMessageBufferSendFromISR()            | `xMessageBufferSendFromISR() <https://freertos.org/xMessageBufferSendFromISR.html>`_                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event Flags                                      | OSFlagCreate()          | xEventGroupCreate()                    | `xEventGroupCreate() <https://freertos.org/xEventGroupCreate.html>`_                                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xEventGroupCreateStatic()              | `xEventGroupCreateStatic() <https://freertos.org/xEventGroupCreateStatic.html>`_                                                                                                                                           |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSFlagDel()             | vEventGroupDelete()                    | `vEventGroupDelete() <https://freertos.org/vEventGroupDelete.html>`_                                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSFlagPend()            | xEventGroupWaitBits()                  | `xEventGroupWaitBits() <https://freertos.org/xEventGroupWaitBits.html>`_                                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSFlagPendAbort()       | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSFlagPendGetFlagsRdy() | xEventGroupGetBits()                   | `xEventGroupGetBits() <https://freertos.org/xEventGroupGetBits.html>`_                                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xEventGroupGetBitsFromISR()            | `xEventGroupGetBitsFromISR() <https://freertos.org/xEventGroupGetBitsFromISR.html>`_                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSFlagPost()            | xEventGroupSetBits()                   | `xEventGroupSetBits() <https://freertos.org/xEventGroupSetBits.html>`_                                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xEventGroupSetBitsFromISR()            | `xEventGroupSetBitsFromISR() <https://freertos.org/xEventGroupSetBitsFromISR.html>`_                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xEventGroupClearBits()                 | `xEventGroupClearBits() <https://freertos.org/xEventGroupClearBits.html>`_                                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xEventGroupClearBitsFromISR()          | `xEventGroupClearBitsFromISR() <https://freertos.org/xEventGroupClearBitsFromISR.html>`_                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xEventGroupSync()                      | `xEventGroupSync() <https://freertos.org/xEventGroupSync.html>`_                                                                                                                                                           |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Software Timers                                  | OSTmrCreate()           | xTimerCreate()                         | `xTimerCreate() <https://freertos.org/FreeRTOS-timers-xTimerCreate.html>`_                                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTimerCreateStatic()                   | `xTimerCreateStatic() <https://freertos.org/xTimerCreateStatic.html>`_                                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTmrDel()              | xTimerDelete()                         | `xTimerDelete() <https://freertos.org/FreeRTOS-timers-xTimerDelete.html>`_                                                                                                                                                 |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTmrStart()            | xTimerStart()                          | `xTimerStart() <https://freertos.org/FreeRTOS-timers-xTimerStart.html>`_                                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTimerStartFromISR()                   | `xTimerStartFromISR() <https://freertos.org/FreeRTOS-timers-xTimerStartFromISR.html>`_                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTmrStop()             | xTimerStop()                           | `xTimerStop() <https://freertos.org/FreeRTOS-timers-xTimerStop.html>`_                                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTimerStopFromISR()                    | `xTimerStopFromISR() <https://freertos.org/FreeRTOS-timers-xTimerStopFromISR.html>`_                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | xTimerReset()                          | `xTimerReset() <https://freertos.org/FreeRTOS-timers-xTimerReset.html>`_                                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTimerResetFromISR()                   | `xTimerResetFromISR() <https://freertos.org/FreeRTOS-timers-xTimerResetFromISR.html>`_                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTmrRemainGet()        | xTimerGetExpiryTime()                  | `xTimerGetExpiryTime() <https://freertos.org/FreeRTOS-timers-xTimerGetExpiryTime.html>`_                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTmrSet()              | vTimerSetReloadMode()                  | `vTimerSetReloadMode() <https://freertos.org/FreeRTOS-Timers-vTimerSetReloadMode.html>`_                                                                                                                                   |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | vTimerSetTimerID()                     | `vTimerSetTimerID() <https://freertos.org/FreeRTOS-timers-vTimerSetTimerID.html>`_                                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTimerChangePeriod()                   | `xTimerChangePeriod() <https://freertos.org/FreeRTOS-timers-xTimerChangePeriod.html>`_                                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTimerChangePeriodFromISR()            | `xTimerChangePeriodFromISR() <https://freertos.org/FreeRTOS-timers-xTimerChangePeriodFromISR.html>`_                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTimerPendFunctionCall()               | `xTimerPendFunctionCall() <https://freertos.org/xTimerPendFunctionCall.html>`_                                                                                                                                             |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTimerPendFunctionCallFromISR()        | `xTimerPendFunctionCallFromISR() <https://freertos.org/xTimerPendFunctionCallFromISR.html>`_                                                                                                                               |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSTmrStateGet()         |                                        | `OSTmrStateGet() <https://freertos.org/FreeRTOS-timers-xTimerIsTimerActive.html>`_                                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | N.A.                    | pcTimerGetName()                       | `pcTimerGetName() <https://freertos.org/FreeRTOS-timers-pcTimerGetName.html>`_                                                                                                                                             |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | pvTimerGetTimerID()                    | `pvTimerGetTimerID() <https://freertos.org/FreeRTOS-timers-pvTimerGetTimerID.html>`_                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTimerGetPeriod()                      | `xTimerGetPeriod() <https://freertos.org/FreeRTOS-timers-xTimerGetPeriod.html>`_                                                                                                                                           |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  |                         | xTimerGetTimerDaemonTaskHandle()       | `xTimerGetTimerDaemonTaskHandle() <https://freertos.org/FreeRTOS-Software-Timer-API-Functions.html#xTimerGetTimerDaemonTaskHandle>`_                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fixed-Size Memory Partitions (Memory Management) | OSMemCreate()           | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSMemGet()              | pvPortMalloc()                         | `pvPortMalloc() <https://freertos.org/a00111.html>`_                                                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OSMemPut()              | vPortFree()                            | `vPortFree() <https://freertos.org/a00111.htmlf>`_                                                                                                                                                                         |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Thread Local Storage                             | OS_TLS_GetID()          |                                        | N.A.                                                                                                                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OS_TLS_GetValue()       | pvTaskGetThreadLocalStoragePointer()   | `pvTaskGetThreadLocalStoragePointer() <https://freertos.org/pvTaskGetThreadLocalStoragePointer.html>`_                                                                                                                     |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OS_TLS_SetDestruct()    | N.A.                                   |                                                                                                                                                                                                                            |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  | OS_TLS_SetValue()       | vTaskSetThreadLocalStoragePointer()    | `vTaskSetThreadLocalStoragePointer() <https://freertos.org/vTaskSetThreadLocalStoragePointer.html>`_                                                                                                                       |
+--------------------------------------------------+-------------------------+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. container:: Centeralign

   <fc #4682b4>\ **Table 16** API Mapping</fc>



--------------

Error Handling
--------------

The errors reported back from the FreeRTOS API are different from µC/OS-III. In µC/OS-III, each API function returns an error code concerning the outcome of the function call via a pointer to a variable of type OS_ERR that is always the last argument of the API function, but in FreeRTOS, Typically you just declare a variable to store the return value from some of the API functions.

.. container:: column

   **µC/OS-III**

   
   .. code:: c++
   
      OS_MUTEX MyMutex;
   
   
      void MyFunction (void)
      {
          OS_ERR err;
          OSMutexCreate( &MyMutex,
                         "Mutex Name Here",
                         &err );
           
          if (err == OS_ERR_NONE) {
          // The mutex was created
          // and can be used
          } else {
          // Handle the error
          }
      }
   


.. container:: column

   **FreeRTOS**

   
   .. code:: c++
   
      SemaphoreHandle_t MyMutex;
      StaticSemaphore_t MyMutexBuffer;
       
      void MyFunction(void)
      {
          MyMutex = xSemaphoreCreateMutexStatic( &MyMutexBuffer );
        
          if( MyMutex != pdFALSE )
          {
              // The mutex was created
              // and can be used
          } else
          {
              // Handle the error
          }
      }
   



.. container:: Centeralign

   <fc #4682b4>\ **Table 17 - 1** Error Handling </fc>



As a basic error handling, you can simply check that the returned error code is OS_ERR_NONE, which is equivalent to the way you are currently doing it with FreeRTOS, where the returned error code can basically be either 0 or 1 as shown in the following table:

+-------+---------------------------------------+--------------------------+------------------------------------------+
| Group | Macro Name                            | Values                   | Note                                     |
+=======+=======================================+==========================+==========================================+
| a     | pdFALSE                               | ``( ( BaseType_t ) 0 )`` | FreeRTOS general error code check values |
+-------+---------------------------------------+--------------------------+------------------------------------------+
|       | pdTRUE                                | ``( ( BaseType_t ) 1 )`` |                                          |
+-------+---------------------------------------+--------------------------+------------------------------------------+
| b     | pdPASS                                | ``( ( BaseType_t ) 1 )`` | FreeRTOS general error code check values |
+-------+---------------------------------------+--------------------------+------------------------------------------+
|       | pdFAIL                                | ``( ( BaseType_t ) 0 )`` |                                          |
+-------+---------------------------------------+--------------------------+------------------------------------------+
| c     | errQUEUE_EMPTY                        | ``( ( BaseType_t ) 0 )`` | Queue functions error check values       |
+-------+---------------------------------------+--------------------------+------------------------------------------+
|       | errQUEUE_FULL                         | ``( ( BaseType_t ) 0 )`` |                                          |
+-------+---------------------------------------+--------------------------+------------------------------------------+
| d     | errCOULD_NOT_ALLOCATE_REQUIRED_MEMORY | ``( -1 )``               | Memory and other error check values      |
+-------+---------------------------------------+--------------------------+------------------------------------------+
|       | errQUEUE_BLOCKED                      | ``( -4 )``               |                                          |
+-------+---------------------------------------+--------------------------+------------------------------------------+
|       | errQUEUE_YIELD                        | ``( -5 )``               |                                          |
+-------+---------------------------------------+--------------------------+------------------------------------------+

.. container:: Centeralign

   <fc #4682b4>\ **Table 17 - 2** FreeRTOS Error Check Codes</fc>



--------------

Further Reading
---------------

To learn more about FreeRTOS including the API reference and the Features, Please refer to ADI FreeRTOS Wiki and FreeRTOS.org official website.

**ADI FreeRTOS:**

-  ADI FreeRTOS Wiki :doc:`/wiki-migration/resources/tools-software/freertos`

**FreeRTOS.org:**

-  API reference: https://freertos.org/a00106.html
-  PDF Reference Manual: https://freertos.org/Documentation/RTOS_book.html
-  Features/Getting Started: https://freertos.org/FreeRTOS-quick-start-guide.html

--------------

Getting Help
------------

If you need further help with migrations, please get in touch via:

-  ADI EngineerZone: :ez:`community/dsp/software-and-development-tools/freertos`
-  Support Email: <fc #4682b4>\ *processor.tools.support@analog.com*\ </fc>

--------------
