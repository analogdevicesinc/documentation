:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

A2B schematics components
=========================

Components required for drawing A2B schematics in SigmaStudio+ are described here. Make sure that SigmaStudio+ setup is completed as explained in :doc:`A2B Quick Start Guide </wiki-migration/resources/tools-software/a2bv2/quickstartguide>`.

Hardware configuration Tab
--------------------------

AD24xx
~~~~~~

The A2B transceiver chip AD24xx is listed under platforms in the Tree Toolbox of hardware configuration tab. By dragging an AD24xx icon on the Hardware configuration tab schematics for an A2B network can be drawn in the schematic tab. Refer :doc:`A2B Platform </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/navigating-a2b-schematic>` Toolbox for more details.

Communication Channel
~~~~~~~~~~~~~~~~~~~~~

Two host adapter options are available for A2B under Communication Adaptors to interface between SigmaStudio+ and A2B transceiver chip.

-  **A2B-USBi:** Uses Analog Devices USBi I2C host adapter.
-  **A2B-Aardvark:** Uses Aardvark (from Total phase) I2C/SPI host adapter

Drag a communication channel block corresponding to your host adapter and connect to AD24xx block by drawing a wire between the two as shown in :doc:`A2B Platform </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/navigating-a2b-schematic>` Toolbox

.. note::

   A2B-USBi Rev1.4 (or below) SPI interface is not functional for AD243x. Use USBi **Rev1.5** for SPI interface


Schematic Tab
-------------

Target Processor
~~~~~~~~~~~~~~~~

The target processor is the controller that connects to the main A2B node in the bus. The target processor can control any A2B/Peripheral node in the bus through the main A2B node.

In the schematic, the target processor is represented as shown in the below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/schematics-components>`. This is the starting node in an A2B schematic and has one output pin (in brown color) representing I2C or SPI connectivity.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/toolbox.png
   :align: center

.. container:: centeralign

   **Figure :** Target Processor


Target Processor Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users can set the network properties by accessing the “Network properties” window by right clicking the main node, opening the settings. User can also access Network Properties form Project Window. This window offers the network properties. Refer :doc:`Network Properties </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/networkproperties>` for more details.

Transceiver
~~~~~~~~~~~

There are two hierarchies of transceivers AD242x and AD243x. In each hierarchy, there are A2B transceiver node types.

The transceiver nodes are represented as shown :doc:`here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/navigating-a2b-schematic>`. In an A2B schematic, the main transceiver node connects to the PC over the I2C/SPI pin whereas it connects to a sub-node over the network output pin “B”. The sub-node transceiver node takes incoming connection on the network input pin “A” and connects to another sub-node on output pin “B”. A2B Transceiver nodes interface with peripherals via I2C/Tx/Rx pins. Rx pin can be used for either PDM or I2S/TDM reception by clicking on the Rx box.

If the output pin B is left open in a sub-node, then it is the last device of the A2B bus.

AD243x is not pin compatible with AD242x. However, both can be part of same network.

Different variants of transceiver node can be selected using the drop-down box on the node of a custom platform. Depending on the variant selected features/pins become available. Refer A2B Transceiver variant data sheet for more details on the supported features.


|image1|

.. container:: centeralign

   **Figure:** A2B Transceiver nodes in TreeToolBox


Transceiver Node Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^

User can set properties for an A2B transceiver node by accessing the properties window by right-clicking on the Transceiver platform and selecting “Open AD24xx Settings”. This window offers four tabs. The ‘General View’ tab provides functionality-based controls whereas the ‘Register View’ tab provides register fields for configuring the node. ‘Stream View’ provides the stream / tunnel information for the node. ‘Crossbar View’ provides the mapping between A2B slots and TDM Channels.

.. note::

   The register configuration of a node can also be automated using Thrift. For more information, you can refer to the :doc:`Thrift documentation </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/readwriteregister>`.


Node configuration can be done from both General and Register Views tabs of Device properties window. Any change in one tab will be reflected in the other. Refer :doc:`Transceiver settings </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/transceiversetting>` for more details.

AD243x Transceivers
"""""""""""""""""""

Unlike AD242x, Rx and Tx Pins of AD243x are highly flexible and programmable. They are represented as SIO pins. SIO pins can be connected to either Rx or Tx pins of the peripherals. After the connection, one can assign the functionality to various multiplexed pins using the ‘Assign Tab’ of General view as shown below.

Also note that, Main AD243x transceiver can either interface via SPI or I2C.


|image2|

.. container:: centeralign

   **Figure :** Pin Assign Tab


Peripheral device
~~~~~~~~~~~~~~~~~

A **custom platform's** A2B transceiver nodes are able to connect to peripheral devices over the I2C/SPI. Some of the peripherals available on the evaluation boards are SigmaDSP codec, PDM microphones, EEPROM etc.

There are multiple variants of peripheral devices available as shown in the below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/schematics-components>` (Peripheral nodes in TreeToolBox). The Tx slots of the peripherals can be connected to the corresponding Rx slots of the A2B nodes and the Rx slots of the peripherals can be connected to the corresponding Tx slots of the A2B nodes. The Tx pins can be swapped by using the right click option as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/schematics-components>`.


|image3|

.. container:: centeralign

   **Figure:** Swapping Tx Rx pins


   |image4|

.. container:: centeralign

   **Figure:** Peripheral nodes in TreeToolBox


.. note::

   Refer :doc:`Peripheral Properties </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/peripheralproperties>` for further details


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/transceiver_nodes.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/pin_assign_tab.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/swapping_rx_tx_pin.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/peripheral_tree_toolbox.png
