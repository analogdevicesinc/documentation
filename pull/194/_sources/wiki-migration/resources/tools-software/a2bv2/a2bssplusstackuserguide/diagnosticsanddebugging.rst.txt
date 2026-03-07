Appendix A: Diagnostics and Debugging
=====================================

| :doc:`Click here to return to the A2B SSPLUS STACK USER GUIDE </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>`
| Diagnostic and debugging is one of the most powerful aspects of the Stack. Every logged event is timestamped and presented to the PAL for storage or reporting. Internally logged items include:

-  All I2C transactions
-  All messages
-  All timer events
-  All application interactions
-  Discovery details
-  Power fault details

The Stack included two discrete classes of logging. The first class of logs are used to build structured sequence diagrams. The second class are unstructured trace messages. While both types utilize the pal_logXXX() functions, separate handles allow the PAL layer to distinguish between the two logging classes.

Sequence diagrams provide unparalleled transparency into the complex interactions between the master and slaves throughout the entire lifecycle of an A2B network. This includes all aspects of discovery and steady-state operation after discovery.

Once the deployment of an A2B network reaches a certain state of stability, trace messages can be utilized to log Stack operations in a less detailed manner than the Sequence diagrams. Trace messages are routinely integrated into larger system-level logging frameworks where message types and severity can be monitored and filtered.

Additionally, the Stack automatically performs power and line fault diagnostics whenever a network discovery fails. The diagnostics are reported back to the application through the diagnostic event handler registered with the Stack.

Generating Sequence Diagrams
----------------------------

The sequence diagrams created by the Stack are compatible with an open-source tool called PlantUML (http://plantuml.com/). The raw syntax for PlantUML is human-readable and friendly for processing with different tools or checking into document repositories. When post-processed by the PlantUML tool, extremely rich graphical sequence diagrams can be created.

The script to post-process the sequence diagrams to a more readable format is given in ‘Target/tools’.

.. note::

   Python must be installed on the developer’s system for the post-processing script to function.


Sequence diagram support in the Stack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Sequence diagram support is an optional Stack feature and must be enabled by defining A2B_FEATURE_SEQ_CHART in ‘features.h’ prior to compiling the Stack.
-  Once sequence diagram support is included in the Stack, sequence diagrams must be enabled as part of the Stack start-up.
-  All logging, including sequence diagrams and tracing, go through the pal_logXXX() set of functions in the PAL. The table below illustrates the primary functions:

PAL Logging Functions-Info:-
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PAL Function     | Use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+==================+====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| a2b_LogOpenFunc  | The second argument passed to a2b_seqChartStart() is passed back into this function.This argument is a URI that the PAL code should recognize and open. A handle must be returned back to the Stack from this function. The handle will be passed along to the a2b_LogCloseFunc and a2b_LogWriteFunc functions.NOTE: The URI passed into a2b_seqChartStart() can be a pointer to any object, not just a constant string. For systems without an underlying filesystem, a common trick is to pass a pointer to a “logging” structure that contains an application level log buffer. This pointer should then be returned to the Stack by this function as the handle. The Stack will then forward the pointer to the logging structure to the a2b_LogWriteFunc and a2b_LogCloseFunc functions whenever any sequence chart data needs to be written. |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_LogCloseFunc | Closes the device handle returned by a2b_LogOpenFunc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| a2b_LogWriteFunc | Writes a line of sequence chart data to the device handle returned by a2b_LogOpenFunc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enabling Sequence Chart in Sample Demo Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Pre-Requisites

   -  Set the PATH environment variable for running ‘java.exe’

      -  C:\\Program Files (x86)\\Java\\jre<<xx>>\\bin


      |image1|

.. container:: centeralign

   \ **Figure: Setting Path in Environment Variables**\


-  Enable ’A2B_FEATURE_SEQ_CHART’ macro in ‘Target\\examples\\demo\\<a2b-xx>\\ a2bstack-pal\\platform\\a2b\\features.h’
-  Build, load and execute the a2bstack application on to the Target in Emulator mode using JTAG (ICE1000/ICE2000).
-  Run the ‘Target\\tools\\SeqChartProcess\_<platform>.jar’ once discovery is done and nodes are configured
-  ‘SequenceFile.detailed.png’ is created in ‘Target/examples/demo/<a2b-xx>>’ folder

|image2|

.. container:: centeralign

   \ **Figure: Sample Sequence Chart**\


| 
| ===== Capturing Trace Messages ===== In addition to sequence charts, the Stack also provides mechanisms to emit trace messages. Like sequence charts, trace messages are also sent through the logging subsystem of the PAL. It is important that a unique URI be used for trace messages, so the PAL can distinguish between trace messages and sequence charts. Similarly, if one is running two stack contexts concurrently, insure that each context has a unique URI to keep the trace outputs from mixing together.

Trace support in the Stack
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Trace support is an optional Stack feature. Support for tracing must be enabled by defining A2B_FEATURE_TRACE in ‘features.h’ prior to compiling the Stack.
-  Both the tracing URI as well as the default trace level mask are configured within the Environment Control Block (ECB).
-  For tracing, both traceUrl and traceLvl should be initialized along with the PAL.
-  Trace levels can be changed by the application at any time.

Enabling Trace in Sample Demo Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Enable A2B_FEATURE_TRACE macro in ‘Target\\examples\\demo\\<a2b-xx>\\ a2bstack-pal\\platform\\a2b\\features.h’
-  Optionally, modify the Trace Level in the Application header file

   -  Target\\examples\\demo\\<a2b-xx>\\app\\a2bapp_defs.h

-  Build, load and execute the a2bstack application on Target in Emulator mode using JTAG (ICE1000/ICE2000).
-  Halt the target in CCES after discovery and nodes are configured (after audio is configured)
-  By default, trace messages will be stored in ‘Target/a2bstack/demo/<a2b-xx>/a2b_trace.txt’

Trace Levels Description
^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------+----------------------------------------------------------------------------------------------------------------+
| Trace Levels(Macros) | Description                                                                                                    |
+======================+================================================================================================================+
| A2B_TRC_LVL_DEFAULT  | Log fatal errors and warnings. This is a combination of A2B_TRC_LVL_WARN, A2B_TRC_LVL_ERROR, A2B_TRC_LVL_FATAL |
+----------------------+----------------------------------------------------------------------------------------------------------------+
| A2B_TRC_LVL_INFO     | Log information wrt A2B node properties, slave plugin processing                                               |
+----------------------+----------------------------------------------------------------------------------------------------------------+
| A2B_TRC_LVL_DEBUG    | Log discovery-related messages and interrupts                                                                  |
+----------------------+----------------------------------------------------------------------------------------------------------------+
| A2B_TRC_LVL_TRACE1   | Log typical function In/Out messages                                                                           |
+----------------------+----------------------------------------------------------------------------------------------------------------+
| A2B_TRC_LVL_TRACE2   | Log verbose messages                                                                                           |
+----------------------+----------------------------------------------------------------------------------------------------------------+
| A2B_TRC_LVL_TRACE3   | Log Interrupt Mask for Master Plugin                                                                           |
+----------------------+----------------------------------------------------------------------------------------------------------------+
| A2B_TRC_LVL_ALL      | Log all messages                                                                                               |
+----------------------+----------------------------------------------------------------------------------------------------------------+

Trace Domains Description
^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Trace Domains(Macros) | Description                                                                                                                                                 |
+=======================+=============================================================================================================================================================+
| A2B_TRC_DOM_STACK     | Log messages or events from Stack alone. The messages logged will be for a failure case. Hence A2B_TRC_LVL_DEFAULT should be enabled to log these messages. |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| A2B_TRC_DOM_TICK      | Log information with respect to Stack Tick. Enable A2B_TRC_LVL_TRACE2 to log these messages.                                                                |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| A2B_TRC_DOM_TIMERS    | Log timer related messages. Enable A2B_TRC_LVL_TRACE1 to log the timer functions.                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| A2B_TRC_DOM_MSGRTR    | Log information with respect to message Request and Notifications. Enable A2B_TRC_LVL_TRACE1 to log the events with respect to message transactions.        |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| A2B_TRC_DOM_PLUGIN    | Log messages or events from all Plugins                                                                                                                     |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| A2B_TRC_DOM_I2C       | Log I2C transactions only. Enable A2B_TRC_LVL_TRACE2 to log the I2C transactions.                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| A2B_TRC_DOM_SPI       | Log SPI transactions only. Enable A2B_TRC_LVL_TRACE2 to log the SPI transactions.                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| A2B_TRC_DOM_ALL       | Log messages from all domains                                                                                                                               |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

Stack scalability and optimization options
------------------------------------------

A2B stack is scalable for small micro-controllers to large SoC running complex OS. In this section, we provide options to optimize memory based on a few configurations.

-  In ‘Target\\examples\\demo\\<a2b-xx>\\ a2bstack-pal\\platform\\a2b\\features.h’, undefine the following macro(s):

   -  A2B_FEATURE_COMM_CH
   -  ENABLE_PERI_CONFIG_BCF
   -  A2B_FEATURE_TRACE
   -  A2B_FEATURE_SEQ_CHART

-  In ‘Target/examples/demo/<a2b-xx>>/a2bstack-pal/platform/a2b/conf.h’

   -  Set A2B_CONF_MAX_NUM_MASTER_NODES to 1
   -  Set A2B_CONF_MAX_NUM_SLAVE_NODES to 2

-  Remove Slave plugin usage in a2bapp.c if no slave peripheral configuration is required.

   -  In function a2bapp_pluginsLoad, remove A2B_SLAVE_PLUGIN_INIT(&appPlugins[i]) and set \*numPlugins = 1;

-  Use compressed BCF export.

   -  Ensure ADI_A2B_BCF_COMPRESSED is defined in a2bapp_defs.h

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/environmental_settings.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/sequence_chart.png
