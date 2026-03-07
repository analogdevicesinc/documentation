:doc:`Click here to return to the QSG homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide>`

Navigating A2B schematic in SigmaStudio+
========================================

Standard Platforms
------------------

The A2B Plugin for SigmaStudio+ gives the following default platforms for the user:

-  **A2B**

   -  **AD242x:**

      -  EVAL- AD2428WD1BZ: This can be used as both a main and a sub node
      -  EVAL- AD2428WB1BZ: This is a sub node only platform
      -  EVAL- AD2428WC1BZ: This is a sub node only platform

   -  **AD243x:**

      -  EVAL- AD2433WA1BZ: This can be used as both a main and a sub node
      -  EVAL- AD2433WB1BZ: This is a sub node only platform
      -  EVAL- AD2435WA3LZ: This can be used as both a main and a sub node
      -  EVAL- AD2435WJ3LZ: This is a sub node only platform
      -  EVAL- AD2430WD1BZ: This can be used as both a main and a sub node
      -  EVAL- AD2430WC1BZ: This is a sub node only platform
      -  EVAL- AD2430WG1BZ: This is a sub node only platform
      -  EVAL- AD2438WD1BZ: This can be used as main node
      -  EVAL- AD2437A1NZ: This can be used as both a main and a sub node
      -  EVAL- AD2437B1NZ: This is a sub node only platform.
      -  EVAL- AD2437A1MZ: This can be used as both a main and a sub node.
      -  EVAL- AD2437B1MZ: This is a sub node only platform.

-  **A2BBusAnalyzer**

   -  **AD242x:** This can be used for Main/Sub Node Emulation or Bus Monitoring of 242x transceiver variants on the A2B Bus Analyzer Hardware
   -  **AD243x:** This can be used for Main/Sub Node Emulation or Bus Monitoring of 243x transceiver variants on the A2B Bus Analyzer Hardware

   |image1|

.. container:: centeralign

   **Figure:** A2B platforms in toolbox


Transceivers and Peripherals
----------------------------

In addition to these, the plugin also provides a range of transceivers and generic peripheral devices as follows:

-  AD242x, AD243x Main transceiver
-  AD242x, AD243x Subordiante transceiver
-  Generic device: A device that takes an xml file as input for programming via I2C.
-  Non-Programmable generic device: A device that is used for representing not programmable peripherals in A2B system (e.g. Microphone).

These devices are available as part of the toolbox once inside the platform view/canvas as shown in below, the platform canvas can be opened by double clicking on the platform in the system view or by clicking the “Canvas” option under the platform in the Project window.

Custom Platforms
----------------

A2B Platforms different from standard platforms can be created using custom platforms. This is also available as part of tool box.

.. note::

   \ :doc:`How to create loadable custom platforms </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/defineplatforms>`


.. note::

   \ `Refer <https://wiki.analog.com/resources/tools-software/sigmastudiov2/usingsigmastudio/_customvsstandard>`_ Standard vs Custom Platforms


Transceiver settings (General View, Register View, Stream View and Crossbar View)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The transceivers and peripheral settings window can be opened by double clicking on the transceiver/peripheral in the platform view. Additionally, it can also be opened by clicking on the “Settings” option under the transceiver/peripheral in the project window.

.. container:: centeralign

   |image2| **Figure:** A2B transceivers and generic devices

   
   |image3| **Figure:** General View
   
   |image4| **Figure:** Register View
   
   |image5| **Figure:** Node Level Stream View
   
   |image6| **Figure:** Crossbar View Tab


Network Properties
------------------

The Network Properties tab, as shown in :doc:`Figure 61 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-a>`, offers configurable options for the target processor software. With these settings one can select the node discovery and initialization method to be used and the clock source for the A2B network.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/network_settings_tab.png
   :align: center
   :width: 600px

.. container:: centeralign

   **Figure:** Network Properties Tab


The four possible discovery methods are

**Simple:** All sub nodes are discovered sequentially from sub 0 to the last available sub node in the system. Once all the sub nodes are discovered, they are initialized for synchronous data exchange.

**Modified:** All sub nodes are discovered and immediately initialized (for synchronous data exchange) sequentially from sub 0 to the last available sub node in the system.(Not supported for AD2437)

**Optimized:** Even before a node is initialized the host tries to discover the next node. The time for the next node to be discovered is used to initialize the current node. Synchronous data can start only after all nodes are discovered and initialized. (Not supported for AD2437)

**Advanced:** Even before a node is initialized the host tries to discover the next node. The time for the next node to be discovered is used to initialize the current node. Synchronous data exchange can start as soon as a main and sub node 0 is initialized (Not supported for AD243x main).

**Discovery Start Delay (ms):** Delay (in milliseconds) to wait after a software reset and before discovery start.

The Line Fault settings allow user to enable fault diagnostic feature of the software. With this any line fault encountered in the system is handled and reported to the user.

**Override Bus Self Discovery:** If checked, Bus self-discovery status is ignored, discovery process starts with the soft-reset of A2B network. If unchecked, software looks for a self-discovered network, configures the network as per the schematic.

**Enable Line Fault Diagnostics:** Enables line fault diagnostic feature of software. When set, SigmaStudio+ will continuously monitor the network for faults at 1 second interval. Detected faults will be handled and notified.

**Rediscovery upon faults:** If checked, automatic network rediscovery or partial discovery will be performed upon detecting post-discovery faults.

-  **No. of Attempts:** Specifies the number of re-discovery attempts to be tried if the fault persists (-1 for infinite retry).
-  **Discovery Interval (ms):** Delay between each rediscovery attempt in milliseconds.

**Stack Debug Settings:** This feature allows the user to analyze/ understand the system by using the information logged during stack execution. Information can be either through TRACE or sequence chart or both.

-  **Tracing:** Logs key information and network events during the stack execution to a text file. User can configure the required ‘Level’ and ‘Domain’ for tracing.
-  **Sequence Chart:** Sequence Chart captures network transactions in the form of a rich graphical sequence diagram. The sequence chart enables easy understanding of the discovery flow, fault analysis and various other interactions within the system thus enabling quick debugging.

The Refresh |image7| button checks and updates the discovery status of connected A2B Nodes upon a click.

.. note::

   The Network Properties can also be updated using Thrift. For more information you can refer to :doc:`Thrift Document </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/networkproperties>`.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/tree_toolbox_.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/a2b_transceivers_and_generic_devices.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/general_view.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/register_view.png
   :width: 500px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/node_level_stream_view.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/crosbar_view.png
   :width: 500px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/refresh.png
   :width: 20px
