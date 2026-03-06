:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

Network Analysis and Debug
==========================

SigmaStudioPlus allows user to estimate important network parameters like Bandwidth and power consumption. It also allows user to monitor real-time bit errors in the system using pseudo or actual bit stream. This option can be accessed using the Right-Click menu of the Main Transceiver node as shown in below figure. Note that calculate… option is accessible only if the A2B schematic is ‘Link’ed after the last schematic modification. Save schematic and click on the ‘Link’ icon if the option is disabled.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/calculation_option.png
   :align: center
   :width: 400px

**Figure :** Calculation Option

Bandwidth Calculation
---------------------

The Bandwidth calculation tab allows user to estimate the total bandwidth used in the A2B network. Bandwidth calculation is useful to design an efficient A2B network.

The following steps are involved in Bandwidth calculation

-  Create an A2B schematic (or open an existing A2B Schematic project) in SigmaStudio Plus.
-  Navigate to “Bandwidth Calculations” tab under “Networks -> A2B” in “Project window as shown in :doc:`Figure 1 </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>`.
-  Enter required details (Cable delay and Sampling Rate parameters) for calculation. Other values required for Bandwidth calculation like Slot format, data width and number of upstream /downstream slots etc. will be picked up from the device properties window settings.
-  Press Run button to get the bandwidth information as shown in :doc:`Figure 72 </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>`

|image1|

.. container:: centeralign

   \ **Figure 72:** Bandwidth Calculation


-  Press Save button to store the results in a text file.
-  Optionally, user can edit Main node response cycles (RESPCYCS) to better utilize the overall bandwidth.
-  Reset button can be pressed to clear the results and rerun the calculation.

Bandwidth Breakdown chart
~~~~~~~~~~~~~~~~~~~~~~~~~

The “Chart Breakdown” tab allows user to get a breakdown chart, which will have detail of operation of each node.

-  After following :doc:`step1 to step 4 of C.1 Bandwidth Calculation </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>`, select “Chart Breakdown” tab to get breakdown chart as shown in :doc:`Figure 73: Bandwidth breakdown chart. </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/bandwidth_breakdown_chart.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **Figure 73:** Bandwidth breakdown chart


Power Calculation
-----------------

Overall power consumption of the A2B network can be estimated using the Power Calculation tab. Power calculation can assist board designers in estimating power requirements for power supply design.

The following steps are involved in Power calculation

-  Create an A2B schematic (or open an existing A2B Schematic project) in SigmaStudio+.
-  Set power source and cable length in the Node ‘Device Properties’ window as shown in :doc:`Figure 74 </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>`

|image2|

.. container:: centeralign

   \ **Figure 74:** Power Source


-  Navigate to “Power Calculations” tab under “Networks -> A2B” in “Project window as shown in :doc:`Figure 1 </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>`.
-  Provide values for power calculation parameters of each A2B node in the system. Select the desired power calculation Mode.
-  Press Run button to get the power consumption information as shown in :doc:`Figure 75 </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>`

|image3|

.. container:: centeralign

   \ **Figure 75:** Power Calculation


-  Press Save button to store the results in a text file.

Power Breakdown chart
~~~~~~~~~~~~~~~~~~~~~

The “Power Breakdown” tab allows user to get a breakdown chart, which will have detail of power requirement of each node.

-  After following step1 to step 5 of :doc:`C.2 Power Calculation </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>`, select “Power Breakdown” tab to get breakdown chart as shown in :doc:`Figure 76 </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/power_breakdown_chart.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **Figure 76:** Power Breakdown chart


Bit Error Rate (BERT) Monitoring
--------------------------------

Bit errors generated over an A2B network can be monitored in the GUI. BERT calculation is useful to design an efficient error-free A2B network. BERT is supported both via I2C and SPI interfaces.

The following steps are involved in Bandwidth calculation

-  Create an A2B schematic (or open an existing A2B Schematic project) in SigmaStudio.
-  Navigate to “BERT” tab under “Networks -> A2B” in “Project window as shown in :doc:`Figure 1 </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>`.
-  Select the Bit Stream type to be monitored for errors. Select ‘Pseudo Random’ option to monitor errors on pseudo random bit stream else select ‘Audio’ option to monitor errors on actual audio bit stream.
-  Select required errors to be monitored and make required display settings. Refer to the tool tip for more information by hovering the mouse pointer over the fields.

   -  **Display Update Rate (s)** defines the rate at which error counts are read and updated on the display.
   -  **Graph Display Mode** sets the BERT graph display mode to either Time vs. Bit error count or Time vs. Bit error ratio.

-  Press Run button to get the bit error information as shown in :doc:`Figure 77 </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>`.


|image4|

.. container:: centeralign

   \ **Figure 77:** BERT Calculation


-  Optionally, Bit errors can be generated from Generate Error Tab.
-  Press Save button to store the results in a text file.
-  Optionally, Reset button can be pressed to clear the results and restart the calculation.

Debug
-----

Trace
~~~~~

The Trace option in the Network properties window show in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/navigating-a2b-schematic>` enables user to log various transactions and network events into a .txt file. Upon enabling this feature the A2B stack running inside SigmaStudio Plus captures all transactions as per the ‘Level’ and ‘Domain’ set. :doc:`Figure 78 </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkanalysisanddebug>` shows a sample Trace file generated for selected Level (Debug, Info, Trace3) and Domain (Plugin, Message, I2C). The Trace file gets saved inside the ‘Settings’ folder corresponding to the A2B schematic project file location.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/sample_trace_file.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **Figure 78:** Sample Trace file


Sequence Chart
~~~~~~~~~~~~~~

The Sequence Chart option in the Network properties window show in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/navigating-a2b-schematic>` enables user to view various transactions and network events as a rich graphical sequence diagram (.png).

The sequence diagram shows interactions between different stack modules arranged in time sequence and the messages exchanged between the stack modules to discover, configure and handle various network events.

The Sequence Chart file gets saved inside the ‘Settings’ folder corresponding to the A2B schematic project file location.

Following prerequisites shall be ensured to generate the sequence chart upon discovery completion.

**Prerequisites:**

-  Ensure ‘postProcessUML.exe’ and ‘plantuml.jar’ from A2B release package (<<A2B plugin for SigmaStudio+ installation path>>\\\\\\Target\\\\tools) are copied to C:\\ProgramData\\Analog Devices\\A2B-AddOns
-  Set the PATH environment variable for running ‘java.exe’ (Most of the times they are set by default)

   -  C:\\Program Files (x86)\\Java\\jre<<xx>>\\bin

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/setting_path_in_environment_variables.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **Figure 79:** Setting Path in Environment Variables


If the prerequisites are met and sequence chart option is enabled in the Network properties tab, then upon successful discovery of A2B network, the Sequence chart will be generated which can be viewed by clicking on the View button. A Sequence chart generated for a 3 node sample demo schematic is shown in Figure 80.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/sequence_chart_sample.png
   :align: center
   :width: 600px

.. container:: centeralign

   **Figure 80:** Sequence Chart Sample


If the prerequisites are not met, then a pop up window will display the error message as shown in Figure 81.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/error_message_sequence_chart_prerequisites_not_met.png
   :align: center
   :width: 600px

.. container:: centeralign

   **Figure 81:** Error Message – Sequence Chart Prerequisites not met


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/bwpage.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/power_source.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/power_calculation.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/bert_calculation.png
   :width: 600px
