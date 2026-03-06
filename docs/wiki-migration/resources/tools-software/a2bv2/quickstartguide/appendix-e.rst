:doc:`Click here to return to the QSG homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide>`

APPENDIX E: Crossbar View & Configuration
=========================================

Crossbar view is available for all the nodes.

Crossbar view depends on the below configuration:

-  Number of Tx/Rx pins
-  TX Crossbar registers (A2B_TXXBAR0 - A2B_TXXBAR31)
-  RX Crossbar registers (A2B_RXMASK0 - A2B_RXMASK7)
-  TDM Mode Configuration
-  Tx/Rx Interleave Configuration (A2B_I2SCFG. RXPINS & A2B_I2SCFG. TXPINS)

In addition to the above, Crossbar view for main node supports offset on the TX pins which can be configured using the register (A2B_I2STXOFFSET.TXOFFSET).

**Hint :** Tx Offset adjustment is not supported for sub-nodes, only supported on main node

Crossbar View Dependencies Configuration
----------------------------------------

Number of Tx/Rx Pins Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/number_of_tx_rx_pins_configuration.png
   :width: 300px

**Figure 86 :** Number of Tx/Rx Pins Configuration

TX Crossbar registers (A2B_TXXBAR0 - A2B_TXXBAR31)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/tx_crossbar_registers_a2b_txxbar0_-_a2b_txxbar31_.png
   :width: 300px

**Figure 87 :** TX Crossbar registers (A2B_TXXBAR0 - A2B_TXXBAR31)

RX Crossbar registers (A2B_RXMASK0 - A2B_RXMASK7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/rx_crossbar_registers_a2b_rxmask0_-_a2b_rxmask7_.png
   :width: 300px

**Figure 88 :** RX Crossbar registers (A2B_RXMASK0 - A2B_RXMASK7)

TDM Mode & Tx/Rx Interleave Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/tdm_mode_tx_rx_interleave_configuration.png
   :width: 300px

**Figure 89 :** TDM Mode & Tx/Rx Interleave Configuration

Crossbar View
-------------

For example, considering the 3-node schematic with the :doc:`stream configuration example </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-e>`, crossbar view looks like as mentioned in the snapshots for all the nodes

Sample Stream Definition & Assignment for 3 node schematics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/sample_stream_definition_assignment_for_crossbar_view_visualization.png
   :width: 400px

**Figure 90 :** Sample Stream Definition & Assignment for Crossbar view visualization

Crossbar view at Main node with no Tx offset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/crossbar_view_at_main_node.png
   :width: 400px

**Figure 91 :** Crossbar view at Main node

Crossbar view at sub node – 0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/crossbar_view_at_sub_node_0.png
   :width: 400px

**Figure 92 :** Crossbar view at sub node – 0

.. note::

   The channel D0 and D1 received on RX0 pin is “MicIn” stream. Because of the data-tunnel addition, the stream colour is mis-represented in RX0. This is under investigation and will be updated in next release.


Crossbar view at sub node – 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/crossbar_view_at_sub_node_1.png
   :width: 400px

**Figure 93 :** Crossbar view at sub node – 1

Crossbar view at Main node with Tx Offset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The below snapshot is taken with the Tx Offset value “4” on TX 0 pin

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/crossbar_view_at_main_node_with_tx_offset.png
   :width: 300px

**Figure 94 :** Crossbar view at Main node with Tx Offset

Crossbar view at Main node with Tx Interleave enabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The similar way Rx Interleave also works.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/crossbar_view_at_main_node_with_tx_rx_interleave_enabled.png
   :width: 300px

**Figure 95 :** Crossbar view at Main node with Tx & Rx Interleave enabled

Context Menu’s on Crossbar
--------------------------

Context Menu’s on Tx Crossbar at Main Node side
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crossbar supports the below options on Tx pin at the main node side as shown in the below snapshot:

-  Set Offset (this option can be used to set the offset on the desired location of TX pin)
-  Clear Offset (this option clears the existing offset)
-  Reset Channel Map (this option reset’s channel mapping if any mapping is done manually on crossbar)

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/context_menu_s_on_tx_pin_of_crossbar_at_main_node.png
   :width: 300px

**Figure 96 :** Context Menu's on Tx Pin of Crossbar at Main Node

Context Menu’s on Rx Crossbar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crossbar supports the below options on Rx pin as shown in the below snapshot:

-  Enable Mapping (this option can be used to enable a particular slot on the Rx Pin)
-  Clear Mapping (this option clears the mapping of a particular slot on the Rx pin)

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/context_menu_s_on_rx_crossbar.png
   :width: 300px

**Figure 97 :** Context Menu's on Rx Crossbar
