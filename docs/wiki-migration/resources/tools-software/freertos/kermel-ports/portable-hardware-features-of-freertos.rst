Features of the GUL FreeRTOS Hardware Port
==========================================

Introduction
------------

This page describes the features of the ADSP GUL FreeRTOS hardware port, aimed to make it easier for our customers to understand how the FreeRTOS official features are implemented at the underlying hardware.

--------------

Core Clock
----------

The Core (CPU) Clock can be controlled at the Clock Generation Unit (CGU) and for the full information please refer to the :adi:`ADSP-2156x SHARC+ Processor Hardware Reference <media/en/technical-documentation/user-guides/adsp-2156x_hwr.pdf>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/kermel-ports/d01_cgu.png
   :align: center
   :width: 700px

.. container:: centeralign

   **Diagram 1** CGU PLL Block Diagram


According to the hardware reference and the below diagram we can get the formula for processor Core Clock frequency (CCLCK0):

.. container:: centeralign

   
   .. code:: 
   
      CCLCK0 =  SYS_CLKIN  / ( CGU0_CTL.DF + 1 ) * CGU0_CTL.MSEL  /  CGU0_DIV.CSEL
   


**Register Group**

CGU0 register list is shown below

+---------------------------+-------------------+----------------------------+------------+
| ``Memory Mapped Address`` | ``Register Name`` | ``Description``            | ``value``  |
+===========================+===================+============================+============+
| 0x3108D000                | CGU0_CTL          | CGU0 Control Register      | 0x00025000 |
+---------------------------+-------------------+----------------------------+------------+
| 0x3108D00C                | CGU0_DIVC         | GU0Clocks Divisor Register | 0x04034482 |
+---------------------------+-------------------+----------------------------+------------+
|                           |                   |                            |            |
+---------------------------+-------------------+----------------------------+------------+

From the below Diagram Register Group **CGU0**, the target CGU registers values can be accessed.


|image1|

.. container:: centeralign

   **Diagram 2** CGU0 Register Group


Now we can calculate the CPU Core Clock Frequency:

.. code:: 

   CCLCK0 =  SYS_CLKIN  / ( CGU0_CTL.DF + 1 ) * CGU0_CTL.MSEL  /  CGU0_DIV.CSEL
          = 25 MHz / ( 0 +1 ) * 80 / 2 
          = 1 GHz

--------------

System Tick Interrupt
---------------------

The System Tick Interrupt is used to to generate the tick interrupts at the required frequency for the FreeRTOS System. And it has been implemented using the Core Timer interrupt in the port.c

.. code:: java

   __attribute__(( weak )) void vPortSetupTimerInterrupt( void )
   {
       /* Configure SysTick to interrupt at the requested rate. */
       const uint32_t ulTimerCountsForOneTick = ( configSYSTICK_CLOCK_HZ / configTICK_RATE_HZ );
       sysreg_bit_clr(sysreg_MODE2, BITM_REGF_MODE2_TIMEN);         /* make sure the core timer is off */
       asm volatile ("TPERIOD=%0;\n"                       /* The period and current count = ulTimerCountsForOneTick */
           "TCOUNT=%1;\n" : :"d" (ulTimerCountsForOneTick), "d" (ulTimerCountsForOneTick) );
       adi_rtl_register_dispatched_handler(configTIMER_INTERRUPT, xPortSysTickHandler, NULL);
       adi_rtl_activate_dispatched_handler(configTIMER_INTERRUPT);
       
       sysreg_bit_set(sysreg_MODE2, BITM_REGF_MODE2_TIMEN); /* start the core timer */
   }

The above needed macros are defined at the FreeRTOSConfig.h

+----------------------------+---------------------------------------------+--------------------------------+
| ``Type``                   | ``Macro``                                   | ``Value``                      |
+============================+=============================================+================================+
| ``CPU Core Clock``         | configSYSTICK_CLOCK_HZ (configCPU_CLOCK_HZ) | 1 GHz                          |
+----------------------------+---------------------------------------------+--------------------------------+
| ``RTOS SysTick Frequency`` | configTICK_RATE_HZ                          | 1000 Hz                        |
+----------------------------+---------------------------------------------+--------------------------------+
| :::                        | ulTimerCountsForOneTick                     | 1GHz / 1000Hz = 1000,000 cycle |
+----------------------------+---------------------------------------------+--------------------------------+

So the System Tick Interrupt will come every 1000,000 cycles.

--------------

Reschedule Interrupt
--------------------

For ADSP-21569 processor, FreeRTOS uses the SEC (System Event Controller) interrupts SOFT6 (Software Interrupt 6 ) as this reschedule interrupt, and it is implemented at the file of port.c

**port.c**

.. code:: c++

   BaseType_t xPortStartScheduler( void )
   {
       /* Set bit in the MMASK register so that the foreground (system) data and
     * DAG registers will be selected on interrupt entry.
        */
       sysreg_bit_set(sysreg_MMASK, FRTOS_MMASK_SET_BITS);
       
       /* Use SEC interrupts SOFT6 for SHARC0 (core 1) and SOFT7 for SHARC1 (core 2) */
   #if defined(__ADSP2156x__)
       _adi_OSRescheduleIntID = INTR_SYS_SOFT6_INT;
   #endif
       adi_rtl_register_dispatched_handler (_adi_OSRescheduleIntID, _adi_SoftIntTaskSw, 0u);
       adi_sec_SetCoreID(_adi_OSRescheduleIntID, (ADI_SEC_CORE_ID)adi_core_id()); /* route the interrupt to this core */
       adi_sec_EnableSource(_adi_OSRescheduleIntID, true);                        /* enable the interrupt source */
       adi_sec_EnableInterrupt(_adi_OSRescheduleIntID, true);                     /* enable the interrupt */
       adi_rtl_activate_dispatched_handler (_adi_OSRescheduleIntID);
   ... 
   }

**Register Group**

SEC0 register list is shown below

+---------------------------+----------------------------+--------------------------------+------------+
| ``Memory Mapped Address`` | ``Register Name``          | ``Description``                | ``value``  |
+===========================+============================+================================+============+
| 0x31089918                | SEC0_SCTL[n] (SEC0_SCTL35) | SEC0 Source Control Register n | 0x00000005 |
+---------------------------+----------------------------+--------------------------------+------------+
|                           |                            |                                |            |
+---------------------------+----------------------------+--------------------------------+------------+

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/kermel-ports/sec0.png
   :align: center
   :width: 700px

.. container:: centeralign

   **Diagram 3** SEC0 Register Group


When blocks occur, or delay timing, or other situations that require scheduler rescheduling，they will raise the reschedule interrupt and notify the RTOS System to reschedule the tasks.

+------------------------+-------------------------+--------------------------------------------+
| ``macro``              | ``Interrupt``           | ``Note``                                   |
+========================+=========================+============================================+
| portYIELD()            | \_adi_OSRescheduleIntID | Without waiting for the IRQ to be serviced |
+------------------------+-------------------------+--------------------------------------------+
| portYIELD_WITHIN_API() | \_adi_OSRescheduleIntID | wait for the IRQ to be serviced            |
+------------------------+-------------------------+--------------------------------------------+

This above macros are implemented at the file of portmacro.h

**portmacro.h**

.. code:: c++

   /* Raise the reschedule interrupt, without waiting for it to be serviced */
   #define portYIELD() { *pREG_SEC0_RAISE = _adi_OSRescheduleIntID;}
   /* Raise the reschedule interrupt and wait for it to be serviced *unless* interrupts are globally disabled */
   #define portYIELD_WITHIN_API() { _adi_OSWaitingForSched = 1u; *pREG_SEC0_RAISE = _adi_OSRescheduleIntID; if (__builtin_sysreg_bit_tst(sysreg_MODE1, 0x1000)) { while(_adi_OSWaitingForSched) {}; } }

--------------

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/kermel-ports/d02_cgu0.png
   :width: 700px
