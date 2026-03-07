How to Debug SHARC Applications While Running Linux on the ARM Core of the ADSP-SC5xx Processor
===============================================================================================

When attempting to debug SHARC applications using CrossCore Embedded Studio, it is important to ensure that the debug session does not interfere with execution of Linux running on the ARM core of the processor.

Since the ARM is the booting core for the SC5xx processors, Linux will be running when you connect to the Cross Core Embedded Studio debugger.

You will need to make several changes when creating a debug session for the SHARC cores to avoid interfering with Linux.

Ensure that the debug session does not load any preloads or applications to the ARM core
----------------------------------------------------------------------------------------

By default the debug session will attempt to load applications on to the ARM core.

When creating the debug session you will need to remove any preload or initcode binary and ensure that an application is not loaded. This will ensure that the L2 and L3 memory reserved for the ARM core is not changed by the debug session (Assuming that you have either used the default memory configuration or correctly repartitioned the memory between the cores)

Ensure that the debug session does not reset the processor when loading the SHARC cores
---------------------------------------------------------------------------------------

By default the debug session will reset the processor when starting a debug session. Since this cannot be performed on a core by core basis the whole system is reset, wiping the running Linux from memory.

When creating the debug session you will need to uncheck the option to "reset on reload" from the debug session settings.

Ensure that semihosting does not interfere with Linux running on the ARM core
-----------------------------------------------------------------------------

When creating a debug session for SC5xx processors by default CrossCore Embedded Studio uses the ARM supervisor call (SVC) instruction to trigger a communication to the host PC. Unfortunately this instruction is used by Linux for other purposes. By leaving this feature active the execution of Linux will become considerably slower and may result in crashes.

When creating the debug session you will need to uncheck the "Use semihosting" checkbox from the debug session settings.

This will ensure that the emulator does not halt the board for each execution of the SVC instruction.
