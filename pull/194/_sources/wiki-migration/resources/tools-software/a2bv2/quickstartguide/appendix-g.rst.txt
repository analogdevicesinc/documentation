:doc:`Click here to return to the QSG homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide>`

A2B Bus Analyzer Platform
=========================

.. _a2b-bus-analyzer-platform-1:

A2B Bus Analyzer Platform
-------------------------

Drag/Drop the platform listed under A2BBusAnalyzer in the System View Canvas to create A2B Schematics representing A2B Bus Analyzer hardware included in the network. Choose the Analyzer Platform based on the part number you want emulate. and enter the Analyzer Serial number.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/a2bbusanalyzer_platform_treetoolbox.png
   :align: center
   :width: 600px

**Figure:** A2BBusAnalyzer Platform TreeToolBox

Table below shows the part numbers currently supported for Emulation.

+---------------------------+--------------------+---------------------------+--------------------+
| **A2BBusAnalyzer ->243x** |                    | **A2BBusAnalyzer ->242x** |                    |
+===========================+====================+===========================+====================+
| Main Node Emulation       | Sub Node Emulation | Main Node Emulation       | Sub Node Emulation |
+---------------------------+--------------------+---------------------------+--------------------+
| 0x33                      | 0x33               | 0x28                      | 0x28               |
+---------------------------+--------------------+---------------------------+--------------------+
| 0x35                      | 0x35               | 0x29                      | 0x26               |
+---------------------------+--------------------+---------------------------+--------------------+
| 0x30                      | 0x31               |                           | 0x27               |
+---------------------------+--------------------+---------------------------+--------------------+
| 0x38                      | 0x32               |                           |                    |
+---------------------------+--------------------+---------------------------+--------------------+

A2B Bus Analyzer Platform Configurations
----------------------------------------

A2B Bus Analyzer Platform can be configured in the modes described in table below

=========== ==============================================
**Mode**    **Description**
=========== ==============================================
Bus Monitor Represents A2B Bus Analyzer Bus Monitor Node
Main Node   Represents A2B Bus Analyzer Main Node Emulator
Sub Node    Represents A2B Bus Analyzer Sub Node Emulator
=========== ==============================================

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/analyser_views.png
   :align: center
   :width: 600px

**Figure:** A2B Bus Analyzer Platform Configurations

Bus Monitor
~~~~~~~~~~~

Bus Monitor Node can be connected between any 2 nodes of the A2B network and represents the location in the network where the A2B Bus Analyzer hardware is connected for Monitor purpose.

Shown below is an A2B network, where A2B Bus Analyzer is connected for Bus Monitoring between Main and Sub Node 0.

|image1| **Figure:** Schematic with A2B Bus Analyzer as Bus Monitor

Sub Node Emulation
~~~~~~~~~~~~~~~~~~

A2B Bus Analyzer Platform can be configured as a Sub Node when the A2B Bus Analyzer hardware must be used for Sub Node Emulation in an A2B network. Shown below is an example A2B network, where the A2B Bus Analyzer is used for Sub Node Emulation of Node 0

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/sub_node_emulator.png
   :align: center
   :width: 600px

**Figure:** Schematic with A2B Bus Analyzer as Sub Node Emulator

Sub Node Emulation Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the A2B Bus Analyzer platform is configured as a Sub Node, the Sub Node Transceiver of the platform can be configured from the settings view

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/a2b_bus_analyzer_sub_node_transceiver_settings.png
   :align: center
   :width: 600px

**Figure:** A2B Bus Analyzer Sub Node Transceiver Settings

Main Node Emulation
~~~~~~~~~~~~~~~~~~~

A2B Bus Analyzer Platform can be configured as a Main Node when the A2B Bus Analyzer hardware must be used for Main Node Emulation in an A2B network. Shown below is an example schematic with A2B Bus Analyzer connected as Main Node and discovering two Sub Nodes.

.. note::

   PC is connected directly to the A2B Bus Analyzer Main Node and not through USBi.


|image2| **Figure:** Schematic with A2B Bus Analyzer as Main Node Emulator

Main Node Emulation Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the A2B Bus Analyzer platform is configured as a Main Node, the Main Node Transceiver of the platform can be configured from the settings view

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/a2b_bus_analyzer_main_node_transceiver_settings.png
   :align: center
   :width: 600px

**Figure:** A2B Bus Analyzer Main Node Transceiver Settings

Bus Monitoring & Emulation
~~~~~~~~~~~~~~~~~~~~~~~~~~

A2B Bus Analyzer currently supports running Bus Monitoring and Main/Sub Node Emulation simultaneously. A2B Bus Analyzer Platform configured as Main/Sub Node platform and Bus Monitor can be connected in a network chain as shown below.

|image3| **Figure:** Schematic with A2B Bus Analyzer as Main Node Emulator & Bus Monitor

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/subnode_emulator_and_monitor.png
   :align: center
   :width: 600px

**Figure:** Schematic with A2B Bus Analyzer as Sub Node Emulator & Bus Monitor

High Power Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

A2B Bus Analyzer platform is configured by default as a Standard Power Main/Sub Node. To Configure Analyzer for High Power Emulation

-  Double Click on the A2B Bus Analyzer Platform or Click on the A2B Bus Analyzer Platform Canvas in the Project window to view the transceiver shape as shown below


|image4|

-  Choose the part number that supports High Power Configuration for High Power Main/Sub Node Emulation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/high_power_configuration_1.png
   :align: center
   :width: 300px

Using A2B Bus Analyzer UI from SigmaStudio+
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The A2B Bus Analyzer UI can be launched from SigmaStudio+ when A2B Bus Analyzer Platform is used in an A2B network. Steps to launch A2B Bus Analyzer software and the interactions between SigmaStudio+ and A2B Bus Analyzer software can be found in

-  :doc:`A2B Bus Analyzer QSG </wiki-migration/resources/tools-software/a2b-bus-analyzer/quick-start-guide>`
-  A2B Bus Analyzer User Guide available under Help->User Guide, on launching the A2B Bus Analyzer Software

.. note::

   SigmaStudio+ supports the multi-instance analyzer UI launch, but only one monitor and one emulator will be supported per channel.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/bus_monitor.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/main_node_emulator.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/main_node_emulator_and_bus_monitor.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/high_power_configuration.png
   :width: 300px
