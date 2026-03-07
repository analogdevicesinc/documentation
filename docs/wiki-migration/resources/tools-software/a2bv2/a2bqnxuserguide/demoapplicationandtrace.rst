:doc:`Click here to return to A2B QNX User Guide Homepage. </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide>`

Demo Application and A2B stack features on QNX
==============================================

Demo application a2bapp-qnx and a2b stack in QNX supports several features that can be configured during build time.

Build Time options
------------------

Utilizing a custom schematic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default demo application uses the bus configuration file adi_a2b_busconfig.c to perform bus discovery. This file corresponds to the 3-node sample node schematic in ADI_A2B_Software-QNX RelX.Y.Z/Schematics/QNX/A2BSchematics/adi_a2b_3NodeSampleDemoConfig_AD2428.dspproj. To use a different schematic user must first export the bus configuration C file from Sigma Studio. Refer to :doc:`A2B SigmaStudio User Guide [2 </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide/references>`] for more details on creating and exporting a custom schematic from Sigma Studio. The default adi_a2b_busconfig.c should be replaced with this file in the ADI_A2B_Software-QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/app/ and application must be rebuilt.

Sequence Chart
~~~~~~~~~~~~~~

To enable the sequence chart feature, define the macro A2B_FEATURE_SEQ_CHART in file features.h in ADI_A2B_Software-QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/a2bstack- pal/platform/a2b folder. The sequence chart file can be set with the macro A2B_CONF_DEFAULT_SEQCHART_CHAN_URL in the a2bapp_defs.h file in ADI_A2B_Software-QNX- RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/app/ folder.

Generating UML diagram
~~~~~~~~~~~~~~~~~~~~~~

The sequence chart generated can be visualized as a UML diagram using the plantuml utility. The steps for the same are given below.

-  Generate the sequence chart by running the application specifying the sequence file name as SequenceFile.txt as described in :doc:`Sequence Chart </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide/demoapplicationandtrace>`. The file is created in the same directory from which the application is run on the target.
-  Transfer the file from target to host using the QNX File Transfer launch configuration type by following the steps given below:

   -  Click on New Launch Configuration from the toolbar as shown in Steps of :doc:`Running Sample Demo </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide/a2bdemoonqnx>` Section.

      -  Select Run/Debug as the Initial Launch Mode and click Next
      -  Select QNX File Transfer as the Launch Configuration Type and click Next
      -  Click on Add button in the configuration properties window as shown in below Figure

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/file_transfer_launch_config.png
   :align: center
   :width: 600px

-  Specify the File Transfer settings as shown in below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/file_transfer_settings.png
   :align: center
   :width: 600px

-  Ensure that JAVA Runtime Environment is installed on the host machine.
-  To generate the plantuml diagram run the SeqChartProcess_qnx.bat script from the tools folder. The sequence chart uml diagram namely SequenceFile.detailed.png is created in the ADI_A2B_Software-QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx folder.

Trace file and Level
--------------------

The steps to log trace messages from A2B Stack Software are described below.

-  To enable trace feature, define the macro A2B_FEATURE_TRACE in the file features.h in ADI_A2B_Software-QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/a2bstack- pal/platform/a2b folder. The trace file and trace debug level can be set in the file a2bapp_defs.h with the macros A2B_CONF_DEFAULT_TRACE_CHAN_URL and A2B_CONF_DEFAULT_TRACE_LVL. The a2bapp_defs.h file is present in ADI_A2B_Software-QNXRelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/app/ folder.
-  A2B_CONF_DEFAULT_TRACE_LVL specifies the default level of trace messages to be captured. The levels are defined based on the severity of messages. This also specifies the domains for eg: stack, plugin etc., from which to capture messages. The default value is set to (A2B_TRC_DOM_ALL \| A2B_TRC_LVL_DEBUG \| A2B_TRC_LVL_INFO \| A2B_TRC_LVL_DEFAULT \| A2B_TRC_LVL_ALL). This causes all levels of messages from all domains to be captured. For a description of the different trace domains and levels refer to the A2B Software :doc:`Stack API reference document [3 </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide/references>`].
-  The A2B_CONF_DEFAULT_TRACE_CHAN_URL specifies the channel where the trace output is logged in terms of an URL. By default, it is set to "`file:\\\\a2b_trace.txt <file:\\a2b_trace.txt>`_\ ” which causes the trace messages to be stored in the file a2b_trace.txt in the same folder. Build and run the demo application on the BeagleBone Board as described in :doc:`Running Sample Demo </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide/a2bdemoonqnx>`. The trace file namely " a2b_trace.txt” is created in the folder from where the application is run. Open the file in a text editor to analyze the messages. Note that the next time the application is run old trace messages are removed in the existing file and written with the new messages. To view the trace messages on console where the application is running instead of logging it to a file, the URL should be modified to “stdio:\\\\stdout”.

Line Fault messages
~~~~~~~~~~~~~~~~~~~

The application supports notifying the user of any line faults that occur both during discovery and post discovery. This feature can be enabled in the Target Processor properties in SigmaStudio as shown in below Figure. After enabling this feature the bus config file must be exported to C:/Analog Devices/ADI_A2B_Software-QNX-RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/app/ and application must be rebuilt. Refer to :doc:`A2B SigmaStudio User Guide [2 </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide/references>`] for more details on exporting the bus config file.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/line_fault_settings.png
   :align: center
   :width: 600px

Whenever a line fault occurs a message is printed on the console specifying the fault type and the node at which the fault occurred. The Below Figure shows the output when the “B” side cable is disconnected at Master Node before running the application. As expected discovery fails and error message indicating open or disconnected cable at Master Node is flashed. The Below Figure shows the output when the cable is removed post successful discovery at Slave Node 0.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/line_fault_console_output_cable_issue.png
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/line_fault_console_output.png
   :align: center
   :width: 600px

Rediscovery
~~~~~~~~~~~

The application supports rediscovery of A2B network upon line fault. This feature can be enabled in the Target Processor properties in SigmaStudio as shown in below Figure. After enabling this feature the bus config file must be exported to C:/Analog Devices/ADI_A2B_Software-QNX- RelX.Y.Z/Target/examples/demo/a2b-qnx/a2bapp-qnx/app/ and application must be rebuilt. Refer to :doc:`A2B SigmaStudio User Guide [2 </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide/references>`] for more details on exporting the bus config file.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/rediscovery_settings.png
   :align: center
   :width: 600px

This causes the discovery message to be sent to the stack once again from the application whenever a line fault is detected and the entire discovery of the network to be carried.
