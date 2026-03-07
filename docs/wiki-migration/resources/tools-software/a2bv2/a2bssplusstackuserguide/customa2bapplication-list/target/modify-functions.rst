:doc:`Click here to return to Building Target software for a custom platform </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication-list/target>`

Modify Application Call-back Functions
======================================

By this time, we should have completed the porting of A2B Stack as explained in Section ":doc:`Porting A2B Software Stack to a custom platform </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>`". At this stage, the A2B Stack ported on the custom platform should be capable of discovering and configuring a connected A2B network as per the added bus configuration file.

The A2B Stack offers provision for the application running on the Target software to register callback functions for important network activities. Three important application callback functions are registered with the Stack. These functions can be modified by the user to perform an action specific to the application.

.. note::

   All examples provided in the A2B Software package come with default implementations for these callback functions. Modifications to these functions are required only if the default implementation doesn’t match your targeted system requirement. When requiring additional functionality, it is recommended to add on top of the existing implementation unless rewriting completely.


The three application callback functions are explained in the following sub-sections.

Discovery completion Callback function
--------------------------------------

The discovery completion callback function is invoked by the stack upon completing the discovery and configuration of the whole A2B network. :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>` shows the application registration of a discovery completion callback function with the stack. The status of the discovery is notified by this function allowing the application to perform any additional tasks based on the notified status.


|image1|

.. container:: centeralign

   \ **Figure: A2BAPP OnDiscoveryComplete Callback Function**\


.. note::

   a2bapp_onDiscoveryComplete() comes with a default implementation for post-discovery bus drop monitoring and rediscovery upon faults (if it was set in SigmaStudioPlus while exporting the bus configuration file). Modify this function only to override default functionality (if required).


The code snippet shows a sample implementation of this callback function.

::

   a2bapp_onDiscoveryComplete
       (
       struct a2b_Msg* msg;
       a2b_Bool isCancelled;
       )
   {
       a2b_NetDiscovery* results;
       a2b_Bool* discDone;

       if ( A2B_NULL == msg )
       {
   #ifdef A2B_PRINT_CONSOLE
           /* This should "never" happen */
           fprintf(stderr, "Error: no response message for network discovery\n");
   #endif
       }
       else
       {
           discDone = a2b_msgGetUserData(msg);

           if ( isCancelled )
           {
   #ifdef A2B_PRINT_CONSOLE
               fprintf(stderr, "Discovery request was cancelled.\n");
   #endif
           }
           else
           {
               results = (a2b_NetDiscovery*)a2b_msgGetPayload(msg);
               if ( A2B_SUCCEEDED(results->resp.status) )
               {
                   printf("Discovery succeeded with %d nodes discovered\n", 
                          results->resp.numNodes);
                   gNumSlaveNodes = results->resp.numNodes;
               }
               else
               {
   #ifdef A2B_PRINT_CONSOLE
                   fprintf(stderr, "Discovery failed!\n");
   #endif
               }
           }
           /* Force the main loop to exit */
           *discDone = A2B_TRUE;
       }
   }

Power/Line Fault Callback function
----------------------------------

The power fault callback function is invoked by the stack upon detecting a power-related fault in any node of the network. An application callback function can be registered with the Stack for power fault notifications as shown in the below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>`.


|image2|

.. container:: centeralign

   \ **Figure: A2BAPP OnPowerFault Callback Function**\


The Stack provides a callback function to the application layer upon the occurrence of a fault in the A2B System. The stack performs necessary diagnostics and fault localization (in case of concealed faults) and reports the fault type and location to the application for further handling.

.. note::

   The Stack performs all necessary actions to handle the fault as recommended by the A2B Transceiver Programmer’s reference manual and finally invokes the application callback.


The function is invoked under the following fault conditions during and post discovery.

-  Critical faults

   -  Cable terminal shorted to GND
   -  Cable terminal shorted to VBat

-  Non-Critical faults

   -  Cable terminals shorted together
   -  Cable disconnected or open circuit
   -  Cable is reversely connected

-  Indeterminate faults
-  Bus/Node drop condition

Code Snippet shows a sample implementation of the a2bapp_onPowerFault callback function.

::

   a2bapp_onPowerFault (struct a2b_Msg *msg, a2b_Handle userData)
   {
       A2B_UNUSED(userData);
       a2b_PowerFault *fault;
       const char *faultString;

       if ( msg )
       {
           fault = (a2b_PowerFault *)a2b_msgGetPayload(msg);
           if ( fault )
           {
               if ( A2B_SUCCEEDED(fault->status) )
               {
                   switch (fault->intrType)
                   {
                       case A2B_ENUM_INTTYPE_PWRERR_CS_GND:
                           faultString = "Cable Shorted to GND";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_CS_VBAT:
                           faultString = "Cable Shorted to VBat";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_CS:
                           faultString = "Cable Shorted Together";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_CDISC:
                           faultString = "Cable Disconnected or Open Circuit";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_CREV:
                           faultString = "Cable Reverse Connected or Wrong Port";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_FAULT:
                           faultString = "Indeterminate Fault";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_NLS_GND:
                           faultString = "Non-Localized Short to GND";
                           /* Add your code to handle fault */
                           break;
                       case A2B_ENUM_INTTYPE_PWRERR_NLS_VBAT:
                           faultString = "Non-Localized Short to VBat";
                           /* Add your code to handle fault */
                           break;
                       default:
                           faultString = "Unknown";
                           /* Add your code to handle fault */
                           break;
                   }
                   gAPP_Info.faultNode = fault->faultNode;
               }
           }
       }
   }

The information about the presence of a locally powered slave is made known to the stack through the BDD. In case of critical faults (Cable terminal shorted to GND, Cable terminal shorted to VBat), the stack switches of the bus from the immediate upstream local powered slave onwards.

Partial bus operation is possible between master and this upstream local powered slave.

Interrupt Callback function
---------------------------

The Interrupt callback function is invoked by the Stack upon seeing any interrupts at the master node. The below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>` shows the application registration of an interrupt callback function with the Stack.


|image3|

.. container:: centeralign

   \ **Figure: Interrupt Callback Function**\


The code snippet shows a simple implementation of this callback function.

::

   static void a2bapp_onInterrupt(struct a2b_Msg* msg, a2b_Handle userData)
   {
       a2b_Interrupt* interrupt;

       A2B_UNUSED(userData);

       if (msg)
       {
           interrupt = a2b_msgGetPayload(msg);
           if (gDebug)
           {
               if (interrupt)
               {
   #ifdef A2B_PRINT_CONSOLE
                   printf("INTERRUPT: intrType=%u nodeAddr=%d\n",
                          interrupt->intrType, interrupt->nodeAddr);
   #endif
                   /* Add your code to handle interrupt */
               }
               else
               {
   #ifdef A2B_PRINT_CONSOLE
                   fprintf(stderr, "INTERRUPT: failed to retrieve payload\n");
   #endif
               }
           }
       }
   }

.. note::

   Any interrupt on the slave node can be handled within a2bplugin_slave\\ a2bslave_plugin.c file in the function a2b_pluginInterrupt as explained in "Handling Interrupts in a Plugin" in :doc:`applicationintegration </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/applicationintegration>`


Node Discovery Callback function
--------------------------------

The node discovery callback function is an optional callback, which is invoked by the stack upon each node discovery or when node authentication fails. The below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>` shows the application registration of this callback function with the Stack.


|image4|

.. container:: centeralign

   \ **Figure: Node Discovery Callback Function**\


The below Code Snippet shows a sample implementation of this callback function. The application can decide whether to continue with discovery or not and has more control with this callback function.

::

   static void a2bapp_onNodeDiscovery(struct a2b_Msg* msg, a2b_Handle userData)
   {
   #ifdef A2BAPP_ENABLE_RTMBOOT
       a2b_HResult                 nRes;
       a2b_App_t *pApp_Info        =   userData;
   #endif
       a2b_Nodedscvry* dscvrdNodeMsg;

   #ifdef A2B_PRINT_CONSOLE
       a2b_Int16 nodeAddr;
       bdd_Node *bddnode;
       bdd_Network *bddNetwork;
   #endif

   #ifndef A2BAPP_ENABLE_RTMBOOT
       A2B_UNUSED(userData);
   #endif

       if (msg)
       {
           /* details of the currently discovered node */
           dscvrdNodeMsg = a2b_msgGetPayload(msg);

   #ifdef A2B_PRINT_CONSOLE
           nodeAddr = dscvrdNodeMsg->nodeAddr; //this will number of slave node discovered
           bddNetwork = (bdd_Network *)dscvrdNodeMsg->bddNetObj;
           bddnode = (bdd_Node *)(&bddNetwork->nodes[nodeAddr]);
   #endif
           if (dscvrdNodeMsg)
           {
   #ifdef A2BAPP_ENABLE_RTMBOOT
               if(dscvrdNodeMsg->nodeAddr == (A2BAPP_RTM_NODEADDR + 1U))
               {
                   /* Call to boot the RTM Module */
                   nRes = a2bapp_RTMBoot(pApp_Info->ctx, A2BAPP_RTM_NODEADDR);
                   if (A2B_FAILED(nRes))
                   {
                       A2B_APP_LOG("NODE DISCOVERY: failed to boot RTM\n\r");
                   }
               }
   #endif
               A2B_APP_LOG("NODE DISCOVERY: nodeType=%u nodeAddr=%d discoveryCompleteCode=%u\n\r", bddnode->nodeType, nodeAddr, dscvrdNodeMsg->discoveryCompleteCode);

   #ifndef ENABLE_SUPERBCF
               /* CRITICAL: Populate the further action which is required to be taken by stack
                * Set,
                *      bContinueDisc to true if required to proceed with discovery process
                *      bContinueDisc to false if required to end the discovery process
                */
               dscvrdNodeMsg->bContinueDisc = A2B_TRUE;
   #endif  /* ENABLE_SUPERBCF */
           }
           else
           {
               A2B_APP_LOG("NODE DISCOVERY: failed to retrieve payload\n\r");
           }
       }
   }

I2C Error Callback Function
---------------------------

The I2C error callback function is invoked by the Stack upon seeing any I2C errors at the master node or at sub-node peripherals.


|image5|

.. container:: centeralign

   \ **Figure: I2C Error Callback Function**\


The code snippet shows a simple implementation of this callback function.

::

   static void a2bapp_onI2CError(struct a2b_Msg *msg, a2b_Handle userData)
   {
       a2b_I2CError *I2CError;
       A2B_UNUSED(userData);
       a2b_App_t *gApp_Info;

       I2CError = (a2b_I2CError *)a2b_msgGetPayload(msg);

       gApp_Info->bfaultDone = A2B_TRUE;
       gApp_Info->bRetry = A2B_TRUE;
       if(I2CError->nodeAddr == A2B_NODEADDR_MASTER)
       {
           A2B_APP_LOG("\n\Incorrect I2C address at main node\n\r");
       }
       else
       {
           A2B_APP_LOG("\n\rPeripheral configuration failed with I2C address 0x%x on node %d\n\r", I2CError->I2CAddr, I2CError->nodeAddr);
       }
   }

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/a2bapp_ondiscoverycomplete_callback_function.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/a2bapp_onpowerfault_callback_registration.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/interrupt_callback_function.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/node_discovery_callback_function.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/i2c_error_callback_function.png
