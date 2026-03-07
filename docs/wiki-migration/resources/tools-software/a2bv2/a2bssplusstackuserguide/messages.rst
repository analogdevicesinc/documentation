Appendix B: Messages
====================

| :doc:`Click here to return to the A2B SSPLUS STACK USER GUIDE </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>`
| Messages are shared between the Stack, Plugins and the Application to request or notify specific events.

Request Message
---------------

Request Message Example:-
~~~~~~~~~~~~~~~~~~~~~~~~~

|image1|

.. container:: centeralign

   \ **Figure: Request Message Example**


The list of Request message commands is listed below.

Request Message Commands
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------+
| Commands                          | Description                                                                                                           | Payload Type         |
+===================================+=======================================================================================================================+======================+
| A2B_MSGREQ_UNKNOWN                | Unknown message request command, typically to indicate error                                                          | -                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------+
| A2B_MSGREQ_NET_RESET              | Reset the A2B network                                                                                                 | -                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------+
| A2B_MSGREQ_NET_DISCOVERY          | Start A2B network discovery                                                                                           | a2b_NetDiscovery     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------+
| A2B_MSGREQ_NET_DISCOVERY_DIAGMODE | Start A2B network discovery in diag mode                                                                              | Not supported        |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------+
| A2B_MSGREQ_PLUGIN_PERIPH_INIT     | Request directed to a slave plugin to complete any necessary initialization of peripherals attached to the slave node | a2b_PluginInit       |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------+
| A2B_MSGREQ_PLUGIN_PERIPH_DEINIT   | Request directed to a slave plugin to de-initialize any peripherals attached to the slave node                        | a2b_PluginDeinit     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------+
| A2B_MSGREQ_PLUGIN_VERSION         | Request directed to a master or slave plugin for version and build information about this plugin itself               | a2b_PluginVerInfo    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------+
| A2B_MSGREQ_CUSTOM                 | Arbitrary custom command                                                                                              | -                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------+
| A2B_MSGREQ_NET_POST_DISCOVERY     | Starts partial discovery attempt of dropped nodes                                                                     | a2b_NetPostDiscovery |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+----------------------+

.. container:: centeralign

   \ **Table: Request Message Commands**


Notify Messages
---------------

Notify Message Examples:-
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/notifymessageexamples.jpg
   :align: center

.. container:: centeralign

   \ **Figure: Notify Message Example**\


The list of Notify Message Commands is listed below ^Notify Message Commands^Description^Payload type^ \|A2B_MSGNOTIFY_GPIO_INTERRUPT|Notify type used when a plugin triggers a GPIO interrupt.Causes an interrupt notification to be emitted|a2b_Interrupt

+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| A2B_MSGNOTIFY_POWER_FAULT    | Notify type used when a plugin sends a power fault notification                                                                                                                                       | a2b_PowerFault      |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| A2B_MSGNOTIFY_INTERRUPT      | Notify type used when the stack detects any interrupt and emits a notification.This also includes any GPIO-related interrupts                                                                         | a2b_Interrupt       |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| A2B_MSGNOTIFY_DISCOVERY_DONE | Notification that is emitted at the end of discovery whether it resulted in success or failure. This message also captures whether audio host provided SYNC to master PLL for locking (MSTR_RUNNING). | a2b_DiscoveryStatus |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| A2B_MSGNOTIFY_CUSTOM         | Arbitrary custom command.Anything at or beyond this value is considered a custom command                                                                                                              | -                   |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| A2B_MSGNOTIFY_NODE_DISCOVERY | Notify type used when the stack discovers a node OR custom node authentication fails for a particular node.                                                                                           | a2b_Nodedscvry      |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

.. container:: centeralign

   \ **Table: Notify Message Commands**\


Sending custom messages and notifications
-----------------------------------------

To send a custom message, one must allocate the message, find the payload area, deposit the message contents, send the message, and optionally release the reference to the message. Sending a typical message looks like this:

Code Snippet: Sending Custom Message Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image2|

.. container:: centeralign

   \ **Code Snippet: ending Custom Message Example**\


As illustrated in the example code above, the caller unreferences the message following the call to a2b_msgRtrSendRequest(). This is because the Stack adds its own reference to the message following the send request. In the event that caller requires that the message live longer, i.e. because it is carrying pointers to data, then one should register a complete callback with the a2b_msgRtrSendRequest() and unreference the message there.

The callee of the message is free to modify the contents of the message within the callee’s message handler. A callback optionally registered by the caller can be called when the callee completes processing of the message. This callback can be used by the caller to process return values from the callee.

Receiving custom messages and notifications
-------------------------------------------

Messages are handled exclusively through the Execute method of a plugin. A plugin simply has to have defined entries for custom message within the switch/case statement. The message payload can be extracted from the message using ‘a2b_msgGetPayload()’

Code snippet: Receiving Custom Message Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image3|

.. container:: centeralign

   \ **Code Snippet: Receiving Custom Message Example**\


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/request_message_example.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/sending_custom_message_example.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/receiving_custom_message_example.jpg
