:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

Transceiver Properties
======================

Transceiver settings
--------------------

The transceivers and peripheral settings window can be opened by double clicking on the transceiver/peripheral in the platform view. Additionally, it can also be opened by clicking on the “Settings” option under the transceiver/peripheral in the project window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/a2b_transceivers_and_generic_devices.png
   :align: center
   :width: 600px

.. container:: centeralign

   **Figure:** A2B transceivers and generic devices


General View
~~~~~~~~~~~~

In General View, user can set the constraints using UI without making any changes in the registers. Below is the image to show different tabs in General view.


|image1|

.. container:: centeralign

   **Figure:** General View


Register View
~~~~~~~~~~~~~

In Register View, user can change each register which will also affect in General view. Similar to General View, register view contains many tab for each functionality. User can download or upload the register values directly using this view.


|image2|

.. container:: centeralign

   \ **Figure:** Register View


Stream View
~~~~~~~~~~~

Stream view provides information about number of upstream and downstream slots from each stream. It also in provides details about the slots add and used.


|image3|

.. container:: centeralign

   **Figure:** Node Level Stream View


Crossbar View
~~~~~~~~~~~~~

Crossbar view provides ability for the users to rearrange the slots that are in the TX and RX buffers.


|image4|

.. container:: centeralign

   \ **Figure:** Crossbar View Tab


.. note::

   Refer\ :doc:`Stream and Export Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>` for more information on Stream view


.. note::

   Refer\ :doc:`Crossbar View and Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/transceiversetting>` for more information on Crossbar view


Custom Node Information
=======================

A Custom ID field allows users to provide unique information in hex format to every node which will be a part of only DAT file during export. In the target, stack parses the DAT file and user can retrieve the information from it.


|image5|

.. container:: centeralign

   \ **Figure:** Custom ID Tab


User can use the browse option to locate/create a hex file with the contents. An additional checkbox is added giving a privilege to the user to include or exclude the Custom Node Information contents in DAT file.

.. note::

   The textbox only accepts hex file input.


Custom Node ID based Configuration
==================================

A Custom Node Identifier allows A2B software stack to determine, at run-time, whether the nodes are physically connected in the expected order so that right configuration is applied to the node. This enables system integrators to uniquely identify and authenticate a Node in an A2B network.

.. note::

   We can also perform custom node ID-based configuration using Thrift. For more information, you can refer to the custom node ID-based configuration in the :doc:`Thrift documentation </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/customnodeauthentication>`.


User can set unique ID for a node in an attached I2C enabled Memory device such as an EEPROM attached or by setting unique combination of A2B Transceiver GPIO pin(s) and levels (low/high) or even store in an attached processor memory. The Custom ID information (as set in the hardware) shall be provided in SigmaStudio+ so that it is used for A2B node validation during discovery process.

Custom Node Identifier can be set from the Node’s ‘Device Properties->General View->ID’ tab.

I2C Device
----------

Use the ‘I2C Device’ option as shown in the below Figure when the Custom ID for the node is stored in a Memory device attached to it.

Specify the Custom ID (either as an ASCII string or as a Hexadecimal number) – Max 50 characters, device address, address width and the memory location in the device where the ID is stored.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/customenode_i2c.png
   :align: center

.. container:: centeralign

   \ **Figure:** Custom Node ID using I2C


It is possible to write Custom Node ID into an I2C enabled memory device from SigmaStudio+ using the ‘peripheral properties’ window as shown in Figure. The data in the XML file represents comma separated ASCII values of Custom Node ID.

GPIO Pins
---------

Use ‘GPIO Pins’ option as shown in Figure when A2B Transceiver GPIO pins are used for Custom Node Identification. Specify transceiver GPIO Pins and their level (high/low) to be matched on the actual hardware during A2B discovery process. A GPIO pin not used for Node Identification shall be set to ‘IGNORE’.

As most GPIO pins are multiplexed with other functionality, user shall select pin(s) that are free for Node ID. Note that a GPIO pin will assume a multiplexed functionality only after the A2B Transceiver is discovered and configured. So, with additional on-board circuitry (pull-up/pull-downs) one should be able to use A2B GPIO pins (including multiplexed GPIO) for Custom Node ID. If multiple nodes in a network use GPIO pins for Identification, then each node shall have unique GPIO pin/level settings.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/gpio_pins.png
   :align: center

.. container:: centeralign

   \ **Figure:** Custom Node ID using GPIO pins


Mailbox
-------

Use ‘Mailbox’ option as shown in the below Figure when Custom Node Identifier for the sub-node is to be requested from a connected processor.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/customenode_mailbox.png
   :align: center

.. container:: centeralign

   \ **Figure:** Custom Node ID using A2B mailbox


When a schematic is downloaded with this option set, SigmaStudio+ sends Custom Node Identifier request message to the sub-node over A2B Mailbox, using A2B Stack’s Communication channel module. The sub-node processor, running the Communication channel instance, is expected to handle the request message and respond with its Custom ID as set in SigmaStudio+ before the ‘TimeOut’ period. The ‘TimeOut’ field specifies the time in milliseconds before which the sub-node must respond with its custom Node ID. If the sub-node fails to respond after ‘number of Retries’ or responds with an invalid ID, then SigmaStudio+ aborts discovery and a discovery fail message is provided to the user. For more details on communication channel to be run on sub-node and application integration details to :doc:`refer </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/applicationintegration>`\ in 2.0.x release.

Operability within the A2B Stack
--------------------------------

During A2B discovery process, the Software stack will read the Custom Identifier value from the remote memory device via I2C at the specified address or will read levels on the specified GPIO lines and validate it against the assigned value. In case of mailbox authentication, the Software stack will request for the ID via the communication channel over A2B mailbox. The sub-node controller is expected to the run the communication channel and the sub-node application is required to handle the request message and respond with the custom node ID as set in SigmaStudio+. In all cases if there is a match then the node will be successfully configured otherwise the discovery will be aborted. Additionally, user may register a call back after custom node authentication check, where authentication status can be overridden.

Note that a node may not have a Custom ID set, in which case the stack discovery and initialization process will not perform any Custom ID authentication and hence simply applies the configuration available for that node position

Crossbar View & Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crossbar view is available for all the nodes.

Crossbar view depends on the below configuration:

-  Number of Tx/Rx pins
-  TX Crossbar registers (A2B_TXXBAR0 - A2B_TXXBAR31)
-  RX Crossbar registers (A2B_RXMASK0 - A2B_RXMASK7)
-  TDM Mode Configuration
-  Tx/Rx Interleave Configuration (A2B_I2SCFG. RXPINS & A2B_I2SCFG. TXPINS)

Crossbar View Dependencies Configuration
========================================

Number of Tx/Rx Pins Configuration
----------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/numberof_tx_rx_pins.png
   :align: center

.. container:: centeralign

   \ **Figure:** Number of Tx/Rx Pins Configuration


TX Crossbar registers (A2B_TXXBAR0 - A2B_TXXBAR31)
--------------------------------------------------

.. container:: centeralign

   \ |image6|\


.. container:: centeralign

   \ **Figure:** TX Crossbar registers (A2B_TXXBAR0 - A2B_TXXBAR31)


RX Crossbar registers (A2B_RXMASK0 - A2B_RXMASK7)
-------------------------------------------------

.. container:: centeralign

   \ |image7|\


.. container:: centeralign

   \ **Figure:** RX Crossbar registers (A2B_RXMASK0 - A2B_RXMASK7)


TDM Mode & Tx/Rx Interleave Configuration
-----------------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/tdm_mode.png
   :align: center

.. container:: centeralign

   \ **Figure:** TDM Mode & Tx/Rx Interleave Configuration


Crossbar View with an example
=============================

For example, considering the 3-node schematic with this stream configuration example, crossbar view looks like as mentioned in the snapshots for all the nodes

Sample Stream Definition & Assignment for 3 node schematics
-----------------------------------------------------------

|image8|

.. container:: centeralign

   \ **Figure:** Sample Stream Definition & Assignment for Crossbar view visualization


Crossbar view at subnode0
-------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/crossbar_view_subnode0.png
   :align: center

.. container:: centeralign

   \ **Figure:** Crossbar view at subnode0


Crossbar view at subnode1
-------------------------

.. container:: centeralign

   \ |image9|\


.. container:: centeralign

   \ **Figure:** Crossbar view at subnode1


Crossbar view at Main node with Tx Interleave enabled
-----------------------------------------------------

The similar way Rx Interleave also works.

.. container:: centeralign

   \ |image10|\


.. container:: centeralign

   \ **Figure:** Crossbar view at Main node with Tx & Rx Interleave enabled


Context Menu’s on Crossbar
==========================

Context Menu’s on Tx Crossbar at Main Node side
-----------------------------------------------

Crossbar supports the below options on Tx pin at the main node side as shown in the below snapshot:

-  Reset Channel Map (this option reset’s channel mapping if any mapping is done manually on crossbar)

.. container:: centeralign

   \ |image11|\


.. container:: centeralign

   \ **Figure:** Context Menu's on Tx Pin of Crossbar at Main Node


Context Menu’s on Rx Crossbar
-----------------------------

Crossbar supports the below options on Rx pin as shown in the below snapshot:

-  Enable Mapping (this option can be used to enable a particular slot on the Rx Pin)
-  Clear Mapping (this option clears the mapping of a particular slot on the Rx pin)

.. container:: centeralign

   \ |image12|\


.. container:: centeralign

   \ **Figure:** Context Menu's on Rx Crossbar


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/generalview_mainnodesettings.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/registerview_mainnode.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/streamview_mainnode.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/crossbarview_mainnode.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/customid.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/tx_x-bar.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/ad243x_rx-x_bar.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/sample_stream.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/crossbar_view_subnode1.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/crossbar_view_main_tx_rx.png
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/contextmenu_tx_settings.png
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/contextmenu_rx_settings.png
