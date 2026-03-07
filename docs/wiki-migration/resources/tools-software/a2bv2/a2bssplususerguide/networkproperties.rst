:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

Network Properties
==================

The Network Properties tab, as shown in figure below, offers configurable options for the target processor software. With these settings one can select the node discovery and initialization method to be used and the clock source for the A2B network.

The four possible discovery methods are

**Simple:** All sub nodes are discovered sequentially from sub 0 to the last available sub node in the system. Once all the sub nodes are discovered, they are initialized for synchronous data exchange.

**Modified:** All sub nodes are discovered and immediately initialized (for synchronous data exchange) sequentially from sub 0 to the last available sub node in the system.(Not supported for AD2437)

**Optimized:** Even before a node is initialized the host tries to discover the next node. The time for the next node to be discovered is used to initialize the current node. Synchronous data can start only after all nodes are discovered and initialized. (Not supported for AD2437)

**Advanced:** Even before a node is initialized the host tries to discover the next node. The time for the next node to be discovered is used to initialize the current node. Synchronous data exchange can start as soon as a main and sub node 0 is initialized (Not supported for AD243x main).

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties.png
   :align: right

.. container:: centeralign

   **Figure:** Network Properties Tab


**Discovery Start Delay (ms):** Delay (in milliseconds) to wait after a software reset and before discovery start.

**Rediscovery wait time (ms):** Delay(in milliseconds) to wait between discovery for systems containing Medium and High-Power Slaves.

The Line Fault settings allow user to enable fault diagnostic feature of the software. With this any line fault encountered in the system is handled and reported to the user.

**Override Bus Self Discovery:** If checked, Bus self-discovery status is ignored, discovery process starts with the soft-reset of A2B network. If unchecked, software looks for a self-discovered network, configures the network as per the schematic.

**Enable Line Fault Diagnostics:** Enables line fault diagnostic feature of software. When set, SigmaStudio+ will continuously monitor the network for faults at 1 second interval. Detected faults will be handled and notified.

| **Rediscovery upon faults:** If checked, automatic network rediscovery or partial discovery will be performed upon detecting post-discovery faults.
| **Partial discovery:**\ If checked, automatic partial re-discovery of dropped nodes are attempted instead of a bus discovery of all nodes.

-  **No. of Attempts:** Specifies the number of partial re-discovery attempts to be tried if the fault persists(-1 for infinite retry).
-  **Discovery Interval(ms):** Delay between each re-discovery attempt in milliseconds.

**Stack Debug Settings:** This feature allows the user to analyze/ understand the system by using the information logged during stack execution. Information can be either through TRACE or sequence chart or both.

-  **Tracing:** Logs key information and network events during the stack execution to a text file. User can configure the required ‘Level’ and ‘Domain’ for tracing.
-  **Sequence Chart:** Sequence Chart captures network transactions in the form of a rich graphical sequence diagram. The sequence chart enables easy understanding of the discovery flow, fault analysis and various other interactions within the system thus enabling quick debugging.

The Refresh |image1| button checks and updates the discovery status of connected A2B Nodes upon a click.

.. note::

   The Network Properties can also be updated using Thrift. For more information you can refer to :doc:`Thrift Document </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/networkproperties>`.


Debug
=====

Trace
-----

The Trace option in the Network properties window show in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>` enables user to log various transactions and network events into a .txt file. Upon enabling this feature the A2B stack running inside SigmaStudio+ captures all transactions as per the ‘Level’ and ‘Domain’ set. :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>` shows a sample Trace file generated for selected Level (Debug, Info, Trace3) and Domain (Plugin, Message, I2C). The Trace file gets saved inside the ‘Settings’ folder corresponding to the A2B schematic project file location.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/sample_trace_file.png
   :align: center

.. container:: centeralign

   \ **Figure:** Sample Trace file


Sequence Chart
--------------

The Sequence Chart option in the Network properties window show in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>` enables user to view various transactions and network events as a rich graphical sequence diagram (.png).

The sequence diagram shows interactions between different stack modules arranged in time sequence and the messages exchanged between the stack modules to discover, configure and handle various network events.

The Sequence Chart file gets saved inside the ‘Settings’ folder corresponding to the A2B schematic project file location.

Following prerequisites shall be ensured to generate the sequence chart upon discovery completion.

**Prerequisites:**

-  Ensure ‘postProcessUML.exe’ and ‘plantuml.jar’ from A2B release package (<<A2B plugin for SigmaStudio+ installation path>>\\\\\\Target\\\\tools) are copied to C:\\ProgramData\\Analog Devices\\A2B-AddOns
-  Set the PATH environment variable for running ‘java.exe’ (Most of the times they are set by default)

   -  C:\\Program Files (x86)\\Java\\jre<<xx>>\\bin

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/environmental_settings.png
   :align: center

.. container:: centeralign

   \ **Figure:** Setting Path in Environment Variables


If the prerequisites are met and sequence chart option is enabled in the Network properties tab, then upon successful discovery of A2B network, the Sequence chart will be generated which can be viewed by clicking on the View button. A Sequence chart generated for a 3 node sample demo schematic is shown in Figure below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/sequence_chart.png
   :align: center

.. container:: centeralign

   **Figure:** Sequence Chart Sample


If the prerequisites are not met, then a pop up window will display the error message as shown in Figure below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/error_message_sequence_chart_prerequisites_not_met.png
   :align: center

.. container:: centeralign

   **Figure:** Error Message – Sequence Chart Prerequisites not met


Network Analysis and Debug
~~~~~~~~~~~~~~~~~~~~~~~~~~

SigmaStudio+ allows user to estimate important network parameters like Bandwidth and power consumption. It also allows user to monitor real-time bit errors in the system using pseudo or actual bit stream. This option can be accessed using the Right-Click menu of the Main Transceiver node as shown in below figure. Note that calculate… option is accessible only if the A2B schematic is ‘Link’ed after the last schematic modification. Save schematic and click on the ‘Link’ icon if the option is disabled.


|image2|

.. container:: Centeralign

   \ **Figure :** Calculation Option


Bandwidth Calculation
=====================

The Bandwidth calculation tab allows user to estimate the total bandwidth used in the A2B network. Bandwidth calculation is useful to design an efficient A2B network.

The following steps are involved in Bandwidth calculation

-  Create an A2B schematic (or open an existing A2B Schematic project) in SigmaStudio+.
-  Navigate to “Bandwidth Calculations” tab under “Networks -> A2B” in “Project window as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`.
-  Enter required details (Cable delay and Sampling Rate parameters) for calculation. Other values required for Bandwidth calculation like Slot format, data width and number of upstream /downstream slots etc. will be picked up from the device properties window settings.
-  Press Run button to get the bandwidth information as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`

|image3|

.. container:: centeralign

   \ **Figure:** Bandwidth Calculation


-  Press Save button to store the results in a text file.
-  Optionally, user can edit Main node response cycles (RESPCYCS) to better utilize the overall bandwidth.
-  Reset button can be pressed to clear the results and rerun the calculation.

Bandwidth Breakdown chart
-------------------------

The “Chart Breakdown” tab allows user to get a breakdown chart, which will have detail of operation of each node.

-  After following :doc:`step1 to step 4 of C.1 Bandwidth Calculation </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`, select “Chart Breakdown” tab to get breakdown chart as shown in :doc:`Figure: Bandwidth breakdown chart. </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/bandwidthbreakdownchart.png
   :align: center

.. container:: centeralign

   \ **Figure:** Bandwidth breakdown chart


Power Calculation
=================

Overall power consumption of the A2B network can be estimated using the Power Calculation tab. Power calculation can assist board designers in estimating power requirements for power supply design.

The following steps are involved in Power calculation

-  Create an A2B schematic (or open an existing A2B Schematic project) in SigmaStudio+.
-  Set power source and cable length in the Node ‘Device Properties’ window as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`

|image4|

.. container:: centeralign

   \ **Figure:** Power Source


-  Navigate to “Power Calculations” tab under “Networks -> A2B” in “Project window as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`.
-  Provide values for power calculation parameters of each A2B node in the system. Select the desired power calculation Mode.
-  Press Run button to get the power consumption information as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`

|image5|

.. container:: centeralign

   \ **Figure:** Power Calculation


-  Press Save button to store the results in a text file.

Power Breakdown chart
---------------------

The “Power Breakdown” tab allows user to get a breakdown chart, which will have detail of power requirement of each node.

-  After following step1 to step 5 of :doc:`C.2 Power Calculation </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`, select “Power Breakdown” tab to get breakdown chart as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/power_breakdown_chart.png
   :align: center

.. container:: centeralign

   \ **Figure:** Power Breakdown chart


Bit Error Rate (BERT) Monitoring
================================

Bit errors generated over an A2B network can be monitored in the GUI. BERT calculation is useful to design an efficient error-free A2B network. BERT is supported both via I2C and SPI interfaces.

The following steps are involved in Bandwidth calculation

-  Create an A2B schematic (or open an existing A2B Schematic project) in SigmaStudio+.
-  Navigate to “BERT” tab under “Networks -> A2B” in “Project window as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`.
-  Select the Bit Stream type to be monitored for errors. Select ‘Pseudo Random’ option to monitor errors on pseudo random bit stream else select ‘Audio’ option to monitor errors on actual audio bit stream.
-  Select required errors to be monitored and make required display settings. Refer to the tool tip for more information by hovering the mouse pointer over the fields.

   -  **Display Update Rate (s)** defines the rate at which error counts are read and updated on the display.
   -  **Graph Display Mode** sets the BERT graph display mode to either Time vs. Bit error count or Time vs. Bit error ratio.

-  Press Run button to get the bit error information as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>`.


|image6|

.. container:: centeralign

   \ **Figure:** BERT Calculation


-  Optionally, Bit errors can be generated from Generate Error Tab.
-  Press Save button to store the results in a text file.
-  Optionally, Reset button can be pressed to clear the results and restart the calculation.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/refresh.png
   :width: 20px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/bndcal.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/bwpage.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/power_source.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/screenshot_2024-10-08_145916.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/bert_calculation.png
