:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

:doc:`Click here to return to the QSG homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide>`

A2B Bus Analyzer Platform
=========================

Drag/Drop the platform listed under A2BBusAnalyzer in the System View Canvas to create A2B Schematics representing A2B Bus Analyzer hardware included in the network. Choose the Analyzer Platform based on the part number you want emulate. and enter the Analyzer Serial number.


|image1|

.. container:: centeralign

   \ **Figure:** A2BBusAnalyzer Platform TreeToolBox


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
========================================

A2B Bus Analyzer Platform can be configured in the modes described in table below

=========== ==============================================
**Mode**    **Description**
=========== ==============================================
Bus Monitor Represents A2B Bus Analyzer Bus Monitor Node
Main Node   Represents A2B Bus Analyzer Main Node Emulator
Sub Node    Represents A2B Bus Analyzer Sub Node Emulator
=========== ==============================================

|image2|

.. container:: centeralign

   \ **Figure:** A2B Bus Analyzer Platform Configurations


Bus Monitor
-----------

Bus Monitor Node can be connected between any 2 nodes of the A2B network and represents the location in the network where the A2B Bus Analyzer hardware is connected for Monitor purpose.

Shown below is an A2B network, where A2B Bus Analyzer is connected for Bus Monitoring between Main and Sub Node 0.


|image3|

.. container:: centeralign

   \ **Figure:** Schematic with A2B Bus Analyzer as Bus Monitor


Sub Node Emulation
------------------

A2B Bus Analyzer Platform can be configured as a Sub Node when the A2B Bus Analyzer hardware must be used for Sub Node Emulation in an A2B network. Shown below is an example A2B network, where the A2B Bus Analyzer is used for Sub Node Emulation of Node 0

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/analyzer_subnode.png
   :align: center

.. container:: centeralign

   \ **Figure:** Schematic with A2B Bus Analyzer as Sub Node Emulator


Sub Node Emulation Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the A2B Bus Analyzer platform is configured as a Sub Node, the Sub Node Transceiver of the platform can be configured from the settings view


|image4|

.. container:: centeralign

   \ **Figure:** A2B Bus Analyzer Sub Node Transceiver Settings


Main Node Emulation
-------------------

A2B Bus Analyzer Platform can be configured as a Main Node when the A2B Bus Analyzer hardware must be used for Main Node Emulation in an A2B network. Shown below is an example schematic with A2B Bus Analyzer connected as Main Node and discovering two Sub Nodes.

.. note::

   PC is connected directly to the A2B Bus Analyzer Main Node and not through USBi.


   |image5|

.. container:: centeralign

   \ **Figure:** Schematic with A2B Bus Analyzer as Main Node Emulator


Main Node Emulation Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the A2B Bus Analyzer platform is configured as a Main Node, the Main Node Transceiver of the platform can be configured from the settings view

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/main_node_settings.png
   :align: center

.. container:: centeralign

   \ **Figure:** A2B Bus Analyzer Main Node Transceiver Settings


Bus Monitoring & Emulation
--------------------------

A2B Bus Analyzer currently supports running Bus Monitoring and Main/Sub Node Emulation simultaneously. A2B Bus Analyzer Platform configured as Main/Sub Node platform and Bus Monitor can be connected in a network chain as shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/analyzer_mainnode_monitor.png
   :align: center

.. container:: centeralign

   \ **Figure:** Schematic with A2B Bus Analyzer as Main Node Emulator & Bus Monitor


   |image6|

.. container:: centeralign

   \ **Figure:** Schematic with A2B Bus Analyzer as Sub Node Emulator & Bus Monitor


High Power Configuration
------------------------

A2B Bus Analyzer platform is configured by default as a Standard Power Main/Sub Node. To Configure Analyzer for High Power Emulation

-  Double Click on the A2B Bus Analyzer Platform or Click on the A2B Bus Analyzer Platform Canvas in the Project window to view the transceiver shape as shown below

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/i2c.png
   :align: center

-  Choose the part number that supports High Power Configuration for High Power Main/Sub Node Emulation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/spi.png
   :align: center

Using A2B Bus Analyzer UI from SigmaStudio+
-------------------------------------------

The A2B Bus Analyzer UI can be launched from SigmaStudio+ when A2B Bus Analyzer Platform is used in an A2B network. Steps to launch A2B Bus Analyzer software and the interactions between SigmaStudio+ and A2B Bus Analyzer software can be found in

-  :doc:`A2B Bus Analyzer QSG </wiki-migration/resources/tools-software/a2b-bus-analyzer/quick-start-guide>`
-  A2B Bus Analyzer User Guide available under Help->User Guide, on launching the A2B Bus Analyzer Software

.. note::

   SigmaStudio+ supports the multi-instance analyzer UI launch, but only one monitor and one emulator will be supported per channel.


-  SS+ can launch multi-instances of A2B Bus Analyzer when they are in separate A2B chains (multi-main setup). In a single channel, it can perform functions as:

   -  Main + Monitor (OR)

      -  Sub + monitor

Steps to use 2 A2B analyzer in a single chain
---------------------------------------------

-  Use a standard ADI evaluation board as a sub-node platform in SS+ (but use A2B Analyzer in your network). Define streams as per your requirement.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/analyzermain_2433sub.png
   :align: center

-  Power-on the sub-node emulator, but don’t launch the UI and connect yet.
-  Link-compile-Download in SS+ à SS+ will now launch main emulator, load .dat file and discover the network.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/mainnodeemulator.png
   :align: center

-  If you get sub-node0 authentication failure, please change the Si revision to 1.0 in the standard platform (sub-node) as shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/si_revision.png
   :align: center

-  Launch another instance of A2B Bus Analyzer UI and connect to sub-node emulator device. Activate the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/subnode_a2ba_ui.png
   :align: center

-  Streams will be available in sub-node as well. You can use the A2B Analyzer GUI to feed in USB audio into sub-node and then receive it on main or vice-versa.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/main_subnode_audio_copy.png
   :align: center

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/a2b_bus_analyzer_platform_tree_toolbox.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/analyzermain_monitor_subnode.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/analyzerasmonitor.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/sub_node_settings.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/analyzer_mainnode.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/analyzer_subnode_monitor.png
