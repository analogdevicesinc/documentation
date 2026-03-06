SEC driver and multicore development
====================================

Introduction
------------

| There are two Interrupt Controllers on the ADSP-SC573, SC584 and SC589. The GIC (Generic Interrupt Controller) for the ARM core and the SEC (System Event Controller) for the SHARC cores. The SEC manages the configuration of all system event sources, and also manages the propagation of system events to all connected SHARC cores and the system fault interface.
| Linux, running on the ARM core, manages all of its interrupts via the GIC. However, if any Linux driver wants to trigger an interrupt to the SHARC cores directly it should raise an SSI source event in the SEC. In addition, the watchdog device can only reset the cores via the system fault interface. The Linux watchdog driver has to set up its event route in the SEC as well. All of these interactions with the SSI depend on proper initialization of the SEC controller. Because, the SEC controller can be initialized by code on either the ARM core or the SHARC cores, there must be a way to avoid conflicting initialization on different cores. This guide apply to both ADSP-SC573, SC584 and SC589. Take ADSP-SC589 as example in following sections.

Linux kernel Configuration
--------------------------

The SHARC slave core number in the ADSP-SC58x serial processors differs among models. So, the slave core count should be set up accordingly in the Linux kernel. The Linux SEC driver initializes the proper SCIs in the SEC controller according to this setting. However, the SEC driver is built into the Linux kernel no matter how many slave cores are configured.

::

   System Type  ---> 
       sc58x platform type  --->
           (2) Slave core count in sc58x

The valid slave core count is 0, 1 or 2.

When the Linux kernel is booting up, following message is printed out.

::

   sec init...
   enabled

SHARC Remoteproc Framework Introduction
---------------------------------------

ADI provides some examples including the remoteproc developing examples. Users can download the examples from here: https://github.com/analogdevicesinc/lnxdsp-examples.git. Refer to the LED blinky example under the remoteproc directory. Two APIs are implemented for users to call for:

::

   void prvRemoteProcProbe( ADI_CORE_ID __core_id );
   void prvRemoteProcRemove( ADI_CORE_ID __core_id );

One bool parameter is defined to indicate the ARM core's message through SEC interface. Currently the ARM core will raise a core reset interrupt through SEC.

::

   bool SEC_RESET;

How to use Remoteproc Framework in Your Own SHARC Project
---------------------------------------------------------

Call the "prvRemoteProcProbe(coreid);" at the begin of your main function. In this probe function, SEC_RESET will be set to false and one specific interrupt (INTR_SOFT0 for SHARC Core0, INTR_SOFT1 is for SHARC Core1) will be registered to handle the reset request from ARM core. It is not recommended to do any modification in this function. Create a while loop or a task to check the "bool SEC_RESET" value. Once this bool value is set to true, call the prvRemoteProcRemove() to uninstall the interrupt handler. SEC_RESET will set to true once the SEC_HANDLR is called, which means the SHARC core reset request is triggered by ARM core, and the program should release all related resources and execute the Idle loop.

One simple example code
-----------------------

::

   /* main function of the example */
   int main(int argc, char *argv[])
   {
       ....
       /* Remoteproc framework initialization */
       prvRemoteProcProbe(CoreID);
       /* Create the Remoteproc state check task */
       createTask(checkTask);
       ....
   }
   /* Body of the Remoteproc state check task */
   void checkTask()
   {
       while(1)
       {
           if (SEC_RESET) {
                   /* call Remoteproc Remove to free all requested resources on SHARC core and execute the IDLE loop */
                   prvRemoteProcRemove(nCoreID);
           } else {
               ....
           }
       }
   }

| 
| ---- **BACK TO** :doc:`Multi-Core Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mcapi/start>`
